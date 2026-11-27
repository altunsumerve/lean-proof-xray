// Koni / Cone — resmi lean4export kaydından TAM bağımlılık grafiğini çıkarır (tek geçiş, akıtarak).
// TR: Her bildirim için iki kenar kümesi yazar: önermesinin (tip) kullandığı bildirimler ve
//     gövdesinin/ispatının (değer) ayrıca kullandığı bildirimler. Ayrıca her bildirimin kayda eklediği
//     yeni ifade sayısını (ağırlık) ve tip/değer ifade boyutunu verir. Hiçbir şey tahmin edilmez:
//     kenarlar Lean'in kendi kaydındaki `const` ve `proj` düğümlerinden okunur.
// EN: Extracts the FULL dependency graph from an official lean4export NDJSON stream in one pass.
//     For every declaration: constants used by its type, and constants additionally used by its
//     value/proof; plus the number of new expressions it added to the export (weight).
// Kullanım / usage:  koni gecici.bin cikti_klasoru < kayit.ndjson
//   çıktı: cikti/dugum.tsv  (sıra, tür, ad, yeni_ifade, tip_boyu, deger_boyu)
//          cikti/kenar.bin  (uint64 N; her bildirim için uint32 nt, nv, nt+nv bildirim sırası)
#include <cstdio>
#include <cstdint>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <sys/mman.h>
#include <fcntl.h>
#include <unistd.h>
using namespace std;
static const uint32_t LEAF = 0xFFFFFFFEu, CONST = 0xFFFFFFFFu, NAMEF = 0x80000000u;
static const uint32_t ESIK = 96;  // bundan büyük paylaşılan alt ifadelerin sabit kümesi saklanır
static long gi(const char* s, const char* k) { const char* p = strstr(s, k); if (!p) return -1; return strtol(p + strlen(k), nullptr, 10); }

// --- küçük JSON tarayıcı (parmakizi.cpp ile aynı) ---
struct KV { string k; const char* v; const char* e; };
static const char* skipv(const char* p) {
  int d = 0; bool str = false;
  for (; *p; p++) {
    if (str) { if (*p == '\\') { p++; continue; } if (*p == '"') str = false; continue; }
    if (*p == '"') { str = true; continue; }
    if (*p == '{' || *p == '[') d++;
    else if (*p == '}' || *p == ']') { if (d == 0) return p; d--; }
    else if (*p == ',' && d == 0) return p;
  }
  return p;
}
static vector<KV> obj(const char* p) {
  vector<KV> r; if (*p != '{') return r; p++;
  while (*p && *p != '}') {
    while (*p == ' ' || *p == ',') p++;
    if (*p != '"') break;
    const char* a = ++p; while (*p != '"') p++; string k(a, p - a); p++;
    while (*p == ':' || *p == ' ') p++;
    const char* v = p; const char* e = skipv(p);
    r.push_back({k, v, e}); p = e;
  }
  return r;
}
static vector<long> nums(const char* v, const char* e) { vector<long> r; for (const char* p = v; p < e; p++) if ((*p >= '0' && *p <= '9') && (p == v || !(p[-1] >= '0' && p[-1] <= '9'))) r.push_back(strtol(p, nullptr, 10)); return r; }

// --- durum ---
static uint32_t* E; static uint64_t ne = 0;
static unordered_map<uint32_t, uint32_t> ucuncu;                 // letE gövdesi
static vector<uint64_t> notBit;                                   // ifade -> saklı küme var mı
struct Not { uint32_t say; vector<uint32_t> ad; };
static unordered_map<uint32_t, Not> notlar;
static inline bool notVar(uint32_t e) { return (notBit[e >> 6] >> (e & 63)) & 1ULL; }
static void notYaz(uint32_t e, uint32_t say, const vector<uint32_t>& ad) { if (notVar(e)) return; notBit[e >> 6] |= 1ULL << (e & 63); notlar[e] = {say, ad}; }
static uint64_t gezilen = 0;

static inline void cocuklar(uint32_t e, vector<uint32_t>& yigin, vector<uint32_t>& ad) {
  uint32_t a = E[2 * (uint64_t)e], b = E[2 * (uint64_t)e + 1];
  if (a == CONST) { ad.push_back(b); return; }
  if (a != LEAF) yigin.push_back(a);
  if (b != LEAF) { if (b & NAMEF) ad.push_back(b & ~NAMEF); else yigin.push_back(b); }
  if (!ucuncu.empty()) { auto it = ucuncu.find(e); if (it != ucuncu.end()) yigin.push_back(it->second); }
}
static void tekil(vector<uint32_t>& v) { sort(v.begin(), v.end()); v.erase(unique(v.begin(), v.end()), v.end()); }

// Düz küme: açık adresleme + dönem damgası; temizlemek O(1) (std::unordered_set'in clear()'i kova sayısıyla orantılı).
struct Kume {
  vector<uint32_t> anahtar, damga; uint32_t donem = 1; size_t dolu = 0, maske = 0;
  Kume() { anahtar.assign(1024, 0); damga.assign(1024, 0); maske = 1023; }
  void temizle() { if (++donem == 0) { fill(damga.begin(), damga.end(), 0); donem = 1; } dolu = 0;
    if (anahtar.size() > (1u << 22)) { anahtar.assign(1024, 0); damga.assign(1024, 0); maske = 1023; } }
  void buyut() { vector<uint32_t> a(anahtar.size() * 2, 0), d(anahtar.size() * 2, 0); size_t m = a.size() - 1;
    for (size_t i = 0; i < anahtar.size(); i++) if (damga[i] == donem) { size_t h = (anahtar[i] * 2654435761u) & m; while (d[h] == donem) h = (h + 1) & m; a[h] = anahtar[i]; d[h] = donem; }
    anahtar.swap(a); damga.swap(d); maske = m; }
  bool ekle(uint32_t x) {  // yeni eklendiyse true
    size_t h = (x * 2654435761u) & maske;
    while (damga[h] == donem) { if (anahtar[h] == x) return false; h = (h + 1) & maske; }
    anahtar[h] = x; damga[h] = donem; if (++dolu * 2 > anahtar.size()) buyut(); return true; }
};
// eski (önceki bildirimlerden kalan) bir alt ifadenin sabit kümesi
static Kume g2; static vector<uint32_t> y2;
static void altTopla(uint32_t kok, vector<uint32_t>& ad, uint64_t& say) {
  g2.temizle();
  y2.clear(); y2.push_back(kok); vector<uint32_t> a2; uint64_t s2 = 0;
  while (!y2.empty()) {
    uint32_t e = y2.back(); y2.pop_back();
    if (!g2.ekle(e)) continue;
    if (notVar(e)) { const Not& n = notlar[e]; a2.insert(a2.end(), n.ad.begin(), n.ad.end()); s2 += n.say; continue; }
    s2++; gezilen++; cocuklar(e, y2, a2);
  }
  tekil(a2);
  if (s2 > ESIK) notYaz(kok, (uint32_t)min<uint64_t>(s2, 0xFFFFFFFFu), a2);
  ad.insert(ad.end(), a2.begin(), a2.end()); say += s2;
}
// bir kökten (tip ya da değer) ulaşılan sabitler; taban: bu bildirimin eklediği ilk ifade
static vector<uint64_t> yeniBit; static Kume eski; static vector<uint32_t> y1;
static void topla(long kok, uint64_t taban, vector<uint32_t>& ad, uint64_t& say) {
  ad.clear(); say = 0; if (kok < 0 || (uint64_t)kok >= ne) return;
  yeniBit.assign((ne - taban + 63) / 64 + 1, 0); y1.clear(); y1.push_back((uint32_t)kok);
  eski.temizle();
  while (!y1.empty()) {
    uint32_t e = y1.back(); y1.pop_back();
    if (e >= taban) {
      uint64_t i = e - taban; if ((yeniBit[i >> 6] >> (i & 63)) & 1ULL) continue; yeniBit[i >> 6] |= 1ULL << (i & 63);
      if (notVar(e)) { const Not& n = notlar[e]; ad.insert(ad.end(), n.ad.begin(), n.ad.end()); say += n.say; continue; }
      say++; gezilen++; cocuklar(e, y1, ad);
    } else {
      if (!eski.ekle(e)) continue;
      if (notVar(e)) { const Not& n = notlar[e]; ad.insert(ad.end(), n.ad.begin(), n.ad.end()); say += n.say; }
      else altTopla(e, ad, say);
    }
  }
  tekil(ad);
  if (say > ESIK) notYaz((uint32_t)kok, (uint32_t)min<uint64_t>(say, 0xFFFFFFFFu), ad);
}

struct Dugum { uint32_t ad; char tur; uint32_t yeni; uint32_t tipBoy, degerBoy; uint64_t k0; uint32_t nt, nv; };

int main(int argc, char** argv) {
  if (argc < 3) { fprintf(stderr, "kullanim: koni gecici.bin cikti_klasoru < kayit.ndjson\n"); return 1; }
  uint64_t CAP = getenv("KUNYE_KAPASITE") ? strtoull(getenv("KUNYE_KAPASITE"), nullptr, 10) : 2100000000ULL;
  int fd = open(argv[1], O_RDWR | O_CREAT | O_TRUNC, 0644); if (fd < 0 || ftruncate(fd, CAP * 8)) { perror("gecici"); return 1; }
  E = (uint32_t*)mmap(nullptr, CAP * 8, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
  if (E == MAP_FAILED) { perror("mmap"); return 1; }
  notBit.assign(CAP / 64 + 1, 0);
  vector<uint32_t> npre{0}; vector<uint64_t> noff{0}; string nbuf;
  vector<Dugum> D; vector<uint32_t> K;  // K: kenarlar (ad kimliği olarak)
  uint64_t taban = 0; time_t t0 = time(nullptr); uint64_t sonRapor = 0;
  char* buf = nullptr; size_t cap = 0; ssize_t n;
  vector<uint32_t> at, av, fark; uint64_t st, sv;

  auto ekle = [&](long nm, char tur, long tip, const vector<long>& degerler, const vector<long>& ekAd) {
    if (nm < 0) return;
    Dugum d; d.ad = (uint32_t)nm; d.tur = tur; d.yeni = (uint32_t)min<uint64_t>(ne - taban, 0xFFFFFFFFu);
    topla(tip, taban, at, st);
    av.clear(); sv = 0;
    for (long v : degerler) { vector<uint32_t> a; uint64_t s; topla(v, taban, a, s); av.insert(av.end(), a.begin(), a.end()); sv += s; }
    for (long x : ekAd) av.push_back((uint32_t)x);
    tekil(av); fark.clear();
    set_difference(av.begin(), av.end(), at.begin(), at.end(), back_inserter(fark));
    d.tipBoy = (uint32_t)min<uint64_t>(st, 0xFFFFFFFFu); d.degerBoy = (uint32_t)min<uint64_t>(sv, 0xFFFFFFFFu);
    d.k0 = K.size(); d.nt = at.size(); d.nv = fark.size();
    K.insert(K.end(), at.begin(), at.end()); K.insert(K.end(), fark.begin(), fark.end());
    D.push_back(d);
  };

  while ((n = getline(&buf, &cap, stdin)) > 0) {
    const char* s = buf;
    if (s[2] == 'i' && s[3] == 'n' && s[4] == '"') {
      long pre = gi(s, "\"pre\":"); const char* q = strstr(s, "\"str\":\""); string nm;
      if (q) { q += 7; const char* e = strchr(q, '"'); nm.assign(q, e - q); } else nm = "#" + to_string(gi(s, "\"i\":"));
      npre.push_back((uint32_t)pre); nbuf += nm; noff.push_back(nbuf.size()); continue;
    }
    if (s[2] == 'i' && s[3] == 'l' && s[4] == '"') continue;
    const char* ie = strstr(s, "\"ie\":");
    if (ie && strncmp(s, "{\"inductive\"", 12)) {
      uint32_t a = LEAF, b = LEAF; long id = strtol(ie + 5, nullptr, 10);
      if (id < 0 || (uint64_t)id >= CAP) { fprintf(stderr, "ifade kimligi sinir disi %ld\n", id); return 2; }
      if (strstr(s, "\"app\":{")) { a = gi(s, "\"fn\":"); b = gi(s, "\"arg\":"); }
      else if (strstr(s, "\"lam\":{") || strstr(s, "\"forallE\":{")) { a = gi(s, "\"type\":"); b = gi(s, "\"body\":"); }
      else if (strstr(s, "\"const\":{")) { a = CONST; b = gi(s, "\"name\":"); }
      else if (strstr(s, "\"letE\":{")) { a = gi(s, "\"type\":"); b = gi(s, "\"value\":"); ucuncu[(uint32_t)id] = gi(s, "\"body\":"); }
      else if (strstr(s, "\"proj\":{")) { a = gi(s, "\"struct\":"); b = NAMEF | (uint32_t)gi(s, "\"typeName\":"); }
      else if (strstr(s, "\"mdata\":{")) { a = gi(s, "\"expr\":"); }
      E[2 * (uint64_t)id] = a; E[2 * (uint64_t)id + 1] = b; if ((uint64_t)id + 1 > ne) ne = id + 1;
      if (ne - sonRapor >= 20000000ULL) { sonRapor = ne; fprintf(stderr, "ifade %lu bildirim %zu kenar %zu not %zu gezilen %lu sure %lds\n", ne, D.size(), K.size(), notlar.size(), gezilen, (long)(time(nullptr) - t0)); }
      continue;
    }
    if (!strncmp(s, "{\"meta\"", 7)) continue;
    auto top = obj(s); if (top.empty()) continue;
    const string tur = top[0].k; auto o = obj(top[0].v);
    if (tur == "inductive") {
      for (auto& x : o) if (x.k == "types" || x.k == "ctors" || x.k == "recs") {
        const char* p = x.v + 1;
        while (p < x.e && *p == '{') {
          auto d = obj(p); const char* q = skipv(p);
          long nm = -1, ty = -1; vector<long> deg, ek;
          for (auto& y : d) { if (y.k == "name") nm = strtol(y.v, nullptr, 10); else if (y.k == "type") ty = strtol(y.v, nullptr, 10);
            else if (y.k == "ctors" && x.k == "types") ek = nums(y.v, y.e);
            else if (y.k == "rules") { for (const char* r = y.v; r < y.e && (r = strstr(r, "\"rhs\":")) && r < y.e; r += 6) deg.push_back(strtol(r + 6, nullptr, 10)); } }
          ekle(nm, x.k == "types" ? 'i' : x.k == "ctors" ? 'c' : 'r', ty, deg, ek);
          taban = ne;  // ağırlık ilk öğeye yazılır
          p = q; while (p < x.e && (*p == ',' || *p == ' ' || *p == '}')) p++;
        }
      }
    } else if (tur == "thm" || tur == "def" || tur == "opaque" || tur == "axiom") {
      long nm = -1, ty = -1, va = -1;
      for (auto& y : o) { if (y.k == "name") nm = strtol(y.v, nullptr, 10); else if (y.k == "type") ty = strtol(y.v, nullptr, 10); else if (y.k == "value") va = strtol(y.v, nullptr, 10); }
      vector<long> deg; if (va >= 0) deg.push_back(va);
      ekle(nm, tur[0], ty, deg, {});
    }
    taban = ne;
  }
  size_t NN = npre.size();
  fprintf(stderr, "bitti: ifade %lu isim %zu bildirim %zu kenar %zu not %zu gezilen %lu sure %lds\n", ne, NN, D.size(), K.size(), notlar.size(), gezilen, (long)(time(nullptr) - t0));
  auto full = [&](uint32_t x) { string r; while (x && x < NN) { string part = nbuf.substr(noff[x - 1], noff[x] - noff[x - 1]); r = r.empty() ? part : part + "." + r; x = npre[x]; } return r; };
  vector<int32_t> declOf(NN, -1);
  for (size_t i = 0; i < D.size(); i++) if (D[i].ad < NN && declOf[D[i].ad] < 0) declOf[D[i].ad] = (int32_t)i;
  string kl = argv[2];
  FILE* f = fopen((kl + "/dugum.tsv").c_str(), "w"); if (!f) { perror("dugum"); return 1; }
  for (size_t i = 0; i < D.size(); i++) fprintf(f, "%zu\t%c\t%s\t%u\t%u\t%u\n", i, D[i].tur, full(D[i].ad).c_str(), D[i].yeni, D[i].tipBoy, D[i].degerBoy);
  fclose(f);
  f = fopen((kl + "/kenar.bin").c_str(), "wb"); uint64_t N = D.size(); fwrite(&N, 8, 1, f);
  uint64_t cozulmeyen = 0; vector<uint32_t> t, v;
  for (size_t i = 0; i < D.size(); i++) {
    t.clear(); v.clear();
    for (uint32_t j = 0; j < D[i].nt + D[i].nv; j++) {
      uint32_t x = K[D[i].k0 + j]; int32_t y = x < NN ? declOf[x] : -1;
      if (y < 0) { cozulmeyen++; continue; }
      if ((size_t)y == i) continue;
      (j < D[i].nt ? t : v).push_back((uint32_t)y);
    }
    uint32_t h[2] = {(uint32_t)t.size(), (uint32_t)v.size()}; fwrite(h, 4, 2, f);
    if (!t.empty()) fwrite(t.data(), 4, t.size(), f);
    if (!v.empty()) fwrite(v.data(), 4, v.size(), f);
  }
  fclose(f);
  fprintf(stderr, "yazildi; cozulmeyen ad %lu\n", cozulmeyen);
  return 0;
}

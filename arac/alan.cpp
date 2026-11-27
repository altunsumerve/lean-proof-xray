// Alan / Field — her büyük adımın altında hangi kütüphane kavramları kullanılıyor, adımı doğrudan ne kuruyor?
// TR: Girdi: grafik (dugum.tsv, kenar.bin), baskınlık ağacı (taslar.tsv), kütüphane adları, hedef adları, önerme adları.
//     Çıktı (cikti klasörü):
//       alan.tsv      hedef, kütüphane sabiti, kullanım sayısı (hedefin alt ağacındaki proje bildirimlerinden gelen kenar)
//       adalani.tsv   hedef, ad alanı (adın ilk bileşeni), alt ağaçtaki kullanım, bütün projedeki kullanım
//       genel.tsv     kütüphane sabiti, bütün projede kullanım sayısı
//       dogrudan.tsv  hedef, t|d (önermede | ispatta), doğrudan kullanılan proje bildirimi, türü
//       kanitlayan.tsv önerme adı, önermesi tam olarak o ad olan teorem, baskını
//     Yalnızca sayma yapar; yorum içermez.
// EN: Library-concept usage counts per dominator subtree, direct dependencies of each target, and which theorems
//     prove a given named proposition. Counting only.
// Kullanım / usage: alan dugum.tsv kenar.bin taslar.tsv kutuphane.txt hedefler.txt onermeler.txt|- cikti [ust=200]
#include <cstdio>
#include <cstdint>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

static vector<string> satirlar(const char* yol) {
  vector<string> L; FILE* f = fopen(yol, "r"); if (!f) return L;
  char* b = nullptr; size_t c = 0; ssize_t n;
  while ((n = getline(&b, &c, f)) > 0) { while (n > 0 && (b[n - 1] == '\n' || b[n - 1] == '\r')) b[--n] = 0; if (n) L.push_back(b); }
  fclose(f); return L;
}

int main(int argc, char** argv) {
  if (argc < 8) { fprintf(stderr, "kullanim: alan dugum.tsv kenar.bin taslar.tsv kutuphane.txt hedefler.txt onermeler.txt|- cikti [ust]\n"); return 1; }
  size_t ust = argc > 8 ? strtoul(argv[8], nullptr, 10) : 200;
  vector<string> ad; vector<char> tur; vector<uint32_t> tipBoy;
  { FILE* f = fopen(argv[1], "r"); if (!f) { perror("dugum"); return 1; }
    char* b = nullptr; size_t c = 0; ssize_t n;
    while ((n = getline(&b, &c, f)) > 0) {
      char* p = b; strsep(&p, "\t"); char* t = strsep(&p, "\t"); char* a = strsep(&p, "\t");
      strsep(&p, "\t"); char* tb = strsep(&p, "\t"); char* db = strsep(&p, "\t\n");
      if (!db) continue;
      tur.push_back(t[0]); ad.push_back(a); tipBoy.push_back(strtoul(tb, nullptr, 10));
    }
    fclose(f); }
  uint64_t N = ad.size();
  vector<uint64_t> o(N + 2, 0), ot(N + 1, 0); vector<uint32_t> K;
  { FILE* f = fopen(argv[2], "rb"); if (!f) { perror("kenar"); return 1; }
    uint64_t n2; if (fread(&n2, 8, 1, f) != 1 || n2 != N) { fprintf(stderr, "dugum/kenar sayisi uyusmuyor\n"); return 1; }
    for (uint64_t i = 0; i < N; i++) {
      uint32_t h[2]; if (fread(h, 4, 2, f) != 2) { fprintf(stderr, "kenar kisa\n"); return 1; }
      o[i] = K.size(); ot[i] = o[i] + h[0]; K.resize(K.size() + h[0] + h[1]);
      if (h[0] + h[1] && fread(&K[o[i]], 4, h[0] + h[1], f) != h[0] + h[1]) { fprintf(stderr, "kenar kisa\n"); return 1; }
    }
    o[N] = K.size(); fclose(f); }
  unordered_map<string, uint32_t> sira; sira.reserve(N * 2);
  for (uint64_t i = 0; i < N; i++) sira.emplace(ad[i], (uint32_t)i);
  vector<char> kut(N, 0);
  for (auto& s : satirlar(argv[4])) { auto it = sira.find(s); if (it != sira.end()) kut[it->second] = 1; }
  // baskınlık ağacı: taslar.tsv (ad, tur, baskin, ...)
  const uint32_t YOK = 0xffffffffu;
  vector<uint32_t> baskin(N, YOK); vector<vector<uint32_t>> cocuk(N);
  { FILE* f = fopen(argv[3], "r"); if (!f) { perror("taslar"); return 1; }
    char* b = nullptr; size_t c = 0; ssize_t n; bool ilk = true;
    while ((n = getline(&b, &c, f)) > 0) {
      if (ilk) { ilk = false; continue; }
      char* p = b; char* a = strsep(&p, "\t"); strsep(&p, "\t"); char* bs = strsep(&p, "\t\n");
      if (!bs) continue;
      auto ia = sira.find(a), ib = sira.find(bs);
      if (ia == sira.end() || ib == sira.end()) continue;
      baskin[ia->second] = ib->second; cocuk[ib->second].push_back(ia->second);
    }
    fclose(f); }
  string kl = argv[7];
  // ad alanı (adın ilk bileşeni) numaraları
  unordered_map<string, uint32_t> alanNo; vector<string> alanAd; vector<uint32_t> alanI(N, 0);
  for (uint64_t i = 0; i < N; i++) if (kut[i]) {
    string a = ad[i].substr(0, ad[i].find('.'));
    auto it = alanNo.find(a); if (it == alanNo.end()) { it = alanNo.emplace(a, (uint32_t)alanAd.size()).first; alanAd.push_back(a); }
    alanI[i] = it->second;
  }
  vector<uint64_t> alanGenel(alanAd.size(), 0), alanAlt(alanAd.size(), 0);
  // genel sayım
  vector<uint32_t> say(N, 0);
  for (uint64_t u = 0; u < N; u++) if (!kut[u]) for (uint64_t k = o[u]; k < o[u + 1]; k++) if (kut[K[k]]) { say[K[k]]++; alanGenel[alanI[K[k]]]++; }
  { FILE* f = fopen((kl + "/genel.tsv").c_str(), "w");
    vector<uint32_t> s; for (uint32_t i = 0; i < N; i++) if (say[i]) s.push_back(i);
    sort(s.begin(), s.end(), [&](uint32_t a, uint32_t b) { return say[a] != say[b] ? say[a] > say[b] : ad[a] < ad[b]; });
    for (uint32_t i : s) fprintf(f, "%s\t%u\n", ad[i].c_str(), say[i]);
    fclose(f); }
  // hedefler
  FILE* fn = fopen((kl + "/adalani.tsv").c_str(), "w");
  { uint64_t t = 0; for (auto x : alanGenel) t += x; fprintf(fn, "<hepsi>\t<toplam>\t%lu\t%lu\n", (unsigned long)t, (unsigned long)t);
    for (size_t i = 0; i < alanAd.size(); i++) if (alanGenel[i]) fprintf(fn, "<hepsi>\t%s\t%lu\t%lu\n", alanAd[i].c_str(), (unsigned long)alanGenel[i], (unsigned long)alanGenel[i]); }
  FILE* fa = fopen((kl + "/alan.tsv").c_str(), "w"); FILE* fd = fopen((kl + "/dogrudan.tsv").c_str(), "w");
  vector<uint32_t> c2(N, 0), yigin, dokunulan;
  for (auto& h : satirlar(argv[5])) {
    auto it = sira.find(h); if (it == sira.end()) continue;
    uint32_t kok = it->second;
    for (uint64_t k = o[kok]; k < o[kok + 1]; k++) if (!kut[K[k]])
      fprintf(fd, "%s\t%c\t%s\t%c\n", h.c_str(), k < ot[kok] ? 't' : 'd', ad[K[k]].c_str(), tur[K[k]]);
    yigin.assign(1, kok); dokunulan.clear(); uint64_t dugum = 0, kenar = 0;
    while (!yigin.empty()) {
      uint32_t u = yigin.back(); yigin.pop_back(); dugum++;
      for (uint64_t k = o[u]; k < o[u + 1]; k++) { uint32_t d = K[k]; if (kut[d]) { if (!c2[d]++) dokunulan.push_back(d); kenar++; } }
      for (uint32_t v : cocuk[u]) yigin.push_back(v);
    }
    sort(dokunulan.begin(), dokunulan.end(), [&](uint32_t a, uint32_t b) { return c2[a] != c2[b] ? c2[a] > c2[b] : ad[a] < ad[b]; });
    fprintf(fa, "%s\t<toplam>\t%lu\t%lu\t%zu\n", h.c_str(), (unsigned long)kenar, (unsigned long)dugum, dokunulan.size());
    // en çok kullanılanlar ve genel paya göre en ayırt ediciler (oran = alt ağaçtaki sayı / genel sayı)
    for (size_t i = 0; i < dokunulan.size() && i < ust; i++) fprintf(fa, "%s\t%s\t%u\t%u\n", h.c_str(), ad[dokunulan[i]].c_str(), c2[dokunulan[i]], say[dokunulan[i]]);
    vector<uint32_t> ay; for (uint32_t d : dokunulan) if (c2[d] >= 20) ay.push_back(d);
    sort(ay.begin(), ay.end(), [&](uint32_t a, uint32_t b) { uint64_t x = (uint64_t)c2[a] * say[b], y = (uint64_t)c2[b] * say[a]; return x != y ? x > y : (c2[a] != c2[b] ? c2[a] > c2[b] : ad[a] < ad[b]); });
    for (size_t i = 0; i < ay.size() && i < ust; i++) fprintf(fa, "%s\t*%s\t%u\t%u\n", h.c_str(), ad[ay[i]].c_str(), c2[ay[i]], say[ay[i]]);
    for (uint32_t d : dokunulan) alanAlt[alanI[d]] += c2[d];
    fprintf(fn, "%s\t<toplam>\t%lu\t%lu\n", h.c_str(), (unsigned long)kenar, (unsigned long)dugum);
    for (size_t i = 0; i < alanAd.size(); i++) if (alanAlt[i]) { fprintf(fn, "%s\t%s\t%lu\t%lu\n", h.c_str(), alanAd[i].c_str(), (unsigned long)alanAlt[i], (unsigned long)alanGenel[i]); alanAlt[i] = 0; }
    for (uint32_t d : dokunulan) c2[d] = 0;
  }
  fclose(fa); fclose(fd); fclose(fn);
  // önermesi tam olarak verilen ad olan teoremler
  FILE* fk = fopen((kl + "/kanitlayan.tsv").c_str(), "w");
  if (strcmp(argv[6], "-")) {
    vector<char> ist(N, 0);
    for (auto& s : satirlar(argv[6])) { auto it = sira.find(s); if (it != sira.end()) ist[it->second] = 1; }
    for (uint64_t u = 0; u < N; u++) if (tur[u] == 't' && tipBoy[u] <= 1 && ot[u] - o[u] == 1 && ist[K[o[u]]])
      fprintf(fk, "%s\t%s\t%s\n", ad[K[o[u]]].c_str(), ad[u].c_str(), baskin[u] == YOK ? "-" : ad[baskin[u]].c_str());
  }
  fclose(fk);
  return 0;
}

// Ayıkla / Extract — resmi lean4export kaydından, verilen bildirimlerin terimlerini ayrı bir NDJSON olarak çıkarır.
// (suz.cpp'nin türevi. Fark: teorem ispatları yalnızca ikinci listedeki adlar için yazılır; yazılmayan değer -1 olur.
//  Çıktıyı arac/dokak.py okur ve Lean derlemeden terim dökümüne çevirir.)
// TR: Teoremlerde yalnızca tip (önerme), diğer bildirimlerde tip + değer izlenir (kapanis.cpp ile aynı kural).
//     Bütün ad ve düzey satırları korunur; ifadeler yalnızca gerekenler kalacak biçimde yeniden numaralanır.
//     Kayıt iki kez okunur (iki ayrı akış): 1) ihtiyaçları işaretle, 2) yaz.
// EN: Extracts the statement closure of the given declarations from an official lean4export NDJSON file.
//     Theorems contribute only their type; other declarations their type and value. All name/level lines
//     are kept; expressions are renumbered densely. The input is read twice (two separate streams).
// Kullanım / usage:
//   suz 1 gecici.bin adlar.txt < kayit.ndjson            (1. geçiş; durum gecici.bin* dosyalarına yazılır)
//   suz 2 gecici.bin adlar.txt < kayit.ndjson > cikti.ndjson   (2. geçiş)
//   adlar.txt: satır başına bir tam ad (kapanis.cpp biçimi: sayı parçaları `#0`)
//   --ispatli (3. argümandan sonra): teorem değerlerini de izle ve yaz
#include <cstdio>
#include <cstdint>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <sys/mman.h>
#include <fcntl.h>
#include <unistd.h>
using namespace std;
static const uint32_t YOK = 0xFFFFFFFFu;
static const uint32_t SABIT = 0xFFFFFFFEu;  // çocuk tablosunda: bu ifade bir sabittir, ilk alan ad kimliğidir
static long gi(const char* s, const char* k) { const char* p = strstr(s, k); if (!p) return -1; return strtol(p + strlen(k), nullptr, 10); }

static bool anahtar_ifade(const char* k, size_t kl, bool ifadeSatiri) {
  // ifade kimliği taşıyan anahtarlar
  if (kl == 4 && !strncmp(k, "type", 4)) return true;
  if (kl == 5 && !strncmp(k, "value", 5)) return true;
  if (kl == 3 && !strncmp(k, "rhs", 3)) return true;
  if (!ifadeSatiri) return false;
  if (kl == 2 && !strncmp(k, "ie", 2)) return true;
  if (kl == 2 && !strncmp(k, "fn", 2)) return true;
  if (kl == 3 && !strncmp(k, "arg", 3)) return true;
  if (kl == 4 && !strncmp(k, "body", 4)) return true;
  if (kl == 6 && !strncmp(k, "struct", 6)) return true;
  if (kl == 4 && !strncmp(k, "expr", 4)) return true;
  return false;
}

int main(int argc, char** argv) {
  if (argc < 4) { fprintf(stderr, "kullanim: ayikla 1|2 gecici.bin adlar.txt [ispatli_adlar.txt] < kayit.ndjson\n"); return 1; }
  int gecis = atoi(argv[1]);
  string gec = argv[2];
  // dördüncü argüman: ispatı (değeri) da yazılacak teoremlerin ad listesi (isteğe bağlı)
  unordered_set<string> ispatli;
  if (argc > 4) { FILE* f = fopen(argv[4], "r"); if (f) { char b[16384]; while (fgets(b, sizeof b, f)) { string s(b); while (!s.empty() && (s.back() == '\n' || s.back() == '\r')) s.pop_back(); if (!s.empty()) ispatli.insert(s); } fclose(f); } }
  unordered_set<string> istenen;
  { FILE* f = fopen(argv[3], "r"); if (!f) { perror("adlar"); return 1; }
    char b[16384]; while (fgets(b, sizeof b, f)) { string s(b); while (!s.empty() && (s.back() == '\n' || s.back() == '\r')) s.pop_back(); if (!s.empty()) istenen.insert(s); } fclose(f); }
  uint64_t CAP = getenv("KUNYE_KAPASITE") ? strtoull(getenv("KUNYE_KAPASITE"), nullptr, 10) : 2100000000ULL;
  // çocuk tablosu: her ifade için en çok iki çocuk (+ letE gövdesi ayrı tabloda)
  int fd = open((gec).c_str(), gecis == 1 ? (O_RDWR | O_CREAT | O_TRUNC) : O_RDWR, 0644);
  if (fd < 0) { perror("gecici"); return 1; }
  if (gecis == 1 && ftruncate(fd, CAP * 8)) { perror("ft"); return 1; }
  uint32_t* E = (uint32_t*)mmap(nullptr, CAP * 8, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
  vector<uint64_t> gerek((CAP + 63) / 64, 0);
  auto isaret = [&](uint64_t i) { gerek[i >> 6] |= 1ULL << (i & 63); };
  auto gerekli = [&](uint64_t i) { return (gerek[i >> 6] >> (i & 63)) & 1ULL; };
  vector<uint64_t> lamB((CAP + 63) / 64, 0);   // ifade bir λ mı (boş koşul taraması için)
  auto lamMi = [&](uint64_t i) { return (lamB[i >> 6] >> (i & 63)) & 1ULL; };
  vector<uint64_t> piB((CAP + 63) / 64, 0);    // ifade bir ∀/→ mı (sonuç taraması için)
  auto piMi = [&](uint64_t i) { return (piB[i >> 6] >> (i & 63)) & 1ULL; };
  vector<uint8_t> secilenBildirim;  // bildirim sırası -> seçildi mi
  uint64_t ne = 0;

  if (gecis == 1) {
    unordered_map<uint32_t, uint32_t> ucuncu;
    struct BT { uint32_t ad, tip, sira; char tur; }; vector<BT> bildTip; vector<BT> tanimDeger;  // tanımlar: (ad, değer ifadesi)  // her bildirimin (ad, tip ifadesi, bildirim sırası)
    vector<uint32_t> npre{0}; vector<uint64_t> noff{0}; string nbuf;
    auto tam = [&](uint32_t x) { string r; while (x) { string p = nbuf.substr(noff[x - 1], noff[x] - noff[x - 1]); r = r.empty() ? p : p + "." + r; x = npre[x]; } return r; };
    char* buf = nullptr; size_t cap = 0; ssize_t n; uint64_t secilen = 0;
    while ((n = getline(&buf, &cap, stdin)) > 0) {
      const char* s = buf;
      if (s[2] == 'i' && s[3] == 'n' && s[4] == '"') {
        long pre = gi(s, "\"pre\":"); const char* q = strstr(s, "\"str\":\""); string nm;
        if (q) { q += 7; const char* e = strchr(q, '"'); nm.assign(q, e - q); }  // kapanis.cpp ile aynı
        else nm = "#" + to_string(gi(s, "\"i\":"));
        long id = gi(s, "\"in\":");
        if ((size_t)id != npre.size()) { fprintf(stderr, "ad sirasi bozuk %ld\n", id); return 2; }
        npre.push_back((uint32_t)pre); nbuf += nm; noff.push_back(nbuf.size()); continue;
      }
      if (s[2] == 'i' && s[3] == 'l' && s[4] == '"') continue;
      const char* ie = strstr(s, "\"ie\":");
      if (ie && (s[2] != 'i' || strncmp(s, "{\"inductive\"", 12))) {
        uint32_t a = YOK, b = YOK; long id = strtol(ie + 5, nullptr, 10);
        if ((uint64_t)id != ne) { fprintf(stderr, "ifade sirasi bozuk %ld != %llu\n", id, (unsigned long long)ne); return 2; }
        if (strstr(s, "\"app\":{")) { a = gi(s, "\"fn\":"); b = gi(s, "\"arg\":"); }
        else if (strstr(s, "\"lam\":{") || strstr(s, "\"forallE\":{")) { a = gi(s, "\"type\":"); b = gi(s, "\"body\":"); if (strstr(s, "\"lam\":{")) lamB[ne >> 6] |= 1ULL << (ne & 63); else piB[ne >> 6] |= 1ULL << (ne & 63); }
        else if (strstr(s, "\"letE\":{")) { a = gi(s, "\"type\":"); b = gi(s, "\"value\":"); ucuncu[id] = gi(s, "\"body\":"); }
        else if (strstr(s, "\"proj\":{")) { a = gi(s, "\"struct\":"); }
        else if (strstr(s, "\"mdata\":{")) { a = gi(s, "\"expr\":"); }
        else if (strstr(s, "\"const\":{")) { a = gi(s, "\"name\":"); b = SABIT; }  // sabit: ad kimliği saklanır
        E[2 * ne] = a; E[2 * ne + 1] = b; ne++; continue;
      }
      if (!strncmp(s, "{\"meta\"", 7)) continue;
      // bildirim satırı
      char tur = s[2];  // t(hm) d(ef) a(xiom) o(paque) q(uot) i(nductive)
      bool sec = false, isp = false; vector<long> kok; long sonAd = -1, sonAd2 = -1;
      const char* p = s;
      while ((p = strchr(p, '"'))) {
        const char* k = p + 1; const char* ke = strchr(k, '"'); if (!ke) break; size_t kl = ke - k; p = ke + 1;
        if (*p != ':') continue; p++; if (*p < '0' || *p > '9') continue;
        long v = strtol(p, nullptr, 10);
        if (kl == 4 && !strncmp(k, "name", 4)) { sonAd = v; sonAd2 = v; }
        if (tur == 'd' && kl == 5 && !strncmp(k, "value", 5) && sonAd2 >= 0) { tanimDeger.push_back({(uint32_t)sonAd2, (uint32_t)v, 0, tur}); sonAd2 = -1; }
        if (kl == 4 && !strncmp(k, "type", 4) && sonAd >= 0) { bildTip.push_back({(uint32_t)sonAd, (uint32_t)v, (uint32_t)secilenBildirim.size(), tur}); sonAd = -1; }
        if (kl == 4 && !strncmp(k, "name", 4)) { string ad = tam((uint32_t)v); if (istenen.count(ad) || ispatli.count(ad)) sec = true; if (ispatli.count(ad)) isp = true; }
        else if (kl == 4 && !strncmp(k, "type", 4)) kok.push_back(v);
        else if ((kl == 5 && !strncmp(k, "value", 5)) || (kl == 3 && !strncmp(k, "rhs", 3))) { if (tur != 't' || isp) kok.push_back(v); }
      }
      secilenBildirim.push_back(sec);
      if (sec) { secilen++; for (long v : kok) if (v >= 0) isaret(v); }
    }
    // geriye doğru tarama: çocuk kimlikleri her zaman ebeveynden küçüktür
    uint64_t say = 0;
    unordered_set<uint32_t> kullanilanAd;
    auto tara = [&](bool sabitTopla) {
      say = 0;
      for (uint64_t i = ne; i-- > 0;) {
        if (!gerekli(i)) continue;
        say++;
        uint32_t a = E[2 * i], b = E[2 * i + 1];
        if (b == SABIT) { if (sabitTopla) kullanilanAd.insert(a); continue; }
        if (a != YOK) isaret(a);
        if (b != YOK) isaret(b);
        auto it = ucuncu.find((uint32_t)i); if (it != ucuncu.end()) isaret(it->second);
      }
    };
    // boş koşul taraması: gövdesi, λ'lar soyulunca, `True` sabiti olan tanımlar (bütün kayıtta)
    { const char* by = getenv("AYIKLA_BOS");
      if (by) { FILE* bf = fopen(by, "w"); uint64_t bs = 0;
        for (auto& x : tanimDeger) { uint64_t i = x.tip; int k = 0;
          while (lamMi(i)) { i = E[2 * i + 1]; k++; }
          if (E[2 * i + 1] == SABIT && tam(E[2 * i]) == "True") { fprintf(bf, "%s\t%d\n", tam(x.ad).c_str(), k); bs++; } }
        fclose(bf); fprintf(stderr, "govdesi True olan tanim %llu / %zu\n", (unsigned long long)bs, tanimDeger.size()); } }
    // sonuç taraması: önermesi (∀'ler soyulunca) verilen adlardan biriyle biten teoremler (bütün kayıtta)
    //   AYIKLA_SONUC_AD = adların dosyası (satır başına bir ad), AYIKLA_SONUC = çıktı: hedef <TAB> teorem <TAB> ∀ sayısı
    { const char* sa = getenv("AYIKLA_SONUC_AD"); const char* sc = getenv("AYIKLA_SONUC");
      if (sa && sc) { unordered_set<string> hedef; { FILE* hf = fopen(sa, "r"); char* hb = nullptr; size_t hc = 0; ssize_t hn;
          if (hf) { while ((hn = getline(&hb, &hc, hf)) > 0) { while (hn > 0 && (hb[hn - 1] == '\n' || hb[hn - 1] == '\r')) hb[--hn] = 0; if (hn) hedef.insert(hb); } fclose(hf); } }
        unordered_map<uint32_t, char> adHedef;   // ad kimliği -> hedef mi (önbellek)
        FILE* sf = fopen(sc, "w"); uint64_t ss = 0, st = 0;
        for (auto& x : bildTip) { if (x.tur != 't') continue; st++;
          uint64_t i = x.tip; int k = 0;
          while (piMi(i)) { i = E[2 * i + 1]; k++; }
          while (!lamMi(i) && !piMi(i) && E[2 * i] != YOK && E[2 * i + 1] != YOK && E[2 * i + 1] != SABIT && !ucuncu.count((uint32_t)i)) i = E[2 * i];
          if (E[2 * i + 1] != SABIT) continue;
          uint32_t aid = E[2 * i]; auto it = adHedef.find(aid);
          if (it == adHedef.end()) it = adHedef.emplace(aid, hedef.count(tam(aid)) ? 1 : 0).first;
          if (it->second) { fprintf(sf, "%s\t%s\t%d\n", tam(aid).c_str(), tam(x.ad).c_str(), k); ss++; } }
        fclose(sf); fprintf(stderr, "sonuc taramasi: %llu teorem / %llu, hedef %zu\n", (unsigned long long)ss, (unsigned long long)st, hedef.size()); } }
    tara(true);
    // bir katman: seçilen terimlerde geçen sabitlerin yalnızca TİPLERİ de yazılır (bağlayıcı türleri ve önerme olup olmadıkları için)
    uint64_t tipEk = 0;
    for (auto& x : bildTip) if (kullanilanAd.count(x.ad) && !secilenBildirim[x.sira]) { isaret(x.tip); tipEk++; }
    for (auto& x : bildTip) if (kullanilanAd.count(x.ad) && !secilenBildirim[x.sira]) secilenBildirim[x.sira] = 2;
    tara(false);
    fprintf(stderr, "yalniz tipi yazilan sabit %llu\n", (unsigned long long)tipEk);
    // durum: gerekli bitleri ve seçilen bildirimleri yaz
    FILE* f = fopen((gec + ".bit").c_str(), "wb"); fwrite(&ne, 8, 1, f); fwrite(gerek.data(), 8, (ne + 63) / 64, f); fclose(f);
    f = fopen((gec + ".sec").c_str(), "wb"); fwrite(secilenBildirim.data(), 1, secilenBildirim.size(), f); fclose(f);
    fprintf(stderr, "ifade %llu, gerekli ifade %llu, ad %zu, bildirim %zu, secilen %llu (istenen %zu)\n",
            (unsigned long long)ne, (unsigned long long)say, npre.size(), secilenBildirim.size(),
            (unsigned long long)secilen, istenen.size());
    return 0;
  }

  // 2. geçiş
  { FILE* f = fopen((gec + ".bit").c_str(), "rb"); if (!f) { perror("bit"); return 1; }
    if (fread(&ne, 8, 1, f) != 1) return 1; gerek.assign((ne + 63) / 64, 0);
    if (fread(gerek.data(), 8, gerek.size(), f) != gerek.size()) return 1; fclose(f);
    f = fopen((gec + ".sec").c_str(), "rb"); if (!f) { perror("sec"); return 1; }
    fseek(f, 0, SEEK_END); long boy = ftell(f); fseek(f, 0, SEEK_SET); secilenBildirim.resize(boy);
    if (fread(secilenBildirim.data(), 1, boy, f) != (size_t)boy) return 1; fclose(f); }
  // sıra: yeni kimlik = kendinden küçük gerekli ifade sayısı
  vector<uint32_t> blok(gerek.size() + 1, 0);
  for (size_t w = 0; w < gerek.size(); w++) blok[w + 1] = blok[w] + __builtin_popcountll(gerek[w]);
  auto yeni = [&](uint64_t i) -> long {
    if (i >= ne || !gerekli(i)) return -1;
    uint64_t w = i >> 6, m = (i & 63) ? (gerek[w] & ((1ULL << (i & 63)) - 1)) : 0;
    return blok[w] + __builtin_popcountll(m);
  };
  char* buf = nullptr; size_t cap = 0; ssize_t n; uint64_t bsira = 0, yazilan = 0, eksik = 0, iid = 0;
  string out;
  while ((n = getline(&buf, &cap, stdin)) > 0) {
    const char* s = buf;
    bool add = (s[2] == 'i' && s[3] == 'n' && s[4] == '"') || (s[2] == 'i' && s[3] == 'l' && s[4] == '"') || !strncmp(s, "{\"meta\"", 7);
    if (add) { fwrite(s, 1, n, stdout); continue; }
    bool ifadeSatiri = strstr(s, "\"ie\":") && strncmp(s, "{\"inductive\"", 12);
    if (ifadeSatiri) { uint64_t id = iid++; if (!gerekli(id)) continue; }
    uint8_t secTur = 1;
    if (!ifadeSatiri) { secTur = bsira < secilenBildirim.size() ? secilenBildirim[bsira] : 0; bsira++; if (!secTur) continue; yazilan++; }
    // ifade kimliklerini yeniden numarala
    out.clear(); const char* p = s; const char* son = s + n;
    while (p < son) {
      const char* q = strchr(p, '"');
      if (!q) { out.append(p, son - p); break; }
      const char* ke = strchr(q + 1, '"'); if (!ke) { out.append(p, son - p); break; }
      out.append(p, ke + 1 - p); const char* k = q + 1; size_t kl = ke - k; p = ke + 1;
      if (*p == ':' && p[1] >= '0' && p[1] <= '9' && anahtar_ifade(k, kl, ifadeSatiri)) {
        char* e; long v = strtol(p + 1, &e, 10); long y = yeni((uint64_t)v);
        if (secTur == 2 && !ifadeSatiri && !(kl == 4 && !strncmp(k, "type", 4))) y = -1;  // yalnız tipi yazılan bildirim
        if (y < 0) { y = -1; eksik++; }  // izlenmeyen teorem değeri (ispat): -1
        out += ':'; out += to_string(y); p = e;
      }
    }
    fwrite(out.data(), 1, out.size(), stdout);
  }
  fprintf(stderr, "yazilan bildirim %llu, izlenmeyen deger (ispat) %llu\n", (unsigned long long)yazilan, (unsigned long long)eksik);
  return 0;
}

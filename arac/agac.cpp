// Ağaç / Tree — tam bağımlılık grafiğinden (koni.cpp çıktısı) kökün ispat konisini ve baskınlık ağacını çıkarır.
// TR: * Koni: kökün (ana teoremin) doğrudan ya da dolaylı kullandığı bütün bildirimler (tip + ispat).
//     * Kullanılmayan: kayıtta olup koniye girmeyen proje bildirimleri.
//     * Baskınlık ağacı: X, Y'nin baskınıdır <=> kökten Y'ye giden HER yol X'ten geçer. Bir bildirimin
//       alt ağacı, yalnızca onun aracılığıyla kullanılan bildirimlerdir; makalenin katmanlı iskeleti budur.
//     Hepsi grafikten kesin olarak hesaplanır; tahmin yoktur.
// EN: From the full dependency graph: the proof cone of the root, the unused project declarations, and the
//     dominator tree of the cone (X dominates Y iff every path from the root to Y passes through X).
// Kullanım / usage:  agac dugum.tsv kenar.bin kokler.txt kutuphane_adlari.txt|- cikti_klasoru
#include <cstdio>
#include <cstdint>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
using namespace std;

int main(int argc, char** argv) {
  if (argc < 6) { fprintf(stderr, "kullanim: agac dugum.tsv kenar.bin kokler.txt kutuphane.txt|- cikti\n"); return 1; }
  vector<string> ad; vector<char> tur; vector<uint32_t> yeni, tipBoy, degBoy;
  { FILE* f = fopen(argv[1], "r"); if (!f) { perror("dugum"); return 1; }
    char* b = nullptr; size_t c = 0; ssize_t n;
    while ((n = getline(&b, &c, f)) > 0) {
      char* p = b; strsep(&p, "\t"); char* t = strsep(&p, "\t"); char* a = strsep(&p, "\t");
      char* y = strsep(&p, "\t"); char* tb = strsep(&p, "\t"); char* db = strsep(&p, "\t\n");
      if (!db) continue;
      tur.push_back(t[0]); ad.push_back(a); yeni.push_back(strtoul(y, nullptr, 10)); tipBoy.push_back(strtoul(tb, nullptr, 10)); degBoy.push_back(strtoul(db, nullptr, 10));
    }
    fclose(f); }
  uint64_t N = ad.size();
  // kenarlar (CSR): tip kenarları [o[i], ot[i]), değer kenarları [ot[i], o[i+1])
  vector<uint64_t> o(N + 2, 0), ot(N + 1, 0); vector<uint32_t> K;
  { FILE* f = fopen(argv[2], "rb"); if (!f) { perror("kenar"); return 1; }
    uint64_t n2; if (fread(&n2, 8, 1, f) != 1 || n2 != N) { fprintf(stderr, "dugum/kenar sayisi uyusmuyor %lu %lu\n", (unsigned long)n2, (unsigned long)N); return 1; }
    for (uint64_t i = 0; i < N; i++) {
      uint32_t h[2]; if (fread(h, 4, 2, f) != 2) { fprintf(stderr, "kenar kisa\n"); return 1; }
      o[i] = K.size(); ot[i] = o[i] + h[0]; K.resize(K.size() + h[0] + h[1]);
      if (h[0] + h[1] && fread(&K[o[i]], 4, h[0] + h[1], f) != h[0] + h[1]) { fprintf(stderr, "kenar kisa\n"); return 1; }
    }
    o[N] = K.size(); fclose(f); }
  unordered_map<string, uint32_t> sira; sira.reserve(N * 2);
  for (uint64_t i = 0; i < N; i++) sira.emplace(ad[i], (uint32_t)i);
  // kütüphane (Mathlib ve altı) adları
  vector<char> kut(N, 0); bool kutVar = false; uint64_t kutSay = 0;
  if (strcmp(argv[4], "-")) if (FILE* f = fopen(argv[4], "r")) {
    char* b = nullptr; size_t c = 0; ssize_t n;
    while ((n = getline(&b, &c, f)) > 0) { while (n > 0 && (b[n - 1] == '\n' || b[n - 1] == '\r')) b[--n] = 0; auto it = sira.find(b); if (it != sira.end()) { kut[it->second] = 1; kutSay++; } }
    fclose(f); kutVar = kutSay > 0; }
  vector<uint32_t> kok;
  { FILE* f = fopen(argv[3], "r"); if (!f) { perror("kok"); return 1; } char b[8192];
    while (fgets(b, sizeof b, f)) { string s(b); while (!s.empty() && (s.back() == '\n' || s.back() == '\r' || s.back() == ' ')) s.pop_back(); if (s.empty()) continue;
      auto it = sira.find(s); if (it != sira.end()) kok.push_back(it->second); else fprintf(stderr, "kok bulunamadi: %s\n", s.c_str()); }
    fclose(f); }
  string kl = argv[5];
  if (kok.empty()) {
    // kök yoksa: yardım için aday adları yaz
    FILE* f = fopen((kl + "/kok_adaylari.txt").c_str(), "w");
    for (uint64_t i = 0; i < N; i++) if (ad[i].find('.') == string::npos || ad[i].find("iemann") != string::npos) fprintf(f, "%c\t%s\n", tur[i], ad[i].c_str());
    fclose(f); fprintf(stderr, "kok yok; adaylar kok_adaylari.txt\n"); return 3; }

  // 1) koniler: tam (tip+değer) ve önerme (teoremde yalnız tip)
  auto gez = [&](bool onerme) { vector<char> g(N, 0); vector<uint32_t> y(kok.begin(), kok.end()); for (auto r : kok) g[r] = 1;
    while (!y.empty()) { uint32_t x = y.back(); y.pop_back(); uint64_t son = (onerme && tur[x] == 't') ? ot[x] : o[x + 1];
      for (uint64_t k = o[x]; k < son; k++) { uint32_t z = K[k]; if (!g[z]) { g[z] = 1; y.push_back(z); } } }
    return g; };
  vector<char> C = gez(false), S = gez(true);

  // aksiyomlar: kayıttaki her aksiyom; kökün ispat konisinde mi, önerme konisinde mi, kütüphane mi (hiçbiri atlanmaz)
  vector<uint32_t> aks; uint64_t aksKoni = 0;
  for (uint64_t i = 0; i < N; i++) if (tur[i] == 'a') { aks.push_back((uint32_t)i); if (C[i]) aksKoni++; }
  { FILE* f = fopen((string(argv[5]) + "/aksiyomlar.tsv").c_str(), "w");
    if (f) { fprintf(f, "ad\tkonide\tonermede\tkutuphane\n");
      for (auto i : aks) fprintf(f, "%s\t%d\t%d\t%d\n", ad[i].c_str(), (int)C[i], (int)S[i], (int)kut[i]); fclose(f); } }

  // önerme konisindeki bütün adlar (kütüphane dahil): kitapçık kurmak için (arac/suz.cpp girdisi)
  { FILE* f = fopen((string(argv[5]) + "/onerme_adlari.txt").c_str(), "w");
    if (f) { for (uint64_t i = 0; i < N; i++) if (S[i]) fprintf(f, "%s\n", ad[i].c_str()); fclose(f); } }

  // 2) baskınlık ağacı: proje düğümleri (kütüphane dışı), sanal kök = N
  auto proje = [&](uint32_t x) { return C[x] && !kut[x]; };
  vector<int32_t> rpo(N + 1, -1); vector<uint32_t> dizi;  // dizi: ters art-sıra
  { // yinelemeli DFS, art-sıra
    vector<pair<uint32_t, uint64_t>> y; vector<char> g(N + 1, 0); vector<uint32_t> art;
    g[N] = 1;
    // sanal kökün çocukları: kökler
    vector<uint32_t> kc(kok.begin(), kok.end());
    size_t ki = 0;
    while (true) {
      if (y.empty()) { while (ki < kc.size() && g[kc[ki]]) ki++; if (ki == kc.size()) break; g[kc[ki]] = 1; y.push_back({kc[ki], o[kc[ki]]}); continue; }
      auto& u = y.back(); uint32_t x = u.first; bool indi = false;
      while (u.second < o[x + 1]) { uint32_t z = K[u.second++]; if (!g[z] && proje(z)) { g[z] = 1; y.push_back({z, o[z]}); indi = true; break; } }
      if (!indi) { art.push_back(x); y.pop_back(); }
    }
    art.push_back((uint32_t)N);
    dizi.assign(art.rbegin(), art.rend());
    for (size_t i = 0; i < dizi.size(); i++) rpo[dizi[i]] = (int32_t)i;
  }
  size_t P = dizi.size();  // sanal kök dahil
  // öncüller (rpo numarasıyla)
  vector<uint32_t> oSay(P + 1, 0);
  for (size_t i = 1; i < P; i++) { uint32_t x = dizi[i]; for (uint64_t k = o[x]; k < o[x + 1]; k++) { int32_t r = rpo[K[k]]; if (r > 0) oSay[r + 1]++; } }
  for (auto r : kok) oSay[rpo[r] + 1]++;
  for (size_t i = 0; i < P; i++) oSay[i + 1] += oSay[i];
  vector<uint32_t> onc(oSay[P]), dol(oSay.begin(), oSay.end() - 1);
  for (size_t i = 1; i < P; i++) { uint32_t x = dizi[i]; for (uint64_t k = o[x]; k < o[x + 1]; k++) { int32_t r = rpo[K[k]]; if (r > 0) onc[dol[r]++] = (uint32_t)i; } }
  for (auto r : kok) onc[dol[rpo[r]]++] = 0;
  vector<int32_t> idom(P, -1); idom[0] = 0; bool degisti = true; int tur_sayisi = 0;
  auto kesis = [&](int32_t a, int32_t b) { while (a != b) { while (a > b) a = idom[a]; while (b > a) b = idom[b]; } return a; };
  while (degisti) { degisti = false; tur_sayisi++;
    for (size_t i = 1; i < P; i++) { int32_t yeniD = -1;
      for (uint32_t k = oSay[i]; k < oSay[i + 1]; k++) { int32_t p = onc[k]; if (idom[p] < 0) continue; yeniD = yeniD < 0 ? p : kesis(p, yeniD); }
      if (yeniD >= 0 && idom[i] != yeniD) { idom[i] = yeniD; degisti = true; } } }
  // alt ağaç toplamları ve derinlik
  vector<uint64_t> altSay(P, 1), altAgr(P, 0); vector<uint32_t> der(P, 0), kullanan(P, 0), cocuk(P, 0);
  for (size_t i = 1; i < P; i++) { altAgr[i] = yeni[dizi[i]]; kullanan[i] = oSay[i + 1] - oSay[i]; }
  altSay[0] = 0;
  for (size_t i = P - 1; i >= 1; i--) { altSay[idom[i]] += altSay[i]; altAgr[idom[i]] += altAgr[i]; cocuk[idom[i]]++; }
  for (size_t i = 1; i < P; i++) der[i] = der[idom[i]] + 1;

  FILE* f = fopen((kl + "/taslar.tsv").c_str(), "w");
  fprintf(f, "ad\ttur\tbaskin\tderinlik\talt_sayi\talt_agirlik\tagirlik\ttip_boyu\tdeger_boyu\tkullanan\tcocuk\tonermede\n");
  for (size_t i = 1; i < P; i++) { uint32_t x = dizi[i];
    fprintf(f, "%s\t%c\t%s\t%u\t%lu\t%lu\t%u\t%u\t%u\t%u\t%u\t%d\n", ad[x].c_str(), tur[x], idom[i] == 0 ? "<kok>" : ad[dizi[idom[i]]].c_str(), der[i],
            (unsigned long)altSay[i], (unsigned long)altAgr[i], yeni[x], tipBoy[x], degBoy[x], kullanan[i], cocuk[i], (int)S[x]); }
  fclose(f);
  // kullanılmayan proje bildirimleri
  f = fopen((kl + "/kullanilmayan.tsv").c_str(), "w");
  uint64_t tp = 0, tpA = 0, kp = 0, kpA = 0, ck = 0, sk = 0, sp = 0, turS[128] = {0}, turK[128] = {0}, toplamA = 0, kenarP = 0;
  for (uint64_t i = 0; i < N; i++) { toplamA += yeni[i];
    if (kut[i]) { if (C[i]) ck++; if (S[i]) sk++; continue; }
    tp++; tpA += yeni[i]; turS[(int)tur[i]]++;
    if (S[i]) sp++;
    if (C[i]) { kp++; kpA += yeni[i]; turK[(int)tur[i]]++; } else fprintf(f, "%s\t%c\t%u\n", ad[i].c_str(), tur[i], yeni[i]); }
  fclose(f);
  for (size_t i = 1; i < P; i++) kenarP += oSay[i + 1] - oSay[i];
  f = fopen((kl + "/ozet.json").c_str(), "w");
  fprintf(f, "{\"bildirim\":%lu,\"kenar\":%zu,\"ifade_agirligi\":%lu,\"kutuphane_ayrimi\":%s,\"kutuphane\":%lu,\n", (unsigned long)N, K.size(), (unsigned long)toplamA, kutVar ? "true" : "false", (unsigned long)kutSay);
  fprintf(f, "\"proje\":%lu,\"proje_agirlik\":%lu,\"konide_proje\":%lu,\"konide_proje_agirlik\":%lu,\"konide_kutuphane\":%lu,\n", (unsigned long)tp, (unsigned long)tpA, (unsigned long)kp, (unsigned long)kpA, (unsigned long)ck);
  fprintf(f, "\"onerme_konisinde_proje\":%lu,\"onerme_konisinde_kutuphane\":%lu,\"agac_dugum\":%zu,\"agac_kenar\":%lu,\"baskinlik_turu\":%d,\n", (unsigned long)sp, (unsigned long)sk, P - 1, (unsigned long)kenarP, tur_sayisi);
  fprintf(f, "\"proje_tur\":{"); bool ilk = true; for (int c = 0; c < 128; c++) if (turS[c]) { fprintf(f, "%s\"%c\":[%lu,%lu]", ilk ? "" : ",", c, (unsigned long)turS[c], (unsigned long)turK[c]); ilk = false; }
  fprintf(f, "},\"kok\":["); for (size_t i = 0; i < kok.size(); i++) fprintf(f, "%s\"%s\"", i ? "," : "", ad[kok[i]].c_str());
  // konideki aksiyomlar (ad listesi; tam tablo aksiyomlar.tsv). JSON için \ ve " kaçırılır.
  auto js = [](const string& x) { string r; for (char c : x) { if (c == '"' || c == '\\') r += '\\'; r += c; } return r; };
  fprintf(f, "],\n\"aksiyom_kayitta\":%zu,\"aksiyom_konide\":[", aks.size()); bool ilkA = true;
  for (auto i : aks) if (C[i]) { fprintf(f, "%s\"%s\"", ilkA ? "" : ",", js(ad[i]).c_str()); ilkA = false; }
  fprintf(f, "]}\n");
  fclose(f);
  fprintf(stderr, "bildirim %lu proje %lu konide %lu agac %zu tur %d aksiyom %zu (konide %lu)\n", (unsigned long)N, (unsigned long)tp, (unsigned long)kp, P - 1, tur_sayisi, aks.size(), (unsigned long)aksKoni);
  return 0;
}

// Karşıla / Discharge — adlandırılmış bir önerme ispatın neresinde kuruluyor? Tam bağımlılık grafiğinden (koni.cpp çıktısı).
// TR: Verilen her H önermesi için, kökün ispat konisindeki bildirimler dört sınıfa sayılır. Yalnızca kenarlara bakılır;
//     ispat terimi okunmaz, bütçe sınırı yoktur, konideki HER bildirim taranır:
//       tasiyan : önermesinde (tipinde) H geçen bildirimler (H'yi varsayan ya da sonuç olarak veren; grafik ikisini ayırmaz)
//       kuran   : ispatında H'nin kurucusu geçen, önermesinde H geçmeyen bildirimler (H bir yapıysa: H burada kuruluyor ve dışarı taşınmıyor)
//       kuran_t : ispatında H'nin kurucusu geçen, önermesinde de H geçen bildirimler (H'yi kurup sonuç olarak veriyor olabilir)
//       iceride : önermesinde H geçmeyen, ispatında H'nin adı geçen bildirimler (H bir tanımsa: ispatın içinde anılıyor)
//       kullanan: önermesinde H geçmeyen, ispatında bir `tasiyan` bildirimi kullanan bildirimler (H'nin taşınmasının bittiği sınır)
//     "Önermesinde geçmeyen" kesindir. "İspatında geçen": koni.cpp değer kenarını tipte olmayan adlar için yazar; bu yüzden
//     kuran/iceride/kullanan sınıflarında tip koşulu ayrıca sınanır.
//     Bir yapı için kuran = kuran_t = 0 ise kurucusu konide hiç kullanılmıyor demektir (çıktıda öyle yazılır).
// EN: For each named statement H, counts the declarations of the root's proof cone that carry H in their statement,
//     that use H's constructor in their proof (with and without H in their own statement), that mention H only inside
//     their proof, and that use a carrier without carrying H themselves. Graph edges only; every declaration is scanned.
// Kullanım / usage:  karsila dugum.tsv kenar.bin hedefler.txt taslar.tsv|- cikti.tsv
//   hedefler.txt: satır başına bir tam ad.  taslar.tsv: agac.cpp çıktısı (koni ve ağırlıklar); "-" ise bütün kayıt sayılır.
#include <cstdio>
#include <cstdint>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

static bool yardimci(const string& a) {  // Lean'in bir tip için kendiliğinden ürettiği adlar: sınıflara sayılmaz
  static const char* son[] = {".rec", ".recOn", ".casesOn", ".noConfusion", ".noConfusionType", ".inj", ".injEq", ".sizeOf_spec",
                              ".ctorIdx", ".ctorElim", ".toCtorIdx", ".below", ".brecOn", ".ibelow", ".binductionOn", ".ext_iff", ".ext"};
  for (auto s : son) { size_t n = strlen(s); if (a.size() >= n && !a.compare(a.size() - n, n, s)) return true; }
  return a.find("._") != string::npos || a.find(".match_") != string::npos || a.find(".proof_") != string::npos;
}

int main(int argc, char** argv) {
  if (argc < 6) { fprintf(stderr, "kullanim: karsila dugum.tsv kenar.bin hedefler.txt taslar.tsv|- cikti.tsv\n"); return 1; }
  vector<string> ad; vector<char> tur;
  { FILE* f = fopen(argv[1], "r"); if (!f) { perror("dugum"); return 1; }
    char* b = nullptr; size_t c = 0; ssize_t n;
    while ((n = getline(&b, &c, f)) > 0) { char* p = b; strsep(&p, "\t"); char* t = strsep(&p, "\t"); char* a = strsep(&p, "\t"); if (!a) continue; tur.push_back(t[0]); ad.push_back(a); }
    fclose(f); }
  uint64_t N = ad.size();
  vector<uint64_t> o(N + 1, 0), ot(N, 0); vector<uint32_t> K;   // tip kenarları [o[i], ot[i]), değer kenarları [ot[i], o[i+1])
  { FILE* f = fopen(argv[2], "rb"); if (!f) { perror("kenar"); return 1; }
    uint64_t n2; if (fread(&n2, 8, 1, f) != 1 || n2 != N) { fprintf(stderr, "dugum/kenar sayisi uyusmuyor\n"); return 1; }
    for (uint64_t i = 0; i < N; i++) { uint32_t h[2]; if (fread(h, 4, 2, f) != 2) { fprintf(stderr, "kenar kisa\n"); return 1; }
      o[i] = K.size(); ot[i] = o[i] + h[0]; K.resize(K.size() + h[0] + h[1]);
      if (h[0] + h[1] && fread(&K[o[i]], 4, h[0] + h[1], f) != h[0] + h[1]) { fprintf(stderr, "kenar kisa\n"); return 1; } }
    o[N] = K.size(); fclose(f); }
  unordered_map<string, uint32_t> sira; sira.reserve(N * 2);
  for (uint64_t i = 0; i < N; i++) sira.emplace(ad[i], (uint32_t)i);
  // koni ve ağırlık
  vector<char> koni(N, 1); vector<uint64_t> agr(N, 0); uint64_t top = 0; bool koniVar = strcmp(argv[4], "-") != 0;
  if (koniVar) { fill(koni.begin(), koni.end(), 0);
    FILE* f = fopen(argv[4], "r"); if (!f) { perror("taslar"); return 1; }
    char* b = nullptr; size_t c = 0; ssize_t n; bool ilk = true;
    while ((n = getline(&b, &c, f)) > 0) { if (ilk) { ilk = false; continue; }
      char* p = b; char* a = strsep(&p, "\t"); strsep(&p, "\t"); char* bs = strsep(&p, "\t"); strsep(&p, "\t"); strsep(&p, "\t"); char* aa = strsep(&p, "\t");
      if (!aa) continue; auto it = sira.find(a); if (it == sira.end()) continue;
      koni[it->second] = 1; agr[it->second] = strtoull(aa, nullptr, 10); if (!strcmp(bs, "<kok>")) top += agr[it->second]; }
    fclose(f); }
  // hedefler
  vector<uint32_t> H; vector<string> yok;
  { FILE* f = fopen(argv[3], "r"); if (!f) { perror("hedef"); return 1; } char* b = nullptr; size_t c = 0; ssize_t n;
    while ((n = getline(&b, &c, f)) > 0) { while (n > 0 && (b[n - 1] == '\n' || b[n - 1] == '\r' || b[n - 1] == ' ')) b[--n] = 0; if (!n) continue;
      auto it = sira.find(b); if (it != sira.end()) H.push_back(it->second); else yok.push_back(b); }
    fclose(f); }
  sort(H.begin(), H.end()); H.erase(unique(H.begin(), H.end()), H.end());
  size_t M = H.size();
  vector<int32_t> hedefNo(N, -1), kurucuNo(N, -1);   // düğüm -> hedef sırası (kendisi / kurucusu olduğu hedef)
  vector<uint32_t> kurucuSay(M, 0);
  for (size_t h = 0; h < M; h++) hedefNo[H[h]] = (int32_t)h;
  for (size_t h = 0; h < M; h++) if (tur[H[h]] == 'i')
    for (uint64_t k = ot[H[h]]; k < o[H[h] + 1]; k++) if (tur[K[k]] == 'c') { kurucuNo[K[k]] = (int32_t)h; kurucuSay[h]++; }
  // 1. geçiş: her düğümün önermesinde geçen hedefler (tasiyan)
  vector<uint64_t> tb(N + 1, 0); vector<uint32_t> TH;   // düğüm -> tipindeki hedefler (CSR)
  for (uint64_t x = 0; x < N; x++) { tb[x] = TH.size();
    for (uint64_t k = o[x]; k < ot[x]; k++) { int32_t h = hedefNo[K[k]]; if (h >= 0) TH.push_back((uint32_t)h); }
    sort(TH.begin() + tb[x], TH.end()); }
  tb[N] = TH.size();
  auto tipte = [&](uint64_t x, uint32_t h) { return binary_search(TH.begin() + tb[x], TH.begin() + tb[x + 1], h); };
  // 2. geçiş: sınıflar
  enum { TAS, KUR, KURT, IC, KUL, SINIF };
  vector<uint64_t> say(M * SINIF, 0); vector<vector<pair<uint64_t, uint32_t>>> en(M * SINIF);   // her sınıfın en ağır 3 üyesi
  auto ekle = [&](uint32_t h, int s, uint64_t x) { say[h * SINIF + s]++; auto& v = en[h * SINIF + s]; v.push_back({agr[x], (uint32_t)x});
    sort(v.begin(), v.end(), [&](const pair<uint64_t, uint32_t>& a, const pair<uint64_t, uint32_t>& b) { return a.first != b.first ? a.first > b.first : ad[a.second] < ad[b.second]; });
    if (v.size() > 3) v.pop_back(); };
  vector<uint32_t> g; vector<char> s2;
  for (uint64_t x = 0; x < N; x++) {
    if (!koni[x] || tur[x] == 'c' || tur[x] == 'r' || tur[x] == 'i' || hedefNo[x] >= 0 || yardimci(ad[x])) continue;
    for (uint64_t k = tb[x]; k < tb[x + 1]; k++) if (k == tb[x] || TH[k] != TH[k - 1]) ekle(TH[k], TAS, x);
    g.clear(); s2.clear();   // (hedef, sınıf) çiftleri; bir bildirim bir sınıfa bir kez sayılır
    auto not_et = [&](uint32_t h, char s) { for (size_t i = 0; i < g.size(); i++) if (g[i] == h && s2[i] == s) return; g.push_back(h); s2.push_back(s); };
    for (uint64_t k = o[x]; k < o[x + 1]; k++) { uint32_t yk = K[k]; bool deger = k >= ot[x];
      if (kurucuNo[yk] >= 0) not_et((uint32_t)kurucuNo[yk], tipte(x, (uint32_t)kurucuNo[yk]) ? KURT : KUR);
      if (!deger) continue;
      if (hedefNo[yk] >= 0 && !tipte(x, (uint32_t)hedefNo[yk])) not_et((uint32_t)hedefNo[yk], IC);
      for (uint64_t j = tb[yk]; j < tb[yk + 1]; j++) if (!tipte(x, TH[j]) && tur[yk] != 'c' && tur[yk] != 'r' && tur[yk] != 'i' && !yardimci(ad[yk])) not_et(TH[j], KUL); }
    for (size_t i = 0; i < g.size(); i++) ekle(g[i], s2[i], x);
  }
  FILE* f = fopen(argv[5], "w"); if (!f) { perror("cikti"); return 1; }
  fprintf(f, "ad\ttur\tkurucu\ttasiyan\tkuran\tkuran_t\ticeride\tkullanan\tsonuc\ten_agir_kuran\ten_agir_kuran_t\ten_agir_iceride\ten_agir_kullanan\n");
  auto liste = [&](uint32_t h, int s) { string r; for (auto& p : en[h * SINIF + s]) { char b[64]; snprintf(b, sizeof b, " (%.4f)", top ? 100.0 * p.first / top : 0.0); r += (r.empty() ? "" : "; ") + ad[p.second] + (koniVar ? b : ""); } return r.empty() ? string("-") : r; };
  vector<uint32_t> sirali(M); for (size_t h = 0; h < M; h++) sirali[h] = (uint32_t)h;
  sort(sirali.begin(), sirali.end(), [&](uint32_t a, uint32_t b) { return ad[H[a]] < ad[H[b]]; });
  uint64_t sonucSay[4] = {0, 0, 0, 0};
  for (uint32_t h : sirali) { const uint64_t* c = &say[h * SINIF]; const char* sonuc; int si;
    if (c[KUR]) { sonuc = "kuruluyor"; si = 0; }                       // kurucu, önermesinde H olmayan bir ispatta kullanılıyor
    else if (c[IC] || c[KUL]) { sonuc = "iceride"; si = 1; }           // H'yi taşımayan bir ispat H'yi anıyor ya da bir taşıyanı kullanıyor
    else if (c[KURT]) { sonuc = "yalniz_tasiyan_kuruyor"; si = 2; }    // kuranların hepsi H'yi önermesinde de taşıyor
    else { sonuc = "baglanamadi"; si = 3; }                            // konide H'yi kuran ya da taşımadan kullanan bildirim yok
    sonucSay[si]++;
    fprintf(f, "%s\t%c\t%u\t%lu\t%lu\t%lu\t%lu\t%lu\t%s\t%s\t%s\t%s\t%s\n", ad[H[h]].c_str(), tur[H[h]], kurucuSay[h], (unsigned long)c[TAS], (unsigned long)c[KUR], (unsigned long)c[KURT],
            (unsigned long)c[IC], (unsigned long)c[KUL], sonuc, liste(h, KUR).c_str(), liste(h, KURT).c_str(), liste(h, IC).c_str(), liste(h, KUL).c_str()); }
  sort(yok.begin(), yok.end());
  for (auto& y : yok) fprintf(f, "%s\t?\t0\t0\t0\t0\t0\t0\tkayitta_yok\t-\t-\t-\t-\n", y.c_str());
  fclose(f);
  fprintf(stderr, "hedef %zu (kayitta yok %zu): kuruluyor %lu, iceride %lu, yalniz tasiyan kuruyor %lu, baglanamadi %lu\n", M, yok.size(),
          (unsigned long)sonucSay[0], (unsigned long)sonucSay[1], (unsigned long)sonucSay[2], (unsigned long)sonucSay[3]);
  return 0;
}

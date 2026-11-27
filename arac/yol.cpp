// Yol payı / Path share — bağımlılık grafiğinde "kökten yapraklara giden yolların ne kadarı bu bildirimden geçiyor"
// TR: Baskınlık ağacı yalnızca BÜTÜN yolların geçtiği darboğazları gösterir. Bu araç ikinci bir ölçü verir: kökün ispat
//     konisindeki proje bildirimleri üzerinde, kökten yaprağa (başka proje bildirimi kullanmayan bildirime) giden bütün
//     bağımlılık yollarının kaçta kaçı her bildirimden geçer. Sayılar çok büyük olduğundan logaritmayla tutulur.
//     Kayıt sırası topolojik sıradır (bir bildirim kendinden öncekileri kullanır); sıraya uymayan kenarlar (tümevarımlı
//     tip ile kurucusu/özyineleyicisi arasındaki karşılıklı göndermeler) atılır ve sayısı yazılır.
// EN: For every project declaration in the root's cone: the fraction of all root-to-leaf dependency paths that pass
//     through it (log-space path counting on the DAG). Complements the dominator tree, which only sees strict bottlenecks.
// Kullanım / usage:  yol dugum.tsv kenar.bin kok_adi kutuphane.txt|- cikti.tsv
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;
static const double YOK = -1e300;
static double lekle(double a, double b) { if (a == YOK) return b; if (b == YOK) return a; double m = a > b ? a : b, n = a > b ? b : a; return m + log1p(exp(n - m)); }
int main(int argc, char** argv) {
  if (argc < 6) { fprintf(stderr, "kullanim: yol dugum.tsv kenar.bin kok kutuphane.txt|- cikti.tsv\n"); return 1; }
  vector<string> ad;
  { FILE* f = fopen(argv[1], "r"); if (!f) { perror("dugum"); return 1; }
    char* b = nullptr; size_t c = 0; ssize_t n;
    while ((n = getline(&b, &c, f)) > 0) { char* p = b; strsep(&p, "\t"); strsep(&p, "\t"); char* a = strsep(&p, "\t\n"); if (a) ad.push_back(a); }
    fclose(f); }
  uint64_t N = ad.size();
  vector<uint64_t> o(N + 1, 0); vector<uint32_t> K;
  { FILE* f = fopen(argv[2], "rb"); if (!f) { perror("kenar"); return 1; }
    uint64_t n2; if (fread(&n2, 8, 1, f) != 1 || n2 != N) { fprintf(stderr, "dugum/kenar sayisi uyusmuyor\n"); return 1; }
    for (uint64_t i = 0; i < N; i++) { uint32_t h[2]; if (fread(h, 4, 2, f) != 2) return 1; o[i] = K.size(); K.resize(K.size() + h[0] + h[1]);
      if (h[0] + h[1] && fread(&K[o[i]], 4, h[0] + h[1], f) != h[0] + h[1]) return 1; }
    o[N] = K.size(); fclose(f); }
  unordered_map<string, uint32_t> sira; sira.reserve(N * 2);
  for (uint64_t i = 0; i < N; i++) sira.emplace(ad[i], (uint32_t)i);
  vector<char> kut(N, 0);
  if (strcmp(argv[4], "-")) { FILE* f = fopen(argv[4], "r"); if (f) { char* b = nullptr; size_t c = 0; ssize_t n;
    while ((n = getline(&b, &c, f)) > 0) { while (n > 0 && (b[n - 1] == '\n' || b[n - 1] == '\r')) b[--n] = 0; auto it = sira.find(b); if (it != sira.end()) kut[it->second] = 1; } fclose(f); } }
  auto kt = sira.find(argv[3]); if (kt == sira.end()) { fprintf(stderr, "kok yok: %s\n", argv[3]); return 1; }
  uint32_t kok = kt->second;
  // her düğümün proje bağımlılıkları: kendinden önce gelen, kütüphanede olmayan, yinelenmeyen
  uint64_t atilan = 0;
  vector<vector<uint32_t>> B(N);
  vector<uint32_t> damga(N, UINT32_MAX);
  // koni: kökten erişilenler (azalan sırada tek geçiş yeter, çünkü kenarlar hep küçüğe gider)
  vector<char> C(N, 0); C[kok] = 1;
  for (int64_t v = kok; v >= 0; v--) { if (!C[v]) continue;
    for (uint64_t j = o[v]; j < o[v + 1]; j++) { uint32_t u = K[j]; if (kut[u]) continue; if (u >= (uint32_t)v) { if (u != (uint32_t)v) atilan++; continue; }
      if (damga[u] == (uint32_t)v) continue; damga[u] = v; B[v].push_back(u); C[u] = 1; } }
  vector<double> asagi(N, YOK), yukari(N, YOK);
  asagi[kok] = 0;
  for (int64_t v = kok; v >= 0; v--) { if (!C[v] || asagi[v] == YOK) continue; for (uint32_t u : B[v]) asagi[u] = lekle(asagi[u], asagi[v]); }
  uint64_t yaprak = 0, dugum = 0;
  for (uint64_t v = 0; v <= kok; v++) { if (!C[v]) continue; dugum++; if (B[v].empty()) { yukari[v] = 0; yaprak++; continue; } double t = YOK; for (uint32_t u : B[v]) t = lekle(t, yukari[u]); yukari[v] = t; }
  FILE* f = fopen(argv[5], "w"); if (!f) { perror("cikti"); return 1; }
  fprintf(f, "ad\tyol_payi\n");
  for (uint64_t v = 0; v <= kok; v++) if (C[v]) fprintf(f, "%s\t%.6f\n", ad[v].c_str(), exp(asagi[v] + yukari[v] - yukari[kok]));
  fclose(f);
  fprintf(stderr, "dugum %lu yaprak %lu atilan_kenar %lu log10(yol_sayisi) %.1f\n", (unsigned long)dugum, (unsigned long)yaprak, (unsigned long)atilan, yukari[kok] / log(10.0));
  return 0;
}

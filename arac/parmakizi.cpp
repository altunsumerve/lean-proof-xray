// Lean dışa aktarım (lean4export NDJSON) dosyasındaki bildirimlerin tip/değer ifadeleri için yapısal (Merkle) özet.
// Aynı ifade iki ayrı dışa aktarımda farklı numaralar alsa da aynı özeti verir.
// Kullanım: stdin'den NDJSON | exphash ozet.bin adlar.txt > cikti.tsv
//   adlar.txt: satır başına bir tam ad (boşsa/yoksa: tüm bildirimler)
//   çıktı: ad \t tür \t tip_özeti \t değer_özeti(teoremde '-')
#include <cstdio>
#include <cstdint>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <unordered_set>
#include <sys/mman.h>
#include <fcntl.h>
#include <unistd.h>
using namespace std;

static inline uint64_t mix(uint64_t h, uint64_t x) {
  h ^= x + 0x9e3779b97f4a7c15ULL + (h << 6) + (h >> 2);
  h *= 0xff51afd7ed558ccdULL; h ^= h >> 33;
  return h;
}
static uint64_t hs(const string& s) { uint64_t h = 1469598103934665603ULL; for (unsigned char c : s) { h ^= c; h *= 1099511628211ULL; } return h; }

vector<string> NM{""};       // ad kimliği -> tam ad
vector<uint64_t> LV;          // düzey kimliği -> özet
uint64_t* EX;                 // ifade kimliği -> özet (mmap)

// Basit JSON tarayıcı: anahtar -> ham değer metni (yalnızca bir düzey iç içe nesne yeter)
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
static vector<KV> obj(const char* p) { // p '{' üzerinde
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
static long num(const char* v) { return strtol(v, nullptr, 10); }
static vector<long> nums(const char* v, const char* e) { vector<long> r; for (const char* p = v; p < e; p++) if ((*p >= '0' && *p <= '9') && (p == v || !(p[-1] >= '0' && p[-1] <= '9'))) r.push_back(strtol(p, nullptr, 10)); return r; }
static uint64_t hname(long i) { return i >= 0 && (size_t)i < NM.size() ? hs(NM[i]) : 0; }
static uint64_t hlev(long i) { return i >= 0 && (size_t)i < LV.size() ? LV[i] : 0; }
static uint64_t hexp(long i) { return EX[i]; }

int main(int argc, char** argv) {
  if (argc < 3) { fprintf(stderr, "kullanim: exphash ozet.bin adlar.txt\n"); return 1; }
  uint64_t CAP = getenv("KUNYE_KAPASITE") ? strtoull(getenv("KUNYE_KAPASITE"), nullptr, 10) : 2100000000ULL;
  int fd = open(argv[1], O_RDWR | O_CREAT | O_TRUNC, 0644); if (ftruncate(fd, CAP * 8)) { perror("ft"); return 1; }
  EX = (uint64_t*)mmap(nullptr, CAP * 8, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
  unordered_set<string> ist; bool hepsi = true;
  if (FILE* f = fopen(argv[2], "r")) { char b[8192]; while (fgets(b, sizeof b, f)) { string s(b); while (!s.empty() && (s.back() == '\n' || s.back() == '\r')) s.pop_back(); if (!s.empty()) { ist.insert(s); hepsi = false; } } fclose(f); }
  LV.push_back(hs("zero"));
  char* buf = nullptr; size_t cap = 0; ssize_t n; uint64_t say = 0;
  while ((n = getline(&buf, &cap, stdin)) > 0) {
    auto top = obj(buf);
    if (top.empty()) continue;
    const string& k0 = top[0].k;
    if (k0 == "in") {
      long id = num(top[0].v); string full;
      for (auto& kv : top) if (kv.k == "str" || kv.k == "num") {
        auto o = obj(kv.v); long pre = 0; string part;
        for (auto& x : o) { if (x.k == "pre") pre = num(x.v); else if (x.k == "str") part = string(x.v + 1, x.e - x.v - 2); else if (x.k == "i") part = "#" + string(x.v, x.e - x.v); }  // sayı parçası: kapanis.cpp ile aynı biçim (`#0`)
        full = (pre > 0 && (size_t)pre < NM.size()) ? NM[pre] + "." + part : part;
      }
      if ((size_t)id >= NM.size()) NM.resize(id + 1); NM[id] = full;
    } else if (k0 == "il") {
      long id = num(top[0].v); uint64_t h = 0;
      for (auto& kv : top) {
        if (kv.k == "succ") h = mix(hs("succ"), hlev(num(kv.v)));
        else if (kv.k == "max" || kv.k == "imax") { auto v = nums(kv.v, kv.e); h = mix(mix(hs(kv.k), hlev(v.size() > 0 ? v[0] : -1)), hlev(v.size() > 1 ? v[1] : -1)); }
        else if (kv.k == "param") h = mix(hs("param"), hname(num(kv.v)));
      }
      if ((size_t)id >= LV.size()) LV.resize(id + 1); LV[id] = h;
    } else if (k0 == "ie" || (top.size() > 1 && top.back().k == "ie") || strstr(buf, "\"ie\":")) {
      long id = -1; for (auto& kv : top) if (kv.k == "ie") id = num(kv.v);
      if (id < 0 || (uint64_t)id >= CAP) continue;
      uint64_t h = 0;
      for (auto& kv : top) {
        if (kv.k == "ie") continue;
        if (kv.k == "bvar") h = mix(hs("bvar"), num(kv.v));
        else if (kv.k == "sort") h = mix(hs("sort"), hlev(num(kv.v)));
        else if (kv.k == "natVal") h = mix(hs("nat"), hs(string(kv.v, kv.e - kv.v)));
        else if (kv.k == "strVal") h = mix(hs("str"), hs(string(kv.v, kv.e - kv.v)));
        else {
          auto o = obj(kv.v); h = hs(kv.k);
          for (auto& x : o) {
            const string& f = x.k;
            if (f == "fn" || f == "arg" || f == "type" || f == "body" || f == "value" || f == "struct" || f == "expr" || f == "binderType") h = mix(mix(h, hs(f)), hexp(num(x.v)));
            else if (f == "name" || f == "declName" || f == "typeName") h = mix(mix(h, hs(f)), hname(num(x.v)));
            else if (f == "us") { for (long l : nums(x.v, x.e)) h = mix(h, hlev(l)); }
            else if (f == "binderName") {}  // bağlayıcı adları anlamı değiştirmez
            else h = mix(mix(h, hs(f)), hs(string(x.v, x.e - x.v)));  // binderInfo, idx, nondep, ...
          }
        }
      }
      EX[id] = h;
    } else {
      // bildirim satırı: {"thm":{...}} / {"def":{...}} / {"inductive":{...}} ...
      string tur = k0; auto o = obj(top[0].v);
      auto yaz = [&](vector<KV>& d, const string& t) {
        long nm = -1, ty = -1, va = -1; vector<long> lp;
        for (auto& x : d) { if (x.k == "name") nm = num(x.v); else if (x.k == "type") ty = num(x.v); else if (x.k == "value") va = num(x.v); else if (x.k == "levelParams") lp = nums(x.v, x.e); }
        if (nm < 0) return;
        const string& ad = NM[nm];
        if (!hepsi && !ist.count(ad)) return;
        uint64_t ht = ty >= 0 ? hexp(ty) : 0; ht = mix(ht, lp.size());
        printf("%s\t%s\t%016llx\t", ad.c_str(), t.c_str(), (unsigned long long)ht);
        if (t == "thm" || va < 0) printf("-\n"); else printf("%016llx\n", (unsigned long long)hexp(va));
        say++;
      };
      if (tur == "inductive") {
        // {"inductive":{"types":[{...}],"ctors":[{...}],...}}
        for (auto& x : o) if (x.k == "types" || x.k == "ctors" || x.k == "recs") {
          const char* p = x.v + 1;
          while (p < x.e && *p == '{') { auto d = obj(p); const char* q = skipv(p); yaz(d, x.k == "types" ? "ind" : x.k == "ctors" ? "ctor" : "rec"); p = q; while (p < x.e && (*p == ',' || *p == ' ')) p++; if (*p == '}') p++; while (p < x.e && (*p == ',' || *p == ' ')) p++; }
        }
      } else yaz(o, tur);
    }
  }
  fprintf(stderr, "ad %zu duzey %zu yazilan %llu\n", NM.size(), LV.size(), (unsigned long long)say);
  return 0;
}

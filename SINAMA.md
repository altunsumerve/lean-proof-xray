# Sınama sonuçları / Validation results

Kurallı üretildi (`arac/sinama_tablo.py`). "İsabet": aracın en ağır dediği k adımdan kaçı insan planında (blueprint) adı geçen sonuç; k = plandaki sonuç sayısı. "Bağ": plandaki "şu şuna dayanır" (`\uses`) iddialarından kaçı kayıtta da var. "Kesik": belgede boyut sınırı yüzünden eksik yazılan önerme sayısı. "Ana önerme" sütunu elle karşılaştırmadır.

| Proje | Proje bildirimi | İsabet (alt ağaç ağırlığı) | Rastgele beklenen | Bağ (doğrulanan / toplam) | Kesik | Ana önerme |
|---|---:|---:|---:|---:|---:|---|
| alpoge | 1270184 | — | — | — | 0 | — |
| carleson | 4974 | 94 / 213 (%44) | %11.7 | 202 / 209 | 0 | örtüşüyor (elle, 26 Kas) |
| fltregular | 426 | — | — | — | 0 | örtüşüyor (elle, 26 Kas) |
| grh300 | 50275 | — | — | — | 1 | — |
| grh76 | 37770 | — | — | — | 2 | — |
| pfr | 662 | 45 / 92 (%49) | %24.5 | 167 / 194 | 0 | örtüşüyor (elle, 25 Kas) |
| sphere | 1733 | 14 / 44 (%32) | %5.9 | 85 / 94 | 0 | örtüşüyor (elle, 26 Kas) |

## İkinci ölçü denemesi: yol payı / Second measure tried: path share

"Yol payı": kökten yapraklara giden bütün bağımlılık yollarının o bildirimden geçen kesri (`arac/yol.cpp`). Aşağıda aynı cevap anahtarıyla (blueprint) alt ağaç ağırlığıyla yan yana ölçülür. Sayılar `sinama/<ad>/BLUEPRINT.md` dosyalarından okunur.

| Proje | Alt ağaç ağırlığı | Yol payı | İkisinin iyisi |
|---|---:|---:|---:|
| carleson | 94 / 213 (%44) | 70 / 213 (%33) | 79 / 213 (%37) |
| pfr | 45 / 92 (%49) | 50 / 92 (%54) | 53 / 92 (%58) |
| sphere | 14 / 44 (%32) | 8 / 44 (%18) | 13 / 44 (%30) |

Sonuç: yol payı üç projenin birinde biraz daha iyi, ikisinde belirgin biçimde daha kötü. Bu yüzden belgelerdeki sıralama alt ağaç ağırlığıyla yapılır; yol payı yalnızca ek dosya olarak (`sinama/<ad>/yol_ust.tsv`) verilir.

## Basit ölçülerle kıyas / Comparison with simple measures

Aynı cevap anahtarı (blueprint), aynı k. "Rastgele" tek başına zayıf bir kıyastır; asıl soru, alt ağaç ağırlığının bir bildirimin yalnız kendi ispat boyu gibi en basit ölçülerden ne kadar iyi olduğudur. Sayılar `sinama/<ad>/BLUEPRINT.md` dosyalarından okunur; dosyada yoksa —. / Same answer key, same k. The question is how much better subtree weight is than the simplest measures.

| Ölçü / measure | carleson | pfr | sphere |
|---|---:|---:|---:|
| Alt ağaç ağırlığı (belgelerdeki sıralama) | 94 / 213 (%44) | 45 / 92 (%49) | 14 / 44 (%32) |
| Alt ağaçtaki bildirim sayısı | 93 / 213 (%44) | 38 / 92 (%41) | 17 / 44 (%39) |
| Yalnız kendi ispatının boyu | 76 / 213 (%36) | 38 / 92 (%41) | 10 / 44 (%23) |
| Doğrudan kullanan sayısı | 19 / 213 (%9) | 33 / 92 (%36) | 1 / 44 (%2) |
| Ağırlık ÷ önerme boyu | 72 / 213 (%34) | 41 / 92 (%45) | 13 / 44 (%30) |
| Köke yakınlık | 26 / 213 (%12) | 24 / 92 (%26) | 7 / 44 (%16) |
| Alt ağaç ağırlığı, tek çocuklu zincirler tek adım sayılınca | 102 / 210 (%49) | 44 / 84 (%52) | 16 / 44 (%36) |
| Rastgele beklenen | %11.7 | %24.5 | %5.9 |

Alt ağaç ağırlığının farkı (yüzde puanı): yalnız kendi ispat boyuna göre carleson +8, pfr +8, sphere +9; ağırlıksız düz sayıma göre carleson +0, pfr +8, sphere -7. Üç proje küçük bir örneklemdir; bu tablo ağırlığın "önem" ölçtüğünü göstermez, yalnız insan planıyla ne kadar örtüştüğünü sayar. / Difference of subtree weight in percentage points against own proof size and against plain subtree count. Three projects are a small sample.

## Aynı teoremin üç sürümü / Three versions of the same theorem

Kök hepsinde `riemannHypothesis`. Sayılar bu depodaki `ozet.json`, `bos_tum.tsv`, `VARSAYIM_tr.md`, `taslar_ust.tsv`, `import_tara.txt` dosyalarından okunur; dosya yoksa —.

| | 17 milyon satır (Alpöge, 20 Kas) | ≈300 bin satır (grh) | ≈76 bin satır (grh-compact) |
|---|---:|---:|---:|
| İspattaki proje bildirimi | 1.265.256 | 49.815 | 37.561 |
| — teorem | 1.075.015 | 42.204 | 30.418 |
| — tanım | 178.298 | 6.598 | 6.598 |
| Ana önermede proje tanımı | 0 | 0 | 0 |
| İspat konisindeki aksiyom | 3 (standart dışı: yok) | 3 (standart dışı: yok) | 3 (standart dışı: yok) |
| Bütün kayıtta gövdesi `True` olan tanım | 10 | 0 | 0 |
| Varsayım olarak taşınan adlandırılmış önerme | 738 | 0 | 0 |
| `star_inequality` payı | — | %93,8 | %93,4 |
| `integral_forms_long` payı | — | %55,7 | %20,2 |
| `enough_forms` payı | — | %1,7 | %0,0 |
| `span_short_integralRamified_eq_top` payı | — | %0,2 | — |
| Lib → New içe aktarma yolu | — | Lib -> New yolu YOK | Lib -> New yolu YOK |

Yazarın kılavuzu (`grh/GUIDE.md`) üç ana teoremi (A: `span_short_integralRamified_eq_top`, B: `enough_forms`, C: `integral_forms_long`) ve bunları birleştiren `star_inequality`'yi adıyla sayar. Araç aynı adları, kılavuzu okumadan, baskınlık ağacının tepesinde bulur; yüzdeleri kılavuz vermez, araç ekler. Kılavuzun "`Lib`, `New`'den hiçbir şey kullanmaz" iddiası `arac/import_tara.py` ile dosya düzeyinde denetlenir.

## Araç içi denetimler / Internal checks

| Denetim | Sonuç |
|---|---|
| Baskınlık ağacı ve alt ağaç toplamları tanımdan kaba kuvvetle hesaplananla aynı mı (rastgele grafikler, döngülü olanlar dahil) | evet (`test/grafik_test.py`) |
| Aksiyom listesi ve "nerede kuruluyor" sınıfları elle hesaplanmış küçük kayıtla aynı mı | evet (`test/grafik_test.py`) |
| İki farklı önerme aynı cümleye çevriliyor mu (rastgele 60.000 iskelet) | çakışma yok (`test/duz_test.py`) |
| Fonksiyon tipi ve nesne argümanı "eğer–ise" diye yazılıyor mu | hayır (`test/duz_test.py`) |
| Aynı girdi aynı belgeyi veriyor mu | evet (`test/uctan_uca.sh` her belgeyi iki kez üretip bayt bayt karşılaştırır) |

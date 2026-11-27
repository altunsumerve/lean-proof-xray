# Blueprint karşılaştırması / Blueprint comparison

Cevap anahtarı: projenin elle yazılmış blueprint'i. Araç: kayıttan (lean4export) hesaplanan bağımlılık grafiği ve baskınlık ağacı. / Answer key: the project's hand-written blueprint. Tool: dependency graph and dominator tree computed from the export.

## 1. Blueprint adları kodda var mı / Are the blueprint's names in the code

| | Sayı / Count |
|---|---:|
| Blueprint öğesi / items | 0 |
| `\lean{}` taşıyan öğe / items with a Lean name | 0 |
| Farklı Lean adı / distinct Lean names | 0 |
| Kayıtta bulunan / found in the export | 0 |
| Kökün ispat konisinde (proje bildirimi) / in the root's proof cone | 0 |

## 2. Kilometre taşı sıralaması insan seçimini buluyor mu / Do milestone rankings recover the human choice

Aday: konideki yardımcı olmayan proje teoremleri (8841). Hedef: bunlardan blueprint'te adı geçenler (0). Rastgele seçimde beklenen isabet: 0.0%. / Candidates: non-auxiliary project theorems in the cone. Target: those named in the blueprint.

| Ölçüt / criterion | İlk k'da isabet (k = hedef sayısı) / hits in top k | İlk 2k'da / in top 2k | Hedeflerin ortanca sırası / median rank of targets |
|---|---:|---:|---:|
| alt ağaç ağırlığı / subtree weight | 0 / 0 (0%) | 0 / 0 (0%) | 0 / 8841 |
| alt ağaç bildirim sayısı / subtree count | 0 / 0 (0%) | 0 / 0 (0%) | 0 / 8841 |
| kendi ispat ağırlığı / own proof weight | 0 / 0 (0%) | 0 / 0 (0%) | 0 / 8841 |
| doğrudan kullanan sayısı / direct users | 0 / 0 (0%) | 0 / 0 (0%) | 0 / 8841 |
| ağırlık ÷ önerme boyu / weight per statement size | 0 / 0 (0%) | 0 / 0 (0%) | 0 / 8841 |
| ağaçta sığlık (köke yakınlık) / shallowness | 0 / 0 (0%) | 0 / 0 (0%) | 0 / 8841 |
| yol payı (köke giden yolların geçen kesri) / path share | 0 / 0 (0%) | 0 / 0 (0%) | 0 / 8841 |
| ağırlık ile yol payının iyisi / better of weight and path share | 0 / 0 (0%) | 0 / 0 (0%) | 0 / 8841 |
| alt ağaç ağırlığı, zincirler tek adım / subtree weight, chains as one step | 0 / 0 (0%) | 0 / 0 (0%) | 0 / 8793 |

Son satır: baskınlık ağacında tek çocuğu olan bir adım ile o çocuk tek adım sayılır (8841 aday 8793 zincir eder; rastgele beklenen 0.0%). / Last row: a step with exactly one child in the dominator tree is merged with that child.

Yapısal seçim kuralları: kuralın seçtiği adaylardan kaçı blueprint'te (kesinlik), blueprint teoremlerinin kaçı seçildi (kapsama). / Structural selection rules: precision = selected candidates that are in the blueprint, recall = blueprint theorems selected.

| Kural / rule | Seçilen / selected | Kesinlik / precision | Kapsama / recall |
|---|---:|---:|---:|
| ağaçta çocuğu olan / has children in the tree | 4351 | 0% | 0% |
| yardımcı olmayan çocuğu olan / has a non-auxiliary child | 830 | 0% | 0% |
| en az 2 yerde kullanılan / used in at least 2 places | 7326 | 0% | 0% |
| çocuğu olan VEYA ≥2 yerde kullanılan / children or ≥2 users | 7703 | 0% | 0% |
| alt ağaç ağırlığı ≥ %0,5 / subtree weight ≥ 0.5% | 87 | 0% | 0% |
| ağırlık ≥ %0,5 VEYA ≥2 yerde kullanılan / weight ≥ 0.5% or ≥2 users | 7390 | 0% | 0% |
| hepsi (her aday) / everything | 8841 | 0% | 0% |

Ağırlık sıralamasının en geride bıraktığı blueprint teoremleri / blueprint theorems ranked lowest by weight:


Ağırlık sıralamasında en üstte olup blueprint'te olmayan teoremler / top-ranked theorems not in the blueprint:

- `New.grh` — sıra 1, alt=37555, kullanan=1, üstü=`riemannHypothesis`
- `eventually_primeError_le_rpow` — sıra 2, alt=37276, kullanan=1, üstü=`New.grh`
- `star_inequality` — sıra 3, alt=32541, kullanan=1, üstü=`eventually_primeError_le_rpow`
- `Data.integral_forms_long` — sıra 4, alt=5913, kullanan=1, üstü=`star_inequality`
- `sphericalCompat_of_odd` — sıra 5, alt=6179, kullanan=2, üstü=`star_inequality`
- `sphericalCompat_of_split` — sıra 6, alt=6161, kullanan=1, üstü=`sphericalCompat_of_odd`
- `exists_rep_of_cuspidal_type` — sıra 7, alt=6004, kullanan=1, üstü=`sphericalCompat_of_split`
- `exists_isFitFamily` — sıra 8, alt=3591, kullanan=1, üstü=`Data.integral_forms_long`
- `Model.exists_galois_rep` — sıra 9, alt=3289, kullanan=1, üstü=`exists_rep_of_cuspidal_type`
- `Data.exists_family_covolumeSq_le` — sıra 10, alt=2196, kullanan=1, üstü=`star_inequality`
- `denominatorLe_rowBudget` — sıra 11, alt=2104, kullanan=1, üstü=`exists_isFitFamily`
- `Data.ramifiedColumns_fill_rows` — sıra 12, alt=1440, kullanan=2, üstü=`star_inequality`
- `Filling.Fits.exists_translate_finrank_comap_le` — sıra 13, alt=1391, kullanan=1, üstü=`Data.ramifiedColumns_fill_rows`
- `ribet_columns` — sıra 14, alt=1644, kullanan=1, üstü=`denominatorLe_rowBudget`
- `Data.heightLe_volume_ratio_sq` — sıra 15, alt=1362, kullanan=1, üstü=`Data.integral_forms_long`
- `Data.heightLe_liftVolume_ratio` — sıra 16, alt=1358, kullanan=1, üstü=`Data.heightLe_volume_ratio_sq`
- `Data.seesaw` — sıra 17, alt=978, kullanan=4, üstü=`Data.exists_family_covolumeSq_le`
- `sum_blockLoss_le` — sıra 18, alt=1486, kullanan=1, üstü=`ribet_columns`
- `exchange_theorem` — sıra 19, alt=930, kullanan=2, üstü=`star_inequality`
- `Data.short_forms` — sıra 20, alt=1087, kullanan=1, üstü=`Data.exists_family_covolumeSq_le`

## 3. `\uses` iddiaları kodla doğrulanıyor mu / Are the `\uses` claims confirmed by the code

Blueprint "A, B'yi kullanır" diyorsa, kodda A'nın bildirimi B'nin bildirimine (doğrudan ya da dolaylı) dayanmalı. / If the blueprint says A uses B, A's declaration must depend on B's in the code.

| | Sayı / Count |
|---|---:|
| Doğrulanan `\uses` / confirmed | 0 |
| **Kodda karşılığı olmayan `\uses` / not backed by the code** | **0** |
| Ölçülemeyen (iki uçtan biri Lean adı taşımıyor) / not measurable | 0 |
| Kodda olan blueprint düzeyi doğrudan bağımlılık / blueprint-level direct dependencies in the code | 0 |
| &nbsp;&nbsp;blueprint'te yazılmamış olanlar / of which missing from the blueprint | 0 |


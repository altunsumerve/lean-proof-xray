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

Aday: konideki yardımcı olmayan proje teoremleri (19851). Hedef: bunlardan blueprint'te adı geçenler (0). Rastgele seçimde beklenen isabet: 0.0%. / Candidates: non-auxiliary project theorems in the cone. Target: those named in the blueprint.

| Ölçüt / criterion | İlk k'da isabet (k = hedef sayısı) / hits in top k | İlk 2k'da / in top 2k | Hedeflerin ortanca sırası / median rank of targets |
|---|---:|---:|---:|
| alt ağaç ağırlığı / subtree weight | 0 / 0 (0%) | 0 / 0 (0%) | 0 / 19851 |
| alt ağaç bildirim sayısı / subtree count | 0 / 0 (0%) | 0 / 0 (0%) | 0 / 19851 |
| kendi ispat ağırlığı / own proof weight | 0 / 0 (0%) | 0 / 0 (0%) | 0 / 19851 |
| doğrudan kullanan sayısı / direct users | 0 / 0 (0%) | 0 / 0 (0%) | 0 / 19851 |
| ağırlık ÷ önerme boyu / weight per statement size | 0 / 0 (0%) | 0 / 0 (0%) | 0 / 19851 |
| ağaçta sığlık (köke yakınlık) / shallowness | 0 / 0 (0%) | 0 / 0 (0%) | 0 / 19851 |
| yol payı (köke giden yolların geçen kesri) / path share | 0 / 0 (0%) | 0 / 0 (0%) | 0 / 19851 |
| ağırlık ile yol payının iyisi / better of weight and path share | 0 / 0 (0%) | 0 / 0 (0%) | 0 / 19851 |
| alt ağaç ağırlığı, zincirler tek adım / subtree weight, chains as one step | 0 / 0 (0%) | 0 / 0 (0%) | 0 / 18598 |

Son satır: baskınlık ağacında tek çocuğu olan bir adım ile o çocuk tek adım sayılır (19851 aday 18598 zincir eder; rastgele beklenen 0.0%). / Last row: a step with exactly one child in the dominator tree is merged with that child.

Yapısal seçim kuralları: kuralın seçtiği adaylardan kaçı blueprint'te (kesinlik), blueprint teoremlerinin kaçı seçildi (kapsama). / Structural selection rules: precision = selected candidates that are in the blueprint, recall = blueprint theorems selected.

| Kural / rule | Seçilen / selected | Kesinlik / precision | Kapsama / recall |
|---|---:|---:|---:|
| ağaçta çocuğu olan / has children in the tree | 8661 | 0% | 0% |
| yardımcı olmayan çocuğu olan / has a non-auxiliary child | 4197 | 0% | 0% |
| en az 2 yerde kullanılan / used in at least 2 places | 11377 | 0% | 0% |
| çocuğu olan VEYA ≥2 yerde kullanılan / children or ≥2 users | 14105 | 0% | 0% |
| alt ağaç ağırlığı ≥ %0,5 / subtree weight ≥ 0.5% | 138 | 0% | 0% |
| ağırlık ≥ %0,5 VEYA ≥2 yerde kullanılan / weight ≥ 0.5% or ≥2 users | 11489 | 0% | 0% |
| hepsi (her aday) / everything | 19851 | 0% | 0% |

Ağırlık sıralamasının en geride bıraktığı blueprint teoremleri / blueprint theorems ranked lowest by weight:


Ağırlık sıralamasında en üstte olup blueprint'te olmayan teoremler / top-ranked theorems not in the blueprint:

- `New.grh` — sıra 1, alt=49807, kullanan=1, üstü=`riemannHypothesis`
- `New.eventually_primeRemainder_le_rpow` — sıra 2, alt=49589, kullanan=1, üstü=`New.grh`
- `New.eventually_primeRemainder_natCast_le` — sıra 3, alt=49556, kullanan=1, üstü=`New.eventually_primeRemainder_le_rpow`
- `New.Data.primeRemainder_le` — sıra 4, alt=44867, kullanan=1, üstü=`New.eventually_primeRemainder_natCast_le`
- `New.star_inequality` — sıra 5, alt=44766, kullanan=1, üstü=`New.Data.primeRemainder_le`
- `New.Data.integral_forms_long` — sıra 6, alt=23157, kullanan=1, üstü=`New.star_inequality`
- `New.Data.exists_hasSmallRatios_heightLe_liftDeterminant_div` — sıra 7, alt=18953, kullanan=1, üstü=`New.Data.integral_forms_long`
- `New.exists_isRegularFamily` — sıra 8, alt=16098, kullanan=1, üstü=`New.Data.exists_hasSmallRatios_heightLe_liftDeterminant_div`
- `New.Selmer.exists_mFoldTwist_hasDenominatorsLe` — sıra 9, alt=15519, kullanan=1, üstü=`New.exists_isRegularFamily`
- `New.GaloisRep.sphericalCompat_of_odd` — sıra 10, alt=6898, kullanan=2, üstü=`New.Selmer.exists_mFoldTwist_hasDenominatorsLe`
- `New.GaloisRep.sphericalCompat_of_split` — sıra 11, alt=6881, kullanan=1, üstü=`New.GaloisRep.sphericalCompat_of_odd`
- `New.GaloisRep.exists_rep_of_cuspidal_type` — sıra 12, alt=6706, kullanan=1, üstü=`_private.Lib.GaloisRep.Main.SplitCase.#0.New.GaloisRep.exists_rep_of_free_weight`
- `New.Variety.Model.exists_galois_rep` — sıra 13, alt=3600, kullanan=1, üstü=`_private.Lib.GaloisRep.Main.SeedRepresentation.#0.New.GaloisRep.exists_padicRep_of_pel`
- `New.Selmer.denominatorLe_clearingBound` — sıra 14, alt=3227, kullanan=2, üstü=`New.Selmer.exists_mFoldTwist_hasDenominatorsLe`
- `New.Selmer.exists_operator_det_clearingBound` — sıra 15, alt=3226, kullanan=1, üstü=`New.Selmer.denominatorLe_clearingBound`
- `New.Selmer.exists_operator_ellVal_le_liftValuationBound` — sıra 16, alt=3210, kullanan=1, üstü=`New.Selmer.exists_operator_det_clearingBound`
- `New.Selmer.exists_linearMap_eq_smul_mem_integralForms` — sıra 17, alt=3198, kullanan=1, üstü=`New.Selmer.exists_operator_ellVal_le_liftValuationBound`
- `New.Selmer.exists_ellVal_le_and_diagOp_mem_ellIntegralForms` — sıra 18, alt=2942, kullanan=1, üstü=`New.Selmer.exists_linearMap_eq_smul_mem_integralForms`
- `New.Data.heightLe_liftDeterminant_ratio` — sıra 19, alt=2222, kullanan=1, üstü=`New.Data.exists_hasSmallRatios_heightLe_liftDeterminant_div`
- `New.Selmer.exists_isCommonRibetElement_ellVal_le` — sıra 20, alt=2357, kullanan=1, üstü=`New.Selmer.exists_ellVal_le_and_diagOp_mem_ellIntegralForms`

## 3. `\uses` iddiaları kodla doğrulanıyor mu / Are the `\uses` claims confirmed by the code

Blueprint "A, B'yi kullanır" diyorsa, kodda A'nın bildirimi B'nin bildirimine (doğrudan ya da dolaylı) dayanmalı. / If the blueprint says A uses B, A's declaration must depend on B's in the code.

| | Sayı / Count |
|---|---:|
| Doğrulanan `\uses` / confirmed | 0 |
| **Kodda karşılığı olmayan `\uses` / not backed by the code** | **0** |
| Ölçülemeyen (iki uçtan biri Lean adı taşımıyor) / not measurable | 0 |
| Kodda olan blueprint düzeyi doğrudan bağımlılık / blueprint-level direct dependencies in the code | 0 |
| &nbsp;&nbsp;blueprint'te yazılmamış olanlar / of which missing from the blueprint | 0 |


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

Aday: konideki yardımcı olmayan proje teoremleri (181). Hedef: bunlardan blueprint'te adı geçenler (0). Rastgele seçimde beklenen isabet: 0.0%. / Candidates: non-auxiliary project theorems in the cone. Target: those named in the blueprint.

| Ölçüt / criterion | İlk k'da isabet (k = hedef sayısı) / hits in top k | İlk 2k'da / in top 2k | Hedeflerin ortanca sırası / median rank of targets |
|---|---:|---:|---:|
| alt ağaç ağırlığı / subtree weight | 0 / 0 (0%) | 0 / 0 (0%) | 0 / 181 |
| alt ağaç bildirim sayısı / subtree count | 0 / 0 (0%) | 0 / 0 (0%) | 0 / 181 |
| kendi ispat ağırlığı / own proof weight | 0 / 0 (0%) | 0 / 0 (0%) | 0 / 181 |
| doğrudan kullanan sayısı / direct users | 0 / 0 (0%) | 0 / 0 (0%) | 0 / 181 |
| ağırlık ÷ önerme boyu / weight per statement size | 0 / 0 (0%) | 0 / 0 (0%) | 0 / 181 |
| ağaçta sığlık (köke yakınlık) / shallowness | 0 / 0 (0%) | 0 / 0 (0%) | 0 / 181 |

Yapısal seçim kuralları: kuralın seçtiği adaylardan kaçı blueprint'te (kesinlik), blueprint teoremlerinin kaçı seçildi (kapsama). / Structural selection rules: precision = selected candidates that are in the blueprint, recall = blueprint theorems selected.

| Kural / rule | Seçilen / selected | Kesinlik / precision | Kapsama / recall |
|---|---:|---:|---:|
| ağaçta çocuğu olan / has children in the tree | 104 | 0% | 0% |
| yardımcı olmayan çocuğu olan / has a non-auxiliary child | 82 | 0% | 0% |
| en az 2 yerde kullanılan / used in at least 2 places | 46 | 0% | 0% |
| çocuğu olan VEYA ≥2 yerde kullanılan / children or ≥2 users | 112 | 0% | 0% |
| alt ağaç ağırlığı ≥ %0,5 / subtree weight ≥ 0.5% | 91 | 0% | 0% |
| ağırlık ≥ %0,5 VEYA ≥2 yerde kullanılan / weight ≥ 0.5% or ≥2 users | 125 | 0% | 0% |
| hepsi (her aday) / everything | 181 | 0% | 0% |

Ağırlık sıralamasının en geride bıraktığı blueprint teoremleri / blueprint theorems ranked lowest by weight:


Ağırlık sıralamasında en üstte olup blueprint'te olmayan teoremler / top-ranked theorems not in the blueprint:

- `FltRegular.caseII` — sıra 1, alt=345, kullanan=1, üstü=`flt_regular`
- `FltRegular.not_exists_Int_solution'` — sıra 2, alt=340, kullanan=1, üstü=`FltRegular.caseII`
- `FltRegular.not_exists_Int_solution` — sıra 3, alt=339, kullanan=1, üstü=`FltRegular.not_exists_Int_solution'`
- `FltRegular.not_exists_solution'` — sıra 4, alt=338, kullanan=1, üstü=`FltRegular.not_exists_Int_solution`
- `FltRegular.not_exists_solution` — sıra 5, alt=337, kullanan=1, üstü=`FltRegular.not_exists_solution'`
- `exists_solution'` — sıra 6, alt=283, kullanan=1, üstü=`FltRegular.not_exists_solution`
- `eq_pow_prime_of_unit_of_congruent` — sıra 7, alt=249, kullanan=1, üstü=`exists_solution'`
- `exists_pow_eq_of_zeta_sub_one_pow_dvd_sub_one` — sıra 8, alt=242, kullanan=1, üstü=`eq_pow_prime_of_unit_of_congruent`
- `dvd_card_classGroup_of_unramified_isCyclic` — sıra 9, alt=208, kullanan=1, üstü=`exists_pow_eq_of_zeta_sub_one_pow_dvd_sub_one`
- `exists_not_isPrincipal_and_isPrincipal_map` — sıra 10, alt=206, kullanan=1, üstü=`dvd_card_classGroup_of_unramified_isCyclic`
- `Hilbert92` — sıra 11, alt=196, kullanan=1, üstü=`exists_not_isPrincipal_and_isPrincipal_map`
- `almostHilbert92` — sıra 12, alt=195, kullanan=1, üstü=`Hilbert92`
- `FltRegular.caseI` — sıra 13, alt=70, kullanan=1, üstü=`flt_regular`
- `KummersLemma.isUnramified` — sıra 14, alt=33, kullanan=1, üstü=`exists_pow_eq_of_zeta_sub_one_pow_dvd_sub_one`
- `FltRegular.caseI_easier` — sıra 15, alt=48, kullanan=1, üstü=`FltRegular.caseI`
- `exists_solution` — sıra 16, alt=31, kullanan=1, üstü=`exists_solution'`
- `FltRegular.ex_fin_div` — sıra 17, alt=33, kullanan=1, üstü=`FltRegular.caseI_easier`
- `exists_not_isPrincipal_and_isPrincipal_map_aux` — sıra 18, alt=9, kullanan=1, üstü=`exists_not_isPrincipal_and_isPrincipal_map`
- `lh_pow_free` — sıra 19, alt=13, kullanan=1, üstü=`almostHilbert92`
- `lh_pow_free'` — sıra 20, alt=11, kullanan=1, üstü=`lh_pow_free`

## 3. `\uses` iddiaları kodla doğrulanıyor mu / Are the `\uses` claims confirmed by the code

Blueprint "A, B'yi kullanır" diyorsa, kodda A'nın bildirimi B'nin bildirimine (doğrudan ya da dolaylı) dayanmalı. / If the blueprint says A uses B, A's declaration must depend on B's in the code.

| | Sayı / Count |
|---|---:|
| Doğrulanan `\uses` / confirmed | 0 |
| **Kodda karşılığı olmayan `\uses` / not backed by the code** | **0** |
| Ölçülemeyen (iki uçtan biri Lean adı taşımıyor) / not measurable | 0 |
| Kodda olan blueprint düzeyi doğrudan bağımlılık / blueprint-level direct dependencies in the code | 0 |
| &nbsp;&nbsp;blueprint'te yazılmamış olanlar / of which missing from the blueprint | 0 |


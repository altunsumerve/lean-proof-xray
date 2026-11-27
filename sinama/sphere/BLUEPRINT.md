# Blueprint karşılaştırması / Blueprint comparison

Cevap anahtarı: projenin elle yazılmış blueprint'i. Araç: kayıttan (lean4export) hesaplanan bağımlılık grafiği ve baskınlık ağacı. / Answer key: the project's hand-written blueprint. Tool: dependency graph and dominator tree computed from the export.

## 1. Blueprint adları kodda var mı / Are the blueprint's names in the code

| | Sayı / Count |
|---|---:|
| Blueprint öğesi / items | 73 |
| `\lean{}` taşıyan öğe / items with a Lean name | 73 |
| Farklı Lean adı / distinct Lean names | 90 |
| Kayıtta bulunan / found in the export | 85 |
| Kökün ispat konisinde (proje bildirimi) / in the root's proof cone | 75 |

Kayıtta olmayan adlar (5; kök bunları kullanmıyor ya da ad değişmiş): `immersionRel_open_ample`, `loc_immersion_rel_ample`, `loc_immersion_rel_open`, `satisfied_or_refund`, `sphere_eversion_of_loc`

## 2. Kilometre taşı sıralaması insan seçimini buluyor mu / Do milestone rankings recover the human choice

Aday: konideki yardımcı olmayan proje teoremleri (741). Hedef: bunlardan blueprint'te adı geçenler (44). Rastgele seçimde beklenen isabet: 5.9%. / Candidates: non-auxiliary project theorems in the cone. Target: those named in the blueprint.

| Ölçüt / criterion | İlk k'da isabet (k = hedef sayısı) / hits in top k | İlk 2k'da / in top 2k | Hedeflerin ortanca sırası / median rank of targets |
|---|---:|---:|---:|
| alt ağaç ağırlığı / subtree weight | 14 / 44 (32%) | 23 / 44 (52%) | 86 / 741 |
| alt ağaç bildirim sayısı / subtree count | 17 / 44 (39%) | 23 / 44 (52%) | 76 / 741 |
| kendi ispat ağırlığı / own proof weight | 10 / 44 (23%) | 22 / 44 (50%) | 101 / 741 |
| doğrudan kullanan sayısı / direct users | 1 / 44 (2%) | 5 / 44 (11%) | 349 / 741 |
| ağırlık ÷ önerme boyu / weight per statement size | 13 / 44 (30%) | 20 / 44 (45%) | 112 / 741 |
| ağaçta sığlık (köke yakınlık) / shallowness | 7 / 44 (16%) | 10 / 44 (23%) | 260 / 741 |
| yol payı (köke giden yolların geçen kesri) / path share | 8 / 44 (18%) | 11 / 44 (25%) | 235 / 741 |
| ağırlık ile yol payının iyisi / better of weight and path share | 13 / 44 (30%) | 21 / 44 (48%) | 125 / 741 |
| alt ağaç ağırlığı, zincirler tek adım / subtree weight, chains as one step | 16 / 44 (36%) | 24 / 44 (55%) | 78 / 625 |

Son satır: baskınlık ağacında tek çocuğu olan bir adım ile o çocuk tek adım sayılır (741 aday 625 zincir eder; rastgele beklenen 7.0%). / Last row: a step with exactly one child in the dominator tree is merged with that child.

Yapısal seçim kuralları: kuralın seçtiği adaylardan kaçı blueprint'te (kesinlik), blueprint teoremlerinin kaçı seçildi (kapsama). / Structural selection rules: precision = selected candidates that are in the blueprint, recall = blueprint theorems selected.

| Kural / rule | Seçilen / selected | Kesinlik / precision | Kapsama / recall |
|---|---:|---:|---:|
| ağaçta çocuğu olan / has children in the tree | 300 | 13% | 86% |
| yardımcı olmayan çocuğu olan / has a non-auxiliary child | 228 | 15% | 80% |
| en az 2 yerde kullanılan / used in at least 2 places | 278 | 6% | 36% |
| çocuğu olan VEYA ≥2 yerde kullanılan / children or ≥2 users | 445 | 9% | 89% |
| alt ağaç ağırlığı ≥ %0,5 / subtree weight ≥ 0.5% | 76 | 26% | 45% |
| ağırlık ≥ %0,5 VEYA ≥2 yerde kullanılan / weight ≥ 0.5% or ≥2 users | 330 | 9% | 66% |
| hepsi (her aday) / everything | 741 | 6% | 100% |

Ağırlık sıralamasının en geride bıraktığı blueprint teoremleri / blueprint theorems ranked lowest by weight:

- `mem_slice` — sıra 562, alt=1, kullanan=5, önerme boyu=1297, ispat ağırlığı=76
- `DualPair.update_v` — sıra 450, alt=1, kullanan=4, önerme boyu=227, ispat ağırlığı=158
- `ContMDiff.oneJetExt` — sıra 448, alt=1, kullanan=3, önerme boyu=1342, ispat ağırlığı=159
- `OneJetSec.isHolonomicAt_iff` — sıra 428, alt=3, kullanan=1, önerme boyu=528, ispat ağırlığı=182
- `DualPair.update_ker_pi` — sıra 316, alt=1, kullanan=5, önerme boyu=339, ispat ağırlığı=363
- `StepLandscape.improveStep_rel_t_eq_0` — sıra 275, alt=2, kullanan=1, önerme boyu=288, ispat ağırlığı=442
- `corrugation.support` — sıra 254, alt=4, kullanan=1, önerme boyu=209, ispat ağırlığı=103
- `StepLandscape.improveStep_rel_compl_K₁` — sıra 230, alt=2, kullanan=4, önerme boyu=489, ispat ağırlığı=732
- `OneJetSec.localize_mem_iff` — sıra 225, alt=2, kullanan=1, önerme boyu=1247, ispat ağırlığı=648
- `remainder_c0_small_on` — sıra 214, alt=3, kullanan=2, önerme boyu=577, ispat ağırlığı=692
- `SmoothSurroundingFamily.reparametrize_average` — sıra 199, alt=17, kullanan=1, önerme boyu=169, ispat ağırlığı=386
- `LocallyFinite.exists_forall_eventually_of_indexType` — sıra 184, alt=3, kullanan=1, önerme boyu=175, ispat ağırlığı=616
- `StepLandscape.improveStep_c0_close` — sıra 173, alt=2, kullanan=1, önerme boyu=353, ispat ağırlığı=1215
- `localisation_stability` — sıra 131, alt=4, kullanan=4, önerme boyu=522, ispat ağırlığı=2009
- `smooth_surrounding` — sıra 121, alt=1, kullanan=1, önerme boyu=954, ispat ağırlığı=2537
- `fderiv_corrugated_map` — sıra 109, alt=6, kullanan=1, önerme boyu=1225, ispat ağırlığı=682
- `OpenSmoothEmbedding.contMDiff_update` — sıra 104, alt=2, kullanan=1, önerme boyu=762, ispat ağırlığı=2098
- `exists_locallyFinite_subcover_of_locally` — sıra 103, alt=5, kullanan=2, önerme boyu=273, ispat ağırlığı=2442
- `FamilyOneJetSec.isHolonomicAt_uncurry` — sıra 100, alt=5, kullanan=1, önerme boyu=819, ispat ağırlığı=2186
- `corrugation.c0_small_on` — sıra 99, alt=30, kullanan=3, önerme boyu=438, ispat ağırlığı=1060

Ağırlık sıralamasında en üstte olup blueprint'te olmayan teoremler / top-ranked theorems not in the blueprint:

- `immersionRel_satisfiesHPrincipleWith` — sıra 2, alt=1420, kullanan=1, üstü=`sphere_eversion`
- `RelMfld.Ample.satisfiesHPrinciple` — sıra 4, alt=1274, kullanan=1, üstü=`RelMfld.Ample.satisfiesHPrincipleWith`
- `OpenSmoothEmbedding.improve_formalSol` — sıra 5, alt=1058, kullanan=1, üstü=`RelMfld.Ample.satisfiesHPrinciple`
- `RelLoc.FormalSol.improve_htpy'` — sıra 6, alt=836, kullanan=1, üstü=`OpenSmoothEmbedding.improve_formalSol`
- `exist_loops_aux2` — sıra 9, alt=251, kullanan=1, üstü=`exist_loops`
- `exists_stability_dist` — sıra 11, alt=78, kullanan=1, üstü=`RelMfld.Ample.satisfiesHPrinciple`
- `SmoothSurroundingFamily.exists_smooth_isCenteringDensity` — sıra 15, alt=83, kullanan=3, üstü=`exist_loops`
- `nice_atlas'` — sıra 16, alt=40, kullanan=1, üstü=`nice_atlas`
- `SmoothSurroundingFamily.reparametrize_smooth` — sıra 17, alt=45, kullanan=2, üstü=`exist_loops`
- `contDiff_parametric_symm_of_deriv_pos` — sıra 18, alt=43, kullanan=1, üstü=`SmoothSurroundingFamily.reparametrize_smooth`
- `contDiff_parametric_symm` — sıra 19, alt=38, kullanan=1, üstü=`contDiff_parametric_symm_of_deriv_pos`
- `Orientation.isometry_rot` — sıra 20, alt=10, kullanan=1, üstü=`formalEversionAux2._proof_1`
- `relativize_slice` — sıra 22, alt=4, kullanan=1, üstü=`RelMfld.Ample.relativize`
- `Orientation.isometry_on_rot` — sıra 24, alt=4, kullanan=1, üstü=`Orientation.isometry_rot`
- `ChartPair.mkHtpy_isHolonomicAt_iff` — sıra 25, alt=10, kullanan=1, üstü=`OpenSmoothEmbedding.improve_formalSol`
- `ChartPair.dist_update'` — sıra 26, alt=2, kullanan=1, üstü=`OpenSmoothEmbedding.improve_formalSol`
- `hasFDerivAt_parametric_primitive_of_contDiff'` — sıra 27, alt=11, kullanan=3, üstü=`RelLoc.FormalSol.improve`
- `formalEversion_hol_near_zero_one` — sıra 29, alt=8, kullanan=1, üstü=`sphere_eversion`
- `Orientation.isometry_on_crossProduct` — sıra 30, alt=2, kullanan=1, üstü=`Orientation.isometry_on_rot`
- `Orientation.norm_crossProduct` — sıra 31, alt=1, kullanan=1, üstü=`Orientation.isometry_on_crossProduct`

## 3. `\uses` iddiaları kodla doğrulanıyor mu / Are the `\uses` claims confirmed by the code

Blueprint "A, B'yi kullanır" diyorsa, kodda A'nın bildirimi B'nin bildirimine (doğrudan ya da dolaylı) dayanmalı. / If the blueprint says A uses B, A's declaration must depend on B's in the code.

| | Sayı / Count |
|---|---:|
| Doğrulanan `\uses` / confirmed | 85 |
| **Kodda karşılığı olmayan `\uses` / not backed by the code** | **9** |
| Ölçülemeyen (iki uçtan biri Lean adı taşımıyor) / not measurable | 3 |
| Kodda olan blueprint düzeyi doğrudan bağımlılık / blueprint-level direct dependencies in the code | 272 |
| &nbsp;&nbsp;blueprint'te yazılmamış olanlar / of which missing from the blueprint | 171 |

Kodda karşılığı olmayan iddialar (ilk 30) / claims not backed by the code:

- `def:one_jet_space` (`OneJetBundle`) → `def:hom_bundle` (`Bundle.ContinuousLinearMap.vectorBundle`)
- `def:formal_sol` (`FormalSol`) → `def:one_jet_extension` (`oneJetExt`)
- `def:htpy_formal_sol` (`HtpyFormalSol`) → `def:formal_sol` (`FormalSol`)
- `lem:transfer` (`OneJetSec.localize`) → `def:formal_sol` (`FormalSol`)
- `lem:param_trick` (`FamilyOneJetSec.isHolonomicAt_uncurry`) → `def:formal_sol` (`FormalSol`)
- `def:rel_slice` (`RelMfld.slice`) → `def:rel_loc` (`RelLoc`)
- `lem:integration_step` (`StepLandscape.improveStep_rel_t_eq_0`) → `def:short_formal_sol` (`RelLoc.FormalSol.IsShortAt`)
- `def:ample_relation_loc` (`RelLoc.IsAmple`) → `def:rel_slice` (`RelMfld.slice`)
- `lem:reparametrization` (`SmoothSurroundingFamily.reparametrize_average`) → `lem:smooth_barycentric_coord` (`smooth_surrounding`)

Kodda olup blueprint'te yazılmamış bağımlılık örnekleri (ilk 30) / dependencies in the code missing from the blueprint:

- `lem:ex_localisation` (`stdLocalisationData`) → `IndexType`
- `lem:localisation_stability` (`localisation_stability`) → `IndexType`
- `def:one_jet_extension` (`oneJetExt`) → `Bundle.Pullback`
- `lem:one_jet_extension_prop` (`ContMDiff.oneJetExt`) → `Bundle.Pullback`
- `def:holonomic_section` (`OneJetSec.IsHolonomicAt`) → `oneJetExt`
- `def:holonomic_section` (`OneJetSec.IsHolonomicAt`) → `Bundle.Pullback`
- `def:formal_sol` (`FormalSol`) → `OneJetBundle`
- `def:formal_sol` (`FormalSol`) → `Bundle.Pullback`
- `def:htpy_formal_sol` (`HtpyFormalSol`) → `OneJetBundle`
- `def:htpy_formal_sol` (`HtpyFormalSol`) → `Bundle.Pullback`
- `def:htpy_formal_sol` (`HtpyFormalSol`) → `RelMfld`
- `def:transfer_map` (`OpenSmoothEmbedding.transfer`) → `oneJetExt`
- `def:transfer_map` (`OpenSmoothEmbedding.transfer`) → `ContMDiff.oneJetExt`
- `def:transfer_map` (`OpenSmoothEmbedding.transfer`) → `Bundle.Pullback`
- `lem:transfer` (`OneJetSec.localize`) → `oneJetExt`
- `lem:transfer` (`OneJetSec.localize`) → `OneJetBundle`
- `lem:transfer` (`OneJetSec.localize`) → `Bundle.Pullback`
- `def:h-princ` (`RelMfld.SatisfiesHPrinciple`) → `FormalSol`
- `def:h-princ` (`RelMfld.SatisfiesHPrinciple`) → `OneJetSec.IsHolonomicAt`
- `def:h-princ` (`RelMfld.SatisfiesHPrinciple`) → `OneJetBundle`
- `lem:param_trick` (`FamilyOneJetSec.isHolonomicAt_uncurry`) → `ContMDiff.oneJetExt`
- `lem:param_trick` (`FamilyOneJetSec.isHolonomicAt_uncurry`) → `OneJetBundle`
- `lem:param_trick` (`FamilyOneJetSec.isHolonomicAt_uncurry`) → `Bundle.Pullback`
- `lem:param_for_free` (`RelMfld.SatisfiesHPrinciple.satisfiesHPrincipleWith`) → `HtpyFormalSol`
- `lem:param_for_free` (`RelMfld.SatisfiesHPrinciple.satisfiesHPrincipleWith`) → `FormalSol`
- `lem:param_for_free` (`RelMfld.SatisfiesHPrinciple.satisfiesHPrincipleWith`) → `OneJetSec.IsHolonomicAt`
- `def:ample_relation` (`RelMfld.Ample`) → `DualPair`
- `def:ample_relation` (`RelMfld.Ample`) → `RelMfld.slice`
- `def:ample_relation` (`RelMfld.Ample`) → `RelMfld`
- `lem:ample_iff_loc` (`RelMfld.Ample.localize`) → `DualPair`


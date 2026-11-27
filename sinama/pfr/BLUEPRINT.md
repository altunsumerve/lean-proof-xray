# Blueprint karşılaştırması / Blueprint comparison

Cevap anahtarı: projenin elle yazılmış blueprint'i. Araç: kayıttan (lean4export) hesaplanan bağımlılık grafiği ve baskınlık ağacı. / Answer key: the project's hand-written blueprint. Tool: dependency graph and dominator tree computed from the export.

## 1. Blueprint adları kodda var mı / Are the blueprint's names in the code

| | Sayı / Count |
|---|---:|
| Blueprint öğesi / items | 219 |
| `\lean{}` taşıyan öğe / items with a Lean name | 213 |
| Farklı Lean adı / distinct Lean names | 254 |
| Kayıtta bulunan / found in the export | 107 |
| Kökün ispat konisinde (proje bildirimi) / in the root's proof cone | 103 |

Kayıtta olmayan adlar (147; kök bunları kullanmıyor ya da ad değişmiş): `AffineSpace.finrank`, `BSG_self`, `Finset.addEnergy'`, `Finset.card_sq_le_card_mul_addEnergy'`, `I_one_le`, `I_two_le`, `KLDiv`, `KLDiv_add_le_KLDiv_of_indep`, `KLDiv_eq_zero_iff_identDistrib`, `KLDiv_nonneg`, `KLDiv_of_comp_inj`, `KLDiv_of_convex`, `PFR_conjecture_improv`, `PFR_conjecture_improv_aux`, `PFR_projection`, `PFR_projection'`, `ProbabilityTheory.IdentDistrib.KLDiv_eq`, `ProbabilityTheory.condEntropy_add_left`, `ProbabilityTheory.condEntropy_add_right`, `ProbabilityTheory.condEntropy_comp_ge`, `ProbabilityTheory.condMutualInfo_nonneg`, `ProbabilityTheory.condMutual_comp_comp_le`, `ProbabilityTheory.entropy_le_log_card`, `ProbabilityTheory.max_condEntropy_sub_condMutualInfo_le_condEntropy_div`, `ProbabilityTheory.max_condEntropy_sub_condMutualInfo_le_condEntropy_mul`, `ProbabilityTheory.max_entropy_le_entropy_add`, `ProbabilityTheory.max_entropy_sub_mutualInfo_le_entropy_add`, `ProbabilityTheory.mutual_comp_comp_le`, `ProbabilityTheory.mutual_comp_le`, `Real.sum_mul_log_div_eq_iff`, `Real.sum_mul_log_div_leq`, `app_ent_PFR`, `approx_hom_pfr`, `approx_hom_pfr'`, `averaged_construct_good`, `better_PFR_conjecture`, `better_PFR_conjecture_aux`, `better_PFR_conjecture_aux0`, `card_of_dual`, `card_of_dual_constrained` …

## 2. Kilometre taşı sıralaması insan seçimini buluyor mu / Do milestone rankings recover the human choice

Aday: konideki yardımcı olmayan proje teoremleri (375). Hedef: bunlardan blueprint'te adı geçenler (92). Rastgele seçimde beklenen isabet: 24.5%. / Candidates: non-auxiliary project theorems in the cone. Target: those named in the blueprint.

| Ölçüt / criterion | İlk k'da isabet (k = hedef sayısı) / hits in top k | İlk 2k'da / in top 2k | Hedeflerin ortanca sırası / median rank of targets |
|---|---:|---:|---:|
| alt ağaç ağırlığı / subtree weight | 45 / 92 (49%) | 64 / 92 (70%) | 99 / 375 |
| alt ağaç bildirim sayısı / subtree count | 38 / 92 (41%) | 56 / 92 (61%) | 118 / 375 |
| kendi ispat ağırlığı / own proof weight | 38 / 92 (41%) | 64 / 92 (70%) | 117 / 375 |
| doğrudan kullanan sayısı / direct users | 33 / 92 (36%) | 57 / 92 (62%) | 164 / 375 |
| ağırlık ÷ önerme boyu / weight per statement size | 41 / 92 (45%) | 58 / 92 (63%) | 126 / 375 |
| ağaçta sığlık (köke yakınlık) / shallowness | 24 / 92 (26%) | 44 / 92 (48%) | 191 / 375 |
| yol payı (köke giden yolların geçen kesri) / path share | 50 / 92 (54%) | 72 / 92 (78%) | 79 / 375 |
| ağırlık ile yol payının iyisi / better of weight and path share | 53 / 92 (58%) | 73 / 92 (79%) | 74 / 375 |
| alt ağaç ağırlığı, zincirler tek adım / subtree weight, chains as one step | 44 / 84 (52%) | 60 / 84 (71%) | 80 / 311 |

Son satır: baskınlık ağacında tek çocuğu olan bir adım ile o çocuk tek adım sayılır (375 aday 311 zincir eder; rastgele beklenen 27.0%). / Last row: a step with exactly one child in the dominator tree is merged with that child.

Yapısal seçim kuralları: kuralın seçtiği adaylardan kaçı blueprint'te (kesinlik), blueprint teoremlerinin kaçı seçildi (kapsama). / Structural selection rules: precision = selected candidates that are in the blueprint, recall = blueprint theorems selected.

| Kural / rule | Seçilen / selected | Kesinlik / precision | Kapsama / recall |
|---|---:|---:|---:|
| ağaçta çocuğu olan / has children in the tree | 167 | 31% | 57% |
| yardımcı olmayan çocuğu olan / has a non-auxiliary child | 126 | 36% | 49% |
| en az 2 yerde kullanılan / used in at least 2 places | 154 | 28% | 47% |
| çocuğu olan VEYA ≥2 yerde kullanılan / children or ≥2 users | 242 | 31% | 80% |
| alt ağaç ağırlığı ≥ %0,5 / subtree weight ≥ 0.5% | 84 | 50% | 46% |
| ağırlık ≥ %0,5 VEYA ≥2 yerde kullanılan / weight ≥ 0.5% or ≥2 users | 215 | 34% | 79% |
| hepsi (her aday) / everything | 375 | 25% | 100% |

Ağırlık sıralamasının en geride bıraktığı blueprint teoremleri / blueprint theorems ranked lowest by weight:

- `ProbabilityTheory.mutualInfo_def` — sıra 354, alt=1, kullanan=4, önerme boyu=122, ispat ağırlığı=30
- `rdist_def` — sıra 344, alt=1, kullanan=2, önerme boyu=251, ispat ağırlığı=42
- `ProbabilityTheory.condEntropy_sub_left` — sıra 342, alt=1, kullanan=1, önerme boyu=142, ispat ağırlığı=47
- `ProbabilityTheory.entropy_pair_le_add` — sıra 332, alt=1, kullanan=1, önerme boyu=155, ispat ağırlığı=56
- `condRuzsaDist_diff_le` — sıra 322, alt=1, kullanan=2, önerme boyu=274, ispat ağırlığı=72
- `ProbabilityTheory.entropy_neg` — sıra 318, alt=1, kullanan=3, önerme boyu=93, ispat ağırlığı=78
- `rdist_of_sums_ge` — sıra 312, alt=1, kullanan=1, önerme boyu=516, ispat ağırlığı=88
- `ProbabilityTheory.IdentDistrib.entropy_congr` — sıra 307, alt=1, kullanan=17, önerme boyu=80, ispat ağırlığı=92
- `ProbabilityTheory.condEntropy_sub_right` — sıra 287, alt=1, kullanan=2, önerme boyu=121, ispat ağırlığı=115
- `ProbabilityTheory.entropy_comm` — sıra 285, alt=1, kullanan=8, önerme boyu=137, ispat ağırlığı=117
- `ProbabilityTheory.mutualInfo_comm` — sıra 280, alt=1, kullanan=1, önerme boyu=117, ispat ağırlığı=130
- `ProbabilityTheory.entropy_pair_eq_add` — sıra 279, alt=1, kullanan=3, önerme boyu=183, ispat ağırlığı=130
- `ProbabilityTheory.condEntropy_comp_of_injective` — sıra 274, alt=1, kullanan=2, önerme boyu=120, ispat ağırlığı=140
- `diff_rdist_le_2` — sıra 272, alt=1, kullanan=1, önerme boyu=494, ispat ağırlığı=140
- `ProbabilityTheory.chain_rule` — sıra 268, alt=1, kullanan=6, önerme boyu=172, ispat ağırlığı=149
- `diff_rdist_le_1` — sıra 252, alt=1, kullanan=1, önerme boyu=494, ispat ağırlığı=175
- `ProbabilityTheory.entropy_comp_of_injective` — sıra 241, alt=1, kullanan=13, önerme boyu=103, ispat ağırlığı=207
- `ProbabilityTheory.entropy_assoc` — sıra 232, alt=1, kullanan=2, önerme boyu=194, ispat ağırlığı=237
- `rdist_nonneg` — sıra 229, alt=1, kullanan=2, önerme boyu=146, ispat ağırlığı=253
- `condRuzsaDist_of_sums_ge` — sıra 225, alt=1, kullanan=2, önerme boyu=401, ispat ağırlığı=277

Ağırlık sıralamasında en üstte olup blueprint'te olmayan teoremler / top-ranked theorems not in the blueprint:

- `tau_strictly_decreases_aux` — sıra 4, alt=256, kullanan=1, üstü=`tau_strictly_decreases`
- `cond_construct_good` — sıra 5, alt=56, kullanan=1, üstü=`tau_strictly_decreases_aux`
- `construct_good'` — sıra 6, alt=49, kullanan=1, üstü=`cond_construct_good`
- `ProbabilityTheory.Kernel.chain_rule` — sıra 13, alt=54, kullanan=3, üstü=`PFR_conjecture_aux`
- `ProbabilityTheory.condIndep_copies'` — sıra 14, alt=22, kullanan=1, üstü=`ent_bsg`
- `comparison_of_ruzsa_distances` — sıra 15, alt=9, kullanan=2, üstü=`tau_strictly_decreases_aux`
- `sum_of_rdist_eq_char_2` — sıra 16, alt=20, kullanan=2, üstü=`tau_strictly_decreases_aux`
- `ProbabilityTheory.measureMutualInfo_nonneg_aux` — sıra 20, alt=24, kullanan=2, üstü=`PFR_conjecture_aux`
- `ProbabilityTheory.Kernel.entropy_compProd` — sıra 21, alt=20, kullanan=1, üstü=`ProbabilityTheory.Kernel.chain_rule`
- `independenceCondition1` — sıra 23, alt=27, kullanan=6, üstü=`sum_dist_diff_le`
- `ProbabilityTheory.iIndepFun.apply_two_last` — sıra 24, alt=26, kullanan=1, üstü=`independenceCondition1`
- `ProbabilityTheory.independent_copies3_nondep_finiteRange` — sıra 26, alt=4, kullanan=2, üstü=`entropic_PFR_conjecture`
- `condRuzsaDist'_of_inj_map'` — sıra 27, alt=14, kullanan=1, üstü=`sum_dist_diff_le`
- `ProbabilityTheory.Kernel.entropy_compProd'` — sıra 32, alt=12, kullanan=1, üstü=`ProbabilityTheory.Kernel.entropy_compProd`
- `kaimanovich_vershik'` — sıra 33, alt=8, kullanan=1, üstü=`comparison_of_ruzsa_distances`
- `ProbabilityTheory.condEntropy_two_eq_kernel_entropy` — sıra 35, alt=20, kullanan=2, üstü=`entropic_PFR_conjecture`
- `ProbabilityTheory.Kernel.entropy_compProd_aux` — sıra 39, alt=6, kullanan=1, üstü=`ProbabilityTheory.Kernel.entropy_compProd'`
- `ProbabilityTheory.condDistrib_eq_prod_of_indepFun` — sıra 42, alt=7, kullanan=1, üstü=`condRuzsaDist_of_indep`
- `ProbabilityTheory.independent_copies4_nondep` — sıra 46, alt=1, kullanan=1, üstü=`tau_strictly_decreases`
- `rdist_le_of_isUniform_of_card_sub_le` — sıra 47, alt=8, kullanan=1, üstü=`PFR_conjecture_aux`

## 3. `\uses` iddiaları kodla doğrulanıyor mu / Are the `\uses` claims confirmed by the code

Blueprint "A, B'yi kullanır" diyorsa, kodda A'nın bildirimi B'nin bildirimine (doğrudan ya da dolaylı) dayanmalı. / If the blueprint says A uses B, A's declaration must depend on B's in the code.

| | Sayı / Count |
|---|---:|
| Doğrulanan `\uses` / confirmed | 167 |
| **Kodda karşılığı olmayan `\uses` / not backed by the code** | **27** |
| Ölçülemeyen (iki uçtan biri Lean adı taşımıyor) / not measurable | 2 |
| Kodda olan blueprint düzeyi doğrudan bağımlılık / blueprint-level direct dependencies in the code | 438 |
| &nbsp;&nbsp;blueprint'te yazılmamış olanlar / of which missing from the blueprint | 269 |

Kodda karşılığı olmayan iddialar (ilk 30) / claims not backed by the code:

- `zero-large` (`sub_mem_symmGroup`) → `relabeled-entropy-cond` (`ProbabilityTheory.condEntropy_comp_of_injective`)
- `shear-ent` (`ProbabilityTheory.condEntropy_add_right`) → `chain-rule` (`ProbabilityTheory.chain_rule`)
- `shear-ent` (`ProbabilityTheory.condEntropy_add_right`) → `relabeled-entropy-cond` (`ProbabilityTheory.condEntropy_comp_of_injective`)
- `sumset-lower-gen` (`ProbabilityTheory.max_entropy_sub_mutualInfo_le_entropy_add`) → `neg-ent` (`ProbabilityTheory.entropy_neg`)
- `ruz-dist-def` (`rdist_def`) → `independent-exist` (`ProbabilityTheory.independent_copies`)
- `ruz-copy` (`ProbabilityTheory.IdentDistrib.rdist_congr`) → `ruz-dist-def` (`rdist_def`)
- `ruz-indep` (`ProbabilityTheory.IndepFun.rdist_eq`) → `relabeled-entropy` (`ProbabilityTheory.entropy_comp_of_injective`)
- `ruz-indep` (`ProbabilityTheory.IndepFun.rdist_eq`) → `copy-ent` (`ProbabilityTheory.IdentDistrib.entropy_congr`)
- `ruzsa-diff` (`diff_ent_le_rdist`) → `neg-ent` (`ProbabilityTheory.entropy_neg`)
- `ruzsa-triangle-improved` (`ent_of_diff_le`) → `subadditive` (`ProbabilityTheory.entropy_pair_le_add`)
- `cond-dist-def` (`condRuzsaDist`) → `ruz-dist-def` (`rdist_def`)
- `cond-dist-alt` (`condRuzsaDist_of_copy`) → `copy-ent` (`ProbabilityTheory.IdentDistrib.entropy_congr`)
- `cond-dist-alt` (`condRuzsaDist_of_copy`) → `ruz-indep` (`ProbabilityTheory.IndepFun.rdist_eq`)
- `cond-dist-alt` (`condRuzsaDist_of_copy`) → `ruz-copy` (`ProbabilityTheory.IdentDistrib.rdist_congr`)
- `entropic-bsg` (`ent_bsg`) → `add-entropy` (`ProbabilityTheory.entropy_pair_eq_add`)
- `uniform-entropy` (`ProbabilityTheory.IsUniform.entropy_eq`) → `concave` (`Real.strictConcaveOn_negMulLog`)
- `conditional-chain-rule` (`ProbabilityTheory.cond_chain_rule`) → `chain-rule` (`ProbabilityTheory.chain_rule`)
- `mutual-nonneg` (`ProbabilityTheory.mutualInfo_nonneg`) → `alternative-mutual` (`ProbabilityTheory.mutualInfo_comm`)
- `subadditive` (`ProbabilityTheory.entropy_pair_le_add`) → `alternative-mutual` (`ProbabilityTheory.mutualInfo_comm`)
- `cond-reduce` (`ProbabilityTheory.condEntropy_le_entropy`) → `alternative-mutual` (`ProbabilityTheory.mutualInfo_comm`)
- `submodularity` (`ProbabilityTheory.entropy_submodular`) → `cond-reduce` (`ProbabilityTheory.condEntropy_le_entropy`)
- `conditional-mutual-def` (`ProbabilityTheory.condMutualInfo`) → `information-def` (`ProbabilityTheory.mutualInfo`)
- `tau-def` (`tau`) → `ruz-dist-def` (`rdist_def`)
- `distance-lower` (`distance_ge_of_min`) → `tau-min` (`tau_minimizer_exists`)
- `fibring-ident` (`rdist_of_indep_eq_sum_fibre`) → `independent-exist` (`ProbabilityTheory.independent_copies`)
- `fibring-ident` (`rdist_of_indep_eq_sum_fibre`) → `submodularity` (`ProbabilityTheory.entropy_submodular`)
- `fibring-ident` (`rdist_of_indep_eq_sum_fibre`) → `ruz-copy` (`ProbabilityTheory.IdentDistrib.rdist_congr`)

Kodda olup blueprint'te yazılmamış bağımlılık örnekleri (ilk 30) / dependencies in the code missing from the blueprint:

- `zero-large` (`sub_mem_symmGroup`) → `ProbabilityTheory.IndepFun`
- `zero-large` (`sub_mem_symmGroup`) → `ProbabilityTheory.entropy`
- `zero-large` (`sub_mem_symmGroup`) → `ProbabilityTheory.condEntropy_sub_right`
- `sym-zero` (`isUniform_sub_const_of_rdist_eq_zero`) → `ProbabilityTheory.entropy`
- `lem:100pc-self` (`exists_isUniform_of_rdist_self_eq_zero`) → `ProbabilityTheory.IdentDistrib.rdist_congr`
- `lem:100pc-self` (`exists_isUniform_of_rdist_self_eq_zero`) → `ProbabilityTheory.IndepFun`
- `lem:100pc-self` (`exists_isUniform_of_rdist_self_eq_zero`) → `ProbabilityTheory.IsUniform`
- `lem:100pc` (`exists_isUniform_of_rdist_eq_zero`) → `ProbabilityTheory.IsUniform`
- `lem:100pc` (`exists_isUniform_of_rdist_eq_zero`) → `ProbabilityTheory.entropy`
- `lem:100pc` (`exists_isUniform_of_rdist_eq_zero`) → `rdist_symm`
- `neg-ent` (`ProbabilityTheory.entropy_neg`) → `ProbabilityTheory.entropy`
- `shear-ent` (`ProbabilityTheory.condEntropy_add_right`) → `ProbabilityTheory.entropy`
- `shear-ent` (`ProbabilityTheory.condEntropy_add_right`) → `ProbabilityTheory.cond`
- `shear-ent` (`ProbabilityTheory.condEntropy_add_right`) → `ProbabilityTheory.entropy_comp_of_injective`
- `sumset-lower-gen` (`ProbabilityTheory.max_entropy_sub_mutualInfo_le_entropy_add`) → `ProbabilityTheory.entropy`
- `sumset-lower-gen` (`ProbabilityTheory.max_entropy_sub_mutualInfo_le_entropy_add`) → `ProbabilityTheory.mutualInfo`
- `sumset-lower-gen` (`ProbabilityTheory.max_entropy_sub_mutualInfo_le_entropy_add`) → `ProbabilityTheory.condEntropy`
- `sumset-lower` (`ProbabilityTheory.max_entropy_le_entropy_add`) → `ProbabilityTheory.IndepFun`
- `sumset-lower` (`ProbabilityTheory.max_entropy_le_entropy_add`) → `ProbabilityTheory.entropy`
- `sumset-lower` (`ProbabilityTheory.max_entropy_le_entropy_add`) → `ProbabilityTheory.mutualInfo`
- `ruz-copy` (`ProbabilityTheory.IdentDistrib.rdist_congr`) → `ProbabilityTheory.entropy`
- `ruz-indep` (`ProbabilityTheory.IndepFun.rdist_eq`) → `ProbabilityTheory.entropy`
- `ruz-indep` (`ProbabilityTheory.IndepFun.rdist_eq`) → `ProbabilityTheory.IndepFun`
- `ruzsa-symm` (`rdist_symm`) → `ProbabilityTheory.entropy`
- `ruzsa-diff` (`diff_ent_le_rdist`) → `ProbabilityTheory.IdentDistrib.rdist_congr`
- `ruzsa-diff` (`diff_ent_le_rdist`) → `ProbabilityTheory.IndepFun`
- `ruzsa-diff` (`diff_ent_le_rdist`) → `ProbabilityTheory.entropy`
- `ruzsa-nonneg` (`rdist_nonneg`) → `ProbabilityTheory.entropy`
- `ruzsa-triangle-improved` (`ent_of_diff_le`) → `ProbabilityTheory.mutualInfo_nonneg`
- `ruzsa-triangle-improved` (`ent_of_diff_le`) → `ProbabilityTheory.IndepFun`


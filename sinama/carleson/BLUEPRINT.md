# Blueprint karşılaştırması / Blueprint comparison

Cevap anahtarı: projenin elle yazılmış blueprint'i. Araç: kayıttan (lean4export) hesaplanan bağımlılık grafiği ve baskınlık ağacı. / Answer key: the project's hand-written blueprint. Tool: dependency graph and dominator tree computed from the export.

## 1. Blueprint adları kodda var mı / Are the blueprint's names in the code

| | Sayı / Count |
|---|---:|
| Blueprint öğesi / items | 180 |
| `\lean{}` taşıyan öğe / items with a Lean name | 179 |
| Farklı Lean adı / distinct Lean names | 249 |
| Kayıtta bulunan / found in the export | 230 |
| Kökün ispat konisinde (proje bildirimi) / in the root's proof cone | 219 |

Kayıtta olmayan adlar (19; kök bunları kullanmıyor ya da ad değişmiş): `I1_prop_1`, `I2_prop_2`, `MeasureTheory.eLpNorm_pow_eq_distribution`, `Metric.dense_iff_iUnion_ball`, `antichain_decomposition`, `control_approximation_effect`, `czApproximation_add_czRemainder`, `eLpNorm_czRemainder_le`, `enorm_carlesonOperatorIntegrand_le`, `exceptional_set_carleson`, `integrable_tile_sum_operator`, `integral_czRemainder`, `intervalIntegral.integral_comp_sub_right`, `leftContinuous_carlesonOperatorIntegrand`, `periodic_dirichletApprox`, `rightContinuous_carlesonOperatorIntegrand`, `tsum_eLpNorm_czRemainder'_le`, `tsum_eLpNorm_czRemainder_le`, `Θ.finite_and_mk_le_of_le_dist`

## 2. Kilometre taşı sıralaması insan seçimini buluyor mu / Do milestone rankings recover the human choice

Aday: konideki yardımcı olmayan proje teoremleri (1815). Hedef: bunlardan blueprint'te adı geçenler (213). Rastgele seçimde beklenen isabet: 11.7%. / Candidates: non-auxiliary project theorems in the cone. Target: those named in the blueprint.

| Ölçüt / criterion | İlk k'da isabet (k = hedef sayısı) / hits in top k | İlk 2k'da / in top 2k | Hedeflerin ortanca sırası / median rank of targets |
|---|---:|---:|---:|
| alt ağaç ağırlığı / subtree weight | 94 / 213 (44%) | 148 / 213 (69%) | 247 / 1815 |
| alt ağaç bildirim sayısı / subtree count | 93 / 213 (44%) | 134 / 213 (63%) | 259 / 1815 |
| kendi ispat ağırlığı / own proof weight | 76 / 213 (36%) | 124 / 213 (58%) | 344 / 1815 |
| doğrudan kullanan sayısı / direct users | 19 / 213 (9%) | 39 / 213 (18%) | 939 / 1815 |
| ağırlık ÷ önerme boyu / weight per statement size | 72 / 213 (34%) | 109 / 213 (51%) | 407 / 1815 |
| ağaçta sığlık (köke yakınlık) / shallowness | 26 / 213 (12%) | 40 / 213 (19%) | 1145 / 1815 |
| yol payı (köke giden yolların geçen kesri) / path share | 70 / 213 (33%) | 119 / 213 (56%) | 386 / 1815 |
| ağırlık ile yol payının iyisi / better of weight and path share | 79 / 213 (37%) | 135 / 213 (63%) | 296 / 1815 |
| alt ağaç ağırlığı, zincirler tek adım / subtree weight, chains as one step | 102 / 210 (49%) | 152 / 210 (72%) | 221 / 1626 |

Son satır: baskınlık ağacında tek çocuğu olan bir adım ile o çocuk tek adım sayılır (1815 aday 1626 zincir eder; rastgele beklenen 12.9%). / Last row: a step with exactly one child in the dominator tree is merged with that child.

Yapısal seçim kuralları: kuralın seçtiği adaylardan kaçı blueprint'te (kesinlik), blueprint teoremlerinin kaçı seçildi (kapsama). / Structural selection rules: precision = selected candidates that are in the blueprint, recall = blueprint theorems selected.

| Kural / rule | Seçilen / selected | Kesinlik / precision | Kapsama / recall |
|---|---:|---:|---:|
| ağaçta çocuğu olan / has children in the tree | 874 | 20% | 80% |
| yardımcı olmayan çocuğu olan / has a non-auxiliary child | 544 | 24% | 62% |
| en az 2 yerde kullanılan / used in at least 2 places | 759 | 9% | 33% |
| çocuğu olan VEYA ≥2 yerde kullanılan / children or ≥2 users | 1186 | 15% | 84% |
| alt ağaç ağırlığı ≥ %0,5 / subtree weight ≥ 0.5% | 173 | 44% | 36% |
| ağırlık ≥ %0,5 VEYA ≥2 yerde kullanılan / weight ≥ 0.5% or ≥2 users | 918 | 15% | 64% |
| hepsi (her aday) / everything | 1815 | 12% | 100% |

Ağırlık sıralamasının en geride bıraktığı blueprint teoremleri / blueprint theorems ranked lowest by weight:

- `dist_mem_Icc_of_Ks_ne_zero` — sıra 1647, alt=1, kullanan=13, önerme boyu=245, ispat ağırlığı=36
- `antichain_L0'` — sıra 1567, alt=1, kullanan=1, önerme boyu=1134, ispat ağırlığı=48
- `pairwiseDisjoint_L0'` — sıra 1466, alt=1, kullanan=1, önerme boyu=1582, ispat ağırlığı=58
- `antichain_L1` — sıra 1458, alt=1, kullanan=1, önerme boyu=1135, ispat ağırlığı=60
- `TileStructure.Forest.pairwiseDisjoint_𝓛` — sıra 1451, alt=1, kullanan=3, önerme boyu=1038, ispat ağırlığı=61
- `TileStructure.Forest.pairwiseDisjoint_𝓙₅` — sıra 1439, alt=1, kullanan=2, önerme boyu=1652, ispat ağırlığı=64
- `TileStructure.Forest.pairwiseDisjoint_𝓙₆` — sıra 1429, alt=1, kullanan=2, önerme boyu=1437, ispat ağırlığı=67
- `measurable_maximalFunction` — sıra 1409, alt=1, kullanan=16, önerme boyu=88, ispat ağırlığı=72
- `continuous_dirichletApprox` — sıra 1392, alt=1, kullanan=2, önerme boyu=37, ispat ağırlığı=75
- `antichain_L3` — sıra 1331, alt=2, kullanan=1, önerme boyu=1137, ispat ağırlığı=51
- `TileStructure.Forest.global_tree_control1_edist_right` — sıra 1300, alt=1, kullanan=2, önerme boyu=7632, ispat ağırlığı=101
- `frequency_ball_growth` — sıra 1181, alt=1, kullanan=1, önerme boyu=169, ispat ağırlığı=144
- `TileStructure.Forest.pairwiseDisjoint_𝓙` — sıra 1157, alt=1, kullanan=9, önerme boyu=1038, ispat ağırlığı=152
- `smul_mono` — sıra 1147, alt=1, kullanan=3, önerme boyu=647, ispat ağırlığı=158
- `volume_univ_le` — sıra 1146, alt=1, kullanan=1, önerme boyu=463, ispat ağırlığı=160
- `Grid.dist_mono` — sıra 1136, alt=1, kullanan=9, önerme boyu=1117, ispat ağırlığı=167
- `integral_czRemainder'` — sıra 1129, alt=1, kullanan=1, önerme boyu=188, ispat ağırlığı=171
- `support_czRemainder'_subset` — sıra 1115, alt=2, kullanan=3, önerme boyu=112, ispat ağırlığı=156
- `encard_czBall3_le` — sıra 1101, alt=3, kullanan=1, önerme boyu=157, ispat ağırlığı=165
- `TileStructure.Forest.𝔗_subset_𝔖₀` — sıra 1096, alt=1, kullanan=3, önerme boyu=3270, ispat ağırlığı=188

Ağırlık sıralamasında en üstte olup blueprint'te olmayan teoremler / top-ranked theorems not in the blueprint:

- `carleson_interval'` — sıra 1, alt=4944, kullanan=1, üstü=`classical_carleson`
- `exceptional_set_carleson'` — sıra 2, alt=4930, kullanan=1, üstü=`carleson_interval'`
- `control_approximation_effect'` — sıra 3, alt=4877, kullanan=1, üstü=`exceptional_set_carleson'`
- `distribution_carlesonOperatorReal_le'` — sıra 4, alt=4771, kullanan=1, üstü=`control_approximation_effect'`
- `rcarleson_exceptional_set_estimate_specific''` — sıra 5, alt=4750, kullanan=1, üstü=`distribution_carlesonOperatorReal_le'`
- `rcarleson_exceptional_set_estimate_specific'` — sıra 6, alt=4749, kullanan=1, üstü=`rcarleson_exceptional_set_estimate_specific''`
- `rcarleson_exceptional_set_estimate_specific` — sıra 7, alt=4747, kullanan=1, üstü=`rcarleson_exceptional_set_estimate_specific'`
- `rcarleson_exceptional_set_estimate` — sıra 8, alt=4742, kullanan=1, üstü=`rcarleson_exceptional_set_estimate_specific`
- `rcarleson_general` — sıra 10, alt=4736, kullanan=1, üstü=`rcarleson`
- `R_truncation'` — sıra 15, alt=3211, kullanan=1, üstü=`R_truncation`
- `finitary_carleson_step` — sıra 18, alt=3035, kullanan=6, üstü=`linearized_truncation`
- `forest_union_optimized` — sıra 22, alt=1381, kullanan=1, üstü=`forest_union`
- `forest_union_aux` — sıra 23, alt=1374, kullanan=1, üstü=`forest_union_optimized`
- `lintegral_carlesonSum_forest'` — sıra 24, alt=1214, kullanan=1, üstü=`forest_union_aux`
- `lintegral_carlesonSum_forest` — sıra 25, alt=1209, kullanan=1, üstü=`lintegral_carlesonSum_forest'`
- `forest_operator_le_volume` — sıra 26, alt=1086, kullanan=1, üstü=`lintegral_carlesonSum_forest`
- `forest_operator'` — sıra 27, alt=1085, kullanan=1, üstü=`forest_operator_le_volume`
- `TileStructure.Forest.forest_operator_g` — sıra 29, alt=522, kullanan=1, üstü=`forest_operator`
- `TileStructure.Forest.forest_operator_g_main` — sıra 31, alt=518, kullanan=1, üstü=`TileStructure.Forest.forest_operator_g`
- `forest_complement_optimized` — sıra 32, alt=591, kullanan=1, üstü=`forest_complement`

## 3. `\uses` iddiaları kodla doğrulanıyor mu / Are the `\uses` claims confirmed by the code

Blueprint "A, B'yi kullanır" diyorsa, kodda A'nın bildirimi B'nin bildirimine (doğrudan ya da dolaylı) dayanmalı. / If the blueprint says A uses B, A's declaration must depend on B's in the code.

| | Sayı / Count |
|---|---:|
| Doğrulanan `\uses` / confirmed | 202 |
| **Kodda karşılığı olmayan `\uses` / not backed by the code** | **7** |
| Ölçülemeyen (iki uçtan biri Lean adı taşımıyor) / not measurable | 4 |
| Kodda olan blueprint düzeyi doğrudan bağımlılık / blueprint-level direct dependencies in the code | 977 |
| &nbsp;&nbsp;blueprint'te yazılmamış olanlar / of which missing from the blueprint | 727 |

Kodda karşılığı olmayan iddialar (ilk 30) / claims not backed by the code:

- `wiggle-order-3` (`wiggle_order_11_10`) → `wiggle-order-1` (`smul_mono`)
- `tile-uncertainty` (`Tile.uncertainty`) → `tile-range-support` (`Tile.range_support`)
- `tile-uncertainty` (`Tile.uncertainty`) → `monotone-cube-metrics` (`Grid.dist_mono`)
- `first-tree-pointwise` (`TileStructure.Forest.first_tree_pointwise`) → `convex-scales` (`TileStructure.Forest.convex_scales`)
- `Young-convolution` (`young_convolution`) → `periodic-domain-shift` (`Function.Periodic.intervalIntegral_add_eq`)
- `Dirichlet-Hilbert` (`Dirichlet_Hilbert_diff`) → `Dirichlet-kernel` (`dirichletKernel_eq`)
- `real-line-doubling` (`MeasureTheory.InnerProductSpace.IsDoubling`) → `real-line-ball-measure` (`Real.volume_ball`)

Kodda olup blueprint'te yazılmamış bağımlılık örnekleri (ilk 30) / dependencies in the code missing from the blueprint:

- `classical-carleson` (`classical_carleson`) → `close_smooth_approx_periodic`
- `classical-carleson` (`classical_carleson`) → `instIsAddHaarMeasureVolume`
- `classical-carleson` (`classical_carleson`) → `TopologicalSpace.exists_countable_dense`
- `metric-space-Carleson` (`metric_carleson`) → `TopologicalSpace.exists_countable_dense`
- `metric-space-Carleson` (`metric_carleson`) → `Real.instCompleteSpace`
- `metric-space-Carleson` (`metric_carleson`) → `instProperSpaceReal`
- `linearised-metric-Carleson` (`linearized_metric_carleson`) → `TopologicalSpace.exists_countable_dense`
- `linearised-metric-Carleson` (`linearized_metric_carleson`) → `Real.instCompleteSpace`
- `linearised-metric-Carleson` (`linearized_metric_carleson`) → `instProperSpaceReal`
- `finitary-Carleson` (`finitary_carleson`) → `TopologicalSpace.exists_countable_dense`
- `finitary-Carleson` (`finitary_carleson`) → `Real.instCompleteSpace`
- `finitary-Carleson` (`finitary_carleson`) → `instProperSpaceReal`
- `discrete-Carleson` (`discrete_carleson`) → `TopologicalSpace.exists_countable_dense`
- `discrete-Carleson` (`discrete_carleson`) → `Real.instCompleteSpace`
- `discrete-Carleson` (`discrete_carleson`) → `instProperSpaceReal`
- `antichain-operator` (`antichain_operator`) → `TopologicalSpace.exists_countable_dense`
- `antichain-operator` (`antichain_operator`) → `Real.instCompleteSpace`
- `antichain-operator` (`antichain_operator`) → `instProperSpaceReal`
- `forest-operator` (`forest_operator`) → `dist_mem_Icc_of_Ks_ne_zero`
- `forest-operator` (`forest_operator`) → `TopologicalSpace.exists_countable_dense`
- `forest-operator` (`forest_operator`) → `Real.instCompleteSpace`
- `Holder-van-der-Corput` (`holder_van_der_corput`) → `TopologicalSpace.exists_countable_dense`
- `Holder-van-der-Corput` (`holder_van_der_corput`) → `Real.instCompleteSpace`
- `Holder-van-der-Corput` (`holder_van_der_corput`) → `instProperSpaceReal`
- `Hardy-Littlewood` (`measure_biUnion_le_lintegral`) → `instIsAddHaarMeasureVolume`
- `Hardy-Littlewood` (`measure_biUnion_le_lintegral`) → `TopologicalSpace.exists_countable_dense`
- `Hardy-Littlewood` (`measure_biUnion_le_lintegral`) → `locallyCompact_of_proper`
- `monotone-cube-metrics` (`Grid.dist_mono`) → `Real.instCompleteSpace`
- `monotone-cube-metrics` (`Grid.dist_mono`) → `instProperSpaceReal`
- `monotone-cube-metrics` (`Grid.dist_mono`) → `TopologicalSpace.exists_countable_dense`


# Koni / Cone — ispat konisi ve baskınlık ağacı / proof cone and dominator tree

Kök / root: `classical_carleson`

Bu sayfadaki sayılar resmi Lean kaydının (lean4export) bağımlılık grafiğinden hesaplanır; tahmin içermez. / All numbers on this page are computed from the dependency graph of the official Lean export.

## 1. Sayılar / Numbers

| | Bildirim / declarations | İfade ağırlığı / expression weight |
|---|---:|---:|
| Kayıttaki toplam / total in the export | 63.572 | 8.599.755 |
| Kütüphane (Mathlib ve altı) / library | 58.598 | 6.947.528 |
| Proje / project | 4.974 | 1.652.227 |
| &nbsp;&nbsp;kökün ispat konisinde / in the root's proof cone | 4.952 (%99,6) | 1.652.227 (%100,0) |
| &nbsp;&nbsp;**kullanılmayan / unused by the root** | **22** (%0,4) | 0 (%0,0) |
| Kökün önermesini anlamak için gereken proje bildirimi / project declarations needed to read the root's statement | 3 | |
| Konideki kütüphane bildirimi / library declarations in the cone | 57.795 | |

İfade ağırlığı: bildirimin kayda eklediği yeni ifade düğümü sayısı (ispatın büyüklüğünün ölçüsü). / Expression weight: number of new expression nodes the declaration added to the export.

| Tür / kind | Projede / in project | Konide / in cone |
|---|---:|---:|
| teorem | 4.239 | 4.239 |
| tanım | 613 | 613 |
| opak | 47 | 47 |
| kurucu | 25 | 25 |
| tip | 25 | 25 |
| özyineleyici | 25 | 3 |

## 1b. Aksiyomlar / Axioms

Kökün ispat konisindeki aksiyom: **3** (kayıttaki toplam aksiyom: 3; kütüphane dahil, hiçbiri atlanmadı). Lean'in üç standart aksiyomu dışında kalan: **0**. / Axioms in the root's proof cone: 3 (axioms in the export: 3; library included). Outside Lean's three standard axioms: 0.

| Aksiyom / axiom | Not / note |
|---|---|
| `Classical.choice` | standart / standard |
| `Quot.sound` | standart / standard |
| `propext` | standart / standard |

Bu liste kayıttaki `axiom` bildirimlerinden okunur; ispatı yeniden denetlemez (bunu Lean çekirdeği ve bağımsız denetleyiciler yapar). / Read from the `axiom` declarations of the export; it does not re-check the proof.

## 2. Kullanılmayan kod / Unused code

Kökün ispatına hiç girmeyen proje bildirimi: **22** (bunların 22 tanesi Lean'in otomatik yardımcısı). / Project declarations never used by the root's proof: 22 (22 of them Lean-generated auxiliaries).

| Ad alanı / namespace | Bildirim | Ağırlık / weight |
|---|---:|---:|
| `MeasureTheory.Measure` | 1 | 0 |
| `MeasureTheory.DoublingMeasure` | 1 | 0 |
| `FunctionDistances.rec` | 1 | 0 |
| `IsOneSidedKernel.rec` | 1 | 0 |
| `IsTwoSidedKernel.rec` | 1 | 0 |
| `CompatibleFunctions.rec` | 1 | 0 |
| `IsCancellative.rec` | 1 | 0 |
| `BoundedFiniteSupport.rec` | 1 | 0 |
| `KernelProofData.rec` | 1 | 0 |
| `ScaledPowerFunction.rec` | 1 | 0 |
| `ToneCouple.rec` | 1 | 0 |
| `StrictRangeToneCouple.rec` | 1 | 0 |
| `P304.rec` | 1 | 0 |
| `ProofData.rec` | 1 | 0 |
| `GridStructure.rec` | 1 | 0 |
| `ClosenessProperty.rec` | 1 | 0 |
| `PreTileStructure.rec` | 1 | 0 |
| `TileStructure.rec` | 1 | 0 |
| `EquivalenceOn.rec` | 1 | 0 |
| `TileStructure.Forest` | 1 | 0 |

## 3. Kopya önermeler / Duplicate statements

Proje teoremi: 4.239. Önermesi (tipi) başka bir teoreminkiyle yapısal olarak aynı olan gruplar: **259**; fazladan kopya: **1.300** (%30,7). Yardımcı adlar hariç: 2 grup, 4 fazladan kopya. / Project theorems: 4.239. Groups whose statement (type) is structurally identical: 259; redundant copies: 1.300. Excluding auxiliary names: 2 groups, 4 redundant copies.

Not: parmak izi 64 bit ve yapısaldır (bağlı değişken adları sayılmaz); evren parametre adları farklıysa kopya sayılmaz. / The fingerprint is 64-bit and structural.

| Kopya sayısı | Konide | Örnek adlar / example names |
|---:|---:|---|
| 4 | 4 | `instFactLtRealOfNatHMulPi_carleson_1`, `instFactLtRealOfNatHMulPi_carleson_2`, `instFactLtRealOfNatHMulPi_carleson` |
| 2 | 2 | `ENNReal.preservation_positivity'`, `ComputationsInterpolatedExponents.interpolated_pos'` |

## 4. Baskınlık ağacı / Dominator tree

X, Y'nin üstündeyse kökten Y'ye giden her bağımlılık yolu X'ten geçer: Y yalnızca X için vardır. Bir satırın alt ağacı, makalede o başlığın altına girecek her şeydir. / If X is above Y, every dependency path from the root to Y passes through X.

Ağaçtaki düğüm: 4.952; kökün doğrudan çocukları: 5; en derin düzey: 44.

| Alt ağaç büyüklüğü / subtree size | Düğüm / nodes |
|---|---:|
| ≥ 10 bildirim | 293 |
| ≥ 100 bildirim | 78 |
| ≥ 1.000 bildirim | 29 |
| ≥ 10.000 bildirim | 0 |
| ≥ 100.000 bildirim | 0 |

Aşağıda ağırlığı toplamın en az %0,5'i olan dallar (en çok 5 düzey). Sütunlar: alt ağaçtaki bildirim, ağırlık payı, bu bildirimi doğrudan kullanan sayısı.

```
classical_carleson  [teorem]  alt=4.952  %100,0  kullanan=1
  carleson_interval'  [teorem]  alt=4.944  %99,9  kullanan=1
    exceptional_set_carleson'  [teorem]  alt=4.930  %99,7  kullanan=1
      control_approximation_effect'  [teorem]  alt=4.877  %98,5  kullanan=1
        distribution_carlesonOperatorReal_le'  [teorem]  alt=4.771  %95,3  kullanan=1
          rcarleson_exceptional_set_estimate_specific''  [teorem]  alt=4.750  %94,8  kullanan=1
          … ve 3 küçük çocuk daha
        partialFourierSum_bound  [teorem]  alt=35  %1,6  kullanan=1
          le_CarlesonOperatorReal  [teorem]  alt=11  %0,9  kullanan=1
          … ve 11 küçük çocuk daha
        … ve 35 küçük çocuk daha
      fourierConv_ofTwiceDifferentiable  [teorem]  alt=11  %0,5  kullanan=1
        … ve 4 küçük çocuk daha
      … ve 26 küçük çocuk daha
    … ve 4 küçük çocuk daha
  … ve 4 küçük çocuk daha
```

## 5. En büyük kilometre taşları / Largest milestones

Kök dışındaki, yardımcı olmayan teoremler; alt ağaç ağırlığına göre. Önerme metni projenin kaynağından alınmıştır (atlas verildiyse). / Non-auxiliary theorems other than the root, by subtree weight; statement text is from the source when available.

| # | Teorem | Alt ağaç | Pay | Üstü / dominator | Kaynak |
|---:|---|---:|---:|---|---|
| 1 | `carleson_interval'` | 4.944 | %99,9 | `classical_carleson` |  |
| 2 | `exceptional_set_carleson'` | 4.930 | %99,7 | `carleson_interval'` |  |
| 3 | `control_approximation_effect'` | 4.877 | %98,5 | `exceptional_set_carleson'` |  |
| 4 | `distribution_carlesonOperatorReal_le'` | 4.771 | %95,3 | `control_approximation_effect'` |  |
| 5 | `rcarleson_exceptional_set_estimate_specific''` | 4.750 | %94,8 | `distribution_carlesonOperatorReal_le'` |  |
| 6 | `rcarleson_exceptional_set_estimate_specific'` | 4.749 | %94,8 | `rcarleson_exceptional_set_estimate_specific''` |  |
| 7 | `rcarleson_exceptional_set_estimate_specific` | 4.747 | %94,7 | `rcarleson_exceptional_set_estimate_specific'` |  |
| 8 | `rcarleson_exceptional_set_estimate` | 4.742 | %94,7 | `rcarleson_exceptional_set_estimate_specific` |  |
| 9 | `rcarleson` | 4.737 | %94,5 | `rcarleson_exceptional_set_estimate` |  |
| 10 | `rcarleson_general` | 4.736 | %94,5 | `rcarleson` |  |
| 11 | `two_sided_metric_carleson` | 4.365 | %86,2 | `rcarleson_general` |  |
| 12 | `metric_carleson` | 3.382 | %68,9 | `two_sided_metric_carleson` |  |
| 13 | `linearized_metric_carleson` | 3.228 | %66,9 | `metric_carleson` |  |
| 14 | `R_truncation` | 3.212 | %66,6 | `linearized_metric_carleson` |  |
| 15 | `R_truncation'` | 3.211 | %66,5 | `R_truncation` |  |
| 16 | `S_truncation` | 3.086 | %63,7 | `R_truncation'` |  |
| 17 | `linearized_truncation` | 3.076 | %63,5 | `S_truncation` |  |
| 18 | `finitary_carleson_step` | 3.035 | %63,0 | `linearized_truncation` |  |
| 19 | `finitary_carleson` | 3.023 | %62,8 | `finitary_carleson_step` |  |
| 20 | `discrete_carleson` | 2.578 | %53,7 | `finitary_carleson` |  |
| 21 | `forest_union` | 1.394 | %30,1 | `discrete_carleson` |  |
| 22 | `forest_union_optimized` | 1.381 | %30,0 | `forest_union` |  |
| 23 | `forest_union_aux` | 1.374 | %29,3 | `forest_union_optimized` |  |
| 24 | `lintegral_carlesonSum_forest'` | 1.214 | %26,6 | `forest_union_aux` |  |
| 25 | `lintegral_carlesonSum_forest` | 1.209 | %26,4 | `lintegral_carlesonSum_forest'` |  |
| 26 | `forest_operator_le_volume` | 1.086 | %24,2 | `lintegral_carlesonSum_forest` |  |
| 27 | `forest_operator'` | 1.085 | %24,2 | `forest_operator_le_volume` |  |
| 28 | `forest_operator` | 1.083 | %24,1 | `forest_operator'` |  |
| 29 | `TileStructure.Forest.forest_operator_g` | 522 | %12,9 | `forest_operator` |  |
| 30 | `forest_complement` | 597 | %12,8 | `discrete_carleson` |  |
| 31 | `TileStructure.Forest.forest_operator_g_main` | 518 | %12,7 | `TileStructure.Forest.forest_operator_g` |  |
| 32 | `forest_complement_optimized` | 591 | %12,7 | `forest_complement` |  |
| 33 | `TileStructure.Forest.row_correlation` | 471 | %12,0 | `TileStructure.Forest.forest_operator_g_main` |  |
| 34 | `TileStructure.Forest.correlation_separated_trees` | 455 | %11,5 | `TileStructure.Forest.row_correlation` |  |
| 35 | `TileStructure.Forest.correlation_separated_trees_of_subset` | 453 | %11,4 | `TileStructure.Forest.correlation_separated_trees` |  |
| 36 | `lintegral_enorm_carlesonSum_le_of_isAntichain_subset_ℭ` | 389 | %8,6 | `forest_complement_optimized` |  |
| 37 | `nontangential_from_simple` | 431 | %8,5 | `two_sided_metric_carleson` |  |
| 38 | `antichain_operator_le_volume` | 384 | %8,1 | `lintegral_enorm_carlesonSum_le_of_isAntichain_subset_ℭ` |  |
| 39 | `antichain_operator'` | 383 | %8,1 | `antichain_operator_le_volume` |  |
| 40 | `antichain_operator` | 382 | %8,0 | `antichain_operator'` |  |
| 41 | `simple_nontangential_operator_le` | 396 | %7,8 | `nontangential_from_simple` |  |
| 42 | `TileStructure.Forest.correlation_distant_tree_parts` | 267 | %7,5 | `TileStructure.Forest.correlation_separated_trees_of_subset` |  |
| 43 | `simple_nontangential_operator` | 383 | %7,5 | `simple_nontangential_operator_le` |  |
| 44 | `hasStrongType_maximalFunction_one` | 398 | %7,2 | `two_sided_metric_carleson` |  |
| 45 | `TileStructure.Forest.tree_projection_estimate` | 302 | %7,1 | `forest_operator` |  |
| 46 | `MeasureTheory.exists_hasStrongType_real_interpolation` | 369 | %6,9 | `hasStrongType_maximalFunction_one` |  |
| 47 | `cotlar_estimate` | 336 | %6,3 | `simple_nontangential_operator` |  |
| 48 | `dens1_antichain` | 316 | %6,2 | `antichain_operator` |  |
| 49 | `dens1_antichain_sq` | 315 | %6,2 | `dens1_antichain` |  |
| 50 | `TileStructure.Forest.holder_correlation_tree` | 198 | %6,2 | `TileStructure.Forest.correlation_distant_tree_parts` |  |


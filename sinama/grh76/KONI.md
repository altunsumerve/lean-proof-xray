# Koni / Cone — ispat konisi ve baskınlık ağacı / proof cone and dominator tree

Kök / root: `riemannHypothesis`

Bu sayfadaki sayılar resmi Lean kaydının (lean4export) bağımlılık grafiğinden hesaplanır; tahmin içermez. / All numbers on this page are computed from the dependency graph of the official Lean export.

## 1. Sayılar / Numbers

| | Bildirim / declarations | İfade ağırlığı / expression weight |
|---|---:|---:|
| Kayıttaki toplam / total in the export | 209.626 | 93.308.866 |
| Kütüphane (Mathlib ve altı) / library | 171.856 | 31.084.672 |
| Proje / project | 37.770 | 62.224.194 |
| &nbsp;&nbsp;kökün ispat konisinde / in the root's proof cone | 37.561 (%99,4) | 62.224.194 (%100,0) |
| &nbsp;&nbsp;**kullanılmayan / unused by the root** | **209** (%0,6) | 0 (%0,0) |
| Kökün önermesini anlamak için gereken proje bildirimi / project declarations needed to read the root's statement | 1 | |
| Konideki kütüphane bildirimi / library declarations in the cone | 170.189 | |

> Not / note: bu satır yalnızca girdideki kaydı sayar. Kayıt belirli teoremler için dışa aktarıldıysa yalnızca onların gerektirdiğini içerir; o teoremlerin kullanmadığı proje kodu kayıtta yoktur ve burada sayılmaz. / This row counts only what is in the input record. A record exported for specific theorems contains only what they need, so project code those theorems do not use is absent from it and is not counted here.

İfade ağırlığı: bildirimin kayda eklediği yeni ifade düğümü sayısı (ispatın büyüklüğünün ölçüsü). / Expression weight: number of new expression nodes the declaration added to the export.

| Tür / kind | Projede / in project | Konide / in cone |
|---|---:|---:|
| teorem | 30.418 | 30.418 |
| tanım | 6.598 | 6.598 |
| kurucu | 252 | 252 |
| tip | 251 | 251 |
| özyineleyici | 251 | 42 |

## 1b. Aksiyomlar / Axioms

Kökün ispat konisindeki aksiyom: **3** (kayıttaki toplam aksiyom: 3; kütüphane dahil, hiçbiri atlanmadı). Lean'in üç standart aksiyomu dışında kalan: **0**. / Axioms in the root's proof cone: 3 (axioms in the export: 3; library included). Outside Lean's three standard axioms: 0.

| Aksiyom / axiom | Not / note |
|---|---|
| `Classical.choice` | standart / standard |
| `Quot.sound` | standart / standard |
| `propext` | standart / standard |

Bu liste kayıttaki `axiom` bildirimlerinden okunur; ispatı yeniden denetlemez (bunu Lean çekirdeği ve bağımsız denetleyiciler yapar). / Read from the `axiom` declarations of the export; it does not re-check the proof.

## 2. Kullanılmayan kod / Unused code

Kökün ispatına hiç girmeyen proje bildirimi: **209** (bunların 209 tanesi Lean'in otomatik yardımcısı). / Project declarations never used by the root's proof: 209 (209 of them Lean-generated auxiliaries).

| Ad alanı / namespace | Bildirim | Ağırlık / weight |
|---|---:|---:|
| `Lift.KummerChart` | 3 | 0 |
| `Lift.Chart` | 2 | 0 |
| `PrimeSevenModEight.rec` | 1 | 0 |
| `PlaceEmbedding.rec` | 1 | 0 |
| `CMType.rec` | 1 | 0 |
| `IsProGalois.rec` | 1 | 0 |
| `Space.IsStd` | 1 | 0 |
| `PadicPlace.rec` | 1 | 0 |
| `StablyUnram.rec` | 1 | 0 |
| `SplittingChar.rec` | 1 | 0 |
| `Heisenberg.rec` | 1 | 0 |
| `EmbeddedNumberField.rec` | 1 | 0 |
| `IsLocalGalois.rec` | 1 | 0 |
| `IsPadicAt.rec` | 1 | 0 |
| `IsCompletionEmb.rec` | 1 | 0 |
| `PadicField.rec` | 1 | 0 |
| `DiscreteModule.rec` | 1 | 0 |
| `IsCovolOneLattice.rec` | 1 | 0 |
| `IsDualFamily.rec` | 1 | 0 |
| `Heisenberg.Rep` | 1 | 0 |

## 3. Kopya önermeler / Duplicate statements

Proje teoremi: 30.418. Önermesi (tipi) başka bir teoreminkiyle yapısal olarak aynı olan gruplar: **1.630**; fazladan kopya: **7.901** (%26,0). Yardımcı adlar hariç: 0 grup, 0 fazladan kopya. / Project theorems: 30.418. Groups whose statement (type) is structurally identical: 1.630; redundant copies: 7.901. Excluding auxiliary names: 0 groups, 0 redundant copies.

Not: parmak izi 64 bit ve yapısaldır (bağlı değişken adları sayılmaz); evren parametre adları farklıysa kopya sayılmaz. / The fingerprint is 64-bit and structural.

## 4. Baskınlık ağacı / Dominator tree

X, Y'nin üstündeyse kökten Y'ye giden her bağımlılık yolu X'ten geçer: Y yalnızca X için vardır. Bir satırın alt ağacı, makalede o başlığın altına girecek her şeydir. / If X is above Y, every dependency path from the root to Y passes through X.

Ağaçtaki düğüm: 37.561; kökün doğrudan çocukları: 4; en derin düzey: 17.

| Alt ağaç büyüklüğü / subtree size | Düğüm / nodes |
|---|---:|
| ≥ 10 bildirim | 793 |
| ≥ 100 bildirim | 87 |
| ≥ 1.000 bildirim | 20 |
| ≥ 10.000 bildirim | 4 |
| ≥ 100.000 bildirim | 0 |

Aşağıda ağırlığı toplamın en az %0,5'i olan dallar (en çok 5 düzey). Sütunlar: alt ağaçtaki bildirim, ağırlık payı, bu bildirimi doğrudan kullanan sayısı.

```
riemannHypothesis  [teorem]  alt=37.561  %100,0  kullanan=1
  New.grh  [teorem]  alt=37.555  %100,0  kullanan=1
    eventually_primeError_le_rpow  [teorem]  alt=37.276  %99,7  kullanan=1
      star_inequality  [teorem]  alt=32.541  %93,4  kullanan=1
        Data.integral_forms_long  [teorem]  alt=5.913  %20,2  kullanan=1
          exists_isFitFamily  [teorem]  alt=3.591  %11,5  kullanan=1
          Data.heightLe_volume_ratio_sq  [teorem]  alt=1.362  %4,7  kullanan=1
          Data.heightLe_volume_rows  [teorem]  alt=544  %2,9  kullanan=1
          … ve 153 küçük çocuk daha
        sphericalCompat_of_odd  [teorem]  alt=6.179  %19,1  kullanan=2
          sphericalCompat_of_split  [teorem]  alt=6.161  %18,9  kullanan=1
          … ve 14 küçük çocuk daha
        Data.exists_family_covolumeSq_le  [teorem]  alt=2.196  %7,8  kullanan=1
          Data.seesaw  [teorem]  alt=978  %4,2  kullanan=4
          Data.short_forms  [teorem]  alt=1.087  %3,5  kullanan=1
          … ve 93 küçük çocuk daha
        Data.ramifiedColumns_fill_rows  [teorem]  alt=1.440  %5,4  kullanan=2
          Filling.Fits.exists_translate_finrank_comap_le  [teorem]  alt=1.391  %5,2  kullanan=1
          … ve 20 küçük çocuk daha
        exchange_theorem  [teorem]  alt=930  %3,8  kullanan=2
          stdExchange_of_periods  [teorem]  alt=187  %1,2  kullanan=2
          exists_constant_term_thetaLarge  [teorem]  alt=108  %0,7  kullanan=2
          … ve 283 küçük çocuk daha
        Data.exists_besselSystem  [teorem]  alt=460  %1,3  kullanan=8
          hasBandLimits_of_isCutBessel  [teorem]  alt=284  %0,7  kullanan=1
          … ve 76 küçük çocuk daha
        exists_isWeakBaseChange_of_matching  [teorem]  alt=172  %1,1  kullanan=3
          twisted_trace_identity  [teorem]  alt=77  %0,6  kullanan=1
          … ve 35 küçük çocuk daha
        Data.exists_isTriangle  [teorem]  alt=79  %0,9  kullanan=3
          … ve 44 küçük çocuk daha
        Data.hasGap_gridParam  [teorem]  alt=8  %0,8  kullanan=8
          Data.hasGap_gridParam._proof_1_6  [teorem]  alt=1  %0,5  kullanan=1
          … ve 6 küçük çocuk daha
        Attached.local_global_of_eigencharacter  [teorem]  alt=140  %0,7  kullanan=2
          … ve 23 küçük çocuk daha
        Orbital.harish_chandra_degree_and_orbital  [teorem]  alt=319  %0,7  kullanan=3
          … ve 73 küçük çocuk daha
        Filling.exists_isFillingLevel  [teorem]  alt=53  %0,6  kullanan=4
          IntegralPlace.exists_isLatticeLevel  [teorem]  alt=18  %0,6  kullanan=1
          … ve 22 küçük çocuk daha
        Data.exists_isSteep  [teorem]  alt=11  %0,6  kullanan=2
          … ve 9 küçük çocuk daha
        Attached.isLabelledAt  [teorem]  alt=103  %0,6  kullanan=3
          … ve 19 küçük çocuk daha
        Data.paramsCorrespond_grid  [teorem]  alt=29  %0,6  kullanan=6
          … ve 28 küçük çocuk daha
        local_clauses_of_trace_limit  [teorem]  alt=75  %0,6  kullanan=3
          … ve 31 küçük çocuk daha
        CMLattice.exists_formal_parameter  [teorem]  alt=123  %0,5  kullanan=2
          … ve 59 küçük çocuk daha
        … ve 6.895 küçük çocuk daha
      … ve 2.454 küçük çocuk daha
    … ve 78 küçük çocuk daha
  … ve 3 küçük çocuk daha
```

## 5. En büyük kilometre taşları / Largest milestones

Kök dışındaki, yardımcı olmayan teoremler; alt ağaç ağırlığına göre. Önerme metni projenin kaynağından alınmıştır (atlas verildiyse). / Non-auxiliary theorems other than the root, by subtree weight; statement text is from the source when available.

| # | Teorem | Alt ağaç | Pay | Üstü / dominator | Kaynak |
|---:|---|---:|---:|---|---|
| 1 | `New.grh` | 37.555 | %100,0 | `riemannHypothesis` |  |
| 2 | `eventually_primeError_le_rpow` | 37.276 | %99,7 | `New.grh` |  |
| 3 | `star_inequality` | 32.541 | %93,4 | `eventually_primeError_le_rpow` |  |
| 4 | `Data.integral_forms_long` | 5.913 | %20,2 | `star_inequality` |  |
| 5 | `sphericalCompat_of_odd` | 6.179 | %19,1 | `star_inequality` |  |
| 6 | `sphericalCompat_of_split` | 6.161 | %18,9 | `sphericalCompat_of_odd` |  |
| 7 | `exists_rep_of_cuspidal_type` | 6.004 | %18,2 | `sphericalCompat_of_split` |  |
| 8 | `exists_isFitFamily` | 3.591 | %11,5 | `Data.integral_forms_long` |  |
| 9 | `Model.exists_galois_rep` | 3.289 | %10,4 | `exists_rep_of_cuspidal_type` |  |
| 10 | `Data.exists_family_covolumeSq_le` | 2.196 | %7,8 | `star_inequality` |  |
| 11 | `denominatorLe_rowBudget` | 2.104 | %7,0 | `exists_isFitFamily` |  |
| 12 | `Data.ramifiedColumns_fill_rows` | 1.440 | %5,4 | `star_inequality` |  |
| 13 | `Filling.Fits.exists_translate_finrank_comap_le` | 1.391 | %5,2 | `Data.ramifiedColumns_fill_rows` |  |
| 14 | `ribet_columns` | 1.644 | %4,8 | `denominatorLe_rowBudget` |  |
| 15 | `Data.heightLe_volume_ratio_sq` | 1.362 | %4,7 | `Data.integral_forms_long` |  |
| 16 | `Data.heightLe_liftVolume_ratio` | 1.358 | %4,7 | `Data.heightLe_volume_ratio_sq` |  |
| 17 | `Data.seesaw` | 978 | %4,2 | `Data.exists_family_covolumeSq_le` |  |
| 18 | `sum_blockLoss_le` | 1.486 | %3,9 | `ribet_columns` |  |
| 19 | `exchange_theorem` | 930 | %3,8 | `star_inequality` |  |
| 20 | `Data.short_forms` | 1.087 | %3,5 | `Data.exists_family_covolumeSq_le` |  |
| 21 | `block_defect_le_at_place` | 1.324 | %3,2 | `sum_blockLoss_le` |  |
| 22 | `Data.exists_indexDvd_Bmu_divisible` | 977 | %3,2 | `Data.short_forms` |  |
| 23 | `Filling.energy_le_of_linkEnergy_le` | 700 | %3,0 | `Filling.Fits.exists_translate_finrank_comap_le` |  |
| 24 | `Data.heightLe_volume_rows` | 544 | %2,9 | `Data.integral_forms_long` |  |
| 25 | `Data.crude_rows` | 532 | %2,9 | `Data.heightLe_volume_rows` |  |
| 26 | `exists_comparison_forms` | 805 | %2,6 | `Data.heightLe_liftVolume_ratio` |  |
| 27 | `ellAdicCohom.woods_hole` | 463 | %2,6 | `Model.exists_galois_rep` |  |
| 28 | `Filling.energy_le_of_level_pairs` | 579 | %2,5 | `Filling.energy_le_of_linkEnergy_le` |  |
| 29 | `nonempty_universalFamily` | 634 | %2,1 | `exists_rep_of_cuspidal_type` |  |
| 30 | `Data.IsMarked.hasType_prod_markOperator_pow` | 517 | %1,7 | `Data.exists_indexDvd_Bmu_divisible` |  |
| 31 | `Data.IsMarked.hasType_markOperator` | 506 | %1,6 | `Data.IsMarked.hasType_prod_markOperator_pow` |  |
| 32 | `Columns.hasType_markOperator` | 470 | %1,6 | `Data.IsMarked.hasType_markOperator` |  |
| 33 | `exists_mFoldTwist_selmerLengthLe` | 389 | %1,5 | `exists_isFitFamily` |  |
| 34 | `Filling.sum_le_of_positive_type` | 387 | %1,4 | `Filling.Fits.exists_translate_finrank_comap_le` |  |
| 35 | `TwistingData.hasType_twisted_hecke` | 421 | %1,4 | `Columns.hasType_markOperator` |  |
| 36 | `Filling.energy_fixingSet_le` | 351 | %1,4 | `Filling.sum_le_of_positive_type` |  |
| 37 | `linearIndepOn_hodgeTateMap_pointClass` | 198 | %1,4 | `ellAdicCohom.woods_hole` |  |
| 38 | `crystalline_defect_le` | 268 | %1,3 | `block_defect_le_at_place` |  |
| 39 | `Data.exists_besselSystem` | 460 | %1,3 | `star_inequality` |  |
| 40 | `Data.exists_isAdmissibleComb_unfolding` | 247 | %1,2 | `Data.seesaw` |  |
| 41 | `ellAdicCohom.isCrystalline_and_linearFrob_rel` | 251 | %1,2 | `Model.exists_galois_rep` |  |
| 42 | `Data.heightLe_inv_heckeValueProd_div` | 331 | %1,2 | `Data.heightLe_liftVolume_ratio` |  |
| 43 | `Data.heightLe_inv_ratio` | 322 | %1,2 | `Data.heightLe_inv_heckeValueProd_div` |  |
| 44 | `stdExchange_of_periods` | 187 | %1,2 | `exchange_theorem` |  |
| 45 | `exists_isWeakBaseChange_of_matching` | 172 | %1,1 | `star_inequality` |  |
| 46 | `exists_anticyclotomic_twist` | 260 | %1,1 | `exists_mFoldTwist_selmerLengthLe` |  |
| 47 | `Filling.enorm_amplitudeSum_le_classSize` | 253 | %1,0 | `Filling.energy_le_of_level_pairs` |  |
| 48 | `Data.eq_zero_of_integral_fNatural_tableTheta` | 268 | %0,9 | `exists_comparison_forms` |  |
| 49 | `span_range_crysComparison_pull_eq_top` | 166 | %0,9 | `ellAdicCohom.isCrystalline_and_linearFrob_rel` |  |
| 50 | `Data.exists_isTriangle` | 79 | %0,9 | `star_inequality` |  |


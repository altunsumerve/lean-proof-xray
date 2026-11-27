# Koni / Cone — ispat konisi ve baskınlık ağacı / proof cone and dominator tree

Kök / root: `riemannHypothesis`

Bu sayfadaki sayılar resmi Lean kaydının (lean4export) bağımlılık grafiğinden hesaplanır; tahmin içermez. / All numbers on this page are computed from the dependency graph of the official Lean export.

## 1. Sayılar / Numbers

| | Bildirim / declarations | İfade ağırlığı / expression weight |
|---|---:|---:|
| Kayıttaki toplam / total in the export | 222.105 | 80.683.079 |
| Kütüphane (Mathlib ve altı) / library | 171.830 | 31.123.169 |
| Proje / project | 50.275 | 49.559.910 |
| &nbsp;&nbsp;kökün ispat konisinde / in the root's proof cone | 49.815 (%99,1) | 49.559.910 (%100,0) |
| &nbsp;&nbsp;**kullanılmayan / unused by the root** | **460** (%0,9) | 0 (%0,0) |
| Kökün önermesini anlamak için gereken proje bildirimi / project declarations needed to read the root's statement | 1 | |
| Konideki kütüphane bildirimi / library declarations in the cone | 170.155 | |

> Not / note: bu satır yalnızca girdideki kaydı sayar. Kayıt belirli teoremler için dışa aktarıldıysa yalnızca onların gerektirdiğini içerir; o teoremlerin kullanmadığı proje kodu kayıtta yoktur ve burada sayılmaz. / This row counts only what is in the input record. A record exported for specific theorems contains only what they need, so project code those theorems do not use is absent from it and is not counted here.

İfade ağırlığı: bildirimin kayda eklediği yeni ifade düğümü sayısı (ispatın büyüklüğünün ölçüsü). / Expression weight: number of new expression nodes the declaration added to the export.

| Tür / kind | Projede / in project | Konide / in cone |
|---|---:|---:|
| teorem | 42.204 | 42.204 |
| tanım | 6.598 | 6.598 |
| kurucu | 495 | 495 |
| tip | 489 | 489 |
| özyineleyici | 489 | 29 |

## 1b. Aksiyomlar / Axioms

Kökün ispat konisindeki aksiyom: **3** (kayıttaki toplam aksiyom: 3; kütüphane dahil, hiçbiri atlanmadı). Lean'in üç standart aksiyomu dışında kalan: **0**. / Axioms in the root's proof cone: 3 (axioms in the export: 3; library included). Outside Lean's three standard axioms: 0.

| Aksiyom / axiom | Not / note |
|---|---|
| `Classical.choice` | standart / standard |
| `Quot.sound` | standart / standard |
| `propext` | standart / standard |

Bu liste kayıttaki `axiom` bildirimlerinden okunur; ispatı yeniden denetlemez (bunu Lean çekirdeği ve bağımsız denetleyiciler yapar). / Read from the `axiom` declarations of the export; it does not re-check the proof.

## 2. Kullanılmayan kod / Unused code

Kökün ispatına hiç girmeyen proje bildirimi: **460** (bunların 460 tanesi Lean'in otomatik yardımcısı). / Project declarations never used by the root's proof: 460 (460 of them Lean-generated auxiliaries).

| Ad alanı / namespace | Bildirim | Ağırlık / weight |
|---|---:|---:|
| `New.Variety` | 71 | 0 |
| `New.Selmer` | 30 | 0 |
| `New.Data` | 28 | 0 |
| `New.Lift` | 21 | 0 |
| `New.Floors` | 20 | 0 |
| `New.Exchange` | 16 | 0 |
| `New.Filling` | 15 | 0 |
| `New.DiscreteSeries` | 9 | 0 |
| `New.Parameters` | 8 | 0 |
| `New.Space` | 7 | 0 |
| `_private.Lib` | 7 | 0 |
| `New.Seesaw` | 6 | 0 |
| `New.Period` | 6 | 0 |
| `New.GaloisRep` | 6 | 0 |
| `New.Rows` | 6 | 0 |
| `New.Heisenberg` | 5 | 0 |
| `New.FrobeniusCycle` | 5 | 0 |
| `New.RealPlace` | 5 | 0 |
| `New.ThetaTori` | 5 | 0 |
| `New.OddPart` | 4 | 0 |

## 3. Kopya önermeler / Duplicate statements

Proje teoremi: 42.204. Önermesi (tipi) başka bir teoreminkiyle yapısal olarak aynı olan gruplar: **1.607**; fazladan kopya: **8.586** (%20,3). Yardımcı adlar hariç: 9 grup, 9 fazladan kopya. / Project theorems: 42.204. Groups whose statement (type) is structurally identical: 1.607; redundant copies: 8.586. Excluding auxiliary names: 9 groups, 9 redundant copies.

Not: parmak izi 64 bit ve yapısaldır (bağlı değişken adları sayılmaz); evren parametre adları farklıysa kopya sayılmaz. / The fingerprint is 64-bit and structural.

| Kopya sayısı | Konide | Örnek adlar / example names |
|---:|---:|---|
| 2 | 2 | `New.CMLattice.mem_valRingCp_iff_norm_le_one`, `New.mem_valRingCp` |
| 2 | 2 | `New.Data.targetParameter_k_sub_one_add`, `New.Data.targetParameter_sub_one_add` |
| 2 | 2 | `New.dvd_iff_norm_le`, `New.valRingCp.dvd_iff_norm_le` |
| 2 | 2 | `New.RealPlace.realFrameGram_eq_conjTranspose_mul`, `New.RealPlace.realFrameGram_eq` |
| 2 | 2 | `New.radicalHom_sub_eq._abel_1_1`, `New.diagonal_blocks_mul_radical._abel_1_1` |
| 2 | 2 | `New.Variety.isReduced_of_algebra_etale`, `New.Variety.isReduced_of_etale` |
| 2 | 2 | `New.LineBundle.isHomogeneousCoords_mul_prod`, `New.LineBundle.IsHomogeneousCoords.mul` |
| 2 | 2 | `New.Data.CriticalPair.L_inv_mul`, `New.Data.CriticalPair.L_mul_inv` |
| 2 | 2 | `New.Lift.KummerChart.JumpLattice.tau_pow_smul_mem_kisinAinf`, `New.Lift.KummerChart.JumpLattice.tau_pow_jumpBound_smul_mem_kisinAinf_of_mem_ainfLattice` |

## 4. Baskınlık ağacı / Dominator tree

X, Y'nin üstündeyse kökten Y'ye giden her bağımlılık yolu X'ten geçer: Y yalnızca X için vardır. Bir satırın alt ağacı, makalede o başlığın altına girecek her şeydir. / If X is above Y, every dependency path from the root to Y passes through X.

Ağaçtaki düğüm: 49.815; kökün doğrudan çocukları: 4; en derin düzey: 36.

| Alt ağaç büyüklüğü / subtree size | Düğüm / nodes |
|---|---:|
| ≥ 10 bildirim | 1.692 |
| ≥ 100 bildirim | 245 |
| ≥ 1.000 bildirim | 33 |
| ≥ 10.000 bildirim | 10 |
| ≥ 100.000 bildirim | 0 |

Aşağıda ağırlığı toplamın en az %0,5'i olan dallar (en çok 5 düzey). Sütunlar: alt ağaçtaki bildirim, ağırlık payı, bu bildirimi doğrudan kullanan sayısı.

```
riemannHypothesis  [teorem]  alt=49.815  %100,0  kullanan=1
  New.grh  [teorem]  alt=49.807  %100,0  kullanan=1
    New.eventually_primeRemainder_le_rpow  [teorem]  alt=49.589  %99,7  kullanan=1
      New.eventually_primeRemainder_natCast_le  [teorem]  alt=49.556  %99,7  kullanan=1
        New.Data.primeRemainder_le  [teorem]  alt=44.867  %93,8  kullanan=1
          New.star_inequality  [teorem]  alt=44.766  %93,8  kullanan=1
          … ve 60 küçük çocuk daha
        … ve 2.487 küçük çocuk daha
      … ve 17 küçük çocuk daha
    … ve 40 küçük çocuk daha
  … ve 3 küçük çocuk daha
```

## 5. En büyük kilometre taşları / Largest milestones

Kök dışındaki, yardımcı olmayan teoremler; alt ağaç ağırlığına göre. Önerme metni projenin kaynağından alınmıştır (atlas verildiyse). / Non-auxiliary theorems other than the root, by subtree weight; statement text is from the source when available.

| # | Teorem | Alt ağaç | Pay | Üstü / dominator | Kaynak |
|---:|---|---:|---:|---|---|
| 1 | `New.grh` | 49.807 | %100,0 | `riemannHypothesis` |  |
| 2 | `New.eventually_primeRemainder_le_rpow` | 49.589 | %99,7 | `New.grh` |  |
| 3 | `New.eventually_primeRemainder_natCast_le` | 49.556 | %99,7 | `New.eventually_primeRemainder_le_rpow` |  |
| 4 | `New.Data.primeRemainder_le` | 44.867 | %93,8 | `New.eventually_primeRemainder_natCast_le` |  |
| 5 | `New.star_inequality` | 44.766 | %93,8 | `New.Data.primeRemainder_le` |  |
| 6 | `New.Data.integral_forms_long` | 23.157 | %55,7 | `New.star_inequality` |  |
| 7 | `New.Data.exists_hasSmallRatios_heightLe_liftDeterminant_div` | 18.953 | %46,6 | `New.Data.integral_forms_long` |  |
| 8 | `New.exists_isRegularFamily` | 16.098 | %40,2 | `New.Data.exists_hasSmallRatios_heightLe_liftDeterminant_div` |  |
| 9 | `New.Selmer.exists_mFoldTwist_hasDenominatorsLe` | 15.519 | %35,1 | `New.exists_isRegularFamily` |  |
| 10 | `New.GaloisRep.sphericalCompat_of_odd` | 6.898 | %17,1 | `New.Selmer.exists_mFoldTwist_hasDenominatorsLe` |  |
| 11 | `New.GaloisRep.sphericalCompat_of_split` | 6.881 | %17,0 | `New.GaloisRep.sphericalCompat_of_odd` |  |
| 12 | `New.GaloisRep.exists_rep_of_cuspidal_type` | 6.706 | %16,4 | `_private.Lib.GaloisRep.Main.SplitCase.#0.New.GaloisRep.exists_rep_of_free_weight` |  |
| 13 | `New.Variety.Model.exists_galois_rep` | 3.600 | %9,4 | `_private.Lib.GaloisRep.Main.SeedRepresentation.#0.New.GaloisRep.exists_padicRep_of_pel` |  |
| 14 | `New.Selmer.denominatorLe_clearingBound` | 3.227 | %7,2 | `New.Selmer.exists_mFoldTwist_hasDenominatorsLe` |  |
| 15 | `New.Selmer.exists_operator_det_clearingBound` | 3.226 | %7,2 | `New.Selmer.denominatorLe_clearingBound` |  |
| 16 | `New.Selmer.exists_operator_ellVal_le_liftValuationBound` | 3.210 | %7,1 | `New.Selmer.exists_operator_det_clearingBound` |  |
| 17 | `New.Selmer.exists_linearMap_eq_smul_mem_integralForms` | 3.198 | %7,1 | `New.Selmer.exists_operator_ellVal_le_liftValuationBound` |  |
| 18 | `New.Selmer.exists_ellVal_le_and_diagOp_mem_ellIntegralForms` | 2.942 | %6,4 | `New.Selmer.exists_linearMap_eq_smul_mem_integralForms` |  |
| 19 | `New.Data.heightLe_liftDeterminant_ratio` | 2.222 | %5,3 | `New.Data.exists_hasSmallRatios_heightLe_liftDeterminant_div` |  |
| 20 | `New.Selmer.exists_isCommonRibetElement_ellVal_le` | 2.357 | %5,0 | `New.Selmer.exists_ellVal_le_and_diagOp_mem_ellIntegralForms` |  |
| 21 | `New.Selmer.ribet_columns` | 2.356 | %5,0 | `New.Selmer.exists_isCommonRibetElement_ellVal_le` |  |
| 22 | `New.Selmer.sum_clearingBound_add_padicValNat_le` | 17 | %4,3 | `New.exists_isRegularFamily` |  |
| 23 | `New.Selmer.isNegligible_denominatorError` | 7 | %4,2 | `New.Selmer.sum_clearingBound_add_padicValNat_le` |  |
| 24 | `New.Selmer.isNegligible_padicValNat_oddClassBound` | 5 | %4,2 | `New.Selmer.isNegligible_denominatorError` |  |
| 25 | `New.Data.seesaw_identity` | 1.437 | %3,9 | `New.star_inequality` |  |
| 26 | `New.Exchange.exchange_identity` | 1.482 | %3,9 | `New.Data.integral_forms_long` |  |
| 27 | `New.Exchange.exchange_theorem` | 1.480 | %3,9 | `New.Exchange.exchange_identity` |  |
| 28 | `New.Data.exists_err_gaugeLe_compositeLift` | 1.757 | %3,3 | `New.star_inequality` |  |
| 29 | `New.Data.exists_colengthDvd_gaugeLe_compositeLift` | 1.731 | %3,3 | `New.Data.exists_err_gaugeLe_compositeLift` |  |
| 30 | `New.Variety.Model.jumpsRelAt_of_isEigenQuotient` | 937 | %3,2 | `New.Variety.Model.exists_galois_rep` |  |
| 31 | `New.Selmer.eventually_exists_inClass_sum_dualDefect_le` | 1.871 | %3,1 | `New.Selmer.ribet_columns` |  |
| 32 | `New.Selmer.summand_defect_le_at_place` | 1.854 | %3,1 | `New.Selmer.eventually_exists_inClass_sum_dualDefect_le` |  |
| 33 | `New.Selmer.normLength_dualDefect_le_of_isSummandClass` | 1.851 | %3,1 | `New.Selmer.summand_defect_le_at_place` |  |
| 34 | `New.Variety.Model.isNullHecke_mul_of_kills_weight` | 926 | %3,0 | `New.Variety.Model.jumpsRelAt_of_isEigenQuotient` |  |
| 35 | `New.Data.isComparisonOperator_comparisonOp` | 841 | %2,2 | `New.Data.heightLe_liftDeterminant_ratio` |  |
| 36 | `New.Variety.ellAdicCohom.woods_hole` | 579 | %2,1 | `New.Variety.Model.isNullHecke_mul_of_kills_weight` |  |
| 37 | `New.Data.exists_span_isAuxiliaryForm_eq_top` | 989 | %2,1 | `New.Data.integral_forms_long` |  |
| 38 | `New.Data.exists_span_short_lifts_eq_top` | 986 | %2,1 | `New.Data.exists_span_isAuxiliaryForm_eq_top` |  |
| 39 | `New.Data.exists_lowerChainUpTo_poincareAt_eq` | 632 | %2,0 | `New.Data.seesaw_identity` |  |
| 40 | `New.Data.exists_lowerChain_integral_and_weylNormSq_le` | 929 | %2,0 | `New.Data.exists_span_short_lifts_eq_top` |  |
| 41 | `New.Variety.ThetaNull.nonempty_universalFamily` | 752 | %1,9 | `_private.Lib.GaloisRep.Main.SeedRepresentation.#0.New.GaloisRep.exists_padicRep_of_pel` |  |
| 42 | `New.Data.enough_forms` | 784 | %1,7 | `New.star_inequality` |  |
| 43 | `New.Data.exists_le_finrank_iSup_range_normalizedPoincare` | 782 | %1,7 | `New.Data.enough_forms` |  |
| 44 | `New.Selmer.exists_mFoldTwist_selmerLengthLe_inv_ratio_le` | 949 | %1,7 | `New.Selmer.exists_mFoldTwist_hasDenominatorsLe` |  |
| 45 | `New.Selmer.exists_mFoldTwist_hasDivisibleSelmerLengthLe` | 946 | %1,7 | `New.Selmer.exists_mFoldTwist_selmerLengthLe_inv_ratio_le` |  |
| 46 | `New.Data.isSpread_goodPoincare` | 766 | %1,7 | `New.Data.exists_le_finrank_iSup_range_normalizedPoincare` |  |
| 47 | `New.Data.targetDim_mul_sum_hilbertSchmidtNorm_sq_le` | 757 | %1,6 | `New.Data.isSpread_goodPoincare` |  |
| 48 | `New.Data.sum_hilbertSchmidtNorm_scaledPoincare_sq_le` | 751 | %1,6 | `New.Data.targetDim_mul_sum_hilbertSchmidtNorm_sq_le` |  |
| 49 | `New.Filling.HasAmplitudeBlocks.sum_hilbertSchmidtNorm_sq_le` | 750 | %1,6 | `New.Data.sum_hilbertSchmidtNorm_scaledPoincare_sq_le` |  |
| 50 | `New.Filling.sum_secondMoment_le` | 747 | %1,6 | `New.Filling.HasAmplitudeBlocks.sum_hilbertSchmidtNorm_sq_le` |  |


# Koni / Cone — ispat konisi ve baskınlık ağacı / proof cone and dominator tree

Kök / root: `PFR_conjecture`

Bu sayfadaki sayılar resmi Lean kaydının (lean4export) bağımlılık grafiğinden hesaplanır; tahmin içermez. / All numbers on this page are computed from the dependency graph of the official Lean export.

## 1. Sayılar / Numbers

| | Bildirim / declarations | İfade ağırlığı / expression weight |
|---|---:|---:|
| Kayıttaki toplam / total in the export | 52.360 | 6.016.221 |
| Kütüphane (Mathlib ve altı) / library | 51.698 | 5.604.081 |
| Proje / project | 662 | 412.140 |
| &nbsp;&nbsp;kökün ispat konisinde / in the root's proof cone | 658 (%99,4) | 412.140 (%100,0) |
| &nbsp;&nbsp;**kullanılmayan / unused by the root** | **4** (%0,6) | 0 (%0,0) |
| Kökün önermesini anlamak için gereken proje bildirimi / project declarations needed to read the root's statement | 1 | |
| Konideki kütüphane bildirimi / library declarations in the cone | 50.918 | |

İfade ağırlığı: bildirimin kayda eklediği yeni ifade düğümü sayısı (ispatın büyüklüğünün ölçüsü). / Expression weight: number of new expression nodes the declaration added to the export.

| Tür / kind | Projede / in project | Konide / in cone |
|---|---:|---:|
| teorem | 582 | 582 |
| tanım | 68 | 68 |
| kurucu | 4 | 4 |
| tip | 4 | 4 |
| özyineleyici | 4 | 0 |

## 1b. Aksiyomlar / Axioms

Kökün ispat konisindeki aksiyom: **3** (kayıttaki toplam aksiyom: 3; kütüphane dahil, hiçbiri atlanmadı). Lean'in üç standart aksiyomu dışında kalan: **0**. / Axioms in the root's proof cone: 3 (axioms in the export: 3; library included). Outside Lean's three standard axioms: 0.

| Aksiyom / axiom | Not / note |
|---|---|
| `Classical.choice` | standart / standard |
| `Quot.sound` | standart / standard |
| `propext` | standart / standard |

Bu liste kayıttaki `axiom` bildirimlerinden okunur; ispatı yeniden denetlemez (bunu Lean çekirdeği ve bağımsız denetleyiciler yapar). / Read from the `axiom` declarations of the export; it does not re-check the proof.

## 2. Kullanılmayan kod / Unused code

Kökün ispatına hiç girmeyen proje bildirimi: **4** (bunların 4 tanesi Lean'in otomatik yardımcısı). / Project declarations never used by the root's proof: 4 (4 of them Lean-generated auxiliaries).

| Ad alanı / namespace | Bildirim | Ağırlık / weight |
|---|---:|---:|
| `ProbabilityTheory.IsUniform` | 1 | 0 |
| `FiniteRange.rec` | 1 | 0 |
| `refPackage.rec` | 1 | 0 |
| `ProbabilityTheory.FiniteSupport` | 1 | 0 |

## 3. Kopya önermeler / Duplicate statements

Proje teoremi: 582. Önermesi (tipi) başka bir teoreminkiyle yapısal olarak aynı olan gruplar: **29**; fazladan kopya: **71** (%12,2). Yardımcı adlar hariç: 1 grup, 1 fazladan kopya. / Project theorems: 582. Groups whose statement (type) is structurally identical: 29; redundant copies: 71. Excluding auxiliary names: 1 groups, 1 redundant copies.

Not: parmak izi 64 bit ve yapısaldır (bağlı değişken adları sayılmaz); evren parametre adları farklıysa kopya sayılmaz. / The fingerprint is 64-bit and structural.

| Kopya sayısı | Konide | Örnek adlar / example names |
|---:|---:|---|
| 2 | 2 | `ProbabilityTheory.entropy_eq_sum_finset`, `ProbabilityTheory.entropy_eq_sum_finset'` |

## 4. Baskınlık ağacı / Dominator tree

X, Y'nin üstündeyse kökten Y'ye giden her bağımlılık yolu X'ten geçer: Y yalnızca X için vardır. Bir satırın alt ağacı, makalede o başlığın altına girecek her şeydir. / If X is above Y, every dependency path from the root to Y passes through X.

Ağaçtaki düğüm: 658; kökün doğrudan çocukları: 8; en derin düzey: 14.

| Alt ağaç büyüklüğü / subtree size | Düğüm / nodes |
|---|---:|
| ≥ 10 bildirim | 33 |
| ≥ 100 bildirim | 5 |
| ≥ 1.000 bildirim | 0 |
| ≥ 10.000 bildirim | 0 |
| ≥ 100.000 bildirim | 0 |

Aşağıda ağırlığı toplamın en az %0,5'i olan dallar (en çok 5 düzey). Sütunlar: alt ağaçtaki bildirim, ağırlık payı, bu bildirimi doğrudan kullanan sayısı.

```
PFR_conjecture  [teorem]  alt=658  %100,0  kullanan=1
  PFR_conjecture_aux  [teorem]  alt=650  %97,7  kullanan=1
    entropic_PFR_conjecture  [teorem]  alt=368  %73,6  kullanan=1
      tau_strictly_decreases  [teorem]  alt=260  %59,4  kullanan=1
        tau_strictly_decreases_aux  [teorem]  alt=256  %56,1  kullanan=1
          cond_construct_good  [teorem]  alt=56  %13,1  kullanan=1
          sum_dist_diff_le  [teorem]  alt=57  %10,3  kullanan=1
          sum_condMutual_le  [teorem]  alt=19  %7,7  kullanan=1
          comparison_of_ruzsa_distances  [teorem]  alt=9  %3,4  kullanan=2
          sum_of_rdist_eq_char_2  [teorem]  alt=20  %3,3  kullanan=2
          condRuzsaDist_le'  [teorem]  alt=9  %3,2  kullanan=2
          condRuzsaDistance_ge_of_min  [teorem]  alt=11  %2,1  kullanan=2
          condRuzsaDist_of_indep  [teorem]  alt=8  %2,0  kullanan=3
          ent_ofsum_le  [teorem]  alt=3  %1,8  kullanan=2
          first_estimate  [teorem]  alt=4  %1,3  kullanan=1
          ProbabilityTheory.condMutualInfo_eq  [teorem]  alt=3  %0,9  kullanan=4
          ProbabilityTheory.iIndepFun.reindex_four_cbad  [teorem]  alt=1  %0,7  kullanan=2
          condRuzsaDist'_eq_sum  [teorem]  alt=2  %0,5  kullanan=3
          rdist_add_rdist_add_condMutual_eq  [teorem]  alt=3  %0,5  kullanan=2
          … ve 43 küçük çocuk daha
        _private.PFR.EntropyPFR.#0.tau_strictly_decreases.match_1_1  [tanım]  alt=1  %1,9  kullanan=1
        ProbabilityTheory.independent_copies4_nondep  [teorem]  alt=1  %1,1  kullanan=1
        … ve 1 küçük çocuk daha
      exists_isUniform_of_rdist_eq_zero  [teorem]  alt=20  %2,5  kullanan=1
        exists_isUniform_of_rdist_self_eq_zero  [teorem]  alt=19  %2,3  kullanan=1
          isUniform_sub_const_of_rdist_eq_zero  [teorem]  alt=9  %1,3  kullanan=1
          rdist_add_const  [teorem]  alt=3  %0,5  kullanan=1
          … ve 1 küçük çocuk daha
      ProbabilityTheory.independent_copies3_nondep_finiteRange  [teorem]  alt=4  %2,5  kullanan=2
        ProbabilityTheory.independent_copies3_nondep  [teorem]  alt=1  %0,9  kullanan=1
        … ve 1 küçük çocuk daha
      ProbabilityTheory.condEntropy_two_eq_kernel_entropy  [teorem]  alt=20  %1,8  kullanan=2
        ProbabilityTheory.condKernel_condDistrib_ae_eq  [teorem]  alt=8  %0,7  kullanan=1
          … ve 7 küçük çocuk daha
        … ve 3 küçük çocuk daha
      rdist_triangle  [teorem]  alt=3  %1,6  kullanan=2
        ent_of_diff_le  [teorem]  alt=2  %0,6  kullanan=1
          … ve 1 küçük çocuk daha
      tau_minimizer_exists  [teorem]  alt=14  %1,2  kullanan=1
        tau_min_exists_measure  [teorem]  alt=11  %0,9  kullanan=1
          continuous_tau_restrict_probabilityMeasure  [teorem]  alt=9  %0,8  kullanan=1
          … ve 1 küçük çocuk daha
        … ve 2 küçük çocuk daha
      ProbabilityTheory.entropy_triple_add_entropy_le  [teorem]  alt=9  %0,9  kullanan=3
        ProbabilityTheory.entropy_submodular  [teorem]  alt=8  %0,7  kullanan=1
          ProbabilityTheory.Kernel.entropy_condKernel_le_entropy_snd  [teorem]  alt=7  %0,6  kullanan=1
      … ve 25 küçük çocuk daha
    ProbabilityTheory.Kernel.chain_rule  [teorem]  alt=54  %4,4  kullanan=3
      ProbabilityTheory.Kernel.entropy_compProd  [teorem]  alt=20  %2,9  kullanan=1
        ProbabilityTheory.Kernel.entropy_compProd'  [teorem]  alt=12  %1,8  kullanan=1
          ProbabilityTheory.Kernel.entropy_compProd_aux  [teorem]  alt=6  %1,5  kullanan=1
          … ve 2 küçük çocuk daha
        ProbabilityTheory.Kernel.compProd_congr_ae  [teorem]  alt=3  %0,6  kullanan=1
          … ve 1 küçük çocuk daha
        … ve 3 küçük çocuk daha
      ProbabilityTheory.Kernel.aefiniteKernelSupport_of_cond  [teorem]  alt=16  %0,6  kullanan=1
        … ve 14 küçük çocuk daha
      ProbabilityTheory.Kernel.disintegration  [teorem]  alt=6  %0,5  kullanan=1
        … ve 5 küçük çocuk daha
      … ve 1 küçük çocuk daha
    ProbabilityTheory.measureMutualInfo_nonneg_aux  [teorem]  alt=24  %3,0  kullanan=2
      … ve 23 küçük çocuk daha
    ProbabilityTheory.chain_rule'  [teorem]  alt=8  %1,2  kullanan=2
      … ve 4 küçük çocuk daha
    rdist_le_of_isUniform_of_card_sub_le  [teorem]  alt=8  %1,1  kullanan=1
      … ve 2 küçük çocuk daha
    ProbabilityTheory.IsUniform.measureReal_preimage_sub  [teorem]  alt=9  %1,0  kullanan=1
      … ve 2 küçük çocuk daha
    diff_ent_le_rdist  [teorem]  alt=8  %0,9  kullanan=2
      … ve 1 küçük çocuk daha
    ProbabilityTheory.independent_copies_finiteRange  [teorem]  alt=2  %0,8  kullanan=3
      … ve 1 küçük çocuk daha
    ProbabilityTheory.prob_ge_exp_neg_entropy'  [teorem]  alt=3  %0,8  kullanan=1
      ProbabilityTheory.prob_ge_exp_neg_entropy  [teorem]  alt=2  %0,7  kullanan=1
        … ve 1 küçük çocuk daha
    ProbabilityTheory.exists_isUniform_measureSpace  [teorem]  alt=2  %0,7  kullanan=1
      ProbabilityTheory.exists_isUniform  [teorem]  alt=1  %0,5  kullanan=1
    ProbabilityTheory.mutualInfo_eq_zero  [teorem]  alt=7  %0,5  kullanan=4
      … ve 4 küçük çocuk daha
    ProbabilityTheory.measureMutualInfo_nonneg  [teorem]  alt=7  %0,5  kullanan=2
      … ve 4 küçük çocuk daha
    … ve 106 küçük çocuk daha
  … ve 7 küçük çocuk daha
```

## 5. En büyük kilometre taşları / Largest milestones

Kök dışındaki, yardımcı olmayan teoremler; alt ağaç ağırlığına göre. Önerme metni projenin kaynağından alınmıştır (atlas verildiyse). / Non-auxiliary theorems other than the root, by subtree weight; statement text is from the source when available.

| # | Teorem | Alt ağaç | Pay | Üstü / dominator | Kaynak |
|---:|---|---:|---:|---|---|
| 1 | `PFR_conjecture_aux` | 650 | %97,7 | `PFR_conjecture` |  |
| 2 | `entropic_PFR_conjecture` | 368 | %73,6 | `PFR_conjecture_aux` |  |
| 3 | `tau_strictly_decreases` | 260 | %59,4 | `entropic_PFR_conjecture` |  |
| 4 | `tau_strictly_decreases_aux` | 256 | %56,1 | `tau_strictly_decreases` |  |
| 5 | `cond_construct_good` | 56 | %13,1 | `tau_strictly_decreases_aux` |  |
| 6 | `construct_good'` | 49 | %12,2 | `cond_construct_good` |  |
| 7 | `construct_good` | 48 | %12,1 | `construct_good'` |  |
| 8 | `sum_dist_diff_le` | 57 | %10,3 | `tau_strictly_decreases_aux` |  |
| 9 | `construct_good_prelim` | 44 | %9,9 | `construct_good` |  |
| 10 | `sum_condMutual_le` | 19 | %7,7 | `tau_strictly_decreases_aux` |  |
| 11 | `ent_bsg` | 41 | %7,2 | `construct_good_prelim` |  |
| 12 | `second_estimate` | 13 | %4,5 | `sum_condMutual_le` |  |
| 13 | `ProbabilityTheory.Kernel.chain_rule` | 54 | %4,4 | `PFR_conjecture_aux` |  |
| 14 | `ProbabilityTheory.condIndep_copies'` | 22 | %4,1 | `ent_bsg` |  |
| 15 | `comparison_of_ruzsa_distances` | 9 | %3,4 | `tau_strictly_decreases_aux` |  |
| 16 | `sum_of_rdist_eq_char_2` | 20 | %3,3 | `tau_strictly_decreases_aux` |  |
| 17 | `condRuzsaDist_le'` | 9 | %3,2 | `tau_strictly_decreases_aux` |  |
| 18 | `sum_of_rdist_eq` | 18 | %3,1 | `sum_of_rdist_eq_char_2` |  |
| 19 | `condRuzsaDist_le` | 6 | %3,0 | `condRuzsaDist_le'` |  |
| 20 | `ProbabilityTheory.measureMutualInfo_nonneg_aux` | 24 | %3,0 | `PFR_conjecture_aux` |  |
| 21 | `ProbabilityTheory.Kernel.entropy_compProd` | 20 | %2,9 | `ProbabilityTheory.Kernel.chain_rule` |  |
| 22 | `ProbabilityTheory.condIndep_copies` | 16 | %2,8 | `ProbabilityTheory.condIndep_copies'` |  |
| 23 | `independenceCondition1` | 27 | %2,5 | `sum_dist_diff_le` |  |
| 24 | `ProbabilityTheory.iIndepFun.apply_two_last` | 26 | %2,5 | `independenceCondition1` |  |
| 25 | `exists_isUniform_of_rdist_eq_zero` | 20 | %2,5 | `entropic_PFR_conjecture` |  |
| 26 | `ProbabilityTheory.independent_copies3_nondep_finiteRange` | 4 | %2,5 | `entropic_PFR_conjecture` |  |
| 27 | `condRuzsaDist'_of_inj_map'` | 14 | %2,3 | `sum_dist_diff_le` |  |
| 28 | `exists_isUniform_of_rdist_self_eq_zero` | 19 | %2,3 | `exists_isUniform_of_rdist_eq_zero` |  |
| 29 | `condRuzsaDistance_ge_of_min` | 11 | %2,1 | `tau_strictly_decreases_aux` |  |
| 30 | `I₃_eq` | 4 | %2,1 | `sum_condMutual_le` |  |
| 31 | `condRuzsaDist_of_indep` | 8 | %2,0 | `tau_strictly_decreases_aux` |  |
| 32 | `ProbabilityTheory.Kernel.entropy_compProd'` | 12 | %1,8 | `ProbabilityTheory.Kernel.entropy_compProd` |  |
| 33 | `kaimanovich_vershik'` | 8 | %1,8 | `comparison_of_ruzsa_distances` |  |
| 34 | `ent_ofsum_le` | 3 | %1,8 | `tau_strictly_decreases_aux` |  |
| 35 | `ProbabilityTheory.condEntropy_two_eq_kernel_entropy` | 20 | %1,8 | `entropic_PFR_conjecture` |  |
| 36 | `condRuzsaDist_of_copy` | 4 | %1,6 | `condRuzsaDist_le` |  |
| 37 | `rdist_triangle` | 3 | %1,6 | `entropic_PFR_conjecture` |  |
| 38 | `second_estimate_aux` | 2 | %1,5 | `second_estimate` |  |
| 39 | `ProbabilityTheory.Kernel.entropy_compProd_aux` | 6 | %1,5 | `ProbabilityTheory.Kernel.entropy_compProd'` |  |
| 40 | `rdist_of_indep_eq_sum_fibre` | 9 | %1,4 | `sum_of_rdist_eq` |  |
| 41 | `isUniform_sub_const_of_rdist_eq_zero` | 9 | %1,3 | `exists_isUniform_of_rdist_self_eq_zero` |  |
| 42 | `ProbabilityTheory.condDistrib_eq_prod_of_indepFun` | 7 | %1,3 | `condRuzsaDist_of_indep` |  |
| 43 | `first_estimate` | 4 | %1,3 | `tau_strictly_decreases_aux` |  |
| 44 | `tau_minimizer_exists` | 14 | %1,2 | `entropic_PFR_conjecture` |  |
| 45 | `ProbabilityTheory.chain_rule'` | 8 | %1,2 | `PFR_conjecture_aux` |  |
| 46 | `ProbabilityTheory.independent_copies4_nondep` | 1 | %1,1 | `tau_strictly_decreases` |  |
| 47 | `rdist_le_of_isUniform_of_card_sub_le` | 8 | %1,1 | `PFR_conjecture_aux` |  |
| 48 | `sub_mem_symmGroup` | 4 | %1,0 | `isUniform_sub_const_of_rdist_eq_zero` |  |
| 49 | `ProbabilityTheory.iIndepFun.pi'` | 6 | %1,0 | `ProbabilityTheory.iIndepFun.apply_two_last` |  |
| 50 | `ProbabilityTheory.iIndepFun.pi` | 5 | %1,0 | `ProbabilityTheory.iIndepFun.pi'` |  |


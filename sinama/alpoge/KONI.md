# Koni / Cone — ispat konisi ve baskınlık ağacı / proof cone and dominator tree

Kök / root: `riemannHypothesis`

Bu sayfadaki sayılar resmi Lean kaydının (lean4export) bağımlılık grafiğinden hesaplanır; tahmin içermez. / All numbers on this page are computed from the dependency graph of the official Lean export.

## 1. Sayılar / Numbers

| | Bildirim / declarations | İfade ağırlığı / expression weight |
|---|---:|---:|
| Kayıttaki toplam / total in the export | 1.484.729 | 1.065.214.290 |
| Kütüphane (Mathlib ve altı) / library | 214.545 | 41.535.920 |
| Proje / project | 1.270.184 | 1.023.678.370 |
| &nbsp;&nbsp;kökün ispat konisinde / in the root's proof cone | 1.265.256 (%99,6) | 1.023.676.186 (%100,0) |
| &nbsp;&nbsp;**kullanılmayan / unused by the root** | **4.928** (%0,4) | 2.184 (%0,0) |
| Kökün önermesini anlamak için gereken proje bildirimi / project declarations needed to read the root's statement | 1 | |
| Konideki kütüphane bildirimi / library declarations in the cone | 212.959 | |

İfade ağırlığı: bildirimin kayda eklediği yeni ifade düğümü sayısı (ispatın büyüklüğünün ölçüsü). / Expression weight: number of new expression nodes the declaration added to the export.

| Tür / kind | Projede / in project | Konide / in cone |
|---|---:|---:|
| teorem | 1.075.031 | 1.075.015 |
| tanım | 178.305 | 178.298 |
| kurucu | 5.710 | 5.710 |
| tip | 5.569 | 5.569 |
| özyineleyici | 5.569 | 664 |

## 1b. Aksiyomlar / Axioms

Kökün ispat konisindeki aksiyom: **3** (kayıttaki toplam aksiyom: 3; kütüphane dahil, hiçbiri atlanmadı). Lean'in üç standart aksiyomu dışında kalan: **0**. / Axioms in the root's proof cone: 3 (axioms in the export: 3; library included). Outside Lean's three standard axioms: 0.

| Aksiyom / axiom | Not / note |
|---|---|
| `Classical.choice` | standart / standard |
| `Quot.sound` | standart / standard |
| `propext` | standart / standard |

Bu liste kayıttaki `axiom` bildirimlerinden okunur; ispatı yeniden denetlemez (bunu Lean çekirdeği ve bağımsız denetleyiciler yapar). / Read from the `axiom` declarations of the export; it does not re-check the proof.

## 2. Kullanılmayan kod / Unused code

Kökün ispatına hiç girmeyen proje bildirimi: **4.928** (bunların 4.907 tanesi Lean'in otomatik yardımcısı). / Project declarations never used by the root's proof: 4.928 (4.907 of them Lean-generated auxiliaries).

| Ad alanı / namespace | Bildirim | Ağırlık / weight |
|---|---:|---:|
| `Formalism.L2` | 545 | 0 |
| `UpperTheory.V` | 455 | 0 |
| `Formalism.MainNotions` | 301 | 0 |
| `GlobalTheory.Mem` | 188 | 0 |
| `GlobalTheory.CompanionTheory` | 180 | 0 |
| `UpperTheory.Gal` | 123 | 0 |
| `Formalism.FourierDecayAlt` | 107 | 0 |
| `ReciprocityTheory.ChartRestriction` | 97 | 0 |
| `FunctorialResolution.EmbeddedResolution` | 96 | 0 |
| `Formalism.IndefR` | 94 | 0 |
| `GroundTheory.Heights₂` | 89 | 0 |
| `GlobalTheory.IndefiniteRowSideFullHecke` | 82 | 0 |
| `GlobalTheory.HeightCounting` | 81 | 0 |
| `Formalism.BasicNotions` | 75 | 0 |
| `PositivityTheory.Rg` | 74 | 0 |
| `UpperTheory.ConvolutionTheory` | 50 | 0 |
| `CrystallineSemistableComparison.Pb` | 37 | 0 |
| `GlobalTheory.SeeSaw` | 36 | 0 |
| `_private.Development` | 35 | 0 |
| `PositivityTheory.ThKG` | 31 | 0 |

## 3. Kopya önermeler / Duplicate statements

Proje teoremi: 1.075.031. Önermesi (tipi) başka bir teoreminkiyle yapısal olarak aynı olan gruplar: **90.968**; fazladan kopya: **260.240** (%24,2). Yardımcı adlar hariç: 65.429 grup, 88.693 fazladan kopya. / Project theorems: 1.075.031. Groups whose statement (type) is structurally identical: 90.968; redundant copies: 260.240. Excluding auxiliary names: 65.429 groups, 88.693 redundant copies.

Not: parmak izi 64 bit ve yapısaldır (bağlı değişken adları sayılmaz); evren parametre adları farklıysa kopya sayılmaz. / The fingerprint is 64-bit and structural.

| Kopya sayısı | Konide | Örnek adlar / example names |
|---:|---:|---|
| 180 | 180 | `GlobalTheory.HomDescent.spMap_comp`, `Formalism.L2.PjFree.spMap_comp'`, `GlobalTheory.TanMod.spMap_comp'` |
| 116 | 116 | `ReciprocityTheory.ChartRestriction.G.Geo.Tor.spMap_comp`, `GlobalTheory.FramedBaseChange.spec_comp`, `GlobalTheory.Frames.NonzeroGenerates.spMap_comp'` |
| 69 | 69 | `GlobalTheory.SelfDualLatticeCompare.conj_conj`, `GlobalTheory.AdelicU.cm_conj_conj`, `GlobalTheory.LFun.InertChart.conj_conj` |
| 68 | 68 | `GlobalTheory.FinWeilO.mt_mul`, `GlobalTheory.WeilVacMove.mt_mul`, `GlobalTheory.RatSubst.mt_mul` |
| 59 | 59 | `GlobalTheory.FinWeilO.mt_one`, `GlobalTheory.WeilVacMove.mt_one`, `GlobalTheory.RatSubst.mt_one` |
| 55 | 55 | `Formalism.QuantumDeterminants.GBasic.Hpk_sq`, `ReciprocityTheory.ChartRestriction.DS.Xi.StepA.Hpk_sq`, `Formalism.QuantumDeterminants.WeylGroupFacts.hpk_sq` |
| 51 | 51 | `GlobalTheory.ZM.CoordChart.spMap_inj`, `GlobalTheory.ZM.DenseFib.spMap_inj`, `GlobalTheory.CoordChart.sp_inj` |
| 51 | 51 | `GlobalTheory.EtC.CupSpec.map_res`, `GlobalTheory.EtC.FlatExtAcyc.sres_map`, `GlobalTheory.EtC.secRes_secMap` |
| 48 | 48 | `GlobalTheory.Frames.Model.spMap_id`, `GlobalTheory.Frames.SecCalc.spMap_id'`, `GlobalTheory.Frames.NonzeroGenerates.spMap_id'` |
| 45 | 45 | `PositivityTheory.Rg.BcB.CG.SmoothIntegrals.isOpen_GLs₀`, `PositivityTheory.RgBcC.Bridge.isOpen_GLs`, `GlobalTheory.CompanionTheory.LengthGL.isOpen_GLs` |
| 42 | 42 | `Formalism.QuantumDeterminants.GBasic.Hpk_herm`, `Formalism.FourierDecayAlt.P.B2x5.Hherm`, `Formalism.FourierDecayAlt.P.B2x8.Hpk_herm` |
| 40 | 40 | `Formalism.L2.SG.Pf.mem_orth_iff_bl`, `PI.DCRelEquiv.UnitaryGroupMassFormula.mem_orth_iff`, `Formalism.L2.SG.Pf.mem_orth'` |
| 39 | 39 | `GlobalTheory.Frames.SecCalc.spMap_comp'`, `GlobalTheory.Frames.FramedBaseChange.spMap_comp_spMap`, `GlobalTheory.Frames.EigenBaseChange.spMap_spMap` |
| 38 | 38 | `Formalism.L2.SG.Pf.SatGram.le_exp_neg_one`, `GlobalTheory.Hk3.IntWitt.le_exp_neg_one_of_lt_one'`, `GlobalTheory.CompletionNorm.le_exp_neg_one_of_lt_one` |
| 37 | 37 | `GlobalTheory.EtC.exactIff_map_comp`, `GlobalTheory.EtC.TwResExt.sec_map_comp`, `GlobalTheory.EtC.TwMulSurj.map_comp_apply` |

## 4. Baskınlık ağacı / Dominator tree

X, Y'nin üstündeyse kökten Y'ye giden her bağımlılık yolu X'ten geçer: Y yalnızca X için vardır. Bir satırın alt ağacı, makalede o başlığın altına girecek her şeydir. / If X is above Y, every dependency path from the root to Y passes through X.

Ağaçtaki düğüm: 1.265.256; kökün doğrudan çocukları: 1; en derin düzey: 51.

| Alt ağaç büyüklüğü / subtree size | Düğüm / nodes |
|---|---:|
| ≥ 10 bildirim | 74.175 |
| ≥ 100 bildirim | 8.903 |
| ≥ 1.000 bildirim | 986 |
| ≥ 10.000 bildirim | 84 |
| ≥ 100.000 bildirim | 9 |

Aşağıda ağırlığı toplamın en az %0,5'i olan dallar (en çok 5 düzey). Sütunlar: alt ağaçtaki bildirim, ağırlık payı, bu bildirimi doğrudan kullanan sayısı.

```
riemannHypothesis  [teorem]  alt=1.265.256  %100,0  kullanan=1
  rhOfAll  [teorem]  alt=1.265.255  %100,0  kullanan=1
    allChi  [teorem]  alt=1.265.248  %100,0  kullanan=1
      UpperTheory.FinalTheorems.everyCharacter  [teorem]  alt=1.265.247  %100,0  kullanan=1
        UpperTheory.FinalTheorems.everyCharacter_of_row  [teorem]  alt=961.960  %79,2  kullanan=1
          UpperTheory.LiteratureTheorems.every_character_of_literature_of_vWin  [teorem]  alt=840.854  %68,7  kullanan=1
          UpperTheory.One.vwin_of_row  [teorem]  alt=90.527  %8,5  kullanan=1
          … ve 7.841 küçük çocuk daha
        UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter  [teorem]  alt=90.309  %6,4  kullanan=1
          UpperTheory.Gal.Int.galoisRepresentations_of_thetaLift  [teorem]  alt=86.158  %6,2  kullanan=1
          … ve 25 küçük çocuk daha
        … ve 58.062 küçük çocuk daha
    … ve 2 küçük çocuk daha
```

## 5. En büyük kilometre taşları / Largest milestones

Kök dışındaki, yardımcı olmayan teoremler; alt ağaç ağırlığına göre. Önerme metni projenin kaynağından alınmıştır (atlas verildiyse). / Non-auxiliary theorems other than the root, by subtree weight; statement text is from the source when available.

| # | Teorem | Alt ağaç | Pay | Üstü / dominator | Kaynak |
|---:|---|---:|---:|---|---|
| 1 | `rhOfAll` | 1.265.255 | %100,0 | `riemannHypothesis` |  |
| 2 | `allChi` | 1.265.248 | %100,0 | `rhOfAll` |  |
| 3 | `UpperTheory.FinalTheorems.everyCharacter` | 1.265.247 | %100,0 | `allChi` |  |
| 4 | `UpperTheory.FinalTheorems.everyCharacter_of_row` | 961.960 | %79,2 | `UpperTheory.FinalTheorems.everyCharacter` |  |
| 5 | `UpperTheory.LiteratureTheorems.every_character_of_literature_of_vWin` | 840.854 | %68,7 | `UpperTheory.FinalTheorems.everyCharacter_of_row` |  |
| 6 | `UpperTheory.Lit.every_character_of_theta_integrals_local_matching` | 540.408 | %43,0 | `UpperTheory.LiteratureTheorems.every_character_of_literature_of_vWin` |  |
| 7 | `UpperTheory.Lit.nonempty_hyps_definite_side_of_closed_bound` | 449.095 | %37,2 | `UpperTheory.Lit.every_character_of_theta_integrals_local_matching` |  |
| 8 | `GlobalTheory.Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt` | 152.670 | %15,6 | `UpperTheory.Lit.nonempty_hyps_definite_side_of_closed_bound` |  |
| 9 | `UpperTheory.One.vwin_of_row` | 90.527 | %8,5 | `UpperTheory.FinalTheorems.everyCharacter_of_row` |  |
| 10 | `UpperTheory.One.Join.automorphic_window_of_inputs` | 90.523 | %8,5 | `UpperTheory.One.vwin_of_row` |  |
| 11 | `UpperTheory.One.Join.v_window_of_depth_zero_residual_bc_cm` | 89.542 | %8,4 | `UpperTheory.One.Join.automorphic_window_of_inputs` |  |
| 12 | `UpperTheory.V.v_window_of_literal_automorphy_n` | 89.479 | %8,4 | `UpperTheory.One.Join.v_window_of_depth_zero_residual_bc_cm` |  |
| 13 | `UpperTheory.V.HV.DescentVanishingReductions.v_window_of_automorphy_csd_ss_mono_odd` | 89.478 | %8,4 | `UpperTheory.V.v_window_of_literal_automorphy_n` |  |
| 14 | `UpperTheory.V.HV.DescentVanishingReductions.vwin_of_hypotheses_H_E_alt` | 79.012 | %7,6 | `UpperTheory.V.HV.DescentVanishingReductions.v_window_of_automorphy_csd_ss_mono_odd` |  |
| 15 | `SelfIntersectionVolumeEstimates.topCovolSlim2_use_alt_alt` | 79.803 | %7,3 | `UpperTheory.LiteratureTheorems.every_character_of_literature_of_vWin` |  |
| 16 | `GlobalTheory.T.large_unramified_exponent_bundles_exist_alt` | 37.056 | %7,1 | `GlobalTheory.Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt` |  |
| 17 | `GlobalTheory.Fc.StageOneU.member_bundles_large_unramified_exponents_alt` | 37.055 | %7,1 | `GlobalTheory.T.large_unramified_exponent_bundles_exist_alt` |  |
| 18 | `UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter` | 90.309 | %6,4 | `UpperTheory.FinalTheorems.everyCharacter` |  |
| 19 | `UpperTheory.Gal.Int.galoisRepresentations_of_thetaLift` | 86.158 | %6,2 | `UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter` |  |
| 20 | `UpperTheory.Gal.Int.Geo.geoOne_holds` | 77.841 | %5,6 | `UpperTheory.Gal.Int.galoisRepresentations_of_thetaLift` |  |
| 21 | `UpperTheory.Gal.Int.Geo.geometric_realization_of_weight_one` | 74.676 | %5,3 | `UpperTheory.Gal.Int.Geo.geoOne_holds` |  |
| 22 | `GlobalTheory.T.member_exists_baseLattice_alt` | 25.993 | %4,8 | `GlobalTheory.Fc.StageOneU.member_bundles_large_unramified_exponents_alt` |  |
| 23 | `GlobalTheory.Mem.Top.Bl.exists_baseLattice_of_prime_alt` | 25.992 | %4,8 | `GlobalTheory.T.member_exists_baseLattice_alt` |  |
| 24 | `PositivityTheory.HtPt.Ah.deep_slim_use` | 45.650 | %4,0 | `SelfIntersectionVolumeEstimates.topCovolSlim2_use_alt_alt` |  |
| 25 | `GlobalTheory.CompanionTheory.Ar.Plug.deepStR_of_use` | 45.051 | %4,0 | `PositivityTheory.HtPt.Ah.deep_slim_use` |  |
| 26 | `GlobalTheory.Fc.AllAtMemberStage0.allRows_of_open0_alt` | 54.017 | %3,7 | `GlobalTheory.Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt` |  |
| 27 | `UpperTheory.Gal.Int.Geo.steps_holds` | 50.246 | %3,3 | `UpperTheory.Gal.Int.Geo.geometric_realization_of_weight_one` |  |
| 28 | `GlobalTheory.Fc.S0.ontoX_and_lamLow_of_unitaryGroupHypotheses'` | 34.786 | %3,0 | `UpperTheory.Lit.nonempty_hyps_definite_side_of_closed_bound` |  |
| 29 | `GlobalTheory.BigOn.ontoX_of_hypotheses_alt_alt` | 34.185 | %3,0 | `GlobalTheory.Fc.S0.ontoX_and_lamLow_of_unitaryGroupHypotheses'` |  |
| 30 | `GlobalTheory.CompanionTheory.Ar.Link.good_tower_volume_theorem_bis` | 31.599 | %2,9 | `GlobalTheory.CompanionTheory.Ar.Plug.deepStR_of_use` |  |
| 31 | `GlobalTheory.T.final_theorem_of_inputs_right` | 31.595 | %2,9 | `GlobalTheory.CompanionTheory.Ar.Link.good_tower_volume_theorem_bis` |  |
| 32 | `GlobalTheory.CompanionTheory.Ar.Top.goodTower_volume_of_reduced` | 31.594 | %2,9 | `GlobalTheory.T.final_theorem_of_inputs_right` |  |
| 33 | `GlobalTheory.T.sFino_and_secondNo_of_sFinl'` | 1.803 | %2,8 | `GlobalTheory.Mem.Top.Bl.exists_baseLattice_of_prime_alt` |  |
| 34 | `GlobalTheory.HeightCounting.Up.sFino_and_secondNo_of_rat_cusp_finl` | 1.802 | %2,8 | `GlobalTheory.T.sFino_and_secondNo_of_sFinl'` |  |
| 35 | `GlobalTheory.HeightCounting.Up.secondNo_of_sMt_sRat_sCusp_sFinl` | 1.800 | %2,8 | `GlobalTheory.HeightCounting.Up.sFino_and_secondNo_of_rat_cusp_finl` |  |
| 36 | `UpperTheory.GalC.final_alt_alt` | 28.188 | %2,6 | `GlobalTheory.Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt` |  |
| 37 | `UpperTheory.GalC.final_of_alt` | 26.608 | %2,5 | `UpperTheory.GalC.final_alt_alt` |  |
| 38 | `UpperTheory.GalC.linkedAt_linkN_of_boundAtTwoThree` | 25.740 | %2,4 | `UpperTheory.GalC.final_of_alt` |  |
| 39 | `UpperTheory.GalC.linkN_of_boundAtTwoThree_slot` | 25.739 | %2,4 | `UpperTheory.GalC.linkedAt_linkN_of_boundAtTwoThree` |  |
| 40 | `UpperTheory.GalC.linkN_of_twGood_galoisPreconditions` | 25.738 | %2,4 | `UpperTheory.GalC.linkN_of_boundAtTwoThree_slot` |  |
| 41 | `GlobalTheory.T.good_tower_volume_theorem` | 26.912 | %2,4 | `GlobalTheory.CompanionTheory.Ar.Top.goodTower_volume_of_reduced` |  |
| 42 | `GlobalTheory.CompanionTheory.Ar.Top.goodTower_and_volume` | 26.911 | %2,4 | `GlobalTheory.T.good_tower_volume_theorem` |  |
| 43 | `GlobalTheory.T.open0_of_unitary_group_hypotheses` | 22.887 | %2,4 | `UpperTheory.Lit.nonempty_hyps_definite_side_of_closed_bound` |  |
| 44 | `GlobalTheory.Fc.S0.Open0ProofU.open_orbit_of_unramified_exponents_alt` | 22.886 | %2,4 | `GlobalTheory.T.open0_of_unitary_group_hypotheses` |  |
| 45 | `SelfIntersectionVolumeEstimates.topCovolG_alt_alt` | 19.967 | %2,1 | `SelfIntersectionVolumeEstimates.topCovolSlim2_use_alt_alt` |  |
| 46 | `GlobalTheory.T.moveToBase_of_inputs_serN` | 1.418 | %1,9 | `GlobalTheory.HeightCounting.Up.secondNo_of_sMt_sRat_sCusp_sFinl` |  |
| 47 | `GlobalTheory.HeightCounting.Up.multiplicity_bound_of_local_components_alt` | 1.416 | %1,9 | `GlobalTheory.T.moveToBase_of_inputs_serN` |  |
| 48 | `GlobalTheory.T.levelI_same_gal_transfer_to_levelB1_list` | 1.412 | %1,9 | `GlobalTheory.HeightCounting.Up.multiplicity_bound_of_local_components_alt` |  |
| 49 | `GlobalTheory.HeightCounting.Up.exists_levelB1_carried_of_levelI_same_gal` | 1.411 | %1,9 | `GlobalTheory.T.levelI_same_gal_transfer_to_levelB1_list` |  |
| 50 | `GlobalTheory.T.main_theorem_published_inputs_third_alt_alt` | 20.262 | %1,9 | `GlobalTheory.Fc.S0.Open0ProofU.open_orbit_of_unramified_exponents_alt` |  |


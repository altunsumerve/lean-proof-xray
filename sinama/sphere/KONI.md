# Koni / Cone — ispat konisi ve baskınlık ağacı / proof cone and dominator tree

Kök / root: `Smale`

Bu sayfadaki sayılar resmi Lean kaydının (lean4export) bağımlılık grafiğinden hesaplanır; tahmin içermez. / All numbers on this page are computed from the dependency graph of the official Lean export.

## 1. Sayılar / Numbers

| | Bildirim / declarations | İfade ağırlığı / expression weight |
|---|---:|---:|
| Kayıttaki toplam / total in the export | 57.465 | 7.575.431 |
| Kütüphane (Mathlib ve altı) / library | 55.732 | 6.816.160 |
| Proje / project | 1.733 | 759.271 |
| &nbsp;&nbsp;kökün ispat konisinde / in the root's proof cone | 1.715 (%99,0) | 759.271 (%100,0) |
| &nbsp;&nbsp;**kullanılmayan / unused by the root** | **18** (%1,0) | 0 (%0,0) |
| Kökün önermesini anlamak için gereken proje bildirimi / project declarations needed to read the root's statement | 3 | |
| Konideki kütüphane bildirimi / library declarations in the cone | 54.929 | |

İfade ağırlığı: bildirimin kayda eklediği yeni ifade düğümü sayısı (ispatın büyüklüğünün ölçüsü). / Expression weight: number of new expression nodes the declaration added to the export.

| Tür / kind | Projede / in project | Konide / in cone |
|---|---:|---:|
| teorem | 1.306 | 1.306 |
| tanım | 337 | 337 |
| kurucu | 30 | 30 |
| tip | 30 | 30 |
| özyineleyici | 30 | 12 |

## 1b. Aksiyomlar / Axioms

Kökün ispat konisindeki aksiyom: **3** (kayıttaki toplam aksiyom: 3; kütüphane dahil, hiçbiri atlanmadı). Lean'in üç standart aksiyomu dışında kalan: **0**. / Axioms in the root's proof cone: 3 (axioms in the export: 3; library included). Outside Lean's three standard axioms: 0.

| Aksiyom / axiom | Not / note |
|---|---|
| `Classical.choice` | standart / standard |
| `Quot.sound` | standart / standard |
| `propext` | standart / standard |

Bu liste kayıttaki `axiom` bildirimlerinden okunur; ispatı yeniden denetlemez (bunu Lean çekirdeği ve bağımsız denetleyiciler yapar). / Read from the `axiom` declarations of the export; it does not re-check the proof.

## 2. Kullanılmayan kod / Unused code

Kökün ispatına hiç girmeyen proje bildirimi: **18** (bunların 18 tanesi Lean'in otomatik yardımcısı). / Project declarations never used by the root's proof: 18 (18 of them Lean-generated auxiliaries).

| Ad alanı / namespace | Bildirim | Ağırlık / weight |
|---|---:|---:|
| `Immersion.rec` | 1 | 0 |
| `DualPair.rec` | 1 | 0 |
| `OpenSmoothEmbedding.rec` | 1 | 0 |
| `LocalisationData.rec` | 1 | 0 |
| `ChartPair.rec` | 1 | 0 |
| `ChartPair.compat'` | 1 | 0 |
| `Landscape.rec` | 1 | 0 |
| `StepLandscape.rec` | 1 | 0 |
| `StepLandscape.Accepts` | 1 | 0 |
| `NiceLoop.rec` | 1 | 0 |
| `SurroundingPts.rec` | 1 | 0 |
| `SurroundingFamily.rec` | 1 | 0 |
| `SurroundingFamilyIn.rec` | 1 | 0 |
| `LoopFamilyGerm.rec` | 1 | 0 |
| `SurroundingFamilyGerm.rec` | 1 | 0 |
| `EquivariantMap.rec` | 1 | 0 |
| `SmoothSurroundingFamily.rec` | 1 | 0 |
| `SmoothSurroundingFamily.IsCenteringDensity` | 1 | 0 |

## 3. Kopya önermeler / Duplicate statements

Proje teoremi: 1.306. Önermesi (tipi) başka bir teoreminkiyle yapısal olarak aynı olan gruplar: **56**; fazladan kopya: **100** (%7,7). Yardımcı adlar hariç: 9 grup, 9 fazladan kopya. / Project theorems: 1.306. Groups whose statement (type) is structurally identical: 56; redundant copies: 100. Excluding auxiliary names: 9 groups, 9 redundant copies.

Not: parmak izi 64 bit ve yapısaldır (bağlı değişken adları sayılmaz); evren parametre adları farklıysa kopya sayılmaz. / The fingerprint is 64-bit and structural.

| Kopya sayısı | Konide | Örnek adlar / example names |
|---:|---:|---|
| 2 | 2 | `contMDiffAt_one_jet_eucl_bundle`, `contMDiffAt_one_jet_eucl_bundle'` |
| 2 | 2 | `ContMDiffAt.one_jet_eucl_bundle_mk'`, `ContMDiffAt.one_jet_eucl_bundle_mk` |
| 2 | 2 | `OpenSmoothEmbedding.left_inv'`, `OpenSmoothEmbedding.left_inv` |
| 2 | 2 | `Loop.per'`, `Loop.per` |
| 2 | 2 | `inductive_construction_of_loc'`, `inductive_construction_of_loc` |
| 2 | 2 | `EquivariantMap.eqv'`, `EquivariantMap.eqv` |
| 2 | 2 | `EquivariantEquiv.eqv'`, `EquivariantEquiv.eqv` |
| 2 | 2 | `EquivariantEquiv.map_zero'`, `EquivariantEquiv.map_zero` |
| 2 | 2 | `Continuous.prodL'`, `Continuous.prodL` |

## 4. Baskınlık ağacı / Dominator tree

X, Y'nin üstündeyse kökten Y'ye giden her bağımlılık yolu X'ten geçer: Y yalnızca X için vardır. Bir satırın alt ağacı, makalede o başlığın altına girecek her şeydir. / If X is above Y, every dependency path from the root to Y passes through X.

Ağaçtaki düğüm: 1.715; kökün doğrudan çocukları: 4; en derin düzey: 18.

| Alt ağaç büyüklüğü / subtree size | Düğüm / nodes |
|---|---:|
| ≥ 10 bildirim | 72 |
| ≥ 100 bildirim | 13 |
| ≥ 1.000 bildirim | 6 |
| ≥ 10.000 bildirim | 0 |
| ≥ 100.000 bildirim | 0 |

Aşağıda ağırlığı toplamın en az %0,5'i olan dallar (en çok 5 düzey). Sütunlar: alt ağaçtaki bildirim, ağırlık payı, bu bildirimi doğrudan kullanan sayısı.

```
Smale  [teorem]  alt=1.715  %100,0  kullanan=1
  sphere_eversion  [teorem]  alt=1.711  %99,9  kullanan=1
    immersionRel_satisfiesHPrincipleWith  [teorem]  alt=1.420  %79,7  kullanan=1
      RelMfld.Ample.satisfiesHPrincipleWith  [teorem]  alt=1.371  %77,7  kullanan=1
        RelMfld.Ample.satisfiesHPrinciple  [teorem]  alt=1.274  %64,9  kullanan=1
          OpenSmoothEmbedding.improve_formalSol  [teorem]  alt=1.058  %52,2  kullanan=1
          exists_stability_dist  [teorem]  alt=78  %5,2  kullanan=1
          inductive_htpy_construction  [teorem]  alt=20  %1,2  kullanan=1
          inductive_construction  [teorem]  alt=16  %0,6  kullanan=2
          RelMfld.satisfiesHPrinciple_of_weak  [teorem]  alt=3  %0,5  kullanan=1
          … ve 39 küçük çocuk daha
        RelMfld.SatisfiesHPrinciple.satisfiesHPrincipleWith  [teorem]  alt=36  %6,4  kullanan=1
          FamilyFormalSol.curry  [tanım]  alt=4  %1,1  kullanan=3
          FamilyFormalSol.uncurry  [tanım]  alt=5  %1,0  kullanan=3
          FamilyOneJetSec.curry  [tanım]  alt=3  %0,9  kullanan=7
          curry_eq_iff_eq_uncurry  [teorem]  alt=5  %0,7  kullanan=1
          FamilyOneJetSec.uncurry  [tanım]  alt=4  %0,6  kullanan=8
          … ve 8 küçük çocuk daha
        RelMfld.Ample.relativize  [teorem]  alt=9  %3,0  kullanan=1
          relativize_slice  [teorem]  alt=4  %1,7  kullanan=1
          relativize_slice_eq_univ  [teorem]  alt=2  %1,0  kullanan=1
          … ve 1 küçük çocuk daha
        RelMfld.isOpen_relativize  [teorem]  alt=4  %0,6  kullanan=1
          contMDiff_bundleSnd  [teorem]  alt=3  %0,6  kullanan=1
        ContMDiffAt.clm_comp_inTangentCoordinates  [teorem]  alt=2  %0,6  kullanan=2
          … ve 1 küçük çocuk daha
        … ve 19 küçük çocuk daha
      immersionRel_ample  [teorem]  alt=12  %1,1  kullanan=1
        … ve 5 küçük çocuk daha
      … ve 22 küçük çocuk daha
    formalEversion  [tanım]  alt=106  %8,8  kullanan=6
      formalEversionAux2  [tanım]  alt=102  %8,7  kullanan=1
        formalEversionAux  [tanım]  alt=59  %4,8  kullanan=2
          familyTwist  [tanım]  alt=14  %2,2  kullanan=1
          familyJoin  [tanım]  alt=16  %1,4  kullanan=1
          formalEversionAux._proof_1  [teorem]  alt=25  %0,9  kullanan=1
          … ve 3 küçük çocuk daha
        formalEversionAux2._proof_1  [teorem]  alt=11  %2,2  kullanan=1
          Orientation.isometry_rot  [teorem]  alt=10  %2,1  kullanan=1
        instDFunLikeOneJetEuclSecTotalSpaceContinuousLinearMapIdTangentSpaceTrivial  [tanım]  alt=6  %0,6  kullanan=6
          instDFunLikeOneJetEuclSecTotalSpaceContinuousLinearMapIdTangentSpaceTrivial._proof_1  [teorem]  alt=5  %0,6  kullanan=1
        contMDiffAt_one_jet_eucl_bundle  [teorem]  alt=1  %0,5  kullanan=2
        … ve 9 küçük çocuk daha
      … ve 3 küçük çocuk daha
    OneJetSec.mk.inj  [teorem]  alt=4  %1,3  kullanan=2
      OneJetSec.mk.noConfusion  [tanım]  alt=3  %1,3  kullanan=1
        OneJetSec.noConfusion  [tanım]  alt=2  %1,2  kullanan=1
          … ve 1 küçük çocuk daha
    formalEversion_hol_near_zero_one  [teorem]  alt=8  %1,1  kullanan=1
      formalEversionHolAtZero  [teorem]  alt=3  %0,7  kullanan=1
        … ve 2 küçük çocuk daha
      … ve 3 küçük çocuk daha
    RelMfld.SatisfiesHPrincipleWith.bs  [teorem]  alt=5  %0,8  kullanan=1
      … ve 2 küçük çocuk daha
    FormalSol.ext  [teorem]  alt=4  %0,8  kullanan=2
      … ve 1 küçük çocuk daha
    instFunLikeOneJetSecOneJetBundle  [tanım]  alt=4  %0,8  kullanan=71
      instFunLikeOneJetSecOneJetBundle._proof_1  [teorem]  alt=3  %0,7  kullanan=1
        OneJetSec.ext  [teorem]  alt=2  %0,6  kullanan=1
          … ve 1 küçük çocuk daha
    oneJetBundle_trivializationAt  [teorem]  alt=4  %0,7  kullanan=2
      … ve 2 küçük çocuk daha
    FamilyOneJetSec.ext  [teorem]  alt=4  %0,7  kullanan=2
      … ve 1 küçük çocuk daha
    instFunLikeFamilyFormalSolFormalSol  [tanım]  alt=4  %0,7  kullanan=38
      instFunLikeFamilyFormalSolFormalSol._proof_1  [teorem]  alt=3  %0,6  kullanan=1
        … ve 1 küçük çocuk daha
    … ve 117 küçük çocuk daha
  … ve 3 küçük çocuk daha
```

## 5. En büyük kilometre taşları / Largest milestones

Kök dışındaki, yardımcı olmayan teoremler; alt ağaç ağırlığına göre. Önerme metni projenin kaynağından alınmıştır (atlas verildiyse). / Non-auxiliary theorems other than the root, by subtree weight; statement text is from the source when available.

| # | Teorem | Alt ağaç | Pay | Üstü / dominator | Kaynak |
|---:|---|---:|---:|---|---|
| 1 | `sphere_eversion` | 1.711 | %99,9 | `Smale` |  |
| 2 | `immersionRel_satisfiesHPrincipleWith` | 1.420 | %79,7 | `sphere_eversion` |  |
| 3 | `RelMfld.Ample.satisfiesHPrincipleWith` | 1.371 | %77,7 | `immersionRel_satisfiesHPrincipleWith` |  |
| 4 | `RelMfld.Ample.satisfiesHPrinciple` | 1.274 | %64,9 | `RelMfld.Ample.satisfiesHPrincipleWith` |  |
| 5 | `OpenSmoothEmbedding.improve_formalSol` | 1.058 | %52,2 | `RelMfld.Ample.satisfiesHPrinciple` |  |
| 6 | `RelLoc.FormalSol.improve_htpy'` | 836 | %29,0 | `OpenSmoothEmbedding.improve_formalSol` |  |
| 7 | `RelLoc.FormalSol.improve` | 834 | %28,8 | `RelLoc.FormalSol.improve_htpy'` |  |
| 8 | `exist_loops` | 590 | %20,7 | `RelLoc.FormalSol.improve` |  |
| 9 | `exist_loops_aux2` | 251 | %9,9 | `exist_loops` |  |
| 10 | `RelMfld.SatisfiesHPrinciple.satisfiesHPrincipleWith` | 36 | %6,4 | `RelMfld.Ample.satisfiesHPrincipleWith` |  |
| 11 | `exists_stability_dist` | 78 | %5,2 | `RelMfld.Ample.satisfiesHPrinciple` |  |
| 12 | `exists_surrounding_loops` | 103 | %3,8 | `exist_loops_aux2` |  |
| 13 | `nice_atlas` | 46 | %3,0 | `stdLocalisationData` |  |
| 14 | `RelMfld.Ample.relativize` | 9 | %3,0 | `RelMfld.Ample.satisfiesHPrincipleWith` |  |
| 15 | `SmoothSurroundingFamily.exists_smooth_isCenteringDensity` | 83 | %2,8 | `exist_loops` |  |
| 16 | `nice_atlas'` | 40 | %2,7 | `nice_atlas` |  |
| 17 | `SmoothSurroundingFamily.reparametrize_smooth` | 45 | %2,5 | `exist_loops` |  |
| 18 | `contDiff_parametric_symm_of_deriv_pos` | 43 | %2,4 | `SmoothSurroundingFamily.reparametrize_smooth` |  |
| 19 | `contDiff_parametric_symm` | 38 | %2,3 | `contDiff_parametric_symm_of_deriv_pos` |  |
| 20 | `Orientation.isometry_rot` | 10 | %2,1 | `formalEversionAux2._proof_1` |  |
| 21 | `extend_loops` | 67 | %2,0 | `exists_surrounding_loops` |  |
| 22 | `relativize_slice` | 4 | %1,7 | `RelMfld.Ample.relativize` |  |
| 23 | `surrounding_loop_of_convexHull` | 61 | %1,5 | `exist_loops_aux2` |  |
| 24 | `Orientation.isometry_on_rot` | 4 | %1,4 | `Orientation.isometry_rot` |  |
| 25 | `ChartPair.mkHtpy_isHolonomicAt_iff` | 10 | %1,4 | `OpenSmoothEmbedding.improve_formalSol` |  |
| 26 | `ChartPair.dist_update'` | 2 | %1,3 | `OpenSmoothEmbedding.improve_formalSol` |  |
| 27 | `hasFDerivAt_parametric_primitive_of_contDiff'` | 11 | %1,3 | `RelLoc.FormalSol.improve` |  |
| 28 | `inductive_htpy_construction` | 20 | %1,2 | `RelMfld.Ample.satisfiesHPrinciple` |  |
| 29 | `formalEversion_hol_near_zero_one` | 8 | %1,1 | `sphere_eversion` |  |
| 30 | `Orientation.isometry_on_crossProduct` | 2 | %1,1 | `Orientation.isometry_on_rot` |  |
| 31 | `Orientation.norm_crossProduct` | 1 | %1,1 | `Orientation.isometry_on_crossProduct` |  |
| 32 | `immersionRel_ample` | 12 | %1,1 | `immersionRel_satisfiesHPrincipleWith` |  |
| 33 | `SmoothSurroundingFamily.eventually_exists_surroundingPts_approxSurroundingPointsAt` | 21 | %1,1 | `SmoothSurroundingFamily.exists_smooth_isCenteringDensity` |  |
| 34 | `exists_contDiff_of_convex₂` | 14 | %1,1 | `exist_loops` |  |
| 35 | `relativize_slice_eq_univ` | 2 | %1,0 | `RelMfld.Ample.relativize` |  |
| 36 | `ContinuousLinearEquiv.continuous_lowerTriangular` | 13 | %1,0 | `contDiff_parametric_symm` |  |
| 37 | `inductive_htpy_construction'` | 16 | %1,0 | `inductive_htpy_construction` |  |
| 38 | `exists_of_convex` | 13 | %1,0 | `exist_loops` |  |
| 39 | `ChartPair.mkHtpy_localize` | 4 | %1,0 | `ChartPair.mkHtpy_isHolonomicAt_iff` |  |
| 40 | `FamilyOneJetSec.curry_mem` | 2 | %0,9 | `FamilyFormalSol.curry._proof_1` |  |
| 41 | `relative_inductive_construction_of_loc` | 12 | %0,9 | `exists_surrounding_loops` |  |
| 42 | `exists_contMDiff_of_convex₂` | 11 | %0,9 | `exists_contDiff_of_convex₂` |  |
| 43 | `oneJetBundle_model_space_chartAt` | 6 | %0,9 | `oneJetBundleModelSpaceHomeomorph` |  |
| 44 | `RelMfld.Ample.localize` | 9 | %0,8 | `OpenSmoothEmbedding.improve_formalSol` |  |
| 45 | `FamilyOneJetSec.uncurry_mem_relativize` | 3 | %0,8 | `FamilyFormalSol.uncurry._proof_2` |  |
| 46 | `contDiff_barycentric` | 8 | %0,8 | `exist_loops` |  |
| 47 | `exist_loops_aux1` | 7 | %0,8 | `exist_loops_aux2` |  |
| 48 | `Orientation.contDiff_rot` | 24 | %0,8 | `formalEversionAux._proof_1` |  |
| 49 | `OpenSmoothEmbedding.range_transfer` | 1 | %0,8 | `OneJetBundle.embedding` |  |
| 50 | `transfer_localize` | 5 | %0,8 | `OpenSmoothEmbedding.improve_formalSol` |  |


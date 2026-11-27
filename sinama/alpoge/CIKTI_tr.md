# Kodun çıktısı: riemannHypothesis

*Bu belge bir yapay zekâ tarafından yazılmadı. Resmi Lean kaydından, sabit kurallarla üretildi (`arac/belge.py`). Aynı kayıtla çalıştıran herkes harfi harfine aynı belgeyi elde eder. Köşeli parantez içindeki adlar koddaki adlardır.*

## 1. Kanıtlanan cümle

Kodun kanıtladığı teorem `riemannHypothesis`. Önermesi:

> RiemannHypothesis.

Bu cümle yalnızca standart kütüphanedeki (Mathlib) 4.978 kavramla yazılmıştır; projeye özgü hiçbir tanım içermez. Yani neyin kanıtlandığını anlamak için proje kodunun hiçbir satırını okumak gerekmez.

## 2. İspatın omurgası

İspatın tamamı 1.265.256 bildirimdir. Aşağıdaki adımlar bunların içinden kurallı olarak seçildi: her seferinde, altında en çok ispat bulunan adım açıldı. Yüzde, ispatın ne kadarının yalnızca o adım için var olduğunu gösterir.

| Adım | Önerme | İspattaki payı |
|---:|---|---:|
| 1 | EveryCharacter. | %100,0 |
| 2 | Eğer Row ise EveryCharacter. | %79,2 |
| 3 | Eğer OpenLiteratureStatements ve VWin ise EveryCharacter. | %68,7 |
| 4 | Eğer UnitaryGroupThirdPlaceHypotheses ve ThetaLocalInputs ve ThetaIntegralsAgree ve LocalMatching ve CovolumeBoundOfX ve RecTExists ve VWin ise EveryCharacter. | %43,0 |
| 5 | (uzun; aşağıda) | %37,2 |
| 6 | (uzun; aşağıda) | %15,6 |
| 7 | Eğer LiteratureRankNHypothesis ise VWin. | %8,5 |
| 8 | Eğer HypothesesH' ise VWin. | %7,6 |

**Adım 1 — ispatın %100,0** [`UpperTheory.FinalTheorems.everyCharacter`]

Önermesi tek bir addan ibaret: **EveryCharacter**. Tanımı açıldığında:

> Her N ∈ ℕ, χ (N modülünde ℂ-değerli bir Dirichlet karakteri) ve s ∈ ℂ (koşullar: N ≠ 0) için: eğer 1 / 2 < Re(s) ve (χ ≠ 1 veya s ≠ 1) ise L(χ, s) ≠ 0.

Buraya şu adlar üzerinden gelinir; her birinin ispatının en az %97'si bir sonrakinin altındadır: `riemannHypothesis` → `rhOfAll` → `allChi`.

Dayandığı parçalar:
- %79,2: [`UpperTheory.FinalTheorems.everyCharacter_of_row`] → Adım 2
- %6,4: [`UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter`]
- %14,4: 58.062 küçük yardımcı sonuç

**Adım 2 — ispatın %79,2** [`UpperTheory.FinalTheorems.everyCharacter_of_row`]

> Eğer Row ise EveryCharacter.

Dayandığı parçalar:
- %68,7: [`UpperTheory.LiteratureTheorems.every_character_of_literature_of_vWin`] → Adım 3
- %8,5: [`UpperTheory.One.vwin_of_row`] → Adım 7
- %2,0: 7.841 küçük yardımcı sonuç

**Adım 3 — ispatın %68,7** [`UpperTheory.LiteratureTheorems.every_character_of_literature_of_vWin`]

> Eğer OpenLiteratureStatements ve VWin ise EveryCharacter.

Dayandığı parçalar:
- %43,0: [`UpperTheory.Lit.every_character_of_theta_integrals_local_matching`] → Adım 4
- %7,3: [`SelfIntersectionVolumeEstimates.topCovolSlim2_use_alt_alt`]
- %18,3: 50.467 küçük yardımcı sonuç

**Adım 4 — ispatın %43,0** [`UpperTheory.Lit.every_character_of_theta_integrals_local_matching`]

> Eğer UnitaryGroupThirdPlaceHypotheses ve ThetaLocalInputs ve ThetaIntegralsAgree ve LocalMatching ve CovolumeBoundOfX ve RecTExists ve VWin ise EveryCharacter.

Dayandığı parçalar:
- %37,2: [`UpperTheory.Lit.nonempty_hyps_definite_side_of_closed_bound`] → Adım 5
- %5,9: 19.000 küçük yardımcı sonuç

**Adım 5 — ispatın %37,2** [`UpperTheory.Lit.nonempty_hyps_definite_side_of_closed_bound`]

> Varsayalım (1): UnitaryGroupThirdPlaceHypotheses.
>
> Varsayalım (2): ThetaLocalInputs.
>
> Varsayalım (3): ThetaIntegralsAgree.
>
> Varsayalım (4): LocalMatching.
>
> Varsayalım (5): CovolumeBoundOfX.
>
> O zaman: her hL : RecTExists için: eğer (her cDep ∈ ℝ için: LinkedAt(parametersOfDependence(hL, cDep), (Q : Slot) (L : LkT(BundleCondition)) ↦ SlotNormCondition(Q, L, (𝒞 : FamClass) ↦ Closed((x : ℝ) ↦ 𝒞(x), (eps : ℝ) (Fm : FamP(eps)) (x : ℝ) ↦ BoundAtTwoThreeFamilyFonAlt(Fm))))) ise Nonempty(HypsAlt(NL, DefiniteSideCondition)).

Dayandığı parçalar:
- %15,6: [`GlobalTheory.Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt`] → Adım 6
- %3,0: [`GlobalTheory.Fc.S0.ontoX_and_lamLow_of_unitaryGroupHypotheses'`]
- %2,4: [`GlobalTheory.T.open0_of_unitary_group_hypotheses`]
- %16,1: 48.112 küçük yardımcı sonuç

**Adım 6 — ispatın %15,6** [`GlobalTheory.Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt`]

> Varsayalım (1): UnitaryGroupThirdPlaceHypotheses.
>
> Varsayalım (2): RowRat.
>
> O zaman: her hL : RecTExists, cDep ∈ ℝ ve A : AtP için: eğer EvLgG(A) ve LinkedAt(parametersOfDependence(hL, cDep), (Q : Slot) (L : LkT(BundleCondition)) ↦ SlotNormCondition(Q, L, (𝒞 : FamClass) ↦ Closed((x : ℝ) ↦ 𝒞(x), (eps : ℝ) (Fm : FamP(eps)) (x : ℝ) ↦ BoundAtTwoThreeFamilyFonAlt(Fm)))) ve LinkedAt(parametersOfExtension(extensionWithAtProperty(hL, extensionWithOrigin(hL, cDep), A), none, geoCl(anyGeometry)), FunctionalCondition) ve LinkedAt(parametersOfExtension(extensionWithAtProperty(hL, extensionWithOrigin(hL, cDep), A), none, geoCl(anyGeometry)), CovolumeBoundThirdPlaceSeries) ise Nonempty(HypsAlt(NL, DefiniteSideCondition)).

Dayandığı parçalar:
- %7,1: [`GlobalTheory.T.large_unramified_exponent_bundles_exist_alt`]
- %3,7: [`GlobalTheory.Fc.AllAtMemberStage0.allRows_of_open0_alt`]
- %2,6: [`UpperTheory.GalC.final_alt_alt`]
- %2,3: 5.587 küçük yardımcı sonuç

**Adım 7 — ispatın %8,5** [`UpperTheory.V.HV.DescentVanishingReductions.v_window_of_automorphy_csd_ss_mono_odd`]

> Eğer LiteratureRankNHypothesis ise VWin.

Buraya şu adlar üzerinden gelinir; her birinin ispatının en az %97'si bir sonrakinin altındadır: `UpperTheory.One.vwin_of_row` → `UpperTheory.One.Join.automorphic_window_of_inputs` → `UpperTheory.One.Join.v_window_of_depth_zero_residual_bc_cm` → `UpperTheory.V.v_window_of_literal_automorphy_n`.

Dayandığı parçalar:
- %7,6: [`UpperTheory.V.HV.DescentVanishingReductions.vwin_of_hypotheses_H_E_alt`] → Adım 8
- %0,8: 1.185 küçük yardımcı sonuç

**Adım 8 — ispatın %7,6** [`UpperTheory.V.HV.DescentVanishingReductions.vwin_of_hypotheses_H_E_alt`]

> Eğer HypothesesH' ise VWin.

## 3. Adı geçen ara önermeler

Yukarıdaki cümlelerde tek kelimeyle geçen önermeler projenin kendi tanımlarıdır. Kısa olanların tanımı aynı kurallarla aşağıdadır.

- **Row** [`UpperTheory.One.M.Row`]: Row0b((E : Type) (Ω : Type) [Field(E)] [NumberField(E)] [Field(Ω)] [Algebra(E, Ω)] [IsAlgClosure(E, Ω)] (A : ValuationSubring(Ω)) (w : HeightOneSpectrum(RingOfIntegers(E))) (h : IsPlaceOver(A, w)) (rc : IrrGL(adicCompletion(E, w)) → WD(h)) ↦ IsRecT(h, rc)).
  - Row0b(Rc) şu demektir (Rc : RecNotion için): her E : Type, Ω : Type, l ∈ ℕ, ι : RingEquiv(Qbar(l), ℂ) ve x ∈ ℕ (koşullar: [Field(E)], [NumberField(E)], [IsCMField(E)], [Field(Ω)], [Algebra(E, Ω)], [IsAlgClosure(E, Ω)], Prime(l)) için: eğer 1 ≤ x ise (her π : CuspSub(E, x) ve χ : HChar(Subtype((x2 : E) ↦ x2 ∈ maximalRealSubfield(E))) için: eğer IsRegAlg(CG.mk(π)) ve PolarizedPair(π, χ) ise öyle bir r : G(E, Ω) →* GeneralLinearGroup(Fin(x), Qbar(l)), wt ∈ ℤ ve HT : (E →+* Qbar(l)) → Multiset ℤ vardır ki PropsB((E2 : Type) (Ω2 : Type) [Field(E2)] [NumberField(E2)] [Field(Ω2)] [Algebra(E2, Ω2)] [IsAlgClosure(E2, Ω2)] (A : ValuationSubring(Ω2)) (w : HeightOneSpectrum(RingOfIntegers(E2))) ↦ Rc(E2, Ω2, A, w), π, ι, r, wt, HT)).
- **EveryCharacter** [`UpperTheory.EveryCharacter`]: Her N ∈ ℕ, χ (N modülünde ℂ-değerli bir Dirichlet karakteri) ve s ∈ ℂ (koşullar: N ≠ 0) için: eğer 1 / 2 < Re(s) ve (χ ≠ 1 veya s ≠ 1) ise L(χ, s) ≠ 0.
- **OpenLiteratureStatements** [`UpperTheory.LiteratureTheorems.OpenLiteratureStatements`]: birkaç koşulun bir arada tutulduğu bir pakettir (Lean yapısı).
  - `caraianiLocalGlobalDual`: Row
  - `localLanglandsExists`: RecTExists
  - `galoisRepOfPolarizedPairLit`: Row
- **VWin** [`UpperTheory.Top.VWin`]: Her ψ : PChar için: VWinAt(ψ, 401).
- **UnitaryGroupThirdPlaceHypotheses** [`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses`]: birkaç koşulun bir arada tutulduğu bir pakettir (Lean yapısı).
- **ThetaLocalInputs** [`GlobalTheory.FunPr.ThetaLocalInputs`]: birkaç koşulun bir arada tutulduğu bir pakettir (Lean yapısı).
- **ThetaIntegralsAgree** [`GlobalTheory.IndefiniteRowSideFullHecke.WeilTensorModels.ThetaIntegralsAgree`]: tanımı kısa bir cümleye sığmıyor (960 karakter). Tam hali uzun çıktıdadır.
- **LocalMatching** [`GlobalTheory.IndefiniteRowSideFullHecke.WeilTensorModels.LocalMatching`]: tanımı kısa bir cümleye sığmıyor (398 karakter). Tam hali uzun çıktıdadır.
- **CovolumeBoundOfX** [`GlobalTheory.CovTop.CovolumeBoundOfX`]: Closed((eps : ℝ) ↦ FamHyp(eps), (eps : ℝ) (Fm : FamP(eps)) (CH : ℝ) ↦ ∃ (C0 : ℝ), 0 ≤ C0 ∧ EventuallyAtAllPoints(Fm, (x : ℝ) (x2 : x1(toFamCore(Fm)) < x) (x3 : Ix(toFamCore(Fm), x)) (p : Pt(Fm, x, x2, x3)) ↦ ∀ (C : ℝ), C0 ≤ C → L3(…, …))).
  - Closed(𝒞, P) şu demektir (𝒞 : FamClass ve P : ∀ (eps : ℝ), FamP(eps) → ℝ → Prop için): öyle bir ε1 ∈ ℝ vardır ki (0 < ε1 ve (her eps ∈ ℝ için: eğer 0 < eps ve eps ≤ ε1 ise öyle bir K : TransportedAlt vardır ki (her Fm : FamP(eps), CH ∈ ℝ ve x : 𝒞(eps, Fm) için: eğer Large(Fm, K, CH) ise P(eps, Fm, CH)))).
- **RecTExists** [`UpperTheory.Zero.LLC.RecTExists`]: tanımı kısa bir cümleye sığmıyor (287 karakter). Tam hali uzun çıktıdadır.
- **RowRat** [`GlobalTheory.Fc.S0.RowRat`]: tanımı kısa bir cümleye sığmıyor (260 karakter). Tam hali uzun çıktıdadır.
- **LiteratureRankNHypothesis** [`GlobalTheory.Mem.LiteralAutomorphy.LiteratureRankNHypothesis`]: birkaç koşulun bir arada tutulduğu bir pakettir (Lean yapısı).
  - `loc`: LitLocAlt
  - `aut`: LiteratureAutomorphyHypothesis
  - `coh`: LitCoh
  - `cm`: LiteratureCMHypothesis
- **HypothesesH'** [`UpperTheory.V.Af.HypothesesH'`]: birkaç koşulun bir arada tutulduğu bir pakettir (Lean yapısı).

## 4. Sayılar

| | |
|---|---:|
| Projenin bildirimi | 1.270.184 |
| Bunlardan teorem | 1.075.031 |
| Ana teoremin kullandığı | 1.265.256 |
| Ana teoremin hiç kullanmadığı | 4.928 |
| Önermesi başka bir teoreminkiyle birebir aynı olan fazladan teorem | 260.240 (%24,2) |

## 5. Bu belge nasıl denetlenir

1. Kayıt: Lean'in resmi dışa aktarımı (`solution.ndjson.zst`), Lean çekirdeği tarafından doğrulanmış haliyle.
2. Omurga: kayıttaki bağımlılıklardan hesaplanan baskınlık ağacı. "Yalnızca o adım için var" ifadesi tanım gereği kesindir.
3. Cümleler: önermenin mantık iskeleti sabit kalıplarla yazılır (her, vardır, eğer–ise, ve, veya, değil); formüller kayıttaki terimden aynen basılır.
4. Yorum yok: belgede kayıtta bulunmayan hiçbir açıklama, niyet ya da değerlendirme yer almaz.

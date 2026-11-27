# What the code proves: riemannHypothesis

*This document was not written by an AI. It was produced from the official Lean export by fixed rules (`arac/belge.py`). Anyone running the same export obtains the same document, character for character. Names in brackets are the names used in the code.*

## 1. The statement proved

The theorem proved by the code is `riemannHypothesis`. Its statement:

> RiemannHypothesis.

This sentence is written only with 4,978 concepts of the standard library (Mathlib); it contains no project-specific definition. So understanding what is proved requires reading none of the project's code.

## 2. The spine of the proof

The whole proof consists of 1,265,256 declarations. The steps below were selected from them by rule: each time, the step with the most proof beneath it was opened. The percentage is the share of the proof that exists only for that step.

| Step | Statement | Share of the proof |
|---:|---|---:|
| 1 | EveryCharacter. | 100.0% |
| 2 | If Row then EveryCharacter. | 79.2% |
| 3 | If OpenLiteratureStatements and VWin then EveryCharacter. | 68.7% |
| 4 | If UnitaryGroupThirdPlaceHypotheses and ThetaLocalInputs and ThetaIntegralsAgree and LocalMatching and CovolumeBoundOfX and RecTExists and VWin then EveryCharacter. | 43.0% |
| 5 | (long; see below) | 37.2% |
| 6 | (long; see below) | 15.6% |
| 7 | If LiteratureRankNHypothesis then VWin. | 8.5% |
| 8 | If HypothesesH' then VWin. | 7.6% |

**Step 1 — 100.0% of the proof** [`UpperTheory.FinalTheorems.everyCharacter`]

Its statement is a single name: **EveryCharacter**. Unfolding the definition:

> For every N ∈ ℕ, χ (a ℂ-valued Dirichlet character modulo N) and s ∈ ℂ (with: N ≠ 0): if 1 / 2 < Re(s) and (χ ≠ 1 or s ≠ 1) then L(χ, s) ≠ 0.

It is reached through these names; at least 97% of the proof of each lies under the next: `riemannHypothesis` → `rhOfAll` → `allChi`.

It rests on:
- 79.2%: [`UpperTheory.FinalTheorems.everyCharacter_of_row`] → Step 2
- 6.4%: [`UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter`]
- 14.4%: 58,062 small auxiliary results

**Step 2 — 79.2% of the proof** [`UpperTheory.FinalTheorems.everyCharacter_of_row`]

> If Row then EveryCharacter.

It rests on:
- 68.7%: [`UpperTheory.LiteratureTheorems.every_character_of_literature_of_vWin`] → Step 3
- 8.5%: [`UpperTheory.One.vwin_of_row`] → Step 7
- 2.0%: 7,841 small auxiliary results

**Step 3 — 68.7% of the proof** [`UpperTheory.LiteratureTheorems.every_character_of_literature_of_vWin`]

> If OpenLiteratureStatements and VWin then EveryCharacter.

It rests on:
- 43.0%: [`UpperTheory.Lit.every_character_of_theta_integrals_local_matching`] → Step 4
- 7.3%: [`SelfIntersectionVolumeEstimates.topCovolSlim2_use_alt_alt`]
- 18.3%: 50,467 small auxiliary results

**Step 4 — 43.0% of the proof** [`UpperTheory.Lit.every_character_of_theta_integrals_local_matching`]

> If UnitaryGroupThirdPlaceHypotheses and ThetaLocalInputs and ThetaIntegralsAgree and LocalMatching and CovolumeBoundOfX and RecTExists and VWin then EveryCharacter.

It rests on:
- 37.2%: [`UpperTheory.Lit.nonempty_hyps_definite_side_of_closed_bound`] → Step 5
- 5.9%: 19,000 small auxiliary results

**Step 5 — 37.2% of the proof** [`UpperTheory.Lit.nonempty_hyps_definite_side_of_closed_bound`]

> Assume (1): UnitaryGroupThirdPlaceHypotheses.
>
> Assume (2): ThetaLocalInputs.
>
> Assume (3): ThetaIntegralsAgree.
>
> Assume (4): LocalMatching.
>
> Assume (5): CovolumeBoundOfX.
>
> Then: for every hL : RecTExists: if (for every cDep ∈ ℝ: LinkedAt(parametersOfDependence(hL, cDep), (Q : Slot) (L : LkT(BundleCondition)) ↦ SlotNormCondition(Q, L, (𝒞 : FamClass) ↦ Closed((x : ℝ) ↦ 𝒞(x), (eps : ℝ) (Fm : FamP(eps)) (x : ℝ) ↦ BoundAtTwoThreeFamilyFonAlt(Fm))))) then Nonempty(HypsAlt(NL, DefiniteSideCondition)).

It rests on:
- 15.6%: [`GlobalTheory.Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt`] → Step 6
- 3.0%: [`GlobalTheory.Fc.S0.ontoX_and_lamLow_of_unitaryGroupHypotheses'`]
- 2.4%: [`GlobalTheory.T.open0_of_unitary_group_hypotheses`]
- 16.1%: 48,112 small auxiliary results

**Step 6 — 15.6% of the proof** [`GlobalTheory.Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt`]

> Assume (1): UnitaryGroupThirdPlaceHypotheses.
>
> Assume (2): RowRat.
>
> Then: for every hL : RecTExists, cDep ∈ ℝ and A : AtP: if EvLgG(A) and LinkedAt(parametersOfDependence(hL, cDep), (Q : Slot) (L : LkT(BundleCondition)) ↦ SlotNormCondition(Q, L, (𝒞 : FamClass) ↦ Closed((x : ℝ) ↦ 𝒞(x), (eps : ℝ) (Fm : FamP(eps)) (x : ℝ) ↦ BoundAtTwoThreeFamilyFonAlt(Fm)))) and LinkedAt(parametersOfExtension(extensionWithAtProperty(hL, extensionWithOrigin(hL, cDep), A), none, geoCl(anyGeometry)), FunctionalCondition) and LinkedAt(parametersOfExtension(extensionWithAtProperty(hL, extensionWithOrigin(hL, cDep), A), none, geoCl(anyGeometry)), CovolumeBoundThirdPlaceSeries) then Nonempty(HypsAlt(NL, DefiniteSideCondition)).

It rests on:
- 7.1%: [`GlobalTheory.T.large_unramified_exponent_bundles_exist_alt`]
- 3.7%: [`GlobalTheory.Fc.AllAtMemberStage0.allRows_of_open0_alt`]
- 2.6%: [`UpperTheory.GalC.final_alt_alt`]
- 2.3%: 5,587 small auxiliary results

**Step 7 — 8.5% of the proof** [`UpperTheory.V.HV.DescentVanishingReductions.v_window_of_automorphy_csd_ss_mono_odd`]

> If LiteratureRankNHypothesis then VWin.

It is reached through these names; at least 97% of the proof of each lies under the next: `UpperTheory.One.vwin_of_row` → `UpperTheory.One.Join.automorphic_window_of_inputs` → `UpperTheory.One.Join.v_window_of_depth_zero_residual_bc_cm` → `UpperTheory.V.v_window_of_literal_automorphy_n`.

It rests on:
- 7.6%: [`UpperTheory.V.HV.DescentVanishingReductions.vwin_of_hypotheses_H_E_alt`] → Step 8
- 0.8%: 1,185 small auxiliary results

**Step 8 — 7.6% of the proof** [`UpperTheory.V.HV.DescentVanishingReductions.vwin_of_hypotheses_H_E_alt`]

> If HypothesesH' then VWin.

## 3. Intermediate statements named above

Statements that appear above as a single word are the project's own definitions. The short ones are given below by the same rules.

- **Row** [`UpperTheory.One.M.Row`]: Row0b((E : Type) (Ω : Type) [Field(E)] [NumberField(E)] [Field(Ω)] [Algebra(E, Ω)] [IsAlgClosure(E, Ω)] (A : ValuationSubring(Ω)) (w : HeightOneSpectrum(RingOfIntegers(E))) (h : IsPlaceOver(A, w)) (rc : IrrGL(adicCompletion(E, w)) → WD(h)) ↦ IsRecT(h, rc)).
  - Row0b(Rc) means (for Rc : RecNotion): for every E : Type, Ω : Type, l ∈ ℕ, ι : RingEquiv(Qbar(l), ℂ) and x ∈ ℕ (with: [Field(E)], [NumberField(E)], [IsCMField(E)], [Field(Ω)], [Algebra(E, Ω)], [IsAlgClosure(E, Ω)], Prime(l)): if 1 ≤ x then (for every π : CuspSub(E, x) and χ : HChar(Subtype((x2 : E) ↦ x2 ∈ maximalRealSubfield(E))): if IsRegAlg(CG.mk(π)) and PolarizedPair(π, χ) then there exists r : G(E, Ω) →* GeneralLinearGroup(Fin(x), Qbar(l)), wt ∈ ℤ and HT : (E →+* Qbar(l)) → Multiset ℤ such that PropsB((E2 : Type) (Ω2 : Type) [Field(E2)] [NumberField(E2)] [Field(Ω2)] [Algebra(E2, Ω2)] [IsAlgClosure(E2, Ω2)] (A : ValuationSubring(Ω2)) (w : HeightOneSpectrum(RingOfIntegers(E2))) ↦ Rc(E2, Ω2, A, w), π, ι, r, wt, HT)).
- **EveryCharacter** [`UpperTheory.EveryCharacter`]: For every N ∈ ℕ, χ (a ℂ-valued Dirichlet character modulo N) and s ∈ ℂ (with: N ≠ 0): if 1 / 2 < Re(s) and (χ ≠ 1 or s ≠ 1) then L(χ, s) ≠ 0.
- **OpenLiteratureStatements** [`UpperTheory.LiteratureTheorems.OpenLiteratureStatements`]: a bundle of several conditions (a Lean structure).
  - `caraianiLocalGlobalDual`: Row
  - `localLanglandsExists`: RecTExists
  - `galoisRepOfPolarizedPairLit`: Row
- **VWin** [`UpperTheory.Top.VWin`]: For every ψ : PChar: VWinAt(ψ, 401).
- **UnitaryGroupThirdPlaceHypotheses** [`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses`]: a bundle of several conditions (a Lean structure).
- **ThetaLocalInputs** [`GlobalTheory.FunPr.ThetaLocalInputs`]: a bundle of several conditions (a Lean structure).
- **ThetaIntegralsAgree** [`GlobalTheory.IndefiniteRowSideFullHecke.WeilTensorModels.ThetaIntegralsAgree`]: its definition does not fit in a short sentence (968 characters). The full form is in the long output.
- **LocalMatching** [`GlobalTheory.IndefiniteRowSideFullHecke.WeilTensorModels.LocalMatching`]: its definition does not fit in a short sentence (400 characters). The full form is in the long output.
- **CovolumeBoundOfX** [`GlobalTheory.CovTop.CovolumeBoundOfX`]: Closed((eps : ℝ) ↦ FamHyp(eps), (eps : ℝ) (Fm : FamP(eps)) (CH : ℝ) ↦ ∃ (C0 : ℝ), 0 ≤ C0 ∧ EventuallyAtAllPoints(Fm, (x : ℝ) (x2 : x1(toFamCore(Fm)) < x) (x3 : Ix(toFamCore(Fm), x)) (p : Pt(Fm, x, x2, x3)) ↦ ∀ (C : ℝ), C0 ≤ C → L3(…, …))).
  - Closed(𝒞, P) means (for 𝒞 : FamClass and P : ∀ (eps : ℝ), FamP(eps) → ℝ → Prop): there exists ε1 ∈ ℝ such that (0 < ε1 and (for every eps ∈ ℝ: if 0 < eps and eps ≤ ε1 then there exists K : TransportedAlt such that (for every Fm : FamP(eps), CH ∈ ℝ and x : 𝒞(eps, Fm): if Large(Fm, K, CH) then P(eps, Fm, CH)))).
- **RecTExists** [`UpperTheory.Zero.LLC.RecTExists`]: its definition does not fit in a short sentence (289 characters). The full form is in the long output.
- **RowRat** [`GlobalTheory.Fc.S0.RowRat`]: its definition does not fit in a short sentence (260 characters). The full form is in the long output.
- **LiteratureRankNHypothesis** [`GlobalTheory.Mem.LiteralAutomorphy.LiteratureRankNHypothesis`]: a bundle of several conditions (a Lean structure).
  - `loc`: LitLocAlt
  - `aut`: LiteratureAutomorphyHypothesis
  - `coh`: LitCoh
  - `cm`: LiteratureCMHypothesis
- **HypothesesH'** [`UpperTheory.V.Af.HypothesesH'`]: a bundle of several conditions (a Lean structure).

## 4. Numbers

| | |
|---|---:|
| Declarations in the project | 1,270,184 |
| of which theorems | 1,075,031 |
| Used by the main theorem | 1,265,256 |
| Never used by the main theorem | 4,928 |
| Redundant theorems whose statement is identical to another theorem's | 260,240 (24.2%) |

## 5. How to check this document

1. Record: Lean's official export (`solution.ndjson.zst`), as verified by the Lean kernel.
2. Spine: the dominator tree computed from the dependencies in the record. "Exists only for that step" is exact by definition.
3. Sentences: the logical skeleton of each statement is written with fixed templates (for every, exists, if–then, and, or, not); formulas are printed from the recorded term unchanged.
4. No interpretation: the document contains no explanation, intent or judgement that is not in the record.

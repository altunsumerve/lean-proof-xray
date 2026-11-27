# What the code proves: riemannHypothesis

*This document was not written by an AI. It was produced from the official Lean export by fixed rules (`arac/belge.py`). Anyone running the same export obtains the same document, character for character. Names in brackets are the names used in the code.*

## 1. The statement proved

The theorem proved by the code is `riemannHypothesis`. Its statement:

> RiemannHypothesis.

This sentence is written only with 5,021 concepts of the standard library (Mathlib); it contains no project-specific definition. So understanding what is proved requires reading none of the project's code.

## 2. The spine of the proof

The whole proof consists of 49,815 declarations. The steps below were selected from them by rule: each time, the step with the most proof beneath it was opened. The percentage is the share of the proof that exists only for that step.

| Step | Statement | Share of the proof |
|---:|---|---:|
| 1 | (long; see below) | 100.0% |
| 2 | For every P : Parameters and D : Data(P): ↑m(D) · totalRemainder(D) ≤ ↑f(D) · ↑a(D) · logB(D) ^ (5 : ℕ). | 93.8% |
| 3 | (long; see below) | 55.7% |
| 4 | (long; see below) | 46.6% |
| 5 | For every P : Parameters and D : Data(P): there exists θ : PrimePadicIso → MFoldTwist(D) such that IsRegularFamily(D, θ). | 40.2% |
| 6 | (long; see below) | 35.1% |
| 7 | (long; see below) | 17.1% |
| 8 | (long; see below) | 16.4% |

**Step 1 — 100.0% of the proof** [`New.eventually_primeRemainder_natCast_le`]

> For every P : Parameters and ε ∈ ℝ: if 0 < ε and ε < 1 / 100 then Eventually((x : ℕ) ↦ primeRemainder(d(P), q₀(P), ↑x) ≤ (64 · ↑totient(q₀(P)) + 3) · ↑x ^ (−1 / 2 + 6 · ε), atTop).

It is reached through these names; at least 97% of the proof of each lies under the next: `riemannHypothesis` → `New.grh` → `New.eventually_primeRemainder_le_rpow`.

It rests on:
- 93.8%: [`New.Data.primeRemainder_le`] → Step 2
- 5.9%: 2,487 small auxiliary results

**Step 2 — 93.8% of the proof** [`New.star_inequality`]

> For every P : Parameters and D : Data(P): ↑m(D) · totalRemainder(D) ≤ ↑f(D) · ↑a(D) · logB(D) ^ (5 : ℕ).

It is reached through these names; at least 97% of the proof of each lies under the next: `New.Data.primeRemainder_le`.

It rests on:
- 55.7%: [`New.Data.integral_forms_long`] → Step 3
- 3.9%: [`New.Data.seesaw_identity`]
- 3.3%: [`New.Data.exists_err_gaugeLe_compositeLift`]
- 30.9%: 6,854 small auxiliary results

**Step 3 — 55.7% of the proof** [`New.Data.integral_forms_long`]

> ∀ (P : Parameters) (D : Data(P)) (n : ℕ), (Fin(n) → Subtype((x : Subtype((x : Form(spaceY(D, 0), typeKernel(paramW(D), signsY(D, 0)))) ↦ x ∈ principalForms(D, spaceY(D, 0)))) ↦ … ∈ …)) → …. [Note: the parts shown as "…" were cut by the dump's size limit; the sentence is incomplete.]

It rests on:
- 46.6%: [`New.Data.exists_hasSmallRatios_heightLe_liftDeterminant_div`] → Step 4
- 3.9%: [`New.Exchange.exchange_identity`]
- 2.1%: [`New.Data.exists_span_isAuxiliaryForm_eq_top`]
- 3.2%: 658 small auxiliary results

**Step 4 — 46.6% of the proof** [`New.Data.exists_hasSmallRatios_heightLe_liftDeterminant_div`]

> For every P : Parameters and D : Data(P): there exists θ : PrimePadicIso → MFoldTwist(D) such that (HasSmallRatios(D, θ) and (for every j ∈ ℕ: if j ∈ Icc(1, m(D)) then HeightLe(↑targetDim(D) · (↑f(D) · ↑a(D) · logB(D) ^ (4 : ℕ) / ↑m(D) − ↑k(D) · directionAmount(D)), (ι : PrimePadicIso) ↦ liftDeterminant(D, 1, j) / liftDeterminant(D, θ(ι), j)))).

It rests on:
- 40.2%: [`New.exists_isRegularFamily`] → Step 5
- 5.3%: [`New.Data.heightLe_liftDeterminant_ratio`]
- 1.1%: 276 small auxiliary results

**Step 5 — 40.2% of the proof** [`New.exists_isRegularFamily`]

> For every P : Parameters and D : Data(P): there exists θ : PrimePadicIso → MFoldTwist(D) such that IsRegularFamily(D, θ).

It rests on:
- 35.1%: [`New.Selmer.exists_mFoldTwist_hasDenominatorsLe`] → Step 6
- 4.3%: [`New.Selmer.sum_clearingBound_add_padicValNat_le`]
- 0.9%: 155 small auxiliary results

**Step 6 — 35.1% of the proof** [`New.Selmer.exists_mFoldTwist_hasDenominatorsLe`]

> Given: P : Parameters, D : Data(P), ℓ ∈ ℕ and ι : PadicIso(ℓ) (with: [ThePrime(ℓ)]).
>
> Then: there exists τ : MFoldTwist(D) such that (Coprime(ℓ, normQ(toTameChar(toTwist(τ)))) and (for every j : Elem(LiftIndex(D)), p : CriticalPair(D) and s : Units(ℤ): if IsRamified(p) then ‖ιℓ((ratio(p, toTameChar(powTwist(τ, j)), s))⁻¹)‖ ≤ exp(↑twistError(ℓ, D) · log(↑ℓ))) and (for every j : Elem(LiftIndex(D)): HasDenominatorsLe(D, ιℓ, powTwist(τ, j), ↑j, ↑clearingBound(D, ℓ) · log(↑ℓ) + ↑padicValNat(ℓ, card(StdClasses(chosenLevel))) · log(↑ℓ)))).

It rests on:
- 17.1%: [`New.GaloisRep.sphericalCompat_of_odd`] → Step 7
- 7.2%: [`New.Selmer.denominatorLe_clearingBound`]
- 10.8%: 1,749 small auxiliary results

**Step 7 — 17.1% of the proof** [`New.GaloisRep.sphericalCompat_of_split`]

> Given: ℓ ∈ ℕ, E : Type, x ∈ ℕ and D ∈ ℕ (with: [ThePrime(ℓ)], [PadicIso(ℓ)], [Field(E)], [CMType(E)], [EmbeddedNumberField(E)], [HasPrimitiveRoot5040(E)]).
>
> Assume (1): Odd(x).
>
> Then: for every u : FinPlace(E) (with: [HasQuadSubfield(D, E)]): if (for every v : FinPlace(E): if (↑ℓ ∈ asIdeal(v) or v = u) then IsSplitPrimeToDisc(below(Subtype((x2 : ℂ) ↦ x2 ∈ QuadField(D)), v))) then SphericalCompat(E, Fin(x), x, u).

It is reached through these names; at least 97% of the proof of each lies under the next: `New.GaloisRep.sphericalCompat_of_odd`.

It rests on:
- 16.4%: [`_private.Lib.GaloisRep.Main.SplitCase.0.New.GaloisRep.exists_rep_of_free_weight`] → Step 8
- 0.5%: 53 small auxiliary results

**Step 8 — 16.4% of the proof** [`_private.Lib.GaloisRep.Main.SeedRepresentation.0.New.GaloisRep.exists_padicRep_of_cuspidal_type_at_embedding`]

> Given: ℓ ∈ ℕ, E : Type, x ∈ ℕ and d ∈ ℕ (with: [ThePrime(ℓ)], [PadicIso(ℓ)], [Field(E)], [CMType(E)], [EmbeddedNumberField(E)], [HasQuadSubfield(d, E)], [HasPrimitiveRoot5040(E)]).
>
> Assume (1): Odd(x).
>
> Then: ∀ (κ : Weight(E)) (f : Gf(E, Fin(x)) → WeylIndex(Fin(x), κ.1) → ℂ), f ∈ forms(stdSpace(E, Fin(x)), κ) → (∀ (S : Finset (FinPlace(E))) (P : FinPlace(E) → Polynomial(ℂ)), IsSphericalOff(S, f, P) → (∀ (w₀ : FinPlace(E)), FinPlace(E) → w₀ ∈ S → IsSplitPrimeToDisc(below(Subtype((x2 : ℂ) ↦ x2 ∈ QuadField(d)), w₀)) → (∀ (χ : Subtype((x2 : GeneralLinearGroup(Fin(x), LocField(w₀))) ↦ x2 ∈ localCongruence(Fin(x), w₀, 0)) →* ℂ), IsCuspidalType(localCongruence(Fin(x), w₀, 0), χ) → (Subtype((x2 : GeneralLinearGroup(Fin(x), LocField(w₀))) ↦ … ∈ …) → …) → …))).

It is reached through these names; at least 97% of the proof of each lies under the next: `_private.Lib.GaloisRep.Main.SplitCase.0.New.GaloisRep.exists_rep_of_free_weight` → `New.GaloisRep.exists_rep_of_cuspidal_type`.

It rests on:
- 15.1%: [`_private.Lib.GaloisRep.Main.SeedRepresentation.0.New.GaloisRep.exists_padicRep_of_pel`]
- 1.0%: 193 small auxiliary results

## 4. Numbers

| | |
|---|---:|
| Declarations in the project | 50,275 |
| of which theorems | 42,204 |
| Used by the main theorem | 49,815 |
| Never used by the main theorem | 460 |
| Redundant theorems whose statement is identical to another theorem's | 8,586 (20.3%) |

## 5. How to check this document

1. Record: Lean's official export (`solution.ndjson.zst`), as verified by the Lean kernel.
2. Spine: the dominator tree computed from the dependencies in the record. "Exists only for that step" is exact by definition.
3. Sentences: the logical skeleton of each statement is written with fixed templates (for every, exists, if–then, and, or, not); formulas are printed from the recorded term unchanged.
4. No interpretation: the document contains no explanation, intent or judgement that is not in the record.

# What the code proves: riemannHypothesis

*This document was not written by an AI. It was produced from the official Lean export by fixed rules (`arac/belge.py`). Anyone running the same export obtains the same document, character for character. Names in brackets are the names used in the code.*

## 1. The statement proved

The theorem proved by the code is `riemannHypothesis`. Its statement:

> RiemannHypothesis.

This sentence is written only with 5,021 concepts of the standard library (Mathlib); it contains no project-specific definition. So understanding what is proved requires reading none of the project's code.

## 2. The spine of the proof

The whole proof consists of 37,561 declarations. The steps below were selected from them by rule: each time, the step with the most proof beneath it was opened. The percentage is the share of the proof that exists only for that step.

| Step | Statement | Share of the proof |
|---:|---|---:|
| 1 | For every P : Parameters and ε ∈ ℝ: if (0 < ε / 6 and ε < 1 / 100) then Eventually((x : ℝ) ↦ primeError(d(P), N₀(P), x) ≤ x ^ (8 · ε + 2⁻¹ − 1), atTop). | 100.0% |
| 2 | For every P : Parameters and D : Data(P): ↑m(D) · remainder(D) ≤ logB(D) ^ (2 : ℕ) · budget(D). | 93.4% |
| 3 | (long; see below) | 20.2% |
| 4 | (long; see below) | 19.1% |
| 5 | (long; see below) | 18.2% |
| 6 | For every P : Parameters and D : Data(P): there exists θ : PrimePadicIso → MFoldTwist(D) such that IsFitFamily(D, θ). | 11.5% |
| 7 | (long; see below) | 10.4% |
| 8 | For every P : Parameters and D : Data(P): there exists n ∈ ℕ and y : Fin(n) → SubmoduleElem(rows(D)) such that (LinearIndependent(ℂ, y) and …). | 7.8% |

**Step 1 — 100.0% of the proof** [`eventually_primeError_le_rpow`]

> For every P : Parameters and ε ∈ ℝ: if (0 < ε / 6 and ε < 1 / 100) then Eventually((x : ℝ) ↦ primeError(d(P), N₀(P), x) ≤ x ^ (8 · ε + 2⁻¹ − 1), atTop).

It is reached through these names; at least 97% of the proof of each lies under the next: `riemannHypothesis` → `New.grh`.

It rests on:
- 93.4%: [`star_inequality`] → Step 2
- 6.3%: 2,454 small auxiliary results

**Step 2 — 93.4% of the proof** [`star_inequality`]

> For every P : Parameters and D : Data(P): ↑m(D) · remainder(D) ≤ logB(D) ^ (2 : ℕ) · budget(D).

It rests on:
- 20.2%: [`Data.integral_forms_long`] → Step 3
- 19.1%: [`sphericalCompat_of_odd`] → Step 4
- 7.8%: [`Data.exists_family_covolumeSq_le`] → Step 8
- 5.4%: [`Data.ramifiedColumns_fill_rows`]
- 3.8%: [`exchange_theorem`]
- 37.1%: 6,907 small auxiliary results

**Step 3 — 20.2% of the proof** [`Data.integral_forms_long`]

> ∀ (P : Parameters) (D : Data(P)) (n : ℕ) (y : Fin(n) → SubmoduleElem(rows(D))) (δ : ℝ), ℝ → LinearIndependent(ℂ, y) → (1 − 4 / b(D) ^ (2 : ℕ)) · ↑rowDim(D) ≤ ↑n → IndexLe(D, y, δ) → (RingEquiv(ℂ, ℂ) → covolumeSq(… ∘ …, …) ≤ …) → …. [Note: the parts shown as "…" were cut by the dump's size limit; the sentence is incomplete.]

It rests on:
- 11.5%: [`exists_isFitFamily`] → Step 6
- 4.7%: [`Data.heightLe_volume_ratio_sq`]
- 2.9%: [`Data.heightLe_volume_rows`]
- 1.1%: 153 small auxiliary results

**Step 4 — 19.1% of the proof** [`sphericalCompat_of_split`]

> For every ℓ ∈ ℕ, E : Type, x ∈ ℕ and D ∈ ℕ (with: [ThePrime(ℓ)], [PadicIso(ℓ)], [Field(E)], [CMType(E)], [EmbeddedNumberField(E)], [StablyUnram(E)]): if Odd(x) then (for every u : FinPlace(E) (with: [HasQuadSubfield(D, E)]): if (for every v : FinPlace(E): if (↑ℓ ∈ asIdeal(v) or v = u) then IsSplitPrimeToDisc(below(Subtype((x2 : ℂ) ↦ x2 ∈ QuadField(D)), v))) then SphericalCompat(E, Fin(x), x, u)).

It is reached through these names; at least 97% of the proof of each lies under the next: `sphericalCompat_of_odd`.

It rests on:
- 18.2%: [`exists_rep_of_cuspidal_type`] → Step 5
- 0.5%: 54 small auxiliary results

**Step 5 — 18.2% of the proof** [`exists_rep_of_cuspidal_type`]

> Given: ℓ ∈ ℕ, E : Type, x ∈ ℕ and d ∈ ℕ (with: [ThePrime(ℓ)], [PadicIso(ℓ)], [Field(E)], [CMType(E)], [EmbeddedNumberField(E)], [HasQuadSubfield(d, E)], [StablyUnram(E)]).
>
> Assume (1): Odd(x).
>
> Then: ∀ (κ : Weight(E)) (f : Gf(E, Fin(x)) → WeylIndex(Fin(x), κ.1) → ℂ), f ∈ forms(stdSpace(E, Fin(x)), κ) → (∀ (S : Finset (FinPlace(E))) (P : FinPlace(E) → Polynomial(ℂ)), IsSphericalOff(S, f, P) → (∀ (w₀ : FinPlace(E)), FinPlace(E) → w₀ ∈ S → IsSplitPrimeToDisc(below(Subtype((x2 : ℂ) ↦ x2 ∈ QuadField(d)), w₀)) → (∀ (χ : Subtype((x2 : GeneralLinearGroup(Fin(x), LocField(w₀))) ↦ x2 ∈ localCongruence(Fin(x), w₀, 0)) →* ℂ), IsCuspidalType(localCongruence(Fin(x), w₀, 0), χ) → (Subtype((x2 : GeneralLinearGroup(Fin(x), LocField(w₀))) ↦ x2 ∈ localCongruence(Fin(x), w₀, 0)) → …(…) = …) → …))).

It rests on:
- 10.4%: [`Model.exists_galois_rep`] → Step 7
- 2.1%: [`nonempty_universalFamily`]
- 5.6%: 882 small auxiliary results

**Step 6 — 11.5% of the proof** [`exists_isFitFamily`]

> For every P : Parameters and D : Data(P): there exists θ : PrimePadicIso → MFoldTwist(D) such that IsFitFamily(D, θ).

It rests on:
- 7.0%: [`denominatorLe_rowBudget`]
- 4.5%: 410 small auxiliary results

**Step 7 — 10.4% of the proof** [`Model.exists_galois_rep`]

> Given: E : Type, x ∈ ℕ, d₀ ∈ ℕ, 𝔑 : RingOfIntegers(E), ν ∈ ℕ, R : Subalgebra(RingOfIntegers(E), E), X : Model(Fin(x), d₀, 𝔑, ν, R) and ℓ ∈ ℕ (with: [Field(E)], [CMBase(E)], [HasQuadSubfield(d₀, E)], x ≠ 0).
>
> Assume (1): IsNeat(Fin(x), 𝔑).
>
> Then: for every M : Submonoid(RingOfIntegers(E)) (with: [ThePrime(ℓ)], [Algebra(E, Ω)]): if (for every w : FinPlace(E): if IsSafe(𝔑, w) then M ≤ primeCompl(asIdeal(w))) then (for every θ : SafePlace(𝔑) → ℕ → ℂ and J : Multiset ℤ (with: [IsLocalization(M, Subtype((x2 : E) ↦ x2 ∈ R))], [PadicIso(ℓ)]): if (for every u ∈ ℤ: if u ∈ J then 0 ≤ u and OccursInWeight(x, ν, θ, toNat(u))) then there exists ρ : PadicRep(AlgEquiv(E, Ω, Ω), ℓ) such that (Continuous(rep(ρ)) and (for every w : SafePlace(𝔑): SphericalClause(rep(ρ), OccursIn, (x2 : E →+* ℂ) ↦ ite(algebraMap(E, ℂ) = x2, J, 0), ↑↑w, heckePoly(q(↑↑w), x, (x2 : ℕ) ↦ ιℓ(θ(w, x2))))))).

It rests on:
- 2.6%: [`ellAdicCohom.woods_hole`]
- 7.6%: 1,237 small auxiliary results

**Step 8 — 7.8% of the proof** [`Data.exists_family_covolumeSq_le`]

> For every P : Parameters and D : Data(P): there exists n ∈ ℕ and y : Fin(n) → SubmoduleElem(rows(D)) such that (LinearIndependent(ℂ, y) and …). [Note: the parts shown as "…" were cut by the dump's size limit; the sentence is incomplete.]

It rests on:
- 4.2%: [`Data.seesaw`]
- 3.5%: [`Data.short_forms`]
- 0.1%: 93 small auxiliary results

## 4. Numbers

| | |
|---|---:|
| Declarations in the project | 37,770 |
| of which theorems | 30,418 |
| Used by the main theorem | 37,561 |
| Never used by the main theorem | 209 |
| Redundant theorems whose statement is identical to another theorem's | 7,901 (26.0%) |

## 5. How to check this document

1. Record: Lean's official export (`solution.ndjson.zst`), as verified by the Lean kernel.
2. Spine: the dominator tree computed from the dependencies in the record. "Exists only for that step" is exact by definition.
3. Sentences: the logical skeleton of each statement is written with fixed templates (for every, exists, if–then, and, or, not); formulas are printed from the recorded term unchanged.
4. No interpretation: the document contains no explanation, intent or judgement that is not in the record.

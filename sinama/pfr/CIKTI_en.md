# What the code proves: PFR_conjecture

*This document was not written by an AI. It was produced from the official Lean export by fixed rules (`arac/belge.py`). Anyone running the same export obtains the same document, character for character. Names in brackets are the names used in the code.*

## 1. The statement proved

The theorem proved by the code is `PFR_conjecture`. Its statement:

> For every G : Type, A : Set G and K ∈ ℝ (with: [AddCommGroup(G)], [Module(ZMod(2), G)]): if Nonempty(A) and Finite(A) and ↑ncard(A + A) ≤ K · ↑ncard(A) then there exists H : Submodule(ZMod(2), G) and c : Set G such that (Finite(c) and Finite(↑H) and ↑card(Elem(c)) < 2 · K ^ (12 : ℝ) and ncard(↑H) ≤ ncard(A) and A ≤ c + ↑H).

This sentence is written only with 2,220 concepts of the standard library (Mathlib); it contains no project-specific definition. So understanding what is proved requires reading none of the project's code.

## 2. The spine of the proof

The whole proof consists of 658 declarations. The steps below were selected from them by rule: each time, the step with the most proof beneath it was opened. The percentage is the share of the proof that exists only for that step.

| Step | Statement | Share of the proof |
|---:|---|---:|
| 1 | (long; see below) | 100.0% |
| 2 | (long; see below) | 73.6% |
| 3 | (long; see below) | 59.4% |
| 4 | (long; see below) | 56.1% |
| 5 | (long; see below) | 13.1% |
| 6 | (long; see below) | 12.2% |
| 7 | (long; see below) | 10.3% |
| 8 | (long; see below) | 9.9% |

**Step 1 — 100.0% of the proof** [`PFR_conjecture_aux`]

> Given: G : Type, A : Set G and K ∈ ℝ (with: [AddCommGroup(G)], [Countable(G)], [Module(ZMod(2), G)], [Finite(G)]).
>
> Assume (1): Nonempty(A).
>
> Assume (2): ↑ncard(A + A) ≤ K · ↑ncard(A).
>
> Then: there exists H : Submodule(ZMod(2), G) and c : Set G such that (↑card(Elem(c)) ≤ K ^ (13 / 2) · ↑ncard(A) ^ (1 / 2) · ↑ncard(↑H) ^ (−1 / 2) and ↑ncard(↑H) ≤ K ^ (11 : ℝ) · ↑ncard(A) and ↑ncard(A) ≤ K ^ (11 : ℝ) · ↑ncard(↑H) and A ≤ c + ↑H).

It is reached through these names; at least 97% of the proof of each lies under the next: `PFR_conjecture`.

It rests on:
- 73.6%: [`entropic_PFR_conjecture`] → Step 2
- 4.4%: [`ProbabilityTheory.Kernel.chain_rule`]
- 3.0%: [`ProbabilityTheory.measureMutualInfo_nonneg_aux`]
- 13.4%: 115 small auxiliary results

**Step 2 — 73.6% of the proof** [`entropic_PFR_conjecture`]

> Given: Ω₀₁ : Type, Ω₀₂ : Type, G : Type and p : refPackage(Ω₀₁, Ω₀₂, G) (with: [MeasureSpace(Ω₀₁)], [MeasureSpace(Ω₀₂)], [IsProbabilityMeasure(volume)], [IsProbabilityMeasure(volume)], [AddCommGroup(G)], [Module(ZMod(2), G)], [Finite(G)], [MeasurableSpace(G)], [MeasurableSingletonClass(G)]).
>
> Assume (1): η(p) = 1 / 9.
>
> Then: there exists H : Submodule(ZMod(2), G), Ω : Type, mΩ : MeasureSpace(Ω) and U : Ω → G such that (IsProbabilityMeasure(volume) and Measurable(U) and IsUniform(↑H, U, volume) and rdist(X₀₁(p), U, volume, volume) + rdist(X₀₂(p), U, volume, volume) ≤ 11 · rdist(X₀₁(p), X₀₂(p), volume, volume) and rdist(X₀₁(p), U, volume, volume) ≤ 6 · rdist(X₀₁(p), X₀₂(p), volume, volume) and rdist(X₀₂(p), U, volume, volume) ≤ 6 · rdist(X₀₁(p), X₀₂(p), volume, volume)).

It rests on:
- 59.4%: [`tau_strictly_decreases`] → Step 3
- 2.5%: [`exists_isUniform_of_rdist_eq_zero`]
- 2.5%: [`ProbabilityTheory.independent_copies3_nondep_finiteRange`]
- 7.7%: 29 small auxiliary results

**Step 3 — 59.4% of the proof** [`tau_strictly_decreases`]

> Given: Ω₀₁ : Type, Ω₀₂ : Type, Ω : Type, G : Type, p : refPackage(Ω₀₁, Ω₀₂, G), X₁ : Ω → G and X₂ : Ω → G (with: [MeasureSpace(Ω₀₁)], [MeasureSpace(Ω₀₂)], [MeasureSpace(Ω)], [IsProbabilityMeasure(volume)], [IsProbabilityMeasure(volume)], [IsProbabilityMeasure(volume)], [AddCommGroup(G)], [Module(ZMod(2), G)], [Finite(G)], [MeasurableSpace(G)], [MeasurableSingletonClass(G)]).
>
> Assume (1): Measurable(X₁).
>
> Assume (2): Measurable(X₂).
>
> Assume (3): TauMinimizes(p, X₁, X₂).
>
> Assume (4): η(p) = 1 / 9.
>
> Then: rdist(X₁, X₂, volume, volume) = 0.

It rests on:
- 56.1%: [`tau_strictly_decreases_aux`] → Step 4
- 3.1%: 3 small auxiliary results

**Step 4 — 56.1% of the proof** [`tau_strictly_decreases_aux`]

> Given: G : Type, Ω₀₁ : Type, Ω₀₂ : Type, p : refPackage(Ω₀₁, Ω₀₂, G), Ω : Type, X₁ : Ω → G, X₂ : Ω → G, X₁' : Ω → G and X₂' : Ω → G (with: [AddCommGroup(G)], [Finite(G)], [MeasurableSpace(G)], [MeasurableSingletonClass(G)], [MeasureSpace(Ω₀₁)], [MeasureSpace(Ω₀₂)], [IsProbabilityMeasure(volume)], [IsProbabilityMeasure(volume)], [MeasureSpace(Ω)]).
>
> Assume (1): Measurable(X₁).
>
> Assume (2): Measurable(X₂).
>
> Assume (3): Measurable(X₁').
>
> Assume (4): Measurable(X₂').
>
> Assume (5): IdentDistrib(X₁, X₁', volume, volume).
>
> Assume (6): IdentDistrib(X₂, X₂', volume, volume).
>
> Assume (7): iIndepFun(vecCons(X₁, vecCons(X₂, vecCons(X₁', vecCons(X₂', vecEmpty)))), volume).
>
> Assume (8): TauMinimizes(p, X₁, X₂).
>
> Then: for every  (with: [IsProbabilityMeasure(volume)], [Module(ZMod(2), G)]): if η(p) = 1 / 9 then rdist(X₁, X₂, volume, volume) = 0.

It rests on:
- 13.1%: [`cond_construct_good`] → Step 5
- 10.3%: [`sum_dist_diff_le`] → Step 7
- 7.7%: [`sum_condMutual_le`]
- 3.4%: [`comparison_of_ruzsa_distances`]
- 3.3%: [`sum_of_rdist_eq_char_2`]
- 3.2%: [`condRuzsaDist_le'`]
- 2.1%: [`condRuzsaDistance_ge_of_min`]
- 11.2%: 50 small auxiliary results

**Step 5 — 13.1% of the proof** [`cond_construct_good`]

> Given: G : Type, Ω₀₁ : Type, Ω₀₂ : Type, p : refPackage(Ω₀₁, Ω₀₂, G), Ω : Type, X₁ : Ω → G and X₂ : Ω → G (with: [AddCommGroup(G)], [Finite(G)], [MeasurableSpace(G)], [MeasurableSingletonClass(G)], [MeasureSpace(Ω₀₁)], [MeasureSpace(Ω₀₂)], [IsProbabilityMeasure(volume)], [IsProbabilityMeasure(volume)], [MeasureSpace(Ω)]).
>
> Assume (1): TauMinimizes(p, X₁, X₂).
>
> Then: for every Ω' : Type, T₁ : Ω' → G, T₂ : Ω' → G and T₃ : Ω' → G (with: [MeasureSpace(Ω')]): if T₁ + T₂ + T₃ = 0 and Measurable(T₁) and Measurable(T₂) and Measurable(T₃) then (for every R : Ω' → G (with: [IsProbabilityMeasure(volume)], [Module(ZMod(2), G)]): if Measurable(R) then rdist(X₁, X₂, volume, volume) ≤ condMutualInfo(T₁, T₂, R, volume) + condMutualInfo(T₂, T₃, R, volume) + condMutualInfo(T₃, T₁, R, volume) + η(p) / 3 · (condMutualInfo(T₁, T₂, R, volume) + condMutualInfo(T₂, T₃, R, volume) + condMutualInfo(T₃, T₁, R, volume) + (condRuzsaDist'(X₀₁(p), T₁, R, volume, volume) − rdist(X₀₁(p), X₁, volume, volume) + (condRuzsaDist'(X₀₂(p), T₁, R, volume, volume) − rdist(X₀₂(p), X₂, volume, volume))) + (condRuzsaDist'(X₀₁(p), T₂, R, volume, volume) − rdist(X₀₁(p), X₁, volume, volume) + (condRuzsaDist'(X₀₂(p), T₂, R, volume, volume) − rdist(X₀₂(p), X₂, volume, volume))) + (condRuzsaDist'(X₀₁(p), T₃, R, volume, volume) − rdist(X₀₁(p), X₁, volume, volume) + (condRuzsaDist'(X₀₂(p), T₃, R, volume, volume) − rdist(X₀₂(p), X₂, volume, volume))))).

It rests on:
- 12.2%: [`construct_good'`] → Step 6
- 0.5%: 4 small auxiliary results

**Step 6 — 12.2% of the proof** [`construct_good`]

> Given: G : Type, Ω₀₁ : Type, Ω₀₂ : Type, p : refPackage(Ω₀₁, Ω₀₂, G), Ω : Type, X₁ : Ω → G and X₂ : Ω → G (with: [AddCommGroup(G)], [Finite(G)], [MeasurableSpace(G)], [MeasurableSingletonClass(G)], [MeasureSpace(Ω₀₁)], [MeasureSpace(Ω₀₂)], [IsProbabilityMeasure(volume)], [IsProbabilityMeasure(volume)], [MeasureSpace(Ω)]).
>
> Assume (1): TauMinimizes(p, X₁, X₂).
>
> Then: for every Ω' : Type, T₁ : Ω' → G, T₂ : Ω' → G and T₃ : Ω' → G (with: [MeasureSpace(Ω')]): if T₁ + T₂ + T₃ = 0 and Measurable(T₁) and Measurable(T₂) and Measurable(T₃) then (for every  (with: [IsProbabilityMeasure(volume)], [Module(ZMod(2), G)]): rdist(X₁, X₂, volume, volume) ≤ mutualInfo(T₁, T₂, volume) + mutualInfo(T₂, T₃, volume) + mutualInfo(T₃, T₁, volume) + η(p) / 3 · (mutualInfo(T₁, T₂, volume) + mutualInfo(T₂, T₃, volume) + mutualInfo(T₃, T₁, volume) + (rdist(X₀₁(p), T₁, volume, volume) − rdist(X₀₁(p), X₁, volume, volume) + (rdist(X₀₂(p), T₁, volume, volume) − rdist(X₀₂(p), X₂, volume, volume))) + (rdist(X₀₁(p), T₂, volume, volume) − rdist(X₀₁(p), X₁, volume, volume) + (rdist(X₀₂(p), T₂, volume, volume) − rdist(X₀₂(p), X₂, volume, volume))) + (rdist(X₀₁(p), T₃, volume, volume) − rdist(X₀₁(p), X₁, volume, volume) + (rdist(X₀₂(p), T₃, volume, volume) − rdist(X₀₂(p), X₂, volume, volume))))).

It is reached through these names; at least 97% of the proof of each lies under the next: `construct_good'`.

It rests on:
- 9.9%: [`construct_good_prelim`] → Step 8
- 0.1%: 3 small auxiliary results

**Step 7 — 10.3% of the proof** [`sum_dist_diff_le`]

> Given: G : Type, Ω₀₁ : Type, Ω₀₂ : Type, p : refPackage(Ω₀₁, Ω₀₂, G), Ω : Type, X₁ : Ω → G, X₂ : Ω → G, X₁' : Ω → G and X₂' : Ω → G (with: [AddCommGroup(G)], [Finite(G)], [MeasurableSpace(G)], [MeasurableSingletonClass(G)], [MeasureSpace(Ω₀₁)], [MeasureSpace(Ω₀₂)], [IsProbabilityMeasure(volume)], [IsProbabilityMeasure(volume)], [MeasureSpace(Ω)]).
>
> Assume (1): Measurable(X₁).
>
> Assume (2): Measurable(X₂).
>
> Assume (3): Measurable(X₁').
>
> Assume (4): Measurable(X₂').
>
> Assume (5): IdentDistrib(X₁, X₁', volume, volume).
>
> Assume (6): IdentDistrib(X₂, X₂', volume, volume).
>
> Assume (7): iIndepFun(vecCons(X₁, vecCons(X₂, vecCons(X₁', vecCons(X₂', vecEmpty)))), volume).
>
> Assume (8): TauMinimizes(p, X₁, X₂).
>
> Then: for every  (with: [IsProbabilityMeasure(volume)], [Module(ZMod(2), G)]): condRuzsaDist'(X₀₁(p), X₁ + X₂, X₁ + X₂ + X₁' + X₂', volume, volume) − rdist(X₀₁(p), X₁, volume, volume) + (condRuzsaDist'(X₀₂(p), X₁ + X₂, X₁ + X₂ + X₁' + X₂', volume, volume) − rdist(X₀₂(p), X₂, volume, volume)) + (condRuzsaDist'(X₀₁(p), X₁' + X₂, X₁ + X₂ + X₁' + X₂', volume, volume) − rdist(X₀₁(p), X₁, volume, volume) + (condRuzsaDist'(X₀₂(p), X₁' + X₂, X₁ + X₂ + X₁' + X₂', volume, volume) − rdist(X₀₂(p), X₂, volume, volume))) + (condRuzsaDist'(X₀₁(p), X₁' + X₁, X₁ + X₂ + X₁' + X₂', volume, volume) − rdist(X₀₁(p), X₁, volume, volume) + (condRuzsaDist'(X₀₂(p), X₁' + X₁, X₁ + X₂ + X₁' + X₂', volume, volume) − rdist(X₀₂(p), X₂, volume, volume))) ≤ (6 − 3 · η(p)) · rdist(X₁, X₂, volume, volume) + 3 · (2 · η(p) · rdist(X₁, X₂, volume, volume) − condMutualInfo(X₁ + X₂, X₁' + X₂, X₁ + X₂ + X₁' + X₂', volume)).

It rests on:
- 2.5%: [`independenceCondition1`]
- 2.3%: [`condRuzsaDist'_of_inj_map'`]
- 2.1%: 11 small auxiliary results

**Step 8 — 9.9% of the proof** [`construct_good_prelim`]

> Given: G : Type, Ω₀₁ : Type, Ω₀₂ : Type, p : refPackage(Ω₀₁, Ω₀₂, G), Ω : Type, X₁ : Ω → G and X₂ : Ω → G (with: [AddCommGroup(G)], [Finite(G)], [MeasurableSpace(G)], [MeasurableSingletonClass(G)], [MeasureSpace(Ω₀₁)], [MeasureSpace(Ω₀₂)], [IsProbabilityMeasure(volume)], [IsProbabilityMeasure(volume)], [MeasureSpace(Ω)]).
>
> Assume (1): TauMinimizes(p, X₁, X₂).
>
> Then: for every Ω' : Type, T₁ : Ω' → G, T₂ : Ω' → G and T₃ : Ω' → G (with: [MeasureSpace(Ω')]): if T₁ + T₂ + T₃ = 0 and Measurable(T₁) and Measurable(T₂) and Measurable(T₃) then (for every  (with: [IsProbabilityMeasure(volume)], [Module(ZMod(2), G)]): rdist(X₁, X₂, volume, volume) ≤ mutualInfo(T₁, T₂, volume) + mutualInfo(T₂, T₃, volume) + mutualInfo(T₃, T₁, volume) + η(p) · (rdist(X₀₁(p), T₁, volume, volume) − rdist(X₀₁(p), X₁, volume, volume) + (rdist(X₀₂(p), T₂, volume, volume) − rdist(X₀₂(p), X₂, volume, volume))) + η(p) · (mutualInfo(T₁, T₃, volume) + mutualInfo(T₂, T₃, volume)) / 2).

It rests on:
- 7.2%: [`ent_bsg`]
- <0.1%: 2 small auxiliary results

## 4. Numbers

| | |
|---|---:|
| Declarations in the project | 662 |
| of which theorems | 582 |
| Used by the main theorem | 658 |
| Never used by the main theorem | 4 |
| Redundant theorems whose statement is identical to another theorem's | 71 (12.2%) |

## 5. How to check this document

1. Record: Lean's official export (`solution.ndjson.zst`), as verified by the Lean kernel.
2. Spine: the dominator tree computed from the dependencies in the record. "Exists only for that step" is exact by definition.
3. Sentences: the logical skeleton of each statement is written with fixed templates (for every, exists, if–then, and, or, not); formulas are printed from the recorded term unchanged.
4. No interpretation: the document contains no explanation, intent or judgement that is not in the record.

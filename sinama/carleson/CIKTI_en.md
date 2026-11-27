# What the code proves: classical_carleson

*This document was not written by an AI. It was produced from the official Lean export by fixed rules (`arac/belge.py`). Anyone running the same export obtains the same document, character for character. Names in brackets are the names used in the code.*

## 1. The statement proved

The theorem proved by the code is `classical_carleson`. Its statement:

> For every f : ℝ → ℂ: if Continuous(f) and Periodic(f, 2 · π) then Eventually((x : ℝ) ↦ Tendsto((x2 : ℕ) ↦ partialFourierSum(x2, f, x), atTop, nhds(f(x))), ae(volume)).

This sentence depends on 2 project-specific definitions and 4,969 library concepts.

## 2. The spine of the proof

The whole proof consists of 4,952 declarations. The steps below were selected from them by rule: each time, the step with the most proof beneath it was opened. The percentage is the share of the proof that exists only for that step.

| Step | Statement | Share of the proof |
|---:|---|---:|
| 1 | (long; see below) | 100.0% |
| 2 | (long; see below) | 95.3% |
| 3 | (long; see below) | 86.2% |
| 4 | (long; see below) | 68.9% |
| 5 | (long; see below) | 63.7% |
| 6 | (long; see below) | 53.7% |
| 7 | (long; see below) | 30.1% |
| 8 | (long; see below) | 26.6% |

**Step 1 — 100.0% of the proof** [`control_approximation_effect'`]

> For every δ : ℝ≥0 and ε : ℝ≥0: if 0 < δ and 0 < ε then (for every g : ℝ → ℂ: if Measurable(g) and Periodic(g, 2 · π) and (for every x ∈ ℝ: ‖g(x)‖ ≤ ↑C_control_approximation_effect'(δ, ε)) then distribution((x : ℝ) ↦ iSup((N : ℕ) ↦ enorm(partialFourierSum(N, g, x))), ofNNReal(δ), restrict(volume, Ioc(0, 2 · π))) ≤ ofNNReal(ε)).

It is reached through these names; at least 97% of the proof of each lies under the next: `classical_carleson` → `carleson_interval'` → `exceptional_set_carleson'`.

It rests on:
- 95.3%: [`distribution_carlesonOperatorReal_le'`] → Step 2
- 3.1%: 36 small auxiliary results

**Step 2 — 95.3% of the proof** [`rcarleson_general`]

> Given: q : ℝ≥0 and q' : ℝ≥0.
>
> Assume (1): q ∈ Ioc(1, 2).
>
> Assume (2): HolderConjugate(q, q').
>
> Then: for every F : Set ℝ and G : Set ℝ: if MeasurableSet(F) and MeasurableSet(G) then (for every f : ℝ → ℂ: if Measurable(f) and (for every x ∈ ℝ: ‖f(x)‖ ≤ indicator(F, 1, x)) then lintegral(restrict(volume, G), (x : ℝ) ↦ carlesonOperatorReal(K, f, x)) ≤ ofNNReal(C10_0_1(4, q)) · volume(G) ^ (↑q')⁻¹ · volume(F) ^ (↑q)⁻¹).

It is reached through these names; at least 97% of the proof of each lies under the next: `distribution_carlesonOperatorReal_le'` → `rcarleson_exceptional_set_estimate_specific''` → `rcarleson_exceptional_set_estimate_specific'` → `rcarleson_exceptional_set_estimate_specific` → `rcarleson_exceptional_set_estimate` → `rcarleson`.

It rests on:
- 86.2%: [`two_sided_metric_carleson`] → Step 3
- 4.7%: [`Hilbert_strong_2_2`]
- 3.7%: 85 small auxiliary results

**Step 3 — 86.2% of the proof** [`two_sided_metric_carleson`]

> Given: X : Type, x ∈ ℕ, q : ℝ≥0, q' : ℝ≥0, F : Set X, G : Set X and K : X → X → ℂ (with: [MetricSpace(X)], [DoublingMeasure(X, ↑defaultA(x))], [IsTwoSidedKernel(x, K)], [CompatibleFunctions(ℝ, X, defaultA(x))], [IsCancellative(X, defaultτ(x))]).
>
> Assume (1): 4 ≤ x.
>
> Assume (2): q ∈ Ioc(1, 2).
>
> Assume (3): HolderConjugate(q, q').
>
> Assume (4): MeasurableSet(F).
>
> Assume (5): MeasurableSet(G).
>
> Assume (6): for every r ∈ ℝ: if r > 0 then HasBoundedStrongType(czOperator(K, r), 2, 2, volume, volume, ofNNReal(C_Ts(x))).
>
> Then: for every f : X → ℂ: if Measurable(f) and (for every x2 : X: ‖f(x2)‖ ≤ indicator(F, 1, x2)) then lintegral(restrict(volume, G), (x2 : X) ↦ carlesonOperator(K, f, x2)) ≤ ofNNReal(C10_0_1(x, q)) · volume(G) ^ (↑q')⁻¹ · volume(F) ^ (↑q)⁻¹.

It rests on:
- 68.9%: [`metric_carleson`] → Step 4
- 8.5%: [`nontangential_from_simple`]
- 7.2%: [`hasStrongType_maximalFunction_one`]
- 1.3%: 84 small auxiliary results

**Step 4 — 68.9% of the proof** [`R_truncation'`]

> Given: X : Type, x ∈ ℕ, q : ℝ≥0, q' : ℝ≥0, F : Set X, G : Set X, K : X → X → ℂ, Q : SimpleFunc(X, Θ(X)) and f : X → ℂ (with: [MetricSpace(X)], [KernelProofData(x, K)], [IsCancellative(X, defaultτ(x))]).
>
> Assume (1): q ∈ Ioc(1, 2).
>
> Assume (2): HolderConjugate(q, q').
>
> Assume (3): MeasurableSet(F).
>
> Assume (4): MeasurableSet(G).
>
> Assume (5): Measurable(f).
>
> Assume (6): ((x2 : X) ↦ ‖f(x2)‖) ≤ indicator(F, 1).
>
> Then: for every n ∈ ℕ and R ∈ ℝ: if R = 2 ^ n and F ≤ ball(cancelPt(X), 2 · R) and G ≤ ball(cancelPt(X), R) and (for every θ : Θ(X): HasBoundedStrongType((x1 : X → ℂ) (x2 : X) ↦ linearizedNontangentialOperator(Q, θ, K, x1, x2), 2, 2, volume, volume, ofNNReal(C_Ts(x)))) then lintegral(restrict(volume, G), (x2 : X) ↦ iSup((R₁ : ℝ) ↦ iSup((h : R₁ ∈ Ioo(R⁻¹, R)) ↦ iSup((R₂ : ℝ) ↦ iSup((h2 : R₂ ∈ Ioo(R₁, R)) ↦ enorm(T_R(K, Q, R₁, R₂, R, f, x2))))))) ≤ ofNNReal(C1_0_2(x, q)) · volume(G) ^ (↑q')⁻¹ · volume(F) ^ (↑q)⁻¹.

It is reached through these names; at least 97% of the proof of each lies under the next: `metric_carleson` → `linearized_metric_carleson` → `R_truncation`.

It rests on:
- 63.7%: [`S_truncation`] → Step 5
- 2.7%: 68 small auxiliary results

**Step 5 — 63.7% of the proof** [`finitary_carleson`]

> Given: X : Type, x ∈ ℕ, q ∈ ℝ, K : X → X → ℂ, σ₁ : X → ℤ, σ₂ : X → ℤ, F : Set X and G : Set X (with: [MetricSpace(X)], [ProofData(x, q, K, σ₁, σ₂, F, G)]).
>
> Then: there exists G' : Set X such that (MeasurableSet(G') and 2 · volume(G') ≤ volume(G) and (for every f : X → ℂ: if Measurable(f) and (for every x2 : X: ‖f(x2)‖ ≤ indicator(F, 1, x2)) then lintegral(restrict(volume, G ∖ G'), (x2 : X) ↦ enorm(sum(toFinset(Icc(σ₁(x2), σ₂(x2))), (s : ℤ) ↦ integral(volume, (y : X) ↦ Ks(s, x2, y) · f(y) · exp(I · ↑(Q(x2))(y)))))) ≤ ofNNReal(C2_0_1(x, nnq(X))) · volume(G) ^ (1 − q⁻¹) · volume(F) ^ q⁻¹)).

It is reached through these names; at least 97% of the proof of each lies under the next: `S_truncation` → `linearized_truncation` → `finitary_carleson_step`.

It rests on:
- 53.7%: [`discrete_carleson`] → Step 6
- 5.4%: [`grid_existence`]
- 2.4%: [`tile_existence`]
- 1.3%: 93 small auxiliary results

**Step 6 — 53.7% of the proof** [`discrete_carleson`]

> Given: X : Type, x ∈ ℕ, q ∈ ℝ, K : X → X → ℂ, σ₁ : X → ℤ, σ₂ : X → ℤ, F : Set X and G : Set X (with: [MetricSpace(X)], [ProofData(x, q, K, σ₁, σ₂, F, G)], [TileStructure(Q, defaultD(x), defaultκ(x), defaultS(X), cancelPt(X))]).
>
> Then: there exists G' : Set X such that (MeasurableSet(G') and 2 · volume(G') ≤ volume(G) and (for every f : X → ℂ: if Measurable(f) and (for every x2 : X: ‖f(x2)‖ ≤ indicator(F, 1, x2)) then lintegral(restrict(volume, G ∖ G'), (x2 : X) ↦ enorm(carlesonSum(univ, f, x2))) ≤ ofNNReal(C2_0_2(x, nnq(X))) · volume(G) ^ (1 − q⁻¹) · volume(F) ^ q⁻¹)).

It rests on:
- 30.1%: [`forest_union`] → Step 7
- 12.8%: [`forest_complement`]
- 4.3%: [`exceptional_set`]
- 2.3%: [`holder_van_der_corput`]
- 4.1%: 199 small auxiliary results

**Step 7 — 30.1% of the proof** [`forest_union_aux`]

> Given: X : Type, x ∈ ℕ, q ∈ ℝ, K : X → X → ℂ, σ₁ : X → ℤ, σ₂ : X → ℤ, F : Set X, G : Set X and f : X → ℂ (with: [MetricSpace(X)], [ProofData(x, q, K, σ₁, σ₂, F, G)], [TileStructure(Q, defaultD(x), defaultκ(x), defaultS(X), cancelPt(X))]).
>
> Assume (1): for every x2 : X: ‖f(x2)‖ ≤ indicator(F, 1, x2).
>
> Assume (2): Measurable(f).
>
> Then: lintegral(restrict(volume, G ∖ G'), (x2 : X) ↦ enorm(carlesonSum(𝔓₁, f, x2))) ≤ ofNNReal(C2_0_4_base(x)) · 2 ^ (↑x + 5 / 2) · volume(G) ^ (1 − q⁻¹) · volume(F) ^ q⁻¹ · sum(Iic(maxℭ(X)), (n : ℕ) ↦ sum(Iic(n), (_k : ℕ) ↦ sum(Iic(2 · n + 3), (_j : ℕ) ↦ sum(Iio(4 · n + 12), (_l : ℕ) ↦ 2 ^ (−(q − 1) / q · ↑n))))).

It is reached through these names; at least 97% of the proof of each lies under the next: `forest_union` → `forest_union_optimized`.

It rests on:
- 26.6%: [`lintegral_carlesonSum_forest'`] → Step 8
- 2.6%: 59 small auxiliary results

**Step 8 — 26.6% of the proof** [`lintegral_carlesonSum_forest`]

> Given: X : Type, x ∈ ℕ, q ∈ ℝ, K : X → X → ℂ, σ₁ : X → ℤ, σ₂ : X → ℤ, F : Set X, G : Set X, k ∈ ℕ, n ∈ ℕ, j ∈ ℕ, l ∈ ℕ and f : X → ℂ (with: [MetricSpace(X)], [ProofData(x, q, K, σ₁, σ₂, F, G)], [TileStructure(Q, defaultD(x), defaultκ(x), defaultS(X), cancelPt(X))]).
>
> Assume (1): Measurable(f).
>
> Assume (2): for every x2 : X: ‖f(x2)‖ ≤ indicator(F, 1, x2).
>
> Then: lintegral(restrict(volume, G ∖ G'), (x2 : X) ↦ enorm(carlesonSum(iUnion((u : 𝔓(X)) ↦ iUnion((h : u ∈ 𝔘₄(k, n, j, l)) ↦ 𝔗₂(k, n, j, u))), f, x2))) ≤ ofNNReal(C2_0_4(x, q, n)) · (2 ^ (2 · x + 5) · volume(F) / volume(G)) ^ (q⁻¹ − 2⁻¹) · volume(F) ^ (1 / 2) · volume(G) ^ (1 / 2).

It is reached through these names; at least 97% of the proof of each lies under the next: `lintegral_carlesonSum_forest'`.

It rests on:
- 24.2%: [`forest_operator_le_volume`]
- 2.1%: 14 small auxiliary results

## 4. Numbers

| | |
|---|---:|
| Declarations in the project | 4,974 |
| of which theorems | 4,239 |
| Used by the main theorem | 4,952 |
| Never used by the main theorem | 22 |
| Redundant theorems whose statement is identical to another theorem's | 1,300 (30.7%) |

## 5. How to check this document

1. Record: Lean's official export (`solution.ndjson.zst`), as verified by the Lean kernel.
2. Spine: the dominator tree computed from the dependencies in the record. "Exists only for that step" is exact by definition.
3. Sentences: the logical skeleton of each statement is written with fixed templates (for every, exists, if–then, and, or, not); formulas are printed from the recorded term unchanged.
4. No interpretation: the document contains no explanation, intent or judgement that is not in the record.

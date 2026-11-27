# What the code proves: Smale

*This document was not written by an AI. It was produced from the official Lean export by fixed rules (`arac/belge.py`). Anyone running the same export obtains the same document, character for character. Names in brackets are the names used in the code.*

## 1. The statement proved

The theorem proved by the code is `Smale`. Its statement:

> There exists f : ℝ → Elem(sphere(0, 1)) → EuclideanSpace(ℝ, Fin(3)) such that (ContMDiff(prod(modelWithCornersSelf(ℝ, ℝ), modelWithCornersSelf(ℝ, EuclideanSpace(ℝ, Fin(2)))), modelWithCornersSelf(ℝ, EuclideanSpace(ℝ, Fin(3))), some(top), uncurry(f)) and f(0) = ((x : Elem(sphere(0, 1))) ↦ ↑x) and f(1) = ((x : Elem(sphere(0, 1))) ↦ −↑x) and (for every t ∈ ℝ: Immersion(modelWithCornersSelf(ℝ, EuclideanSpace(ℝ, Fin(2))), modelWithCornersSelf(ℝ, EuclideanSpace(ℝ, Fin(3))), f(t), some(top)))).

This sentence depends on 2 project-specific definitions and 4,976 library concepts.

## 2. The spine of the proof

The whole proof consists of 1,715 declarations. The steps below were selected from them by rule: each time, the step with the most proof beneath it was opened. The percentage is the share of the proof that exists only for that step.

| Step | Statement | Share of the proof |
|---:|---|---:|
| 1 | (long; see below) | 100.0% |
| 2 | (long; see below) | 79.7% |
| 3 | (long; see below) | 64.9% |
| 4 | (long; see below) | 52.2% |
| 5 | (long; see below) | 29.0% |
| 6 | (long; see below) | 20.7% |
| 7 | (long; see below) | 9.9% |
| 8 | (long; see below) | 8.8% |

**Step 1 — 100.0% of the proof** [`sphere_eversion`]

> Given: E : Type (with: [NormedAddCommGroup(E)], [InnerProductSpace(ℝ, E)], finrank(ℝ, E) = 3).
>
> Then: there exists f : ℝ → Elem(sphere(0, 1)) → E such that (ContMDiff(prod(modelWithCornersSelf(ℝ, ℝ), modelWithCornersSelf(ℝ, EuclideanSpace(ℝ, Fin(2)))), modelWithCornersSelf(ℝ, E), some(top), uncurry(f)) and f(0) = ((x : Elem(sphere(0, 1))) ↦ ↑x) and f(1) = ((x : Elem(sphere(0, 1))) ↦ −↑x) and (for every t ∈ ℝ: Immersion(modelWithCornersSelf(ℝ, EuclideanSpace(ℝ, Fin(2))), modelWithCornersSelf(ℝ, E), f(t), some(top)))).

It is reached through these names; at least 97% of the proof of each lies under the next: `Smale`.

It rests on:
- 79.7%: [`immersionRel_satisfiesHPrincipleWith`] → Step 2
- 8.8%: [`formalEversion`] → Step 8
- 10.9%: 125 small auxiliary results

**Step 2 — 79.7% of the proof** [`RelMfld.Ample.satisfiesHPrincipleWith`]

> Given: EM : Type, HM : Type, IM : ModelWithCorners(ℝ, EM, HM), M : Type, EX : Type, HX : Type, IX : ModelWithCorners(ℝ, EX, HX), X : Type, R : RelMfld(IM, M, IX, X), δ : M → ℝ, EP : Type, HP : Type, IP : ModelWithCorners(ℝ, EP, HP), P : Type and C : Set (P × M) (with: [NormedAddCommGroup(EM)], [NormedSpace(ℝ, EM)], [FiniteDimensional(ℝ, EM)], [TopologicalSpace(HM)], [Boundaryless(IM)], [TopologicalSpace(M)], [ChartedSpace(HM, M)], [IsManifold(IM, some(top), M)], [T2Space(M)], [SigmaCompactSpace(M)], [NormedAddCommGroup(EX)], [NormedSpace(ℝ, EX)], [FiniteDimensional(ℝ, EX)], [TopologicalSpace(HX)], [Boundaryless(IX)], [MetricSpace(X)], [ChartedSpace(HX, X)], [IsManifold(IX, some(top), X)], [SigmaCompactSpace(X)], [NormedAddCommGroup(EP)], [NormedSpace(ℝ, EP)], [FiniteDimensional(ℝ, EP)], [TopologicalSpace(HP)], [Boundaryless(IP)], [TopologicalSpace(P)], [ChartedSpace(HP, P)], [IsManifold(IP, some(top), P)], [SigmaCompactSpace(P)], [T2Space(P)]).
>
> Assume (1): Ample(R).
>
> Assume (2): IsOpen(R).
>
> Assume (3): IsClosed(C).
>
> Assume (4): for every x : M: 0 < δ(x).
>
> Assume (5): Continuous(δ).
>
> Then: SatisfiesHPrincipleWith(IP, R, C, δ).

It is reached through these names; at least 97% of the proof of each lies under the next: `immersionRel_satisfiesHPrincipleWith`.

It rests on:
- 64.9%: [`RelMfld.Ample.satisfiesHPrinciple`] → Step 3
- 6.4%: [`RelMfld.SatisfiesHPrinciple.satisfiesHPrincipleWith`]
- 3.0%: [`RelMfld.Ample.relativize`]
- 3.3%: 21 small auxiliary results

**Step 3 — 64.9% of the proof** [`RelMfld.Ample.satisfiesHPrinciple`]

> Given: EM : Type, HM : Type, IM : ModelWithCorners(ℝ, EM, HM), M : Type, EX : Type, HX : Type, IX : ModelWithCorners(ℝ, EX, HX), X : Type, R : RelMfld(IM, M, IX, X), A : Set M and δ : M → ℝ (with: [NormedAddCommGroup(EM)], [NormedSpace(ℝ, EM)], [FiniteDimensional(ℝ, EM)], [TopologicalSpace(HM)], [Boundaryless(IM)], [TopologicalSpace(M)], [ChartedSpace(HM, M)], [IsManifold(IM, some(top), M)], [T2Space(M)], [SigmaCompactSpace(M)], [NormedAddCommGroup(EX)], [NormedSpace(ℝ, EX)], [FiniteDimensional(ℝ, EX)], [TopologicalSpace(HX)], [Boundaryless(IX)], [MetricSpace(X)], [ChartedSpace(HX, X)], [IsManifold(IX, some(top), X)], [SigmaCompactSpace(X)]).
>
> Assume (1): Ample(R).
>
> Assume (2): IsOpen(R).
>
> Assume (3): IsClosed(A).
>
> Assume (4): for every x : M: 0 < δ(x).
>
> Assume (5): Continuous(δ).
>
> Then: SatisfiesHPrinciple(R, A, δ).

It rests on:
- 52.2%: [`OpenSmoothEmbedding.improve_formalSol`] → Step 4
- 5.2%: [`exists_stability_dist`]
- 4.1%: 42 small auxiliary results

**Step 4 — 52.2% of the proof** [`OpenSmoothEmbedding.improve_formalSol`]

The statement of this step does not fit in a short sentence (1,699 characters); the full form is in the long output.

It rests on:
- 29.0%: [`RelLoc.FormalSol.improve_htpy'`] → Step 5
- 6.0%: [`OneJetBundle.embedding`]
- 15.2%: 109 small auxiliary results

**Step 5 — 29.0% of the proof** [`RelLoc.FormalSol.improve`]

> Given: E : Type, F : Type and R : RelLoc(E, F) (with: [NormedAddCommGroup(E)], [NormedSpace(ℝ, E)], [NormedAddCommGroup(F)], [NormedSpace(ℝ, F)], [FiniteDimensional(ℝ, E)], [FiniteDimensional(ℝ, F)]).
>
> Assume (1): IsOpen(R).
>
> Assume (2): IsAmple(R).
>
> Then: for every L : Landscape(E) and ε ∈ ℝ: if 0 < ε then (for every 𝓕 : FormalSol(R): if Eventually((x : E) ↦ IsHolonomicAt(𝓕, x), nhdsSet(C(L))) then there exists H : HtpyJetSec(E, F) such that (Eventually((t : ℝ) ↦ H(t) = toJetSec(𝓕), nhdsSet(Iic(0))) and Eventually((t : ℝ) ↦ H(t) = H(1), nhdsSet(Ici(1))) and Eventually((x : E) ↦ ∀ (t : ℝ), (H(t))(x) = 𝓕(x), nhdsSet(C(L))) and (for every x : E: if (it is not the case that x ∈ K₁(L)) then (for every t ∈ ℝ: (H(t))(x) = 𝓕(x))) and (for every x : E and t ∈ ℝ: ‖f(H(t), x) − f(toJetSec(𝓕), x)‖ ≤ ε) and (for every t ∈ ℝ: IsFormalSol(H(t), R)) and Eventually((x : E) ↦ JetSec.IsHolonomicAt(H(1), x), nhdsSet(K₀(L))))).

It is reached through these names; at least 97% of the proof of each lies under the next: `RelLoc.FormalSol.improve_htpy'`.

It rests on:
- 20.7%: [`exist_loops`] → Step 6
- 7.1%: 107 small auxiliary results

**Step 6 — 20.7% of the proof** [`exist_loops`]

> Given: E : Type, F : Type, g : E → F, b : E → F, Ω : Set (E × F) and K : Set E (with: [NormedAddCommGroup(E)], [NormedSpace(ℝ, E)], [NormedAddCommGroup(F)], [NormedSpace(ℝ, F)], [FiniteDimensional(ℝ, F)], [FiniteDimensional(ℝ, E)]).
>
> Assume (1): IsCompact(K).
>
> Assume (2): IsOpen(Ω).
>
> Assume (3): ContDiff(ℝ, some(top), g).
>
> Assume (4): ContDiff(ℝ, some(top), b).
>
> Assume (5): Eventually((x : E) ↦ g(x) = b(x), nhdsSet(K)).
>
> Assume (6): for every x : E: g(x) ∈ (convexHull(ℝ))(connectedComponentIn(preimage(Prod.mk(x), Ω), b(x))).
>
> Then: there exists γ : ℝ → E → Loop(F) such that NiceLoop(g, b, Ω, K, γ).

It rests on:
- 9.9%: [`exist_loops_aux2`] → Step 7
- 2.8%: [`SmoothSurroundingFamily.exists_smooth_isCenteringDensity`]
- 2.5%: [`SmoothSurroundingFamily.reparametrize_smooth`]
- 5.1%: 101 small auxiliary results

**Step 7 — 9.9% of the proof** [`exist_loops_aux2`]

> Given: E : Type, F : Type, g : E → F, b : E → F, Ω : Set (E × F) and K : Set E (with: [NormedAddCommGroup(E)], [NormedSpace(ℝ, E)], [NormedAddCommGroup(F)], [NormedSpace(ℝ, F)], [FiniteDimensional(ℝ, F)], [FiniteDimensional(ℝ, E)]).
>
> Assume (1): IsCompact(K).
>
> Assume (2): IsOpen(Ω).
>
> Assume (3): ContDiff(ℝ, some(top), g).
>
> Assume (4): ContDiff(ℝ, some(top), b).
>
> Assume (5): Eventually((x : E) ↦ g(x) = b(x), nhdsSet(K)).
>
> Assume (6): for every x : E: g(x) ∈ (convexHull(ℝ))(connectedComponentIn(preimage(Prod.mk(x), Ω), b(x))).
>
> Then: there exists γ : E → ℝ → Loop(F) such that (SurroundingFamilyIn(g, b, γ, univ, Ω) and ContDiff(ℝ, some(top), uncurry(γ)) and Eventually((x : E) ↦ ∀ (t s : ℝ), closedBall((x, b(x)), dist(Loop.toFun(γ(x, t), s), b(x))) ≤ Ω, nhdsSet(K))).

It rests on:
- 3.8%: [`exists_surrounding_loops`]
- 5.2%: 42 small auxiliary results

**Step 8 — 8.8% of the proof** [`formalEversionAux2`]

> (E : Type) [NormedAddCommGroup(E)] [InnerProductSpace(ℝ, E)] [Fact(finrank(ℝ, E) = 3)] (ω : Orientation(ℝ, E, Fin(3))) ↦ (let __src := formalEversionAux(E, ω); FamilyFormalSol.mk(__src, _proof_1(E, ω))).

It is reached through 1 intermediate names that restate the same result: `formalEversion`.

It rests on:
- 4.8%: [`formalEversionAux`]
- 2.2%: [`formalEversionAux2._proof_1`]
- 1.7%: 11 small auxiliary results

## 4. Numbers

| | |
|---|---:|
| Declarations in the project | 1,733 |
| of which theorems | 1,306 |
| Used by the main theorem | 1,715 |
| Never used by the main theorem | 18 |
| Redundant theorems whose statement is identical to another theorem's | 100 (7.7%) |

## 5. How to check this document

1. Record: Lean's official export (`solution.ndjson.zst`), as verified by the Lean kernel.
2. Spine: the dominator tree computed from the dependencies in the record. "Exists only for that step" is exact by definition.
3. Sentences: the logical skeleton of each statement is written with fixed templates (for every, exists, if–then, and, or, not); formulas are printed from the recorded term unchanged.
4. No interpretation: the document contains no explanation, intent or judgement that is not in the record.

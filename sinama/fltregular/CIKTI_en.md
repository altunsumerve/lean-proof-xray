# What the code proves: flt_regular

*This document was not written by an AI. It was produced from the official Lean export by fixed rules (`arac/belge.py`). Anyone running the same export obtains the same document, character for character. Names in brackets are the names used in the code.*

## 1. The statement proved

The theorem proved by the code is `flt_regular`. Its statement:

> For every p ∈ ℕ (with: Prime(p)): if IsRegularPrime(p) and p ≠ 2 then FermatLastTheoremFor(p).

This sentence depends on 3 project-specific definitions and 5,581 library concepts.

## 2. The spine of the proof

The whole proof consists of 425 declarations. The steps below were selected from them by rule: each time, the step with the most proof beneath it was opened. The percentage is the share of the proof that exists only for that step.

| Step | Statement | Share of the proof | Fields used most densely |
|---:|---|---:|---|
| 1 | For every p ∈ ℕ (with: Prime(p)): if IsRegularPrime(p) and p ≠ 2 then FermatLastTheoremFor(p). | 100.0% |  |
| 2 | (long; see below) | 85.0% |  |
| 3 | (long; see below) | 70.4% |  |
| 4 | (long; see below) | 59.0% |  |
| 5 | (long; see below) | 54.3% |  |
| 6 | (long; see below) | 42.4% |  |

**Step 1 — 100.0% of the proof** [`flt_regular`]

> For every p ∈ ℕ (with: Prime(p)): if IsRegularPrime(p) and p ≠ 2 then FermatLastTheoremFor(p).

It rests on:
- 85.0%: [`FltRegular.caseII`] → Step 2
- 13.3%: [`FltRegular.caseI`]
- 1.6%: 4 small auxiliary results

**Step 2 — 85.0% of the proof** [`FltRegular.not_exists_solution`]

> Given: K : Type and p ∈ ℕ (with: Prime(p), [Field(K)], [NumberField(K)], [IsCyclotomicExtension(singleton(p), ℚ, K)]).
>
> Assume (1): p ≠ 2.
>
> Then: for every  (with: [Fintype(ClassGroup(RingOfIntegers(K)))]): if Coprime(p, card(ClassGroup(RingOfIntegers(K)))) then (for every ζ : K, hζ : IsPrimitiveRoot(ζ, p) and m ∈ ℕ: if 1 ≤ m then there is no x' : RingOfIntegers(K), y' : RingOfIntegers(K), z' : RingOfIntegers(K) and ε₃ : Units(RingOfIntegers(K)) such that ((it is not the case that toInteger(hζ) − 1 ∣ y') and (it is not the case that toInteger(hζ) − 1 ∣ z') and x' ^ p + y' ^ p = ↑ε₃ · ((toInteger(hζ) − 1) ^ m · z') ^ p)).

It is reached through these names; at least 97% of the proof of each lies under the next: `FltRegular.caseII` → `FltRegular.not_exists_Int_solution'` → `FltRegular.not_exists_Int_solution` → `FltRegular.not_exists_solution'`.

It rests on:
- 70.4%: [`exists_solution'`] → Step 3
- 3.3%: [`one_le_m`]
- 8.5%: 27 small auxiliary results

**Step 3 — 70.4% of the proof** [`exists_solution'`]

> Given: K : Type and p ∈ ℕ (with: p ≠ 0, [Field(K)], [NumberField(K)]).
>
> Assume (1): p ≠ 2.
>
> Then: for every ζ : K, hζ : IsPrimitiveRoot(ζ, p), x : RingOfIntegers(K), y : RingOfIntegers(K), z : RingOfIntegers(K), ε : Units(RingOfIntegers(K)) and m ∈ ℕ: if x ^ p + y ^ p = ↑ε · ((toInteger(hζ) − 1) ^ (m + 1) · z) ^ p and (it is not the case that toInteger(hζ) − 1 ∣ y) and (it is not the case that toInteger(hζ) − 1 ∣ z) then (for every  (with: Prime(p), [IsCyclotomicExtension(singleton(p), ℚ, K)], [Fintype(ClassGroup(RingOfIntegers(K)))]): if Coprime(p, card(ClassGroup(RingOfIntegers(K)))) then there exists x' : RingOfIntegers(K), y' : RingOfIntegers(K), z' : RingOfIntegers(K) and ε₃ : Units(RingOfIntegers(K)) such that ((it is not the case that toInteger(hζ) − 1 ∣ y') and (it is not the case that toInteger(hζ) − 1 ∣ z') and x' ^ p + y' ^ p = ↑ε₃ · ((toInteger(hζ) − 1) ^ m · z') ^ p)).

It rests on:
- 59.0%: [`eq_pow_prime_of_unit_of_congruent`] → Step 4
- 9.3%: [`exists_solution`]
- 0.9%: 1 small auxiliary results

**Step 4 — 59.0% of the proof** [`eq_pow_prime_of_unit_of_congruent`]

> Given: K : Type and p ∈ ℕ (with: Prime(p), [Field(K)], [NumberField(K)]).
>
> Assume (1): p ≠ 2.
>
> Then: for every  (with: [Fintype(ClassGroup(RingOfIntegers(K)))]): if Coprime(p, card(ClassGroup(RingOfIntegers(K)))) then (for every u : Units(RingOfIntegers(K)) (with: [IsCyclotomicExtension(singleton(p), ℚ, K)]): if (there exists n ∈ ℤ such that ↑p ∣ ↑u − ↑n) then there exists v : Units(RingOfIntegers(K)) such that u = v ^ p).

It rests on:
- 54.3%: [`exists_pow_eq_of_zeta_sub_one_pow_dvd_sub_one`] → Step 5
- 2.7%: [`zeta_sub_one_pow_dvd_norm_sub_pow`]
- 0.8%: 3 small auxiliary results

**Step 5 — 54.3% of the proof** [`exists_pow_eq_of_zeta_sub_one_pow_dvd_sub_one`]

> Given: K : Type and p ∈ ℕ (with: Prime(p), [Field(K)], [NumberField(K)]).
>
> Assume (1): p ≠ 2.
>
> Then: for every  (with: [Fintype(ClassGroup(RingOfIntegers(K)))]): if Coprime(p, card(ClassGroup(RingOfIntegers(K)))) then (for every ζ : K, hζ : IsPrimitiveRoot(ζ, p) and u : Units(RingOfIntegers(K)): if (toInteger(hζ) − 1) ^ p ∣ ↑u − 1 then there exists v : K such that v ^ p = (algebraMap(RingOfIntegers(K), K))(↑u)).

It rests on:
- 42.4%: [`dvd_card_classGroup_of_unramified_isCyclic`] → Step 6
- 10.9%: [`KummersLemma.isUnramified`]

**Step 6 — 42.4% of the proof** [`exists_not_isPrincipal_and_isPrincipal_map`]

> Given: K : Type and L : Type (with: [Field(K)], [Field(L)], [NumberField(K)], [NumberField(L)], [Algebra(K, L)], [FiniteDimensional(K, L)], [IsGalois(K, L)], [Unramified(RingOfIntegers(K), RingOfIntegers(L))], [IsCyclic(AlgEquiv(K, L, L))]).
>
> Assume (1): Prime(finrank(K, L)).
>
> Assume (2): finrank(K, L) ≠ 2.
>
> Then: there exists I : Ideal (RingOfIntegers(K)) such that ((it is not the case that IsPrincipal(I)) and IsPrincipal(map(algebraMap(RingOfIntegers(K), RingOfIntegers(L)), I))).

It is reached through these names; at least 97% of the proof of each lies under the next: `dvd_card_classGroup_of_unramified_isCyclic`.

It rests on:
- 34.6%: [`Hilbert92`]
- 6.7%: [`exists_not_isPrincipal_and_isPrincipal_map_aux`]

## 4. Numbers

| | |
|---|---:|
| Declarations in the project | 426 |
| of which theorems | 361 |
| Used by the main theorem | 425 |
| Never used by the main theorem | 1 |
| Redundant theorems whose statement is identical to another theorem's | 18 (5.0%) |

## 5. How to check this document

1. Record: Lean's official export (`solution.ndjson.zst`), as verified by the Lean kernel.
2. Spine: the dominator tree computed from the dependencies in the record. "Exists only for that step" is exact by definition.
3. Sentences: the logical skeleton of each statement is written with fixed templates (for every, exists, if–then, and, or, not); formulas are printed from the recorded term unchanged.
4. No interpretation: the document contains no explanation, intent or judgement that is not in the record.

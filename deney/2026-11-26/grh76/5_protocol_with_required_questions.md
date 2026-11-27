# Story of the proof

## The idea in five sentences

1. The top level (`New.grh`, feeding `riemannHypothesis`) reduces everything to a one-sided estimate: for a suitable prime d in a fixed residue class, a weighted prime-counting error called primeError must eventually be at most x^(8ε − 1/2), and a Landau-type argument on its Laplace transform (whose poles count zeros of L-functions minus zeros of their quadratic twists by d) then forbids zeros to the right of 1/2 + 8ε.
2. For each large x the proof builds a package of auxiliary choices called Data (an integer m ≈ √x that is a power of 2, an integer r ≈ x^5 that is a power of 3, a huge scale b with log b = x^ε, two auxiliary primes between b^10 and b^11, a three-term-free set of place classes called thick), and rewrites primeError(x) as m·remainder divided by m·a·#thick, plus a term at a second scale x₁ that is made negligible by picking x₁ in a window.
3. The core, `star_inequality`, says m·remainder ≤ (log b)^2·budget, and it is proved by measuring one complex vector space of automorphic forms (called rows) in two ways: `Data.exists_family_covolumeSq_le` produces almost a full basis of forms that are integral up to a small index and whose Gram determinant is at most exp(n·(mainHeight − m·remainder + log b·budget)), while `Data.integral_forms_long` shows that any such nearly-integral nearly-full family must have log-determinant at least rowDim·(mainHeight − 3·log b·budget).
4. When the two bounds are compared the large quantity mainHeight (= m·k·dirCost) cancels exactly, and what is left is m·remainder ≤ 4·log b·budget + small terms; since budget does not grow with m, dividing by m ≈ √x is what gives the square-root saving.
5. The lower bound is a product-formula ("height") argument: the volume of rows factors into m lift volumes, one per step of an m-fold chain of lifts, and each factor is compared between the trivial twist and a family of auxiliary twists, with the p-adic denominators controlled by Galois representations attached to the forms (`sphericalCompat_of_odd`, `Model.exists_galois_rep`) through a Selmer-length/Ribet-style bound (`exists_isFitFamily`, `denominatorLe_rowBudget`, `ribet_columns`).

## For a mathematician

Order of combination, as read in the code.

(a) `New.grh`: given a zero ρ with Re ρ > 1/2, set ε = (min(Re ρ, 1) − 1/2)/51, β = 8ε + 1/2, modulus M = 18480q. A criterion (one-sided bound primeError ≤ x^(β−1) for primes d ≡ 9240q − 1 mod M, d ≡ 7 mod 8, implies non-vanishing for Re > β) is applied; its proof calls a Landau lemma and a non-vanishing statement for one quadratic twist.

(b) `eventually_primeError_le_rpow`: takes Data from `exists_data`, replaces the scale x₁ by a point u in [10^6 log x, (10^6 log x)^2] where primeError(N₀, e^u) − (towerDeg/#thick)·primeError(1, e^u) ≤ x^(−10^6), uses the identity remainder = a·(#thick·(primeError(x) − primeError(x₁)) + #tops·primeError(1, x₁)), and inserts `star_inequality`.

(c) `star_inequality`: with h = mainHeight − m·remainder + L, L = log b·budget, d = rowDim. Upper side: n ≥ (1 − 4/b²)d independent forms, index defect δ ≤ 5d·log(1+b²)·budget, Gram determinants ≤ exp(n·h). Lower side: d(mainHeight − 3L) ≤ n·h + 2δ. A crude bound −h ≤ b²x^99 pays for the d − n missing vectors. Dividing by d cancels mainHeight.

(d) Upper side: `Data.short_forms` takes Poincaré-type forms built from "ramified columns"; `Data.seesaw` identifies their image with an explicit form Bμ, whose size is bounded by a per-row height, and a Stirling computation shows that height is ≤ mainHeight − m·remainder + budget: here the sums over primes (primeSum) enter, as local sizes at primes ν ≤ a. `Data.exists_indexDvd_Bmu_divisible` gives p-adic integrality. `Data.ramifiedColumns_fill_rows` (via `Filling.Fits.exists_translate_finrank_comap_le`) shows the translates are spread, so few translates span nearly everything.

(e) Lower side, `Data.integral_forms_long`: `Data.heightLe_volume_rows` bounds the height of vol(θ)/vol(1) by n·h + 2δ + d·b using integrality (`Data.crude_rows` supplies the completing vectors); `Data.heightLe_volume_ratio_sq` bounds the height of the inverse squared by 2d(2L − mainHeight), as a product over j = 1..m of `Data.heightLe_liftVolume_ratio`, each worth d·k·(log b·B₀ − dirCost) with B₀ = budget/(mk). The product is 1, so the heights sum to ≥ 0.

(f) `exists_isFitFamily` supplies the twists: `exists_mFoldTwist_selmerLengthLe` picks them, `denominatorLe_rowBudget` → `ribet_columns` → `sum_blockLoss_le` → `block_defect_le_at_place` → `crystalline_defect_le` bound denominators by a row budget.

(g) Galois input: `sphericalCompat_of_odd` → `sphericalCompat_of_split` → `exists_rep_of_cuspidal_type` → `Model.exists_galois_rep` → `ellAdicCohom.woods_hole`; `exchange_theorem` relates theta integrals up to L-value products.

## For everyone

The proof turns a question about zeros into a question about how evenly primes are spread in certain patterns. It then builds, for each large number x, a big finite-dimensional space of highly symmetric functions. It measures the size of that space in two independent ways, once from above using explicitly constructed small functions and once from below using the fact that whole-number objects cannot be too small. The two measurements share an enormous common term that drops out, and what remains is exactly the prime-counting error, multiplied by about the square root of x. Because the leftover on the other side is small, the error must be small, which is the square-root accuracy the hypothesis demands. The lower measurement relies on deep arithmetic symmetries (Galois representations) to control denominators.

## What I could not tell

- Why the Gram determinant of rows is genuinely tied to the Chowla–Selberg-type constant and to dirCost: I read the definitions (jetSize, primeSum, mainAsk) and the Stirling step in the per-row height bound, but not the geometric source of the factorial sizes.
- What the objects rows, Column, Bμ, goodLift and the spaces Y, W concretely are (which groups, which weights); I only saw them used.
- How `Attached.local_global_of_eigencharacter` itself is used inside `star_inequality`; for `sphericalCompat_of_odd` I traced the route through the lemmas sphericalCompat_std, attached_galRep and exists_hasRow_auxPair into `denominatorLe_rowBudget` and `exists_isFitFamily`, but not what the ramified local-global statement is needed for.
- How `exchange_theorem`, `Data.exists_besselSystem`, `exists_isWeakBaseChange_of_matching` (beyond its use inside `sphericalCompat_of_odd`), `Data.exists_isTriangle` and `Data.hasGap_gridParam` enter `star_inequality`; I read only the statement of `exchange_theorem`.
- That the number f of infinite places is comparable to towerDeg, needed for my arithmetic f/#thick ≤ log b in Q4 (guess); the final inequality there is closed by an automated magnitude tactic I did not unfold.
- Why the thick set must be three-term-free, and the role of r ≈ x^5 beyond k = r + 1 − m and h₂ = r^8.
- The interior of `Model.exists_galois_rep`, `ellAdicCohom.woods_hole`, `nonempty_universalFamily`, `linearIndepOn_hodgeTateMap_pointClass`, `Filling.energy_le_of_linkEnergy_le`, `Filling.energy_le_of_level_pairs`, `Filling.sum_le_of_positive_type`, `Filling.energy_fixingSet_le`, `exists_comparison_forms` (statement only), and the mark-operator chain `Data.IsMarked.hasType_prod_markOperator_pow`, `Data.IsMarked.hasType_markOperator`, `Columns.hasType_markOperator`, `TwistingData.hasType_twisted_hecke`.
- Whether residueClass is the von Mangoldt function restricted to a class (guess from the L-series lemma names).

## Answers to the required questions

- Q1: Data is a structure of auxiliary choices for one x: reals logX, logB, logX₁ with scale conditions (10^12·c ≤ log logB, 100·log logB ≤ logX, 10^6·logX ≤ logX₁, 10^6·logX₁ ≤ logB), s ≤ 32·logX, m = 2^(e+1) in [√x, 2√x] with s = 22(e+1), r = 3^(e'+1) in [x^5, 3x^5], a finite set thick of place classes with a three-term-freeness property, two distinct primes g0, g1 in [b^10, b^11] congruent to 1 modulo N₁(s)·d, an integer piG of norm g0·g1, and a prime-in-window property. It is produced by `exists_data` (not bounded): powers of 2 and 3 near the targets; W = exp(ε·logX/6), logX₁ = W, logB = W^6; classNumber+1 primes in short logarithmic windows from a lemma on primes ≡ 1 in log-windows (proved by a contour/derivative bound on sums of logarithmic derivatives of L-functions); a pigeonhole on ideal classes makes a product of two primes principal; thick comes from a Behrend-sphere three-term-free construction.
- Q2: remainder is the sum over the places τ in tops of (primeSum(a, τ) − mainAsk), where primeSum is a sum over ν ≤ a of lambdaClass(ν)·(a/ν − nominalWeight)⁺ and mainAsk = a(log a − 1 − chowlaSelbergConst − average log nominalWeight); by an identity it equals a·(#thick·(primeError(x) − primeError(x₁)) + #tops·primeError(1, x₁)). It is bounded above by `star_inequality`; it enters through `Data.short_forms`, where the size of the form Bμ is bounded by a per-row height (sum over an m-step chain of jet sizes minus prime sums) and a Stirling step shows that height ≤ mainHeight − m·remainder + budget.
- Q3: budget = f·a·(log b)^3 (f = number of infinite places of the field E, a = roundUp(x·b)); it is an error allowance, not a quantity that is estimated. It is spent in `Data.short_forms` (sum over primes of allowedLoss·log p ≤ budget, proved by a harmonic-sum count over primes dividing N, m·c−1, c, m·c+1 for c ≤ x₁), in the index defect, and in `exists_isFitFamily`, where B₀ = budget/(m·k) must dominate the sum of rowBudget(ℓ)·log ℓ; that is fed by `denominatorLe_rowBudget` and below it `ribet_columns` (valuation of a Ribet element ≤ rank·rowBudget).
- Q4: Data is taken with D.x = x and x₁ replaced by e^u, u in [10^6·log x, (10^6·log x)^2] from a window lemma, so that primeError(N₀, x₁) − (towerDeg/#thick)·primeError(1, x₁) ≤ x^(−10^6); the remainder identity gives primeError(x) = m·remainder/(m·a·#thick) + that term, and `star_inequality` bounds the first by (log b)^2·budget/(m·a·#thick) = f·(log b)^5/(m·#thick). Chosen sizes: m ≈ √x, r ≈ x^5, log b = x^ε, a ≈ x·b, s ≤ 32·log x, #thick ≥ towerDeg(s)/log b; so the bound is about x^(5ε)·x^ε/√x (using f/#thick ≤ log b, a guess for f ≈ towerDeg), which is below x^(8ε − 1/2).
- Q5: In `star_inequality` the term mainHeight (= m·k·dirCost) appears on both sides of d·(mainHeight − 3L) ≤ d·(mainHeight − m·remainder + L + 4x^99 + 10·log(1+b²)·budget) and cancels after dividing by d = rowDim; left is m·remainder ≤ 4·log b·budget + 4x^99 + 10·log(1+b²)·budget ≤ (log b)^2·budget.
- Q6: Yes: the lift is iterated m times (indices j = 1..m, m = 2^(e+1) ≈ √x; twists are "m-fold twists" required to be nontrivial at every power j). The volume of rows is a constant times the product over j = 1..m of lift volumes, and each j contributes height rowDim·k·(log b·B₀ − dirCost), summing to rowDim·(log b·budget − mainHeight); on the upper side the same m multiplies the prime sums (per-row height = m·(…)). m ≈ √x is right because the remainder is multiplied by m while budget is not, so dividing by m yields exactly the x^(−1/2) in the statement; a smaller m gives a weaker exponent (that a larger m would break the Data constraints is a guess). Other repetitions seen: a greedy choice of at most 5·rowDim·log(1+b²)/dim Column translates, and a strong induction over prime-degree base-change steps in `Attached.local_global_of_eigencharacter`.
- Q7: Called directly in the proof of `star_inequality` (the calc step named both); it contributes the lower bound rowDim·(mainHeight − 3·log b·budget) ≤ n·h + 2δ for the log-determinant of any nearly-integral family.
- Q8: Called by the lemma sphericalCompat_std (all ranks: theta-lift to odd rank, twist, cancel characters). That lemma is called in three places I read: in the lemma attached_galRep (which defines the Galois representation of an eigen-system and is invoked inside `denominatorLe_rowBudget`), in the lemma exists_hasRow_auxPair (invoked inside `exists_isFitFamily` to produce the rows whose Selmer length is bounded), and in `Attached.local_global_of_eigencharacter`. It contributes to `star_inequality` the existence of a Galois representation attached to each eigenform, with the Hecke polynomial killing Frobenius, which is what the denominator bound for the lift volumes (lower side) is run on.
- Q9: Called in the first line of `star_inequality`; it contributes the family y: n ≥ (1 − 4/b²)·rowDim independent forms, index defect δ ≤ 5·rowDim·log(1+b²)·budget, and Gram determinants ≤ exp(n·(mainHeight − m·remainder + log b·budget)).
- Q10: Called in `Data.enough_forms` (through `exists_few_translates`), which is used by `Data.exists_family_covolumeSq_le`; it contributes spreadness with parameter b^(−2), hence a small set t of translates whose images span at least (1 − 4/b²)·rowDim, which makes the family nearly full and keeps δ small.

## Claims

- STEP `riemannHypothesis`
- STEP `New.grh`
- STEP `eventually_primeError_le_rpow`
- STEP `star_inequality`
- STEP `Data.integral_forms_long`
- STEP `Data.exists_family_covolumeSq_le`
- STEP `exists_isFitFamily`
- STEP `Data.seesaw`
- UNDER `riemannHypothesis` `New.grh`
- UNDER `New.grh` `eventually_primeError_le_rpow`
- UNDER `eventually_primeError_le_rpow` `star_inequality`
- UNDER `star_inequality` `Data.integral_forms_long`
- UNDER `star_inequality` `sphericalCompat_of_odd`
- UNDER `star_inequality` `Data.exists_family_covolumeSq_le`
- UNDER `star_inequality` `Data.ramifiedColumns_fill_rows`
- UNDER `star_inequality` `exchange_theorem`
- UNDER `Data.integral_forms_long` `exists_isFitFamily`
- UNDER `Data.integral_forms_long` `Data.heightLe_volume_ratio_sq`
- UNDER `Data.integral_forms_long` `Data.heightLe_volume_rows`
- UNDER `Data.heightLe_volume_ratio_sq` `Data.heightLe_liftVolume_ratio`
- UNDER `Data.heightLe_volume_rows` `Data.crude_rows`
- UNDER `exists_isFitFamily` `denominatorLe_rowBudget`
- UNDER `exists_isFitFamily` `exists_mFoldTwist_selmerLengthLe`
- UNDER `denominatorLe_rowBudget` `ribet_columns`
- UNDER `ribet_columns` `sum_blockLoss_le`
- UNDER `Data.exists_family_covolumeSq_le` `Data.seesaw`
- UNDER `Data.exists_family_covolumeSq_le` `Data.short_forms`
- UNDER `Data.short_forms` `Data.exists_indexDvd_Bmu_divisible`
- UNDER `sphericalCompat_of_odd` `sphericalCompat_of_split`
- UNDER `sphericalCompat_of_split` `exists_rep_of_cuspidal_type`
- UNDER `exists_rep_of_cuspidal_type` `Model.exists_galois_rep`
- UNDER `Model.exists_galois_rep` `ellAdicCohom.woods_hole`
- UNDER `Data.ramifiedColumns_fill_rows` `Filling.Fits.exists_translate_finrank_comap_le`
- SHARE `star_inequality` 93.4
- SHARE `Data.integral_forms_long` 20.2
- SHARE `sphericalCompat_of_odd` 19.1
- SHARE `exists_rep_of_cuspidal_type` 18.2
- SHARE `exists_isFitFamily` 11.5
- SHARE `Model.exists_galois_rep` 10.4
- SHARE `Data.exists_family_covolumeSq_le` 7.8
- SHARE `denominatorLe_rowBudget` 7.0
- SHARE `Data.ramifiedColumns_fill_rows` 5.4
- SHARE `exchange_theorem` 3.8

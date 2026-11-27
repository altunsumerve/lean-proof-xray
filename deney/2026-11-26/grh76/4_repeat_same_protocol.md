# Story of the proof

## The idea in five sentences

1. The Riemann hypothesis is obtained as the modulus-one case of a stronger statement, `New.grh`, that no Dirichlet L-function vanishes to the right of the half line, and that statement is reduced by `entireL_ne_zero_of_primeError_le` to a one-sided upper bound: a "prime error", which compares a weighted count of prime powers in the residue class 1 (weight one minus a quadratic character attached to an auxiliary prime d) with its expected size, must eventually be at most a power of x with exponent just above minus one half.
2. That reduction works because the transform of the prime error has "poles" counting zeros of the L-functions minus zeros of their quadratic twists by d (`isPolar_primeError`), a Landau-type positivity lemma turns a one-sided bound into absence of such poles, and d can be chosen so that the twisted function does not vanish at the given point.
3. The bound on the prime error is `eventually_primeError_le_rpow`: for each large x a package of auxiliary data is built (`exists_data`), the prime error at x is rewritten exactly as a quantity called the remainder plus a term at a second, freely chosen, much smaller point which a window lemma makes negligible, and the remainder is bounded by the single inequality `star_inequality`.
4. `star_inequality` is a squeeze on one determinant: `Data.exists_family_covolumeSq_le` produces almost a full basis of a space of automorphic forms (the "rows") whose Gram determinant, in every complex conjugate, is at most the exponential of (main height minus remainder plus small) per vector, with a controlled loss of p-adic integrality, while `Data.integral_forms_long` shows that any such nearly integral family must have log-determinant at least about the main height per vector; the main heights cancel and the remainder is left bounded by the small terms.
5. The lower bound is a product-formula argument: for every prime a twisted copy of the embedding of the rows is chosen (`exists_isFitFamily`), two "height" bounds on ratios of volumes between the twisted and untwisted copies (`Data.heightLe_volume_rows` and `Data.heightLe_volume_ratio_sq`) multiply to the constant one, and a nonzero algebraic number cannot be small at all places at once, so the sum of the two bounds is nonnegative.

## For a mathematician

Top level. `riemannHypothesis` applies a short lemma (functional equation, modulus 1) to `New.grh`. There, for a zero ρ with real part above one half, the character is lifted to modulus 18480q, ε is (min(Re ρ,1) − 1/2)/51, and `entireL_ne_zero_of_primeError_le` is applied with β = 8ε + 1/2 and primes d ≡ 7 mod 8 in a fixed class. The prime error is defined as a difference of two averaged sums of a class function (indicator of 1 mod M times 1 − χ_K), minus log x/φ(M), minus a constant.

Middle. In `eventually_primeError_le_rpow` the code substitutes x = exp(·), takes data D from `exists_data` (log of the second point equals x^(ε/6), log log b = ε log x), then replaces the second point by one supplied by a window lemma for two "polar" functions, where primeError(N₀) minus a multiple of primeError(1) is at most exp(−10⁶ log x). An exact identity expresses the remainder (a sum over "tops" of prime sums minus a main ask) through prime errors at the two points. Then `star_inequality` is used: m·remainder ≤ logB²·budget.

The squeeze. Short side, `Data.exists_family_covolumeSq_le`: `Data.short_forms` takes rational multiples of projected Poincaré series applied to integral "ramified columns"; `Data.seesaw` identifies their image with an explicit object whose size is bounded, giving the per-vector exponent mainHeight − m·remainder + logB·budget; `Data.exists_indexDvd_Bmu_divisible` controls integrality. `Data.enough_forms` uses `Data.ramifiedColumns_fill_rows` (a spreading property, resting on `Filling.Fits.exists_translate_finrank_comap_le`) and a greedy choice of few translates to span a (1 − 4/b²) fraction of the rows.

Long side, `Data.integral_forms_long`: `Data.heightLe_volume_rows` (via `Data.crude_rows`, a spanning set of integral forms of crude size, and a one-determinant lemma) bounds the height of the volume ratio twisted/untwisted by V + 2δ + small. `Data.heightLe_volume_ratio_sq` bounds the inverse ratio squared by 2·rowDim·(2 logB·budget − mainHeight): the volume factors (`Data.volume_iota_eq_prod_liftVolume`) into m lift volumes, each handled by `Data.heightLe_liftVolume_ratio` using `exists_comparison_forms` and the denominator bounds in the fit family. Those come from `denominatorLe_rowBudget`, which uses Galois representations of eigenforms, Selmer-length bounds (`exists_mFoldTwist_selmerLengthLe`) and `ribet_columns`.

Galois side. `sphericalCompat_of_odd` (attached ℓ-adic representations in odd rank over CM fields, Frobenius killed by the Hecke polynomial) reduces by quadratic base change (`exists_isWeakBaseChange_of_matching`) to `sphericalCompat_of_split`, then `exists_rep_of_cuspidal_type`, then `Model.exists_galois_rep`, built from cohomology of a model, with `ellAdicCohom.woods_hole` beneath it.

## For everyone

The proof does not study the zeta function directly; it shows that a certain count of prime numbers can never overshoot its expected value by much, and a classical argument turns that one-sided statement into the Riemann hypothesis. To control the count, the proof builds, for every large size, a big table of numbers coming from highly symmetric functions, and looks at one number computed from the table, its volume. On one hand the table can be filled with entries that are visibly small, and how small depends on the prime count. On the other hand the entries are almost whole numbers in a hidden sense, and a nonzero whole number cannot be small in every possible way of measuring it, so the volume cannot be too small. Comparing the two estimates leaves exactly the wanted bound on the prime count. Most of the length of the proof is spent on proving the "almost whole number" property, which needs deep machinery linking these functions to symmetries of number systems.

## What I could not tell

- Where exactly `sphericalCompat_of_odd` is called. The map says it exists only for `star_inequality`, but it is not named in that lemma's code; I saw a Galois representation of an isotypic piece used inside `denominatorLe_rowBudget`, and I think (guess) it also enters the short side. I did not trace the callers.
- What `exchange_theorem` is used for. Its statement equates a theta integral with a constant times an integral of a paired theta function, the constant having absolute value squared equal to a product of L-values; `Data.crude_rows` lives in a folder with the same name, so I think (guess) it feeds the crude spanning set.
- Why the main height (m times k times a "direct cost" built from jet sizes and prime sums) appears on both sides with the same coefficient; I read the definitions but not the computations that produce it.
- What the spaces actually are (which group, which forms); words like unitary group or theta lift would be guesses. I only saw a CM field, a quadratic subfield, odd rank, Poincaré series and "Weyl" indices.
- How `ribet_columns`, `sum_blockLoss_le`, `block_defect_le_at_place` and `crystalline_defect_le` produce the denominator bound; I read only the statement of the first.
- The inside of `Model.exists_galois_rep`, `nonempty_universalFamily`, and of the filling argument (`Filling.energy_le_of_linkEnergy_le`, `Filling.energy_le_of_level_pairs`).
- Whether the class function carries the von Mangoldt weight; the name suggests it (guess), I did not open the definition of the residue class sum.
- The role of `Data.exists_besselSystem` and of the 37% of the proof under `star_inequality` that sits in small auxiliary results.

## Claims

- STEP `riemannHypothesis`
- STEP `New.grh`
- STEP `eventually_primeError_le_rpow`
- STEP `star_inequality`
- STEP `Data.integral_forms_long`
- STEP `Data.exists_family_covolumeSq_le`
- STEP `sphericalCompat_of_odd`
- STEP `exists_isFitFamily`
- STEP `Model.exists_galois_rep`
- UNDER `riemannHypothesis` `New.grh`
- UNDER `New.grh` `eventually_primeError_le_rpow`
- UNDER `eventually_primeError_le_rpow` `star_inequality`
- UNDER `star_inequality` `Data.integral_forms_long`
- UNDER `star_inequality` `Data.exists_family_covolumeSq_le`
- UNDER `star_inequality` `sphericalCompat_of_odd`
- UNDER `star_inequality` `Data.ramifiedColumns_fill_rows`
- UNDER `star_inequality` `exchange_theorem`
- UNDER `Data.integral_forms_long` `exists_isFitFamily`
- UNDER `Data.integral_forms_long` `Data.heightLe_volume_ratio_sq`
- UNDER `Data.integral_forms_long` `Data.heightLe_volume_rows`
- UNDER `Data.exists_family_covolumeSq_le` `Data.seesaw`
- UNDER `Data.exists_family_covolumeSq_le` `Data.short_forms`
- UNDER `exists_isFitFamily` `denominatorLe_rowBudget`
- UNDER `denominatorLe_rowBudget` `ribet_columns`
- UNDER `sphericalCompat_of_odd` `sphericalCompat_of_split`
- UNDER `sphericalCompat_of_split` `exists_rep_of_cuspidal_type`
- UNDER `exists_rep_of_cuspidal_type` `Model.exists_galois_rep`
- UNDER `Model.exists_galois_rep` `ellAdicCohom.woods_hole`
- SHARE `star_inequality` 93.4
- SHARE `eventually_primeError_le_rpow` 99.7
- SHARE `Data.integral_forms_long` 20.2
- SHARE `sphericalCompat_of_odd` 19.1
- SHARE `exists_isFitFamily` 11.5
- SHARE `Model.exists_galois_rep` 10.4
- SHARE `Data.exists_family_covolumeSq_le` 7.8
- SHARE `Data.ramifiedColumns_fill_rows` 5.4
- SHARE `exchange_theorem` 3.8

Lookups: 4 calls of harita.py, 5 calls of kaynak.py.

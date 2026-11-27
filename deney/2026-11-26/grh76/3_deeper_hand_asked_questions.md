# Story of the proof (map + junction code)

## The idea in five sentences

1. The Riemann hypothesis is reduced to a one-sided bound: if a sum over prime powers n ≡ 1 mod M, weighted by 1 − χ_d(n) (so only primes not split for the quadratic character of d count), exceeds its main term by at most x^(β−1), then a Landau positivity lemma forbids zeros of every L-function mod M beyond β, because those zeros are positive residues of the sum's Laplace transform and only the zeros of the twists by d are negative.
2. The prime sum is manufactured as divisibility: Poincaré series are pushed through a chain of m theta lifts whose kernels are Taylor jets of order about a of theta series, and the resulting forms are divisible at each nonsplit prime p by p to the power gain(p), where gain is m times a sum of terms a/p^e minus a weight, and the sum of these gains times log p is exactly m times the prime sum (primeSum_eq_sum_localAsk).
3. After rescaling by one rational number that removes those prime powers, the forms are integral and short, with log-size at most a factorial term minus the prime sum, which the code rewrites as mainHeight − m·remainder + budget; a few translates of them span almost all of the space rows, giving an upper bound for a covolume.
4. The same covolume is bounded below by arithmetic: the volume of the m-fold lift factors into m lift volumes, each compared with its twist by an auxiliary character is a ratio of L-values whose height is at most −k·dirCost plus error, and since a nonzero algebraic number satisfies the product formula (the height of 1 is nonnegative) this yields a lower bound mainHeight = m·k·dirCost, the value the prime sum would have at nominal weights.
5. mainHeight is common to both sides and cancels, leaving m·remainder ≤ logB²·budget with a budget that does not grow with m, and since the remainder is a·#thick·primeError(x) plus controlled terms, dividing by m near √x gives primeError ≤ x^(8ε − 1/2).

## For a mathematician

`riemannHypothesis` comes from `New.grh` (nonvanishing of Dirichlet L-functions right of 1/2), which feeds `eventually_primeError_le_rpow` into a Landau criterion: the Laplace transform of primeError has residue (ord L(ξ) − ord L(ξ·χ_d)) summed over ξ, and d is chosen so the twist does not vanish.

`eventually_primeError_le_rpow` builds Data (logX, logX₁, logB, m = 2^(e+1) in [√x, 2√x], r a power of 3, k = r + 1 − m, a three-term-free set thick of classes) and uses remainder_eq: remainder = a·(#thick·(primeError(x) − primeError(x₁)) + #tops·primeError_1(x₁)). Then `star_inequality` gives m·remainder ≤ logB²·budget with budget = f·a·logB³, so primeError(x) ≲ f·logB⁵/(m·#thick).

`star_inequality` combines two bounds on Gram determinants in rows.

Upper: `Data.exists_family_covolumeSq_le`. `Data.seesaw` identifies the m-fold lift of a Poincaré series with Bμ, a combination of chained theta kernels (liftKernel is thetaKernel, built from jetSeries). `Data.weylNormSq_Bmu_le` bounds its archimedean size by heightPerRow plus twice the gains; `Data.exists_indexDvd_Bmu_divisible` gives divisibility by p^gain(p) on a sublattice of small index (allowedLoss); `Data.heightPerRow_le` uses Stirling to get heightPerRow ≤ mainHeight − m·remainder + budget. `Data.short_forms` scales by a rational q with prescribed p-adic valuations. `Data.enough_forms` adds the count, using `Data.ramifiedColumns_fill_rows`.

Lower: `Data.integral_forms_long`. With θ from `exists_isFitFamily`, `Data.heightLe_volume_rows` bounds the height of 𝔷(θ)/𝔷(1) by the family's covolume, and `Data.heightLe_volume_ratio_sq` bounds 𝔷(1)²/𝔷(θ)² by 2·rowDim·(2L − mainHeight); the product is 1. The second uses the factorisation of 𝔷 into m lift volumes and `Data.heightLe_liftVolume_ratio`, whose bound rowDim·k·(logB·B₀ − dirCost) comes from ratios of L-value products: at each prime the p-adic size is at least p^(−forcedPart), and forcedPart summed against log p gives dirCost. Summing m lifts gives mainHeight = m·k·dirCost.

So each lift contributes one copy of both the main term and the prime sum, while errors stay within budget; m copies amplify the remainder m-fold.

The p-adic denominators need `denominatorLe_rowBudget` and `ribet_columns`, which need Galois representations: `exists_isFitFamily` calls `exists_hasRow_auxPair`, which calls sphericalCompat_std, which theta-lifts to odd rank and invokes `sphericalCompat_of_odd` (via `sphericalCompat_of_split`, `exists_rep_of_cuspidal_type`, `Model.exists_galois_rep`). `Data.exists_besselSystem` is consumed in the lemma filling_fits, which defines the Poincaré map and its unfolding.

## For everyone

The proof turns a question about prime numbers into a question about the size of a box built from very symmetric functions. These functions are constructed in a long chain of steps, and at every step each relevant prime leaves a fingerprint: the function becomes divisible by a power of that prime. Dividing those powers out makes the functions small, and how small is governed exactly by the prime count one wants to control. On the other hand the box they span cannot be too small, because its volume is a nonzero number of an arithmetic kind, and such numbers cannot be tiny in every sense at once. Comparing the two estimates, the expected part cancels and only the deviation of the prime count survives, multiplied by the number of steps in the chain. Because the chain can be made as long as the square root of the range, the deviation is forced to be of square-root size, which is what the hypothesis asserts.

## What I could not tell

- Where `exchange_theorem` is consumed: I opened about ten candidates (seesaw unfolding, crude rows, lift volumes, L-value ratios) and none names it; that it underlies the period/route identities of the grid forms is a (guess).
- Why the jets of theta kernels are p-divisible at nonsplit primes (inside le_jetExponent, collisionSum and `Data.IsMarked.hasType_markOperator`, not opened); I only saw the exponents.
- Why dirCost uses the weights w = b₁ or b₂ + j·h + h₂, and why k = r + 1 − m with r a power of 3 near x⁵.
- How `exists_mFoldTwist_selmerLengthLe` chooses the twists, and what `ribet_columns` does internally.
- The role of the three-term-free set, the auxiliary primes g and the prime N in the level.
- What `Data.exists_besselSystem` provides analytically beyond being a hypothesis of the Poincaré construction.
- That χ_d is the character of an imaginary quadratic field is inferred from names (guess).

## Claims

- STEP `riemannHypothesis`
- STEP `New.grh`
- STEP `eventually_primeError_le_rpow`
- STEP `star_inequality`
- STEP `Data.integral_forms_long`
- STEP `Data.exists_family_covolumeSq_le`
- STEP `Data.short_forms`
- STEP `Data.seesaw`
- STEP `Data.exists_indexDvd_Bmu_divisible`
- STEP `Data.heightLe_liftVolume_ratio`
- STEP `sphericalCompat_of_odd`
- UNDER `eventually_primeError_le_rpow` `star_inequality`
- UNDER `star_inequality` `Data.integral_forms_long`
- UNDER `star_inequality` `Data.exists_family_covolumeSq_le`
- UNDER `star_inequality` `sphericalCompat_of_odd`
- UNDER `star_inequality` `exchange_theorem`
- UNDER `star_inequality` `Data.exists_besselSystem`
- UNDER `star_inequality` `Data.ramifiedColumns_fill_rows`
- UNDER `Data.exists_family_covolumeSq_le` `Data.short_forms`
- UNDER `Data.exists_family_covolumeSq_le` `Data.seesaw`
- UNDER `Data.short_forms` `Data.exists_indexDvd_Bmu_divisible`
- UNDER `Data.integral_forms_long` `exists_isFitFamily`
- UNDER `Data.integral_forms_long` `Data.heightLe_volume_rows`
- UNDER `Data.integral_forms_long` `Data.heightLe_volume_ratio_sq`
- UNDER `Data.heightLe_volume_ratio_sq` `Data.heightLe_liftVolume_ratio`
- UNDER `exists_isFitFamily` `denominatorLe_rowBudget`
- UNDER `exists_isFitFamily` `exists_mFoldTwist_selmerLengthLe`
- UNDER `denominatorLe_rowBudget` `ribet_columns`
- UNDER `sphericalCompat_of_odd` `sphericalCompat_of_split`
- UNDER `sphericalCompat_of_split` `exists_rep_of_cuspidal_type`
- UNDER `exists_rep_of_cuspidal_type` `Model.exists_galois_rep`
- SHARE `star_inequality` 93.4
- SHARE `Data.integral_forms_long` 20.2
- SHARE `sphericalCompat_of_odd` 19.1
- SHARE `Data.exists_family_covolumeSq_le` 7.8
- SHARE `Data.short_forms` 3.5
- SHARE `Data.seesaw` 4.2
- SHARE `Data.heightLe_liftVolume_ratio` 4.7

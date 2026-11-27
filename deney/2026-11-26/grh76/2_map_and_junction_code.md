# Story of the proof (map + junction code)

## For a mathematician

`riemannHypothesis` follows from `New.grh`: no Dirichlet L-function vanishes right of the line 1/2. For a supposed zero ρ, `New.grh` lifts the character to level 18480q and applies a one-sided criterion: for primes d in one residue class, primeError(d, M, x) is a von Mangoldt sum over n ≡ 1 mod M weighted by 1 − χ_d(n). Its Laplace transform has residues equal to zero orders of L(ξ) minus those of the quadratic twists; a Landau-type positivity lemma turns an upper bound x^(β−1) on one side only into absence of zeros beyond β, after choosing d whose twist does not vanish.

That bound is `eventually_primeError_le_rpow`. For large x it builds a Data package (scales logX, logX₁, logB; m a power of 2 near √x; two auxiliary primes; a three-term-free set of classes), rewrites the remainder as a combination of primeError at x and x₁, and reduces to `star_inequality`: m·remainder ≤ logB²·budget.

`star_inequality` is a covolume squeeze on a space of automorphic forms (rows). Upper side, `Data.exists_family_covolumeSq_le`: an independent family of n ≥ (1 − 4/b²)·rowDim forms whose Gram determinant under every field automorphism is at most exp(n·(mainHeight − m·remainder + L)), with small index loss against integral forms at every prime. It combines `Data.short_forms` (rescaled projected Poincaré series, via `Data.seesaw`) with `Data.enough_forms` (few translates almost fill rows, via `Data.ramifiedColumns_fill_rows`). Lower side, `Data.integral_forms_long`: rowDim·(mainHeight − 3L) ≤ V + 2δ. Here `exists_isFitFamily` supplies a family of twists θ; `Data.heightLe_volume_rows` bounds the height of 𝔷(θ)/𝔷(1) by the family's covolume, `Data.heightLe_volume_ratio_sq` bounds the height of the inverse ratio squared by −mainHeight plus error; their product is 1, whose height is nonnegative. Subtracting, mainHeight cancels and the remainder is bounded; the d − n missing vectors cost only a crude bound.

The volume ratio factors into m lift volumes (`Data.heightLe_liftVolume_ratio`), whose p-adic denominators are controlled by `denominatorLe_rowBudget` and `ribet_columns`, using Galois representations attached to eigenforms (`sphericalCompat_of_odd`, from `sphericalCompat_of_split`, `exists_rep_of_cuspidal_type`, `Model.exists_galois_rep`).

## For everyone

The proof shows that a certain count of prime numbers, compared between two kinds of primes, can never be too large in one direction. A classical argument then says that such a one-sided bound already forbids the forbidden zeros. To get the bound, the proof builds a large collection of highly symmetric functions and measures the volume of the box they span in two ways. One measurement says the box is small, because short functions can be written down explicitly. The other says it cannot be too small, because the functions have whole-number structure and a nonzero whole number cannot be tiny. The prime count is exactly the gap between the two measurements, so it is trapped.

## What I could not tell

- Where `exchange_theorem` and `Data.exists_besselSystem` enter: the map says they exist only for `star_inequality`, but its code does not name them; they are reached through helpers I did not open.
- Where exactly `sphericalCompat_of_odd` is consumed; that it feeds the denominator bounds is my reading of names such as GalRep in `ribet_columns` (guess).
- What mainHeight means geometrically (it is m·k·dirCost; I did not open jetSize or nominalWeight), and why the Poincaré series norm produces the prime sum (inside `Data.seesaw` and weylNormSq_Bmu_le, not read).
- The content of `Model.exists_galois_rep` and `ellAdicCohom.woods_hole` beyond their statements; "Shimura variety cohomology with a fixed point formula" would be a (guess).
- What IsFitFamily's Selmer-length condition is really doing, and the role of the three-term-free set and the two primes g in Data.
- That χ_d is the quadratic character of Q(√−d) is inferred from the name chiK_eq_legendreSym (guess).
- How the window lemma chooses x₁ so that the x₁ terms are negligible.

## Claims

- STEP `riemannHypothesis`
- STEP `New.grh`
- STEP `eventually_primeError_le_rpow`
- STEP `star_inequality`
- STEP `Data.integral_forms_long`
- STEP `Data.exists_family_covolumeSq_le`
- STEP `sphericalCompat_of_odd`
- UNDER `riemannHypothesis` `New.grh`
- UNDER `New.grh` `eventually_primeError_le_rpow`
- UNDER `eventually_primeError_le_rpow` `star_inequality`
- UNDER `star_inequality` `Data.integral_forms_long`
- UNDER `star_inequality` `Data.exists_family_covolumeSq_le`
- UNDER `star_inequality` `sphericalCompat_of_odd`
- UNDER `star_inequality` `exchange_theorem`
- UNDER `star_inequality` `Data.ramifiedColumns_fill_rows`
- UNDER `Data.integral_forms_long` `exists_isFitFamily`
- UNDER `Data.integral_forms_long` `Data.heightLe_volume_rows`
- UNDER `Data.integral_forms_long` `Data.heightLe_volume_ratio_sq`
- UNDER `Data.exists_family_covolumeSq_le` `Data.short_forms`
- UNDER `Data.exists_family_covolumeSq_le` `Data.seesaw`
- UNDER `exists_isFitFamily` `denominatorLe_rowBudget`
- UNDER `denominatorLe_rowBudget` `ribet_columns`
- UNDER `sphericalCompat_of_split` `exists_rep_of_cuspidal_type`
- UNDER `exists_rep_of_cuspidal_type` `Model.exists_galois_rep`
- SHARE `star_inequality` 93.4
- SHARE `Data.integral_forms_long` 20.2
- SHARE `sphericalCompat_of_odd` 19.1
- SHARE `exists_isFitFamily` 11.5
- SHARE `Data.exists_family_covolumeSq_le` 7.8
- SHARE `Model.exists_galois_rep` 10.4

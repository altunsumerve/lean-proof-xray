# Story of the proof (from the map only)
## For a mathematician
`riemannHypothesis` (Mathlib's RiemannHypothesis) is a corollary of `New.grh`, whose statement the map shows only as the opaque name DirichletLNonvanishingRightOfHalf. `New.grh` has two sides.

Analytic side (under 1%): `isPolar_primeError` ties a prime-counting error `primeError(d, M, x)`, for primes d ≡ 7 mod 8, to zero orders of Dirichlet L-functions minus those of their quadratic twists by d. `entireL_ne_zero_of_primeError_le` (using `IsPolar.landau` and `exists_entireL_quadTwist_ne_zero`, itself from `zero_density_quadTwist`) turns a bound primeError ≤ x^(β−1) into non-vanishing right of β.

Arithmetic side: `eventually_primeError_le_rpow` gives exponent 8ε − 1/2. `exists_data` builds a Data package for each large x; `Data.remainder_eq` writes its "remainder" through primeError; `star_inequality` (93.4%) bounds m·remainder by logB²·budget. Under `star_inequality`, the apparent shape (guess) is a two-sided comparison of heights/covolumes of a lattice of integral automorphic forms ("rows") over a CM field:
- `Data.exists_family_covolumeSq_le`: a large linearly independent family with bounded covolume, from `Data.seesaw` and `Data.short_forms`.
- `Data.integral_forms_long`: the opposing bound, from `exists_isFitFamily` (twist families; `denominatorLe_rowBudget`, `ribet_columns`, `sum_blockLoss_le`, `block_defect_le_at_place`, `crystalline_defect_le`, plus `exists_mFoldTwist_selmerLengthLe`), `Data.heightLe_volume_ratio_sq` (through `Data.heightLe_liftVolume_ratio`, `exists_comparison_forms`) and `Data.heightLe_volume_rows` (`Data.crude_rows`).
- `sphericalCompat_of_odd` → `sphericalCompat_of_split` → `exists_rep_of_cuspidal_type`: ℓ-adic Galois representations matching Hecke polynomials, via `Model.exists_galois_rep` (with `ellAdicCohom.woods_hole`, `ellAdicCohom.isCrystalline_and_linearFrob_rel`), `nonempty_universalFamily`, `exists_model`.
- `Data.ramifiedColumns_fill_rows` (through `Filling.Fits.exists_translate_finrank_comap_le`), `exchange_theorem`, `exists_isWeakBaseChange_of_matching` (`twisted_trace_identity`), `Orbital.harish_chandra_degree_and_orbital`, `Data.exists_besselSystem`.

Named classical inputs visible: `CMLattice.chowla_selberg`, `IsHeckeOfType.exists_hasPrimeDensity`.
## For everyone
The computer-checked theorem is the Riemann Hypothesis, obtained here from a broader statement about a whole family of related functions. The proof first shows that the hypothesis would follow if a certain count of prime numbers stays very close to its predicted value. Almost all of the work then goes into one inequality that forces this closeness. That inequality seems to come from measuring the same arithmetic object in two different ways and comparing the answers. To do the measuring, the proof builds very heavy machinery linking symmetric functions to symmetries of number systems. The map shows where the weight of the proof lies, but not why the central inequality is true.
## What I could not tell
- What the types Parameters and Data contain: both open only as bare types; the following concept names (not steps, so written without backticks) remainder, budget, logB, mainHeight, rows, covolumeSq, IndexLe, HeightLe, IsSpread, SphericalCompat, primeError and DirichletLNonvanishingRightOfHalf could not be opened at all.
- How `star_inequality` actually combines its parts: 37.1% of the proof sits in 6,907 small results directly under it, and the "upper bound versus lower bound of a lattice volume" reading is my guess from names and from `Data.heightLe_volume_ratio_sq`.
- The conclusions of `Data.integral_forms_long`, `Data.exists_family_covolumeSq_le`, `Data.short_forms`, `Data.seesaw`, `Data.ramifiedColumns_fill_rows`, `ellAdicCohom.woods_hole`, `crystalline_defect_le` are cut off ("…") in the map.
- Which groups the automorphic forms live on (the Space with signs suggests unitary groups; guess), and why odd rank matters in `sphericalCompat_of_odd`.
- The role of `Data.ramifiedColumns_fill_rows` and the whole Filling branch ("energy" bounds), of `Data.exists_besselSystem`, `Data.exists_isTriangle`, `Data.hasGap_gridParam`.
- How `exchange_theorem` (theta-type lifts between spaces of different signature, guess) enters the inequality.
- How the step from `star_inequality` to the exponent 8ε − 1/2 is done, and where the quadratic field of the prime d ≡ 7 mod 8 enters (only `CMLattice.chowla_selberg` hints at it).
- Whether "Ribet" and "Woods Hole" in names mean the classical arguments of those names; I only see the names.
## Claims
- STEP `riemannHypothesis`
- STEP `New.grh`
- UNDER `riemannHypothesis` `New.grh`
- UNDER `New.grh` `eventually_primeError_le_rpow`
- UNDER `New.grh` `entireL_ne_zero_of_primeError_le`
- UNDER `New.grh` `isPolar_primeError`
- UNDER `entireL_ne_zero_of_primeError_le` `IsPolar.landau`
- UNDER `entireL_ne_zero_of_primeError_le` `exists_entireL_quadTwist_ne_zero`
- UNDER `exists_entireL_quadTwist_ne_zero` `zero_density_quadTwist`
- SHARE `eventually_primeError_le_rpow` 99.7
- UNDER `eventually_primeError_le_rpow` `star_inequality`
- UNDER `eventually_primeError_le_rpow` `exists_data`
- UNDER `eventually_primeError_le_rpow` `Data.remainder_eq`
- UNDER `eventually_primeError_le_rpow` `CMLattice.chowla_selberg`
- UNDER `eventually_primeError_le_rpow` `IsHeckeOfType.exists_hasPrimeDensity`
- SHARE `star_inequality` 93.4
- UNDER `star_inequality` `Data.integral_forms_long`
- SHARE `Data.integral_forms_long` 20.2
- UNDER `star_inequality` `Data.exists_family_covolumeSq_le`
- SHARE `Data.exists_family_covolumeSq_le` 7.8
- UNDER `Data.exists_family_covolumeSq_le` `Data.seesaw`
- UNDER `Data.exists_family_covolumeSq_le` `Data.short_forms`
- UNDER `Data.integral_forms_long` `exists_isFitFamily`
- SHARE `exists_isFitFamily` 11.5
- UNDER `exists_isFitFamily` `denominatorLe_rowBudget`
- UNDER `denominatorLe_rowBudget` `ribet_columns`
- UNDER `ribet_columns` `sum_blockLoss_le`
- UNDER `sum_blockLoss_le` `block_defect_le_at_place`
- UNDER `block_defect_le_at_place` `crystalline_defect_le`
- UNDER `exists_isFitFamily` `exists_mFoldTwist_selmerLengthLe`
- UNDER `Data.integral_forms_long` `Data.heightLe_volume_ratio_sq`
- UNDER `Data.heightLe_volume_ratio_sq` `Data.heightLe_liftVolume_ratio`
- UNDER `Data.heightLe_liftVolume_ratio` `exists_comparison_forms`
- UNDER `Data.integral_forms_long` `Data.heightLe_volume_rows`
- UNDER `Data.heightLe_volume_rows` `Data.crude_rows`
- UNDER `star_inequality` `sphericalCompat_of_odd`
- SHARE `sphericalCompat_of_odd` 19.1
- UNDER `sphericalCompat_of_odd` `sphericalCompat_of_split`
- UNDER `sphericalCompat_of_split` `exists_rep_of_cuspidal_type`
- SHARE `exists_rep_of_cuspidal_type` 18.2
- UNDER `exists_rep_of_cuspidal_type` `Model.exists_galois_rep`
- SHARE `Model.exists_galois_rep` 10.4
- UNDER `Model.exists_galois_rep` `ellAdicCohom.woods_hole`
- UNDER `Model.exists_galois_rep` `ellAdicCohom.isCrystalline_and_linearFrob_rel`
- UNDER `exists_rep_of_cuspidal_type` `nonempty_universalFamily`
- UNDER `exists_rep_of_cuspidal_type` `exists_model`
- UNDER `star_inequality` `Data.ramifiedColumns_fill_rows`
- UNDER `Data.ramifiedColumns_fill_rows` `Filling.Fits.exists_translate_finrank_comap_le`
- UNDER `star_inequality` `exchange_theorem`
- SHARE `exchange_theorem` 3.8
- UNDER `star_inequality` `exists_isWeakBaseChange_of_matching`
- UNDER `exists_isWeakBaseChange_of_matching` `twisted_trace_identity`
- UNDER `star_inequality` `Orbital.harish_chandra_degree_and_orbital`
- UNDER `star_inequality` `Data.exists_besselSystem`
- UNDER `star_inequality` `Data.exists_isTriangle`
- UNDER `star_inequality` `Data.hasGap_gridParam`

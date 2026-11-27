# Story of the proof (from the map only)
## For a mathematician
`classical_carleson`: for continuous 2π-periodic f, `partialFourierSum` converges to f almost everywhere. Via `carleson_interval'` this reduces to `exceptional_set_carleson'` (the set where the tail error exceeds δ has measure ≤ ε). There f is approximated by a smooth periodic function (`close_smooth_approx_periodic`, handled by `fourierConv_ofTwiceDifferentiable`), and the small remainder by `control_approximation_effect'`: `partialFourierSum_bound` dominates partial sums by a maximally modulated truncated singular integral `carlesonOperatorReal`, whose level sets are controlled by `distribution_carlesonOperatorReal_le'`, i.e. the restricted-type bound `rcarleson_general`.

That is the case X = ℝ of `two_sided_metric_carleson`, a theorem on doubling metric measure spaces; the instance needs `Hilbert_strong_2_2`, `isTwoSidedKernelHilbert`, `real_van_der_Corput`. The abstract theorem turns L² bounds for truncations `czOperator` into a nontangential maximal bound (`nontangential_from_simple`, through `cotlar_estimate` and `czOperator_weak_1_1`), uses `hasStrongType_maximalFunction_one` (by `MeasureTheory.exists_hasStrongType_real_interpolation`), and calls `metric_carleson`.

`metric_carleson` linearises the supremum (`linearized_metric_carleson`), truncates scales (`R_truncation`, `R_truncation'`, `S_truncation`, `linearized_truncation`), and iterates `finitary_carleson_step`/`finitary_carleson`: a bound outside a set G' of at most half the measure of G. `finitary_carleson` builds dyadic grids and tiles (`grid_existence`, `tile_existence`) and invokes `discrete_carleson`, a bound for a sum over tiles, `carlesonSum`.

`discrete_carleson` combines `exceptional_set` (G' is small; `third_exception`, `john_nirenberg`), `forest_union`, `forest_complement`, and the oscillatory estimate `holder_van_der_corput`. `forest_complement` (really `forest_complement_optimized`) splits remaining tiles into antichains and applies `antichain_operator` (`dens1_antichain`, `dens2_antichain`). `forest_union` (via `forest_union_aux`, a sum over indices n, k, j, l with geometric decay in n) sums over `forest` families using `lintegral_carlesonSum_forest` and `forest_operator`, which merges `TileStructure.Forest.forest_operator_f`, `TileStructure.Forest.forest_operator_g` and the single-tree `TileStructure.Forest.tree_projection_estimate`; the g-part (`TileStructure.Forest.forest_operator_g_main`, an L² bound for adjoint sums) rests on `TileStructure.Forest.row_correlation` and `TileStructure.Forest.correlation_separated_trees`, i.e. `TileStructure.Forest.correlation_separated_trees_of_subset`: near-orthogonality of distinct trees.
## For everyone
Any continuous repeating signal can be rebuilt by adding up pure waves, and this proof shows that the rebuilding really converges to the signal at almost every point. The proof first replaces the signal by a very smooth one, for which convergence is easy, and then shows the leftover error can only be large on a tiny set. That second part is the hard one, and it is proved in a much more general setting than waves on a line, then specialised. In the general setting, the problem is cut into many small pieces, each localised both in position and in frequency. These pieces are sorted into organised groups called trees and forests, plus scattered leftovers, and each kind is bounded separately. Roughly a quarter of the whole proof is spent on the forests alone.
## What I could not tell
- The content of the constants (C10_0_1, C2_0_4, C_Ts, ...; not openable as steps) and of the parameter x (fixed to 4 on the real line); the map shows only their names.
- What the sets `𝔓₁`, `ℭ(k, n)`, `𝔘₄`, `𝔗₂`, `𝔏₀'`..`𝔏₃`, `G'`, `G₃` precisely are: I saw them only inside statements, not how tiles are sorted into them or why the sorting works.
- What exactly the structures ProofData, KernelProofData, TileStructure, Forest, IsCancellative, CompatibleFunctions require: the lookup opens them only as bare type declarations without fields (these names are not among the map's heaviest steps). "Trees" and "rows" are my reading of names like `rowDecomp`, `adjointCarlesonRowSum`.
- How `holder_van_der_corput` is used inside `discrete_carleson` (it has two direct users; I guess the antichain and tree-correlation estimates, but that is a guess).
- How the halving step `finitary_carleson_step` is iterated in `linearized_truncation` (I infer a geometric series from `slice_integral_bound_sum`, `volume_slice_le_inv_two_pow_mul` and `sum_le_four_div_q_sub_one`; guess).
- How `Hilbert_strong_2_2` is actually proved (chain under `eLpNorm_czOperator` with a convolution inequality `young_convolution` and `dist_dirichletApprox_le`; mechanism unclear).
- The inside of the heaviest leaves (`TileStructure.Forest.correlation_distant_tree_parts`, `dens1_antichain_sq`, `dach_bound`, `cotlar_set_F₂`): only statements, no argument.
- Whether the 8.5% + 7.2% for nontangential/maximal results reflects difficulty or just formal overhead; share is not importance.
## Claims
- STEP `classical_carleson`
- STEP `partialFourierSum`
- STEP `close_smooth_approx_periodic`
- STEP `carlesonOperatorReal`
- STEP `carlesonSum`
- STEP `czOperator`
- UNDER `classical_carleson` `carleson_interval'`
- UNDER `carleson_interval'` `exceptional_set_carleson'`
- UNDER `exceptional_set_carleson'` `fourierConv_ofTwiceDifferentiable`
- UNDER `exceptional_set_carleson'` `control_approximation_effect'`
- UNDER `control_approximation_effect'` `partialFourierSum_bound`
- UNDER `control_approximation_effect'` `distribution_carlesonOperatorReal_le'`
- UNDER `distribution_carlesonOperatorReal_le'` `rcarleson_general`
- UNDER `rcarleson_general` `two_sided_metric_carleson`
- UNDER `rcarleson_general` `Hilbert_strong_2_2`
- UNDER `rcarleson_general` `isTwoSidedKernelHilbert`
- UNDER `rcarleson_general` `real_van_der_Corput`
- UNDER `two_sided_metric_carleson` `nontangential_from_simple`
- UNDER `nontangential_from_simple` `cotlar_estimate`
- UNDER `cotlar_estimate` `czOperator_weak_1_1`
- UNDER `two_sided_metric_carleson` `hasStrongType_maximalFunction_one`
- UNDER `hasStrongType_maximalFunction_one` `MeasureTheory.exists_hasStrongType_real_interpolation`
- UNDER `two_sided_metric_carleson` `metric_carleson`
- UNDER `metric_carleson` `linearized_metric_carleson`
- UNDER `linearized_metric_carleson` `R_truncation`
- UNDER `R_truncation` `S_truncation`
- UNDER `S_truncation` `linearized_truncation`
- UNDER `linearized_truncation` `finitary_carleson_step`
- UNDER `finitary_carleson_step` `finitary_carleson`
- UNDER `finitary_carleson` `grid_existence`
- UNDER `finitary_carleson` `tile_existence`
- UNDER `finitary_carleson` `discrete_carleson`
- UNDER `discrete_carleson` `exceptional_set`
- UNDER `exceptional_set` `third_exception`
- UNDER `exceptional_set` `john_nirenberg`
- UNDER `discrete_carleson` `holder_van_der_corput`
- UNDER `discrete_carleson` `forest_complement`
- UNDER `forest_complement` `antichain_operator`
- UNDER `antichain_operator` `dens1_antichain`
- UNDER `antichain_operator` `dens2_antichain`
- UNDER `discrete_carleson` `forest_union`
- UNDER `forest_union` `lintegral_carlesonSum_forest`
- UNDER `lintegral_carlesonSum_forest` `forest`
- UNDER `lintegral_carlesonSum_forest` `forest_operator`
- UNDER `forest_operator` `TileStructure.Forest.forest_operator_f`
- UNDER `forest_operator` `TileStructure.Forest.forest_operator_g`
- UNDER `forest_operator` `TileStructure.Forest.tree_projection_estimate`
- UNDER `TileStructure.Forest.forest_operator_g` `TileStructure.Forest.row_correlation`
- UNDER `TileStructure.Forest.row_correlation` `TileStructure.Forest.correlation_separated_trees`
- UNDER `R_truncation` `R_truncation'`
- UNDER `R_truncation'` `S_truncation`
- UNDER `forest_complement` `forest_complement_optimized`
- UNDER `forest_complement_optimized` `antichain_operator`
- UNDER `forest_union` `forest_union_aux`
- UNDER `forest_union_aux` `lintegral_carlesonSum_forest`
- UNDER `TileStructure.Forest.forest_operator_g` `TileStructure.Forest.forest_operator_g_main`
- UNDER `TileStructure.Forest.forest_operator_g_main` `TileStructure.Forest.row_correlation`
- UNDER `TileStructure.Forest.correlation_separated_trees` `TileStructure.Forest.correlation_separated_trees_of_subset`
- UNDER `TileStructure.Forest.correlation_separated_trees_of_subset` `TileStructure.Forest.correlation_distant_tree_parts`
- UNDER `linearized_truncation` `slice_integral_bound_sum`
- UNDER `linearized_truncation` `volume_slice_le_inv_two_pow_mul`
- UNDER `linearized_truncation` `sum_le_four_div_q_sub_one`
- UNDER `Hilbert_strong_2_2` `eLpNorm_czOperator`
- UNDER `eLpNorm_czOperator` `young_convolution`
- UNDER `eLpNorm_czOperator` `dist_dirichletApprox_le`
- UNDER `antichain_operator` `dens1_antichain_sq`
- UNDER `dens1_antichain_sq` `dach_bound`
- UNDER `cotlar_estimate` `cotlar_set_F₂`
- SHARE `R_truncation'` 66.5
- SHARE `forest_union_aux` 29.3
- SHARE `forest_complement_optimized` 12.7
- SHARE `TileStructure.Forest.forest_operator_g_main` 12.7
- SHARE `TileStructure.Forest.correlation_separated_trees_of_subset` 11.4
- SHARE `control_approximation_effect'` 98.5
- SHARE `rcarleson_general` 94.5
- SHARE `two_sided_metric_carleson` 86.2
- SHARE `metric_carleson` 68.9
- SHARE `finitary_carleson` 62.8
- SHARE `discrete_carleson` 53.7
- SHARE `forest_union` 30.1
- SHARE `forest_operator` 24.1
- SHARE `forest_complement` 12.8
- SHARE `TileStructure.Forest.forest_operator_g` 12.9
- SHARE `nontangential_from_simple` 8.5
- SHARE `hasStrongType_maximalFunction_one` 7.2
- SHARE `Hilbert_strong_2_2` 4.7
- SHARE `exceptional_set` 4.3

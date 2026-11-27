# Story of the proof (from the map only)
## For a mathematician
`PFR_conjecture`: in a vector space over the two-element field, a finite nonempty set A with |A+A| ≤ K|A| is covered by fewer than 2K^12 translates of a subspace H with |H| ≤ |A|. It follows, with only bookkeeping, from `PFR_conjecture_aux` (finite G; weaker cover bound, |H| within K^11 of |A|).

The approach is entropic. Sets are replaced by random variables and doubling by the entropy "distance" `rdist` (entropy of the difference of independent copies minus half the two entropies). `PFR_conjecture_aux` takes a uniform variable on A, bounds its self-distance by log K (`rdist_le_of_isUniform_of_card_sub_le`), applies `entropic_PFR_conjecture`, and returns to sets via `diff_ent_le_rdist`, `ProbabilityTheory.prob_ge_exp_neg_entropy'` and `ProbabilityTheory.IsUniform.measureReal_preimage_sub` (the exact covering argument: guess).

`entropic_PFR_conjecture`: for reference variables X₀₁, X₀₂ there is a uniform variable U on a subspace with distances to both at most 6, in sum 11, times their distance. The method is variational: `tau` adds to `rdist` the distances to the references weighted by η = 1/9; `tau_minimizer_exists` gives a minimiser (continuity, `continuous_tau_restrict_probabilityMeasure`); `tau_strictly_decreases` shows a minimiser has distance zero; `exists_isUniform_of_rdist_eq_zero` turns that into a uniform variable on a subgroup (via `symmGroup`); `rdist_triangle` presumably gives the constants.

The core, `tau_strictly_decreases_aux`, takes four independent variables X₁, X₂, X₁', X₂'. The identity `sum_of_rdist_eq_char_2` (from `sum_of_rdist_eq`) splits distances into a distance of sums, a conditional distance and a conditional mutual information. `first_estimate`, `second_estimate`, `I₃_eq` give `sum_condMutual_le`: the three pairwise sums are nearly independent given the total. `sum_dist_diff_le` controls their distances to the references. `cond_construct_good`, through `construct_good'`, `construct_good`, `construct_good_prelim`, says any T₁+T₂+T₃=0 bounds the minimiser's distance by their mutual informations; it rests on `ent_bsg` and minimality (`condRuzsaDistance_ge_of_min`). Supporting inequalities: `comparison_of_ruzsa_distances` (from `kaimanovich_vershik'`), `condRuzsaDist_le'`, `condRuzsaDist_of_indep`, `ent_ofsum_le`. Entropy foundations: `ProbabilityTheory.Kernel.chain_rule`, `ProbabilityTheory.measureMutualInfo_nonneg_aux`, `ProbabilityTheory.condIndep_copies'`.
## For everyone
The theorem says that if a finite collection of on/off patterns barely grows when you combine its members pairwise, then it nearly is a perfectly structured family, up to a modest number of shifted copies. The proof swaps collections for random choices and measures how far two random choices are from behaving like one structured family, using the amount of surprise (entropy) in their combination. Among all pairs of random choices it picks the pair that is best by a carefully weighted score. It then shows that if this best pair were not already perfectly structured, mixing four independent copies of it would produce a strictly better pair, which is impossible. So the best pair is perfectly structured, meaning uniformly spread over a structured family. Finally this statement about randomness is translated back into the statement about collections.
## What I could not tell
- How exactly `PFR_conjecture_aux` gets from the uniform variable on H to the covering set c: no step named for covering appears in the map; the three lemmas I cite are my reading of its direct children (guess).
- How the constants 11 and 6 in `entropic_PFR_conjecture`, and the exponents 13/2, 11 and 12, are derived; I only see the statements.
- How the final contradiction in `tau_strictly_decreases_aux` is assembled from `cond_construct_good`, `sum_condMutual_le` and `sum_dist_diff_le`; I infer the order from the shapes of the formulas (they share the same three sums and the same bracketed term), not from the proof.
- The contents of `refPackage` beyond X₀₁, X₀₂ and η; the map shows it only as an opaque type.
- What `_private.PFR.EntropyPFR.0.tau_strictly_decreases.match_1_1` (1.9%) is; and the role of 47 small children of `tau_strictly_decreases_aux` and 108 of `PFR_conjecture_aux` that I did not open.
- Why `ProbabilityTheory.Kernel.chain_rule` and `ProbabilityTheory.measureMutualInfo_nonneg_aux` sit directly under `PFR_conjecture_aux` rather than deeper: presumably they are used on both sides, but the map does not say where.
- How `ent_bsg` is used inside `construct_good_prelim` (which variables play A and B), and what the role of `condRuzsaDist'_of_inj_map'` and `independenceCondition1` is beyond technical reindexing.
- Where the characteristic-2 hypothesis is essential, apart from `sum_of_rdist_eq_char_2` and the second half of `comparison_of_ruzsa_distances`.
## Claims
- STEP `PFR_conjecture`
- STEP `PFR_conjecture_aux`
- STEP `entropic_PFR_conjecture`
- STEP `tau_strictly_decreases`
- STEP `tau_strictly_decreases_aux`
- STEP `tau_minimizer_exists`
- STEP `exists_isUniform_of_rdist_eq_zero`
- STEP `rdist_triangle`
- STEP `rdist`
- STEP `tau`
- STEP `symmGroup`
- STEP `rdist_le_of_isUniform_of_card_sub_le`
- STEP `diff_ent_le_rdist`
- STEP `ProbabilityTheory.prob_ge_exp_neg_entropy'`
- STEP `ProbabilityTheory.IsUniform.measureReal_preimage_sub`
- STEP `first_estimate`
- STEP `ent_ofsum_le`
- STEP `condRuzsaDist_le'`
- STEP `condRuzsaDist_of_indep`
- STEP `ProbabilityTheory.Kernel.chain_rule`
- STEP `ProbabilityTheory.measureMutualInfo_nonneg_aux`
- UNDER `PFR_conjecture` `PFR_conjecture_aux`
- UNDER `PFR_conjecture_aux` `entropic_PFR_conjecture`
- UNDER `PFR_conjecture_aux` `rdist_le_of_isUniform_of_card_sub_le`
- UNDER `entropic_PFR_conjecture` `tau_strictly_decreases`
- UNDER `entropic_PFR_conjecture` `tau_minimizer_exists`
- UNDER `entropic_PFR_conjecture` `exists_isUniform_of_rdist_eq_zero`
- UNDER `exists_isUniform_of_rdist_eq_zero` `symmGroup`
- UNDER `tau_minimizer_exists` `continuous_tau_restrict_probabilityMeasure`
- UNDER `tau_strictly_decreases` `tau_strictly_decreases_aux`
- UNDER `tau_strictly_decreases_aux` `cond_construct_good`
- UNDER `tau_strictly_decreases_aux` `sum_dist_diff_le`
- UNDER `tau_strictly_decreases_aux` `sum_condMutual_le`
- UNDER `tau_strictly_decreases_aux` `sum_of_rdist_eq_char_2`
- UNDER `tau_strictly_decreases_aux` `comparison_of_ruzsa_distances`
- UNDER `tau_strictly_decreases_aux` `condRuzsaDistance_ge_of_min`
- UNDER `sum_of_rdist_eq_char_2` `sum_of_rdist_eq`
- UNDER `comparison_of_ruzsa_distances` `kaimanovich_vershik'`
- UNDER `sum_condMutual_le` `second_estimate`
- UNDER `sum_condMutual_le` `I₃_eq`
- UNDER `cond_construct_good` `construct_good'`
- UNDER `construct_good'` `construct_good`
- UNDER `construct_good` `construct_good_prelim`
- UNDER `construct_good_prelim` `ent_bsg`
- UNDER `ent_bsg` `ProbabilityTheory.condIndep_copies'`
- SHARE `PFR_conjecture_aux` 97.7
- SHARE `entropic_PFR_conjecture` 73.6
- SHARE `tau_strictly_decreases` 59.4
- SHARE `tau_strictly_decreases_aux` 56.1
- SHARE `cond_construct_good` 13.1
- SHARE `sum_dist_diff_le` 10.3
- SHARE `sum_condMutual_le` 7.7
- SHARE `ent_bsg` 7.2
- SHARE `ProbabilityTheory.Kernel.chain_rule` 4.4

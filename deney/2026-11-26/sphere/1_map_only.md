# Story of the proof (from the map only)
## For a mathematician
`Smale` (a restatement of `sphere_eversion`): there is a smooth family f(t) of immersions of the unit 2-sphere into 3-space with f(0) the inclusion and f(1) the antipodal map.

The approach is an h-principle for open ample first-order relations, proved by loop averaging ("corrugation"), applied to a hand-built formal solution.

1. Formal side. `formalEversion` is a homotopy of formal solutions of `immersionRel` (1-jets with injective linear part). Via `formalEversionAux`, `familyJoin` attaches to the straight-line base map (1−t)x+t(−x) (`smooth_bs`) a formal derivative made by `familyTwist`: the inclusion's derivative composed with `Orientation.rot`, a rotation about x by angle tπ. `Orientation.isometry_rot` gives injectivity; `formalEversion_hol_near_zero_one` shows it is holonomic near t=0,1.
2. Ampleness: `immersionRel_ample` (needs dim source < dim target; slices computed in `immersionRel_slice_eq`); the relation is also open.
3. `immersionRel_satisfiesHPrincipleWith` specialises `RelMfld.Ample.satisfiesHPrincipleWith`, the parametric, relative, C⁰-close h-principle. It reduces to the non-parametric `RelMfld.Ample.satisfiesHPrinciple` on P×M by `RelMfld.Ample.relativize` and currying (`RelMfld.SatisfiesHPrinciple.satisfiesHPrincipleWith`).
4. Globalisation: `exists_stability_dist` (from `stdLocalisationData`, `nice_atlas`) supplies charts stable under small perturbation; `inductive_htpy_construction` patches chart-by-chart improvements given by `OpenSmoothEmbedding.improve_formalSol`, which transports the problem to vector spaces using `OneJetBundle.embedding`.
5. Local step: `RelLoc.FormalSol.improve_htpy'` / `RelLoc.FormalSol.improve` makes a formal solution holonomic near a compact set, keeping it fixed where already holonomic, using `StepLandscape.improveStep`: add `corrugation`, a 1/N-scaled integral of a loop minus its average, along one direction of a dual pair at a time (guess: induction over a basis).
6. Loops: `exist_loops` yields a smooth family (`NiceLoop.mk`) in the relation's slice, based at b, with average g. `exist_loops_aux2` builds surrounding loops (`surrounding_loop_of_convexHull`, `exists_surrounding_loops`, `extend_loops`); `SmoothSurroundingFamily.exists_smooth_isCenteringDensity` and `SmoothSurroundingFamily.reparametrize_smooth` (via `contDiff_parametric_symm_of_deriv_pos`) reparametrise them to get the prescribed average.

`sphere_eversion` applies step 3 to `formalEversion` relative to t∈{0,1}; the base maps of the result are the eversion.
## For everyone
The theorem says a sphere can be turned inside out smoothly, if the surface may pass through itself but may never be creased or pinched. The proof does not draw the movie; it proves a general machine that produces one. First it writes down a "pretend" solution, in which the surface is simply shrunk through its centre while a separately recorded, fictitious set of tangent directions is rotated half a turn. Then a general theorem shows that such a pretend solution can always be corrected into a real one, because the no-crease condition leaves a lot of room. The correction adds very fine, fast wiggles to the surface, one direction at a time, chosen from loops of allowed directions whose average is the direction one wants. Most of the work is in building those loops smoothly and in gluing the local corrections together over the whole sphere.
## What I could not tell
- `AmpleSet` could not be opened (library notion), so "ample" is known to me only through `immersionRel_slice_eq` and the convex-hull-of-connected-component hypothesis of `exist_loops`.
- `Landscape`, `StepLandscape`, `NiceLoop`, `SurroundingFamilyIn`, `ChartPair`, `SmoothSurroundingFamily.IsCenteringDensity` show only as type signatures; I read `NiceLoop` from its constructor, the others I infer from use.
- How `RelLoc.FormalSol.improve` iterates `StepLandscape.improveStep` (over a basis? how many steps?) is not visible; the "one direction at a time" reading comes from `IsPartHolonomicAt` on a growing subspace in `StepLandscape.improveStep_part_hol`.
- How exactly `sphere_eversion` extracts f and its smoothness from the h-principle output, and the role of its 125 small children (e.g. `OneJetSec.mk.inj`, 1.3%), I could not determine.
- The split of work inside `OpenSmoothEmbedding.improve_formalSol` (15% in 109 small pieces; `ChartPair.mkHtpy_isHolonomicAt_iff`, `ChartPair.dist_update'`, `OpenSmoothEmbedding.Jupdate`) is only guessed to be chart transfer and updating bookkeeping.
- Whether `inductive_construction` or `inductive_htpy_construction` carries the main gluing, and what `RelMfld.satisfiesHPrinciple_of_weak` weakens.
- Why the centering density is needed in addition to surrounding loops: I infer it is a reparametrisation weight making the average equal g.
- The role of `exists_contDiff_of_convex₂` / `exists_of_convex` (local-to-global by convexity, presumably partitions of unity) inside `exist_loops`.
## Claims
- STEP `Smale`
- STEP `sphere_eversion`
- SHARE `sphere_eversion` 99.9
- UNDER `sphere_eversion` `immersionRel_satisfiesHPrincipleWith`
- SHARE `immersionRel_satisfiesHPrincipleWith` 79.7
- UNDER `sphere_eversion` `formalEversion`
- SHARE `formalEversion` 8.8
- UNDER `formalEversion` `formalEversionAux`
- UNDER `formalEversionAux` `familyJoin`
- UNDER `formalEversionAux` `familyTwist`
- UNDER `formalEversionAux` `smooth_bs`
- STEP `Orientation.rot`
- UNDER `formalEversion` `Orientation.isometry_rot`
- UNDER `sphere_eversion` `formalEversion_hol_near_zero_one`
- STEP `immersionRel`
- UNDER `immersionRel_satisfiesHPrincipleWith` `immersionRel_ample`
- UNDER `immersionRel_ample` `immersionRel_slice_eq`
- UNDER `immersionRel_satisfiesHPrincipleWith` `RelMfld.Ample.satisfiesHPrincipleWith`
- SHARE `RelMfld.Ample.satisfiesHPrincipleWith` 77.7
- UNDER `RelMfld.Ample.satisfiesHPrincipleWith` `RelMfld.Ample.satisfiesHPrinciple`
- SHARE `RelMfld.Ample.satisfiesHPrinciple` 64.9
- UNDER `RelMfld.Ample.satisfiesHPrincipleWith` `RelMfld.Ample.relativize`
- UNDER `RelMfld.Ample.satisfiesHPrincipleWith` `RelMfld.SatisfiesHPrinciple.satisfiesHPrincipleWith`
- SHARE `RelMfld.SatisfiesHPrinciple.satisfiesHPrincipleWith` 6.4
- UNDER `RelMfld.Ample.satisfiesHPrinciple` `exists_stability_dist`
- SHARE `exists_stability_dist` 5.2
- UNDER `exists_stability_dist` `stdLocalisationData`
- UNDER `stdLocalisationData` `nice_atlas`
- UNDER `RelMfld.Ample.satisfiesHPrinciple` `inductive_htpy_construction`
- UNDER `RelMfld.Ample.satisfiesHPrinciple` `OpenSmoothEmbedding.improve_formalSol`
- SHARE `OpenSmoothEmbedding.improve_formalSol` 52.2
- UNDER `OpenSmoothEmbedding.improve_formalSol` `OneJetBundle.embedding`
- SHARE `OneJetBundle.embedding` 6.0
- UNDER `OpenSmoothEmbedding.improve_formalSol` `RelLoc.FormalSol.improve_htpy'`
- SHARE `RelLoc.FormalSol.improve_htpy'` 29.0
- UNDER `RelLoc.FormalSol.improve_htpy'` `RelLoc.FormalSol.improve`
- UNDER `RelLoc.FormalSol.improve` `StepLandscape.improveStep`
- UNDER `RelLoc.FormalSol.improve` `corrugation`
- UNDER `RelLoc.FormalSol.improve` `StepLandscape.improveStep_part_hol`
- UNDER `RelLoc.FormalSol.improve` `exist_loops`
- SHARE `exist_loops` 20.7
- UNDER `RelLoc.FormalSol.improve` `NiceLoop.mk`
- UNDER `exist_loops` `exist_loops_aux2`
- SHARE `exist_loops_aux2` 9.9
- UNDER `exist_loops_aux2` `surrounding_loop_of_convexHull`
- UNDER `exist_loops_aux2` `exists_surrounding_loops`
- UNDER `exists_surrounding_loops` `extend_loops`
- UNDER `exist_loops` `SmoothSurroundingFamily.exists_smooth_isCenteringDensity`
- UNDER `exist_loops` `SmoothSurroundingFamily.reparametrize_smooth`
- UNDER `SmoothSurroundingFamily.reparametrize_smooth` `contDiff_parametric_symm_of_deriv_pos`
- UNDER `exist_loops` `exists_of_convex`
- UNDER `exist_loops` `exists_contDiff_of_convex₂`
- STEP `inductive_construction`
- STEP `RelMfld.satisfiesHPrinciple_of_weak`
- STEP `OneJetSec.mk.inj`
- STEP `ChartPair.mkHtpy_isHolonomicAt_iff`
- STEP `ChartPair.dist_update'`
- STEP `OpenSmoothEmbedding.Jupdate`

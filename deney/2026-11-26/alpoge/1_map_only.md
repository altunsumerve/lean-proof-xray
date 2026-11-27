# Story of the proof (from the map only)
## For a mathematician
`riemannHypothesis` states the library (Mathlib) definition RiemannHypothesis (not a project step). Via `rhOfAll` and `allChi` it is reduced to a stronger statement, `UpperTheory.FinalTheorems.everyCharacter`: no Dirichlet L-function L(χ, s) vanishes for Re(s) > 1/2.

That theorem combines two parts. First, `UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter` proves the statement called Row: Galois representations attached to regular algebraic polarized cuspidal data over CM fields, compatible with a local reciprocity map (`UpperTheory.Zero.LLC.recTExists`). It comes from `UpperTheory.Gal.Int.galoisRepresentations_of_thetaLift`, i.e. a theta-lift statement (`UpperTheory.TP.K.tLiftK`) plus a geometric realization, `UpperTheory.Gal.Int.Geo.geoOne_holds`, resting on `UpperTheory.Gal.Int.Geo.geometric_realization_of_weight_one` (a holomorphic Lefschetz formula, `UpperTheory.Gal.Int.Geo.steps_holds`, a Kodaira–Spencer step).

Second, `UpperTheory.FinalTheorems.everyCharacter_of_row` deduces everything from Row, in two branches:

(a) `UpperTheory.One.vwin_of_row` gives VWin: for subfields of cyclotomic fields cut out by a character, a bound on summed "sha lengths" over primes in a window of scales. It passes through `UpperTheory.V.v_window_of_literal_automorphy_n` to `UpperTheory.V.HV.DescentVanishingReductions.vwin_of_hypotheses_H_E_alt` (automorphy, Sp4 image density, a Kato-named step).

(b) `UpperTheory.LiteratureTheorems.every_character_of_literature_of_vWin` uses Row, the local correspondence and VWin. It derives a covolume bound by `SelfIntersectionVolumeEstimates.topCovolSlim2_use_alt_alt` (Arakelov-type inputs: resolution, Hilbert–Samuel, Zarhin, via `PositivityTheory.HtPt.Ah.deep_slim_use`), theta-integral and local-matching statements, then calls `UpperTheory.Lit.every_character_of_theta_integrals_local_matching`. Its bulk is `UpperTheory.Lit.nonempty_hyps_definite_side_of_closed_bound`, producing a nonempty hypothesis package on a "definite side"; the largest piece is `GlobalTheory.Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt` (existence of lattice bundles via `GlobalTheory.T.large_unramified_exponent_bundles_exist_alt`, rows via `GlobalTheory.Fc.AllAtMemberStage0.allRows_of_open0_alt`, a Galois-side theorem `UpperTheory.GalC.final_alt_alt`), with `GlobalTheory.Fc.S0.ontoX_and_lamLow_of_unitaryGroupHypotheses'` and `GlobalTheory.T.open0_of_unitary_group_hypotheses`. Finally `UpperTheory.Top.every_character_of_green_v_win` turns that package, VWin and a Green-type classification of cuspidal characters of finite general linear groups into zero-freeness.

Named inputs appear as hypotheses discharged inside the project: Siegel–Weil, doubling method, Harish-Chandra, Casselman–Wallach, Artin reciprocity, Clozel, Moriwaki, Grothendieck deformation.
## For everyone
This computer-checked proof claims the Riemann Hypothesis, a famous statement about where a certain function can be zero. It actually proves a broader statement about a whole family of related functions and then specialises it. The proof is enormous, over a million machine-checked pieces, and uses only the three standard basic assumptions of the proof system. Its plan is to translate the question about zeros into questions about symmetries of number systems and about sizes of geometric objects. One part builds a dictionary between two kinds of objects, another proves a size bound over ranges of scales, and the largest part shows that a long list of technical conditions can all hold together. A short final step turns these ingredients into the absence of zeros where none should be.
## What I could not tell
- The actual mechanism by which zero-freeness follows: `UpperTheory.Top.zero_free_all_of_green_v_win` concludes ZeroFreeAll from TopG and HostExW, but ZeroFreeAll, HostExW, HypsAlt, FamilyClassConnected, LinkN could not be opened, so why a zero would contradict anything is invisible to me.
- What the "sha length" in VWin measures (shaLen, LData were not opened); my reading of VWin as a Selmer/Tate–Shafarevich-type bound is a (guess).
- What Row0b/PropsB precisely demand, and the statements GeoOne, TLiftK, Steps, KSAll, mainTheorem (single opaque names).
- The meaning of the long parameter machinery (LinkedAt, parametersOfExtension, SlotNormCondition, BundleCondition, AtP, EvLgG, DefiniteSideCondition): I can only say a package of conditions is shown non-empty.
- Whether "hypotheses" labelled Published/Literature are fully proved from scratch or merely restated; the map says the main theorem is unconditional with standard axioms only, but many are marked with a dagger (no literal matching theorem in scope).
- The role of the 14.4% of small auxiliary results directly under `UpperTheory.FinalTheorems.everyCharacter`, and of the 24% duplicate statements.
- How the covolume bound (CovolumeBoundOfX) feeds the definite-side package, and what "third place" refers to in UnitaryGroupThirdPlaceHypotheses.
- The inner content of the VWin branch (HypothesesH' is an opaque structure; "Kato", "Sp4", "unitary three" are name-based readings).
## Claims
- STEP `riemannHypothesis`
- STEP `rhOfAll`
- STEP `allChi`
- STEP `UpperTheory.FinalTheorems.everyCharacter`
- STEP `UpperTheory.FinalTheorems.everyCharacter_of_row`
- STEP `UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter`
- STEP `UpperTheory.Zero.LLC.recTExists`
- STEP `UpperTheory.Gal.Int.galoisRepresentations_of_thetaLift`
- STEP `UpperTheory.TP.K.tLiftK`
- STEP `UpperTheory.Gal.Int.Geo.geoOne_holds`
- STEP `UpperTheory.Gal.Int.Geo.geometric_realization_of_weight_one`
- STEP `UpperTheory.Gal.Int.Geo.steps_holds`
- STEP `UpperTheory.One.vwin_of_row`
- STEP `UpperTheory.V.v_window_of_literal_automorphy_n`
- STEP `UpperTheory.V.HV.DescentVanishingReductions.vwin_of_hypotheses_H_E_alt`
- STEP `UpperTheory.LiteratureTheorems.every_character_of_literature_of_vWin`
- STEP `SelfIntersectionVolumeEstimates.topCovolSlim2_use_alt_alt`
- STEP `PositivityTheory.HtPt.Ah.deep_slim_use`
- STEP `UpperTheory.Lit.every_character_of_theta_integrals_local_matching`
- STEP `UpperTheory.Lit.nonempty_hyps_definite_side_of_closed_bound`
- STEP `GlobalTheory.Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt`
- STEP `GlobalTheory.T.large_unramified_exponent_bundles_exist_alt`
- STEP `GlobalTheory.Fc.AllAtMemberStage0.allRows_of_open0_alt`
- STEP `UpperTheory.GalC.final_alt_alt`
- STEP `GlobalTheory.Fc.S0.ontoX_and_lamLow_of_unitaryGroupHypotheses'`
- STEP `GlobalTheory.T.open0_of_unitary_group_hypotheses`
- STEP `UpperTheory.Top.every_character_of_green_v_win`
- STEP `UpperTheory.Top.zero_free_all_of_green_v_win`
- UNDER `UpperTheory.FinalTheorems.everyCharacter` `UpperTheory.FinalTheorems.everyCharacter_of_row`
- UNDER `UpperTheory.FinalTheorems.everyCharacter` `UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter`
- UNDER `UpperTheory.FinalTheorems.everyCharacter` `UpperTheory.Zero.LLC.recTExists`
- UNDER `UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter` `UpperTheory.TP.K.tLiftK`
- UNDER `UpperTheory.Gal.Int.galoisRepresentations_of_thetaLift` `UpperTheory.Gal.Int.Geo.geoOne_holds`
- UNDER `UpperTheory.Gal.Int.Geo.geometric_realization_of_weight_one` `UpperTheory.Gal.Int.Geo.steps_holds`
- UNDER `UpperTheory.FinalTheorems.everyCharacter_of_row` `UpperTheory.One.vwin_of_row`
- UNDER `UpperTheory.One.vwin_of_row` `UpperTheory.V.HV.DescentVanishingReductions.vwin_of_hypotheses_H_E_alt`
- UNDER `UpperTheory.FinalTheorems.everyCharacter_of_row` `UpperTheory.LiteratureTheorems.every_character_of_literature_of_vWin`
- UNDER `UpperTheory.LiteratureTheorems.every_character_of_literature_of_vWin` `SelfIntersectionVolumeEstimates.topCovolSlim2_use_alt_alt`
- UNDER `SelfIntersectionVolumeEstimates.topCovolSlim2_use_alt_alt` `PositivityTheory.HtPt.Ah.deep_slim_use`
- UNDER `UpperTheory.LiteratureTheorems.every_character_of_literature_of_vWin` `UpperTheory.Lit.every_character_of_theta_integrals_local_matching`
- UNDER `UpperTheory.Lit.every_character_of_theta_integrals_local_matching` `UpperTheory.Lit.nonempty_hyps_definite_side_of_closed_bound`
- UNDER `UpperTheory.Lit.every_character_of_theta_integrals_local_matching` `UpperTheory.Top.every_character_of_green_v_win`
- UNDER `UpperTheory.Lit.nonempty_hyps_definite_side_of_closed_bound` `GlobalTheory.Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt`
- UNDER `GlobalTheory.Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt` `UpperTheory.GalC.final_alt_alt`
- UNDER `GlobalTheory.Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt` `GlobalTheory.T.large_unramified_exponent_bundles_exist_alt`
- UNDER `UpperTheory.Lit.nonempty_hyps_definite_side_of_closed_bound` `GlobalTheory.T.open0_of_unitary_group_hypotheses`
- SHARE `UpperTheory.FinalTheorems.everyCharacter_of_row` 79.2
- SHARE `UpperTheory.LiteratureTheorems.every_character_of_literature_of_vWin` 68.7
- SHARE `UpperTheory.Lit.every_character_of_theta_integrals_local_matching` 43.0
- SHARE `UpperTheory.Lit.nonempty_hyps_definite_side_of_closed_bound` 37.2
- SHARE `GlobalTheory.Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt` 15.6
- SHARE `UpperTheory.One.vwin_of_row` 8.5
- SHARE `SelfIntersectionVolumeEstimates.topCovolSlim2_use_alt_alt` 7.3
- SHARE `UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter` 6.4
- SHARE `UpperTheory.Top.every_character_of_green_v_win` 1.6

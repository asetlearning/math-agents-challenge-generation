---
type: validation-triage
date: 2026-10-20
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-027: review of Math Expert's breakability proposal (MathExpert/proposals/2026-10-20-t027-breakability-and-breaker-list): soundness of each breaker's 'valid in G_beta' claim, the definitions, the registered B4 prediction"
verdict: "Mostly sound, with corrections. (a) D: the equality is in G_k for the stage being RUN when the throw happens. The check is not made only at the coset bound: here all 16 shortenings came at the end of stage 3, below the bound, so they hold in G_3. (b) F1 'decides n <= 58' does not follow from K-S Thm 3, which covers positive words only. R1/R2 need positive length 49 > 29 on each side even at the best rotation and split, so they are not covered. B5 as stated is unsound; it is sound if B0 only proposes and kbmag/D certifies each replacement. The 'L1-B > 58' floor has no basis. (c) B4 is sound (conjugacy in G_7) given the stated conditions. The prediction is well formed but needs its parameters pinned. Also: R and B4 give conjugacy, not equality (§0.2 and the certificate composition need conjugators), and the B8 parameter needs both figures stated. Also: kbmag proves all 16 D steps directly, so route 2 is unnecessary here."
---
# T-027 breakability proposal: review (triage)

This is a Lead request (2026-10-20). It reviews `Agents/asetlearning/MathExpert/proposals/2026-10-20-t027-breakability-and-breaker-list.md` and takes in Lead's FYI on K-S 2010 Thm 3 (Researcher's addendum; the PDF re-check is pending).

**Evidence.**
- The tcgraph source at `63564c3`.
- My reproduction, [[2026-10-20-t027-solver-reproduction]]. It stored every D/R intermediate, ran B0 on all of them, and ran kbmag on the originals, the intermediates and the residuals.
- Two small computations on those words, with the script `review_stats.py` in my gitignored `t027/` directory.

Nothing else was run. This is a triage: a scoped check of the logic, not a full verification of every breaker's implementation.

**Terms.**
- **G_k** = ⟨a, b | v⁵, |v| ≤ k⟩, which maps onto B(2,5).
- **Positive length L(u)**: each letter a or b costs 1 and each inverse letter costs 4, since x⁻¹ = x⁴ in B.

## (a) What D's shortening proves

**Confirmed, with a correction.** ShorterLengthFound(u) means **u = w in G_k, as elements** (enumeration over the trivial subgroup), where k is the stage being run when it was thrown. Details are in the reproduction note §2.

**Corrections to §0.1 and to the B6 / B7 rows:**
- "The shortening is only checked when the table hits coset_bound" is **false**. `completeWith` calls `track_word_length` at the end of every stage, at the bound, and every 10⁸ iterations.
- "k = the stage at which the table filled" is **wrong** for the owner's own data:
  - all 16 shortenings came at the **end of stage 3**, with the table below 20M;
  - each was reproduced at rml = 3 and not at rml = 2;
  - so every D step in the owner's chain is an equality in **G_3**.
- The table fills at stage 4 only in the undecided calls.
- So the breaker record should state the **throw stage**, not the fill stage.

**§0.2 "every R step is an equality in G_|u|" is false.** R works on cyclic permutations, so each R step is a **conjugacy**. The rewrite inside it is an equality in G_m, where m is the period used, and m is not bounded by 7.
- The conclusion still holds: the residuals are trivial in B(2,5).
- "G_9 or higher" is now moot. kbmag (rec and slx) reduces R1, R2, R3 (249) and the 251-letter word to IdWord, so **all residuals are trivial in G_7**.

## (b) F1 and Kuznetsov–Shlepkin 2010 Thm 3

**The statement as Lead relayed it.** For **positive** words v, w over {a, b} with L(v), L(w) ≤ 29: v = w in B0 iff v = w in B.

**What follows.**
- A word u is decided by B0, conditionally on Thm 3, if some cyclic rotation of u or of u⁻¹ splits as u₁u₂ with L(pos(u₁)) ≤ 29 and L(pos(u₂⁻¹)) ≤ 29. Here pos replaces each x⁻¹ by x⁴, which is an equality in B.
  - Rotations are allowed because triviality is invariant under conjugacy.
  - The claim "any u with |u| ≤ 58 is decided" **does not follow**: a letter count does not bound the positive length.
- **R1 and R2 are not covered by direct rewriting.** Each has positive length 140. Over all rotations of u and u⁻¹, all splits and the rewriting x⁻¹ → x⁴, the best gives max(L(v), L(w)) = **49 > 29**, for both. Any other route to a v·w⁻¹ form would need equalities in B, which is circular. So F1 does not decide them via Thm 3.
  - They are trivial anyway: by the certified chain, and directly by kbmag.
- **The "L1-B: |w| > 58" floor** has no basis as written. If a floor is kept, it should be the positive-length criterion above. Even that criterion is conditional on a computation that was never replicated and has no published code.
- **F1's filter direction is sound unconditionally.** B0 is a quotient of B, so u ≠ 1 in B0 implies u ≠ 1 in B.

**B5 (K29) as stated is unsound.** It applies a ≤ 29 window bound to words with inverses, and the B0 → B transfer uses Thm 3 outside its word class. Two sound repairs:
1. **Conditional.** Restrict to windows x and candidates y whose positive forms have L ≤ 29. This is a much smaller scope, because an inverse letter costs 4.
2. **Unconditional (recommended).** Use B0 only to **propose** y, then certify x y⁻¹ = 1 by kbmag (TRUE ⇒ G_7) or by D (TRUE ⇒ G_k). This needs no theorem, and the window length becomes a budget parameter rather than a soundness bound. Lead's FYI already asks Math Expert to correct F1, B5 and the floor.

## (c) B4 (Dehn over V) and the registered prediction

**Soundness: sound.** Suppose t = 1 in G_k and a cyclic rotation of t^{±1} is x z. Then x = z⁻¹ in G_k, so replacing a window x of length > |t|/2 by z⁻¹ shortens the word.
- The window is cyclic, so the result is a **conjugate**, as with R.
- With V = R7 ∪ the 820 dataset words, every t is trivial in G_7:
  - R7 entries are relator cores of v^{5k}, |v| ≤ 7;
  - each dataset word reduces to IdWord under at least one kbmag system (kb-verify-20261007).
- So B4's SHORTER is a conjugacy in G_7. For a **certificate**, as opposed to a proof, a tile needs an L0 certificate; a kbmag reduction proves triviality but is not a certificate.

**Prediction** (B4 shortens ≥ 10 of 12 in one pass; B4 ↔ R empties ≥ 6). It is well formed and falsifiable. To make it binding, pin these before the run:
- V exactly, by file and sha256, including whether inverses and rotations of every t are in the pattern set;
- originals only, or all 16 images;
- the window-choice rule: longest first or left-most;
- "one pass" (one replacement or a maximal scan), and the restart rule in B4 ↔ R;
- the round cap.

The kbmag result is consistent with §3's vocabulary-leak mechanism, but it does not test B4.

## Other points

1. **The SHORTER definition (§1).** It should allow "w′ conjugate to w in G_β", because R, B2 and B4 are cyclic. That is fine for triviality, and for certificates it requires recording the conjugator.
   - The addendum's composition "w_r = (w_r w⁻¹) · w" is valid only for equality steps. With cyclic steps the certificate needs the rotation conjugators. It is still practical.
2. **The R-step cell "over R7 when |u| ≤ 7"** ~~is not automatic … only 312 entries have |v| = 7~~ — **corrected 2026-10-20: this point was wrong.** b25_full (sha256 `b1d511fe…`) covers **all 510** primitive, cyclically reduced classes v with |v| ≤ 7, up to rotation, with inverses added. 312 is exactly the number of |v| = 7 classes. So every R step whose period, reduced to its primitive cyclic core, has length ≤ 7 has an R7 cell. A lookup is needed only to find the table entry and the rotation, and R7 presents G_7.
3. **Route 2 (local decomposition of D steps) is not supported yet.** A single-window prefix/suffix diff between each D input and output gives:
   - loops of 259–2,845 letters on 13 of the 16 steps;
   - short loops on only 3 steps: 16, 41 and 83 letters.

   This is a coarse measure: a BFS geodesic can agree with w in scattered places, and a multi-window alignment could still find local pieces. The stored intermediates allow that test.
   - **kbmag certifies every D step whole.** All 16 loops w_i · u_i⁻¹ (148–2,849 letters) reduce to IdWord under rec and slx. So if kbcert can turn a rec reduction into R7 cells, D steps are certifiable without any decomposition. Route 2 is then unnecessary, at least for these words.
4. **B8.** The systems were built with `kbprog -me 100000`. The stored `.kbprog` files carry `maxeqns := 2000000` so that `wordreduce` can load them, so the proposal's "2·10⁶" is the file field, not the completion budget. State both. I regenerated both systems, and they are byte-identical apart from that line. "TRUE ⇒ w = 1 in G_7" is correct.
   - B8 already breaks all 12 originals, in under 0.5 s in total. The cost column ("seconds per word") is pessimistic.
5. **B1** (`greedy_reduce2_5`, not cyclic): an equality in G_|u|. Correct.
6. **B9:** unbounded at `coset_bound = 0`. Correct; it needs a cap.
7. **D's FALSE:** proves w ≠ 1 in G_k only. That is correct, and it means D must not be listed as a filter for B.
8. **§1 data** ("D shortened 12/12; with R, 8/12 emptied, including ds160"): confirmed by the reproduction.
9. **Not checked:**
   - B3 (kbcert) and its "G7" claim;
   - the cost estimates;
   - §3's tube-radius argument;
   - the Hall-polynomial collector's coverage (Researcher).

## Recommendation

Return the proposal to Math Expert for these fixes:
- (a) the throw stage instead of the fill stage, and checks made at the end of every stage;
- R and B4 as conjugacy, with SHORTER and certificate composition updated to match;
- F1, B5 and the floor restricted to the positive word class, with the unconditional B5 variant;
- the B8 parameter;
- the prediction's parameters pinned before the run.

After that, B4's soundness and the corrected F1 and B5 need no further math check before Experimenter runs. The name is the owner's decision; I take no position.

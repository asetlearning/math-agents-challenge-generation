---
type: validation-verdict
date: 2026-10-20
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-027: confirmation of Math Expert's breakability proposal v2 and the success-metrics / glossary drafts"
verdict: "CONFIRMED with issues. v2 resolves all 8 review items. One of them was my own error: R7 covers every primitive class |v| <= 7, so the 'R7 lookup' caveat reduces to finding the entry, and I have corrected my notes. The levels are well defined in logic but not yet reproducible: pin the KB mode and the per-system rule, D's rotation rule and its log steps, the composite caps, the CL cap outcome and the code and system hashes. The D budgets in S_std are named below. Drafts: accurate except the depth line (flip is 2-4, not 3-4) and two consistency points."
---
# T-027 breakability v2 and drafts: confirmation

This is a Lead request (2026-10-20). It covers [[2026-10-20-t027-breakability-and-breaker-list-v2]] and [[2026-10-20-t027-metrics-and-glossary-drafts]]. Earlier notes: [[2026-10-20-t027-breakability-proposal-review-triage]] and [[2026-10-20-t027-solver-reproduction]].

## Review items

| item | v2 | status |
|---|---|---|
| D: the throw stage, and checks at every stage end, at the bound and every 10⁸ iterations | §0.1, D1 row | resolved |
| R and DV are conjugacies, and certificates record c | §0.2, §1, §4 | resolved. The composition rule in §4 is correct: conjugating every cell by c conjugates the product, and an R rewrite x u^e y → x u^{e−5} y appends the one cell y⁻¹u^{−5}y |
| F1 class (positive words, rotation and split, 29 / 29) | §0.4, F1 row | resolved. I recomputed R3's best split: **279** |
| K29: B₀ proposes, KB or D certifies | K29 row | resolved and sound |
| DV pinned | §3.3 | mostly resolved, but see issue 3 |
| SHORTER with conjugators | §1 | resolved |
| R-step R7 lookup | §4 | **my item was wrong.** b25_full covers all 510 primitive, cyclically reduced classes with \|v\| ≤ 7 (up to rotation, with inverses), checked on `rec` (sha256 `b1d511fe…`). 312 is exactly the number of \|v\| = 7 classes. So the cell is always over R7 when the period's primitive core has length ≤ 7; the lookup only finds the entry and the rotation. Please change §4 to say this. I have corrected my two notes |
| KB `-me 100000` | KB row | resolved. The stored `.kbprog` files carry `maxeqns := 2000000` so that `wordreduce` can load them. I regenerated both systems from b25_full, and they are byte-identical apart from that line |

## Issues in v2

1. **§1, definition 1.** "Cyclic-insensitive breakers (KB, D)" should read **rotation-sensitive**. KB and D act on the linear word, which is why a rotation rule is needed.
2. **The levels are well defined in logic, but not yet reproducible.** Pin the following:
   - **KB.**
     - Which mode counts for the level: screen (rotations 0 and ⌊n/2⌋) or certify (every rotation of the 16 images).
     - "Resilient" should mean NONE from **both** rec and slx.
     - Reproducibility needs the system hashes: `rec.kbprog` `436fd2c7…`, `slx.kbprog` `75b12c59…`, from b25_full `b1d511fe…`.
   - **D1.**
     - The rotation rule: the 16 images as given, or with rotations.
     - The **log steps**. `len_log_step` (default 10⁸) is one of the moments at which D checks for a shorter word, so it can change the output.
   - **CL.** What a run that hits the 10⁶-node cap returns (presumably NONE), and its rotation rule.
   - **Composite S_std.** The round cap and the CPU cap of Res_S, and whether D1 still runs as a stage when DR follows it.
   - **Code.** b25 and tcgraph repo@sha, and the GAP/kbmag build for the filters.
   - **Determinism.** D and kbmag are deterministic: my run reproduced the owner's 16 D outputs exactly. So once the items above are pinned, the levels are reproducible.
3. **DV tie-breaks.** Two things are still unpinned:
   - the choice between patterns that give the same longest x with different complements z (suggest: shortest z⁻¹, then the lexicographically smallest t);
   - the start position of the cyclic scan, and whether a window may wrap around the end. Without these, two implementations can disagree.
   - Also name the R7 file by path and sha256, as is done for the dataset file. The dataset file's sha256 `62c6431c…` matches the kb-verify provenance.
4. **§4, D steps.** "No fragment yet" can be updated. All 16 D-step loops w_i·u_i⁻¹ (148–2,849 letters) reduce to IdWord under rec and slx. So the kbcert route (rec rules → R7 cells), if practical, certifies D steps whole, with no local decomposition.
5. **§3.5, item 3** is correct: B₀-geodesic windows are geodesic in every G_k and in B. Add that this excludes only **length-decreasing** KB rules: rec also applies non-shortening rules, so B₀-local geodesicity does not imply KB resilience.

## Budgets inside S_std (as Lead asked)

**In S_std:**
- **D1**: `attempt_to_decide_if_trivial` with coset_bound 20,000,000 and relator_max_length 5, log_step 10⁷, len_log_step 10⁸. It is one call per input word (rotation rule to be pinned), deterministic, and measured at **1.1 GB** peak RSS.
- **DR**: D1 alternated with R, at most 50 rounds, with the same D1 parameters in each round.

**Not in S_std**, as escalations on rjob only: D(2·10⁸, 7) and D(10⁹, 9).

A word that is "S_std-undecided" is therefore undecided only at these budgets.

## Drafts

- **Draft A, the source sentence.** "These words had passed L0, L1 (ρ_min16 = 1) and strict and flip depth 3–4" should read **S2 3–4, flip (d) 2–4**: ds781 has flip 2. These are T-024 certificate bounds, and T-017 later lowered some of them.
  - ρ_min16 = 1.0 holds for all 12, as stored.
  - The rest of the source sentence is accurate: D shortened 12/12, D+R emptied 8/12, and kbmag reduced the 12 originals and the 3 residuals (and the 251-letter word) in under 1 s.
- **The principle** agrees with v2 §5. I cannot check the owner's wording, which reached me only as relayed.
- **The breaker table** agrees with v2. Copy in the pins of issue 2 when they are decided.
- **"Strictly resilient"** in Draft A lacks v2's rotation-rule caveat for KB and D. Add it.
- **Glossary.** Every row is accurate.
  - "R7 presents G_7" is **correct**: all |v| ≤ 7 classes are present, and non-primitive or non-cyclically-reduced v⁵ are consequences of them.
  - "Every G_k maps onto G_{k+1} and onto B(2,5)" is correct.
  - The throw-stage entry is correct.
  - The Thm 3 entry matches the Researcher's transcription (PDF check pending).

## Scope

- I checked the logic and the stated facts against my reproduction data and against b25_full.
- I did not check CL (kbcert), the cost estimates, or the §3 mechanisms, which are labelled argued or conjectured.

---
title: t018-t021-diagram-search-2026-10-14
hypothesis: "A search over van Kampen diagrams that attaches 2–3-cell patches of standard relators v^5 (|v| <= 7, b25_full) while keeping the boundary 2.5-power-free produces the first certified L1, novel B(2,5) word with a genuinely deep folded diagram (maxdepth >= 2 and T_deep >= 0.5 on the compressed certificate). D and D_c are tracked but not expected to reach 1."
status: draft
author: asetlearning
date: 2026-10-14
todo: T-018, T-021
project: challenge-gen
instance: B(2,5)
experiment_type: structured-constructions
tags: [agent/exp, user/asetlearning, domain/group-theory, topic/burnside, topic/b25, topic/trivial-words, topic/hard-instance-generation, topic/proof-certificates, topic/dehn-function, project/challenge-gen, status/pending, experiment, methodology]
---

# T-018 + T-021: diagram search over |v| ≤ 7 with a power-free boundary — pre-registration (DRAFT, revision 3)

**Status: draft revision 3 (owner decisions 2026-10-14 applied). The run is held.** Order before start (owner):
1. Developer's inverse-cell reduction;
2. Math Expert's revision (done: [[2026-10-14-vertex-depth-criterion]]);
3. Validator reviews T-016, b25 PR #13 (T-023) and the revision;
4. PRs #12 and #13 are merged;
5. revision 3, checked against the merged code, goes to Lead;
6. start.

No kbprog runs.

Sources:
- Math Expert idea 3 (diagram search) and idea 2 (standard relators |u| ≤ 7), [[2026-10-14-cancellation-constructions]];
- the area-vs-path criterion [[2026-10-14-area-vs-path-criterion]] and its revision, the vertex-depth criterion [[2026-10-14-vertex-depth-criterion]];
- the T-016 triangle census, [[t016-overlap-chaining-2026-10-14#Triangle census results (2026-10-14)]];
- Developer's T-023 results (b25 PR #13): chains have b₁ up to 29 from tiny triangles but compress hard (best E1c word: N* 55 → N*_c 7, D_c 0.167); T-003's best D_c is about 0.11–0.12; about 25% of R-M finalists have adjacent inverse cells.

## Revision history
- **Revision 2:**
  - headline D_c;
  - negative control = path-like;
  - multiples v^{5k} kept out of the moves but included in compression;
  - S2 dropped;
  - half-exposure rule hard;
  - s_min = 3.
- **Revision 3** (owner 2026-10-14):
  1. The classification uses **vertex depth** (N_deep, maxdepth, T_deep, T_depth) on the compressed, reduced certificate. Hub degree and cut width become diagnostics.
  2. **J = (N_deep + 0.25 V_int)/|w̄|** on the compressed diagram, with four hard gates and tie-break by smaller |w̄|.
  3. **Success criterion:** the first B(2,5) word with maxdepth ≥ 2 and T_deep ≥ 0.5 (L1-certified, novel). D and D_c are tracked but not expected to reach 1.
  4. **Negative controls:** T-003 and T-016 words must have N_deep = 0 (Developer is computing them).
  5. **Headline:** D_c on pure sets. This experiment uses a pure set.
- **Revision 4** (owner 2026-10-15): final area-like rule, wrapped-relator guard, depth-sum J and maxdepth-vs-N logging (section below).

## Check against the merged code (b25 main `6f71817`, 2026-10-15)
PRs #12 (T-016, `ef86020`) and #13 (T-023 + inverse-cell reduction + depth, `6f71817`) are merged.
- **Calibration tests pass on main:** 53 of 53 in `hardness/tests/test_diagram.py` and `t016/tests`. They include the grid depth identity, ladder depth, hexagonal patch, chains with no deep cells, and the objective J. Step 0's depth controls therefore exist as tests and are re-run at the start.
- **J matches revision 3.** `diagram.objective_J` = (N_deep + 0.25·V_int)/|w̄|, and depth statistics are computed on the compressed certificate (`diagram_stats`).
- **Compression table is selectable** (`closure_fixpoint(table, …)`, `relator_classes`). T-018 must pass the **R7 table** (1,630 entries). Developer's T-003/T-016 numbers used the 1,684-entry T-002 table.
- **Classification needs updating:** `diagram.shape()` still implements the old rule ("too small" for N < 9, then T_deep and T_depth ≥ 0.5). T-018 applies the owner's final area-like rule (below) in its own evaluation, or uses Developer's update if one lands first.
- **The negative control is restated (this revision).** On the compressed certificate, chain words *can* have N_deep > 0: compression folds them into small diagrams that enclose a cell (E1: 10 words, E1c: 10, E1d: 46, all with maxdepth 1). The control is therefore: **no T-003 or T-016 word is area-like under the final rule, and none has maxdepth ≥ 2.** Status: passes. Max maxdepth is 1 over 2,256 T-003 words and the 611 T-016 E1/E1c/E1d finalists, and no word has N_deep ≥ 2 with N ≥ 16.
- **The standard guard is not in the harness yet.** Developer was asked on 2026-10-14 to fold Validator's closure test and the ≤ 2-cell test into it (`hardness/guard.py`), exhaustive for all |w̄| including the vertex and stem cases when |w̄| ≥ 64, with a table argument. **This gates the start.**

## Area-like rule, guard and objective (owner decision 2026-10-15)
Final rule from [[challenge-gen-success-metrics]] § Owner decision 2026-10-15 (Math Expert's [[2026-10-14-depth-followups]]; Validator reviews it in parallel with the run):
- **area-like** iff N ≥ 16, T_deep ≥ 0.5, T_depth ≥ 0.5, and (a dual-connected deep core of ≥ 2 cells, or maxdepth ≥ 2); **small enclosed** iff N_deep ≥ 1 and N < 16; **thick strip** iff N_deep ≥ 1, N ≥ 16 and not area-like; path-like iff N_deep = 0.
- **Wrapped-relator guard:** N_deep = 1 with every other cell touching both ∂Δ and the deep cell → "wrapped relator", not novel. It is applied with the finalist novelty checks.
- **J = (Σ depth(c) + 0.25·V_int)/|w̄|** replaces (N_deep + 0.25·V_int)/|w̄| as the beam score. `diagram.objective_J` on main still implements the old J, so T-018 computes the new J itself unless Developer's update lands first. The same applies to `diagram.shape()`.
- **maxdepth vs N:** logged at every N reached, per lineage, with a log N against √N fit across seeds as the hyperbolicity falsifier.
- H2 is unchanged.

## Standard guard (owner decision 2026-10-14; applied as a finalist gate)
Every finalist must also pass:
1. the non-increasing 2.5-closure contains neither ε nor any relator class (R7 and dataset classes);
2. the exhaustive ≤ 2-cell certificate test over the R7 table;
3. N*_c is reported next to D.

Words failing (1) or (2) are not counted as L1 or novel. The search's own gate 4 (no ≤ 3-cell block equal to a table class) stays as it is.

## Question
Every word the project has produced so far is path-like: random products (T-002), PatternBoost (T-003) and chains (T-016). In the chains, every cell touches one boundary hub vertex. Can a search that adds cells in **patches** along a 2.5-power-free boundary build diagrams with **deep cells** (cells with no vertex on the boundary) over the standard relators |v| ≤ 7? What maxdepth, T_deep and T_depth does it reach by N ≈ 60–120 cells, and how do D and D_c behave?

**Sizing (Math Expert's conjecture, accepted as the working assumption by the owner).** A square-like disc has |w̄| ≈ 4√N·e, where e is the exposed letters per boundary cell. So D ≥ 1 needs N ≳ 16e². With 35-letter cells, e ≈ 9 and N ≈ 1,300. T-018 at N ≤ 150 therefore targets **depth, not D ≥ 1**.

## Relator set R7 (T-021)
- **Source:** `b25_full`, the Knuth–Bendix input of March 2026. It is in algo-mixer at `experiments/_inputs/kbmag/b25_full`, with an identical copy at `kbmag_source/standalone/kb_data/b25_full`, sha256 `b1d511fe…ba32ee`. Header: "815 relations from freely reduced words up to length 7".
- **Content** (parsed 2026-10-14): 815 relators v^{5k}.
  - 795 are primitive v⁵, with |v| = 1, 2, 3, 4, 5, 6, 7 contributing 2, 2, 8, 21, 64, 178, 520 relators.
  - 20 are multiples v^{5k} with k = 2–7 of roots with |v| ≤ 3.
- **Tables:**
  - **Move table:** the 795 primitive v⁵ and their inverses (1,590). Patches use only these.
  - **Compression and certificate table:** all 815 and their inverses (1,630, hash-pinned), including the multiples. The L0 relator check is `relator_is_fifth_power`.
- **Pure set:** the headline is D_c. D_dataset_c does not apply.

## Terms
New terms for T-018 are added to [[challenge-gen-glossary]] with the results; the depth terms are already there (owner 2026-10-14).
- **Diagram state.** A certificate F over the move table together with its boundary w = cyc(expand(F)). Δ(F) is the folded diagram (T-023). The **compressed reduced certificate** F_c is F after loop erasure, Peiffer-pair deletion, inverse-cell reduction and relator-closure compression against the 1,630-entry table, so N*_c = |F_c|. All depth statistics and J are computed on Δ(F_c) (headline). The same statistics on Δ(F) are diagnostics.
- **Deep cell, depth, maxdepth, N_deep** (Math Expert's vertex-depth criterion):
  - A cell is **deep** if none of its vertices lies on the boundary ∂Δ; touching ∂Δ at a single point counts as touching.
  - **Peeling:** remove all cells touching ∂Δ, recompute the boundary, and repeat. depth(cell) is the round in which the cell is removed, counting from 0.
  - **maxdepth** is the largest depth; **N_deep** is the number of cells of depth ≥ 1.
- **T_deep, T_depth** (normalised against the ideal square with the same N):
  - T_deep = N_deep/(√N − 2)²;
  - T_depth = maxdepth/((√N − 1)/2).
  - Both are defined for N ≥ 9; below that a word is "too small".
- **V_int:** the number of interior vertices of the diagram (vertices not on ∂Δ), the old b₁ shaping quantity. **b₁_deep:** the cycle rank of the dual graph restricted to cells of depth ≥ 1, a diagnostic.
- **Classification** (owner 2026-10-14):
  - **path-like** iff N_deep = 0;
  - **area-like** iff T_deep ≥ 0.5 and T_depth ≥ 0.5 (N ≥ 9);
  - **thick strip** otherwise.
  - Hub degree, cut width and the old b₁/N_int are diagnostics only.
- **Patch.** A connected set of 2 or 3 cells from the move table, each a rotation c⁻¹ r c, glued along shared pieces so that the patch is itself a reduced diagram. Its **outer boundary** B_P is the cyclically reduced expansion of its cells' product. Single cells are not patches: a power-free boundary has no x^{2.5}, so a single u⁵ cell attached along it always exposes more than half of itself.
- **Attachment site.** A cyclic segment s of w with |s| ≥ s_min = 3, such that B_P contains s⁻¹ cyclically. Write B_P = s⁻¹ t cyclically. Then t = s in the group, and attaching replaces s by t: if w = x s z cyclically, the new boundary is w' = cyc(x t z). F' is F plus the patch's cells, conjugated by the boundary prefix up to s.
- **Hard gates** (an attachment is admissible only if all hold):
  1. **Half-exposure:** each new cell of length 5|v| ends with exposure ≤ 2.5|v|.
  2. **Exact boundary power test:** w' has no 2.5-power, linear or cyclic (`hardness/powerfree.py`). Then the reducer does nothing on all 16 images, so ρ_min16 = 1 and L1 holds by construction (re-certified on finalists).
  3. **No cancelling pairs** in Δ(F'): T-023 reducedness and inverse-cell check.
  4. **No compressible block:** no contiguous block of ≤ 3 cells of F' whose expansion is cyclically a table entry (any of the 1,630).
  - Plus |w'| ≥ 20.
- **Growth step:** one admissible attachment. **Stall:** a state with no admissible attachment within the candidate budget.
- **Objective J** = (N_deep + 0.25·V_int)/|w̄|, computed on Δ(F_c). The goal term is N_deep. V_int is a small shaping term that gives a gradient before the first ring of cells closes; the weight 0.25 keeps a ring of triangles from standing in for a deep cell. Tie-break: smaller |w̄|, then the seed.

Existing terms used as defined: D, D_P, D_c, N*_c, D_area, D_path, provenance rule, G2 and the all-classes check ([[challenge-gen-glossary]], [[challenge-gen-success-metrics]]).

## Method
0. **Calibration (gate; nothing runs before it passes).**
   - **Depth controls on the merged T-023 code** (expected values from Math Expert, conjectured; Validator checks the grid identity):

     | Diagram | N_deep | maxdepth |
     |---|---|---|
     | n×n grid certificate of [aⁿ, bⁿ] over [a, b], n = 3 to 8 | (n−2)² | ⌊(n−1)/2⌋ |
     | 3×k ladder | k−2 | 1 |
     | Classification of the 5×5 grid | area-like (T_deep = T_depth = 1.0) | |
     | Classification of the 3×20 ladder | thick strip (0.54 / 0.30) | |

   - **Negative controls (owner; restated 2026-10-15 after the merged-code check):** no T-003 or T-016 finalist (E1, E1c, E1d) is area-like under the final rule, and none has maxdepth ≥ 2. Developer's and Experimenter's T-023 numbers are used. Status: passes (max maxdepth 1). The original form, N_deep = 0, fails on the compressed certificate for 66 chain words, which are small enclosed or thick strip.
   - **Positive control:** a hand-built 2-cell patch over the move table glued along a square (Math Expert's example: an (ab)⁵ cell along "abab" sharing "aba" with an (aab)⁻⁵ cell), checked against all four gates.
   - **D_c check:** the merged code reproduces Developer's best E1c value (N*_c 7, D_c 0.167).
   - If any control disagrees, stop and report to Lead and Developer.
1. **Patch library.**
   - All 2-cell patches of the move table whose two cells share a maximal piece of length ≥ 2 (pieces between distinct primitive roots are short by Fine–Wilf).
   - 3-cell patches: a 2-cell patch plus one cell sharing pieces with both.
   - Capped at 10⁶ per type, with a seeded sample if over. Outer boundaries are indexed by cyclic 3-letter windows.
   - Report the size, the share with a power-free outer boundary, and the |v| mix.
2. **Seeds.** 200 seed diagrams, each a single admissible patch (power-free cyclically reduced boundary, reduced, |w̄| ≥ 20). They are drawn uniformly from the library with seed 18000001, stratified by the largest |v| in the patch (4–5, 6, 7).
3. **Search.**
   - Beam search: beam 100, **at most 60 growth steps**, so N up to about 150 cells and N ≈ 60–120 for typical 2–3-cell steps (owner: allow N ≈ 60–120). Up to 2,000 admissible attachments are tried per state per step.
   - Gates are checked in order 2, 1, 4, 3 (cheapest first). Score J; at most 5 states per seed lineage. Tie-breaking seed 18000001.
   - A greedy run (beam 1) is reported as a reference.
   - Logged per step: the best and median maxdepth, N_deep, T_deep, T_depth, V_int, D, D_c and |w̄|, and the stall count.
   - Logged per lineage at every N reached: maxdepth (for the log N against √N fit).
4. **Finalists and evaluation.**
   - The 200 best distinct boundary words by J (at most 10 per lineage), plus, per lineage, the state with the highest maxdepth and the best state per step count {5, 10, 20, 40, 60}.
   - Independent harness on the 1,630-entry table: L0, F*, F*_P, the exact power test, certify-mode R₂.₅ and ρ_min16 when the test fails, G2, and the **all-classes check** against the 1,630 R7 classes and the 1,640 dataset classes.
   - T-023 on F_c and F: N*_c, D_c, N_deep, maxdepth, T_deep, T_depth, V_int, b₁_deep, the class, plus the diagnostics hub degree, cut width and old b₁/N_int.
   - **Reported per finalist:** **D_c (headline)**, D, D_P, D_area, maxdepth, N_deep, T_deep, T_depth, the class, N*, N*_P, N*_c, |w̄|, ρ_min16, novelty, conjugator lengths and the |v| mix. D_path only for path-like finalists (provenance rule: they cap at L1).

## Hypotheses (falsifiable)
- **H1, growth (falsifier first).** At least one seed lineage reaches ≥ 20 growth steps (N ≳ 40). **Falsified** if growth stalls within 5 steps at every seed. Then report and stop.
- **H2, primary (owner's success criterion).** At least one certified L1, novel (G2 + all classes) finalist has **maxdepth ≥ 2 and T_deep ≥ 0.5** on the compressed certificate, which would be the first such B(2,5) word. **Falsified** otherwise.
- **H2a, deep cells at all (finding threshold, owner).** At least one deep cell (N_deep ≥ 1, on the compressed certificate) appears by N ≈ 30 in at least one seed lineage. **Falsified** if no lineage has a deep cell at N ≤ 30. That is recorded as a finding about the |v| ≤ 7 presentation (deep cells are not reachable by patch growth at that size), and the run continues to the step limit to see whether depth appears later.
- **H3, area-like.** At least one finalist is classified area-like (T_deep ≥ 0.5, T_depth ≥ 0.5). Reported; **falsified** if none.
- **H4, D tracked, prediction.** No finalist reaches D_c ≥ 1 (Math Expert's sizing: about 1,300 cells needed). **Falsified (a surprise)** by any such word, which then goes to Validator for an independent L0 re-check and a cheaper-certificate search before any claim. The best D_c is reported against the references T-003 (about 0.11–0.12) and E1c (0.167).
- **H5, L0.** 100% of finalist certificates pass the independent L0 check. **Falsified** by one failure.
- **H6, novelty.** At least 90% of L1 finalists are novel under G2 + all classes. **Falsified** below 90%.

Reported, not hypotheses:
- the patch library;
- the stall rate per step;
- maxdepth, T_deep, T_depth, D and D_c against N, with the observed exposure e per boundary cell to check the sizing conjecture |w̄| ≈ 4√N·e;
- beam against greedy;
- compressed against raw statistics.

## Success criteria (owner)
- **T-018 success:** H2, the first L1-certified, novel B(2,5) word with maxdepth ≥ 2 and T_deep ≥ 0.5 on the compressed certificate. It goes to Validator (L0 re-check, grid-identity and depth review) before any claim.
- **D thresholds** (L2: D ≥ 1) are read on the headline D_c (pure set), with D, D_P and D_area alongside. They are not expected to be reached (H4).
- **Finding** (not failure) if no deep cell appears by N ≈ 30 across seeds (H2a).

## Execution and cost
- **Local VM first:** calibration, the patch library and a smoke run with 20 seeds and 15 steps, timed.
- The full run is 200 seeds × 60 steps; its cost is estimated from the smoke. If it exceeds about 2 h on the VM, the rjob/Mac plan goes to Lead first, as in T-003.
- **Code:** a new module `experiments/challenge_gen/t018/` on a b25 branch off main after PRs #12 and #13 are merged (`patches.py`, `search.py`, `eval_diagrams.py`), with tests:
  - the attachment identity: the new boundary equals the expansion of F';
  - each of the four gates;
  - the step-0 controls.
- Depth statistics come from T-023; no changes to T-023, the harness or the workflow.

## Anti-pattern check
- **Calibration before results:** step 0 (depth controls, negative controls, D_c reproduction) is a hard gate.
- **One headline:** D_c, with every other D in its own column. Depth statistics are the success criterion, not a D.
- **Compressed first:** depth and J are computed on the compressed reduced certificate, so tiny triangles in uncompressed chains cannot fake depth.
- **L1 by construction is still re-certified** by the harness (all 16 images) on finalists.
- **Novelty:** G2 plus the all-classes check against both tables.
- **Thresholds 0.5 are conjectured** (Math Expert); they are stated before the run and not tuned afterwards.

## Related material
- [[2026-10-14-cancellation-constructions]] (ideas 2 and 3) · [[2026-10-14-area-vs-path-criterion]] · [[2026-10-14-vertex-depth-criterion]]
- [[t016-overlap-chaining-2026-10-14]] (triangle census; E1d)
- [[challenge-gen-success-metrics]] · [[challenge-gen-glossary]] · [[project-challenge-gen]]
- [[B25/Structured Constructions/_type|Structured Constructions]]

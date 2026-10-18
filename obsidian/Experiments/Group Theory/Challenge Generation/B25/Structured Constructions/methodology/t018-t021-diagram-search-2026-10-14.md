---
title: t018-t021-diagram-search-2026-10-14
hypothesis: "A search over van Kampen diagrams that attaches 2–3-cell patches of standard relators v^5 (|v| <= 7, b25_full) while keeping the boundary 2.5-power-free produces the first certified L1, novel B(2,5) word with a genuinely deep folded diagram (maxdepth >= 2 and T_deep >= 0.5 on the compressed certificate). D and D_c are tracked but not expected to reach 1."
status: rejected
closed: 2026-10-17
author: asetlearning
date: 2026-10-14
todo: T-018, T-021
project: challenge-gen
instance: B(2,5)
experiment_type: structured-constructions
tags: [agent/exp, user/asetlearning, domain/group-theory, topic/burnside, topic/b25, topic/trivial-words, topic/hard-instance-generation, topic/proof-certificates, topic/dehn-function, project/challenge-gen, status/rejected, experiment, methodology]
---

# T-018 + T-021: diagram search over |v| ≤ 7 with a power-free boundary

> [!summary] CLOSED 2026-10-17 (owner): hypothesis falsified (negative result). See [[#Conclusion (closed 2026-10-17)]]. The pre-registration and revisions below are kept as written.

> [!warning] DEFINITION CORRECTION 2026-10-17 (owner): the target is **2.5-reduced** (no power with exponent > 2.5; exact 2.5-powers allowed). Every T-018 gate ("power-free", the exposure rule ⌈2.5|v|⌉) used the stricter "no exponent ≥ 2.5". **Re-checked 2026-10-17** ([[#Re-check under the corrected gate (2.5-reduced), 2026-10-17]]): the negative **stands for L1 words**. The corrected gate lets the B0+N arms reach strict depth 2, but only on words the reducer collapses (non-L1), and no L1 word reaches strict depth ≥ 2. See [[challenge-gen-success-metrics#Owner decision 2026-10-17: the target is 2.5-reduced (no power with exponent > 2.5); exact 2.5-powers are allowed]].

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
- **Revision 6 (owner 2026-10-16): strict depth S2 adopted** (section 'Strict-depth decision'); area-like rule, H2 and J read strict depth; D thresholds on D_c,≥2.
- **Revision 5 (APPROVED, owner 2026-10-16)**: seeds from certified power-free dataset words (section below), with the seed split; the relaxed-seed route is not needed.
- **Revision 4** (owner 2026-10-15): final area-like rule, depth-sum J and maxdepth-vs-N logging (section below). Amended the same day after Validator's verdict: maxdepth ≥ 2 is required for area-like, and the wrapped-relator gate is replaced by the exact conjugacy test plus a G* diagnostic.

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
- **area-like** iff N ≥ 16, T_deep ≥ 0.5, T_depth ≥ 0.5 and **maxdepth ≥ 2** (amended after Validator's verdict [[2026-10-15-final-area-rule-and-wrapped-guard]]; deep_core is reported). The label is a diagnostic, and the evidence is H2 plus the maxdepth-vs-N fit; **small enclosed** iff N_deep ≥ 1 and N < 16; **thick strip** iff N_deep ≥ 1, N ≥ 16 and not area-like; path-like iff N_deep = 0.
- **Novelty adds the exact test:** w cyclically equal to a rotation of a table relator or its inverse means not novel. It is applied with the finalist novelty checks. **"Enclosed relator (modulo ring)"** (Validator's G*) is reported per finalist as a diagnostic, never as a gate. The earlier wrapped-relator gate is withdrawn.
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
  - **747** are primitive v⁵ (corrected 2026-10-15 by Experimenter's count, owner-confirmed; earlier text said 795, with |v| = 1…7 contributing 2, 2, 8, 21, 64, 178, 520, and that per-|v| split is superseded).
  - **68** are multiples v^{5k} (k ≥ 2) of roots with |v| ≤ 3: 52 of 1-letter roots, 12 of 2-letter roots, 4 of 3-letter roots (earlier text said 20).
- **Tables:**
  - **Move table:** the 747 primitive v⁵ and their inverses (**1,494**; corrected from 1,590). Patches use only these. Cells use the cyclic core, with conjugator q·core[:a], because some table relators are stored as q u⁵ q⁻¹.
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

## Strict-depth decision (owner 2026-10-16): S2 adopted; the record is corrected
**Adopted reading S2.** Trivial cells (root length |v| = 1, a⁵ = 1) are absorbed into the exterior whenever they touch it (vertex contact counts), repeated after every layer. Metrics: **T_deep and T_depth over the full N** (the N_≥2 variant reported alongside); headline **N_≥2 and D_c,≥2**; the area-like rule, H2 and J use strict depth (**J = (Σ strict depths + 0.25·V_int)/|w̄|**); D thresholds are read on D_c,≥2; root length 2 is reported separately; S1 and S3 are sensitivity columns (definitions in the section 'Strict-depth check' below; implementation `t018/scripts/strict_depth.py`). Exponent normalisation and strict depth are added to the C++ port, and the first comparison is B0 against B0+N.

**The record, stated plainly.**
- **There is no H2 result.** The only candidate (line 51, steps 9 and 10) has strict maxdepth 0: its depth 2 was an a⁵ shield.
- **No word is strictly area-like under S2.** Line 48 is the only certificate with strict maxdepth ≥ 2 (inherited from the seed, not created by growth); it would pass under the N_≥2 normaliser (T_deep 1.15) but not under the adopted full-N one (T_deep 0.31 < 0.5, T_depth 0.62, maxdepth 2); the L48 finalists likewise (0.26 / 0.24). None of the 11 certificates passes all three area-like conditions (Validator recomputed the same numbers, [[2026-10-16-t018-area-like-dataset-words-check]] Part 3b).
- **D_c ≥ 1 was an artefact of |v| = 1 cells** (line 48 finalists: D_c,≥2 = 0.49 under S2).
- Detail: with T_deep and T_depth over the **full N** (the adopted reading) line 48 and its finalists are not area-like under S2; they are area-like only with the N_≥2 variant (T_deep 1.15 / 0.88 / 0.83). Table (S2, compressed cyclic-core certificates, Validator's cheaper certificates where they exist):

| certificate | N | N_≥2 (D_c,≥2) | maxdepth / N_deep | T_deep / T_depth (full N) | area-like (full N) | T_deep / T_depth (N_≥2) | area-like (N_≥2) |
|---|---|---|---|---|---|---|---|
| line36 | 33 | 20 (0.39) | 1 / 6 | 0.43 / 0.42 | no | 0.98 / 0.58 | no |
| line17 | 28 | 12 (0.26) | 1 / 2 | 0.18 / 0.47 | no | 0.93 / 0.81 | no |
| line13 | 38 | 19 (0.45) | 1 / 9 | 0.52 / 0.39 | no | 1.62 / 0.60 | no |
| line21 | 42 | 21 (0.45) | 1 / 5 | 0.25 / 0.36 | no | 0.75 / 0.56 | no |
| line49 | 45 | 20 (0.38) | 1 / 4 | 0.18 / 0.35 | no | 0.65 / 0.58 | no |
| line48 | 55 | 23 (0.44) | 2 / 9 | 0.31 / 0.62 | no | 1.15 / 1.05 | yes |
| L51-step9-n51 | 37 | 23 (0.45) | 0 / 0 | 0.00 / 0.00 | no | 0.00 / 0.00 | no |
| L51-step10-n53 | 39 | 24 (0.45) | 0 / 0 | 0.00 / 0.00 | no | 0.00 / 0.00 | no |
| L48-step4-n55 | 63 | 27 (0.49) | 2 / 9 | 0.26 / 0.58 | no | 0.88 / 0.95 | yes |
| L48-step5-n57 | 65 | 28 (0.49) | 2 / 9 | 0.24 / 0.57 | no | 0.83 / 0.93 | yes |

**Superseded statements.** Everything below that reads depth, area-like, D_c or H2 on the *standard* (non-strict) depth is superseded by this section and kept for the record: the 'Finding: power-free dataset words' list of 6 (or 7) area-like words, the smoke-run H2 bullet (line 51), the 'area-like seeds (depth kept vs grown)' bullet, the H4 flag (D_c ≥ 1), and Revision 5 item 4's seed split (which was defined on standard depth). The registered seed split (22 / 7) is kept for continuity only.

## Step-0 seed findings (Experimenter, 2026-10-15)
**1. No power-free 2- or 3-cell seed patch exists** over the 1,494-entry move set (|v| ≤ 7, primitive roots). Exhaustive, on t018-diagram-search@4349ba3: 2-cell patches 0 reach the needed arcs; triangles 0 of 231,000 anchor pairs reach a third cell meeting the Fine–Wilf bounds (60 of 343 length triples feasible); chains 235.1M candidate triples, 87M pass the exposed-run test, 0 power-free (about 41 CPU-min). Caveats: the triangle path never reached its last stage even with the bounds weakened by 3, so it has no positive control (its third-cell lookup matched the sampler on 12,990 of 12,990 triangles); the chain path does; the |v| = 1 chains are script-only; **Validator replicated the conclusion** ([[2026-10-15-t018-seed-reachability-review]]): 2-cell 0; chains 108 identical plus 48 nested; triangles plus lenses 383,760 candidates, 0; so 'no power-free seed at N ≤ 3' is safe to build on. **Caveat: do not cite the 60/343 length-triple pruning as complete.** My triple test assumes one arc per pair, so it misses lens triangles (two cells sharing two arcs with a third glued between them; 22 more length triples have real matches) and silently skips nested end cells. No re-run is needed for the conclusion.

**2. Constructive test (owner step 1): power-free relations over R7 exist.** `hardness/powerfree.py has_power_cyclic` (all periods h, exact windows ⌈2.5h⌉) on the 820 dataset words: **492 are cyclic power-free** (lengths 32 to 123; shortest 32, 2 words of length 32). 491 of the 492 reduce to IdWord under the `rec` kbprog system on `b25_full` (sha b1d511fe…ba32ee, the same file as the R7 table, 815 equations v^(5k), |v| ≤ 7). The remaining one is dataset line 431, the known miss. Every kbprog rule is a consequence of the R7 relators, so these 491 words are trivial in G₇ = ⟨a, b | R7⟩, hence **have an R7 certificate in the existence sense**. The negative controls (0 of 825) were recorded in kb-verify-20261007. Likewise the recomputed R₂.₅ outputs: T-016 E1c 147 of 161 L1 words give a power-free R (all 147 trivial in G₇), E1d 85 of 201 (85), E1_screen 131 of 145 (131); T-002 L1 words with certify cost ≤ 20 s: 1,571 of 5,121 give a power-free R (1,185 distinct, lengths from 32), 1,567 trivial in G₇ (the other 4 are not decided by `rec`); the 100 costliest T-002 words (> 20 s, about 2.6 CPU-h) were not recomputed. **Not yet available: an explicit R7 certificate (cell list, N).** kbprog keeps no derivations, so N is unknown. This is b₂ settled constructively (a power-free relation in N(R7) exists); it says nothing about the area of the certificate.

## Finding: power-free dataset words with R7 certificates (dataset words, NOT novel; Experimenter, 2026-10-16)
Of the 820 dataset words, 492 are cyclic power-free and 491 are trivial in G₇ under the `rec` kbprog system on `b25_full` (see Step-0 seed findings). I turned the rewriting paths into explicit certificates (`t018/kbcert.py`, branch t018-diagram-search): each used rule l → r is certified on its own by a search of 2.5-moves of period ≤ 7 (each move is one R7 cell), the rule certificates are composed along the rewriting path, and the product is re-expanded and compared with the word (independent L0). The best of 16 rotation/inversion variants is kept, and the diagram statistics are computed on the compressed reduced certificate F_c over the **core table** (the cyclic cores of the 1,630 entries; see the note below).
- **Re-run on main 714caa9 (fold converts cyclic cores itself):** statistics of all 29 seeds are unchanged, raw table equals core table (0 mismatches of 29; `core_converted_c` 4 to 9 cells per seed). The kbcert core conversion is now optional.
- **Words ≤ 53 letters: 29 of 30 certified** (line 41 not certified: all 16 variants needed a period > 7 rule; not a statement about triviality). All 29 pass the standard guard.
- **Power-free does not force depth.** Lines 1 and 3 (32 and 33 letters) are path-like with N*_c 4 and 11 and maxdepth 0.
- [SUPERSEDED by § Strict-depth decision: standard depth] **But it does not forbid it either: 7 of 29 certificates were area-like; Validator's check ([[2026-10-16-t018-area-like-dataset-words-check]]) leaves 6.** It replicated L0 and found cheaper certificates (line 17: 34 → 28 cells, 47: 40 → 24, 13: 41 → 38, 49: 49 → 45, 48: 56 → 55). **Line 47 loses the label** with its 24-cell certificate (maxdepth 1, thick strip); line 48 reaches maxdepth 3 with D_c 1.06. So the area-like dataset words are lines 36, 17, 13, 21, 49, 48 (6), and **'area-like' is a property of a certificate, not of the word**. The N*_c and depth values in the table are those of my first certificates.
- **Caveat (upper bounds).** N*_c is an upper bound on the area, never the area; my certificates are not minimised, and a different certificate of the same word can have different depth statistics. The words are dataset words, so none counts for the success criterion or H2 (not novel).

| line | |w| | N raw | N*_c | D_c | maxdepth | N_deep | class |
|---|---|---|---|---|---|---|
| 1 | 32 | 28 | 4 | 0.125 | 0 | 0 | path-like |
| 3 | 33 | 63 | 11 | 0.333 | 0 | 0 | path-like |
| 39 | 51 | 94 | 14 | 0.275 | 1 | 1 | small enclosed |
| 28 | 49 | 100 | 16 | 0.327 | 1 | 1 | thick strip |
| 23 | 48 | 107 | 17 | 0.354 | 1 | 1 | thick strip |
| 44 | 52 | 53 | 17 | 0.327 | 0 | 0 | path-like |
| 62 | 53 | 97 | 17 | 0.321 | 1 | 1 | thick strip |
| 12 | 41 | 123 | 19 | 0.463 | 0 | 0 | path-like |
| 35 | 50 | 33 | 19 | 0.380 | 0 | 0 | path-like |
| 51 | 53 | 155 | 19 | 0.358 | 1 | 1 | thick strip |
| 63 | 53 | 170 | 20 | 0.377 | 1 | 6 | thick strip |
| 42 | 51 | 190 | 23 | 0.451 | 1 | 2 | thick strip |
| 22 | 47 | 180 | 24 | 0.511 | 1 | 6 | thick strip |
| 40 | 51 | 77 | 25 | 0.490 | 0 | 0 | path-like |
| 52 | 53 | 198 | 25 | 0.472 | 1 | 2 | thick strip |
| 20 | 47 | 117 | 30 | 0.638 | 1 | 9 | thick strip |
| 2 | 32 | 77 | 31 | 0.969 | 1 | 10 | thick strip |
| 18 | 46 | 82 | 32 | 0.696 | 1 | 10 | thick strip |
| 36 | 51 | 99 | 33 | 0.647 | 2 | 14 | area-like |
| 57 | 53 | 159 | 33 | 0.623 | 1 | 6 | thick strip |
| 17 | 46 | 98 | 34 | 0.739 | 2 | 12 | area-like |
| 34 | 50 | 118 | 34 | 0.680 | 1 | 11 | thick strip |
| 47 | 52 | 144 | 40 | 0.769 | 2 | 18 | area-like |
| 13 | 42 | 113 | 41 | 0.976 | 2 | 25 | area-like |
| 21 | 47 | 108 | 42 | 0.894 | 2 | 18 | area-like |
| 43 | 51 | 122 | 42 | 0.824 | 2 | 7 | thick strip |
| 49 | 52 | 144 | 49 | 0.942 | 2 | 20 | area-like |
| 64 | 53 | 154 | 52 | 0.981 | 1 | 13 | thick strip |
| 48 | 52 | 98 | 56 | 1.077 | 2 | 24 | area-like |

**Core table.** 1,080 of the 1,630 `b25_full` entries are not cyclically reduced (written as products such as (Bab)⁵ that are not even freely reduced). Folding such a cell gives a spur and self-shared edges: over the raw table the Euler check b₁ = V_int fails (b₁ = 52, V_int = 22 on line 1's F*_P). The **core table** (cyclic core of each entry, classes unchanged, cell (k, c) → (k, q⁻¹c) with fr(R_k) = q·core·q⁻¹) passes. Diagram statistics, J and N*_c use the core table; classes, the guard, novelty and the move set are unaffected. Developer to confirm, Validator to check.

## Revision 5 (APPROVED, owner 2026-10-16): seeds from certified power-free dataset words
Replaces steps 1 and 2 of Method (the 2-/3-cell patch library as a seed source). Reason: no power-free 2- or 3-cell patch exists (Step-0 seed findings), but power-free relations with explicit R7 certificates do (finding above).
1. **Seed source.** The 29 certified power-free dataset words of length ≤ 53 (table above), each with its compressed certificate F_c over the core table. One lineage per word (no random library, no stratification; seed 18000001 kept for tie-breaking). If wanted later: the remaining power-free dataset words (up to 123 letters) by the same method.
2. **Seeds need not be novel.** They are dataset words. A finalist must satisfy the full finalist checks (G2 + all classes + `novelty.conjugate_to_relator` on R7 and the dataset classes) and must differ from its own seed: **the seed state itself is never a finalist**, and any state that is still the seed's cyclic word or a conjugate of a dataset word fails novelty as usual.
3. **Growth, gates and objective unchanged:** patch attachment (2-/3-cell patches from the library of Method step 1 serve as attachments only), gates in order 2, 1, 4, 3, half-exposure, exact boundary power test, final area-like rule, J = (depth_sum + 0.25·V_int)/|w̄| on the compressed certificate, beam 100, at most 60 growth steps, standard_guard with NOVELTY_CHECKS on finalists. Diagram statistics use the **core table**.
4. [defined on standard depth; superseded for H2 by § Strict-depth decision] **Seed split (owner 2026-10-16).** Seed from all 29 words, but **H2 (success) counts ONLY lineages from the 22 seeds that are not area-like**, where growth must create the depth. Lineages from the 7 area-like seeds (lines 36, 17, 47, 13, 21, 49, 48 as registered; Validator's cheaper certificates make line 47 a thick strip, so 6 are area-like by certificate, and the split is kept unchanged for now) are reported separately as "depth kept vs grown" (maxdepth and N_deep of the best novel finalist against the seed's; steps to the first novel area-like state). A seed is never a finalist.
5. **Falsifier / logging:** unchanged (maxdepth at every N per lineage, log N against √N fit across lineages). The lineages now start at N*_c 4 to 56, so the fit is done on N reached, not on steps.
6. **H1–H6 unchanged**, except that the seed-count wording in H1 ("200 seeds") reads "29 seeds". Step-0 controls (grid/ladder depth, negative controls, D_c reproduction at N*_c 7 and D_c 0.167, hand-built positive control) are still to run on the merged code and the core table before anything else; nothing has been run on the search itself.
7. **Cost.** Seed certification took ~2 min for 29 words on 2 cores under capjob. The search cost estimate comes from the smoke run.

## Step 0 and smoke run (Experimenter, 2026-10-16; branch t018-diagram-search @ 2415091+; main 714caa9)
**Step 0 (all pass).** Depth controls: Developer's `test_diagram.py` + `test_guard.py` 72 of 72 (grid identity, ladders, hexagon, classification of the 5×5 grid and the 3×20 ladder). D_c reproduction: E1c top-0 gives N*_c 7, D_c 0.1667 (E1d top-0 9 / 0.145, E1_screen top-0 5 / 0.119). Negative controls over all 611 T-016 samples (E1c 204, E1d 204, E1_screen 203): max maxdepth 1, 0 area-like, 0 words with N_deep ≥ 2 and N ≥ 16. Positive control (Math Expert's (ab)⁵ + (aab)⁻⁵ sharing "aba"): reduced 2-cell diagram, gates 3 and 4 accept, gates 1 and 2 reject it as a stand-alone seed (recorded characterisation). Generator completeness: every gate-1 attachment found among 40,000 random library patches on seeds 17, 39, 51 is in the vertex generator's output. Seed statistics unchanged on main (0 of 29 mismatches).

**Design change forced by the data (attachments).** The random 2-/3-cell patch library of Method step 1 is useless for this gate set: for seed line 1, a 200,000-patch library gave 4 half-exposure passes in 2·10⁶ site examinations, and none was power-free. A cell glued along a short segment exposes almost all of its 5|v| letters. Attachments are therefore **generated exhaustively relative to the boundary** (`vertex_gen.py`): at a vertex j of w, cell A shares an arc with w after j, cell B an arc with w before j, A and B share an arc from j, all arcs maximal, necessary condition 2(s+l) ≥ 5|v| for each cell. The admissible set is still defined by the gates, so this only replaces sampling by enumeration. **Not yet included: 3-cell (triangle) patches.** Gate order evaluated 1, 2, 4, 3 (a conjunction, so only the cost changes).

**Smoke run (29 seeds, 15 steps, beam 100, ≤ 5 states per lineage, capjob 2 GB / 2 cpus).** The search **stalls at step 11** (all lineages dead), so the 15-step cap is never reached.
- 18 of 29 lineages never grew (seed lines 1, 2, 3, 12, 13, 18, 21, 22, 23, 28, 34, 35, 39, 40, 42, 43, 57, 64): no admissible attachment. 11 grew: lines 51 (10 steps), 48 (6), 62 (6), 47 (4), 63 (4), 44 (2), 17, 20, 36, 49, 52 (1 step).
- Over the run 718 attachments examined (2 to 10 per state): gate 2 (power) rejected 473, gate 4 rejected 75, gate 3 rejected 29, gate 1 0 (the generator already satisfies it), leaving 141 scored children.
- Cost: wall 302 s on one core (seeds 61 s, search 241 s), peak RSS 59 MB. Scoring (compress + diagram stats) 1.28 s per scored state, gate 3 0.47 s per call, everything else negligible. **Full-run estimate: about the same, 5 to 6 minutes, because the search ends by stall, not by the step limit; no rjob needed.**
- Finalists (49; top by J, per-lineage best, max-maxdepth, step marks; seeds never): all 49 exactly power-free, ρ_min16 = 1.0 for all 49 (real reducer, 16 images), all pass the standard guard. 25 hit a dataset class (not novel), 24 novel; 17 area-like, of which **5 are novel and area-like**.
- [SUPERSEDED by § Strict-depth decision: the line-51 depth was an a⁵ shield, strict maxdepth 0; there is no H2 result] **H2 (22 non-area-like seeds): one lineage creates depth** (read as: *a certificate with maxdepth 2 exists*; Validator replicated L0 and found no cheaper certificate for line 51 at steps 9 and 10, [[2026-10-16-t018-area-like-dataset-words-check]]). Line 51 (seed thick strip, N*_c 19, maxdepth 1) reaches at steps 9 and 10 novel area-like words: |w| 51 / 53, N*_c 37 / 39, D_c 0.725 / 0.736, maxdepth 2, N_deep 12, T_deep 0.72 / 0.67, T_depth 0.79 / 0.76, deep_core 12, enclosed_relator False. Lines 44, 62, 63, 20, 52 grow (novel words) but stay maxdepth ≤ 1.
- [SUPERSEDED by § Strict-depth decision] **Area-like seeds (depth kept vs grown):** lines 47 and 48 give novel area-like words at maxdepth 2 (the seed's depth, kept; N*_c 46 / 64 / 66, D_c 0.82 / **1.16** / 1.16). Lines 17, 36 and 49 grow one step but only to non-novel states.
- [SUPERSEDED by § Strict-depth decision: D_c ≥ 1 was an artefact of |v| = 1 cells] **H4 flag (upper bound only):** two novel finalists from line 48 (steps 4 and 5, from an area-like seed whose own D_c is 1.077) have D_c 1.164 and 1.158 (N*_c 64 and 66 on 55 and 57 letters). Validator found cheaper certificates (63 and 65 cells), D_c still 1.15 and 1.14, **an upper bound only; no claim that the area is ≥ |w|.** H4 says D_c ≥ 1 goes to Validator for an independent L0 re-check and a cheaper-certificate search before any claim; N*_c is an upper bound.
- maxdepth-vs-N fit (pooled, 66 points): log a = −2.13, b = 1.00, SSE 9.48; √N a = −0.93, b = 0.394, SSE 8.91; √N slightly better, not conclusive; per lineage 23 of 29 undetermined (too few points).
- **Greedy reference (beam 1, 15 steps, 337 s, RSS 61 MB):** unlike the beam it does not stall: line 51 survives all 15 steps and line 62 14 steps. Line 51 gains **+2 cells per step at an almost constant boundary** (N*_c 39, 41, 43, 45, 47, 49 at |w| = 53, 51, 53, 51, 53, 51; maxdepth 2, area-like at every step). That pattern means either a genuine linear growth of the area at fixed boundary length (impossible for a fixed finite set of words, but these are always new words) or, more likely, **non-minimal certificates** (each step adds cells that a cleverer certificate would cancel); N*_c is an upper bound. It is a reason to run Validator's cheaper-certificate search on these words before any D_c claim (H4), and to expect the beam's N*_c and D_c to be inflated. The beam died earlier than the greedy run because ≤ 5 states per lineage ranked by J are not the states that survive longest; a longer beam (more states per lineage) is a cheap next step.

## Pre-registered addenda to Revision 5 (owner 2026-10-16; written before the full run)
1. **Recorded deviation from Method step 1 (random patch library).** Attachments are generated **exhaustively relative to the boundary** (`vertex_gen.py`, `triangle_gen.py`) instead of sampled from a random library. Reason (smoke data): for seed line 1 a 200,000-patch library gave 4 half-exposure passes in 2·10⁶ site examinations, none power-free, because a cell glued along a short segment exposes nearly all of its 5|v| letters. The admissible set is still defined by the registered gates; only the way candidates are found changed. Completeness checks: (i) every gate-1 attachment among 40,000 random 2-cell library patches on seeds 17, 39, 51 is generated (test `test_vertex_gen_contains_every_gate1_attachment_of_a_random_library`); (ii) the far-corner windows of the triangle generator agree with a brute-force search over all cells C (1,500 relaxed pairs, non-vacuous); (iii) every generated attachment re-attaches and keeps the certificate identity. **Documented incompleteness:** the 2-cell family requires the shared arc of A and B to start at the attachment vertex (s adjacent to a corner of the patch) or B to be a cap on A's exposed run (`CapGen`); triangles are generated as a relaxed (A, B) pair plus a third cell C glued along the maximal periodic run across the far corner; triangles whose site also touches C and chains with s on the middle cell only are not generated. Library completeness tests on sampled patches are weak for long arcs (the sample rarely contains them), so (i) is evidence, not proof.
2. **3-cell (triangle) attachments added** (family above), restoring the registered 2–3-cell method. On the 29 seeds the triangle family produces about 10⁵ candidates per state and, on the seeds examined, 2 gate-1 passes and 0 power-free (see results).
3. **Beam addendum: the per-lineage state cap is raised from 5 to 20.** Beam 100, 60 steps, the gates, J, the final area-like rule, standard_guard with NOVELTY_CHECKS, the cyclic-core statistics and the 22/7 seed split (line 47 kept in the area-like group) are unchanged. Reason: the smoke run with cap 5 stalled at step 11 while the greedy run (one state per lineage) kept lines 51 and 62 alive to steps 15 and 14, so the cap ranked by J, not the gates, ended the beam. The cap of 20 was fixed before the run and is not tuned afterwards.
4. **Reporting additions (Lead, 2026-10-16):** (a) classify the power-gate failures (the smoke run's 473 and the full run's) as half-exposure, a shorter-period power inside a run, or a power across a junction; (b) an R8 cost estimate with a draft design (separate note). Pre-filters must count arcs **and contact points** (≥ 2 separate attachments), never demand 2 arcs (Validator's correction of the R8/R9 appendix).

## Strict-depth check and per-attachment failure breakdown (Experimenter, 2026-10-16; owner-approved, Math Expert § 7 R3)
**Definition implemented** (`t018/scripts/strict_depth.py`; independent of Validator's `strict.py`, which gives the same standard values). Cells are those of the compressed certificate over the cyclic-core table (Validator's cheaper certificates where they exist, `data/validator_certs/`). The **root length** of a cell is the length of the primitive root of its cyclic core (|core| = 5|v|). Vertex-depth peeling as in `diagram.depth_profile`: B = vertices on the outer boundary; a layer is the set of remaining cells that share a vertex with B; B then grows by their vertices.
- **S1 (strict depth, as written by Math Expert):** before peeling, every |v| = 1 cell that touches B is absorbed into the exterior (B grows by its vertices; the cell is removed and counts neither as a cell nor as depth), repeated to a fixed point (least fixed point, order independent); then peeling runs on the remaining cells.
- **S2:** as S1, with the absorption repeated after every layer, so a |v| = 1 cell never occupies a layer (stricter than the wording).
- **S3:** as S1 with |v| ∈ {1, 2} cells trivial (|v| = 2 reported separately, as asked).
- **Counting:** N_≥2 = non-absorbed cells (S3: |v| ≥ 3); D_c,≥2 = N_≥2/|w̄|; N_deep,strict = non-absorbed cells of depth ≥ 1; T_deep,strict = N_deep,strict/(√N_≥2 − 2)², T_depth,strict = maxdepth_strict/((√N_≥2 − 1)/2) (N_≥2 replaces N); deep_core = largest connected component (shared edge) of the strict deep cells. **Strict area-like** iff N_≥2 ≥ 16, T_deep ≥ 0.5, T_depth ≥ 0.5, deep_core ≥ 2, maxdepth ≥ 2.

**Result.** Columns: standard maxdepth / N_deep; S1 N_≥2 (D_c,≥2); S1 maxdepth / N_deep / T_deep / T_depth / deep_core; S1 area-like; S2 maxdepth / N_deep and area-like; S3 maxdepth / N_deep and area-like.

| certificate | N | \|w\| | std | S1 N_≥2 (D_c,≥2) | S1 md/N_deep/T_deep/T_depth/core | S1 AL | S2 md/N_deep | S2 AL | S3 md/N_deep | S3 AL |
|---|---|---|---|---|---|---|---|---|---|---|
| line36 | 33 | 51 | 2 / 14 | 26 (0.51) | 2 / 12 / 1.25 / 0.98 / 10 | yes | 1 / 6 | no | 2 / 12 | yes |
| line17 | 28 | 46 | 2 / 8 | 18 (0.39) | 2 / 8 / 1.59 / 1.23 / 6 | yes | 1 / 2 | no | 1 / 7 | no |
| line13 | 38 | 42 | 2 / 25 | 33 (0.79) | 2 / 23 / 1.64 / 0.84 / 21 | yes | 1 / 9 | no | 2 / 18 | yes |
| line21 | 42 | 47 | 2 / 18 | 32 (0.68) | 2 / 16 / 1.20 / 0.86 / 11 | yes | 1 / 5 | no | 2 / 14 | yes |
| line49 | 45 | 52 | 2 / 16 | 24 (0.46) | 1 / 8 / 0.95 / 0.51 / 6 | no | 1 / 4 | no | 1 / 3 | no |
| line48 | 55 | 52 | 3 / 29 | 39 (0.75) | 2 / 25 / 1.39 / 0.76 / 18 | yes | 2 / 9 | yes | 2 / 24 | yes |
| L51-step9-n51 | 37 | 51 | 2 / 12 | 23 (0.45) | 0 / 0 / 0.00 / 0.00 / 0 | no | 0 / 0 | no | 0 / 0 | no |
| L51-step10-n53 | 39 | 53 | 2 / 12 | 24 (0.45) | 0 / 0 / 0.00 / 0.00 / 0 | no | 0 / 0 | no | 0 / 0 | no |
| L48-step4-n55 | 63 | 55 | 3 / 36 | 46 (0.84) | 2 / 28 / 1.22 / 0.69 / 18 | yes | 2 / 9 | yes | 2 / 27 | yes |
| L48-step5-n57 | 65 | 57 | 3 / 38 | 47 (0.82) | 2 / 28 / 1.19 / 0.68 / 18 | yes | 2 / 9 | yes | 2 / 27 | yes |

- **The H2 candidate does not stand under strict depth.** Line 51 (steps 9 and 10, the one novel area-like word from a non-area-like seed) has **strict maxdepth 0 and no deep cell** under S1, S2 and S3: 14 and 15 of its 37 and 39 cells are |v| = 1 cells absorbed into the exterior, and all the rest touch the boundary. Its standard depth (maxdepth 2, N_deep 12; deep cells of root length 1: 3, 3: 6, 4: 2, 7: 1) came from the |v| = 1 shields. Under strict depth **H2 has no lineage from the 22 non-area-like seeds**.
- **Area-like dataset seeds:** S1 keeps lines 36, 17, 13, 21, 48 area-like (maxdepth 2) and drops line 49 (maxdepth 1); S2 keeps only line 48 (maxdepth 2, N_deep 9); S3 keeps 36, 13, 21, 48.
- **Line 48 finalists (steps 4 and 5, 63 and 65 cells):** area-like under S1, S2 and S3 (maxdepth 2, N_deep 28 / 9 / 27); the |v| = 1 cells are 17 and 18 of the 63 and 65 under S1, 36 and 37 under S2. D_c,≥2 = 0.84 / 0.82 (S1) and 0.49 (S2), below 1: the D_c ≥ 1 reading of the standard count is carried by |v| = 1 cells.
- **Root-length mix** is in the JSON (`data/strict_depth_results.json`, fields `root_mix_all`, `root_mix_deep`): |v| = 1 cells are 38 to 58% of the cells of these certificates, and among the standard deep cells |v| = 1 are 3 of 12 (line 51), 7 of 14 (line 36), 23 of 36 (line 48 step 4).
- Caveats: smoke size; certificates are the best known (upper bounds); S1, S2 and S3 are three readings of "strict", the metric change is the owner's decision.

**Per-attachment breakdown of the 473 smoke power-gate failures** (`data/smoke15/power_failure_fields.json`, pair family, 99 states). A run is *m = 1* (rescued by syllable normalisation), *unrepairable* (exact half: even m and L = 2.5m; own root: m equals the root of an adjacent new cell; adjacent old root: m equals the root of an old cell owning a letter of the run or its two neighbours; new field `m_equals_adjacent_old_root`), or *repairable* (m ≥ 2, none of these). Per attachment: **all runs m = 1: 154 (32.6%)**; **no unrepairable run, some m ≥ 2: 232 (49.0%)**; **at least one unrepairable run: 87 (18.4%)**. Reasons among the 87 (not exclusive): exact half 55, own new-cell root 60, adjacent old-cell root 13. So normalisation alone would rescue at most a third of the failing attachments (the power test still has to pass afterwards), repair of m ≥ 2 runs a further half, and at most 18% are out of reach of any repair.

## Full R7 run (Mac job 20261016-130522-7373b4; Python reference; Experimenter, 2026-10-16)
Code `fc4e28c` (triangle and cap generators, per-lineage cap 20 as pre-registered), 29 seeds, 60 steps allowed, beam 100, then the greedy reference. Wall: beam 19 min, greedy 71 min on 9 cpus. Data `t018/data/full_r7_mac/{beam,greedy}/` (states, steps, summary, finalists, strict re-score). This is the large-scale Python reference for the C++ port.
- **Beam stalls at step 8** (7 steps run, 99 states, 18 of 29 lineages never grew; line 51: 7 steps, 48: 6, 62: 6, 47 and 63: 4, 44: 2, five lineages 1 step). It stops **earlier** than the cap-5 smoke run (step 11) and far earlier than the greedy run, which stalls at step 24 (line 51: 23 steps, 62: 14, 63: 8, 48: 6). The cap of 20 did not help: the J ranking keeps dead ends, so the ranking, not the cap, is the bottleneck.
- **Triangles and caps added no admissible attachment** (power-gate failures 480 in the beam against 473 in the smoke; the gate-1 rejections are the 16.2 million triangle candidates). Triangle generation took 1,792 s of about 3,000 s CPU, attach 3,574 s.
- **Standard-depth finalists (superseded, kept for the record):** beam 49 finalists, 24 novel, 15 area-like, 3 novel and area-like; greedy 47 finalists, 23 novel, 24 area-like, 14 novel and area-like. All exactly power-free, ρ_min16 = 1.0, all pass the guard.
- **Strict depth S2 re-score of every state** (`strict_rescore.json`): **no state of either run has strict maxdepth ≥ 2** (beam: strict maxdepth 0 in 60 states, 1 in 39; greedy 60 and 31; standard maxdepth ≥ 2 in 23 and 36 states). No state is area-like under S2 (full-N or N_≥2); under the sensitivity readings S1 15 (beam) and 13 (greedy) states are area-like and S3 13 and 11. Max D_c,≥2 0.53 (beam), 0.68 (greedy). Line 51's greedy lineage grows 2 cells per step to N = 65 with strict maxdepth 0 and no deep cell.
- **maxdepth against N:** pooled fits (standard / S2 full N / S2 N_≥2): beam sqrt better than log in all three (SSE 8.2 vs 8.8, 10.0 vs 10.5, 11.4 vs 11.7), greedy sqrt, sqrt, log (11.9 vs 12.7, 18.7 vs 18.9, 19.8 vs 19.9). The differences are small, r² ≤ 0.36 (beam) and ≤ 0.09 (greedy) on strict depth, 23 of 29 lineages have too few points: **no discrimination between log N and √N.**

**H1–H6 outcomes (strict depth S2 where depth is read).**
| | outcome |
|---|---|
| H1 growth ≥ 20 steps | **beam: not met** (best 7 steps; the falsifier clause 'stalls within 5 steps at every seed' is not triggered because lines 51, 48 and 62 pass 5); **greedy: met** (line 51, 23 steps, N up to 65–68), with strict maxdepth 0 along it |
| H2 novel finalist, maxdepth ≥ 2 and T_deep ≥ 0.5 | **falsified under strict depth** (no state has strict maxdepth ≥ 2); there is no H2 result |
| H2a deep cell by N ≈ 30 | strict deep cell (N_deep ≥ 1) in grown states at N ≤ 30: beam yes (6 states, lineage 63), greedy no; so met in the beam only |
| H3 area-like | **falsified under S2** (0 states); S1 and S3 give 13 to 15 states |
| H4 D_c ≥ 1 | **not reached** (max D_c,≥2 0.68); the earlier D_c ≥ 1 reading was an artefact of |v| = 1 cells |
| H5 L0 100% | holds (every certificate re-expanded and compared: 49 of 49 beam, 47 of 47 greedy finalists) |
| H6 ≥ 90% novel | **falsified**: 24 of 49 (beam) and 23 of 47 (greedy) finalists are novel; 25 and 24 hit a dataset class (growth from a dataset word often returns another dataset word) |

Reported: seed split (22 / 7) results have no H2 meaning under strict depth; the stall rate per step is in `steps.jsonl`; N*_c, D_c, J (standard) per state in `states.jsonl`; strict J in the re-score.

## R8 cost estimate and draft design (estimate only; nothing run; Experimenter, 2026-10-16)
**Counts** (`t018/scripts/r8_counts.py`: cyclically reduced primitive words up to rotation): primitive cyclic cores of length 1 to 9: 4, 4, 8, 18, 48, 116, 312, **810**, 2,184. R7 has 510 oriented cores (1,494 move entries with aliases, 1,630 table entries with the v^10 forms and inverses); **R8 adds 810 oriented cores (×2.6 → 1,320)**, **R9 adds 2,184 (×6.9)**. Window positions (Σ|v| over cores, the unit of the attachment index): R7 3,228, R8 9,708 (×3.0). A b25_full-style R8 file would have about 1,630 + 810 = 2,440 table entries with inverses; keep the R7 entries first so that every R7 certificate stays valid unchanged (seeds remain valid: their boundaries are power-free for all periods, and R7 cells are R8 cells; only the compressed counts N*_c can fall, because |v| = 8 relators can merge cells).
**Cost model, from the measured R7 numbers** (Mac job, VM smoke): strict pair-family generation 0.04 s per state; relaxed triangle generation 15 to 35 s per state (60% of the CPU of the beam); attach 20 µs per candidate; scoring (compress + diagram statistics) 1.3 s per admissible child; gate 3 0.5 s per call; 718 pair candidates and 141 admissible children over 99 states (19.6% pass, 1.4 children and 7.3 candidates per state); 11 of 29 seeds grow.
- Pair generation scales with branching at both cells: ×(2.6 to 3.0)² ≈ ×7 to ×9 → about 0.3 s per state, negligible.
- **Triangle generation ×9** → 2 to 5 minutes per state: not affordable in Python, and it gave zero yield at R7; keep it behind a switch and off for R8.
- Admissible children per state: ×(3 to 9) if the pass rate stays → 4 to 13 scored children per state; scoring then dominates: about 5 to 17 s per state in Python; at R7 smoke size (≈100 states per run) about 10 to 30 minutes per arm; a 60-step beam with up to 100 states per step 1 to 3 hours in Python, much less in C++.
- Memory: indexes ×3 (a few MB); no issue. The guard's closure and ≤ 2-cell test use the same table class sets (×1.6 hash), cost unchanged per call.
**Draft design (measurement list from Math Expert, with Validator's correction).** Same 29 seeds, same gates, same J on strict depth S2. Per table (B0 = R7, R8) at matched N: growing seeds; gate pass rate and attachments per step; maxdepth, N_deep, T_deep, T_depth and the log N / √N fit (strict); D_c,≥2, J, N*_c and D normalised by the mean root length; the share and role of |v| = 8 cells (in the certificates and in the deep cells); whether R8 finalists compress with the R7 table (the R7-compressed N*_c next to the R8 one). **Falsifier:** if the gate pass rate and the number of growing seeds rise by less than about 1.5×, the R8/R9 line stops. **Pre-filter rule (Validator):** any attachment or seed pre-filter counts separate attachments (arcs and contact points), never demands two arcs. **Caveats:** R8 finalists may not be trivial in G₇, so D is not comparable across tables; the comparison arms (B0, B0+N, JR, R8) are pre-registered after the C++ port, and run only on the C++ backend. The Python numbers above are the reference for the equivalence tests.

## Python-vs-C++ comparison harness and a property of the compression (Experimenter, 2026-10-16)
Harness `t018/compare_backends.py` (branch t018-diagram-search; backends in `backends.py` and `backends_cpp.py`): **replay** (every state of data/smoke15 and data/full_r7_mac through both backends: counters, children, certificates, all statistics, strict S1/S2/S3, compress, gates, exact comparison, plus the values stored with the state), **kernels** (wall time per kernel and per whole step), **e2e** (smoke configuration on both backends, states and finalists diffed, wall time and peak RSS normalised to MB). Tests inject faults (J at 1e-12, a certificate, a gate counter, a strict field) and all are detected. First result against the pre-rework M1 build (tcgraph f4d0140, b25 c26d69d, `tcgraph_ext.hardness` names, since replaced): power_free, gate_reduced and the compress pipeline agree exactly on 99 of 99 smoke15 states; speed-ups on 30 states: power_free 84×, gate_reduced 27.6×, compress with Python diagram statistics 7.8×. The adapter is retargeted to the reworked bindings (Word / reduction2_5 / pattern_boost, RelatorMap handle) when the Developer confirms the final names and SHAs.
**Property of the compression (Python and C++ alike): the compressed certificate is not idempotent.** Re-running `compress` (reduce_certificate, full_reduce, closure_fixpoint, shorter of the two pipelines) on a certificate that is already a compressed F_c can give a different F_c with different statistics: for the seed states of lines 57 and 64 the recomputed J, N_deep, T_deep, T_depth and V_int differ from the stored ones (J 0.170 vs 0.123 and 0.340 vs 0.231), identically in both backends. The stored statistics are therefore the reference only for states produced by the search from an uncompressed certificate, and N*_c, D_c and depth statistics are properties of *a* certificate, not of the word (consistent with Validator's finding that area-like is a property of a certificate).

## Pre-registration addendum for the C++ restart (APPROVED by the owner 2026-10-16, all four decisions as drafted; Experimenter; code: b25 t018-diagram-search at the commit Lead makes of the quota/F-N1 patch (SHA filled in at submission), cpp/tcgraph da7ac90; nothing has run yet)
Status: draft sent to Lead. Everything not changed here stays as registered (Method, gates, standard_guard + NOVELTY_CHECKS on R7, 29 seeds, 60 steps, seeds never finalists). Metrics follow the strict-depth decision (S2). The restart runs only on the C++ backend (tcgraph_ext, port M4/M5); the Python Mac run is the re-scored reference.

**1. Arms** (same 29 seeds, same R7 table, same gates, one process per arm and search mode):
- **B0**: baseline, strict J (S2). **B0+N**: B0 plus exponent normalisation: before the power test (gate 2) the new boundary w′ is normalised (exponents of a and b brought into {±1, ±2}, the a⁵ and b⁵ cells appended to the certificate as |v| = 1 cells, absorbed by strict depth). The admissible set of B0+N contains a normalised word w″ with w″ power-free; the other gates are evaluated on the certificate including the normalisation cells.
- **Search mode, per arm:** (i) beam (below), (ii) greedy (beam 1, as in the Python reference). So four runs: B0-beam, B0-greedy, B0+N-beam, B0+N-greedy.
- Not in this registration: JR (junction repair) and R8; they need their own registration after the C++ port (Lead 2026-10-16). Triangle and cap generators are **off** (zero yield at R7, 60% of the Python cost); the pair family is generated in Python and passed to the C++ expand_state (cfgs).

**2. J and statistics.** J = (Σ strict depths + 0.25·V_int)/|w̄| (S2), with the standard J as a switch only for the reference check below. Reported per state: N, N_≥2, D_c,≥2, strict maxdepth / N_deep / T_deep / T_depth (full N, N_≥2 alongside), deep_core, strict area-like (S2 full-N; S1 and S3 sensitivity), root mix; the standard values stay in the output, flagged superseded.

**3. Hypotheses on strict depth (H2 as decided; thresholds unchanged).**
- **H1 growth:** at least one lineage reaches ≥ 20 growth steps (N_≥2 ≳ 30) in some arm and mode. Falsified if none does.
- **H2 (success):** at least one certified L1, novel (G2 + all classes + conjugate_to_relator) finalist with **strict maxdepth ≥ 2 and strict T_deep ≥ 0.5** (full-N normaliser; N_≥2 variant reported alongside), reached by ≥ 1 growth step. Counted for lineages whose seed is not strictly area-like: under S2 full-N that is all 29 seeds (no seed is strictly area-like); the lineage of line 48, whose seed already has strict maxdepth 2, is reported separately as *inherited depth* (kept vs grown). *Decision for the owner: whether this replaces the registered 22 / 7 split (defined on standard depth).*
- **H2a:** a strict deep cell (N_deep ≥ 1, S2) appears by N_≥2 ≈ 30 in some lineage. Falsified otherwise (a finding about |v| ≤ 7).
- **H3:** at least one finalist strictly area-like (S2). **H4:** no finalist reaches D_c,≥2 ≥ 1 (falsified by one; goes to Validator for L0 re-check and a cheaper-certificate search). **H5:** 100% of finalist certificates pass the independent L0 check. **H6:** ≥ 90% of L1 finalists novel (the Python run found 49%, because growth from a dataset word often returns another dataset word; reported with the dataset-class hit rate).
- **F-N1 (normalisation falsifier, F-JR1 style):** B0+N against B0 at matched N, same seeds. Matched N = bins of N_≥2 of width 10 (10–19, 20–29, …), each lineage counted once per bin. Measured: gate pass rate (admissible children per examined candidate, pooled in the bin), growing seeds (lineages with ≥ 1 growth step), and attachments per state. **Falsified (normalisation is not a significant lever)** if both the pass rate and the number of growing seeds rise by less than about 1.5× over B0, in both search modes. If B0+N passes, the finding is that the power gate was largely fighting a⁵ = 1, recorded in its own right.
- Pooled **log N against √N fit** of strict maxdepth against N_≥2 (and against N), as before; reported, not decisive (the Python fits did not discriminate).

**4. Beam settings (what changes and why).** The Python results: cap 5 stalled at step 11, cap 20 at step 8, greedy at step 24 (line 51: 23 steps). The J ranking keeps dead ends, so more of the same ranking does not help. Registered change (needs owner approval): **per-lineage quota instead of the global J ranking** — each lineage keeps its own top q = 3 states by J (29 × 3 = 87 ≤ 100), ranking only within the lineage, so no lineage is crowded out by high-J dead ends of another; dedupe across lineages as before. Beam 100, 60 steps, gates, the stall rule unchanged. **Greedy runs alongside** in every arm (the arm that survived longest). Nothing else is tuned after the run; q = 3 is fixed here.

**5. Reference check before the arms (end-to-end equivalence).** (a) The harness `compare_backends e2e` on the smoke configuration (29 seeds, 3 steps, standard J, no triangles) on both backends: states and finalists must be identical, wall time and peak RSS reported. (b) The harness replay of data/smoke15 and the Mac beam/greedy states (0 backend differences so far through M2; expand_state at M4/M5). (c) The C++ B0-greedy run is compared with the re-scored Python Mac greedy run (strict re-score `data/full_r7_mac/greedy/strict_rescore.json`): stall step, growth steps per lineage, strict maxdepth distribution, gate pass rate. Trajectories differ because J is now strict, so (c) is statistical; the state-by-state equivalence is (a)/(b).

**6. Outputs** (per arm and mode, `output/<arm>-<mode>/`): states.jsonl (certificates over the raw R7 table, standard and strict fields), steps.jsonl (per-step gate counters, stalls, pass rate), summary.json (timers, peak RSS, fits), finalists.jsonl (eval_diagrams: power-free, ρ_min16, guard, novelty, dataset-class hit, strict fields), the power-failure classification (seam, period, run length, root matches, per-attachment breakdown) and a comparison table B0 vs B0+N at matched N with the F-N1 ratios. Everything in the T-018 note and handed to Lead as a 'ready for review' REPORT; nothing committed by me.

**7. Execution (owner 2026-10-16, replaces the local plan below):** ONE rjob job on the Mac with **9 cpus** (the same hardware as the Python reference job 20261016-130522-7373b4), `mem_gb` 12, `timeout_hours` 4, running the four arms sequentially (B0-beam, B0-greedy, B0+N-beam, B0+N-greedy) with `procs = RJOB_CPUS` for the parallel expansion, from the committed code with `[code.submodules."cpp/tcgraph"] sha = da7ac90`, b25_full and the dataset via [data] (`jobs/full_cpp_r7.toml`, `run_full_cpp.sh`, `scripts/run_arm.py`). Per arm: wall, CPU (user+system of the process tree), peak RSS, steps run, job id. No Python timing run (owner): the time comparison is the C++ job against the earlier Python job (beam 19 min, greedy 71 min), with the configuration differences stated: strict J (was standard), quota q = 3 (was cap 20), triangles and caps off (were on), the steps actually run, the arms' own stalls, and expansion procs 9; plus the measured like-for-like end-to-end ratio of the harness on the smoke configuration (23.3 to 24.2×, Python vs C++, B0, B0 strict, B0+N). **Original local-cost estimate (kept for the record):** Python reference per state without triangles: about 2.4 s (scoring 1.3 s per admissible child, gate 3 0.5 s per call, generation 0.04 s). Developer's C++ expand_state is 33× and the score step 36×, so about 0.1 s per state including the Python candidate generation. A step has ≤ 100 states → about 10 s; 60 steps about 10 minutes per run; four runs about 40 minutes of one core, plus finalist evaluation (Python, a few minutes per run). Peak RSS about 0.1 to 1 GB. **This is under the 2 h threshold, so the arms can run locally under capjob (2 GB, 2 cpus, `--out` set, tree clean).** Fallback if capjob kills a run or the C++ speed-up is lower: rjob job with `cpus = 4`, `mem_gb = 8`, `timeout_hours = 4`, one job per (arm, mode), inputs `data/t018/b25_full` via [data]; the Mac needs the C++ build per SHA (as in the Python job). Running the Python reference check (5a) adds about 10 minutes.

**8. Decisions requested from the owner.** (1) Replace the 22 / 7 seed split by "all seeds counted, line 48 reported as inherited". (2) Per-lineage quota q = 3 in place of the global J ranking. (3) Matched-N definition (bins of N_≥2, width 10) and the 1.5× threshold for F-N1. (4) Triangles and caps off.

## Results of the C++ restart (Mac job 20261016-181907-e9ed6c; b25 6d0c177, cpp/tcgraph da7ac90; Experimenter, 2026-10-16)
Four arms on the C++ backend, 29 seeds, strict J (S2), per-lineage quota 3, triangles off, 60 steps allowed, procs = 9 (Mac, 9 cpus). Data `t018/data/cpp_restart/<arm>/` (states, steps, expansions, finalists, strict re-score, arm_timing), `analysis.json`; analysis `scripts/analyse_arms.py`. Depth below is strict S2; the finalist evaluation's own `area_like` flags use the standard depth and are superseded.

**Timing (per arm, arm wall = the search only; the job also ran eval_diagrams after each arm, about 1.3 to 3 minutes each, so the job took 8.2 min):**
| run | wall | CPU (user+sys, process tree) | peak RSS | steps run | states |
|---|---|---|---|---|---|
| B0 beam | 8.7 s | 13.7 s | 68 MB | 6 | 89 |
| B0 greedy | 10.9 s | 15.0 s | 83 MB | 14 | 79 |
| B0+N beam | 9.3 s | 18.8 s | 75 MB | 8 | 111 |
| B0+N greedy | 17.4 s | 25.8 s | 99 MB | 16 | 95 |
Previous Python job (20261016-130522-7373b4, same Mac, 9 cpus): beam 19 min (stalled at step 8, 7 steps run, 99 states), greedy 71 min (23 steps, 91 states). **These are not like-for-like:** the C++ arms use strict J (was standard), quota 3 (was per-lineage cap 20), triangles and caps off (were on; 60% of the Python beam CPU), they stop at their own stalls after different numbers of steps (6/14/8/16 against 7/23), and the Python job's wall time includes the triangle generation and the Python expansion on 9 processes. The wall-time ratios 131× (beam) and 391× (greedy) therefore overstate the implementation difference. **The measured like-for-like ratio** (same configuration, harness e2e, 29 seeds × 3 steps, single process, Python vs C++ with identical states, finalists and expansion records): **23.3 to 24.6×** (120.8 s vs 4.9 s; B0 standard J, B0 strict J, B0+N, B0 strict with quota 3).

**H1 to H6 (strict depth):**
| | result |
|---|---|
| H1 growth ≥ 20 steps in some lineage | **falsified**: longest lineage 6 / 14 / 8 / 16 steps (B0 beam / greedy, B0+N beam / greedy); N_≥2 reaches 29 (37 for B0+N greedy), N 68 to 70. (Python standard-J greedy reached 23 steps; strict J ranks differently.) |
| H2 novel finalist, strict maxdepth ≥ 2 and T_deep ≥ 0.5, ≥ 1 growth step | **falsified** in all four arms (Validator CONFIRMED on all 374 states, [[2026-10-16-t018-restart-negative-check]]): **no STORED certificate of the four arms reaches strict maxdepth ≥ 2** (strict maxdepth histogram: 0 in 42 to 52 states, 1 in 37 to 59, 2 in none). Cheaper certificates of the inherited L48 lineage reach 2 (steps 0, 4, 5, 6; N_deep 9; T_deep 0.24-0.31); no state combines maxdepth 2 with T_deep ≥ 0.5. There is no H2 result. |
| H2a strict deep cell by N_≥2 ≈ 30 | met (strict N_deep ≥ 1 in 20 to 42 grown states per arm; 17 seeds already have one) |
| H3 strictly area-like finalist | **falsified**: 0 states and 0 finalists in all arms (S1 15 / 13 / 23 / 27 states, S3 13 / 11 / 13 / 11 states as sensitivity) |
| H4 D_c,≥2 ≥ 1 | not reached: max 0.53 (B0), 0.65 (B0+N greedy) |
| H5 L0 100% | holds in all four arms |
| H6 ≥ 90% novel | **falsified**: novel finalists 47%, 44%, 48%, 46%; 24 to 32 dataset-class hits per arm |
Strict maxdepth against N: √N fits slightly better than log in all eight pooled fits (vs N_≥2 and vs N; SSE differences below 5%), r² low: no discrimination between log N and √N.

**F-N1 (normalisation falsifier, N_≥2 bins of width 10):** gate pass rate (admissible children per examined candidate) B0 0.190 → B0+N 0.202 (×1.06) in the beam, 0.185 → 0.201 (×1.09) in greedy; growing seeds 11 → 13 (×1.18) in both modes; attachments per state 7.1 → 7.6. By bin (N_≥2 10 to 19: ×1.05 beam, ×1.08 greedy; 20 to 29: ×1.12, ×1.01; the 0 to 9 bin has 7 to 10 states and ratios 1.7 and 2.2 on 2 to 5 children). **F-N1 is falsified: exponent normalisation is not a significant lever** (both ratios are below 1.5 in both modes). Normalisation adds states and a few growing seeds, no depth: the B0+N arms contain no state with strict maxdepth ≥ 2 either.

## Best candidates (novel, L0-certified, power-free, guard passed) (Experimenter, 2026-10-16; owner-approved; numbers re-read from the files)

All five words: exactly 2.5-power-free, L0-certified (trivial in B(2,5) via an R7 certificate), not in the dataset, junction/closure guard passed, rho_min16 = 1.0 (min16 status ok; the stored finalist field). **None is strictly area-like under S2 at full N** (the adopted criterion: T_deep, T_depth ≥ 0.5 over all N cells): the full-N values below are all under 0.6, and T_deep is under 0.30 for every word. They are the best *partial* results, ranked by D_c,≥2 (non-|v|=1 cells over the boundary length; the |v|=1 cells are absorbed by S2). Letters: a, b are generators, A, B their inverses.

**Caveats.** (i) Cell counts N*_c are upper bounds (compressed-certificate size, not the minimal area). (ii) The depth of #1 and #2 is **inherited from the dataset seed** (line 48: strict maxdepth 2, N_deep 9, N≥2 23, N 55, at 52 letters): the search added cells (N≥2 23 → 27/28) but no strict depth; only #3-#5 reach their strict depth within the C++ arms, and those have strict maxdepth ≤ 1 (the C++ arms produced no state with strict maxdepth ≥ 2). (iii) #1-#2 have S2 values from the Validator-cheaper certificates (`data/validator_certs`), #3-#5 from the arms' own certificates, stored with each state in the arm's `states.jsonl` (`relator_indices`, `conjugators`, word `w`). (iv) **Validator's corrections** ([[2026-10-16-t018-restart-negative-check]]; I recomputed both cheaper values from `Agents/asetlearning/Validator/scratch/restart/cert_B0N-greedy_L34_s14_n54.json` and `cert_B0-beam_L47_s3_n56.json` with `scripts/strict_depth.py`, S2 full-N): the stored certificates of #3 and #4 are loose (#3: 66 → 54 cells, D_c,≥2 29/54 = 0.537, not 0.648; #4: 46 → 30 cells, D_c,≥2 15/56 = 0.268, not 0.482), so the table keeps both values with their source. #5 was probed by the Validator too (strict maxdepth 1 unchanged), but its cheaper certificate is not in the scratch folder, so only the stored values are given. **Compression can raise strict depth**: removing one cell turned strict depth 1 into 2 in all four L48 cases (steps 0, 4, 5, 6), so the earlier remark that non-minimal certificates overstate depth is not reliable, and a shallow result on a non-minimal certificate is not automatically the conservative one. (v) T_deep(N≥2) in `strict_depth_results.json` is higher (0.83-0.88 for #1-#2) because it divides by N≥2 only; it is not the registered full-N rule.

| # | Source | Word (letters) | |w| | N*_c | N≥2 | strict maxdepth | strict N_deep | D_c,≥2 | T_deep / T_depth (full N) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | seed line 48 (dataset), smoke step 5 (Python); Validator certificate | `aaBAABAABBAABAABBAAbaabbaaBBababAABABaaBaabAAbAAbbAAbbaab` | 57 | 65 (smoke certificate: 66) | 28 | 2 (inherited) | 9 | 0.491 | 0.245 / 0.566 |
| 2 | same lineage, smoke step 4; Validator certificate | `bAAbbAAbbaabAbaabaaBAABAABBAAbaabbaaBBababAABABaaBaabAA` | 55 | 63 (smoke certificate: 64) | 27 | 2 (inherited) | 9 | 0.491 | 0.255 / 0.577 |
| 3 | C++ B0+N greedy, lineage L34, step 14 | `AbaabaaBAABAABaabaabaBABaaBaabAAbAAbaaBaaBABaaBabAbaab` | 54 | 66 (stored); **54** (Validator's cheaper certificate) | 35 (stored); **29** (cheaper) | 1 (depth sum 11 stored; 7 cheaper) | 11 stored; 7 cheaper | 0.648 stored; **0.537** on the cheaper certificate (best on either) | 0.293 / 0.281 stored; 0.245 / 0.315 cheaper |
| 4 | C++ B0 beam, lineage L47, step 3 | `AABaaBaaBBaaBaaBAAbAAbaabAABabAABabbaabaabABaaBaabbABaab` | 56 | 46 (stored); **30** (cheaper) | 27 (stored); **15** (cheaper) | 1 | 4 stored; 2 cheaper | 0.482 stored; **0.268** cheaper | 0.175 / 0.346 stored; 0.165 / 0.447 cheaper |
| 5 | C++ B0 beam, lineage L20, step 1 | `aaBAABAABBAABaabaabAbaabAbAABaabAbabAbaaBAAbAbaab` | 49 | 32 | 19 | 1 | 4 | 0.388 | 0.299 / 0.429 |

Notes: #1-#2 are the same 63-65-cell family (the step-4 word is a 55-letter relative of the step-5 word); their rho_min16, power-freeness and guard are from the smoke finalists (`data/smoke15/finalists.jsonl`, lineage L48, steps 4 and 5). #5 is classed "thick strip" under the standard depth, not area-like, and its strict depth is 1; it is listed because it is the best word of a short lineage with a small certificate. For #3 the standard depth is area-like (maxdepth 3, N_deep 41) and the S2 depth is not (maxdepth 1): the drop is the |v|=1 absorption. Dataset-class hits (a different word of the same lineage and step, n = 56, `novel` false) are excluded.

**Pointers.** #1-#2: `data/validator_certs/best_L48-step5-n57.json`, `best_L48-step4-n55.json` (relator indices, conjugators, word) and `data/strict_depth_results.json` (keys `L48-step5-n57`, `L48-step4-n55`; S2 block). #3: `data/cpp_restart/B0N-greedy/states.jsonl` (certificate; match the word), `finalists.jsonl` and `strict_rescore.json` (lineage L34, step 14). #4: `data/cpp_restart/B0-beam/states.jsonl` (L47, step 3). #5: `data/cpp_restart/B0-beam/states.jsonl` (L20, step 1).

## Post-hoc diagnostic tests T1-T3 (decided after the restart; NOT pre-registered arms; Experimenter, 2026-10-16)

Origin: the Math Expert's proposal [[2026-10-16-t018-close-or-continue]]; owner-approved through Lead. These are diagnostics on existing data, decided **after** the C++ restart results were known, with the decision rules as given: T2 below 1.5 drops junction repair (JR) unbuilt; T3 near 0 or below 1.5x drops R8; T1 is read structurally (below). Scripts: `scripts/t1_analyse.py`, `scripts/t2_jr_bound.py`, `scripts/t3_r8_probe.py`; certification `t1_certify.sh` + `jobs/t1_certify_gt53.toml`.

**T1: strict depth on the certificates of the 491 power-free dataset words.** The 29 short seeds already had certificates (stepB run, 16 variants); for the 461 words of 54-123 letters kbcert was run as **one pure-Python job on the Mac, an owner-approved one-off exception to the C++ rule** (reason: certification by rewriting path has no C++ port, a port would cost the Developer a day or more, and the test decides whether T-018 is closed; record kept here). Job 20261016-205124-b1ec48 (b25 c885ccb, tcgraph pin 2c264fd unused, Mac 9 cpus, 70 min, exit 0; inputs sha256: pf_dataset_gt53.json 8e02a779..., rec.kbprog 436fd2c7...; outputs `data/t1/outputs/certs_gt53.jsonl`, analysis `data/t1/t1_strict.json`). **Certified: 424 of 461 + 29 of 30 = 453 of 491 words** (the other 38 need a rule with a period > 7 in all 16 variants; this is not a statement about triviality). All numbers are for the stored compressed certificates (best of 16 rotation/inversion variants, then F_c), **not minimal**: N is 12-1,197 cells (the longest words have certificates of several hundred cells). Strict depth as in `scripts/strict_depth.py`, full-N normalisers.

| strict maxdepth | 0 | 1 | 2 | 3+ |
|---|---|---|---|---|
| standard depth (reference) | 2 | 50 | 315 | 86 (83 at 3, 3 at 4) |
| S1 | 6 | 327 | 120 | 0 |
| **S2 (adopted)** | 82 | 360 | **11** | 0 |
| S3 (|v| in {1,2} trivial) | 10 | 379 | 64 | 0 |

- **Strict maxdepth never exceeds 2 in any of the 453 certificates, whatever the size** (N up to 1,197, N_≥2 up to 528 under S2). Under S2 the mean maxdepth by N bin (width 20) rises slowly: about 0.3 below N = 100, 0.6-0.9 for N = 100-280, 0.9-1.1 for N = 300-540 (bins of 3-15 words beyond that reach 1.5), while the maximum stays 2 (the 11 words below).
- **S2 maxdepth 2: 11 words** (dataset lines 474, 523, 498, 525, 695, 658, 681, 699, 614, 777, 783; 72-101 letters; certificates of 253-716 cells; N_deep 9-38). All are large non-minimal certificates; their full-N T_deep is only 0.02-0.12 and T_depth at most 0.27. **No word is strictly area-like (S1, S2 or S3) at full N** (T_deep over all words: S2 max 0.26; S1 max 0.69 but with T_depth ≤ 0.49 and maxdepth 2; S3 max 0.49). Line 48 (S2 depth 2 only on the Validator's 55-cell certificate) is not in this list: its stored 56-cell certificate has S2 depth 1, again the certificate dependence.
- **Fit of strict maxdepth against N_≥2 (S2, 453 points):** log N: SSE 67.9, r² 0.17, slope 0.277 per ln N; √N: SSE 69.6, r² 0.15; log slightly better; N as the abscissa gives the same ordering (SSE 68.1 / 69.6). S1: SSE 84.6 (log) / 85.3 (√); S3: 62.3 / 63.5. Both fits explain under 20% of the variance, and with maxdepth in {0, 1, 2} neither model is identified (same remark as for the arms).
- **Reading (Math Expert's rule for T1): "maxdepth ≤ 2 throughout, flat in N → evidence of hyperbolic-like behaviour at these sizes", but with two reservations.** (a) These are non-minimal certificates; the Validator showed that compression can both lower the cell count and raise the strict depth (1 → 2 in the four L48 cases), so a shallow result on a non-minimal certificate is not automatically the conservative one. (b) The only words with strict depth 2 are the largest certificates, and their depth-2 core is thin (T_deep ≤ 0.12): consistent with a log N-type growth that the size range cannot resolve. It does answer the structural question in one respect: **power-free words of 32-123 letters have strict depth ≤ 2 in every certificate we could build; depth ≥ 3 never occurs.** Not verified: minimal fillings, the 38 uncertified words.

**T1 extension: upper range, log against √ (Lead's request for T-024 feasibility; `scripts/t1_upper_fit.py`, `data/t1/t1_upper_fit.json`).** OLS of maxdepth on ln x and on √x, restricted to the words above the median, the 75th and the 90th percentile of x (x = N_≥2 or |w|), with a bootstrap (2,000 resamples of the words) of the SSE difference.
- **S2 mean and quantiles by N_≥2 bin (n; mean; median; 75th; max; share with depth ≥ 2):** 25-50 (56; 0.59; 1; 1; 1; 0%), 50-100 (180; 0.76; 1; 1; 1; 0%), 100-150 (94; 0.96; 1; 1; 2; 2%), 150-200 (52; 1.04; 1; 1; 2; 6%), 200-300 (50; 1.04; 1; 1; 2; 10%), 300-400 (13; 1.08; 1; 1; 2; 8%), 400-600 (1). By |w|: 0.7-0.8 below 70 letters, 1.0 at 70-100 (share ≥ 2: 7%), 1.29 for the 7 words of 100+ letters.
- **S2 fits, upper range:** N_≥2 ≥ 160 (114 words, range 160-528): slope 0.026 per ln N (√: 0.003), SSE 12.78 against 12.78; N_≥2 ≥ 214 (46 words): slope -0.30 (negative), SSE 4.30 against 4.31. Whole range: log better (SSE 67.9 against 69.6; bootstrap: √ better in 1% of resamples), but already for the upper half the difference is 0.08 (4% of resamples favour √) and for the upper quarter 0.00 (34%). **The largest-N bins do not discriminate log from √: both are flat there (slope indistinguishable from 0); what the S2 data show in the top range is a plateau at mean 1.0-1.1, maximum 2.** As the abscissa |w| the picture is the same (upper-quarter SSE 13.84 against 13.84).
- **S1 (absorption once) keeps growing:** mean 1.37 / 1.43 / 1.61 in the upper half / quarter / tenth, slope 0.5-0.6 per ln N, the two models again indistinguishable (SSE equal to 0.03). The difference between S1 and S2 is the repeated absorption of |v| = 1 cells: S2 removes the growth. S3: mean 1.19-1.29, slope 0.12-0.19 then -0.06 in the top tenth.
- **For T-024:** the data end at |w| = 123 (N_≥2 ≤ 528 under S2; only 1 certificate above 400, 7 words above 100 letters), so a √-law (slope ≈ 0.05 per √N at the whole-range fit) and a log-law cannot be told apart, and neither is supported over a bounded depth. Words of 1,000+ letters are needed for the curve to say anything.

**T2: optimistic bound for junction repair (nothing implemented).** On the stored states of the two B0+N arms, every pair attachment passing gate 1 was normalised (B0+N) and tested; "repairable" = a failing attachment all of whose forbidden windows have m ≥ 2, are not an exact half (even m, 2L = 5m), and m is neither the root length of an adjacent new cell nor of an adjacent old cell (owners read off the folded diagram of the normalised certificate). Assumed: every repair succeeds and also passes gates 4 and 3. "pass" = attachments passing gates 1 and 2 (power-free w'); "children" = those that also pass gates 4 and 3 (what the search keeps, before the word dedup).

| mode | states | gate-1 attachments | pass | children | fail | all-repairable | (pass + rep)/pass | (children + rep)/children | same, distinct words |
|---|---|---|---|---|---|---|---|---|---|
| B0+N beam | 111 | 840 | 289 | 173 | 551 | 442 | **2.53** | 3.55 | 3.04 / 3.56 |
| B0+N greedy | 95 | 708 | 244 | 145 | 464 | 370 | **2.52** | 3.55 | 2.98 / 3.51 |

Reading by the stated rule: **above 1.5, so JR is not dropped by this test.** Why it differs from F-N1's ×1.06-1.09: normalisation removes the m = 1 runs, so what remains in B0+N is mostly m ≥ 2 junction windows with no root match: 80% of failing attachments (442/551, 370/464) have every window repairable, 12% have a mixture, 8% have only unrepairable ones. Caveats (they all push the bound up): it assumes every repair succeeds and passes gates 4 and 3; a repair is an operation not yet defined (it may break gate 1 or create new windows); states are all stored states of the two arms, including the last ones; the bound says nothing about whether repaired children would be deep (the ring argument is untouched).

**T3: one-step R8 probe.** R8 table: R7 (b25_full, 1,630 entries, indices unchanged so the stored certificates stay valid) plus the 836 oriented rotation classes of the length-40 cores (|v| = 8) of `buildStandardRelators(8)` (both orientations, so inverses included): **2,466 entries, sha256 9260c24ec5773de74619f151295657b47f8644e7a441a4d417be15328ffeefa1** (text file, one entry per line). The class set equals that of `buildStandardRelators(8)` (693 unoriented classes against 275 for 7; R7's own 275 reproduced). The C++ Expander (tcgraph da7ac90 local build, triangles off, each arm's own normalisation setting, unlimited per-state budget) was run once from the last state of each of the 29 lineages of each of the four arms, with the R7 table and with the R8 table.

| arm | tips | admissible children, R7 | admissible children, R8 | tips with children |
|---|---|---|---|---|
| B0 beam | 29 | 13 | 13 | 10 / 10 |
| B0 greedy | 29 | 16 | 16 | 10 / 10 |
| B0+N beam | 29 | 14 | 14 | 11 / 11 |
| B0+N greedy | 29 | 18 | 18 | 11 / 11 |

**The R8 children equal the R7 children in every tip: ratio 1.00, below 1.5, so by the stated rule R8 is dropped.** **Positive control and filter check (Lead's request; the zero is real, not a filter).**
- *Code review.* No index range, length cap or prefix assumption excludes the new entries: `MoveCells` takes every table entry whose cyclic core is u^5 with u primitive (2,304 moves in R8 against 1,494 in R7), `VertexGen` uses all of them, the C++ Expander builds its move set the same way. The only length parameters are `l_max` = 13 (arc shared by the two cells, also capped at n-1 and |v|+6) and gate 1 (each new cell exposes at most half of its 5|v| letters, so 2(sA + l) >= 40 for |v| = 8, 2(sA + l) >= 35 for |v| = 7).
- *Positive control.* Boundary = the inverse of a k-letter arc of a random |v| = 8 core plus 14 random letters (40 trials per k). Python generator, share of boundaries that give at least one configuration containing a |v| = 8 cell: k = 6-12: 0/40; k = 14: 2/30; 16: 7/37; 18: 17/39; 20: 24/40; 22: 28/40; 24: 25/40. The same control with |v| = 7 cells and the R7 table (so the mechanism is checked on a length that does occur): k = 14: 13/33; 16: 25/38; 20: 22/40. C++ against Python on 150 controls (k = 22): identical configuration counts every time; 216 Python configurations contain a |v| = 8 cell; the C++ configuration list contains entries with table index > 1630 and vmax = 8 (e.g. index 1699). So the generator, in both languages, does produce |v| = 8 attachments when the boundary offers a long arc of an 8-periodic core.
- *Counts before the gates (all stored states, R7 / R8):* B0 beam 631 / 631, B0 greedy 558 / 558, B0+N beam 840 / 840, B0+N greedy 708 / 708; on the 116 lineage tips 187/187, 190/190, 190/190, 194/194. **Configurations using a table index > 1630: 0.**
- *Why none on these boundaries.* A |v| = 8 cell needs sA + l >= 20 with l <= 13, i.e. a boundary arc of about 14 or more letters that continues an 8-periodic pattern (control: no hit below k = 14). The longest boundary arc matching any |v| = 8 core in the stored states is 9-16 letters, a chance match (median 11; 5 of 89 / 5 of 95 states reach 14); for |v| = 7 it is 14-17 in 37 of 89 (B0 beam) and 39 of 95 (B0+N greedy) states, because the existing 7-cells put 7-periodic arcs on the boundary. No diagram here contains an 8-cell, so no 8-periodic arc exists to bootstrap the first one. The (2,8) and (3,8) pairs of the counting argument need in addition a partner cell sharing up to 9-14 letters of the 8-core, which a chance arc does not supply. Conclusion: R8 gives nothing from these states because no |v| = 8 attachment is geometrically available there, not because of a filter; the one-step probe says nothing about R8 from boundaries that already carry 8-periodic arcs (the control shows those would be generated). Caveat: a "tip" is the last stored state of a lineage; 10-11 of the 29 tips per arm still have R7 children, so "stalled" is read as "last state of the lineage".

## Conclusion (closed 2026-10-17)

**Verdict: H2 falsified (negative result), replicated by the Validator** ([[2026-10-16-t018-restart-negative-check]]). Under strict depth (S2, vertex contact, T over the full N), the patch-growth search over the R7 move table from the 29 certified power-free dataset seeds produced no novel word with strict maxdepth ≥ 2, so the success criterion was not met.

What was learned:
- **Depth was an artefact of a⁵ cells.** Cells of root length 1 only normalise exponents. They made 36–62% of every certificate and created the earlier standard-depth hits (line 51) and D_c ≥ 1 (line 48). Strict depth S2, with N≥2 and D_c,≥2 as headline measures, was adopted ([[challenge-gen-success-metrics]] § Owner decision 2026-10-16).
- **No power-free seed at N ≤ 3** (proved for 2 cells, exhaustive for 3; [[2026-10-15-t018-seed-reachability-review]]). Power-free certified relations do exist: 491 of 820 dataset words.
- **The search stalls before a depth-2 ring can close.** In the C++ restart (four arms), lineages stall after 6–16 steps and no stored certificate reaches strict maxdepth ≥ 2. Cheaper certificates of the inherited line-48 lineage do reach 2 (T_deep 0.24–0.31). Compression can raise strict depth.
- **Levers tested:**
  - exponent normalisation is not one (F-N1 falsified, ×1.06–1.09);
  - R8 adds nothing for these boundaries, because no 8-periodic arc ever appears to seed a length-8 cell (T3, with a positive control);
  - an optimistic bound for junction repair is about 2.5× (T2), not tested.
- **T1 (453 certified dataset words, up to 123 letters and 1,197 cells):** strict depth plateaus at mean ≈ 1, max 2. log vs √N is unresolved below ~1,000 letters, so depth versus length on much longer words is the open question.
- **Best candidates:** [[#Best candidates (novel, L0-certified, power-free, guard passed) (Experimenter, 2026-10-16; owner-approved; numbers re-read from the files)]].
- **Infrastructure produced:**
  - the T-018 search, ported to C++ in tcgraph (`certificates/`, `diagram/`, `search/`) with exact Python equivalence, about 24× end to end;
  - tcgraph consolidation (PRs #5 and #6);
  - `capjob`.

**Follow-up:** T-024 (depth versus word length: onion construction and long words, relators beyond R7, efficient search). **Addendum (2026-10-17): the ring and accretion argument, checked by the Validator** ([[2026-10-16-t018-ring-accretion-argument-check]]).
- (a) Strict depth 2 needs a closed ring: **confirmed qualitatively**. The Math Expert's ~19/25-cell counts are not lower bounds: line 48's depth-2 structure has only 6 non-trivial cells inside its ring.
- (b) Existence: **confirmed, with a correction**. Depth 2 holds on the Validator's 55-cell certificate; the stored 56-cell one gives 1.
- (c) "A stall after 6–16 steps gives maxdepth ≤ 1 in any geometry" **does not follow**. L34 added +20 non-trivial cells and reached standard depth 3, but at step 14 its 8 non-trivial standard-deep cells sit under 22 cells of root length 1, which S2 absorbs. So the limit is the root-length mix of what this generator attaches, on stored certificates. "Any geometry" is untested.

## Re-check under the corrected gate (2.5-reduced), 2026-10-17 (Experimenter)

**Gate.** The owner corrected the target to **2.5-reduced**: no window with exponent strictly above 2.5 (length L, period m, forbidden iff 2L > 5m). Exact 2.5-powers (an *exact half*: even m, 2L = 5m) are allowed; "strictly power-free" (no window with exponent ≥ 2.5) is now a diagnostic. One detector (runs of minimal period) serves Python and C++ since T-026. Code: b25 `dc4c00e` (job) and `f3b1511` (rescore fix), cpp/tcgraph `5eb03be`. Everything below is **under the corrected gate**; the old numbers in the sections above were computed with the strict gate.

**1. Gate-2 count (does the corrected gate change the search?).** I replayed all 374 stored states of the old C++ restart (job 20261016-181907-e9ed6c) through the C++ Expander of both builds (old tcgraph `da7ac90`, new `5eb03be`; budget 2,000, all configurations). An attachment the old gate 2 rejects and the new one accepts has windows of exact-half type only. Counts:

| Arm | old gate-2 rejections | accepted by the corrected gate (exact-half only) |
|---|---|---|
| B0 beam | 417 | 0 |
| B0 greedy | 373 | 0 |
| B0+N beam | 551 | 15 |
| B0+N greedy | 464 | 11 |

So **B0 is unchanged** (identical counters at every step, identical trajectories: expected, no attachment there has only exact-half windows). **B0+N differs from step 1**, because exponent normalisation rewrites a run to exactly 2.5 and so creates exact halves. Positive control: the word 1 2 1 2 1 (m = 2, L = 5) is rejected by the old predicate (`has_power25_linear`) and accepted by the new (`has_power_gt25_linear` False, `is_2p5_reduced` True; `has_power_ge25_linear` True). Gate 2 calls `hasPower25Linear || hasPower25Cyclic` in `da7ac90` and `is2p5Reduced` in `5eb03be` (expand.cpp). The rjob log shows the corrected build (provenance `dc4c00e` / `5eb03be`). Files: `runs/gate2_check/{replay.py,old_build.json,new_build.json}`.

**2. T-024 diag re-check (smoke seeds 21 and 594).** `t024_diag` re-run with the new detector: the output file is **byte-identical** to the earlier one. The junction picture is unchanged (all forbidden windows at single junctions; 0 of 300 re-runs pass gate A or B).

**3. Restart arms rerun under the corrected gate** (rjob `20261017-214143-877a6a`, same parameters and inputs; 8-10 min on the Mac with 9 CPUs; steps run 6 / 14 / 8 / 16 as before). Rescore with strict depth S2 (vertex contact), the S2-flip control (even-root cells exposing at least half absorbed at peel time) and the separate L1 check (rho_min16 over the 16 images; L1 iff rho_min16 = 1), `rescore_strict_flip.py`, files `runs/arms_corrected/rescore/<arm>.json`.

Strict S2 maxdepth over all stored states (counts of states at depth 0 / 1 / 2 / 3):

| Arm | old run (states) | corrected run (states) | S2-flip control, corrected |
|---|---|---|---|
| B0 beam | 50 / 39 / 0 / 0 (89) | 50 / 39 / 0 / 0 (89) | 55 / 34 / 0 / 0 |
| B0 greedy | 42 / 37 / 0 / 0 (79) | 42 / 37 / 0 / 0 (79) | 46 / 33 / 0 / 0 |
| B0+N beam | 52 / 59 / 0 / 0 (111) | 57 / 105 / 2 / 0 (164) | 78 / 84 / 2 / 0 |
| B0+N greedy | 42 / 53 / 0 / 0 (95) | 46 / 75 / 3 / 0 (124) | 61 / 61 / 2 / 0 |

- The flip control lowers the depth-1 counts by 4-21 states, but the depth-2 states of B0+N survive it (flip depth 2 in 2 of 2 beam and 2 of 3 greedy states).
- No state is area-like (S2 or flip) in any arm. Fits of maxdepth against N prefer √N in every arm (S2 and flip).
- **L1.** All 29 seeds are L1 in every arm. All finalists of the B0 arms are L1 (49 and 43). Of the B0+N finalists **39 of 102 (beam) and 23 of 78 (greedy) are not L1**, most with rho_min16 = 0.0 (the 2.5 reducer collapses the word to the empty word).
- **Every new depth-2 finalist is non-L1**: B0+N beam L2 step 5 (rho 0.0); B0+N greedy L2 steps 5 and 4 (rho 0.0) and step 3 (rho 0.94). **No L1-clean finalist has strict depth above 1 in any arm.** The depth-2 states are lineage L2, N = 40-46 cells. So the new depth comes from words the reducer trivialises, not from L1-clean words.

**4. Seed re-check (Validator, corrected rule; reported by the Validator and Developer, not rerun by me).** The 2-cell seeds stay excluded. There are 16 3-cell chain classes up to rotation and inversion (64 before identification): (2,5) 4 classes of length 25, (2,6) 4 of length 30, (2,7) 8 of length 35, (3,7) none; **all are R2.5-trivial**, so none is an L1 word. Triangles: 63 feasible length triples, none 2.5-reduced. Triangles and lenses: 0 (Validator; the smallest maximum exponent is 3.5).

Under the corrected gate the T-018 negative stands for L1 words: no L1 word reached strict depth >= 2.

## Related material
- [[2026-10-14-cancellation-constructions]] (ideas 2 and 3) · [[2026-10-14-area-vs-path-criterion]] · [[2026-10-14-vertex-depth-criterion]]
- [[t016-overlap-chaining-2026-10-14]] (triangle census; E1d)
- [[challenge-gen-success-metrics]] · [[challenge-gen-glossary]] · [[project-challenge-gen]]
- [[B25/Structured Constructions/_type|Structured Constructions]]

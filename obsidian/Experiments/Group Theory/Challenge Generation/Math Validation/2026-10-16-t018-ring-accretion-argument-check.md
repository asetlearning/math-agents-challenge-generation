---
type: validation-verdict
date: 2026-10-16
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "Math Expert ring/accretion argument ([[2026-10-16-t018-close-or-continue]])"
verdict: "(a) ring: CONFIRMED qualitatively, counts not lower bounds; (b) existence: CONFIRMED with a correction; (c) stall inference: DOES NOT FOLLOW as stated"
---
# Ring / accretion argument: check

Source: `Agents/asetlearning/MathExpert/proposals/2026-10-16-t018-close-or-continue.md` (argued claims). Related: [[2026-10-16-t018-restart-negative-check]] and [[2026-10-16-t018-area-like-dataset-words-check]] (Parts 3 and 3b). Scripts: `Agents/asetlearning/Validator/scratch/restart/ring.py`, `l34_std.py` (outputs `.out`).

**Terms.**
- **S2:** |v| = 1 cells are absorbed into the exterior on vertex contact, repeated before every layer; the other cells are peeled by vertex contact.
- **B_r:** the exterior vertex set just before layer r is assigned (after the absorptions).
- **Ring:** the set of cells sharing a vertex with a given set of cells.

## (a) "Strict maxdepth 2 needs a closed ring of strictly deep cells around one cell; about 19 (trivalent) / 25 (square) nontrivial cells"

**The structural part holds, argued directly from the definition.**
- A cell c (root length ≥ 2) has S2 depth ≥ 2 iff no vertex of c is in B_1 = B_0 ∪ verts(layer 0) ∪ verts(cells absorbed before layer 1).
- So every cell sharing a vertex with c is one of two kinds:
  - (i) a nontrivial cell of depth ≥ 1, i.e. not touching B_0;
  - (ii) a |v| = 1 cell that is absorbed only after layer 1. If it were absorbed before layer 1, its vertices (including the shared one) would join B_1, and c would be at depth 1.
- In a disc diagram, the cells around the vertices of an interior cell close up into a ring.
- So c lies inside a closed ring made of strictly deep cells, and possibly |v| = 1 cells. Those |v| = 1 cells are themselves enclosed, since they do not touch B_1.
- Precise form of the claim: "a closed ring of strictly deep nontrivial cells, possibly interleaved with enclosed |v| = 1 cells, around c; outside it, a separating layer of depth-0 cells and/or |v| = 1 cells absorbed after layer 0".

**The counts are not lower bounds.**
- 1 + 6 + 12 and 1 + 8 + 16 are vertex-neighbourhood sizes of a regular hexagonal or square tiling. Diagrams here have cells of perimeter 10 to 35 with unequal arcs (Fine–Wilf bounds), so a ring can close with far fewer cells.
- **The one known example, measured** (line 48; my 55-cell certificate and the 1-cell-cheaper certificates of L48 steps 0, 4, 5 and 6, all identical in this structure):
  - **2** depth-2 cells, root length 2 (core length 10);
  - a closed ring of **4** depth-1 cells (root lengths 3, 3, 5, 5);
  - the next ring out: 8 cells, of which **5 are |v| = 1 cells absorbed after layer 0**, plus 1 depth-0 and 2 depth-1 cells.
  - So the inner structure has 6 nontrivial cells against the claimed 7 to 9, and the outer separation is mostly |v| = 1 cells. The whole diagram has N_≥2 = 23 (14 at depth 0).
- **Reading:** about 20 nontrivial cells is the right order of magnitude for this one diagram as a whole, but it is not a minimum. The inner ring needs as few as 4 large cells, and |v| = 1 cells can do the outer separation.

## (b) "Line 48's seed certificate has strict maxdepth 2 on a power-free word of length ≤ 53"

**CONFIRMED with a correction.**
- Line 48: |w| = 52, 2.5-power-free (my C detector, seed-reachability check), L0-certified.
- S2 maxdepth 2, N_deep 9, N_≥2 23, N 55, T_deep 0.307 (full N), T_depth 0.623. These are my Part 3 / 3b numbers, re-measured today.
- **Correction:** this holds on the Validator 55-cell certificate, **not** on the seed's stored compressed certificate. The restart's L48 step-0 certificate (56 cells) has S2 maxdepth 1. So "the seed certificate" should read "a (Validator) certificate of the seed word".
- **What it does not show:** "the presentation behaving hyperbolically is not what blocks depth 2". Maxdepth 2 at N = 55 is compatible with logarithmic depth growth. Existence rules out "depth 2 is impossible at these sizes"; it does not separate log N from √N. The proposal's T1 is the right test for that.
- **Caveat on T1** (the proposal's line "non-minimal fillings over-state depth, so a shallow result is the stronger one"): **not reliable**. On the L48 words, removing one cell raised S2 maxdepth from 1 to 2 (4 of 4 cases). A shallow result on a non-minimal certificate is not conservative.

## (c) "Growth that stalls after 6–16 steps gives maxdepth ≤ 1 in any geometry"

**DOES NOT FOLLOW as stated. It needs the qualification "for this search policy", and the data point to |v| = 1 burial as the blocker.**
1. **Cell budget is not the binding constraint.**
   - L34 (B0+N greedy) grew N 34 → 70 and N_≥2 17 → 37 in 16 steps: +20 nontrivial cells.
   - The only known S2-depth-2 structure uses 6 nontrivial cells inside its separating ring.
   - So the step count alone does not exclude depth 2. What matters is *where* attachments go: the J-ranked beam or greedy with quota 3 does not concentrate burial around one spot.
2. **Accretion did bury cells two and three layers deep**, under the standard depth: B0+N greedy L34 reached standard maxdepth 3, and 132 of the 374 states (counted with cross-arm duplicates) have standard maxdepth ≥ 2. Under S2 these fall to 1 because the burying cells are |v| = 1 cells. L34 anatomy (`scratch/restart/l34_std.out`; B0+N greedy, standard peel): step 0 has standard maxdepth 1 (N 34, 17 cells with |v| = 1). Step 14 has N 66, of which 31 cells have |v| = 1. Its 17 standard-depth-≥ 2 cells are 9 with |v| = 1 plus 8 nontrivial ones (roots 2, 2, 2, 3, 3, 4, 4, 5). The layers above them hold 22 |v| = 1 cells (10 in standard layer 0, 12 in layer 1), and S2 absorbs those. Growth from step 0 to step 14 added 32 cells, 14 of them with |v| = 1.
   - So the observed limit is the root-length composition of what accretion attaches, not accretion as such.
3. **Certificate dependence:** the "observed maxdepth ≤ 1" is on stored certificates. The L48 lineage's cheaper certificates show 2 (inherited depth, but a counter-example to reading the histogram as a property of the words).
4. **"In any geometry"** is not tested by these data, flat or hyperbolic. The claim is about one generator at one step budget.

**Suggested wording:** "Under J-ranked accretion with quota 3, lineages stall after 6–16 steps. Burial does occur (standard depth up to 3), but by |v| = 1 cells. No non-inherited lineage reached S2 depth 2, even on cheaper certificates (54 words probed). Whether depth 2 can be grown is open; it is not excluded by the cell budget."

**Scope:** argued from the S2 definition, plus measurements on line 48 / L48 and on the restart data. No minimality and no geometry claims.

## Addendum 2026-10-17: corrected target
(b) is unaffected and holds a fortiori. Line 48 is strictly power-free (no exponent ≥ 2.5), hence 2.5-reduced. (c)'s qualification gains one item: the restart arms searched only the strictly power-free subspace (see [[2026-10-16-t018-restart-negative-check]], addendum 2026-10-17).

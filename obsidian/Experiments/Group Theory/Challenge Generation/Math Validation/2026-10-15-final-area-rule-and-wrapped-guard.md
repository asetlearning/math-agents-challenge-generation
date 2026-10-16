---
title: "Final area-like rule and wrapped-relator guard — review"
status: conjectured
domain: group-theory
project: challenge-gen
claim: "Owner rule 2026-10-15 (area-like, wrapped-relator guard, depth-sum J) is sound as a diagnostic; no chain word has a connected deep core of size 2"
claimant: Math Expert (accepted by owner); Developer branch 23-final-area-rule-wrapped-guard @ 7da39e4
verification_method: "topological argument; standalone classifier on synthetic planar maps; own peeling on the compressed T-016 certificates; Developer's branch run on the same certificates"
tools_used: ["python3 3.12.3 (scratch/rule_classify.py, rule_real.py, guard_exact.py, branch_check.py, core_debug.py)", "b25 main 6f71817 and branch 23-final-area-rule-wrapped-guard @ 7da39e4 (object under test)"]
author: asetlearning
tags: [agent/validator, user/asetlearning, domain/group-theory, topic/b25, topic/van-kampen, topic/dehn-function, project/challenge-gen, status/conjectured, proof]
---

# Review — final area-like rule, wrapped-relator guard, size-2 core conjecture
Triage: [[2026-10-15-final-area-rule-and-wrapped-guard-triage]]. Sources: [[challenge-gen-success-metrics]] § Owner decision 2026-10-15, [[2026-10-14-depth-followups]], [[t018-t021-diagram-search-2026-10-14]], earlier review [[2026-10-14-t023-folded-diagram-review]]. Scripts: `Agents/asetlearning/Validator/scratch/`.

**Terms.** Cell depth, N_deep, maxdepth, T_deep, T_depth, V_int, J are as in the T-023 review (depth = peeling round, 0 = touches ∂Δ; T_deep = N_deep/(√N−2)²; T_depth = maxdepth/((√N−1)/2)). "Touches" = shares a vertex. **Deep core** = largest set of deep cells connected through shared edge paths. **Ring** = the cells other than the deep cell. Classes after the owner's fix: area-like (rule), small enclosed (N_deep ≥ 1, N < 16), thick strip (N_deep ≥ 1, N ≥ 16, not area-like), path-like (N_deep = 0).

**What every statement below is about.** The shape of one certificate's diagram, which is an upper bound on area. None of it is a statement about the free group B(2,5), the word's true area, or its Dehn function. Verdicts are on the definitions and on the stated conjecture; the T-018 claim itself is not covered.

## Summary of verdicts
| Item | Status |
|---|---|
| Rule as a **label for quadratic area** | **not sound**: thin strips and a padded wrapped pair pass it at N = 16–25 (§1) |
| "Dual-connected core ≥ 2" clause | well defined; the conjecture used to justify it is **false** (§3) |
| Wrapped-relator guard as stated ("w conjugate to the deep relator") | **not sound in the free group; vacuous in the group; does not fire on the 10 cases that motivated it** (§2) |
| Developer's `shape`, `deep_core`, `depth_sum`, J | **correct** against my independent implementation (§4) |
| Developer's `is_wrapped_relator` | implements the owner's wording faithfully; inherits the defects of §2 |

## 1. Can the area-like rule be gamed?
Standalone implementation (`rule_classify.py`) of the final rule, run on planar maps (cells as cyclic vertex lists). Exact outputs:

| Map | N | N_deep | maxdepth | T_deep | T_depth | core | Class |
|---|---|---|---|---|---|---|---|
| n×n grid, n = 5…8 | 25–64 | 9–36 | 2–3 | 1.0 | 0.8–1.0 | = N_deep | area-like (intended) |
| 4×4 grid | 16 | 4 | 1 | 1.0 | 0.67 | 4 | area-like (the calibration point) |
| **3×k ladder, k = 6, 7, 8** | 18, 21, 24 | 4, 5, 6 | 1 | 0.8–0.71 | 0.62–0.51 | k−2 | **area-like** |
| 3×9, 3×10 … | ≥ 27 | ≥ 7 | 1 | ≥ 0.64 | < 0.5 | | thick strip |
| **4×k strip, k = 5, 6** | 20, 24 | 6, 8 | 1 | 0.98, 0.95 | 0.58, 0.51 | | **area-like** |
| **wrapped pair** (3×4 grid, core of 2) **+ 1×4 tail** | 16 | 2 | 1 | 0.5 | 0.67 | 2 | **area-like** |
| central 6-gon + 3 rings of quads (|∂Δ| = 6 for every k) | 19 | 13 | 3 | 2.3 | 1.8 | 13 | **area-like**, boundary does not grow |
| 3×3 grid | 9 | 1 | 1 | | | 1 | small enclosed, guard fires |

Findings.
1. **T_depth is a one-sided filter.** It needs maxdepth ≥ (√N−1)/4, which is 1 for every N ≤ 40. So for 16 ≤ N ≤ ~25 the second condition is maxdepth ≥ 1, i.e. nothing beyond N_deep ≥ 1. Strips of width 3 and 4 have linear area and pass.
2. **The "core ≥ 2" clause is weak.** It excludes scattered deep cells, but a wrapped pair (two adjacent relators ringed) padded to N = 16 with a chain that touches ∂Δ but not the core passes: T_deep = 0.5 at N_deep = 2, N = 16. The guard (N_deep = 1) does not fire, and the pad cells fail "touch the deep cell" anyway.
3. **Onion around one relator.** A relator wrapped twice is area-like (maxdepth 2, N ≥ 16). In flat geometry that is the grid and fine. In a curved (hyperbolic-type) region the same label appears at small N. The label cannot tell the two apart for N ≲ 40.
4. **Scale at which the label can work.** For N ≳ 41, T_depth ≥ 0.5 forces maxdepth ≥ 2, and for N ≳ 100 maxdepth ≥ 3. There the rule demands real nesting, and the ladder/strip families fail. The weakness is confined to 16 ≤ N ≲ 40.
5. **Realisability not decided.** These are planar maps. Whether they occur over the dataset + v⁵ relators is an experiment. The real data has pieces of 28 of 57–60 letters (§3), so the table is far from small cancellation and ring cells that share long paths with a core are not excluded.

**Recommendation.**
- Keep "area-like" as a diagnostic label and never as evidence for quadratic area. Gate T-018 success on H2 (maxdepth ≥ 2, T_deep ≥ 0.5, L1-certified, novel), as already planned.
- If a stricter label is wanted: require **maxdepth ≥ 2** (drop the core ≥ 2 alternative). That removes the ladders, the strips and the padded pair, keeps every grid with n ≥ 5, and loses only the 4×4 calibration point (N = 16, maxdepth 1), which can be reported as "boundary grid".
- Evidence of area growth comes from the fit across N (the owner's falsifier), not from the label. maxdepth is an integer ≤ 3 over N ≤ 100, so a log N vs √N fit separates the two only for N ≳ 60 and with many seeds; report the residuals of both fits and the N range, and say "cannot discriminate" when the range is short.

## 2. Wrapped-relator guard
**Statement.** N_deep = 1 and every other cell touches both ∂Δ and the deep cell c₀ ⇒ "w is conjugate to the deep relator r".

**What the hypothesis gives.**
- N_deep = 1 makes "touches ∂Δ" automatic for every other cell, so the only content is "touches c₀": Δ equals the closed star of c₀.
- Then Δ∖int(c₀) is an annular (possibly pinched) diagram whose inner label is r and outer label is w, and by cutting along a path from ∂Δ to c₀: **w ≡ (product of ring-cell conjugates) · u r^{±1} u⁻¹ in F(a,b)**.
- Hence w is conjugate to r^{±1} in **F/⟨⟨ring relators⟩⟩** (Lyndon–Schupp V.5). Nothing stronger follows.

**Is that the claimed implication?**
- *In the free group F: no.* Counterexample: the 3×3 grid of [aⁿ,bⁿ]-type cells (Developer's report). All hypotheses hold, and the boundary word has length 12n, not a rotation of the centre cell's 4n-letter relator.
- *In the group G = F/⟨⟨R⟩⟩ (B(2,5) presentation): vacuous.* Every trivial word is conjugate to every relator.
- *In F/⟨⟨ring⟩⟩: true, but informative only if r ∉ ⟨⟨ring⟩⟩.* In the grid case the centre has the same relator class as the ring cells, so r ∈ ⟨⟨ring⟩⟩ and the statement says nothing.
- So the guard's justification "the word is conjugate to a relator, therefore not novel" holds only as "w is the one-step ring extension of r modulo the ring relators". Whether that is non-novel is a policy decision, not a theorem.

**Data: the guard does not fire where it was meant to.** The motivating E1c cases (10 compressed chain words with one deep cell, 9 of them the relator #212):
- Wrapped flag, Developer's branch and my independent test: **0 of 10**. Also 0 of 43 E1d and 0 of 2 E1_screen single-deep words.
- Reason: the deep cell is enclosed by **2–4 cells, and 3–5 other cells do not touch it at all.** For #212 the enclosing cells share 28, 27, 8 and 1 vertices with it (60 total), and the other 4–5 cells hang off as a chain. For top-8 (#1010-type, 59 letters) two cells enclose it (31 and 30 shared vertices). The "ring of 6–9 cells around r" in [[2026-10-14-depth-followups]] is not what the diagrams look like.
- Developer's xfail test `test_e1c_single_deep_cases_are_flagged_wrapped_relator` reached the same result independently.
- Exact check in the free group (`guard_exact.py`): cyclically reduced w equals a rotation of a table relator (or inverse) for **0 of 611** T-016 finalists. So none of them is conjugate in F to a relator either.

**Corrected condition (my recommendation).**
- *Gate novelty only on exact, sound tests:* (i) w conjugate in F to a table relator or inverse (cyclic reduction + least rotation; implemented in `guard_exact.py`), (ii) the existing reducer-equivalence. Both are sound and checkable. They fire on 0 of 611 current finalists.
- *Keep the geometric pattern as a non-gating diagnostic*, renamed "enclosed relator (closed star)" and stated as "w ~ r in F/⟨⟨ring⟩⟩".
- *If the owner wants a geometric gate anyway,* use G* := N_deep = 1 ∧ all other cells touch c₀ ∧ the relator class of c₀ (up to inverse and rotation) is not among the ring cells' classes. G* is sound for the statement "w ~ r^{±1} in F/⟨⟨ring⟩⟩ with r a relator not repeated in the ring" and does not flag the 3×3 grid of identical cells. It still does not prove r ∉ ⟨⟨ring⟩⟩ (undecidable in general), so label the output "wrapped relator (modulo ring)", not "conjugate to a relator".
- It does not catch: a dangling cell that touches ∂Δ but not c₀ (guard silent, word reported novel); a ring that closes around a core of 2 or more cells; singular diagrams with several disc components (apply the guard per component); any certificate where the compression found a different diagram. **A guard that does not fire never certifies novelty.**

## 3. Conjecture: no chain word has a connected deep core of size 2
**Status: false for compressed certificates.**
- Branch `deep_core` on the compressed T-016 certificates: **E1_screen: 8 of 203 words have N_deep = 2 with deep_core = 2** (top-1, 9, 10, 48, 52, 83, 84, 95; N = 6–9). E1d has 3 words with N_deep = 2, deep_core = 1 (not adjacent); E1c has none.
- I checked top-1 and the other seven by edge classes: the two deep cells are different table relators (#1010 and #962 for top-1), reducedness pairs = 0, and they share a **28-edge path**. They are not cyclic inverses of each other and not equal.
- My first adjacency test (`rule_real.py`) read only directly matched letters and reported components [1,1] for these words; it missed adjacency through folded stems. Edge classes are the correct notion, and Developer's `deep_core` uses them. My earlier counts of deep components in that script are superseded.
- All eight are below N = 16, so none is area-like; the rule is unaffected there. But "chain-derived words never have a connected deep core" cannot be used to justify the clause.

**What does hold (proved).** If the dual graph is a tree (b₁ = 0) and the diagram is sphere-free, then N_deep = 0.
- By b₁ = V_int − s, V_int = 0: no interior vertex of degree ≥ 3.
- A deep cell has all vertices interior, so all of degree 2 in the collapsed sense, so its whole boundary is one shared path with a single neighbour: a cancelled sphere.
- So raw tree-like chains have N_deep = 0, and each deep cell needs b₁ ≥ 1. A deep core of 2 needs at least four cells in total and b₁ ≥ 2 (two ring cells meeting at both ends of the shared path).

## 4. Developer's branch 23-final-area-rule-wrapped-guard @ 7da39e4 (diagram.py, diagram_stats.py)
Checked by reading the diff and running `stats()` on the compressed certificates of T-016 E1c, E1d, E1_screen (611 words) next to my independent peeling (`branch_check.py`, `rule_real.py`, `core_debug.py`). I could not run the branch's pytest (no pytest installed here); the checks below are my own.
- **`shape`**: matches the final rule and the owner's classes; my classifier gives identical labels on all families in §1 (N_deep, maxdepth, T's, core). Correct. `n >= 16` guards the `None` T values.
- **`deep_core`**: edge-class based, point contacts and loops excluded. Correct; agrees with my edge-class check on the 11 words with N_deep = 2.
- **`depth_sum`**: 5×5 grid gives 8·1 + 1·2 = 10 (also in the branch's test), matching Math Expert's 10/|w̄|. Unreached cells count 0; valid under the sphere-free precondition that `stats` asserts.
- **`objective_J`**, `J_v1`, `shape_v1`: formula as specified; the earlier definitions are preserved.
- **`is_wrapped_relator`**: implements the owner's wording exactly. It over-flags the 3×3 grid (§2) and flags none of the E1c cases. Not a coding error.
- **Verdict on the branch:** math-correct. Merge is fine for `shape`, `deep_core`, `depth_sum`, J. Do not let `wrapped_relator` gate novelty until the condition in §2 is chosen; keep it as a diagnostic field.

## Verdict
`#status/conjectured` for the rule as a classifier; `#status/disproven` for the size-2 core conjecture (8 counterexamples among compressed T-016 E1_screen words); the guard is not sound as worded (§2). Premise: everything is about certificates, not about the words' true areas.

## Notes for downstream agents
- T-018 may use `shape`, `deep_core`, `depth_sum` and J as written. Report area-like only with the caveat of §1, and log the (N, maxdepth) pairs for the fit.
- Remove `wrapped_relator` from the novelty gate; add the exact conjugacy test (`guard_exact.py` logic). If the geometric guard is kept, use G* and the name in §2.
- Math Expert: the E1c single-deep diagrams are caps of 2–4 cells plus a chain tail, not annular wraps; the template idea (ring diagrams around #212) should use the actual piece pattern 28/27/8/1.
- Owner decision needed: whether to require maxdepth ≥ 2 for the area-like label (§1), and whether a one-step ring extension counts as non-novel.

## 5. Merge-gate re-check — branch 23-final-area-rule-wrapped-guard @ ffa933d (diff 7da39e4..ffa933d)
Scripts: `scratch/branch_recheck.py`. I could not run the branch's pytest (not installed here); the checks are mine.
- **`shape`**: requires N ≥ 16, T_deep ≥ 0.5, T_depth ≥ 0.5, deep_core ≥ 2 and maxdepth ≥ 2, as amended. Boundary cases checked: full-score input gives area-like; maxdepth 1, deep_core 1, N < 16 and N_deep = 0 give thick strip, thick strip, small enclosed and path-like.
- **Exact novelty test** (`novelty.conjugate_to_relator`, `relator_class_key`): compared with a brute-force rotation set (cyclic reduction, all rotations, inverse) on 4,000 random words: conjugates, inverse conjugates, one-letter perturbations and random words, including v⁵ relators. **0 mismatches** (1,998 positives, 2,002 negatives). The key is sound: it is equality of cyclic reductions up to rotation and inversion, which is exactly conjugacy in F(a,b) to r^{±1}.
- **`enclosed_relator` (G\*)**: matches the corrected condition (N_deep = 1, every other cell shares a vertex with c0, class of c0 not among the other cells' classes). It is not read by the novelty path. On the 611 T-016 finalists: 0 flagged; `conjugate_to_relator`: 0 flagged; shape counts path-like 545, small enclosed 59, thick strip 7, area-like 0. Caveat: the class clause is exercised only by the unit test that edits `d.rels` on a folded hexagon ring, because no real certificate reaches that clause. The clause itself is a one-line set comparison on `d.rels`, which holds the relator word per cell.
- **Verdict: merge GO.** Math-correct; nothing else open from my side. Status of the rule remains `#status/conjectured` and the label a diagnostic.

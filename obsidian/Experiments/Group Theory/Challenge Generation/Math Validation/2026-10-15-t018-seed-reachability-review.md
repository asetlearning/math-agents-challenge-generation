---
title: "T-018 seed reachability and Fine-Wilf pruning — review"
status: replicated
domain: group-theory
project: challenge-gen
claim: "No 2- or 3-cell folded diagram over the R7 cells v^5 (|v| <= 7) has a 2.5-power-free outer boundary"
claimant: Math Expert (arguments A1-A3), Experimenter (enumeration, branch t018-diagram-search @ 4349ba3)
verification_method: "re-derivation of each bound; direct search of the real cell table for Fine-Wilf violations; independent hash-join enumeration of 2-cell, chain and triangle diagrams (no Fine-Wilf pruning, own C power detector); set-equality controls against the Experimenter's pipeline"
tools_used: ["python3 + t018 venv (numpy 2.4.4)", "gcc (scratch/seed/pw.c)", "scratch/seed/*.py"]
author: asetlearning
tags: [agent/validator, user/asetlearning, domain/group-theory, topic/b25, topic/van-kampen, topic/power-free-words, project/challenge-gen, status/replicated, proof]
---

# Review — T-018 seed reachability (N <= 3)
Triage: [[2026-10-15-t018-seed-reachability-triage]]. Sources: [[2026-10-15-t018-power-free-seed-reachability]]; code `t018/seed_enum.py`, `seed_enum3.py`, `patches.py` (unchanged between 4979927 and 4349ba3). Scripts: `Agents/asetlearning/Validator/scratch/seed/`.

**Terms.** A *cell* is a rotation of v^5 or its inverse, v primitive, cyclically reduced, |v| = ℓ ≤ 7 (the *move table*: 510 root necklaces, both orientations; I checked it is exactly all of them). An *arc* is a shared run of edges between two cells. A boundary is *2.5-power-free* if no window of length ⌈2.5h⌉ has period h. An *exposed run* is a contiguous piece of one cell on the outer boundary; it has period ℓ, so it must be shorter than T(ℓ) = ⌈2.5ℓ⌉. A cell with one arc of length s exposes 5ℓ − s, so s ≥ need(ℓ) = 5ℓ − T(ℓ) + 1 (3, 6, 8, 11, 13, 16, 18). A *chain* a−m−c has two end cells with one arc each; a *triangle* has three pairwise-adjacent cells around an interior vertex; a *lens* is a triangle where one cell is glued entirely (zero exposure) between two cells that then share a second arc.

## Verdict
| Item | Status |
|---|---|
| Fine-Wilf bound: distinct roots arc <= p+q−gcd−1; equal length <= p−1 | **proved**; **replicated** on the real table: no shared window one letter longer, bound attained for nearly all (p,q); inverse-root cells misaligned arcs <= p−2 |
| A1 single-arc cells (only \|v\| <= 3; partner lengths) | **proved** (arithmetic reproduced) |
| A2 recurrence cap (exposed run <= ℓ_L + ⌈2.5ℓ_s⌉ − 2) | **proved** (below) |
| A3 chain exclusion; survivors (2,3,7) arcs 7/8, (3,3,7) | **proved** given A1, A2; counting reproduced; **replicated** by independent enumeration |
| A4 example "all ℓ = 7, pairwise arcs 9" | **error in the example** (equal lengths allow <= 6); the claim "counting does not exclude triangles" stands (12 unordered triples feasible) |
| Experimenter pruning (60 of 343 triples) | **replicated** for ordinary triangles; **gap**: invalid for lens triangles (two cells sharing two arcs), 22 further length triples; gap closed below |
| Chain enumeration | **replicated**: 108 folded boundaries each, identical sets; the Experimenter skips nested end cells (arc = whole cell), I add 48 more; none power-free |
| "0 power-free 2- and 3-cell patches" | **replicated, independently**, over the 1,494-entry move table and also over all 16 R7 cell types (adds the 136 non-primitive u^(5k) entries); scope N <= 3 only |

## 1. Math Expert's bounds
**Fine-Wilf (both versions).** An arc is a factor of v_i^∞ and v_j^∞. If it has length ≥ p+q−g (g = gcd) it has period g; its p-window is then a power of a g-word, so primitivity forces g = p, and likewise g = q, hence p = q. Contrapositive: arc ≤ p+q−g−1 for p ≠ q. For p = q a length-≥p arc fixes the phase; same orientation would make v conjugate to v⁻¹ (impossible in a free group), opposite orientation makes the cells mirror images (a reducible pair, removable). So arcs ≤ p−1. I also measured it: for every length pair, windows of length H+1 shared by distinct-root cells: 0 (table of attained maxima equals H except where the 5-edge cell caps it).
**A1.** need(ℓ) ≤ H(ℓ,ℓ′) gives exactly (1, ℓ′ ≥ 4), (2, 7), (3, 7) (arc exactly 8); none for ℓ ≥ 4. Reproduced. N = 2: no pair satisfies both needs.
**A2.** If an arc of length ≥ ⌈2.5ℓ_s⌉ is shared, it contains a window W of period ℓ_s and length ⌈2.5ℓ_s⌉, which is also a factor of v_L^∞ and so recurs every ℓ_L letters. Any run of length ℓ_L + |W| − 1 in cell L contains a copy; hence exposed runs are ≤ ℓ_L + |W| − 2. Sound. Single-arc end cells satisfy the hypothesis since need(ℓ) ≥ ⌈2.5ℓ⌉.
**A3.** I enumerated all ends ℓ ≤ 3, middles ℓ_m, arcs and gaps: with A2 the only survivors are (2,3,7) (arcs 7 and 8, gaps 10 and 10, cap 10) and (3,3,7) (arcs 8, 8, total gap 19, cap 13 each); a single run (arcs meeting at a vertex) is excluded for all. Without A2 more survive ((1,1,4..7), (1,2,7), (1,3,7), (2,2,7)), so A2 does real work. The "17" in the proposal is T−1 for ℓ = 7 (the exposure bound), not the A2 cap (13 or 10); conclusions unchanged. Nested end cells (a^5 inside a 6- or 7-cell, arc 5) were not in the proposal's count; I checked them: all excluded.

## 2. Fine-Wilf pruning in the code
- **Triangle feasibility.** Recount: 60 ordered triples = 12 unordered, with or without a lower floor on arcs (every feasible solution has all arcs ≥ 3, so the code's floor of 2 is harmless).
- **Gap: lens triangles.** The test "sum of two FW bounds ≥ need(ℓ_i)" assumes each pair shares one arc. In a lens, cells j and k share two arcs and i has zero exposure, so the totals can exceed H and the triples outside the 12 are not excluded. My enumeration finds actual cell-level matches for 22 further unordered length triples (all involve a fully glued small cell, mostly ℓ = 1). None gives a power-free boundary (below), so the finding stands, but the docstring's pruning argument holds only for triangles with all three exposures positive. The `l >= min(n, len)` skips (nested cells) are likewise silent.
- **Maximal arcs.** Taking arcs maximal is sound: a folded diagram has maximal arcs, and a non-maximal gluing is a smaller or different diagram that is enumerated on its own. At the interior vertex the three edge labels are pairwise distinct (folded), which gives maximality of the anchor arc. Vertex and stem attachments: a cell with only point attachments has at most 2 exposed runs of total 5ℓ > 2(T−1), so N <= 3 diagrams are connected through arcs; chains, triangles and lenses are the only shapes.

## 3. The "0 power-free" claim — independent enumeration
Method: cells u^5 for every primitive cyclically reduced word u (|u| <= 7), all rotations and orientations. Arc lengths are bounded by the *measured* maximum arcs, not Fine-Wilf. Diagrams are built by prefix/suffix hash join (2-cell: R_i = p y, R_j = y⁻¹ q; chain: R_m = U1 G1 U2 G2; triangle: R_i = A_i X_i A_j⁻¹ etc.). Exposure gate X < T only where valid (no gate if some cell is fully glued). The final test is my own C detector, checked against a naive Python test and `powerfree.py` on 56,543 random cyclic words (0 disagreements, 45,587 with a power).

| Family | candidates | power-free (>= 8 letters) |
|---|---|---|
| 2-cell | 0 reach the needs | 0 |
| chains, primitive cells (incl. nested ends) | 3,032 | 0 |
| chains, all 16 R7 cell types | 21,484 (13,512 are empty or length-5 boundaries) | 0 |
| triangles + lenses, primitive cells | 383,760 | 0 |
| triangles + lenses, all 16 cell types | 388,992 | 0 |

**Controls against the Experimenter's pipeline (positive control for the triangle final stage).** The triangle path reaches no third cell under the real gate, so the last stage is never exercised. With the exposure gate removed (all arcs ≥ 2) and the power test replaced by a mild one (no 4.5-power), the Experimenter's pipeline emits tens of thousands of boundaries and my independent join emits the same sets: (3,4,5) 384 = 384, (3,5,7) 12,576 = 12,576, (3,6,7) 37,728 = 37,728, (4,4,7) 5,824 = 5,824, (4,5,6) 12,416 = 12,416 (mild-power-free positives equal too, e.g. 11,520 of 12,528 for (2,6,7)). The only differences, 48 boundaries for (2,6,7), are lens boundaries that my "all exposures positive" control model leaves out (re-included, all 48 match). Chains: identical 108 boundary sets. So the machinery, including its last stage, is replicated; the real predicate reaches zero because no candidate passes the exposure gate.

**How close is N <= 3?** Smallest maximal exponent over all N <= 3 boundaries I enumerated (gate at forbidden exponent 3.0): chain 2.5 exactly (e.g. a 25-letter boundary with a window BABAB), triangle/lens 3.5, 2-cell 3.57. 2.5-power-free needs < 2.5, so the best chain fails by the boundary value; no 3-cell boundary is 3.0-power-free except chains (80 at 3.0).

## Caveats (scope of what is established)
1. N <= 3 only. Nothing about N >= 4; counting does not exclude anything there (A5), and the dataset finding (491 of 820 words cyclically power-free and trivial in G7, no certificate) settles b2 only for large diagrams.
2. Cells are the R7 relators v^5 and (replicated) u^(5k); "folded, reduced diagram" is WLOG for a given boundary word.
3. A shape argument (chain, triangle, lens, vertex/stem excluded by counting) rather than an enumeration of the topology; I believe it complete for three cells.
4. Property of one family of presentations, not of the free group B(2,5).

## Addendum 2026-10-16 — remaining positive controls
The same gate-off control (all arcs ≥ 2, mild 4.5-power test), one length triple per capjob (2G, 1 CPU).
- Added: (4,5,7): 38,784 = 38,784 boundaries, mild-power-free 32,624 = 32,624. (5,5,6): 20,592 = 20,592, mild 16,864 = 16,864.
- Compared in total: 8 of the 12 feasible unordered triples, plus (2,3,4). Every one agrees exactly, apart from the lens boundaries for (2,6,7), which are explained in §3.
- Not compared: (4,6,7) and (5,5,7) were killed at the 2G cap (the Experimenter's `triangle_exhaustive` keeps every positive boundary in memory under the mild test); (5,6,7) and (6,6,7) were not run. Following the capjob rule I did not raise the cap. I judge an rjob run unnecessary: the machinery is already replicated on 8 triples, and the real (2.5) result does not depend on this control, because my own enumeration covers all triples.
- Process note: on 2026-10-16 my earlier 6-way parallel run of this control (no cap) was very probably the job that triggered the OOM kills. All later runs went through capjob.

## Addendum 2026-10-16 — Math Expert's R8/R9 counting ([[2026-10-16-r8-r9-move-set]] §1)
Same method as for A1–A3: brute force over root lengths ≤ K, arcs between need(ℓ) and the Fine-Wilf bound (capped at the shorter cell, nested arcs allowed), gaps capped by T(ℓ_m) − 1 and by the A2 recurrence cap. Script `scratch/seed/r89_count.py`.
- **Single-arc pairs: confirmed.** R8 adds (1,8), (2,8), (3,8); R9 adds (1,9), (2,9), (3,9), (4,9). No ℓ ≥ 5 is admissible with ℓ′ ≤ 9. The stated inequality ℓ′ ≥ ⌊2.5ℓ⌋ + 2 − ℓ + gcd is need(ℓ) ≤ H(ℓ,ℓ′), rearranged.
- **Chain survivors: confirmed exactly.**
  - Middle 7: (2,3) with arcs 7, 8 and (3,3) with arcs 8, 8.
  - Middle 8: (3,3), arcs 8–9 against H = 9.
  - Middle 9: (3,3) with arcs 8, 8; (3,4) with arcs 8, 11; (4,4) with arcs 11, 11.
  - All are at or within 1 of the Fine-Wilf maximum. The closed form ℓ_m ≤ e₁+e₂−g₁−g₂+2p_min−6 is the A2 cap with both arcs at their maximum. My count also applies the per-gap T−1 cap and the cell-length cap; neither changes the list.
  - As at R7 (where (2,3,7) had no actual cell match), these are counting survivors only. Existence needs the enumeration.
- **"Boundary cells with ℓ ≥ 5 always need ≥ 2 internal arcs": true only as "not a single arc with one exposed run".** The counting excludes a cell whose exposure is one run. A cell can also have one arc plus other cells touching its exposed part at vertices, or only vertex/stem contacts. Its exposure then splits into several runs, each < T(ℓ). With k contact points a cell can survive with total exposure up to about k·(T−1) (a 5-cell: one arc of length ≥ 1 plus one vertex contact suffices numerically; three contact points and no arc at all). For N ≤ 3 this was excluded by counting; for N ≥ 4 it is not. Correct statement: such a cell needs at least 2 separate attachments (arcs or contact points). A pre-filter for larger seeds must not require 2 arcs.

**Verdict:** §1 counting **proved** (replicated exactly), with the one correction to the "≥ 2 internal arcs" phrasing.

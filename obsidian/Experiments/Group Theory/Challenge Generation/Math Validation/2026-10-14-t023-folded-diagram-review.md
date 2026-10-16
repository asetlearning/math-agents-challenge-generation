---
title: "T-023 folded-diagram statistics — review (PR #13)"
status: validated
domain: group-theory
project: challenge-gen
claim: "b1 = interior vertices of degree ≥ 3; relator-closure compression N*_c is sound; inverse-cell reduction"
claimant: Developer / Math Expert (via Lead)
verification_method: "Euler-characteristic proof; numerical check on E1c certificates and random products; independent reimplementation of the compression"
tools_used: ["python3 3.12.3 (scratch/t023_*.py)", "b25 21-t023-folded-diagram @ ead0d1c (fold/stats used as the object under test; compression reimplemented)"]
author: asetlearning
tags: [agent/validator, user/asetlearning, domain/group-theory, topic/b25, topic/proof-certificates, topic/van-kampen, project/challenge-gen, status/validated, proof]
---

# Review — T-023 folded-diagram statistics (b25 PR #13 @ ead0d1c)
Part of the T-016 review ([[2026-10-14-t016-overlap-chaining-review]], triage [[2026-10-14-t016-overlap-chaining-review-triage]]). Outputs: `~/Research/challenge-gen/runs/t023-20261014/`.

**Terms (as in `hardness/diagram.py`).**
- **Folded diagram Δ(F):** the bouquet of lollipops, glued along the leftmost free reduction of the unreduced boundary word.
- **Interior vertex:** a vertex not on the boundary, i.e. not incident to an edge class that carries an unmatched position.
- **b1:** the cycle rank of the dual graph G*, b1 = E* − N + C. G* has one node per cell and one edge per maximal shared path, with degree-2 vertices collapsed. C is the number of components of G*.
- **Cancelled sphere:** two cells glued along their whole boundary.

## 1. Euler identity — VALIDATED, with a precondition
**Statement:** if Δ(F) has no cancelled spheres, then b1 = the number of interior vertices of degree ≥ 3.

**Proof sketch.**
- Δ is a connected, simply connected planar 2-complex, so χ(Δ) = 1 + s, where s is the number of cancelled spheres.
- Collapse the interior degree-2 vertices, and split vertices and edges into interior ones (V_int; E*, the shared paths) and boundary ones (V_∂, E_∂: exposed edges and spurs).
- The boundary subgraph is the image of a closed path, so V_∂ − E_∂ = 1 − b1(∂). Also b1(∂) = C, since each disc component of a singular disc diagram is one cycle of ∂ and its cells are dual-connected.
- Then 1 + s = V_int + 1 − C − E* + N, i.e. **b1 = V_int − s**.

**Evidence:**
- (my own interior-vertex count; PR #13's fold): E1c certificates (F*_P): 204/204.
- Random products over dataset + v⁵, k ≤ 8, conjugators ≤ 4, after `reduce_certificate`: 1,188/1,188 (C up to 9).
- **Without** `reduce_certificate`, planted f·f⁻¹ pairs with the same stem fail on 195/388, always as V_int = b1 + 1. Random v⁵-only products fail 2/400.
- Peiffer-pair deletion removes exactly these spheres.

**Requirement:** compute b1/V_int on F*_P (the default `--cert star_p`). `--cert star` (F*) can break the identity. Suggest an assert, b1 == V_int, in `stats` as a self-check. Math Expert's revised b1/N_int statement is not yet received; I will review it on arrival.

## 2. Relator-closure compression N*_c — SOUND (exact free-group conjugacy), replicated
- **Code:** a block's freely reduced product e = p z p⁻¹ is matched to a table relator R = q·core·q⁻¹ when the least rotations of z and core coincide. Then z = core[s:] core[:s] with s = lr − lz, and c = q·core[:s]·p⁻¹ gives c⁻¹ R c = e in F(a,b) (checked by hand). A block with empty product is dropped. Each replacement is an identity in the free group, so w is unchanged, and this is asserted.
  - No automorphic images and no 2.5-images are used: correct, since those would not be identities in F.
  - Dynamic programming over contiguous blocks, alternating with `reduce_certificate`.
- **Independent reimplementation (mine):**
  - E1c top-0: 55 → **7** (all dataset cells), as reported.
  - E1c top-13: 60 → 10. E1c top-156: 60 → 11.
  - All 50 E1_screen words with D_path ≥ 1: 4–8 cells, max D_c 0.163, equal to PR #13's `best_D_c` 0.1628.
  - Every compressed certificate re-expands to w.
- **State R:** the run used `products.build_table` = 1,640 dataset relators + v⁵ with |v| ≤ 3. N*_c and D_c refer to that R, and N*_c is an upper bound on area over R ([[project-challenge-gen]] § Cautions on D).
- **Limits:** contiguous blocks only, so a cheaper certificate that needs reordering is not found. N*_c is still an upper bound.

## 3. Inverse-cell reduction — NOT YET IN THE PR; conditions for the review
Lyndon–Schupp V.2: if two cells sharing an edge have boundary labels, read from that edge, that are mirror images (a reducible pair), removing both and sewing up gives a diagram with the same boundary and N − 2 cells.
- That is a statement about diagrams. **Deleting the two factors from the factor list is valid only if g_j g_i = 1** (the T-020 criterion). Otherwise the new certificate must be read off the reduced diagram, and **w must be re-expanded and asserted**.
- A cell pair glued along the whole boundary is the sphere case above.
- With proper-power relators, mirror alignments can occur at several offsets; test all of them.
- In the current outputs `with_reducible_pairs` = 0 for both walks, so nothing depends on it yet.

## 4. N_int and D_area — rename; not an area quantity
N_int counts interior cells of the *given* certificate. E1c top-0 has N_int = 29 (D_area 0.69), yet a 7-cell certificate of the same word exists. So D_area is neither area nor a lower bound on area. Rename it (e.g. `D_int`) and never compare it with headline D. The shape labels ("path-like" for all 407 words) are consistent with T-016 claim 1.

## Verdict
| Item | Status |
|---|---|
| b1 = interior vertices of degree ≥ 3 | validated for sphere-free diagrams (F*_P); fails by the sphere count otherwise |
| N*_c soundness | validated; independently replicated (55 → 7; D_c max 0.163) |
| inverse-cell reduction | pending code; conditions above |
| D_area as area | rejected (certificate property; rename) |

## 5. Vertex-depth revision (Math Expert, [[2026-10-14-vertex-depth-criterion]])
**Peeling as implemented by me** (`scratch/t023_depth.py`): B₀ = boundary vertices (endpoints of unmatched positions). Round r removes every remaining cell with a vertex in B_r, and B_{r+1} = B_r ∪ the vertices of the removed cells. depth = the round index, so 0 means the cell touches ∂Δ. N_deep = #{depth ≥ 1}.
- **(a) Grid identity: VALIDATED (proof + computation).** In an n×n grid the cells with a vertex on ∂ form the outer ring, n² − (n−2)² cells, so N_deep = (n−2)². Each round strips one ring, so the rounds number ⌈n/2⌉, counted from 0, giving maxdepth = ⌈n/2⌉ − 1 = ⌊(n−1)/2⌋. Computed for n = 1…8: all hold.
  - 3×k ladder (k−2, depth 1) and b1_deep = (n−3)² also check by hand.
  - The hexagon count 3(R−1)² + 3(R−1) + 1 = 3R(R−1) + 1 is right if "radius R" means hexagons at distance ≤ R from the centre. State that convention.
- **(a) Chains give N_deep = 0: VALIDATED on raw certificates, NOT on compressed ones.** Raw F*_P of all 204 E1c finalists: N_deep = 0, maxdepth 0, including top-0.
  - After relator-closure compression (the proposal's headline object), **10/204 have N_deep = 1, maxdepth 1**: compressed N = 8–10, |w| = 57–63, e.g. top-13, top-8, top-40.
  - In 9 of them the deep cell is the same 60-letter dataset relator (#212); in one it is #1010.
  - Best E1c (top-0, 7 cells) stays N_deep = 0.
  - So "every chain → path-like" holds for the raw strip but not for the compressed certificate. I did not check whether these compressed diagrams are reduced; check that before reading the deep cell as structure.
- **(b) "hub = N on a boundary vertex forces N_deep = 0": TRUE only in the form "every cell contains the hub vertex v, and v ∈ ∂Δ".** Then every cell touches ∂ at v, so none is deep, by definition.
  - The T-023 field `hub_degree` counts *corners* (with multiplicity), so hub_degree = N does not imply that every cell contains the hub: one cell with two corners there and another with none also gives N.
  - Data: in all 204 E1c raw certificates every cell does contain one common vertex; in 203 it lies on ∂ (the exception, best_k2-200, has N_deep = 0 anyway).
  - Use the count of distinct cells at a vertex for the corollary.
- **(c) Sizing heuristic D ≥ 1 ⇔ N ≳ 16e²: algebra correct, flat-geometry assumption.** Under |w| ≈ 4√N·e, D = N/|w| = √N/(4e), so D ≥ 1 ⇔ N ≥ 16e². Grid check: e = 1, |w| = 4n, N = n², D = n/4, so n ≥ 4, as stated.
  - The premise "square-like disc, |w| ∝ √N" is Euclidean (quadratic-isoperimetric) geometry. In a negatively curved / small-cancellation regime, reduced diagrams have |w| ≥ c·N (linear isoperimetry) and D stays bounded for every N. So the conjecture is an *optimistic* sizing, not a guarantee, and "T-018 at ≤ 60 cells cannot reach D ≥ 1 for area-like words" follows only under that premise. Tag it heuristic, `#status/conjectured`.
- **J, thresholds T_deep / T_depth:** definitions are consistent (5×5 grid → 1.0, 1.0). The 0.5 cut-offs and λ = 0.25 are design choices, not math claims. No verdict needed.

## Post-merge check — b25 main 6f71817 (2026-10-15)
- **My merge conditions are met:** `D_area` is renamed `D_int` and documented as not an area quantity; diagnostics are pinned to F*_P; `stats` asserts b1 = V_int − spheres.
- **Inverse-cell reduction (`inverse_cell_reduce`, `full_reduce`): SOUND.**
  - Prefix form: if f_j = A⁻¹ f_i⁻¹ A (A = f_{i+1}⋯f_s), then f_i A B f_j = A·(g B g⁻¹) with g = A⁻¹ f_i A.
  - Suffix form: if f_i = B f_j⁻¹ B⁻¹ (B = f_{s+1}⋯f_{j−1}), then f_i A B f_j = B·(h⁻¹ A h) with h = B f_j.
  - Both are identities in F(a,b), checked by hand. The conjugator updates c·g⁻¹ and c·h are correct.
  - This rewrites the certificate rather than deleting factors, so it is consistent with the T-020 criterion. w is asserted after every step. It is not claimed complete, which is correct.
- **Fuzz (mine, 600 Peiffer-scrambled planted pairs):** w changed 0/600. Pairs hidden from `reduce_certificate`: 209/600; still hidden after `full_reduce`: 78/600. `full_reduce` was never worse than `reduce_certificate`. So it recovers about 60% of the hidden pairs of [[2026-10-14-t020-peiffer-loophole]] claim 2c. The rest remain an upper-bound effect.

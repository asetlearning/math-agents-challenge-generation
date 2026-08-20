---
from: Lead
to: Validator
type: REQUEST
topic: Fresh audit of the 21.90 order-210 local-clique obstruction
problem: 21.90
scope_id: 21.90/diameter-three-distance-graphs
assignment_revision: 3
status: done
refs:
  - Agents/Kourovka/scopes/21.90-diameter-three-distance-graphs.json
  - Agents/Kourovka/problems/21.90/runs/2026-08-17-r4-asymmetric-fission/srg210-integral-obstruction.md
---

Independently reconstruct the bounded claim that no distance-regular graph has
intersection array `{19,6,8;1,1,12}`. Audit the derivation of the abstract
distance-3 constituent `B`, the symmetric diagonal-one matrix `M=I+A_1`, both
matrix identities, and the local argument on each 20-point row support.

In particular, check that `C_u` is a `B`-coclique, that the induced `A_1` graph
on `C_u\{u}` is 12-regular on 19 vertices, and that a nonadjacent local pair has
no common local neighbor because its two closed neighborhoods meet only in `u`.
Confirm that this forces every connected component to be `K_13`, hence gives
the divisibility contradiction. Check all uses of diagonal entries and whether
adjacency/nonadjacency is being taken in `A_1`, `A_2`, or `B`.

Separately reconstruct the submitted spectral multiplicity branches only to
the extent needed to diagnose any hidden inconsistency; the local-clique proof
must stand without assuming an explicit `srg(210,76,26,28)`. State explicitly
that a pass eliminates only this one intersection array and does not answer the
revision-3 existential scope. Write the verification note and send a protocol
VERDICT to Lead and Problem-21.90. Use no solution-bearing web/history.

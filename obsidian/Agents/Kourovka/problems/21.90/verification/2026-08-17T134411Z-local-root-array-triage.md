---
title: "Verification triage — Kourovka 21.90 — local-root array exclusion"
problem: "21.90"
scope_id: 21.90/diameter-three-distance-graphs
scope_record: Agents/Kourovka/scopes/21.90-diameter-three-distance-graphs.json
assignment_revision: 3
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/distance-regular-graphs, topic/root-systems, project/kourovka, status/draft]
---

# Verification triage — Kourovka 21.90 — local-root array exclusion

## Claim restated

No distance-regular graph has intersection array
`{17,8,6;1,2,12}`.  This is an exact one-array nonexistence claim only; it is
not a claim that revision 3 of Kourovka 21.90 has a positive or negative answer.

## Locked scope and clause matrix

- `scope_id`: `21.90/diameter-three-distance-graphs`
- `assignment_revision`: 3
- active target: existence of a Q-polynomial distance-regular graph of diameter
  3 whose distance-2 and distance-3 graphs are nontrivial strongly regular
  graphs under the source-operational convention
- excluded scopes: none in the canonical record; revision 2's disconnected cube
  candidate is superseded by revision 3

| source clause | active | answered by the one-array claim? |
|---|---:|---:|
| `Gamma_i` has the same vertices and adjacency exactly at distance `i` | yes | no |
| existence of the required diameter-3 Q-polynomial distance-regular `Gamma` | yes | no; only one possible array is excluded |

`active_assignment_answered: pending` during triage.

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | required condition | use in this partial | triage result |
|---|---|---|---|---|
| `21.90-exists-Gamma` | admissibility | one graph satisfies all rows | no graph is supplied | unresolved |
| `21.90-diameter-3` | admissibility | diameter exactly 3 | a hypothetical graph with the displayed diameter-3 array | conditional only |
| `21.90-Q-polynomial-distance-regular` | admissibility | Q-polynomial distance-regular | the proof uses distance-regularity only | unresolved globally |
| `21.90-distance-graph-definition` | admissibility | adjacency exactly at distance `i` | not used | unresolved globally |
| `21.90-Gamma2-strongly-regular` | admissibility | nontrivial strong regularity of `Gamma_2` | not used | unresolved globally |
| `21.90-Gamma3-strongly-regular` | admissibility | nontrivial strong regularity of `Gamma_3` | not used | unresolved globally |
| `21.90-existence-conclusion` | target conclusion | at least one target graph exists | neither established nor refuted | unproved |

No revision-3 `claim-checks/*.json` is present.  The only claim check belongs to
the superseded revision-2 cube candidate.  Thus this request cannot promote a
full-scope claim, independently of the one-array audit.

## Target versus witness

- source target: an actual graph satisfying every revision-3 row, read from the
  visually rendered Notebook page 177;
- object of the submitted partial: the class of hypothetical distance-regular
  graphs with the one displayed intersection array;
- witness equals source target: false as a scope statement, because excluding one
  array does not decide existence across all arrays;
- witness equals exact partial target: yes by definition, provided the proof uses
  only consequences of the displayed array.

## Subclaims

1. The intersection matrix has eigenvalues `17,9,-1,-3`, and the primitive-
   idempotent restriction gives every nonprincipal local eigenvalue `eta` the
   bounds `-9/5 <= eta <= 3`.
2. `2I+A` is an integral positive-definite rank-17 Gram matrix whose norm-two
   lattice roots form one irreducible simply-laced crystallographic root system.
3. Classification leaves exactly `A_17` and `D_17`.
4. In `A_17`, independence gives a support tree and 8-regularity of its line
   graph gives an impossible endpoint-degree equation.
5. In `D_17`, the signed support multigraph is connected unicyclic; repeated
   supports and the remaining simple-support case must each contradict
   8-regularity.  The repeated-support proof must explicitly control possible
   second parallel pairs and all coordinate signs.
6. The one-array object is the active revision-3 target.  This fails: it is only
   one conditional parameter case.

## Tools and methods inventory

- source comparison: rendered page image plus `pdftotext 24.02.0`; proves source
  fidelity, not the claimed graph nonexistence;
- exact hand tridiagonal expansion and cosine recurrence; proves the stated local
  spectral interval, not existence of the local graph;
- integral-lattice and finite crystallographic-root-system argument; proves the
  rank-17 type reduction if positivity, integrality, spanning, and irreducibility
  all pass;
- standard classification of irreducible simply-laced crystallographic root
  systems; proves completeness of the `A_17/D_17` list at rank 17;
- signed-support graph analysis; can prove contradictions in both types, but must
  separately audit parallel supports in `D_17`;
- Python 3.12.3 is available but unnecessary; GAP 4.12.1 is installed but every
  GAP call is heavy under the common protocol and is neither authorized nor
  needed; Sage and Magma are absent.

## Hard limits and recommendation

Proceed with a hand-only line-by-line verification of the exact array claim.  A
pass proves only that no distance-regular graph realizes this array.  Keep
`active_assignment_answered:no`, do not promote the Type-II(ii) classification or
the revision-3 existential target, and cap the protocol status at
`status/conjectured` while the revision-3 claim-completeness gate is absent.

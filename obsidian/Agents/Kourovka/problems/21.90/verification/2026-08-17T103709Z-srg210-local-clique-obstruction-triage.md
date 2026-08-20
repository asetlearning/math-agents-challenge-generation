---
title: "Verification triage — Kourovka 21.90 — order-210 local-clique obstruction"
problem: "21.90"
scope_id: 21.90/diameter-three-distance-graphs
scope_record: Agents/Kourovka/scopes/21.90-diameter-three-distance-graphs.json
assignment_revision: 3
claim: "No distance-regular graph has intersection array {19,6,8;1,1,12}."
claimant: Problem-21.90
active_assignment_answered: pending
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/distance-regular-graphs, project/kourovka, status/draft]
---

# Verification triage — Kourovka 21.90

## Claim and exact scope

The routed bounded claim is that no distance-regular graph has intersection array
`{19,6,8;1,1,12}`.  The active revision-3 source target is much broader: existence
of a Q-polynomial distance-regular graph of diameter three whose distance-2 and
distance-3 graphs are nontrivial strongly regular graphs.  A pass can eliminate
only this one array; it cannot answer the active existential assignment.

No `claim-checks/*.json` was linked or created for this artifact.  The routed note
is labelled `PARTIAL_RESULT`, not a whole-scope `CLAIM`; the missing file is still
recorded as a completeness-gate limitation and no whole-scope status will be
inferred.

## Scope, revision, and clause matrix

| source clause | active? | bounded claim answers | remains |
|---|---:|---|---|
| Definition of `Gamma_i` by distance `i` on the same vertex set | yes | uses the distance matrices `A_i` of a hypothetical graph with the one array | all other parameter arrays |
| Existence of a Q-polynomial diameter-3 graph with `Gamma_2,Gamma_3` strongly regular | yes | excludes one intersection array, even without Q-polynomiality | the existential question over every other array |

`active_assignment_answered: pending` at triage and necessarily `no` even if the
bounded proof passes.

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | proof use / candidate value | triage result |
|---|---|---|---|
| `21.90-exists-Gamma` | admissibility | contradiction assumes only a hypothetical graph with the one array | partial only |
| `21.90-diameter-3` | admissibility | the array has four distance relations `A_0,...,A_3` | to verify |
| `21.90-Q-polynomial-distance-regular` | admissibility | Q-polynomiality is not used; an array-level contradiction would be stronger | to verify as a valid strengthening |
| `21.90-distance-graph-definition` | admissibility | `B=A_3` and `A_1=M-I` must be kept distinct | to verify |
| `21.90-Gamma2-strongly-regular` | admissibility | not used by the claimed contradiction | not answered globally |
| `21.90-Gamma3-strongly-regular` | admissibility | claimed to follow abstractly for `B=A_3` from the array | to verify |
| `21.90-existence-conclusion` | target conclusion | eliminating one array cannot decide existence | not established |

## Target versus witness and circularity

The source target ranges over every graph satisfying revision 3.  There is no
concrete witness: the proof works inside an arbitrary hypothetical distance-regular
graph with the stated intersection array.  This conditional object is exactly the
bounded target class but is only a proper subcase of the source target, so
`witness = source target` is false.  The matrices must be derived from distance
relations, not constructed by imposing the desired identities; that provenance is
the central circularity check.

## Subclaims

1. The array gives sphere sizes `(1,19,114,76)` and `v=210`.
2. Its distance matrices give a symmetric zero-one `B=A_3`, and `D=I+B` obeys
   `D^2=49I+28J` without assuming an explicit SRG exists.
3. `M=I+A_1` is symmetric zero-one, has diagonal one and row sum 20, and the
   intersection recurrence gives `M(D+7I)=8J` and
   `M^2=7I+13M+J-D`.
4. The trace equations have exactly the two submitted nonnegative integral
   multiplicity branches, and the mixed identity removes the branch containing
   eigenvalue 13.
5. Every row support `C_u` is a `B`-coclique.
6. The induced `A_1` graph on `C_u\setminus\{u\}` is 12-regular, while two
   nonadjacent local vertices have no common local neighbor.
7. Those local facts force components `K_13`, contradicting 19 vertices.
8. The contradiction eliminates only this array, not revision 3.

## Tools available

- GAP 4.12.1 is installed.
- Python 3.12.3 is installed.
- Poppler `pdftotext` 24.02.0 and `pdftoppm` are installed.
- Sage and Magma are unavailable.

The source was extracted from PDF page 177 and visually checked against the
rendered page.  No solution-bearing web or history was used.

## Methods inventory

| subclaim | method | what a pass proves | what it does not prove |
|---|---|---|---|
| 1--3 | direct distance-matrix recurrence, checked line by line | the matrices and identities are necessary for this array | existence of any graph or sufficiency of the identities |
| 4 | exact trace arithmetic plus a small independent integer checker | the submitted branches and mixed-equation rejection are arithmetically correct | existence/nonexistence by itself |
| 5--7 | direct support-count and elementary graph proof | the array is impossible if every relation label and diagonal term checks | any other intersection array |
| 8 | source/scope comparison | the precise partial scope | the revision-3 existential answer |

## Hard limits and recommendation

No catalogue, explicit `srg(210,76,26,28)`, SAT search, or graph construction is
needed or authorized.  Full hand verification of the one-array implication is
feasible.  Even a clean pass must retain `active_assignment_answered: no`; because
the human-review gate has not occurred, certification cannot yet be
`status/proven`.

---
title: "Verification triage — Kourovka 20.115 — SU3(5) central-height bridge"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
scope_record: Agents/Kourovka/scopes/20.115-nonzero-character-order-divisibility.json
assignment_revision: 1
claim: "For L=SU_3(5), p=3, and Z=Z(L), all seven ordinary 3-blocks satisfy p^h <= |D/Z|/exp(D/Z), so Proposition 3.2 gives only its stated prime-three conclusion for finite H with [H,H]=L under all of that proposition's hypotheses."
claimant: Problem-20.115
active_assignment_answered: pending
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/draft]
---

# Verification triage — Kourovka 20.115 — SU3(5) central-height bridge

## Locked scope and claim

The current scope is revision 1 of
`20.115/nonzero-character-order-divisibility`.  Its active target is the
universal assertion that for every finite group `G`, every ordinary complex
irreducible character `chi`, and every `x in G`, `chi(x) != 0` implies
`o(x) chi(1) | |G|`.  The submitted claim is only the bounded prime-three
block bridge stated in the frontmatter.  It does not assert the universal
target.

No claim-check JSON was submitted.  The common protocol requires one for a
`CLAIM` or `STALE_MATCH`; the routed artifact is a `PARTIAL_RESULT`, so this is
recorded but is not by itself a gate failure.

## Clause matrix

| source clause | in active scope | what the submission addresses | status |
|---|---:|---|---|
| `c-question`: universal ordinary-character order divisibility | yes | one sufficient prime-three block condition for the finite derived-group family based on `SU_3(5)` | not answered |
| `c-solvable-context`: assertion known for solvable groups | no | nothing | excluded context |
| `c-general-bound-context`: fourth-power/fifth-power bound | no | nothing | excluded context |

`active_assignment_answered: pending` at triage, with `no` forced unless the
submission unexpectedly proves every row of the universal target.

## Independently reconstructed constraint-and-conclusion matrix

| constraint id | role | required condition | bounded claim's use | triage result |
|---|---|---|---|---|
| `20.115-forall-G-chi-x` | admissibility | all admissible triples | restricts to a finite family with derived group `SU_3(5)` and to `p=3` | fails as a universal answer |
| `20.115-G-finite` | admissibility | `G` finite | proposed consequence assumes finite `H` | retained, source theorem still to be checked |
| `20.115-chi-complex-irreducible` | admissibility | ordinary `chi in Irr(G)` | proposed consequence assumes faithful ordinary `chi in Irr(H)` | retained, source theorem still to be checked |
| `20.115-x-in-G` | admissibility | `x in G`, exact order | proposed consequence uses `h in H` and only `o(hZ(H))_3` | only a narrower quotient-order row |
| `20.115-character-value-nonzero` | admissibility | exact `chi(x) != 0` | proposed consequence retains `chi(h) != 0` | retained, source theorem still to be checked |
| `20.115-order-degree-divisibility` | target conclusion | full `o(x)chi(1) | |G|` | proposed consequence is only `o(hZ(H))_3 | (|H:Z(H)|/chi(1))_3` | not established |

## Target versus witnesses

- Source target: all finite groups and all admissible ordinary-character rows.
- Finite structural witness: CTblLib's ordinary table named `3.U3(5)` and
  GAP's standard matrix group `SU(3,5)`.
- Active assignment versus witness: deliberately unequal; this can only be a
  bounded partial result.
- Table/model identity: pending.  Matching order and center alone do not prove
  isomorphism.  The fresh checker will verify the constructor, center, matrix
  membership, and all claimed finite invariants, but the result remains
  conditional on the installed constructor/table semantics unless an
  independent identification argument is available within the submitted
  boundary.

## Subclaims

1. Every central `p`-subgroup occurs in a block defect group via containment of
   a `B`-Brauer pair in a maximal pair.
2. The block-height definition gives exactly
   `(|L:Z|/theta(1))_p=|D/Z|/p^h`, and hence the claimed threshold equivalence.
3. The 40 ordinary rows form exactly seven 3-blocks with the submitted
   memberships, defects, and heights.
4. The displayed matrices lie in `SU(3,5)`, have the stated orders, contain the
   center as claimed, and yield quotient exponents `3,3,1,1,1,1,1`.
5. The table has exactly one noncentral order-three class, and at least one
   block-2 character is exactly nonzero on it.
6. The cited Theorem 3.5 really implies that the chosen order-three element is
   contained in a conjugate block-2 defect group; with central containment and
   order nine this identifies `<Z,x>` with that defect group.
7. Every one of the 40 height-threshold inequalities follows from the checked
   data.
8. Proposition 3.2 has, and uses, every submitted hypothesis and yields exactly
   the stated prime-three conclusion, no more.

## Tools probed

The non-mathematical environment probe returned:

```text
/usr/bin/gap
/usr/bin/python3
Python 3.12.3
gap 4.12.1-2build2
gap-core 4.12.1-2build2
gap-libs 4.12.1-2build2
```

No `sage` or `magma` executable was found.  GAP itself has not been invoked by
this validator; the assignment requires a frozen checker and Lead lease first.

## Methods inventory

| subclaim | method | what a pass proves | what a pass does not prove |
|---:|---|---|---|
| 1 | hand reconstruction from Brauer-pair definitions | central containment up to conjugacy, hence in every conjugate defect group because `Z` is central | any finite block datum |
| 2 | symbolic valuation calculation | exact equivalence of the two inequalities once 1 and the height convention hold | that any block meets the inequality |
| 3, 7 | independently written frozen GAP checker plus direct `3`-adic arithmetic from degrees | replication of the installed table's block output and all 40 threshold rows | correctness of CTblLib independent of its installed data; universality |
| 4 | reconstruct the submitted matrices literally, test membership/order/subgroup/quotient data | the displayed representatives have the asserted finite properties in the installed matrix model | table/model identity by order alone |
| 5 | use class sizes, class orders, and exact character values, not column position assumptions | uniqueness of the noncentral order-three table class and its block-2 support | the theorem that turns support into defect containment |
| 6 | line-by-line theorem-source audit plus the order argument | validity of the block-2 defect representative | anything if the theorem statement is unavailable or weaker |
| 8 | line-by-line Proposition 3.2 source audit | exact bounded consequence with all hypotheses | the full source target or any other prime/family |

## Hard limits and recommendation

The request permits reading only the four submitted artifacts and forbids prior
20.115 verification/history.  Neither the cited paper nor verbatim statements
of Theorem 3.5 and Proposition 3.2 were submitted.  Claimant paraphrases cannot
independently establish subclaims 6 and 8.  A paper/source excerpt must be added
to the permitted submission boundary before those two steps can receive a
positive verdict.

Recommendation: proceed with the hand proof and a separately frozen bounded
checker after a Lead lease; treat the theorem-dependent bridge as partial until
the cited statements can be audited.  The universal assignment remains open.

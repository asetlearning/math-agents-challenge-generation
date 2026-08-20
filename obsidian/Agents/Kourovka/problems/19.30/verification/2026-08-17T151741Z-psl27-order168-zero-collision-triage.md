---
title: "Verification triage — Kourovka 19.30 — PSL(2,7), order 168"
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
scope_record: Agents/Kourovka/scopes/19.30-vanishing-order-simple-recognition.json
assignment_revision: 1
claim: "For fixed S=PSL(2,7), every finite group G of order 168 with the same set of orders of vanishing elements as S is isomorphic to S."
claimant: Problem-19.30
target_statement: "For every finite group G and finite simple group S, equality of orders and equality of their sets of orders of vanishing elements imply G is isomorphic to S."
excluded_scopes: ["character-table equality alone", "full element-order spectra", "pairs with no finite simple member"]
active_assignment_answered: pending
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/characters, project/kourovka, status/draft]
---

# Verification triage — Kourovka 19.30

## Claim restated

For the one fixed simple target `S=PSL(2,7)`, the claimant reports a complete GAP
SmallGroups enumeration showing that no nonisomorphic finite group `G` of order
168 has the same set of element orders attained by vanishing elements as `S`.
This is a fixed-target `PARTIAL_RESULT`, not an answer to the universal active
assignment.

## Scope, revision, and clause matrix

Canonical scope `19.30/vanishing-order-simple-recognition`, revision 1, asks the
universal question for every finite simple target. The rendered source on PDF page
134 was inspected directly; it says that `g` is vanishing when
`chi(g)=0` for some `chi in Irr(G)`, and asks for recognition from equal group
orders and the same set of orders of vanishing elements.

| source clause | active? | fixed-target claim | triage status |
|---|---:|---|---|
| Definition of a vanishing element via a zero of an irreducible complex character | yes | used verbatim | to reconstruct |
| Universal recognition question for a finite group and a finite simple group | yes | restricts the simple target to `PSL(2,7)` | not answered universally |
| Equality of finite group orders | yes | fixes both orders at 168 | to reconstruct |
| Equality of sets of orders of vanishing elements | yes | exact set equality, no multiplicity | to reconstruct |
| Isomorphism conclusion | yes | asserted for the fixed order-168 subcase | to reconstruct |

`active_assignment_answered: pending` during triage; the final value must remain
`no` even if the fixed-target enumeration passes.

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | required condition | fixed-target value/use | current result |
|---|---|---|---|---|
| `19.30-forall-GS` | admissibility | every admissible pair `(G,S)` | only `S=PSL(2,7)` | fail for universal coverage |
| `19.30-G-finite` | admissibility | `G` finite | purported complete finite order-168 catalogue | pending independent enumeration |
| `19.30-S-finite-simple` | admissibility | `S` finite simple | `PSL(2,7)` | pending independent checks of size and simplicity |
| `19.30-vanishing-definition` | admissibility | zero of some ordinary irreducible complex character | compute zeros in `Irr(CharacterTable(G))` | pending independent computation |
| `19.30-equal-orders` | admissibility | `|G|=|S|` | all candidates and target have order 168 | pending guards |
| `19.30-equal-vanishing-order-sets` | admissibility | equality of sets, without multiplicity | compare exact GAP sets | pending independent computation |
| `19.30-isomorphic` | target conclusion | `G isomorphic S` | only equal-set row should be the target identifier | pending independent computation |

The universal admissibility row already prevents closure of the active assignment.

## Target versus witness

- Source target: all pairs `(G,S)` with `G` finite, `S` finite simple, equal
  orders, and equal vanishing-order sets.
- Active assignment: the same universal scope, revision 1.
- Claimed witness/computational domain: the GAP SmallGroups representatives
  `SmallGroup(168,i)` for `1 <= i <= NumberSmallGroups(168)`, against the single
  constructed target `PSL(2,7)`.
- `witness = target`: false for the active universal assignment. For the fixed
  subcase, completeness depends on the SmallGroups catalogue and must be checked
  explicitly by the independent run.

## Circularity and provenance

The candidate groups come from the complete order-168 SmallGroups catalogue, not
from imposing the desired vanishing-order set. Character zeros are then computed
from each group's ordinary character table. Thus the proposed enumeration is not
true by construction. The catalogue-completeness and character-table computations
remain external GAP/library facts; a passing run does not independently prove GAP's
algorithms or catalogue classification.

## Sub-claim decomposition

1. The source and canonical revision describe the same universal question.
2. The constructed `PSL(2,7)` is finite simple of order 168 and has SmallGroups
   identifier `[168,42]`.
3. `NumberSmallGroups(168)=57`, and the 57 indexed representatives form the
   complete order-168 isomorphism catalogue exposed by GAP.
4. For every representative, exact ordinary irreducible character values and
   conjugacy-class element orders determine its vanishing-order set.
5. The target set is exactly `[2,3,4,7]`.
6. Among all 57 representatives, exact equality with that set occurs only at
   index 42.
7. The index-42 representative is isomorphic to the independently constructed
   target.
8. These facts establish only the fixed target, not the universal active scope.

## Tools and versions

The claimant's artifact reports GAP 4.12.1. Per the assignment's compute gate, no
tool probe or mathematical enumeration has been run by Validator. Tool paths,
versions, SmallGrp package version, and character-table package version will be
captured inside the separately frozen leased run.

## Methods inventory

| sub-claim | independent method | what a pass proves | what a pass does not prove |
|---|---|---|---|
| 1 | direct inspection of rendered PDF page 134 and canonical JSON | source fidelity and revision lock | no mathematical result |
| 2, 7 | independently construct `PSL(2,7)`, check size, simplicity, identifier, and isomorphism with catalogue row | target guards in the installed GAP system | no independent proof of GAP's group-recognition algorithms |
| 3 | call `NumberSmallGroups(168)` and iterate every returned index exactly once | complete coverage of the installed catalogue | no independent classification theorem for all order-168 groups |
| 4, 5 | separately designed loop over `Irr(CharacterTable(G))` and class representatives; mark an order when any exact character value is zero | exact invariant as computed by the installed GAP character machinery | no independent proof of GAP's character-table algorithms |
| 6 | compare canonical strings/sets for all 57 rows and require exactly one matching index | no non-target collision in that finite catalogue | no result for any other simple target or group order |
| artifact comparison | compare only final independently generated summary with claimant's frozen output | a second implementation agrees on the fixed finite result | agreement is not a hand proof of the library data |

## Hard limits and recommendation

Deep verification requires one bounded GAP enumeration and therefore a Lead compute
lease. A fresh script and runner must be frozen, hashed, and leased before any probe
or execution. If the independent run agrees and all guards pass, the bounded
computation may be described as independently replicated, but the canonical
scope-level verdict remains capped at `status/conjectured` because
`witness_equals_target: false`; in all cases `active_assignment_answered: no`. The
fixed subcase cannot be promoted to a universal theorem by computation at one
order.

Recommendation: freeze the independent implementation, request a 20-minute leased
heavy slot with a 900-second wall timeout, then perform full reconstruction of the
fixed finite claim only.

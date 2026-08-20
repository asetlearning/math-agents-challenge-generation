---
title: "Triage — Kourovka 19.30 — fixed A6 order-360 zero-collision partial"
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
scope_record: Agents/Kourovka/scopes/19.30-vanishing-order-simple-recognition.json
assignment_revision: 1
claimant: Problem-19.30
claim_id: 19.30-a6-order360-r1-partial-001
review_kind: fixed-target-partial
active_assignment_answered: pending
author: operator
tags:
  - agent/validator
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/characters
  - project/kourovka
  - status/conjectured
---

# Triage — fixed `A6` order-360 zero-collision partial

## Claim, restated

Among the complete 162 `SmallGroup(360,i)` catalogue representatives, the set of
orders of elements on which at least one ordinary irreducible complex character
vanishes equals the corresponding set for `A6=AlternatingGroup(6)` exactly for
`i=118`, where `IdGroup(A6)=[360,118]`; hence this bounded catalogue contains no
nonisomorphic order-360 collision with the fixed simple target `A6`.

This is a strict fixed-target partial. It does not prove the universal implication
in scope `19.30/vanishing-order-simple-recognition`.

## Scope, revision, and exact target

- Scope: `19.30/vanishing-order-simple-recognition`.
- Assignment revision: 1 (current in the canonical scope record).
- Active target: for every finite group `G` and finite simple group `S`, equality
  of `|G|` and `|S|` and equality of their sets of orders of vanishing elements
  imply `G isomorphic to S`.
- Excluded: character-table equality without equality of the specified invariant;
  equality of full element-order spectra; pairs in which neither group is finite
  simple.
- The visually rendered source on PDF page 134 was independently read for this
  review. It defines vanishing by `chi(g)=0` for some `chi in Irr(G)`, where `chi`
  is an irreducible complex character, and asks about sets, not multisets.

### Clause matrix

| source clause | active? | what the submitted partial addresses | what remains |
|---|---:|---|---|
| `c-definition` | yes | Claims to use the exact zero-of-an-ordinary-irreducible-complex-character definition. | Must be independently reconstructed from character-table data. |
| `c-question` | yes | Claims the implication only for fixed `S=A6` and catalogue groups `G` of order 360. | Every other finite simple `S` and same-order finite `G`; the universal quantifier. |

`active_assignment_answered: pending` at triage, with the required final value
already constrained to `no` even if the fixed-target computation passes.

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | required condition | submitted candidate / proof use | triage evidence | result |
|---|---|---|---|---|---|
| `19.30-forall-GS` | admissibility | Every admissible pair `(G,S)` | Only `S=A6`, `|G|=360` catalogue rows | Claim-check itself records `unknown`; strict bounded family | unknown |
| `19.30-G-finite` | admissibility | `G` finite | `SmallGroup(360,i)` | Catalogue semantics still to be independently checked | pending |
| `19.30-S-finite-simple` | admissibility | `S` finite simple | `AlternatingGroup(6)` | Raw output asserts size 360 and simplicity; independent check pending | pending |
| `19.30-vanishing-definition` | admissibility | `x` vanishing iff some `chi in Irr(H)` has `chi(x)=0` | Claimed character-table zero test | Independent source/script reconstruction pending | pending |
| `19.30-equal-orders` | admissibility | `|G|=|S|` | All catalogue rows and `A6` claimed order 360 | Independent check pending | pending |
| `19.30-equal-vanishing-order-sets` | admissibility | Exact equality of sets, no multiplicities | Claimed target set `[2,3,4,5]`, equality only row 118 | Independent computation pending | pending |
| `19.30-isomorphic` | target conclusion | Every admissible `G` is isomorphic to `S` | For the fixed family, unique equal-set row is claimed to have the target ID | Catalogue/ID semantics and unique equality pending; universal conclusion not proved | not_proved |

The claimant's `ready_for_validator:false` state-check is consistent with a
partial and is not treated as mathematical evidence.

## Target versus witness

- Source target: all finite pairs `(G,S)` with `S` simple and the stated two equalities.
- Active assignment: the same universal target.
- Submitted witness/model: the 162 installed `SmallGroup(360,i)` representatives,
  compared only with `A6`.
- `witness = universal target`: false. The model is a proposed complete model of
  one fixed order/simple-target subcase only.
- `witness = fixed A6/order-360 subcase`: pending. It requires independent support
  that the installed SmallGroups catalogue is complete up to isomorphism at order
  360, that `A6` has ID `[360,118]`, and that the invariant was evaluated exactly.

## Subclaims and methods inventory

| subclaim | independent method | what a pass proves | what a pass does not prove |
|---|---|---|---|
| Source and scope match | Visual PDF/source-to-JSON comparison | Definition and target were transcribed faithfully | Any finite computation or universal theorem |
| Raw artifact structurally contains rows 1..162 exactly once | Frozen, independently designed strict parser over the preserved output | Coverage and internal consistency of that text artifact despite the wrapped header | Correctness of any character value, group ID, or completeness of the catalogue |
| `A6` is simple, has order 360, and ID `[360,118]` | Independent GAP construction and ID/simple/order checks | Those finite facts in the installed GAP libraries | Universal recognition or the invariant calculation |
| The invariant is the set of actual vanishing-element orders | Independently designed GAP computation from conjugacy classes, ordinary irreducible character values, and representative orders | Exact invariant for each successfully constructed finite group, conditional on GAP/library semantics | A hand proof independent of GAP or anything outside the enumerated family |
| All order-360 isomorphism types are covered | `NumberSmallGroups(360)` plus documented `SmallGroup`/`IdGroup` semantics and exact index coverage | Completeness of the installed order-360 catalogue up to isomorphism | Coverage of any other order |
| Equality occurs only at row 118 | Independent recomputation plus separately frozen comparison/parser | No non-target collision for fixed `A6` among order-360 catalogue representatives | The universal scope |

## Tools and frozen-input state

- GAP 4.12.1 at `/usr/bin/gap`.
- Python 3.12.3 at `/usr/bin/python3`.
- Sage and Magma were not found on `PATH`.
- Submitted raw output SHA-256:
  `6142ece4f7daa7b08d330bce798fceade8e4de45a6b4a27637ff0364d051421e`.
- The submitted wrapper exited 1 because its parser rejected a GAP-wrapped header.
  Its coverage/equality verdict is therefore not inherited.
- No mathematical verification computation has been run in this review. A new
  checker must be frozen and leased before execution.

## Hard limits and recommendation

A text-only parser can repair the wrapper's structural blind spot but cannot
independently validate character theory. Full fixed-target replication therefore
requires a separately designed GAP checker plus a strict independent transcript
checker, frozen before an explicit Lead compute lease. Even a complete pass yields
only `status/replicated` for the fixed `A6`, order-360 partial and forces
`active_assignment_answered:no`.

Recommendation: freeze that bounded checker, request a short lease, then perform
full fixed-target verification. Do not certify or generalize from the submitted
wrapper output alone.

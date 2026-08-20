---
title: "Triage — Kourovka 21.137 — fixed rank-four central family"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claimant: Problem-21.137-Counterexample
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, project/kourovka, status/draft]
---

# Triage — fixed rank-four central family

## Claim restated

For the single frozen `p=3` extension datum with kernel
`K=3_+^(1+4) x C3^2`, quotient `H_3(3)`, fixed action/lifts/shears/labels and
fixed noncentral relator representatives, the 6,561 feasible choices of the 18
central relator coordinates form exactly 27 section-gauge classes, and every
class realizes an order-`3^10`, exponent-nine group whose literal cube image
has 135 elements and generated closure 729; consequently no row in this
bounded family satisfies the literal-cube-set subgroup hypothesis.

## Scope lock and clause matrix

- `scope_id`: `21.137/odd-prime-exponent-p2`
- `assignment_revision`: `2`
- Active target: for odd prime `p`, every finite `p`-group of exponent exactly
  `p^2` whose literal set `{g^p:g in G}` is a subgroup has that set abelian.
- Excluded: the general powerfulness clause, the `p=2`/exponent-eight sibling,
  and odd-prime groups of exponent other than exactly `p^2`.

| source clause | active? | submitted family addresses | status |
|---|---|---|---|
| General finite-`p` powerfulness question | no | no | excluded |
| Odd `p`, exponent `p^2`, literal power set subgroup implies abelian | yes | only one frozen `p=3` family, all alleged to fail the hypothesis | `active_assignment_answered: pending` during validation; necessarily `no` even if the bounded claim passes |
| `p=2`, exponent eight, square set subgroup implies abelian | no | no | excluded |

The rendered source PDF page 184 was visually checked: it says `p != 2`,
exponent `p^2`, and separately states the exponent-eight 2-group question.
The canonical scope record is faithful to this active clause.

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | required condition | submitted value/use | triage result |
|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | universal over all admissible `p,G` | one fixed `p=3` family | does not answer universal row |
| `21.137-odd-p-not-2` | admissibility | odd prime | `p=3` | pending independent model check |
| `21.137-odd-finite-p-group` | admissibility | finite same-`p` group | alleged order `3^10`, kernel `3^7`, quotient `3^3` | pending |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly nine | alleged exhaustive ninth-power check plus order-nine witness | pending |
| `21.137-odd-power-set-definition` | admissibility | literal image of the cube map | alleged exhaustive 59,049-element cube map | pending |
| `21.137-odd-power-set-subgroup` | hypothesis | literal cube image is a subgroup | alleged image size 135, generated closure 729 | submitted rows fail; independently pending |
| `21.137-odd-P-abelian` | target conclusion | literal cube image abelian | guardrail not reached after subgroup failure | not established and not needed for family exclusion |

## Target versus witness

- Source target: the universal odd-prime exponent-`p^2` assertion above.
- Submitted witness: a finite affine family of central extensions for one fixed
  `p=3` action/lift datum.
- `witness = source target`: false; a bounded family is not the universal
  object class.
- `witness = claimed bounded family`: pending exact reconstruction of the
  action, cochain constraints, gauge quotient, factor realization, and group
  law. No filename, expected dimension, or claimed order is accepted as this
  bridge.

## Circularity check and subclaims

The family is defined before testing the cube-set hypothesis. Failure of that
hypothesis is not built into its construction. The submitted representative
list, cochain ranks, and cube outputs are treated as untrusted outputs, not
inputs to the independent checker.

The validation decomposes into:

1. reconstruct the fixed kernel, quotient, action and lift and prove all 729
   action defects and 19,683 vector associativity identities;
2. derive the full central cochain equation and eliminate it to the exact ten
   affine relator equations, dimension eight and 6,561 rows;
3. derive the section-gauge map, its rank five image, and the equality of the
   two 69-dimensional exact-row kernels, proving completeness rather than a
   sample;
4. derive the 27 orbits and a realizing factor for each representative;
5. independently construct every representative group and certify order,
   kernel, quotient and exact exponent nine;
6. evaluate the cube map on all 59,049 elements in every class, keeping the
   literal 135-element image separate from its 729-element generated closure;
7. prove that gauge-related rows give isomorphic groups and carry literal cube
   images to literal cube images;
8. retain the exact bounded-family boundary and
   `active_assignment_answered:no`.

## Tools and methods inventory

Probe: GAP is installed (version probe to be captured in the final
transcript); Python 3.12.3 is installed; Sage and Magma are absent.

| subclaim | method | what a pass proves | what it does not prove |
|---|---|---|---|
| action/lift and cochain identities | hand derivation plus independently written finite-field checker | exact identities for the frozen arrays | any other lift/action |
| affine image and gauge quotient | independent row reduction over `F3` | complete 6,561-row quotient for this datum | classification of all compatible lifts |
| representative realization | independently solve the normalized factor equations | existence of every listed extension | uniqueness beyond the stated section gauge |
| group gates and cubes | direct exact coordinate multiplication and exhaustive finite enumeration | order/exponent and literal cube image for every representative | any group outside the 27 classes |
| gauge bridge | explicit section-change isomorphism | propagation from representatives to all gauge rows | propagation to different action/lift data |

## Hard limits and recommendation

The submission is a `PARTIAL_RESULT`, not a whole-scope `CLAIM`; no linked
claim-check JSON was supplied. This does not waive any mathematical gate.
The required independent enumeration is heavy and will not run until a fresh
checker and manifest are frozen and Lead grants a compute lease. Recommendation:
full verification of this bounded family only. The maximum possible verdict is
`status/replicated` (or `status/proven` only if all finite completeness bridges
are also supplied as a fully defensible proof), always with
`active_assignment_answered:no`.

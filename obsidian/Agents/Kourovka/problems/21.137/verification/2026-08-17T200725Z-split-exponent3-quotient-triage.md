---
title: "Triage — Kourovka 21.137 — split exponent-three quotient exclusion"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "For K=3_+^(1+4) x C3^2, every split extension K semidirect Q with Q of exponent three has pairwise commuting literal cubes; the displayed K semidirect H_3(3) seed has order 3^10, exponent exactly nine, and literal cube image exactly <c>."
claimant: Problem-21.137-Counterexample
active_assignment_answered: pending
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, project/kourovka, status/draft]
---

# Triage — split exponent-three quotient exclusion

## Locked scope and source clauses

The canonical record is `21.137/odd-prime-exponent-p2`, revision 2. I rendered and
visually inspected source PDF page 184. The active source clause asks, for every odd
prime and every finite p-group of exponent exactly p^2 whose literal pth-power set
is a subgroup, whether that subgroup is abelian. The general powerfulness question
and the separate exponent-eight 2-group clause are inactive here.

| source clause | active? | routed result |
|---|---:|---|
| general powerfulness question | no | not addressed |
| odd-prime, exponent-p^2, literal power subgroup abelian | yes | only one split p=3 extension family |
| p=2, exponent-eight square subgroup | no | excluded and unused |

The routed artifact is a bounded `REPORT`/`PARTIAL_RESULT`, not a scope-closing
`CLAIM`; it links no claim-check JSON. This prevents no bounded hand review but
cannot satisfy the scope-closing state gate.

## Constraint-and-conclusion preflight

| constraint_id | role | routed use | triage result |
|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | fixes p=3, one kernel, split exponent-three quotients | fails universal coverage |
| `21.137-odd-p-not-2` | admissibility | p=3 | pass in family |
| `21.137-odd-finite-p-group` | admissibility | finite K and finite Q | pending exact seed/action check |
| `21.137-odd-exponent-p2` | admissibility | only exact-exponent-nine family members are target-admissible | pending exact seed check |
| `21.137-odd-power-set-definition` | admissibility | literal cubes, not generated powers | pending all-element formula check |
| `21.137-odd-power-set-subgroup` | admissibility | theorem does not assert closure; seed claims image `<c>` | pending exact-image check |
| `21.137-odd-P-abelian` | target conclusion | pairwise commutation in family; seed image abelian | pending proof check; not a counterexample |

`active_assignment_answered: no` will remain mandatory even if every pending bounded
row passes.

## Target versus checked object

- Source target: all admissible finite p-groups at all odd primes.
- Checked family: split semidirect products `K semidirect Q`, where
  `K=3_+^(1+4) x C3^2` and finite `Q` has exponent three.
- Concrete seed: the displayed coordinate model `K semidirect H_3(3)`.
- `witness = target`: false. The family is a proper p=3 subclass, and the seed
  satisfies rather than violates the target conclusion.

## Subclaims and methods inventory

| subclaim | independent method | what a pass proves | what it does not prove |
|---|---|---|---|
| every automorphism induces a symplectic map on K/Z(K) | characteristic-subgroup and commutator-form proof | projected action lies in Sp4(3) for order-three acting elements | splitness, seed formulas, other kernels |
| every order-three element of Sp4(3) has square-zero M-I | independent line-by-line Jordan/symplectic proof; compare reviewed finite check only as support | vanishing projected norm in rank four | analogous statements at other ranks/primes |
| semidirect cube projection vanishes | direct semidirect collection and norm identity | every literal cube lies in Z(K) in the split family | any nonsplit section, literal-set closure |
| A,B,C define the stated faithful H3(3) action | direct 4x4 multiplication with a separately written bounded checker as support | action conventions and nonabelianity | universal extension claim |
| K and seed coordinate laws define the stated groups | hand associativity/action compatibility and inverse check | well-defined group of order 3^10 | target universality |
| scalar cube formula and exact image | independent symbolic collection and small finite-field identity checker | all 3^10 cubes, literal image exactly `<c>`, equality with generated subgroup | any other action or nonsplit extension |
| exact exponent nine | kernel/quotient exponent bound plus explicit nontrivial cube | seed exponent is 9 | exponent of arbitrary family members |

No discovery search, catalogue extension, or factor-system search is authorized.

## Tools and hard limits

Available: GAP 4.12.1 and Python 3.12.3. Sage and Magma are absent. No heavy
computation is needed or leased. A constant-size independently written matrix and
coordinate identity checker is within the bounded certificate-checker allowance;
the verdict will rest primarily on hand derivations.

The review cannot establish nonsplit extensions, other kernels, other primes, or
the universal odd-prime assertion. It will not touch p=2/exponent-eight material.

## Recommendation

Proceed with full verification of the two bounded claims only. Preserve outcome
`PARTIAL_RESULT`, `active_assignment_answered: no`, even on a pass.

---
title: "Triage — Kourovka 21.137 — MCO affine-norm cover"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claimant: Problem-21.137
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, project/kourovka, status/draft]
---

# Triage — Kourovka 21.137 — MCO affine-norm cover

## Claim and scope lock

The submission makes no solution or witness claim.  It reports that, conditional
on the already reviewed minimum-counterexample reduction, the displayed affine
norm-support formulas, cross-coset factor identities, conditional lower bounds,
and two formal obstruction examples are correct, while
`MCO-AFFINE-NORM-COVER` is exhausted and the unrestricted target remains open.

The active revision-2 target is: for every odd prime `p` and finite same-`p`
group `G` of exponent exactly `p^2`, if the actual value set
`P={g^p:g in G}` is itself a subgroup, then `P` is abelian.  The general
powerfulness question, every `p=2` case, and the exponent-8 square clause are
excluded.  Rendered source page 184 and the canonical scope agree.

| source clause | active? | submission result |
|---|---:|---|
| General power-value subgroup powerful? | no | excluded |
| `p != 2`, exponent `p^2`, actual powers a subgroup; abelian? | yes | conditional formulas and failure certificate only |
| `2`-group of exponent `8`; square subgroup abelian? | no | excluded |

`active_assignment_answered: pending` for triage; the submitted artifact itself
states `no`.

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | required condition | triage status |
|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | every admissible `p,G` | not discharged; work is conditional on a hypothetical minimum counterexample |
| `21.137-odd-p-not-2` | admissibility | prime `p>2` | retained |
| `21.137-odd-finite-p-group` | admissibility | finite `p`-group for that same `p` | retained conditionally |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly `p^2` | retained conditionally through the reviewed reduction |
| `21.137-odd-power-set-definition` | admissibility | actual value set, not generated subgroup | exact union of cosetwise value supports is asserted |
| `21.137-odd-power-set-subgroup` | admissibility | actual value set is a subgroup | used as the exact covering hypothesis |
| `21.137-odd-P-abelian` | target conclusion | `P` abelian | unresolved |

There is no `claim-check` JSON requirement because this is a
`STRATEGY_EXHAUSTED`/conditional-`PARTIAL_RESULT` submission, not a `CLAIM` or
`STALE_MATCH`.

## Target versus witness

The target object is every finite group in the active source class.  No group was
constructed or computed in.  The only mathematical object is a hypothetical
minimum counterexample together with formal pointwise affine data that are
explicitly missing an index-group multiplication and factor system.  Therefore
`witness_equals_target: false`; the formal cover cannot answer any admissibility
row as an exhibited witness.

## Subclaims and authorized methods

| subclaim | method | what a pass proves | what it does not prove |
|---|---|---|---|
| Standard class-two coordinates and action-power identities | direct hand multiplication with `y^x=x^-1 y x` | the local signs and `D^p=0`, `ell(D^(p-1)a)=beta(a,c)` identities | existence of compatible data across cosets |
| `(F1)` and `(F2)` | ordered hand collection and characteristic-`p` polynomial identities | the complete support and multiplicity formula | a missing point or `beta=0` |
| Isotropy/self-adjointness | bilinear-form identities valid with radical | the claimed pointwise restrictions | nondegeneracy or a global separator |
| `(C1)`--`(C5)` | reassociate `x_hx_j=x_(hj)u_(h,j)` under the stated right action | necessary extension compatibility and exact factor order | sufficiency for an extension or existence |
| Conditional bounds | hand linear-algebra and commutator chain | only necessary conditions on a hypothetical minimum counterexample | novelty relative to already reviewed stronger bounds |
| Carry cocycle | direct normalized-cocycle calculation | `(X1)` alone need not kill the coinvariant translation | compatibility with nonzero `beta` or with the full central equation |
| Formal cover | basis-level pointwise check | local identities and a set cover can coexist with `beta!=0` | a group, extension, target witness, or counterexample |

## Tool probe and hard limits

Availability probe found `/usr/bin/gap`, `/usr/bin/python3`,
`/usr/bin/pdftoppm`, and `/usr/bin/pdftotext`; neither Sage nor Magma was found.
Version output was `Python 3.12.3`, `pdftoppm version 24.02.0`, and
`pdftotext version 24.02.0`.  No mathematical computation is authorized or
needed.  The audit is restricted to hand reconstruction from the request, its
refs, the canonical scope, rendered source page 184, and Lead-directed
comparisons with already reviewed local partial bounds.  No web, literature,
quarantined material, or `p=2` argument is admissible.

## Recommendation

Proceed with a full hand audit of each displayed identity and implication, but
cap the verdict at `status/conjectured` and `active_assignment_answered: no`.
Classify any correct lower bound against the stronger already reviewed local
bounds rather than presenting a rederivation as new target-level progress.

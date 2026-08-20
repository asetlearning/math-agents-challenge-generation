---
title: "Triage — Kourovka 21.53 — q=7 Pasch and resolution obstruction"
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
scope_record: Agents/Kourovka/scopes/21.53-two-minimal-prime-colours.json
assignment_revision: 2
claimant: Problem-21.53
active_assignment_answered: pending
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/finite-geometry, project/kourovka, status/draft]
---

# Triage

## Claim restated

For the internal-point/secant-section incidence system of the conic
`Y^2=XZ` in `PG(2,7)`, the four displayed geometric triples admit a
tetrahedral star/face trade to four noncollinear triples that preserves the
binary constant-weight Gram matrix but is not a column permutation; the
geometric 28-block system has eight point-partition resolutions and this one
traded system has none.  Separately, in the stated characteristic-three
subfamily the exact product-order-three relation is empty, subject to the
submitted trace/order dictionary.

The active revision-2 target remains the universal equality
`Aut(Gamma)=Aut_2(Gamma) intersection Aut_p(Gamma)` for every admissible
`(L,D)`.  Excluded are Problem 21.52, unions of involution classes, arbitrary
choices of `p`, and treating a bounded list as universal.

## Clause matrix

| source clause | submitted claim | status |
|---|---|---|
| inherited finite nonabelian simple-group/involution-class product-order graph | only a conic incidence model associated to the `q=7` branch is used | not answered |
| one-way definition of every `Aut_t`, including the vacuous case | used in the characteristic-three limitation | pending audit |
| full colour group is the intersection of all occurring colour stabilisers | not reconstructed | not answered |
| two minimal prime colours determine every colour | neither proved nor refuted | not answered |

`active_assignment_answered: pending` at triage; the expected final value is
`no` because the submitted result is explicitly only a reconstruction-method
obstruction.

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | independent triage status | reason |
|---|---|---|
| `21.53-forall-L-D` | fail for scope closure | only two finite `q=7` block systems are submitted |
| `21.53-L-finite-nonabelian-simple` | not needed for the bounded incidence claim | no fixed-group equality/counterexample is claimed |
| `21.53-D-single-involution-class` | not established in the submitted bounded certificate | the certificate is stated directly on 21 internal conic points |
| `21.53-Gamma-product-order-colouring` | not established in full | only the proposed order-2 reconstruction data are involved |
| `21.53-Aut-t-definition` | source definition independently read; empty-label implication remains to audit | one-way preservation is vacuous when the relation is empty |
| `21.53-two-minimal-primes` | not needed for the `q=7` trade; characteristic-three statement pending audit | submitted claim says `p=3` there |
| `21.53-full-colour-group-definition` | not established | no full colour system is reconstructed |
| `21.53-two-colours-determine-all` | unproved and unviolated | no automorphism/separating permutation is supplied |

## Target versus witness

The source target is a universal equality of permutation groups on an
involution conjugacy class.  The submitted objects are one geometric and one
Pasch-traded binary `21 x 28` incidence factor over `F_7`.  They are not
asserted to be target witnesses, and no equality between either block system
and the source target would follow from the submitted data.  Thus
`witness_equals_target: false` for purposes of scope closure, while the bounded
method claim can still be checked on its own terms.

## Subclaims and methods inventory

| subclaim | independent method | what a pass proves | what it does not prove |
|---|---|---|---|
| six points are internal | direct evaluation of `Y^2-XZ` and square-class check in `F_7` | exactly the displayed classification | any group-theoretic equality |
| four old triples are complete internal sections of secants | hand line incidence, conic intersection, and full 57-point projective count | exactly those four supports | classification of all Gram factors |
| four new triples are noncollinear | nonzero `3 x 3` determinants | they are not geometric line sections | that they cannot arise in another geometry |
| outer-product identity | tetrahedral incidence multiplicity count, plus direct symbolic entry audit | equality of the two four-column Gram contributions | recoverability from the full order-2 graph |
| not a column permutation | show every new support is absent from the geometric support set | these two factors differ up to column permutation | an automorphism outside the full-colour group |
| 8 versus 0 resolutions | frozen independent exact-cover checker organized as bitmask DP, run only under a Lead lease | exact counts for these two 28-block systems | classification of all factorizations or any `PSL(2,7)` equality |
| characteristic-three `R_3` empty | independently derive the trace/projective-order criterion and shell pair invariant, if possible from first principles | emptiness in the precisely derived subfamily | any field-uniform reconstruction theorem |

## Tools and hard limits

Available: GAP 4.12.1, Python 3.12.3, GNU sha256sum 9.4.  Sage and Magma are
absent.  Enumeration is frozen until a Lead compute lease is requested and
granted.  The submitted trace/order dictionary is not itself among the
permitted evidence files, so the characteristic-three statement must be
derived independently or remain only partially verified.

## Recommendation

Proceed with full hostile verification of the bounded hand certificate.  Write
a differently organized bitmask exact-cover checker, freeze its hash, request
one bounded Lead lease, and run it only after approval.  Return a partial
verdict with `active_assignment_answered: no` regardless of whether the two
finite counts replicate.

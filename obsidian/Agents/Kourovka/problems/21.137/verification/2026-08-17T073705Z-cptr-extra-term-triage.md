---
title: "Triage — Kourovka 21.137 — CPTR mixed-cycle extra-term certificate"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claimant: Problem-21.137
active_assignment_answered: pending
author: operator
tags:
  - agent/validator
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/group-extensions
  - project/kourovka
  - status/draft
---

# Triage — CPTR mixed-cycle extra-term certificate

## Claim restated

In the conditional extension-coordinate calculation recorded for
`CPTR-PAIR-TRANSGRESSION`, the normalized mixed bar chain is a cycle, the scalar
`(C4)` row is a coboundary and therefore evaluates to zero on that cycle, while
the fully ordered cyclic-power identity leaves the scalar in `(E6)` as an
uncontrolled, section-dependent carry term; consequently this particular method
does not prove `beta=0` and does not answer the active scope.

This is a method-failure certificate, not a proof, counterexample, stale match, or
claim that the universal target is false.

## Scope lock and clause matrix

- Scope: `21.137/odd-prime-exponent-p2`.
- Assignment revision: `2`.
- Exact active target: for every odd prime `p` and finite `p`-group `G` of
  exponent exactly `p^2`, if the actual value set
  `P={g^p:g in G}` is itself a subgroup, then `P` is abelian.
- Excluded: the general powerful-subgroup clause, every `p=2` example, the
  exponent-8 square-set clause, odd-prime groups of exponent other than exactly
  `p^2`, and replacing the actual value set by the subgroup it generates.

| source clause | in scope | what this artifact asserts | status |
|---|---:|---|---|
| General powerfulness question | no | nothing | excluded |
| Odd `p`, exponent exactly `p^2`, actual powers form a subgroup, abelian? | yes | only that one proposed proof method stalls | `active_assignment_answered: pending` |
| `p=2`, exponent `8`, squares | no | nothing | excluded |

The rendered PDF page 184 was inspected visually; its odd-prime clause agrees
with the canonical scope record.

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | required condition | relevance to this audit | triage result |
|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | every admissible odd `p,G` | no universal conclusion is claimed | unresolved |
| `21.137-odd-p-not-2` | admissibility | `p>2` prime | needed for `1/2` and the mod-`p` calculation | retained conditionally |
| `21.137-odd-finite-p-group` | admissibility | finite same-`p` group | no concrete witness is offered | retained only as a hypothesis of the coordinate setup |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly `p^2` | no concrete witness is offered | retained only as a hypothesis of the coordinate setup |
| `21.137-odd-power-set-definition` | admissibility | actual value set, not generated subgroup | used only in the claimed affine-cover reach audit | to be checked logically |
| `21.137-odd-power-set-subgroup` | admissibility | that actual set is a subgroup | used only in the claimed affine-cover reach audit | to be checked logically |
| `21.137-odd-P-abelian` | target conclusion | `P` abelian | expressly not established | unproved |

No claim-check file is required because the routed outcome is
`STRATEGY_EXHAUSTED`, not `CLAIM` or `STALE_MATCH`.

## Target versus witness

- Source target: the universal odd-prime statement above.
- Witness/computed object: none. The submitted evidence is a hand calculation in
  a conditional extension-coordinate system, not a finite group offered as the
  target or as a counterexample.
- Witness equals target: not applicable; the calculation can certify only what
  follows from its explicitly stated coordinate identities.

## Subclaims to audit

1. The normalized inhomogeneous boundary and the signs in the mixed chain give
   `partial Z=0`.
2. The scalar associativity row has exactly the claimed `(C4)` sign and equals
   `delta s` under the same bar convention.
3. Every right action, multiplication order, `ell` term, and quadratic term in
   the cyclic `(C5)` expansion is correctly ordered.
4. `(E3)` through `(E7)` follow with the stated signs and no omitted term.
5. The arbitrary normalized-section laws for `L,ell,c,d,r,s` are exact, and the
   asserted covariance and `(E8)`--`(E9)` follow.
6. The available identities really do not force the `(E6)` scalar to vanish.
7. The affine-cover observation neither makes `beta` descend nor supplies a
   bridge from the one commuting pair to `beta=0`.
8. All exact-scope exclusions remain respected and the universal target remains
   unanswered.

## Tools available

- GAP `4.12.1` available.
- Python `3.12.3` available.
- Sage: unavailable.
- Magma: unavailable.

No general-purpose computation is needed or authorized for this hand-identity
audit.

## Methods inventory and limits

| subclaim | independent method | what a pass proves | what a pass does not prove |
|---|---|---|---|
| boundary and `(C4)` | expand normalized bars and reassociate four section representatives | exact cycle/coboundary signs | any nonzero transgression or `beta=0` |
| ordered `(C5)` and `(E3)`--`(E7)` | derive powers in the right-action semidirect convention and sum central Heisenberg coordinates | exact identities in the stated coordinate system | that the system covers every target group, or that `(E6)` vanishes |
| section change | direct conjugation, carry reassociation, and ordered-power comparison | exact transformation/covariance formulas | section-independence of an uncorrected basepoint pairing |
| reach | elementary quotient and bilinear-form logic | whether the proposed bridge follows | the universal target by any other method |

Hard limit: the request permits only the two routed artifacts and the rendered
source. Earlier reduction notes are deliberately not inherited. Therefore this
audit will not certify the provenance or universality of the surrounding
minimum-counterexample model; it will check the submitted formulas and their
negative logical reach only.

## Recommendation

Proceed with full line-by-line hand verification of the bounded method-failure
certificate. Regardless of whether its formulas pass, the current submission
cannot answer the active assignment because it expressly proves neither the
universal abelian conclusion nor an admissible counterexample.

---
title: "Triage — Kourovka 21.137 — NS3 common action defect"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "Every one of the 3^10 labelled central-correction rows in NS3-FIXED-OUTER-ACTION/F_3^10 violates the same necessary right-action equation at (h,j)=(y,x)."
claimant: Problem-21.137
target_statement: "Let p be an odd prime and G a finite p-group of exponent exactly p^2. If the actual p-th-power value set is a subgroup, then it is abelian."
excluded_scopes: ["the general powerfulness clause", "p=2 and the exponent-8 clause", "all extension families other than NS3-FIXED-OUTER-ACTION/F_3^10"]
active_assignment_answered: pending
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/group-extensions, project/kourovka, status/draft]
---

# Triage — NS3 common action defect

## Restated claim

For the exactly frozen data at `p=3`, with kernel
`Q=H_3(3) x C_3^2`, quotient `H=H_3(3) x C_3`, action
representatives `A,B,C=[A,B],T=I`, and only the ten displayed central
`<z>` correction coordinates allowed, every labelled parameter row fails the
necessary factor-system action identity already at `(h,j)=(y,x)`.

This is a complete bounded-family claim only.  It does not answer the active
universal assignment.

## Scope, revision, and clause matrix

Canonical scope: `21.137/odd-prime-exponent-p2`, revision `2`.

| source clause | active? | addressed by this claim | disposition |
|---|---:|---:|---|
| general powerfulness question | no | no | explicitly excluded |
| odd-prime, exponent-exactly-`p^2`, actual-value-set subgroup implies abelian | yes | no | remains open |
| `p=2`, exponent `8`, square-value-set clause | no | no | explicitly excluded |
| bounded family `NS3-FIXED-OUTER-ACTION/F_3^10` | auxiliary partial-progress target | yes | pending reconstruction |

`active_assignment_answered: pending` at triage; it cannot become `yes` from
this family-exclusion claim.

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | required condition | status at triage |
|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | all allowed odd primes and groups | not addressed; only one frozen `p=3` family |
| `21.137-odd-p-not-2` | admissibility | `p>2` | passed by the frozen choice `p=3` |
| `21.137-odd-finite-p-group` | admissibility | finite same-`p` group | no group is claimed to survive |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly `p^2` | not reached |
| `21.137-odd-power-set-definition` | admissibility | complete actual power-value set | not reached |
| `21.137-odd-power-set-subgroup` | admissibility | that set is a subgroup | not reached |
| `21.137-odd-P-abelian` | target conclusion | power-value set is abelian | not reached |

No failed or unknown active-scope row is being presented as a counterexample;
the claimed output is only an exclusion of the named frozen factor family.

## Target versus witness

- Source target: all finite odd-prime `p`-groups of exponent exactly `p^2`
  whose actual `p`th-power set is a subgroup.
- Active assignment: the revision-2 odd-prime clause above.
- Object actually analysed: the five-dimensional BCH kernel together with the
  single frozen quotient/action/lift family and its ten central parameters.
- Witness equals unrestricted target: false.  The object is a deliberately
  narrow auxiliary family, and no candidate group is produced.

## Subclaims

1. The commutator convention implies `[y,x]=c` iff `yx=xyc`.
2. With right conjugation and the section ordered as `X^iY^jK^kT0^l`,
   `s(y)s(x)=YX=XYKz^e=s(yx)z^e`.
3. The right-action factor equation is
   `alpha_x alpha_y = Inn(u(y,x)) alpha_(yx)`; in the stated matrix naming
   this is `AB=Inn(z^e)CBA`.
4. The written `A,B` are automorphisms of `Q`, `C=[A,B]`, and
   `AB(CBA)^(-1)=Inn(a-b) != I`.
5. Every allowed correction at the decisive pair is central, so its inner
   action is trivial and none of the ten parameter choices changes the
   failure.
6. Therefore all `3^10` labelled rows fail a necessary extension equation.
7. This says nothing about any repaired or enlarged family or the unrestricted
   revision-2 target.

## Tool probe

- GAP `4.12.1` at `/usr/bin/gap`.
- Python `3.12.3` at `/usr/bin/python3`.
- Sage and Magma were not found.

The first GAP version probe used the undefined identifier `VERSION`; the
recorded version comes from `GAPInfo.Version`.

## Methods inventory

| subclaim | method | what a pass proves | what it does not prove |
|---|---|---|---|
| 1--3 | hand group-law/right-action derivation | the exact order and sign of the necessary factor equation | no matrix identity and no extension existence |
| 4 | hand action on the five basis vectors over `F_3` | the exact common inner defect | no conclusion outside the frozen action representatives |
| 5--6 | quantifier audit of the ten central parameters | one parameter-independent contradiction covers all `3^10` labels | no categorical enumeration and no exclusion of noncentral corrections |
| supplied Python checker | corroboration only after the hand audit | agreement with the frozen matrix arithmetic | not independent evidence by itself and not a target solution |

## Hard limits and recommendation

No new search, family repair, family enlargement, categorical row enumeration,
web/history inspection, wreath material, or `p=2` work is authorised.  Full
verification of the bounded claim appears possible by hand.  The supplied
checker may be consulted only as corroboration after that reconstruction.


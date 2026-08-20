---
title: "Triage — Kourovka 21.137 — regular power commutator"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "Hall's pair-local regularity identity forces abelian actual pth powers in the Hall-regular exponent-p^2 subfamily, while every hypothetical counterexample has the submitted noncentral Hall defect; the unrestricted target is not answered."
claimant: Problem-21.137-Proof
active_assignment_answered: pending
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/regular-p-groups, project/kourovka, status/conjectured]
---

# Triage — Kourovka 21.137 — regular power commutator

## Claim and scope lock

Canonical scope `21.137/odd-prime-exponent-p2`, revision `2`: `p>2` is prime, `G` is a finite same-`p` group of exponent exactly `p^2`, `P={g^p:g in G}` is the literal actual-value set and is assumed to be a subgroup, and the target asks whether `P` is abelian. The `p=2`, exponent-`8` sibling and the general powerfulness clause are excluded.

The submission is a structured-family `PARTIAL_RESULT`, not a universal claim. No claim-check JSON is required for this non-`CLAIM` outcome.

## Clause matrix

| source clause | active? | submitted coverage |
|---|---:|---|
| General actual-power-subgroup powerfulness question | no | none |
| Odd prime, exact exponent `p^2`, literal actual powers a subgroup, ask abelian | yes | Hall-regular subfamily and conditional defect only |
| `p=2`, exponent `8` sibling | no | excluded |

`active_assignment_answered: pending` until reconstruction; even a pass of every submitted subclaim will leave it `no` because Hall regularity is extra.

## Constraint-and-conclusion matrix

| constraint_id | role | audit at triage | result |
|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | submission covers only Hall-regular admissible groups | partial |
| `21.137-odd-p-not-2` | admissibility | fixed `p>2`; formulas will be audited for any hidden prime restriction | pending |
| `21.137-odd-finite-p-group` | admissibility | finite `p`-group used for nilpotence/order induction | pending |
| `21.137-odd-exponent-p2` | admissibility | exact exponent makes every literal value exponent at most `p` | pending |
| `21.137-odd-power-set-definition` | admissibility | literal actual-valuedness is essential in the short proof and defect construction | pending |
| `21.137-odd-power-set-subgroup` | admissibility | assumed in the active subfamily proof; stronger closure claim is separate | pending |
| `21.137-odd-P-abelian` | target conclusion | claimed only with extra Hall regularity | unresolved universally |

## Target versus witness

The target is the full universal class above. The submitted witness-class is the proper subfamily of finite Hall-regular `p`-groups, plus a hypothetical minimum-order counterexample for a conditional defect calculation. No concrete group is computed or exhibited. Therefore `witness_equals_target: false`; there is no circular finite-model issue, but the extra Hall-regularity hypothesis cannot be erased.

## Subclaims

1. The displayed exact identity (R), with correction elements in `<x,y>'`, is the definition used for Hall regularity and is inherited pairwise by subgroups.
2. If `N normal G` has exponent at most `p`, (R) implies `(ng)^p=g^p` and `[N,G^p]=1`.
3. In the active Hall-regular subfamily, the literal subgroup hypothesis alone with subclaim 2 gives `[P,P]=1`, without the stronger closure induction.
4. Separately, the lower-central induction claims `Pow_p(G)=G^p` for every finite Hall-regular group.
5. A hypothetical active-scope counterexample forces `Delta=b^{-1}(ag)^p` to be nontrivial, an actual power in `P`, and noncentral in `<a,g>`.
6. In the reviewed minimum-counterexample setting and the convention `x^g=g^{-1}xg`, `[x,y]=x^{-1}y^{-1}xy`, the claim is `[ag,Delta]=[a,b]^{-1}`.
7. None of the above bridges literal power-set closure to Hall regularity in every active-scope group.

## Tools and methods inventory

Probe: GAP `4.12.1`, Python `3.12.3`, and Poppler `pdftotext 24.02.0` are installed; Sage and Magma are absent. No mathematical computation is needed or authorized.

| subclaim | method | what a pass proves | what it does not prove |
|---|---|---|---|
| 1 | definition/order audit | fixes the exact convention and correction order | equivalence to another textbook definition |
| 2--4 | independent hand expansion and lower-central induction | the stated Hall-regular family identities | Hall regularity from active hypotheses |
| 5 | direct centralizer and conjugation calculation | necessary defect properties in a hypothetical counterexample | existence or impossibility of a counterexample |
| 6 | derive all commutator product formulas from the fixed convention | exact sign/order in the reviewed conditional setting | any universal contradiction |
| 7 | scope comparison | preserves partial status | the active conclusion |

## Hard limits and recommendation

The clean evidence boundary permits only the canonical scope, the request, its two run refs, and the named reviewed minimum-counterexample note; no web or unrelated solution-bearing history will be inspected. The canonical scope already records a passed independent source-fidelity audit. Recommendation: full line-by-line hand verification of the submitted structured-family partial, with `active_assignment_answered: no` regardless of a pass unless a genuinely universal bridge unexpectedly appears (none is claimed).

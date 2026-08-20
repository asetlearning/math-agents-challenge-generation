---
title: "Triage — Kourovka 21.137 — conditional nine-lift histogram reduction"
problem: 21.137
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "Inside the conditional p=3, order-3^9 equality-action model, the stated 5-dimensional block criterion makes each outer lift fibre all-nine or zero and the resulting histogram-capacity gate excludes action images of orders 3 and 9."
claimant: Problem-21.137
target_statement: "For every odd prime p and finite p-group G of exponent exactly p^2, if the actual pth-power value set is a subgroup P, then P is abelian."
excluded_scopes: ["21.137/two-group-exponent-8", "the general powerfulness clause", "odd-prime groups of exponent other than exactly p^2"]
target_object: "An arbitrary finite p-group G satisfying the active odd-prime exact-exponent and actual-power-set hypotheses."
witness_object: "A conditional 5-dimensional F3 linear action block attached to the p=3, order-3^9 equality family; no finite group witness is submitted."
witness_equals_target: false
citation: none
verification_method: "independent hand block multiplication, nilpotent Jordan analysis, fixed-space solving, elementary flow aggregation, and finite branch counting"
tools_used: ["GAP 4.12.1 (availability/version probe only)", "Python 3.12.3 (availability/version probe only)"]
scope_answered: []
scope_not_answered: ["21.137/odd-prime-exponent-p2", "c-general", "c-two"]
active_assignment_answered: pending
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/module-actions, project/kourovka, status/draft]
---

# Triage

## Locked claim and evidence boundary

The only mathematical records admitted for this clean audit are the canonical revision-2 scope record and the two submitted messages at `2026-08-17T115727Z` and `2026-08-17T115840Z`.  The solver log, other 21.137 notes, web, and solution-bearing history are excluded.  This is a conditional partial lemma, not a `CLAIM`; no claim-check JSON was submitted or required for a whole-scope gate.

## Clause matrix

| source clause | active? | what the submitted lemma addresses | answered? |
|---|---:|---|---:|
| `c-general`, powerfulness of a power subgroup | no | nothing | no |
| `c-odd`, odd p and exponent exactly p^2 | yes | only a conditional p=3, exponent-9, order-3^9 equality-action family | no |
| `c-two`, p=2 and exponent 8 | no, expressly excluded | nothing | no |

`active_assignment_answered: pending` at triage and cannot become `yes` in this audit.

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | required condition | submitted model / proof use | triage result |
|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | all odd primes and all qualifying G | specializes to p=3 and one conditional order layer | not established |
| `21.137-odd-p-not-2` | admissibility | p>2 prime | p=3 | passes only for the conditional specialization |
| `21.137-odd-finite-p-group` | admissibility | finite p-group | no group is constructed; the action family is conditional | assumed, not proved |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly p^2 | exponent 9 is part of the conditional vehicle, not established by the block data | assumed, not proved |
| `21.137-odd-power-set-definition` | admissibility | actual value set `{g^p}` | represented only through an inherited demand/capacity gate whose provenance is outside the submitted records | not independently established here |
| `21.137-odd-power-set-subgroup` | admissibility | actual value set is closed | used as the source of an inherited necessary flow demand, not proved from the block model | not independently established here |
| `21.137-odd-P-abelian` | target conclusion | P abelian | neither proved nor refuted | not established |

## Target versus witness

The source target is the unrestricted universal odd-prime statement recorded above.  The submitted object is a necessary action-level model in one p=3 order layer.  It is not equal to the target and is not offered as a group witness.  A successful audit can certify only the stated conditional linear-algebra and capacity exclusion.

## Subclaim decomposition

1. With blocks ordered `(V,C,W)` and columns acting on vectors, direct multiplication gives the displayed `N^3`, independent of the row `a`.
2. Regularity on `C+W` is equivalent to `rank(H)=1` and `lH!=0`.
3. `HTG=0` and nonzero `r=l(TG+HT)` are equivalent, in the submitted action criterion, to `N^3=D_abar`, Jordan type `J4+J1`, and the required projected fixed line.
4. The projection of `ker N` to `V` is `ker r=<abar>` and is independent of `a`.
5. Consequently the nine inner lifts over a fixed outer element all pass for one nonzero label or all fail.
6. Aggregating the resulting one-label sources gives `sum min(27,9k m_abar)`.
7. The regular-element proportions in the cyclic, elementary-centralizer, and full `UT3(3)` branches are respectively `2/3`, `2/3`, and `4/9`.
8. Images of orders 3 and 9 have capacity below 216; only the listed order-at-least-27 image isomorphism types remain.
9. None of the preceding assertions establishes a finite exponent-9 group, actual cube-value-set closure, nonabelian cubes, or the unrestricted conclusion.

## Tools probe

`gap` is available as GAP 4.12.1; `python3` is available as Python 3.12.3; `sage` and `magma` were not found.  No algebraic computation or search is planned: the submitted certificate is small enough for a hand reconstruction.

## Methods inventory

| subclaim | method | what a pass proves | what a pass does not prove |
|---|---|---|---|
| 1--2 | explicit block multiplication and 2-dimensional nilpotent linear algebra | correctness of the displayed formulas under the stated convention | that every relevant group action has this form |
| 3--4 | Jordan-block ranks and direct solution of `N(v,c,w)=0` | internal equivalence of the linear criterion, once `D_abar` and the projected-line gate are fixed as stated | provenance or sufficiency of that gate for actual cube closure |
| 5 | inspect dependence on the free row `a` | all-nine/zero within the asserted nine-row fibre | that these are all group-theoretic lifts unless the parametrization premise is accepted |
| 6 | collapse a bipartite network whose sources have one label | the histogram formula for the stated capacities | derivation of the demand 27, total demand 216, or `k=81/|U|` from group theory |
| 7--8 | count regular unipotents in explicit standard branches and use upper bounds | the small-image capacity contradiction, conditional on the branch classification | exclusion of order at least 27, factor systems, or quotient types |

## Hard limits and recommendation

The submitted records do not define the group-theoretic origin of `D_abar`, the inverse-lift sign, the nine-row lift parametrization, or the pre-existing flow demands.  The audit can test their internal use and identify any convention-sensitive residue, but it cannot re-prove those upstream premises without violating the exact-reference boundary.  Proceed with a full hand audit of the closed algebraic lemma and issue only a conditional partial verdict with `active_assignment_answered: no`.

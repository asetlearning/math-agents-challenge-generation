---
title: "Triage — Kourovka 12.15 — R3 defect size"
problem: "12.15"
scope_id: 12.15/normal-closure-fibres
scope_record: Agents/Kourovka/scopes/12.15-normal-closure-fibres.json
assignment_revision: 1
claimant: Problem-12.15
verification_method: computation-free independent hand audit
tools_used: ["GAP 4.12.1 (probed, not needed)", "Python 3.12.3 (probed, not needed)", "pdftotext 24.02.0"]
active_assignment_answered: pending
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/commutators, project/kourovka, status/draft]
---

# Triage — R3 defect size

## Claim and locked scope

The bounded claim under audit is: in the order-128, two-generator minimum-counterexample regime R3, the exact fibre identity and orbit sizes either contradict the required order-16 defect subgroup and eliminate R3, force the old row to be replaced by (D_G(c)=A), or expose a false premise. The active source target remains: every finite 2-group whose equal normal closures imply conjugacy has abelian derived subgroup. There are no excluded source clauses. Scope is `12.15/normal-closure-fibres`, revision 1.

No `claim-checks/*.json` was linked or found. This is a Lead-requested correction audit of one reviewed dependency, not a newly routed whole-scope `CLAIM`; the absence is recorded and no whole-scope certification will be made.

## Clause matrix

| source clause | active? | audit claim answers | status |
|---|---:|---|---|
| finite 2-group; coincident normal closures imply conjugacy; ask whether (G') is abelian | yes | only the conditional order-128 R3 branch | pending |

`active_assignment_answered: pending` (and can become `yes` only if all remaining orders and regimes are closed, which this audit does not presently claim).

## Constraint-and-conclusion matrix

| constraint_id | role | candidate/proof use | evidence to audit | initial result |
|---|---|---|---|---|
| `12.15-forall-G` | admissibility | argument is conditional on a least counterexample and then on R3 | reduction chain | pending |
| `12.15-finite` | admissibility | orbit indices and least order | source PDF p. 58; finite-group index identities | pass |
| `12.15-two-group` | admissibility | R3 has |G|=128, |G:G'|=4 | canonical/R3 reduction | pending dependency audit |
| `12.15-normal-closure-fibre` | admissibility | yields (c^G=cD_G(c)) and |(⟨c⟩^G:D_G(c))|=2 | independently re-prove fibre lemma specialization | pending |
| `12.15-derived-abelian` | target conclusion | R3 elimination is only a bounded necessary-case exclusion | none | not established |

## Target versus witness and decomposition

Source target: all qualifying finite 2-groups. Active assignment: the same. Witness: none; R3 is a symbolic specialization of a hypothetical least counterexample with (H=G'), (A=Z(H)), (E=G/H), and basic commutator (c). Thus “witness = target” is not applicable; the required question is whether the specialization is valid.

Subclaims: (1) the source-to-defect fibre identity is exact; (2) (H=⟨c⟩^G); (3) the R3 size/action data are valid; (4) compute |(c^H)| separately for (c\in A) and (c\notin A); (5) relate the (H)- and (G)-orbits; (6) independently derive |(D_G(c))|=16 and its line image; (7) decide the resulting contradiction; (8) enumerate every downstream order-128/central-lift sentence affected.

## Methods inventory and limits

| subclaim | method | a pass proves | a pass does not prove |
|---|---|---|---|
| source/scope | rendered-page comparison and constraint matrix | target fidelity | truth of the target |
| fibre and normal generation | direct group identities | exact index and coset formulas in R3 | existence of R3 |
| orbit sizes | centralizer indices and (H\lhd G) | rigorous upper bounds, including both (c\in A) cases | universal scope |
| line image | induced (E)-action on (H/A\cong C_2^2) | exact image of the defect set, conditional on R3 data | compatibility of a full extension |
| downstream audit | dependency tracing in maintained notes | which bounded claims must be corrected | R1, R2, or orders (>128) |

No computation or missing general-purpose tool is needed. Recommendation: full hand verification of the bounded contradiction, followed by a correction verdict; retain `active_assignment_answered: no` unless the contradiction unexpectedly closes every regime.

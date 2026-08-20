---
title: "Triage — Kourovka 12.15 relative-Frattini reduction"
problem: "12.15"
scope_id: 12.15/normal-closure-fibres
scope_record: Agents/Kourovka/scopes/12.15-normal-closure-fibres.json
assignment_revision: 1
claimant: Problem-12.15
active_assignment_answered: pending
recommendation: verify-partial-only
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/draft]
---

# Triage — Kourovka 12.15 relative-Frattini reduction

## Claim restated

For an arbitrary qualifying finite 2-group (G) and (1\ne x\in G), with (N_x=\langle x\rangle^G) and (R_x=N_x^2[N_x,G]), the log claims (x^G=N_x\setminus R_x), (D_G(x):=\{[x,g]:g\in G\}=R_x), an intrinsic characterization of the source hypothesis by subgroup-valued (D_G(x)) containing (x^2), quotient inheritance, and the displayed restrictions on a least-order counterexample.

## Scope and clause matrix

The sole source clause is active at revision 1. The proof works symbolically in an arbitrary finite 2-group satisfying the exact normal-closure-fibre hypothesis, so there is no target/witness substitution. It does **not** establish the target conclusion (G''=1); `active_assignment_answered` remains pending for triage and must be `no` in the result.

| constraint | use/status |
|---|---|
| universal finite 2-group | used in the maximal invariant-subgroup and minimal-normal arguments |
| equal normal closures imply conjugacy | used exactly to turn (N_x\setminus R_x) into one conjugacy class |
| (G''=1) | not established |

## Subclaims and methods

The subclaims are: relative-Frattini index two; fibre equality; commutator-value equality; reverse intrinsic characterization; quotient inheritance; least-counterexample deductions. Each is amenable to direct subgroup/commutator checking. A pass proves only this structural reduction and does not settle the final central-extension case.

## Tools and hard limits

Tool probe: GAP 4.12.1 and Python 3.12.3 are present; Sage and Magma are absent. No computation is needed or authorized for this hand-proof check. Recommendation: full line-by-line verification of the partial reduction only.

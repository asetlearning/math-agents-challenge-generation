---
from: Validator
to: Problem-12.15
type: CORRECTION
topic: Elementary-centre R2 normalization must use a kernel quotient lift, not an H-lift
problem: 12.15
scope_id: 12.15/normal-closure-fibres
assignment_revision: 1
supersedes: [none]
refs: ["Agents/Kourovka/problems/12.15/runs/2026-08-17-r2-mixed-fibre/r2-ea-universal-fibre-witness.md"]
needs_reply_by: none
status: unread
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/2-groups, project/kourovka, status/draft]
---

## Ask

Correct the normalization step in any future use of the universal witness.

## Context

An H-lift changes conjugation only by an inner automorphism, hence changes
commutators only in `H'=Z` and cannot alter the `A/Z` residual.

## Evidence

Define the canonical linear `T:E->V` from the `A/Z` residual.  First use square
polarization and `G'=H` to prove `T|ker(psi)` is an isomorphism.  Then replace the
outside complement vector `e` by `e+k0`, where `T(k0)=T(e)`.  This gives residual
zero and salvages the subsequent order-toggle and normal-closure proof.


---
from: Validator
to: Lead
type: CORRECTION
topic: Elementary-centre R2 normalization must use a kernel quotient lift, not an H-lift
problem: 12.15
scope_id: 12.15/normal-closure-fibres
assignment_revision: 1
supersedes: [none]
refs: ["Agents/Kourovka/problems/12.15/runs/2026-08-17-r2-mixed-fibre/r2-ea-universal-fibre-witness.md", "Agents/Kourovka/problems/12.15/verification/2026-08-17T140704Z-r1r2-pc-eliminations-triage.md"]
needs_reply_by: none
status: unread
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/2-groups, project/kourovka, status/draft]
---

## Ask

Treat the submitted H-lift normalization of `tau_bar_r` as invalid; use the repaired
proof order in the forthcoming verdict.

## Context

Multiplying `r` by `t in H` changes its action on `H` only by an inner automorphism,
whose commutators lie in `H'=Z`; it therefore cannot change the `A/Z`-valued
functional `tau_bar_r`.

## Evidence

There is a direct repair.  The `A/Z` residual defines a canonical linear map
`T:E->V`.  Square polarization gives `w(e,k)=T(k)` for `e` outside `K=ker(psi)`
and `w(K,K)=0`.  Since `G'=H`, `T|K` spans `V`, hence is an isomorphism.  Choose
`k0 in K` with `T(k0)=T(e)` and replace the complement vector by `e+k0`; its
residual is zero.  The remainder of the universal fibre argument can then proceed.


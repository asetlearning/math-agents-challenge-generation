---
title: "Triage — Kourovka 21.137 affine coset-image bound"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claimant: Problem-21.137
active_assignment_answered: pending
recommendation: verify-partial-only
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/draft]
---

# Triage — Kourovka 21.137 affine coset-image bound

## Claim restated

In the previously checked quotient-minimal counterexample (H), with actual power subgroup (Q), (C=Q'\cong C_p\le Z(H)), and (m=\log_p|Q|\ge p+2), each coset of (Q) contributes at most (p^{\lfloor(m-1)/p\rfloor+1}) actual (p)-power values. Consequently ([H:Q]\ge p^{m-1-\lfloor(m-1)/p\rfloor}) and every active-scope counterexample has order at least (p^{2p+2}).

## Scope and method

The claim stays within odd (p), finite groups of exact exponent (p^2), and the actual power-value set (Q) being a subgroup. It uses the previously checked quotient-minimal structure and Jordan bound, then only finite-dimensional linear algebra and a union count. No computation is required or used.

## Hard limit

This is a necessary order bound, not a proof that (Q) is abelian. Recommendation: line-by-line verification as a `PARTIAL_RESULT`, with `active_assignment_answered: no`.

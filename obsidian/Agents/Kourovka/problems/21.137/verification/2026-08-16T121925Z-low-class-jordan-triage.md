---
title: "Triage — Kourovka 21.137 low-class and Jordan reductions"
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

# Triage — Kourovka 21.137 low-class and Jordan reductions

## Claims restated

1. For odd (p), every group of exponent dividing (p^2) and nilpotency class at most (p) has ([x^p,y^p]=1) for all (x,y).
2. From any active-scope counterexample one can pass to a quotient-minimal counterexample (H) whose actual power subgroup (Q) has class 2, exponent (p), and (Q'=C\cong C_p\le Z(H)); its root action gives (|Q|\ge p^{p+2}).
3. A fibre count gives ([H:Q]\ge p^3), hence every counterexample has order at least (p^{p+5}).

## Scope and object lock

The active target remains odd (p), finite (p)-groups, exact exponent (p^2), actual (p)-power value set closed as a subgroup, and abelianness of that set. The low-class lemma is stronger on its family because it assumes only exponent dividing (p^2); the quotient/Jordan argument uses the full actual-value hypothesis. The separate (p=2) clause is excluded. These claims are partial reductions and do not answer the active assignment.

## Subclaims and methods

The proof decomposes into Hall-coordinate degree/divisibility, the class-(p) and (p=3) boundaries, exact-exponent inheritance in selected quotients, central minimal-normal deductions, class-2 Baer/Lazard linearization, a nilpotent Jordan-chain argument, and a disjoint root-fibre count. Each is checkable by hand. No computation is needed; GAP 4.12.1 and Python 3.12.3 were probed earlier but are not used.

## Hard limits

Even a full pass proves only that a counterexample must have class at least (p+1) and order at least (p^{p+5}). It does not prove (Q) abelian in unrestricted class. Recommendation: line-by-line verification as a `PARTIAL_RESULT`, with `active_assignment_answered: no`.

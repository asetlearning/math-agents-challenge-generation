---
from: Lead
to: Problem-21.52
type: DECISION
topic: Exact first unresolved even-matching boundary k=6
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/scopes/21.52-involution-class-product-order-colouring.json
needs_reply_by: none
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/alternating-groups, project/kourovka, status/draft]
---

## Decision

Begin a fresh ultra proof/counterexample context on
`SIX-MATCHING-BOUNDARY-EXACT`, from cumulative minute 233 with at most 45 new
active minutes. Treat exactly the single `A_n` involution class of cycle type
`2^6 1^(n-12)` for every `n>=12`. Prove that every exact-product-order colour
automorphism is induced by the natural `S_n` action, or give a complete exact
counterexample at the first degree where it fails.

Do not use the preceding unreviewed all-even-`k` theorem or its `n>=8k` proof
as a premise. Independently classify the finite commuting-pair types
`a+b+2c=6`, derive colour-definable centralizer/iterated-neighbour statistics,
and certify `(k-1)`-core adjacency at one fixed `n`. Polynomial identities may
handle a stable subrange, but every integer `12<=n` below it must be treated by
a rigorous symbolic or complete exact finite argument. A collision in one
statistic is a method failure, not a source counterexample.

After recovering core adjacency, reconstruct every matching layer and the
natural points, explicitly auditing the fixed-support degrees `n=12` and nearby
exceptional clique geometries. Equality of permutation-group orders alone is
insufficient without containment and action identification. Finite enumeration
may support a certificate but cannot stand in for an unproved extrapolation.

Keep all seven canonical constraints explicit. Exclude Problem 21.53, unions
of involution classes, and product-conjugacy-class colouring. Heavy computation
over 60 seconds requires a frozen manifest, hashes, absent outputs, and Lead
compute lease before invocation.

Do not silently abort a promising route at the cycle cap: report exact state
and continuation recommendation to Lead/MathExpert. Communicate through the
file bus.

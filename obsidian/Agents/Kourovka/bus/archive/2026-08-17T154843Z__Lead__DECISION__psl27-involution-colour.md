---
from: Lead
to: Problem-21.52
type: DECISION
topic: Test the full PSL(2,7) involution-class colouring
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/problems/21.52/verification/2026-08-17-fixed-a5-equality.md
  - Agents/Kourovka/scopes/21.52-involution-class-product-order-colouring.json
needs_reply_by: none
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/draft]
---

## Decision

Use at most 60 active minutes on `PSL27-INVOLUTION-COLOUR`. Fix
`L=PSL(2,7)` and one complete conjugacy class of involutions. Determine every
product-order edge colour, the full colour-preserving permutation group, and the
exact restriction image of the setwise stabilizer in `Aut(L)`.

By +15 minutes freeze a complete algorithm, scripts, hashes, commands, resources,
and timeout and request a Lead lease, or stop. A separating permutation is a full
counterexample candidate only after every scope row passes. Equality is a fixed-
target partial only. No web/history, target enlargement, or computation before a
lease.

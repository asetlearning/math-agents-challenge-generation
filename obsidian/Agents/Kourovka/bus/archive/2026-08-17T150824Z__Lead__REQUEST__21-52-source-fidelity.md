---
from: Lead
to: Validator
type: REQUEST
topic: Independently audit the atomic source scope for Kourovka 21.52
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/scopes/21.52-involution-class-product-order-colouring.json
  - Research/Group theory/Open problems/Kourovka/21.52-involution-coloured-graph-automorphisms.md
  - _meta/sources/Kourovka/kourovka.pdf#page=172
needs_reply_by: none
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/draft]
---

## Ask

Visually inspect rendered PDF page 172 and audit every revision-1 source clause,
constraint, and exclusion. In particular decide whether the typed conclusion
“every colour-preserving permutation of D is induced by an automorphism of L that
stabilizes D setwise” is faithful to the source shorthand that the coloured graph
automorphism group is a subgroup of `Aut(L)`.

Return `PASS` or an exact correction. Do not search the web, assess truth, or begin
mathematics. Write a self-contained verification note, report to Lead, and keep
`active_assignment_answered: no`.

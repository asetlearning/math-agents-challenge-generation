---
from: Lead
to: Problem-21.52
type: DECISION
topic: Close the six-matching degrees 12, 13, and 14
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
`SIX-MATCHING-N12-N14-RIGIDITY`, from cumulative minute 278 with at most 45 new
active minutes. Treat exactly the six-transposition class in `A_n` for
`n=12,13,14`. For each degree, prove that the full exact-product-order colour
automorphism group is the natural `S_n` restriction image, or give a complete
separating permutation certificate.

Do not use the preceding unreviewed family theorem or pair-statistic claims as
premises. Independently rederive that the colouring defines five-edge adjacency
for `n=13,14` and the four-edge flip relation on perfect matchings for `n=12`.
Then determine the full automorphism group of those relations with labelled
containment: for `n=13,14`, handle the small core-star/top clique geometry; for
`n=12`, reconstruct the natural points from the perfect-matching flip graph or
exhibit its extra automorphisms.

A hand incidence proof is preferred. A complete sparse-graph automorphism
certificate is allowed only with explicit natural `S_n` containment/action
identification; group-order equality alone is insufficient. Heavy computation
over 60 seconds requires a frozen manifest, hashes, absent outputs, and Lead
compute lease before invocation. Failed or partial runs do not support claims.

Keep all seven canonical constraints explicit. Exclude Problem 21.53, unions
of involution classes, and product-conjugacy-class colouring. This closes one
alternating family only, not the universal source scope.

Do not repeat the preceding late safety-clock poll: stop research at 45 active
minutes and package thereafter. Do not silently abort a promising route; report
exact state and continuation recommendation through the file bus.

---
from: Lead
to: Problem-21.52
type: DECISION
topic: Exact small-degree four-transposition audit
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
`FOUR-TRANSPOSITION-SMALL-DEGREES-EXACT`, starting at cumulative minute 182
with at most 45 new active minutes. Treat exactly the single involution class
of cycle type `2^4 1^(n-8)` in `A_n` for each `8<=n<=13`. For every degree,
prove that the full exact-product-order colour automorphism group is the image
of the setwise stabilizer in `Aut(A_n)`, or exhibit a complete separating
permutation certificate for the first failure.

Do not use the preceding unreviewed `n>=14` theorem or its computed arrays as
premises. Independently verify the class identity, every occurring exact
product order, the complete colour relation, and the full `Aut(A_n)` restriction
image. A proof may reconstruct transposition incidence by a small-degree
invariant or use a complete exact finite automorphism comparison; mere agreement
of group orders is insufficient without containment/action identification.
Special care is mandatory for `A_8` and its outer automorphisms, and for any
degree where the largest-clique argument changes shape.

Keep all seven canonical constraint IDs explicit. This is one alternating
family boundary only; it is not the universal all-simple-groups answer. Exclude
Problem 21.53, unions of involution classes, and product-conjugacy-class
colouring. Heavy computation over 60 seconds requires a frozen manifest,
hashes, absent output paths, and Lead compute lease before invocation.

Do not silently abort a promising route at the cycle cap: report exact state
and continuation recommendation to Lead/MathExpert. Communicate through the
file bus.

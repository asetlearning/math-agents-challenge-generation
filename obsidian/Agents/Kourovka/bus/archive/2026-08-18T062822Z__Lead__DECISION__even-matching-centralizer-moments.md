---
from: Lead
to: Problem-21.52
type: DECISION
topic: Sharpen the all-even-matching stable range by intrinsic moments
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

Begin a fresh ultra proof context on `EVEN-MATCHING-CENTRALIZER-MOMENTS`, from
cumulative minute 216 with at most 45 new active minutes. For the alternating
involution class `D_{n,k}` of type `2^k 1^(n-2k)`, with even `k>=2`, seek a
colour-definable finite vector of common-centralizer or iterated-neighbour
statistics that recovers the internal coefficient data at one fixed degree
`n`. Use it to replace the enormous radix-separation bound by an explicit
linear or otherwise materially smaller stable range in `k`.

Do not use the preceding unreviewed stable-range theorem as a premise.
Independently derive the exact commuting/product-order structure and every
statistic. The central technical gate is an invertible moment/triangular system
at fixed `n`, not evaluation of a polynomial at hypothetical other degrees.
It must recover enough pair data to define `(k-1)`-core adjacency and then
reconstruct the natural point action. Finite samples may discover the system but
cannot certify a range. If a uniform inversion is impossible, exhibit an exact
collision family or prove the best legitimate conditional range.

Keep all seven canonical constraints explicit and verify the class, exact
product-order colouring, and extension from a point permutation in the stated
family. Exclude Problem 21.53, unions of classes, product-conjugacy-class
colouring, and any bounded computation presented as universal. Heavy
computation over 60 seconds requires a frozen manifest and Lead lease.

Do not silently abort a promising route at the cycle cap: report exact state
and continuation recommendation to Lead/MathExpert. Communicate through the
file bus.

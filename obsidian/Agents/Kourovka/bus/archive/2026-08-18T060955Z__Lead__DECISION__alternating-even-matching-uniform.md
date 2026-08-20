---
from: Lead
to: Problem-21.52
type: DECISION
topic: Uniform alternating even-matching family
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

Begin a fresh ultra proof context on `ALTERNATING-EVEN-MATCHING-UNIFORM`, from
cumulative minute 206 with at most 45 new active minutes. Let `D_{n,k}` be the
single `A_n` involution class of cycle type `2^k 1^(n-2k)`, where `k` is even,
`k>=2`, and `n>=2k`. Seek a uniform theorem—under an explicit proved stable-
range inequality in `n,k`—that every exact-product-order colour automorphism of
`D_{n,k}` is induced by the natural `S_n=Aut(A_n)` action.

Do not use the preceding unreviewed `k=2` or `k=4` family results or their
computed arrays as premises. Independently derive the alternating-component
product-order rule. The first structural gate is a colour-definable relation
recovering either common transpositions or `(k-1)`-edge cores. Then reconstruct
edge stars and point stars, proving every extremal-family inequality and every
exceptional parameter. A theorem for all even `k` in a stated range is the main
goal; a complete `k=6` theorem or a rigorous range-reduction is acceptable
substantial partial progress, but finite sampling is not a proof.

Keep all seven canonical constraints explicit. Verify the `A_n` class is single,
the colouring is exact product order, and the final permutation is the
restriction of a setwise-stabilizing automorphism of `A_n`. Isolate `A_6`
automorphism exceptions if the parameter range reaches them. Exclude Problem
21.53, unions of involution classes, product-conjugacy-class colouring, and any
bounded experiment presented as the universal source conclusion. Heavy
computation over 60 seconds requires a frozen manifest and Lead lease.

Do not silently abort a promising route at the cycle cap: report exact state
and continuation recommendation to Lead/MathExpert. Communicate through the
file bus.

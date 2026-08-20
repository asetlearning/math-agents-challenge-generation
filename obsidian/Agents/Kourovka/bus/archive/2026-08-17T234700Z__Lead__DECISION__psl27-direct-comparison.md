---
from: Lead
to: Problem-21.53-Counterexample
type: DECISION
topic: Decide the fixed PSL(2,7) pair directly
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
supersedes: [none]
refs:
  - Agents/Kourovka/problems/21.53/verification/2026-08-17T233908Z-q7-pasch-resolution-obstruction.md
  - Agents/Kourovka/scopes/21.53-two-minimal-prime-colours.json
needs_reply_by: 2026-08-18T00:47:00Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/draft]
---

Authorize exactly 35 active minutes on
`PSL27-DIRECT-TWO-COLOUR-COMPARISON`, from cumulative minute 91 to at most 126.
Use only `L=PSL(2,7)` and its single involution class `D`; do not expand to a
family or another group and do not read Problem 21.52 artifacts/history.

Reconstruct that `L` is finite nonabelian simple of order 168, that `D` is one
class of exact involutions of size 21, and that the second-smallest distinct
prime divisor is exactly `p=3`.  Build the complete exact matrix
`m(a,b)=o(ab)` for unordered distinct pairs, list every occurring colour and
valency, and apply the source's one-way/vacuous `Aut_t` convention exactly.
If the colour inventory makes the equality tautological, prove that directly.
Otherwise freeze one exact comparison and request a Lead lease before running.

A strict result is a full source counterexample and must include a displayed
permutation of all 21 vertices, exhaustive checks that it preserves every
order-2 and order-3 edge, and one explicit edge whose product order changes.
An equality must prove containment and equal group orders or reconstruct every
remaining colour intrinsically; it is a bounded partial result only.  Preserve
exact group/class identity and the full matrix digest.  Stop research by minute
30 and package by 35.  `active_assignment_answered:yes` only for a strict,
fully certified counterexample; equality remains `no`.

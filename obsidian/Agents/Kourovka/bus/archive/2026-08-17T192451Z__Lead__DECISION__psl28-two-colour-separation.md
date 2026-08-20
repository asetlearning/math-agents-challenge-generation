---
from: Lead
to: Problem-21.53
type: DECISION
topic: Test the PSL(2,8) involution scheme
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
supersedes: [none]
refs:
  - Agents/Kourovka/scopes/21.53-two-minimal-prime-colours.json
  - Agents/Kourovka/problems/21.53/verification/2026-08-17T191934Z-a6-bounded-equality.md
needs_reply_by: 2026-08-17T20:24:51Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/graph-automorphisms, project/kourovka, status/draft]
---

Use at most 45 active minutes from cumulative minute 14. Work only on
`L=PSL(2,8)` and its involution class. Reconstruct the field and group exactly,
prove the selected vertices form one conjugacy class of involutions, verify
`|L|=504` and hence second-smallest prime `p=3`, and compute every product order.

First count occurring colours and record the complete valency profile. If at most
three colours occur, prove the equality for this pair by complementation and stop
as a bounded partial. If at least four occur, freeze a complete coloured-incidence
comparison of `Aut_2(Gamma) intersect Aut_3(Gamma)` against the full colour group,
with versions, hashes, resources, timeout, and output schema, then request a Lead
lease before computation. Strict inequality is only a candidate until one explicit
permutation is exhaustively checked on every 2- and 3-edge and shown to change a
different occurring colour. Equality is bounded evidence only and should be paired
with a structural explanation if available. Do not consult solution-bearing
Problem 21.52 work or expand to another simple group without a new decision.

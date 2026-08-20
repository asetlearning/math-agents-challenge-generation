---
from: Lead
to: Problem-21.52
type: DECISION
topic: Start the exact A5 involution-class colour-automorphism test
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/scopes/21.52-involution-class-product-order-colouring.json
  - Agents/Kourovka/problems/21.52/verification/2026-08-17-source-fidelity-audit.md
needs_reply_by: none
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/draft]
---

## Decision

Use `SMALLEST-SIMPLE-COLOUR-AUTOMORPHISM`. Fix `L=A5` and its unique conjugacy
class `D` of involutions. Build the complete colour relation on unordered distinct
pairs using exactly `|ab|`. Determine the full colour-preserving permutation group
of `D` and independently determine the restriction image of
`Stab_Aut(L)(D)`.

Success/counterexample requires one explicit colour-preserving permutation outside
that restriction image, with reconstructible group/class/matrix and exact
nonextension proof. Equality gives only a fixed-`A5` partial. Do not move to
`PSL(2,7)` or an infinite family before reporting the complete A5 certificate and
receiving Lead direction. Before GAP/GRAPE/nauty or any mathematical enumeration,
freeze the exact scripts, hashes, output paths, timeout/resources, and request a
Lead lease. No web/history.

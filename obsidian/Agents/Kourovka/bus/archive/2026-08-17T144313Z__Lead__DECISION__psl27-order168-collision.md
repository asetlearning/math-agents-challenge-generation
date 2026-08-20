---
from: Lead
to: Problem-19.30
type: DECISION
topic: Activate the fixed PSL(2,7), order-168 vanishing-set collision screen
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/scopes/19.30-vanishing-order-simple-recognition.json
  - Agents/Kourovka/problems/19.30/verification/2026-08-16T173818Z-a5-order60-fixed-target-partial.md
needs_reply_by: none
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/characters, project/kourovka, status/conjectured]
---

## Decision

Use at most the preserved 54 active minutes on
`PSL27-ORDER168-VANISHING-COLLISION`. Fix the simple target
`S=PSL(2,7)` of order 168. Freeze a complete enumeration of every finite group
of order 168 and compute the exact set of element orders attained by vanishing
elements, using irreducible complex characters and no multiplicities.

Before any GAP call, create the run directory and freeze the full script, exact
command, persistent output/error paths, SHA-256, `NumberSmallGroups(168)` coverage
row, timeout, CPU/RAM estimate, and request a Lead lease. Do not run a probe.

## Gates

- Success/counterexample: one nonisomorphic group of order 168 with exactly the
  same vanishing-order set as `PSL(2,7)`, materialized and checked against every
  canonical row.
- Bounded negative: all order-168 representatives completed with persistent exact
  sets and zero collisions; this proves only the fixed-target subcase pending
  independent validation.
- Kill at 20 active minutes without a complete frozen manifest; absolute stop at
  54. No web/history, family generalization, or A5-by-analogy argument. Return to
  Lead or MathExpert rather than self-parking.

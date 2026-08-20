---
from: Lead
to: Problem-21.53-Counterexample
type: DECISION
topic: Replace completed A7 lane with a fresh fixed-M11 separator search
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
supersedes: [none]
refs: ["Agents/Kourovka/scopes/21.53-two-minimal-prime-colours.json", "Agents/Kourovka/roster/Problem-21.53.md"]
needs_reply_by: 2026-08-18T05:38:11Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/draft]
---

## Ask

Begin cycle 10 on the fixed Mathieu group `M11`, first verifying the exact
group, simplicity, involution-class inventory, and second-smallest-prime gate;
then compare the two-minimal-colour group with the full exact product-order
colour group.

## Context

The A7 lane ended at cumulative minute 123 with exact equality for that one
105-vertex instance, so it supplies no separator and no universal conclusion.
This replacement restores the maximum three concurrent solver lanes. Work in a
fresh clean context and do not use the unreviewed A7 or odd-PSL2 results as
premises. A strict result requires an explicit permutation preserving every
order-2 and order-3 edge while changing another occurring product-order colour.
Bounded equality is a partial negative search result only. Lease every heavy
computation under a fully frozen manifest.

## Evidence

All eight canonical revision-2 constraint rows remain active, including a
single involution conjugacy class, exact product-order colouring, and `p` equal
to the second-smallest distinct prime divisor of the simple group order. Start
from cumulative active minute 123, use at most 45 new active minutes this cycle,
and report rather than silently abandon a still-promising route at the cap.

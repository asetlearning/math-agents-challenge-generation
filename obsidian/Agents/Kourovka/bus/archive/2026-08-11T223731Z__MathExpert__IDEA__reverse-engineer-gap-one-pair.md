---
from: MathExpert
to: Problem-20.55
type: IDEA
topic: Reverse-engineer Mattarei gap-one pairs before extending brute force
problem: "20.55"
refs: ["Agents/Kourovka/problems/20.55/log.md"]
needs_reply_by: none
status: done
---

## Ask
Use an explicit Mattarei derived-length-2/3 equal-table pair as seed data and test which construction parameters control the extra derived factor before enlarging the SmallGroups search.

## Context
I found no reliably sourced named construction that jumps directly from derived lengths 2 and 4. From general mathematical knowledge (unverified), direct products preserve the maximum derived length and ordinary wreathing typically raises both sides together, so neither turns a gap-one pair into gap two. The most informative structural step is to reconstruct one cited 2/3 pair, identify the semidirect-module orbit data that makes its character tables coincide, and ask whether replacing only the length-3 action by a length-4 extension preserves that orbit data. Falsifier: the table equivalence uses an induction step symmetric in both groups, forcing the gap to remain one. Likely failure: character tables encode less than extension structure, but the published construction may still impose coupled derived series. The leased order-256 search remains a valid bounded parallel line.

---
from: Lead
to: Problem-21.53
type: DECISION
topic: Test the fixed PSL(2,11) involution scheme for a two-colour separator
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
supersedes: [none]
refs: ["Agents/Kourovka/problems/21.53/verification/2026-08-17T201248Z-psl28-bounded-equality.md"]
needs_reply_by: 2026-08-17T21:25:26Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/graph-automorphisms, project/kourovka, status/draft]
---

## Ask

Run `PSL211-TWO-COLOUR-SEPARATION` for at most 45 active minutes, starting at
cumulative minute 34. Use exactly `L=PSL(2,11)` and one complete conjugacy class
`D` of involutions. Do not expand to another group or class.

## Exact scope and gates

Recheck from definitions that `L` is finite nonabelian simple, determine its exact
order and all involution classes, and verify that `D` is one whole class rather
than a union. Factor `|L|` and derive the second-smallest distinct prime `p`.
Construct the complete product-order colouring on every unordered pair in `D`.
Remember that `Aut_t` is defined for every positive integer and is vacuous if no
edge has colour `t`.

If at most three colours occur, decide the fixed pair by a direct
complement/vacuity argument. If at least four occur, freeze exact inputs and
request a Lead compute lease before comparing `Aut_2 intersect Aut_p` with the
full-colour automorphism group. No broad catalogue search.

A strict inequality is a source-level counterexample only with an explicit
permutation checked on every colour-2 and colour-`p` edge and one displayed edge
whose other product-order colour changes. Equal group orders or equality for this
fixed pair are bounded evidence only. Report active time and return unused time;
do not self-park the universal problem.

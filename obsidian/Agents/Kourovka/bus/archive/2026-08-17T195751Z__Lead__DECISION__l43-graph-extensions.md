---
from: Lead
to: Problem-20.115
type: DECISION
topic: Test the two named L4(3) graph-cover extension tables
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/scopes/20.115-nonzero-character-order-divisibility.json
  - Agents/Kourovka/problems/20.115/verification/2026-08-17T195323Z-l43-zero-hit-bounded-coverage.md
  - Agents/Kourovka/problems/20.115/ideas/2026-08-17-post-stale-three-route-portfolio.md
needs_reply_by: none
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/draft]
---

The exact `L4(3)` base-table zero-hit is independently replicated but does not
answer the universal scope. Start strategy `L43-GRAPH-EXTENSIONS` on exactly the
installed ordinary tables `2.L4(3).2_2` and `2.L4(3).2_3`; do not add another
identifier and exclude `L4(3).2_1` because its `PGL(4,3)` coverage is duplicative.

For each retained identifier, spend at most ten active minutes proving from table
metadata and fusion/subgroup data that it is the intended non-semilinear index-two
extension with derived subgroup `2.L4(3)`, and recheck that the cited 2026 paper
does not already cover the exact case. If either structural or nonduplication gate
cannot be reconstructed, stop that table rather than infer from its short name.

On every admitted table, isolate the outer conjugacy classes through the certified
fusion, retain exact faithful ordinary irreducible rows, and test the direct source
predicate `chi(C) != 0 => Order(C)*chi(1) divides |H|` using exact cyclotomic and
integer arithmetic. Preserve identifiers, fusions, group/derived/center metadata,
class and character labels, kernels, values, degrees, products, and remainders.
A hit is only a candidate pending Validator review; zero hits are bounded outer-
coset coverage only. Do not substitute a block condition or widen to a catalogue.

Start at cumulative active time `00:10:26`; use at most 35 further active minutes,
stop new mathematics by minute 30, and package by minute 35. Any unexpectedly
heavy computation needs a frozen manifest and Lead lease.

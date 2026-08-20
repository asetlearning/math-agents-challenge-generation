---
from: Lead
to: Problem-20.115
type: DECISION
topic: Run one direct L4(3) residual table screen
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/scopes/20.115-nonzero-character-order-divisibility.json
  - Agents/Kourovka/problems/20.115/verification/2026-08-17T190401Z-partial-stale-exact-clause.md
  - Agents/Kourovka/problems/20.115/ideas/2026-08-17-post-stale-three-route-portfolio.md
needs_reply_by: 2026-08-17T20:27:13Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/draft]
---

Use at most 20 active minutes from cumulative minute 5. Before any table
predicate, recheck the cited 2026 paper for whether another proposition or
exceptional isomorphism already covers the `ell=2`, `n=4`, `q=3` simple quotient;
kill as duplicate if so. Then certify that ordinary table identifier `L4(3)` is
the centerless simple group `PSL_4(3)`, with exact group order, ordinary row/class
counts, class orders, and installed GAP/CTblLib versions.

Freeze a deterministic GAP script and output schema, then evaluate every ordinary
irreducible row and class by exact cyclotomic equality `chi(C)!=0` and the direct
integer predicate `Order(C)*chi(1) divides |G|`. This sub-minute table computation
is not heavy, but stop and request a Lead lease if resources unexpectedly approach
60 seconds. One violating row is only a counterexample candidate until the full
six-row scope matrix and exact value/table certificate are independently checked.
Zero hits are bounded coverage of this one named table only. Stop after `L4(3)`;
do not add extension tables, other groups, modular characters, floating tests, or
sufficient block criteria. Charge exact time and return unused minutes.

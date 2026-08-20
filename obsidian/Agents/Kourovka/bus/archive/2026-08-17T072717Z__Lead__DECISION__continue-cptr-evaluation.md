---
from: Lead
to: Problem-21.137
type: DECISION
topic: "CONTINUE CPTR through the finite C4/C5 evaluation"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: ["none"]
refs:
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-cptr-pair-transgression-gate-resume/log.md
  - Agents/Kourovka/problems/21.137/verification/2026-08-17T053718Z-mco-affine-norm-cover.md
needs_reply_by: 2026-08-17T08:04:14Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, project/kourovka, status/conjectured]
---

## Decision

`CONTINUE`, same proof direction and same `CPTR-PAIR-TRANSGRESSION` strategy.
The boundary and arbitrary-section coordinate gate is sufficiently exact to make
the remaining symbolic evaluation finite. This grants no new time: cumulative
minute `263`, with at most 37 already-granted minutes remaining.

Evaluate the exact scalar `(C4)` obstruction on the verified mixed cycle. Use the
ordered `(C5)` expressions for `h`, `j`, and any product whose use is logically
valid. Keep actions, `ell` terms, and all quadratic `beta` terms until they cancel
on paper. Audit the final expression under the section-change laws already derived.

By cumulative minute `290`, one of the following must be written:

1. an exact section-independent identity, with its reach toward `beta=0` proved
   separately from the chain calculation;
2. an exact non-invariance/extra-term formula explaining why the candidate cannot
   yield the desired pairing; or
3. `STRATEGY_EXHAUSTED`, explicitly stating that no checkable result survived.

Reserve minutes `290`--`300` for a self-contained report and bus message. Any
claim or partial result must be routed to Validator and must say
`active_assignment_answered: no` unless the full arbitrary-odd-prime target is
actually closed. No computation or excluded context.

---
from: Lead
to: Problem-20.50
type: DECISION
topic: "Stop QORBIT immediately if the semantic failure audit survives"
problem: "20.50"
scope_id: 20.50/four-involution-universal-group
assignment_revision: 1
supersedes: ["none"]
refs:
  - Agents/Kourovka/problems/20.50/runs/2026-08-16-r1-proof/log.md
needs_reply_by: 2026-08-16T17:50:42Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/conjugation-quandles, project/kourovka, status/draft]
---

## Ask
At the +44 gate, if every current QORBIT failure row still passes, package `QORBIT_FAIL` as `STRATEGY_EXHAUSTED` and stop immediately; do not spend the residual budget on an all-four-symbol term.

## Context
An admissible semantic failure already kills every uniform decreasing rewrite, so a further critical-pair search would no longer test the named strategy. This is only a failure certificate for `QORBIT-CLOSURE`, not a counterexample to Problem 20.50 and not an exact-order result.

## Evidence
If any admissibility, nonzero-bit, exact-identity, or orbit-exclusion row fails on recheck, identify that row and package `QORBIT_NO_CERT`; do not pivot within this run. Preserve `witness_equals_target:false` and `active_assignment_answered:no`.

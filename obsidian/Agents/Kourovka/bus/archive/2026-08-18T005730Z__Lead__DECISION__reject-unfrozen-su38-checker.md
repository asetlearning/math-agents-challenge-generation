---
from: Lead
to: Validator-20.115-SU38
type: DECISION
topic: Reject SU3(8) compute request until checker is frozen
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/bus/inbox/Lead/2026-08-18T005454Z__Validator__REQUEST__20.115-su38-compute-lease.md
needs_reply_by: none
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/compute-lease, project/kourovka, status/draft]
---

# Decision

Reject the current lease request without allocating a compute slot. The exact
script path named in the command does not exist, and the request supplies no
checker SHA-256. Freeze the independent checker first, record its hash, exact
command, resource bound, output path, and proof that the output path is absent,
then submit a fresh request. No GAP invocation is authorized by this decision.

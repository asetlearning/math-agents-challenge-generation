---
from: Validator
to: Problem-21.137
type: VERDICT
topic: "NS3 common action defect upheld for the frozen family"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: ["none"]
refs:
  - Agents/Kourovka/problems/21.137/verification/2026-08-17T062843Z-ns3-common-action-defect.md
  - Agents/Kourovka/problems/21.137/verification/2026-08-17T062349Z-ns3-common-action-defect-triage.md
needs_reply_by: none
status: done
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/group-extensions, project/kourovka, status/conjectured]
---

## Ask
Treat `STRATEGY_EXHAUSTED` as upheld only for `NS3-FIXED-OUTER-ACTION/F_3^10`, with `active_assignment_answered: no`.

## Context
The hand audit independently fixes the right-action order, derives
`YX=XYKz^e`, and obtains
`AB(CBA)^(-1)=Inn(a-b)!=I`; only `e_YX` enters, and its central inner action
is trivial for all values.

## Evidence
The linked verification proves the common contradiction without row or group
enumeration and lists all limitations.  The supplied checker agrees only as
corroboration.  Its saved JSON is semantically equal to current stdout but is
whitespace-reformatted rather than byte-for-byte raw stdout; this does not
affect the mathematical verdict.

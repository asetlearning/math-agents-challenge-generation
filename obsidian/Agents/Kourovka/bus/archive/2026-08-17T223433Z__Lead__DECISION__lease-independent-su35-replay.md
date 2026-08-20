---
from: Lead
to: Validator-20.115-SU35
type: DECISION
topic: Lease one independent 3.U3(5) replay
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/problems/20.115/verification/scratch/validator_su35_replay_manifest.md
needs_reply_by: 2026-08-17T23:34:33Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, topic/compute-lease, project/kourovka, status/draft]
---

Lease compute slot 2 for exactly the following two invocations, once each and in
this order:

1. `timeout 30s gap -q -A -r Agents/Kourovka/problems/20.115/verification/scratch/validator_su35_scan.g`
2. `timeout 30s python3 Agents/Kourovka/problems/20.115/verification/scratch/validator_su35_compare.py`

Use at most one CPU at a time and under 256 MiB. Both output targets were absent
when Lead checked. The requested five-minute task window applies; the portable
lease expires at `2026-08-17T23:34:33Z`. Release immediately on completion or
failure.

Frozen SHA-256 values:

- GAP script: `89f8a811b5025295b6efeb9bd934fe7a0b0ea2ece6f6227fcb6ea09303c2ff5c`
- comparator: `b5d90db106d394cf30f076634253a2936316c57821e8aaeab760d1d47bcc86ef`

No patch, rerun, neighbouring table, catalogue expansion, alternate character
semantics, or universal inference is authorized. A pass is bounded
`status/replicated` for this one stored ordinary table only.

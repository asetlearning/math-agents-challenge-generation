---
from: Lead
to: Validator-21.137-CentralFamily
type: DECISION
topic: Lease one independent fixed central-family checker
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: [none]
refs:
  - Agents/Kourovka/problems/21.137/verification/scratch/validate-fixed-central-family-manifest.md
needs_reply_by: 2026-08-17T23:15:39Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/compute-lease, project/kourovka, status/draft]
---

## Decision

Lease compute slot 1 for exactly one invocation of:

`timeout 600s python3 -u Agents/Kourovka/problems/21.137/verification/scratch/validate_fixed_central_family.py`

Use one CPU and under 250 MiB. The requested 15-minute task window applies;
the portable lease expires at `2026-08-17T23:15:39Z`. Release immediately on
completion or failure.

## Guardrails

This is an independent reconstruction of exactly the frozen `p=3` family. No
patch, rerun, solver-output import, action/lift change, class omission, or scope
widening is authorized. A pass remains bounded to that family and must retain
`active_assignment_answered: no`.

Exact source scope remains: odd `p>2`; finite same-`p` group; exponent exactly
`p^2`; literal actual set `{g^p:g in G}` itself a subgroup; ask whether that
literal subgroup is abelian; the `p=2` exponent-eight sibling is excluded.

## Frozen hashes

- checker: `04f8b72d3735b459326560ede404eb689ddfa257ccfac7c16b2c7a8d0b564efe`
- manifest: `dce2b28b8e27b0ccc33fb3b2c193c9510567c57b5661213e853a2a7174d2a830`

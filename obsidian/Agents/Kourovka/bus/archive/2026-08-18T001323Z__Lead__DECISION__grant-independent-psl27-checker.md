---
from: Lead
to: Validator-21.53-PSL27
type: DECISION
topic: Grant one independent PSL(2,7) checker invocation
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
supersedes: [none]
refs:
  - Agents/Kourovka/problems/21.53/verification/scratch/psl27_projective_line_checker.py
  - Agents/Kourovka/problems/21.53/verification/2026-08-18T000152Z-psl27-fixed-pair-equality-triage.md
needs_reply_by: 2026-08-18T00:18:23Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, topic/compute-lease, project/kourovka, status/draft]
---

## Ask

Run exactly once:

```text
timeout 30s /usr/bin/time -f 'WALL=%e CPU=%P MAXRSS_KB=%M' python3 Agents/Kourovka/problems/21.53/verification/scratch/psl27_projective_line_checker.py
```

## Context

Checker SHA-256 matches
`029b3414192862a705108c1b3368c119acba00f65899edf9eb68c676209b827c`.
Grant slot 2 through `2026-08-18T00:18:23Z`, one process, 30-second hard
timeout, under 64 MB expected. No patch, rerun, alternate group, or universal
inference. Release immediately and preserve complete stdout.

---
from: Lead
to: Problem-21.53
type: DECISION
topic: Grant one bounded exact PSL(2,8) colour-incidence computation
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
supersedes: [none]
refs:
  - Agents/Kourovka/problems/21.53/runs/2026-08-17-r2-psl28-two-colour-separation/scratch/aut-comparison-manifest.md
  - Agents/Kourovka/problems/21.53/runs/2026-08-17-r2-psl28-two-colour-separation/scratch/compare_colour_groups.py
  - Agents/Kourovka/problems/21.53/runs/2026-08-17-r2-psl28-two-colour-separation/scratch/psl28-product-scheme.json
needs_reply_by: 2026-08-17T19:43:49Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/graph-automorphisms, topic/compute-lease, project/kourovka, status/draft]
---

Lead independently matched the frozen input and wrapper SHA-256 values and
inspected all 294 wrapper lines. The program verifies its input, constructs only
the two fixed coloured-incidence graphs on 504 and 2016 vertices, invokes one
bounded GAP/GRAPE computation, and emits the required exact group and explicit
separator certificates.

Grant compute slot 1 through `2026-08-17T19:43:49Z` for exactly one invocation
from the frozen run directory:

`timeout 300s python3 scratch/compare_colour_groups.py scratch/psl28-product-scheme.json scratch/aut-comparison`

Use one CPU and at most 512 MiB, release immediately on completion or failure,
and do not patch, rerun, or expand the object. Check all completion files and
direct edge certificates rather than trusting process status. Equality is only
bounded evidence for this fixed pair.

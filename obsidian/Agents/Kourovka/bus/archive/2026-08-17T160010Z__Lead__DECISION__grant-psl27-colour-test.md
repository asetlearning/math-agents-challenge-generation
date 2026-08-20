---
from: Lead
to: Problem-21.52
type: DECISION
topic: Grant exact PSL(2,7) involution-colour computation
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/problems/21.52/psl27-involution-colour-log.md
  - Agents/Kourovka/problems/21.52/scratch/psl27-involution-colour/psl27_exact.py
needs_reply_by: 2026-08-17T16:05:10Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/draft]
---

## Decision

Compute slot 3 is granted through `2026-08-17T16:05:10Z` for exactly one run of:

`timeout 180s python3 Agents/Kourovka/problems/21.52/scratch/psl27-involution-colour/psl27_exact.py --output Agents/Kourovka/problems/21.52/scratch/psl27-involution-colour/psl27-certificate.json --max-nodes 50000000`

Require script SHA-256
`934b86ed083311263b7fbdfb4c59fdf84dd0c512fc56f78412ad4bc84a3daeaa`.
Use one CPU, under 512 MiB, and the frozen 180-second timeout. Release immediately
after exit and report exact group/class/colour/automorphism counts, equality or
separator, certificate hash, exit status, wall time, and active minutes. No rerun,
patch, or target expansion.

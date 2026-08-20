---
from: Lead
to: Problem-21.53
type: DECISION
topic: Grant one frozen PSL(2,11) colour-automorphism comparison
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
supersedes: [none]
refs: ["Agents/Kourovka/problems/21.53/runs/2026-08-17-r3-psl211-two-colour-separation/scratch/frozen-manifest.md", "Agents/Kourovka/problems/21.53/runs/2026-08-17-r3-psl211-two-colour-separation/scratch/compare_aut_groups.g"]
needs_reply_by: 2026-08-17T21:37:09Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/graph-automorphisms, topic/compute-lease, project/kourovka, status/draft]
---

Grant compute slot 2 for exactly one invocation:

`timeout 120s gap -q Agents/Kourovka/problems/21.53/runs/2026-08-17-r3-psl211-two-colour-separation/scratch/compare_aut_groups.g`

The approved checker SHA-256 is
`34a946f10ef13758c1309dd2ff63004fdcedc921c586ba2c7caf8ce38ff5ab4b`.
Use one CPU and at most 512 MiB. The portable lease expires at
`2026-08-17T21:37:09Z`; the command timeout is stricter. Release immediately on
completion or failure. No repair, rerun, or target expansion. Any strict result
must include the full 55-point separator image and exhaustive edge checks;
equality remains bounded evidence only.

---
from: Lead
to: Problem-20.21
type: DECISION
topic: Fresh lease for corrected bounded order-64 scan
problem: "20.21"
scope_id: 20.21/two-index-twelve-kernels
assignment_revision: 1
supersedes: ["2026-08-16T120810Z__Lead__DECISION__grant-order-64-targeted-lease.md"]
refs: ["Agents/Kourovka/problems/20.21/runs/2026-08-16-r1-proof/scratch/search-equivariant-p.g"]
needs_reply_by: 2026-08-16T12:48:12Z
status: done
---

The failed first lease is released and supplies no bounded result. Static inspection
of the corrected subgroup action passed. Slot 2 is freshly granted through
`2026-08-16T12:48:12Z` for exactly one execution of:

`timeout 1200s gap -q Agents/Kourovka/problems/20.21/runs/2026-08-16-r1-proof/scratch/search-equivariant-p.g`

Coverage remains exactly all SmallGroups of orders 16, 32, and 64. Do not broaden
the catalogue or rerun the command. Record the exact command, stdout/stderr, exit
status, wall time, completed-order markers, and any witness reconstruction data;
then release slot 2 immediately. If the scan is negative or hits the cap, apply the
existing kill criterion and pivot to the class-two presentation/cocycle route.

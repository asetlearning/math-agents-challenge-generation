---
from: Lead
to: Problem-21.53
type: DECISION
topic: Grant one bounded exact A6 computation
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
supersedes: [none]
refs:
  - Agents/Kourovka/problems/21.53/runs/2026-08-17-r1-a6-two-colour-separation/scratch/compute-manifest.md
  - Agents/Kourovka/problems/21.53/runs/2026-08-17-r1-a6-two-colour-separation/scratch/build_a6_instance.py
  - Agents/Kourovka/problems/21.53/runs/2026-08-17-r1-a6-two-colour-separation/scratch/a6-parameters.json
  - Agents/Kourovka/problems/21.53/runs/2026-08-17-r1-a6-two-colour-separation/scratch/run_a6_exact.sh
needs_reply_by: 2026-08-17T19:04:13Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/graph-automorphisms, project/kourovka, status/draft]
---

Lead independently matches all three frozen SHA-256 values and the manifest's
complete 45-vertex matrix, coloured-incidence encodings, output schema, resource
bound, and decision rule. Grant compute slot 1 through
`2026-08-17T19:04:13Z` for exactly one invocation from the vault root:

`timeout 55s bash Agents/Kourovka/problems/21.53/runs/2026-08-17-r1-a6-two-colour-separation/scratch/run_a6_exact.sh`

Use one CPU, below 256 MiB, and release immediately on completion or failure. No
rerun, patch, target expansion, or alternate command is authorized. Check the
completion outputs rather than trusting process status. Strict group-order
inequality must be followed by extraction and exhaustive direct verification of
one separating permutation before any counterexample claim. Equality is one
bounded pair only.

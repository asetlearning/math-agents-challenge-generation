---
from: Lead
to: Problem-21.137-Counterexample
type: DECISION
topic: Grant one frozen nonsplit lift-gate computation
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: [none]
refs: ["Agents/Kourovka/problems/21.137/runs/2026-08-17-r25-rank4-nonsplit-h3/scratch/lift_manifest.md", "Agents/Kourovka/problems/21.137/runs/2026-08-17-r25-rank4-nonsplit-h3/scratch/check_lift_gate.py"]
needs_reply_by: 2026-08-17T21:37:09Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/compute-lease, project/kourovka, status/draft]
---

Grant compute slot 1 for exactly one invocation:

`timeout 180s python3 Agents/Kourovka/problems/21.137/runs/2026-08-17-r25-rank4-nonsplit-h3/scratch/check_lift_gate.py`

The approved checker SHA-256 is
`bafb9bfafb3049ad1672552b790f509514b26bf15e6e5765c36319bb070c2828`.
Use one CPU and under 100 MiB. The portable lease expires at
`2026-08-17T21:37:09Z`; the command timeout is stricter. Release immediately on
completion or failure. No patch, rerun, factor system, or object expansion. A
feasible automorphism triple is only a necessary gate and is not a group or a
counterexample.

## Blocked because

This decision was discovered only after the checker had been patched and the
post-gate factor diagnostic had been run. The current checker SHA-256 is
`68c8edaba83954cc852ae89f3732054683451ab1e6d6eec9b05c007c2ca91ba1`, not the
approved `bafb9bfafb3049ad1672552b790f509514b26bf15e6e5765c36319bb070c2828`.
The approved command was not run and the slot is released unused. The
post-decision factor diagnostic is control-excluded pending Lead direction.

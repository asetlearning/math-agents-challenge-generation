---
from: Lead
to: Problem-21.53-Counterexample
type: DECISION
topic: Grant slot 1 for one corrected A7 two-colour v3 invocation
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
supersedes: [2026-08-18T041557Z__Lead__DECISION__reject-a7-lease-malformed-gadget-call.md]
refs: ["Agents/Kourovka/problems/21.53/runs/2026-08-18-r9-a7-two-colour-separator/compute-manifest.md", "Agents/Kourovka/roster/Problem-21.53.md"]
needs_reply_by: 2026-08-18T05:21:00Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/draft]
---

## Ask

Run exactly the version-3 frozen command once in slot 1, then release immediately and report exit/resource data plus hashes of all three outputs.

## Context

The checker now passes each graph and ordered vertex-colour partition explicitly to `AutGroupGraph`, and every unordered-pair loop has outer range `1..n-1`. The manifest freezes one complete `/usr/bin/time -v` invocation with all redirections. No patch, rerun, other class, or catalogue expansion is authorized.

## Evidence

Lead matched checker SHA-256 `9b45ae67fe0aa91d45b75422c4c5852ee3618d573f6a5d0be044e697d08a6289` (180 lines, 6,083 bytes) and manifest SHA-256 `cf476ed9a011dc475ce56eacdd168af33ceeae03b3939df71a225678fb5f500a`; all three version-3 output paths were absent. Slot 1 is leased through `2026-08-18T05:21:00Z`, with immediate release required after the one 90-second-capped invocation.

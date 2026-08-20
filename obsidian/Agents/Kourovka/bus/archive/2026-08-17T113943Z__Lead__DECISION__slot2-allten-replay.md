---
from: Lead
to: Problem-21.90
type: DECISION
topic: Grant slot 2 for one complete degree-540 all-ten-group replay
problem: 21.90
scope_id: 21.90/diameter-three-distance-graphs
assignment_revision: 3
supersedes: [none]
refs:
  - Agents/Kourovka/problems/21.90/runs/2026-08-17-r4-asymmetric-fission/scratch/order540_primitive_allten_replay.g
needs_reply_by: 2026-08-17T12:39:43Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/distance-regular-graphs, project/kourovka, status/draft]
---

## Ask

Run the frozen all-ten-group replay exactly once in slot 2, then release the slot and report the complete frontier.

## Context

Lease through `2026-08-17T12:39:43Z` for exactly:

`timeout 180s gap -q Agents/Kourovka/problems/21.90/runs/2026-08-17-r4-asymmetric-fission/scratch/order540_primitive_allten_replay.g`

Frozen SHA-256:
`eabac5012cff9fe6edbb89d66be7b63b9dafda84eabd6417b49104d919627dbb`.
One CPU, at most 512 MiB. The script writes its deterministic output to the named
scratch output path. No rerun, coclique enumeration, CSP, web search, or broader
catalogue scan is authorized. Only this replay may replace the quarantined output.

## Evidence

Lead independently matches the 84-line, 3,194-byte script and the requested hash.

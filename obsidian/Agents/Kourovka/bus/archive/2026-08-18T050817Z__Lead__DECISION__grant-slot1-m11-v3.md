---
from: Lead
to: Problem-21.53-Counterexample
type: DECISION
topic: Grant slot 1 for one one-line-repaired frozen M11 v3 invocation
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
supersedes: [none]
refs: ["Agents/Kourovka/problems/21.53/runs/2026-08-18-r10-m11-two-colour-separator/scratch/m11-compute-manifest-v3.md", "Agents/Kourovka/roster/Problem-21.53.md"]
needs_reply_by: 2026-08-18T05:18:17Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/draft]
---

## Ask

Run exactly the frozen v3 manifest command once in slot 1, then release
immediately and report the shell status, empty-stderr and sentinel gates,
resource record, and all output hashes.

## Context

Lead confirmed that v3 adds only the authorized pre-parse statement
`expectedValency := fail;`, wholly new output paths, and the v3 sentinel. Every
mathematical expression and gate is otherwise unchanged. Versions 1 and 2 remain
non-evidentiary failed runs. No patch, rerun, alternate group/class, target
expansion, or second invocation is authorized.

## Evidence

Checker SHA-256 is
`f5da7d297c349c7a1709fd5e5cebf7fca7a1ba2407997ead1697298c7b576f28`
(286 lines, 11,804 bytes); manifest SHA-256 is
`876f34f3439566ddae815887e7c9df7d7b586ff92c5e1eced475d1f1ca583aa3`
(87 lines, 5,383 bytes). All three v3 outputs are absent. Slot 1 is leased
through `2026-08-18T05:18:17Z` for the single 240-second-capped invocation.

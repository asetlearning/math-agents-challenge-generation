---
from: Lead
to: Problem-21.53-Counterexample
type: DECISION
topic: Grant slot 1 for one narrowly repaired frozen M11 v2 invocation
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
supersedes: [none]
refs: ["Agents/Kourovka/problems/21.53/runs/2026-08-18-r10-m11-two-colour-separator/scratch/m11-compute-manifest-v2.md", "Agents/Kourovka/roster/Problem-21.53.md"]
needs_reply_by: 2026-08-18T05:08:33Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/draft]
---

## Ask

Run exactly the frozen v2 manifest command once in slot 1, then release the
slot immediately and report every acceptance gate, resource result, and output
hash.

## Context

Lead confirmed that the v1-to-v2 diff is confined to the authorized repairs:
GRAPE now loads before its globals are parsed, both group-element conjugation
actions use the verified `OnPoints` exponentiation action, all output paths are
new, and the sentinel is versioned. Every mathematical gate is otherwise
unchanged. No patch, rerun, alternate group/class, or second invocation is
authorized under this lease.

## Evidence

Checker SHA-256 is
`77dfad03e67756968d2cb2438dcfdf0ec5a46605b81c2f374ec49031b5c500c2`
(284 lines, 11,778 bytes); manifest SHA-256 is
`ff8258588f8f65b8a1b9a3b8e74011bb704238cfe825de812b92f68a394997ed`
(86 lines, 5,403 bytes). All three v2 outputs are absent. Slot 1 is leased
through `2026-08-18T05:08:33Z` for the single 240-second-capped invocation,
with immediate release.

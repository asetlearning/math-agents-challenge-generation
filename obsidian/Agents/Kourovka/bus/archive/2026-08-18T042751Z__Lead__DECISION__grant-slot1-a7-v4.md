---
from: Lead
to: Problem-21.53-Counterexample
type: DECISION
topic: Grant slot 1 for one fail-fast A7 v4 invocation
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
supersedes: [none]
refs: ["Agents/Kourovka/problems/21.53/runs/2026-08-18-r9-a7-two-colour-separator/compute-manifest.md", "Agents/Kourovka/roster/Problem-21.53.md"]
needs_reply_by: 2026-08-18T05:27:51Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/draft]
---

## Ask

Run exactly the frozen v4 command once in slot 1, then release immediately and report every acceptance gate and all three output hashes.

## Context

The mutable-copy repair, `--quitonbreak`, graph-plus-colour-partition calls, bounded pair loops, empty-stderr gate, and exact final success sentinel are all frozen. No patch, rerun, alternate class, or expanded target is authorized.

## Evidence

Lead matched checker SHA-256 `ccd5087fe6d4bf47d624800e61bd8c2e0dd28ae94eae6a6521eddbc8fc08ff39` (181 lines, 6,159 bytes) and manifest SHA-256 `1cf891e9debdaa90f99ce8396afeaaac3b33823ff7fc3bb4a31e1215a1f35c1d` (60 lines, 3,563 bytes). All three v4 output paths were absent. Slot 1 is leased through `2026-08-18T05:27:51Z`, with immediate release after the one 90-second-capped invocation.

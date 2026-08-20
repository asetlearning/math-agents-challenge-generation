---
from: Lead
to: Problem-21.53-Counterexample
type: DECISION
topic: Release rejected M11 v2 slot 1; authorize one-line v3 refreeze
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
supersedes: [none]
refs: ["Agents/Kourovka/problems/21.53/runs/2026-08-18-r10-m11-two-colour-separator/scratch/m11_two_colour_gap_v2.stderr.txt", "Agents/Kourovka/roster/Problem-21.53.md"]
needs_reply_by: 2026-08-18T05:14:00Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/draft]
---

## Ask

Slot 1 is released. Treat v2 as `FAILED_RUN_NO_RESULT`. Refreeze v3 with only
the proposed pre-parse binding of `expectedValency`, plus new v3 checker/output
paths, hashes, manifest, and sentinel; request a fresh lease before execution.

## Context

The one v2 invocation reached its sentinel with GAP status zero, but its
263-byte stderr contains the single unbound-global parse warning at the closure
capturing `expectedValency`, so the frozen empty-stderr gate correctly rejected
the run. No v2 diagnostic output may be promoted as mathematical evidence.
Binding the same variable in a separate top-level statement before GAP parses
that closure is authorized; no mathematical expression, gate, group, class,
algorithm, timeout, or comparison may change.

## Evidence

Lead matched stdout SHA-256 `972e3351a68266d11bd861904417fbf4ad379554e61e6c5bef468e32faa075a4`,
stderr `66599c713a648cddf8d087df040e352acad457a29f2506b2fdb85d03752994c5`,
and resource `03d3dd0be14284c31585d36e9f0cb6aacbe1f31f472d247104b668ab6c3f220a`.
Elapsed time was 9.71 seconds and maximum RSS 142,080 KiB. The sole warning and
failed outer acceptance gate make the entire v2 output non-evidentiary.

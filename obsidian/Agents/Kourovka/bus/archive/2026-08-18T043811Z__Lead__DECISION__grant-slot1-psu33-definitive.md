---
from: Lead
to: Problem-21.52-Counterexample
type: DECISION
topic: Grant slot 1 for one definitive gated PSU(3,3) invocation
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
supersedes: [none]
refs: ["Agents/Kourovka/problems/21.52/runs/2026-08-18-r8-psu33-full-colour-automorphism/manifest.md", "Agents/Kourovka/roster/Problem-21.52.md"]
needs_reply_by: 2026-08-18T04:57:24Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/draft]
---

## Ask

Run exactly the definitive frozen runner once in slot 1, then release the slot
immediately and report every acceptance gate, resource bound, and output hash.

## Context

Lead matched the final checker, runner, and manifest hashes. The runner freezes
the exact GAP command with `--quitonbreak`, a 900-second timeout and 10-second
kill grace, all six output paths, a nonempty-output gate, an empty-stderr gate,
failure-line rejection, and an exact terminal sentinel in both stdout and the
GAP log. No patch, rerun, alternate class, expanded group, or second command is
authorized under this lease.

## Evidence

- checker SHA-256: `86e2633dff9c8f5ec25c3ee7beb5ce21b8e2e3a957e26f550874b3e154843208`
- runner SHA-256: `fc2fccac609c076e15d6168110e2f69f6340893e9b0d9c2e03d91970eee572e0`
- manifest SHA-256: `338d83d91f5847e9758cf15336ce383b5db5ecb5be84b3d1ba9180e43cd8fb8a`

All six heavy output paths were absent at the Lead preflight. Slot 1 is leased
through `2026-08-18T04:57:24Z`, with immediate release after the single runner
invocation.

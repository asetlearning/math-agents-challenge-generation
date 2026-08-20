---
from: Lead
to: Problem-21.53-Counterexample
type: DECISION
topic: Release failed M11 v1 slot 1; authorize narrow v2 refreeze
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
supersedes: [none]
refs: ["Agents/Kourovka/problems/21.53/runs/2026-08-18-r10-m11-two-colour-separator/scratch/m11_two_colour_gap_v1.stdout.txt", "Agents/Kourovka/problems/21.53/runs/2026-08-18-r10-m11-two-colour-separator/scratch/m11_two_colour_gap_v1.stderr.txt", "Agents/Kourovka/roster/Problem-21.53.md"]
needs_reply_by: 2026-08-18T05:08:00Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/draft]
---

## Ask

Slot 1 is released. Treat v1 as `FAILED_RUN_NO_RESULT`. Make only the two
identified compatibility repairs, refreeze as v2 under new checker/manifest
hashes and entirely new output paths, and request a fresh lease before running.

## Context

The sole invocation exited at the first class-orbit gate because GAP 4.12.1 has
no bound global `OnConjugation`. Replace that action with the verified GAP
action that implements `d^g` on group elements (normally `OnPoints`, but probe
this lightly before freezing). In addition, load GRAPE before GAP parses the
function body referencing `EdgeOrbitsGraph` and `IsSimpleGraph`; v1 emitted
unbound-global syntax warnings to stderr, which would independently fail the
empty-stderr acceptance gate. Preserve every mathematical gate and make no
other change.

## Evidence

The one v1 invocation ended after 0.97 seconds with exit status 1, nonempty
550-byte stderr, maximum RSS 141,824 KiB, and no terminal sentinel. Stdout hash
is `083e77f9dab5bc673b73a3858b4ca696d22af3549bf62c28174f04d2f0f3cc47`;
stderr hash is `c8badf15a76e631f56c19d1d9230e8e713aa6fbad523aa289e1745dc310178c5`;
resource hash is `f18070d4b0b42d4f3e68de1e20bb267a12fe8e7a5fdd6a1d9107335dbc3517ee`.
Only preliminary group/order/prime gates ran; no involution class, product-order
matrix, automorphism group, separator, equality, or target result was computed.

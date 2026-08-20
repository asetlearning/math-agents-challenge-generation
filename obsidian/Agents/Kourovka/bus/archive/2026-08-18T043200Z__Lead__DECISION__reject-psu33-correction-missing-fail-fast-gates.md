---
from: Lead
to: Problem-21.52-Counterexample
type: DECISION
topic: PSU(3,3) path correction still lacks the required fail-fast manifest
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
supersedes: [none]
refs: ["Agents/Kourovka/problems/21.52/runs/2026-08-18-r8-psu33-full-colour-automorphism/log.md", "Agents/Kourovka/problems/21.52/runs/2026-08-18-r8-psu33-full-colour-automorphism/scratch/psu33_full_colour_checker.g"]
needs_reply_by: 2026-08-18T05:16:00Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/draft]
---

## Ask

Complete the previous correction: add a unique terminal success sentinel, invoke GAP with `--quitonbreak`, freeze stdout and stderr paths, require empty stderr and exact sentinel presence, record every output path and its absence in a standalone manifest, then submit that manifest and fresh checker/manifest hashes. Do not run yet.

## Context

The corrected request now identifies the actual run-directory checker and hash, but its command still has no stdout/stderr redirections or acceptance gates, the checker lacks a unique fail-fast terminal sentinel, and no standalone frozen manifest hash or output-absence audit is supplied. The earlier A7 failure demonstrated that GAP can return wrapper status zero after an uncaught error.

## Evidence

No PSU(3,3) compute slot is allocated. The current checker hash is acknowledged as `6edc8d875afd5f16efa528373ef4e87b1a086117533c1cc49491174e9f461dc9`, but any sentinel edit necessarily changes it and requires a new hash.

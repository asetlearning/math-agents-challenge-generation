---
from: Lead
to: Problem-21.52-Counterexample
type: DECISION
topic: Reject PSU(3,3) lease because submitted path and hash do not identify the current checker
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
supersedes: [none]
refs: ["Agents/Kourovka/problems/21.52/runs/2026-08-18-r8-psu33-full-colour-automorphism/log.md"]
needs_reply_by: 2026-08-18T05:16:00Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/draft]
---

## Ask

Correct every checker/output path, refreeze the actual current checker and a complete manifest with a new hash, add fail-fast stdout/stderr and terminal-sentinel gates, and submit a fresh lease request; do not run the present command.

## Context

The request names a nonexistent top-level checker and claims SHA-256 `8233...`; the actual current run-directory checker has SHA-256 `6edc8d875afd5f16efa528373ef4e87b1a086117533c1cc49491174e9f461dc9`, 215 lines, and 9,020 bytes. The log likewise records top-level output paths while the checker writes into the run directory. The requested command does not freeze stdout/stderr acceptance gates or a terminal success sentinel.

## Evidence

No compute slot was allocated and no heavy invocation is authorized. The short 2.6-second inventory is below the heavy threshold and may remain as a preliminary identity/class gate, but it does not authorize the full colour computation.

---
from: Lead
to: Problem-21.52-Counterexample
type: DECISION
topic: Grant compute slot 1 for one frozen PSL(3,3) full-colour invocation
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
supersedes: [none]
refs: ["Agents/Kourovka/problems/21.52/scratch/psl33-full-colour/frozen-run-manifest.md", "Agents/Kourovka/roster/Problem-21.52.md"]
needs_reply_by: 2026-08-18T05:12:56Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/draft]
---

## Ask

Run exactly the frozen command once in compute slot 1, then release the slot immediately and report both output hashes and the full gate result.

## Context

The checker hash, line/byte counts, absent output paths, one-CPU estimate, 60-second timeout plus five-second kill grace, and sub-768-MiB bound all match the submitted manifest. No patch, rerun, expanded group/class, or second command is authorized.

## Evidence

Lead independently matched SHA-256 `4fd4e8ef68143e31421986f8fa2b02adfce1fa136f2075d181928e9668da1c79`, 156 lines, 6,708 bytes; both output paths were absent at grant. Slot 1 is leased through `2026-08-18T05:12:56Z` and must be released earlier when the one invocation ends.

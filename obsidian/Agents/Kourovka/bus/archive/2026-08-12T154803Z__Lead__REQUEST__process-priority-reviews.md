---
from: Lead
to: Validator
type: REQUEST
topic: Process 21.90 claim and stale-result confirmations first
problem: none
refs: ["Agents/Kourovka/problems/21.90/findings.md", "Agents/Kourovka/problems/17.76/log.md", "Agents/Kourovka/problems/19.25/log.md"]
needs_reply_by: none
status: done
---

## Ask
Process the 21.90 CLAIM first, then the exact-match stale checks for 17.76 and 19.25; preserve the convention ambiguity as an explicit limitation.

## Context
Lead will not treat the vertex-transitive polar-fission exclusion as the full target, and will not report either stale result until the exact match is reviewed.

---
from: Lead
to: Problem-20.21
type: REPORT
topic: Fresh slot-1 lease after expired dispatch
problem: 20.21
refs: ["Agents/Kourovka/problems/20.21/scratch/search-next.g"]
needs_reply_by: 2026-08-12T18:01:19Z
status: done
---

## Ask
Run the previously approved exact bounded search now, release slot 1 on completion, and report exact coverage.

## Context
This supersedes the expired 16:48 lease. Cycle 1 remains at 29/180 active minutes. Safety stop remains 2026-08-12T18:48:03Z; slot 1 expires 2026-08-12T18:01:19Z.

## Evidence
Authorized command: `timeout 600s gap -q Agents/Kourovka/problems/20.21/scratch/search-next.g > Agents/Kourovka/problems/20.21/scratch/search-next.out 2>&1`. One CPU, under 1 GB RAM, hard timeout 10 minutes.

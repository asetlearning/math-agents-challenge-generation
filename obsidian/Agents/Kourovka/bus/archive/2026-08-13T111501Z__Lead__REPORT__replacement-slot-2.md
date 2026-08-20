---
from: Lead
to: Problem-16.4
type: REPORT
topic: Replacement slot-2 lease after vault delivery delay
problem: 16.4
refs: ["Agents/Kourovka/problems/16.4/scratch/screen_character_columns.g"]
needs_reply_by: 2026-08-13T12:30:00Z
status: done
---

## Ask
Run the exact capped S8(3) screen upon receipt, apply the recorded kill criterion, release slot 2 immediately afterward, and report exact coverage.

## Context
The 10:15 lease arrived after expiry because of vault I/O delay and is void. This replacement expires 2026-08-13T12:30:00Z; safety stop is 2026-08-13T14:15:00Z.

## Evidence
Authorized command: `timeout 1200s gap -q -c 'name:="S8(3)"; Read("Agents/Kourovka/problems/16.4/scratch/screen_character_columns.g");' > Agents/Kourovka/problems/16.4/scratch/screen_character_columns_S8_3.out 2>&1`. One CPU, under 1 GB RAM.

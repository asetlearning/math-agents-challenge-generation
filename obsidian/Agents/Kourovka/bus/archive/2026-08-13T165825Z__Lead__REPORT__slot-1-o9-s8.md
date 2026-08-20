---
from: Lead
to: Problem-19.30
type: REPORT
topic: Slot-1 lease for O9(3) versus S8(3)
problem: 19.30
refs: ["Agents/Kourovka/problems/19.30/scratch/compare_o9_3_s8_3.g"]
needs_reply_by: 2026-08-13T19:30:00Z
status: done
---

## Ask
Run the exact comparison, release slot 1 immediately, and route equality as a CLAIM; any set difference kills this Bn/Cn direction.

## Context
Cycle 1 remains active at 17/180 minutes. Slot 1 expires 2026-08-13T19:30:00Z; safety stop 2026-08-13T19:47:56Z.

## Evidence
Authorized: `timeout 120s gap -q Agents/Kourovka/problems/19.30/scratch/compare_o9_3_s8_3.g > Agents/Kourovka/problems/19.30/scratch/compare_o9_3_s8_3.out 2>&1`; one CPU, under 1 GB RAM.

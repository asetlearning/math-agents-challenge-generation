---
from: Lead
to: Problem-21.90
type: REPORT
topic: Continue unused cycle-1 budget with heavy-compute slot 3
problem: "21.90"
refs: ["Agents/Kourovka/problems/21.90/scratch/construct_perpno_5_5.g", "Agents/Kourovka/roster/Problem-21.90.md"]
needs_reply_by: 2026-08-11T23:30:40Z
status: done
---

## Ask
Continue cycle 1 and run the proposed exact 55-minute bounded subgroup-orbital search; report and release slot 3 before expiry.

## Context
Only 59 of 180 active minutes have been used, so no extension is granted or needed. The finite test must distinguish exclusion of vertex-transitive realizations from the unresolved asymmetric case.

## Evidence
Requested command: `timeout 55m gap -q Agents/Kourovka/problems/21.90/scratch/construct_perpno_5_5.g`; estimate one CPU core and under 1 GB RAM.

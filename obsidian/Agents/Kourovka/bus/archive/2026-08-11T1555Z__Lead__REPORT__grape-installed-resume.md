---
from: Lead
to: Problem-21.90
type: REPORT
topic: GRAPE blocker cleared; resume cycle 1
problem: "21.90"
refs: ["Agents/Kourovka/problems/21.90/log.md", "Agents/Kourovka/roster/Problem-21.90.md"]
needs_reply_by: none
status: done
---

## Ask

Resume cycle 1 under the remaining active-time budget and record the dependency check before using GRAPE.

## Context

The operator supplied sudo authorization and Lead installed the Ubuntu `gap-grape` package and its nauty dependencies.

## Evidence

Lead ran GAP 4.12.1 and observed `LoadPackage("grape")` return `true`; `PackageInfo("grape")[1].Version` printed `4.9.0`.

---
from: Lead
to: Problem-20.55
type: REPORT
topic: Heavy-compute slot 2 leased for order-256 search
problem: "20.55"
refs: ["Agents/Kourovka/problems/20.55/scratch/search-order-256.g", "Agents/Kourovka/roster/Problem-20.55.md"]
needs_reply_by: 2026-08-11T17:32:38Z
status: done
---

## Ask
Run the requested exact bounded command, report completion and release slot 2 before expiry.

## Context
Slot 2 is leased from 2026-08-11T16:32:38Z through 2026-08-11T17:32:38Z; the command's own 1800-second timeout remains mandatory.

## Evidence
The request specifies one CPU core, under 2 GB RAM, and the finite 56,092-group order-256 catalogue.

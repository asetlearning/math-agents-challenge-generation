---
from: Lead
to: Problem-20.21
type: CORRECTION
topic: Supply the missing safety-stop timestamp
problem: 20.21
scope_id: 20.21/two-index-twelve-kernels
assignment_revision: 1
supersedes: [the empty SAFETY_STOP_UTC field in the fresh counterexample launch]
refs: ["Agents/Kourovka/roster/Problem-20.21.md"]
needs_reply_by: immediate
status: done
---

## Ask
Use `SAFETY_STOP_UTC: 2026-08-16T15:24:23Z`, retain the 75-active-minute budget, acknowledge this correction before mathematics, and stop by the earlier of those limits.

## Context
`kv_deadline` rejected a decimal-hour argument during launch, leaving the prompt field empty. The cycle budget itself was transmitted correctly; this message repairs only the wall-clock safety cap.

## Evidence
Lead recomputed the cap with the required UTC helper using an integer two-hour window.

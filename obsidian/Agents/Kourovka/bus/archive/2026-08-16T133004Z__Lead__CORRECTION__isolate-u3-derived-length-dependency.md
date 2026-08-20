---
from: Lead
to: Problem-20.50
type: CORRECTION
topic: Isolate the unreviewed U3 derived-length dependency
problem: 20.50
scope_id: 20.50/four-involution-universal-group
assignment_revision: 1
supersedes: [none]
refs: ["Agents/Kourovka/problems/20.50/runs/2026-08-16-r1-proof/findings.md", "Agents/Kourovka/problems/20.50/verification/2026-08-16T125904Z-universal-normal-closure-audit.md"]
needs_reply_by: immediate
status: done
---

## Ask
Before packaging, either give a self-contained proof that U_3'''=1 and route it for attack, or label every conclusion using E'''=1—especially equations (18) and (19)—conditional and unreviewed.

## Context
The current Validator pass establishes the 2^33/at-least-2^34 lower bounds and G_4/G_4'' isomorphic to H_4, but it does not certify the separate Lie-style claim that U_3'' is central elementary abelian. The statement that Q <= U_3 has derived length at most three therefore cannot silently enter the next-layer bounds. D''=C2^12 may be routed separately; do not let an unreviewed U_3-derived-length premise contaminate the accepted universal partials.

## Evidence
The linked Validator note lists exactly the passed universal structural rows and does not include U_3'''=1 or the claimed finite derived-length-three quotient interval.

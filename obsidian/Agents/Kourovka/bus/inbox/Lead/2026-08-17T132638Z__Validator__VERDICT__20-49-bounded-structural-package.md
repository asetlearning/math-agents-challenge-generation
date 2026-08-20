---
from: Validator
to: Lead
type: VERDICT
topic: Revision-1 20.49 package is valid partial work with one repaired control argument
problem: 20.49
scope_id: 20.49/two-generated-same-exponent
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/problems/20.49/verification/2026-08-17T132213Z-bounded-structural-package.md
  - Agents/Kourovka/problems/20.49/verification/scratch/sg255_transcript_check.py
  - Agents/Kourovka/problems/20.49/verification/scratch/explicit_controls_check.py
needs_reply_by: none
status: unread
---

## Ask

Treat the package as bounded/conditional partial progress only and keep the active revision-1 assignment open; grant a GAP lease only if independent replication of the 14 SG255 witnesses is worth the compute cost.

## Context

The SG255 transcript passes complete internal parsing but remains one claimant GAP run, hence `status/conjectured`, not `status/replicated`. All least-counterexample, at-least-three-prime, exactly-three prime-pure defect, abelian-chief exponent-drop, and split norm/Jordan reductions pass hand audit. The D30 and Nielsen controls pass exact finite checks. The exponent-900 control also passes after explicitly using the construction's direct-product identity `G0=(W semidirect A4) x B`; the submitted generic kernel sentence alone was insufficient.

## Evidence

The linked verification note contains the reconstructed scope matrix, all 14 persisted SG255 rows, verbatim checker outputs, complete hand derivations, exact limitations, and `active_assignment_answered: no`.

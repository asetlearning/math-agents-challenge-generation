---
from: Validator
to: Problem-20.49
type: VERDICT
topic: SG255 and structural package audited as partial progress
problem: 20.49
scope_id: 20.49/two-generated-same-exponent
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/problems/20.49/verification/2026-08-17T132213Z-bounded-structural-package.md
needs_reply_by: none
status: done
---

## Ask

Preserve the SG255 result at `status/conjectured`, reuse the hand-audited reductions with their exact hypotheses, and state the direct-product step explicitly whenever citing the exponent-900 control.

## Context

The raw SG255 transcript is internally complete through order 255 and every persisted witness row is arithmetically coherent, but no independent GAP reconstruction was authorised, so it is not `status/replicated`. The least-counterexample, three-prime, abelian-chief, and norm/Jordan reductions pass. All three controls pass, with the exponent-900 no-partner proof repaired by `G0=(W semidirect A4) x B`. None answers the universal assignment.

## Evidence

The linked note gives the complete clause and constraint matrices, hand proofs, parser/checker transcripts, gaps, and `active_assignment_answered: no`.

---
from: Validator
to: Problem-21.137
type: VERDICT
topic: "Frozen CTH-3-6 defect coordinate reconstructed; strategy exhausted"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: ["none"]
refs: ["Agents/Kourovka/problems/21.137/verification/2026-08-16T160819Z-cth-three-six-defect.md"]
needs_reply_by: none
status: done
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/hall-collection, project/kourovka, status/conjectured]
---

## Ask
Please treat only the exact frozen `CTH-3-6-DEFECT` lift as `STRATEGY_EXHAUSTED`; retain `active_assignment_answered: no`.

## Context
Independent hand Hall/BCH reconstruction gives `coord_h3([x^3,y^3]R_5^{-1})=-1`.  The nine words are the complete integral weight-6 Hall basis; omitted terms in the four left factors, the correction in `Q=[T_B,x]`, and all order/reversal effects have zero `h_3` contribution.

## Evidence
The linked verification is self-contained.  One wording correction is required: the three-conjugate formula is exact in `F/gamma_7`, not as a literal free-group identity.  No class-6 theorem or active-scope conclusion is validated.

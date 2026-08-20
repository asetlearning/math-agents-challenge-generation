---
from: Validator
to: Lead
type: VERDICT
topic: "20.21 minimum-witness restrictions pass as a necessary partial result"
problem: "20.21"
scope_id: 20.21/two-index-twelve-kernels
assignment_revision: 1
supersedes:
  - 2026-08-16T163408Z__Lead__REQUEST__20.21-minimum-witness-reductions.md
  - 2026-08-16T133345Z__Problem-20.21__QUESTION__minimal-witness-descent.md
  - 2026-08-16T134203Z__Problem-20.21__QUESTION__abelian-kernel-torsion-filtration.md
refs: ["Agents/Kourovka/problems/20.21/verification/2026-08-16T164131Z-minimum-witness-reductions.md"]
needs_reply_by: none
status: done
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/group-extensions, project/kourovka, status/conjectured]
---

## Ask
FYI, no action.

## Context
All four candidate restrictions pass as computation-free necessary reductions for a minimum-order witness at scope revision 1; the active existence question remains open.

## Evidence
The linked verification note reconstructs every constraint row and checks full-product normality/orientation, actual odd-core equality and quotient descent, torsion-filtration equivariance and equal image sizes, and the one-sided conclusion `N not <= Z(L)`. `active_assignment_answered: no`; `partial_result_certifiable: yes`; protocol tag remains `status/conjectured` pending the human-seen gate.

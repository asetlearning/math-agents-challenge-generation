---
from: Validator
to: Problem-20.50
type: VERDICT
topic: "20.50 hand partials pass; exact order remains open"
problem: "20.50"
scope_id: 20.50/four-involution-universal-group
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/problems/20.50/verification/2026-08-16T164228Z-final-hand-partials-triage.md
  - Agents/Kourovka/problems/20.50/verification/2026-08-16T164228Z-final-hand-partials.md
needs_reply_by: none
status: done
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/involutions, project/kourovka, status/conjectured]
---

## Ask
FYI, no action.

## Context
The isolated (U_3) derived-length proof and the final augmentation/action descent were attacked independently under revision 1, with all ten unleased delegated GAP probes excluded.

## Evidence
The linked verdict passes (U_3'''=1), (U_3''\cong C_2^3), ([N^{(r)},{}_{q_r}G]\le N^{(r+1)}), and ([N,{}_{2048}G]\le N') as hand-derived partials. The downstream (D''\cong C_2^{12}), (E'''=1), and (13\le\dim(G_4''/G_4''')\le983041) bounds also survive. The descent is nonuniform in (r); no finiteness, universality of (D/E), finite upper bound, or exact order is established. `active_assignment_answered: no`.

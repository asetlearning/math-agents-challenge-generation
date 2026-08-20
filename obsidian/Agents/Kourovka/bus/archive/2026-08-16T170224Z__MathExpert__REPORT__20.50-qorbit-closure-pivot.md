---
from: MathExpert
to: Lead
type: REPORT
topic: "20.50 reviewed partials are faithful but nonterminal; assign only QORBIT-CLOSURE"
problem: "20.50"
scope_id: 20.50/four-involution-universal-group
assignment_revision: 1
supersedes: ["none"]
refs:
  - Agents/Kourovka/problems/20.50/ideas/2026-08-16-qorbit-closure-pivot.md
  - Agents/Kourovka/problems/20.50/verification/2026-08-16T164228Z-final-hand-partials.md
needs_reply_by: none
status: done
author: operator
tags: [agent/math-expert, user/operator, domain/group-theory, topic/kourovka, topic/conjugation-quandles, project/kourovka, status/conjectured]
---

## Ask
Use the linked assessment to decide whether to assign the single 63-minute `QORBIT-CLOSURE` pivot.

## Context
SCOPE: `20.50/four-involution-universal-group`; REVISION: 1. Fidelity is a universal structural partial only: the rank-three lemma is auxiliary, the action descent is nonuniform, and the finite derived-truncation bounds do not bound the target. `witness_equals_target:false`; `active_assignment_answered:no`; novelty was not searched under the blind boundary.

The one proposed representation change is to test whether the finite \(H=\langle a,b,c\rangle\)-orbit \(d^H\) is closed under conjugation by \(d\). A uniform pass makes every marked-generator conjugacy class finite and, via the linked centralizer/Schur reduction, proves \(G_4\) finite. The note gives the exact defect set, success/failure certificates, minute allocation totaling 63, and hard kills at minutes 44, 54, and 63.

## Evidence
Only the three artifacts in the request were used. All ten unleased delegated GAP probes and every dependent inference were excluded; no web, history, computation, or delegate was used.

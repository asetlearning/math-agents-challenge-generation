---
from: Lead
to: Validator
type: REQUEST
topic: Reproduce SG255 and reconstruct the complete 20.49 structural package
problem: 20.49
scope_id: 20.49/two-generated-same-exponent
assignment_revision: 1
supersedes: [none]
refs:
  - Agents/Kourovka/problems/20.49/runs/2026-08-17-r1-nonsoluble-pair-orbits/partial-result-sg255.md
  - Agents/Kourovka/problems/20.49/runs/2026-08-17-r1-nonsoluble-pair-orbits/monolithic-socle-gate.md
  - Agents/Kourovka/problems/20.49/runs/2026-08-17-r1-nonsoluble-pair-orbits/three-pair-defect-hypergraph.md
  - Agents/Kourovka/problems/20.49/runs/2026-08-17-r1-nonsoluble-pair-orbits/three-prime-abelian-chief-norm.md
needs_reply_by: none
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/exponent, project/kourovka, status/conjectured]
---

## Ask

Independently audit:

1. exact SG255 coverage, every persisted nonsoluble witness row, and zero candidates;
2. the least-counterexample reductions (nonsoluble, directly indecomposable,
   exactly three-generated, exponent drop in proper subgroups/quotients);
3. the order-30 obstruction to monolithicity;
4. the at-least-three-prime and exactly-three distinct-defect claims, plus the
   Nielsen non-invariance control;
5. the abelian-chief quotient exponent drop, norm, full-Jordan-block claim, and the
   presented exponent-900 split no-partner pattern.

Separate valid partial reductions from strategy controls, identify every gap, and
keep `active_assignment_answered:no` unless the universal target is actually closed.

## Context

No new computation is authorized. You may run a small independent exact checker
only if it is non-heavy under protocol; every GAP call still requires a Lead lease,
so otherwise reconstruct by hand and validate the frozen output consequences.

## Evidence

Use the four linked self-contained notes plus the canonical scope. Do not infer a
universal theorem from the order-255 layer or mistake a soluble control for a
counterexample.

---
from: Lead
to: Problem-21.137
type: DECISION
topic: Test the first nonabelian truncated-substitution edge
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes:
  - 2026-08-17T153924Z__Lead__DECISION__nott3-n2-n14-cubeset.md
refs:
  - Agents/Kourovka/problems/21.137/scratch/nott-n2-n14/hand-obstruction.md
  - Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
needs_reply_by: none
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/draft]
---

## Decision

Use exactly the 27 active minutes remaining on `NOTT3-N2-N15-EDGE`. Fix `p=3`
and the full carrier `t+a_3t^3+...+a_14t^14 mod t^15` under composition. This is
the first truncation where the depth-6/depth-7 cube bracket can survive.

By +5 minutes, derive the exact cube projection to degrees 7 and 8 and its induced
degree-14 commutator form. If the projected image is isotropic, stop without
computation. Otherwise freeze one optimized complete `3^12` carrier enumerator,
with exact exponent-9, literal cube-image, subgroup-closure, and nonabelianity
gates, and request one Lead lease. Absolute stop +27. No N16, parameter sweep,
web/history, hidden/wreath input, p=2, exponent-8, or generated-subgroup proxy.

---
from: Lead
to: Problem-21.137
type: DECISION
topic: Execute the final K32 nonsplit root-saturation route
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: [none]
refs:
  - Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
  - Agents/Kourovka/problems/21.137/ideas/2026-08-17-k32-nonsplit-root-saturation.md
  - Agents/Kourovka/problems/21.137/verification/2026-08-16T181302Z-minimal-central-obstruction.md
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r18-pf-holomorph-cube/findings.md
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r19-pf-holomorph-transvection/findings.md
needs_reply_by: none
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/conjectured]
---

## Decision

Use exactly the final 55 active minutes on `K32-NONSPLIT-ROOT-SATURATION` in
the counterexample direction. Enforce the linked frozen starting data and gates.

The only success is a reconstructible finite 3-group of exponent exactly 9 whose
complete actual cube-value set itself equals a nonabelian subgroup. Generated
cube-subgroup equality, a missing label in `P/<c>`, a nonclosed set, or commuting
cubes is failure. The central root `z^3=c` can fill only the `<c>` fibres; prove
the quotient-label set before using it.

Stop at +10/+24/+42/+50 on the stated gate failures and absolutely at +55. Do not
open a second cocycle ansatz, change representatives, add PF generators, compute
without a frozen Lead lease, or use web/history, p=2, exponent-8, wreath-shaped,
or hidden material. Return to Lead rather than self-parking.

---
from: Lead
to: Problem-21.137-Counterexample
type: CORRECTION
topic: Cyclic quotient already excluded; use noncyclic union-of-coset saturation
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes:
  - r22 strategy-portfolio item selecting a cyclic C3 quotient
refs:
  - Agents/Kourovka/problems/21.137/runs/2026-08-16-r2-odd-proof/findings.md
  - Agents/Kourovka/problems/21.137/verification/2026-08-17T164459Z-grad-pimage-jordan-reduction.md
needs_reply_by: 2026-08-17T19:36:18Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/conjectured]
---

Stop the cyclic-quotient carrier immediately. The reviewed cyclic-root-coset
theorem already forces all power values to commute when every root coset lies in
one cyclic subgroup of `G/P`; therefore `G/P=C3` cannot yield the required
nonabelian literal image.

The saturation equation is also a union condition:

`P = union_{v in G/P} Image(N_v)`.

Do not replace it by the stronger and unsupported demand that every individual
coset norm be surjective. Pivot within the same increment to the smallest quotient
with at least two independent directions, or the first stronger unresolved
reviewed quotient type. Keep the full action, factor set, cross-coset products,
exact exponent 9, and literal-image closure. Record charged time and do not park.

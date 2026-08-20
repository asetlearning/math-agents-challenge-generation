---
from: Lead
to: Problem-20.21
type: DECISION
topic: Continue equivariant kernel-pair route; slot 2 granted through the order-64 kill criterion
problem: "20.21"
scope_id: 20.21/two-index-twelve-kernels
assignment_revision: 1
supersedes: ["none"]
refs: ["Agents/Kourovka/problems/20.21/runs/2026-08-16-r1-proof/scratch/search-equivariant-p.g", "Agents/Kourovka/roster/Problem-20.21.md"]
needs_reply_by: 2026-08-16T13:08:10Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/compute-lease, project/kourovka, status/draft]
---

## Ask

Run the exact requested 1200-second-capped GAP command once, stop at order 64, then
report/release slot 2 and apply the recorded pivot criterion.

## Context

The sufficient semidirect-product reduction is accepted as a strategy-level lemma,
not as a witness. If the bounded scan is negative or automorphism groups dominate,
pivot to the class-two presentation/cocycle route; do not extend to order 128.

## Evidence

Lead inspected the script: it enumerates exactly 2+14+267 groups, filters index-four
normal kernels and their quotient types before automorphism construction, verifies
kernel isomorphism, and tests the induced quotient actions of an order-three
automorphism.

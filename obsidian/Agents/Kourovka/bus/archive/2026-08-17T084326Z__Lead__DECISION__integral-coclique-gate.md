---
from: Lead
to: Problem-21.90
type: DECISION
topic: CONTINUE with a constituent-independent integral coclique gate
problem: 21.90
scope_id: 21.90/diameter-three-distance-graphs
assignment_revision: 3
supersedes: [none]
refs: ["Agents/Kourovka/problems/21.90/runs/2026-08-17-r4-asymmetric-fission/findings.md", "Agents/Kourovka/problems/21.90/runs/2026-08-17-r4-asymmetric-fission/constraints.md"]
needs_reply_by: 2026-08-17T09:18:15Z
status: done
---

## Ask
Use the remaining 38 active minutes to test constituent-independent integral, p-rank, Smith-form, and quasi-symmetric-design obstructions for the forced symmetric 300-block maximum-coclique incidence matrix.

## Context
Preserve the fixed-polar exclusion as a bounded candidate partial result awaiting Validator. Now assume only an arbitrary `srg(300,65,10,15)` distance-3 constituent and the exact equations already derived for `M=I+A1`. Work from `M^2=25I+10M+5J-5B`, `M(B+10I)=10J`, symmetry, diagonal one, and 0/1 entries. Check reductions modulo relevant primes, rank/Smith constraints, and the resulting quasi-symmetric block design. A contradiction must be independent of the isomorphism type of B. If all elementary gates are compatible, state that exact limitation and return `awaiting_lead`; do not assume the polar constituent is unique or start an unbounded SRG search.

## Evidence
Twenty-two active minutes were used, so 38 of the current 60-minute allocation remain. No heavy compute lease is granted.

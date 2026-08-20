---
from: Lead
to: Problem-21.90
type: DECISION
topic: Constituent-independent Delsarte and integral gate
problem: 21.90
scope_id: 21.90/diameter-three-distance-graphs
assignment_revision: 3
status: unread
refs:
  - Agents/Kourovka/problems/21.90/runs/2026-08-17-r4-asymmetric-fission/srg210-constituent-gate.md
---

The explicit-constituent route is stopped correctly: no graph or incidence
matrix may be inferred from a putative design. This is not a user blocker and
does not settle the candidate array.

The gate used 15 active minutes. Cumulative active time is 144 minutes, leaving
36 in the initial cycle. Continue on `SRG210-DELSARTE-INTEGRAL-GATE`, without
assuming an explicit constituent. Use only the necessary identities
`D=I+B`, `D^2=49I+28J`, `M(B+8I)=8J`, and
`M^2=6I+13M+J-B`, with symmetric zero-one `M`, diagonal one and row sum 20.
Derive and check the two possible rational spectral-multiplicity branches first.
Then seek a constituent-independent contradiction via modular ranks, Smith
constraints, or the associated quasi-symmetric incidence design. Every claimed
exclusion must cover every hypothetical `srg(210,76,26,28)`. If the elementary
gates remain compatible, freeze the exact residual matrix problem and report
method exhaustion; do not launch an unbounded catalogue, SAT, or graph search.

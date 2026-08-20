---
from: Lead
to: Problem-21.137
type: DECISION
topic: First possible TRI3 seed layer and cyclic-centre quotient filter
problem: 21.137
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
status: done
refs:
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/findings.md
  - Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/scratch/tri3_order2187.g
---

Accept the exact bounded exhaustion: the official SmallGrp 1.6.0 layer contains
9310 groups of order 2187; all were screened, 8302 have exact exponent 9, and
none has a noncommuting pair in its complete actual cube-value set. This is not
the unrestricted answer and is not evidence from `p=2`. Do not rerun it.

Charge two active minutes. Cumulative time is 305 minutes, leaving 46 in the
current human-priority increment. Continue counterexample work on
`TRI3-ORDER6561-CYCLIC-CENTRE-LIFT`.

Begin with a convention-explicit proof of this quotient filter. If `A` is an
exponent-9 group of order `3^8` and two actual cubes have nontrivial commutator
`c`, then for each `N<=Z(A)` of order 3 their images in `A/N` must commute by the
complete order-2187 result (the exponent-3 quotient case is automatic). Hence
`c` lies in every such `N`; deduce precisely that `Z(A)` has a unique order-3
subgroup and is cyclic. Check every inference, including whether `c` has order 3
and centrality, rather than assuming them.

Then impose the TRI3 seed conditions: an eligible central `C` lies in the actual
cube set, projected cube image is a subgroup, every occupied `C`-fibre has size
2 or 3, at least one has size 2, and actual cubes do not commute. Either derive a
contradiction from the cyclic-centre structure or freeze a complete finite
power-commutator/central-extension parameterization of the surviving order-6561
seed class. Do not launch unbounded descendant generation. A computation needs
an exact coverage statement, frozen script, resource estimate, and Lead lease.
If this route exhausts, report the precise residual family and await Lead or
MathExpert; do not stop the whole problem or direction.

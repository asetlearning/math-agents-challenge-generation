---
from: Lead
to: Problem-21.137
type: REQUEST
topic: "CPTR-PAIR-TRANSGRESSION: bounded proof audit for one commuting pair"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: ["none"]
refs:
  - Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
  - Agents/Kourovka/problems/21.137/verification/2026-08-16T181302Z-minimal-central-obstruction.md
  - Agents/Kourovka/problems/21.137/verification/2026-08-17T053718Z-mco-affine-norm-cover.md
  - Agents/Kourovka/problems/21.137/ideas/2026-08-17-portfolio-reset-park.md
needs_reply_by: 2026-08-17T08:04:14Z
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, project/kourovka, status/conjectured]
---

## Assignment

Work only on the exact revision-2 odd-prime clause. For arbitrary odd prime `p`,
use the reviewed minimum-counterexample coordinates and equations `(C1)--(C5)`.
Freeze a commuting pair `h,j in H` of order `p` and audit whether the central
associativity obstruction has a canonical mixed cyclic evaluation coupling their
`p`-power/carry data to `beta`.

Begin with the standard mod-`p` bar-resolution cross-product candidate

`Z(h,j)=sum_(i=1)^(p-1)([j|h^i|h]-[h^i|j|h]+[h^i|h|j])`.

Do not assume this displayed sign/order is correct: compute its boundary first.
If necessary, replace it by the exact Eilenberg--Zilber shuffle representing the
cross product of `[j]` with the cyclic norm 2-cycle for `h`, and record the full
corrected chain rather than citing it abstractly.

Then:

1. Derive the complete transformation of `c_h,d_h,r,s` under arbitrary normalized
   section changes `x_t -> x_t k_t`. Test whether the proposed mixed evaluation is
   genuinely section-independent before interpreting it.
2. Evaluate the exact `(C4)` scalar obstruction on the verified cycle and use the
   ordered `(C5)` formulas for `h` and `j`. Keep every `ell`, action, and
   `1/2 beta` term; do not silently pass to coinvariants where `beta` may not
   descend.
3. If a section-independent identity survives, state precisely what it proves for
   a commuting pair and give a separate argument—or an explicit gap—between that
   statement and `beta=0` under actual-value-set coverage.

## Exact certificates and kill rule

- **Positive certificate:** a line-by-line arbitrary-odd-`p` chain calculation,
  exact section-invariance proof, and a logically separate reach statement. A
  commuting-pair lemma alone is a `PARTIAL_RESULT`, not a solution.
- **Negative certificate:** an exact section-change formula showing that the
  candidate evaluation is not invariant, or explicit normalized finite data
  satisfying every restricted `(C1)--(C5)` row while the proposed identity fails.
- **Hard kill:** spend at most 10 active minutes on the boundary and invariance
  gate, at most 25 more on the evaluation, and reserve 10 minutes for a
  self-contained report. Stop immediately on an exact invariance defect. If no
  checkable identity or defect exists by cumulative minute 290, package
  `STRATEGY_EXHAUSTED`; do not convert unsuccessful manipulation into a claim.

The shared ledger starts at cumulative active minute `255` and may not exceed
`300`. No computation, web/history, wreath-shaped material, `p=2`, exponent-8
clause, generated-verbal-subgroup substitution, or return to a stopped family.
Record UTC start/stop and cumulative active minutes in the new run log. Send all
research output through the file bus.

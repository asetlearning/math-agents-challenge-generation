---
from: Lead
to: Problem-21.137-Counterexample
type: DECISION
topic: Test one complete nonabelian-quotient extension over the reviewed rank-four kernel
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: [none]
refs:
  - Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
  - Agents/Kourovka/problems/21.137/verification/2026-08-17T194155Z-rank4-kernel-hand-exclusion.md
needs_reply_by: none
status: done
author: operator
tags: [agent/lead, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, project/kourovka, status/draft]
---

## Exact scope lock

Work only on the odd-prime clause: `p>2`, finite same-`p` group, exponent
**exactly** `p^2`, the **literal complete set** `{g^p:g in G}` itself a subgroup,
and whether that subgroup is abelian. Every `p=2`/exponent-8 example, generated
power subgroup, formal local action cover, or incomplete coset sample is excluded.

## Strategy: `RANK4-HEISENBERG-QUOTIENT-SEMIDIR`

The reviewed theorem excludes every elementary-quotient extension of
`K=3_+^(1+4) x C3^2`. Test the first missing quotient type instead of changing
the kernel: freeze `p=3`, `Q=H_3(3)` of exponent three, and one canonical explicit
split extension `G=K semidirect Q` in which the induced `Q`-action on the
four-dimensional symplectic quotient is genuinely nonabelian. Prefer the
canonical pair of root-unipotent symplectic transformations and derive their
commutator; do not assume such a homomorphism exists. If it cannot lift to
`Aut(K)`, the exact lift obstruction is the early result.

For a successful action, give a complete coordinate multiplication/inverse law
for the order-`3^10` group and evaluate the cube of every one of its 59,049
elements, symbolically or by one frozen bounded computation. Check separately:

1. the action relations and exact group order;
2. exponent exactly nine, not merely dividing nine;
3. the cardinality and membership representation of the literal full cube image;
4. subgroup equality by comparing that image with the subgroup it generates
   (never substituting the latter for the former);
5. if closed, whether two explicit actual cubes fail to commute.

A counterexample claim requires all five certificates. Closure failure or
commuting cubes is an exact out-of-scope/family-exclusion result only. Do not
enumerate alternative actions, cocycles, descendants, or catalogues in this
increment.

## Time and compute gates

Start at cumulative active minute 556 and use at most 60 further active minutes.
By minute 12 either freeze the exact action/lift or stop with its obstruction; by
minute 30 freeze the complete group/cube algorithm; stop new mathematics at
minute 52 and package by minute 60. Any computation at or above the protocol's
heavy threshold requires a frozen manifest and Lead lease. Strategy exhaustion
returns unused minutes; it never parks the human-mandated window through minute
765.

---
title: "PCOVER-QUOTIENT-INHERITANCE run log"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
active_assignment_answered: no
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/draft]
---

## 2026-08-18T00:39:46Z — start, cumulative 737

Accepted the final 28-minute `PCOVER-QUOTIENT-INHERITANCE` allocation.  Scope is
only `p=3`, exact exponent nine, complete literal cube set itself a subgroup;
the desired counterexample would require that set to be nonabelian.

## 2026-08-18T00:42:15Z — exact quotient reduction

For a hypothetical minimum order-`3^9` counterexample, derived that the reviewed
monolith `N=Pow_3(H)'` is the last nontrivial lower-exponent-three term.  Hence
`H/N` is the exact p-parent, and its literal cube set is the nontrivial abelian
subgroup `Pow_3(H)/N`.  Froze the complete recursive p-cover enumeration method,
including all allowable step sizes.

## 2026-08-18T00:43:17Z — mandatory tool/count gate fails

Read-only probes:

```text
command -v gap
/usr/bin/gap

command -v pq pga anupq gap3
<no output>

filesystem search for ANUPQ or pq under available GAP roots
<no output>
```

No p-cover engine is available.  Therefore multiplicator/nucleus data and the
required numerical descendant-orbit bound cannot be obtained.  No mathematical
computation was run, no manifest was submitted for a lease, and no general-purpose
tool was reimplemented.

## 2026-08-18T00:44:48Z — stop, cumulative 742

Outcome: `STRATEGY_EXHAUSTED` by the explicit missing-tool and missing-count
hard kills.  Charged 5 active minutes and returned 23 unused minutes to Lead.
`active_assignment_answered: no`.

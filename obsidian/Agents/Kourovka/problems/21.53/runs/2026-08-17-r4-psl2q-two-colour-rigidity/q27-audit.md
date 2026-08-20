---
title: "Finite stress test — q=27 orthogonality graph"
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
outcome: FINITE_AUDIT
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/graph-automorphisms, project/kourovka, status/draft]
---

# `q=27` finite stress test

Lead leased one invocation of the frozen manifest because `q=27` is the first
simple odd field in the subfamily `q=3^f`, `f` odd, where the hand calculation
shows that the order-3 edge relation is empty.

The exact authorized command was

`timeout 120s gap -q Agents/Kourovka/problems/21.53/runs/2026-08-17-r4-psl2q-two-colour-rigidity/scratch/q27_orthogonality_audit.g`.

It exited zero after 3.186 seconds under GAP 4.12.1 and GRAPE 4.9.0. The complete
output was:

```text
Q27_ORTHOGONALITY_AUDIT_OK
GAP_VERSION=4.12.1
GRAPE_VERSION=4.9.0
GROUP_ORDER=9828
INVOLUTION_CLASS_COUNT=1
VERTEX_COUNT=351
VALENCY=14
AUT2_ORDER=58968
EXPECTED_PGAMMAL2_ORDER=58968
```

The output SHA-256 is
`1a72c8261cab058a0f4b04a59f7d123a372712601b1692b5406bb0b85d6bd130`.

## Meaning and limitation

The graph is the exact commuting graph on the complete involution class of the
GAP object `PSL(2,27)`. Its full graph automorphism group has the same order as
`PGammaL(2,27)`. This is consistent with the odd orthogonal-shell rigidity lemma
precisely where `Aut_3=S_D` vacuously.

It is one finite stress test, not evidence for every odd `q`, not an independent
proof that the GAP object and every source relation were reconstructed from first
principles, and not a substitute for the missing incidence/orthogonal rigidity
argument. No catalogue continuation or rerun is authorized.

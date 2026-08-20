---
title: "RANK4-NONSPLIT-H3 — feasible automorphism-lift gate"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
outcome: CHECKPOINT
active_assignment_answered: no
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, project/kourovka, status/conjectured]
---

# Feasible first gate

The one frozen nonorthogonal label row is feasible at the complete
automorphism-lift level. This is not yet a factor system, extension, group, or
counterexample.

## Exact coordinates

Use columns in `V=<e1,e2,f1,f2>` and center basis `(c,s,t)`. The reviewed
outer matrices `A,B,C` are frozen in `scratch/lift_manifest.md`. Choose

```
qX=f2=(0,0,0,1)^T,       qY=e2=(0,1,0,0)^T.
```

Directly, `AqX=qX`, `BqY=qY`, and
`omega(qX,qY)=-1=2`, so `[qX,qY]` is nontrivial in `K`.

The following center representation of `H_3(3)` fixes `c`:

```
TX = [1 2 0]   TY = [1 1 0]   TZ = [1 0 1]
     [0 1 1]        [0 1 1]        [0 1 0]
     [0 0 1]        [0 0 1]        [0 0 1]
```

It satisfies `TZ=TX^-1 TY^-1 TX TY`, all three cubes are the identity,
and `TX,TZ` and `TY,TZ` commute.

For `alphaX=(A,TX,LX)`, `alphaY=(B,TY,LY)`, and
`alphaZ=(C,TZ,LZ)`, one exact shear solution is

```
LX = [0 0 0 0]   LY = [0 0 0 0]   LZ = [0 0 0 0]
     [1 1 0 0]        [1 0 0 0]        [0 2 0 1]
     [0 0 0 0]        [0 0 0 0]        [0 0 0 0].
```

## Complete linear-system certificate

Using

`(M,T,L)o(M',T',L')=(MM',TT',T L'+L M')`

and `[u,v]=u^-1 v^-1 u v`, the 56 equations in the manifest have 36
variables and exact ranks

```
rank(coefficient)=17,  rank(augmented)=17,
solution-space dimension=19.
```

For the displayed solution, the six relator shears have zero `s,t` rows and
the following `c` rows / inner labels:

| relator word | `c` row | inner label `q` |
|---|---|---|
| `x^3` | `0200` | `(0,0,0,1)=qX` |
| `y^3` | `0001` | `(0,1,0,0)=qY` |
| `z^3` | `0000` | `0` |
| `[x,y]z^-1` | `1220` | `(2,0,2,1)` |
| `[x,z]` | `0102` | `(0,2,0,2)` |
| `[y,z]` | `0201` | `(0,1,0,1)` |

All 56 exact residuals are zero. Reproduction:

```text
$ /usr/bin/time -f 'elapsed=%e sec maxrss=%M KB' python3 Agents/Kourovka/problems/21.137/runs/2026-08-17-r25-rank4-nonsplit-h3/scratch/check_lift_gate.py --frozen-only
frozen feasible center row
TX 120011001
TY 110011001
TZ 101010001
system equations/variables/rank/augmented-rank: 56 36 17 17
solution-space dimension: 19
LX 000011000000
LY 000010000000
LZ 000002010000
x3 J-row 0200 q (0, 0, 0, 1)
y3 J-row 0001 q (0, 1, 0, 0)
z3 J-row 0000 q (0, 0, 0, 0)
comm_xy_zinv J-row 1220 q (2, 0, 2, 1)
comm_xz J-row 0102 q (0, 2, 0, 2)
comm_yz J-row 0201 q (0, 1, 0, 1)
all 56 residuals: [0]
elapsed=0.18 sec maxrss=12032 KB
```

## Limits

This only proves feasibility of one outer-action lift. The inner labels shown
above do not yet choose central representatives or satisfy the factor-system
associativity/collection equations. No finite group has yet been constructed,
and none of the exponent, literal cube-set closure, or nonabelian-image target
gates has been tested. `active_assignment_answered: no`.


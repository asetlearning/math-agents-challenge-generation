---
title: "Frozen manifest — rank-four nonsplit H3 automorphism-lift gate"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, project/kourovka, status/draft]
---

# Exact finite manifest

This manifest freezes one and only one nonorthogonal label row. It searches no
factor systems and constructs no extension group.

## Kernel and outer action

All arithmetic is over `F3`. Use column coordinates on
`V=<e1,e2,f1,f2>` and

`omega(v,w)=v_e1 w_f1+v_e2 w_f2-v_f1 w_e1-v_f2 w_e2`.

The reviewed outer matrices are

```
A = [1 1 0 0]    B = [1 0 0 1]    C = [1 0 2 0]
    [0 1 0 0]        [0 1 1 0]        [0 1 0 0]
    [0 0 1 0]        [0 0 1 0]        [0 0 1 0]
    [0 0 2 1]        [0 0 0 1]        [0 0 0 1]
```

They satisfy `C=A^-1 B^-1 A B`, `A^3=B^3=C^3=I`, and
`[A,C]=[B,C]=I` for `[u,v]=u^-1 v^-1 u v`.

Freeze

```
qX=f2=(0,0,0,1)^T in ker(A-I),
qY=e2=(0,1,0,0)^T in ker(B-I).
```

Then `omega(qX,qY)=-1=2`, so the corresponding kernel elements do not
commute. This is the only label pair admitted by the run.

## Complete center-action domain

Use the ordered center basis `(c,s,t)`, where `c` spans `K'`. An
automorphism triple is `(M,T,L)` with `T(c)=c` and `L:V->Z` linear.
Enumerate every `T=I+R` with `R(c)=0` and `R^3=0`; this is exactly every
order-dividing-three center action fixing `c`.

Enumerate every ordered pair `(TX,TY)` in that finite domain. Define
`TZ=[TX,TY]`. Retain exactly those pairs satisfying

```
TX^3=TY^3=TZ^3=I,
[TX,TZ]=[TY,TZ]=I.
```

Thus retained triples are exactly the center representations of the frozen
Heisenberg presentation
`<x,y,z | x^3,y^3,z^3,[x,y]z^-1,[x,z],[y,z]>`.

## Complete linear shear system

For each retained center triple, solve for all 36 entries of
`LX,LY,LZ in Mat_(3x4)(F3)`. Triple composition is

`(M,T,L)o(M',T',L')=(MM',TT',T L' + L M')`.

An inner automorphism is exactly `(I,I,J_q)`, with only the `c` row nonzero
and `J_q(v)=omega(q,v)c`. Impose all rows:

1. `alphaX^3=(I,I,J_qX)` (all 12 shear coordinates);
2. `alphaY^3=(I,I,J_qY)` (all 12 shear coordinates);
3. `alphaZ^3` is inner (the eight `s,t` coordinates vanish);
4. `[alphaX,alphaY] alphaZ^-1` is inner (eight `s,t` rows);
5. `[alphaX,alphaZ]` is inner (eight `s,t` rows);
6. `[alphaY,alphaZ]` is inner (eight `s,t` rows).

The fixed-label invariance rows `(A-I)qX=0` and `(B-I)qY=0` are checked
separately and exactly. The six relators above are the complete first-gate
automorphism compatibility system for the frozen quotient presentation. Any
kernel representatives of the four unspecified inner relators belong to the
factor-system gate and are forbidden unless this linear system is feasible.

## Certificate contract

For every retained center triple, compute exact coefficient rank and augmented
rank over `F3`. Feasibility requires equality. If no triple is feasible, report
the complete `(rank,augmented-rank)` distribution, deterministic enumeration
counts, and a concrete left-null row certificate for each distinct system class
needed to make the inconsistency independently checkable. Do not infer anything
about another label pair or the universal source scope.


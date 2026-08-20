---
title: "Partial result — the nonsquare-shell Gram factorization is not canonical"
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
outcome: PARTIAL_RESULT
active_assignment_answered: no
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/finite-geometry, project/kourovka, status/replicated]
---

# Exact obstruction to the assigned polarity-completion route

For the internal-point shell of the conic in `PG(2,7)`, the matrix

`K=7I+J-A^2`

does **not** have a unique binary factorization into 28 columns of weight three,
even up to column permutation.  In particular, the geometric columns indexed by
exterior points/secant lines cannot be recovered canonically from the displayed
Gram identity and the prescribed column weights alone.

This is a bounded partial result about the assigned reconstruction lemma.  It is
not an automorphism of the order-2 graph, not a counterexample to the desired
equality for `PSL(2,7)`, and not a conclusion about all `q=3 mod 4`.

## Hand certificate

Use

`Q(X,Y,Z)=Y^2-XZ`

over `F_7`, whose nonzero nonsquares are `3,5,6`.  Let

```
P=(1,0,1)   A=(3,1,1)   B=(5,2,1)
C=(2,0,1)   D=(4,0,1)   R=(6,4,1).
```

Their `Q`-values are `6,5,6,5,3,3`, so all six points are internal.  The four
lines

```
l_1: X=2Y+Z,       l_2: Y=0,
l_3: X=Y+2Z,       l_4: X=4Y+4Z
```

meet the conic `Y^2=XZ` at parameter pairs

`{4,5}, {0,infinity}, {2,6}, {1,3}`,

respectively.  Thus they are secants, and these pairs partition the eight conic
points.  A secant over `F_7` has exactly three internal points.  Direct
substitution gives the complete internal sections

```
S_1=PAB,  S_2=PCD,  S_3=ACR,  S_4=BDR.
```

The six displayed points are the six pairwise intersections of the four lines.
Consequently each pair in each of the four noncollinear triples

```
T_1=PAC,  T_2=PBD,  T_3=ABR,  T_4=CDR
```

lies together on one of `l_1,...,l_4`.  Equivalently, every such pair has zero
order-2 codegree, exactly as a pair inside a candidate column support must.

For a set `U`, write `v_U` for its `0`--`1` indicator column.  Then

```
v_S1 v_S1^T + v_S2 v_S2^T + v_S3 v_S3^T + v_S4 v_S4^T
 =
v_T1 v_T1^T + v_T2 v_T2^T + v_T3 v_T3^T + v_T4 v_T4^T.       (*)
```

To check `(*)`, label the four lines by `1,2,3,4` and their six intersection
points by `p_ij`.  The `S_i` are the four three-edge stars in `K_4`, while the
`T_i` are its four triangular faces.  On each side every `p_ij` occurs twice,
and the same twelve unordered pairs occur once.  Hence the diagonal and
off-diagonal entries agree individually.

Let `X` be the geometric `21 x 28` incidence matrix.  Replace only the columns
`v_S1,...,v_S4` by `v_T1,...,v_T4`, leaving the other 24 columns fixed.  The
result `X'` is binary, still has 28 columns all of weight three, and satisfies

`X'X'^T=XX^T=7I+J-A^2`

by `(*)`.  None of the `T_i` is collinear, so none is a geometric secant
section.  Therefore `X'` is not obtained from `X` by permuting columns.

## The resolution stage

The assigned first-stage uniqueness lemma is false, so the geometric block
system is not yet an intrinsic object on which a uniqueness theorem for
`q`-block resolutions can automatically operate.  A once-only leased exact-cover
audit was subsequently run on the displayed original and Pasch-traded systems.
It found exactly eight seven-block resolutions in the geometric system and none
in the traded system.  Thus the resolution pattern rejects this particular
competing factorization; the Pasch trade does not refute a stronger global
criterion that jointly selects a factorization and its resolutions.

The exact observed stdout was:

```
points=57 conic=8 internal=21
geometric_columns=28 traded_columns=28
gram_equal=True
original_resolutions=8
traded_resolutions=0
```

The frozen checker and complete stdout are `scratch/q7_pasch_audit.py` and
`scratch/q7_pasch_audit.stdout.txt`.  Its SHA-256 matched the leased value
`87abf88b48cd189708b19d61442c1deaa6ee60cd1b4e0fb31b218582297ed33f`.
This computation covers only the two displayed `q=7` column systems.  No theorem
that every competing factorization lacks the required resolutions has been
proved here.

## The empty-order-three subfamily

Let `q=3^f` with `f` odd and `q>=7`; hence in the simple-group range actually
`f>=3`, `q>=27`, and `chi(-1)=-1`.  The reviewed trace/order dictionary says
that exact order three would require `u=1=4`.  For two distinct points of this
internal shell, the degenerate value `u=4` does not occur: it occurs precisely
in the `chi(-1)=1` exterior-shell branch.  Therefore `R_3` is empty.

Under the source's exact one-way convention, this gives

`Aut_3(Gamma)=S_D`

vacuously.  Since `3` is the second-smallest distinct prime divisor of
`|PSL(2,q)|`, the desired two-colour group is exactly `Aut_2(Gamma)` in this
subfamily.  Thus there is no retained colour besides `R_2` with which to choose
among candidate completions.  The Pasch trade is a `q=7` obstruction and is not
claimed to persist at `q=3^f`; the exact remaining requirement is a new
field-uniform intrinsic characterization of the geometric factorization (and
then of its conic-point resolutions) from `A`, stronger than Gram equality plus
binary constant-weight data.

## Scope matrix

| constraint_id | result in this run |
|---|---|
| `21.53-forall-L-D` | not universal; only a reconstruction obstruction in the odd `PSL(2,q)` branch |
| `21.53-L-finite-nonabelian-simple` | `PSL(2,7)` is in the source class; no equality or counterexample is asserted for it |
| `21.53-D-single-involution-class` | the reviewed internal shell is the unique involution class for odd `PSL(2,q)` |
| `21.53-Gamma-product-order-colouring` | `A` is only the exact order-2 relation; no full-colour conclusion is made |
| `21.53-Aut-t-definition` | the empty-label convention is used explicitly for characteristic three |
| `21.53-two-minimal-primes` | `p=3` for every `PSL(2,q)` considered here |
| `21.53-full-colour-group-definition` | not reconstructed in this run |
| `21.53-two-colours-determine-all` | not established or refuted |

`active_assignment_answered: no`.

## What this does not establish

- It does not produce a permutation in `Aut_2` outside the full colour group.
- It does not decide the fixed pair `PSL(2,7)`.
- It does not decide any `q=3^f`, `f` odd, empty-`R_3` case.
- It does not rule out a stronger canonical completion that uses information in
  `A` beyond `7I+J-A^2` and column weights; indeed the resolution audit filters
  the one explicit traded factorization.
- It does not cover any finite simple group outside the odd `PSL(2,q)` family or
  Problem 21.52.

Verified by [[Agents/Kourovka/problems/21.53/verification/2026-08-17T233908Z-q7-pasch-resolution-obstruction]].

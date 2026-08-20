---
title: "Partial result — odd PSL(2,q), square-minus-one branch"
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
outcome: PARTIAL_RESULT
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/finite-geometry, project/kourovka, status/conjectured]
---

# Odd orthogonal shell when `chi(-1)=1`

## Exact bounded claim

Let `q>=9` be an odd prime power with `q=1 mod 4`, let
`L=PSL(2,q)`, and let `D` be its unique involution class.  In the reviewed
orthogonal model

`D={ [x] in P(sl_2(q)) : chi(Q(x))=chi(-1)=1 }`,

the following hand reconstruction gives

`Aut(D;R_2,R_3)=PGammaO(3,q)`.

Together with the reviewed trace-to-order dictionary, this would give
`Aut(Gamma)=Aut_2(Gamma) intersect Aut_3(Gamma)` for this bounded family.  The
claim is `status/conjectured` pending independent validation.  It does not cover
`q=3 mod 4`, any simple group outside `PSL(2,q)`, or the universal source scope.

## 1. Two intersection numbers

Let `epsilon=chi(-1)` and, for distinct `x,y in D`, put

`u=B(x,y)^2/(Q(x)Q(y))`.

The Gram determinant of `<x,y>` is
`Delta=Q(x)Q(y)(4-u)`.  If `z=<x,y>^perp`, comparison with the determinant
square class `chi(det B)=chi(-2)` in `sl_2(q)` gives

`chi(Q(z))=epsilon chi(4-u)`.

Therefore

`c_22(x,y):=|N_2(x) intersect N_2(y)|`

is `1` when `chi(4-u)=1` and `0` otherwise.

Assume temporarily that the characteristic is not 3 and `u!=4`.  Scale the
representatives so that `Q(x)=Q(y)=kappa`, and write

`y=a x+y_0`,  `y_0 perpendicular x`,
`A=Q(y_0)=kappa(4-u)/4`.

Choose `w perpendicular y_0` inside `x^perp` and put `C=Q(w)`.  The determinant
of `Q|x^perp` has square class 1, so `chi(A/C)=1`.  A projective point
`z=c y_0+d w` belongs to `N_2(x) intersect N_3(y)` exactly when

`4A^2 c^2=kappa(Ac^2+Cd^2)`,

or

`(d/c)^2=A(3-u)/C`.

There is no solution with `c=0`, and every nonzero solution automatically has
the square class defining `D`.  Hence

`m_23(x,y):=|N_2(x) intersect N_3(y)|=1+chi(3-u)`       (1)

for `u!=4`.

If `u=4`, this case occurs on `D` precisely when `epsilon=1`.  Choose the signs
so that `B(x,y)=2kappa` and write `y=x+r`, where `r` is isotropic and
`r perpendicular x`.  In the split plane `x^perp`, choose an isotropic `s`
with `B(r,s)=1`.  Substitution of `z=alpha r+beta s` into the two relations gives
`beta=kappa alpha`, hence exactly one projective solution.  Thus

`m_23(x,y)=1` when `u=4`.                              (2)

Equations (1)--(2), together with `c_22`, canonically define

`T(x,y) iff x!=y, c_22(x,y)=0, and m_23(x,y)=1`.

Indeed (1) can equal 1 only at `u=3`, where `c_22=1`, while (2) has
`c_22=0`.  Therefore, in characteristic different from 3,

`T(x,y) iff u(x,y)=4`.                                  (3)

In characteristic 3 with `epsilon=1` (equivalently `q=3^f`, `f` even), the
defining equation for `R_3` is already `u=1=4`, so set `T=R_3`.  Thus (3) is
available throughout the claimed family.

## 2. Reconstructing the ambient conic

Let `C` be the isotropic conic of `Q`.  Since `epsilon=1`, the points of `D`
are exactly the exterior points of `C`.  Sending an exterior point to the two
contact points of its tangent lines is a bijection

`D -> { two-element subsets of C }`.

For two exterior points, `u=4` says that their span is degenerate, equivalently
that they lie on a common tangent to `C`.  Under the displayed bijection this
means that their two-element subsets meet.  Hence `(D,T)` is the triangular
graph on the `q+1` points of `C`.

Its cliques are either stars (all pairs containing a fixed conic point) or the
three pairs supported on a three-element set.  Since a star has size `q>3`, its
maximum cliques are canonically exactly the stars.  Every automorphism preserving
`R_2,R_3` therefore induces a unique permutation `pi` of `C`, and on `D` it is

`{a,b} -> {pi(a),pi(b)}`.                                (4)

This recovers the missing isotropic points and tangent lines from the two given
relations alone.

## 3. Orthogonality is harmonicity

Identify `C` with `P^1(F_q)`.  If `x_ab` is the intersection of the tangents at
`a,b`, conic polarity gives `x_ab^perp=<a,b>`, the chord through `a,b`.
Therefore

`x_ab R_2 x_cd`

holds exactly when the intersection of the tangents at `c,d` lies on that chord.
For the parametrization `(t^2,t,1)` of a conic, this incidence is

`2(ab+cd)=(a+b)(c+d)`,

equivalently

`(a,b;c,d)=-1`.                                         (5)

Thus (4) and preservation of `R_2` say that `pi` preserves all harmonic
quadruples.

Here is a self-contained field reconstruction.  Compose `pi` with a unique
element of `PGL(2,q)` so that the resulting map `h` fixes `infinity,0,1`.
Harmonicity of `(infinity,0;c,-c)` gives

`h(-c)=-h(c)`.

Harmonicity of `(infinity,b;c,2b-c)` gives

`h(2b-c)=2h(b)-h(c)`.

Taking midpoints (and using the trivial coincident special cases separately)
now gives

`h(x+y)=h(x)+h(y)`.

For `x` other than `0,1,-1`, the four points in

`(x,-x;1,x^2)`

are distinct and harmonic by (5).  Hence `h(x^2)=h(x)^2`; the omitted values
satisfy the same identity directly.  Polarizing this identity and using odd
characteristic yields

`h(xy)=h(x)h(y)`.

Therefore `h` is a field automorphism and

`pi in PGammaL(2,q)`.                                   (6)

The action of `PGammaL(2,q)` on the conic is exactly the action of
`PGammaO(3,q)` on the ambient projective plane.  Since (4) determines the
original permutation on every vertex, (6) gives the asserted upper bound.
The reverse inclusion preserves both defining equations, so equality follows.

## What this does not establish

- It does not treat `epsilon=-1`, including the genuine empty-`R_3` family
  `q=3^f` with `f` odd.
- It does not turn the reviewed `q=27` finite stress test into a family proof.
- It does not cover all odd `PSL(2,q)`, all finite simple groups, or Problem 21.52.
- Its bounded family claim still requires independent validation.

## Empty-`R_3` obstruction retained for the next route

When `epsilon=-1`, every isotropic tangent polar has empty intersection with
`D`.  The `R_2` graph recovers `D`-polar line sections as neighbourhoods, while
an exterior-pole line contributes `(q-1)/2` vertices whose pairs all have zero
`R_2` codegree.  Completing the plane from `R_2` alone therefore requires a
new classification theorem: identify exactly the concurrency classes (or the
corresponding large pairwise-zero-codegree sets) and rule out non-collinear
competitors.  The elementary intersection numbers above do not do this.

There is a useful exact matrix form of the obstruction.  Let `C,D,E` be the
isotropic, internal and exterior point orbits when `epsilon=-1`, and let `M` be
the full polarity-incidence matrix on `PG(2,q)`, loops included at isotropic
points.  Projective-plane incidence gives

`M^2=qI+J`.

The `D`--`C` block is zero.  If `A=M_DD` is the known `R_2` adjacency matrix and
`X=M_DE`, then the `D`--`D` block of this identity is

`XX^T=qI+J-A^2`.                                         (7)

Every column of `X` is the characteristic vector of

`S_e=D intersect e^perp`, `e in E`,

of weight `(q-1)/2`; every row has weight `(q+1)/2`.  Off the diagonal, the
right side of (7) is 1 precisely for a zero-`R_2`-codegree pair.  Thus every
such pair lies in a unique geometric block `S_e`.

Recovering the exterior points from `A` is exactly the missing canonical
`0`--`1` factorization/clique-decomposition step in (7).  After those blocks are
recovered, an isotropic point `c` would be recovered as the `q` exterior blocks
indexed by `e in c^perp minus {c}`: their supports `S_e` are pairwise disjoint
and partition all of `D`.  Hence the next completion step is the uniqueness of
these geometric resolutions.  A hypothetical exotic automorphism in the
empty-`R_3` branch must first fail to preserve the geometric column supports in
(7), or later exploit a non-geometric resolution.  This is a concrete
counterexample signature, not evidence that such an automorphism exists.

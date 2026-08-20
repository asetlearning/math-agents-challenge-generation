---
title: "Partial result — complete PSL(2,q) trace model and even-characteristic rigidity"
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
outcome: PARTIAL_RESULT
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/graph-automorphisms, project/kourovka, status/conjectured]
---

# Partial result: `PSL(2,q)`

## Exact scope

Let `q>=4` be a prime power and `L=PSL(2,q)`. The note proves the source equality
for every `q=2^f`, `f>=2` (and consequently for the identical `A5` pair arising
from `q=5`). It also gives a complete trace/norm description of every colour for
all odd `q`, reducing that half to one explicit finite-geometry rigidity lemma.
It does **not** prove the lemma and therefore does not claim the whole `PSL(2,q)`
family or the universal source statement.

## 1. The second prime is always 3

Put `d=gcd(2,q-1)`. Then

`|PSL(2,q)| = q(q-1)(q+1)/d`.

This number is even for every `q>=4`. If the characteristic is 3, it is visibly
divisible by 3; otherwise one of `q-1,q+1` is divisible by 3, and division by
`d<=2` does not remove that factor. Hence the two least distinct prime divisors
are exactly `2,3`. Thus the source parameter is `p=3` throughout this family.

## 2. Characteristic two: a complete proof

Let `q=2^f`, `f>=2`, let `V=F_q^2`, and write

`[x,y]=det(x,y)`.

For a nonzero column `x`, set

`N_x = x(x^T J)`,  `J=((0,1),(1,0))`,  and  `u_x=I+N_x`.

Thus, for `x=(r,s)^T`,

`N_x=((rs,r^2),(s^2,rs))`.

We have `N_x^2=0`, so `u_x` is an involution. Frobenius squaring is
bijective on `F_q`; the displayed entries show that `x -> N_x` is injective and
hits every nonzero rank-one nilpotent trace-zero matrix. Consequently

`D={u_x:x in V\{0}}`

is the entire set of `q^2-1` nonidentity involutions. Also
`A u_x A^-1=u_{Ax}` for `A in SL(2,q)`, because `A^T J A=J`; transitivity of
`SL(2,q)` on `V\{0}` proves that `D` is one complete conjugacy class. The centre
is trivial, so this is directly a model in `PSL(2,q)=SL(2,q)`.

For distinct nonzero `x,y`, direct multiplication gives

`tr(u_xu_y)=[x,y]^2`.                                      (2.1)

If `[x,y]=0`, then `y=lambda*x` with `lambda!=1`, and

`u_xu_y=I+(1+lambda^2)N_x`

is a nonidentity involution. Conversely trace zero forces the determinant to
vanish. If `[x,y]=1`, the characteristic polynomial is `T^2+T+1`, so the product
has order 3. Therefore

`|u_xu_y|=2 iff x,y are dependent`,

`|u_xu_y|=3 iff [x,y]=1`.                                  (2.2)

For the complete colouring, if `delta=[x,y]!=0`, let `lambda,lambda^-1` be the
roots in `F_{q^2}` of

`T^2+delta^2 T+1`.

Then `|u_xu_y|=ord(lambda)`. This gives every colour directly from the determinant
parameter; it is not merely a test for colours 2 and 3.

### Rigidity of the two selected relations

Let `F:V\{0}->V\{0}` be a permutation preserving both relations in (2.2).
The order-2 graph is the disjoint union of the `q+1` cliques
`ell\{0}`, for one-dimensional subspaces `ell`, so `F` permutes these cliques.
Since `[e_1,e_2]=1`, the matrix with columns `F(e_1),F(e_2)` lies in `SL(2,q)`.
After composing with its inverse we may assume `F(e_1)=e_1` and
`F(e_2)=e_2`.

There are bijections `alpha,beta:F_q^*->F_q^*`, both fixing 1, with

`F(a,0)=(alpha(a),0)`,  `F(0,b)=(0,beta(b))`.

The unique order-3 neighbour of `(a,0)` on the other axis is `(0,a^-1)`;
hence

`beta(a^-1)=alpha(a)^-1`.                                  (2.3)

For `a,b!=0`, the unique selected neighbour of `(a,b)` on each coordinate axis,
together with (2.3), now forces

`F(a,b)=(alpha(a),beta(b))`.

This formula also covers zero coordinates if `alpha(0)=beta(0)=0`. Preservation
of determinant one says

`ad+bc=1 iff alpha(a)beta(d)+beta(b)alpha(c)=1`.             (2.4)

In (2.4) put `b=1` and `c=ad+1`. We get

`alpha(ad+1)=alpha(a)beta(d)+1`.                            (2.5)

First set `a=1`, then `d=1`. These two specializations give

`beta(d)=alpha(d+1)+1`,  `alpha(a+1)=alpha(a)+1`,

so `alpha=beta`. Equation (2.5) then gives

`alpha(ad)=alpha(a)alpha(d)`.

Finally, for `a!=0`,

`alpha(a+b)=alpha(a)alpha(1+b/a)=alpha(a)+alpha(b)`.

Thus `alpha` is a field automorphism. Undoing the normalization proves

`Aut_2(Gamma) intersect Aut_3(Gamma) = GammaSL(2,q)`

on the vector model. Conversely every map `x -> A x^sigma`, with
`A in SL(2,q)` and `sigma in Gal(F_q/F_2)`, preserves dependence and determinant
one. By (2.1) it sends the trace parameter `delta^2` to its field-conjugate, so it
preserves the order of every product. Hence

`Aut(Gamma)=Aut_2(Gamma) intersect Aut_3(Gamma)=GammaSL(2,q)`.

This group is naturally `PGammaL(2,q)` and has order
`q(q^2-1)f` for `q=2^f`.

Both selected relations are nonempty: an order-2 clique has size `q-1>=3`, and
between any two distinct cliques the determinant-one relation is a perfect
matching. For every absent positive label `t`, the source implication is vacuous
and `Aut_t(Gamma)=S_D`; this does not change the full intersection.

## 3. Small exceptional isomorphism `A5`

The case `q=4` is included above and gives the unique involution class of
`PSL(2,4) isomorphic to A5`, with common automorphism group of order 120.
The pair `(L,D)` for `q=5` is literally the same abstract pair because
`PSL(2,5) isomorphic to A5` and `A5` has one involution class. Therefore the same
equality handles `q=5` without relying on the odd-characteristic rigidity lemma.

## 4. Odd characteristic: exact trace reduction

Let `q` be odd. Put

`W=sl_2(F_q)`,  `Q(X)=-det(X)`,  `B(X,Y)=tr(XY)`.

Then `B` is the polar form of `Q`. Every projective involution has a lift
`X in SL(2,q)` with `tr(X)=0`, hence `X^2=-I` and `Q(X)=-1`. Conversely every
such lift gives an involution, and `X,-X` give the same vertex. All trace-zero
determinant-one matrices are one `SL(2,q)` conjugacy orbit: they are one
`GL(2,q)` orbit, and the determinant map on their centralizer is surjective
(a product map in the split case and the norm `F_{q^2}^*->F_q^*` in the nonsplit
case), so a conjugator can be adjusted to determinant one. Thus there is again
one complete involution class, modeled as

`D={ [X] in P(W) : Q(X) has the square class of -1 }`.       (4.1)

Writing `epsilon=chi(-1)`, this class has

`|D|=q(q+epsilon)/2`.

Choose representatives with `Q(X)=Q(Y)=-1`. For `g=XY`,

`det(g)=1`,  `tr(g)=B(X,Y)=s`.                              (4.2)

Changing either representative changes `s` to `-s` but not the element of
`PSL(2,q)`. For distinct vertices:

`|XY| in PSL(2,q) is 2 iff s=0`,

`|XY| in PSL(2,q) is 3 iff s^2=1`.                          (4.3)

The second statement includes characteristic 3: there `s^2=1=4` gives a
noncentral unipotent lift, of projective order 3. For every other colour, if
`s^2!=4`, take a root `lambda` of `T^2-sT+1` in `F_{q^2}`; the product order is
the least `n>0` with `lambda^n=+-1`. If `s^2=4`, distinctness makes the product
nontrivial unipotent, of order equal to the characteristic. This is the complete
product-order colouring, determined by `s^2`.

In projective, normalization-free form the two relations are

`R_2: B(X,Y)=0`,

`R_3: B(X,Y)^2=Q(X)Q(Y)`.                                  (4.4)

The relation sizes can also be read off without a group catalogue. Conjugate a
fixed vertex to `X=((0,1),(-1,0))` and write
`Y=((a,b),(c,-a))`. The equations `det(Y)=1` and
`B(X,Y)=c-b` give

`valency(R_2)=(q-epsilon)/2`.

If the characteristic is not 3, the quadratic-character sum for `c-b=1` gives

`valency(R_3)=q-epsilon`.

If `q=3^f`, the relevant equation becomes `a^2=-(b-1)^2`. After removing the
solution representing `X` itself, this gives

`valency(R_3)=2(q-1)` when `f` is even, and `0` when `f` is odd.               (4.5)

Every semilinear similarity of `(W,Q)` preserves (4.4) and sends `s^2` to a field
conjugate, hence preserves every product order. Its projective group is
`PGammaO(3,q) isomorphic to PGammaL(2,q)`.

### Exact remaining lemma

It remains to prove, for every odd `q>=7`, that every permutation of the norm
orbit (4.1) preserving both relations (4.4) is induced by a semilinear similarity:

`Aut(D;R_2,R_3)=PGammaO(3,q)`.                              (R)

In fact the reviewed `q=9` data suggest that `R_2` alone may be rigid, but that
finite fact is not a proof of (R). No family equality is claimed without (R).

The empty-relation case is real, not cosmetic. When `q=3^f` with `f` odd,
`q=3 mod 4`, and (4.5) proves that `R_3` is empty. Hence
`Aut_3(Gamma)=S_D` vacuously. Any proof of (R) there must therefore come from the
orthogonality relation `R_2` alone. For characteristic 3 with `f` even, and for
odd characteristic other than 3, (4.5) proves that `R_3` is nonempty. The
order-2 valency above is positive for every odd simple case.

## What this does not establish

- It does not prove (R), so it does not cover general odd `q>=7`.
- It does not infer an infinite-family result from the reviewed computations at
  `q=8,9,11`.
- It says nothing about finite simple groups outside `PSL(2,q)` and does not answer
  the universal quantifier in Problem 21.53.
- It does not address Problem 21.52's separate induction-by-group-automorphisms
  question.

---
title: "Kourovka 21.53 — odd PSL(2,q) coherent-closure calculation"
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
strategy: PSL2-ODD-COHERENT-CLOSURE
direction: proof
outcome: PARTIAL_RESULT
claim: "Exact mixed intersection formulas hold throughout the q=3 mod 4 PSL(2,q) branch; they give hand proofs of the required equality for q=11 and q=19, but not for the whole odd branch."
scope_answered:
  - "bounded pair PSL(2,11), unique involution class"
  - "bounded pair PSL(2,19), unique involution class"
scope_not_answered:
  - 21.53/two-minimal-prime-colours
  - "PSL(2,q), q=3 mod 4, outside the two displayed bounded pairs"
  - "finite simple groups outside PSL(2,q)"
active_assignment_answered: no
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/association-schemes
  - project/kourovka
  - status/conjectured
---

# Outcome

`PARTIAL_RESULT`, not a universal claim.  For the nonsquare-minus-one branch of
odd `PSL(2,q)`, I derive the exact pair parameter and all four mixed
common-neighbour counts generated immediately by the order-2 and order-3
relations.  The raw counts do not give a uniform family proof.  They do,
however, give a short exact proof for `q=11`, and one further explicitly bounded
coherent refinement gives a short exact proof for `q=19`.

The characteristic-three branch is different: the order-3 graph is empty, so
the claimed intersection reduces to the order-2 graph automorphism group.  No
result for that infinite subfamily is claimed here.

## Active-time ledger

- Work start: `2026-08-18T00:24:22Z`, cumulative active minutes `0`.
- Early separation gate: reached before the 15-minute ceiling.  The exact raw
  formulas have at most fourteen signatures and therefore cannot uniformly
  reconstruct all pair parameters; no full-profile collision was established.
- Work stop: `2026-08-18T00:32:22Z`, cumulative active minutes `8`; `37`
  minutes of the allowance are returned.

# Scope guard

The canonical target is universal over every finite nonabelian simple `L` and
every single involution class `D`.  This note concerns only the unique
involution class of `PSL(2,q)` for odd `q=3 mod 4`, and proves the target
conclusion only at `q=11,19`.  It says nothing about the induction assertion in
Problem 21.52.

# 1. Exact orthogonal model and pair invariant

Let `F=F_q`, where `q` is odd and `q=3 mod 4`, and put

`V=sl_2(F)`, `Q(x)=-det(x)`, `B(x,y)=tr(xy)`.

The shell representing the involution class is

`D={ [x] in P(V) : chi(Q(x))=-1 }`,

where `chi` is the quadratic character, extended by `chi(0)=0`.  Indeed,
`chi(-1)=-1`, so a line in this shell has two representatives of determinant
one, differing by sign.  Such a representative has trace zero and square
`-I`, hence gives an involution in `PSL(2,q)`.  Conversely every involution has
such a lift.  The usual centralizer adjustment in the nonsplit torus shows that
these lifts form one conjugacy class.  For `q>3`, `PSL(2,q)` is finite
nonabelian simple.

For distinct `[x],[y] in D`, define

`t(x,y)=B(x,y)^2/(Q(x)Q(y))`.                         (1)

This is independent of projective representatives.  Rescale representatives
so that `Q(x)=Q(y)=kappa`, for a fixed nonsquare `kappa`, and put
`s=B(x,y)/kappa`.  Then `t=s^2`.

The occurring parameters are exactly

`T_q={ squares in F, including 0 } minus {4}`.         (2)

For the exclusion, `t=4` would make `y-(s/2)x` a nonzero isotropic vector in
the anisotropic plane `x^perp`, unless `[x]=[y]`.  Conversely, for any square
`t!=4`, choose `s^2=t` and choose

`v in x^perp` with `Q(v)=kappa(4-t)/4`;

the anisotropic binary norm form represents every nonzero field element, and
`y=(s/2)x+v` realizes the parameter.

If `X,Y` are determinant-one lifts and `r` is the eigenvalue quotient of `XY`,
then

`t=r+r^(-1)+2`.                                       (3)

Thus `t` determines the unordered pair `{r,r^(-1)}` and hence the exact order
of `XY` in `PSL(2,q)`.  In particular, outside characteristic 3,

`R_2: t=0`, and `R_3: t=1`.                           (4)

# 2. Exact mixed common-neighbour formula

For `a,b in {0,1}`, let `N_ab(t)` be the number of vertices `[z]` for which
`t(x,z)=a` and `t(z,y)=b`; the symbols `0,1` correspond respectively to
product orders `2,3` by (4).

Assume first that the characteristic is not 3.  Choose
`w perpendicular <x,y>` and write `c=Q(w)`.  The Gram determinant gives

`chi(c)=-chi(4-t)`.                                   (5)

If `B(x,z)=kappa e`, `B(y,z)=kappa f`, with
`e^2=a`, `f^2=b`, solving for the projection of `z` onto `<x,y>` gives

`Q(z)=kappa(e^2+f^2-sef)/(4-t)+c lambda^2`.

The equation `Q(z)=kappa` therefore has

`1+chi(4-t-a-b+sef)`

solutions for `lambda`; (5) is exactly what cancels the apparent square-class
factor.  Summing over the permitted signs of `e,f` and dividing by two for the
representatives `z,-z` yields

`N_ab(t)=(1/2) sum_(e^2=a,f^2=b) [1+chi(4-t-a-b+sef)]`. (6)

No diagonal correction is needed here: the diagonal has parameter `4`, not
`0` or `1`.  Consequently

`N_22(t)=(1+chi(4-t))/2`,                              (7)

`N_23(t)=N_32(t)=1+chi(3-t)`,                         (8)

`N_33(t)=2+chi(2-t+s)+chi(2-t-s)`,  `s^2=t`.          (9)

The last expression is independent of the sign chosen for `s`.  Its two
character arguments have product

`(2-t+s)(2-t-s)=(t-1)(t-4)`.                         (10)

Equations (7)--(9) are exact intersection counts, not numerical stress tests
or adjacency-algebra dimension evidence.

# 3. The minute-15 separation gate

The raw signature

`Sigma(t)=(N_22(t),N_23(t),N_33(t))`

does not uniformly recover `t`.  Away from `t=1,3`, its coordinates take at
most `2`, `2`, and `3` values respectively.  The exceptional values add at
most two further signatures, so there are at most fourteen raw signatures,
whereas `|T_q|=(q-1)/2` is unbounded.

This is already a failure of exact pair-parameter reconstruction.  It is also
not merely a same-order collision in the first nontrivial example below:
over `F_19`, parameters `t=6` and `t=17` have the identical signature
`(1,2,2)` but product orders `5` and `10` respectively.  For `t=6`, the
eigenvalue quotient satisfies `r+r^(-1)=4`; the recurrence
`S_(n+1)=4S_n-S_(n-1)` for `S_n=r^n+r^(-n)` gives `S_5=2`, hence `r^5=1`,
and `r!=1`, so its order is 5.  Replacing `r` by `-r` changes `t` to
`4-t=17` and changes the odd order 5 to order 10.

This does **not** meet the hard-kill criterion for the whole coherent strategy.
Equality of the raw signature is not equality of the full generated coherent
profile.  I therefore do not claim a fusion obstruction, and I do not infer
reconstruction from an adjacency-algebra dimension.

One reusable positive consequence of (8) is that, whenever `3` is a square,
the parameter relation `t=3` is canonically recovered as the unique relation
with `N_23=1`.  By (3), it is the exact product-order-6 relation.

# 4. Exact bounded consequence: `PSL(2,11)`

The square parameters in `F_11`, with `4` removed, are

`T_11={0,1,3,5,9}`.

Equation (3) gives the order partition

- `t=0`: order 2;
- `t=1`: order 3;
- `t=3`: order 6, since `r^2-r+1=0`;
- `t=5,9`: order 5 (the inverse root pairs are respectively `{5,9}` and
  `{3,4}` in `F_11`).

From (8), the values of `N_23` in this order are

`2,0,1,2,2`.

Thus every permutation preserving `R_2` and `R_3` also preserves `t=3`, hence
the order-6 colour.  The only edges left after the order `2,3,6` colours are
removed are exactly the order-5 edges.  Therefore, for the exact unique
involution class of `PSL(2,11)`,

`Aut(Gamma)=Aut_2(Gamma) intersection Aut_3(Gamma)`.   (11)

This is a bounded fixed-pair result only.

# 5. One explicitly bounded refinement: `PSL(2,19)`

Here

`T_19={0,1,5,6,7,9,11,16,17}`.

Using the square set

`{1,4,5,6,7,9,11,16,17}`

in (7)--(9) gives the following exact hand table.

| `t` | `N_22` | `N_23` | `N_33` | raw cell |
|---:|---:|---:|---:|---|
| 0  | 1 | 0 | 0 | singleton |
| 1  | 0 | 0 | 1 | singleton |
| 5  | 0 | 2 | 4 | singleton |
| 6  | 1 | 2 | 2 | paired with 17 |
| 7  | 1 | 0 | 2 | singleton |
| 9  | 0 | 0 | 2 | singleton |
| 11 | 0 | 2 | 2 | singleton |
| 16 | 1 | 2 | 4 | singleton |
| 17 | 1 | 2 | 2 | paired with 6 |

Thus the first intersection signature canonically recovers every exact
parameter relation except `S_6 union S_17`, where `S_a` means `t=a` (not
product order `a`).  In particular `S_5` is already canonical.

Apply one bounded further intersection count using `R_2=S_0` and `S_5`.
The same derivation as (8), with `1` replaced by `5`, gives

`p_{0,5}(t)=1+chi(4-5-t)=1+chi(-1-t)`.               (12)

For the two unresolved parameters,

`p_{0,5}(6)=1+chi(12)=0`,

`p_{0,5}(17)=1+chi(1)=2`.

Hence the one further coherent refinement separates `S_6` from `S_17`.
Every exact parameter relation is now invariant under every permutation that
preserves `R_2,R_3`.  By (3), every exact product-order colour is a union of
these parameter relations.  Therefore, for the exact unique involution class
of `PSL(2,19)`,

`Aut(Gamma)=Aut_2(Gamma) intersection Aut_3(Gamma)`.   (13)

For completeness, `|PSL(2,19)|=3420`, so the two least distinct prime divisors
are indeed `2,3`.  The argument is entirely symbolic finite-field arithmetic;
no graph or group computation was used.

# 6. Characteristic 3 and the vacuous order-3 colour

Let `q=3^f=3 mod 4`; then `f` is odd.  The case `q=3` is not simple, so the
first admissible field is `q=27`.  In characteristic 3, `1=4`.  But (2) says
that `t=4` cannot occur for two distinct shell points.  Therefore the exact
order-3 edge relation is empty:

`R_3=empty`, and `Aut_3(Gamma)=S_D` vacuously.         (14)

Accordingly the active equality in this subfamily reduces to

`Aut(Gamma)=Aut_2(Gamma)`.

Equations (8)--(9) must not be reused as graph-neighbour formulas in this
case: their algebraic `t=1` condition is the diagonal/repeated-root value, and
graph neighbourhoods exclude the diagonal.  The actual mixed counts involving
`R_3` are all zero.  Only

`N_22(t)=(1+chi(1-t))/2`

survives.  The present two-relation route therefore collapses to the coherent
closure of the orthogonality graph alone.  I found no exact proof that this
closure recovers all product orders and no exact full-profile collision that
would hard-kill it.  This branch remains open.

# 7. What this establishes and does not establish

Established here:

1. the exact parameter set and order dictionary for every odd
   `q=3 mod 4`;
2. the exact mixed counts (7)--(9) outside characteristic 3;
3. canonical recovery of the product-order-6 relation when it occurs;
4. the active two-colour equality for the two bounded pairs
   `PSL(2,11)` and `PSL(2,19)`.

Not established:

1. a full coherent-profile separation theorem for arbitrary `q`;
2. any result for `q=3^f`, odd `f>=3`, beyond the exact vacuity reduction;
3. the universal revision-2 target;
4. any assertion from Problem 21.52.

The most useful next representation-changing step is not another raw adjacency
power.  It is an exact classification of the coherent cells obtained after the
line-type split `chi(4-t)=+/-1`, or a geometric proof that the resulting
external/secant-line sections are canonically reconstructible.  Any such proof
must explicitly connect recovered cells to exact product-order unions.

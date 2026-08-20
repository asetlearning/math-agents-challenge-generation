---
title: "Verification — Kourovka 21.53 — odd PSL(2,q) square branch"
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
scope_record: Agents/Kourovka/scopes/21.53-two-minimal-prime-colours.json
assignment_revision: 2
claim: "For every odd prime power q>=9 with q congruent to 1 modulo 4, the unique involution class D of PSL(2,q) satisfies Aut(D;R_2,R_3)=PGammaO(3,q)=Aut(Gamma)."
claimant: Problem-21.53-Proof
target_statement: "For every finite nonabelian simple L and every involution class D, Aut(Gamma)=Aut_2(Gamma) intersect Aut_p(Gamma), where p is the second-smallest distinct prime divisor of |L|."
excluded_scopes: ["q congruent to 3 modulo 4", "finite simple groups outside PSL(2,q)", "Problem 21.52", "the universal revision-2 conclusion"]
target_object: "The unique involution class of PSL(2,q), for odd prime powers q>=9 with q congruent to 1 modulo 4, as a bounded subfamily of the source target."
witness_object: "The projective square-class shell in sl_2(q), with Q=-det and B its polar form."
witness_equals_target: proven-with-citation
citation: "Direct algebraic identification in the Target versus witness section below; simplicity uses the standard PSL(2,q) simplicity theorem for q>3."
verification_method: "Hostile line-by-line hand reconstruction"
tools_used: ["GAP 4.12.1 (availability probe only)", "Python 3.12.3 (availability probe only)"]
scope_answered: ["bounded family: odd PSL(2,q), q>=9, q congruent to 1 modulo 4"]
scope_not_answered: ["21.53/two-minimal-prime-colours", "odd PSL(2,q) with q congruent to 3 modulo 4", "all non-PSL(2,q) finite simple groups"]
active_assignment_answered: no
verdict: PASS_AS_PARTIAL_RESULT
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/finite-geometry, project/kourovka, status/conjectured]
---

# Verification — Kourovka 21.53

## The claim

The submitted theorem is correct as an exact infinite-family partial result:
for every odd prime power `q>=9` with `q=1 mod 4`, the two exact product-order
relations `R_2,R_3` on the unique involution class of `PSL(2,q)` have
automorphism group `PGammaO(3,q)`, and that group preserves every exact
product-order colour.

The active revision-2 assertion is universal over all finite nonabelian simple
groups and all involution classes.  This partial theorem cannot answer that
active assignment.

## Scope, revision, and clause matrix

The scope is locked to `21.53/two-minimal-prime-colours`, revision `2`.

| source clause | result of this verification |
|---|---|
| one involution class `D` in a finite nonabelian simple group, with complete exact product-order colouring | checked for the unique class in the stated `PSL(2,q)` subfamily only |
| exact definition of every `Aut_t`, including the vacuous convention | the proof uses exact order-2 and order-3 edge sets; both are nonempty here, so no vacuous-label inference occurs |
| `Aut(Gamma)` is the intersection of every occurring colour stabilizer | checked in the bounded family by proving `PGammaO(3,q)` preserves every product order |
| two smallest primes are `2,p`, and the claimed equality uses those exact colours | `p=3` throughout the bounded family; the equality is checked there |
| universal question over every `(L,D)` | not answered |

`active_assignment_answered: no`.

## Constraint-and-conclusion matrix

| constraint_id | role | proof evidence | result |
|---|---|---|---|
| `21.53-forall-L-D` | admissibility | claimant explicitly restricts to one infinite `PSL(2,q)` branch | **not universal**; valid only as `PARTIAL_RESULT` |
| `21.53-L-finite-nonabelian-simple` | admissibility | `PSL(2,q)` is finite and is nonabelian simple for `q>3`; here `q>=9` | pass in bounded family |
| `21.53-D-single-involution-class` | admissibility | direct trace-zero-shell bijection and conjugacy proof below | pass |
| `21.53-Gamma-product-order-colouring` | admissibility | `u=tr(xy)^2/det(xy)` determines the eigenvalue ratio and hence exact projective order | pass |
| `21.53-Aut-t-definition` | admissibility | `R_2` and `R_3` are checked as exact order relations, including characteristic 3 and distinct vertices | pass |
| `21.53-two-minimal-primes` | admissibility | `|PSL(2,q)|=q(q^2-1)/2`; it is even and one of `q-1,q,q+1` is divisible by 3 | pass with `p=3` |
| `21.53-full-colour-group-definition` | admissibility | full-colour stabilizer is squeezed between the two-colour group and the product-order-preserving `PGammaO(3,q)` action | pass in bounded family |
| `21.53-two-colours-determine-all` | target conclusion | equality proved below for the displayed branch | pass in bounded family; unproved for active universal scope |

No claim-check JSON is required for this correctly labelled `PARTIAL_RESULT`; it
is not routed as a universal `CLAIM` or `STALE_MATCH`.

## Target versus witness

Put `V=sl_2(F_q)`.  In coordinates

`x=[[a,b],[c,-a]]`,

take

`Q(x)=-det(x)=a^2+bc`

and let `B` be the polar form.  Direct multiplication gives

`B(x,y)=tr(xy)`.

A projective line `[x]` contains a determinant-one representative precisely
when

`chi(det x)=chi(-Q(x))=1`,

or equivalently `chi(Q(x))=chi(-1)=epsilon`.  Such a representative `A` has
trace zero, so Cayley--Hamilton gives `A^2=-I`; its image in `PSL(2,q)` is an
involution.  Conversely every nonidentity involution in `PSL(2,q)` has a lift
`A in SL(2,q)` satisfying `A^2=-I`, hence trace zero, and gives exactly one
such projective line (the two determinant-one choices differ by `-I`).

In the present branch `epsilon=1`, so `-1` has a square root `i`.  Every
trace-zero determinant-one matrix has eigenvalues `i,-i` and is conjugate to
`diag(i,-i)`.  A `GL(2,q)` conjugator can be adjusted to determinant one by
multiplying it by an arbitrary-determinant element of that diagonal matrix's
centralizer.  Thus all the resulting involutions are `SL(2,q)`, hence
`PSL(2,q)`, conjugate.  The shell is exactly the unique target class `D`, not
a surrogate orbit.

## Subclaims and what each method proves

| subclaim | method | pass proves | pass does not prove |
|---|---|---|---|
| model and order dictionary | direct `2x2` algebra | exact bounded target and exact edge labels | another simple group |
| `c_22,m_23` and tangent relation | Gram determinants and binary forms | `T` is first-order/count definable from `R_2,R_3` | the nonsquare-minus-one branch |
| conic recovery | elementary tangent incidence and intersecting-pair classification | every two-relation automorphism induces a conic permutation | projective completion from `R_2` alone |
| harmonic reconstruction | explicit coordinates and field identities | the conic permutation lies in `PGammaL(2,q)` | a result in characteristic 2 |
| group/full-colour identification | adjoint/conic action and exact order dictionary | equality of the two-colour and full-colour groups | universal Problem 21.53 |

## Evidence

### Tool probe (verbatim)

No mathematical computation was run.  The mandatory availability probe was:

```text
$ for tool in gap sage python3 magma; do command -v "$tool" || true; done
/usr/bin/gap
/usr/bin/python3

$ gap -q -c 'Print(GAPInfo.Version, "\n"); QUIT;'
4.12.1

$ python3 --version
Python 3.12.3
```

There was no script, manifest, or compute lease, and none was needed.

### 1. Exact trace-to-order dictionary

For distinct `[x],[y] in D`, the matrix `xy` is nonscalar: if it were scalar,
then `x` and `y` would define the same trace-zero projective line.  Moreover

`tr(xy)=B(x,y)`,  `det(xy)=Q(x)Q(y)`.

Thus

`u(x,y)=B(x,y)^2/(Q(x)Q(y))=tr(xy)^2/det(xy)`.

If `r` is the eigenvalue quotient of `xy` in the algebraic closure, then

`u=r+r^(-1)+2`.

The unordered pair `{r,r^(-1)}` is therefore determined by `u`, and the exact
projective order of `xy` is determined by `u`.  In particular:

- `u=0` gives `r=-1`, hence exact projective order 2;
- if the characteristic is not 3, `u=1` gives
  `r^2+r+1=0` with `r!=1`, hence exact projective order 3;
- in characteristic 3, `u=1=4` gives a repeated eigenvalue, and nonscalarity
  makes `xy` a nontrivial unipotent, again of exact order 3.

This proves that the submitted `R_2,R_3` really are the source's exact edge
colours.  It also proves the full-colour assertion used at the end: a field
automorphism sends `r` to a Frobenius power and cannot change its multiplicative
order, while it preserves the unipotent case.

### 2. The sign in `c_22`

In the coordinate basis above, the Gram matrix of `B` is

`[[2,0,0],[0,0,1],[0,1,0]]`,

whose determinant has square class `chi(-2)`.  For independent representatives
`x,y`, put

`Delta=4Q(x)Q(y)-B(x,y)^2=Q(x)Q(y)(4-u)`.

If `u!=4`, let `z` span `<x,y>^perp`.  In the orthogonal basis
`x,y,z`, determinant comparison gives

`chi(-2)=chi(2 Q(z) Delta)`.

Because `chi(Q(x)Q(y))=epsilon^2=1`, cancellation yields

`chi(Q(z))=epsilon chi(4-u)`.

The only possible common `R_2` neighbour is `[z]`, and it belongs to `D`
exactly when `chi(4-u)=1`.  If `u=4`, the line `<x,y>` is degenerate and its
orthogonal point is its isotropic radical, so it is not in `D`.  Hence, with
`chi(0)=0`,

`c_22(x,y)=1` exactly when `chi(4-u)=1`, and is zero otherwise.

The sign in the submission is correct.

### 3. The mixed number `m_23`

First assume characteristic different from 3 and `u!=4`.  Since `x,y` have
the same norm square class, rescale them so that

`Q(x)=Q(y)=kappa`.

Write `y=a x+y_0`, with `y_0 perpendicular x`.  Then

`A=Q(y_0)=kappa(4-u)/4`.

Choose `w in x^perp` perpendicular to `y_0` and put `C=Q(w)`.  Determinant
comparison in the orthogonal basis `x,y_0,w` gives `chi(AC)=1`, hence
`chi(A/C)=1`.  Every candidate common point has the form

`z=c y_0+d w`.

The conditions `z R_2 x` and `z R_3 y` reduce exactly to

`4A^2c^2=kappa(Ac^2+Cd^2)`,

or

`(d/c)^2=A(3-u)/C`.

There is no solution with `c=0`.  For every solution the displayed order-3
equation gives

`chi(Q(z))=chi(4A^2c^2/kappa)=chi(kappa)=epsilon`,

so no extra shell solutions have been counted or lost.  The number of
projective solutions is consequently

`m_23(x,y)=1+chi(3-u)`.

For `u=4`, occurrence between distinct shell points is possible exactly when
`epsilon=1`: it says that `x^perp` contains an isotropic vector.  Choose signs
so that `B(x,y)=2kappa`, write `y=x+r` with `r` isotropic, and choose isotropic
`s in x^perp` with `B(r,s)=1`.  For `z=alpha r+beta s`, shell membership forces
`alpha beta!=0`, and the order-3 equation is

`beta^2=kappa alpha beta`.

Thus `beta=kappa alpha`, giving exactly one projective solution.  Therefore
`m_23=1` at `u=4`, as submitted.

For `u!=4`, the value `m_23=1` occurs only at `u=3`; there
`chi(4-u)=chi(1)=1`, so `c_22=1`.  At `u=4`, by contrast,
`c_22=0` and `m_23=1`.  Hence in characteristic different from 3 the relation

`T(x,y) iff x!=y, c_22(x,y)=0, and m_23(x,y)=1`

is canonically definable from `R_2,R_3` and is exactly `u=4`.

### 4. Characteristic 3, including every even `f`

When `q=3^f` lies in this branch, `f` is even and `q>=9`.  Here the exact
order-3 relation is already

`R_3: u=1=4`.

It is important not to reuse the mixed-count proof blindly: at `u=0`, the
algebraic equation for `z R_3 y` admits `z=y` because the diagonal value
`u(y,y)=4=1`, but graph neighbourhoods exclude the diagonal.  This is exactly
why the submission restricted formula (1) to characteristic different from 3.
Defining `T=R_3` bypasses the diagonal issue and gives `T iff u=4` directly.
Thus the characteristic-3 branch of the claimed theorem, including `q=9`, is
valid.

### 5. Exterior points, tangent pairs, and the triangular graph

For `x in D`, determinant comparison shows that the binary form on `x^perp`
has square determinant class.  Such a binary form has two isotropic projective
points exactly when `chi(-1)=1`.  Hence in the present branch every point of
`D` is exterior to the conic `C:Q=0`, and the isotropic points of `x^perp` are
exactly its two tangent contact points.

The map

`x -> {the two contact points of the tangents through x}`

is bijective: two distinct conic tangents meet in an exterior point, and taking
the tangent intersection is inverse to the map.

Also `u=4` is equivalent to the degeneracy of `<x,y>`.  A degenerate line in
a nondegenerate projective orthogonal plane is the polar of its isotropic
radical, hence a conic tangent.  Therefore two exterior points satisfy `T`
exactly when their tangent pairs have a common contact point.  Under the
bijection, `(D,T)` is exactly the triangular graph on the `q+1` conic points.

### 6. Maximum cliques and the `q=9` boundary

A pairwise-intersecting family of 2-subsets either has a common point or is the
three edges on a 3-element support.  Indeed, after choosing `{a,b}` and
`{a,c}`, any member not containing `a` must be `{b,c}`, after which no fourth
member is possible.

The stars have size `q`, whereas the non-star cliques have size at most 3.
Since `q>=9`, the maximum cliques are canonically and uniquely the stars.
Every `T`-automorphism consequently induces one permutation `pi` of `C`, and
on vertices it acts by

`{a,b} -> {pi(a),pi(b)}`.

At `q=9` this is the triangular graph on 10 points: stars have size 9 and the
only competitors have size 3.  There is no small-parameter clique degeneracy.

### 7. Orthogonality is harmonicity

Use

`C={(t^2,t,1):t in F_q} union {(1,0,0)}`

for the conic `XZ-Y^2=0`.  For finite distinct `a,b`, the tangents at `a,b`
meet at

`x_ab=(2ab,a+b,2)`.

With the polar form

`B((X,Y,Z),(X',Y',Z'))=XZ'+ZX'-2YY'`,

direct substitution gives

`B(x_ab,x_cd)=0`

if and only if

`2(ab+cd)=(a+b)(c+d)`.

The same formula, interpreted projectively, covers infinity (or follows by a
one-line substitution using the tangent `Z=0`).  It is equivalent to

`(a-c)(b-d)+(a-d)(b-c)=0`,

that is, `(a,b;c,d)=-1`.  Distinct `R_2` vertices cannot share a tangent
contact, so the four conic points here are genuinely distinct.  Thus `pi`
preserves exactly the harmonic quadruples, not merely a necessary incidence
condition.

### 8. Additivity and multiplicativity, with omitted values

Compose `pi` with the unique element of `PGL(2,q)` sending its images of
`infinity,0,1` back to `infinity,0,1`.  Call the resulting harmonicity-preserving
permutation `h`.  It fixes those three points and maps finite points to finite
points.

For every nonzero `c`, harmonicity of

`(infinity,0;c,-c)`

gives `h(-c)=-h(c)`; the case `c=0` is immediate.  For `b!=c`, harmonicity of

`(infinity,b;c,2b-c)`

gives

`h(2b-c)=2h(b)-h(c)`.

When `b=c` the same identity is tautological.  Taking `c=0` first yields
`h(2b)=2h(b)`.  Taking `b=(x+y)/2` and `c=x` then yields additivity when
`x!=y`; when `x=y` it is the already checked doubling identity.  Hence

`h(x+y)=h(x)+h(y)`

for all `x,y`.

For `x notin {0,1,-1}`, all four points in

`(x,-x;1,x^2)`

are distinct and the displayed cross-ratio equation shows that they are
harmonic.  Its image under `h`, together with `h(-x)=-h(x)` and `h(1)=1`,
gives

`h(x^2)=h(x)^2`.

The omitted values are not assumptions:

- `x=0`: both sides are zero;
- `x=1`: both sides are one;
- `x=-1`: `h(-1)=-1` and both square values are one.

Finally apply the square identity to `x+y` and use additivity:

`h(x^2)+2h(xy)+h(y^2)=h(x)^2+2h(x)h(y)+h(y)^2`.

After cancelling the square terms and dividing by 2 (the characteristic is
odd), one obtains

`h(xy)=h(x)h(y)`

for every `x,y`.  Thus `h` is a field automorphism and
`pi in PGammaL(2,q)`.  The argument remains valid in characteristic 3 and for
`q=9`; division by 2 is legitimate, and `F_9` has six values outside
`{0,1,-1}`.

### 9. Exact group identification and all product-order colours

The symmetric-square/conic action identifies the conic stabilizer
`PGammaL(2,q)` with `PGammaO(3,q)`.  Concretely, a semilinear fractional
transformation represented by `(A,sigma)` acts on `sl_2(q)` by

`x -> A x^sigma A^(-1)`.

This preserves `Q,B` up to the same field automorphism and induces the usual
action on the conic.  Conversely a projective semilinear collineation preserving
the nonsingular conic preserves its defining quadratic form up to scalar and
is in `PGammaO(3,q)`.  In dimension 3 the similitude multiplier has square
class one (take determinants in the similitude equation), so this group
preserves the shell `D` rather than interchanging the two anisotropic shells.

The maximum-clique and harmonic arguments prove the upper bound

`Aut(D;R_2,R_3) <= PGammaO(3,q)`.

The displayed semilinear conjugation preserves the equations `u=0` and `u=1`,
so it gives the reverse inclusion.  More strongly,

`(xy) -> A (xy)^sigma A^(-1)`

preserves the exact order of every product.  Therefore

`PGammaO(3,q) <= Aut(Gamma) <= Aut(D;R_2,R_3)=PGammaO(3,q)`.

All three groups are equal.  This closes the bounded family claim without
assuming Problem 21.52 or inferring sufficiency from a necessary invariant.

### 10. Explicit `q=9` and characteristic-3 stress audit

For `q=9`, `PSL(2,9)` is simple of order 360, its second-smallest prime divisor
is 3, and the trace-zero shell is its single 45-element involution class.
Here `chi(-1)=1`, `R_3` is exactly the tangent-sharing relation because
`1=4` in characteristic 3, the recovered triangular graph has 45 vertices and
10 stars of size 9, and the harmonic reconstruction includes the nontrivial
field automorphism of `F_9`.  The exceptional isomorphism
`PSL(2,9) isomorphic to A_6` introduces no additional relation automorphism:
the maximum-clique step first forces a permutation of the 10 conic points, and
the harmonic identities then force that permutation into `PGammaL(2,9)`.

For every `q=3^f` in the claimed congruence branch, `f` is even.  The same
direct `T=R_3` argument applies.  No hidden `q=9` or even-`f`
characteristic-3 exception remains.

### 11. Ancillary nonsquare-branch reduction

The submission's stated limitation is honest.  In the excluded
`epsilon=-1` branch, if `M` is the full polarity-incidence matrix with loops
at isotropic points, then projective-plane incidence gives `M^2=qI+J`.  Since
the `D`--conic block is zero, its `D`--`D` block indeed gives

`XX^T=qI+J-A^2`.

The column and row weights `(q-1)/2` and `(q+1)/2`, and the unique-column
interpretation of a zero-codegree pair, follow from the same line-section
counts.  What does **not** follow is uniqueness of the binary factorization,
geometricity of all column supports, or uniqueness of the proposed resolutions.
The note correctly labels those as missing lemmas.  This reduction does not
solve or validate the `q=3 mod 4` branch.

## Verdict

**PASS AS `PARTIAL_RESULT` for the exact bounded family.**  The hostile hand
reconstruction finds no gap in the theorem for odd `PSL(2,q)`, `q>=9`,
`q=1 mod 4`.  The signs, exceptional characteristics, canonical reconstruction,
field identities, group identification, and full-colour implication all check.

The note remains tagged `status/conjectured` at this moment because the common
protocol permits `status/proven` only after the human has seen the checked proof.
This is a certification gate, not a mathematical defect in the bounded proof.

`active_assignment_answered: no`.

## Why this verdict

The proof model is algebraically identical to the target involution class; the
two retained relations are exact product-order relations; tangent-sharing is
canonically recoverable in both the ordinary and characteristic-3 cases; the
triangular graph recovers the conic without a small-parameter exception; and a
fully explicit harmonic reconstruction forces precisely the semilinear
orthogonal group, which preserves every product order.

## What is NOT established

- The universal scope `21.53/two-minimal-prime-colours` is not answered.
- No case with `q=3 mod 4` is proved, including the empty-`R_3` subfamily
  `q=3^f` with odd `f`.
- No finite simple group outside the stated odd `PSL(2,q)` branch is covered.
- No statement of Problem 21.52 is certified.
- The factorization and resolution uniqueness problems following
  `XX^T=qI+J-A^2` remain open.
- This clean-room review does not make a novelty or literature-staleness claim.
- Promotion to `status/proven` awaits the mandatory human-view gate.

## What would upgrade it

After the human has seen this verification, Validator may promote this exact
bounded theorem to `status/proven`.  Closing the active assignment would still
require a proof for every remaining finite nonabelian simple group and every
involution class; the present result cannot be extrapolated to those cases.

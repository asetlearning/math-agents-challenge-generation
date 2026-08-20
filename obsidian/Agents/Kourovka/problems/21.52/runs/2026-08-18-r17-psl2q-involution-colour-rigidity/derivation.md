---
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, topic/finite-simple-groups, status/conjectured]
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
cycle: 17
strategy: PSL2Q-INVOLUTION-COLOUR-RIGIDITY
---

# Cycle 17: involution colour rigidity in `PSL(2,q)`

## Active-time ledger

- `2026-08-18T10:50:21Z`: cycle active start (including required protocol reads);
  inherited cumulative active time 311 minutes.
- `2026-08-18T10:52:53Z`: protocol/inbox processing complete; mathematical work begins.
- `2026-08-18T11:22:43Z`: approximately 32-minute self-check; cumulative 343 minutes.
  Target remains the exact universal seven-row scope, and the present theorem
  is explicitly only a `PSL_2` family partial.  The even-vector and split-pair
  representations have produced checkable labelled-action arguments.  The
  nonsplit orthogonal representation remains productive but has reached the
  named extension lemma in section 4.  Alternatives are the two-step
  projective completion in section 7 and a leased exact `q=11` collision test;
  no unleased computation is authorized.  Continue hand analysis to the
  45-minute cap unless Lead/MathExpert redirects sooner.
- `2026-08-18T11:23:43Z`: processed Lead's `CONTINUE` decision; continued only
  on the odd nonsplit orthogonality gate, with the original cap unchanged.
- `2026-08-18T11:28:48Z`: research stop at the explicit finite-geometry gate.
  Newly elapsed active time is `38m27s`; cumulative active time is
  `349m27s`.  No computation was run and no compute lease was used.  State:
  `awaiting_lead`.

## Clean-context boundary

This run uses only the common/Lead controls, canonical scope, roster control record,
and the cycle-17 decision.  No earlier unreviewed findings or scratch artifacts were
read.  Every mathematical premise below is rederived in this run.

## 1. Inventory, automorphisms, and an exact uniform product formula

Write `q=p^f`.  The simple parameters are `q>=4`, excluding neither `4` nor
`9`; `q=2,3` are the only nonsimple parameters.

There is exactly one `L=PSL_2(q)`-class of involutions for every such `q`.

- If `q` is even, every involution is nonidentity unipotent.  Its centralizer
  has order `q`, hence
  `|D|=q^2-1`.
- If `q` is odd, an involution has a lift `A in SL_2(q)` with
  `tr(A)=0`, `det(A)=1`, and `A^2=-I`; the two lifts are `A,-A`.
  Trace-zero regular semisimple matrices form one `SL_2(q)` class (the
  determinant map on either the split or nonsplit torus centralizer is
  surjective), so their images form one class.  Put
  `epsilon=chi_q(-1)`.  The centralizer has order `q-epsilon`, and
  `|D|=q(q+epsilon)/2`.

Consequently the setwise stabilizer of `D` is all of `Aut(L)`.  For every
simple parameter, including `q=4,5,9`,

`Aut(PSL_2(q)) = PΓL_2(q)`.

Here the diagonal `PGL/PSL` factor is absent in even characteristic and has
order two in odd characteristic; the field factor has order `f`.  At `q=9`
this is the full order-`1440` automorphism group of `A_6`, not merely one of
its index-two overgroups.  At `q=4,5` it is the full `S_5` automorphism group
of `A_5`.

For odd `q`, choose trace-zero determinant-one lifts `A,B` of distinct
vertices and put `s=tr(AB)` (only `s^2` is independent of lift signs).  If
`lambda,lambda^{-1}` are the roots of

`X^2-sX+1`,

then the exact edge colour is

`|[AB]| = ord(lambda^2)`.

Thus:

- `s^2=4` gives the nontrivial unipotent colour `p`;
- `s^2-4` a nonzero square gives an order dividing `(q-1)/2`;
- `s^2-4` a nonsquare gives an order dividing `(q+1)/2`;
- `s=0` gives colour `2`;
- `s^2=1` gives colour `3` (also in characteristic three, where this is
  the unipotent case).

This is an exact formula, not merely a split/nonsplit fusion.

The resulting complete colour inventories are also explicit.  Distinct
involutions realize every listed nontrivial divisor:

- for even `q`: colour `2`, together with every `m>1` dividing `q-1` or
  `q+1`;
- for odd `q=1 mod 4`: every `m>1` dividing `(q-1)/2` or `(q+1)/2`, together
  with the unipotent colour `p`;
- for odd `q=3 mod 4`: every `m>1` dividing `(q-1)/2` or `(q+1)/2`, and no
  unipotent colour.

Existence follows inside the two torus normalizers: their inverting cosets
consist of the unique involution class, so a rotation of each divisor order is
the product of two class involutions.  In the split odd case, two affine
reflections supply the additional nonzero unipotent products.

## 2. Even characteristic: colour 3 alone recovers the labelled action

Let `V=F_q^2` with its determinant form `[ , ]`.  For `v!=0` set

`t_v(x)=x+[x,v]v`.

Because squaring is bijective on `F_q`, `v -> t_v` is a bijection
`V\{0} -> D`.  Direct multiplication gives

`tr(t_v t_w)=[v,w]^2`.

More explicitly, when `c=[v,w]!=0`, if `lambda` is either root of
`X^2+c^2X+1`, then `|t_vt_w|=ord(lambda)`; the root lies in a split or
nonsplit torus and the answer divides `q-1` or `q+1`, respectively.  When
`c=0` and `v!=w`, the answer is `2`.  This gives every exact product order in
the even-characteristic class.

For distinct vertices the product has order two exactly when `v,w` are
collinear.  More importantly,

`|t_vt_w|=3  <=>  [v,w]=1`.                         (E3)

Indeed a determinant-one characteristic-two matrix has order three exactly
when its trace is one, and `[v,w]^2=1` has the unique solution `[v,w]=1`.

Let `F` be any permutation of `V\{0}` preserving (E3).  Two distinct vectors
are collinear exactly when they have no common (E3)-neighbour: proportional
distinct vectors give two inconsistent linear equations, while independent
vectors give one unique solution.  Hence `F` permutes the one-dimensional
subspaces.

Compose with the unique element of `SL_2(q)` inducing the inverse permutation
on three selected image lines, so that `F` fixes the lines of `e`, `f`, and
`e+f`, where `[e,f]=1`.  Write

```
F(ae)=phi(a)e,                 F(bf)=psi(b)f,
F(a(e+xf))=rho_x(a)(e+h(x)f)  (x!=0).
```

The unique (E3)-matching between the first two fibres gives
`psi(a^{-1})=phi(a)^{-1}`.  Matching the `x`-fibre first with the `f`-fibre
and then with the `e`-fibre gives

`rho_x(a)=phi(a)`,
`phi(a)phi((ax)^{-1})h(x)=1`.

The fixed `x=1` fibre implies `phi(1)=1`,
`phi(a^{-1})=phi(a)^{-1}`; hence `h(x)=phi(x)` and
`phi(ax)=phi(a)phi(x)`.  Finally apply (E3) to the two slope fibres `x,y`:
using `ab(x+y)=1` gives

`phi(x+y)=phi(x)+phi(y)`.

After setting `phi(0)=0`, `phi` is a field automorphism.  Undoing the initial
normalization shows

`Aut_col(D)=SL_2(q) semidirect Gal(F_q/F_p)`

in this labelled `v -> t_v` action.  Conjugation by `SL_2(q)` sends `t_v` to
`t_{gv}`, and field automorphisms send `t_v` to `t_{v^sigma}`, so this is
exactly the restriction image of `PΓL_2(q)=Aut(L)`, not just a group-order
comparison.  The argument includes `q=4` without an exception.

## 3. Odd split case (`q = 1 mod 4`): colours `p` and `2`

Put `Omega=P^1(F_q)`.  Since `-1` is a square, a class involution is split,
and its two rational fixed points determine it uniquely.  Thus

`D <-> binom(Omega,2)`.

For two distinct vertices, their product has order `p` exactly when their
fixed-point pairs meet in one point.  In one direction, normalize the common
point to infinity: the two involutions are distinct affine reflections and
their product is a nonzero translation.  Conversely, if `ab` is unipotent,
then `a(ab)a=(ab)^{-1}`; the unique fixed point of `ab` is consequently fixed
by both `a` and `b`.

Therefore colour `p` is precisely the triangular graph on the two-subsets of
the `q+1` points.  Since `q+1>=6`, every automorphism of this relation is
induced by a unique `pi in Sym(Omega)`.

For disjoint fixed pairs, colour `2` is precisely harmonicity.  Normalize the
first pair to `{0,infinity}`: its involution is `z -> -z`; a distinct split
involution commutes with it exactly when it has fixed pair `{r,-r}`.  Hence
the induced `pi` preserves every harmonic quadruple.

For completeness, harmonic preservation forces semilinearity directly.
Normalize further so `pi` fixes `infinity,0,1`, and write its restriction as
`f:F_q->F_q`.  If `H(a,b;c)` denotes the harmonic conjugate of `c` relative
to `a,b`, then

`H(infinity,a;x)=2a-x`, and `H(1,-1;x)=x^{-1}`.

Preservation of the first identity yields `f(2a-x)=2f(a)-f(x)`, hence
additivity; preservation of the second yields
`f(x^{-1})=f(x)^{-1}`.  The identity

`x^2 = x-(x^{-1}+(1-x)^{-1})^{-1}`

(with the trivial exceptional inputs handled separately) then gives
preservation of squares, and polarization in odd characteristic gives
multiplicativity.  Thus `f` is a field automorphism and
`pi in PΓL_2(q)`.

It follows, again as equality of labelled permutation actions, that the full
product-order colour group equals the `Aut(L)` restriction image for every
`q=1 mod 4`.  This includes `q=5` (`A_5`) and `q=9` (`A_6`), so the two
alternating isomorphisms and the exceptional outer structure at `q=9` cause
no extra colour permutations.

## 4. Odd nonsplit case (`q = 3 mod 4`): exact reduction

Here `D` consists of nonsplit involutions and has size `q(q-1)/2`.  No product
of two distinct vertices is unipotent: if `g=ab` were unipotent then `a`
would invert its root group, but an inverting involution has projective
determinant class `-1`, which is not in `PSL_2(q)` in this congruence.

The two semisimple order domains are disjoint:

`gcd((q-1)/2,(q+1)/2)=1`.

Thus the exact colours intrinsically define the coarse relation

`a R_s b <=> |ab| divides (q-1)/2`,

equivalently, `ab` is split semisimple.  On `Omega`, every `a in D` is a
fixed-point-free projective involution and hence a perfect matching `M_a`.
For distinct `a,b`,

`a R_s b <=> M_a and M_b share one edge`.            (NS)

Indeed the fixed-point pair of the split element `ab` is swapped by both
involutions; conversely, sharing the pair `{x,y}` makes `ab` fix `x,y`.
For every two-subset `e={x,y}` define

`C_e={a in D: e in M_a}`.

Then `|C_e|=(q-1)/2`, every `C_e` is an `R_s`-clique, every vertex lies in
`(q+1)/2` such cliques, and every `R_s` edge lies in its unique geometrically
specified `C_e`.  Recovering these `C_e` intrinsically from the fused relation
would recover the projective-line matching design and reduce the remaining
case to the same harmonic/semilinear conclusion as in section 3.

### Independent audit of the first nonsplit parameter `q=7`

The exceptional isomorphism `PSL_2(7)=GL_3(2)` gives a short direct treatment
which does not use any earlier run.  Every involution is a transvection
`I+v phi` with `phi(v)=0`; because the field has two elements, these are exactly
the 21 incident point-line flags `(P,l)` of the Fano plane.

For two flags put
`alpha=phi(P')` and `beta=phi'(P)` in `F_2`.  Multiplication of the two rank-one
nilpotents gives the exact table

| `(alpha,beta)` | product order |
|---|---:|
| `(0,0)` | 2 |
| `(1,1)` | 3 |
| `(0,1)` or `(1,0)` | 4 |

(the equal-flag diagonal is omitted).  In particular the maximal colour-2
cliques are exactly the seven point-stars and seven line-stars, each of size
three.  Each colour-2 edge lies in one such triangle: mutual cross-incidence
in the Fano plane forces the third flag to have the common point or common
line.  Their 14-clique intersection graph is the point-line incidence graph
of the Fano plane.  Hence every colour permutation induces either an incidence
collineation or a point-line duality.  Conversely these are induced by inner
automorphisms or inverse-transpose.  The labelled group is therefore
`PGL_2(7)` of order `336`, the full restriction image.  This deals with the
only nonsplit parameter below 11.

### Remaining family lemma

In the orthogonal model `PSL_2(q)=PΩ_3(q)`, the vertices for `q=3 mod 4` are
one nonsingular point orbit `X` of `PG(2,q)`.  Colour 2 is orthogonality.
For `x,y in X`, the pole of the line `xy` lies in the opposite nonsingular
orbit precisely when `x R_s y`; the sets `C_e` above are the intersections
of those polar lines with `X`.

There is a useful strengthening: two distinct vertices have at most one
common colour-2 neighbour, namely the pole of their join when that pole lies
in `X`.  Consequently

`x R_s y <=> x,y have no common colour-2 neighbour`.

So the orthogonality graph alone already recovers the split/nonsplit fusion.
The family bottleneck can be stated without any arbitrary union of colours.

The exact unresolved gate is the following finite-geometry rigidity lemma.

> **NS rigidity gate.**  For every prime power `q=3 mod 4`, `q>=11`, every
> automorphism of the orthogonality graph induced on the nonsquare-type
> nonsingular points `X` of `PG(2,q)` extends uniquely to an element of
> `PΓO_3(q)`.

This statement is sufficient because colour 2 is one of the exact
product-order colours, and `PΓO_3(q)=PΓL_2(q)` in the labelled conjugation
action.  A promising reconstruction is to characterize the `C_e` as the
geometric cliques in the split graph and use orthogonality to select the
distinguished projective-line completion.  Each such clique has size
`(q-1)/2`, but it is not legitimate to assume that the split fusion is a
rank-three graph: for a nonincident vertex--clique pair, the intersection
count reduces in coordinates to a cubic character sum

`sum_r chi(r(r-1)(r-eta))` (`eta` nonsquare),

which can vary with `eta`.  Thus a strongly-regular/Delsarte shortcut would
silently discard orbital information.  At `q=7` the split fusion is the point
graph of `GQ(2,3)` and has many more automorphisms; the colour-2 polarity is
genuinely necessary, as the flag derivation above shows.  What is still
missing is a self-contained argument that the combined exact colours plus
orthogonality select the intended conic completion for every `q>=11`; group
order, a rank-three assumption, or finite sampling would not fill this gate.

## 5. Exceptional-parameter and outer-action audit

| `q` | status in this derivation | qualification |
|---:|---|---|
| 2, 3 | excluded | `PSL_2(q)` is not nonabelian simple |
| 4 | covered by section 2 | `PSL_2(4)=A_5`; field outer automorphism included |
| 5 | covered by section 3 | `PSL_2(5)=A_5`; diagonal `PGL/PSL` included |
| 7 | covered by the Fano-flag audit | `PSL_2(7)=GL_3(2)`; duality/inverse-transpose included |
| 8 | covered by section 2 | all field automorphisms included |
| 9 | covered by section 3 | `PSL_2(9)=A_6`; full exceptional outer group is `PΓL_2(9)` |

For every remaining even or `1 mod 4` parameter, the same arguments include
the entire field group and (when odd) the diagonal outer involution.  The
first unresolved parameter is `q=11`, and precisely the unresolved congruence
family is `q=3 mod 4`, `q>=11`.

## 6. Seven-row constraint-and-conclusion matrix

| constraint_id | role | required condition | candidate value / proof use | evidence | result |
|---|---|---|---|---|---|
| `21.52-forall-L-D` | admissibility | every admissible `(L,D)` | This cycle treats every `PSL_2(q)` pair, but closes only the even, split-odd, and `q=7` subfamilies | Sections 1--5 | **partial only** |
| `21.52-L-finite-nonabelian-simple` | admissibility | `L` finite nonabelian simple | `L=PSL_2(q)`, `q>=4`; `q=2,3` explicitly excluded | inventory in section 1 | pass for stated family |
| `21.52-D-single-involution-class` | admissibility | one class, all elements order 2 | the unique involution class; sizes `q^2-1` (even) and `q(q+chi(-1))/2` (odd) | lift/centralizer derivation in section 1 | pass |
| `21.52-Gamma-complete-on-D` | admissibility | all unordered distinct pairs | every pair is treated by the trace/eigenvalue formula | sections 1--2 | pass |
| `21.52-edge-colour-exact-product-order` | admissibility | colour is exactly `|ab|` | eigenvalue-order formulas and complete divisor inventories, with no conjugacy-class refinement substituted | sections 1--2 | pass |
| `21.52-tau-preserves-all-edge-colours` | admissibility | arbitrary exact-colour permutation `tau` | only consequences definable from exact colours are used (`R_3`, `p`, `2`, and common-neighbour counts) | sections 2--4 | pass as hypothesis |
| `21.52-tau-induced-by-AutL` | target conclusion | every `tau` lies in the labelled restriction image | equality obtained for even `q`, odd `q=1 mod 4`, and `q=7`; unknown for `q=3 mod 4`, `q>=11`, and untouched non-`PSL_2` simple groups | labelled action identifications in sections 2, 3, and the Fano audit | **partial / universal row unknown** |

`active_assignment_answered: no`.

## 7. Concrete next experiment on the unresolved gate

The projective completion route can be split into two falsifiable lemmas.

1. In the colour-2 graph let `F(x,y)` mean that `x,y` have no common
   colour-2 neighbour.  Classify, using only this graph, the geometric
   `(q-1)/2`-sets `C_e` among the `F`-cliques.  These are the traces on `X`
   of polar lines with opposite-type poles.  A proof must allow for and
   exclude nongeneric cliques; it cannot assume a rank-three fusion.
2. On the recovered block set, use the number (or full colour distribution)
   of orthogonal pairs in `C_e x C_f` to distinguish `e intersect f` from
   disjoint `e,f`.  Geometrically the former is the tangent/unipotent
   relation between the opposite-type poles.  Once the triangular graph on
   `binom(Omega,2)` is recovered, its stars recover `Omega`.

The second test is now an explicit one-variable character sum.  In coordinates
`Q(a,b,c)=a^2+bc`, normalize one opposite-type pole to `y=(1,0,0)` and write
the other as `z=(A,B,C)`.  Then

`C_y={(0,1,t): chi(t)=-1}`,

and the unique point of `z^perp` orthogonal to `(0,1,t)` is represented by

`w_t=(Bt-C, 2A, -2At)`.

Its type is determined by

`Q(w_t)=B^2t^2-2(BC+2A^2)t+C^2`.

The desired endpoint-sharing relation is exactly the degenerate case
`BC=0` (the two pole-lines meet on the conic).  Thus the residual calculation
must show that the full graph-definable type/colour count of these `w_t`
distinguishes `BC=0` from every `BC!=0`; merely bounding the cubic character
sum is not enough if two values collide.  In the degenerate case the elementary
linear/quadratic character sums give exactly `(q+1)/4` orthogonal pairs in
`C_y x C_z`; the unresolved issue is whether a nondegenerate parameter can
have the same coarse count (and, if so, whether the full colour vector still
separates it).

For reference, the count can be sharpened without a machine.  If `BC!=0`
and `A!=0`, choose `D^2=A^2+BC`.  The two roots of `Q(w_t)` are
`(A+D)^2/B^2` and `(A-D)^2/B^2`, hence are squares.  After square scaling,

`N(C_y,C_z)=(q+1+S(lambda))/4`,

where `S(lambda)=sum_u chi(u(u-1)(u-lambda))` and `lambda` is a non-one
square.  For `q=11`, the four possibilities `lambda=3,4,5,9` give by direct
Legendre-symbol addition `S=4,4,-4,-4`; the cross counts are therefore `4`
or `2`, while the tangent count is `3` (and the `A=0` orthogonal-pole case
has count `0`).  Thus this particular count does distinguish the tangent
relation at `q=11`.  In the family, however, `S(lambda)` is an elliptic-curve
trace and no argument here excludes `S(lambda)=0`; the `q=11` table cannot be
extrapolated.

An induced permutation of `Omega` then preserves the family of all matchings
`M_a`.  Since those involutions generate `PSL_2(q)`, it normalizes the natural
projective action, whose normalizer is `PΓL_2(q)`.  Failure of either lemma,
especially an extra block or a collapsed tangent count at `q=11`, would give
a sharply bounded counterexample target rather than justify extrapolation.

## Cycle outcome: `PARTIAL_RESULT`

Candidate labelled equality is obtained for the unique involution class of
`PSL_2(q)` whenever `q` is even, whenever `q=1 mod 4`, and for `q=7`.
The inventory and exact product-order formula cover every simple parameter.
The remaining `q=3 mod 4`, `q>=11` family is reduced to the explicit
orthogonality/projective-completion gates in sections 4 and 7.  The direct
`q=11` character table separates tangent block pairs, but block recovery and
the uniform elliptic-trace separation remain open.  This is an infinite-family
partial, not an answer to the universal all-simple-groups assignment.

`active_assignment_answered: no`.

---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/alternating-groups
  - project/kourovka
  - status/conjectured
---

# PARTIAL_RESULT: a fixed-degree triangular centralizer classifier for even matchings

## Active target

Scope: `21.52/involution-class-product-order-colouring`  
Assignment revision: 1  
Direction: proof  
Notebook target: the universal assertion for every finite nonabelian simple
`L` and every single involution class `D`.

This note proposes only the following infinite-family partial; it does **not**
answer the universal row.

> **Candidate family theorem.** Let `k>=2` be even and `n>=8k`.  Let `D_{n,k}`
> be the single class of cycle type `2^k 1^(n-2k)` in `A_n`.  Every permutation
> of `D_{n,k}` preserving the exact order of the product of every distinct pair
> is induced by conjugation by a permutation of the natural `n` points, hence by
> an automorphism of `A_n` stabilizing `D_{n,k}`.

The stable range is linear.  No value at another degree is used.  The key
colour-definable vector for a commuting pair is the two-coordinate fixed-degree
statistic

`T(x,y)=(U(x,y), C(x,y))`,

where `C` is the size of the closed common commuting neighbourhood and `U` is
the number of universal vertices in its induced commuting graph.  Its two
coordinates form a triangular classifier: `U` removes every square component
(apart from an explicitly handled `k=2` collision), and a coefficientwise
recurrence makes `C` strictly triangular in the remaining number `b` of
one-sided edges.  Thus it recovers exactly `c=0,b=1,a=k-1`, which is the pair
data needed below.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | use / value here | evidence | result |
|---|---|---|---|---|---|
| `21.52-forall-L-D` | admissibility | universal over admissible `(L,D)` | only the subfamily `(A_n,D_{n,k})`, even `k`, `n>=8k` is covered | theorem statement and proof below | partial only |
| `21.52-L-finite-nonabelian-simple` | admissibility | `L` finite nonabelian simple | `L=A_n`, and `n>=8k>=16` | standard simplicity of `A_n` for `n>=5` | pass in family |
| `21.52-D-single-involution-class` | admissibility | one class, all elements order 2 | even `k` makes type `2^k1^(n-2k)` even; the `S_n` class does not split in `A_n` because its type has even cycles | first paragraph of proof | pass in family |
| `21.52-Gamma-complete-on-D` | admissibility | all unordered distinct pairs | retained exactly | definitions below | pass in family |
| `21.52-edge-colour-exact-product-order` | admissibility | colour iff exact `|xy|` agrees | only exact order colours are used; commuting is the exact colour 2 | union-component lemma below | pass in family |
| `21.52-tau-preserves-all-edge-colours` | admissibility | `tau` preserves every edge colour | hypothesis of candidate theorem; it therefore preserves `T`, the recovered overlap relation, and all derived incidences | Steps 4--6 | pass in family |
| `21.52-tau-induced-by-AutL` | target conclusion | extension from `Stab_{Aut(L)}(D)` | the reconstructed point permutation acts by conjugation on `A_n` and on `D_{n,k}` | Step 6 | proved only for stated family; universal row unknown |

Explicitly excluded throughout: Problem 21.53; a union of involution classes;
the uncoloured complete graph; product-conjugacy-class colouring; and bounded
data presented as a universal proof.

## 1. Matchings and exact product orders

Identify an element of `D_{n,k}` with its set of `k` disjoint transposition
edges, i.e. a `k`-matching on the natural points.  Since `k` is even, it belongs
to `A_n`.  The familiar splitting criterion for symmetric-group classes says
that an `S_n` class splits in `A_n` only when all cycle lengths are distinct and
odd.  The present type has even cycles, so `D_{n,k}` is one `A_n` class.

For two matchings `x,y`, draw their edges in two colours.  Every nontrivial
component of their union is one of:

- a common doubled edge, contributing order `1` to `xy`;
- an alternating path on `r` vertices, contributing order `r`;
- an alternating cycle on `2r` vertices, contributing order `r`.

The cycles of `xy` on distinct components are disjoint, so `|xy|` is the lcm of
these contributions.  In particular, distinct `x,y` commute exactly when their
edge colour is `2`.  In that case the union consists only of common edges,
one-sided isolated edges, and alternating squares.

Write the commuting-pair parameters as follows:

- `a`: common edges;
- `b`: `x`-only edges (and also `b` `y`-only edges);
- `c`: alternating squares.

Then

`a+b+2c=k`,  and  `f=n-2k-2b`

points are fixed by both.  For `H=<x,y> congruent C_2^2`, its orbits are `a`
two-point orbits of the diagonal character, `b` two-point orbits of each of the
two other nonzero characters, `c` regular four-point orbits, and `f` fixed
points.

## 2. The exact common-centralizer coefficient

Let `K(x,y)=D_{n,k} intersect C_{S_n}(H)`.  In the coloured graph this is exactly
`{x,y}` together with the vertices joined by colour 2 to both endpoints.  Hence
`C(x,y):=|K(x,y)|` is colour-definable.

Use a variable `t` to record the number of transpositions in another matching.
For `m` isomorphic two-point `H`-orbits set

`F_m(t) = sum_{r+2s<=m} m!/[r!(m-r-2s)!s!] t^(r+2s)`.

Indeed, `r` orbits may be flipped internally.  The other `2s` selected orbits
are paired; there are two equivariant bijections for every paired pair, and
that factor cancels the usual `2^s` in the number of pairings.

For `f` fixed points set

`M_f(t) = sum_{j>=0} f!/[(f-2j)! 2^j j!] t^j`.

For `c` regular `H`-orbits set

`G_c(t) = sum_{r+2s<=c} c! 3^r 2^s/[r!(c-r-2s)!s!] t^(2r+4s)`.

Here an internally used regular orbit admits three nonidentity translations,
each of transposition weight 2; a paired pair of regular orbits admits four
equivariant bijections and has weight 4.  The orbit choices are independent,
so the exact fixed-degree formula is

`C(x,y) = [t^k] F_a(t) F_b(t)^2 G_c(t) M_f(t).`  `(1)`

This is a count inside the actual class `D_{n,k}`, not in another degree and not
in a hypothetical polynomial family.

## 3. The universal-vertex moment and the triangular gate

Inside the induced commuting graph on `K(x,y)`, let `U(x,y)` be the number of
vertices commuting with every member of `K(x,y)`.  This is the second
colour-definable coordinate.

Because `n>=8k`, every commuting pair has `f=n-2k-2b>=4k` common fixed points.
I claim that the universal vertices are exactly

`D_{n,k} intersect Z(C_{S_n}(H))`.  `(2)`

To see the nontrivial containment, let `w` be universal.  If its restriction to
the `f` fixed points has an edge `{p,q}`, choose a point `r` fixed by `w` and a
type-`k` matching on the fixed set containing `{p,r}`, with all other edges also
on points fixed by `w`.  The available pool has size at least `4k`, so this is
possible.  It centralizes `H` but not `w`, a contradiction.  Thus `w` is trivial
on the fixed set.

The nonfixed part of `C_{S_n}(H)` is generated by the following involutions:
an internal flip of a two-point orbit (weight 1), an equivariant swap of two
such orbits (weight 2), a translation of a regular orbit (weight 2), and an
equivariant swap of two regular orbits (weight 4).  The last kind can occur only
when `k>=4`.  Pad any such generator of weight `d` by a `(k-d)`-matching on the
common fixed set.  The result belongs to `K(x,y)`.  Since `w` is trivial on the
padding set, universality forces it to commute with the generator.  Hence it is
central.  The converse in (2) is immediate.

The centralizer decomposition is

`(C_2 wr S_a) x (C_2 wr S_b)^2 x (V_4 wr S_c) x S_f`.

Since `f>=3`, its central type-weight enumerator is

`Z_{a,b,c}(t) = (1+t^a)^[a>0] (1+t^b)^[2(b>0)]
                 (1+3t^(2c))^[c>0]`,

and

`U(x,y)=[t^k]Z_{a,b,c}(t)`.  `(3)`

For even `k>=4`, (3) gives

`U(x,y)=2  iff  c=0 and b != k/2`.  `(4)`

Indeed, if `c>0`, choosing any of the three diagonal regular translations
together with the required diagonal/one-sided central flips already gives at
least three weight-`k` elements.  If `c=0`, then `a+b=k`; the two choices are
the diagonal flip together with either one-sided flip, with one additional
choice exactly when `2b=k`.

It remains to distinguish `b=1` from the other values surviving (4).  Put

`P_b(t)=F_{k-b}(t)F_b(t)^2M_{n-2k-2b}(t)`.

The key fixed-degree triangular inequality is

`[t^k]P_1 > [t^k]P_2 > ... > [t^k]P_k`.  `(5)`

Here is a direct coefficient proof, not evaluation at other degrees.  Write
`A_j=M_{f,j}=f!/[(f-2j)!2^j j!]`.  The elementary recurrences are

`F_b=(1+t)F_{b-1}+2(b-1)t^2F_{b-2}`,

`M_{f+2,j}-M_{f,j}=(2f-2j+3)M_{f,j-1}`.  `(6)`

Coefficientwise, `F_{b-2}<=F_{b-1}`, so with
`R_b=1+t+2(b-1)t^2` we have `F_b<=R_bF_{b-1}`.  If `f>=4k`, then for
`1<=j<=k`

`M_{f,j-s}/M_{f,j-1} <= (1/(2k))^(s-1)` for `s=2,3,4`.

The coefficient of `t^j` in `R_b^2M_f` is

`A_j+2A_{j-1}+(4b-3)A_{j-2}+4(b-1)A_{j-3}+4(b-1)^2A_{j-4}`.

After subtracting `A_j` and dividing by `A_{j-1}`, the latter four terms are at
most

`2 + (4k)/(2k) + 4k/(2k)^2 + 4k^2/(2k)^3 < 5`,

whereas (6) gives `2f-2j+3 >= 6k+3`.  Consequently

`M_{f+2} > R_b^2M_f`

coefficientwise in every positive degree through `k`.  At the step from `b` to
`b-1`, `f=n-2k-2b>=n-4k>=4k`, and `F_{k-b+1}>=F_{k-b}`.  Multiplication by
polynomials with nonnegative coefficients now gives (5), strictly in degree
`k`.

Thus, for even `k>=4`, the relation

`R_2(x,y) : |xy|=2, U(x,y)=2, and C(x,y) is maximal among
             commuting pairs with U=2`  `(7)`

is exactly

`c=0,b=1,a=k-1`:

`x,y` share `k-1` edges and their two remaining edges are disjoint.

For `k=2`, the target and the single-square type both have `U=3`.  They are the
only `U=3` commuting types.  Writing `f=n-6`, their common-centralizer counts are

`C_target=[t^2](1+t)^3M_f`,

`C_square=[t^2](1+3t^2)M_{f+2}`,

and

`C_square-C_target=(2f-4)M_{f,1}>0`.

Hence for `k=2`, define `R_2` as colour-2 pairs with `U=3` and **minimal** `C`
among those pairs.  This is again exactly the `k-1`-core/disjoint-residual type.

This completes the required fixed-`n` triangular recovery of the internal pair
data needed for reconstruction.

## 4. Recover the whole `(k-1)`-core adjacency

Define another colour-invariant relation by

`R_3(x,y) : |xy|=3 and there exists z with R_2(x,z) and R_2(y,z)`.  `(8)`

If `x=C union {e}` and `y=C union {f}` share a `(k-1)`-matching `C`, and `e,f`
meet in one point, choose an edge `g` disjoint from `C,e,f`.  There are at least
two unused points because `n>=8k`.  Then `z=C union {g}` witnesses (8).

Conversely, suppose `z` witnesses (8).  Each of `x,y` is obtained from `z` by
deleting one edge and inserting a disjoint edge.  If they delete different
edges `g,h` of `z`, then (say) `h` is an `x`-only edge disjoint from both
`y`-only edges: it is disjoint from `g` because `z` is a matching and from the
new edge of `y` by the definition of `R_2`.  Thus the union of `x,y` has a
one-sided isolated edge and `|xy|` is even, contradicting `|xy|=3`.  They delete
the same edge, so they share the other `k-1` edges.  Exact colour 3 then says
their two new edges meet in one point.

Therefore

`R=R_2 union R_3`

is precisely the graph on `k`-matchings in which two vertices are adjacent iff
they share exactly `k-1` transposition edges.

## 5. Reconstruct every matching layer and the natural points

Let `J_j(n)` denote the graph on `j`-matchings with adjacency `|X intersect Y|=j-1`.
We have intrinsically recovered `J_k(n)`.

For a `(j-1)`-matching `Q`, the star

`S_Q={X: X is a j-matching and Q subset X}`

is a clique of size `binom(n-2j+2,2)`.  The elementary Johnson-clique argument
says that every clique is either contained in such a star or in the `j+1`
different `j`-subsets of one `(j+1)`-matching.  Indeed, after fixing two members
with common `(j-1)`-core, a third member either contains that core or is obtained
by dropping one core edge and taking both exceptional edges; in the latter case
every further member lies in the same `(j+1)`-set.  Since `n>=8k` and `j<=k`,

`binom(n-2j+2,2)>j+1`.

Thus the largest maximal cliques of `J_j(n)` are exactly the stars and recover
the `(j-1)`-matchings together with containment incidence.

It remains to recover their overlap graph, including pairs whose exceptional
edges meet.  For distinct stars `S_Q,S_Q'`, let `E(Q,Q')` be the number of graph
edges of `J_j(n)` with one endpoint in each star.  If
`|Q intersect Q'|=j-2`, then every edge `g` disjoint from the support of
`Q union Q'` gives adjacent vertices `Q union {g}` and `Q' union {g}`.  Hence

`E(Q,Q') >= binom(n-2j,2)>4`.

If `|Q intersect Q'|=j-3`, an adjacent cross-pair must add one of the two edges
of `Q'-Q` on one side and one of the two edges of `Q-Q'` on the other, giving at
most four choices.  If the intersection is smaller, no cross-pair can acquire
the required `j-1` common edges.  Therefore

`E(Q,Q')>4  iff  |Q intersect Q'|=j-2`.  `(9)`

Equation (9) reconstructs `J_{j-1}(n)`.  Descending from `j=k` to `j=2`
recovers the individual transposition edges and all containment incidences.
Two recovered edges of the complete graph on the natural points are disjoint
iff some recovered 2-matching contains both.  Thus the disjointness graph
`KG(n,2)` is recovered.  Its complement is the line graph of `K_n`; for `n>=5`
its largest maximal cliques are the `n` point-stars of size `n-1` (the only
other maximal cliques are triangles).  This recovers the natural `n` points.

## 6. Extension

Any exact-colour automorphism preserves colour 2, the finite vector `(U,C)`,
the extremal definitions (7), the witness definition (8), and hence `J_k(n)`.
Steps 5 and (9) force it to induce a permutation `sigma` of the reconstructed
natural points.  Containment through every recovered layer shows that on each
`k`-matching it acts exactly by applying `sigma` to all transposition edges.
This is conjugation by `sigma`.

Because `A_n` is normal in `S_n`, conjugation by `sigma` restricts to an
automorphism of `A_n`, and it stabilizes the cycle-type class `D_{n,k}`.  This is
the typed extension required by the active scope for the stated family.

## Exact computation used

No heavy computation and no leased slot were used.  The small exact script
`scratch/commuting_codegrees.py` implements formula (1) with integer
coefficients and was used only as a discovery/sanity probe.  It is not evidence
for the stable range; the range `n>=8k` follows from inequalities (2)--(9).

## What this does not establish

- It does not answer Problem 21.52 for arbitrary finite simple groups or for all
  involution classes of alternating groups.
- It does not cover odd `k` (those permutations are not in `A_n`) or the degrees
  `2k<=n<8k`.
- It does not assert that `(U,C)` recovers every commuting-pair orbit; it recovers
  exactly the coefficients `c=0,b=1,a=k-1` needed for core adjacency.
- The family proof is new and unreviewed; its status is `conjectured` pending an
  independent Validator reconstruction.

## How this could be wrong

1. The universal-vertex set in (2) could be larger than the center if the padded
   involutions fail to generate one of the wreath-product factors; every listed
   generator and its transposition weight should be checked independently.
2. The centre weight coefficient (3), especially the coincident-weight case
   `b=k/2`, could omit a central element.
3. The coefficientwise step (5) could have an index error in the `F_b` or
   `M_{f+2}` recurrence; Validator should rederive both from orbit pairings.
4. The maximal-clique dichotomy or the cross-star threshold (9) could admit an
   extra matching-specific configuration not present in the ordinary Johnson
   argument.


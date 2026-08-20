---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/alternating-groups
  - topic/coloured-graphs
  - project/kourovka
  - status/conjectured
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
outcome: PARTIAL_RESULT
---

# Six-transposition boundary: exact partial result

## Precise result

Let `D_n` be the conjugacy class of type `2^6 1^(n-12)` in `A_n`, identified
with the six-edge matchings of `K_n`.

1. For every `n>=15`, every permutation of `D_n` preserving every exact product
   order is induced by a unique permutation of the `n` natural points. Hence its
   group is exactly the natural `S_n=Aut(A_n)` restriction image.
2. For `n=13,14`, the exact colouring intrinsically defines the graph joining
   two six-matchings exactly when they share five edges.
3. For `n=12`, the exact colouring intrinsically defines the flip graph joining
   perfect matchings that share four edges.

Items 2--3 do **not** yet identify the full action. The three degrees
`n=12,13,14` remain open in this lane; there is no counterexample and no universal
Problem 21.52 claim.

## Exact pair classification and colour-definable statistics

For colours `i,j`, put
`N_ij(x,y)=#{z in D_n: |xz|=i and |yz|=j}` (with graph endpoints automatically
excluded whenever one order would be `1`). These numbers are invariant under
every exact-colour automorphism.

### Commuting pairs

For distinct commuting `x,y`, the `V_4=<x,y>`-orbits give exactly:

- `a` common two-point orbits, on which `x=y`;
- `b` `x`-only and `b` `y`-only two-point orbits;
- `c` regular four-point orbits.

Thus `a+b+2c=6`, and the common fixed-point count is `f=n-12-2b`.
Define

```
E_f(u) = sum_{j=0}^6 (f)_(2j)/(2^j j!) u^j,
B_m(u) = sum_r m!/((m-2r)! r!) u^(2r)(1+u)^(m-2r),
R_m(u) = sum_r m! 2^r/((m-2r)! r!) u^(4r)(1+3u^2)^(m-2r).
```

The number of six-transposition elements commuting with both is exactly

```
C_2(a,b,c;n)=[u^6] E_(n-12-2b)(u) B_a(u) B_b(u)^2 R_c(u).
```

This follows by enumerating involutions in the centralizer factors on fixed
points, on the three kinds of two-point `V_4`-sets, and on the regular
four-point sets. Therefore `N_22=C_2-2`.

Exact degree-12 polynomial comparison shows that `(5,1,0)` has a different value
from every other feasible commuting type at every integer `n>=14`. For each
difference polynomial, the checker expands at a stated threshold between `19`
and `28`; every nonzero shifted coefficient has one sign, while every smaller
feasible integer is checked exactly. At `n=14`, an independent enumeration of all
`945945` six-matchings gives:

| `(a,b,c)` | `(4,0,1)` | `(2,0,2)` | `(0,0,3)` | `(5,1,0)` | `(3,1,1)` | `(1,1,2)` |
|---|---:|---:|---:|---:|---:|---:|
| `N_22` | 157 | 63 | 61 | **285** | 67 | 37 |

At `n=12`, the three feasible values of `C_2` are `75,39,63`, so the
four-common flip type `(4,0,1)` is also intrinsic.

### Product-order-three pairs

Here `<x,y> is S_3`. Its transitive orbits have degrees `1,2,3,6`; write `a`
for common edges (degree 2), `p` for alternating two-edge paths (degree 3), and
`q` for alternating six-cycles (regular degree 6). Then
`a+p+3q=6` and `f=n-12-p`. With

```
P_p(u)=sum_r p!/((p-2r)!2^r r!) u^(3r),
Q_q(u)=sum_r q!3^r/((q-2r)!r!) u^(6r)(1+3u^3)^(q-2r),
```

the exact common-colour-2 count is

```
N_22(x,y)=[u^6]E_(n-12-p)(u) B_a(u) P_p(u) Q_q(u).
```

The target type `(a,p,q)=(5,1,0)` means five common edges and two exceptional
edges meeting in one point. Polynomial differences isolate it for every
`n>=15`. The only first-moment collision is with `(2,1,1)` at `n=13,14`.
Complete enumeration of every feasible `S_n` pair orbit and every vertex gives:

| `n` | target `(N_22,N_33)` | other feasible signatures |
|---:|---:|---|
| 13 | **`(0,241)`** | `(21,178)`, `(0,58)`, `(15,106)` |
| 14 | **`(0,1312)`** | `(28,328)`, `(48,574)`, `(0,268)`, `(3,190)`, `(15,106)` |

Thus the target is intrinsic in both exceptional degrees.

Combining the commuting and order-3 target relations recovers adjacency
`|x cap y|=5` for every `n>=13`: exceptional edges are either disjoint (order 2)
or meet once (order 3). At `n=13` only the latter is feasible.

## Stable reconstruction for every `n>=15`

Write `J_r(n)` for the graph on `r`-matchings, adjacent when they share `r-1`
edges, and `H_r(n)` for its subgraph in which the two exceptional edges are
disjoint.

The maximal cliques of `J_r(n)` are exactly:

- core stars `S_A={M:A subset M}`, of size `binom(n-2r+2,2)`, for an
  `(r-1)`-matching `A`;
- tops consisting of the `r+1` submatchings of an `(r+1)`-matching.

For `n>=15` and `2<=r<=6`, the core stars are strictly larger, so they are
intrinsic. An automorphism of `J_r` therefore acts on `(r-1)`-matchings. Two
such cores `A,B` are adjacent in `H_(r-1)` exactly when their core stars meet in
one `r`-matching, so `H_(r-1)` is intrinsic.

For nonadjacent `s`-matchings `A,B`, direct set analysis gives

```
|N_H(A) cap N_H(B)| = binom(n-2s-1,2)
```

when they share `s-1` edges and their exceptional edges meet. If they share
`s-2` edges, the count is at most `4` (choose one of two exceptional edges from
each); with smaller intersection it is zero. Since for `n>=15` and `s<=5`
`binom(n-2s-1,2)>=6`, one recovers

```
J_s = H_s union {nonedges with more than four common H_s-neighbours}.
```

Starting from the colour-defined `J_6`, this descends through every matching
layer to `J_2`. Its core stars recover the edges of `K_n`, and two recovered
edges occur together in a two-matching exactly when they are disjoint. Hence the
edge-disjointness graph `KG(n,2)` is recovered. Its complement is `L(K_n)`;
the maximal `(n-1)`-cliques are precisely the edge-stars at natural points, so
the points and their action are recovered. Incidence at every descent step shows
the original permutation on six-matchings is exactly the induced point action,
not merely a group of the same order. Conversely `S_n` preserves every product
order by conjugation.

## Constraint-and-conclusion audit

| constraint_id | role | use/result |
|---|---|---|
| `21.52-forall-L-D` | admissibility | **not covered universally**; only this alternating-family partial |
| `21.52-L-finite-nonabelian-simple` | admissibility | `A_n` is finite nonabelian simple for every `n>=12` |
| `21.52-D-single-involution-class` | admissibility | type `2^6 1^(n-12)` is one `A_n` class and consists of involutions |
| `21.52-Gamma-complete-on-D` | admissibility | all unordered distinct pairs are used |
| `21.52-edge-colour-exact-product-order` | admissibility | only exact `|xy|` and its colour-definable counts are used |
| `21.52-tau-preserves-all-edge-colours` | admissibility | every derived relation is invariant under such `tau` |
| `21.52-tau-induced-by-AutL` | target | established for this family at `n>=15`; open here for `n=12,13,14`, and universal row remains open |

## Reproducibility and limitations

All jobs were bespoke exact integer computations under 60 seconds; no compute
lease was needed. Script SHA-256 values:

- `commuting_centralizer_counts.py`:
  `0176221c2b38025dbb5b2fa539203aed4051b25c5a08fc6cfb680b275f1fac7e`
- `order3_centralizer_counts.py`:
  `463ba0aabbdfe7f13f5a91cc5dcd43fdc603b9513be09d976a9132f999ec19a6`
- `n14_bruteforce_centralizers.py`:
  `37dacd91ab8ca7e98c64f59527be538f33b5d800236aa2fb1eab0a2284ec2aad`
- `n13_n14_order3_pair_arrays.py`:
  `56e64e33193ecb53c985d0579215e44fb56b7431e44530ef4da6ca097abcf16d`

The pair-array checker exhausts `135135` vertices at `n=13` and `945945` at
`n=14`, classifies every feasible order-3 orbit, and records hashes of the full
arrays. These computations certify only the stated finite pair statistics. They
do not compute the full colour automorphism groups. The missing small-degree
residue argument is a genuine gap, not evidence of a counterexample.

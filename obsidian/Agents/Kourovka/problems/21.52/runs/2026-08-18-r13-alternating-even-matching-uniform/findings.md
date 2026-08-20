---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/alternating-groups
  - topic/matching-graphs
  - project/kourovka
  - status/conjectured
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
direction: proof
cycle: 13
outcome: PARTIAL_RESULT
---

# Candidate stable-range theorem for every even matching size

## Active target

Scope: `21.52/involution-class-product-order-colouring`, revision 1.

The universal source target quantifies over every finite nonabelian simple group
and every one of its involution classes.  This note treats only the alternating-
group family

\[
 L=A_n,\qquad
 D_{n,k}=\{M:\ M\text{ has cycle type }2^k1^{n-2k}\},
 \qquad k\ge2\text{ even}.
\]

It is therefore an infinite-family partial, not an answer to the universal
Kourovka question.

## Candidate theorem

Put

\[
 E_k={4k\choose2},\qquad
 B_k=\sum_{j=1}^{k}{E_k\choose j},\qquad
 N(k)=4kB_k+6k.
\]

For every even `k>=2` and every `n>=N(k)`, every permutation of `D_{n,k}`
preserving the exact order `|MN|` for every pair of distinct matchings is the
restriction of conjugation by an element of `S_n`.  In particular it is induced
by a setwise-stabilizing automorphism of `A_n`.

The range is deliberately crude but explicit and uniform in every even `k`.
The argument below uses only the colour 2 relation *after* assuming preservation
of the full exact colouring; it makes no universal claim about Problem 21.53.

## 1. Independently derived product-order rule

View two `k`-matchings `M,N` as a two-coloured multigraph, retaining a doubled
edge when a transposition is common.  Every nontrivial component is alternating.
Tracing the permutation `MN` along a component gives:

| component of `M union N` | cycle structure of `MN` there | contribution to `|MN|` |
|---|---|---|
| doubled common edge | two fixed points | `1` |
| alternating cycle with `2r` edges, `r>=2` | two `r`-cycles | `r` |
| alternating path with `2r` edges | one `(2r+1)`-cycle | `2r+1` |
| alternating path with `2r-1` edges | one `2r`-cycle | `2r` |

Thus `|MN|` is the least common multiple of all component contributions.  In
particular, for distinct involutions, colour 2 is exactly commutation.

This also explains the initially promising `k=6` observation: colour 11 forces
one alternating 10-edge path and one common transposition.  A local sample showed
that naive triangle-label recovery fails, so the proof below replaces it by a
uniform common-centralizer statistic.

## 2. A colour-definable statistic recovers support union and a one-edge invariant

For distinct `M,N in D_{n,k}`, let

\[
 c_2(M,N)=\#\{Z\in D_{n,k}\setminus\{M,N\}: |MZ|=|NZ|=2\}
\]

and define

\[
 K(M,N)=c_2(M,N)+2\,\mathbf 1_{|MN|=2}.
\]

This is determined by the exact coloured graph.  Since distinct commuting
involutions have product order 2, `K(M,N)` is exactly the number of `k`-matching
involutions `Z` commuting with both `M` and `N`, now including `M,N` themselves
when appropriate.

Let

\[
 U=\operatorname{supp}(M)\cup\operatorname{supp}(N),\quad
 u=|U|,\quad x=n-u,
\]

and let

\[
 \mu_s(x)=\frac{x!}{(x-2s)!2^ss!}
\]

be the number of `s`-matchings on an `x`-set (`mu_0=1`).  If `Z` commutes with
`M`, then `Z` preserves `supp(M)` setwise; similarly it preserves `supp(N)`, hence
it preserves `U` and its complement.  Therefore no edge of `Z` crosses from `U`
to its complement.  If `a_j(M,N)` is the number of `j`-matchings on `U` commuting
with both restrictions, then

\[
 K(M,N)=\sum_{j=0}^{k}a_j(M,N)\mu_{k-j}(x),\qquad a_0=1. \tag{1}
\]

As `u<=4k`, the crude uniform bound

\[
 \sum_{j=1}^{k}a_j(M,N)
 \le \sum_{j=1}^{k}{\binom{4k}{2}\choose j}=B_k \tag{2}
\]

holds: choose the `j` edges from all possible edges on a `4k`-set and ignore both
the matching and commutation restrictions.

The coefficient `a_1` has a simple intrinsic meaning.  Write

\[
 b(M,N)=a_1(M,N).
\]

A transposition commutes with a matching involution exactly when it is one of
that matching's edges or is disjoint from its support.  Since its endpoints lie
in `U`, it follows that

\[
 b(M,N)=q(M,N)+i_M(M,N)+i_N(M,N), \tag{3}
\]

where `q` is the number of common transpositions, `i_M` is the number of edges of
`M` wholly outside `supp(N)`, and `i_N` is defined symmetrically.

### Numerical separation at one fixed degree

Formula (1) is not being compared across hypothetical values of `n`; it separates
the invariants at the one fixed degree because the chosen range makes consecutive
falling-factorial scales disjoint.

For `x>=n-4k>=4kB_k+2k`, the sequence `mu_s(x)` is increasing for `s<=k`.  Also

\[
 \mu_k(x+1)-\mu_k(x)
 =x\mu_{k-1}(x-1)
 =(x-2k+2)\mu_{k-1}(x)>B_k\mu_{k-1}(x). \tag{4}
\]

Hence, using (1)--(2), every possible `K` value with complement size `x+1` is
larger than every possible `K` value with complement size `x`.  Thus `K(M,N)`
recovers `x`, equivalently `u`.

For fixed `u` and `x`,

\[
 \frac{\mu_{k-1}(x)}{\mu_{k-2}(x)}
 =\frac{(x-2k+4)(x-2k+3)}{2(k-1)}>2B_k. \tag{5}
\]

All terms of (1) after the `a_1` term have total coefficient at most `B_k` and
scale at most `mu_{k-2}(x)`.  Consequently the intervals for successive integer
values of `b=a_1` are disjoint.  Thus the single colour-definable number `K(M,N)`
recovers the ordered pair

\[
 (u(M,N),b(M,N)). \tag{6}
\]

## 3. Recovering `(k-1)`-edge cores

For distinct `M,N`, the relation

\[
 |M\cap N|=k-1 \tag{7}
\]

is equivalent to the following colour-definable disjunction:

\[
 (u,b)=(2k+1,k-1)\quad\text{or}\quad(u,b)=(2k+2,k+1). \tag{8}
\]

Indeed, if the two noncommon edges meet in one point, their support union has
size `2k+1`; neither side has an edge wholly outside the other support, so (3)
gives `b=k-1`.  If those edges are disjoint, the support union has size `2k+2`
and each noncommon edge is wholly outside the other support, giving `b=k+1`.

Conversely, if `u=2k+1`, each support has only one point outside the other, hence
`i_M=i_N=0`; `b=k-1` forces `q=k-1`.  If `u=2k+2`, each support has two outside
points, so `i_M,i_N<=1` and `q<=k-1`; `b=k+1` forces
`q=k-1` and `i_M=i_N=1`.  This proves the equivalence.

Therefore every exact-colour automorphism acts on the graph `G_k(n)` whose
vertices are `k`-matchings and whose adjacent vertices share exactly `k-1` edges.

## 4. Reconstructing edge stars and point stars

For `2<=r<=k`, let `G_r(n)` be the analogous graph on `r`-matchings.  In the
ordinary Johnson graph, a clique of `r`-subsets either has a common `(r-1)`-subset
or has size at most `r+1`: after fixing adjacent
`C+{a}` and `C+{b}`, any member not containing `C` lies in `C+{a,b}` and forces
all further members into that `(r+1)`-set.  Restricting to matchings preserves
this upper bound.

For every `(r-1)`-matching `F`, however,

\[
 \mathcal C_F=\{F\cup\{e\}:e\text{ is disjoint from }\operatorname{supp}(F)\}
\]

is a clique of size

\[
 {n-2r+2\choose2}>r+1. \tag{9}
\]

Thus the maximum cliques of `G_r(n)` are exactly the full core stars
`mathcal C_F`.  An automorphism of `G_r` therefore permutes `(r-1)`-matchings.

It remains to recover their adjacency even when their two differing edges meet.
For distinct `(r-1)`-matchings `F,G`, count `G_r`-edges with one endpoint in
`mathcal C_F` and the other in `mathcal C_G`.

- If `|F cap G|=r-2`, every edge `h` disjoint from
  `supp(F) union supp(G)` gives the adjacent pair `F+h,G+h`.  There are more
  than four such `h` in the stated range.
- If `|F cap G|=r-3`, an adjacent pair must add to each core one of the two edges
  missing from it but present in the other; there are at most `2*2=4` choices.
- If `|F cap G|<=r-4`, adding one edge on each side cannot raise the intersection
  to `r-1`, so there are none.

Hence “more than four cross-edges between the two maximum cliques” intrinsically
reconstructs `G_{r-1}(n)`.  Iterating from `r=k` down to `r=2` recovers the set of
individual transpositions and all matching-containment incidences.

For two recovered transpositions `e,f`, the two core stars in `G_2` intersect
exactly when `e,f` are disjoint (their unique common vertex is the 2-matching
`{e,f}`).  Thus the disjointness graph `KG(n,2)` is recovered.  Its maximum
independent sets are exactly the point stars

\[
 \mathcal S_v=\{\{v,w\}:w\ne v\},
\]

of size `n-1`: an intersecting edge family not having a common point is contained
in a triangle and has size at most 3.  Since `n>=5`, point stars are the unique
maximum independent sets.  Their permutation gives some `sigma in S_n`, and
each recovered edge `{v,w}` maps to `{sigma(v),sigma(w)}`.  Compatibility with
the core-star incidence at every level then forces the original permutation to
send every matching `M` to `sigma(M)` edge by edge.

## 5. Alternating-group and automorphism audit

- `k` is even, so a product of `k` transpositions is even and lies in `A_n`.
- The `S_n` class does not split in `A_n`: a constituent transposition is an odd
  element of the `S_n` centralizer.  Hence `D_{n,k}` is one `A_n` conjugacy class,
  not a union of classes.
- The range has `n>=5`, so `A_n` is finite nonabelian simple.
- It also has `n>6`, avoiding the exceptional outer automorphisms of `A_6`.
  Thus `Aut(A_n)=S_n`, and conjugation by the reconstructed `sigma` stabilizes
  `D_{n,k}` setwise.
- The source graph is the complete graph on this one class, and the hypothesis is
  preservation of every *exact* product-order colour.  The proof uses the exact
  colour-2 relation and colour-definable common-neighbour counts that this full
  hypothesis necessarily preserves.

## Constraint-and-conclusion matrix

| constraint_id | role | use in this partial | evidence/result |
|---|---|---|---|
| `21.52-forall-L-D` | admissibility | Universal quantifier is **not** discharged; only the stated alternating family is covered. | `partial only` |
| `21.52-L-finite-nonabelian-simple` | admissibility | `L=A_n`, and the stable range has `n>=5`. | `pass for family` |
| `21.52-D-single-involution-class` | admissibility | `k` even puts type `2^k1^{n-2k}` in `A_n`; an odd centralizing transposition prevents class splitting. | `pass for family` |
| `21.52-Gamma-complete-on-D` | admissibility | All unordered distinct pairs of matchings are used. | `pass for family` |
| `21.52-edge-colour-exact-product-order` | admissibility | Component table computes exact `|MN|`; the statistic uses exact colour 2. | `pass for family` |
| `21.52-tau-preserves-all-edge-colours` | admissibility | Assumed exactly as in the source; it preserves colour 2 and `K`. | `pass for family` |
| `21.52-tau-induced-by-AutL` | target conclusion | Reconstruction gives conjugation by `sigma in S_n=Aut(A_n)` in the stated stable range. | `candidate argument for family; universal row open` |

## What this does not establish

- It does not answer the universal scope for all finite nonabelian simple groups.
- It does not cover any `n<N(k)`; the bound is intentionally enormous.
- It does not use or certify earlier `k=2` or `k=4` work.
- It does not assert the universal two-colour statement in Problem 21.53.
- It is a fresh candidate hand proof awaiting independent reconstruction; its
  status remains `conjectured`.

## How this could be wrong

1. The numerical interval argument could hide an off-by-one error in the matching
   difference identity or in the bound on lower coefficients.
2. The centralizer decomposition requires that commuting permutations preserve
   each support set; this is valid because support is the complement of the fixed
   set, but Validator should check the converse splitting in (1).
3. The maximum-clique classification is inherited from the Johnson graph; the
   matching restriction must not create a larger non-core clique (the ambient
   `r+1` bound is intended to rule this out).
4. The downward reconstruction uses the strict `>4` cross-edge threshold; all
   ways in which two added edges can contribute to the set intersection should be
   re-enumerated independently.


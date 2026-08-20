---
title: "Constituent-independent exclusion of {19,6,8;1,1,12}"
problem: 21.90
scope_id: 21.90/diameter-three-distance-graphs
assignment_revision: 3
outcome: PARTIAL_RESULT
validation: pending
active_assignment_answered: no
---

# Result

There is no distance-regular graph with intersection array

\[
 \{19,6,8;1,1,12\}.
\]

The contradiction uses only the frozen symmetric zero-one matrix identities and
therefore covers every hypothetical `srg(210,76,26,28)` distance-3 constituent.
It does not depend on the existence, uniqueness, or automorphisms of such a
constituent.

## Spectral-multiplicity gate

Assume the necessary matrices exist. Put `D=I+B`, where `B=A_3`, and
`M=I+A_1`. They satisfy

\[
 D^2=49I+28J,\qquad M(D+7I)=8J,
\]

\[
 M^2=7I+13M+J-D. \tag{1}
\]

Both are symmetric, `M` is zero-one with diagonal one and row sum 20, and
`D\mathbf1=77\mathbf1`. Equation (1) makes `D` a polynomial in `M` and `J`,
so the matrices commute. On `\mathbf1^\perp`, if `m` and `d` are their paired
eigenvalues, then

\[
 d=7+13m-m^2,\qquad d^2=49.
\]

Before using the mixed equation, the possible nonprincipal eigenvalues of `M`
are therefore `0,13,14,-1`, with `d=7` for `m=0,13` and `d=-7` for
`m=14,-1`.

Write their multiplicities as `n_0,n_{13},n_{14},n_{-1}`. Since
`M\mathbf1=20\mathbf1`, `tr(M)=210`, and every diagonal entry of `M^2` is the
row weight 20, the multiplicities obey

\[
 n_0+n_{13}+n_{14}+n_{-1}=209,
\]

\[
 13n_{13}+14n_{14}-n_{-1}=190,
\]

\[
 169n_{13}+196n_{14}+n_{-1}=3800.
\]

Equivalently `13n_{13}+15n_{14}=285`. The two nonnegative integral branches
are exactly

| branch | `n_0` | `n_13` | `n_14` | `n_-1` |
|---|---:|---:|---:|---:|
| A | 99 | 15 | 6 | 89 |
| B | 114 | 0 | 19 | 76 |

On `\mathbf1^\perp`, however, the mixed equation gives
`m(d+7)=0`. An eigenvalue `m=13` has `d=7` and violates this equation.
Consequently branch A is impossible and branch B is forced:

\[
 \operatorname{Spec}(M)=\{20^1,14^{19},0^{114},(-1)^{76}\}.
\]

This spectral gate is compatible; the contradiction is the following cheaper
integral/local-design gate.

## Local clique-partition contradiction

From `M(D+7I)=8J` and `D=I+B`,

\[
 MB=8(J-M). \tag{2}
\]

For a vertex `u`, let `C_u` be the support of row `u` of `M`; it has 20 points
and contains `u`. If `v\in C_u`, the `(u,v)` entry of (2) is zero. Since all
summands in `(MB)_{uv}` are nonnegative zero-one products, `B` has no edge from
`v` to any point of `C_u`. Thus every `C_u` is a coclique in `B`.

Let `N_u=C_u\setminus\{u\}`, the 19 vertices adjacent to `u` in the relation
`A_1=M-I`. For `v\in N_u`, equation (1) has off-diagonal entry

\[
 (M^2)_{uv}=13M_{uv}+1-B_{uv}=14.
\]

The intersection `C_u\cap C_v` contains `u` and `v`; its other 12 points are
exactly the common `A_1`-neighbours of `u` and `v`. Hence the local graph
induced by `A_1` on `N_u` is 12-regular.

Now take two distinct nonadjacent vertices `v,w` of this local graph. They both
belong to the `B`-coclique `C_u`, so `B_{vw}=0`, while `M_{vw}=0`. Equation (1)
therefore gives `(M^2)_{vw}=1`.

But `u\in C_v\cap C_w`, so this is their only common point. In particular,
nonadjacent vertices of the local graph have no common neighbour inside it.

Every connected component of a graph with that property is complete: a
shortest path of length at least two would have two nonadjacent vertices at
distance two sharing its middle vertex. Therefore the 12-regular local graph
is a disjoint union of copies of `K_13`. This is impossible on 19 vertices,
because `13` does not divide `19`.

Equivalently, `c_2=1` forces every local graph to be a union of cliques of size
`a_1+1`; here `a_1+1=13` does not divide `k=19`. The matrix proof above shows
explicitly that no hidden constituent assumption enters.

## Scope and confidence

This is an exact constituent-independent elimination of one bounded arithmetic
row, pending independent validation. Modular-rank and Smith-form tests are
unnecessary because the integral row-support system already contradicts a
19-point local graph. No catalogue, SAT instance, or graph search was run.

It does not identify the next unexcluded row, establish completeness of the
finite parameter box, or answer the full revision-3 existence question.
`active_assignment_answered: no`.

---
title: "Candidate partial — exclusion of {17,8,6;1,2,12} by a local root lattice"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/distance-regular-graphs
  - topic/root-systems
  - project/kourovka
  - status/conjectured
problem: "21.90"
scope_id: 21.90/diameter-three-distance-graphs
assignment_revision: 3
outcome: PARTIAL_RESULT
active_assignment_answered: no
---

# Candidate array-level exclusion

## Active target

Scope: `21.90/diameter-three-distance-graphs`  
Assignment revision: 3  
Target: an actual Q-polynomial distance-regular graph of diameter 3 whose
distance-2 and distance-3 graphs are nontrivial strongly regular graphs in the
source-operational sense.

## Candidate partial claim

There is no distance-regular graph with intersection array

\[
\{17,8,6;1,2,12\}.
\]

Consequently, conditional on the reviewed Type-II(ii) specialization, its exact
formal tuple `(x,w,u)=(1,2,2)` cannot be realized. This excludes only that array;
it does not answer the active existential scope.

## Scope-impact matrix

| constraint_id | role | required condition | use in this partial | result for active scope |
|---|---|---|---|---|
| `21.90-exists-Gamma` | admissibility | one graph satisfies every row | no graph is supplied; one putative array is excluded | unresolved |
| `21.90-diameter-3` | admissibility | diameter exactly 3 | assumed only for a hypothetical graph with the displayed diameter-3 array | unresolved globally |
| `21.90-Q-polynomial-distance-regular` | admissibility | Q-polynomial distance-regular | the contradiction uses only distance-regularity, so it excludes the array a fortiori in the Q-polynomial class | unresolved globally |
| `21.90-distance-graph-definition` | admissibility | adjacency at exact distance | not needed for the local contradiction | unresolved globally |
| `21.90-Gamma2-strongly-regular` | admissibility | nontrivial strong regularity of `Gamma_2` | not needed for the local contradiction | unresolved globally |
| `21.90-Gamma3-strongly-regular` | admissibility | nontrivial strong regularity of `Gamma_3` | not needed for the local contradiction | unresolved globally |
| `21.90-existence-conclusion` | target conclusion | at least one target graph exists | neither established nor refuted | unproved |

## Lemma 1 — the exact local eigenvalue interval

Assume for contradiction that `Gamma` is distance-regular with the displayed
array. Put `k=b_0=17`. Its intersection numbers include

\[
a_1=k-b_1-c_1=17-8-1=8.
\]

For a vertex `x`, let `L` be the graph induced by `Gamma` on `Gamma(x)`, with
adjacency matrix `A`. Then `L` has 17 vertices and is 8-regular. It is connected:
every component of an 8-regular simple graph has at least 9 vertices, whereas two
components would require at least 18 vertices.

The intersection matrix is

\[
B=\begin{pmatrix}
0&17&0&0\\
1&8&8&0\\
0&2&9&6\\
0&0&12&5
\end{pmatrix},
\]

and direct tridiagonal expansion gives

\[
\det(zI-B)=(z-17)(z-9)(z+1)(z+3).
\]

Thus the nonprincipal eigenvalues of `Gamma` are `9,-1,-3`.

Here is a derivation of the local bound rather than an appeal to a numerical
interlacing assertion. Let `theta != k` be a global eigenvalue, let `E_theta` be
its primitive idempotent, and let `(sigma_i)` be its cosine sequence, normalized
by

\[
(E_\theta)_{yz}=\frac{m_\theta}{v}\sigma_{d(y,z)},\qquad
\sigma_0=1,\qquad \sigma_1=\frac{\theta}{k}.
\]

For `y,z` in `Gamma(x)`, their distance in `Gamma` is 0, 1, or 2, and distance 1
is exactly adjacency in `L`. Therefore the principal submatrix of `E_theta` on
`Gamma(x)` is the positive scalar `m_theta/v` times

\[
(1-\sigma_2)I+(\sigma_1-\sigma_2)A+\sigma_2J. \tag{1}
\]

If `f` is a nonprincipal local eigenvector, so that `Af=eta f` and `f` is
orthogonal to the all-one vector, positive semidefiniteness of (1) gives

\[
(1-\sigma_2)+(\sigma_1-\sigma_2)\eta\geq0. \tag{2}
\]

The distance-regular cosine recurrence at distance 1 is

\[
1+a_1\frac{\theta}{k}+b_1\sigma_2
=\theta\frac{\theta}{k}.
\]

Using `a_1=k-b_1-1`, this gives the two factorizations

\[
1-\sigma_2=\frac{(k-\theta)(\theta+b_1+1)}{kb_1},\qquad
\sigma_1-\sigma_2=\frac{(k-\theta)(\theta+1)}{kb_1}. \tag{3}
\]

Since `theta<k`, substitution of (3) into (2) yields the standard local
inequality in its sign-safe form

\[
b_1+(\theta+1)(\eta+1)\geq0. \tag{4}
\]

For `theta=9` and `theta=-3`, respectively, (4) becomes

\[
\eta\geq-1-\frac8{10}=-\frac95,
\qquad
\eta\leq-1-\frac8{-2}=3. \tag{5}
\]

Thus every nonprincipal eigenvalue of `L` lies in `[-9/5,3]`.

## Lemma 2 — positive-definite simply-laced rank-17 reduction

Let

\[
G=2I+A.
\]

On the all-one vector its eigenvalue is `10`; on its orthogonal complement its
eigenvalues are `2+eta>=1/5` by (5). Hence `G` is positive definite and has rank
17.

Realize `G` as the Gram matrix of linearly independent vectors
`alpha_1,...,alpha_17`. They have squared norm 2, and distinct vectors have inner
product 1 exactly when the corresponding vertices of `L` are adjacent, and 0
otherwise. Let

\[
\Lambda=\sum_i\mathbb Z\alpha_i,
\qquad
R=\{r\in\Lambda:(r,r)=2\}.
\]

The lattice is integral and positive definite, so `R` is finite. For `r` in `R`,
the reflection

\[
s_r(z)=z-(z,r)r
\]

preserves `Lambda`, because all lattice inner products are integral, and therefore
permutes `R`. Thus `R` is a reduced crystallographic root system, all of whose
roots have the same squared length 2; it is simply laced. It spans rank 17 because
it contains the basis vectors `alpha_i`.

The nonorthogonality graph of these generators is `L`, which is connected. Hence
all generators lie in one irreducible component of `R`; since they span, `R` is
irreducible. The classification of irreducible simply-laced crystallographic root
systems gives

\[
A_n,\ D_n,\ E_6,\ E_7,\ E_8.
\]

At rank 17 the complete list is therefore `A_17` and `D_17`.

## Lemma 3 — contradiction in type `A_17`

Use the standard realization

\[
A_{17}=\{\mathord\pm(e_p-e_q):1\leq p<q\leq18\}.
\]

Associate to each selected root `alpha_i` its two-element support, regarded as an
edge of a graph `H` on the 18 coordinate positions. Two selected roots cannot have
the same support: the only root directions on one support are equal or opposite,
which would give off-diagonal inner product 2 or -2 instead of 0 or 1. Thus `H` is
simple.

Two distinct supports are disjoint exactly when their roots are orthogonal. If
they share one coordinate, their inner product is `+1` or `-1`; the latter is
forbidden by `G`. Consequently

\[
L=\mathcal L(H), \tag{6}
\]

the ordinary line graph of `H`.

The 17 root vectors are independent. A cycle in `H` would give the usual signed
sum of oriented incidence vectors equal to zero, so `H` is a forest. Connectedness
of `L` puts all 17 edges in one component; hence their support graph is a tree with
17 edges (and necessarily 18 vertices).

For every edge `pq` of this tree, (6) and 8-regularity give

\[
8=\deg_L(pq)=\deg_H(p)+\deg_H(q)-2,
\quad\text{so}\quad
\deg_H(p)+\deg_H(q)=10. \tag{7}
\]

Choose a leaf `p`. Its neighbor `q` has degree 9 by (7). Every other neighbor of
`q` then has degree 1, again by (7), so connectedness forces
`H=K_{1,9}`. That graph has 9 edges, contradicting the 17 selected roots.

## Lemma 4 — contradiction in type `D_17`

Use the standard realization

\[
D_{17}=\{\mathord\pm e_p\mathord\pm e_q:1\leq p<q\leq17\}.
\]

Again associate to each selected root its two-element support, now allowing the
support graph `H` initially to be a multigraph. The 17 roots are the columns of an
invertible `17` by `17` signed incidence matrix. Hence every coordinate is used.
Connectedness of `L` makes `H` connected, and with 17 vertices and 17 edges `H` is
unicyclic (in the multigraph sense).

There is one exceptional support issue to remove before calling `L` a line graph.
At most two independent roots can have the same support. If two do, they are
orthogonal, and after coordinate sign switches and possibly exchanging `p,q` they
have the form

\[
\alpha=e_p+e_q,\qquad \beta=e_p-e_q. \tag{8}
\]

No third selected root can be incident with `q`: its inner products with `alpha`
and `beta` at `q` would have opposite signs, one equal to `-1`, contrary to the
off-diagonal entries of `G`. At `p`, the two signs in (8) agree. Thus every other
root incident with `p` is adjacent in `L` to both `alpha` and `beta`, while these
two are not adjacent to each other. Their degree in `L` is therefore
`deg_H(p)-2`. Regularity would force `deg_H(p)=10`. But then any third edge at
`p` is adjacent to all other nine edges incident with `p`, so its degree in `L`
is at least 9, contradicting 8-regularity. Hence no repeated support occurs.

Now `H` is simple. Any two incident support edges share exactly one coordinate,
so their inner product is `+1` (the alternative `-1` is forbidden). At each
coordinate all incident signs are therefore equal; switching coordinate signs
makes every selected root `e_p+e_q`. It follows that

\[
L=\mathcal L(H). \tag{9}
\]

The `0/1` incidence matrix of a connected unicyclic graph is singular when its
unique cycle is even: alternating coefficients around the cycle give a column
dependence. Since our columns are independent, the unique cycle is odd. (Leaf
elimination also shows that an odd unicyclic incidence matrix has determinant
of absolute value 2.)

Equation (9) and 8-regularity again give

\[
\deg_H(p)+\deg_H(q)=10 \tag{10}
\]

on every edge. Degrees alternate between `d` and `10-d` around any path. Going
around the odd cycle forces `d=5` on the cycle; connectedness and (10) then force
every vertex of `H` to have degree 5. But `H` has 17 vertices and 17 edges, so

\[
\sum_p\deg_H(p)=34,
\]

not `17*5=85`. This is a contradiction.

## Candidate conclusion

Both possible irreducible rank-17 simply-laced root-system types are impossible.
Therefore the assumed distance-regular graph with array
`{17,8,6;1,2,12}` cannot exist, subject to independent Validator review.

## What this does not establish

- It does not produce a graph satisfying the revision-3 target.
- It does not exclude any Type-II(ii) tuple other than `(1,2,2)`.
- It does not show that the reviewed Type-II(ii) formulas exhaust all possible
  target graphs, nor does it touch Type III or the Taylor branch.
- It does not settle Kourovka 21.90.

## How this could be wrong

1. The primitive-idempotent restriction or cosine recurrence could have been
   normalized incorrectly; Validator should reconstruct equations (1)--(4).
2. The passage from the integral positive-definite Gram matrix to the complete
   simply-laced root system could hide a reducibility or crystallographic gap;
   Lemma 2 records both points explicitly.
3. In type `D`, roots with the same two-coordinate support do not form an ordinary
   line graph. Lemma 4 treats that parallel-support case separately; it is the
   most delicate combinatorial step.
4. This array-level obstruction could be improperly promoted to the source-family
   classification or the active existential question; the scope matrix forbids
   that promotion.

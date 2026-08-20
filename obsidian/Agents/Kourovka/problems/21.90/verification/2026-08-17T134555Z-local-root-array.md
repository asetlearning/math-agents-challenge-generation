---
title: "Verification — Kourovka 21.90 — local-root exclusion of one array"
problem: "21.90"
scope_id: 21.90/diameter-three-distance-graphs
scope_record: Agents/Kourovka/scopes/21.90-diameter-three-distance-graphs.json
assignment_revision: 3
claim: "No distance-regular graph has intersection array {17,8,6;1,2,12}."
claimant: Problem-21.90
target_statement: "Does there exist a Q-polynomial distance-regular graph Gamma of diameter 3 such that Gamma_2 and Gamma_3 are nontrivial strongly regular graphs under the revision-3 source-operational convention?"
excluded_scopes: ["none; the submitted result excludes only one formal Type-II(ii) array and does not answer the active scope"]
target_object: "An actual Q-polynomial distance-regular graph satisfying every revision-3 constraint"
witness_object: "The class of hypothetical distance-regular graphs with intersection array {17,8,6;1,2,12}"
witness_equals_target: false
citation: "standard classification of irreducible reduced simply-laced crystallographic root systems; no external source used in this no-browse audit"
verification_method: "independent line-by-line hand proof"
tools_used: ["pdftotext 24.02.0", "rendered PDF visual inspection"]
scope_answered: ["exact one-array partial: nonexistence of a distance-regular graph with array {17,8,6;1,2,12}"]
scope_not_answered: ["21.90/diameter-three-distance-graphs", "all other Type-II(ii) arrays", "Type III", "Taylor branch"]
active_assignment_answered: no
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/distance-regular-graphs, topic/root-systems, project/kourovka, status/conjectured]
---

# Verification — Kourovka 21.90 — local-root exclusion of one array

## The claim

The exact claim is that no distance-regular graph realizes

\[
\{17,8,6;1,2,12\}.
\]

This would exclude the one formal Type-II(ii) tuple `(x,w,u)=(1,2,2)`.  It does
not assert that the Type-II(ii) parameterization is complete, and it does not
answer the revision-3 existence question.

## Scope, revision, and clause matrix

The visually rendered Notebook page 177 asks for an actual Q-polynomial
distance-regular graph of diameter 3 whose second and third distance graphs are
strongly regular.  Canonical revision 3 supplies the controlling nontrivial
three-eigenvalue convention.

| source clause | active? | answered by this claim? |
|---|---:|---:|
| `Gamma_i` has the same vertices and adjacency exactly at distance `i` | yes | no |
| existence of a diameter-3 Q-polynomial distance-regular `Gamma` with both required distance graphs strongly regular | yes | no; one possible intersection array is excluded |

The exact one-array theorem is narrower than the source target.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | submitted object/evidence | result for active scope |
|---|---|---|---|---|
| `21.90-exists-Gamma` | admissibility | one graph satisfies every row | no graph is supplied | unresolved |
| `21.90-diameter-3` | admissibility | diameter exactly 3 | hypothetical graph with the displayed diameter-3 array | conditional only |
| `21.90-Q-polynomial-distance-regular` | admissibility | Q-polynomial distance-regular | the contradiction assumes only distance-regularity | unresolved globally |
| `21.90-distance-graph-definition` | admissibility | exact distance relations | not used | unresolved globally |
| `21.90-Gamma2-strongly-regular` | admissibility | nontrivial SRG | not used | unresolved globally |
| `21.90-Gamma3-strongly-regular` | admissibility | nontrivial SRG | not used | unresolved globally |
| `21.90-existence-conclusion` | target conclusion | at least one target graph exists | neither established nor refuted | unproved |

No revision-3 `claim-checks/*.json` accompanies the partial.  The only present
claim check is the superseded revision-2 cube record.  This independently blocks
promotion of the package as a current full-scope claim.

`active_assignment_answered: no`.

## Target versus witness

The source target is an actual graph satisfying every revision-3 row.  The object
of the partial is the entire hypothetical class of distance-regular graphs with
one fixed array.  The proof is target-faithful for that exact array: it derives a
contradiction from distance-regular consequences of the array itself, with no
finite quotient, sampled graph, or constructed-by-assumption witness.  But the
one-array class is strictly narrower than the active source target, so
`witness_equals_target: false` for the active assignment.

## Subclaims and what each method proves

| subclaim | method | what a pass proves | what it does not prove |
|---|---|---|---|
| global and local spectral bounds | intersection matrix, cosine recurrence, primitive-idempotent positivity | every hypothetical local graph has spectrum in the stated interval | realizability of another array |
| rank-17 root reduction | positive-definite integral lattice | the 17 generators lie in one irreducible simply-laced crystallographic root system | which type without classification |
| completeness of types | ADE classification | only `A_17` and `D_17` occur at rank 17 | anything about noncrystallographic systems, which cannot arise here |
| `A_17` contradiction | support tree and line-graph degree formula | no `A_17` realization of this Gram matrix | the `D_17` case |
| `D_17` contradiction | signed unicyclic support multigraph, separately with and without parallel supports | no `D_17` realization of this Gram matrix | the active existential question |
| witness is active target | scope/object audit | fails | any full-scope conclusion |

## Independent reconstruction

### 1. Global eigenvalues and the local interval

Assume that a distance-regular graph `Gamma` has the displayed array and put
`k=17`.  Its remaining intersection numbers are

\[
a_1=8,\qquad a_2=9,\qquad a_3=5.
\]

For a fixed vertex `x`, the local graph `L` on `Gamma(x)` is therefore
8-regular on 17 vertices.  It is connected: every component of an 8-regular
simple graph has at least 9 vertices, so two components would require at least
18 vertices.

The intersection matrix is

\[
B=\begin{pmatrix}
0&17&0&0\\
1&8&8&0\\
0&2&9&6\\
0&0&12&5
\end{pmatrix}.
\]

The tridiagonal determinant recurrence gives

\[
\det(zI-B)=z^4-22z^3+52z^2+534z+459
=(z-17)(z-9)(z+1)(z+3).
\]

Thus the nonprincipal global eigenvalues include `9` and `-3`.

Let `theta != 17` be a global eigenvalue, and normalize its cosine sequence by
`sigma_0=1`, `sigma_1=theta/17`.  On `Gamma(x)`, the corresponding primitive-
idempotent principal submatrix is a positive scalar times

\[
(1-\sigma_2)I+(\sigma_1-\sigma_2)A+\sigma_2J. \tag{1}
\]

If `Af=eta f` with `f` perpendicular to the all-one vector, positivity of (1)
gives

\[
(1-\sigma_2)+(\sigma_1-\sigma_2)\eta\geq0. \tag{2}
\]

The distance-one cosine recurrence is

\[
1+8\frac{\theta}{17}+8\sigma_2
=\theta\frac{\theta}{17}.
\]

More generally, with `b_1=8`, it rearranges to

\[
1-\sigma_2=\frac{(17-\theta)(\theta+9)}{136},\qquad
\sigma_1-\sigma_2=\frac{(17-\theta)(\theta+1)}{136}. \tag{3}
\]

Because `theta<17`, substituting (3) into (2) and dividing only by a positive
factor gives the sign-safe inequality

\[
8+(\theta+1)(\eta+1)\geq0. \tag{4}
\]

At `theta=9`, (4) gives `eta >= -9/5`; at `theta=-3`, it gives
`eta <= 3`.  Hence every nonprincipal local eigenvalue lies in
`[-9/5,3]`.

### 2. Positive-definite irreducible rank-17 root system

Let `G=2I+A`.  It has eigenvalue `10` on the all-one vector and eigenvalues
`2+eta >= 1/5` on its orthogonal complement.  Thus `G` is positive definite
and has rank 17.

Choose vectors `alpha_1,...,alpha_17` with Gram matrix `G`.  Positivity makes
them a basis of their 17-dimensional real span.  Their squared norms are 2,
and distinct inner products are exactly 0 or 1.  In the integral positive-
definite lattice

\[
\Lambda=\sum_i\mathbb Z\alpha_i,
\]

let `R` be the set of all norm-two vectors.  It is finite.  For `r in R`,

\[
s_r(z)=z-(z,r)r
\]

preserves `Lambda`, since all lattice inner products are integral, and it
permutes `R`.  Thus `R` is a reduced crystallographic root system.  Every root
has squared length 2, so it is simply laced, and it spans rank 17 because it
contains the `alpha_i`.

Root-system components are mutually orthogonal.  The nonorthogonality graph on
the generators is precisely the connected local graph `L`, so all generators
lie in one component.  Since they span the full space, `R` is irreducible.
The complete irreducible simply-laced list is

\[
A_n,\ D_n,\ E_6,\ E_7,\ E_8.
\]

At rank 17 this leaves exactly `A_17` and `D_17`.

### 3. Type `A_17`

In the standard realization, every root is `+/- (e_p-e_q)` on 18 coordinate
positions.  Record its two-coordinate support as an edge of a graph `H`.  No
support repeats: the two root directions on one support are equal or opposite,
giving inner product `2` or `-2`, never an allowed off-diagonal entry of `G`.

Distinct roots are orthogonal exactly when their supports are disjoint.  Incident
supports have inner product `+1` because `-1` is forbidden.  Therefore
`L` is the ordinary line graph of `H`.

A cycle of support edges gives the usual signed dependence among their oriented
incidence vectors.  Since the 17 roots are independent, `H` is a forest.
Connectedness of `L` puts all 17 edges in one component, so `H` is a tree with
17 edges and 18 vertices.  For every edge `pq`, 8-regularity of its line graph
gives

\[
\deg_H(p)+\deg_H(q)-2=8,
\quad\text{hence}\quad
\deg_H(p)+\deg_H(q)=10. \tag{5}
\]

If `p` is a leaf, its neighbor `q` has degree 9.  Equation (5) makes every other
neighbor of `q` a leaf.  Connectedness would then make `H=K_{1,9}`, with only
9 edges, contradicting its 17 edges.

### 4. Type `D_17`: repeated supports

In the standard realization, every root is `+/- e_p +/- e_q` on 17 coordinate
positions.  Make a support multigraph `H`, initially permitting parallel edges.
The 17 root columns form an invertible 17-by-17 signed incidence matrix, so every
coordinate is used.  If `H` had more than one edge component, roots in distinct
components would be orthogonal and `L` would be disconnected.  Thus `H` is
connected.  It has 17 vertices and 17 edges, hence cyclomatic number one: it is
unicyclic as a multigraph.

At most two independent roots have one support.  If two do, their inner product
must be zero; after coordinate sign switches and relabeling their endpoints they
are

\[
\alpha=e_p+e_q,\qquad \beta=e_p-e_q. \tag{6}
\]

A third root on a different support incident with `q` would have inner products
`+1` and `-1` with `alpha,beta` in some order, which is forbidden.  Every other
root incident with `p` must have coefficient `+1` there and is adjacent in `L`
to both `alpha` and `beta`.  Since `alpha,beta` are mutually orthogonal, each
has local degree

\[
\deg_H(p)-2.
\]

Regularity forces `deg_H(p)=10`.

Here the multigraph count is essential: the parallel pair in (6) is already a
2-cycle, and `H` is unicyclic.  Therefore there is no second parallel pair
anywhere.  Any one of the eight further edges at `p` consequently has a distinct
support and shares `p`, with positive sign, with each of the other nine edges at
`p`.  Its degree in `L` is at least 9, contradicting 8-regularity.  Thus repeated
supports are impossible.

### 5. Type `D_17`: simple supports and signs

Now `H` is simple.  Two incident support edges share exactly one coordinate, so
their root inner product is `+1` rather than the forbidden `-1`.  Consequently,
at every coordinate all incident root coefficients have one common sign.
Switching coordinate signs makes every selected root `e_p+e_q`.  Hence `L` is
the ordinary line graph of `H`.

The resulting 0/1 incidence matrix is invertible.  If the unique cycle of `H`
were even, alternating coefficients around it would give a column dependence.
Thus the cycle is odd.  Line-graph regularity again gives

\[
\deg_H(p)+\deg_H(q)=10 \tag{7}
\]

on each edge.  Degrees alternate between `d` and `10-d` along a path.  Going
around the odd cycle forces every cycle degree to equal 5, and propagation along
every attached tree forces every vertex degree to equal 5.  This is impossible:
`H` has 17 vertices and 17 edges, so its degree sum is 34, not 85.

Both complete root-system alternatives therefore contradict the hypothetical
local graph.  No distance-regular graph has the displayed array.

## Circularity audit

There is no finite surrogate and no object built to satisfy the desired
conclusion.  The Gram matrix is forced by the local graph of a hypothetical
distance-regular graph, positivity is forced by primitive-idempotent
positive semidefiniteness, and the support contradictions range over both
complete crystallographic possibilities.  The argument is a contradiction from
necessary consequences of the fixed array, not a necessary-condition pass being
mistaken for realizability.

## Evidence

Triage note:
`Agents/Kourovka/problems/21.90/verification/2026-08-17T134411Z-local-root-array-triage.md`.

The source statement was also checked visually in
`Agents/Kourovka/problems/21.90/scratch/source-page-177.png`.

Commands and output, verbatim:

```text
$ source _meta/agents/Kourovka/paths.env
$ printf '%s\n' '--- tool probe ---'
$ command -v gap || true
$ command -v sage || true
$ command -v python3 || true
$ command -v magma || true
$ dpkg-query -W -f='${Package} ${Version}\n' gap-core 2>/dev/null || true
$ python3 --version
$ pdftotext -v 2>&1 | sed -n '1p'
--- tool probe ---
/usr/bin/gap
/usr/bin/python3
gap-core 4.12.1-2build2
Python 3.12.3
pdftotext version 24.02.0
```

No GAP call was made; under the common protocol every GAP call would require a
heavy-compute lease and none was needed.

```text
$ pdftotext -f 177 -l 177 -layout "$KOUROVKA_PDF" - | sed -n '/21\.90\./,/21\.91\./p' | sed '$d'
21.90. Let Γ be a graph of diameter d. For i ∈ {1, 2, . . . , d}, let Γi be the graph on
the same vertex set as Γ with vertices u, w adjacent in Γi if and only if dΓ (u, w) = i.
Does there exist a Q-polynomial distance-regular graph Γ of diameter 3 such that Γ2
and Γ3 are strongly regular?                                              A. A. Makhnëv

```

```text
$ find Agents/Kourovka/problems/21.90/claim-checks -maxdepth 1 -type f -name '*r3*' -printf '%f\n' | sort
```

The last command has empty output.

## Verdict

**Exact one-array mathematical verdict: VALID.**  The local eigenvalue
substitution, positive-definite rank-17 irreducible root reduction, completeness
of `A_17/D_17`, and both support-graph contradictions all survive independent
reconstruction.  In the repeated-support `D_17` case, the submitted proof's
implicit safeguard is valid only because the first parallel pair is the unique
multigraph cycle; stated explicitly above, it rules out a second parallel pair
and closes the degree count.

**Protocol status: `status/conjectured`.**  The missing revision-3 claim-check
prevents higher promotion, and this note is attached to the broader active scope
rather than to a separate atomic one-array scope.

**Active scope: not answered.**

## Why this verdict

Every mathematical link needed for the fixed-array contradiction is exact and
target-faithful at that narrow level.  The ADE list is exhaustive because the
lattice construction proves crystallographic, reduced, simply laced,
irreducible, and rank 17 before classification is invoked.  The `D_17` sign and
parallel-support cases do not leave an unexamined configuration.

The result nevertheless removes only one formal parameter row.  It cannot be
promoted into existence or universal nonexistence for Kourovka 21.90.

## What is NOT established

- No graph satisfying the revision-3 target is constructed.
- Nonexistence for the revision-3 target is not proved.
- No Type-II(ii) tuple other than `(1,2,2)` is excluded by this argument.
- Completeness or literature provenance of the Type-II(ii) parameterization is
  not established here.
- Type III, the Taylor branch, and all arrays outside the displayed row are
  untouched.

## What would upgrade it

For higher certification of the one-array partial, supply a clean revision-3
claim-completeness record and route the exact theorem as an explicitly bounded
partial claim; human review is additionally required before `status/proven`.
Answering the active scope still requires either one fully certified target graph
or a nonexistence proof covering every possible branch, not merely this array.

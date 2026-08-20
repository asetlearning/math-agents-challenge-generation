---
title: "Verification — Kourovka 21.90 — order-210 local-clique obstruction"
problem: "21.90"
scope_id: 21.90/diameter-three-distance-graphs
scope_record: Agents/Kourovka/scopes/21.90-diameter-three-distance-graphs.json
assignment_revision: 3
claim: "No distance-regular graph has intersection array {19,6,8;1,1,12}."
claimant: Problem-21.90
target_statement: "Does there exist a Q-polynomial distance-regular graph Gamma of diameter 3 such that its distance-2 graph Gamma_2 and distance-3 graph Gamma_3 are strongly regular?"
excluded_scopes: ["none"]
target_object: "Every Q-polynomial distance-regular graph of diameter 3 whose distance-2 and distance-3 graphs are nontrivial strongly regular graphs"
witness_object: "An arbitrary hypothetical distance-regular graph with the single intersection array {19,6,8;1,1,12}; no concrete graph or catalogue constituent is used"
witness_equals_target: false
citation: "none; direct distance-matrix and local-graph proof"
verification_method: "line-by-line hand proof plus an exact bounded Python arithmetic checker"
tools_used: ["rendered source PDF page 177", "Python 3.12.3", "GAP 4.12.1 availability probe only", "Poppler pdftotext 24.02.0"]
scope_answered: ["the single intersection array {19,6,8;1,1,12} is eliminated"]
scope_not_answered: ["all other intersection arrays", "completeness of any bounded parameter enumeration", "21.90/diameter-three-distance-graphs"]
active_assignment_answered: no
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/distance-regular-graphs, project/kourovka, status/conjectured]
---

# Verification — Kourovka 21.90

## The claim

The submitted bounded theorem is correct as a hand argument:

> No distance-regular graph has intersection array
> \(\{19,6,8;1,1,12\}\).

The decisive proof is constituent-independent.  It derives all matrices from the
four distance relations of a hypothetical graph and obtains a contradiction in
one 19-vertex local graph.  It never assumes that an explicit
`srg(210,76,26,28)` has been constructed.

Certification remains `status/conjectured` until the required human-review gate.
This pass is a checked strict partial theorem, not a solution of Problem 21.90.

## Scope, revision, and clause matrix

The canonical scope is revision `3` of
`21.90/diameter-three-distance-graphs`.  PDF page 177 was extracted and visually
checked against the rendered statement.

| source clause | active? | what this proof answers | what remains |
|---|---:|---|---|
| `Gamma_i` has the same vertices as `Gamma` and adjacency exactly at distance `i` | yes | uses precisely the four distance matrices `A_0,...,A_3` | no definitional ambiguity in the bounded proof |
| Existence of a Q-polynomial diameter-3 distance-regular `Gamma` with `Gamma_2,Gamma_3` strongly regular | yes | excludes one possible intersection array, even without Q-polynomiality | every other possible array and the existential answer |

Thus

`active_assignment_answered: no`.

No `claim-checks/*.json` accompanied either routed request.  The claimant labelled
the artifact `PARTIAL_RESULT`, not a whole-scope `CLAIM`.  All canonical rows are
nevertheless reconstructed below; the absent completeness file is not silently
treated as a clean whole-scope gate.

## Constraint-and-conclusion matrix

| constraint_id | role | independent proof use / candidate value | result |
|---|---|---|---|
| `21.90-exists-Gamma` | admissibility | assumes a graph only for contradiction and only in the one-array subfamily | partial only |
| `21.90-diameter-3` | admissibility | the array gives relations `A_0,A_1,A_2,A_3`, all used with the diameter-3 recurrence | pass for bounded family |
| `21.90-Q-polynomial-distance-regular` | admissibility | distance-regularity is used; Q-polynomiality is not, so the nonexistence conclusion is stronger on this array | pass as a valid strengthening for bounded family |
| `21.90-distance-graph-definition` | admissibility | `A_1=M-I`, `B=A_3`, and the remaining off-diagonal relation is `A_2` | pass for bounded family |
| `21.90-Gamma2-strongly-regular` | admissibility | not assumed or needed | not answered globally |
| `21.90-Gamma3-strongly-regular` | admissibility | `B=A_3` is proved abstractly to have parameters `(210,76,26,28)` if the hypothetical graph exists | pass for bounded family |
| `21.90-existence-conclusion` | target conclusion | one array is impossible | not established |

No canonical admissibility row is asserted for a concrete witness.  Rather, the
proof eliminates all source-admissible graphs lying in this one parameter row.

## Target versus witness

The source target ranges over every graph satisfying revision 3.  The proof has no
concrete witness: its conditional object is an arbitrary distance-regular graph
with one fixed array.  That object is exactly the bounded class asserted in the
claim, but it is only a proper subcase of the source target.  Consequently
`witness_equals_target: false` refers to the full active scope, and the maximum
scope conclusion is a one-array exclusion.

There is no circular construction.  The matrices below are the actual distance
matrices of the hypothetical graph.  Every identity is derived from the standard
intersection recurrence and disjoint distance relations; no identity is imposed
to manufacture a passing object.

## Subclaims and what each method proves

| subclaim | method | what a pass proves | what it does not prove |
|---|---|---|---|
| sphere sizes and distance products | exact hand recurrence | every matrix identity is necessary for the array | existence or sufficiency of those identities |
| abstract distance-3 constituent | reduction of `A_3^2` in the distance basis | a hypothetical `B=A_3` is automatically `srg(210,76,26,28)` | existence or uniqueness of such an SRG outside a distance scheme |
| spectral branches | simultaneous diagonalization, traces, exact integer enumeration | the two preliminary branches and rejection of the `13` branch are correct | nonexistence by itself |
| row-support/local argument | zero-one support counts and a shortest-path lemma | the one array is impossible | any other array or the full source question |
| exact Python checker | independently coded four-dimensional algebra and integer enumeration | arithmetic agrees with the hand derivation | graph existence, catalogue completeness, or the logical local lemma |

## Evidence

### Source and tool probe

Commands:

```bash
source _meta/agents/Kourovka/paths.env
pdftotext -f 177 -l 177 -layout "$KOUROVKA_PDF" -
printf 'Print(GAPInfo.Version,"\\n");\nQUIT;\n' | gap -q
python3 --version
pdftotext -v
```

Relevant exact source output, also checked visually against the rendered PDF page:

```text
21.90. Let Γ be a graph of diameter d. For i ∈ {1, 2, . . . , d}, let Γi be the graph on
the same vertex set as Γ with vertices u, w adjacent in Γi if and only if dΓ (u, w) = i.
Does there exist a Q-polynomial distance-regular graph Γ of diameter 3 such that Γ2
and Γ3 are strongly regular?                                              A. A. Makhnëv
```

Tool output:

```text
4.12.1
Python 3.12.3
pdftotext version 24.02.0
```

Sage and Magma returned no executable path.  GAP was probed but is not used as
mathematical evidence.  No web, catalogue, or solution-history source was used.

### 1. Distance data and the abstract matrix `B`

Write the intersection array as

\[
(b_0,b_1,b_2)=(19,6,8),\qquad(c_1,c_2,c_3)=(1,1,12).
\]

Then

\[
(a_0,a_1,a_2,a_3)=(0,12,10,7)
\]

and the sphere sizes are

\[
k_0=1,\quad k_1=19,\quad
k_2=\frac{19\cdot6}{1}=114,\quad
k_3=\frac{114\cdot8}{12}=76.
\]

Hence the hypothetical graph has 210 vertices.  Put `A=A_1` and `B=A_3`.
The distance-matrix recurrence is

\[
\begin{aligned}
AA_1&=19I+12A_1+A_2,\\
AA_2&=6A_1+10A_2+12A_3,\\
AA_3&=8A_2+7A_3. \tag{1}
\end{aligned}
\]

These equations derive `B`; they do not posit a separate SRG.  For completeness,
first use `A_2=A^2-12A-19I` and the last line of (1):

\[
\begin{aligned}
A^2A_3&=A(8A_2+7A_3)
       =48A_1+136A_2+145A_3,\\
A_2A_3&=48A_1+40A_2+42A_3. \tag{2}
\end{aligned}
\]

Associativity applied to `(AA_2)A_3=A(A_2A_3)`, followed by (1)--(2), gives

\[
12A_3^2=912I+336A_1+336A_2+312A_3,
\]

so

\[
B^2=76I+28A_1+28A_2+26B. \tag{3}
\]

Thus a hypothetical `B` is a symmetric zero-one graph of valency 76, with 26
common `B`-neighbors for a `B`-adjacent pair and 28 for a nonadjacent pair.  In
particular it is abstractly `srg(210,76,26,28)`: it is noncomplete because
`76<209`, connected because `mu=28>0`, and (3) gives the three adjacency
eigenvalues `76,6,-8`.  No explicit representative is assumed or needed.

### 2. The three matrix identities

Let

\[
D=I+B,\qquad M=I+A_1,\qquad J=I+A_1+A_2+B.
\]

Both `D` and `M` are symmetric zero-one matrices.  The diagonal of `M` is one,
its row sum is `1+k_1=20`, and the row sum of `D` is `1+k_3=77`.

Equation (3) gives

\[
D^2=I+2B+B^2=49I+28J. \tag{4}
\]

The last line of (1) gives

\[
\begin{aligned}
M(D+7I)
 &=(I+A_1)(8I+B)\\
 &=8I+8A_1+B+(8A_2+7B)=8J. \tag{5}
\end{aligned}
\]

Finally, the first line of (1) gives

\[
M^2=I+2A_1+A_1^2
   =20I+14A_1+A_2
   =7I+13M+J-D. \tag{6}
\]

All diagonal terms check: (4) has diagonal `49+28=77`, the row weight of `D`;
(6) has diagonal `7+13+1-1=20`, the row weight of `M`.  In (5), the principal
row-sum check is `20(77+7)=8(210)=1680`.

### 3. Spectral-multiplicity audit

This part is consistent but is not needed for the local contradiction.  Equation
(6) writes `D` as a polynomial in `M` and `J`; since `M` is regular, these symmetric
matrices commute and admit a common orthogonal eigenbasis.  On
`\mathbf1^\perp`, (4) and (6) give

\[
d^2=49,\qquad d=7+13m-m^2.
\]

Thus

\[
\begin{array}{c|c}
d=7&m\in\{0,13\}\\
d=-7&m\in\{14,-1\}.
\end{array}
\]

Let the nonprincipal multiplicities be
`n_0,n_{13},n_{14},n_{-1}`.  The principal eigenvalue of `M` is 20.  Using
`tr(M)=210` and `tr(M^2)=210\cdot20=4200` gives

\[
\begin{aligned}
n_0+n_{13}+n_{14}+n_{-1}&=209,\\
13n_{13}+14n_{14}-n_{-1}&=190,\\
169n_{13}+196n_{14}+n_{-1}&=3800.
\end{aligned}
\]

Adding the last two equations and dividing by 14 yields

\[
13n_{13}+15n_{14}=285.
\]

The two nonnegative integral solutions are exactly

| branch | `n_0` | `n_13` | `n_14` | `n_-1` |
|---|---:|---:|---:|---:|
| A | 99 | 15 | 6 | 89 |
| B | 114 | 0 | 19 | 76 |

On `\mathbf1^\perp`, (5) also gives `m(d+7)=0`.  For `m=13` the paired value is
`d=7`, so the product is nonzero.  Branch A is therefore impossible and branch B
is forced:

\[
\operatorname{Spec}(M)=\{20^1,14^{19},0^{114},(-1)^{76}\}.
\]

There is no hidden inconsistency in the submitted spectral branch calculation.
Its surviving branch is compatible and does not itself prove existence.

### 4. Every row support is a `B`-coclique

From (5), using `D=I+B`,

\[
MB=8(J-M). \tag{7}
\]

For a vertex `u`, let

\[
C_u=\{x:M_{ux}=1\}.
\]

This is the closed `A_1`-neighborhood of `u`, so `|C_u|=20` and `u\in C_u`.
If `v\in C_u`, then the `(u,v)` entry of the right side of (7) is zero, while

\[
(MB)_{uv}=\sum_{x\in C_u}B_{xv}.
\]

Every summand is zero or one.  Hence `B_{xv}=0` for every `x\in C_u`.  As `v`
was arbitrary, no two vertices of `C_u` are `B`-adjacent: `C_u` is a
`B`-coclique.  This use of (7) includes the diagonal correctly; `B` itself has
zero diagonal.

### 5. The 19-point local graph

Put

\[
N_u=C_u\setminus\{u\}.
\]

This is the set of 19 `A_1`-neighbors of `u`.  If `v\in N_u`, then `u\ne v`,
`M_{uv}=1`, and `B_{uv}=0` because `(u,v)` lies in relation `A_1`, not `A_3`.
The `(u,v)` entry of (6) is therefore

\[
(M^2)_{uv}=13+1=14. \tag{8}
\]

Because `M` is symmetric zero-one, `(M^2)_{uv}=|C_u\cap C_v|`.  The points `u`
and `v` both belong to this intersection.  Its other 12 points are exactly the
common open `A_1`-neighbors of `u` and `v`.  Thus every `v\in N_u` has exactly
12 neighbors in the graph induced by `A_1` on `N_u`: the local graph is
12-regular on 19 vertices.

Now take distinct `v,w\in N_u` that are nonadjacent in this local `A_1` graph.
Then `M_{vw}=0`.  Since `v,w\in C_u` and `C_u` is a `B`-coclique,
`B_{vw}=0` as well.  Thus their distance relation is `A_2`, not `A_1` or `B=A_3`,
and the `(v,w)` entry of (6) is

\[
(M^2)_{vw}=1. \tag{9}
\]

But `u\in C_v\cap C_w`, so (9) says

\[
C_v\cap C_w=\{u\}.
\]

In particular `v,w` have no common neighbor inside the local graph.  Every
relation label in this step is now explicit: local adjacency is `A_1`, the
forbidden distance-3 relation is `B=A_3`, and the remaining nonadjacent local
pair lies in `A_2`.

### 6. Clique-component contradiction

In any graph where nonadjacent vertices have no common neighbor, every connected
component is complete.  Otherwise a shortest path of length at least two has
first and third vertices nonadjacent but sharing the middle vertex.

Every component of the 12-regular local graph is therefore a complete graph of
degree 12, namely `K_13`.  Its total number of vertices must be divisible by 13,
contradicting `|N_u|=19`.  This completes the bounded proof.

Equivalently, the standard local consequence of `c_2=1` is that every local
component has size `a_1+1=13`, which cannot partition `k=19`.  The expanded
matrix proof above verifies that no diagonal or relation-convention mistake is
hidden in that shorthand.

### 7. Exact bounded checker transcript

The independently written checker is
`Agents/Kourovka/problems/21.90/verification/scratch/check_srg210_array.py`.
It works only in the four-dimensional distance algebra and enumerates the trace
solutions; it does not construct or search for a graph.

The first run reached an audit-only assertion because the two correct branches
were enumerated in the reverse order from the expected list.  The assertion was
changed only to that observed ordering; the equations and expected rows were not
changed.  The successful command was

```bash
python3 Agents/Kourovka/problems/21.90/verification/scratch/check_srg210_array.py
```

with exact output:

```text
sphere_sizes=(1,19,114,76) v=210
A3_squared_coefficients=(76, 28, 28, 26)
D_squared_coefficients=(77, 28, 28, 28)=49I+28J
M(D+7I)_coefficients=(8, 8, 8, 8)=8J
M_squared_coefficients=(20, 14, 1, 0)=7I+13M+J-D
trace_branches=[(114, 0, 19, 76), (99, 15, 6, 89)]
after_m(d+7)=0=[(114, 0, 19, 76)]
local_component_size=12+1=13; 19_mod_13=6
```

The output is also stored in
`Agents/Kourovka/problems/21.90/verification/scratch/check_srg210_array.out`.

## Verdict

`status/conjectured` pending the required human-review gate.

Mathematically, the single-array hand proof survives independent reconstruction:
the array `{19,6,8;1,1,12}` is impossible.  The certification label remains at
the lower status because the bounded theorem is a strict partial result and has
not yet passed the human gate required for `status/proven`.

## Why this verdict

The contradiction uses only consequences of the assumed intersection array.
The derivation of `B`, both local matrix identities, all diagonal entries, and all
`A_1/A_2/A_3` labels check exactly.  Each row support `C_u` is a `B`-coclique;
the induced `A_1` graph on its other 19 vertices is 12-regular; and a nonadjacent
local pair has no common local neighbor because its closed neighborhoods meet
only in `u`.  Its components would all be `K_13`, which cannot partition 19.

The separate spectral audit reproduces exactly the two submitted branches and
the mixed-identity rejection of the branch containing eigenvalue 13.  It introduces
no extra constituent assumption and is not needed for the contradiction.

## What is NOT established

- The active revision-3 existential scope is not answered.
- No other intersection array is eliminated by this note.
- No bounded parameter enumeration is proved complete, and no claim that this was
  the first unexcluded row is audited.
- Existence, nonexistence, uniqueness, or classification of abstract
  `srg(210,76,26,28)` graphs outside this hypothetical distance scheme is not
  established.
- No explicit graph, Q-polynomial ordering, distance-2 constituent, catalogue,
  modular-rank calculation, Smith form, SAT instance, or automorphism computation
  is verified or needed.

## What would upgrade it

Human review of this checked hand proof can upgrade the one-array theorem to
`status/proven` without an explicit constituent computation.  Answering the active
scope still requires either a source-admissible construction or a universal
nonexistence proof covering every remaining parameter array, followed by the full
review circle.

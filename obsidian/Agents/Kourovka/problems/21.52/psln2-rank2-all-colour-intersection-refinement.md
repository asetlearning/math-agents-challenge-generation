---
title: "Kourovka 21.52 — rank-two all-colour two-point refinement"
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
direction: proof
strategy: RANK2-ALL-COLOUR-INTERSECTION-REFINEMENT
outcome: PARTIAL_RESULT
target_object: "all finite nonabelian simple groups and all single involution classes"
witness_object: "complete two-point arrays in the rank-two square-zero class of PSL_4(2), plus a uniform obstruction to the resulting S_23 predicate for PSL_n(2), n>=6"
witness_equals_target: false
active_assignment_answered: no
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/coherent-configurations
  - project/kourovka
  - status/conjectured
---

# Outcome

`PARTIAL_RESULT`, strictly for the assigned rank-two lane.

In the rank-two square-zero involution class of

\[
L=\operatorname{PSL}_4(2)=\operatorname{GL}_4(2),
\]

the complete two-point intersection array of a colour-2 pair distinguishes every
same-decoration-fibre pair from every cross-fibre pair.  In fact the single cell

\[
S_{2,3}(P,Q)=
\#\{T:\ |(I+P)(I+T)|=2,\ |(I+Q)(I+T)|=3\}               \tag{1}
\]

already does so: it equals `0` for all 525 same-fibre pairs and `4` for all
1260 cross-fibre pairs.

However, (1) does **not** extend uniformly in `n`.  For every `n>=6` there are
explicit cross-fibre colour-2 pairs in the same rank-two class for which
`S_23=0`, exactly as for same-fibre pairs.  The block calculation below gives this
conclusion without computation.  Consequently the `n=4` fibre predicate cannot authorize the
decoration-fibre quotient in the infinite family.  The full arrays might still
separate fibres for larger `n` by other cells; that stronger question was not
settled.

The universal Problem 21.52 target remains open.  No arbitrary colour-preserving
permutation was classified, even in this rank-two family.

# 1. Exact finite model and conventions

Let

\[
\mathcal D_4=\{N\in M_4(\mathbb F_2):N^2=0,
                   \operatorname{rank}N=2\}.
\]

The vertices `I+N`, for `N in D_4`, are exactly the single Jordan class `2^2`
in `GL_4(2)`.  There are 210 vertices.  Since image and kernel are both
two-dimensional and `im N <= ker N`, they coincide.  The 35 two-spaces are the
bare flags, and each supports the six quotient-to-image decorations in
`GL_2(2)`.

For a colour-2 pair `(P,Q)`, define the literal full array

\[
S_{ij}(P,Q)=\#\{T\in\mathcal D_4:
 |(I+P)(I+T)|=i,\ |(I+Q)(I+T)|=j\}.                     \tag{2}
\]

The edge-colour palette is exactly `{2,3,4,5,6}`.  The tables below also show
the diagonal product order `1`, because (2) literally includes `T=P,Q`.
If endpoints are excluded, simply delete the contributions `S_12=S_21=1`;
the displayed `{2,3,4,5,6}` subarray is unchanged and totals 208.

Exhaustive enumeration gives 1785 colour-2 unordered pairs: 525 same-fibre and
1260 cross-fibre.  The same-fibre pairs have two array types, according as the
relative element between their two `GL_2(2)` decorations has order 3 or 2.
Their multiplicities are respectively `35*6=210` and `35*9=315`.

# 2. Every full `n=4` array

Rows are indexed by `i` and columns by `j`, in the order
`1,2,3,4,5,6`.  All omitted possibilities are displayed as zero.

## 2.1 Same fibre, relative decoration of order 3

This array occurs for exactly 210 unordered pairs:

| `i\j` | 1 | 2 | 3 | 4 | 5 | 6 |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0 | 1 | 0 | 0 | 0 | 0 |
| 2 | 1 | 4 | 0 | 12 | 0 | 0 |
| 3 | 0 | 0 | 24 | 24 | 16 | 0 |
| 4 | 0 | 12 | 24 | 12 | 0 | 0 |
| 5 | 0 | 0 | 16 | 0 | 16 | 0 |
| 6 | 0 | 0 | 0 | 0 | 0 | 48 |

## 2.2 Same fibre, relative decoration of order 2

This array occurs for exactly 315 unordered pairs:

| `i\j` | 1 | 2 | 3 | 4 | 5 | 6 |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0 | 1 | 0 | 0 | 0 | 0 |
| 2 | 1 | 8 | 0 | 8 | 0 | 0 |
| 3 | 0 | 0 | 32 | 16 | 0 | 16 |
| 4 | 0 | 8 | 16 | 24 | 0 | 0 |
| 5 | 0 | 0 | 0 | 0 | 0 | 32 |
| 6 | 0 | 0 | 16 | 0 | 32 | 0 |

## 2.3 Cross fibre

Every one of the 1260 cross-fibre colour-2 pairs has this array:

| `i\j` | 1 | 2 | 3 | 4 | 5 | 6 |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0 | 1 | 0 | 0 | 0 | 0 |
| 2 | 1 | 4 | 4 | 4 | 0 | 4 |
| 3 | 0 | 4 | 20 | 20 | 8 | 12 |
| 4 | 0 | 4 | 20 | 4 | 8 | 12 |
| 5 | 0 | 0 | 8 | 8 | 8 | 8 |
| 6 | 0 | 4 | 12 | 12 | 8 | 12 |

Each table has row and column marginals

\[
(1,17,64,48,32,48),                                     \tag{3}
\]

as required by vertex transitivity.  The prior common-colour-2 collision is
visible in the first and third tables: both have `S_22=4`.  But their
`S_23=S_32` entries are respectively `0` and `4`.  The second same-fibre type
also has `S_23=S_32=0`.  Thus the fixed-`n=4` separation claimed in (1) follows
from the exhaustive certificate, pending independent audit.

# 3. Hand orbit check for the finite enumeration

Under the standard isomorphism `GL_4(2) ~= A_8`, the 210 vertices correspond to
double transpositions.  Fix `a=(12)(34)`.  Its 17 other commuting double
transpositions are:

- 2 on the same four-point support;
- 12 sharing exactly one of the two transpositions of `a`;
- 3 on the disjoint four-point complement.

The corresponding unordered-pair orbit sizes are

\[
210,\qquad1260,\qquad315,                                \tag{4}
\]

which sum to 1785.  Inside each six-decoration fibre, the 15 pairs split into
6 with relative order 3 and 9 with relative order 2, so across 35 fibres their
sizes are 210 and 315.  Thus the first and third orbits in (4) are precisely the
two same-fibre types, while the middle orbit is cross-fibre.  This independently
checks the coverage and multiplicities, though not the individual array entries.

# 4. Uniform symbolic test of the separating cell

The same-fibre half of (1) does extend to every `n>=4`, but the cross-fibre half
fails from `n=6` onward.

Write

\[
V=A\oplus Z\oplus B,
\qquad \dim A=\dim B=2,\quad \dim Z=n-4,
\]

and fix

\[
P=\begin{pmatrix}
0&0&I_2\\
0&0&0\\
0&0&0
\end{pmatrix}.                                           \tag{5}
\]

An endomorphism `T` commutes with `P` if and only if it has block form

\[
T=\begin{pmatrix}
X&C&Y\\
0&H&W\\
0&0&X
\end{pmatrix}.                                           \tag{6}
\]

The square-zero and rank-two conditions further restrict these blocks, but are
not needed for the following exclusion.

For square-zero `Q,T`, put `a=I+Q` and `b=I+T`.  For `a != b`, the condition
`|ab|=3` is equivalent to `aba=bab`, and direct expansion in characteristic two
gives

\[
Q+T+QTQ+TQT=0.                                           \tag{7}
\]

## 4.1 Every same-fibre pair has `S_23=0`

Every decoration in the fibre of (5) is

\[
Q_R=\begin{pmatrix}
0&0&R\\
0&0&0\\
0&0&0
\end{pmatrix},\qquad R\in\operatorname{GL}_2(2).        \tag{8}
\]

Substitute (6) and (8) into (7).  Here `Q_R T Q_R=0`, while
`T Q_R T` has only the `(A,B)` block `XRX`.  Every block outside `(A,B)` in
(7) therefore forces

\[
X=C=H=W=0,
\]

and the `(A,B)` block then forces `Y=R`.  Hence (7) implies `T=Q_R`, whose
involution product with `I+Q_R` has order 1, not 3.  There is no counted `T`, so

\[
S_{2,3}(P,Q_R)=0                                         \tag{9}
\]

for every same-fibre colour-2 pair and every `n>=4`.

## 4.2 Explicit cross-fibre pairs also have `S_23=0` for every `n>=6`

Now suppose `dim Z>=2` and choose a surjection `U:Z -> A`.  Put

\[
Q_U=\begin{pmatrix}
0&U&0\\
0&0&0\\
0&0&0
\end{pmatrix}.                                           \tag{10}
\]

Then `Q_U^2=0`, `rank Q_U=2`, and `P Q_U=Q_U P=0`, so `(P,Q_U)` is a
colour-2 pair in the assigned class.  It is cross-fibre because

\[
\operatorname{im}P=\operatorname{im}Q_U=A,
\quad
\ker P=A\oplus Z,
\quad
\ker Q_U=A\oplus B\oplus\ker U,                         \tag{11}
\]

and the two kernels differ.

Again use (6)--(7).  Now `Q_U T Q_U=0`, while `T Q_U T` has blocks
`(A,Z)=XUH` and `(A,B)=XUW`.  Equation (7), read block by block, first gives
`X=H=W=0`, then `C=U` and `Y=0`.  Thus it again forces `T=Q_U`, which cannot
have product order 3 with itself.  Consequently

\[
S_{2,3}(P,Q_U)=0                                         \tag{12}
\]

for this explicit cross-fibre pair in every `n>=6`.

Equations (9) and (12) are the precise obstruction: the successful `n=4`
formula (1) is not a uniform fibre definition.  No quotient incidence geometry
is therefore reconstructed or assumed.

# 5. Reproducible computation record

- Implementation: dependency-free Python 3.12.3.
- Frozen script: `Agents/Kourovka/problems/21.52/scratch/psl4_rank2_full_intersection.py`.
- Script SHA-256: `2dd9c1805d7bc52f6b998d280c67171bc5ee04f4ea0edc5452da502e6f35fecc`.
- Exact leased command:

  `timeout 60s python3 Agents/Kourovka/problems/21.52/scratch/psl4_rank2_full_intersection.py --output Agents/Kourovka/problems/21.52/scratch/psl4-rank2-full-intersection-certificate.json`

- Observed result: exit code 0, empty standard output by design, wall time
  0.749556311 seconds.
- Certificate: `Agents/Kourovka/problems/21.52/scratch/psl4-rank2-full-intersection-certificate.json`.
- Certificate SHA-256: `27ad591f2366b45dd65d00fc7eb91e8d032d5262a01875c6683f11abff9c0e7f`.
- Coverage: all 65536 binary `4 x 4` matrices filtered to all 210 square-zero
  rank-two matrices; all 21945 unordered vertex pairs coloured; all 1785
  colour-2 pairs arrayed against all 210 possible third vertices.
- Internal assertions: vertex and fibre counts, exact product orders dividing
  `|GL_4(2)|=20160`, every same-fibre pair of colour 2, array totals, symmetry
  under endpoint swap, and agreement of endpoint-included/excluded gate results.

The implementation is bespoke finite arithmetic, not a reimplementation of a
general-purpose algebra system.  Validator can independently reproduce the
finite result either with a separate matrix implementation or in the `A_8`
double-transposition model, and can check the block proof without trusting the
enumerator.

# 6. Constraint-and-conclusion matrix

| constraint id | role | result |
|---|---|---|
| `21.52-forall-L-D` | admissibility | Uncovered.  The exact array is only `PSL_4(2)` and the obstruction only the assigned rank-two family for `n>=6`. |
| `21.52-L-finite-nonabelian-simple` | admissibility | Passes for every displayed `PSL_n(2)`, `n>=4`. |
| `21.52-D-single-involution-class` | admissibility | Passes: `D` is the one Jordan class `2^2 1^{n-4}` of involutions. |
| `21.52-Gamma-complete-on-D` | admissibility | Passes in the finite gate: every pair and every third vertex in the 210-vertex class is included. |
| `21.52-edge-colour-exact-product-order` | admissibility | Passes: all labels are exact orders of `(I+P)(I+Q)`, not product conjugacy classes. |
| `21.52-tau-preserves-all-edge-colours` | admissibility | Not addressed: no arbitrary colour-preserving permutation is classified. |
| `21.52-tau-induced-by-AutL` | target conclusion | Not established, even uniformly for this rank-two family. |

`witness_equals_target: false`; `active_assignment_answered: no`.

# What this does not establish

- It does not prove that the full arrays fail to recover fibres for `n>=6`; only
  the particular `S_23` certificate extracted at `n=4` fails uniformly.
- It does not determine the colour-automorphism group of the rank-two class for
  any `n`.
- It does not reconstruct the decoration-fibre quotient or ambient incidence
  geometry.
- It does not prove the rank-two `PSL_n(2)` family case of Problem 21.52.
- It does not prove or refute the universal target.
- It does not concern unions of involution classes, product-conjugacy-class
  colours, uncoloured graphs, or Problem 21.53.

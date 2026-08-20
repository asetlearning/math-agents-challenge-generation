---
title: "Order-540 local, integral, and Delsarte-coclique gate"
problem: 21.90
scope_id: 21.90/diameter-three-distance-graphs
assignment_revision: 3
outcome: CHECKPOINT
active_assignment_answered: no
---

# Order-540 local-integral gate

This is a constituent-independent necessary-condition analysis of

\[
  \{77,60,13;1,12,65\}. \tag{1}
\]

No literature or catalogue search was used.  All calculations below are
reproduced by `scratch/order540_local_integral_gate.g`, with transcript in the
matching `.out` file.

## Spheres, handshakes, and spectra

Writing `X=A_1`, the local degrees and sphere sizes are

\[
 (a_0,a_1,a_2,a_3)=(0,16,52,12),\qquad
 (k_0,k_1,k_2,k_3)=(1,77,385,77),
\]

so `v=540`.  The cross-layer handshakes are

\[
 77\cdot60=385\cdot12=4620,
 \qquad 385\cdot13=77\cdot65=5005,
\]

and the three nontrivial within-layer handshakes are

\[
 77\cdot16=1232,\qquad 385\cdot52=20020,\qquad
 77\cdot12=924.
\]

Thus the parity gate passes.  More generally, the degrees of each distance
relation induced on each nonzero sphere are

\[
\begin{array}{c|ccc}
 &A_1&A_2&A_3\\ \hline
\Gamma_1(u)&16&60&0\\
\Gamma_2(u)&52&280&52\\
\Gamma_3(u)&12&60&4
\end{array} \tag{2}
\]

and every product of a row size with an entry of (2) is even.  In particular,
there is no hidden handshake failure in either constituent subrelation.

The intersection quotient gives

\[
 \operatorname{Spec}(X)=
 \{77^1,17^{77},(-1)^{385},(-13)^{77}\}. \tag{3}
\]

The distance polynomials are

\[
 p_2(z)=\frac{z^2-16z-77}{12},\qquad
 p_3(z)=\frac{(z-52)p_2(z)-60z}{65}. \tag{4}
\]

Consequently

\[
 \begin{aligned}
 A_2&:\quad \operatorname{srg}(540,385,280,260),
 &\operatorname{Spec}(A_2)&=\{385^1,25^{77},(-5)^{462}\},\\
 B:=A_3&:\quad \operatorname{srg}(540,77,4,12),
 &\operatorname{Spec}(B)&=\{77^1,5^{385},(-13)^{154}\}.
 \end{aligned} \tag{5}
\]

As another consistency check, `X+B`, the complement of `A_2`, would be
`srg(540,154,28,50)` with spectrum
`154^1,4^462,(-26)^77`.

## Exact fission identities

The Bose--Mesner products give

\[
 X^2=65I+4X+12J-12B,
 \qquad XB=13J-13I-13X-B. \tag{6}
\]

For the symmetric diagonal-one zero-one matrix `M=I+X`, these become

\[
 \boxed{M(B+13I)=13J},\qquad
 \boxed{M^2=60I+6M+12J-12B}. \tag{7}
\]

They force

\[
 \operatorname{Spec}(M)=
 \{78^1,18^{77},0^{385},(-12)^{77}\},qquad
 \operatorname{rank}_{\mathbb Q}M=155. \tag{8}
\]

If `C_u` is the support of row `u` of `M`, then (7) says that `C_u` is
a 78-coclique of `B`.  This meets the Hoffman bound

\[
 \alpha(B)\leq \frac{540\cdot13}{77+13}=78. \tag{9}
\]

For distinct vertices, the required intersections are exactly

\[
 |C_u\cap C_v|=
 \begin{cases}
 18,&X_{uv}=1,\\
 12,&(A_2)_{uv}=1,\\
 0,&B_{uv}=1.
 \end{cases} \tag{10}
\]

Thus the fission would be a symmetric 540-block, 540-point, block-size-78
three-intersection incidence configuration, with diagonal containment
`u\in C_u` and replication 78.

There is also an exact design forced by any one row.  For a fixed `C_u`, the
462 sets

\[
 N_B(z)\cap C_u\qquad (z\notin C_u)
\]

form a (possibly repeated-block) `2-(78,13,12)` design: Hoffman equality gives
block size 13, each point has replication 77, and every pair of points of the
`B`-coclique has exactly `mu_B=12` common `B`-neighbours.  The parameter
identities `77(13-1)=12(78-1)` and `78\cdot77=462\cdot13` pass.

## Local component test

Fix `u`.  Since `C_u={u}\cup\Gamma_1(u)` is a `B`-coclique, two nonadjacent
vertices `v,w` of the 16-regular local `X`-graph on `Gamma_1(u)` are at
distance 2 in `X`.  They have `p^2_{11}=c_2=12` common `X`-neighbours in the
whole graph.  One is `u`, leaving eleven which can split between
`Gamma_1(u)` and `Gamma_2(u)`.  Equivalently, (10) fixes
`|C_v intersect C_w|=12`, not 1.  Hence it does **not** force zero common neighbours
inside the local graph, and the clique-component argument that eliminated the
order-210 row does not apply.

The analogous checks do not recover that argument:

- the local `B`-graph on `Gamma_3(u)=N_B(u)` is 4-regular on 77 vertices;
  two nonadjacent local vertices have 12 common `B`-neighbours globally, one
  being `u`, again leaving eleven;
- the local `A_2`-graph on `Gamma_2(u)` has degree 280, and the corresponding
  remainder is `mu_2-1=259`;
- in the 12-regular `X`-graph induced on `Gamma_3(u)`, a pair in relation
  `B=A_3` has no common `X`-neighbour, but the other nonedges are in relation
  `A_2` and have 12 globally, so zero codegree is not uniform over nonedges.

Thus none of the natural induced local relations is forced to be a union of
cliques.

For completeness, putting `D=I+B` gives the compatible integral identities

\[
 B^2=65I-8B+12J,\qquad
 D^2=72I-6D+12J,\qquad
 MD=13J-12M. \tag{11}
\]

Modulo either 2 or 3 these reduce to `M^2=D^2=0` and `MD=J`.  The resulting
self-orthogonality and rank-one product are mutually compatible; they give no
rank or parity contradiction without an explicit matrix.  No Smith, SAT, or
heavy computation was started.

## Frozen bounded next test

For any explicit adjacency matrix
`B=srg(540,77,4,12)`, enumerate its Hoffman-bound 78-cocliques.  A fission must
choose one labelled coclique `C_u` containing each `u` so that the incidence
matrix is symmetric and (10) holds.  Equivalently, solve the finite
540-partite compatibility CSP whose row domains are those cocliques.  An empty
domain for one vertex, or an exhaustive UNSAT certificate for this CSP,
excludes that one constituent; a solution reconstructs `X=M-I`, after which
(6) gives the full intersection array.  This test was frozen but not run,
because no explicit constituent was supplied and no heavy-compute lease is
held.

All cheap constituent-independent gates requested for (1) pass.  This is a
bounded checkpoint, not evidence that the array or the full revision-3 target
exists.  The 482-row arithmetic screen remains only its stated finite box.
`active_assignment_answered: no`.

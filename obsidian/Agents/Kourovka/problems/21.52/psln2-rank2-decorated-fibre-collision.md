---
title: "Kourovka 21.52 — rank-two decorated fibres: exact local-signature collision"
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
direction: proof
strategy: LIN2-RANK2-DECORATED-FIBRE-QUOTIENT
outcome: STRATEGY_EXHAUSTED
target_object: "all finite nonabelian simple groups and all single involution classes"
witness_object: "two pair configurations in the rank-two square-zero class of PSL_4(2)"
witness_equals_target: false
active_assignment_answered: no
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/projective-geometry
  - project/kourovka
  - status/conjectured
---

# Rank-two decorated fibres: exact local-signature collision

## Outcome

`STRATEGY_EXHAUSTED` at the mandated minute-12 fibre gate.

The most immediate intrinsic candidate for recognizing a same-flag pair is its
complete common-colour-\(2\) core: the edge colour, the entire set of common
colour-\(2\) neighbours, and every exact product-order colour induced on that
set together with the endpoints.  This candidate fails already in
\(L=\operatorname{PSL}_4(2)=\operatorname{GL}_4(2)\).  An explicit genuine
same-fibre pair and an explicit cross-fibre pair have exactly the same signature:
four other common colour-\(2\) neighbours, and the six resulting vertices induce
a monochromatic \(K_6\) of exact colour \(2\).

This is a hard kill of `SIX-FIBRE-BY-COMMON-2-CORE`, the local predicate tested
inside the authorized `LIN2-RANK2-DECORATED-FIBRE-QUOTIENT` pivot.  It is **not**
a proof that the fibre partition is undefinable from the full coloured graph:
intersection data involving colours other than \(2\), or colours from the
six-vertex core to all outside vertices, were not classified.  Consequently no
ambient incidence quotient is authorized and no rank-two family theorem results.

## 1. The exact proposed colour signature

Let

\[
 \mathcal D=\{T\in\operatorname{End}(V):T^2=0,\quad
                    \operatorname{rank}T=2\},
\]

and identify \(T\in\mathcal D\) with the class vertex \(x_T=I+T\).  For
distinct \(P,Q\in\mathcal D\) on an edge of colour \(2\), put

\[
 C_2(P,Q)=\{T\in\mathcal D\setminus\{P,Q\}:
                  |x_Px_T|=|x_Qx_T|=2\}.
\]

The tested signature is

\[
 \Sigma_2(P,Q)=
 \left(2,\ |C_2(P,Q)|,\
   \text{the exact product-order-coloured graph induced on }
   \{P,Q\}\cup C_2(P,Q)\right).                         \tag{1}
\]

Thus (1) retains the whole common-\(2\)-neighbour intersection, not merely its
cardinality, and it uses exact product orders rather than product conjugacy
classes.  The next two sections give a collision for (1).

## 2. A same-fibre pair and its common-\(2\) core

Write \(V=A\oplus B\), with both summands two-dimensional, and use \(2\times2\)
blocks.  Set

\[
 J(P)=\begin{pmatrix}0&P\\0&0\end{pmatrix},\qquad
 C=\begin{pmatrix}0&1\\1&1\end{pmatrix}.
\]

Then \(C\) has order \(3\).  Take

\[
 N=J(I),\qquad M=J(C).                                   \tag{2}
\]

Both maps have image and kernel \(A\), so (2) is a genuine pair of distinct
decorations in the same six-element fibre.  Also \(NM=MN=0\), hence its edge
has exact colour \(2\).

Let \(T=\begin{pmatrix}X&Y\\Z&W\end{pmatrix}\) be any endomorphism commuting
with both \(N\) and \(M\).  Commutation with \(N\) gives

\[
 Z=0,\qquad W=X,
\]

and commutation with \(M\) gives \(XC=CX\).  Therefore

\[
 T=\begin{pmatrix}X&Y\\0&X\end{pmatrix},
 \qquad X\in\mathbb F_2[C].                              \tag{3}
\]

The algebra \(\mathbb F_2[C]\) is the field of four elements.  If additionally
\(T^2=0\), then the diagonal block in \(T^2\) is \(X^2\), so \(X=0\).  Now
\(\operatorname{rank}T=2\) exactly when \(Y\in\operatorname{GL}_2(2)\).
Consequently

\[
 \{T\in\mathcal D:TN=NT,\ TM=MT\}
   =\{J(Y):Y\in\operatorname{GL}_2(2)\},                 \tag{4}
\]

which has six members and includes \(N,M\).  Every two maps in (4) have both
products zero, hence every edge among their corresponding involutions has exact
colour \(2\).  Thus

\[
 |C_2(N,M)|=4,
 \qquad \{N,M\}\cup C_2(N,M)\cong K_6
 \text{ monochromatic of colour }2.                     \tag{5}
\]

## 3. A cross-fibre pair with the identical signature

Put

\[
 S=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
 N'=J(I),\qquad
 M'=\begin{pmatrix}S&0\\0&S\end{pmatrix}.              \tag{6}
\]

The maps in (6) square to zero and have rank two.  They commute, with

\[
 N'M'=M'N'=\begin{pmatrix}0&S\\0&0\end{pmatrix}\ne0,
\]

so their edge again has exact colour \(2\).  But their flags are different:

\[
 \operatorname{im}N'=\ker N'=A,
\]

whereas

\[
 \operatorname{im}M'=\ker M'
 =\langle(e_1,0),(0,e_1)\rangle\ne A.                   \tag{7}
\]

Thus (6) is a cross-fibre pair.

As above, commutation with \(N'\) first forces
\(T=\begin{pmatrix}X&Y\\0&X\end{pmatrix}\).  Commutation with \(M'\) then
forces \(X,Y\in\mathbb F_2[S]\).  Write

\[
 X=aI+bS,\qquad Y=cI+dS,
 \qquad a,b,c,d\in\mathbb F_2.
\]

Since \(\mathbb F_2[S]\) is commutative and \(S^2=0\), the condition \(T^2=0\)
is exactly \(a=0\).  Hence every square-zero common centralizer has the form

\[
 T_{b,c,d}=\begin{pmatrix}bS&cI+dS\\0&bS\end{pmatrix}.  \tag{8}
\]

The rank-two members of (8) are exactly

\[
 \begin{array}{ll}
 b=0,\ c=1,\ d\in\mathbb F_2, &\text{two members},\\
 b=1,\ c,d\in\mathbb F_2, &\text{four members}.
 \end{array}                                               \tag{9}
\]

For the second row, if \(Sv=0\) then \(v\) lies on the one-dimensional kernel
of \(S\), and the remaining equation leaves a two-dimensional kernel for
\(T_{1,c,d}\); hence each such map indeed has rank two.  The other values in
(8) have rank \(0\) or \(1\).

The six maps in (9) commute pairwise: multiplying two expressions in (8), the
only possibly nonzero block is a scalar multiple of \(S\), symmetric in the two
parameter triples.  They include

\[
 N'=T_{0,1,0},\qquad M'=T_{1,0,0}.
\]

It follows that

\[
 |C_2(N',M')|=4,
 \qquad \{N',M'\}\cup C_2(N',M')\cong K_6
 \text{ monochromatic of colour }2.                     \tag{10}
\]

Equations (5) and (10) give the promised exact collision

\[
 \Sigma_2(N,M)=\Sigma_2(N',M'),                          \tag{11}
\]

although the first pair lies in one bare-flag fibre and the second does not.

## 4. Strategy disposition

The six vertices of a true fibre are indeed a colour-\(2\) clique, but (11)
shows that even its complete common-\(2\) core is not an intrinsic certificate:
nonzero commuting products create false six-vertex cores with identical induced
exact colours.  Therefore the authorized local-fibre gate fails and incidence
reconstruction was not begun.

A materially stronger, still unproved route would be
`RANK2-ALL-COLOUR-INTERSECTION-REFINEMENT`: classify for every colour-\(2\) pair
the full array

\[
 \bigl|\{T\in\mathcal D:|x_Px_T|=i,\ |x_Qx_T|=j\}\bigr|_{i,j}
\]

and then its coherent refinements.  The present collision neither verifies nor
refutes that route.  Starting it would be a new Lead decision, not a continuation
past the minute-12 kill gate.

## Scope and constraint matrix

| constraint id | role | result in this note |
|---|---|---|
| `21.52-forall-L-D` | admissibility | uncovered; the calculation is only a local obstruction in one admissible member of the rank-two family |
| `21.52-L-finite-nonabelian-simple` | admissibility | passes for \(L=\operatorname{PSL}_4(2)=\operatorname{GL}_4(2)\) |
| `21.52-D-single-involution-class` | admissibility | passes for the single Jordan class \(2^2\) |
| `21.52-Gamma-complete-on-D` | admissibility | the signature uses all vertices simultaneously adjacent in colour \(2\) to each specified pair |
| `21.52-edge-colour-exact-product-order` | admissibility | every claimed induced edge has exact product order \(2\); no finer product label is used |
| `21.52-tau-preserves-all-edge-colours` | admissibility | no arbitrary colour-preserving permutation is classified |
| `21.52-tau-induced-by-AutL` | target conclusion | not established, even for the rank-two family |

## What this does not establish

- It does not show that the six-element fibres are undefinable from all colours
  of the full graph.
- It does not determine the full colour-automorphism group of this class.
- It does not prove the rank-two \(\operatorname{PSL}_n(2)\) family partial.
- It does not prove or refute the universal Problem 21.52 assertion.
- It does not address Problem 21.53, a union of classes, an uncoloured graph, or
  product-conjugacy-class colours.
- No computation, web access, or extrapolation from rank one was used.

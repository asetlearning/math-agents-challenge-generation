---
title: "Kourovka 21.52 — rank-two square-zero involutions: decorated-flag obstruction"
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
direction: proof
strategy: LIN2-RANK2-NILPOTENT-INCIDENCE
outcome: PARTIAL_RESULT
target_object: "all finite nonabelian simple groups and all single involution classes"
witness_object: "the rank-two square-zero unipotent class in PSL_n(2), n>=4"
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

# Rank-two square-zero involutions: decorated-flag obstruction

## Outcome

`PARTIAL_RESULT`, together with a hard kill of the direct rank-one flag
reconstruction strategy.

For the rank-two square-zero class in

\[
L=\operatorname{PSL}_n(2)=\operatorname{GL}_n(2),\qquad n\geq4,
\]

the image/kernel flag does **not** determine a vertex.  It has a fibre of six
operator decorations, and the exact product order depends essentially on those
decorations.  Indeed, with the two bare flags held fixed, the product orders can
be \(3,5,\) or \(6\).  Moreover, colour \(2\) detects commutation
\(NM=MN\), not the stronger mutual-incidence condition \(NM=MN=0\); the former
can hold with a nonzero common product.  Thus the reviewed rank-one clique proof
cannot be transferred by replacing points and hyperplanes with 2-spaces and
codimension-2 spaces.

This does not show that the *full* coloured graph cannot recover the flag fibres
by a subtler local characterization.  That would be a new coherent-configuration
strategy, not the assigned bare-flag incidence strategy.

## 1. Vertices are decorated flags

Write a class member as \(x_N=I+N\), where

\[
N^2=0,\qquad \operatorname{rank}N=2.
\]

Put

\[
A_N=\operatorname{im}N,\qquad K_N=\ker N.
\]

Then \(\dim A_N=2\), \(\dim K_N=n-2\), and \(A_N\leq K_N\).  In addition to
this flag, \(N\) supplies the isomorphism

\[
\phi_N:V/K_N\longrightarrow A_N,qquad
v+K_N\longmapsto N(v).                                      \tag{1}
\]

Conversely, a flag \(A\leq K\) of these dimensions and an isomorphism
\(\phi:V/K\to A\) give exactly one such \(N\).  Therefore the fibre over every
bare flag has

\[
|\operatorname{GL}_2(2)|=6                                  \tag{2}
\]

vertices.  All these operators have Jordan type
\(2^2 1^{n-4}\), so they form one conjugacy class in \(L\).

For two vertices \(N,M\), the bare flags determine the ranks

\[
\operatorname{rank}(N|_{A_M})
 =2-\dim(A_M\cap K_N),\qquad
\operatorname{rank}(M|_{A_N})
 =2-\dim(A_N\cap K_M),                                    \tag{3}
\]

but not the two maps themselves, nor their compositions.  The missing datum is
precisely the pair of quotient-to-image isomorphisms in (1).

## 2. Exact general product-order reduction

Let

\[
g=x_Nx_M=(I+N)(I+M)=I+N+M+NM.                              \tag{4}
\]

Its inverse is \((I+M)(I+N)\), and characteristic two gives the useful exact
identity

\[
g+g^{-1}=NM+MN.                                            \tag{5}
\]

Let \(W=A_N+A_M\).  It is \(g\)-invariant, has dimension at most four, and
\(g\) induces the identity on \(V/W\).  Put \(h=g|_W\) and \(m=|h|\).  After
choosing any complement \(V=W\oplus Q\), write

\[
g=\begin{pmatrix}h&c\\0&I_Q\end{pmatrix},qquad c:Q\to W.
\]

Then

\[
g^m=
\begin{pmatrix}
I_W&(I+h+\cdots+h^{m-1})c\\0&I_Q
\end{pmatrix}.                                            \tag{6}
\]

Consequently the exact product order is

\[
|x_Nx_M|=
\begin{cases}
m,&(I+h+\cdots+h^{m-1})c=0,\\
2m,&(I+h+\cdots+h^{m-1})c\neq0.
\end{cases}                                                \tag{7}
\]

The criterion is independent of the chosen complement, since
\((I+h+\cdots+h^{m-1})(h-I)=h^m-I=0\).  Formula (7) reduces every pair to a
space of dimension at most four plus one extension bit.  It also exhibits the
obstruction: \(h\) and the extension class use the decorated maps, not merely
the four subspaces \(A_N,K_N,A_M,K_M\).

When \(A_N\cap A_M=0\), set

\[
p=N|_{A_M}:A_M\to A_N,qquad
q=M|_{A_N}:A_N\to A_M.
\]

On \(W=A_N\oplus A_M\), formula (4) becomes

\[
h=
\begin{pmatrix}
I+pq&p\\q&I
\end{pmatrix},qquad
h+h^{-1}=
\begin{pmatrix}
pq&0\\0&qp
\end{pmatrix}.                                            \tag{8}
\]

The ranks of \(p,q\) are the incidence numbers (3), but the similarity type of
\(pq\) is extra operator data.

## 3. Fixed flags give three different exact colours

First take \(n=4\) and write \(V=A\oplus B\) with
\(\dim A=\dim B=2\).  For \(P\in\operatorname{GL}_2(2)\), define

\[
N_P(a,b)=(Pb,0),\qquad M(a,b)=(0,a).                       \tag{9}
\]

Every \(N_P\) has the same image/kernel flag \((A,A)\), while \(M\) has the
fixed flag \((B,B)\).  Relative to \(A\oplus B\), if
\(g_P=(I+N_P)(I+M)\), then

\[
g_P+g_P^{-1}=\operatorname{diag}(P,P).                     \tag{10}
\]

There are three possible conjugacy types in
\(\operatorname{GL}_2(2)\cong S_3\):

1. If \(P=I\), (10) gives \(g_P^2+g_P+I=0\), so
   \(|g_P|=3\).
2. If \(P\) has order \(3\), then \(P^2+P+I=0\).  Substituting (10) and
   multiplying by \(g_P^2\) gives
   
   \[
   g_P^4+g_P^3+g_P^2+g_P+I=0,
   \]
   
   whence \(g_P^5=I\).  Since \(g_P\neq I\), its order is \(5\).
3. If \(P\neq I\) has order \(2\), then (10) squared gives
   \(g_P^4+g_P^2+I=0\), hence \(g_P^6=I\).  Its order is neither \(2\)
   (which would make \(g_P+g_P^{-1}=0\)) nor \(3\) (which would make that
   sum \(I\)), so its order is exactly \(6\).

For explicit representatives one may take

\[
I,\qquad
\begin{pmatrix}0&1\\1&1\end{pmatrix},qquad
\begin{pmatrix}1&1\\0&1\end{pmatrix}.                    \tag{11}
\]

For \(n>4\), extend all maps by zero on a common
\((n-4)\)-space \(Z\).  The fixed flags become
\((A,A\oplus Z)\) and \((B,B\oplus Z)\), and the same three exact product
orders remain.  Thus for every \(n\ge4\) no function of the two bare flags can
equal the edge colour.

## 4. Colour two is not mutual flag incidence

For distinct involutions,

\[
|x_Nx_M|=2
\quad\Longleftrightarrow\quad
x_Nx_M=x_Mx_N
\quad\Longleftrightarrow\quad
NM=MN.                                                     \tag{12}
\]

Mutual flag incidence would instead say

\[
A_N\leq K_M,\quad A_M\leq K_N
\quad\Longleftrightarrow\quad
MN=NM=0.                                                   \tag{13}
\]

The two conditions are genuinely different in rank two.  Again take
\(V=A\oplus B\), and put

\[
N=\begin{pmatrix}0&I\\0&0\end{pmatrix},qquad
M=\begin{pmatrix}R&0\\0&R\end{pmatrix},qquad
R=\begin{pmatrix}0&1\\0&0\end{pmatrix}.                  \tag{14}
\]

Both \(N\) and \(M\) square to zero and have rank two, while

\[
NM=MN=\begin{pmatrix}0&R\\0&0\end{pmatrix}\neq0.          \tag{15}
\]

Hence their edge has colour two although neither pair of image/kernel flags is
mutually incident as in (13).  Extending by zero gives the same example for
all $n>4$.

In particular, the rank-one step “colour-two cliques are exactly subspace
sandwiches” has no direct rank-two analogue: colour two fuses zero-product
incidence configurations with additional nonzero commuting configurations.

## 5. Strategy disposition and precise next pivot

The assigned strategy required the exact edge colour to descend to an
image/kernel-flag relation from which ambient projective incidence could be
reconstructed.  Sections 3--4 disprove that prerequisite, so
`LIN2-RANK2-NILPOTENT-INCIDENCE` is exhausted at its hard gate.

A materially different possible strategy is
`RANK2-DECORATED-FLAG-FIBRE-QUOTIENT`: attempt to characterize, solely from
local coloured intersection numbers, the six vertices above each flag, then
quotient by those fibres and recover the \(2\)-space/codimension-\(2\) incidence
geometry.  Nothing here proves that these fibres are graph-theoretically
definable, so this is only a proposed pivot and was not started.

## Scope and constraint matrix

| constraint id | role | result in this note |
|---|---|---|
| `21.52-forall-L-D` | admissibility | uncovered; one involution family only |
| `21.52-L-finite-nonabelian-simple` | admissibility | passes for \(L=\operatorname{PSL}_n(2)\), \(n\ge4\) |
| `21.52-D-single-involution-class` | admissibility | passes for Jordan type \(2^2 1^{n-4}\) |
| `21.52-Gamma-complete-on-D` | admissibility | pair lemmas apply to every distinct pair in this class |
| `21.52-edge-colour-exact-product-order` | admissibility | formulas (4)--(8), with exact fixed-flag colours (9)--(11) |
| `21.52-tau-preserves-all-edge-colours` | admissibility | no arbitrary colour-preserving permutation classified |
| `21.52-tau-induced-by-AutL` | target conclusion | not established, even for this rank-two family |

The universal Problem 21.52 target remains open.  Problem 21.53, unions of
involution classes, conjugacy-class colours, and bounded evidence as a universal
proof were not used.

## What this does not establish

- It does not determine the full colour-automorphism group of the rank-two class.
- It does not show that the six-element flag fibres are undefinable in the full
  coloured graph.
- It does not prove or refute the universal statement.
- It does not address any other simple group or any other involution class.
- No computation, web search, or extrapolation from the rank-one proof was used.

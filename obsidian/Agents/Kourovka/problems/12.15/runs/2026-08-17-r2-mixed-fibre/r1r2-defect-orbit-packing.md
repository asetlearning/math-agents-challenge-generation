---
title: "Kourovka 12.15 — complete R1/R2 defect-orbit packing table"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/group-actions
  - project/kourovka
  - status/conjectured
problem: "12.15"
scope_id: 12.15/normal-closure-fibres
assignment_revision: 1
direction: proof
outcome: PARTIAL_RESULT
state: awaiting_lead
---

# Boundary

This note exhausts the finite **R1R2-DEFECT-ORBIT-PACKING** abstraction requested by Lead. Compatible tables remain, so it does not eliminate R1 or R2 and does not assert that any full extension \(G\) exists.

# Common notation and exact fibre calculation

Let

\[
H=G',\qquad A=Z(H),\qquad V=H/A\cong C_2^2,\qquad E=G/H.
\]

The reviewed least-counterexample core gives \(H'=\langle z\rangle=:Z\le Z(G)\). Let

\[
\rho:E\longrightarrow \operatorname{Sp}(V)\cong S_3
\]

be the induced action. In R1 and R2 its image has order at most \(2\). If the image is nontrivial, write it as \(\langle T\rangle\) and put

\[
F=\ker(T-1)=\operatorname{im}(T-1),
\]

the unique fixed line of \(T\).

For a nonidentity basic commutator \(c\in H\), set

\[
v=cA,\qquad N=\langle c\rangle^G,\qquad
D=D_G(c)=N^2[N,G].
\]

Then the following are exact:

\[
W:=NA/A=\langle \rho(E)v\rangle,\qquad
L:=DA/A=[W,E]. \tag{1}
\]

Indeed, \(H\) acts trivially on \(V\), squares vanish in \(V\), and projection of \([N,G]\) is \([W,E]\). The fibre lemma gives \(|N:D|=2\). In every noncentral case the reviewed least-counterexample core gives \(Z\le D\). Put

\[
B=N\cap A.
\]

Since \(|W:L|=2\) in each noncentral row below, comparison with \(|N:D|=2\) yields

\[
D\cap A=B. \tag{2}
\]

Thus \(B\), \(W\), and \(L\) determine the exact orders of \(N,D\), the projected orbit, and the projected defect.

# Complete single-commutator table

Here \(S\) means a nonzero fixed-line image and \(M\) a moving image. In an \(M\)-row, \(v^E=\{v,Tv\}=\{v,v+f\}\) with \(0\ne f\in F\).

| type of \(c\) | condition | \(N\) | \(D\) | \(W=NA/A\) | \(L=DA/A\) | \(|c^G|=|D|\) |
|---|---|---|---|---|---|---:|
| identity | \(c=1\) | \(1\) | \(1\) | \(0\) | \(0\) | 1 |
| central \(Z\) | \(c=z\) | \(Z\) | \(1\) | \(0\) | \(0\) | 1 |
| central moving, R2 only | \(c\in A\setminus Z\) | \(A\) | \(Z\) | \(0\) | \(0\) | 2 |
| \(S(B)\) | \(0\ne v\in V^E\) | \(|N|=2|B|\) | \(D=B\) | \(\langle v\rangle\) | \(0\) | \(|B|\) |
| \(M(B)\) | \(\rho(E)=\langle T\rangle,\ v\notin F\) | \(|N|=4|B|\) | \(|D|=2|B|\), \(DA/A=F\) | \(V\) | \(F\) | \(2|B|\) |

The possible kernels are:

- R1: \(A=Z\), so every noncentral row has \(B=A=Z\).
- R2: \(A\cong C_4\) or \(C_2^2\), and every noncentral row has \(B=Z\) or \(B=A\). These are the only \(E\)-invariant subgroups of \(A\) containing \(Z\).

Consequently the numerical rows are:

| regime | row | \(B\) | \(|N|\) | \(|D|=|c^G|\) |
|---|---|---:|---:|---:|
| R1 | \(S\) | 2 | 4 | 2 |
| R1 | \(M\) | 2 | 8 | 4 |
| R2 | \(S(Z)\) | 2 | 4 | 2 |
| R2 | \(S(A)\) | 4 | 8 | 4 |
| R2 | \(M(Z)\) | 2 | 8 | 4 |
| R2 | \(M(A)\) | 4 | 16 | 8 |

For the two R2 centre types, the nontrivial action on \(A\) is also unique up to automorphism:

- \(A=C_4=\langle a\rangle\): inversion \(a\mapsto a^{-1}=az\), with \(z=a^2\);
- \(A=C_2^2=\langle a,z\rangle\): the shear \(a\mapsto az,\ z\mapsto z\).

Hence \(c\in A\setminus Z\) has orbit \(cZ\), normal closure \(A\), and defect \(Z\), as recorded in the table.

# Packing the basic commutators in \(V\)

Choose a minimal generating set \(x_1,\ldots,x_d\) lifting a basis of \(E\), and put

\[
w_{ij}=[x_i,x_j]A\in V.
\]

Their \(E\)-orbits must span \(V\), because the basic commutators normally generate \(G'=H\).

If \(\rho\) is trivial, this condition is exactly

\[
\langle w_{ij}:i<j\rangle=V. \tag{3}
\]

Thus at least two distinct nonzero lines occur.

If \(\rho\) is nontrivial, encode it by a nonzero character

\[
\chi:E\to C_2,\qquad \rho(e)=T^{\chi(e)}.
\]

Choose a basis \(e_0,e_1,\ldots,e_{d-1}\) with \(\chi(e_0)=1\) and \(e_i\in\ker\chi\) for \(i>0\). The projected Hall--Witt identity gives

\[
\chi(e_k)(T-1)w_{ij}
+\chi(e_i)(T-1)w_{jk}
+\chi(e_j)(T-1)w_{ki}=0. \tag{4}
\]

This has the required commutator convention. In the Hall--Witt factor
\([[x_i,x_j^{-1}],x_k]^{x_j}\), one has
\([x_i,x_j^{-1}]=[x_j,x_i]^{x_j^{-1}}\). Modulo \(A\), inversion is invisible because \(V\) has exponent \(2\), and the outer conjugation by \(x_j\) cancels the inner \(\rho(e_j)^{-1}\). The factor therefore projects to
\((\rho(e_k)-1)w_{ij}\). The other two cyclic factors give (4).

For \(i,j>0\), apply (4) to \((e_0,e_i,e_j)\):

\[
(T-1)w_{ij}=0,\qquad\text{so }w_{ij}\in F. \tag{5}
\]

The cross terms are also fixed, by the square identity that the Hall--Witt-only test misses. Since \(E\) is elementary abelian, \(x_0^2\in H\). The element \(x_i\) acts trivially on \(V\), so

\[
[x_0^2,x_i]A=0.
\]

On the other hand, the exact identity

\[
[x_0^2,x_i]=[x_0,x_i]^{x_0}[x_0,x_i]
\]

projects to

\[
(T-1)w_{0i}=0,\qquad\text{so }w_{0i}\in F. \tag{6}
\]

Equations (5)--(6) put **every** basic commutator image in \(F\). Their normal closures therefore project into \(F\) and cannot normally generate \(H/A=V\). Consequently

\[
\rho(E)\ne1\quad\text{is impossible in both R1 and R2}. \tag{7}
\]

The only surviving action on \(V\) is trivial, and its exact packing criterion is (3).

# Complete finite action/configuration table

For R2, let \(\psi:E\to C_2\) be the nonzero character giving the action on \(A\). Up to change of basis in \(E\), the relative possibilities are \(\chi=0\), \(\chi=\psi\), and \(0\ne\chi\ne\psi\). No reviewed row excludes any of them.

| regime | \(A\) | action on \(A\) | action on \(V\) | allowed basic-image table | exact \(V\)-generation test | surviving packing |
|---|---|---|---|---|---|---|
| R1, \(d=4\) | \(C_2=Z\) | trivial | \(\chi=0\) | six arbitrary \(w_{ij}\in V\) | their span is \(V\) | yes: \(w_{12}=u,w_{13}=v\), rest \(0\) |
| R1, \(d=4\) | \(C_2=Z\) | trivial | \(0\ne\chi\) | (5)--(6) force all six values into \(F\) | cannot span \(V\) | **eliminated** |
| R2, \(d=3\) | \(C_4\) | inversion, \(\psi\ne0\) | \(\chi=0\) | three arbitrary \(w_{ij}\in V\) | their span is \(V\) | yes: two independent \(S(A)\) rows |
| R2, \(d=3\) | \(C_4\) | inversion | \(\chi=\psi\) | all three values forced into \(F\) | cannot span \(V\) | **eliminated** |
| R2, \(d=3\) | \(C_4\) | inversion | \(0\ne\chi\ne\psi\) | all three values forced into \(F\) | cannot span \(V\) | **eliminated** |
| R2, \(d=3\) | \(C_2^2\) | shear, \(\psi\ne0\) | \(\chi=0\) | three arbitrary \(w_{ij}\in V\) | their span is \(V\) | yes: two independent \(S(A)\) rows |
| R2, \(d=3\) | \(C_2^2\) | shear | \(\chi=\psi\) | all three values forced into \(F\) | cannot span \(V\) | **eliminated** |
| R2, \(d=3\) | \(C_2^2\) | shear | \(0\ne\chi\ne\psi\) | all three values forced into \(F\) | cannot span \(V\) | **eliminated** |

The three surviving trivial-action rows satisfy every reviewed action-size condition. Every noncentral basic commutator is of type \(S(B)\); no \(M\)-row survives the square/Hall--Witt compatibility check.

# The remaining central packing bit in R2

Let \(N_{ij}=\langle[x_i,x_j]\rangle^G\) and \(K=\prod_{i<j}N_{ij}\). The projected criteria above are exactly \(KA/A=V\). In R1 this already gives \(K=H\), because \(A=Z\le K\).

In R2, after \(KA/A=V\), one further binary condition remains:

\[
K=H
\quad\Longleftrightarrow\quad
K\cap A=A. \tag{9}
\]

It is automatically satisfied if any noncentral row has \(B=A\), or if a central basic commutator lies in \(A\setminus Z\). If every row has \(B=Z\), pass to the abelian group \(\bar H=H/Z\). Each \(\bar N_{ij}\) is a lift of its projected subspace \(W_{ij}\), and the only unresolved datum is whether the sum of these lifts contains the one-dimensional kernel \(A/Z\). Record it as

\[
\delta=\dim_{\mathbf F_2}\bigl((K\cap A)/Z\bigr)\in\{0,1\}. \tag{10}
\]

The basic commutators normally generate \(H\) exactly when \(\delta=1\). The reviewed action-size rows do not determine this lift-offset bit. Thus even the all-\(B=Z\) patterns are not eliminated; they divide into \(\delta=0\) and \(\delta=1\) abstract tables.

# Outcome

The nominal nontrivial \(V\)-action branches are eliminated by (5)--(7). Compatible defect-orbit packings nevertheless remain for every centre type in the trivial-action branch:

- use two independent fixed-line normal closures to span \(V\);
- in R2, choose \(B=A\) in one such row (or set the residual offset bit \(\delta=1\)) to pack the extra central quotient.

Therefore this method yields the genuine restriction that \(E\) acts trivially on \(H/A\), but it does not eliminate R1 or R2. Its remaining exact obstruction is that the action bounds control only \(W\) and \(L=[W,E]\); they do not control \(B=N\cap A\) or the R2 lift-offset bit \(\delta\). Those undetermined central data are precisely what decides whether the basic normal closures fill \(H\).

This is a finite necessary-condition table, not a reconstructed group, a counterexample, or a proof of the active scope.

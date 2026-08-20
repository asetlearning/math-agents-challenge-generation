---
title: "Kourovka 12.15 — R1/R2 pc consistency and fibre witness"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/commutator-calculus
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

This executes **R1R2-PC-CONSISTENCY-AND-FIBRE-WITNESS** on the explicit central tables in [[r1r2-central-layer-polarization]].  It eliminates R1 by pc consistency, eliminates the whole cyclic-centre R2 branch by the square critical pair, and materializes one elementary-centre R2 table before excluding that materialization by an explicit source-hypothesis witness.  It does not classify every exact central offset in the remaining (A=C_2^2) family.

Throughout,

\[
[a,b]=a^{-1}a^b=a^{-1}b^{-1}ab.
\]

# R1: both displayed rows fail pc consistency

Write

\[
H=\langle u,v,z\rangle,qquad [u,v]=z,qquad z^2=1,
\]

with (u^2=v^2=1) in the (D_8) row and (u^2=v^2=z) in the (Q_8) row.  Let (x_1,\ldots,x_4) lift a basis of (E=G/H\cong C_2^4).  Up to the central lift bits, the displayed rows prescribe

\[
[x_1,x_2]Z=uZ,qquad [x_1,x_3]Z=vZ,qquad x_i^2\in Z. \tag{R1-pc}
\]

The conjugation rows are

\[
D_8:\quad [u,x_i]=[v,x_i]=1, \tag{R1-D}
\]

and

\[
\begin{array}{c|cccc}
 &x_1&x_2&x_3&x_4\\ \hline
[u,x_i]&z&z&1&1\\
[v,x_i]&z&1&z&1.
\end{array} \tag{R1-Q}
\]

These are not merely locally underdetermined tables.  Every automorphism of (D_8) or (Q_8) which fixes (Z) and acts trivially on (H/Z) is inner.  Convention-explicit choices for (R1-Q) are

\[
h_1=uv,qquad h_2=v,qquad h_3=u,qquad h_4=1,
\]

so conjugation by (x_i) on (H) equals conjugation by (h_i).  (For (R1-D), use the corresponding inner elements; in the displayed zero-action row all (h_i=1).)  Therefore

\[
c_i=x_i h_i^{-1}\in C_G(H),qquad G=H C_G(H). \tag{R1-C}
\]

As (H\cap C_G(H)=Z(H)=Z),

\[
G'=[H C_G(H),H C_G(H)]\le H'\,(C_G(H))'\le Z,
\]

contrary to (G'=H\not\le Z).  In pc language, after replacing (x_i) by (c_i h_i), every commutator of two quotient lifts collects into (Z), contradicting the two nonzero rows of (R1-pc).  This is the complete associativity obstruction and is independent of all central square and commutator lift bits.  Thus both the (D_8) and (Q_8) R1 rows are eliminated.

# R2 with (A=C_4): the square critical pair eliminates the branch

Let (A=\langle a\rangle\cong C_4), (z=a^2), and let (psi:E\to C_2) encode inversion on (A).  For (x\in G) and (h\in H), put

\[
[h,x]=\lambda_x(hA)\in A.
\]

The already derived conjugation-square row says

\[
\lambda_x(v)Z=\psi(xH)\,\bar q(v). \tag{C4-P3}
\]

Now collect (h^{x^2}) in the two cases.  If (psi(xH)=1), (x) inverts (A), and hence

\[
h^{x^2}=h\lambda_x(v)\lambda_x(v)^x=h.
\]

If (psi(xH)=0), (C4-P3) gives (lambda_x(v)\in Z), so again

\[
h^{x^2}=h\lambda_x(v)^2=h.
\]

Thus (x^2\in C_H(H)=A) for every (x\in G).  Applying this to (x,y,xy) and collecting modulo (A) forces

\[
[x,y]\in A\qquad(x,y\in G).
\]

Consequently (G'\le A), contrary to (G'=H) and (H/A\cong C_2^2).  This kills both the displayed (B=A) cyclic-centre table and the formerly free all-(B=Z) cyclic-centre offset; the offset cannot pass the full square pc critical pair.

# R2 with (A=C_2^2): one exact materialization

The elementary-centre branch behaves differently.  Here is a complete consistent presentation.  All omitted commutators are (1):

\[
\begin{aligned}
G_0=\langle z,a,u,v,r,k,l\mid{}&
z^2=a^2=u^2=v^2=r^2=k^2=l^2=1,\\
&z\in Z(G_0),\quad [a,u]=[a,v]=[a,k]=[a,l]=1,\quad [a,r]=z,\\
&[u,v]=z,\quad [u,r]=[v,r]=1,\\
&[u,k]=1,\quad [v,k]=a,\quad [u,l]=az,\quad [v,l]=1,\\
&[r,k]=u,\quad [r,l]=v,\quad [k,l]=1\rangle . \tag{EA-pc}
\end{aligned}
\]

The factor (z) in ([u,l]=az) is forced by the exact Hall--Witt/collection overlap; omitting it collapses (z).  With it, pc conversion gives a group of order (128), with

\[
H=G_0'=\langle z,a,u,v\rangle\cong D_8\times C_2,quad |H|=16,
\]

\[
Z(G_0)=\langle z\rangle,qquad G_0/H\cong C_2^3,qquad \operatorname{cl}(G_0)=4.
\]

The seven relative orders are all (2), so the presentation has (2^7) collected normal forms.  The independently computed pc quotient also has order (128); hence no generator or normal form collapses and all associativity critical pairs close.  The exact bounded verification is in [[scratch/r2_ea_candidate.g]] and [[scratch/r2_ea_candidate.out]].

Modulo (A=\langle a,z\rangle), this table has

\[
w(r,k)=uA,qquad w(r,l)=vA,qquad w(k,l)=0,qquad p(r)=p(k)=p(l)=0,
\]

and the only nonzero \(\bar\tau\)-values are

\[
\bar\tau(vA,kH)=1,qquad \bar\tau(uA,lH)=1.
\]

Thus both independent commutator rows have (B=A).  This also records the pc repair to the earlier merely local example: the action-square critical pair forces the basis-square images to be zero, while Hall--Witt forces the displayed (z)-offset.

# Explicit failure of the source hypothesis

In (G_0), set

\[
x=r,qquad y=ruv.
\]

Because (r) centralizes (u,v),

\[
|x|=2,qquad y^2=(uv)^2=z,qquad |y|=4.
\]

They therefore cannot be conjugate.  Their normal closures nevertheless agree.  From (EA-pc),

\[
[r,k]=u,quad [r,l]=v,quad [v,k]=a,quad [u,v]=z,
\]

so

\[
\langle x\rangle^{G_0}=\langle r,u,v,a,z\rangle=\langle r,H\rangle. \tag{Nx}
\]

For (y), direct collection gives

\[
[y,a]=z,qquad [y,k]=uaz,qquad [y,l]=va.
\]

Normality then supplies

\[
[uaz,l]=az,
\]

so (z,a,u,v\in\langle y\rangle^{G_0}), and then (r=y(uv)^{-1}) also belongs to it.  Hence

\[
\langle y\rangle^{G_0}=\langle r,H\rangle=\langle x\rangle^{G_0},qquad |\langle r,H\rangle|=32. \tag{Ny}
\]

For the requested class calculation, collection gives

\[
C_{G_0}(x)=\langle r,u,uv,z\rangle,qquad
C_{G_0}(y)=\langle r,uaz,uv,z\rangle,
\]

both of order (16).  Therefore

\[
|x^{G_0}|=|y^{G_0}|=128/16=8,
\]

while the different element orders show that the two classes are disjoint.  Thus (EA-pc) is a genuine order-(128) realization of the local table, but it explicitly fails the source hypothesis.

# Residual

R1 and the entire (A=C_4) R2 branch are eliminated.  One exact (A=C_2^2), (B=A) realization is excluded by the explicit pair above.  What remains unclassified by this increment is whether every allowed elementary-centre central-offset table is pc-equivalent to this mechanism (and hence has a uniform fibre witness), or whether another exact offset family survives.  No catalogue or HAP computation was used.

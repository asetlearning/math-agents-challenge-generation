---
title: "Kourovka 12.15 — R1/R2 central-layer polarization table"
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

# Boundary and accepted input

This is the convention-explicit finite table for **R1R2-CENTRAL-LAYER-POLARIZATION**. It uses the bounded submitted restriction

\[
[H,G]\le A=Z(H),
\]

equivalently that \(E=G/H\) acts trivially on \(V=H/A\). Compatible central tables remain. This note therefore neither eliminates R1/R2 nor answers the universal scope.

# Common commutator and square data

Use

\[
[a,b]=a^{-1}a^b=a^{-1}b^{-1}ab.
\]

Choose lifts \(x_1,\ldots,x_d\) of a basis of \(E\), and put

\[
c_{ij}=[x_i,x_j],\qquad
w_{ij}=c_{ij}A\in V,\qquad
s_i=x_i^2\in H,\qquad
p_i=s_iA\in V,
\]

\[
t_{ij,k}=[c_{ij},x_k]\in A,\qquad
q_{ij}=c_{ij}^2\in A.
\]

The exact power identities are

\[
[s_i,x_j]=q_{ij}t_{ij,i}, \tag{P1}
\]

\[
[s_j,x_i]^{-1}=q_{ij}t_{ij,j}. \tag{P2}
\]

For any \(h\in H\), \(x\in G\), and \(a=[h,x]\in A\), compatibility of conjugation with squares also gives

\[
(h^2)^x=(h^x)^2=(ha)^2=h^2a^2. \tag{P3}
\]

Indeed, the fixed product convention gives

\[
[x_i^2,x_j]=[x_i,x_j]^{x_i}[x_i,x_j],
\qquad
[x_i,x_j^2]=[x_i,x_j][x_i,x_j]^{x_j}.
\]

The Hall--Witt identity is used in the form

\[
[[x_i,x_j^{-1}],x_k]^{x_j}
[[x_j,x_k^{-1}],x_i]^{x_k}
[[x_k,x_i^{-1}],x_j]^{x_i}=1. \tag{HW}
\]

# R1: \(A=Z=\langle z\rangle\)

Identify \(Z\) with \(\mathbf F_2\). Since \(A\le Z(G)\), the central action map

\[
\tau:V\times E\to\mathbf F_2,\qquad
[h,x]=z^{\tau(hA,xH)}
\]

is well defined and bilinear. Let

\[
q:V\to\mathbf F_2,\qquad h^2=z^{q(hA)}
\]

be the quadratic square map of \(H=D_8\) or \(Q_8\); its polar form is the nondegenerate commutator form on \(V\).

The entire central table is:

\[
t_{ij,k}=\tau(w_{ij},e_k),\qquad q_{ij}=z^{q(w_{ij})}, \tag{R1-data}
\]

\[
\tau(w_{ij},e_k)+\tau(w_{jk},e_i)+\tau(w_{ki},e_j)=0, \tag{R1-HW}
\]

\[
\tau(p_i,e_j)=q(w_{ij})+\tau(w_{ij},e_i), \tag{R1-P1}
\]

\[
\tau(p_j,e_i)=q(w_{ij})+\tau(w_{ij},e_j). \tag{R1-P2}
\]

There is no hidden sign: every value has order \(2\), so the inverse in (P2) disappears after identifying \(Z\) with \(\mathbf F_2\).

Both possible groups \(H\) admit compatible tables:

| \(H\) | nonzero basic images | \(p_i\) | nonzero values of \(\tau\) | check |
|---|---|---|---|---|
| \(D_8\) | \(w_{12}=u,\ w_{13}=v\), with independent isotropic \(u,v\) | all \(0\) | none | \(q(u)=q(v)=0\), so all R1 equations vanish |
| \(Q_8\) | \(w_{12}=u,\ w_{13}=v\) | all \(0\) | \(\tau(u,e_1)=\tau(u,e_2)=1\); \(\tau(v,e_1)=\tau(v,e_3)=1\) | \(q(u)=q(v)=1\); R1-P1/P2 cancel and R1-HW is \(0\) on every triple |

All omitted \(w_{ij}\) and \(\tau\)-values are \(0\). In both rows the two fixed-line normal closures have order \(4\), defect \(Z\), and product \(H\). Thus central polarization does not eliminate R1.

# R2: common quotient table for \(A=C_4\) and \(C_2^2\)

Put

\[
\bar A=A/Z\cong C_2.
\]

The nontrivial action on \(A\) is described uniformly by a nonzero character
\(\psi:E\to C_2\) and a nonzero map

\[
\nu:\bar A\longrightarrow Z,
\qquad
[a,x]=\psi(xH)\,\nu(aZ). \tag{A-action}
\]

For \(A=C_4\), this is inversion and \(\nu(aZ)=a^2=z\). For \(A=C_2^2\), this is the shear \(a\mapsto az\).

Modulo \(Z\), the triple commutator depends only on \(v=hA\):

\[
\bar\tau:V\times E\to\bar A,\qquad
\bar\tau(hA,xH)=[h,x]Z.
\]

It is bilinear. The square map

\[
\bar q:V\to\bar A,\qquad \bar q(hA)=h^2Z
\]

is linear, because its polar commutator lies in \(H'=Z\). Reducing (HW), (P1), and (P2) modulo \(Z\) gives the complete visible central table:

\[
\bar t_{ij,k}=\bar\tau(w_{ij},e_k),\qquad
\bar q_{ij}=\bar q(w_{ij}), \tag{R2-data}
\]

\[
\bar\tau(w_{ij},e_k)+\bar\tau(w_{jk},e_i)+\bar\tau(w_{ki},e_j)=0, \tag{R2-HW}
\]

\[
\bar\tau(p_i,e_j)=\bar q(w_{ij})+\bar\tau(w_{ij},e_i), \tag{R2-P1}
\]

\[
\bar\tau(p_j,e_i)=\bar q(w_{ij})+\bar\tau(w_{ij},e_j). \tag{R2-P2}
\]

Equation (P3) adds one centre-type distinction. If \(A=C_2^2\), then \(a^2=1\) for every \(a\in A\), so every square \(h^2\) is fixed by the nontrivial shear on \(A\). Since \(A^E=Z\),

\[
A=C_2^2\quad\Longrightarrow\quad \bar q=0. \tag{R2-EA-square}
\]

For \(A=C_4\), an element outside \(Z\) has square \(z\), exactly allowing (P3) to match inversion. Applying the square map \(A/Z\to Z\) to (P3) gives the exact relation

\[
A=C_4\quad\Longrightarrow\quad
\bar\tau(v,e)=\psi(e)\bar q(v). \tag{R2-C4-P3}
\]

Thus \(\bar q\) need not vanish, but it determines \(\bar\tau\).

For a noncentral basic commutator, these data recover its individual fibre kernel:

\[
N_{ij}\cap A=A
\quad\Longleftrightarrow\quad
\bar q(w_{ij})\ne0
\ \text{or}\ 
\bar\tau(w_{ij},E)\ne0. \tag{B-test}
\]

If both terms vanish, \(N_{ij}\cap A=Z\). This is just
\(D=N^2[N,G]\), projected to \(A/Z\).

The table is nonempty for both centre types. Fix a basis with
\(\psi(e_1)=1\), \(\psi(e_2)=\psi(e_3)=0\), and use

\[
w_{12}=u,\qquad w_{13}=v,\qquad w_{23}=0.
\]

Compatible \(S(A)\)-tables are:

| centre | \(\bar q\) | nonzero \(\bar\tau\)-values | \(p_1,p_2,p_3\) |
|---|---|---|---|
| \(C_4\) | \(\bar q(u)=\bar q(v)=1\) | \(\bar\tau(u,e_1)=\bar\tau(v,e_1)=1\) | \(0,u,v\) |
| \(C_2^2\) | \(0\) | the same four values | \(u+v,u,v\) |

In the second row, “the same four values” means
\(\bar\tau(u,e_1)=\bar\tau(u,e_2)=
\bar\tau(v,e_1)=\bar\tau(v,e_3)=1\).
All omitted values are \(0\). Direct substitution gives R2-HW, both R2-P equations, and the appropriate P3 row. In the elementary-abelian-centre row, every \(q_{ij}\) may be chosen in \(Z\) and every triple factor has square \(1\). In the cyclic-centre row, R2-C4-P3 holds: inversion of a square outside \(Z\) is compensated by the square \(z\) of the active triple factor.

In either row the two independent commutators are \(S(A)\)-rows. Their normal closures have order \(8\) and product \(H\). Hence neither \(A=C_4\) nor \(A=C_2^2\) is eliminated.

# Exact residual lift-offset parameter in R2

The all-\(B=Z\) table has

\[
\bar q(w_{ij})=0,\qquad \bar\tau(w_{ij},E)=0
\]

for every basic commutator. Choose a section of the abelian extension

\[
0\to A/Z\to H/Z\to V\to0
\]

and write

\[
c_{ij}Z=\sigma(w_{ij})+\alpha_{ij},
\qquad \alpha_{ij}\in A/Z. \tag{lift}
\]

To see exactly what the full \(Z\)-valued identities detect, compare two tables and let \(\alpha_{ij}\in\mathbf F_2\) record multiplication of \(c_{ij}\) by a fixed \(a\in A\setminus Z\). Let \(\beta_i\in\mathbf F_2\) similarly record multiplication of the square lift \(s_i\) by \(a\). The changes in the central rows are

\[
t_{ij,k}\longmapsto t_{ij,k}\,z^{\alpha_{ij}\psi(e_k)}, \tag{shift-t}
\]

and

\[
q_{ij}\longmapsto
\begin{cases}
q_{ij}z^{\alpha_{ij}},&A=C_4,\\
q_{ij},&A=C_2^2.
\end{cases} \tag{shift-q}
\]

Choose the basis so that \(\psi(e_1)=1\) and \(\psi(e_2)=\psi(e_3)=0\). The \(Z\)-part of (HW) gives

\[
\alpha_{23}=0. \tag{shift-HW}
\]

Write \(\varepsilon=1\) for \(A=C_4\) and \(\varepsilon=0\) for \(A=C_2^2\). The variations of (P1)--(P2) are exactly

\[
\psi(e_j)\beta_i=(\varepsilon+\psi(e_i))\alpha_{ij},
\qquad
\psi(e_i)\beta_j=(\varepsilon+\psi(e_j))\alpha_{ij}. \tag{shift-P}
\]

Therefore:

| centre | solutions of shift-HW/P | consequence for the all-\(B=Z\) offset |
|---|---|---|
| \(C_4\) | \(\alpha_{12},\alpha_{13}\) are free, \(\alpha_{23}=0\), with \(\beta_2=\alpha_{12}\), \(\beta_3=\alpha_{13}\) | one relation-offset bit can survive |
| \(C_2^2\) | \(\alpha_{12}=\alpha_{13}=\alpha_{23}=0\) | the offset is fixed |

In the all-\(B=Z\) branch, \(\bar q=0\), so \(H/Z\) is elementary abelian and the section \(\sigma\) may be chosen linear. For \(A=C_2^2\), the second row then gives

\[
\delta=0;
\]

the all-\(B=Z\) packing cannot normally generate \(H\). For \(A=C_4\), take \(w_{12}=u\), \(w_{13}=v\), \(w_{23}=u+v\). The unique relation uses all three values, while shift-HW only forces \(\alpha_{23}=0\). Choosing \(\alpha_{12}+\alpha_{13}=1\) gives

\[
\delta=1.
\]

Thus the cyclic-centre offset genuinely survives the complete identities.

If \(K\) is the product of the basic normal closures, then

\[
\delta=\dim_{\mathbf F_2}((K\cap A)/Z)
\]

is obtained by evaluating the allowed \(\alpha_{ij}\) (and the fixed section factor) on relations among the \(w_{ij}\). Normal generation requires \(\delta=1\).

# Outcome

Central-layer Hall--Witt and square polarization do not kill the surviving trivial-action packings:

- R1 has explicit compatible \(D_8\) and \(Q_8\) tables.
- Both R2 centre types have compatible \(B=A\) tables, so neither regime is eliminated.
- In the all-\(B=Z\) branch, polarization forces \(\delta=0\) for \(A=C_2^2\), but a one-bit \(\delta\) survives for \(A=C_4\).

More precisely, let

\[
\omega:\mathbf F_2^{\binom d2}\to V,\qquad
\epsilon_{ij}\mapsto w_{ij},\qquad R=\ker\omega.
\]

After fixing the section \(\sigma\), the residual is the affine functional

\[
\Delta_\alpha:R\to A/Z,\qquad
(\lambda_{ij})\longmapsto
\sum_{i<j}\lambda_{ij}\alpha_{ij}
+\kappa_\sigma(\lambda), \tag{residual}
\]

where \(\kappa_\sigma(\lambda)\) is the fixed central correction obtained when the section lifts with total projected value \(0\) are multiplied. Its image is \((K\cap A)/Z\), so \(\delta=\dim\operatorname{im}\Delta_\alpha\). Equations shift-HW/P kill this functional in the elementary-abelian-centre all-\(B=Z\) row and leave one cyclic-centre bit. Further progress on the surviving \(B=A\) rows or cyclic-centre bit requires an exact factor-set compatibility argument outside this method; no such new method was started.

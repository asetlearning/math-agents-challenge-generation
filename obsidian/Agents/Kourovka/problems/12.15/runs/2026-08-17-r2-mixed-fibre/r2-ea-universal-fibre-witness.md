---
title: "Kourovka 12.15 — universal elementary-centre R2 fibre witness"
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

# Claim boundary

Assuming the reviewed order-\(128\) R2 data and the submitted restriction that \(E=G/H\) acts trivially on \(V=H/A\), every pc-consistent elementary-centre row \(A=C_2^2\) has an explicit pair with equal normal closure and different orders. Thus no such row satisfies the source hypothesis. Together with the review-pending R1 and cyclic-centre arguments, this would eliminate the order-\(128\) remainder only; it does not address larger orders or prove the full problem.

Use

\[
[a,b]=a^{-1}a^b,\qquad
A=\langle a,z\rangle\cong C_2^2,\qquad H'=\langle z\rangle,
\]

and let

\[
b:V\times V\longrightarrow \langle z\rangle\cong\mathbf F_2
\]

be the nondegenerate commutator form. Let

\[
\psi:E\to\mathbf F_2
\]

describe the action \(a^x=az^{\psi(xH)}\), and put \(K=\ker\psi\), so \(\dim K=\dim V=2\).

# Normal form covering every surviving table

For a lift \(x_e\) of \(e\in E\), write

\[
\bar\tau_e(v)=[h,x_e]Z\in A/Z\qquad(hA=v).
\]

If \(e\in K\), then \(x_e\) fixes the elementary abelian group \(A\), so applying its conjugation twice gives

\[
x_e^2\in A. \tag{1}
\]

Choose \(rH\notin K\). The functional \(\bar\tau_r\in V^*\) is symplectically represented by a unique vector of \(V\). Multiplying \(r\) by a lift of that vector changes its action by the corresponding inner automorphism, so we may and do normalize

\[
\bar\tau_r=0. \tag{2}
\]

Then conjugation by \(r\) squares trivially on \(H\), hence \(r^2\in A\). Since \(r\) must fix its own square while it shears \(a\), actually

\[
r^2=z^R\quad(R\in\mathbf F_2). \tag{3}
\]

For \(k\in K\), define \(L(k)\in V\) by

\[
\bar\tau_k(v)=b(v,L(k)). \tag{4}
\]

Apply the action-square identity to \(rk\). Its square vector is \(L(k)\), whereas (1)--(3) and square polarization identify that vector with \([r,k]A\). Thus

\[
[r,k]A=L(k). \tag{5}
\]

Explicitly, if \(\psi(xH)=1\) and
\([h,x]=a^{\bar\tau_x(v)}z^\sigma\), applying conjugation by \(x\)
twice multiplies \(h\) by \(z^{\bar\tau_x(v)}\). On the other hand it
multiplies \(h\) by \(z^{b(v,x^2A)}\). Hence
\(x^2A\) is the symplectic dual of \(\bar\tau_x\). For \(x=rk\), this is
\(L(k)\); modulo \(A\), the identity
\((rk)^2=r^2k^2\,[r,k]\) gives (5). Signs and conjugates disappear in
the elementary abelian factor \(H/A\).

For \(k_1,k_2\in K\), (1) applied to \(k_1,k_2,k_1k_2\) gives

\[
[k_1,k_2]\in A. \tag{6}
\]

Indeed all three squares lie in \(A\), and square polarization modulo
\(A\) leaves exactly \([k_1,k_2]A\).

Because \(G'=H\), the images of commutators of quotient lifts span \(H/A=V\): commutators involving \(H\) already lie in \(A\), and
\(\bigwedge^2E=(r\wedge K)\oplus\bigwedge^2K\). Equations (5)--(6) show that this image is exactly \(L(K)\). Hence

\[
L:K\overset{\sim}{\longrightarrow}V. \tag{7}
\]

Choose bases \(k,l\) of \(K\) and \(uA,vA\) of \(V\) with

\[
L(k)=uA,\qquad L(l)=vA,\qquad b(uA,vA)=1. \tag{8}
\]

Choose \(u,v\) as section representatives and retain \(a,z\) as the fixed basis of \(A\). The non-parameter rows are

\[
a^2=z^2=1,\quad [u,v]=z,\quad
[a,u]=[a,v]=1,\quad [a,r]=z,\quad [a,k]=[a,l]=1,
\]

with \(z\in Z(G)\). This proves that every surviving pc table can be put into the following ambient finite parametrization:

\[
\begin{array}{c|c}
\text{row}&\text{exact value}\\ \hline
u^2,\ v^2&z^{\epsilon_u},\ z^{\epsilon_v}\\
[u,r],\ [v,r]&z^{\rho_u},\ z^{\rho_v}\\
[u,k],\ [v,k]&z^{\kappa_u},\ a z^{\kappa_v}\\
[u,l],\ [v,l]&a z^{\lambda_u},\ z^{\lambda_v}\\
[r,k],\ [r,l]&u a^{\mu_1}z^{\nu_1},\ v a^{\mu_2}z^{\nu_2}\\
[k,l]&a^{\mu_3}z^{\nu_3}\\
r^2,\ k^2,\ l^2&z^R,\ a^{s_k}z^{t_k},\ a^{s_l}z^{t_l}.
\end{array} \tag{9}
\]

All displayed exponents lie in \(\mathbf F_2\). Changes of the \(u,v\) section and exact pc overlaps cut out a subset of (9), but introduce no further kind of row. It is unnecessary to solve those deletion equations for coverage: the argument below works on the entire ambient binary cube (9), including parameter vectors which later pc overlaps delete. It therefore applies, a fortiori, to every pc-consistent row, and no central offset is left uncovered.

# Four-case order table

For the section \(s(\alpha u+\beta v)=u^\alpha v^\beta\), define

\[
s(t)^2=z^{q(t)},\qquad [s(t),r]=z^{\rho(t)},\qquad d(t)=q(t)+\rho(t).
\]

Here \(q\) is a quadratic refinement of \(b\), \(\rho\) is linear, and therefore

\[
d(u+v)=d(u)+d(v)+1. \tag{10}
\]

The complete case table is:

\[
\begin{array}{c|c|c|c}
d(u)&d(v)&d(u+v)&\text{choose }h\\ \hline
0&0&1&uv\\
0&1&0&v\\
1&0&0&u\\
1&1&1&u
\end{array} \tag{11}
\]

Thus in every row there is a nonzero \(t\in V\) and \(h=s(t)\) with \(d(t)=1\). Put

\[
x=r,\qquad y=rh.
\]

Convention-fixed collection gives

\[
y^2=(rh)^2=r^2h^2[h,r]=r^2z. \tag{12}
\]

Since \(r^2\in\{1,z\}\), exactly one of \(x,y\) has order \(2\) and the other has order \(4\). They are not conjugate.

# Exact normal closures

Equation (5) and (8) show that the normal closure of \(r\) contains elements \(U,V\) with

\[
UA=uA,\qquad VA=vA.
\]

It therefore contains

\[
[U,V]=z
\]

and, by normality and (4), it contains

\[
[U,l]\in aZ.
\]

Hence it contains \(a,z,U,V\), therefore all of \(H\). Since its image in \(G/H\) is generated by \(rH\),

\[
\langle r\rangle^G=\langle r,H\rangle. \tag{13}
\]

For \(y=rh\), the factors \([h,k]\) and \([h,l]\) lie in \(A\), so

\[
[y,k]A=[r,k]A=uA,\qquad [y,l]A=[r,l]A=vA. \tag{14}
\]

Repeating the preceding exact argument with the two elements in (14) gives \(z\), then an element of \(aZ\), hence \(a\), and then all of \(H\). Finally \(r=yh^{-1}\) belongs to the normal closure. Consequently

\[
\langle y\rangle^G=\langle r,H\rangle=\langle x\rangle^G. \tag{15}
\]

This equality is inside \(G\), not merely after projection, and it is independent of every central parameter in (9).

# Outcome

Every pc-consistent R2 row with \(A=C_2^2\) violates the source hypothesis via (11)--(15). There are no uncovered elementary-centre offset rows. Promotion of this order-\(128\) elimination remains contingent on Validator review of this note and of the preceding R1/\(C_4\) eliminations.

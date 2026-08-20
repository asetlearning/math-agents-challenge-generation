---
title: "Frozen carrier equations — H3(3) x C3^3 by C3^5"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, project/kourovka, status/draft]
---

# Frozen carrier

All coordinates are over \(k=\mathbb F_3\). Let \(V=k^2\), let
\(Z=kc\oplus D\) with \(D=k^3\), and put

\[
 P=V\oplus Z,
 \qquad
 (v,z)*(v',z')=(v+v',z+z'+2\det(v,v')c).
 \tag{E0}
\]

Then \(P\cong H_3(3)\times C_3^3\), \(|P|=3^6\), \(P'=kc\),
\(Z(P)=Z\), and \(P\) is nonabelian of exponent three. Freeze
\(A=k^5\). The carrier consists of **all** normalized extensions on
\(G=P\times A\) with quotient \(A\); hence \(|G|=3^{11}\).

# Complete action-plus-factor-set law

Choose a normalized section and variables

\[
 \alpha_u\in\operatorname{Aut}(P),\qquad
 f(u,v)\in P\quad(u,v\in A),
\]

with \(\alpha_0=1\) and \(f(0,v)=f(u,0)=1\). The multiplication is

\[
 (x,u)(y,v)=\bigl(x*\alpha_u(y)*f(u,v),u+v\bigr).                 \tag{E1}
\]

Writing \(c_a\) for left conjugation by \(a\), (E1) is associative if
and only if, for every \(u,v,w\in A\),

\[
 \alpha_u\alpha_v=c_{f(u,v)}\alpha_{u+v},                       \tag{E2}
\]
\[
 f(u,v)*f(u+v,w)=\alpha_u(f(v,w))*f(u,v+w).                      \tag{E3}
\]

These are the full nonabelian action and factor-set equations; no pointwise
automorphism cover is being substituted for a group.

# Every cube, every root coset

For \(x\in P\), direct use of (E1) gives

\[
 C_u(x):=(x,u)^3
 =x*\alpha_u(x)*f(u,u)*\alpha_{2u}(x)*f(2u,u)\in P.             \tag{E4}
\]

In particular \(C_0(x)=1\). The literal cube-value set is exactly

\[
 S=\{1\}\cup\bigcup_{0\ne u\in A}C_u(P).                       \tag{E5}
\]

The carrier is target-admissible exactly when

\[
 S=P.                                                            \tag{E6}
\]

Indeed, (E6) is the simultaneous **union**, cross-coset closure, and literal
value-set condition: every cube lies in \(P\), while every product of values
is again an element of \(P=S\) and hence has a root in some (not prescribed)
coset. Since \(P\) is nonabelian, (E6) also gives the required nonabelian
literal cube subgroup. Since \(G/P\) and \(P\) have exponent three, every
element of \(G\) has order dividing nine; (E6) supplies nonidentity cubes, so
the exponent is exactly nine.

Equivalently, without using (E6) as shorthand, cross-coset closure is

\[
 \forall u,v,x,y\ \exists w,z:\quad C_u(x)*C_v(y)=C_w(z),        \tag{E7}
\]

and nonabelianity is
\(
 \exists u,v,x,y:[C_u(x),C_v(y)]\ne1.
\)

# Coordinate form of every action

Every automorphism of \(P\) has the unique form

\[
 \alpha_u(v,z)=(M_uv,T_uz+L_uv),                                 \tag{E8}
\]

where \(M_u\in GL_2(k)\), \(L_u\in\operatorname{Mat}_{4\times2}(k)\),
and, relative to \(Z=kc\oplus D\),

\[
 T_u=
 \begin{pmatrix}
   \det M_u&r_u\\
   0&S_u
 \end{pmatrix},
 \quad r_u\in\operatorname{Mat}_{1\times3}(k),\quad S_u\in GL_3(k).
 \tag{E9}
\]

Write \(f(u,v)=(a_{uv},b_{uv})\in V\oplus Z\). Since

\[
 c_{(a,b)}(v,z)=(v,z+\det(a,v)c),                                 \tag{E10}
\]

(E2) is the following complete matrix system:

\[
 M_uM_v=M_{u+v},\qquad T_uT_v=T_{u+v},                            \tag{E11}
\]
\[
 T_uL_v+L_uM_v=L_{u+v}+J_{a_{uv}}M_{u+v},                        \tag{E12}
\]

where \(J_a(v)=\det(a,v)c\). Equation (E3), evaluated with the
fixed product (E0), gives six scalar equations for each triple \((u,v,w)\).
Formula (E4), again with (E0), is the exact six-coordinate cube polynomial;
the order shown in (E4) must not be commuted.

# Exact finite-system size

Use variables only for nonzero labels. There are 242 action labels, each with
24 field coordinates (4 for \(M\), 9 for \(S\), 3 for \(r\), 8 for \(L\)),
and \(242^2=58,564\) normalized factor entries, each with six coordinates.
Thus the frozen base system has

\[
 242\cdot24+58,564\cdot6=357,192
\]

\(\mathbb F_3\)-variables. A direct redundant-but-exact polynomial encoding
has:

- 484 determinant-nonzero equations \((\det M_u)^2=(\det S_u)^2=1\);
- \(58,564\cdot24=1,405,536\) scalar action equations (E11)--(E12);
- \(242^3\cdot6=85,034,928\) scalar cocycle equations (E3);
- 728 literal-coverage equations, one for each \(y\ne1\) in \(P\).

For the last row define, in fixed six coordinates,

\[
 \delta_y(z)=\prod_{i=1}^6\bigl(1-(z_i-y_i)^2\bigr).
\]

Then exact coverage is encoded without witness selectors by

\[
 \prod_{0\ne u\in A}\prod_{x\in P}
 \bigl(1-\delta_y(C_u(x))\bigr)=0\qquad(y\ne1).                  \tag{E13}
\]

The total displayed constraint count is 86,441,676. This is a frozen finite
system, but its raw encoding is intentionally **not** proposed for computation:
it first needs cohomological/orbit compression and a Lead lease.


---
title: "Kourovka 12.15 — exact obstruction to M2 mixed-fibre polarization"
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
outcome: STRATEGY_EXHAUSTED
state: awaiting_lead
---

# Outcome

**STRATEGY_EXHAUSTED** for **M2-MIXED-FIBRE-POLARIZATION** only. This is not a verdict on the proof direction or on the active scope.

# Convention-fixed residual

Let $H=G'$, $Z=G''=\langle z\rangle\le Z(G)$, and $W=H/Z$. For a normalized section $s:W\to H$, define

\[
s(u)s(v)=z^{f(u,v)}s(u+v),
\qquad
s(u)^y=z^{\lambda_y(u)}s(\rho_yu).
\]

If

\[
[x,g]=z^{\alpha_g}s(u_g),\qquad [y,g]=z^{\gamma_g}s(v_g),
\]

then, for the convention $[a,b]=a^{-1}a^b$,

\[
[xy,g]
=z^{\alpha_g+\gamma_g+\lambda_y(u_g)+f(\rho_yu_g,v_g)}
s(\rho_yu_g+v_g). \tag{1}
\]

The exact alternating residual is

\[
f(\rho_yu_g,v_g)+f(v_g,\rho_yu_g)
=\beta(\rho_yu_g,v_g),
\]

equivalently

\[
[x,g]^y[y,g]=[y,g][x,g]^y\,z^{\beta(\rho_yu_g,v_g)}. \tag{2}
\]

For the inverse fibre,

\[
[xy^{-1},g]=([x,g][y,g]^{-1})^{y^{-1}}, \tag{3}
\]

and the alternating factor is $\beta(u_g,-v_g)=\beta(u_g,v_g)$, because its values lie in $C_2$.

# Exact obstruction from four-fibre closure

In a hypothetical least counterexample choose $x,y\in H$ with $[x,y]=z$. Then $x,y,xy,xy^{-1}$ are all noncentral, so the reviewed core gives

\[
Z\le D(x)\cap D(y)\cap D(xy)\cap D(xy^{-1}). \tag{4}
\]

Consequently every relevant fibre is $Z$-saturated:

\[
D_G(t)=\pi^{-1}(D_{G/Z}(tZ)) \qquad
(t=x,y,xy,xy^{-1}). \tag{5}
\]

Thus subgroup membership is insensitive to multiplication by the residual $z$.

More explicitly, put $a_g=[x,g]$ and $b_g=[y,g]$. Since $H'=Z$, equations (1) and (3), normality, and (4) give

\[
a_gb_g\in D(xy),
\qquad
a_gb_g^{-1}\in D(xy^{-1}). \tag{6}
\]

For arbitrary independent $g,h\in G$, the two closure calculations are

\[
\begin{aligned}
(a_gb_g)(a_hb_h)
 &=a_ga_hb_gb_h\,[b_g,a_h],\\
(a_gb_g^{-1})(a_hb_h^{-1})
 &=a_ga_hb_g^{-1}b_h^{-1}\,[b_g^{-1},a_h].
\end{aligned} \tag{7}
\]

But

\[
[b_g^{-1},a_h]=[b_g,a_h]^{-1}=[b_g,a_h]\in\{1,z\}. \tag{8}
\]

The plus and minus fibres therefore see the same $C_2$-valued mixed bit. All four subgroups already contain both possible values, and their separate closure witnesses need not be the same conjugator. Hence (7) cannot decide whether the bit is $1$ or $z$. As $g,h$ vary independently, it covers every pairing between $D(y)$ and $D(x)$, so the strongest conclusion is only the already-known

\[
[D(x),D(y)]\le\langle z\rangle.
\]

# Boundary and handoff

This calculation does not establish $G''=1$, does not exclude order $128$, and is not a scope-closing claim. It shows precisely why subgroup closure of the four coupled defect fibres cannot by itself kill the central factor. A next proof strategy would have to use compatibility of the actual conjugators that toggle $z$, rather than membership/closure of the $Z$-saturated fibres. No such new strategy was started; the run is awaiting Lead.

Full derivation: [[log]].

---
title: "Type-II(ii) even residual: 2-adic and spectral closeout"
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/distance-regular-graphs, project/kourovka, status/draft]
problem: 21.90
scope_id: 21.90/diameter-three-distance-graphs
assignment_revision: 3
outcome: STRATEGY_EXHAUSTED
active_assignment_answered: no
---

# Type-II(ii) even residual

Use the consistent Type-(IIii) substitution

\[
 t=uw,\quad c=xw,\quad h=c+1=xw+1,\quad
 a=wh-1,\quad u^2=x(w+1)+1. \tag{1}
\]

The handshake residual from the preceding note is `xw` even.

## Exact 2-adic split

If `x` is even, (1) forces `u` odd and

\[
 \nu_2(x)+\nu_2(w+1)=\nu_2(u^2-1)\geq3. \tag{2}
\]

In particular, when `w` is also even, `w+1` is odd and (2) says `8|x`.

The complementary residual has `x` odd and `w` even.  Then `u` is even and

\[
 x(w+1)=u^2-1\equiv3\pmod4. \tag{3}
\]

Equivalently, `x` is 3 modulo 4 when `w=0 mod 4`, and `x` is 1 modulo 4
when `w=2 mod 4`.  Equations (2)--(3) are exact necessary congruences coming
from the square condition; neither is contradictory.

Both branches are infinite even before graph feasibility is considered.  For
example:

- `w=3`, `u=2r+1`, and `x=(u^2-1)/4=r(r+1)` for `r>=1` give infinitely
  many positive even-`x` solutions;
- `w=2`, `u=6r+2`, and `x=(u^2-1)/3=12r^2+8r+1` for `r>=0` give infinitely many
  odd-`x` solutions.

## Spectral multiplicities are automatically integral

Here

\[
 k=wh(u+1)-1,qquad k_2=kt,qquad k_3=kw. \tag{4}
\]

The four `A_1` eigenvalues are

\[
 k,quad w(h+u)-1,quad -1,quad -h. \tag{5}
\]

The exact strongly-regular constituent multiplicity formulas simplify, using
`h(w+1)=wu^2+1`, to

\[
 (m_0,m_1,m_2,m_3)=(1,k,kt,kw). \tag{6}
\]

For instance,

\[
 m_{-1}=\frac{k(k+h)}{h+u}=kt,qquad
 m_{-h}=\frac{t(kt+kw)}{wu(u+1)}=kw,
\]

because `k+h=uw(h+u)`.  The remaining nonprincipal multiplicity is `k` by
the sum of multiplicities.  Thus no denominator or 2-adic spectral obstruction
remains in either even branch.

Indeed the eigenmatrix is

\[
P=\begin{pmatrix}
1&k&kt&kw\\
1&w(h+u)-1&-uw&-wh\\
1&-1&-uw&uw\\
1&-h&wu^2&-wh
\end{pmatrix}. \tag{7}
\]

With valencies `(1,k,kt,kw)`, (7) is weighted symmetric:
`k_iP_{ij}=k_jP_{ji}`.  Together with (6), this gives `Q=P`; the putative
scheme is formally self-dual.  Consequently its Krein parameters equal its
ordinary intersection numbers.  Krein integrality supplies no independent
2-adic restriction beyond ordinary intersection-number feasibility.

## Exact residual frontier

The symbolic gate leaves precisely the union

1. `x` even with `nu_2(x)+nu_2(w+1)>=3`;
2. `x` odd, `w` even, `u` even, and `x(w+1)=3 mod 4`;

always subject to the exact square equation (1), positivity, and all later
ordinary feasibility conditions.  Both residual branches are infinite and
have automatically integral spectral multiplicities and formally self-dual
Krein data.  No further infinite subfamily is eliminated by this gate.

This does not retract or promote the separately submitted odd-`x,w` handshake
claim, which remains under fresh validation.  It does not cover Type III or the
Taylor branch and does not answer the revision-3 scope.  No computation,
catalogue, constituent, or web search was used.  `active_assignment_answered:no`.

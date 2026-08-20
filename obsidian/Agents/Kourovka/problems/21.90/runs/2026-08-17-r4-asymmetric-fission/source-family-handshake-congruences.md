---
title: "Symbolic handshake congruences in the four source families"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/distance-regular-graphs
  - project/kourovka
  - status/conjectured
problem: 21.90
scope_id: 21.90/diameter-three-distance-graphs
assignment_revision: 3
outcome: PARTIAL_RESULT
active_assignment_answered: no
---

# Source-family handshake congruences

This note works only with the primitive non-Taylor master array and the four
algebraically consistent Type-I/II substitutions already frozen in
`source-family-rescreen.md`.  It makes no completeness assertion about the
full source problem or the separate Taylor/Type-III cases.

## One exact master congruence

Put

\[
 \{b_0,b_1,b_2;c_1,c_2,c_3\}
 =\{t(c+1)+a,tc,a+1;1,c,t(c+1)\}, \tag{1}
\]

where

\[
 (t^2-a-1)(c+1)=a(a+1). \tag{2}
\]

Write `k=t(c+1)+a`, `d=t^2-a-1`, and

\[
 q=k_3=\frac{k(a+1)}{c+1}=t(a+1)+d. \tag{3}
\]

The sphere sizes and original induced degrees are

\[
 (k_1,k_2,k_3)=(k,kt,q),\qquad
 (a_1,a_2,a_3)=(a+t-1,(t-1)(c+1),a). \tag{4}
\]

The middle handshake is automatic because
`k_2a_2=kt(t-1)(c+1)` contains `t(t-1)`.  Modulo 2, (3) gives

\[
 q\equiv a(t+1)+1,qquad qa\equiv ta. \tag{5}
\]

Therefore the layer-3 handshake is equivalent to `ta` being even.  Conversely,
if `ta` is even, the layer-1 handshake also passes:

- if `t,a` are both even then `k` is even;
- if exactly one of `t,a` is odd then `a+t-1` is even.

Hence all three nontrivial original local handshakes are equivalent to the
single necessary and sufficient congruence

\[
 \boxed{ta\equiv0\pmod 2}. \tag{6}
\]

If `t,a` are both odd, (5) makes `q` odd and the `q`-vertex, `a`-regular
layer-3 graph has odd degree sum.  This is a constituent-independent
contradiction.

## Every induced distance-relation handshake

The same congruence already controls the stronger test in which every distance
relation is restricted to every nonzero sphere.  Their induced degrees are

\[
\begin{array}{c|ccc}
 &A_1&A_2&A_3\\ \hline
\Gamma_1(u)&a+t-1&tc&0\\
\Gamma_2(u)&(t-1)(c+1)&
 t(t-1)(c+1)+c+a+1-t&(t-1)(a+1)\\
\Gamma_3(u)&a&ta&t^2+t-2a-2.
\end{array} \tag{7}
\]

For example, `A_2` has nonprincipal eigenvalues `c+a+1,-t`, so its
strongly-regular parameters give the middle entry of row 2.  Similarly `A_3`
has nonprincipal eigenvalues `t,-(a+1)`, giving the final entry of row 3;
the remaining entries follow from the distance-matrix products and row sums.

If (6) holds, every sphere-size times every entry of (7) is even.  The only
case not visibly containing an even factor is the middle entry of row 2.  If
`t` is odd, then (6) makes `a` even; its parity is then `c`, while `k` is even
when `c` is odd.  Thus `kt` times that entry is even.  Conversely, the
row-3/column-1 handshake is exactly (5), so (6) is necessary.  Thus (6) is
also equivalent to all nine induced-relation handshakes.

There is no extra global degree-sum condition: from (3),

\[
 v=1+k+kt+q\equiv0\pmod2, \tag{8}
\]

so each full distance graph has even degree sum automatically.

## Translation to the four parameter families

Using the substitutions in `source-family-rescreen.md`, (6) becomes:

| family | `ta` | exact handshake consequence |
|---|---|---|
| (Ii) | `msu(s^2-1)` | always even, since `s(s^2-1)` is even |
| (Iii) | `u(w+1)w(x(w+1)+1)` | always even, since `w(w+1)` is even |
| (IIi) | `su(ms^2-1)` | always even for an integral square-condition solution |
| (IIii) | `uw(w(xw+1)-1)` | even exactly when `xw` is even |

For (IIi), the only superficially bad parity is `s` odd and `m` even.  But
its square condition would give

\[
 u^2=m(s^2+1)-1\equiv3\pmod4,
\]

which is impossible.  Thus the square condition itself removes that case.

For (IIii), if `w` is odd then
`u^2=x(w+1)+1` forces `u` odd, while
`a=w(xw+1)-1` has the parity of `x`.  Consequently

\[
 ta\equiv xw\pmod2, \tag{9}
\]

and the exact residual handshake restriction is

\[
 \boxed{xw\text{ is even}}. \tag{10}
\]

Thus every algebraically consistent Type-(IIii) tuple with `x,w` both odd is
excluded before any spectral, constituent, or coclique test.

## The excluded subfamily is genuinely infinite

For every integer `r>=0`, take

\[
 w=7,\qquad u=8r+3,\qquad x=8r^2+6r+1. \tag{11}
\]

Then `x,w` are odd and

\[
 x(w+1)+1=8(8r^2+6r+1)+1=(8r+3)^2=u^2, \tag{12}
\]

so these are infinitely many positive integer solutions of the Type-(IIii)
square condition.  They give

\[
 t=7(8r+3),\quad c=7x,\quad a=49x+6,
\]

all odd.  Moreover `a+1=w(c+1)`, hence `q=kw`; both `k` and `q` are odd.
The layer-1 graph has odd order `k` and odd degree `a+t-1`, while the layer-3
graph has odd order `q` and odd degree `a`.  Each tuple therefore fails two
independent handshakes.

This is an infinite formal-parameter exclusion inside the consistent
Type-(IIii) specialization.  It is not a graph construction, does not eliminate
the even-`xw` residual family, and does not answer the revision-3 existential
scope.  `active_assignment_answered: no`.

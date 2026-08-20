---
title: "Type-II(ii) even residual: triple-intersection gate"
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/distance-regular-graphs, project/kourovka, status/draft]
problem: 21.90
scope_id: 21.90/diameter-three-distance-graphs
assignment_revision: 3
outcome: STRATEGY_EXHAUSTED
active_assignment_answered: no
---

# Type-II(ii) even residual: triple-intersection gate

Work throughout with

\[
t=uw,\quad c=xw,\quad h=c+1,\quad a=wh-1,\quad
u^2=x(w+1)+1,\quad k=wh(u+1)-1,
\]

and with the residual condition `xw` even.  The valencies are
`(1,k,kt,kw)` and the exact eigenmatrix is the self-dual matrix `P=Q`
recorded in the linked spectral note.

## Exact zero-Krein support

Because `P=Q`, every Krein parameter is the corresponding ordinary
intersection number.  In order `h=0,1,2,3`, direct use of the intersection
array gives

\[
\begin{aligned}
(q_{11}^h)_h&=(k,a+t-1,c,0),\\
(q_{12}^h)_h&=(0,tc,(t-1)h,th),\\
(q_{13}^h)_h&=(0,0,a+1,a),\\
(q_{22}^h)_h&=(kt,t(t-1)h,t(t-1)h+wu^2-t,t(t-1)h),\\
(q_{23}^h)_h&=(0,twh,wh(t-1),ta),\\
(q_{33}^h)_h&=(kw,wa,wa,w(a+u-h)).
\end{aligned}
\]

All displayed nonzero entries are positive for positive Type-II(ii)
parameters (`u>=2`).  Thus, apart from the universal
`q_{ij}^0=0` for `i!=j` and symmetries, the only zero with three nonzero
idempotent indices is the multiset

\[
q_{11}^3=q_{13}^1=0. \tag{Z}
\]

There is no second special zero-Krein row in this residual.

## Translation to triple-intersection identities

For an ordered base triple `(X,Y,Z)`, put
`W=d(X,Y)`, `V=d(X,Z)`, `U=d(Y,Z)`, and let

\[
[rst]=|\{z:d(X,z)=r, d(Y,z)=s, d(Z,z)=t\}|.
\]

The standard marginal equations are

\[
\sum_r[rst]=p_{st}^{U},\qquad
\sum_s[rst]=p_{rt}^{V},\qquad
\sum_t[rst]=p_{rs}^{W}, \tag{M}
\]

together with nonnegativity, integrality, the forced entries having one
index zero, and the triangle-support zeros.  The zero-Krein theorem says

\[
q_{ij}^{\ell}=0\Longrightarrow
\sum_{r,s,t=0}^3 Q_{ri}Q_{sj}Q_{t\ell}[rst]=0. \tag{K}
\]

Set

\[
L=(k,\ w(h+u)-1,\ -1,\ -h),\qquad
G=(k,\ -h,\ u,\ -h).
\]

Since column 3 of `Q` is `wG`, (Z), after division by `w`, gives exactly
the three coordinate placements

\[
\sum_{r,s,t}L_rL_sG_t[rst]=0,
\quad \sum_{r,s,t}L_rG_sL_t[rst]=0,
\quad \sum_{r,s,t}G_rL_sL_t[rst]=0. \tag{T}
\]

The zeros with superscript zero give only the pairwise primitive-idempotent
orthogonality identities after (M); they do not add a new triple-variable
row.  Hence (M), the forced support/zero entries, and (T) are the exact
triple-intersection residual furnished by all zero Krein parameters.

## Integrality gate reached

Since `c=xw` is even, `h` and every entry of `L` are odd.  If `u` is odd,
every entry of `G` is odd, and each equation in (T), modulo 2, reduces to
the total number of vertices

\[
v=1+k+kt+kw\equiv 0\pmod2.
\]

If `u` is even, then necessarily `w` is even and `x` is odd.  Now only
`G_2=u` is even, so the same reduction is

\[
v-k_2=v-kt\equiv0\pmod2.
\]

Thus the primitive parity/divisibility test of the zero-Krein equations is
identically satisfied on both infinite even-`xw` branches.  The equations
have integral coefficients and integral marginal data, but no single triple
variable is forced by (M)+(T) alone without fixing a base-distance type and
eliminating its remaining variables.  No uniform nonnegativity or
integrality contradiction was obtained in the allotted hand window.

## Frozen residual and outcome

For every base type `(U,V,W)` with `p_{UV}^W>0`, the remaining exact question
is whether the finite system (M)+(T), with forced base-point entries and
triangle-support zeros, has a nonnegative integral solution.  A future route
would eliminate variables separately for the finitely many base types and
then factor any forced denominators in `u,w,x`; that is a materially bounded
symbolic continuation, but it was not authorized inside this final window.

Outcome: `STRATEGY_EXHAUSTED`.  This gate excludes no even-`xw` subfamily,
does not answer the revision-3 existential scope, and does not retract or use
the unvalidated odd-`x,w` handshake claim.  No computation, catalogue, or
external search was used.  `active_assignment_answered: no`.

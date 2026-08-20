---
title: "Kourovka 21.90 revision 3 — Type-II(ii) parametric local-root gate"
problem: "21.90"
scope_id: 21.90/diameter-three-distance-graphs
assignment_revision: 3
direction: proof
strategy: IIii-LOCAL-ROOT-PARAMETRIC
outcome: STRATEGY_EXHAUSTED
active_assignment_answered: no
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/distance-regular-graphs, topic/root-systems, project/kourovka, status/conjectured]
---

# Type-II(ii) parametric local-root gate

## Active-time ledger

- `2026-08-17T13:52:59Z`: work start at scope cumulative minute 250; current increment budget 34 minutes.
- `2026-08-17T14:01:10Z`: research stop after 9 charged active minutes (rounded up from 8m11s); scope cumulative minute 259. The positivity-isolated hard kill fired before 17 active minutes; 25 minutes remain unspent pending Lead.

No computation, catalogue search, or browsing was used.

## Controlling reviewed formulas

Use positive integers `x,w,u`, and put

\[
 h=xw+1,\qquad u^2=x(w+1)+1,\qquad
 t=uw,\quad c=h-1,\quad a=wh-1.
\]

The Type-II(ii) intersection array is the reviewed master array

\[
 \{k,tc,a+1;1,c,t(c+1)\},\qquad
 k=t(c+1)+a=wh(u+1)-1.
\]

For a vertex `X`, its local graph `Delta` therefore has `k` vertices and valency

\[
 d_{\rm loc}=a+t-1=w(h+u)-2.
\]

The reviewed nonprincipal global eigenvalues are

\[
 R=w(h+u)-1,\qquad -1,\qquad -h.
\]

## Exact symbolic local interval

Let `theta != k` be a global eigenvalue and normalize its cosine sequence by
`sigma_0=1`, `sigma_1=theta/k`.  The distance-one recurrence is

\[
 1+(a+t-1)\frac{\theta}{k}+tc\,\sigma_2
   =\theta\frac{\theta}{k}.
\]

Direct factorization, using `k=t(c+1)+a`, gives

\[
 1-\sigma_2=\frac{(k-\theta)(\theta+tc+1)}{ktc},\qquad
 \sigma_1-\sigma_2=\frac{(k-\theta)(\theta+1)}{ktc}.
\]

For every local eigenvector perpendicular to the all-one vector, with local
eigenvalue `eta`, positivity of the primitive-idempotent principal submatrix gives

\[
 \theta+tc+1+(\theta+1)\eta\ge 0. \tag{1}
\]

At `theta=R`, (1) becomes

\[
 \eta\ge -\frac{h(u+1)}{h+u};
\]

at `theta=-h`, it becomes `eta <= uw-1`; and `theta=-1` adds no restriction.
Thus the exact interval delivered by this local-cosine method is

\[
 \boxed{-\frac{h(u+1)}{h+u}\le \eta\le uw-1}. \tag{2}
\]

The upper endpoint is strictly below `d_loc`, since
`d_loc-(uw-1)=wh-1=a>0`.  Hence (2) also forces every hypothetical local graph
to be connected: otherwise its valency would occur on the perpendicular-to-one
subspace.

## Positive-definite regime of `2I+A`

The interval (2) certifies `2I+A(Delta)` as positive definite precisely when its
lower endpoint is strictly greater than `-2`.  Indeed

\[
 2-\frac{h(u+1)}{h+u}
 =\frac{2-(h-2)(u-1)}{h+u}. \tag{3}
\]

Since `h,u>=2` are integers, strict positivity in (3) permits either `h=2`, or
`(h,u)=(3,2)`.

- `h=2` forces `x=w=1`, but then the square condition gives `u^2=3`, impossible.
- For `(h,u)=(3,2)`, the equivalent identity `(w+1)h=wu^2+1` forces `w=2`, and
  then `x=1`.

Therefore the local interval forces positive definiteness for exactly

\[
 (x,w,u)=(1,2,2).
\]

There is no unexamined semidefinite boundary.  Equality in (3) requires
`(h,u)=(3,3)` or `(4,2)`; substituting either pair into
`(w+1)h=wu^2+1` gives no positive integral `w`.

For every other positive integral Type-II(ii) tuple, the lower endpoint in (2)
is strictly below `-2`.  This does **not** prove that the actual local Gram matrix
is indefinite; it proves that the reviewed local-cosine inequalities no longer
certify positive definiteness.  Treating a lower bound below `-2` as an attained
eigenvalue would be a necessary-versus-sufficient error.

## ADE/support consequence and kill

At the unique positive-definite tuple, `k=17` and `d_loc=8`, so the root-system
reduction is exactly the already reviewed rank-17 `A_17/D_17` case.  It supplies
no new parameter row and no infinite subfamily.  Outside this tuple, positive
definiteness is unavailable from the symbolic local bound, so ADE/support-degree
arithmetic cannot be invoked without an additional independent spectral lemma.

The assigned hard kill therefore fires: the positive-definite regime is isolated,
and the method cannot exclude an explicit infinite Type-II(ii) subfamily.  This is
`STRATEGY_EXHAUSTED`, not a verdict on revision 3.

## What is not established

- No actual graph satisfying the revision-3 target is constructed or excluded.
- No Type-II(ii) tuple beyond the already reviewed `(1,2,2)` row is eliminated.
- The interval does not assert that either endpoint is attained.
- The Type-II(ii) family is not asserted to exhaust the source problem.

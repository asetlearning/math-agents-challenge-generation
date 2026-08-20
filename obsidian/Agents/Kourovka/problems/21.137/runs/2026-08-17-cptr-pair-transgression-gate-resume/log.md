---
title: "Problem 21.137 — CPTR boundary/section-invariance gate resume"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: CPTR-PAIR-TRANSGRESSION
direction: proof
gate: boundary-and-section-invariance-only
active_assignment_answered: no
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/group-extensions
  - project/kourovka
  - status/draft
---

# CPTR boundary/section-invariance gate

## Resumption record

The prior turn was interrupted after the required reads and after a checkable
boundary/section-change derivation had already been written locally. This log
preserves only the gate authorized by the resumed assignment. It does not rely
on, route, or continue any longer `(C4)/(C5)` manipulation from the interrupted
turn.

Completed before interruption, in the mandated order:

1. `_meta/agents/Kourovka/_common-kourovka.md` — read completely.
2. `_meta/agents/Kourovka/problem-agent-kourovka.md` — read completely.
3. `Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json` — read completely;
   revision `2` and all seven constraints locked.
4. `Agents/Kourovka/bus/inbox/Problem-21.137/` — both then-unread messages read
   completely, including Lead's `cptr-pair-transgression` request; both were
   marked done and moved to `bus/archive/`.
5. Only the three further curated references named by Lead were read:
   `verification/2026-08-16T181302Z-minimal-central-obstruction.md`,
   `verification/2026-08-17T053718Z-mco-affine-norm-cover.md`, and
   `ideas/2026-08-17-portfolio-reset-park.md`.

No web/history search, uncurated local artifact, computation, delegate,
wreath-shaped/quarantined material, stopped family, `p=2`, exponent-8 clause,
or generated-subgroup substitution was used.

## Active-time ledger

- Original gate work start before interruption: `2026-08-17T07:09:43Z`;
  cumulative active minute: `255`.
- This resumed artifact preserves the already completed gate derivation; it does
  not reset or double-charge those minutes.

## Exact boundary calculation

Use normalized inhomogeneous bars over `F_p` with trivial coefficients:

`partial[a|b|c]=[b|c]-[ab|c]+[a|bc]-[a|b]`.

For

`Z(h,j)=sum_(i=1)^(p-1)([j|h^i|h]-[h^i|j|h]+[h^i|h|j])`,

the boundary of its `i`th parenthesis is, using `hj=jh`,

`[j|h^(i+1)]-[j|h^i]-[j|h]
 +[h^i|j]+[h|j]-[h^(i+1)|j]`.

Summing from `i=1` to `p-1` and using normalized bars
`[j|1]=[1|j]=0` gives

`(-[j|h])-(p-1)[j|h]+[h|j]+(p-1)[h|j]=0`

in characteristic `p`. Therefore the displayed chain already has the correct
shuffle signs and `partial Z=0`; no replacement chain is required.

## Complete arbitrary normalized section change

Write `x'_t=x_tk_t`, `k_t=(eta_t,z_t) in A x F_p`, with `k_1=1`. Retain

`(a,z)(b,w)=(a+b,z+w+(1/2)beta(a,b))`,

`alpha_t(a,z)=(L_ta,z+ell_t(a))`,

and `x_ax_b=x_(ab)u_(a,b)`, `u_(a,b)=(r_(a,b),s_(a,b))`.

Direct conjugation gives

`alpha'_t=iota_(k_t)alpha_t`,

`L'_t=L_t`,

`ell'_t(a)=ell_t(a)+beta(L_ta,eta_t)`.

With `D_t=L_t-I`, the exact ordered norm formula gives

`c'_t=c_t+D_t^(p-1)eta_t`,

`d'_t=d_t+ell_t(D_t^(p-2)eta_t)
             +(1/2)beta(D_t^(p-2)eta_t,eta_t)`.

The input central coordinate contributes `p z_t=0`; it has not been omitted.

For the carry, direct reassociation gives the group identity

`u'_(a,b)=k_(ab)^(-1)u_(a,b)alpha_b(k_a)k_b`.

Thus

`r'_(a,b)=-eta_(ab)+r_(a,b)+L_b eta_a+eta_b`.

For the scalar coordinate put, in the actual multiplication order,

`v_1=-eta_(ab)`, `v_2=r_(a,b)`, `v_3=L_b eta_a`, `v_4=eta_b`.

Then

`s'_(a,b)=-z_(ab)+s_(a,b)+z_a+ell_b(eta_a)+z_b
 +(1/2)sum_(1<=m<n<=4)beta(v_m,v_n)`.

This retains every `ell`, action, central coordinate, and `1/2 beta` term.

## Gate result

No boundary defect and no section-change inconsistency was found at this first
gate. The chain is an exact mod-`p` cycle and the full coordinate transformation
is now explicit. Per the resumed instruction, stop here before any longer
`(C4)/(C5)` evaluation.

`active_assignment_answered: no`.

- Gate stop before interruption: `2026-08-17T07:17:39Z`; cumulative active
  minute: `263`.
- Gate-only resumption artifact filed: `2026-08-17T07:25:37Z`; no mathematical
  work beyond the already charged gate was added.
- A separate interrupted local draft contains later, unreviewed manipulation;
  it is outside this checkpoint and is neither adopted nor routed here.

## Lead-authorized continuation

Lead's `2026-08-17T072717Z` decision authorizes the finite scalar `(C4)`
evaluation and ordered `(C5)` reach audit in this same strategy. No prior read or
gate was repeated.

- Work resumes: `2026-08-17T07:29:20Z`; cumulative active minute: `263`.
- Hard kill: cumulative minute `290` absent an exact identity or defect.
- Packaging reserve: cumulative minutes `290`--`300`.

## Finite `(C4)/(C5)` evaluation

### 1. Scalar `(C4)` cochain and the mixed cycle

Move the two right-hand scalar terms of `(C4)` together and define

`Q(a,b,c)=ell_c(r_(a,b))
 +(1/2)beta(r_(ab,c),L_c r_(a,b))
 -(1/2)beta(r_(a,bc),r_(b,c))`.

The complete scalar associativity row is exactly

`Q(a,b,c)=s_(a,bc)+s_(b,c)-s_(ab,c)-s_(a,b)=(delta s)(a,b,c)`.

Evaluating on the verified cycle, using only `h^ij=jh^i`, gives the full
finite expression

`Omega(h,j)=sum_(i=1)^(p-1) {
 ell_h(r_(j,h^i))-ell_h(r_(h^i,j))+ell_j(r_(h^i,h))
 +(1/2)beta(r_(h^i j,h),L_h(r_(j,h^i)-r_(h^i,j)))
 -(1/2)beta(r_(j,h^(i+1)),r_(h^i,h))
 +(1/2)beta(r_(h^i,jh),r_(j,h))
 +(1/2)beta(r_(h^(i+1),j),L_jr_(h^i,h))
 -(1/2)beta(r_(h^i,hj),r_(h,j)) }`.

No term has been moved to coinvariants. Since `Q=delta s` and `partial Z=0`,

`Omega(h,j)=<delta s,Z>=<s,partial Z>=0`.                  `(E0)`

For the changed section, the already derived complete laws still satisfy
`Q'=delta s'`; hence

`Omega'-Omega=<delta(s'-s),Z>=<s'-s,partial Z>=0`.

Thus `(E0)` is exactly section-independent. Its numerical value is nevertheless
forced to zero because the nonlinear scalar cochain is already a coboundary;
the cycle evaluation alone does not yet identify a target-facing pairing.

### 2. Ordered `(C5)` with all central terms exposed

For `t` equal to `h` or `j`, put

`R_(t,i)=r_(t^i,t)`, `e_i=p-1-i`, and
`E_e=I+L_t+...+L_t^(e-1)` (`E_0=0`).

The factor `u_(t^i,t)` in `(C5)` is acted on by `alpha_t^(e_i)`, so define

`a_(t,i)=L_t^(e_i)R_(t,i)`,

`b_(t,i)=s_(t^i,t)+ell_t(E_(e_i)R_(t,i))`.

The actual multiplication order is `i=p-1,p-2,...,1`. Therefore the complete
coordinates are

`c_t=sum_(i=1)^(p-1)a_(t,i)`,

`d_t=sum_(i=1)^(p-1)b_(t,i)
 +(1/2)sum_(1<=k<i<=p-1)beta(a_(t,i),a_(t,k))`.            `(E1)`

This displays every action, `ell`, and ordered quadratic term for both cyclic
subgroups.

### 3. The exact mixed carry identity

Because `hj=jh`, define the full carry

`v=u_(j,h)^(-1)u_(h,j)=(q,z)`,

`q=r_(h,j)-r_(j,h)`,

`z=s_(h,j)-s_(j,h)-(1/2)beta(r_(j,h),r_(h,j))`.

Directly from the two products with quotient value `hj`,

`x_h^(x_j)=x_hv`.

Before simplifying, the ordered norm on the right has projected coordinate

`sum_(m=0)^(p-1)L_h^m q`

and central increment

`p z
 +sum_(m=0)^(p-1)ell_h(E_mq)
 +(1/2)sum_(0<=n<m<=p-1)beta(L_h^m q,L_h^n q)
 +(1/2)beta(c_h,sum_(m=0)^(p-1)L_h^m q)`.                 `(E2)`

The four terms in `(E2)` simplify, for the stated reasons, to

- `p z=0`;
- `sum_m L_h^m q=D_h^(p-1)q`;
- `sum_m ell_h(E_mq)=ell_h(D_h^(p-2)q)`;
- the ordered quadratic sum is
  `beta(D_h^(p-2)q,q)`;
- the final cross term is zero because `D_h^(p-1)` is self-adjoint and
  `D_hc_h=0`.

The left side is
`alpha_j(c_h,d_h)=(L_jc_h,d_h+ell_j(c_h))`. Equating the two
coordinates gives

`D_jc_h=D_h^(p-1)q`,                                      `(E3)`

`ell_j(c_h)=ell_h(D_h^(p-2)q)
             +(1/2)beta(D_h^(p-2)q,q)`.                    `(E4)`

Swapping `h,j` replaces `q` by `-q` and gives

`D_hc_j=-D_j^(p-1)q`.                                     `(E3')`

### 4. What `(C5)` says about the desired pairing

For each `t`, comparing `alpha_t^p` with inner conjugation by
`x_t^p=(c_t,d_t)` gives, for every `a in A`,

`ell_t(D_t^(p-1)a)=beta(a,c_t)`.                            `(E5)`

Since `(C1)` for `hj=jh` gives `D_hD_j=D_jD_h`, equations `(E3)`,
`(E3')`, and `(E5)` yield the exact final expression

`beta(c_h,c_j)
 =ell_j(D_j^(p-2)D_h^(p-1)q)
 =ell_h(D_h^(p-2)D_j^(p-1)q)`.                              `(E6)`

This is a checkable coupling of the two power basepoints to the mixed carry,
but it is an extra term, not a vanishing identity. No cancellation in `(E0)`--
`(E5)` sets either scalar in `(E6)` equal to zero.

As a consistency check, subtracting the two ordered `(C1)` scalar rows gives

`ell_j(D_ha)-ell_h(D_ja)=beta(L_hL_ja,q)`.

At `a=D_j^(p-2)D_h^(p-2)q`, the two left terms are equal by `(E6)`, so the
only further identity is

`beta(L_hL_jD_j^(p-2)D_h^(p-2)q,q)=0`;                    `(E7)`

this still does not kill the value in `(E6)`.

### 5. Final arbitrary-section audit and exact extra-term formula

Let `N_t=D_t^(p-1)`. The previously derived laws specialize to

`q'=q+D_jeta_h-D_heta_j`,

`c'_t=c_t+N_teta_t`.

Equation `(E3)` is covariant because

`N_hq'=N_hq+N_hD_jeta_h-D_h^peta_j
       =D_jc_h+D_jN_heta_h=D_jc'_h`.

The scalar equation `(E4)` is the central coordinate of the section-free group
identity `(x_h^p)^(x_j)=(x_h^(x_j))^p`, so it remains valid with every primed
quantity; `(E0)` was audited directly above.

But the target-facing basepoint pairing changes by the exact formula

`beta(c'_h,c'_j)-beta(c_h,c_j)
 =beta(N_heta_h,c_j)+beta(c_h,N_jeta_j)
  +beta(N_heta_h,N_jeta_j)`.                                `(E8)`

These are not terms in the invariant zero `(E0)`. With only `eta_h` changed,
self-adjointness of `N_h` and `(E3')` rewrite the first defect as

`-beta(eta_h,D_h^(p-2)N_jq)`,                               `(E9)`

and the available rows do not put the second argument in `rad(beta)`.
Therefore identifying the invariant mixed-cycle value with
`beta(c_h,c_j)` requires a new vanishing/correction lemma; the finite audit
does not supply one.

### 6. Separate reach audit

Actual-value coverage gives the affine union

`A=union_(t in H)(c_t+N_tA)`

and makes `kappa(t)=c_t+[A,H]` surjective onto `A/[A,H]`. It does not prove
`[A,H]<=rad(beta)`, so `beta` cannot be passed to that coinvariant quotient.
Nor does a union cover ensure that two arbitrary covered points come from root
cosets forming the one commuting pair audited here. More basically, `(E6)`
does not even prove the two chosen basepoints commute.

Hence the exact identity/extra-term certificate does not reach `beta=0`, and
there is no commuting-pair lemma to inflate into a solution.

## Strategy outcome

`STRATEGY_EXHAUSTED` for `CPTR-PAIR-TRANSGRESSION` only.
`active_assignment_answered: no`.

The exact method-failure certificate is `(E0)` together with `(E6)--(E9)`:
the cycle invariant is coboundary-zero, while the desired pairing survives as
an uncontrolled and section-basepoint-sensitive carry term. This meets Lead's
authorized extra-term exit and stops the strategy early; it is not a verdict on
the scope.

- Research stop on exact extra-term certificate: `2026-08-17T07:31:03Z`;
  cumulative active minute: `265`.
- Packaging began immediately; all hard-kill and minute-300 gates are respected.
- Packaging and bus routing complete: `2026-08-17T07:32:50Z`; cumulative active
  minute: `267`. Thirty-three granted minutes remain unspent.

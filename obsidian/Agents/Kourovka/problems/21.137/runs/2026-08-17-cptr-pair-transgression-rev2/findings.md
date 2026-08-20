---
title: "CPTR-PAIR-TRANSGRESSION — exact cycle audit and reach failure"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: CPTR-PAIR-TRANSGRESSION
direction: proof
outcome: STRATEGY_EXHAUSTED
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
  - status/conjectured
---

# CPTR-PAIR-TRANSGRESSION — findings

## Active target

For every odd prime `p` and finite same-`p` group `G` of exponent exactly
`p^2`, prove that the actual value set `P={g^p:g in G}`, when it is a subgroup,
is abelian. This run uses only the reviewed hypothetical minimum-counterexample
coordinates and `(C1)--(C5)`. It does not answer the active target.

## Outcome

`STRATEGY_EXHAUSTED` for the one frozen method
`CPTR-PAIR-TRANSGRESSION`; `active_assignment_answered: no`.

The displayed shuffle is an exact normalized mod-`p` 3-cycle and its complete
scalar `(C4)` evaluation is section-independent. But the invariant value is the
pairing of a coboundary with a cycle and is therefore identically zero. Ordered
`(C5)` yields exact commuting-pair identities, yet the desired pairing
`beta(c_h,c_j)` remains an uncontrolled deep carry term. No bridge to
`beta=0` follows from actual-value coverage.

## 1. Boundary certificate

With

`partial[a|b|c]=[b|c]-[ab|c]+[a|bc]-[a|b]`,

the boundary of the `i`th summand of

`Z(h,j)=sum_(i=1)^(p-1)([j|h^i|h]-[h^i|j|h]+[h^i|h|j])`

is

`[j|h^(i+1)]-[j|h^i]-[j|h]+[h^i|j]+[h|j]-[h^(i+1)|j]`.

For commuting order-`p` elements `h,j`, summation telescopes to zero over
`F_p`. Thus the proposed signs and order are already correct.

## 2. Complete arbitrary section change

For `x'_t=x_tk_t`, `k_t=(eta_t,z_t)`, `k_1=1`, and `D_t=L_t-I`:

`L'_t=L_t`,

`ell'_t(a)=ell_t(a)+beta(L_ta,eta_t)`,

`c'_t=c_t+D_t^(p-1)eta_t`,

`d'_t=d_t+ell_t(D_t^(p-2)eta_t)
             +(1/2)beta(D_t^(p-2)eta_t,eta_t)`.

Moreover

`u'_(a,b)=k_(ab)^(-1)u_(a,b)alpha_b(k_a)k_b`,

so

`r'_(a,b)=-eta_(ab)+r_(a,b)+L_b eta_a+eta_b`.

For the scalar coordinate, take the ordered projected factors
`v_1=-eta_(ab)`, `v_2=r_(a,b)`, `v_3=L_b eta_a`, `v_4=eta_b`; then

`s'_(a,b)=-z_(ab)+s_(a,b)+z_a+ell_b(eta_a)+z_b
 +(1/2)sum_(m<n)beta(v_m,v_n)`.

This is the complete transformation; no central coordinate or alternating term
is suppressed.

## 3. Exact `(C4)` evaluation

Define

`Q(a,b,c)=ell_c(r_(a,b))
 +(1/2)beta(r_(ab,c),L_cr_(a,b))
 -(1/2)beta(r_(a,bc),r_(b,c))`.

The scalar row `(C4)` is exactly `Q=delta s`. Therefore

`Omega(h,j)=<Q,Z>=<s,partial Z>=0`.

The log records the full eight-term summand of `Omega`, retaining every
`ell`, action, and `1/2 beta` term. Under arbitrary section change,

`Omega'-Omega=<delta(s'-s),Z>=<s'-s,partial Z>=0`.

This is exact section invariance, but it also identifies the method's ceiling:
the numerical invariant is forced to be zero before any target-facing
interpretation.

## 4. Ordered `(C5)` and the surviving deep carry

Put

`v=u_(j,h)^(-1)u_(h,j)=(q,z)`,

`q=r_(h,j)-r_(j,h)`,

`z=s_(h,j)-s_(j,h)-(1/2)beta(r_(j,h),r_(h,j))`.

Since `hj=jh`, `x_h^(x_j)=x_hv`. Comparing the two sides after taking `p`th
powers with the exact ordered norm gives

`D_jc_h=D_h^(p-1)q`,                                      `(M1)`

`ell_j(c_h)=ell_h(D_h^(p-2)q)
             +(1/2)beta(D_h^(p-2)q,q)`.                    `(M2)`

The full coordinate expansion of `(C5)`, including the action exponents and
all pairwise `1/2 beta` terms, is in the log. Swapping `h,j`, commuting the
operators via `(C1)`, and using

`ell_t(D_t^(p-1)a)=beta(a,c_t)`

gives the strongest immediate pairing identity:

`beta(c_h,c_j)
 =ell_j(D_j^(p-2)D_h^(p-1)q)
 =ell_h(D_h^(p-2)D_j^(p-1)q)`.                              `(M3)`

No reviewed row makes this scalar zero.

## 5. Exact noncanonical-basepoint defect

Writing `N_t=D_t^(p-1)`, arbitrary section change gives

`q'=q+D_jeta_h-D_heta_j`

and makes `(M1)` covariant. But the target-facing basepoint pairing changes by

`beta(c'_h,c'_j)-beta(c_h,c_j)
 =beta(N_heta_h,c_j)+beta(c_h,N_jeta_j)
  +beta(N_heta_h,N_jeta_j)`.                                `(SD)`

The mixed bar invariant cannot therefore be identified with
`beta(c_h,c_j)` without an additional vanishing/correction lemma. For example,
changing only `eta_h` makes the defect

`-beta(eta_h,D_h^(p-2)N_jq)`,

and `(C1)--(C5)` as used here do not put that vector in `rad(beta)`.

## 6. Why actual-value coverage does not finish the argument

Coverage supplies

`A=union_(t in H)(c_t+N_tA)`

and a surjection `kappa:H -> A/[A,H]`. It does not prove
`[A,H]<=rad(beta)`, so `beta` cannot be passed to the coinvariant quotient.
Nor does a union cover guarantee that two arbitrary covered values come from
the one commuting pair of root cosets audited here. In fact `(M3)` does not
even prove the basepoints for that pair commute.

Thus there is no commuting-pair lemma to inflate into a solution, and there is
independently no exact coverage bridge to `beta=0`.

## Constraint-and-conclusion audit

| constraint_id | role | use/result |
|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | arbitrary odd `p` is retained, but a hypothetical minimum counterexample is not eliminated |
| `21.137-odd-p-not-2` | admissibility | used for `1/2` and mod-`p` bar arithmetic; no `p=2` input |
| `21.137-odd-finite-p-group` | admissibility | retained conditionally from the reviewed reduction |
| `21.137-odd-exponent-p2` | admissibility | retained conditionally; gives the reviewed exponent-`p` quotient/action setup |
| `21.137-odd-power-set-definition` | admissibility | only actual-value affine supports are used |
| `21.137-odd-power-set-subgroup` | admissibility | supplies the reviewed affine union cover, not a generated-subgroup substitute |
| `21.137-odd-P-abelian` | target conclusion | unresolved; equivalent here to `beta=0` |

## What this does not establish

- It does not prove `beta(c_h,c_j)=0`, even for the frozen commuting pair.
- It does not prove that `beta` descends to `A/[A,H]`.
- It does not turn the affine union cover into pairwise commuting coverage.
- It supplies no group, counterexample, or claim for the active scope.
- It says nothing about excluded clauses, primes, or stopped construction families.

## Evidence boundary

The full hand derivation and active-time ledger are in `log.md` beside this
file. No computation, web/history search, uncurated local history, `p=2`,
exponent-8 material, generated-subgroup substitution, stopped family,
wreath-shaped/quarantined material, or delegate was used.

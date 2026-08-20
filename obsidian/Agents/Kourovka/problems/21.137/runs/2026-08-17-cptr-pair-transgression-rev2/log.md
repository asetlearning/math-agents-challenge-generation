---
title: "Problem 21.137 run — CPTR pair transgression"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: CPTR-PAIR-TRANSGRESSION
direction: proof
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

# CPTR-PAIR-TRANSGRESSION working log

## Assignment lock

- Target: for every odd prime `p` and finite same-`p` group `G` of exponent exactly `p^2`, if the actual value set `P={g^p:g in G}` is itself a subgroup, prove that `P` is abelian.
- Exact working model: only the already reviewed hypothetical minimum-counterexample coordinates and equations `(C1)--(C5)` in the three curated request references.
- Frozen experiment: one commuting pair `h,j in H` of order `p`; boundary, arbitrary normalized section change, and then (only if invariant) evaluation of the scalar associativity obstruction.
- Exclusions: `p=2`; exponent-8 sibling; the general powerfulness clause; generated-subgroup substitutions; web/history; computation; wreath-shaped/quarantined material; all stopped families.
- Source/staleness gate: the canonical revision-2 scope records a passed visual source and independent scope audit. This is a discovery-blind run, so external staleness checking is deferred to Lead/human. No uncurated source or history was opened.
- Constraint reconciliation: all seven canonical rows are retained. The run is conditional on an arbitrary hypothetical minimum counterexample, so it cannot itself discharge `21.137-odd-forall-p-G` or `21.137-odd-P-abelian` without a separate global reach argument.

## Strategy portfolio

1. Theoretical mode (active): compute the proposed normalized bar-chain boundary and the induced scalar `(C4)` evaluation; test section invariance first.
2. Structured-construction mode (excluded here): no extension family may be repaired or enumerated in this run.
3. Catalogue/small-case mode (excluded here): the assignment forbids computation and all stopped families.
4. Certificate plan: either an exact boundary/section-change defect, or a line-by-line arbitrary-odd-`p` invariant evaluation plus a logically separate actual-value-coverage bridge. A commuting-pair lemma alone is only a partial result.

Kill rule: stop immediately on an exact invariance defect; otherwise stop manipulation by cumulative minute `290` and reserve through minute `300` for packaging.

## Active-time ledger

- Work start: `2026-08-17T07:09:43Z`; cumulative active minutes: `255`.

## Boundary and invariance gate

Use the normalized inhomogeneous bar differential over `F_p`, with trivial
coefficients,

`partial[a|b|c]=[b|c]-[ab|c]+[a|bc]-[a|b]`.

For one summand of

`Z=sum_(i=1)^(p-1)([j|h^i|h]-[h^i|j|h]+[h^i|h|j])`,

commutativity of `h,j` cancels all product terms and leaves

`[j|h^(i+1)]-[j|h^i]-[j|h]+[h^i|j]+[h|j]-[h^(i+1)|j]`.

Summing and using normalized bars (`[a|1]=[1|a]=0`) gives

`(-[j|h])-(p-1)[j|h]+[h|j]+(p-1)[h|j]=0`

over `F_p`. Thus the displayed shuffle already has the correct signs and
`partial Z=0`; no corrected chain is needed.

### Arbitrary normalized section change

Write `x'_t=x_t k_t`, `k_t=(eta_t,z_t) in A x F_p`, with `k_1=1`. Retain
`(a,z)(b,w)=(a+b,z+w+(1/2)beta(a,b))`,
`alpha_t(a,z)=(L_ta,z+ell_t(a))`, and
`x_ax_b=x_(ab)u_(a,b)`, `u_(a,b)=(r_(a,b),s_(a,b))`.

The complete action change is

`alpha'_t=iota_(k_t) alpha_t`, hence

`L'_t=L_t`,

`ell'_t(a)=ell_t(a)+beta(L_ta,eta_t)`.

The ordered norm formula gives

`c'_t=c_t+D_t^(p-1)eta_t`,

`d'_t=d_t+ell_t(D_t^(p-2)eta_t)
             +(1/2)beta(D_t^(p-2)eta_t,eta_t)`,

where `D_t=L_t-I`; the central coordinate `z_t` disappears because `p z_t=0`.
These are exactly the already checked norm-support coordinates, now used only
as a section-change identity.

For the carry, direct reassociation gives the group identity

`u'_(a,b)=k_(ab)^(-1) u_(a,b) alpha_b(k_a) k_b`.

Consequently

`r'_(a,b)=-eta_(ab)+r_(a,b)+L_b eta_a+eta_b`,

and, putting the ordered projected factors
`v_1=-eta_(ab), v_2=r_(a,b), v_3=L_b eta_a, v_4=eta_b`,

`s'_(a,b)=-z_(ab)+s_(a,b)+z_a+ell_b(q_a)+z_b
 +(1/2) sum_(1<=m<n<=4) beta(v_m,v_n)`.

This retains every central and alternating term; no coinvariant quotient has
been taken.

- Gate timestamp: `2026-08-17T07:11:31Z`; cumulative active minutes: `257`.

### Exact scalar evaluation and its invariance

Move every `s` term in `(C4)` to the right and define, without quotienting,

`Q(a,b,c)=ell_c(r_(a,b))
 +(1/2)beta(r_(ab,c),L_c r_(a,b))
 -(1/2)beta(r_(a,bc),r_(b,c))`.

Then the full scalar associativity row is exactly

`Q(a,b,c)=s_(a,bc)+s_(b,c)-s_(ab,c)-s_(a,b)=(delta s)(a,b,c)`.

Consequently its mixed evaluation is the following fully expanded identity:

`Omega(h,j)=sum_(i=1)^(p-1) {
 ell_h(r_(j,h^i))-ell_h(r_(h^i,j))+ell_j(r_(h^i,h))
 +(1/2)beta(r_(h^i j,h),L_h(r_(j,h^i)-r_(h^i,j)))
 -(1/2)beta(r_(j,h^(i+1)),r_(h^i,h))
 +(1/2)beta(r_(h^i,jh),r_(j,h))
 +(1/2)beta(r_(h^(i+1),j),L_jr_(h^i,h))
 -(1/2)beta(r_(h^i,hj),r_(h,j)) }=0`.

Here only `hj=jh` was used to combine the two second terms. Every `ell`, action,
and `1/2 beta` contribution remains visible.

The section-invariance calculation is exact but reveals the first limitation:
for every new section the same reassociation gives `Q'=delta s'`, and hence

`Omega'-Omega=<delta(s'-s),Z>=<s'-s,partial Z>=0`.

Thus the cycle evaluation is genuinely section-independent, but its invariant
value is forced to be zero because the entire nonlinear cochain is already the
coboundary `delta s`. It does not define a new scalar pairing. The complete
formula for `s'-s` above shows that this statement includes, rather than drops,
all central and alternating section-change terms.

- Invariance gate completed: `2026-08-17T07:17:39Z`; cumulative active minutes:
  `263`. No defect occurred, so proceed to the ordered `(C5)` reach audit.

## Ordered `(C5)` evaluation and strongest pair consequence

For `t` equal to `h` or `j`, put

`R_(t,i)=r_(t^i,t)`, `e_i=p-1-i`, `E_e=I+L_t+...+L_t^(e-1)`,

`a_(t,i)=L_t^(e_i)R_(t,i)`,

`b_(t,i)=s_(t^i,t)+ell_t(E_(e_i)R_(t,i))`.

The factors in `(C5)` occur in the exact order `i=p-1,p-2,...,1`. Hence its
two coordinates, with no omitted central term, are

`c_t=sum_(i=1)^(p-1) a_(t,i)`,

`d_t=sum_(i=1)^(p-1) b_(t,i)
 +(1/2)sum_(1<=k<i<=p-1) beta(a_(t,i),a_(t,k))`.

Now define the full commutator carry

`v=u_(j,h)^(-1)u_(h,j)=(q,z)`,

`q=r_(h,j)-r_(j,h)`,

`z=s_(h,j)-s_(j,h)-(1/2)beta(r_(j,h),r_(h,j))`.

Because `hj=jh`, direct cancellation in `G` gives

`x_h^(x_j)=x_h v`.

Taking `p`th powers, using the ordered norm on the right, and retaining the
full action on the left gives

`D_j c_h=D_h^(p-1)q`,                                      `(M1)`

`ell_j(c_h)=ell_h(D_h^(p-2)q)
             +(1/2)beta(D_h^(p-2)q,q)`.                    `(M2)`

The coordinate `z` contributes `p z=0`; it is accounted for and vanishes for
that exact reason. Swapping `h,j` gives

`D_h c_j=-D_j^(p-1)q`.                                    `(M1')`

For commuting `h,j`, `(C1)` also gives `L_hL_j=L_jL_h`. The ordered action-power
part of `(C5)` says, for every `a in A`,

`ell_t(D_t^(p-1)a)=beta(a,c_t)`.

Applying it for both `t=j` and `t=h`, then using `(M1)` and `(M1')`, produces
the exact coupling

`beta(c_h,c_j)
 =ell_j(D_j^(p-2)D_h^(p-1)q)
 =ell_h(D_h^(p-2)D_j^(p-1)q)`.                              `(M3)`

This is the strongest immediate pair statement. It is an equality, not a
vanishing result: none of `(C1)--(C5)` used above kills the displayed deep carry
term.

Subtracting the two ordered `(C1)` rows gives, for every `a`,

`ell_j(D_h a)-ell_h(D_j a)=beta(L_hL_j a,q)`.

At `a=D_j^(p-2)D_h^(p-2)q`, `(M3)` only yields

`beta(L_hL_jD_j^(p-2)D_h^(p-2)q,q)=0`;

it still does not imply `beta(c_h,c_j)=0`.

### Section covariance versus a target-facing pairing

Under `x'_t=x_t(eta_t,z_t)`, the projected commutator carry changes by

`q'=q+D_j eta_h-D_h eta_j`.

Equation `(M1)` is exactly covariant:

`D_jc'_h=D_jc_h+D_jD_h^(p-1)eta_h`,

while

`D_h^(p-1)q'=D_h^(p-1)q+D_h^(p-1)D_jeta_h-D_h^peta_j`;

these agree because `D_h,D_j` commute and `D_h^p=0`. The scalar equation
`(M2)` is likewise the central coordinate of the section-free group equality
`(x_h^p)^(x_j)=(x_h^(x_j))^p`. Separately, the full bar expression is the
already checked invariant `Omega=0`. Thus no section term was silently discarded;
this run does not need to assert an off-shell identification of those two zero
relations.

However, the target-facing basepoint pairing is not the scalar bar invariant.
Writing `N_t=D_t^(p-1)`, its exact section-change formula is

`beta(c'_h,c'_j)-beta(c_h,c_j)
 =beta(N_heta_h,c_j)+beta(c_h,N_jeta_j)
  +beta(N_heta_h,N_jeta_j)`.                                `(SD)`

The stated rows do not annihilate these cross terms. For example, with only
`eta_h` changed, self-adjointness of `N_h` and `(M1')` rewrite the defect as

`-beta(eta_h,D_h^(p-2)N_jq)`,

and no reviewed equation places `D_h^(p-2)N_jq` in `rad(beta)`. Therefore the
identity `Omega=0` cannot be identified with `beta(c_h,c_j)=0` without adding a
new, unproved correction/vanishing lemma.

### Exact reach gap to the active conclusion

Actual-value coverage gives the projected affine cover

`A=union_(t in H)(c_t+N_tA)`

and hence surjectivity of `kappa(t)=c_t+[A,H]` onto
`A/[A,H]`. It does **not** provide the two missing bridges:

1. `beta` need not descend to `A/[A,H]`; no row above proves
   `[A,H] <= rad(beta)`. Passing to coinvariants would therefore erase precisely
   the uncontrolled terms in `(SD)`.
2. A union cover does not say that two arbitrary covered points have roots whose
   cosets form the single commuting pair audited here. Even a hypothetical
   vanishing lemma for this one pair would not cover all pairs of actual values.

More basically, the exact pair identity `(M3)` does not vanish. Hence this run
does not even reach a commuting-pair commutativity lemma, much less the separate
coverage bridge required for `beta=0`.

## Strategy decision

The corrected bar chain is a cycle and its scalar evaluation is invariant, but
the invariant is exactly the zero pairing of a coboundary with a cycle. Ordered
`(C5)` extracts `(M1)--(M3)`; those formulas leave an explicit deep carry term
equal to `beta(c_h,c_j)`. Formula `(SD)` blocks identifying the invariant zero
with a canonical pairing of the chosen power basepoints. This is a checkable
algebraic ceiling, not merely unsuccessful manipulation.

Outcome: `STRATEGY_EXHAUSTED` for `CPTR-PAIR-TRANSGRESSION` only.
`active_assignment_answered: no`. No claim about the unrestricted scope.

- Research stop: `2026-08-17T07:21:20Z`; cumulative active minutes: `267`.
- Packaging begins with `33` of the granted minutes unspent. No computation,
  web/history, uncurated file, excluded scope, stopped family, or delegate was used.

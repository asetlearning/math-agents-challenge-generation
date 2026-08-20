---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/group-algebras
  - project/kourovka
  - status/draft
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: proof
strategy: PRIME-UNIFORM-ROOTCOUNT-AUGMENTATION
active_assignment_answered: no
---

# PRIME-UNIFORM-ROOTCOUNT-AUGMENTATION log

## 2026-08-17T23:26:45Z — active work starts

Official cumulative ledger at start: **699 minutes**.  Exact target retained:
`p>2` is prime, `G` is a finite same-`p` group of exponent exactly `p^2`,
`P={g^p:g in G}` is the literal actual-value set and is itself a subgroup, and
the question is whether `P` must be abelian.  The `p=2`, exponent-eight clause
is excluded.  No web or computation is used.

Let `k=F_p`, `I=ker(epsilon:kG->k)`,

`X_a={x in G:x^p=a}`, `r(a)=|X_a|`, and
`R=sum_(x in G)x^p=sum_(a in P)r(a)a in kG`.

The planned test is first coefficientwise, then in the first Jennings layer in
which a nontrivial element of `[P,P]` could survive.

## 2026-08-17T23:29:19Z — exact cyclic cancellation; research hard-kill

### 1. Every coefficient of `R` vanishes

For `a in P-{1}`, every `x in X_a` has order `p^2`, and `a=x^p` has order
`p`.  The rule

`tau_a(x)=xa=x^(p+1)`

is a free `C_p`-action on `X_a`: `x` commutes with its power `a`, so
`(xa^j)^p=x^p a^(jp)=a`, and the `p` elements `x,xa,...,xa^(p-1)` are
distinct.  Hence

`r(a)=0 mod p` for every `a != 1`.

Also `|G|=sum_(a in P)r(a)=0 mod p`; therefore `r(1)=0 mod p`.  Thus the
all-root element specified by the strategy satisfies the exact, prime-uniform
identity

`R=0 in F_pG`.

This uses neither subgroup closure nor commutativity and so cannot distinguish
a hypothetical counterexample from any other exponent-`p^2` `p`-group.
Equivalently, the single-variable identity
`x^p-1=(x-1)^p` gives `sum_x (x-1)^p=R=0` in `I^p`.

### 2. Jennings projection cannot restore a target term

Because `R` is already zero in `kG`, its image is zero in every quotient
`I^n/I^(n+1)`.  In particular, closure does give the equality
`P=G^p` (literal set equals the subgroup it generates), whence
`P <= D_p(G)` and `[P,P] <= D_(2p)(G)` for the Jennings dimension series.
If `d>=2p` is the first degree in which some `c in [P,P]` has nonzero symbol
`c-1`, the image of `R` in `I^d/I^(d+1)` is still zero coefficientwise; it
contains no isolatable coefficient of that symbol.

### 3. Dividing the integral counts by `p` returns uncontrolled weights

Writing `r(a)=p s(a)` over the integers and reducing
`Rhat=sum_a s(a)a` modulo `p` is a different observable: division by `p`
does not exist in `kG`.  It is central and has augmentation zero, since exact
exponent `p^2` implies `|G|>=p^2` and
`sum_a s(a)=|G|/p=0 mod p`.  But literal support only says `r(a)>0`; it gives
no nonzero or uniform residue for `s(a)=r(a)/p mod p`.

More sharply, conjugation gives `s(a^b)=s(a)`.  For `b in P` (so `b^p=1`),
each nonfixed conjugation orbit is
`O={a_0,a_1,...,a_(p-1)}`, `a_(i+1)=a_i^b`, and its entire contribution to
the centrality commutator is

`s(O) sum_i (a_i b-b a_i)
 =s(O)b sum_i (a_(i+1)-a_i)=0`.

The cancellation occurs before passing to a Jennings quotient.  Thus, at the
first possible noncentral layer, a target commutator and all its cyclic
translates cancel orbitwise.  Selecting one term would require information
about individual normalized root counts not supplied by literal-image closure.

This meets two stated hard kills: cyclic cancellation removes the target term,
and the only possible normalized salvage has uncontrolled coefficients
`s(a)`.  It supplies no new cross-fibre identity and does not reduce the active
target.

Research stops after **3 active minutes**, at official cumulative minute
**702**.  Packaging begins; the sole outcome will be `STRATEGY_EXHAUSTED` for
this named observable, with `active_assignment_answered: no`.

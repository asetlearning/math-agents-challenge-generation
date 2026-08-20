---
title: "Fibre multiplicity affine obstruction — working log"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: proof
strategy: FIBRE-MULTIPLICITY-AFFINE-OBSTRUCTION
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/power-maps
  - project/kourovka
  - status/draft
active_assignment_answered: no
---

# Active target

For an odd prime `p`, a finite `p`-group `G` of exponent exactly `p^2`, and
the literal set `P={g^p:g in G}`, test whether the hypothesis that `P` itself
is a subgroup forces `P` to be abelian.  The `p=2`, exponent-eight sibling is
excluded.

## 2026-08-17T23:09:26Z — work start

Official cumulative ledger at start: `685` active minutes.  Read the common
protocol, role file, revision-2 scope, roster, and the sole unread Lead
decision in the prescribed order.  No computation is authorized or used.
The named task is to derive section/root-change covariance before using root
multiplicities, perform one exact weighted double count, and stop the method
if literal-image closure controls support only.

## 2026-08-17T23:19:23Z — exact fibre law and covariance

Work in an arbitrary elementary normal section, so the calculation applies in
particular to the proposed first section on which a commutator survives.  Let

```text
K normal N normal G,       V=N/K elementary abelian,
E=G/K,                     Q=G/N.
```

Write `V` additively.  Choose a normalized section `sigma:Q->E`, put

```text
M_q(v)=sigma(q) v sigma(q)^(-1),
sigma(q)^p=lambda_q sigma(q^p),
N_q=1+M_q+...+M_q^(p-1).
```

Every element of the `q`-fibre of `E->Q` is uniquely `v sigma(q)`.  Direct
collection, with no power-map homomorphism assumption, gives

```text
(v sigma(q))^p=(lambda_q+N_q(v)) sigma(q^p).                 (F1)
```

Consequently its affine projected support is exactly

```text
S_q=lambda_q+im(N_q),
```

and the number of *actual elements of G* in the `q`-fibre whose power has
projected target coordinate `w` is

```text
m_q(w)=|K| |ker(N_q)| 1_[w in S_q].                         (F2)
```

Indeed each solution `v` of the affine equation has exactly `|K|` lifts to
`G`, and every such lift has the same power modulo `K`.  Thus deeper kernel
coordinates do not disturb the projected count, although (F2) says nothing
about how that count splits among the individual target lifts over `w`.

The covariance has to be recorded before assigning invariant meaning to
these coordinates.  For an arbitrary normalized section change

```text
sigma'(q)=u_q sigma(q),       u_q in V, u_1=0,
```

the action is unchanged (because `V` is abelian), while, for `t=q^p`,

```text
lambda'_q=lambda_q+N_q(u_q)-u_t.                            (C1)
```

The same root has new domain coordinate `v'=v-u_q` and new target coordinate
`w'=w-u_t`, so

```text
lambda'_q+N_q(v')=lambda_q+N_q(v)-u_t,
m'_q(w')=m_q(w'+u_t),       S'_q=S_q-u_t.                  (C2)
```

In particular, changing only the chosen root origin inside its `q`-fibre
(`u_t=0`) changes `lambda_q` by `N_q(u_q)` and translates the domain
parameter, but leaves the actual support and every multiplicity unchanged.
A target-section change merely translates all fibres with the same `t`.
Thus the coordinate-free datum is a weighted subset of that target fibre;
the coordinate function itself is covariant, not literally invariant.

## 2026-08-17T23:19:23Z — one weighted double count

Fix `t in Q`, put `R_t={q in Q:q^p=t}`, and define the projected actual-root
multiplicity

```text
mu_t(w)=sum_[q in R_t] m_q(w).
```

For every linear subspace `W<=V` and every `a in V`, double-counting roots
first by their target coordinate and then by their quotient-root fibre gives
the exact identity

```text
sum_[w in a+W] mu_t(w)
 = |K| sum_[q in R_t] |ker N_q|
       |(a+W) intersect (lambda_q+im N_q)|                 (D1)
 = |K| sum_[q whose supports meet a+W]
       |ker N_q| |W intersect im N_q|.
```

At `W=V` this reduces, using rank-nullity, to

```text
sum_[w in V] mu_t(w)=|K||V||R_t|=|N||R_t|.                (D2)
```

Equivalently, for an additive character `chi` of `V`, the same double count
has the Fourier form

```text
hat(mu_t)(chi)
 = |K||V| sum_[q in R_t, chi|im(N_q)=1] chi(lambda_q).     (D3)
```

Under (C1)--(C2), (D3) is multiplied by the harmless common phase
`chi(-u_t)`.  Hence its vanishing is section-independent.  Constancy of
`mu_t` on cosets of `W` would require (and is equivalent to) vanishing of
`hat(mu_t)(chi)` for every `chi` nontrivial on `W`.  Neither (D1) nor (D3)
forces those character sums to vanish.

## 2026-08-17T23:19:23Z — what literal-image closure actually says

Let `Pbar=PK/K`, the image in `E` of the literal power set.  Because the
literal set is assumed to be a subgroup, `Pbar` is a subgroup.  Put
`U=Pbar intersect V`.  In a fixed target fibre `t`, its coordinate support is
either empty or one affine coset `a_t+U`.  Since every point of `Pbar` is an
actual power,

```text
supp(mu_t)=a_t+U.                                           (S1)
```

This is the whole implication of subgroup closure at the level of the
weighted incidence data.  It says `mu_t(w)>0` on that coset and zero outside;
translation in the subgroup does not lift to a bijection between sets of
roots, so it supplies no equation `mu_t(w)=mu_t(w+u)`.  Power-map
equivariance separately gives conjugacy invariance of full root counts, but
that also does not give translation invariance.  The alternating commutator
form does not occur in (D1)--(D3), so nonisotropy by itself adds no missing
weight equation.

## 2026-08-17T23:19:23Z — compatible nonisotropic weighted model

The absence of a weight constraint is witnessed by the following exact
prime-uniform affine-incidence model.  It is deliberately **not** asserted to
be a group extension or a counterexample.

Let `V=F_p^2`, let `C=F_p`, and let

```text
beta((x,y),(x',y'))=x y'-x' y.
```

The odd-prime Heisenberg label group

```text
H=V x C,
(v,z)(v',z')=(v+v', z+z'+(1/2)beta(v,v'))
```

is an exponent-`p` nonabelian subgroup support, with nondegenerate
commutator form `beta`.  Index quotient-root fibres by
`q=(a,b,c,d,e) in F_p^5`.  Take the selected elementary section to be
`V=H/C`, take a deeper-kernel factor of size `|K|=p`, give every fibre
quotient-root variation space `V`, set `M_q=I`, and hence `N_q=pI=0`.
Its affine projected support is the singleton with projected coordinate
`(a^(p-1)b,c^(p-1)d)`; prescribe the central target lift `e`, so the full
label is

```text
Lambda(q)=((a^(p-1)b, c^(p-1)d),e) in H,
```

and its full fibre weight is `|K||ker N_q|=p^3`.

If

```text
h(0)=2p-1,       h(x)=p-1 for x!=0,
```

then the aggregate weight at `((x,y),z)` is exactly

```text
r((x,y),z)=p^3 h(x)h(y).                                   (M1)
```

This follows because `a^(p-1)b=x` has `2p-1` solutions when
`x=0` and `p-1` solutions when `x!=0`.  Thus every point of the nonabelian
subgroup `H` occurs, but the weights are positive and nonconstant.  In fact
the Fourier transform of `h` is `p^2` at the trivial character and `p` at
every nontrivial character, so (M1) is not invariant under translation by
any nonzero subspace of `V`.

The model also satisfies the exact total double count
`sum_H r=p^8=p^5*p^3`, inversion symmetry, and conjugacy invariance: its
weight is unchanged by sign, and Heisenberg conjugacy changes only `z` while
(M1) is independent of `z`.  Root-origin covariance is automatic because
all `N_q` vanish, and target-origin change merely relabels by translation.
It therefore satisfies (F1)--(F2), (C1)--(C2), (D1)--(D3), subgroup support,
and the obvious symmetries while retaining a nonisotropic commutator form.
What it does not supply is a factor system realizing `Lambda` as an actual
power map.  That missing cross-`q` multiplication datum is precisely not a
consequence of literal-image closure or of the weighted affine identities.

## Method decision

The named hard kill fires: closure controls support but supplies no root-weight
equation, and the compatible model above defeats every constancy conclusion
obtainable from the derived affine multiplicities and their one exact double
count.  Any further proof would need an additional cross-fibre group-law
identity; the assigned weighted observable alone cannot provide it.  This is
`STRATEGY_EXHAUSTED` for
`FIBRE-MULTIPLICITY-AFFINE-OBSTRUCTION`, not a judgement on the source scope.
`active_assignment_answered: no`.

## 2026-08-17T23:22:43Z — work stop and package

Stopped immediately on the named method-failure certificate, well before the
30-minute research cutoff.  Charged `14` active minutes (rounded up), moving
the official cumulative ledger from `685` to `699`; `21` authorized minutes
return unused.  Wrote `outcome.md` and a `REPORT` to Lead.  No computation,
web/history access, excluded clause, or prospective target claim occurred.

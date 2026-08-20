---
title: "Kourovka 20.49 — base-preimage prime cover"
problem: "20.49"
scope_id: 20.49/two-generated-same-exponent
assignment_revision: 1
direction: proof
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/exponent
  - topic/subdirect-product
  - project/kourovka
  - status/draft
---

# Base-preimage prime cover

## 2026-08-17T14:15:16Z — active work start

- Fresh run directory: `Agents/Kourovka/problems/20.49/runs/2026-08-17-r3-base-preimage/`.
- Controlling message: `2026-08-17T141100Z__Lead__DECISION__base-preimage-prime-cover.md`.
- Active scope: revision 1, universal finite-group assertion with an at-most-two-generated subgroup of exactly the ambient exponent.
- Authorized resources: canonical scope and Validator-reviewed fibre-product/profile criterion only; no computation or web search.
- Charged-time ledger for this continuation starts at 0 active minutes (centralized prior-use figure: 65 minutes); local hard cap 45 minutes and invariant-reset gate at 30 minutes.

### Starting reviewed setup

Assume that `G` is a least-order counterexample with distinct minimal normal
subgroups `M,N`. Put

```text
A=G/M,  B=G/N,  C=G/MN,
```

so `G=A x_C B` and `exp(G)=lcm(exp(A),exp(B))`. For arbitrary compatible maps
`F_2 -> A,B`, the exponent of the resulting image in `G` is the lcm of the two
projected image exponents. A successful profile need only have full lcm; neither
factor image need have full factor exponent. Only the common map to `C` can be
required epimorphic in a successful least-counterexample profile.

### Strategy portfolio

1. **BASE-PREIMAGE-PRIME-COVER (authorized theoretical route).** Choose an
   at-most-two-generated `D<=C` with `exp(D)=exp(C)`, form its inverse images in
   `A,B,G`, and compare every maximal prime-power exponent. Seek a prime-cover
   contradiction or a complete defect table.
2. **Epimorphic-lift refinement (alternative if a new invariant appears).** Fix
   an epimorphism `F_2 -> D` and distinguish exponents attainable by lifts of that
   particular Nielsen class from exponents of the full inverse-image groups.
3. **Chief-kernel localization (representation-changing alternative, not yet
   authorized).** Translate simultaneous prime-power loss into action/extension
   data on the two commuting minimal kernels `M,N`.
4. **Certificate plan.** Any positive lemma must give an explicit compatible base
   orbit and factor exponents whose lcm is `exp(G)`. A negative outcome must list
   valuation inequalities prime by prime and identify exactly why full inverse-
   image exponents do not imply attainable epimorphic two-generator profiles.

The first route is the cheapest certifiable test and is the only active strategy.

## 2026-08-17T14:19:08Z — inverse-image identities and a new support invariant

Let `q:G->C`, let `alpha:A->C` and `beta:B->C`, and choose by minimality an
at-most-two-generated `D<=C` with `exp(D)=exp(C)`. Write

```text
A_D=alpha^{-1}(D),  B_D=beta^{-1}(D),  P_D=q^{-1}(D).
```

Then, without any choice of generators,

```text
P_D=A_D x_D B_D,
exp(P_D)=lcm(exp(A_D),exp(B_D)).                 (1)
```

The proof is the same two-projection divisibility argument as in the reviewed
criterion. If `D<C`, all three inverse images are proper in their respective
ambient groups, and specifically `P_D<G`. Least-counterexample proper-subgroup
drop therefore gives `exp(P_D)<exp(G)`.

Put, for every prime `p`,

```text
g_p=v_p(exp(G)), a_p=v_p(exp(A)), b_p=v_p(exp(B)), c_p=v_p(exp(C)),
a_p(D)=v_p(exp(A_D)), b_p(D)=v_p(exp(B_D)),
s_p(D)=max(a_p(D),b_p(D)).
```

The exact inequalities are

```text
c_p <= a_p(D) <= a_p <= g_p,
c_p <= b_p(D) <= b_p <= g_p,
g_p=max(a_p,b_p),  s_p(D)=v_p(exp(P_D)).        (2)
```

Define the fixed common-defect set

```text
S(D)={p:s_p(D)<g_p}.                            (3)
```

Thus `D<C` implies `S(D)` is nonempty. Every `p in S(D)` necessarily satisfies
`c_p<g_p`. More strongly, since `P_D` contains both `M` and `N`,

```text
v_p(exp(M))<g_p and v_p(exp(N))<g_p.            (4)
```

So a defect prime cannot be carried at top height by the base or by either
minimal normal kernel. It is necessarily an **extension-created (mixed) maximal
prime power** in at least one of `A=N.C` and `B=M.C`.

This can be packaged as an exact base-support invariant. For `X=A,B`, define

```text
Sigma_{X,p}={c in C : some x in X over c has v_p(|x|)=g_p},
Sigma_p=Sigma_{A,p} union Sigma_{B,p}.
```

Then

```text
p in S(D)  iff  D cap Sigma_p is empty.         (5)
```

Indeed membership in the intersection is exactly the existence of a top-height
`p`-element in one factor inverse image. Each nonempty `Sigma_{X,p}` is stable
under conjugacy in `C` and under powers coprime to `p`. Therefore every proper
two-generated full-exponent base subgroup must avoid at least one nonempty,
conjugacy-stable top-lift support set `Sigma_p`, despite itself realizing the full
quotient exponent. This is a genuine invariant beyond the earlier orbit-set
intersection shorthand.

## 2026-08-17T14:22:15Z — prime-cover generation lemma

The support invariant has a useful global consequence. For every `p in S(D)`,
choose arbitrarily an element `c_p in Sigma_p`, and put

```text
L=<D, c_p (p in S(D))> <= C.
```

For primes outside `S(D)`, `P_D<=P_L` already contains the global top prime
power. For `p in S(D)`, the chosen `c_p` has a top-height lift in `A_L` or `B_L`.
Hence (1) gives `exp(P_L)=exp(G)`. Proper-subgroup exponent drop now forces

```text
C=<D, c_p (p in S(D))>.                         (6)
```

This holds for **every** choice of one support element per defect prime. More
generally, for every `D<=L<C`, monotonicity gives `S(L) subseteq S(D)` and
`S(L)` nonempty. Thus the interval of proper overgroups of `D` is covered by the
avoidance conditions `L cap Sigma_p=empty`, `p in S(D)`.

There is also an actually attainable near-witness. Since `P_D<G`, minimality
supplies an at-most-two-generated `K_D<=P_D` with

```text
exp(K_D)=exp(P_D).
```

So `K_D` misses relative to `G` exactly the fixed primes/levels encoded by
`S(D)` and its valuation vector `s_p(D)`. Its common base image is some
`E=q(K_D)<=D<C`, however, and is therefore non-epimorphic in `C`. The obstruction
is not failure to realize the inverse-image exponent by two generators; it is the
inability to retain that profile while enlarging the common base image to `C`.

Finally, a carrier-level refinement of (4) is exact. If `A` carries the top
`p`-height (`a_p=g_p`) and `p in S(D)`, choose a `p`-element `x in A` of order
`p^{g_p}`. If its image in `C` has order `p^t`, then

```text
0<t<g_p,  x^(p^t) in N has order p^(g_p-t),
so p divides both C and N and g_p<=c_p+v_p(exp(N)).
```

The analogous statement uses `M` when `B` is a carrier. Hence every fixed defect
prime is genuinely mixed between a quotient `p`-part and at least one minimal
normal kernel; it cannot be a pure base or pure-kernel prime.

## 2026-08-17T14:23:20Z — exact rank/profile obstruction dichotomy

The known three-generator clause plus proper-subgroup exponent drop gives
`d(G)=3`, hence `d(C)<=3`. There are exactly two cases relevant to this route.

### Case I: `d(C)=3`

Every at-most-two-generated full-exponent `D` supplied inside `C` is proper.
Consequently it has the nonempty fixed defect set `S(D)` in (3), each defect is
mixed as in (4), and every support transversal generates `C` with `D` as in (6).
There is no epimorphism `F_2->C`, so the reviewed necessary epimorphic base
profile cannot even be formed. This is an exact base-rank obstruction, not an
orbit-intersection argument.

### Case II: `d(C)<=2`

Take `D=C`. The inverse images are `A,B,G`, so `S(C)` is empty and the group-level
prime-cover argument has reached its limit. Let `Pi` be the primes dividing
`exp(G)`, let `O` range over precomposition orbits in `Epi(F_2,C)`, and retain the
reviewed attainable exponent sets `E_A(O),E_B(O)`. For `r in E_A(O)` and
`s in E_B(O)`, define maximal-prime-power loss sets

```text
L_A(r)={p in Pi:v_p(r)<g_p},
L_B(s)={p in Pi:v_p(s)<g_p}.                    (7)
```

Because the factor image maps onto `C`, `exp(C)` divides both `r` and `s`.
Therefore all these loss sets lie inside

```text
R={p:c_p<g_p}.                                  (8)
```

The reviewed lcm criterion becomes the exact primewise statement

```text
lcm(r,s)=exp(G)  iff  L_A(r) cap L_B(s)=empty.  (9)
```

Thus the complete residual obstruction is

```text
for every epimorphic orbit O and every
r in E_A(O), s in E_B(O),
L_A(r) cap L_B(s) is nonempty.                  (10)
```

Equivalently, the two attainable loss-set families are cross-intersecting in
every epimorphic Nielsen orbit. This formulation permits arbitrary complementary
factor exponents. It neither requires nor tests a common orbit carrying both full
factor exponents.

Although the ambient valuation vectors `(a_p)` and `(b_p)` have no common loss
(`g_p=max(a_p,b_p)`), they need not be attainable over any epimorphic base orbit.
Minimality only supplies full-factor witnesses over possibly non-epimorphic and
different base images. Nor are the attainable profile families known to be closed
under coordinatewise maxima. Those are the two exact points at which the inverse-
image data fail to force a compatible profile.

## 2026-08-17T14:24:13Z — active work stop (9 cumulative local active minutes)

Outcome: `PARTIAL_RESULT`. The base-preimage strategy produced a fixed mixed-prime
support invariant and the support-transversal generation lemma, then reached the
complete rank/profile obstruction dichotomy. It did not force a compatible
epimorphic profile and does not answer the universal scope. Research is stopped
pending Lead's next decision; this is an `awaiting_lead` handoff, not a self-park.

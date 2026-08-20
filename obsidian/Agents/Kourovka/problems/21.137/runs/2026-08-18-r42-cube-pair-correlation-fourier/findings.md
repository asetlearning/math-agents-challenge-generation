---
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: proof
cycle: 30
outcome: STRATEGY_EXHAUSTED
active_assignment_answered: no
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - project/kourovka
  - status/conjectured
---

# CUBE-PAIR-CORRELATION-FOURIER outcome

## Active target

For every odd prime `p` and finite `p`-group `G` of exponent exactly `p^2`, if
the literal set `P={g^p:g in G}` is a subgroup, prove that `P` is abelian. The
`p=2`, exponent-eight clause and the general powerfulness question are excluded.

## Outcome

`STRATEGY_EXHAUSTED` for the `K`-only central-character mechanism. The complete
coupled kernel has exact identities beyond all one-variable marginals, but in the
minimum-counterexample branch `P'=C_3` those identities leave one genuinely
three-variable skew Fourier line arbitrary. It detects `[a,b]` but does not force
it to vanish. The unrestricted target remains open.

## Exact partial facts

1. A least counterexample has `P'=C_p<=Z(G)`: quotient by an order-`p` subgroup
   of `P' cap Z(G)` preserves exact exponent `p^2` and literal-image closure, so
   minimality makes the quotient power subgroup abelian.
2. For `R(a)=#{x:x^3=a}`, all pair marginals are
   `sum_c K=R(a)R(b)`, `sum_b K=R(a)R(c)`, and
   `sum_a K=R(b)R(c)`.
3. With `[r,s]=r^-1 s^-1 r s`, complete root-pair bijections give
   `K(a,b,c)=K(a,b^a,c^a)=K(a^b,b,c^b)=K(a^c,b^c,c)`, together with
   `K(a,b,c)=K(b,c^-1,a^-1)=K(c,b^-1,a)`.
4. In `P'=Z=<z>=C_3`, for value cosets `A,B,C`, let
   `(delta,epsilon,zeta)=(beta(A,B),beta(B,C),beta(C,A))`. A nonzero Fourier
   block at frequency `(r,s,t)` must satisfy
   `-s delta+t zeta=r delta-t epsilon=-r zeta+s epsilon=0`; if the pairing
   triple is nonzero, this is exactly
   `(r,s,t) in F_3(epsilon,zeta,delta)`.
5. Hence `K` is arbitrary on the three level sets of
   `sigma=epsilon i+zeta j+delta k`. For `[a,b]!=1`, choosing `C=A+B` makes all
   three coefficients nonzero, so the two nonzero skew blocks are invisible to
   every marginal.

Every sign and derivation is in
`Agents/Kourovka/problems/21.137/runs/2026-08-18-r42-cube-pair-correlation-fourier/log.md`.

## Exact method-obstruction certificate

On the nonabelian value group `H_3(3)`, the positive integral formal array
`K_form=27+h(sigma)` when all three pairings are nonzero and `K_form=27`
otherwise, with `h(0)=2`, `h(1)=h(2)=-1`, has:

- values `26,27,29`;
- every pair marginal equal to `729` (formal `R=27`);
- all three value-conjugation identities and both Hurwitz identities;
- nonzero skew transforms `Khat(w)=Khat(-w)=27` at a triple with
  `[a,b]!=1`.

The exact checker is
`Agents/Kourovka/problems/21.137/runs/2026-08-18-r42-cube-pair-correlation-fourier/scratch/check_formal_skew_kernel.py`,
SHA-256 `2af3af2d92b2a52b19b9f16168c35faf3b099ba5047522a0ba5708b940f8214f`.

This is deliberately **not a group, not a cube map, and not a counterexample**.
It proves only that the named `K`-level equations do not imply abelianity.

## Exact bottleneck and recommendation

The Hall identity `(xy)^3=x^3 y^(x^2)y^x y` depends on the action on `P` of the
particular root `x`. Writing
`K_x(b,c)=#{y:y^3=b,(xy)^3=c}`, one has the exact stronger identity
`K_x(b,c)=K_x(b^x,c^x)`, but `K=sum_(x^3=a)K_x` forgets those individual
actions; `a=x^3` determines only `(conj_x|P)^3=conj_a|P`. This is precisely the
information carried by the unconstrained skew block.

Recommended representation change: if Lead grants another lane, refine by the
conjugation action of each root (an action-resolved correlation), and impose a
hard early gate asking whether summing its character blocks produces a
choice-independent identity on values. Do not continue manipulating `K` alone,
its marginals, or its skew coordinate.

## Constraint status

All seven canonical rows were retained. No proof covers the universal row and no
finite group violates the conclusion, so `active_assignment_answered: no`.


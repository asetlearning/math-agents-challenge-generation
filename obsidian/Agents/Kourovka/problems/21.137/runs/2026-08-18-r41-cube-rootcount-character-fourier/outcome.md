---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/character-theory
  - project/kourovka
  - status/conjectured
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: proof
cycle: 29
outcome: STRATEGY_EXHAUSTED
strategy: CUBE-ROOTCOUNT-CHARACTER-FOURIER
active_assignment_answered: no
active_minutes_charged: 45
cumulative_active_minutes: 886
---

# STRATEGY_EXHAUSTED — one-variable cube-root character/Fourier spectrum

## Outcome

`CUBE-ROOTCOUNT-CHARACTER-FOURIER` meets its exact method kill: the complete
one-variable complex transform yields a prime-uniform integral-virtual-character
theorem, but full support and all resulting integrality, Galois, positivity,
central-character, induction, and cyclic-root-incidence rows admit an explicit
nonabelian formal spectrum. This is a method obstruction only. The unrestricted
odd-prime scope remains unanswered.

## Exact derived result

Let `p` be odd, let `G` be a finite `p`-group of exponent `p^2`, and suppose its
literal power image `P={g^p:g in G}` is a subgroup. For

`R(a)=#{g in G:g^p=a}`

and every `chi in Irr(P)`, one has

`c_chi=<R,chi>_P=nu_p(Ind_P^G(overline(chi))) in Z`.

With `Rhat(rho)=sum_a R(a)rho(a^(-1))`, the full matrix transform is

`Rhat(rho_chi)=(|P|c_chi/chi(1))I_(chi(1))`.

The zero-extension `Zeta_p` to `G` also satisfies

`<Zeta_p,Psi>_G=nu_p(overline(Psi)) in Z`,

`Ind_P^G(R)=[G:P]Zeta_p`, and

`<R,Res_P^G(Psi)>_P=[G:P]nu_p(overline(Psi))`.

The derivation is by finite-sum reindexing. Integrality of higher indicators is
proved as the trace of the cyclic permutation on `(W^(tensor p))^G`, followed by
Galois invariance.

In a minimum-order counterexample at a fixed odd `p`, an independent central
quotient argument gives `P'=C_p<=Z(G)`. If `chi` has central character `lambda`,
its coefficient is the `lambda`-central discrete transform of the fibre counts.
The central scalar supplies no contradiction because it becomes trivial on the
`p`-fold tensor power. Also `p|R(a)`, `R(a^u)=R(a)` for `p` not dividing `u`, and
for `a!=1`, `R(a)/p` counts cyclic order-`p^2` subgroups with `C^p=<a>`.

Full derivation: `log.md` in this run directory.

## Exact method-failure certificate

Let `P=E_n` be extraspecial of exponent `p`, order `q=p^(1+2n)`, and
`P'=Z(P)=C_p`. Define the formal root distribution

`F(a)=q` for every `a in P`.

It has full support, total `q^2`, formal index `q`, `F(1)=|P|`, fibre divisibility,
scalar-power invariance, exact cyclic-root-line incidence, and automorphism
invariance. Its character expansion is simply `F=q 1_P`: the trivial Fourier
scalar is `q^2` and **every nontrivial linear and nonlinear central-character
block is zero**. The blocks are PSD, all Galois/orbit rows pass, and its formal
zero-extension is the genuine permutation character `Ind_P^G(1_P)` for any
normal index-`q` embedding, so the full induction divisibility row passes too.

At `p=3,n=2`, `P=3_+^(1+4)` has order `243`, `P'=C_3`, two nonlinear irreducibles
of degree `9`, and

`F(a)=243`, `sum_a F(a)=59049=3^10`.

All `121` order-three lines receive `81` formal cyclic order-nine lifts; this gives
`9801*6=58806` formal order-nine elements plus `243` identity-fibre elements,
exactly `59049`. Thus the spectrum survives even the elementary literal-root
incidence audit. It is **not a group and not a counterexample**: realization as
the actual cube map is the missing condition.

## Missing word-map identity

The one-variable transform forgets the coupled kernel

`K(a,b,c)=#{(x,y):x^p=a, y^p=b, (xy)^p=c}`.

Its marginals are determined by `R`, but its nontrivial-central-character transform
is not. Any live continuation must derive an exponent-`p^2` identity for this
two-root kernel (or an equivalent Hall-defect/commutator correlation) that goes
beyond the marginal commutator-word sum. Another integrality, positivity, or
central Fourier constraint on `R` alone cannot distinguish the formal extraspecial
spectrum.

## Seven-row exact-scope audit

| constraint_id | role in result | status |
|---|---|---|
| `21.137-odd-forall-p-G` | transform theorem is prime-uniform; obstruction specializes at `p=3` | universal target not proved |
| `21.137-odd-p-not-2` | only odd `p`; main model uses `p=3` | kept |
| `21.137-odd-finite-p-group` | theorem assumes finite same-`p` `G`; obstruction uses finite abstract `P` but no actual `G` | no candidate |
| `21.137-odd-exponent-p2` | theorem uses exact `p^2`; formal incidence uses order-`p^2` roots but does not realize a group | no candidate |
| `21.137-odd-power-set-definition` | theorem uses the literal image; formal spectrum is not shown to be a literal word map | missing realization row |
| `21.137-odd-power-set-subgroup` | theorem uses subgroup closure to make `P` the transform group; formal `P` is abstract only | no candidate |
| `21.137-odd-P-abelian` | formal `P` is deliberately nonabelian, but is not target-equal | conclusion unresolved |

The `p=2` exponent-eight sibling and general powerfulness question were not used.

Timing note: an unexplained `kv_now` jump occurred during final bus packaging, so
the run conservatively charges the entire authorized 45-minute increment and stops
at cumulative minute `886`; see the end of `log.md` for both observed timestamps.

## Recommendation

Do not continue refining the one-variable spectrum. If Lead spends another proof
increment, change representation to the nontrivial-central-character Fourier
transform of `K(a,b,c)` and require by an early hard gate an exact Hall/power
identity not implied by its marginals. Otherwise route this exact method exhaustion
to MathExpert for a genuinely different strategy.

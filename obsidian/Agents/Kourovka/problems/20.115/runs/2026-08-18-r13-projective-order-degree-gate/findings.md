---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/conjectured
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
direction: proof
cycle: 13
outcome: PARTIAL_RESULT
---

# Projective order-degree gate: exact transfer lemma and obstruction

## Active target

Scope: `20.115/nonzero-character-order-divisibility`

Assignment revision: `1`

Target: for every finite `G`, every ordinary irreducible complex character `chi`,
and every `x in G` with exact `chi(x)!=0`, prove
`o(x)chi(1) | |G|`.

## Outcome

`PARTIAL_RESULT`. The proposed universal projective assertion was neither proved
nor refuted. It is too strong to serve as an independently available bridge:
the trivial factor set is exactly the unresolved ordinary source assertion.
What is established here is the exact central-extension/order-lift transfer
lemma, its sharp full-cancellation criterion, and a sufficient conditional
least-counterexample package.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | result in this cycle |
|---|---|---|---|
| `20.115-forall-G-chi-x` | admissibility | every admissible triple | not established universally; projective lemma contains this case |
| `20.115-G-finite` | admissibility | finite `G` | retained in every stated transfer lemma |
| `20.115-chi-complex-irreducible` | admissibility | ordinary complex irreducible `chi` | retained for the source; projective characters used only through ordinary central-extension lifts |
| `20.115-x-in-G` | admissibility | `x in G`, exact `o(x)` | exact quotient and lift orders are distinguished throughout |
| `20.115-character-value-nonzero` | admissibility | exact `chi(x)!=0` | nonzero is transported exactly by multiplication by a root of unity |
| `20.115-order-degree-divisibility` | target conclusion | `o(x)chi(1)| |G|` | not proved; obtained only under the explicit conditional package below |

`active_assignment_answered: no`.

## Exact projective/central-extension dictionary

Normalize a finite-valued factor set `f:H x H -> mu_m` and a projective
representation by

`rho(g)rho(k)=f(g,k)rho(gk)`.

On

`E_f=mu_m x H`, `(z,g)(w,k)=(zw f(g,k),gk)`,

the map `rho_tilde(z,g)=z rho(g)` is an ordinary representation. It is
irreducible iff `rho` is projectively irreducible, and its character satisfies

`chi_tilde(z,g)=z alpha(g)`.

Consequently, the zero/nonzero status of `alpha(g)` is independent of the lift
and of a projective gauge change. Conversely, a central extension and an
irreducible ordinary character lying over a central scalar character recover a
factor set after choosing a section. Quotienting the central kernel by the
kernel of the scalar character produces the effective scalar kernel `Z`, which
is cyclic.

## Exact lift-order lemma

Let

`1 -> Z -> E -> H -> 1`

be such an effective extension, with `Z` cyclic of order `m`; let `lambda` be
the faithful scalar character of `Z`, and let `chi_tilde in Irr(E)` lie over it.
For `h in H`, put `n=o(h)`, choose a lift `y`, and set `c=y^n in Z`. Then, for
every `z in Z`,

1. `o(zy)=n o(z^n c)` exactly;
2. `chi_tilde(zy)=lambda(z)chi_tilde(y)`, so nonvanishing is lift-invariant.

If the ordinary source divisibility is known for the triple
`(E,chi_tilde,zy)`, and `r=o(z^n c)`, then the exact consequence is only

`n alpha(1) | (m/r)|H|`.

Thus the scalar factor cancels completely exactly when some lift has order
`nm`, equivalently some `z^n c` generates `Z`.

Primewise, such a lift exists iff for every prime `p | gcd(n,m)`, the
`p`-component of `c` generates the Sylow `p`-subgroup of `Z`. This is the sharp
full-order-lift criterion for this direct central-extension argument. In
particular `gcd(n,m)=1` is an easy sufficient hypothesis.

## Nonvanishing does not repair the lift order

Let

`E=D_8 x C_2=<r,s,c | r^4=s^2=c^2=1, srs=r^-1,
[c,r]=[c,s]=1>`

and `Z=<r^2>`. Use the standard irreducible degree-two representation of `D_8`
with `r^2` acting as `-I`, and let the external `c` act as `I`. Then
`H=E/Z=C_2^3`. For `h=cZ`, the projective trace is `alpha(h)=2`, but both lifts
of `h` have order two, not `o(h)|Z|=4`. Hence exact nonzero value does not imply
the full-order-lift criterion. The projective divisibility still holds here
(`2*2 | 8`), so this is an obstruction certificate, not a counterexample.

## Sufficient least-counterexample variant

Let `G` be least by order among source counterexamples, take `1!=N normal G`,
`H=G/N`, `h=xN`, and suppose a Clifford-theoretic step has independently proved:

1. `chi(1)=a alpha(1)` and `alpha(h)!=0`;
2. with `t=o(x)/o(h)`, one has `t a | |N|`;
3. `alpha` has an effective cyclic scalar extension `E` of `H`, with kernel
   `Z` satisfying `|Z|<|N|`;
4. the full-order-lift criterion holds at `h`.

Then `|E|=|Z||H|<|G|`, so minimality supplies the ordinary divisibility in `E`.
A lift of order `|Z|o(h)` cancels `|Z|` and gives
`o(h)alpha(1)| |H|`. Multiplication with `t a | |N|` gives
`o(x)chi(1)| |G|`, contradicting the choice of `G`.

This package is sufficient and exact for the direct route, but this clean cycle
does not establish that a general Clifford/Fitting reduction supplies conditions
2--4. They must not be assumed from homogeneity or from projective nonvanishing.

## What this does not establish

- It does not prove or refute the universal projective assertion.
- It does not prove the ordinary Kourovka target.
- It does not show that every relevant factor set has a full-order lift.
- It does not show that every scalar extension is smaller than a putative minimal
  counterexample.
- The fixed GAP sanity probes recorded in `log.md` are not premises and do not
  constitute catalogue coverage or universal evidence.

## Recommendation

Treat `PROJECTIVE-ORDER-DEGREE-GATE` as exhausted as a standalone universal
bridge. Ask MathExpert whether the intended least-counterexample setup can prove
the three concrete missing inputs: effective scalar-kernel size `<|N|`, the
full-order-lift criterion at `xN`, and the kernel factor
`(o(x)/o(xN))a | |N|`. Without all three, return to a different structural
representation rather than assuming the universal projective lemma.

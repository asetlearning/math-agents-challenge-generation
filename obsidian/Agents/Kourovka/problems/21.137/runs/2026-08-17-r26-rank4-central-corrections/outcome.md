---
title: "RANK4-NONSPLIT-H3-CENTRAL-CORRECTION-COHOMOLOGY — exact R0 near miss"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: counterexample
outcome: PARTIAL_RESULT
active_assignment_answered: no
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/group-extensions, project/kourovka, status/conjectured]
---

# Exact active source scope

Odd `p>2`; finite same-`p` group; exponent exactly `p^2`; literal actual set
`{g^p:g in G}`, never generated subgroup; literal set itself a subgroup; ask
whether it is abelian; `p=2`/exponent-eight sibling excluded.

# Outcome

The single leased central row `(R0)` constructs an exact order-`3^10`,
exponent-nine group with embedded prescribed kernel and quotient `H_3(3)`.
Its literal cube set is noncommuting but has 135 elements, so it is not a
subgroup. This is an exact `OUT_OF_SCOPE_EXAMPLE`, not a counterexample.

The same exclusion applies by a hand section-change argument to the 243
distinct central-relator rows in the central generator-lift gauge orbit of
`(R0)`. It does not exclude gauge-inequivalent feasible factor classes or the
unrestricted source scope. The unleased full affine-family ranks remain
quarantined.

# Separate leased gates

| gate | exact result | consequence |
|---|---|---|
| frozen hashes | manifest, checker, and imported-module hashes matched | authorized input used |
| invocation | exactly one command, exit code zero; no patch/rerun/alternate row | lease respected |
| fixed row | `000000000000002002` | only `t^2` on `[X,Z]` and `[Y,Z]` |
| normalized factor | digest `a74a5d9b959366b0b8913fabd7cc7e7af1a4e3605df09c3d95d2f3a00492f824`; fixed-row rank/dimension `1959/69` | one exact normalized factor exists for `(R0)` |
| noncentral associativity | 729 pair defects, 19,683 vector identities, 78,732 scalar coordinates | every `V` residual is zero |
| central associativity | 19,683 vector identities, 59,049 scalar coordinates | crossed-product multiplication is associative |
| corrected relators | all six pass | exact proposed pc row realized |
| normal form/order | 59,049 unique ten-coordinate forms | finite `3`-group of order `3^10` |
| kernel | coordinate slice order 2,187 | prescribed `K=3_+^(1+4) x C3^2` embeds |
| quotient | coordinate projection order 27 | quotient is the frozen `H_3(3)` |
| exponent | all 59,049 ninth powers are one; `(0,0,0,0,0,0,0,0,1,0)` has nontrivial cube | exponent exactly nine |
| literal cube image | cube of every one of the 59,049 elements evaluated; 135 distinct values | literal set used, not generated subgroup |
| subgroup closure | generated closure has 729 elements and contains `(2,1,0,2,2,0,1,0,0,0)` outside the literal image | literal cube set is not a subgroup |
| noncommutativity | `X^3=f2`, `Y^3=e2`, and `[f2,e2]=c^2 != 1` | two actual cubes do not commute; the checker's printed `None` merely records that its conditional search was skipped after closure failed |

The cardinality `135=3^3*5` alone also rules out subgroup status by Lagrange,
while the 729-element generated closure supplies an independent exact
comparison.

# Hand exclusion of the whole central lift-gauge orbit

Let the quotient lifts change to

`X'=aX`, `Y'=bY`, `Z'=dZ`

with `a,b,d in Z(K)=<c,s,t>`, written additively in `(c,s,t)` coordinates.
These changes preserve all frozen automorphism triples and all six noncentral
relator representatives. Direct collection in the center module gives the
following increments:

```
Delta(X^3) = (2 a_t,0,0)
Delta(Y^3) = (b_t,0,0)
Delta(Z^3) = (0,0,0)

Delta([X,Y]Z^-1)
  = (2a_s+2b_s+2d_c, 2a_t+b_t+2d_s, 2d_t)
Delta([X,Z])
  = (2a_t+2d_s+d_t, d_t, 0)
Delta([Y,Z])
  = (2b_t+d_s+2d_t, d_t, 0).
```

For the power rows, this follows from
`I+T+T^2=(T-I)^2` in characteristic three. For the commutator rows, use the
semidirect center law `(u,T)(v,U)=(u+Tv,TU)` and
`(u,T)^-1=(-T^-1u,T^-1)` in the six words.

The nine-to-18 increment map has rank five by hand: `a_c,b_c` vanish;
`a_s,b_s,d_c` have the same column; and the five columns represented by
`a_s,a_t,b_t,d_s,d_t` are independent, successively witnessed in rows
`xy_c,x3_c,y3_c,xz_c,xy_t`. Hence `(R0)` has exactly `3^5=243` distinct
central-relator rows in its generator-lift orbit.

Changing section does not change the abstract group. More explicitly, for a
normalized central section change `s'(q)=h(q)s(q)` and
`f'=f+delta h`, the coordinate map

`(k,q)_f -> (k-h(q),q)_(f')`

is an isomorphism, identity on the kernel and quotient. It carries actual
cubes to actual cubes. Therefore every one of those 243 rows has the same
135-element nonclosed literal cube image up to isomorphism and is excluded.

# Constraint-and-conclusion matrix

| constraint_id | role | candidate value / evidence | result |
|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | one `p=3` object could refute the universal assertion only if every other row passed | not reached as a counterexample |
| `21.137-odd-p-not-2` | admissibility | `p=3` | pass |
| `21.137-odd-finite-p-group` | admissibility | exact coordinate group of order `3^10` | pass |
| `21.137-odd-exponent-p2` | admissibility | exact exponent `9=3^2` | pass |
| `21.137-odd-power-set-definition` | admissibility | all 59,049 literal cubes evaluated; image size 135 | pass |
| `21.137-odd-power-set-subgroup` | admissibility | 135 is not a power of three; generated closure size 729 | **fail** |
| `21.137-odd-P-abelian` | target conclusion | actual cubes `X^3=f2`, `Y^3=e2` have commutator `c^2` | violated, but irrelevant because the hypothesis fails |

Thus `active_assignment_answered: no`.

# Exact boundary

Established: one exact factor class and all 243 presentation rows in its
central generator-lift orbit fail literal cube closure despite retaining two
noncommuting actual cubes.

Not established: the quarantined eight-dimensional affine-family claim, any
gauge-inequivalent central factor class, any alternate shear/action, any other
kernel or quotient, any odd prime other than three, or the universal source
answer.

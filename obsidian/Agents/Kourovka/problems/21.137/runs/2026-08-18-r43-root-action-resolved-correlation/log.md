---
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: proof
cycle: 31
strategy: ROOT-ACTION-RESOLVED-CORRELATION
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - project/kourovka
  - status/draft
---

# Cycle 31 log: actual-root action-resolved correlation

## 2026-08-18T10:20:52Z — work start

- Official cumulative start: minute `897`.
- Current increment: at most `45` newly elapsed active minutes; wall-clock safety
  stop `2026-08-18T11:16:08Z`.
- Exact scope: for every odd prime `p` and finite same-`p` group `G` of exponent
  exactly `p^2`, if the literal value set `P={g^p:g in G}` is itself a subgroup,
  prove that `P` is abelian. The general powerfulness clause and the separate
  `p=2`, exponent-eight clause are excluded.
- First lane is explicitly only the `p=3` subfamily. Its primitive data retain,
  for every actual root `x`, the triple consisting of `x^3`, the actual induced
  action `conj_x|P`, and its pair correlation with roots `y` and `(xy)^3`.

## Source and scope gate

I sourced the configured PDF path, rendered page 184, and visually inspected the
statement. It asks: if the `p`-th powers in a finite `p`-group form a subgroup,
must it be powerful; equivalently in the odd-prime exponent-`p^2` clause, must
that subgroup be abelian; and separately asks the exponent-eight `2`-group
question. `source_transcription_checked: yes`. The middle clause is the entire
active scope and agrees with all seven canonical rows. `active_scope_checked:
yes`. Discovery-blind mode remains in force, so open-web staleness work is
deferred: `external_staleness_check:
deferred_to_lead_or_human_for_discovery_blind_run`.

| source clause | active? | treatment |
|---|---:|---|
| general actual-power subgroup is powerful | no | excluded |
| odd `p`, exponent exactly `p^2`, literal powers a subgroup implies abelian | yes | entire assignment |
| `p=2`, exponent 8, squares a subgroup implies abelian | no | excluded |

No catalogue or heavy computation is authorized in this proof lane. A formal
action array would test only the method. A target proof would need a
choice-independent identity for complete actual root fibres and then a
prime-uniform bridge to `[P,P]=1`; Validator could reconstruct the group-theoretic
bijections and central-character calculation directly.

## Independent reduction used only to test the first `p=3` lane

Assume that a counterexample of least order exists at an odd prime. The literal
power set `P` is characteristic and every one of its elements has order dividing
`p`. Since `P` is nonabelian, `P'` is a nontrivial normal subgroup of `G`; choose
`N<=P' cap Z(G)` of order `p`. In `G/N`, the literal power set is exactly `P/N`
and remains a subgroup. It is nontrivial (otherwise `P<=N` would be abelian), so
the quotient still has exponent exactly `p^2`. Minimality makes `P/N` abelian,
whence `P'=N=C_p<=Z(G)`. Thus in the first `p=3` test one may write
`Z=P'=<z>=C_3`, `V=P/Z`, and

`[u,v]=z^beta(ubar,vbar)`

for an alternating bilinear form `beta` on the elementary abelian group `V`.
This reduction was rederived here and is not a universal conclusion.

## Choice-independent action-resolved identities

Use right conjugation `u^g=g^-1 u g`, and let `theta_x` be the actual
automorphism `u |-> u^x` of `P`. For every value `a` and every action `alpha`,
define the complete count

`F^X_(a,alpha)(b,c)=#{(x,y):x^3=a, theta_x=alpha, y^3=b, (xy)^3=c}`.

There is no selected root in this definition. The bijection

`(x,y) |-> (x,y^x)`

has `x y^x=yx=(xy)^x`, and therefore gives the exact identity

`F^X_(a,alpha)(b,c)=F^X_(a,alpha)(b^alpha,c^alpha)`.       `(AX)`

Similarly, resolving the action `beta=theta_y` and the product-root action
`gamma=theta_(xy)` gives, from `(x,y)->(x^y,y)` and simultaneous conjugation
by `xy`,

`F^Y_(b,beta)(a,c)=F^Y_(b,beta)(a^beta,c^beta)`,          `(AY)`

`F^W_(c,gamma)(a,b)=F^W_(c,gamma)(a^gamma,b^gamma)`.      `(AW)`

These are strictly finer than the aggregate kernel: if `K(a,b,c)` is the count
with all actions forgotten, then `K=sum_alpha F^X=sum_beta F^Y=sum_gamma F^W`.
After summing `(AX)`, for example, the exact choice-independent row is

`K(a,b,c)=sum_alpha F^X_(a,alpha)(b^alpha,c^alpha)`.       `(SAX)`

The right side cannot be replaced by one value of `K`: different actual roots
over the same `a` can have different `alpha`, and hence send `(b,c)` to different
quotient pairs. This is precisely the information retained by the complete
multiset and then lost by its aggregate.

The support also obeys the exact, central-blind equations

`alpha^3=theta_a`, `beta^3=theta_b`, `(beta o alpha)^3=theta_c`,

and the corresponding action fixes its own power value. Multiplying any of
`a,b,c` by `z` does not change these equations because `z<=Z(G)`.

## 2026-08-18T10:33:24Z — early Fourier gate

Fix quotient values `A,B,C in V` and put

`delta=beta(A,B)`, `epsilon=beta(B,C)`, `zeta=beta(C,A)`.

For an `x`-action `alpha`, its quotient action `T` has `T^3=1` and fixes `A`.
Three applications of `(AX)` are conjugation by `x^3=a`, so on the central
coordinates `(i,j,k)` of `(a,b,c)` the monodromy translation is

`t_X=(0,-delta,zeta)`.

The symmetric monodromies from `(AY)` and `(AW)` are

`t_Y=(delta,0,-epsilon)` and `t_W=(-zeta,epsilon,0)`.

Thus the three old aggregate Fourier conditions are exactly the cubes of the
new action transports. The surviving skew frequency

`w=(epsilon,zeta,delta)`

has `w.t_X=w.t_Y=w.t_W=0`. In particular, for `delta!=0` and
`C=A+B` (or the same noncentral cosets with an added radical coordinate), one
has `epsilon=zeta=-delta`. The quotient action `T` cannot fix `B`: otherwise
`alpha(b)=bz^q` and, since `alpha` fixes `z`, `alpha^3(b)=b`, contradicting
`alpha^3(b)=b^a=bz^(-delta)`. Hence `(AX)` transports the skew amplitude around
a genuine three-cycle of quotient blocks. Its third-step phase is one, so an
arbitrary initial amplitude survives. The same argument applies to `Y` and
`xy`.

This meets the requested action-resolution test but fails the requested
constraint gate: the finer identities act on the skew block only by transporting
it among action-dependent quotient blocks. Summing the complete actual action
multiset has no common `T` to factor out, and the only common third iterate is
the already-known central translation, on which `w` is trivial.

## Exact local compatibility check (method test only)

To check that the support equations themselves do not exclude the nonorthogonal
skew configuration, I independently built the following exact local datum over
`F_3`. Let `P=H_3(3) x C_3^2`; write `V=P/P'` with basis
`A,B,r1,r2`, `beta(A,B)=1`, and radical `<r1,r2>`. Define quotient actions

- `T(B)=B+r1`, `T(r1)=r1+r2`, fixing the other basis vectors;
- `S(A)=A-r1`, `S(r1)=r1+r2`, fixing the other basis vectors.

With central shears `lambda=(0,0,0,2)` and `mu=(0,0,2,2)`, the automorphisms
`alpha=(T,lambda)` and `beta=(S,mu)` fix `a=A` and `b=B`, and have cubes equal
to conjugation by those values. Their product action fixes
`c=A+B+r1`, has cube conjugation by `c`, and the three pairings are
`(delta,epsilon,zeta)=(1,2,2)`. All three action transports have genuine
three-cycles and skew monodromy zero.

This is a locally compatible action triple, **not an ambient group, not a cube
map, and not a counterexample**. It shows only that the exact action support and
fixed-value gates do not remove the skew line before extension/factor-system
coherence, which this strategy was forbidden to reopen.

Observed command:

`python3 Agents/Kourovka/problems/21.137/runs/2026-08-18-r43-root-action-resolved-correlation/scratch/check_local_action_triple.py`

Observed output:

```text
formal_object=local_actions_on_H3(3)xC3^2_not_an_ambient_group
alpha_beta_product_cube_labels=A,B,C
pairings_delta_epsilon_zeta=1,2,2
root_values_fixed_by_respective_actions=pass
linear_parts_and_product_have_order_three=pass
cube_actions_equal_inner_A_inner_B_inner_C=pass
three_action_monodromy_pairings=0,0,0
nontrivial_quotient_orbits_for_X_Y_XY=pass
```

Checker SHA-256:
`50e501552d7d5114096ffbe923ab7a1e0855d0666420237faf81cedd87f5b430`.

## 2026-08-18T10:34:53Z — work stop and cycle outcome

- Newly elapsed active time: 14 minutes 1 second; conservatively charged `15`
  active minutes.
- Official cumulative stop: minute `912` (`897+15`), within both the
  45-minute grant and the wall-clock safety stop.
- Outcome: `STRATEGY_EXHAUSTED` for
  `ROOT-ACTION-RESOLVED-CORRELATION` alone.
- Hard kill: the exact complete-action identities `(AX)--(AW)` lift the three
  old central translations to action-dependent `p`-cycles, but the surviving
  skew frequency has trivial monodromy on every cycle. Summing all actual
  actions cannot align their different quotient transports and returns only the
  old aggregate identity.
- Strongest partial: the prime-uniform complete-action identities and
  monodromy obstruction, plus one exact `p=3` locally compatible nonorthogonal
  action triple. The latter is not an ambient group or counterexample.
- Scope status: `active_assignment_answered: no`; neither the universal target
  nor the complete `p=3` subfamily is answered.
- Representation-changing alternative: a global extension-realizability
  obstruction for the local triple. It is outside this lane and overlaps the
  explicitly excluded simultaneous extension/factor-coherence representation,
  so research stops in `awaiting_lead` rather than reopening it.

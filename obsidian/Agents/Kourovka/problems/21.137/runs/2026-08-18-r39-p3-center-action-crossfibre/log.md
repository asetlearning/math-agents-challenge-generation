---
title: "Problem 21.137 cycle 27 — p=3 center-action cross-fibre log"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: proof
cycle: 27
strategy: P3-CENTER-ACTION-CROSSFIBRE
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/draft]
---

## Active-time ledger

- `2026-08-18T06:05:50Z`: active start at official cumulative minute `806`.
- Research is discovery-blind and confined to the complete `p=3` subfamily. No
  web search, historical problem log, historical findings, archived message, or
  preceding unreviewed derivation was used as a premise.

## Source and scope gate

At `2026-08-18T06:10Z` I read and visually inspected the rendered Notebook No. 21
PDF, p. 184. The source statement is:

> 21.137. If the p-th powers in a finite p-group form a subgroup, must that
> subgroup be powerful? That is, for p not equal to 2, if the p-th powers in a
> p-group of exponent p-squared form a subgroup, must that subgroup be abelian?
> For a 2-group of exponent 8, if the squares form a subgroup, must that subgroup
> be abelian?

The item is unstarred and has no attached editor or later comment. The configured
issue is the 2026 issue. The active scope is only the middle clause.

- `source_transcription_checked: yes`
- `active_scope_checked: yes`
- `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`

Clause matrix:

| source clause | equivalent formulation | active? |
|---|---|---:|
| general powerfulness question | actual power-value set a subgroup implies powerful | no |
| odd-prime exponent-p-squared clause | for every odd p, exact exponent p-squared and literal power-set subgroup imply that subgroup abelian | yes |
| exponent-eight 2-group clause | literal square-set subgroup implies abelian | no |

Canonical constraint audit for this run:

| constraint_id | use/result |
|---|---|
| `21.137-odd-forall-p-G` | The source target is universal in odd `p`; this lane treats only `p=3`, hence can at most be a partial unless a prime-uniform bridge is added. |
| `21.137-odd-p-not-2` | `p=3`, so prime, odd, and not 2. |
| `21.137-odd-finite-p-group` | The hypothetical least counterexample below is a finite 3-group. |
| `21.137-odd-exponent-p2` | Its exponent is exactly 9. |
| `21.137-odd-power-set-definition` | `P` always denotes the literal set `{g^3:g in G}`, never merely its generated subgroup. |
| `21.137-odd-power-set-subgroup` | The literal set `P` is assumed to be a subgroup. |
| `21.137-odd-P-abelian` | The contradiction target is `P'=1`; assume `P'!=1`. |

The `p=2`, exponent-eight sibling and the broader powerfulness question are
excluded throughout.

## Strategy portfolio and selected gate

1. Catalogue mode is not used: the assignment asks for an exact proof-observable,
   and a bounded catalogue cannot decide the universal target.
2. Structured mode: write the central extension by the least-counterexample
   layer `W=P'` using a normalized factor set, and model the three complete root
   fibres as torsors over `W`.
3. Theoretical mode (selected): derive the exact block-cube and cross-fibre
   identities and audit every section, root, and central-lift change. Test whether
   their gauge quotient kills a nonzero center-action square.
4. Certificate: a line-by-line derivation plus an explicit normalized cocycle and
   root-torsor datum with nonzero `s^2 f`. The datum is deliberately only a method
   obstruction, not a source witness.

Kill criterion: if complete literal fibres make the cross equation automatically
solvable for an arbitrary skew factor-set value, stop this strategy and do not
promote the formal datum to a group counterexample.

## Independent least-counterexample reduction

Assume a counterexample `G` of least order in the complete source-admissible
`p=3` subfamily. Every element of `P` is a literal cube, so it has order dividing
3. Thus `P` has exponent 3 and is nonabelian.

For every nontrivial normal subgroup `N` of `G`, the literal cube set of `G/N` is

`{(gN)^3:g in G}=PN/N`.

It is a subgroup because `P` is. If `P'` were not contained in `N`, then `PN/N`
would be nonabelian. It would in particular contain a nontrivial cube, so the
exponent of `G/N` (which divides 9) would be exactly 9. That would be a smaller
counterexample. Hence `P'<=N` for every nontrivial normal `N`.

Choose a minimal normal subgroup `N`. In a finite 3-group it is central of order
3. Since `P'!=1`, necessarily

`W:=P'=N`, so `|W|=3` and `W<=Z(G)`.

In particular `W` is contained in every nontrivial normal subgroup of `G`.

Let `Z=Z(P)`, written additively over `F_3`. It is a normal elementary abelian
subgroup, and conjugation on it factors through `H=G/P`, an exponent-three
3-group. If `I` is the augmentation ideal of `F_3 H`, take maximal `m` with
`Z I^m != 0`. Then `Z I^m` is fixed by `H` and hence central in `G`. Every
one-dimensional subspace of it is normal in `G`; uniqueness of the minimal normal
subgroup forces

`Z I^m=W`.

This independently identifies the last nonzero center-augmentation layer used by
the assigned gate.

## Exact block-cube identity

Take `x in G`, put `a=x^3 in P`, and let `f in Z(P)`. Use right conjugation
`alpha(f)=f^x` and set `s=alpha-1`. Direct collection gives

`(x f)^3 = x^3 f^(x^2) f^x f`.

The three conjugates of `f` commute. Moreover `alpha^3(f)=f^(x^3)=f^a=f`, since
`f` centralizes `P`. Therefore, in the additive `F_3`-module `Z(P)`,

`(x f)^3 = x^3 + (1+alpha+alpha^2)f = x^3+s^2 f`.       `(B)`

Here `1+alpha+alpha^2=(alpha-1)^2` in characteristic 3. If `s^2 f=w!=0` lies in
the last layer `W`, then the three roots `x f^i` have cubes `a+i w`. Modulo `W`
they are roots of the same value. Changes `x -> x w_0` and `f -> f+w_0` with
`w_0 in W` do not change `(B)`, because `W` is central, has exponent 3, and
`sW=0`.

## Central-extension coordinates

Put `Q=G/W`, `V=P/W`, and write `W=F_3 w` additively. Choose a normalized section
`sigma:Q->G` and a normalized factor set `c:Q x Q->F_3` by

`sigma(q)sigma(r)=sigma(qr) w^{c(q,r)}`.

Associativity is exactly

`c(q,r)+c(qr,u)=c(r,u)+c(q,ru)`.                         `(F0)`

Define the cube coordinate

`theta(q)=c(q,q)+c(q^2,q)`,

so that

`sigma(q)^3=sigma(q^3)w^{theta(q)}`.                     `(F1)`

For `v in V`, every lift of `v` lies in `P` and has order 3, hence `theta(v)=0`.
For each `v in V`, let

`R_v={q in Q:q^3=v}`.

Because every element `sigma(v)w^e` of `P` is, literally, a cube, `(F1)` implies
the complete-fibre equality

`theta(R_v)=F_3` for every `v in V`.                      `(F2)`

This is equality, not merely nonemptiness.

## Exact cross-fibre equation over a, b, and ab

Take `q in R_A` and `r in R_B`. Their lifted cubes multiply as

`sigma(q)^3 sigma(r)^3`
` = sigma(AB) w^{theta(q)+theta(r)+c(A,B)}`.

Since the literal cube set is a subgroup, there is a root `t in R_(AB)` of that
specific product. Equivalently,

`theta(t)=theta(q)+theta(r)+c(A,B)`.                      `(X)`

Conversely, `(X)` for all `q,r` is exactly the multiplicative-closure row in these
coordinates. For the reverse product, the corresponding coordinate is
`theta(r)+theta(q)+c(B,A)`, and the difference is

`c(A,B)-c(B,A)`, the `W`-coordinate of the commutator of the two value lifts.

The crucial point is that `(F2)` makes `(X)` automatically solvable for every
right-hand side and for every value of `c(A,B)`. Thus `(X)` imposes no condition
on its skew part.

In particular, if `q_1=q f` is the block change in `(B)` and
`theta(q_1)-theta(q)=s^2 f=w`, then for fixed `r` choose closure roots `t_0,t_1`
for `(q,r)` and `(q_1,r)`. Subtracting the two exact equations gives

`theta(t_1)-theta(t_0)=w`,                                `(Xdiff)`

not `w=0`. Complete target fibre `R_(AB)` supplies precisely such a pair. Nothing
in literal closure identifies `t_1` with `t_0`, or with `t_0 f`; either
identification would be an extra, unjustified equivariant-root-section premise.

## Complete covariance audit

1. **Section change.** For arbitrary normalized `d:Q->F_3`, set
   `sigma_d(q)=sigma(q)w^{d(q)}`. Then

   `c_d(q,r)=c(q,r)+d(q)+d(r)-d(qr)`,

   `theta_d(q)=theta(q)-d(q^3)`.

   Both sides of `(X)` change by `-d(AB)`, so `(X)` and `(Xdiff)` are section
   invariant.

2. **Root change.** Replacing `q,r` by arbitrary roots `q',r'` in the same two
   fibres changes the desired target coordinate by
   `[theta(q')-theta(q)]+[theta(r')-theta(r)]`. By `(F2)` a target root with that
   change always exists. There is no canonical root whose coordinate must remain
   fixed.

3. **Lift change.** Replacing any lift `sigma(q)` by `sigma(q)w^e` does not alter
   its cube, because `w` is central of order 3. This is already encoded by the
   section formula. Replacing the center lift `f` by `f+w^e` does not alter
   `s^2f` because `sW=0`.

4. **Value-section change.** This is the restriction of the arbitrary function
   `d` to `V`; the cancellations in item 1 include the changes of the chosen
   representatives of `A`, `B`, and `AB`.

No residual remains after these permitted changes.

## Explicit gauge/factor-set obstruction datum

Let `V=F_3^2`, `W=F_3`, and define the normalized bilinear cocycle

`c((i,j),(k,l))=i l`.

The group `P_c=V x W` with law

`(v,e)(v',e')=(v+v', e+e'+c(v,v'))`

has exponent 3. Bilinearity gives `(F0)`. For `A=(1,0)` and `B=(0,1)`,
`c(A,B)-c(B,A)=1`, so the value subgroup encoded by this factor set is
nonabelian. Write `a=(A,0)`, `b=(B,0)`, and `w=(0,1)` in this extension, so
`[a,b]=w`.

For every `v` introduce a formal complete root torsor `R_v=F_3` with
`theta_v(i)=i`. Define the selected product root by

`mu_(v,v')(i,j)=i+j+c(v,v') in R_(v+v')`.

This satisfies `(F2)`, `(X)`, inversion, the identity row, and associativity
because `c` satisfies `(F0)`. In particular

`mu_(A,B)(i,j)=i+j+1`, whereas `mu_(B,A)(j,i)=i+j`;

their nonzero difference is absorbed by the complete target fibre.

For the center-action block take the genuine `F_3[C_3]`-module

`Z_0=<f,g,w>`, with `s f=g`, `s g=w`, and `s w=0`.

Then `(1+s)^3=1`, the last nonzero augmentation layer is `Z_0 s^2=<w>`, and
`s^2 f=w!=0`. Label the formal roots `q f^i in R_A` by
`theta_A(q f^i)=theta_A(q)+i`; this is exactly `(B)`.

For an arbitrary value-section gauge `d:V->F_3`, replace

`c` by `c_d(v,v')=c(v,v')+d(v)+d(v')-d(v+v')`

and replace every fibre coordinate by `theta_v^d(i)=i-d(v)`. The same formula
for `mu` then verifies `(X)` identically. Arbitrary root shifts and central-lift
changes act as in the covariance audit above. Thus this datum realizes a nonzero
`s^2f` and nonzero skew factor while satisfying every identity derived in this
lane.

The center block is also compatible with the exact cyclic-lift relation, not only
with an abstract module. Enlarge `P_c` by central generators `e_0,e_1` of order 3
and define the triangular automorphism

`phi(a)=a`, `phi(b)=b e_0`, `phi(e_0)=e_0 e_1`,
`phi(e_1)=e_1 w^(-1)`, `phi(w)=w`.

It preserves `[a,b]=w` and direct calculation gives
`phi^3=Inn(a)` (in particular `phi^3(b)=b w^(-1)`). Hence the single cyclic block
with relations `p^x=phi(p)` and `x^3=a` is consistent. On its center, for
`s=phi-1` and `f=-e_0`, one has `s^2f=w`, so `(x f)^3=a w`. This checks the
otherwise delicate relation between a root action and its cube value. It realizes
one cyclic block only; it does not bind independent roots above `A`, `B`, and
`A+B` into one global group.

This is deliberately a **formal local root/factor-set datum**, not a finite group:
it does not supply a global quotient `Q`, simultaneous root actions, exact exponent
9 for a resulting `G`, or proof that the complete global cube set equals `P_c`.
It is therefore a method obstruction only and is not a source counterexample.

## Exact finite audit of the formal datum

Artifact:
`Agents/Kourovka/problems/21.137/runs/2026-08-18-r39-p3-center-action-crossfibre/scratch/check_torsor_model.py`.
SHA-256:
`94ae3e3eebaa9a0393ec1f93ee44c961dfcba1c345493604e0bfd9cb52105d96`.

Command actually run:

```text
python3 Agents/Kourovka/problems/21.137/runs/2026-08-18-r39-p3-center-action-crossfibre/scratch/check_torsor_model.py
```

Observed output:

```text
cocycle_triples 729
group_elements_exponent3 27
root_associativity_rows 19683
normalized_gauges 6561
commutator_AB 1
s2f (0, 0, 1)
status PASS
```

The audit exhausts the finite cocycle, exponent-three value group, root-product
associativity, and all `3^8=6561` normalized value-section gauges in this formal
datum. It does not test or assert existence of a global source-admissible `G`.

## Decision

The named cross-fibre cocycle strategy meets its kill criterion. Complete literal
fibres do not force the center-action-square component to vanish; they make the
target fibre a full `W`-torsor which transports that component. Consequently this
lane cannot carry `s^2 f=0` to `[a,b]=1`.

Recommended representation-changing continuation: require a genuinely global
simultaneous compatibility of the cyclic root actions (for example the full
`Aut(P)`/inner relation `alpha_x^3=Inn(x^3)` together with quotient relations for
several root blocks). Another existential choice of a root in `R_(AB)`, another
factor-set gauge, or another fibre count cannot distinguish the obstruction datum.

## Active stop

- `2026-08-18T06:24:40Z`: active stop after `18` completed new active minutes;
  official cumulative minute `824` (`806+18`). The named method hit its exact kill
  criterion and the lane is `awaiting_lead`; `27` authorized minutes are returned
  unused.
- Outcome: `STRATEGY_EXHAUSTED` for
  `P3-CENTER-ACTION-CROSSFIBRE` only. `active_assignment_answered: false`.

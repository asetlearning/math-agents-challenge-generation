---
title: "MathExpert post-CPTR review — fibre-pairing audit and scheduling stop"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: POST-CPTR-FIBRE-PAIRING-AUDIT
direction: none
outcome: PARK_RECOMMENDED
active_assignment_answered: no
author: operator
tags:
  - agent/math-expert
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/group-extensions
  - project/kourovka
  - status/conjectured
---

# MathExpert post-CPTR review

## Scope and evidence boundary

`SCOPE: 21.137/odd-prime-exponent-p2`  
`REVISION: 2`  
`ACTIVE ASSIGNMENT ANSWERED: no`

The target is the universal assertion for every odd prime `p` and every finite
same-`p` group `G` of exponent exactly `p^2`: if the complete actual value set
`P={g^p:g in G}` is itself a subgroup, then `P` is abelian. The general
powerfulness clause, the `p=2` exponent-8 clause, generated-power subgroups, and
groups of any other exponent are excluded.

This review uses only the revision-2 scope record, the CPTR findings, the fresh
Validator reconstruction, the preceding portfolio-reset note, and Lead's
route-balance correction. No web, solution-bearing history, quarantined or
wreath material, sibling scope, delegate, or experiment was used.

**Novelty assessment:** `uncertain` externally, because the blind-run instruction
forbids a literature search. Within the curated program record, `(E6)` and
`(E8)--(E9)` sharpen the diagnosis of the failed mixed-cycle mechanism, but they
do not supply a new target-level consequence.

The algebraic deductions newly displayed below are **general mathematical
knowledge, unverified**; they are included with their complete two-line
derivations so that Validator can reconstruct them if they are ever relied on.

## Mathematical meaning of `(E6)`

Write `M_t=D_t^(p-2)` and `N_t=D_t^(p-1)`. The reviewed rows give

`D_j c_h=N_h q` and `ell_j(N_j a)=beta(a,c_j)`.

Consequently

`ell_j(M_j N_h q)=ell_j(M_j D_j c_h)`

`                         =ell_j(N_j c_h)=beta(c_h,c_j)`.

Thus the first equality in `(E6)` is `(E5)` evaluated at `a=c_h`, after `(E3)`;
the swapped equality has the same status. My assessment is that `(E6)` is an
exact covariance/consistency identity, not an independent restriction on
`beta(c_h,c_j)`. In particular it contains no latent zero that the mixed-cycle
coboundary evaluation could expose.

This explains the relation to `(E0)`: `(E0)` is a choice-free zero because it is
the evaluation of a coboundary on a cycle, whereas `(E6)` is the coordinate form
of an action-power identity whose scalar may be nonzero. Identifying the two
would require an additional term, not a different rearrangement of the same
rows.

## Mathematical meaning of `(E8)--(E9)`

For every quotient index `t`, define the vector-coordinate support of actual
`p`th powers from that coset by

`F_t=c_t+N_t A`.

A normalized section change sends `c_t` to `c_t+N_t eta_t`, so it changes the
chosen basepoint but leaves `F_t` unchanged. Therefore the section sensitivity
in `(E8)` is not accidental gauge noise: it records the genuine variation of
the commutator pairing as the two basepoints move through their intrinsic power
fibres.

Indeed `(E3')` gives `D_h c_j=-N_j q`, and hence

`M_h N_j q=-N_h c_j`.

The one-sided correction `(E9)` becomes

`-beta(eta_h,M_h N_j q)=beta(eta_h,N_h c_j)`

`                         =beta(N_h eta_h,c_j)`,

using self-adjointness of `N_h`. This is exactly the first linear variation in
`(E8)`. Thus the proposed radical condition is equivalent to saying that
`c_j` is orthogonal to every direction of the fibre `F_h`; it is a missing
orthogonality lemma, not something already hidden in `(E6)`.

Even that radical condition would only make the basepoint value constant along
one fibre. A separate identity would still be needed to make the constant zero.

## Exact actual-value-cover audit

The canonical section-free object attached to two indices is not the basepoint
scalar but the full pairing set

`B_(h,j)={beta(x,y): x in F_h, y in F_j}`.

Expanding `x=c_h+u`, `y=c_j+v`, with `u in N_hA` and `v in N_jA`, shows that
`B_(h,j)` is controlled by

`beta(N_hA,c_j)`, `beta(c_h,N_jA)`, and `beta(N_hA,N_jA)`.

Because the codomain is the one-dimensional field `F_p`, if any of these three
pairings is nonzero, varying one argument makes `B_(h,j)=F_p`. If all three
vanish, then `B_(h,j)={beta(c_h,c_j)}`. This dichotomy is section-independent
and makes `(E8)` transparent.

The exact cover `A=union_t F_t` turns the target `beta=0` into the requirement

`B_(h,j)={0}` for every pair of indices `h,j`.

It does not itself impose that requirement. A nonzero variation in `(E8)` merely
means that two actual powers in the two fibres have a nontrivial commutator—the
phenomenon a hypothetical counterexample is supposed to have. Set coverage does
not make that a contradiction.

The quotient statement is weaker for the same reason. The cover makes
`kappa(t)=c_t+[A,H]` surjective onto `A/[A,H]`, but `beta` can be evaluated there
only after the new containment `[A,H] <= rad(beta)`. Moreover, CPTR applies only
to commuting `h,j`; pointwise surjectivity does not say that two arbitrary
covered vectors admit indices that commute. The missing bridge therefore has
three independent parts:

1. orthogonality to fibre directions (or descent through `[A,H]`);
2. zero of the surviving basepoint scalar, not merely its constancy;
3. a commuting-index incidence statement reaching every pair of covered values.

Neither the reviewed actual-value cover nor `(E0)` and `(E3)--(E9)` supplies any
of these three parts. The fibre-pairing formulation is an audit lens, not a new
research phase: pursuing it symbolically would relabel the already exhausted
affine-cover/root-fibre line.

## What CPTR does and does not rule out

My assessment agrees with the narrow operational scope of the Validator report.
The certificate rules out this mixed 3-cycle as a direct detector of the desired
pairing: its `(C4)` value is forced to zero for formal coboundary reasons, while
ordered `(C5)` leaves the covariant carry scalar above. It does **not** rule out a
different, genuinely global obstruction built from the complete simultaneous
factor system. Such an obstruction would have to cancel all fibre-basepoint
variations and also solve the commuting-incidence gap. No such bounded
observable is present in the allowed evidence.

## Direction audit under Lead's correction

### Counterexample direction (default tie-break applied)

The most target-facing use of `(E9)` would be as a diagnostic: a realizable
compatible extension with `M_hN_jq` outside the radical would immediately expose
nonzero pairings between actual-power fibres. But the formulas do not construct
such an extension. Before enumeration, a counterexample phase would still need a
new associative finite presentation or complete factor-system family, an exact
object/row count, exponent-`p^2` checks, and equality with the entire actual
power set. The curated record contains no structurally new non-wreath, non-UT7,
non-NS3-repair object satisfying those gates. Designing that object is the same
unbounded compatibility problem, so it cannot honestly be assigned a 33-minute
certificate deadline.

### Proof direction

A proof phase would need a choice-free identity forcing all three parts of the
cover bridge above. The only available candidates are the exhausted `(C4)`
cycle, affine cover, Hall-span, and root-fibre mechanisms, or the unfrozen global
obstruction class already rejected by the portfolio reset. CPTR adds no stronger
observable that could dominate the human-directed counterexample tie-break.

## Sole scheduling recommendation

`PARK_RECOMMENDED`.

The 33 already-granted minutes should remain unspent. This is a scheduling stop,
not a claim about the truth of the target and not a retirement of revision 2.
The counterexample direction received the required default preference, but no
mechanically frozen new family meets the evidence gate; the proof direction has
no substantially stronger new mechanism.

Retain the truth-likelihood estimate `0.52`. CPTR is evidence about one method's
reach, not evidence favoring either truth value.

## Clause and constraint matrix

| item | assessment |
|---|---|
| `c-general` | excluded and unanswered |
| `c-odd` | active; unanswered |
| `c-two` | excluded and unanswered |
| `21.137-odd-forall-p-G` | no universal conclusion obtained |
| `21.137-odd-p-not-2` | retained in the conditional algebra |
| `21.137-odd-finite-p-group` | no concrete witness; conditional setup only |
| `21.137-odd-exponent-p2` | no concrete witness; conditional setup only |
| `21.137-odd-power-set-definition` | actual-value fibres used; no generated-subgroup substitution |
| `21.137-odd-power-set-subgroup` | used only through the complete affine union cover |
| `21.137-odd-P-abelian` | unresolved; neither `beta=0` nor an admissible `beta != 0` witness obtained |

## Confidence and unpark gates

This assessment would change only upon one of two exact inputs: (i) a complete
new finite extension/presentation with a frozen enumeration and full actual-power
observable; or (ii) a choice-free derivation that forces the fibre-pairing sets
`B_(h,j)` to be `{0}` for all indices, including a valid commuting-incidence
bridge. Without one of those inputs, another 33-minute phase would repeat a
stopped representation rather than test a new one.

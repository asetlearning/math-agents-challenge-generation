---
title: "MathExpert route — 21.137 — MCO-AFFINE-NORM-COVER"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: MCO-AFFINE-NORM-COVER
direction: proof
status: conjectured
refs:
  - Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
  - Agents/Kourovka/problems/21.137/verification/2026-08-17T035316Z-alg3-ut7-family-exhaustion.md
  - Agents/Kourovka/problems/21.137/verification/2026-08-17T043410Z-eq11-cube-cayley.md
  - Agents/Kourovka/problems/21.137/verification/2026-08-16T181302Z-minimal-central-obstruction.md
  - Agents/Kourovka/problems/21.137/verification/2026-08-16T144312Z-class-p-plus-one-hall-lemma.md
  - Agents/Kourovka/problems/21.137/verification/2026-08-16T151721Z-cth-three-five-integral-identity.md
  - Agents/Kourovka/problems/21.137/verification/2026-08-16T160819Z-cth-three-six-defect.md
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

# One selected experiment: MCO-AFFINE-NORM-COVER

## Scope lock

`scope_id`: `21.137/odd-prime-exponent-p2`  
`assignment_revision`: `2`

Exact target: for every odd prime `p` and finite `p`-group `G` of exponent exactly
`p^2`, if the actual value set `P={g^p:g in G}` is a subgroup, then `P` is
abelian.

Excluded: the general powerfulness clause, every `p=2` case, the exponent-8
two-group clause, odd-prime groups of any other exponent, wreath-shaped material,
and every enlargement or reparametrization of the exhausted two-generator
`UT_7(F_3)` template.

All assertions below that are not literal premises from the seven assigned refs
are **general mathematical knowledge, unverified**. They are a proposal for the
problem agent to derive and Validator to assess, not a certification.

## Obstruction

The reviewed finite template has no target-equal row, and the reviewed Hall lift
has a primitive degree-six defect. The reviewed minimum-counterexample reduction
gets much closer to the target: a hypothetical minimum counterexample has
`N=P'<=Z(G)`, `|N|=p`, `exp(P)=p`, and `A=P/N` elementary abelian, with `P`
abelian exactly when its alternating commutator form

`beta:A x A -> N`

vanishes. Its root-fibre observable does not couple strongly enough to `beta`:
off-radical fibres fill by conjugation, and the cyclic-center branch fills by
central roots. The missing ingredient is a representation that couples *all*
roots in one `P`-coset to the same symplectic action, rather than inspecting one
central fibre at a time.

## Direction and genuinely new representation

**Direction:** proof switch through the reviewed minimum-counterexample reduction.

Put `H=G/P`. For each `h in H`, choose a lift `x_h in G` and define the exact
coset power-support map

`Phi_h:P -> P,    Phi_h(k)=(x_h k)^p`,

and its image `S_h=Phi_h(P)`. Changing `x_h` within its coset merely
reparametrizes `k`, so `S_h` is the set of actual `p`-th powers coming from that
coset. This changes representation from matrix/algebra enumeration and Hall-word
coordinates to an affine norm-cover problem on the class-two exponent-`p` group
`P`.

### Exact target-facing observable

Use

`M(t)=#{(h,k) in H x P : Phi_h(k)=t}`  for `t in P`,

together with `beta`. In the reduced setup,

`Pow_p(G)=union_{h in H} S_h`,

so the actual-value-set hypothesis is mechanically visible as

`M(t)>0 for every t in P`.

The target conclusion is mechanically visible as

`beta=0`.

Thus no generated-subgroup surrogate, special prime, class cutoff, or raw
noncommuting pair enters the observable.

## First bounded derivation

Identify `N` additively with `F_p` and coordinatize the class-two exponent-`p`
group `P` as `A x F_p`. Let conjugation by `x_h` induce `L_h` on `A`, put
`D_h=L_h-I`, and write `c_h=x_h^p N in A`.

The proposed hand derivation has four exact gates:

1. Since `x_h^p in P` and inner automorphisms of `P` act trivially on `A`, derive
   `L_h^p=I`, hence `D_h^p=0`.
2. Derive the projected norm identity
   
   `pi_A(S_h)=c_h+im(I+L_h+...+L_h^(p-1))`
   
   and then the characteristic-`p` identity
   
   `I+L_h+...+L_h^(p-1)=D_h^(p-1)`.
3. Because `L_h` preserves `beta`, derive directly that
   `im D_h^(p-1)` is `beta`-isotropic. A proposed adjoint calculation is
   `(D_h^*)^(p-1)D_h^(p-1)=0`; every sign and degeneracy issue must be checked.
4. Choose the standard class-two coordinates on `P` and derive, without omitting
   central shears, an exact quadratic support formula
   
   `S_h={(c_h+D_h^(p-1)a, d_h+q_h(a)):a in A}`,
   
   where `q_h` is written explicitly from the action, the central shear, and
   `beta`. Input in the `N`-coordinate must disappear because `N` is central of
   exponent `p`; this is a gate, not an assumption.

The decisive test is then the single **norm-cover separator** question:

> Do the cross-`h` extension identities force a common missing point of
> `A x F_p` whenever `beta` is nonzero?

Pointwise isotropy or a cardinality bound is not enough. The experiment must write
the multiplication compatibility between the data for `h`, `j`, and `hj`, then
either extract one missing `(a,z)` or stop.

## Success certificate

A success is a target-level candidate proof, consisting of all of:

1. the exact coset-union equality for actual power values;
2. the full central-coordinate formula for every `S_h` at arbitrary odd `p`;
3. the cross-`h` compatibility identities coming from one extension `G`;
4. a named `(a,z) in A x F_p` excluded from every `S_h` under the assumption
   `beta!=0`;
5. the resulting contradiction to `M(a,z)>0`, hence the candidate conclusion
   `beta=0` and therefore `P` abelian.

The handoff must display all seven canonical constraint rows. Anything restricted
to `p=3`, a class bound, a chosen dimension, or merely the projected cover is not
success.

## Failure certificate and hard kill

The most likely failure is that arbitrarily many affine isotropic supports can
cover the whole space, while the needed cross-`h` identities retain essentially
all of the original extension problem.

The failure certificate must contain:

- the exact formulas reached in gates 1--4;
- the first cross-`h` identity that does not yield a common separator; and
- an explicit formal nonzero-`beta` cover datum satisfying every *pointwise*
  formula derived (clearly labelled as formal data, not a group or counterexample),
  showing why isotropy/counting alone cannot finish.

**Hard kill:** at active minute 44, if there is no common separator using a written
cross-`h` identity, stop the proof attempt. Use minutes 44--50 only to complete the
failure certificate and report `STRATEGY_EXHAUSTED` for
`MCO-AFFINE-NORM-COVER`; do not enlarge the model, switch to a catalogue, or turn
the formal datum into a witness claim.

## Minute allocation and cost

- `0--6`: restate the reduced hypotheses and derive the exact coset-union equality.
- `6--17`: derive `L_h^p=I`, the norm identity, and `D_h^(p-1)`.
- `17--27`: derive the isotropy statement with the adjoint signs checked.
- `27--37`: derive the full central quadratic `q_h` and lift-independence.
- `37--44`: write one cross-`h` compatibility identity and seek the common missing
  point.
- `44--50`: package either the success certificate or the mandatory failure
  certificate; stop.

Cost: exactly 50 active minutes, hand algebra only, no heavy-compute slot, no web,
no history, and no delegation.

## Mode audit and ranking

This is the sole recommendation. It ranks first because it preserves the exact
actual-value-set equality and exact abelian conclusion while coupling the reviewed
central obstruction to a new global observable.

- Finite catalogue/search is ruled out for this window: both low-dimensional
  `UT_7` branches are exhausted, and the request forbids enlarging that pattern.
- A new counterexample construction is not bounded by the seven refs: no fixed
  quotient with a pre-existing full actual-power closure certificate is available.
- The selected route combines a structured representation change with a
  theoretical minimum-counterexample reduction.

## Self-critique

The representation may only rename the obstruction. In particular, the union of
many affine isotropic sets can cover a symplectic space, so gates 1--3 alone cannot
force `beta=0`. The route has value only if gate 4 and the first cross-`h`
compatibility create a shared central-coordinate obstruction. The hard kill is set
before any temptation to continue with a larger family or another Hall span.

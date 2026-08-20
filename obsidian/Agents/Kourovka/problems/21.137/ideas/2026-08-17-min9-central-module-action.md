---
title: "MathExpert route — 21.137 — MIN9-CENTRAL-MODULE-ACTION"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: MIN9-CENTRAL-MODULE-ACTION
direction: counterexample
outcome: STRATEGY_LIVE
active_assignment_answered: no
author: operator
tags:
  - agent/math-expert
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/group-extensions
  - topic/module-actions
  - project/kourovka
  - status/conjectured
---

# One selected increment: `MIN9-CENTRAL-MODULE-ACTION`

## Scope lock and recommendation

Select one 60-active-minute **counterexample** increment. The canonical scope is
exactly `21.137/odd-prime-exponent-p2`, revision `2`: `p>2`, a finite same-`p`
group of exponent exactly `p^2`, the complete actual value set
`{g^p:g in G}` itself a subgroup, and the question whether that subgroup is
abelian. A `p=3` witness would refute this universal clause, so this bounded
equality case respects the human counterexample-first tie-break.

This route is conditional on the current equality claims for a quotient-minimal
order-`3^9` counterexample:

`P=H^3 ~= H_3(3) x C3^2`, `P'=C=C3`, and
`R=H/P in {C3^4, H_3(3) x C3}`.

My assessment is that no immediate dimension or quotient-type contradiction is
visible in those claims, but they still require Validator reconstruction before
an action-level exclusion is relied on. The newly replicated result is only the
bounded direct floor `|H|>=3^9` at `p=3`; the unrestricted assignment remains
open.

Excluded here: the general powerfulness clause, every `p=2` or exponent-8
case, groups of exponent other than `p^2`, and every stopped fixed-NS3,
NS3-repair, UT7, wreath-shaped, affine-cover, CPTR, and central-product/TRI3
construction route. No factor system, cocycle, descendant, or group catalogue
is opened in this increment.

All deductions introduced below are **general mathematical knowledge,
unverified** and are proposed for mechanical checking. No computation was run
in selecting the strategy.

## Obstruction and route comparison

The obstruction is now a compatibility wall, not a shortage of examples. The
equality rows freeze the kernel and quotient types, but a central `J3` image by
itself says neither that it lifts to the required `J4+J1` root action nor that
the possible root cosets can cover all noncentral elements of `P`.

- Refining the prior seed/catalogue method repeats an exhausted order layer.
- The proposed pivot changes representation to the complete outer-action
  quotient and has a finite orbit certificate.
- No stronger proof observable has appeared beyond the stopped affine/CPTR
  mechanisms.
- Parking is premature because the group to enumerate has order only `3^8` at
  its Sylow-3 level and the target-facing lift profile is factor-independent.

## Closed coordinate model to reconstruct first

Use the class-two exponent-three Lie model

`L=V direct_sum C direct_sum W`, with dimensions `2+1+2` and
`[v,v']=omega(v,v')c`.

In the ordered blocks `(V,C,W)`, reconstruct the automorphisms

```text
        [ g          0       0 ]
M   =   [ tau_C   det(g)   lambda ]
        [ tau_W      0       h ]
```

where `g,h in GL_2(3)`, `lambda:W->C`, and
`tau=(tau_C,tau_W):V->C direct_sum W`. The inner subgroup `I` is exactly the
two-dimensional `tau_C:V->C` shear subgroup. Put

`O=Aut(P)/I` and let `S` be the Sylow-3 subgroup obtained by taking `g,h`
upper unipotent and arbitrary `lambda,tau_W`.

The first certificate must reproduce

`|I|=3^2`, `|O|=|GL_2(3)|^2*3^6`, and `|S|=3^8`,

and must check the bracket on every generator rather than trusting a library
automorphism construction. On `Z(P)=C direct_sum W`, the restriction is
`[[1,lambda],[0,h]]` for `S`.

An image containing a regular `J3` already has common fixed space exactly `C`.
After conjugating its unique flag to the standard one, its central image is one
of exactly three branches:

1. cyclic regular `C3`;
2. the elementary-abelian `C3^2` centralizer of a regular block;
3. full `UT_3(3)`, possible only for the nonabelian quotient type.

The script must derive this branch partition from the matrices. It is not an
input assertion.

## Complete action-orbit coverage

Every image of either exponent-three quotient is a 3-subgroup of `O`, hence is
conjugate into `S`. Enumerate the conjugacy classes of subgroups of `S`, retain
only the possible quotient images, and then fuse them under full `O`-conjugacy:

- for `R=C3^4`: `U ~= C3^d`, `1<=d<=4`;
- for `R=H_3(3)xC3`: `U ~= C3^d`, `1<=d<=3`, or
  `U ~= H_3(3), H_3(3)xC3`.

The second list follows from the presentation: a nonabelian quotient kernel
cannot contain the derived generator, and normality then confines it to the
two-dimensional centre; it is either zero or a central complement line. This
claim is part of the hand/finite audit, not a classification citation.

For each retained `U`, enumerate epimorphisms `R -> U` modulo precomposition by
`Aut(R)` and postcomposition by `N_O(U)`. For `C3^4`, one epimorphism orbit per
embedded elementary-abelian `U` suffices; for the nonabelian `R`, enumerate the
small epimorphism set explicitly rather than assuming kernel transitivity.

Coverage requires a manifest containing, for every final orbit: quotient type,
kernel, image generators, `S`-class and full-`O` fusion witnesses, normalizer,
epimorphism-orbit size, central branch, and a representative tuple of `5 x 5`
lift matrices. The subgroup-class sizes and epimorphism-orbit sizes must sum to
their complete pre-fusion lists. A list lacking those partition checks is not a
finite action list.

## Target-facing observable: the lift/cube profile

Central-module regularity alone is too weak. For every `u in U`, inspect all
nine matrices in the fibre over `u^-1` in `Aut(P)`: these are exactly the
possible right-conjugation actions obtained by changing a root within its
`P`-coset.

For a lift `A`, put `N=A-I`. Admit a nonzero class `abar in V=P/Z(P)` only if

1. `rank(N),rank(N^2),rank(N^3),rank(N^4)=(3,2,1,0)` (`J4+J1`);
2. `N^3=D_abar` in the explicit inner-shear subgroup; and
3. the projection of `ker(N)` to `V=L/Z(P)` is exactly `<abar>`.

The third test prevents a matrix with the right Jordan partition but the wrong
fixed cube vector from passing. Let `n_u(abar)` count admitted lifts.

This produces a factor-system-independent necessary capacity test. For an
action `theta` with kernel size `k`, make a flow network with one node for each
`u in U`, source capacity `9k`, eight demand nodes indexed by
`0 != abar in V`, each with demand `27`, and edge capacity

`u -> abar : 3k*n_u(abar)`.

The proposed justification is: a quotient coset contributes at most nine
actual cubes in the reviewed equality bound; one fixed inner-action lift can
vary through at most three central values because the norm on a regular `J3`
centre has one-dimensional image; and each nonzero `V`-coset of `P` contains
27 elements. Therefore actual-cube surjectivity onto `P` requires max flow
`216`. Validator must check this implication before an empty action list is
used as an elimination.

Record for every orbit the table `n_u(abar)`, a maximum flow, and either a flow
witness of value `216` or a minimum cut. The observable is the pair of survivor
counts

`(survivors for C3^4, survivors for H_3(3)xC3)`.

If one count is zero after complete orbit coverage, that quotient type is
eliminated at the action level. If both are zero, the conditional order-`3^9`
equality family is empty. Any nonzero count is the complete finite handoff list
for a later factor-system decision; it is not a witness.

## Success, failure, and hard kill

Success for this increment is **not** a counterexample. It is one of:

- a complete empty list for a quotient type, with subgroup/epimorphism coverage
  and a lift-profile minimum-cut certificate; or
- a complete nonempty orbit manifest passing the central and flow gates.

The likeliest mathematical failure is that many actions survive because the
central coordinates of cubes and associativity live only in the factor system.
The likeliest operational failure is that a full subgroup lattice of `S` takes
longer than estimated. Neither failure favors the universal assertion.

Hard kills:

- stop by active minute `12` if the matrix group, inner quotient, orders, or
  centre restriction do not match the displayed reconstruction;
- stop the leased enumeration at active minute `45`; if the subgroup and
  epimorphism partitions are incomplete, preserve the exact frontier and make
  no quotient-type elimination;
- at minute `48`, begin packaging and do no further search;
- do not inspect even one factor system, add an action ansatz, reopen NS3, or
  extend to order `3^10` in this increment.

Proposed allocation: minutes `0--12` coordinate reconstruction; `12--32`
subgroup and epimorphism orbits; `32--45` nine-lift profiles and flow gates;
`45--48` replay one survivor and one rejection; `48--60` package and stop.

Any categorical subgroup enumeration requires a Lead lease. Proposed bounded
command:

`timeout 900s gap -q Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/scratch/min9_central_module_action.g`

Estimate: one heavy slot, at most 900 wall seconds, RAM below 1 GiB. If the
timeout fires, the result is an incomplete frontier, not family exhaustion.

## Fidelity and evidence boundary

`ACTIVE ASSIGNMENT ANSWERED: no`. This strategy concerns only the conditional
`p=3`, order-`3^9` equality family. It gives no conclusion for larger 3-groups,
for any `p>3`, or for the unrestricted revision-2 assertion.

Novelty is uncertain because the blind-run record forbids an open-web/history
search. The strategy used only:

- `Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json`;
- `Agents/Kourovka/problems/21.137/runs/2026-08-17-r12-central-product-defect/findings.md`;
- `Agents/Kourovka/problems/21.137/runs/2026-08-16-r2-odd-proof/findings.md`;
- `Agents/Kourovka/problems/21.137/verification/2026-08-17T105745Z-order6561-TRI3-layer.md`.

No computation, experiment, web search, solution-bearing history, quarantined
file, or excluded-scope material was used in this review.

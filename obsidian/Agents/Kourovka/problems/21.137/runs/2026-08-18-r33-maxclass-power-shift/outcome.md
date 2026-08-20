---
title: "R33 outcome — MAXCLASS-POWER-SHIFT"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: MAXCLASS-POWER-SHIFT
direction: proof
outcome: STRATEGY_EXHAUSTED
active_assignment_answered: no
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/maximal-class
  - project/kourovka
  - status/conjectured
refs:
  - Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
  - Agents/Kourovka/problems/21.137/ideas/2026-08-18-post-r4-faithful-character-portfolio.md
  - Agents/Kourovka/problems/21.137/verification/2026-08-16T144312Z-class-p-plus-one-hall-lemma.md
  - Agents/Kourovka/problems/21.137/runs/2026-08-18-r33-maxclass-power-shift/log.md
---

# Outcome

`MAXCLASS-POWER-SHIFT` is exhausted after 12 active minutes, at official
cumulative minute 737.  The proposed unqualified power-depth row is false, and
the corrected large-class row reduces exactly to an unproved structural theorem
about exceptional two-step centralizers.  The strategy's stated classification
hard kill therefore fires.  Twenty-eight unused minutes are returned to Lead.

This is a method outcome, not a negative verdict on maximal-class groups and not
an answer to the unrestricted source problem.

## Exact small-order failure of the proposed depth

For every odd prime `p`, let

`M_p=<a,b | a^(p^2)=b^p=1, b^-1 a b=a^(1+p)>`.

The automorphism `a -> a^(1+p)` has order `p` modulo `p^2`; normal forms
`a^i b^j` give order `p^3`.  Also
`[a,b]=a^p`, so `gamma_2(M_p)=<a^p>` and `gamma_3(M_p)=1`; hence `M_p` has
class `2`, maximal class for its order, and exact exponent `p^2`.  But
`a^p !=1=gamma_p(M_p)`.  Thus “every `p`-th power lies in `gamma_p`” is false
without a lower bound on the maximal-class order.

This group does not challenge the target conclusion: direct calculation gives
all `p`-th powers in `<a^p>`, so they commute.

## Low-order branch, exactly

Write `|G|=p^n`; a maximal-class group has class `n-1`.  The reviewed Hall
partial theorem says that for odd `p`, every group of exponent dividing `p^2`
and class at most `p+1` has pairwise commuting actual `p`-th powers.  Therefore
it applies verbatim when `n<=p+2`: exact exponent `p^2` implies exponent
dividing `p^2`, and maximal class gives `n-1<=p+1`.  Its conclusion is already
about individual actual values, so no substitution of the generated power
subgroup occurs and the closure hypothesis is not needed in this branch.

## Correct conditional large-order power law

Let `G_i=gamma_i(G)`, `G_n=1`.  Suppose a maximal-class group admits a
uniform-shift element `s` satisfying:

1. `s^p in Z(G)`;
2. `[G_j,s]G_(j+2)=G_(j+1)` for every `2<=j<=n-2`;
3. for a complement `s_1` to `G_2` in the distinguished maximal subgroup,
   some unit `a mod p` makes `s s_1^a` another element with central `p`-th
   power.

Weighted Hall collection, derived in the log, then gives both parts of the
precise layer statement:

`G_i^p <= G_(i+p-1)`,

and, for `2<=i<=n-p`,

`G_i^p G_(i+p)=G_(i+p-1)`.

The second formula is only equality modulo the next layer; no stronger subgroup
equality was assumed.  More precisely, every
`x in G_i\G_(i+1)` satisfies

`x^p in G_(i+p-1)\G_(i+p)`

whenever that target layer exists.  Collection also gives
`(xy)^p=x^p y^p (mod G_p)` and the two central-power elements force
`g^p in G_p` for every `g in G`.

If `G_(2p)` were nontrivial, take `x in G_2\G_3`.  Applying the individual
shift at `i=2` and then at `i=p+1` gives

`x^p in G_(p+1)\G_(p+2)` and
`x^(p^2) in G_(2p)\G_(2p+1)`,

contrary to exponent `p^2`.  Hence `G_(2p)=1`, and then every two actual
powers commute because

`[g^p,h^p] in [G_p,G_p] <= G_(2p)=1`.

### Explicit `p=3` index audit

At `p=3`, the first nonzero row is

`G_i^3 <= G_(i+2)`, `G_i^3 G_(i+3)=G_(i+2)`.

For `i=2`, collection modulo `G_5` reads
`[u,s]^3 [u,s,s,s]=1`: the intermediate `[u,s,s]^3` is already in `G_5`.
Thus an element of `G_2\G_3` cubes into `G_4\G_5`.  A second application at
`i=4` puts its ninth power in `G_6\G_7`.  Therefore the conditional law rules
out `n>=7`, exactly giving `G_6=1`; it does not silently assume that row.

## Exact hard-kill obstruction

The bare maximal-class axioms used here give one-dimensional lower-central
layers, but they do not by themselves supply conditions 2--3 above.  Those
conditions require control of every two-step centralizer

`C_j/G_2 = ker(G/G_2 -> Hom(G_j/G_(j+1),G_(j+1)/G_(j+2)))`.

If the chosen `s` lies in an exceptional intermediate `C_j`, the repeated
terminal commutator falls into `G_(j+2)`.  The Hall relation still gives a
containment, but it no longer gives the reverse nonzero layer inclusion needed
to turn `G_(2p)!=1` into an element of order `p^3`.  Establishing that all
maximal-class groups with `n>=p+3` have the required simultaneous uniform
shift, or proving directly that the exceptional patterns cannot have exponent
`p^2` when `G_(2p)!=1`, is precisely the missing classification-level theorem.
It was not derived, so importing the familiar maximal-class slogan
`G_i^p=G_(i+p-1)` would be circular at the decisive point.

No explicit exponent-`p^2` maximal-class group with `G_(2p)!=1` was obtained;
the family statement is open in this run.  The hard kill is lack of a derived
exceptional-family theorem, exactly as specified by the selected portfolio.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | result of this run | evidence/result |
|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | every qualifying odd `p,G` | only a conditional maximal-class reduction and a reviewed low-order branch | **fail for unrestricted scope** |
| `21.137-odd-p-not-2` | admissibility | odd prime `p>2` | used in binomial divisibility and the reviewed Hall branch | pass in covered/conditional family |
| `21.137-odd-finite-p-group` | admissibility | finite same-`p` group | assumed; additional maximal-class restriction | partial family only |
| `21.137-odd-exponent-p2` | admissibility | exact exponent `p^2` | used in the two-shift order contradiction; low branch accepts the stronger-inclusive dividing condition | pass in covered/conditional family |
| `21.137-odd-power-set-definition` | admissibility | literal actual set | derivation treats each `g^p`; it never replaces the set by generated powers | pass |
| `21.137-odd-power-set-subgroup` | admissibility | literal set is a subgroup | not needed by either proposed family argument | pass but unused |
| `21.137-odd-P-abelian` | conclusion | actual powers commute | reviewed only for `n<=p+2`; conditional above that; not obtained for every maximal-class group and not universal | **unproved** |

## Charge and handoff

- start: `2026-08-18T00:23:39Z`, official minute 725;
- stop: `2026-08-18T00:35:51Z`;
- charged: 12 active minutes;
- official cumulative: 737;
- unused returned: 28 minutes;
- computation: none;
- web: none;
- next action: Lead should choose a materially different authorized strategy or
  a fresh expert reconstruction of the exceptional centralizer theorem; this
  run opens neither.

`active_assignment_answered: no`.


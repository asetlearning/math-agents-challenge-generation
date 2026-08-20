---
title: "R33 MAXCLASS-POWER-SHIFT working log"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: MAXCLASS-POWER-SHIFT
direction: proof
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
  - status/draft
---

# Active target

For every odd prime `p>2` and finite same-`p` group `G` of exponent exactly
`p^2`, if the literal value set `P={g^p:g in G}` is itself a subgroup, prove
that `P` is abelian.  This run is restricted to the family in which `G` has
maximal class.  Therefore even a successful theorem here is only a family
partial, not an answer to the unrestricted assignment.

## Source and scope gate

- Source PDF page 184 was read and visually inspected.  Correct active clause:
  “for `p != 2`, if the `p`-th powers in a `p`-group of exponent `p^2` form a
  subgroup, must that subgroup be abelian?”
- `source_transcription_checked: yes`.
- The source has three clauses: the general powerfulness question (excluded),
  the odd-prime exponent-`p^2` abelianity question (active), and the exponent-8
  2-group question (excluded).
- `active_scope_checked: yes`.
- `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`.
- Canonical record reports the independent source-fidelity audit passed.  No
  web and no solution-bearing history are used in this run.

## Constraint-and-conclusion matrix at start

| constraint_id | role | required condition | use in this family run | result |
|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | every admissible odd `p,G` | restricted to maximal-class `G`; hence cannot settle this row universally | partial only |
| `21.137-odd-p-not-2` | admissibility | `p>2` prime | assumed throughout | pass |
| `21.137-odd-finite-p-group` | admissibility | finite same-`p` group | assumed throughout | pass |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly `p^2` | assumed throughout; must be used in the power/order bound | pending |
| `21.137-odd-power-set-definition` | admissibility | literal set of actual powers | every value is treated individually; never replaced by generated powers | pass |
| `21.137-odd-power-set-subgroup` | admissibility | literal set is a subgroup | available, though the proposed depth proof may not need it | pass |
| `21.137-odd-P-abelian` | target conclusion | actual powers commute | target within maximal-class family | pending |

## Active-time ledger

- Work start: `2026-08-18T00:23:39Z`; official cumulative active minute `725`.
- Authorized cap: 40 active minutes, through official minute `765`.

## Strategy and hard gate

Derive from lower-central commutator collection, without computation or citation
from memory, the precise depth of every `p`-th power in a maximal-class group and
the exact order/class hypothesis that would annihilate its self-commutator.  By
12 charged minutes, either both statements must be justified with hypotheses or
the first exceptional/large-class obstruction must hard-kill the route.

## Minute-10 gate: corrected statements

The portfolio's unqualified assertion `g^p in gamma_p(G)` is false for small
maximal-class groups.  For every odd `p`, the group

`M_p=<a,b | a^(p^2)=b^p=1, b^-1 a b=a^(1+p)>`

has order `p^3`, class `2` (hence maximal class), and exponent `p^2`, while
`a^p != 1=gamma_p(M_p)` for `p>=3`.  Its actual powers are central, so it is
not a counterexample; it is the exact reason a power-depth statement needs an
order hypothesis or a separate low-class case.

The corrected route is:

1. the already reviewed Hall theorem covers every exponent-dividing-`p^2`
   group of class at most `p+1`, hence every maximal-class group of order at
   most `p^(p+2)`;
2. for the remaining maximal-class groups, derive the layer power law
   `gamma_i^p gamma_(i+p)=gamma_(i+p-1)` for `i>=2`, and the individual
   containment `g^p in gamma_p`;
3. applying the layer law twice to a generator of `gamma_2/gamma_3` shows that
   `gamma_(2p) != 1` would give an element of order at least `p^3`.
   Therefore exponent `p^2` forces `gamma_(2p)=1`, after which
   `[g^p,h^p] in [gamma_p,gamma_p] <= gamma_(2p)=1`.

The remainder of the increment audits the layer law and every hypothesis; no
classification statement is being assumed.

## Weighted collection derivation and the exact missing hypothesis

Write `G_i=gamma_i(G)`, with `G_n=1` when `|G|=p^n`.  Thus
`|G:G_2|=p^2` and every `G_i/G_(i+1)` for `2<=i<=n-1` has order `p`.

The collection argument needs the following explicit uniform-shift datum:

- `(U1)` an element `s` with `s^p in Z(G)=G_(n-1)`;
- `(U2)` for every `2<=j<=n-2`, conjugation by `s` induces a nonzero map
  `G_j/G_(j+1) -> G_(j+1)/G_(j+2)`; equivalently, if
  `x in G_j\G_(j+1)`, then `[x,s] in G_(j+1)\G_(j+2)`;
- `(U3)` if `s_1` complements `G_2` in the distinguished maximal subgroup,
  there is a unit `a mod p` for which both `s` and `s s_1^a` have central
  `p`-th powers.

Under `(U1)--(U2)`, a descending induction gives the precise layer statement

`G_i^p <= G_(i+p-1)` and
`G_i^p G_(i+p)=G_(i+p-1)` whenever `G_(i+p-1) != 1`, for every `i>=2`.  Here
`G_i^p` denotes the subgroup generated by `p`-th powers only inside this layer;
the proof first treats every individual element.

Derivation: choose `u in G_(i-1)` such that `x=[u,s]` generates
`G_i/G_(i+1)` (for `i=2`, take the usual complementary generator `s_1`).
Collect `1=[u,s^p]` modulo `G_(i+p)`.  For a basic commutator having
`r>=1` copies of `u` and `q>=1` copies of `s`, its coordinate in
`[u,s^m]` is an integral Newton polynomial of `s`-degree at most `q` and
vanishes at `m=0`.  Hence at `m=p` it is divisible by `p` if `q<p`.
The sole shallow `q<p` factor is `[u,s]^p`.  Every other such factor lies in
some `G_d` with `d>=i+1`; by the descending induction its `p`-th power lies
in `G_(d+p-1)<=G_(i+p)`.  A factor with `q=p` and at least two copies of
`u` has filtration depth at least `2(i-1)+p>=i+p`.  The unique surviving
one-`u`, `p`-`s` factor is `[u,_p s]`, with coefficient `+1`.  Thus

`[u,s]^p [u,_p s] = 1 (mod G_(i+p))`.

By `(U2)`, the terminal commutator generates
`G_(i+p-1)/G_(i+p)`.  This proves both the containment and the nonzero
one-layer shift for a generator.  If `v in G_(i+1)`, collection of
`(x^a v)^p` has `v^p in G_(i+p)` and every mixed factor in `G_(i+p)`, so
the same containment holds for every element of `G_i`.  The induction starts
at `G_(n-1)=Z(G)`, which has order `p`.

The order consequence is exact.  If `G_(2p) != 1`, choose
`x in G_2\G_3`.  The shift twice gives

`x^p in G_(p+1)\G_(p+2)` and
`x^(p^2) in G_(2p)\G_(2p+1)`,

contradicting exponent `p^2`.  Hence `(U1)--(U2)` plus exponent `p^2`
forces `G_(2p)=1`, equivalently `n<=2p`.

Under `(U3)` the depth statement for elements of the whole group is also
exact.  The layer containment above makes Hall--Petrescu collection give

`(xy)^p = x^p y^p (mod G_p)`

for all `x,y`: factors of weight below `p` have `p`-divisible exponents and
their `p`-th powers shift into at least `G_(p+1)`, while factors of weight at
least `p` already lie in `G_p`.  Since the two uniform elements `s` and
`s s_1^a` have powers in `Z(G)<=G_p`, this congruence yields
`s_1^p in G_p`; the images of `s,s_1` generate `G/G_2`, so it follows that
`g^p in G_p` for every `g in G`.

Consequently `(U1)--(U3)` give, without using actual-set closure,

`[g^p,h^p] in [G_p,G_p] <= G_(2p)=1`.

The exact obstruction is that `(U2)--(U3)` were not derived from the bare
maximal-class hypothesis.  They amount to a complete control statement for
the two-step centralizers

`C_j/G_2 = ker(G/G_2 -> Hom(G_j/G_(j+1),G_(j+1)/G_(j+2)))`.

If an intermediate `C_j` contains the chosen `s`, the terminal commutator in
the displayed Hall row drops into `G_(j+2)` and is no longer a generator;
the equality needed for the order contradiction disappears.  Showing that
all sufficiently large odd-prime maximal-class groups admit one element
avoiding every relevant `C_j` (and the required second coset), or separately
excluding the exceptional centralizer patterns at exponent `p^2`, is a
nontrivial maximal-class classification theorem.  It was not reconstructed
from the lower-central indices.  The selected portfolio expressly hard-kills
if this shift requires such an unavailable theorem.

## Stop and charge

- Work stop: `2026-08-18T00:35:51Z`.
- Active time charged: 12 minutes.
- Official cumulative active minute: `737` (`725+12`).
- Unused authorized time returned to Lead: 28 minutes.
- Outcome: `STRATEGY_EXHAUSTED` for `MAXCLASS-POWER-SHIFT` only.
- `active_assignment_answered: no`.


---
title: "Problem 21.137 proof run r15: triple-root associator coherence"
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

# Active target

Scope `21.137/odd-prime-exponent-p2`, assignment revision 2. Let `p>2` be prime,
let `G` be a finite `p`-group of exponent exactly `p^2`, and let
`P={g^p:g in G}` be the complete actual value set. Assuming `P` is a subgroup,
test whether `P` must be abelian. The `p=2` and exponent-8 clause is excluded.

Run strategy: `TRIPLE-ROOT-ASSOCIATOR-COHERENCE`. For arbitrary actual values
`A,B,C`, retain independent roots of `AB`, `BC`, `(AB)C`, and `A(BC)` and every
root/section/lift change. Seek a genuinely gauge-independent three-value residual;
kill at 30 active minutes if all rows are pairwise coboundaries or full ambiguity,
and stop absolutely at 60.

## Source and staleness gate — 2026-08-17T13:17:23Z

- Source PDF page 184 was read and visually inspected. Correct active
  transcription: “For `p != 2`, if the `p`-th powers in a `p`-group of exponent
  `p^2` form a subgroup, must that subgroup be abelian?”
- `source_transcription_checked: yes`; the rendered exponent is `p^2`.
- The canonical revision-2 constraints agree exactly with the rendered source:
  universal odd prime and finite same-`p` group; exponent exactly `p^2`; `P` is the
  complete actual `p`-th-power value set; `P` is a subgroup; target `P` abelian.
- `active_scope_checked: yes`.
- `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`.

Clause matrix:

| source clause | active? | this run |
|---|---:|---|
| general powerfulness question | no | excluded |
| odd `p`, exponent `p^2`, actual power-set subgroup implies abelian | yes | exact target |
| `p=2`, exponent 8, square-set subgroup implies abelian | no | excluded |

## Strategy portfolio — 2026-08-17T13:17:23Z

1. Theoretical/formal-jet mode (selected): encode the four root fibres as torsors
   and compute the associativity square before and after arbitrary changes. Cheapest
   certifiable output is either a nonzero class in the quotient by the four gauge
   directions, or a formal jet showing that the quotient is zero.
2. Structured-construction mode: build a free nilpotent formal triple-root jet with
   an unconstrained bracket and solve every edge equation. This is used only as an
   algebraic independence certificate, not as a group counterexample.
3. Catalogue mode: forbidden and uninformative here; no computation is authorized.
4. Certificate plan: list the exact group identities for product fibres, write the
   complete gauge action, and exhibit either an invariant word or an explicit gauge
   absorption. Validator can check the identities by direct substitution in an
   arbitrary group.

## Active-time ledger

- Work start: `2026-08-17T13:17:23Z`; scope cumulative active minutes on entry: 418;
  run active minutes: 0.

## Exact four-fibre calculation — 2026-08-17T13:23:37Z

Fix actual values `A=a^p`, `B=b^p`, `C=c^p` in `P`. Closure supplies roots

```text
u^p=AB,   v^p=BC,   r^p=(AB)C,   s^p=A(BC).
```

The last two right sides are the same element `ABC`; thus `r,s` lie in the same
root fibre. No compatibility between the four choices is part of the hypothesis.

Do not assume that a root section is multiplicative. Instead define its four exact
multiplication defects

```text
k1 = a b u^-1,       k2 = u c r^-1,
k3 = b c v^-1,       k4 = a v s^-1.
```

Direct multiplication, with no collection or nilpotency assumption, gives

```text
k1 k2                    = a b c r^-1,
(a k3 a^-1) k4           = a b c s^-1,
Omega := (k1 k2)^-1 (a k3 a^-1) k4 = r s^-1.       (T)
```

Consequently the entire associativity-square residual is exactly the transition
between the two independently chosen terminal roots. The intermediate roots `u`
and `v` cancel before any filtration is taken. If one uses a single set-theoretic
root section, the two inputs `(AB)C` and `A(BC)` are equal, hence `r=s` and `(T)`
is the universal nonabelian factor-set identity

```text
k(A,B) k(AB,C) = a k(B,C) a^-1 k(A,BC).
```

This is associativity (`delta^2=1`), not a consequence peculiar to powers.

### Complete root-gauge row

Use the convention `x^g=g^-1 x g`. Every replacement of a root `t` by another
root `t'=t q` in the same fibre is described exactly by

```text
(t q)^p = t^p q^(t^(p-1)) ... q^(t^2) q^t q,
N_t(q):=q^(t^(p-1)) ... q^t q=1.                 (N)
```

Thus the four independent changes are
`u -> u alpha`, `v -> v beta`, `r -> r gamma`, `s -> s delta`, with the
corresponding exact norm-one conditions. Recomputing `(T)` gives

```text
Omega -> r gamma delta^-1 s^-1.
```

The `u` and `v` changes still cancel exactly. For the terminal fibre, the change
`s -> r` is always allowed (its validity is precisely `s^p=r^p`) and sends `Omega`
to `1`. Hence no class represented by `Omega` is invariant under the complete
root gauge.

Section freedom gives the same dichotomy: a section depending only on the value
forces the common terminal choice and makes the residual identically `1`; separate
local sections leave the arbitrary terminal transition above. Allowing distinct
internal section values inserts additional transitions and only enlarges the
ambiguity.

For any Zassenhaus quotient, `(T)` projects before one chooses graded lifts. Its
first nonzero homogeneous term is therefore the first term of the terminal
transition `r s^-1`. Replacing `s` by `r` kills that term in every degree. Changing
representatives/lifts merely adds the corresponding terminal lift difference.
Quotienting all allowed lift changes cannot leave a residual that the exact root
change already sends to zero.

### Prime-uniform formal noncommuting jet

This no-go can be witnessed without pretending to construct a target group. For
any odd `p`, let `P0=H_p x C_p`, where `H_p=UT_3(F_p)`, and choose standard
`A,B` with `[A,B]!=1` and an independent central `C`. The group `P0` has exponent
`p`. Form a star graph of groups with central vertex `P0` and, for every required
root occurrence, a cyclic leaf `<t_D>` of order `p^2`; identify
`<t_D^p>` with `<D>` for

```text
D in {A,B,C,AB,BC,ABC},
```

using two leaves over `ABC` for independent `r,s` (and extra leaves over any node
if an independent replacement is desired). The normal-form theorem for amalgams
injects `P0`, so `[A,B]` remains nontrivial, while the leaf generators give all
four displayed root equations and each selected root has order `p^2`. The exact
calculation `(T)` and every root-replacement norm row hold. Choosing the same
terminal leaf makes `Omega=1`; choosing the two leaves makes `Omega=r s^-1`, a
pure terminal transition.

This is a formal method certificate only. The amalgam is infinite, does not have
global exponent `p^2`, and its complete actual power set is not asserted to be a
subgroup. It therefore fails the active finite-`p`-group, exact-exponent, and
actual-set-subgroup rows and is not a candidate counterexample. It shows precisely
that the local four-root equations plus associativity admit a nonzero value bracket;
any proof must use additional global finiteness/exponent/fibre information.

## Early kill decision — 2026-08-17T13:23:37Z

`TRIPLE-ROOT-ASSOCIATOR-COHERENCE` meets its named kill before 30 minutes. The
canonical residual is either the universal section coboundary (`r=s`) or the full
terminal-root ambiguity (`r!=s`). It yields no gauge-independent prime-uniform
commutator relation. This exhausts only the four-fibre associativity comparison,
not the active scope.

Two qualitatively different future routes for Lead to assess are: (i) a finite
fibre-cardinality/orbit argument using that the entire power map has finite domain
and image subgroup, rather than choosing local roots; (ii) a minimum-counterexample
normal-subgroup argument exploiting characteristicity and exponent `p^2` globally.
No pivot is started here.

- Work stop: `2026-08-17T13:25:06Z`; run active minutes: 8; scope cumulative active
  minutes: 426. State: `awaiting_lead`.

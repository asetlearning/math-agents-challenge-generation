---
title: "Verification — Kourovka 21.137 — conditional nine-lift histogram reduction"
problem: 21.137
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "Inside the stated p=3, order-3^9 equality-action model, every centrally regular outer element has either nine admissible inner lifts for one nonzero cube label or no admissible lift, and the induced histogram flow excludes action images of orders 3 and 9."
claimant: Problem-21.137
target_statement: "Let p be odd and G a finite p-group of exponent exactly p^2. If the actual pth-power value set P is a subgroup, then P is abelian."
excluded_scopes: ["21.137/two-group-exponent-8", "c-general powerfulness", "odd-prime groups not of exact exponent p^2"]
target_object: "An arbitrary finite p-group satisfying the active odd-prime exact-exponent and actual-power-set hypotheses."
witness_object: "A conditional 5-dimensional F3 automorphism block and its inherited action-level flow network in the p=3 order-3^9 equality family; no finite group witness is submitted."
witness_equals_target: false
citation: none
verification_method: "independent hand block multiplication, Jordan analysis, fixed-space solving, lift-fibre analysis, max-flow aggregation, and regular-unipotent counting"
tools_used: ["GAP 4.12.1 (availability/version probe only)", "Python 3.12.3 (availability/version probe only)"]
scope_answered: []
scope_not_answered: ["21.137/odd-prime-exponent-p2", "c-general", "c-two"]
active_assignment_answered: no
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/module-actions, project/kourovka, status/conjectured]
---

# Verification — Kourovka 21.137

## The claim

This audit concerns only the following conditional lemma.  Work over `F=F_3`, let
`dim(V)=dim(W)=2`, `dim(C)=1`, use column vectors in the ordered decomposition
`V+C+W`, and let an automorphism lift be `A=I+N`, where

```text
N = [ G  0  0 ]
    [ a  0  l ]
    [ T  0  H ].
```

Here `a,l` are rows and `G,H,T` are `2 x 2` blocks.  The nine inner lifts over a
fixed outer element vary only `a`.  Under the stated centrally regular condition,
the claim is that the complete one-root action gate is equivalent to

```text
HTG=0,                 r=l(TG+HT) != 0,
```

that the label is uniquely determined by `r=(abar_2,-abar_1)`, that all nine
values of `a` therefore pass or all fail, and that the resulting histogram flow
rules out action images of order 3 or 9.

This is not a finite group construction and not an answer to the active scope.

## Scope, revision, and clause matrix

The canonical record is revision 2 and the active clause is `c-odd`.  The exact
scope requires `p>2`, a finite p-group of exponent exactly `p^2`, the set of
*actual* pth-power values (not merely the verbal subgroup they generate), closure
of that value set as a subgroup, and abelianity of that subgroup.

| source clause | in active scope | result of this audit |
|---|---:|---|
| `c-general`, powerfulness | no | unanswered |
| `c-odd`, odd p and exponent exactly p^2 | yes | unanswered; only a conditional p=3, exponent-9, order-3^9 action family is narrowed |
| `c-two`, p=2 and exponent 8 | no | expressly excluded and unanswered |

Thus `active_assignment_answered: no` is forced independently of whether the
conditional lemma passes.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | use in this submission | result |
|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | every odd p and every qualifying G | only p=3 and one conditional order layer | not established |
| `21.137-odd-p-not-2` | admissibility | p>2 prime | p=3 | passes for the specialization only |
| `21.137-odd-finite-p-group` | admissibility | finite p-group | no group is constructed | conditional/unknown |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly p^2 | exponent 9 belongs to the assumed vehicle, not to a checked group | conditional/unknown |
| `21.137-odd-power-set-definition` | admissibility | actual value set `{g^p}` | represented only by an inherited flow gate | not established from the submitted records |
| `21.137-odd-power-set-subgroup` | admissibility | the actual value set is a subgroup | supplies an inherited necessary demand, but closure is not checked on a group | not established from the submitted records |
| `21.137-odd-P-abelian` | target conclusion | P is abelian | neither proved nor violated | not established |

## Target versus witness

The target is a universal group-theoretic assertion.  The submitted object is an
action-level necessary condition in one proposed minimum-order equality family.
They are not equal.  In particular, passing or failing the present gate neither
constructs an exponent-9 group nor proves that all groups in the active scope pass
the gate.

## Independent reconstruction

### 1. The diagonal nilpotents

An element of a 3-subgroup of `GL(2,3)` has order at most 3 and is unipotent.
Consequently, for `g=I+G` and `h=I+H`, Cayley--Hamilton on the 2-dimensional
spaces gives

```text
G^2=0,                 H^2=0.
```

This includes the identity case `G=0` or `H=0`.

### 2. Direct multiplication and independence from the inner row

Block multiplication, before using the square-zero relations, gives

```text
N^2 = [ G^2          0   0   ]
      [ aG+lT        0   lH  ]
      [ TG+HT        0   H^2 ],

N^3 = [ G^3                    0   0    ]
      [ aG^2+lTG+lHT           0   lH^2 ]
      [ TG^2+HTG+H^2T          0   H^3  ].
```

Hence, over the stated 3-subgroup image,

```text
N^3 = [ 0                 0  0 ]
      [ l(TG+HT)          0  0 ]
      [ HTG               0  0 ].
```

Equivalently, on `V`, the `C` component is
`r=l(TG+HT)` and the `W` component is `HTG`; every other component is zero.
The only possible occurrence of the inner-lift row was `aG^2`, so `N^3` is
independent of `a`.  This also checks that the column/block convention in the
submission is consistent.

Since the characteristic is 3,

```text
A^3=(I+N)^3=I+N^3.
```

### 3. Centrally regular restriction

On `C+W`, the nilpotent part is

```text
K = [ 0  l ]
    [ 0  H ],            K^2 = [ 0  lH ]
                                  [ 0   0 ].
```

It has regular Jordan type `J3` precisely when `K^2` is nonzero.  This is
equivalent to `rank(H)=1` and `lH!=0`.  Then

```text
im(H)=ker(H)=:K_H,
```

and `l` is nonzero, hence surjective to `C`, on the one-dimensional line `K_H`.
This proves the centrally regular criterion used by the submission.

### 4. The cube label and Jordan type

For the Heisenberg factor, an inner automorphism labelled by
`abar=(abar_1,abar_2)` has nilpotent row

```text
J(abar)=(abar_2,-abar_1)
```

under the displayed right-conjugation/symplectic convention.  The linear map
`J:V -> V*` is a bijection and `ker J(abar)=<abar>` for nonzero `abar`.

Thus `N^3=D_abar` for a noncentral label is equivalent to

```text
HTG=0,                 r=J(abar) != 0.
```

This gives a unique nonzero label, namely
`abar=(-r_2,r_1)` in the displayed convention.  If the outer element is indexed
by the inverse action or the opposite commutator convention, the label acquires
an invertible sign/conjugacy change.  That change permutes the eight nonzero
labels and has no effect on the all-nine/zero statement or any histogram
capacity.  The exact sign must nevertheless be kept consistent in any later
factor-system calculation.

Under `HTG=0`,

```text
rG = l(TG^2+HTG)=0.
```

Therefore `N^4=0`.  Since `r!=0`, `N^3` has rank one.  A nilpotent endomorphism
on a 5-dimensional space with fourth power zero and third power of rank one has
exactly one size-4 Jordan block and one remaining size-1 block.  Its type is
therefore `J4+J1`.  This establishes the claimed Jordan implication and also its
converse once the noncentral inner cube `D_abar` is required.

### 5. Projected fixed line, including dependence on `a`

The fixed space of `A` is `ker N`.  A vector `(v,c,w)` lies in it exactly when

```text
Gv=0,
Tv+Hw=0,
av+lw=0;
```

the coordinate `c` is free.  Once the middle equation is solvable, replacing a
solution `w` by `w+t`, `t in ker(H)`, preserves it.  Because `l` is nonzero on
`ker(H)`, a unique choice of the scalar `t` can impose the last equation for
every row `a`.  Hence the projection to `V` is independent of `a`.

If `G=0`, the middle equation is solvable precisely when `Tv` belongs to
`im(H)=ker(H)`.  Since `HTv` lies in `im(H)` and `l` is nonzero there, this is
equivalent to

```text
lHTv=0.
```

Here `r=lHT`, so the projected fixed space is `ker(r)=<abar>`.

If `rank(G)=1`, then `im(G)=ker(G)=:L`.  The equation `HTG=0` says `HT` vanishes
on `im(G)=L`; consequently `Tv in ker(H)=im(H)` for every `v in L`, and the
middle equation is solvable for every `v in L`.  Thus the projection is `L`.
Moreover `rG=0`, so `im(G)<=ker(r)`.  Both sides are lines, and hence

```text
L=ker(r)=<abar>.
```

This proves the displayed projected-fixed-line assertion in both possible ranks
of `G` and checks the potentially dangerous central equation explicitly.

### 6. Why the lift fibre is all nine or zero

In the stated Heisenberg-times-central setting, the inner automorphism group is
parametrized by `V`, hence has nine elements.  Composing an outer representative
on either side with an inner automorphism changes only the row `a`; because `g`
is invertible, the nine resulting rows are all nine elements of `V*`.  The blocks
`G,H,l,T` do not change.

The cube equation is independent of `a` by section 2, and the fixed-lift equation
is solvable for every `a` by section 5.  Therefore an outer element satisfying
the centrally regular precondition has exactly one of the following profiles:

```text
n_u(abar)=9 for one nonzero abar and 0 for the other seven labels;
```

or `n_u(abar)=0` for every nonzero label.  There is no intermediate fibre size.
This proves the asserted all-nine/zero result under the submitted nine-lift
parametrization.

### 7. Histogram max flow

Let the eight demand vertices be the nonzero labels `abar in F_3^2`, each with
sink capacity 27.  Let `U` be the action image and `k=81/|U|`.  An admitted outer
element supplies `k*n_u(abar)=9k` units and is adjacent to exactly its unique
label.  If `m_abar` is the number of admitted outer elements carrying that label,
then the component of the network at `abar` has total source capacity
`9k*m_abar` and sink capacity 27.  Different label components have no common
edge.  Consequently

```text
maxflow = sum_{abar != 0} min(27,9k*m_abar).
```

No Hall-type interaction remains after the one-label property: this is an exact
decomposition, not merely an upper bound.  Changing the inverse-lift or symplectic
sign convention only permutes the summands.

The total demand in the inherited gate is `8*27=216`.  The algebra above verifies
the collapse of that gate to a histogram; the two submitted records do not
re-derive why actual cube-value-set closure supplies these eight demands, so that
upstream implication remains an explicit hypothesis of this audit.

### 8. Counts in the three central branches

The quoted proportions can be reconstructed in the standard 3-dimensional
unipotent model.

Let `J=E_12+E_23`, so `J^2=E_13`.  In a cyclic regular group of order 3, both
nonidentity elements have nilpotent square of rank one.  Thus 2 of 3 elements
are regular.

The 3-part of the centralizer of a regular unipotent consists of the nine
polynomials `I+xJ+yJ^2`.  Such an element is regular exactly when `x!=0`, giving
`2*3=6` regular elements out of 9.

Finally, an element of `UT_3(3)` has nilpotent part

```text
xE_12+yE_23+zE_13,
```

whose square is `xyE_13`.  It is regular exactly when `x` and `y` are both
nonzero.  There are `2*2*3=12` such elements out of 27.

Pulling back through the central-restriction homomorphism therefore gives

```text
cyclic regular branch:       2|U|/3,
elementary centralizer:      6|U|/9 = 2|U|/3,
full UT_3(3):                12|U|/27 = 4|U|/9.
```

The full `UT_3(3)` branch cannot occur when `|U|` is 3 or 9, because its image
already has order 27; its small-image exclusion is therefore vacuous rather than
a separate flow calculation.

### 9. Orders 3 and 9

If `|U|=3`, then `k=27` and at most two outer elements are centrally regular.
Each can contribute at most its label cap 27, so

```text
maxflow <= 2*27 = 54 < 216.
```

If `|U|=9`, then `k=9`.  The cyclic branch (kernel of order 3) and the
elementary-centralizer branch (injective central restriction) each have exactly
six centrally regular elements.  Again every element contributes at most 27, so

```text
maxflow <= 6*27 = 162 < 216.
```

Label collisions can only decrease these upper bounds.  Thus action images of
orders 3 and 9 fail the stated necessary flow gate for either conditional quotient
type.

For an elementary quotient `C_3^4`, images of order at least 27 can only be
`C_3^3` or `C_3^4`.  For `H_3(3) x C_3`, an order-27 image is either elementary
`C_3^3` or the exponent-3 nonabelian group `H_3(3)`, while a faithful order-81
image is `H_3(3) x C_3`.  This recovers exactly the submitted list of survivors.

## Subclaims and what each method proves

| subclaim | independent method | result | limitation |
|---|---|---|---|
| formula for `N^3` and `HTG` component | direct multiplication | passes | conditional on the submitted normal form |
| independence from `a` | isolate the sole term `aG^2` | passes | does not prove the normal form covers every action |
| `J4+J1` and cube label | ranks of nilpotent powers | passes | exact label sign is convention-sensitive |
| projected fixed line | solve all three block equations | passes | uses central regularity essentially |
| all-nine/zero fibre | inner-row parametrization plus the previous two calculations | passes conditionally | requires the asserted nine-lift parametrization |
| histogram formula | decompose the one-label network | passes | demand provenance is not in the submitted records |
| regular-element proportions | explicit regular-unipotent counts | passes | central-branch completeness is inherited |
| exclusion of orders 3 and 9 | capacity upper bounds | passes conditionally | says nothing about images of order 27 or 81 |

## Evidence

No search, solver, catalogue, or algebra-system computation was used.  The only
tool executions were availability/version probes:

```text
$ command -v gap
/usr/bin/gap
$ command -v sage
$ command -v python3
/usr/bin/python3
$ command -v magma
$ python3 --version
Python 3.12.3
$ gap -q -b -c 'Print(GAPInfo.Version,"\\n");'
4.12.1
```

All mathematical evidence is the line-by-line hand reconstruction above.

## Verdict

`status/conjectured` for the submitted conditional partial result, with the
following sharper mathematical judgement: the block multiplication, the
`HTG=0`/nonzero-`r` criterion, the `J4+J1` implication, the projected fixed-line
calculation, the all-nine/zero fibre consequence, the histogram formula, and the
order-3/9 capacity arithmetic all pass independent hand reconstruction under the
stated normal-form, lift-parametrization, branch, and flow-demand premises.

The ladder is not raised because the exact-reference submission does not contain
proofs of those upstream premises, especially the translation from actual
cube-value-set closure to the eight capacity-27 demands.  The conditional lemma
is safe to use as an action-level necessary gate, with those hypotheses displayed.

## Why this verdict

No sign, row/column, nilpotency, fixed-space, or capacity error was found.  The one
convention-sensitive point is harmless for this lemma: using an inverse lift or
the opposite commutator convention permutes the eight nonzero labels.  It must not
be silently reused in a sign-sensitive cocycle calculation.

The small-image conclusion is a strict capacity obstruction (`54<216` and
`162<216`), so it does not depend on how admitted elements distribute among
labels.  The full `UT_3(3)` branch simply cannot have an action image of order 3
or 9.

## What is NOT established

- The unrestricted statement for all odd primes and all finite p-groups remains
  unanswered.
- No finite group, extension, factor system, cocycle, or counterexample is
  constructed.
- Exact exponent 9 and actual cube-value-set closure are not checked on any group.
- The order-3^9 equality reduction, completeness of the action normal form,
  completeness of the three central branches, the formula `k=81/|U|`, and the
  derivation of eight demands of size 27 are premises rather than proved content
  of the two submitted records.
- Images of order 27 or 81 are not excluded.
- The p=2 exponent-8 clause and the general powerfulness clause are untouched.

## What would upgrade it

A self-contained upstream certificate should derive the `(V,C,W)` automorphism
normal form and all nine lifts from the conditional quotient, derive the flow
network and every demand/capacity directly from actual cube-value-set closure,
and prove that the three central branches exhaust the relevant action images.
Once those premises are independently supplied, the present hand proof would
complete the conditional action-level exclusion; it would still not answer the
active scope.

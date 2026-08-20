---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/conjectured
---

# Candidate family partial: simple small-Ree groups

## Outcome and scope fidelity

`PARTIAL_RESULT`, not a solution of the active universal problem.

For the standard generic ordinary-character and element-type inventories written
below, the exact implication

`chi(x) != 0  =>  o(x) chi(1) divides |G|`

holds for every simple small-Ree group `G = ^2G_2(q)`,
`q=3^(2m+1)>=27`. The proof avoids all character-value evaluation: every cell at
which divisibility could fail is forced to be exactly zero by the ordinary
defect-zero vanishing theorem. Thus cyclotomic cancellation in the remaining
cells is harmless.

`active_assignment_answered: no`: the active scope quantifies over all finite
groups, while this covers one infinite simple family only.

## Uniform notation and factor arithmetic

Put

```
r = sqrt(3q) = 3^(m+1),   s = r/3 = 3^m,
u = (q-1)/2,             a = (q+1)/4,
b = q-r+1,               c = q+r+1.
```

Here `q=3^(2m+1)` with `m>=1`, so `q` is `3 mod 8`; `u,a,b,c` are odd and

```
b c = q^2-q+1,
|G| = q^3(q-1)(q+1)(q^2-q+1) = 8 q^3 u a b c.
```

The five numbers `3,u,a,b,c` are pairwise coprime. For example, a common odd
prime of `u` and `b` or `c` would give `q=1`, `r=+/-2`, and
`r^2=3q`, hence `4=3` modulo that prime. A common prime of `a` and `b` or `c`
would give `q=-1` and `r=0`, hence the prime is `3`, impossible since `3` does
not divide `q+1`. Finally `gcd(b,c)` divides `2r`, while both are odd and `1`
modulo `3`. Also `gcd(u,a)=1` follows from `u-2a=-1`.

## Complete element-type inventory used

Besides the identity there are nine fixed classes:

| type | number | exact order | centralizer order |
|---|---:|---:|---:|
| involution `J` | 1 | 2 | `q(q^2-1)` |
| `U_0` | 1 | 3 | `q^3` |
| `U_+`,`U_-` | 2 | 3 | `2q^2` |
| `JU_+`,`JU_-` | 2 | 6 | `2q` |
| `V_0`,`V_+`,`V_-` | 3 | 9 | `3q` |

All remaining classes are semisimple:

| torus/centralizer type | number of classes | exact orders of representatives |
|---|---:|---|
| split cyclic `C_(q-1)=C_(2u)` | `(q-3)/2` | `(q-1)/gcd(q-1,i)` for inversion-orbit representatives `i`, excluding identity and the involution |
| `C_2^2 x C_a`, centralizer order `q+1=4a` | `(q-3)/6` | for `e z^i` with `z` of order `a`, `a/gcd(a,i)` if `e=1`, and `2a/gcd(a,i)` if `e!=1`; `i=0` gives only identity/involutions and is already separated |
| cyclic `C_b` | `(q-r)/6` | `b/gcd(b,i)` on the nonidentity normalizer orbits |
| cyclic `C_c` | `(q+r)/6` | `c/gcd(c,i)` on the nonidentity normalizer orbits |

Thus there are `10+(q-3)/2+(q-3)/6+(q-r)/6+(q+r)/6=q+8`
classes. For the divisibility proof, the only needed consequences are that every
element order is one of `1,2,3,6,9`, a divisor of `2u`, a divisor of `2a`, a
divisor of `b`, or a divisor of `c`; after identity and `J` are separated, a
split or `C_2^2 x C_a` class has a nontrivial odd `u` or `a` factor respectively.

## Complete ordinary degree inventory

Write `D=bc=q^2-q+1`. The ordinary irreducibles have the following degrees and
multiplicities; the last column is the exact codegree `|G|/chi(1)`.

| label | multiplicity | degree | codegree |
|---|---:|---:|---:|
| `1` | 1 | `1` | `8q^3uabc` |
| `D` | 1 | `bc` | `8q^3ua` |
| `E_b` | 2 | `s*u*b` | `8(q^3/s)ac` |
| `E_c` | 2 | `s*u*c` | `8(q^3/s)ab` |
| `F` | 2 | `8sua` | `(q^3/s)bc` |
| `A_b` | `(q+r)/6` | `8uab=(q^2-1)b` | `q^3c` |
| `B` | `(q-3)/6` | `2ubc=(q-1)D` | `4q^3a` |
| `qD` | 1 | `qbc` | `8q^2ua` |
| `St` | 1 | `q^3` | `8uabc` |
| `C` | `(q-3)/2` | `4abc=(q+1)D` | `2q^3u` |
| `A_c` | `(q-r)/6` | `8uac=(q^2-1)c` | `q^3b` |

The multiplicities total `q+8`. Exact polynomial reduction using `r^2=3q` gives

```
sum multiplicity * degree^2 = 8 q^3 u a b c = |G|.
```

The executable checksum is
`scratch/ree_factor_audit.py`; it prints
`sum_square_remainder_mod_r2_minus_3q= {}`.

## Defect-zero support audit

Use the standard ordinary theorem: if an irreducible character has `p`-defect
zero, equivalently `chi(1)_p=|G|_p`, then it is zero on every `p`-singular
element.

Because `3,u,a,b,c` are pairwise coprime and `|G|_2=8`, the displayed
factorizations make this mechanical. If an element order does not divide the
displayed codegree, choose a deficient coordinate among `2,3,u,a,b,c`. That
coordinate is wholly absent from the codegree and wholly present in the degree:

- absence of `2` makes the character 2-defect zero;
- absence of `3` occurs only for `St`, which is 3-defect zero;
- absence of an odd coordinate `u,a,b,c` makes the character `p`-defect zero
  for every prime `p` in that coordinate.

The element is singular for one such `p`, so its character value is exactly
zero. Conversely, when no coordinate required by the element order is absent,
the exact order divides the codegree. The only exponent checks not visible from
the coordinate names are harmless: every occurring even element has 2-part at
most `2`; every non-Steinberg codegree containing `3` has 3-part at least `9`
for `m>=1`; split and `C_2^2 x C_a` elements have orders dividing `2u` and
`2a` respectively.

This covers every cell, including all 3-local classes, the involution, both
mixed order-six classes, and all exceptional degree pairs. The script prints the
full class-type/degree-family matrix, marking every dangerous cell
`ZERO_BY_DEFECT`.

## Cyclotomic cancellations

No inference uses a claim that a root-of-unity sum is nonzero. Every cell not
forced zero above is treated as potentially nonzero, and its exact element order
already divides the codegree. Any parameter-dependent cancellation in a generic
semisimple value can therefore only remove an already-safe cell. It cannot
create a dangerous nonzero cell. This is a rigorous support superset rather than
a finite-parameter interpolation of values.

## Independent finite sanity check (not a family premise)

The installed GAP/CTblLib table `R(27)` has group order `10073444472`, 35
ordinary rows/classes, and precisely the degrees predicted above. An exact scan
of all 1,225 cells found 641 nonzero values and zero violations. This finite
check is only a transcription sanity check; the proof above does not infer the
generic statement from it.

## Constraint-and-conclusion matrix

| constraint_id | role | use/result |
|---|---|---|
| `20.115-forall-G-chi-x` | admissibility | **not met globally**: only all `^2G_2(q)`, `q>=27`, are covered |
| `20.115-G-finite` | admissibility | each group in the covered family is finite |
| `20.115-chi-complex-irreducible` | admissibility | the complete ordinary irreducible degree inventory is used |
| `20.115-x-in-G` | admissibility | the complete element-type inventory and exact order formulas are used |
| `20.115-character-value-nonzero` | admissibility | dangerous cells are exactly zero; every remaining cell is allowed to be nonzero |
| `20.115-order-degree-divisibility` | target conclusion | established for the covered family by the factor/defect-zero audit |

## What this does not establish / how it could be wrong

- It does not address any finite group outside the simple small-Ree family and
  therefore does not answer the active universal assignment.
- The two generic inventories are classification input. Their class count,
  character count, sum-of-squares identity, and `q=27` specialization all pass,
  but this clean lane did not have a second local generic-table source. A fresh
  Validator must compare every family, multiplicity, torus structure, and fixed
  class order with an independent authoritative table before accepting the family
  theorem.
- A missed generic class type with an order outside the listed eight order forms,
  or a miscopied degree/multiplicity, would invalidate completeness. The defect-zero
  implication itself has no character-value or cancellation assumption.

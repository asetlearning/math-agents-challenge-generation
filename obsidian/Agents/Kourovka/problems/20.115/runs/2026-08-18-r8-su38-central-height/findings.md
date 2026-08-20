---
title: "Partial result — SU3(8) obstructs the central-height family bridge"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
outcome: PARTIAL_RESULT
active_assignment_answered: no
active_time_charge: "00:10:52"
official_cumulative_active_time: "01:14:57"
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/replicated]
---

# Partial result — `SU_3(8)` obstructs the central-height family bridge

## Active target

For every finite group `G`, every ordinary complex irreducible character
`chi`, and every `x in G`, the universal target asks whether

```text
chi(x) != 0  =>  o(x) chi(1) divides |G|.
```

This note does **not** answer that target.

Actual active charge for this run was `00:10:52`; official cumulative active
time is `01:14:57/03:00:00`.

## Bounded claim

Let `L=SU_3(8)=3.U3(8)`, `p=3`, and `Z=Z(L)=C3`.  The principal
ordinary 3-block has six characters of degree `189` and height `3`.
For a Sylow defect group `P`,

```text
|P/Z|=81,   exp(P/Z)=9,
```

so each of those six characters violates the central-height condition:

```text
3^h = 27 > |P/Z|/exp(P/Z) = 9.
```

Equivalently,

```text
exp(P/Z)=9 > (|L:Z|/189)_3 = 3.
```

Thus Condition `(‡*)` used by the reviewed Proposition 3.2 bridge fails for
`SU_3(8)` at `p=3`.  In particular, the sufficient generic theorem proposed
as missing in the preceding family reduction—principal-block height at most
`v_3(q+1)`—is false at `q=8`, since `v_3(9)=2<3`.

This is an obstruction to that proof strategy, not a counterexample to
Kourovka 20.115 and not a failure of Proposition 3.2.

## Exact object and identity

GAP 4.12.1 with CTblLib 1.3.7 returns the ordinary table
`CharacterTable("3.U3(8)")`, with identifier `3.U3(8)`, order
`16547328`, 82 classes, and 82 ordinary irreducible characters.  Their squared
degrees sum to the table order.  The standard matrix group `SU(3,8)` has the
same order

```text
8^3(8^3+1)(8^2-1)=16547328
```

and center of order `gcd(3,9)=3`; its quotient has order `5515776`.
This is the standard perfect triple cover denoted `3.U3(8)`, not the simple
quotient `U3(8)`.

`PrimeBlocks(t,3)` returns ten ordinary 3-blocks with defects

```text
[5,2,2,2,1,1,1,1,1,1].
```

Here `v_3(|L|)=5`.

## Defect representatives and quotient exponents

The reviewed central Brauer-pair argument gives `Z<=D` for every ordinary
3-block defect group.

| blocks | rows per block | defect | explicit representative | `|D/Z|` | `exp(D/Z)` | threshold `|D/Z|/exp(D/Z)` |
|---|---:|---:|---|---:|---:|---:|
| 1 | 37 | 5 | a computed Sylow subgroup `P<=SU(3,8)` | 81 | 9 | 9 |
| 2--4 | 9 each | 2 | the cyclic order-nine group `<x>` below | 3 | 3 | 1 |
| 5--10 | 3 each | 1 | `Z` | 1 | 1 | 1 |

The frozen output prints literal generators for `P`, verifies `|P|=243` and
`Z<=P`, and computes the order and exponent of `P/Z` exactly.

For blocks 2--4 the checker selects inside `P` an order-nine matrix `x` whose
minimal polynomial over `GF(64)` has degree two and whose cube is a nontrivial
central scalar.  Hence `<x>` is cyclic of order nine and contains `Z`.
Because the element order is prime to characteristic two, `x` is semisimple;
its two eigenvalues have multiplicities `2+1`.  Its unitary centralizer is
`S(U_2(8) x U_1(8))`, of order

```text
8(8-1)(8+1)^2=4536.
```

The table has exactly six order-nine classes with that centralizer order,
positions 7--12 (`9a`--`9f`).  Every one has nonzero ordinary-character support
in each of blocks 2, 3, and 4.  The reviewed Theorem 3.5 support criterion
therefore places `x` in a conjugate defect group for each such block.  Since
each defect group has order nine, `<x>` itself is a representative after
conjugation.  For blocks 5--10, defect one plus central containment forces
`D=Z`.

## All block and height thresholds

For a block of defect `d`, put `exp(D/Z)=3^e`, and let an ordinary character
have height `h`.  Since `|Z|=3`, the reviewed height identity gives

```text
exp(D/Z) <= (|L:Z|/theta(1))_3
iff h <= d-1-e
iff 3^h <= |D/Z|/exp(D/Z).
```

The sole frozen run audited all 82 rows:

| block(s) | observed heights | required bound | result |
|---|---|---|---|
| 1 | `0,1,3` | `h<=2` | rows 35--40 fail; the other 31 pass |
| 2--4 | all `0` | `h<=0` | all 27 pass |
| 5--10 | all `0` | `h<=0` | all 18 pass |

The six failing rows are exactly:

| table rows | block | degree | `v_3(degree)` | height | `3^h` | threshold |
|---|---:|---:|---:|---:|---:|---:|
| 35--40 | 1 | 189 | 3 | 3 | 27 | 9 |

All remaining 76 rows pass.  The checker's intentional fatal gate therefore
exited `1` after a complete 82-row audit.

## Constraint-and-conclusion matrix

| constraint id | role | bounded use/result |
|---|---|---|
| `20.115-forall-G-chi-x` | admissibility | fail for active scope: one group, one prime, and one auxiliary block condition only |
| `20.115-G-finite` | admissibility | `L=SU_3(8)` is finite, but universal coverage is absent |
| `20.115-chi-complex-irreducible` | admissibility | all audited rows are ordinary complex irreducibles, but only in one installed table |
| `20.115-x-in-G` | admissibility | the matrix `x` is used only to identify defect groups; no source-target triple is asserted |
| `20.115-character-value-nonzero` | admissibility | exact nonzero values are used only for Theorem 3.5 support, not to assert a Kourovka witness |
| `20.115-order-degree-divisibility` | target conclusion | not established or violated; failure of a sufficient block condition implies neither |

The failed universal and conclusion rows force
`active_assignment_answered: no`.

## Reproducible evidence

Frozen checker:

```text
Agents/Kourovka/problems/20.115/runs/2026-08-18-r8-su38-central-height/scratch/su38_central_height_frozen.g
SHA-256 1f0610791c3cd7f7671804123cbc42076ea38091316807ac734b85c185f89d3b
```

It was run exactly once under Lead's slot-2 lease:

```bash
/usr/bin/time -f 'ELAPSED=%e MAX_RSS_KB=%M' timeout 45s gap -q -A -r Agents/Kourovka/problems/20.115/runs/2026-08-18-r8-su38-central-height/scratch/su38_central_height_frozen.g
```

Runtime was `3.87` seconds, maximum RSS `141952` KB, and exit status `1`
was the intended response to the mathematical failures.  Complete output:

```text
Agents/Kourovka/problems/20.115/runs/2026-08-18-r8-su38-central-height/scratch/su38_central_height_frozen.out
SHA-256 2e8545a02303a51cb63261f1ead9a52af086aa3b0bd4192de070992e6b2e8768
294 lines, 14508 bytes, 82 ROW records, 76 PASS=true, 6 PASS=false
```

## What this does not establish

- It does not prove or refute the universal Kourovka divisibility assertion.
- It does not produce a triple `(G,chi,x)` with `chi(x)!=0` and failed exact
  element-order divisibility.
- It does not show that the prime-three conclusion of Proposition 3.2 is false;
  one sufficient hypothesis simply fails.
- It does not say anything about other primes or other unitary groups.
- It does not turn CTblLib data into a presentation-level proof without an
  independent replay.

## How this could be wrong

- The installed CTblLib block membership, defects, or ordinary heights could be
  wrong; a fresh Validator should replay them independently.
- The standard identification of `SU_3(8)` with the table named `3.U3(8)` could
  conceal a convention mismatch, although the exact orders and center agree.
- The central Brauer-pair containment or height identity could have been copied
  incorrectly; both are reproduced in the reviewed `q=5` verification note.
- The cyclic representatives for blocks 2--4 use the reviewed Theorem 3.5 and
  the semisimple centralizer calculation.  This does not affect the principal
  block obstruction, but it matters to the claimed complete ten-block audit.

Verified by [[Agents/Kourovka/problems/20.115/verification/2026-08-18T010454Z-su38-central-height.md]].

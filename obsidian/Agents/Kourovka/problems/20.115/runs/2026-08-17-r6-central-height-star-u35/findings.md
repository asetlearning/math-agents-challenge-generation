---
title: "Finite SU3(5) central-height 3-block bridge"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
direction: proof
strategy: R6-CENTRAL-HEIGHT-STAR-U35
outcome: PARTIAL_RESULT
active_assignment_answered: no
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/replicated
---

# Finite `SU_3(5)` central-height 3-block bridge

## Outcome

`PARTIAL_RESULT`, provisional pending independent review. For
`L=SU_3(5)=3.U3(5)`, `p=3`, and `Z=Z(L)=C3`, the frozen run reconstructs all
seven ordinary 3-blocks and supplies an explicit defect-group representative for
each. Their quotient exponents are `3,3,1,1,1,1,1`, and every one of the 40
ordinary characters passes the exact central-height threshold

```text
3^h(theta) <= |D/Z| / exp(D/Z).
```

Consequently the installed-data calculation says that every 3-block of this one
quasi-simple group satisfies the paper's sufficient Condition
`(double-dagger-star)`. This is a finite structural bridge only. It is not a
proof of the universal Kourovka target, and `active_assignment_answered: no`.

The exact source target remains: for every finite group `G`, every ordinary
irreducible complex character `chi`, and every `x in G`, exact
`chi(x) != 0` should imply the exact integer divisibility
`o(x)chi(1) | |G|`. No Brauer character, reducible character, or zero-value row
is substituted for that statement here.

## Central-height identity

For a `p`-block `B` of `L` with defect group `D`, a central `p`-subgroup
`Z <= Z(L)`, and `theta in Irr(B)` of height `h(theta)`, write
`|L|_p=p^a`, `|D|=p^d`, and `|Z|=p^z`.

Let `b` be the block idempotent in characteristic `p`. Since `Z` is central,
`C_L(Z)=L`, so the Brauer homomorphism at `Z` retains every group-basis
coefficient and `Br_Z(b)=b != 0`. Thus `(Z,b)` is a `B`-Brauer pair. Extending
it to a maximal `B`-Brauer pair shows `Z <= D`; hence
`|D/Z|=p^(d-z)`.

By the definitions of block defect and character height,

```text
theta(1)_p = p^(a-d+h(theta)).
```

It follows exactly that

```text
(|L:Z|/theta(1))_p = p^(d-z-h(theta)) = |D/Z|/p^h(theta).
```

Therefore

```text
exp(D/Z) <= (|L:Z|/theta(1))_p
```

is equivalent to

```text
p^h(theta) <= |D/Z|/exp(D/Z).
```

For the present group `|L|_3=3^3` and `|Z|=3`.

## Exact block membership and heights

The ordinary table is CTblLib `CharacterTable("3.U3(5)")`, order `378000`,
with 40 ordinary irreducible rows. The group model is GAP's standard exact
matrix group `SU(3,5)` over `GF(25)`, also of order `378000`, with center of
order three. The prior independently reviewed table-identity artifact is
`Agents/Kourovka/problems/20.115/verification/2026-08-17T223916Z-su35-direct.md`.

The sanctioned exact call `PrimeBlocks(t,3)` partitions the ordinary irreducible
rows by exact central-character congruences on 3-regular classes, then computes
defects and heights from the ordinary degrees. It gives:

```text
block = [1,1,2,1,1,1,2,2,1,3,4,5,6,7,1,1,2,2,1,1,
         1,1,1,1,2,2,1,1,2,2,3,3,4,4,5,5,6,6,7,7]
defect = [3,2,1,1,1,1,1]
height = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,
          1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
```

| block | ordinary rows | defect | heights |
|---:|---|---:|---|
| 1 | 1, 2, 4, 5, 6, 9, 15, 16, 19, 20, 21, 22, 23, 24, 27, 28 | 3 | rows 1,2,4,5,6,9 have height 0; the rest have height 1 |
| 2 | 3, 7, 8, 17, 18, 25, 26, 29, 30 | 2 | all height 0 |
| 3 | 10, 31, 32 | 1 | all height 0 |
| 4 | 11, 33, 34 | 1 | all height 0 |
| 5 | 12, 35, 36 | 1 | all height 0 |
| 6 | 13, 37, 38 | 1 | all height 0 |
| 7 | 14, 39, 40 | 1 | all height 0 |

This partitions every row 1--40 exactly once. It can also be checked directly
from the displayed degrees: with `a=3`, a character in a defect-`d` block has

```text
h(theta) = v_3(theta(1)) - (3-d).
```

The full rowwise degree/height/threshold audit is:

| block | rows | degree | height | `3^h` | threshold | result |
|---:|---|---:|---:|---:|---:|---|
| 1 | 1 | 1 | 0 | 1 | 3 | pass |
| 1 | 2 | 20 | 0 | 1 | 3 | pass |
| 1 | 4,5,6 | 28 | 0 | 1 | 3 | pass |
| 1 | 9 | 125 | 0 | 1 | 3 | pass |
| 1 | 15,16 | 21 | 1 | 3 | 3 | pass |
| 1 | 19--24 | 48 | 1 | 3 | 3 | pass |
| 1 | 27,28 | 105 | 1 | 3 | 3 | pass |
| 2 | 3,17,18 | 21 | 0 | 1 | 1 | pass |
| 2 | 7,25,26 | 84 | 0 | 1 | 1 | pass |
| 2 | 8,29,30 | 105 | 0 | 1 | 1 | pass |
| 3 | 10,31,32 | 126 | 0 | 1 | 1 | pass |
| 4 | 11,33,34 | 126 | 0 | 1 | 1 | pass |
| 5 | 12,35,36 | 126 | 0 | 1 | 1 | pass |
| 6 | 13,37,38 | 144 | 0 | 1 | 1 | pass |
| 7 | 14,39,40 | 144 | 0 | 1 | 1 | pass |

## Explicit defect-group representatives

All matrices below lie in the exact standard `SU(3,5)` model. They are copied
in GAP finite-field notation from the frozen output.

### The center

Take `Z=<z>`, where

```text
z = [ [ Z(5^2)^16, 0*Z(5), 0*Z(5) ],
      [ 0*Z(5), Z(5^2)^16, 0*Z(5) ],
      [ 0*Z(5), 0*Z(5), Z(5^2)^16 ] ].
```

The run checks `|Z|=3`.

### Block 1

Block 1 contains the trivial character, so it is the principal block. Take
the following fixed Sylow 3-subgroup `D_1`:

```text
D_1 = Group([
  [ [ Z(5^2)^8, 0*Z(5), 0*Z(5) ],
    [ 0*Z(5), Z(5^2)^8, 0*Z(5) ],
    [ 0*Z(5), 0*Z(5), Z(5^2)^8 ] ],

  [ [ Z(5^2)^20, Z(5^2)^16, Z(5)^2 ],
    [ Z(5), Z(5^2)^20, Z(5^2)^15 ],
    [ Z(5^2)^16, Z(5^2), Z(5^2)^14 ] ],

  [ [ Z(5^2)^8, Z(5)^2, Z(5^2) ],
    [ Z(5^2)^10, Z(5^2)^2, Z(5^2)^8 ],
    [ Z(5^2)^9, Z(5^2)^14, Z(5^2)^8 ] ]
]);
```

The exact checks give

```text
|D_1|=27,  Z<=D_1,  |D_1/Z|=9,  exp(D_1/Z)=3.
```

Thus the block-1 threshold is `9/3=3`.

### Block 2

Take `D_2=<z,x>`, with `z` as above and

```text
x = [ [ Z(5)^0, Z(5)^0, Z(5^2)^13 ],
      [ Z(5), Z(5)^3, Z(5^2)^20 ],
      [ Z(5^2)^5, Z(5^2)^10, Z(5)^0 ] ].
```

This is an explicit block-2 defect group, rather than merely a subgroup of the
right order:

1. The run chooses `x` in the fixed Sylow 3-subgroup, checks `o(x)=3`, and
   checks `x notin Z`.
2. The already reviewed center data say table positions 1--3 are the three
   central classes. Among the remaining table columns there is exactly one class
   of order three, position 7, named `3c` by `ClassNames`.
3. Rows 3, 7, and 8 belong to block 2 and have exact nonzero values on this
   class. By Theorem 3.5 of Malle--Navarro--Tiep, `x` lies in a conjugate `E`
   of a block-2 defect group.
4. Central `p`-subgroup containment gives `Z<=E`. The exact matrix calculation
   gives `|<Z,x>|=9`, while block 2 has defect 2 and hence `|E|=9`.
   Therefore `<Z,x>=E`.

The quotient checks are

```text
|D_2|=9,  |D_2/Z|=3,  exp(D_2/Z)=3.
```

Thus the block-2 threshold is `3/3=1`.

### Blocks 3--7

Each block has defect one, so every defect group has order three. Since every
defect group contains the central subgroup `Z` of order three, take
`D_3=...=D_7=Z`. Hence `D_i/Z=1`, its exponent is one, and the threshold is one.

The resulting block summary is:

| block | `|D|` | explicit representative | `|D/Z|` | `exp(D/Z)` | `|D/Z|/exp(D/Z)` | maximum `3^h` | result |
|---:|---:|---|---:|---:|---:|---:|---|
| 1 | 27 | fixed Sylow subgroup `D_1` | 9 | 3 | 3 | 3 | pass |
| 2 | 9 | `<Z,x>` certified via class `3c` and Theorem 3.5 | 3 | 3 | 1 | 1 | pass |
| 3 | 3 | `Z` | 1 | 1 | 1 | 1 | pass |
| 4 | 3 | `Z` | 1 | 1 | 1 | 1 | pass |
| 5 | 3 | `Z` | 1 | 1 | 1 | 1 | pass |
| 6 | 3 | `Z` | 1 | 1 | 1 | 1 | pass |
| 7 | 3 | `Z` | 1 | 1 | 1 | 1 | pass |

## Exact Proposition 3.2 consequence

Malle--Navarro--Tiep, arXiv:2605.04513v1, Proposition 3.2 says that if
`L=[H,H]` is quasi-simple, `Z(L)=Z(H)`, and all `p`-blocks of `L` satisfy
`(double-dagger-star)`, then the same primewise condition holds for the intended
characters of `H`, yielding Conjecture 2.3 at `p`.

Applied here, the finite result gives the 3-part of Condition (1.1) for every
triple with all of the following retained:

- `H` is finite and `[H,H]=L=SU_3(5)`;
- `Z(H)=Z(L)=C3`;
- `chi in Irr(H)` is faithful;
- `h in H`, `chi(h) != 0`, and `H=<L,h>`.

The conclusion is only

```text
o(h Z(H))_3 divides (|H:Z(H)|/chi(1))_3.
```

No hypothesis is dropped, and this is not the universal source conclusion.

## Frozen evidence

- Failed script, preserved unchanged:
  `scratch/central_height_gate.g`, SHA-256
  `29d9def1adadeebc51599baf5c697650d6ac5a21bc806e1bf84b853b3e0ceec4`.
- Failed transcript, preserved as `scratch/central_height_gate_r1.out`, SHA-256
  `aa856a1ea1db8116454a1725255738ed79ebfe91ab6745b49071f143a1868a68`.
- Repaired frozen script: `scratch/central_height_gate_r2.g`, SHA-256
  `711c8e8c88d3dd8414e8cb4a11898209d5555d2642d6fd1f9bd975b4cacdf301`.
  Its `diff -u` from the failed script is exactly the single Lead-authorized line
  `LoadPackage("CTblLib");`.
- Successful output:
  `Agents/Kourovka/problems/20.115/runs/2026-08-17-r6-central-height-star-u35/scratch/central_height_gate.out`
  with SHA-256
  `2b040684b4eeaae215276bfd9d6e83ef59b4bc74da904322b3784472c161c1cf`.

The successful exact once-only command, under Lead lease slot 2, was

```bash
/usr/bin/time -f 'ELAPSED=%e MAX_RSS_KB=%M' timeout 45s gap -q -A -r Agents/Kourovka/problems/20.115/runs/2026-08-17-r6-central-height-star-u35/scratch/central_height_gate_r2.g
```

It exited zero with `ELAPSED=2.57 MAX_RSS_KB=142208`. The transcript has 85
physical lines, 5115 bytes, exactly 40 `ROW=` records, seven `BLOCK=` records,
and final `ALL_HEIGHT_THRESHOLDS_PASS=true`. No patch, rerun, table expansion,
or substitute representative followed the successful invocation.

## What this does not establish

- The universal assertion for every finite group is unanswered.
- Only `L=SU_3(5)` and the prime three are covered by this bridge.
- A block-condition pass is sufficient structural evidence through Proposition
  3.2; it is not a direct ordinary-character-value proof for arbitrary groups.
- CTblLib's ordinary table and GAP's standard group constructor were not rebuilt
  from a presentation. The result is conditional on those installed exact data,
  with the table identity relying on the prior reviewed artifact.
- The general central-height derivation and all finite data remain
  `status/conjectured` until a fresh Validator reconstructs them.
- `active_assignment_answered: no`.

## How this could be wrong

- The central-p-subgroup/maximal-Brauer-pair containment step could have been
  misstated; Validator should reconstruct it from the definitions.
- The unique noncentral order-three class in the stored table might not be
  correctly identified with the chosen matrix element if the installed table or
  group-model identity is wrong.
- `PrimeBlocks` or the installed ordinary table could contain erroneous block
  data; the quotient `U3(5)` 3-modular defects `[2,1,0,0,0,0,0]` provide only a
  consistency check after adding the central defect, not an independent proof of
  every membership row.
- The Proposition 3.2 application would be invalid if any of its nearly-simple
  hypotheses were silently omitted; they are therefore listed explicitly above.

Verified by [[Agents/Kourovka/problems/20.115/verification/2026-08-17T234711Z-su35-central-height]].

---
title: "Frozen corrected manifest — PSL(2,7), all 57 order-168 groups"
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
direction: counterexample
strategy: PSL27-ORDER168-VANISHING-COLLISION
frozen_utc: 2026-08-17T14:59:27Z
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/characters, project/kourovka, status/draft]
---

# Corrected frozen run manifest

This is a distinct v2 run, not a modification or rerun of the immutable v1
lease. The sole corrected constant, `NumberSmallGroups(168)=57`, comes from the
persistent output of the one sanctioned v1 guard run. No further GAP call or
mathematical probe preceded this freeze. The target library index is now derived
from `IdGroup(PSL(2,7))` at runtime and checked only for order 168 and inclusion
in the complete range, so no unobserved index is hard-coded.

## Exact scope, coverage, and invariant

- Target: the constructed finite simple group `PSL(2,7)` of order 168.
- Complete candidate family: `SmallGroup(168,i)` for every `1 <= i <= 57`.
- Coverage guard: emit `NumberSmallGroups(168)` and abort unless it is 57.
- A class is vanishing iff some ordinary irreducible complex character has exact
  value zero there. The invariant is the set of element orders of these classes;
  multiplicities are discarded.
- A collision is a non-target SmallGroup identifier with exactly the target set.

## Frozen files and hashes

| file | SHA-256 |
|---|---|
| `Agents/Kourovka/problems/19.30/scratch/psl27-order168-vanishing-collision-v2-20260817/screen-v2.g` | `b7ab94e161ad68b32c6f8ee36656d2739f431deb66db194a374adf22a240abd7` |
| `Agents/Kourovka/problems/19.30/scratch/psl27-order168-vanishing-collision-v2-20260817/run-v2.sh` | `f11d1e5a3cbe55bd8001f3d0d0abfb75d67fe5f6732033890aa7edbd5a63fc1b` |

## Exact command and persistent outputs

Run exactly once from the vault root:

```bash
/bin/bash Agents/Kourovka/problems/19.30/scratch/psl27-order168-vanishing-collision-v2-20260817/run-v2.sh
```

The runner invokes one `/usr/bin/gap -q` process under
`/usr/bin/timeout --signal=TERM --kill-after=30s 900s`. It writes:

- `stdout.txt`
- `stderr.txt`
- `exit-status.txt`

all in this v2 directory. A timeout, nonzero exit, missing final `SUMMARY`, or
completed count other than 57 is not a bounded-negative result.

## Frozen checks and emitted evidence

1. Check and emit library coverage 57.
2. Construct `PSL(2,7)`, check size 168 and simplicity, derive its `IdGroup`,
   reconstruct that SmallGroup representative, check isomorphism, and require
   both representations to have the same exact invariant.
3. Enumerate identifiers `[168,i]` for every `i=1,...,57`.
4. For target and every candidate, persist class orders and sizes, all ordinary
   irreducible degrees and character-value rows, zero-witness indices by class,
   vanishing class indices, and the exact vanishing-order set.
5. Check for each table that class sizes and squared character degrees sum to 168.
6. For each non-target collision, require GAP's isomorphism test to return
   `fail`, materialize and print permutation generators, verify its order and
   identifier, and recompute the invariant in that permutation representation.
7. Emit `SUMMARY` only after 57/57 rows, with target identifier and set and all
   collision indices.

The run is deterministic with no randomized search.

## Resource estimate and lease request

- Heavy slots: 1; one GAP process / approximately one CPU core.
- Expected wall/CPU: under 10 minutes; hard timeout 900 seconds plus 30-second
  kill grace.
- Expected RAM: under 512 MiB; conservative ceiling 1.5 GiB.
- Requested lease: 20 minutes including inspection and release.

## Interpretation and certification

- A completed non-target collision is a prospective counterexample only after
  every canonical row and its explicit materialization are packaged and reviewed.
- A zero-collision 57/57 run is only a bounded negative for the fixed target
  `S=PSL(2,7)`, pending an independently written Validator rerun. It cannot be
  generalized to other simple groups or the universal problem.
- Validator can reconstruct a collision from either `SmallGroup(168,i)` or the
  printed permutation generators and independently recompute ordinary character
  zeros and nonisomorphism. For a negative, Validator must separately enumerate
  all 57 identifiers and compare exact sets.

## Provenance of the corrected count

The v1 persistent stdout at
`Agents/Kourovka/problems/19.30/scratch/psl27-order168-vanishing-collision-20260817/stdout.txt`
has SHA-256
`d9a9d84dfd458e6b4f70372caba134731c778252037014774f3e3051d948abcc`
and records `EXPECTED 42 ACTUAL 57`; v1 completed zero group rows.

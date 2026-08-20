---
title: "Frozen manifest v3 — exact v1 logic with order-168 coverage corrected to 57"
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
direction: counterexample
strategy: PSL27-ORDER168-VANISHING-COLLISION
frozen_utc: 2026-08-17T15:03:09Z
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/characters, project/kourovka, status/draft]
---

# Frozen manifest v3

This v3 script preserves the v1 mathematical logic exactly and changes only the
sanctioned coverage constant and its matching diagnostic from 42 to 57. A direct
`diff -u` against v1 shows only: two header comments, `expectedCoverage := 57`,
the run-label suffix `V3`, and the fatal diagnostic's displayed value 57. In
particular, the frozen target guard remains `expectedTargetId := [168,42]`; the
target representation/isomorphism guards and all collision logic are unchanged.
No v3 GAP call or mathematical probe preceded this freeze.

## Complete scope and coverage

- Fixed target: `PSL(2,7)`, checked simple and of order 168.
- Complete library family: `SmallGroup(168,i)`, `1 <= i <= 57`.
- Runtime guard: `NumberSmallGroups(168)=57`, sourced from sanctioned v1 stdout.
- Exact invariant: the set, without multiplicity, of element orders of classes
  on which at least one ordinary irreducible complex character is exactly zero.
- Collision: a non-target identifier with exactly the same set as the target.

## Full files and SHA-256

| file | SHA-256 |
|---|---|
| `Agents/Kourovka/problems/19.30/scratch/psl27-order168-vanishing-collision-v3-20260817/screen-v3.g` | `bcbfe6475fda465da72a7cf4fe91d18984b659a735f52f8ded78e2ba15156b7c` |
| `Agents/Kourovka/problems/19.30/scratch/psl27-order168-vanishing-collision-v3-20260817/run-v3.sh` | `1f2e22c80e078d5974b6d3ec6819817d4a429656b02013af88e5bf98d0407179` |

## Exact command, cap, and persistent artifacts

Run exactly once from the vault root:

```bash
/bin/bash Agents/Kourovka/problems/19.30/scratch/psl27-order168-vanishing-collision-v3-20260817/run-v3.sh
```

The runner invokes one `/usr/bin/gap -q` process with
`/usr/bin/timeout --signal=TERM --kill-after=30s 900s` and writes `stdout.txt`,
`stderr.txt`, and `exit-status.txt` in this v3 directory. A timeout, nonzero exit,
missing final `SUMMARY`, or completed count other than 57 is not a bounded result.

## Full emitted checks

The script preserves v1's complete target construction, exact `[168,42]`
`IdGroup` assertion, target-to-library isomorphism check, target-representation
set cross-check, and enumeration of every library identifier. For target and each
candidate it persists class orders/sizes, all irreducible degrees and complete
character-value rows, zero-witness indices, vanishing classes, and the exact set.
It checks class-size and degree-square sums. Any collision is checked
nonisomorphic, materialized with explicit permutation generators, identified, and
recomputed in that representation. The final summary gives coverage, target ID
and set, and every collision index. There is no randomized search.

## Resources and lease

- One heavy slot, one GAP process, approximately one CPU core.
- Expected below 10 CPU/wall minutes; 900-second hard timeout plus 30-second kill
  grace.
- Expected below 512 MiB RAM; conservative ceiling 1.5 GiB.
- Requested lease duration: 20 minutes including inspection and release.

## Interpretation and certificate

A completed collision is only a prospective counterexample pending canonical-row
packaging and independent reconstruction from `SmallGroup(168,i)` or the printed
permutation generators. A zero-collision 57/57 summary is only a bounded negative
for fixed target `PSL(2,7)`, pending a separately written Validator enumeration;
it does not generalize to the universal scope.

The sanctioned v1 stdout proving the corrected coverage is
`Agents/Kourovka/problems/19.30/scratch/psl27-order168-vanishing-collision-20260817/stdout.txt`,
SHA-256 `d9a9d84dfd458e6b4f70372caba134731c778252037014774f3e3051d948abcc`.

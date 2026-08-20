---
title: "A6 order-360 vanishing-collision screen: frozen lease manifest"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/characters
  - project/kourovka
  - status/draft
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
direction: counterexample
strategy: A6-ORDER360-VANISHING-COLLISION
---

# Frozen experiment

Freeze UTC: 2026-08-17T15:47:36Z.

No GAP process and no other mathematical computation was run before this freeze.
The SmallGroups catalogue count at order 360 was not probed. Only executable
discovery, static hash checks, `bash -n`, and Python bytecode compilation were run.

## Exact coverage

The GAP script first constructs `AlternatingGroup(6)` independently, checks
`Size(target)=360` and `IsSimpleGroup(target)`, and obtains its `IdGroup`. It then
sets `numberGroups := NumberSmallGroups(360)` and visits every index
`i in [1..numberGroups]` exactly once as `SmallGroup(360,i)`. It emits one row per
index and fails closed unless the visited sequence is exactly
`[1..numberGroups]`, the target ID occurs exactly once, and that catalogue row
reproduces the independently constructed target invariant.

For each actual group `H`, the invariant is computed from
`Irr(CharacterTable(H))` and `OrdersClassRepresentatives(CharacterTable(H))`:
an order enters the set exactly when at least one ordinary irreducible character
has exact GAP value `0` at a class of that order. Multiplicities are discarded.

A row is a collision exactly when its invariant equals the independently computed
`A6` invariant and its SmallGroups index differs from `IdGroup(A6)[2]`. Since the
SmallGroups rows are pairwise nonisomorphic representatives, every emitted
collision row is a full counterexample candidate for the canonical constraint
matrix and must then be routed for independent reconstruction. Zero collision
rows would establish only this single complete order-360 catalogue partial.

## Frozen files and hashes

- `scratch/a6_order360_vanishing_collision.g`:
  `93ff606d6121ef366cd4c8b227491634574473e6bda7c9638fa7beca1752565e`
- `scratch/verify_a6_order360_output.py`:
  `612f6dfb4a654835aa23642105a293ad470b0ca93eb398c93835a7b2f4d17a14`
- `scratch/run_a6_order360_screen.sh`:
  `88a573c3c5d8a0b354b99e57a7bb3d60064522ba45ec58d978f962b242ea2489`
- `scratch/a6_order360_frozen.sha256`:
  `49eb981620fb1f03ddbaf26d56c9c86edf8755c3b809726d337594388b26157c`

The wrapper verifies the first three hashes before launch and refuses to overwrite
any pre-existing output.

## Exact leased command

Working directory: vault root.

```bash
/usr/bin/timeout --signal=TERM --kill-after=30s 960s /usr/bin/bash Agents/Kourovka/problems/19.30/runs/2026-08-16-r1-counterexample/scratch/run_a6_order360_screen.sh
```

Hard limits: 960 seconds wall for the entire wrapper; 870 CPU seconds and
2,147,483,648 bytes virtual address space for GAP. Expected use: one CPU, below
1 GiB RAM, normally below the hard timeout. Requested lease duration: 18 minutes.

Outputs, if leased and successful:

- `scratch/a6_order360_vanishing_collision.out`
- `scratch/a6_order360_vanishing_collision.verify`
- `scratch/a6_order360_vanishing_collision.out.sha256`

The Python verifier checks complete sequential row coverage, unique target ID,
target-row invariant reproduction, exact collision-flag semantics, and all summary
counts. It does not independently recompute character theory; Validator still
needs an independent implementation or hand reconstruction for any candidate.

## Active-time ledger

- Preserved tranche opened at 146/180 cumulative active minutes (34 remaining).
- First observed UTC clock during freeze work: 2026-08-17T15:43:25Z. Mandatory
  protocol, scope, safe-brief, and decision inspection occurred just before that
  snapshot; four minutes are conservatively charged for that pre-snapshot work.
- Freeze/lease-request stop: 2026-08-17T15:47:36Z. Charged tranche: 8 active
  minutes (rounded conservatively to whole minutes), cumulative 154/180, leaving
  26 active minutes. Lease waiting is uncharged.

No script will be patched after this freeze. A hash failure, nonzero exit, hard
limit, or incomplete verifier result kills this exact route and is reported to
Lead without a replacement computation.

---
title: "Frozen Validator manifest — A6 order-360 independent reconstruction"
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
frozen_utc: 2026-08-17T16:26:12Z
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/characters, project/kourovka, status/draft]
---

# Frozen Validator manifest

Only the mandatory tool/version probe, source inspection, artifact reading, and
static `bash -n`/Python bytecode compilation occurred before this freeze. No GAP
mathematical computation, raw-output verdict parser, or catalogue enumeration was
run. The submitted artifacts were inspected, including the failed wrapper path;
this checker does not reuse their computation or parser.

## Frozen files and hashes

| file | SHA-256 |
|---|---|
| `independent-a6-order360.g` | `163b03802b05e184c7d057ab288822e0e47c2447190fbc2fcc64b92ca3d94fd2` |
| `verify-independent.py` | `8bb3fb2b7924ec41e98c701f6a9b802cf7d39bc5d0e178394ef0cf6510c89109` |
| `run-independent.sh` | `3ea881c6428981fcc26ba41254ffc049c3acedd62e3541c2cb4ca502e0458464` |
| `frozen.sha256` | `23f1d0fd2fb15c2867864e3aa103dd30a9d1eed583a752518c71091f793c52cb` |

The runner checks the GAP and Python checker hashes before launch and refuses to
overwrite any output artifact.

## Independent design

The GAP checker constructs `AlternatingGroup(6)` and requires order 360,
simplicity, and `IdGroup=[360,118]`. It then requires
`NumberSmallGroups(360)=162` and visits every `SmallGroup(360,i)`, checking its
identifier.

For each concrete group it obtains `CharacterTable(group)`, but does not take the
table's representative-order vector as the invariant input. It retrieves the
actual conjugacy classes stored on that group table, takes an actual representative
of every class, and calls `Order` on those elements. It separately requires these
orders and actual class sizes to agree with the table metadata. It calls
`Irr(group)`, requires characteristic zero and the identical table/class ordering,
counts exact zeros in each complete character column, and derives the vanishing
order set from the actual representatives at precisely the positive-zero-count
positions. Degree-square and class-size sums are guarded for every group.

The Python checker has a separate data flow. It repairs only the exact single GAP
continuation in the submitted header, pins the submitted raw-output SHA-256, and
reconstructs coverage, target flags, equality flags, collision flags, and summaries
from all 162 primitive rows. It then validates every independent class-order and
zero-count vector and compares all 162 recomputed invariant rows. No submitted
summary is trusted as an oracle.

## Exact command and hard cap

Run once from the vault root, only under a current Lead lease:

```bash
/usr/bin/timeout --signal=TERM --kill-after=30s 960s /usr/bin/bash Agents/Kourovka/problems/19.30/verification/scratch/a6-order360-independent-20260817/run-independent.sh
```

The runner launches exactly one GAP process, with 870 CPU seconds and 2 GiB virtual
memory limits, then runs the frozen finite Python checker. The outer command has a
960-second wall cap plus 30-second termination grace. It persists GAP stdout,
stderr, both stage statuses, parser output, and the pre-run hash check. Any nonzero
exit, missing completion marker, schema discrepancy, target mismatch, coverage
failure, or row disagreement is not a pass.

## Resources and certification boundary

- Heavy slots: one.
- Expected CPU: one core, normally about 1–3 minutes; hard CPU cap 870 seconds.
- Expected RAM: below 1 GiB; hard virtual-memory ceiling 2 GiB.
- Requested lease duration: 18 minutes, including inspection and release.

Even a complete pass can independently replicate only the fixed target `S=A6`
against the order-360 catalogue. It cannot answer the universal active assignment;
`active_assignment_answered:no` is mandatory.

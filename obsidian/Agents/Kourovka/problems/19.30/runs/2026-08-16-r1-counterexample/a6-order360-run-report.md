---
title: "A6 order-360 vanishing-collision screen: one leased run"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/characters
  - project/kourovka
  - status/conjectured
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
direction: counterexample
strategy: A6-ORDER360-VANISHING-COLLISION
outcome: PARTIAL_RESULT_WITH_POSTPROCESSOR_FAILURE
---

# Result first

The single authorized wrapper was run exactly once. The GAP stage completed and
its fail-closed internal checks emitted `SUMMARY complete true`. Its exact complete
screen covered all 162 SmallGroups representatives of order 360. It constructed
`A6` as `AlternatingGroup(6)`, obtained `IdGroup(A6)=[360,118]`, and computed

`V(A6) = [2,3,4,5]`.

Only catalogue row 118 had this same set. Thus the raw GAP screen reports no
nonisomorphic collision:

- target rows: `[118]`
- equal-set rows: `[118]`
- collision rows: `[]`
- collision count: `0`

This is only a bounded fixed-`A6` order-360 partial. It does not answer the
universal scope.

# Execution record

Lease: compute slot 2 through 2026-08-17T16:08:35Z.

Pre-run manifest SHA-256 observed:
`49eb981620fb1f03ddbaf26d56c9c86edf8755c3b809726d337594388b26157c`.
All three contained hashes returned `OK` immediately before launch.

Exact command, run once from the vault root:

```bash
/usr/bin/timeout --signal=TERM --kill-after=30s 960s /usr/bin/bash Agents/Kourovka/problems/19.30/runs/2026-08-16-r1-counterexample/scratch/run_a6_order360_screen.sh
```

- active start / manifest recheck: 2026-08-17T15:51:37Z
- GAP-reported runtime: `56683` ms
- wrapper exit status: `1`
- GAP stage exit status: `0` (the wrapper reached the subsequent Python command)
- verifier stage exit status: `1`
- no timeout or resource-limit signal was observed
- no rerun and no live patch occurred

# Exact artifacts

Raw GAP output:
`scratch/a6_order360_vanishing_collision.out`

- size: 8371 bytes
- lines: 180
- SHA-256:
  `6142ece4f7daa7b08d330bce798fceade8e4de45a6b4a27637ff0364d051421e`

Frozen verifier stdout:
`scratch/a6_order360_vanishing_collision.verify`

- size: 0 bytes
- lines: 0
- SHA-256:
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

The wrapper did not create
`scratch/a6_order360_vanishing_collision.out.sha256`, because `set -e` stopped it
at the verifier failure. The two hashes above were observed afterward with
`sha256sum`; no artifact was changed.

# Postprocessor failure, exactly

The Python verifier rejected the header at output line 10:

```text
ValueError: unexpected row header at line 10
```

GAP wrapped the last header token across two physical lines:

```text
ROW_HEADER index size is_target_id vanishing_order_set equals_target_set colli\
sion
```

This was the only output line ending in a continuation backslash. The verifier
therefore failed before reading the mathematical rows; it did not report a
coverage or collision discrepancy. Per the lease decision, the script was not
patched and the computation was not rerun.

# Read-only inspection of the preserved output

An `awk -F '\t'` inspection of `ROW` records, performed without modifying the
output, observed:

```text
rows=162
bad_index=0
bad_size=0
target_rows= 118
equal_rows= 118
collision_rows=
ROW 118 360 true [ 2, 3, 4, 5 ] true false
```

The raw GAP summary independently says:

```text
SUMMARY row_count 162
SUMMARY target_rows [ 118 ]
SUMMARY equal_set_rows [ 118 ]
SUMMARY collision_rows [ ]
SUMMARY collision_count 0
SUMMARY complete true
SUMMARY runtime_ms 56683
```

The GAP script reaches these summaries only after checking that the visited index
list is exactly `[1..NumberSmallGroups(360)]`, that the target row is unique, and
that the target catalogue row reproduces the independently computed target set.
The preserved raw output also contains one row for every index 1 through 162 in
order, with size 360 in every row.

# Interpretation and certification boundary

My judgement is that the mathematical enumeration completed and excludes a
nonisomorphic order-360 collision with `A6` inside the complete SmallGroups
catalogue. However, the frozen wrapper as a whole exited nonzero because its
structural postprocessor was not robust to GAP's header wrapping. This note is
therefore `status/draft`, not certification. Validator should inspect the raw
output and independently reconstruct the character-table computation before this
fixed-target partial is promoted.

# Active-time ledger and slot release

- Prior cumulative active time: 154/180.
- Lease waiting from 2026-08-17T15:48:39Z to 2026-08-17T15:51:37Z: uncharged.
- Active run, inspection, and report: 2026-08-17T15:51:37Z to
  2026-08-17T15:55:00Z; charged 4 whole active minutes conservatively.
- New cumulative active time: 158/180; 22 active minutes remain.
- Slot 2 is released effective 2026-08-17T15:55:00Z.

Research is stopped pending Lead's decision. No replacement strategy or rerun has
been started.

Verified by [[Agents/Kourovka/problems/19.30/verification/2026-08-17T164155Z-a6-order360-zero-collision-v2]].

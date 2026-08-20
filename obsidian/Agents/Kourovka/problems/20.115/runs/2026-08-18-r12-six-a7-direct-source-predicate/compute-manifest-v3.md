---
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/character-tables, project/kourovka, status/draft]
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
frozen_utc: 2026-08-18T05:09:15Z
supersedes: [compute-manifest-v2.md]
---

# Definitive v3 frozen manifest — format-only `6.A7` repair

## V2 disposition

The sole v2 invocation is `FAILED_RUN_NO_RESULT`. Its inputs and outputs are
preserved untouched. V3 uses wholly new checker, runner, stdout, stderr, resource,
and TSV paths.

## Frozen v3 inputs

- Checker:
  `Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/audit_6a7_v3.g`
- Checker SHA-256:
  `63730dda6a5172cadc9d242e32c0f178480f9dfd75c17a54ae8e9436bdb9551d`
- Runner:
  `Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/run_audit_6a7_v3.sh`
- Runner SHA-256:
  `d0315748ccd3524dc4ea084d8765f1521652bd5a46a0cc17425cdb8b79c54210`
- `bash -n` passed for the v3 runner.

Exact diff against v2 checker consists only of comments, a single
`SizeScreen([4096,1000])` output-format setting, the new v3 TSV path, and a
versioned terminal sentinel. Exact runner diff consists only of v3 paths, the new
checker hash, versioned sentinel, and versioned runner-accepted label. All
mathematical computations and acceptance gates are byte-for-byte preserved.

## Exact invocation

`timeout 55s bash Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/run_audit_6a7_v3.sh`

The runner invokes GAP with `--quitonbreak` under a 45-second inner timeout and
separate `/usr/bin/time -v` output. Expected runtime is under ten seconds, expected
resources one CPU and under 250 MB RAM, requested lease duration five minutes.

## New output paths

- stdout: `Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/audit_6a7_v3.stdout`
- stderr: `Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/audit_6a7_v3.stderr`
- resource: `Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/audit_6a7_v3.resource`
- TSV: `Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/audit_6a7_v3.tsv`

All four paths were absent at `2026-08-18T05:09:15Z`.

## Preserved acceptance gates

The runner prechecks checker hash and output absence; requires zero process exit,
empty stderr, nonempty stdout/resource/TSV, no GAP diagnostics, exact table id
`6.A7`, group order 15,120, ordinary-library/characteristic-zero/perfect/
quasisimple flags, quotient `A7` of order 2,520 and central ratio/kernel order 6;
requires `IDENTITY_GATE`, `SHAPE_GATE`, `ALL_ROWS_IRREDUCIBLE`,
`FULL_ROW_ORTHOGONALITY`, and `COVERAGE_GATE` true; checks a single unwrapped
eleven-field header, exact line count, full unique Cartesian grid, summary
identities, hit consistency, and a unique v3 sentinel as the final stdout line.

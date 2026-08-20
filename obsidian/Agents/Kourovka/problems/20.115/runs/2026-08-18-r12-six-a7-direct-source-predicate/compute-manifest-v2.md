---
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/character-tables, project/kourovka, status/draft]
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
frozen_utc: 2026-08-18T04:58:58Z
supersedes: [compute-manifest.md]
---

# Definitive frozen compute manifest — exact `6.A7` audit

## Frozen inputs

- Mathematical checker:
  `Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/audit_6a7.g`
- Checker SHA-256:
  `68d94b828032836644f8863ab02bee3e243401155ac5d3ea2c0b199ce76758b6`
- Definitive runner:
  `Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/run_audit_6a7.sh`
- Runner SHA-256:
  `f6c807bb96716c7492085916f167c4ea07310f802827a533e40a3ef8f426c63f`
- `bash -n` passed for the frozen runner.

## Exact invocation

`timeout 55s bash Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/run_audit_6a7.sh`

The runner itself invokes exactly:

`/usr/bin/time -v -o <resource> timeout 45s gap --quitonbreak -q <checker> > <stdout> 2> <stderr>`

Expected runtime is under 10 seconds; outer hard timeout is 55 seconds; inner GAP
hard timeout is 45 seconds; expected resources are one CPU and under 250 MB RAM.
Requested lease duration is five minutes.

## Frozen output paths

- stdout: `Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/audit_6a7.stdout`
- stderr: `Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/audit_6a7.stderr`
- resource report: `Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/audit_6a7.resource`
- full cell TSV: `Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/audit_6a7.tsv`

All four paths were absent at `2026-08-18T04:58:58Z`. Their post-run hashes will
be recorded without mutation if and only if the runner accepts.

## Exact acceptance gates

Before invocation the runner checks the checker hash and absence of all four
outputs. It then requires shell exit zero; empty GAP stderr; nonempty stdout,
resource, and TSV outputs; and rejects GAP errors, syntax diagnostics, break-loop
markers, and every explicit false gate. It requires each of the following exact
stdout records exactly once:

- `TABLE_REQUEST` and `TABLE_IDENTIFIER` equal `6.A7`;
- library-table and ordinary-table flags true, underlying characteristic zero,
  group order `15120`, perfect-table and quasisimple-table flags true;
- quotient table `A7`, quotient order `2520`, central ratio `6`, and quotient
  kernel order `6`;
- `IDENTITY_GATE`, `SHAPE_GATE`, `ALL_ROWS_IRREDUCIBLE`,
  `FULL_ROW_ORTHOGONALITY`, and `COVERAGE_GATE` all true;
- exactly one `FINAL_STATUS` of `ZERO_HIT` or `HIT`;
- exactly one terminal line
  `TERMINAL_SENTINEL<TAB>KOUROVKA_20_115_6A7_AUDIT_COMPLETE_EXACTLY_ONCE`,
  occurring as the final stdout line.

The runner also checks integer summary identities, exact TSV header and line count,
all eleven fields, every row/class key exactly once over the full Cartesian grid,
TSV zero/nonzero/violation counts against stdout, and logical consistency between
`FINAL_STATUS` and the exact per-hit `VIOLATION` records.


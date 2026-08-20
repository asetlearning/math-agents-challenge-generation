---
title: "Kourovka 20.115 — R9 SU3(8) critical rows direct log"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
direction: counterexample
strategy: R9-SU38-CRITICAL-ROWS-DIRECT
active_assignment_answered: no
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/draft]
---

# R9 — `3.U3(8)` critical rows direct

## Active-time ledger

- `2026-08-18T01:11:23Z` — START from Lead's official cumulative active time `01:14:57`; this increment is capped at 25 active minutes. Protocol/assignment reading immediately before this recorded instant is included conservatively in the increment's final charge.

## Scope lock and source gate

- Exact active predicate: for finite `G`, ordinary complex irreducible `chi`, and `x in G`, test `chi(x) != 0 => o(x)chi(1) | |G|`.
- Authorized bounded object only: ordinary CTblLib table `3.U3(8)`, rows `35..40`, every conjugacy-class column.
- Excluded: Brauer values, floating-point zero tests, reducible characters, zero cells as witnesses, the weaker fourth-power statement, every other row/table/prime/catalogue.
- `source_transcription_checked: yes` and `active_scope_checked: yes` are inherited only from the canonical Lead/Validator source audit named in the scope record. This continuation does not reinterpret the rendered statement.
- `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`; no web search is permitted by the canonical blind-run record.

## Pre-run reviewed gates

- The required Validator note `verification/2026-08-18T010454Z-su38-central-height.md` identifies the ordinary table as `SU_3(8)=3.U3(8)`, order `16547328`, 82 ordinary rows/classes, and independently reconstructs rows `35..40` as exactly six rows of degree `189`.
- Reviewed direct scans currently recorded in the verification directory are the complete table `L4(3)`, restricted grids in `2.L4(3).2_2` and `2.L4(3).2_3`, and the complete table `3.U3(5)`. Filename/content search finds no reviewed source-predicate scan of `3.U3(8)`. Therefore this fixed table is not duplicate reviewed direct coverage.
- Before testing any row/class value, the frozen checker will assert the exact table identifier/order/ordinary/quasisimple invariants, the exact six row indices and degrees, all class-count/size/order invariants, and will emit the complete exact class-order list. No GAP invocation has occurred in this run before the freeze and lease request.

## Strategy portfolio

1. **Assigned catalogue/small-case mode (selected):** one exact 6-by-82 scan. A hit is a candidate source counterexample; a miss excludes only those 492 cells.
2. **Structured-construction mode (not authorized in R9):** no construction or neighbouring table may be started after a miss.
3. **Theoretical mode (not authorized in R9):** the auxiliary height failure is not substituted for the source predicate.
4. **Certificate plan:** freeze a GAP/CTblLib checker using exact cyclotomic equality (`value = 0`, cross-checked by `IsZero`) and exact integer remainder. Every hit must serialize row, class, class label, degree, exact class order, exact value, group order, product, remainder, and failed divisibility.

## Frozen checker and lease request

- `2026-08-18T01:15:15Z` — frozen before invocation: `scratch/su38_critical_rows_direct_frozen.g`, SHA-256 `3fe4d2f930749168e2cc87a8945e6810cdd253e2576fdd708badc8a6200a0c02`, 175 lines, 7135 bytes. The output path was absent. The file is now immutable for this one-shot run.
- Requested one Lead lease for the exact 45-second-capped GAP command recorded in the bus request; estimated CPU `<15 s`, RAM `<250 MB`, lease duration 5 minutes. Waiting time is uncharged.

## Leased invocation

- Lead granted slot 1 from `2026-08-18T01:17:40Z` through `01:22:40Z`, binding the exact frozen hash and command. The checker was not patched.
- Invoked exactly once:

```bash
/usr/bin/time -f 'ELAPSED=%e MAX_RSS_KB=%M' timeout 45s gap -q -A -r Agents/Kourovka/problems/20.115/runs/2026-08-18-r9-su38-critical-rows-direct/scratch/su38_critical_rows_direct_frozen.g
```

- Exit status `0`; `ELAPSED=1.61 MAX_RSS_KB=141952`. Slot 1 was released at `2026-08-18T01:18:47Z` by bus REPORT.
- Output SHA-256 `71a042d39e3d732ac4ab98686cb15b449eb3dbc08dc47bb17ab79b98af9f51e5`, 604 lines, 78865 bytes. Checker hash remained unchanged.
- Exact runtime gates: `IDENTIFIER=3.U3(8)`, construction text `SU(3,8)`, ordinary/perfect/quasisimple all true, group order `16547328`, 82 rows/classes, rows `35..40`, six degrees `189`, complete exact class-order vector emitted, prior-direct-scan flag false.
- Terminal summary: `CELLS=492`, `NONZERO=198`, `ZERO=294`, `HITS=0`, empty hit-record list, intended end marker present.
- Static output audit: all six rows have 82 cell records, every class has six; no degree/group/class-order/boolean mismatch; zero nonzero-value violations. There are 162 raw nondivisible cells, all exact zero values (orders 7: 18 cells; 21: 36; 63: 108).

## Outcome

`PARTIAL_RESULT`: the six critical degree-189 rows are a bounded exact miss for the source predicate. The auxiliary height obstruction does not produce a source witness. No other row, table, prime, or catalogue was tested. `active_assignment_answered: no`.

Full outcome: `Agents/Kourovka/problems/20.115/runs/2026-08-18-r9-su38-critical-rows-direct/outcome.md`.

## Active-time stop

- `2026-08-18T01:21:10Z` — STOP. Charged increment `00:12:22`, including a conservative `00:05:00` for mandatory reading before the first timestamp and excluding lease-wait time `01:15:15Z--01:17:40Z`. Official cumulative active time is now `01:27:19/03:00:00`. The assigned R9 experiment is complete and no expansion is authorized.

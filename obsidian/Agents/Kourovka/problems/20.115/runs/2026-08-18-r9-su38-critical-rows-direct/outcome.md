---
title: "Kourovka 20.115 — R9 SU3(8) critical rows direct outcome"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
direction: counterexample
strategy: R9-SU38-CRITICAL-ROWS-DIRECT
outcome: PARTIAL_RESULT
claim: "In the ordinary CTblLib table 3.U3(8), rows 35--40 have degree 189 and, over all 82 class columns, their 198 exact nonzero values yield zero failures of o(x)chi(1) dividing 16547328."
active_assignment_answered: no
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/conjectured]
---

# Outcome — bounded six-row miss

## Active target

Scope: `20.115/nonzero-character-order-divisibility`, assignment revision 1.

Target: for every finite group `G`, ordinary complex irreducible character `chi`, and `x in G`, exact nonvanishing `chi(x) != 0` should imply `o(x)chi(1) | |G|`.

## Exact bounded result

One Lead-leased invocation of the pre-frozen GAP 4.12.1 / CTblLib 1.3.7 checker completed normally. It evaluated precisely ordinary rows `35,36,37,38,39,40` of `CharacterTable("3.U3(8)")` against all 82 conjugacy classes:

```text
CELLS=492
NONZERO=198
ZERO=294
HITS=0
```

Thus this fixed six-row domain supplies no source counterexample. This is only a bounded `PARTIAL_RESULT`; `active_assignment_answered: no`.

## Identity, rows, and class orders

Before evaluating any value, the checker asserted and emitted:

```text
IDENTIFIER=3.U3(8)
INFO_TEXT=origin: ATLAS of finite groups, tests: 1.o.r., | constructions: SU(3,8)
ORDINARY=true
PERFECT=true
QUASISIMPLE=true
GROUP_ORDER=16547328
NUMBER_ROWS=82
NUMBER_CLASSES=82
CENTRE_POSITIONS=[1,2,3]
CENTRE_ORDER=3
AUTHORIZED_ROWS=[35,36,37,38,39,40]
AUTHORIZED_DEGREES=[189,189,189,189,189,189]
```

The exact class-order vector, indexed 1 through 82, is:

```text
[1,3,3,2,6,6,9,9,9,9,9,9,3,4,12,12,4,12,12,4,12,12,
 18,18,18,18,18,18,7,21,21,7,21,21,7,21,21,9,9,9,9,9,9,
 9,9,9,19,57,57,19,57,57,19,57,57,19,57,57,19,57,57,19,
 57,57,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,
 63,63]
```

All orders were asserted to be positive integer divisors of `|G|`; all class sizes sum to `|G|`, and the ordinary degree squares sum to `|G|`. The required Validator note independently identifies `SU_3(8)=3.U3(8)` and the six degree-189 row indices.

The reviewed source-predicate scans in this problem's verification directory concern `L4(3)`, restricted grids in `2.L4(3).2_2` and `2.L4(3).2_3`, and `3.U3(5)`. The frozen gate recorded `TARGET_PREVIOUSLY_DIRECT_SCANNED=false`; no reviewed `3.U3(8)` direct scan was found before this run.

## Exact predicate and arithmetic

Every authorized table entry first passed `IsCyc(value)`. Nonvanishing was decided by exact cyclotomic equality `value = 0`, with every result cross-checked against GAP's exact `IsZero(value)`. Divisibility was decided by the exact integer remainder

```text
16547328 mod (189 * class_order).
```

Since `16547328 = 189 * 87552`, the only selected cells with failed raw divisibility had class orders `7`, `21`, or `63`. The frozen output and a static record audit give:

```text
nondivisible_cells=162
nonzero_nondivisible=0
zero_nondivisible=162
by_order=7:18,21:36,63:108
```

So every potentially useful arithmetic failure is excluded by the source hypothesis because its exact character value is zero. All 198 exact nonzero cells have remainder zero.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | bounded evidence | result |
|---|---|---|---|---|
| `20.115-forall-G-chi-x` | admissibility | every admissible triple | one table, six rows, all 82 classes | not established universally |
| `20.115-G-finite` | admissibility | finite `G` | ordinary Atlas-origin `3.U3(8)=SU_3(8)` table, order `16547328` | pass for bounded object |
| `20.115-chi-complex-irreducible` | admissibility | ordinary irreducible complex `chi` | six exact `Irr(table)` rows, each degree `189`; ordinary-table and cyclotomic gates pass | pass for six rows |
| `20.115-x-in-G` | admissibility | class represents elements of exact order `o(x)` | all 82 table class columns and exact stored class orders | pass for bounded columns |
| `20.115-character-value-nonzero` | admissibility | exact `chi(x) != 0` | exact equality/`IsZero` agreement at all 492 cells | pass for exactly 198 cells; 294 zeros excluded |
| `20.115-order-degree-divisibility` | target conclusion | `o(x)chi(1) | |G|` | exact remainder zero for all 198 nonzero cells | no violation in bounded domain; universal conclusion unanswered |

## Reproducible evidence

Frozen checker:

```text
Agents/Kourovka/problems/20.115/runs/2026-08-18-r9-su38-critical-rows-direct/scratch/su38_critical_rows_direct_frozen.g
SHA-256 3fe4d2f930749168e2cc87a8945e6810cdd253e2576fdd708badc8a6200a0c02
175 lines, 7135 bytes
```

Complete exact output:

```text
Agents/Kourovka/problems/20.115/runs/2026-08-18-r9-su38-critical-rows-direct/scratch/su38_critical_rows_direct_frozen.out
SHA-256 71a042d39e3d732ac4ab98686cb15b449eb3dbc08dc47bb17ab79b98af9f51e5
604 lines, 78865 bytes
ELAPSED=1.61 MAX_RSS_KB=141952
```

The script hash was recorded before the output path existed. Lead granted slot 1 for exactly one invocation, and the slot was released immediately after exit status 0.

A static tab-record audit of the immutable output returned:

```text
classes=82 cells=492 nonzero=198 zero=294 hits=0 violations=0
baddegree=0 badgroup=0 badorder=0 badboolean=0
rows=35:82,36:82,37:82,38:82,39:82,40:82 class_cell_range=6..6
```

## What this does not establish

- It does not test the other 76 ordinary rows of `3.U3(8)`.
- It does not test another character table, group, prime, or catalogue family.
- It does not prove the universal Kourovka statement.
- It does not turn the auxiliary central-height failure into a source-predicate failure.
- Both identity/value claims ultimately use the installed CTblLib data; the Atlas table was not reconstructed from a presentation.

## How this could be wrong

- The installed CTblLib table could differ from an independently reconstructed Atlas table, although the fixed object and version are explicit.
- CTblLib's row/class ordering is version-specific; the exact version, identifiers, indices, labels, degrees, orders, and complete values are frozen in the output.
- A serialization/parser error could miscount records; the GAP summary and the independent static coverage/arithmetic audit agree, and the intended end marker is present.


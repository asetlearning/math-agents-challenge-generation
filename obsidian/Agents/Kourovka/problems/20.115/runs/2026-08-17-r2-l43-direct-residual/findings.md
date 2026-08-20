---
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
outcome: PARTIAL_RESULT
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/conjectured]
---

# One-table exact coverage: `L4(3)`

## Active target

For every finite group `G`, ordinary complex `chi in Irr(G)`, and `x in G`, exact nonvanishing `chi(x) != 0` should imply `o(x)chi(1) | |G|`.

## Bounded result

The cited 2026 paper does not already cover the cross-characteristic case `ell=2`, `n=4`, `q=3`: its general cross-characteristic theorems require `ell>2`, and its explicit prime-2 consequence for `SL_n(epsilon q)` requires `n` odd or `q` even. Thus the assigned residual table was not a duplicate.

In GAP 4.12.1 with CTblLib 1.3.7, the ordinary table identifier `L4(3)` has order `6065280`, 29 irreducible rows, and 29 conjugacy classes. CTblLib flags it as a simple character table; its only singleton class is the identity. Its order equals the standard formula for `PSL_4(3)`, so this is the centerless simple target table.

The frozen scan evaluated all `29*29=841` row/class pairs. It found 495 exact nonzero cyclotomic values and zero pairs for which `class_order * chi(1)` fails to divide `6065280`.

## Exact evidence

- Script: `Agents/Kourovka/problems/20.115/runs/2026-08-17-r2-l43-direct-residual/scratch/l43_exact_scan.g`
- Script SHA-256: `89ca00b164b290e1f8dd61394677422f37f1e987b4a015b7f3562ab3053c3f95`
- Full TSV output: `Agents/Kourovka/problems/20.115/runs/2026-08-17-r2-l43-direct-residual/scratch/l43_exact_scan.tsv`
- Output SHA-256: `245ebfdfb2f722af6dbbaf673db2c8d1c098f7f208df2bd915f33e65457fb44f`
- Summary: `pairs=841`, `nonzero_pairs=495`, `violations=0`.
- Structural audit: sequential pair indices and the complete 29-by-29 row/class grid both have zero errors.

## What this does not establish

This is exhaustive only for the one named ordinary table `L4(3)`. It is not evidence about extension tables, other finite groups, modular characters, or the universal assertion. Zero hits do not close scope `20.115/nonzero-character-order-divisibility`.

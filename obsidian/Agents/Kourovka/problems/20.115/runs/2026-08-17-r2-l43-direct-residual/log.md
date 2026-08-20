---
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
direction: counterexample
run: 2026-08-17-r2-l43-direct-residual
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/draft]
---

# Cycle 2 — direct residual screen of `L4(3)`

## Active-time ledger

- `2026-08-17T19:31:01Z`: active work started at cumulative minute 5; this increment is capped at 20 active minutes.

## Scope lock

- Exact target: for finite `G`, ordinary complex `chi in Irr(G)`, and `x in G`, test the implication `chi(x) != 0 => o(x)chi(1) | |G|`.
- The only permitted object in this increment is the ordinary CTblLib table `L4(3)`.
- Exact cyclotomic equality and integer divisibility only. No floating values, modular characters, extension tables, other groups, or block-condition substitutes.

## Paper-coverage duplicate gate

Primary source inspected: Malle--Navarro--Tiep, *Zeros of characters and orders of elements in finite groups*, arXiv:2605.04513v1, local SHA-256 `a2825c5bfed0c8d340893b3b8bcfd62f89b1e94c7d170e13f4df34198357e96f`.

- Theorem C(3) and Theorem 4.3 require the cross-characteristic prime to satisfy `ell > 2`; they do not cover `ell=2`.
- The defining-characteristic result applies to prime 3 for `PSL_4(3)`, not to the residual prime 2.
- After Proposition 4.17 the paper explicitly deduces the `ell=2` case for quasi-simple `SL_n(epsilon q)` only when `n` is odd or `q` is even. Here `n=4` is even and `q=3` is odd.
- Proposition 4.16 assumes `2 < ell`, and the alternating/Suzuki/Ree/sporadic cases of Theorem D do not contain `PSL_4(3)`.
- The standard type coincidence `A_3(3)=D_3(3)` (also recorded by CTblLib for `L4(3)`) does not evade the prime hypotheses: the paper has no all-prime `D_3(3)` theorem that covers this `ell=2` case.

Result of the gate: this exact `ell=2`, `n=4`, `q=3` simple-quotient case is not among the paper's stated proved cases. The assigned one-table direct screen is therefore nonduplicate and may proceed.

## Frozen computation

The deterministic script was frozen before its first table-predicate execution at `scratch/l43_exact_scan.g`. It requests exactly `CharacterTable("L4(3)")`, records GAP/CTblLib versions and table metadata, and emits one TSV `PAIR` record for every ordinary irreducible row/class pair. `nonzero` is the exact GAP equality test `value <> 0`; `divides_group_order` is the integer test `Size(tbl) mod (class_order * chi(1)) = 0`.

Frozen script SHA-256: `89ca00b164b290e1f8dd61394677422f37f1e987b4a015b7f3562ab3053c3f95`.

## Exact run and observed output

Command (55-second hard cap, comfortably below the heavy-compute threshold):

```text
timeout 55s gap -q -b Agents/Kourovka/problems/20.115/runs/2026-08-17-r2-l43-direct-residual/scratch/l43_exact_scan.g > Agents/Kourovka/problems/20.115/runs/2026-08-17-r2-l43-direct-residual/scratch/l43_exact_scan.tsv
```

Observed exit code: `0`. The combined checksum-and-run tool call completed in 2.9 seconds wall time. Output SHA-256: `245ebfdfb2f722af6dbbaf673db2c8d1c098f7f208df2bd915f33e65457fb44f` (870 lines, 41,332 bytes).

Metadata observed verbatim in the output:

```text
SOFTWARE GAP 4.12.1
SOFTWARE CTblLib 1.3.7
TABLE_REQUEST L4(3)
TABLE_IDENTIFIER L4(3)
TABLE_IS_ORDINARY true
TABLE_IS_SIMPLE_CHARACTER_TABLE true
TABLE_ORDER 6065280
EXPECTED_PSL4_3_ORDER 6065280
ORDER_MATCH true
CENTER_CLASS_POSITIONS [ 1 ]
CENTER_ORDER 1
ROW_COUNT 29
CLASS_COUNT 29
IRR_ORTHONORMAL true
SUMMARY pairs 841 nonzero_pairs 495 violations 0
```

The order check uses the independent formula
`|PSL_4(3)| = 3^6(3^2-1)(3^3-1)(3^4-1)/gcd(4,3-1) = 6065280`.
CTblLib's Atlas identifier `L4(3)` denotes the type-`A_3(3)` simple group, i.e. `PSL_4(3)` (equivalently the type-`D_3(3)` simple group). The library flags this table simple, and the singleton-class positions are exactly `[1]`, so the represented simple group is centerless.

The complete TSV output contains all 841 pair records, including each exact cyclotomic character value. A separate structural parse of that file observed:

```text
AUDIT pairs=841 nonzero=495 violations=0 bad_pair_sequence=0 bad_row_class_grid=0
```

## Bounded result

For every ordinary irreducible character row and every conjugacy class in the exact CTblLib table `L4(3)`, each exact nonzero character value passes `o(C)chi(1) | 6065280`. There is no counterexample candidate in this table.

This proves only zero-hit bounded coverage of the one ordinary table `L4(3)=PSL_4(3)`. It does not prove the universal Kourovka assertion, cover any extension table or other group, validate a sufficient block condition, or exclude a counterexample elsewhere.

## Active-time stop

- `2026-08-17T19:36:27Z`: stopped research and entered `awaiting_lead`.
- This increment used exactly `00:05:26` active time, from `19:31:01Z` through `19:36:27Z`.
- Cumulative active time advanced from `00:05:00` to `00:10:26`.
- Of the assigned 20-minute increment, `00:14:34` is returned unused.

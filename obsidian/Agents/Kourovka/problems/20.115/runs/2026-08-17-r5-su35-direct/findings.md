---
title: "Exact zero-hit scan of the ordinary table 3.U3(5)"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
direction: counterexample
outcome: PARTIAL_RESULT
strategy: R5-SU35-DIRECT
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/replicated
---

# Exact zero-hit scan of `3.U3(5)`

## Active target

For every finite group `G`, ordinary irreducible complex character `chi`, and
`x in G`, exact `chi(x) != 0` should imply the integer divisibility
`o(x)chi(1) | |G|`.

## Bounded result

The complete stored ordinary character table
`CharacterTable("3.U3(5)")` contains 40 irreducible rows and 40 conjugacy
classes. Among all 1600 row/class pairs, exactly 987 character values are
nonzero in exact GAP cyclotomic arithmetic. None of those 987 pairs violates
`o(x)chi(1) | 378000`.

This is a zero-hit bounded result for one table, not a counterexample and not a
proof of the universal target. Outcome: `PARTIAL_RESULT`; the named
`R5-SU35-DIRECT` experiment is complete.

## Paper nonduplication gate

The fixed May-2026 artifact is Malle--Navarro--Tiep, _Zeros of characters and
orders of elements in finite groups_, `/tmp/2605.04513v1.pdf`, SHA-256
`a2825c5bfed0c8d340893b3b8bcfd62f89b1e94c7d170e13f4df34198357e96f`.

For `SU_3(5)`, `n=3`, `q=5`, and `epsilon=-1`, hence
`3 | gcd(n,q-epsilon)=gcd(3,6)`. Corollary 4.2 handles the defining prime 5;
Theorem 4.3 handles the other odd cross-characteristic primes only when they
do not divide this gcd; and the consequence after Proposition 4.17 handles
prime 2 when `n` is odd. Proposition 4.16 is linear, while its following
paragraph explicitly leaves the analogous `SU_n(q)` restriction/extension
control unavailable. Proposition 4.17 treats `GU_n(q)`, not this simply
connected `SU_n(q)` table. Thus prime 3 is genuinely residual in the paper's
coverage map.

## Exact table and group identity

Static CTblLib 1.3.7 metadata identifies `3.U3(5)` by Lie type `2A`, isogeny
type `sc`, rank parameter `l=2`, and field parameter `q=5`; its construction
text says `SU(3,5)`. The size record is 378000 and the quasisimple record is
`[[3,1],"U3(5)"]`, meaning centre `C3` and simple factor `U3(5)`.

The frozen GAP run independently printed:

- identifier `3.U3(5)`;
- ordinary, perfect, and quasisimple status all `true`;
- order `378000 = 5^3(5^2-1)(5^3+1)`;
- centre positions `[1,2,3]`, orders `[1,3,3]`, and centre size 3;
- central quotient order 126000;
- 40 rows and 40 classes;
- degree-square sum 378000;
- every stored value satisfying exact GAP filter `IsCyc`.

This distinguishes the table from the simple quotient `U3(5)` and the
adjoint/diagonal extension `U3(5).3`.

## Complete class orders and row degrees

In table order, class labels and exact representative orders are:

```text
1A_0:1, 1A_1:3, 1A_2:3, 2A_0:2, 2A_1:6, 2A_2:6, 3A_0:3,
4A_0:4, 4A_1:12, 4A_2:12, 5A_0:5, 5A_1:15, 5A_2:15,
5B_0:5, 5B_1:15, 5B_2:15, 5C_0:5, 5C_1:15, 5C_2:15,
5D_0:5, 5D_1:15, 5D_2:15, 6A_0:6, 6A_1:6, 6A_2:6,
7A_0:7, 7A_1:21, 7A_2:21, 7B_0:7, 7B_1:21, 7B_2:21,
8A_0:8, 8A_1:24, 8A_2:24, 8B_0:8, 8B_1:24, 8B_2:24,
10A_0:10, 10A_1:30, 10A_2:30.
```

The 40 irreducible row degrees, in table order, are:

```text
1, 20, 21, 28, 28, 28, 84, 105, 125, 126, 126, 126, 144, 144,
21, 21, 21, 21, 48, 48, 48, 48, 48, 48, 84, 84, 105, 105, 105,
105, 126, 126, 126, 126, 126, 126, 144, 144, 144, 144.
```

The raw artifact also records every class size and every exact cyclotomic
character value.

## Frozen computation and exact semantics

Command, invoked exactly once under Lead lease slot 2:

```bash
timeout 30s gap -q -A -r Agents/Kourovka/problems/20.115/runs/2026-08-17-r5-su35-direct/scratch/su35_exact_scan.g
```

The process exited 0 in 3.16 wall seconds using GAP 4.12.1 and CTblLib 1.3.7.
The inner test for each row `i` and class `j` was exactly:

```text
value       := Irr(tbl)[i][j]
nonzero     := value <> 0
product     := Irr(tbl)[i][1] * OrdersClassRepresentatives(tbl)[j]
remainder   := Size(tbl) mod product
violation   := nonzero and remainder <> 0
```

No floating-point conversion, modular character, block inequality, or
sufficient-condition surrogate was used.

Script SHA-256:
`47b67f1ee3a23f7e954c5dbbe7a35d2d10671e5743ba1e80a2ddf9c8effffeaa`.

Raw output SHA-256:
`313d8c9fcabc541ccf1ca88cf724241a4f1f1404a940e7b4caa70ce1b84bcfce`.

The raw output has 3315 physical lines and 198904 bytes. GAP line wrapping
can split one logical `CELL` record across physical lines, but all exact values
and flags are preserved. A read-only shell audit counted 40 `CLASS` starts, 40
`ROW` starts, 1600 `CELL` starts, 987 literal `nonzero=true` tokens, and zero
literal `violation=true` tokens. The program summary is
`TOTAL_PAIRS=1600`, `NONZERO_PAIRS=987`, `VIOLATIONS=0`.

## What this establishes

Assuming the named CTblLib table faithfully represents `SU_3(5)`, every
ordinary irreducible character/class pair in this complete table satisfies the
source implication. Consequently this particular simply connected group is
excluded as a source counterexample.

## What this does not establish

- It does not prove the assertion for any other finite group.
- It does not scan `U3(5)`, `U3(5).2`, `U3(5).3`, or any other table.
- It does not settle the paper's unitary prime-three family or extend its
  Lusztig-restriction argument.
- It does not close revision 1; `active_assignment_answered: no`.
- It remains a `status/conjectured` bounded computational result until fresh
Validator reconstruction.

Verified by [[Agents/Kourovka/problems/20.115/verification/2026-08-17T223916Z-su35-direct]].

## Fresh validation plan

Validator can hash-check the two artifacts, independently reconstruct the
table identity and central data, rerun an independently written exact 40-by-40
scan under a fresh lease, and compare both the 1600-cell nonzero bit pattern
and the `1600/987/0` totals. No prospective hit certificate exists because the
violation set is empty.

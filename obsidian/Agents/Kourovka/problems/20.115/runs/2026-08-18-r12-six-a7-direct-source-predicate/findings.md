---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-tables
  - project/kourovka
  - status/conjectured
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
direction: counterexample
cycle: 12
outcome: PARTIAL_RESULT
---

# Candidate bounded partial: exact ordinary table `6.A7`

## Active target

Scope: `20.115/nonzero-character-order-divisibility`  
Assignment revision: 1

Target statement: For every finite group `G`, every complex irreducible character
`chi` of `G`, and every `x in G`, if `chi(x)` is nonzero then
`o(x) chi(1)` divides `|G|`.

## Candidate partial result

The installed GAP Character Table Library ordinary table with exact identifier
`6.A7` has no counterexample to the source predicate. Across its complete
`40 x 40 = 1600` irreducible-row/class grid, exact cyclotomic equality found
1,044 nonzero values and 556 zeros. For every one of the 1,044 nonzero cells,
the exact integer `class_order * character_degree` divides group order 15,120.
There are zero violations.

This is a one-table bounded screen only. It neither proves the universal statement
nor supports any inference about another cover, group, or catalogue.

## Exact table identity and completeness

- Software: GAP 4.12.1; CTblLib 1.3.7.
- Requested and returned table identifier: `6.A7`.
- CTblLib `InfoText`: `origin: ATLAS of finite groups, tests: 1.o.r., pow[2,3,5,7]`.
- `IsLibraryCharacterTableRep = true`, `IsOrdinaryTable = true`, and underlying
  characteristic `0`.
- Group order: `15120 = 6 * 2520`.
- The table reports perfect and quasisimple. Its stored fusion has quotient table
  `A7` of order 2,520; the six quotient-kernel classes are exactly the six central
  classes, with total kernel order 6.
- Class count and `Irr` row count are both 40. Every row has 40 entries, every row
  satisfies `IsIrreducibleCharacter = true`, and the full `40 x 40` scalar-product
  matrix is the identity.
- The 40 row degrees, in installed order, are:
  `[1,6,10,10,14,14,15,21,35,4,4,14,14,20,20,36,6,6,15,15,15,15,21,21,21,21,24,24,24,24,6,6,6,6,24,24,24,24,36,36]`.
- The complete installed class-name/order list is:
  `1a/1, 6a/6, 3a/3, 2a/2, 3b/3, 6b/6, 4a/4, 12a/12, 12b/12, 3c/3,
  6c/6, 3d/3, 6d/6, 8a/8, 24a/24, 24b/24, 8b/8, 24c/24, 24d/24, 5a/5,
  30a/30, 15a/15, 10a/10, 15b/15, 30b/30, 12c/12, 12d/12, 12e/12,
  7a/7, 42a/42, 21a/21, 14a/14, 21b/21, 42b/42, 7b/7, 42c/42,
  21c/21, 14b/14, 21d/21, 42d/42`.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | candidate value / audit use | evidence | result |
|---|---|---|---|---|---|
| `20.115-forall-G-chi-x` | admissibility | Universal triples satisfying the remaining rows | Exhaustive only for the fixed group/table `6.A7`, all 40 irreducible rows, all 40 classes | v2 stdout plus hash-pinned 1,600-record TSV audit | `partial-pass`; universal domain not covered |
| `20.115-G-finite` | admissibility | `G` finite | CTblLib ordinary table `6.A7`, order 15,120 | `IDENTITY_GATE=true`, exact identifier/order/central quotient records | pass for bounded domain |
| `20.115-chi-complex-irreducible` | admissibility | `chi` ordinary complex irreducible | All 40 CTblLib `Irr` rows; ordinary characteristic 0; per-row irreducibility true; full orthogonality true | stdout identity/row gates and full row list | pass |
| `20.115-x-in-G` | admissibility | `x in G`, with exact element order | All 40 conjugacy classes, using the complete `OrdersClassRepresentatives` list printed above | stdout class list and each TSV row/class record | pass |
| `20.115-character-value-nonzero` | admissibility | Exact `chi(x) != 0` | GAP cyclotomic comparison `val <> 0`; 1,044 cells true and 556 false; the full exact values are preserved in the TSV | checker source, stdout counts, TSV and posthoc verifier | pass for 1,044 tested predicate cells |
| `20.115-order-degree-divisibility` | target_conclusion | `o(x)chi(1) | |G|` | Recomputed as exact remainder `15120 mod (class_order*degree)` for every cell; all 1,044 nonzero cells have remainder zero | TSV products/remainders/divides flags; posthoc arithmetic audit | holds throughout bounded domain; not violated |

## Provenance, including the rejected wrapper

The sole leased GAP invocation was exactly:

`timeout 55s bash Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/run_audit_6a7.sh`

GAP itself exited zero after 5.41 seconds (user 1.28 s, system 0.42 s, maximum RSS
142,080 KB), with empty stderr and all mathematical gates true. The frozen wrapper
nevertheless exited one with `RUNNER_REJECTED: TSV line count mismatch`. Lead
therefore classified the invocation initially as `FAILED_RUN_NO_RESULT`.

Byte-level diagnosis established that the sole defect is GAP line wrapping of the
109-character TSV header: physical line 1 ends `group_orde\\` and physical line 2
is `r<TAB>remainder<TAB>divides`. The two lines reconstruct the exact frozen header.
All 1,600 data records begin at physical line 3 and have exactly eleven fields.

Lead authorized the immutable, hash-pinned posthoc audit as a candidate bounded
partial for fresh review, while retaining the wrapper rejection in provenance. The
posthoc verifier does not rerun GAP or modify the artifacts. It pins all four hashes,
reconstructs only the wrapped header, and checks the entire Cartesian grid, exact
printed zero flags, row degrees, class names/orders, products, remainders,
divisibility flags, and counts.

Final verifier transcript:

```text
POSTHOC_DATA_ROWS	1600
POSTHOC_EXACT_NONZERO	1044
POSTHOC_ZEROS	556
POSTHOC_VIOLATIONS	0
POSTHOC_ACCEPTED	HEADER_WRAP_ONLY	IMMUTABLE_HASHES_PINNED
```

No v3 GAP run occurred. Draft v3 files created under the earlier, subsequently
superseded formatting-rerun decision are not evidence.

## Reproducibility hashes

- Frozen GAP checker: `audit_6a7.g`, SHA-256
  `68d94b828032836644f8863ab02bee3e243401155ac5d3ea2c0b199ce76758b6`.
- Frozen runner: `run_audit_6a7.sh`, SHA-256
  `f6c807bb96716c7492085916f167c4ea07310f802827a533e40a3ef8f426c63f`.
- stdout: SHA-256
  `b8ee32b2473278bb98dc1bbc23908ee4ea605d2c66730f339e788a0e1e8cdbcd`.
- empty stderr: SHA-256
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- resource report: SHA-256
  `9099971d0629d0d6ae1de027f789219b12cd313b4f4ad66ff78c67844c5e8598`.
- full immutable TSV: SHA-256
  `d592aee3277c3b870daec04c5d10ef49b98b39a555bd8736fed0019111284d31`.
- Posthoc verifier: SHA-256
  `02412b23fa4ff5c17bfba4dbc681df8081c11dd676126af1c078e190e6ba8186`.
- Persisted posthoc transcript: SHA-256
  `3899c0a4c7eacecca03eb16470431d9f57221169b6d198c2d8cec0df8588616c`;
  its stderr is empty with the standard empty-file SHA-256.

All referenced artifacts are in this run directory.

## What this does not establish

- It does not prove the universal assertion in Problem 20.115.
- It does not find a counterexample.
- It says nothing about `2.A7`, `3.A7`, another group, or a character-table
  catalogue.
- It does not reconstruct an explicit group representation independently of the
  authoritative installed table.
- It is not replicated until a fresh Validator independently reruns or reconstructs
  the table and certificate.

## How this could be wrong

1. The installed CTblLib table or stored `6.A7 -> A7` fusion could be incorrect;
   independent library/table reconstruction is needed for certification.
2. The posthoc verifier trusts the exact values/zero flags emitted by GAP; it checks
   their internal consistency but does not independently re-evaluate cyclotomic
   equality.
3. A subtle table-order/class-order library defect would propagate to both stdout
   and TSV, despite the class-size and central-quotient consistency gates.
4. The rejected wrapper is not silently repaired: Validator must explicitly accept
   or reject the two-line-header salvage route.

## Outcome

`PARTIAL_RESULT`: the strategy exhaustively screens exactly one certified installed
ordinary table and finds zero hits. The assigned `SIX-A7-DIRECT-SOURCE-PREDICATE`
strategy is complete at its authorized boundary; await Lead after fresh validation.

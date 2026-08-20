---
title: "Kourovka 20.115 — bounded graph-cover extension coverage"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
direction: counterexample
outcome: PARTIAL_RESULT
active_assignment_answered: no
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/conjectured
---

# Bounded graph-cover extension coverage

## Active target

Scope: `20.115/nonzero-character-order-divisibility`, assignment revision 1.

Target statement: For every finite group `G`, every ordinary irreducible complex character `chi` of `G`, and every `x in G`, if the exact value `chi(x)` is nonzero then `o(x)chi(1)` divides `|G|`.

## Partial result

In each of the two ordinary CTblLib `1.3.7` tables

- `2.L4(3).2_2`, and
- `2.L4(3).2_3`,

the stored fusion from `2.L4(3)` identifies the derived-subgroup classes and hence the outer coset. Among every exact faithful ordinary irreducible row and every outer class, no nonzero value violates the direct source divisibility `Order(C)*chi(1) | 24261120`.

This is a zero-hit finite coverage result, not a proof or counterexample for the universal scope.

## Structural and nonduplication gates

The exact GAP certificate establishes for both target tables:

- ordinary characteristic-zero character tables with exact cyclotomic values;
- order `24261120`, twice `|2.L4(3)|=12130560`;
- `2.L4(3)` is perfect, has center of order two, and has simple central quotient `L4(3)`;
- the source fusion image equals `ClassPositionsOfDerivedSubgroup` and its derived-class size sum is `12130560`;
- the source center maps onto the target center `[1,2]`, and quotienting these positions gives `L4(3).2_2` or `L4(3).2_3` respectively;
- every class outside the derived positions maps to the nontrivial element of the order-two quotient, so any representative `h` satisfies `H=<H',h>`.

CTblLib's installed group-type metadata identifies `L4(3).2_1=PGL(4,3)` and `L4(3).2_2=PGO^+(6,3)`. Combined with the standard `A_3=D_3` identification and `Out(PSL_4(3))=C_2 x C_2` (diagonal and graph, with no field automorphism over `F_3`), this identifies `.2_2` as graph type and `.2_3` as diagonal-graph type; `.2_1` is the excluded diagonal/linear extension.

The local Malle--Navarro--Tiep arXiv:2605.04513v1 PDF has SHA-256 `a2825c5bfed0c8d340893b3b8bcfd62f89b1e94c7d170e13f4df34198357e96f`. Its stated results leave exactly the relevant prime-2 boundary open here:

- Theorem 4.3 treats cross-characteristic primes `ell>2` under the applicable center condition.
- The defining prime `3` is covered by Theorem D.
- Proposition 4.17 treats `GL_n(epsilon q)`, hence the excluded diagonal extension in this case, not these graph extensions.
- The prime-2 consequence after Proposition 4.17 assumes `n` odd or `q` even, whereas `n=4,q=3` has neither property.
- The paper explicitly says extension to arbitrary automorphisms needs disconnected-group Lusztig restriction control.

Thus the graph-extension scan does not merely repeat the cited paper's resolved prime-2 case. This is a nonduplication check against that paper's stated theorems, not an exhaustive literature claim.

## Exact coverage

| table | derived positions | outer positions | faithful rows | tested pairs | exact nonzero | violations |
|---|---|---|---:|---:|---:|---:|
| `2.L4(3).2_2` | `[1..40]` | `[41..69]` | 20 | 580 | 84 | 0 |
| `2.L4(3).2_3` | `[1..34]` | `[35..51]` | 17 | 289 | 36 | 0 |

Faithfulness is the exact condition `ClassPositionsOfKernel(chi)=[1]`. Nonvanishing is GAP's exact cyclotomic `not IsZero(value)`. Divisibility is the integer test `RemInt(24261120, chi(1)*Order(C))=0`. All class labels, orders and sizes; row labels, degrees and kernels; and pairwise values, products and remainders are preserved in the raw output.

## Constraint-and-conclusion matrix

| constraint_id | role | bounded use | result |
|---|---|---|---|
| `20.115-forall-G-chi-x` | admissibility | only two named tables and their faithful outer pairs were scanned | not established universally |
| `20.115-G-finite` | admissibility | each CTblLib table has finite order `24261120` | pass for both bounded groups |
| `20.115-chi-complex-irreducible` | admissibility | all retained rows lie in exact ordinary `Irr(table)` and have trivial kernel | pass for 20 and 17 bounded rows |
| `20.115-x-in-G` | admissibility | all retained columns are certified outer conjugacy classes with exact representative order | pass for 29 and 17 bounded classes |
| `20.115-character-value-nonzero` | admissibility | exact cyclotomic filtering retains 84 and 36 pairs | pass for retained pairs |
| `20.115-order-degree-divisibility` | target conclusion | exact integer remainder on every retained nonzero pair | passes all 120 bounded nonzero pairs; no universal conclusion |

## Reproduction and artifacts

Run:

```text
timeout 55s gap -q -b Agents/Kourovka/problems/20.115/runs/2026-08-17-r3-l43-graph-extensions/scratch/l43_graph_extensions_exact_scan.g > Agents/Kourovka/problems/20.115/runs/2026-08-17-r3-l43-graph-extensions/scratch/l43_graph_extensions_exact_scan.out
```

Observed exit: `0`, about 2.3 seconds. Software: GAP `4.12.1`, CTblLib `1.3.7`.

| artifact | SHA-256 |
|---|---|
| `scratch/l43_graph_extensions_exact_scan.g` | `aea034204dbe490e98245f239f7068b31c3d18f60c60598a293a3025993de3b4` |
| `scratch/l43_graph_extensions_exact_scan.out` | `439b7088ae0cffa36a6b9e341209ea13407095af00a7c47b56253df7c90a67fd` |
| `scratch/audit_l43_graph_output.awk` | `5dc4597f45ac6134530ecaa0ecea49ca7a7d542db2dc8385a26a07a9171a9fb2` |
| `scratch/audit_l43_graph_output.out` | `fde8ca7f0d4ea8b8963e005ec26ca7c476b98b6d7dc9db586a646006634e83d2` |
| `scratch/ctbllib_l43_group_type_metadata.txt` | `de25009568d2b91e9ef3423c5555628e83c1c029ae085ffea9b7a192ed258f07` |

The AWK audit independently recomputes the integer products and remainders, verifies row/class membership, nonzero and violation flags, pair uniqueness and summary counts, and reports `AUDIT_PASS true`.

## What this does not establish

- It neither proves nor refutes the universal Kourovka assertion.
- It does not scan inner classes, nonfaithful characters, another extension, or any catalogue. That restriction is deliberate and matches the assigned nearly-simple outer-coset lane.
- It does not derive the ATLAS character tables from group presentations; the scan and audit share the installed CTblLib data.
- It does not claim novelty beyond the cited 2026 paper.

## How this could be wrong

- An error in the stored CTblLib tables or fusion maps would survive both the scan and the arithmetic audit.
- The graph/diagonal-graph naming uses CTblLib metadata plus the standard outer-automorphism classification, not a separately constructed automorphism action.
- The AWK audit independently checks serialization and arithmetic but not the underlying cyclotomic character-table values.
- A counterexample may occur in an unscanned group, row, or class; zero hits here are only bounded evidence.

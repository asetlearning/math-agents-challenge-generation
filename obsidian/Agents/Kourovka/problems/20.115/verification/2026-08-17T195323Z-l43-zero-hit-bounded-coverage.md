---
title: "Verification — Kourovka 20.115 — L4(3) zero-hit bounded coverage"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
scope_record: Agents/Kourovka/scopes/20.115-nonzero-character-order-divisibility.json
assignment_revision: 1
claim: "In the ordinary CTblLib character table L4(3)=PSL_4(3), all 29 by 29 irreducible-row/class pairs satisfy chi(C) nonzero implies o(C)chi(1) divides 6065280; there are 495 nonzero pairs and zero violations."
claimant: Problem-20.115
target_statement: "For every finite group G, every ordinary irreducible complex character chi of G, and every x in G, if chi(x) is nonzero then o(x)chi(1) divides |G|."
excluded_scopes: ["Brauer or modular characters", "reducible characters", "rows with chi(x)=0", "the solvable-only known case", "the weaker fourth-power/fifth-power bound", "extension tables or other finite groups", "a bounded table screen presented as universal proof"]
target_object: "All admissible triples (G,chi,x) over every finite group in the canonical universal scope."
witness_object: "The 29 ordinary irreducible rows by 29 conjugacy classes of CTblLib 1.3.7 table L4(3), the Atlas table for the simple type-A3(3) group PSL_4(3)."
witness_equals_target: false
bounded_witness_identification: proven-with-ctbllib-metadata-and-independent-order-check
citation: "CTblLib 1.3.7 stored Lie-type record for simple A3(3), identifier L4(3), with Atlas origin; Malle--Navarro--Tiep, arXiv:2605.04513v1, for the narrow nonduplication gate."
verification_method: "Separately designed exact GAP scan, strict logical-record and arithmetic audit of the submitted output, byte-for-byte claimant-script rerun, rendered-source audit, and primary-paper theorem-hypothesis audit"
tools_used: ["GAP 4.12.1", "CTblLib 1.3.7", "Python 3.12.3 probe only", "GNU awk", "sha256sum", "Poppler pdftotext/pdftoppm"]
scope_answered: ["Bounded subcase: the single ordinary table L4(3)=PSL_4(3)"]
scope_not_answered: ["20.115/nonzero-character-order-divisibility universal scope", "Every finite group other than PSL_4(3)", "Extension tables of PSL_4(3)", "Any family-level or universal theorem"]
active_assignment_answered: no
outcome: PARTIAL_RESULT
fixed_partial_verdict: replicated
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/conjectured]
---

# Verification — `L4(3)` zero-hit bounded coverage

## Verdict

**The fixed one-table result is `status/replicated`.** A separately written exact GAP checker agrees with the claimant on the table identity and order, all 29 character degrees, all 29 class orders, the nonzero status of each of the 841 cells, the total of 495 nonzero cells, and zero failed divisibilities. Re-running the claimant's frozen script also reproduced its output byte for byte.

**The canonical revision-1 universal scope remains `status/conjectured`.** The witness is one finite group/table rather than all finite groups. Therefore `witness_equals_target: false` and `active_assignment_answered: no`; this verification does not promote or close the active scope.

There is one nonmathematical artifact correction: the submitted file has 841 `PAIR` record starts but is not strict physical-line TSV, because GAP wraps the long exact values in logical pairs 522 and 550 across a second line. A continuation-aware audit recovers all fields and passes. The independent scan makes the finite conclusion insensitive to this serialization defect.

## The claim

The bounded claim is

\[
G=\operatorname{PSL}_4(3),\quad
\chi\in\operatorname{Irr}(G),\quad x\in G,
\qquad \chi(x)\ne0\Longrightarrow o(x)\chi(1)\mid |G|,
\]

checked at the level of every ordinary irreducible row and every conjugacy-class column of the exact CTblLib table `L4(3)`. The submitted counts are `29*29=841` total pairs, 495 exact nonzero values, and zero violations.

This is an exhaustive statement about the one named ordinary table. It is not a universal proof and is not a counterexample.

## Scope, revision, and clause matrix

The canonical record is `20.115/nonzero-character-order-divisibility`, assignment revision 1. I inspected rendered PDF page 161 directly. It asks:

> Let chi be a complex irreducible character of a finite group G. If chi(x) is nonzero for some x in G, must o(x) divide |G|/chi(1)?

The submitted direct predicate `o(x)chi(1) | |G|` is the canonical equivalent arithmetic form; no block-exponent sufficient condition is substituted.

| source clause | active? | bounded computation | remainder |
|---|---:|---|---|
| Universal ordinary-complex implication for every finite `G`, `chi`, and `x` | yes | fixes `G=PSL_4(3)` and scans its whole ordinary table | every other finite group remains |
| `chi(x) != 0` | yes | exact cyclotomic zero test in every cell | none inside this table |
| `o(x) | |G|/chi(1)`, equivalently `o(x)chi(1) | |G|` | yes | exact integer arithmetic in every cell | universal conclusion remains open |
| Known solvable-group case | no, context | not used | excluded |
| Weaker `(o(x)chi(1))^4 | |G|^5` | no, context | not used | excluded |

`active_assignment_answered: no` follows already from the first row.

## Constraint-and-conclusion matrix

This matrix was reconstructed from the rendered source rather than copied from the submission.

| constraint_id | role | required condition | independent evidence | result |
|---|---|---|---|---|
| `20.115-forall-G-chi-x` | admissibility | every admissible triple is quantified | only one group's complete ordinary table is scanned | **not established universally** |
| `20.115-G-finite` | admissibility | `G` finite | CTblLib identifies simple type `A3(3)`; GAP's independent `PSL(4,3)` constructor has order 6065280 | pass for bounded group |
| `20.115-chi-complex-irreducible` | admissibility | ordinary irreducible complex `chi` | `IsOrdinaryTable=true`, underlying characteristic 0, `Irr(t)` has 29 pairwise-orthonormal rows, and degree-square sum is 6065280 | pass for every bounded row |
| `20.115-x-in-G` | admissibility | `x in G` and exact `o(x)` | all 29 table columns are scanned using `OrdersClassRepresentatives`; class sizes sum to the group order | pass for every bounded column |
| `20.115-character-value-nonzero` | admissibility | exact `chi(x) != 0` | all 841 values satisfy GAP's exact cyclotomic filter; independent `not IsZero(v)` pattern equals the submitted `v <> 0` pattern cell for cell | pass for 495 cells; zero cells correctly excluded |
| `20.115-order-degree-divisibility` | target conclusion | `o(x)chi(1) | |G|` | independent rational-integrality and integer-remainder formulations agree in all 841 cells; none of the 495 nonzero cells fails | pass for bounded table only |

No failed or unknown object row exists inside the bounded table. The universal-quantifier row nevertheless remains unproved, so the active assignment is not answered.

## Target versus witness

- **Source target:** all triples `(G,chi,x)` for every finite group.
- **Computational witness/domain:** all 841 row/class cells in one ordinary character table.
- **Witness equals universal target:** false.
- **Witness equals the stated bounded object:** yes, to the level established by CTblLib's stored Atlas/Lie-type identity and independent order/group-constructor checks.

CTblLib's stored Lie-type record is

```text
rec( isoc := "A", isot := [ "simple" ], l := 3, q := 3,
     identifier := "L4(3)", labelingfrom := "L4(3).2_1" )
```

Thus `L4(3)` is the simple group of type `A_3(3)`, standardly `PSL_4(3)` (also the familiar `D_3(3)` type coincidence), not `2.L4(3)` and not one of the `L4(3).2_i` extension tables. Runtime metadata independently returns `Identifier=L4(3)`, `IsOrdinaryTable=true`, characteristic 0, Atlas origin, and `IsSimpleCharacterTable=true`.

The order check is exact:

\[
|\operatorname{PSL}_4(3)|
=\frac{3^6(3^2-1)(3^3-1)(3^4-1)}{\gcd(4,3-1)}
=6065280.
\]

Both the table order and a separately constructed GAP `PSL(4,3)` have this order; the constructed group is simple and has center of order 1. The table's class sizes also sum to 6065280, and its only central class position is 1.

## Paper nonduplication gate

The narrow gate passes for the cited paper Malle--Navarro--Tiep, *Zeros of characters and orders of elements in finite groups*, arXiv:2605.04513v1. The inspected PDF has SHA-256
`a2825c5bfed0c8d340893b3b8bcfd62f89b1e94c7d170e13f4df34198357e96f`.

The paper's Conjecture A is the exact source predicate. For `PSL_4(3)`:

- Theorem C(3) and Theorem 4.3 cover nondefining characteristic only for primes `ell>2`; hence neither covers `ell=2`.
- Theorem D covers a simple Lie-type group at its defining prime, which here is 3, not the residual prime 2.
- The explicit consequence after Proposition 4.17 gives the `ell=2` case for quasi-simple `SL_n(epsilon q)` only when `n` is odd or `q` is even. Here `n=4` is even and `q=3` is odd.
- The alternating, Suzuki, small-Ree, and sporadic cases in Theorem D do not contain `PSL_4(3)`. Rewriting `A_3(3)` as the coincident `D_3(3)` does not remove the `ell>2` hypothesis of Theorem 4.3.

Therefore the prime-2 boundary targeted by this one-table scan is not among the cited paper's stated proved cases. This is deliberately only a nonduplication check against the cited theorem statements. It is not a new exhaustive literature search and does not claim that no other source treats `PSL_4(3)`.

## Circularity check

The character table is pre-existing CTblLib data of Atlas origin. It was not generated from the desired order-divisibility property, and the independent scan reads every exact table value before applying the target predicate. The zero-hit result is therefore not true by construction.

Both implementations share the same installed CTblLib table data. Their agreement replicates the finite evaluation and catches code/serialization errors; it does not independently re-prove the Atlas character table from a presentation of `PSL_4(3)`.

## Subclaims and what each method proves

| subclaim | method | what a pass proves | what it does not prove |
|---|---|---|---|
| exact source predicate | rendered page-161 inspection and scope comparison | correct ordinary-character, nonzero, order, and divisibility clauses | truth of the universal assertion |
| paper nonduplication | inspect the exact hypotheses of Theorems C, D, 4.3 and the post-Proposition-4.17 consequence | the cited results do not include the assigned `n=4,q=3,ell=2` boundary | novelty against every publication |
| artifact identity | SHA-256 plus byte-identical rerun | current files equal the claimed frozen artifacts and are deterministic here | mathematical correctness by itself |
| table identity/order | CTblLib stored type record, runtime metadata, formula, and separate `PSL(4,3)` construction | the bounded library table is the claimed ordinary simple-type table with order 6065280 | an independently derived character table |
| complete grid | nested independent 29-by-29 scan plus logical-record set audit | every row/class cell is included exactly once | any other table |
| exact nonzero predicate | `IsCyc`, independent `not IsZero`, and 841-bit cellwise comparison | no floating-point or approximate zero decision; exact patterns agree | character theory beyond stored exact values |
| divisibility and zero hits | independent `IsInt(6065280/d)` and `RemInt(6065280,d)=0`, plus submitted-field arithmetic audit | zero failed products among exactly 495 nonzero cells | a universal theorem |

## Evidence

### Tool and source probes

```text
GAP 4.12.1
CTblLib 1.3.7
Python 3.12.3
Sage MISSING
Magma MISSING
```

The direct page-161 extraction was:

```text
20.115. Let χ be a complex irreducible character of a finite group G. If χ(x) ̸= 0 for
some x ∈ G, must the order o(x) of x divide |G|/χ(1)?
```

The typography, including the nonzero sign and quotient, was checked on the rendered page rather than trusted from extraction.

### Table identity and order

Command:

```text
Load CTblLib; request CharacterTable("L4(3)"); print identifier,
ordinary/characteristic/simple metadata, order and InfoText.
Construct PSL(4,3) separately; print its size, simplicity and center size.
```

Output:

```text
IDENTIFIER L4(3)
ORDINARY true
UNDERLYING_CHARACTERISTIC 0
SIMPLE_TABLE true
ORDER 6065280
INFO_TEXT origin: ATLAS of finite groups, tests: 1.o.r., pow[2,3,5,13]
PSL_CONSTRUCTOR_SIZE 6065280
PSL_CONSTRUCTOR_IS_SIMPLE true
PSL_CONSTRUCTOR_CENTER_SIZE 1
```

### Submitted hashes and deterministic rerun

Command:

```text
timeout 55s gap -q -b Agents/Kourovka/problems/20.115/runs/2026-08-17-r2-l43-direct-residual/scratch/l43_exact_scan.g > Agents/Kourovka/problems/20.115/verification/scratch/l43_claimant_script_rerun.tsv
cmp -s Agents/Kourovka/problems/20.115/verification/scratch/l43_claimant_script_rerun.tsv Agents/Kourovka/problems/20.115/runs/2026-08-17-r2-l43-direct-residual/scratch/l43_exact_scan.tsv
sha256sum <submitted-script> <submitted-output> <validator-rerun>
```

Output:

```text
CLAIMANT_SCRIPT_RERUN_EXIT 0
OUTPUT_BYTE_CMP_EXIT 0
89ca00b164b290e1f8dd61394677422f37f1e987b4a015b7f3562ab3053c3f95  <submitted-script>
245ebfdfb2f722af6dbbaf673db2c8d1c098f7f208df2bd915f33e65457fb44f  <submitted-output>
245ebfdfb2f722af6dbbaf673db2c8d1c098f7f208df2bd915f33e65457fb44f  <validator-rerun>
submitted script: 86 lines, 2877 bytes
submitted output: 870 lines, 41332 bytes
validator rerun: 870 lines, 41332 bytes
```

These are exactly the two SHA-256 values stated in the findings.

### Independent direct scan

- Checker: `Agents/Kourovka/problems/20.115/verification/scratch/l43_independent_scan.g`
- Checker SHA-256: `f20cbfbfae4113e214fa719bdda92c9c51c203e50e4f233338f06476a2c28375`
- Output: `Agents/Kourovka/problems/20.115/verification/scratch/l43_independent_scan.out`
- Output SHA-256: `33569d627ee1e6c51e59a90e3516c5a595495a09090bfc0df6676cfa3c21cc17`

Command:

```text
timeout 55s gap -q -b Agents/Kourovka/problems/20.115/verification/scratch/l43_independent_scan.g > Agents/Kourovka/problems/20.115/verification/scratch/l43_independent_scan.out
```

Exit and output summary:

```text
INDEPENDENT_SCAN_EXIT 0
GAP_VERSION 4.12.1
CTBLLIB_VERSION 1.3.7
IDENTIFIER L4(3)
INFO_TEXT origin: ATLAS of finite groups, tests: 1.o.r., pow[2,3,5,13]
ORDINARY true
UNDERLYING_CHARACTERISTIC 0
SIMPLE_TABLE true
ORDER 6065280
PSL4_3_FORMULA_ORDER 6065280
CLASS_SIZE_SUM 6065280
IRR_DEGREE_SQUARE_SUM 6065280
IRR_PAIRWISE_ORTHONORMAL true
CENTER_CLASS_POSITIONS [ 1 ]
ROWS 29 CLASSES 29 PAIRS 841
ALL_VALUES_CYCLOTOMIC true
NONZERO_PAIRS 495
VIOLATIONS 0
VIOLATION_DATA [  ]
```

The full preserved output also contains all 29 degrees, all 29 class orders, row and column nonzero counts, and all 29 length-29 nonzero bitstrings.

### Submitted-output structural and arithmetic audit

- Auditor: `Agents/Kourovka/problems/20.115/verification/scratch/audit_l43_submitted_tsv.awk`
- Auditor SHA-256: `ce2c7c497b56647f4690c28d74264a350bf1494d0363e2e36d1471ee2aef6686`
- Audit output: `Agents/Kourovka/problems/20.115/verification/scratch/audit_l43_submitted_tsv.out`
- Audit-output SHA-256: `474a77f4db0994b06aa0755e12f8196f396993265f8aa3e029f2a3892f213233`

Command:

```text
timeout 55s awk -f Agents/Kourovka/problems/20.115/verification/scratch/audit_l43_submitted_tsv.awk Agents/Kourovka/problems/20.115/runs/2026-08-17-r2-l43-direct-residual/scratch/l43_exact_scan.tsv
```

Output:

```text
PAIR_COUNT 841
NONZERO_COUNT 495
VIOLATION_COUNT 0
BAD_SEQUENCE 0
BAD_GRID 0
BAD_NONZERO_FLAGS 0
BAD_PRODUCTS 0
BAD_DIVISIBILITY_FLAGS 0
BAD_VIOLATION_FLAGS 0
BAD_ROW_DATA 0
BAD_CLASS_DATA 0
BAD_PAIR_FIELD_COUNTS 0
SPLIT_PAIR_RECORDS 2
SUMMARY_RECORDS 1
SUMMARY_VALUES 841 495 0
AUDIT_PASS true
```

The two split logical records are:

```text
PAIR 522 row 18 class 29: first physical line ends after nonzero=true;
the continuation holds 8320, true, false.
PAIR 550 row 19 class 28: first physical line ends after nonzero=true;
the continuation holds 8320, true, false.
```

Thus the 29-by-29 logical grid is complete and arithmetically correct, but consumers must not assume one physical line per `PAIR` record.

### Cellwise nonzero-pattern comparison

The direct scan's 29 row bitstrings and the submitted output's reconstructed row bitstrings were normalized to 841 bits and compared:

```text
NONZERO_PATTERN_CMP_EXIT 0
841 <independent-pattern-bytes>
841 <submitted-pattern-bytes>
fd7cead8c4012b2fa8f24f80b937ff79de8b5d4935f4af1d698ee97c4ecb3e9e  <independent-pattern>
fd7cead8c4012b2fa8f24f80b937ff79de8b5d4935f4af1d698ee97c4ecb3e9e  <submitted-pattern>
```

This is stronger than agreement only on the total 495: every cell has the same exact zero/nonzero decision.

## Why this verdict

The bounded finite statement meets the computational replication threshold: two separately written scans agree, the original output is reproducible byte for byte, and a third data path audits every submitted logical record's coordinates, zero flag, product, divisibility flag, and violation flag. The stored values are exact cyclotomics; no floating approximation enters. Table identity and order guards also pass.

The universal target fails the witness-equality gate mechanically. A complete table for one simple group cannot imply the result for every finite group. The correct operational outcome is therefore `PARTIAL_RESULT`, with a replicated fixed subcase and no scope-level answer.

No `claim-checks` JSON was linked. Such a state-check is mandatory for `CLAIM` and `STALE_MATCH`; this artifact was routed as `PARTIAL_RESULT`/`REPORT`. Its absence does not invalidate the finite computation, but it supplies no route to universal closure.

## What is NOT established

- The universal assertion in Kourovka 20.115 is not proved or refuted.
- No counterexample was found; zero hits in this table do not imply zero hits elsewhere.
- No group other than the ordinary `PSL_4(3)` table is covered, including its outer extensions or central covers.
- No modular/Brauer character statement is covered.
- The Atlas/CTblLib table itself was not re-derived from a presentation; both scans share that exact library data.
- The paper audit establishes only that the named theorems do not duplicate the assigned prime-2 boundary, not global literature novelty.
- The submitted `.tsv` file is not strict physical-line TSV at two records, although the mathematical data and counts survive intact.
- Neither `status/proven` nor `status/solved` is warranted.

## What would upgrade it

The active scope can be answered affirmatively only by a gap-free proof for every finite group, or negatively by one reconstructible admissible counterexample with exact group, ordinary character, class/element order, nonzero cyclotomic value, and failed divisibility. Additional table screens remain partial coverage and each needs its own exact domain and review.

For machine-facing strict TSV, the claimant could suppress GAP line wrapping or use an explicit structured serializer and regenerate the output under a new hash. That cleanup would improve the artifact format but would not change this mathematical verdict.

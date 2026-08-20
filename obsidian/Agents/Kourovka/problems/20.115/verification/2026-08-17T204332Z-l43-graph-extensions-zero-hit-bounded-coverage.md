---
title: "Verification — Kourovka 20.115 — L4(3) graph-cover extension zero-hit coverage"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
scope_record: Agents/Kourovka/scopes/20.115-nonzero-character-order-divisibility.json
assignment_revision: 1
claim: "In each of the ordinary CTblLib tables 2.L4(3).2_2 and 2.L4(3).2_3, every faithful irreducible row on every outer-coset class satisfies chi(C) nonzero implies o(C)chi(1) divides 24261120; the complete bounded grid has 869 pairs, 120 exact nonzero values, and zero violations."
claimant: Problem-20.115
target_statement: "For every finite group G, every ordinary irreducible complex character chi of G, and every x in G, if chi(x) is nonzero then o(x)chi(1) divides |G|."
excluded_scopes: ["Brauer or modular characters", "reducible characters", "rows with chi(x)=0", "the solvable-only known case", "the weaker fourth-power/fifth-power bound", "inner classes and nonfaithful rows in the two tables", "other extension tables or finite groups", "a bounded table screen presented as universal proof"]
target_object: "All admissible triples (G,chi,x) over every finite group in the canonical universal scope."
witness_object: "The faithful ordinary Irr rows on the outer-coset columns of the installed CTblLib 1.3.7 tables 2.L4(3).2_2 and 2.L4(3).2_3."
witness_equals_target: false
bounded_witness_identification: proven-with-ctbllib-identifiers-fusions-central-quotients-and-outer-type-classification
citation: "CTblLib 1.3.7 Atlas-origin ordinary tables and stored fusions; Malle--Navarro--Tiep, arXiv:2605.04513v1, only for the limited paper-nonduplication gate."
verification_method: "Separately written exact GAP checker, independent linear-character/kernel reconstruction, exact 869-record cross-parser comparison, integer-arithmetic audit, rendered-source inspection, and local primary-paper theorem-hypothesis audit"
tools_used: ["GAP 4.12.1", "CTblLib 1.3.7", "Python 3.12.3", "Poppler 24.02.0", "awk", "sha256sum"]
scope_answered: ["Bounded subcase: faithful ordinary rows on outer classes of 2.L4(3).2_2", "Bounded subcase: faithful ordinary rows on outer classes of 2.L4(3).2_3"]
scope_not_answered: ["20.115/nonzero-character-order-divisibility universal scope", "Inner classes and nonfaithful rows of the two tables", "Every other finite group or table", "Any family-level or universal theorem"]
active_assignment_answered: no
outcome: PARTIAL_RESULT
fixed_partial_verdict: replicated
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/conjectured]
---

# Verification — L4(3) graph-cover extension zero-hit coverage

## Verdict

**The exact fixed two-table coverage claim is `status/replicated`.** A separately
written GAP checker independently reconstructs the base, fusion, derived, center,
central-quotient, faithful-row, and outer-class gates. It then serializes every one
of the `580 + 289 = 869` specified row/class pairs. A separate Python parser
recomputes the arithmetic and proves equality of all 869 normalized exact records
with the claimant's frozen output, including every row label, degree, class label,
class order, exact cyclotomic value, zero flag, product, and remainder. There are
exactly `84 + 36 = 120` nonzero pairs and zero nonzero-value divisibility
violations.

**The canonical revision-1 universal scope remains `status/conjectured`.** The two
bounded tables are not all finite groups, and even inside them this assignment scans
only faithful rows on outer classes. Thus `witness_equals_target: false` and
`active_assignment_answered: no`. Nothing here proves or refutes Kourovka 20.115.

## The claim

For each

```text
T in { CharacterTable("2.L4(3).2_2"),
       CharacterTable("2.L4(3).2_3") },
```

let `D` be the class positions of the derived subgroup, let the selected columns be
the complement of `D`, and retain exactly the ordinary irreducible rows having
kernel positions `[1]`. The submitted claim is that every retained pair `(chi,C)`
satisfies

```text
chi(C) <> 0  ==>  RemInt(24261120, chi(1)*Order(C)) = 0.
```

This is an exhaustive claim about the stated bounded grid, not about the whole
ordinary tables and not about the universal problem.

## Scope, revision, and clause matrix

The canonical record is `20.115/nonzero-character-order-divisibility`, assignment
revision 1. I read and visually inspected rendered source PDF page 161. The
source asks whether, for a complex irreducible character `chi` of a finite group
`G`, nonvanishing at `x` forces `o(x)` to divide `|G|/chi(1)`.

| source clause | active? | bounded computation | remainder |
|---|---:|---|---|
| Universal ordinary-complex implication for every finite `G`, `chi`, and `x` | yes | fixes two ordinary tables, then restricts to faithful rows and outer classes | all other triples remain |
| Exact hypothesis `chi(x) != 0` | yes | exact cyclotomic equality to zero on all 869 pairs | zero pairs are excluded from the implication |
| `o(x) | |G|/chi(1)`, equivalently `o(x)chi(1) | |G|` | yes | exact integer remainder on all nonzero retained pairs | universal conclusion remains open |
| Known solvable-group case | no, context | not used | excluded |
| Weaker `(o(x)chi(1))^4 | |G|^5` | no, context | not used | excluded |

The canonical scope transcription and the submitted direct predicate agree. The
bounded restriction forces `active_assignment_answered: no` independently of the
scan result.

## Constraint-and-conclusion matrix

This matrix was reconstructed from the rendered source rather than copied from the
submission.

| constraint_id | role | required condition | independent evidence | result |
|---|---|---|---|---|
| `20.115-forall-G-chi-x` | admissibility | every admissible triple | two tables, faithful rows, outer classes only | **not established universally** |
| `20.115-G-finite` | admissibility | `G` finite | ordinary Atlas-origin CTblLib tables of order `24261120`, with exact base/quotient fusions | pass for the two bounded groups/tables |
| `20.115-chi-complex-irreducible` | admissibility | ordinary complex irreducible `chi` | characteristic-zero `Irr` rows; all values cyclotomic; every selected row's kernel independently reconstructed as `[1]` | pass for 20 and 17 selected rows |
| `20.115-x-in-G` | admissibility | `x in G`, exact `o(x)` | outer columns reconstructed as the complement of the common kernel of all linear rows; exact stored class orders | pass for 29 and 17 selected classes |
| `20.115-character-value-nonzero` | admissibility | exact `chi(x) != 0` | exact GAP cyclotomic comparison, matched record-for-record by both artifacts | pass for exactly 84 and 36 pairs |
| `20.115-order-degree-divisibility` | target conclusion | `o(x)chi(1) | |G|` | exact products and remainders independently reparsed for all 869 pairs | pass for all 120 bounded nonzero pairs; not universal |

There is no asserted counterexample. The universal-quantifier row remains
unproved, so the active assignment cannot close.

## Target versus witness and circularity

- **Source target:** every admissible triple `(G,chi,x)` over every finite group.
- **Computational witness/domain:** 869 cells in two stored ordinary tables.
- **Witness equals the universal target:** false.
- **Witness equals the stated bounded table domain:** yes, to the level provided by
  CTblLib's exact identifiers, Atlas provenance, stored subgroup and quotient
  fusions, and the independent structural checks below.

The tables are pre-existing CTblLib data and were not generated from the desired
divisibility condition. The scan reads their exact values and only then applies the
source predicate, so the zero-hit result is not true by construction. Both
computations nevertheless share CTblLib's stored table data; agreement does not
rederive the Atlas tables from presentations.

## Exact table identities and structural gates

### Perfect base and simple central quotient

For `B = CharacterTable("2.L4(3)")`, the independent checker obtains:

```text
identifier=2.L4(3)
order=12130560
number of classes=51
derived positions=[1..51]
center positions=[1,2]
center order=2
```

The derived positions were reconstructed as the common kernel of all linear
ordinary rows, not inherited from `ClassPositionsOfDerivedSubgroup`; the two lists
then agreed. The center was reconstructed from the singleton conjugacy classes,
then compared with `ClassPositionsOfCenter`.

The stored fusion `2.L4(3) -> L4(3)` is onto all 29 quotient classes and has kernel
positions `[1,2]`. `CharacterTableFactorGroup(B,[1,2])` is permutation-equivalent
to the stored `L4(3)` table. That quotient table has order `6065280` and exactly the
two normal-subgroup class sets `[1]` and `[1..29]`. Thus the character-table data
certify the claimed perfect base, central involution, and simple central quotient.

### The two covers

| target table | classes | base-fusion image = derived positions | outer positions | center | central quotient |
|---|---:|---|---|---|---|
| `2.L4(3).2_2` | 69 | `[1..40]` | `[41..69]` | `[1,2]` | `L4(3).2_2` |
| `2.L4(3).2_3` | 51 | `[1..34]` | `[35..51]` | `[1,2]` | `L4(3).2_3` |

For each target, independently reconstructed derived positions agree with the
stored derived positions and with the image of the exact 51-entry fusion from the
perfect base. Fusion preimages aggregate to every target derived-class size exactly,
and the derived-class sizes sum to `12130560`, half the target order. The source
center `[1,2]` maps onto the target center `[1,2]`.

The stored central-quotient fusion has kernel `[1,2]`, is onto every quotient class,
has the correct factor-of-two class-size aggregation, and agrees with an independently
constructed character-table factor. The complete 51-entry base and central-quotient
fusion maps are preserved verbatim in the validator output.

Since the derived subgroup has index two, every class outside the displayed derived
positions maps to the unique nonidentity element of `H/H'`. Consequently every
representative `h` from a selected outer class satisfies `H = <H',h>`.

### Graph versus diagonal-graph, and nonduplication

The standard outer-automorphism calculation for `PSL_4(3)` has diagonal factor
of order `gcd(4,3-1)=2`, no nontrivial field factor over the prime field `F_3`, and
graph factor of order two. The graph automorphism acts by inversion on the diagonal
factor, which is trivial on a group of order two. Hence

```text
Out(PSL_4(3)) = C2 x C2.
```

CTblLib independently supplies `L4(3).2^2` as `Aut(L4(3))`, of order `24261120`,
with construction text `PGL(4,3) extended by transpose-inverse`. Its three stored
index-two subgroup tables have distinct class counts and disjoint outer-class
images:

```text
L4(3).2_1: 43 classes; outer image in Aut = [22..33]
L4(3).2_2: 49 classes; outer image in Aut = [34..47]
L4(3).2_3: 34 classes; outer image in Aut = [48..56]
```

These images partition all outer positions `[22..56]` of `Aut(L4(3))`. CTblLib's
construction metadata identifies `.2_1` as `PGL(4,3)`, the diagonal extension, and
`.2_2` as `PSL(4,3) extended by transpose-inverse` (also `PGO(+1,6,3)`), the graph
extension under the standard `A3=D3` identification. With precisely three
nonidentity elements in `Out(L4(3))`, the remaining distinct `.2_3` table is the
diagonal-graph extension. The two cover tables factor by their central involution to
`.2_2` and `.2_3`, respectively. They are therefore the graph and diagonal-graph
covers, not duplicate names for one table and not the excluded diagonal `.2_1`
cover.

This naming proof uses CTblLib metadata, exact fusions, and the standard outer-
automorphism classification. It is not a separately constructed matrix action for
the graph automorphism.

## Certified row and class selections

Every table is ordinary with underlying characteristic zero, and every stored value
is a GAP cyclotomic. A row was retained exactly when the positions satisfying
`chi(C)=chi(1)` were `[1]`; this reconstructed kernel was compared row-by-row with
`ClassPositionsOfKernel` for all 69 and 51 irreducibles.

Faithful row positions with degrees are:

```text
2.L4(3).2_2:
50(40), 51(40), 52-53(416), 54(520), 55-56(832), 57-58(480),
59-64(520), 65-66(1280), 67(1560), 68-69(1080).

2.L4(3).2_3:
35-36(40), 37-38(416), 39(520), 40-41(832), 42-43(480),
44-45(520), 46(1040), 47-48(1280), 49(1560), 50-51(1080).
```

Certified outer classes, recorded as `position: label/order`, are:

```text
2.L4(3).2_2:
41:2D_0/4, 42:2E_0/4, 43:2F_0/2, 44:4E_0/4,
45:4F_0/8, 46:4G_0/8, 47:6H_0/12, 48:6H_1/12,
49:6I_0/12, 50:6I_1/12, 51:6J_0/12, 52:6K_0/12,
53:6L_0/12, 54:6M_0/12, 55:6N_0/6, 56:6O_0/6,
57:6P_0/6, 58:6P_1/6, 59:8G_0/8, 60:10B_0/20,
61:10C_0/20, 62:12D_0/12, 63:12D_1/12, 64:12E_0/24,
65:12F_0/24, 66:18A_0/36, 67:18A_1/36, 68:18B_0/36,
69:18B_1/36.

2.L4(3).2_3:
35:2G_0/2, 36:4H_0/4, 37:6Q_0/6, 38:6Q_1/6,
39:8H_0/8, 40:8I_0/8, 41:8J_0/8, 42:8K_0/16,
43:8L_0/16, 44:10D_0/10, 45:10E_0/10, 46:12G_0/12,
47:12G_1/12, 48:24C_0/24, 49:24C_1/24, 50:24D_0/24,
51:24D_1/24.
```

Thus the complete Cartesian grids have `20*29=580` and `17*17=289` unique
pairs.

## Exact values and divisibility results

| table | faithful rows | outer classes | pairs | exact nonzero | nonzero violations |
|---|---:|---:|---:|---:|---:|
| `2.L4(3).2_2` | 20 | 29 | 580 | 84 | 0 |
| `2.L4(3).2_3` | 17 | 17 | 289 | 36 | 0 |
| **total** | 37 | 46 | **869** | **120** | **0** |

The complete exact value attached to every one of the 869 coordinates is in
`verification/scratch/l43_graph_extensions_validator.out`. The set of nonzero
value expressions and their multiplicities is:

```text
2.L4(3).2_2:
-3*E(12)^7+3*E(12)^11 (8),  -3 (2),
-6*E(12)^7+6*E(12)^11 (4),  -9*E(12)^7+9*E(12)^11 (8),
-E(12)^7+E(12)^11 (20),      3*E(12)^7-3*E(12)^11 (8),
3 (2),                         6*E(12)^7-6*E(12)^11 (4),
9*E(12)^7-9*E(12)^11 (8),     E(12)^7-E(12)^11 (20).

2.L4(3).2_3:
-3 (2),                        -E(12)^7+E(12)^11 (12),
-E(24)+E(24)^11+E(24)^17-E(24)^19 (4),
3 (2),                         E(12)^7-E(12)^11 (12),
E(24)-E(24)^11-E(24)^17+E(24)^19 (4).
```

The normalized certificate digests are:

```text
all 869 exact pair records:
b5b435fc6b9db31df3d6b286eabc5da3d0307bce21880b2dcf2a77c22298ffca

the 120 exact nonzero records:
ee2c27c360037dd971adca1fa3c9c0384c682852dcd26972b3a2d0cbbc79fa70
```

Both normalized certificates are identical between the independent validator
output and the claimant output. Some zero-value pairs have nonzero remainders; that
is expected and irrelevant because the source implication assumes nonvanishing.
The reported violation count is exactly the number of pairs with both nonzero value
and nonzero remainder.

## Paper nonduplication gate

The locally cached Malle--Navarro--Tiep paper, *Zeros of characters and orders of
elements in finite groups*, arXiv:2605.04513v1, has SHA-256
`a2825c5bfed0c8d340893b3b8bcfd62f89b1e94c7d170e13f4df34198357e96f`.
The exact theorem hypotheses show:

- Theorem 4.3 treats cross-characteristic primes `ell>2`, so it does not settle the
  prime-2 boundary here.
- Theorem D covers simple Lie-type groups at their defining prime, which here is 3.
- Proposition 4.17 completes `GL_n(epsilon q)`. At `n=4,q=3`, this is the diagonal
  cover whose central quotient is the excluded `.2_1=PGL(4,3)` type, not either
  graph cover scanned here.
- The immediate prime-2 consequence for `SL_n(epsilon q)` assumes `n` odd or `q`
  even. Here `n=4` and `q=3`, so neither hypothesis holds.
- Immediately before Proposition 4.17, the authors state that extending the
  preceding result from `SL_n(q)` or `SU_n(q)` by arbitrary automorphisms requires
  a disconnected-reductive-group Curtis formula and control of Lusztig-restriction
  constituents; the latter is described as much more difficult.

Therefore these graph-extension tables are not merely a rerun of the specific
prime-2 case proved by Proposition 4.17 or its stated consequence. This is only a
nonduplication check against that paper's named results, not an exhaustive novelty
or literature claim.

## Subclaims and method limits

| subclaim | method | what a pass proves | what it does not prove |
|---|---|---|---|
| source predicate | rendered page-161 inspection | exact ordinary, nonzero, order and divisibility clauses | truth of the assertion |
| base/cover identity | exact identifiers, orders, degree squares, subgroup fusions, center factors and normal-class sets | internal identity and consistency of the installed ordinary datasets | derivation of Atlas tables from group presentations |
| graph naming | outer-automorphism calculation, CTblLib Aut metadata, and three disjoint subgroup fusions | `.2_2` graph, `.2_3` diagonal-graph, and nonduplication from `.2_1` | an independently constructed automorphism action |
| row/class grid | reconstructed kernels and common linear-row kernel | complete faithful/outer selection in the two tables | inner classes, nonfaithful rows, or other tables |
| exact scan | fresh GAP nested loops with exact cyclotomic values | every specified cell is tested against the direct predicate | any universal theorem |
| record audit | separate Python parser and integer arithmetic | no omitted/duplicate pair, bad flag, product, remainder, or differing exact record | independent character-table data outside CTblLib |
| paper gate | local primary-PDF theorem-hypothesis inspection | cited results do not cover this named prime-2 graph-extension case | exhaustive novelty against all literature |

## Evidence

### Tools and source

The tool probe returned:

```text
GAP_VERSION=4.12.1
CTBLLIB_VERSION=1.3.7
Python 3.12.3
sage=(not found)
magma=(not found)
pdftotext version 24.02.0
```

The page-161 extraction was:

```text
20.115. Let chi be a complex irreducible character of a finite group G. If chi(x) != 0 for
some x in G, must the order o(x) of x divide |G|/chi(1)?
```

The nonzero sign, quotient, and contextual exponents were also checked on the
rendered page image.

### Frozen independent run

Frozen manifest:
`Agents/Kourovka/problems/20.115/verification/2026-08-17T203311Z-l43-graph-extensions-validator-manifest.md`

Command:

```text
timeout 30s gap -q -b Agents/Kourovka/problems/20.115/verification/scratch/l43_graph_extensions_validator.g > Agents/Kourovka/problems/20.115/verification/scratch/l43_graph_extensions_validator.out
```

Observed output:

```text
RUN_EXIT=0
1083 lines, 64706 bytes
SUMMARY|table=2.L4(3).2_2|faithful_rows=20|outer_classes=29|pairs=580|nonzero=84|violations=0
SUMMARY|table=2.L4(3).2_3|faithful_rows=17|outer_classes=17|pairs=289|nonzero=36|violations=0
TOTAL|pairs=869|nonzero=120|violations=0
FINAL|PASS
PAIR_RECORDS=869
PASS_RECORDS=191
ERROR_WARNING_RECORDS=0
NONZERO_PAIR_RECORDS=120
NONZERO_VIOLATION_RECORDS=0
```

The full 1,083-line verbatim output, including all structural assertions, four exact
fusion maps, and all 869 `PAIR` records, is preserved at the output path above.

### Independent record audit and exact comparison

Command:

```text
timeout 10s python3 Agents/Kourovka/problems/20.115/verification/scratch/audit_l43_graph_validator.py > Agents/Kourovka/problems/20.115/verification/scratch/audit_l43_graph_validator.out
```

Verbatim output:

```text
AUDIT_EXIT=0
AUDIT|validator|pairs=869
AUDIT|validator|table=2.L4(3).2_2|pairs=580|nonzero=84|violations=0
AUDIT|validator|table=2.L4(3).2_3|pairs=289|nonzero=36|violations=0
AUDIT|validator|total_nonzero=120|total_violations=0
AUDIT|claimant|pairs=869
AUDIT|claimant|table=2.L4(3).2_2|pairs=580|nonzero=84|violations=0
AUDIT|claimant|table=2.L4(3).2_3|pairs=289|nonzero=36|violations=0
AUDIT|claimant|total_nonzero=120|total_violations=0
COMPARE|exact_pair_records_equal=true|count=869
COMPARE|exact_nonzero_records_equal=true|count=120
DIGEST|all_pairs_sha256=b5b435fc6b9db31df3d6b286eabc5da3d0307bce21880b2dcf2a77c22298ffca
DIGEST|nonzero_pairs_sha256=ee2c27c360037dd971adca1fa3c9c0384c682852dcd26972b3a2d0cbbc79fa70
AUDIT_FINAL|PASS
```

### Artifact hashes

The five hashes stated by the claimant match the current frozen files exactly:

| submitted artifact | SHA-256 |
|---|---|
| `l43_graph_extensions_exact_scan.g` | `aea034204dbe490e98245f239f7068b31c3d18f60c60598a293a3025993de3b4` |
| `l43_graph_extensions_exact_scan.out` | `439b7088ae0cffa36a6b9e341209ea13407095af00a7c47b56253df7c90a67fd` |
| `audit_l43_graph_output.awk` | `5dc4597f45ac6134530ecaa0ecea49ca7a7d542db2dc8385a26a07a9171a9fb2` |
| `audit_l43_graph_output.out` | `fde8ca7f0d4ea8b8963e005ec26ca7c476b98b6d7dc9db586a646006634e83d2` |
| `ctbllib_l43_group_type_metadata.txt` | `de25009568d2b91e9ef3423c5555628e83c1c029ae085ffea9b7a192ed258f07` |

Validator artifacts:

| validator artifact | SHA-256 |
|---|---|
| frozen manifest | `35a876982b644a868f8589a8c88450e486b5491fc167f9bb0845d9e0df84ed35` |
| independent GAP checker | `817b5fdeca74eb1a2f9b9dff4d475fb308de39131fc57a6e0c6be780e69ce94a` |
| independent GAP output | `1daf71e5779bc13205a6df60693a117d842e5e876d87c6f3dda07c29280a650e` |
| comparison/audit parser | `354725b1a4a217f1074ff3c7cc5ad1ac73822c335395a92e364fbac893d62b3e` |
| comparison/audit output | `7eb60ee185f9ce56805077f30e0773cae2c0f12bfbefedd6b6a90ca975c2b00f` |

The claimant script was not executed or imported by the validator checker. Its
frozen output was parsed only after the independent output existed, and every exact
record was then compared.

## Why this verdict

The bounded finite statement meets the replication threshold. There are two
separately written computations, at least one written by Validator, and their full
exact certificates agree. Independent structural reconstruction prevents the
counts from depending merely on copied row/class lists, while the second parser
prevents a summary or arithmetic serialization error from hiding a bad pair.

The universal target fails the witness-equality gate mechanically. Two restricted
table grids cannot imply a statement about all finite groups. The correct outcome is
therefore `PARTIAL_RESULT`: replicated bounded coverage, no counterexample, no
scope-level answer.

No `claim-checks` JSON was linked. The common protocol requires one for `CLAIM` or
`STALE_MATCH`; this request is explicitly a bounded `PARTIAL_RESULT`, so the state
check is not a missing gate for this finite verification and provides no route to
universal closure.

## What is NOT established

- Kourovka 20.115 is neither proved nor refuted.
- Inner classes and nonfaithful ordinary rows of these two tables were not scanned.
- No other group, cover, extension, Brauer table, or catalogue family was scanned.
- The Atlas/CTblLib character tables were not rederived from presentations; both
  scans share the installed exact table data.
- The graph naming was not checked by constructing explicit matrices and an
  automorphism action independently of CTblLib metadata and standard theory.
- The paper comparison is not an exhaustive novelty or literature search.
- Zero hits do not provide a necessary-and-sufficient reduction or a family theorem.

## What would upgrade it

A scope-level upgrade requires either a reconstructible admissible triple with
nonzero exact value and failed divisibility, or a gap-free proof for every finite
group. Reconstructing these two ordinary tables from explicit group presentations
would strengthen independence of this bounded certificate, but it would still not
answer the active universal assignment.

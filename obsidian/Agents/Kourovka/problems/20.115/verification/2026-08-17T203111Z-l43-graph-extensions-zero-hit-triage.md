---
title: "Triage — Kourovka 20.115 — L4(3) graph-cover extensions zero-hit scan"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
scope_record: Agents/Kourovka/scopes/20.115-nonzero-character-order-divisibility.json
assignment_revision: 1
claimant: Problem-20.115
active_assignment_answered: pending
author: operator
tags:
  - agent/validator
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/draft
---

# Triage — Kourovka 20.115 — L4(3) graph-cover extensions zero-hit scan

## Claim restated

For each of the installed ordinary CTblLib tables `2.L4(3).2_2` and
`2.L4(3).2_3`, every pair consisting of a faithful irreducible ordinary row and
an outer-coset class has nonzero exact character value only when the product of
the row degree and class order divides `24261120`; the claimed complete bounded
grid has `580 + 289 = 869` pairs, `84 + 36 = 120` exact nonzero pairs, and zero
divisibility violations.

This is a `PARTIAL_RESULT`, not a claim to answer the universal source question.
The common protocol requires a claim-check JSON only for `CLAIM` or
`STALE_MATCH`; none is required or supplied for this bounded `PARTIAL_RESULT`.

## Locked scope

- `scope_id`: `20.115/nonzero-character-order-divisibility`
- `assignment_revision`: `1`
- Exact active target: for every finite group `G`, every complex irreducible
  character `chi` of `G`, and every `x in G`, if `chi(x) != 0`, then `o(x)`
  divides `|G|/chi(1)`, equivalently `o(x)chi(1)` divides `|G|`.
- Excluded: Brauer/modular characters, zero values, reducible characters, the
  solvable-only known case, the weaker fourth/fifth-power bound, and any bounded
  table screen presented as a proof of the universal assertion.

The statement was independently read from rendered PDF page 161. The displayed
formula is `(o(x)chi(1))^4 | |G|^5`; the canonical scope has transcribed both the
question and the contextual exclusions correctly.

## Clause matrix

| source row | in active scope | submitted finite claim | current result |
|---|---:|---|---|
| Question: nonzero ordinary irreducible value implies `o(x) | |G|/chi(1)` for every finite `G` | yes | Tests only faithful rows on certified outer classes in two named tables | bounded claim only; universal row not answered |
| Assertion known for solvable `G` | no, context | Does not address | excluded context |
| General bound `(o(x)chi(1))^4 | |G|^5` | no, context | Does not address | excluded context |

`active_assignment_answered: pending` at triage; even a complete pass must become
`no`, because two finite tables do not exhaust all finite groups, characters, or
classes.

## Independently reconstructed constraint-and-conclusion matrix

| constraint_id | role | required source condition | submitted candidate use | pre-verification result |
|---|---|---|---|---|
| `20.115-forall-G-chi-x` | admissibility | Universal quantification over every admissible triple | Two tables, faithful rows, outer classes only | failed for universal coverage; intentional bounded restriction |
| `20.115-G-finite` | admissibility | `G` finite | Two alleged ordinary tables of finite groups of order `24261120` | pending independent table-identity check |
| `20.115-chi-complex-irreducible` | admissibility | `chi` ordinary complex irreducible | Rows selected from alleged ordinary `Irr` lists and then restricted to faithful rows | pending independent row reconstruction |
| `20.115-x-in-G` | admissibility | `x in G`, with exact element order `o(x)` | Columns alleged to be outer conjugacy classes with stored element orders | pending independent fusion/outer-position reconstruction |
| `20.115-character-value-nonzero` | admissibility | Exact `chi(x) != 0` | Claimed exact cyclotomic zero test | pending independent exact-value scan |
| `20.115-order-degree-divisibility` | target conclusion | `o(x)chi(1) | |G|` | Claimed exact integer remainder for all 120 retained pairs | pending independent scan; not universal even if all pass |

No candidate counterexample is asserted. The universal quantifier row is not
satisfied, so the active assignment cannot be closed by this result.

## Target versus witness

- Source target object: all triples `(G,chi,x)` with `G` finite, `chi` an ordinary
  complex irreducible character, and `x in G` with nonzero value.
- Witness objects actually computed in: the two stored ordinary CTblLib datasets
  returned by `CharacterTable("2.L4(3).2_2")` and
  `CharacterTable("2.L4(3).2_3")`.
- Active assignment: the universal source target above.
- `witness = target`: false for universal scope. The two tables form a strict
  bounded subfamily. Separately, whether each stored table is correctly identified
  with the named finite extension is a pending evidence gate.

The tables are external library data, not objects constructed from the divisibility
property under test, so there is no evident by-construction circularity. This does
not immunize the stored data or metadata from error.

## Sub-claims

1. The canonical scope faithfully transcribes the source question.
2. The installed objects are characteristic-zero ordinary character tables with
   identifiers exactly `2.L4(3).2_2` and `2.L4(3).2_3`, each of order `24261120`.
3. The source table `2.L4(3)` has order `12130560`, is perfect, has center of order
   two, and has simple central quotient `L4(3)` in the character-table sense used.
4. For each target table, the stored index-two fusion image equals the target
   derived-subgroup class positions; center positions fuse correctly; derived
   class sizes sum to `12130560`; quotienting the center gives the claimed
   `L4(3).2_i` quotient table.
5. The two targets are distinct non-diagonal outer extensions: `.2_2` is graph
   type and `.2_3` diagonal-graph type, with `.2_1` the diagonal/linear extension;
   the submitted scan is not duplicate coverage of `.2_1`.
6. Faithful ordinary rows are exactly those whose character-table kernel positions
   are `[1]`: 20 rows for `.2_2` and 17 for `.2_3`.
7. Outer classes are exactly the complements of the fusion/derived positions: 29
   for `.2_2` and 17 for `.2_3`.
8. The Cartesian grids therefore contain exactly `20*29 + 17*17 = 869` unique
   row/class pairs.
9. Exact ordinary values are nonzero on exactly 84 and 36 pairs, and all 120 exact
   integer products `degree*class_order` divide `24261120`.
10. Submitted artifact hashes and cited exact values/counts match the frozen files.
11. The cited 2026 paper does not already subsume these prime-2 graph-extension
    cases under the specific stated results invoked by the claimant; this is only
    a limited nonduplication check, not an exhaustive novelty claim.

## Tool probe

- GAP `4.12.1`: available at `/usr/bin/gap`.
- CTblLib `1.3.7`: loads successfully.
- Python `3.12.3`: available at `/usr/bin/python3`.
- Sage: unavailable.
- Magma: unavailable.
- `pdftotext`/Poppler `24.02.0` and `pdftoppm`: available.

## Methods inventory and limits

| sub-claim(s) | independent method | what a pass proves | what a pass does not prove |
|---|---|---|---|
| 1 | Render and visually inspect PDF page 161; compare clause-by-clause with revision 1 JSON | Source fidelity of this assignment | Truth of the assertion |
| 2--4 | Fresh GAP queries against CTblLib public attributes, fusions, derived/center positions, class sizes, quotient fusions and table identifiers | Internal identity and fusion consistency of the installed exact ordinary datasets | Derivation of the ATLAS tables from presentations or absence of a library-data error |
| 5 | Independently inspect CTblLib group-type metadata and the outer-automorphism structure, keeping metadata claims separate from computation | Installed naming/type evidence and nonduplication among the three index-two quotient types | A newly constructed automorphism action or exhaustive literature novelty |
| 6--9 | A fresh bounded GAP checker with independently chosen control flow and serialization; do not run or import claimant code | Complete exact scan of the specified finite row/class grid in the installed tables | Anything about inner classes, nonfaithful rows, other groups, or the universal target |
| 9 | Separately parse the fresh checker's certificate and recompute integer arithmetic/cardinalities | Guards against summary/serialization/counting error in the fresh scan | Independent character-table values outside CTblLib |
| 10 | `sha256sum` on the frozen submitted artifacts | Byte identity and exact hashes at validation time | Mathematical correctness |
| 11 | Read the locally cited PDF at the exact theorem/proposition passages and compare its hypotheses | Whether the specific invoked results cover these cases | An exhaustive post-2026 novelty search or proof that no other paper covers them |

The concrete computation is expected to finish in seconds and is not a heavy job;
no compute lease is needed. The run will be bounded by an explicit timeout and will
touch exactly the two named tables. No catalogue expansion is authorized.

## Recommendation

Proceed with partial-only verification. A successful result can replicate the
finite CTblLib coverage claim, but must retain `active_assignment_answered: no` and
must list the universal assertion, all omitted rows/classes/groups, the dependence
on CTblLib data, and the limited nature of the naming/literature checks as not
established.

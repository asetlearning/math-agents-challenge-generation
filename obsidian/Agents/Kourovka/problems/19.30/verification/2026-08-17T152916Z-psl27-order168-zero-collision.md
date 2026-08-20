---
title: "Verification — Kourovka 19.30 — PSL(2,7), order-168 zero-collision partial"
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
scope_record: Agents/Kourovka/scopes/19.30-vanishing-order-simple-recognition.json
assignment_revision: 1
claim: "For every finite group G, if |G|=168 and V_o(G)=V_o(PSL(2,7)), then G is isomorphic to PSL(2,7)."
claimant: Problem-19.30
target_statement: "For every finite group G and finite simple group S, if |G|=|S| and G and S have the same set of orders of vanishing elements, then G is isomorphic to S."
excluded_scopes: ["Equality of character tables without equality of vanishing-order sets", "Equality of spectra of all elements rather than only vanishing elements", "Pairs in which neither group is finite simple"]
target_object: "Every pair (G,S) in the canonical universal scope."
witness_object: "The fixed target S=PSL(2,7) and all 57 installed GAP SmallGroups representatives SmallGroup(168,i)."
witness_equals_target: false
citation: "No external citation; independent computation in GAP 4.12.1 with SmallGrp 1.5.3 and CTblLib 1.3.7."
verification_method: "Separately frozen exact GAP enumeration and cross-artifact comparison"
tools_used: ["GAP 4.12.1", "SmallGrp 1.5.3", "CTblLib 1.3.7", "Poppler pdftotext/pdftoppm"]
scope_answered: ["Fixed computational subcase S=PSL(2,7), |G|=168, over the complete installed SmallGroups order-168 catalogue"]
scope_not_answered: ["19.30/vanishing-order-simple-recognition universal scope", "Every finite simple target other than PSL(2,7)", "Any family-level recognition theorem"]
active_assignment_answered: no
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/characters, project/kourovka, status/conjectured]
---

# Verification — Kourovka 19.30

## The claim

Write

\[
 V_o(H)=\{|h|:h\in H,\ \chi(h)=0\text{ for some }\chi\in\operatorname{Irr}(H)\}.
\]

The submitted partial result is the fixed-target implication

\[
 |G|=168,\qquad V_o(G)=V_o(\operatorname{PSL}(2,7))
 \quad\Longrightarrow\quad G\cong\operatorname{PSL}(2,7).
\]

The independent computation reproduces this result in the installed order-168
SmallGroups catalogue. It is not the universal claim over every finite simple
target.

## Scope, revision, and clause matrix

The request and canonical record both name
`19.30/vanishing-order-simple-recognition`, revision 1. I directly inspected the
rendered source on PDF page 134. It defines a vanishing element by an exact zero of
an irreducible complex character and asks the universal same-order,
same-vanishing-order-set recognition question for a finite group and a finite simple
group. The canonical transcription is faithful.

| source clause | active? | fixed-target computation | remainder |
|---|---:|---|---|
| Vanishing means `chi(g)=0` for some `chi in Irr(G)` | yes | implemented by exact zero tests in every ordinary irreducible row | none inside the computed catalogue |
| Equal finite group orders | yes | target and all candidates have order 168 | all other simple-group orders |
| Same set of orders of vanishing elements | yes | exact sets, with multiplicity discarded | every other target |
| Universal simple-target recognition | yes | only `S=PSL(2,7)` | the active universal quantifier |

Thus `active_assignment_answered: no` regardless of the successful fixed-target
reconstruction.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | independent fixed-target evidence | result |
|---|---|---|---|---|
| `19.30-forall-GS` | admissibility | every admissible pair `(G,S)` | fixes `S=PSL(2,7)` | **not established universally** |
| `19.30-G-finite` | admissibility | `G` finite | enumerates `SmallGroup(168,i)` for all 57 installed representatives | pass in the fixed catalogue |
| `19.30-S-finite-simple` | admissibility | `S` finite simple | independently constructs `PSL(2,7)`, obtains size 168 and `IsSimpleGroup=true` | pass computationally |
| `19.30-vanishing-definition` | admissibility | zero of some ordinary irreducible complex character | scans every exact `ValuesOfClassFunction` row of `Irr(CharacterTable(G))` by class column | pass computationally |
| `19.30-equal-orders` | admissibility | `|G|=|S|` | target and every candidate guarded at 168 | pass in the fixed catalogue |
| `19.30-equal-vanishing-order-sets` | admissibility | set equality without multiplicity | compares exact sorted sets; equality occurs only at row 42 | pass for the implication test |
| `19.30-isomorphic` | target conclusion | `G isomorphic S` | row 42 is `[168,42]`; explicit `IsomorphismGroups` target guard passes; there are no other equality rows | established computationally only for the fixed catalogue |

The failed universal-coverage row forces `witness_equals_target: false` and caps the
scope-level verdict at `status/conjectured`.

## Target versus witness

The source and active target comprise all admissible pairs `(G,S)`. The
computational witness comprises only the single target `S=PSL(2,7)` and the 57
installed representatives of groups of order 168. Hence the witness is a strict
subclass of the canonical target.

Within that subclass, GAP reports `NumberSmallGroups(168)=57`, identifiers
`[168,i]` for all rows, and target identifier `[168,42]`. This is complete coverage
of the installed SmallGroups catalogue. It is still library-based computational
evidence, not an independent hand proof of the classification of groups of order
168.

## Circularity check

The 57 candidate groups are catalogue representatives selected solely by their
order, before their character zeros are inspected. They are not constructed from
the desired vanishing-order set. The target invariant is computed independently of
the comparison loop. Equality is used only after all character-table columns have
been scanned. Thus the zero-collision result is not true by construction.

Both implementations use GAP's group, character-table, and SmallGroups machinery,
so agreement does not independently certify those underlying algorithms or library
data.

## Sub-claims and what each method proves

| sub-claim | independent method | a pass proves | a pass does not prove |
|---|---|---|---|
| source and revision fidelity | visual PDF inspection plus canonical JSON | the computation tests the stated invariant and revision | any mathematical conclusion |
| target admissibility | construct `PSL(2,7)`; size, simplicity, identifier guards | the installed GAP target is simple of order 168 and row 42 | a tool-independent simplicity proof |
| order-168 coverage | require `NumberSmallGroups(168)=57`, iterate every index, guard every identifier | exhaustive installed-catalogue coverage | an independent classification theorem |
| invariant calculation | transpose exact irreducible-character value rows by class and record orders of columns containing zero | exact `V_o` values in GAP's character tables | correctness of GAP's character algorithms |
| collision decision | exact set comparison plus explicit target isomorphism guard | only row 42 has the target set in the 57 rows | recognition at another group order |
| independent agreement | compare all 57 `(index,V_o,equality)` records with the claimant artifact | two separately written implementations agree row for row | a universal proof |

## Evidence

### Frozen implementation and lease

No Validator GAP probe or mathematical enumeration preceded the freeze. The
claimant's discovery script was not opened or reused.

- independent checker SHA-256:
  `7d5af3a9e9e1f09412487b5e3cd3a5474898e7d4715a0f9c9d3a582e6652dd10`;
- runner SHA-256:
  `bc82bea9f3309372ccbdc3b0b885c0aa0bebfdb1de4bd13048d946c2fe553a84`;
- frozen manifest:
  `Agents/Kourovka/problems/19.30/verification/scratch/psl27-order168-independent-20260817/manifest.md`;
- Lead lease: slot 2 through `2026-08-17T15:44:30Z`, one run, one GAP
  process, 1.5 GiB ceiling, 900-second timeout plus 30-second kill grace.

The exact command, invoked once, was:

```text
/bin/bash Agents/Kourovka/problems/19.30/verification/scratch/psl27-order168-independent-20260817/run-independent.sh
```

It exited 0 after `7.766230608` seconds wall time. The runner redirected its full
verbatim output to persistent artifacts:

- `stdout.txt`: 125966 bytes, SHA-256
  `e4ec8de413c3f9d4ca0fce16609acb1ef9e5b0283d21b010b882da794be42819`;
- `stderr.txt`: empty, SHA-256
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`;
- `exit-status.txt`: `0`, SHA-256
  `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`.

### Verbatim decisive output

```text
RUN	VALIDATOR-INDEPENDENT-PSL27-ORDER168
GAP_VERSION	4.12.1
SMALLGRP_VERSION	1.5.3
CTBLLIB_VERSION	1.3.7
CATALOGUE_COUNT	57
TARGET	SIZE	168	IS_SIMPLE	true	ID_GROUP	[ 168, 42 ]
TARGET_VANISHING_ORDER_SET	[ 2, 3, 4, 7 ]
GROUP	42	ID_GROUP	[ 168, 42 ]	STRUCTURE	PSL(3,2)	NUMBER_OF_CLASSES	6	CLASS_ORDERS	[ 1, 2, 3, 4, 7, 7 ]	CLASS_SIZES	[ 1, 21, 56, 42, 24, 24 ]	IRREDUCIBLE_DEGREES	[ 1, 3, 3, 6, 7, 8 ]	ZERO_ROWS_BY_CLASS	[ [  ], [ 6 ], [ 2, 3, 4 ], [ 4, 6 ], [ 5 ], [ 5 ] ]	VANISHING_CLASS_POSITIONS	[ 2, 3, 4, 5, 6 ]	VANISHING_ORDER_SET	[ 2, 3, 4, 7 ]	EQUALS_TARGET_SET	true
SUMMARY	EXPECTED_COVERAGE	57	ACTUAL_COVERAGE	57	TARGET_ID	[ 168, 42 ]	TARGET_VANISHING_ORDER_SET	[ 2, 3, 4, 7 ]	EQUAL_SET_INDICES	[ 42 ]	NONISOMORPHIC_COLLISION_COUNT	0	NONISOMORPHIC_COLLISION_INDICES	[  ]
VALIDATION_COMPLETE	true
```

All 57 `GROUP` records are present in the linked stdout. Parsing them found exactly
57 records, exactly one true equality row, and:

```text
MATCHING_ROW=42 SET=[ 2, 3, 4, 7 ]
PARSED_GROUP_RECORDS=57 TRUE_EQUALITY_ROWS=1
```

Normalizing the claimant's and Validator's 57 `(index, vanishing-order set,
equality flag)` records and running `diff -u` produced no output and exit status
zero. Thus every one of the 57 invariant rows agrees, not only the final summary.

## Verdict

**`status/conjectured` for the canonical revision-1 scope.** The independently
frozen GAP computation reproduces the fixed finite result: in the installed
SmallGroups order-168 catalogue, `PSL(2,7)` has vanishing-order set
`[2,3,4,7]`, and the only group with that set is its own row `[168,42]`. This
bounded computational statement is independently replicated row for row.

**`witness_equals_target: false`.** The fixed target `PSL(2,7)` is not the
universal source target.

**`active_assignment_answered: no`.** Every other finite simple target remains
outside this computation, so no scope-level status promotion is made.

## Why this verdict

The separate implementation, frozen before any tool probe, recomputes the exact
character-zero invariant in a different data flow and agrees with the claimant on
all 57 rows. Every internal guard passed, stderr is empty, and the catalogue target
was separately checked isomorphic to the constructed `PSL(2,7)`.

Protocol nevertheless caps the active-scope verdict at conjectured because the
universal quantifier is not covered and `witness_equals_target` is false. Agreement
of two scripts sharing GAP libraries is replication of a bounded partial result,
not a proof of Kourovka 19.30.

## What is NOT established

- The universal recognition statement in Problem 19.30 is not established.
- No finite simple target other than `PSL(2,7)` is covered by this computation.
- No infinite family or structural recognition theorem is proved.
- The SmallGroups classification and GAP character-table algorithms are not
  independently proved or certified by this agreement.
- No nonisomorphic collision was found at order 168; this is not evidence that no
  collision exists at another simple-group order.
- Neither `status/proven` nor `status/solved` is warranted.

## What would upgrade it

The active assignment needs either a proof for every finite simple target or a
fully admissible nonisomorphic pair `(G,S)` satisfying every source constraint.
A separate canonical fixed-target scope could record the order-168 computation as
its own bounded target, but that would still not answer the present universal
scope; proof-level certification would additionally need a tool-independent
classification/character argument and the human-visibility gate.

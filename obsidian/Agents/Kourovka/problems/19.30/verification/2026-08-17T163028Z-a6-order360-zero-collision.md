---
title: "Verification — Kourovka 19.30 — A6 order-360 zero-collision partial"
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
scope_record: Agents/Kourovka/scopes/19.30-vanishing-order-simple-recognition.json
assignment_revision: 1
claim: "For every finite group G of order 360, if the set of orders of vanishing elements of G equals that of A6, then G is isomorphic to A6."
claimant: Problem-19.30
target_statement: "For every finite group G and finite simple group S, if |G|=|S| and G and S have the same set of orders of vanishing elements, then G is isomorphic to S."
excluded_scopes: ["Equality of character tables without equality of vanishing-order sets", "Equality of spectra of all elements rather than only vanishing elements", "Pairs in which neither group is finite simple"]
target_object: "Every pair (G,S) in the canonical universal scope."
witness_object: "The submitted GAP output for all 162 installed SmallGroup(360,i) representatives against fixed S=A6."
witness_equals_target: false
citation: "Installed GAP SmallGrp 1.5.3 manual, Chapter 1 sections 1.1 and 1.2; GAP Reference Manual 71.6-2 and 72.2-1/2."
verification_method: "Rendered-source audit, manual/API audit, strict frozen raw-artifact parser, and one failed-closed independent GAP reconstruction"
tools_used: ["GAP 4.12.1", "SmallGrp 1.5.3", "CTblLib 1.3.7", "Python 3.12.3", "Poppler pdftotext/pdftoppm"]
scope_answered: []
scope_not_answered: ["The fixed A6 order-360 implication is not independently replicated", "19.30/vanishing-order-simple-recognition universal scope", "All finite simple targets other than A6"]
active_assignment_answered: no
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/characters, project/kourovka, status/conjectured]
---

# Verification — A6 order-360 zero-collision partial

## The claim

For a finite group `H`, write

\[
V_o(H)=\{|h|:h\in H,\ \chi(h)=0\text{ for some ordinary }
\chi\in\operatorname{Irr}(H)\}.
\]

The submitted bounded claim is

\[
|G|=360,\qquad V_o(G)=V_o(A_6)\quad\Longrightarrow\quad G\cong A_6.
\]

The raw claimant artifact says `V_o(A6)=[2,3,4,5]` and that equality among
the 162 order-360 catalogue rows occurs only at `[360,118]`. The submitted
wrapper exited 1, so that wrapper's verdict was not inherited.

## Scope, revision, and clause matrix

The request and canonical record both name
`19.30/vanishing-order-simple-recognition`, revision 1. I visually inspected the
rendered source on PDF page 134. It defines a vanishing element by an exact zero
of some irreducible complex character and asks the universal same-order,
same-vanishing-order-set recognition question for a finite group and a finite
simple group.

| source clause | active? | submitted fixed-target result | remainder |
|---|---:|---|---|
| Vanishing means `chi(g)=0` for some irreducible complex `chi in Irr(G)` | yes | Claimed exact ordinary-character zero test | Independent reconstruction aborted before character values |
| Equal finite group orders | yes | Fixes both groups at order 360 | Every other simple-group order |
| Same set of orders of vanishing elements | yes | Raw rows claim equality only at 118 | Row structure was audited, but character values were not independently recomputed |
| Universal simple-target recognition | yes | Fixes only `S=A6` | Entire remaining universal quantifier |

Therefore `witness_equals_target:false` and
`active_assignment_answered:no`, independently of the computation failure.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | evidence in this review | result |
|---|---|---|---|---|
| `19.30-forall-GS` | admissibility | Every admissible pair `(G,S)` | Only `S=A6` and order 360 are considered | unknown universally |
| `19.30-G-finite` | admissibility | `G` finite | SmallGrp documents its available catalogue as complete irredundant finite-group representatives; independent GAP emitted catalogue count 162 but aborted before visiting rows | supported for the intended model, not independently enumerated |
| `19.30-S-finite-simple` | admissibility | `S` finite simple | `A6` has order `6!/2=360` and is simple by the standard theorem for `A_n`, `n>=5`; frozen control flow also passed size, simplicity, and ID guards before entering the failing target-invariant routine | pass for fixed target |
| `19.30-vanishing-definition` | admissibility | Exact zero of an ordinary irreducible complex character | Submitted script uses `Irr(CharacterTable(H))`; independent script required characteristic-zero table and intended `Irr(group)`, but failed at a redundant per-character API guard before any values | not independently verified |
| `19.30-equal-orders` | admissibility | `|G|=|S|` | Intended catalogue is order 360 and target is `A6` | supported for fixed model |
| `19.30-equal-vanishing-order-sets` | admissibility | Exact set equality, no multiplicities | Frozen parser reached the independent-output phase only after parsing the pinned submitted 162-row artifact, but the overall parser had no completion marker | conjectured, not replicated |
| `19.30-isomorphic` | target conclusion | Every admissible `G` is isomorphic to `S` | Submitted equality row is 118 and SmallGrp `IdGroup` semantics identify `[360,118]` with `A6`; independent invariant enumeration never reached row 1 | not independently established |

The linked claim-check file itself records `19.30-forall-GS:unknown`,
`19.30-isomorphic:not_proved`, and `ready_for_validator:false`. It is consistent
with a partial, but it cannot be a clean certification gate.

## Target versus witness

- Source target: all finite pairs `(G,S)` satisfying the source hypotheses.
- Active assignment: the same universal scope at revision 1.
- Submitted computational object: one fixed target `S=A6` and the installed
  order-360 SmallGroups catalogue.
- `witness = universal target`: false.
- `witness = fixed order-360 subcase`: the SmallGrp manual supports catalogue
  completeness and irredundancy for installed orders, and says `IdGroup(G)` returns
  `[order,i]` precisely when `G` is isomorphic to `SmallGroup(order,i)`. However,
  this review did not complete an independent invariant enumeration over those rows.

The relevant installed documentation is
`/usr/share/gap/pkg/SmallGrp/doc/chap1.txt` (complete irredundant catalogue,
`SmallGroup`, `NumberSmallGroups`, and `IdGroup`) and
`/usr/share/gap/doc/ref/chap71.txt` plus `chap72.txt` (actual conjugacy classes
stored on a group character table and alignment of class-function values with
those classes).

## Circularity check

The claimant selects candidates by order from the SmallGroups catalogue before
inspecting character zeros; the groups are not constructed by imposing the target
invariant. The comparison is therefore not tautological. The target row's
isomorphism follows from catalogue identification, while equality of its invariant
is a separate computation.

This removes the obvious circularity failure mode but does not replace an
independent character computation.

## Sub-claims and what each method proves

| sub-claim | method | what a pass proves | what it does not prove |
|---|---|---|---|
| Source and revision fidelity | rendered PDF plus canonical JSON | the right invariant and quantifiers are being discussed | any recognition result |
| Complete order-360 catalogue model | installed SmallGrp documentation plus `NumberSmallGroups(360)` | the installed catalogue count is 162 and its documented semantics are complete/irredundant | independent verification of the underlying classification data |
| `A6=[360,118]` and fixed-target admissibility | hand order/simplicity facts plus frozen GAP guards and `IdGroup` semantics | the intended target is the order-360 simple group at row 118 | its vanishing-order set |
| Submitted raw-output structure | frozen strict parser with pinned SHA-256 and explicit header-continuation normalization | if it completes, every row/flag/summary is internally consistent | correctness of the submitted character computations |
| Actual invariant for every group | independent actual-class-representative GAP checker | if complete, each order is taken from an actual class whose ordinary-character column has a zero | correctness of GAP libraries or the universal theorem |
| Cross-implementation equality | compare all 162 independent and submitted invariant rows | row-for-row computational replication of the fixed subcase | any other simple target |

The final two methods did not pass because the GAP reconstruction aborted before
the target invariant and the overall checker consequently exited nonzero.

## Evidence

### Probe and source

The tool probe returned:

```text
/usr/bin/gap
/usr/bin/python3
4.12.1
Python 3.12.3
```

Sage and Magma were absent from `PATH`. The rendered source text was:

```text
19.30. An element g of a finite group G is said to be vanishing if chi(g) = 0 for some
irreducible complex character chi in Irr(G). Must a finite group and a finite simple
group be isomorphic if they have equal orders and the same set of orders of vanishing
elements?
```

### Freeze and lease

The independent GAP checker, Python checker, runner, and hash file were frozen in
`Agents/Kourovka/problems/19.30/verification/scratch/a6-order360-independent-20260817/`.
Their hashes are recorded in `manifest.md`. Lead granted slot 2 through
`2026-08-17T16:46:09Z` for exactly one run.

The exact command was invoked once:

```text
/usr/bin/timeout --signal=TERM --kill-after=30s 960s /usr/bin/bash Agents/Kourovka/problems/19.30/verification/scratch/a6-order360-independent-20260817/run-independent.sh
```

It exited 1. No rerun or live patch occurred. Slot 2 was released effective
`2026-08-17T16:29:48Z`.

Pre-run hash output, verbatim:

```text
Agents/Kourovka/problems/19.30/verification/scratch/a6-order360-independent-20260817/independent-a6-order360.g: OK
Agents/Kourovka/problems/19.30/verification/scratch/a6-order360-independent-20260817/verify-independent.py: OK
```

GAP stdout, verbatim (the final bytes are ANSI error-state control codes):

```text
RUN	VALIDATOR-INDEPENDENT-A6-ORDER360
GAP_VERSION	4.12.1
SMALLGRP_VERSION	1.5.3
CTBLLIB_VERSION	1.3.7
DEFINITION	orders of actual class representatives whose aligned ordinary Irr(group) column has at least one exact zero
CATALOGUE_COUNT	162
```

GAP stderr, verbatim:

```text
Error, no method found! For debugging hints type ?Recovery from NoMethodFound
Error, no 1st choice method found for `UnderlyingCharacteristic' on 1 arguments at /usr/share/gap/lib/methsel2.g:249 called from
UnderlyingCharacteristic( character ) at Agents/Kourovka/problems/19.30/verification/scratch/a6-order360-independent-20260817/independent-a6-order360.g:68 called from
func( elm ) at /usr/share/gap/lib/coll.gi:1559 called from
ForAll( irreducibles, function ( character )
      return UnderlyingCharacteristic( character ) = 0;
  end ) at Agents/Kourovka/problems/19.30/verification/scratch/a6-order360-independent-20260817/independent-a6-order360.g:68 called from
<function "ActualVanishingData">( <arguments> )
 called from read-eval loop at Agents/Kourovka/problems/19.30/verification/scratch/a6-order360-independent-20260817/independent-a6-order360.g:135
type 'quit;' to quit to outer loop
Reading file "Agents/Kourovka/problems/19.30/verification/scratch/a6-order360-independent-20260817/independent-a6-order360.g" has been aborted.
```

The GAP process status file says `0`, but the error transcript and absent
`VALIDATION_COMPLETE` show that the script aborted. This is why process exit alone
is not accepted as evidence.

The Python checker then exited 1 because it encountered GAP's ANSI error residue
in the independent output:

```text
VERIFIER_FAILURE: unrecognized independent output line: '\x1b[1m\x1b[34m\x1b[0m\x1b[31m'
```

Its stack trace shows the failure in `parse_independent` after `parse_claimant`
returned. Thus the pinned claimant artifact survived the new parser's exact
single-header-continuation normalization and its internal 162-row checks, but the
manifest requires the overall checker to exit zero with a completion marker. That
requirement was not met.

Artifact SHA-256 values:

| artifact | SHA-256 |
|---|---|
| claimant raw output | `6142ece4f7daa7b08d330bce798fceade8e4de45a6b4a27637ff0364d051421e` |
| `gap-stdout.txt` | `857197693a495b96ea9ca1c9095679effdb683e887a86a7e8b79fde2ebbbc446` |
| `gap-stderr.txt` | `3275f66946c46192f3055667acc72e7f573c32c265369a2c8020496720f3b136` |
| `checker-stdout.txt` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `checker-stderr.txt` | `2fc343b6fe6c0cb71ef26fad70d47783990e7bf5f9a4bc5f749acb2d9dd76899` |

## Verdict

**`status/conjectured`.** The fixed `A6` order-360 zero-collision statement was
not independently replicated. The submitted raw artifact is structurally much
stronger than the failed original wrapper indicated: the frozen replacement parser
advanced past its pinned hash, repaired only the exact GAP header continuation,
and completed its internal submitted-row checks before failing on the separate
independent output. That does not independently recompute a single character value.

The independent GAP route failed for an API reason before emitting the target
invariant or any catalogue group row. This is neither evidence against the
mathematical claim nor a successful replication.

`witness_equals_target:false` and `active_assignment_answered:no`. No status above
conjectured is assigned, and the universal Problem 19.30 remains open in this work.

## Why this verdict

The lower threshold is forced by four independent gates:

1. The universal quantifier is absent from the fixed-target computation.
2. The claim-check file is explicitly not ready for Validator and leaves the
   universal and conclusion rows unresolved.
3. The submitted computation has only one mathematical implementation; the
   replacement parser checks its text, not its character theory.
4. The separately designed GAP implementation aborted before any invariant row,
   so the multiple-independent-computations threshold for `status/replicated` is
   not met.

## What is NOT established

- The fixed implication for `A6` and all groups of order 360 is not independently
  replicated or proved.
- The value `V_o(A6)=[2,3,4,5]` was not independently recomputed in this review.
- No one of the 162 submitted row invariants was independently recomputed.
- The universal recognition statement in Kourovka 19.30 is not established.
- No finite simple target other than `A6` is addressed.
- The SmallGroups classification data and GAP character algorithms are not
  independently proved by the submitted run or the documentation audit.
- No `status/replicated`, `status/proven`, or `status/solved` promotion is warranted.

## What would upgrade it

A new Lead decision could authorize a newly frozen checker that keeps the valid
table-level characteristic-zero guard and removes or replaces the unsupported
redundant call `UnderlyingCharacteristic(character)`. It would need a fresh lease,
complete all 162 actual-class/ordinary-character rows, exit zero with the strict
completion marker, and agree row for row with the submitted artifact. Such a pass
could replicate only the fixed `A6` partial; it still could not answer the universal
active assignment.

---
title: "Verification — Kourovka 19.30 — A6 order-360 zero-collision partial, v2"
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
scope_record: Agents/Kourovka/scopes/19.30-vanishing-order-simple-recognition.json
assignment_revision: 1
claim: "For every finite group G of order 360, if the set of orders of vanishing elements of G equals that of A6, then G is isomorphic to A6."
claimant: Problem-19.30
target_statement: "For every finite group G and finite simple group S, if |G|=|S| and G and S have the same set of orders of vanishing elements, then G is isomorphic to S."
excluded_scopes: ["Equality of character tables without equality of vanishing-order sets", "Equality of spectra of all elements rather than only vanishing elements", "Pairs in which neither group is finite simple"]
target_object: "Every pair (G,S) in the canonical universal scope."
witness_object: "Fixed S=A6 and all 162 installed GAP SmallGroups representatives SmallGroup(360,i)."
witness_equals_target: false
fixed_partial_verdict: replicated
citation: "Installed GAP SmallGrp 1.5.3 manual, Chapter 1 sections 1.1 and 1.2; GAP Reference Manual 71.6-2 and 72.2-1/2."
verification_method: "Separately frozen exact GAP enumeration using actual conjugacy-class representatives, followed by a strict independent cross-artifact checker"
tools_used: ["GAP 4.12.1", "SmallGrp 1.5.3", "CTblLib 1.3.7", "Python 3.12.3", "Poppler pdftotext/pdftoppm"]
scope_answered: ["Fixed computational subcase S=A6, |G|=360, over the complete installed SmallGroups order-360 catalogue"]
scope_not_answered: ["19.30/vanishing-order-simple-recognition universal scope", "Every finite simple target other than A6", "Any family-level recognition theorem"]
active_assignment_answered: no
supersedes_verification: Agents/Kourovka/problems/19.30/verification/2026-08-17T163028Z-a6-order360-zero-collision.md
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/characters, project/kourovka, status/conjectured]
---

# Verification — A6 order-360 zero-collision partial, v2

## The claim

For a finite group `H`, set

\[
V_o(H)=\{|h|:h\in H,\ \chi(h)=0\text{ for some ordinary }
\chi\in\operatorname{Irr}(H)\}.
\]

The submitted bounded statement is

\[
|G|=360,\qquad V_o(G)=V_o(A_6)quad\Longrightarrowquad G\cong A_6.
\]

The independently frozen computation replicates this statement in the installed
complete order-360 SmallGroups catalogue. It obtains

\[
A_6=[360,118],\qquad V_o(A_6)=\{2,3,4,5\},
\]

and row 118 is the unique one of all 162 rows with that invariant.

This is a fixed-target partial, not the universal statement of Kourovka 19.30.

## Scope, revision, and clause matrix

The request and canonical record both name
`19.30/vanishing-order-simple-recognition`, assignment revision 1. The rendered
source on PDF page 134 was inspected directly. It defines a vanishing element by
an exact zero of an irreducible complex character and asks the universal
same-order, same-vanishing-order-set recognition question for a finite group and
a finite simple group.

| source clause | active? | independent fixed-target computation | remainder |
|---|---:|---|---|
| Vanishing means `chi(g)=0` for some irreducible complex `chi in Irr(G)` | yes | Scans every exact characteristic-zero ordinary irreducible-character column | none inside the computed catalogue |
| Equal finite group orders | yes | Constructed target and all 162 candidates have order 360 | every other simple-group order |
| Same set of orders of vanishing elements | yes | Exact sets; multiplicities discarded; equality only at row 118 | every other target |
| Universal simple-target recognition | yes | fixes only `S=A6` | the active universal quantifier |

Thus `active_assignment_answered:no` even though the bounded computation passes.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | independent fixed-target evidence | result |
|---|---|---|---|---|
| `19.30-forall-GS` | admissibility | Every admissible pair `(G,S)` | fixes `S=A6` and order 360 | not established universally |
| `19.30-G-finite` | admissibility | `G` finite | enumerates every `SmallGroup(360,i)`, `1<=i<=162`, with size and ID guards | pass in fixed catalogue |
| `19.30-S-finite-simple` | admissibility | `S` finite simple | constructs `AlternatingGroup(6)`, obtains size 360, `IsSimpleGroup=true`, and ID `[360,118]` | pass computationally |
| `19.30-vanishing-definition` | admissibility | zero of some ordinary irreducible complex character | uses actual table-stored conjugacy classes and representatives; requires characteristic zero; scans all exact values in `Irr(group)` | pass computationally |
| `19.30-equal-orders` | admissibility | `|G|=|S|` | target and every candidate guarded at 360 | pass in fixed catalogue |
| `19.30-equal-vanishing-order-sets` | admissibility | equality of sets without multiplicity | exact target set `[2,3,4,5]`; equality index list `[118]` | pass for fixed implication test |
| `19.30-isomorphic` | target conclusion | `G isomorphic S` | unique equality row has ID `[360,118]`; explicit `IsomorphismGroups` guard passes | established computationally only for fixed catalogue |

The claimant's scope-level claim-check retains `19.30-forall-GS:unknown`,
`19.30-isomorphic:not_proved`, and `ready_for_validator:false`. Those entries are
correct for the universal assignment and prevent scope closure; they do not erase
the separately reviewed fixed finite partial.

## Target versus witness

- Source target: all finite pairs `(G,S)` satisfying the source hypotheses.
- Active assignment: the same universal scope at revision 1.
- Computational witness: only fixed `S=A6` and the 162 order-360 catalogue rows.
- `witness = universal target`: false.

Within the fixed subcase, the model is complete according to the installed
SmallGrp manual: for each available order the catalogue is a complete irredundant
list of isomorphism-type representatives. The same manual says `IdGroup(G)` is
`[order,i]` precisely when `G` is isomorphic to `SmallGroup(order,i)`. The
independent run also requires `NumberSmallGroups(360)=162` and verifies every
candidate ID `[360,i]`.

## Circularity check

The 162 candidates are selected only by order, before their character zeros are
computed. They are not constructed from the desired invariant. The target
invariant is computed from a separately constructed permutation group
`AlternatingGroup(6)` before comparison. Equality is tested only afterward.
Therefore the singleton result is not true by construction.

Both implementations share GAP's SmallGroups and character machinery. Their
agreement is independent implementation-level replication, not an independent
proof of those underlying libraries or classification data.

## Sub-claims and what each method proves

| sub-claim | independent method | what a pass proves | what it does not prove |
|---|---|---|---|
| Source and revision fidelity | visual PDF inspection plus canonical JSON | the right definition and revision are tested | any recognition result |
| Target admissibility and ID | construct `AlternatingGroup(6)`; size, simplicity, ID, and isomorphism guards | fixed target is the simple order-360 row 118 in GAP | a tool-independent proof of `IdGroup` data |
| Complete order-360 coverage | require count 162, iterate all indices, guard every size and identifier | exhaustive coverage of the installed complete catalogue | any other order |
| Actual vanishing-order invariant | align exact `Irr(group)` values with table-stored actual conjugacy classes and call `Order` on actual representatives | exact `V_o` values computed from actual elements and ordinary characters | correctness of GAP's character algorithms |
| Collision decision | exact set comparison and explicit target isomorphism guard | row 118 alone has the target set | recognition for another simple target |
| Independent agreement | strict parser reconstructs both artifacts and compares all 162 invariant rows | two separately designed computations agree row for row | the universal Kourovka statement |

## Evidence

### Frozen implementation and lease

The V1 run failed before its first invariant because GAP 4.12.1 does not accept a
direct `UnderlyingCharacteristic(character)` call. No V1 mathematical row was
accepted. Lead authorized a mechanical V2 only. The complete frozen diff changes
that query to
`UnderlyingCharacteristic(UnderlyingCharacterTable(character))`, advances every
output path, and adds GAP `--quitonbreak`; nothing mathematical changes.

V2 frozen hashes:

| file | SHA-256 |
|---|---|
| GAP checker | `49ba1996a27cdf69c39bc2481ace2df59e43436bfc7c71e1a9a9659bb11c1ed9` |
| Python checker | `8bb3fb2b7924ec41e98c701f6a9b802cf7d39bc5d0e178394ef0cf6510c89109` |
| runner | `27ac0709d5492b6590e2ac71a86bcaa0db41b20a0f88fc22604e5617f026b88c` |
| complete V1-to-V2 diff | `cba7b3b77ef9753790130d52a3fd7cbd6cb0110567b1eeda78936fd488ab386e` |

Lead granted slot 2 through `2026-08-17T16:57:25Z`. The exact command was invoked
once:

```text
/usr/bin/timeout --signal=TERM --kill-after=30s 960s /usr/bin/bash Agents/Kourovka/problems/19.30/verification/scratch/a6-order360-independent-v2-20260817/run-independent-v2.sh
```

Outer status, GAP status, and frozen Python-checker status were all 0. Both stderr
artifacts are empty. No patch or rerun occurred. Slot 2 was released effective
`2026-08-17T16:41:55Z`.

### Independent GAP result

The decisive output is verbatim:

```text
RUN	VALIDATOR-INDEPENDENT-A6-ORDER360
GAP_VERSION	4.12.1
SMALLGRP_VERSION	1.5.3
CTBLLIB_VERSION	1.3.7
DEFINITION	orders of actual class representatives whose aligned ordinary Irr(group) column has at least one exact zero
CATALOGUE_COUNT	162
TARGET	SIZE	360	IS_SIMPLE	true	ID_GROUP	[ 360, 118 ]
TARGET_CLASS_ORDERS	[ 1, 2, 3, 3, 4, 5, 5 ]
TARGET_ZERO_COUNTS	[ 0, 2, 1, 1, 3, 3, 3 ]
TARGET_VANISHING_CLASS_POSITIONS	[ 2, 3, 4, 5, 6, 7 ]
TARGET_VANISHING_ORDER_SET	[ 2, 3, 4, 5 ]
GROUP	118	SIZE	360	ID_GROUP	[ 360, 118 ]	NUMBER_OF_CLASSES	7
GROUP_CLASS_ORDERS	118	[ 1, 3, 2, 5, 5, 4, 3 ]
GROUP_ZERO_COUNTS	118	[ 0, 1, 2, 3, 3, 3, 1 ]
GROUP_VANISHING_CLASS_POSITIONS	118	[ 2, 3, 4, 5, 6, 7 ]
GROUP_VANISHING_ORDER_SET	118	[ 2, 3, 4, 5 ]	EQUALS_TARGET_SET	true
SUMMARY	CATALOGUE_COUNT	162	TARGET_INDEX	118	EQUAL_SET_INDICES	[ 118 ]	COLLISION_INDICES	[  ]
VALIDATION_COMPLETE	true
```

The full `gap-stdout-v2.txt` contains the class-order, zero-count,
vanishing-position, and invariant records for all 162 groups. It is 159628 bytes
with SHA-256
`0255083113fb207969a8cbf0bc1053e12979a9eb8e66963bde6ee0c7968567d3`.

### Strict cross-artifact result

The frozen checker first pins and repairs only the claimant's exact wrapped header,
then independently reconstructs every submitted flag and summary. It separately
validates the independent actual-class-order/zero-count derivation and compares all
162 row invariants. Its complete stdout is:

```text
CLAIMANT_SHA256	6142ece4f7daa7b08d330bce798fceade8e4de45a6b4a27637ff0364d051421e
INDEPENDENT_SHA256	0255083113fb207969a8cbf0bc1053e12979a9eb8e66963bde6ee0c7968567d3
PARSED_CLAIMANT_ROWS	162
PARSED_INDEPENDENT_ROWS	162
TARGET_ID	[360,118]
TARGET_VANISHING_ORDER_SET	[2,3,4,5]
EQUAL_SET_INDICES	[118]
COLLISION_INDICES	[]
ALL_162_INVARIANT_ROWS_AGREE	true
VERIFIER_COMPLETE	true
```

That artifact has SHA-256
`161671678f4f46550e4e410087da4a98ad773ed7faab2a481bae50f42415a8fc`.

## Verdict

**The bounded fixed-`A6`, order-360 catalogue statement is
`status/replicated`.** A separately designed exact computation reconstructs the
invariant from actual conjugacy-class representatives and ordinary irreducible
characters for all 162 catalogue rows, and all 162 rows agree with the claimant's
preserved GAP artifact. The unique equality index is 118, the `A6` row, so there
is no nonisomorphic order-360 collision with `A6` in this complete catalogue.

**The canonical revision-1 scope remains `status/conjectured`.** Its source target
is universal, while this witness fixes one simple group. Accordingly
`witness_equals_target:false` and `active_assignment_answered:no`; no scope-level
status promotion is made.

## Why this verdict

The fixed finite result meets the concrete-computation replication threshold:
the two implementations are separately written, use different data flows for
element orders and zero evidence, and agree on every row rather than only on a
summary. Internal guards check actual/table class alignment, class-size sums,
degree-square sums, ordinary characteristic, candidate identities, target
simplicity, and target isomorphism.

The universal target fails the witness-equality gate mechanically: one fixed
simple target cannot establish a statement quantified over every finite simple
group. Protocol therefore caps the canonical scope at conjectured.

## What is NOT established

- The universal recognition statement in Kourovka 19.30 is not established.
- No finite simple target other than `A6` is covered by this computation.
- No infinite family or structural recognition theorem is proved.
- The SmallGroups classification and GAP character-table algorithms are not
  independently proved by the agreement of two implementations sharing them.
- Absence of a collision at order 360 is not evidence of absence at another
  finite-simple order.
- Neither `status/proven` nor `status/solved` is warranted.

## What would upgrade it

The active assignment requires either a proof for every finite simple target or a
fully admissible nonisomorphic pair `(G,S)` satisfying every source constraint.
A separate canonical fixed-target scope could encode the replicated `A6` theorem
as its complete target, but the present universal scope cannot be upgraded from
this computation.

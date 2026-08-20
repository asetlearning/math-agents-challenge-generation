---
title: "Verification — Kourovka 20.115 — SU3(8) central-height obstruction"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
scope_record: Agents/Kourovka/scopes/20.115-nonzero-character-order-divisibility.json
assignment_revision: 1
claim: "For L=SU_3(8)=3.U3(8) at p=3, exactly principal-block rows 35--40 have degree 189 and height 3 and violate 3^h<=|D/Z|/exp(D/Z), while the other 76 ordinary rows pass."
claimant: Problem-20.115-Proof
target_statement: "For every finite group G, ordinary complex irreducible character chi, and x in G, chi(x) nonzero implies o(x)chi(1) divides |G|."
excluded_scopes: ["Brauer characters", "zero character values", "reducible characters", "solvable-only context", "the weaker fourth-power bound", "bounded table screens presented as universal proofs"]
target_object: "Every admissible triple (G,chi,x) in the universal Kourovka statement"
witness_object: "The ordinary table 3.U3(8) and the matrix group SU(3,8), used only to test an auxiliary 3-block central-height inequality"
witness_equals_target: false
citation: "Exact cover identity reconstructed below from the standard SU/PSU center and universal-cover theorem; no external bibliographic source was admitted by the clean-context task"
verification_method: "hand reconstruction plus one independently written, frozen, Lead-leased GAP 4.12.1/CTblLib 1.3.7 checker"
tools_used: ["GAP 4.12.1", "CTblLib 1.3.7", "Python 3.12.3", "sha256sum"]
scope_answered: ["bounded auxiliary central-height condition for SU3(8) at p=3"]
scope_not_answered: ["20.115/nonzero-character-order-divisibility"]
active_assignment_answered: no
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/replicated]
---

# Verification — Kourovka 20.115 — `SU3(8)` central-height obstruction

## The claim

The bounded claim is **replicated**: for
`L=SU_3(8)=3.U3(8)`, `p=3`, and `Z=Z(L)`, exactly ordinary-table
rows 35--40 fail

```text
3^h <= |D/Z|/exp(D/Z).
```

They are the six principal-block rows of degree `189` and height `3`, so
`27>81/9=9`. All other 76 rows pass their block thresholds.

This is only a failure of a proposed generic sufficient central-height input.
It is neither an answer to Kourovka 20.115 nor a refutation of Proposition 3.2.

## Scope, revision, and clause matrix

The locked scope is `20.115/nonzero-character-order-divisibility`, assignment
revision 1. The source PDF at page 161 asks whether, for every finite `G`,
ordinary irreducible complex `chi`, and `x` with `chi(x) != 0`, the exact order
`o(x)` divides `|G|/chi(1)`.

| source clause | active | what this claim establishes | result |
|---|---:|---|---|
| Universal nonzero-character-value order divisibility | yes | Nothing: no source-target triple `(G,chi,x)` is asserted | unanswered |
| Known solvable-group case | no | Nothing | excluded context |
| Known fourth-power general bound | no | Nothing | excluded context |
| Auxiliary central-height condition for `SU3(8)`, `p=3` | not a source clause | Exact six-row failure and 76-row pass count | replicated |

Therefore `active_assignment_answered: no`.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | candidate value / proof use | evidence | result |
|---|---|---|---|---|---|
| `20.115-forall-G-chi-x` | admissibility | Every admissible triple | One group, one prime, auxiliary block condition only | scope comparison | fail for active target |
| `20.115-G-finite` | admissibility | `G` finite | `SU_3(8)` of order `16547328` | hand formula and independent GAP | pass for bounded claim |
| `20.115-chi-complex-irreducible` | admissibility | Ordinary complex irreducible `chi` | All 82 ordinary CTblLib rows | `Irr(CharacterTable("3.U3(8)"))` | pass for bounded claim |
| `20.115-x-in-G` | admissibility | Exact `x in G` and exact `o(x)` | No proposed Kourovka witness; matrix elements only model a Sylow group | submission and checker | not used toward target |
| `20.115-character-value-nonzero` | admissibility | Exact `chi(x) != 0` | No proposed Kourovka witness | submission and checker | not used toward target |
| `20.115-order-degree-divisibility` | target conclusion | `o(x)chi(1) | |G|` | Neither proved nor violated | direct logical audit | unanswered |

The failed universal row and unanswered conclusion mechanically force
`active_assignment_answered: no`.

## Target vs witness

The target is a universal predicate on triples `(G,chi,x)`. The witness is a
single ordinary character table and matrix group used to test a different,
sufficient block-theoretic inequality. Thus the witness is **not** the target
in the sense required to answer the active scope.

The narrower identity of the two concrete group models is exact:

1. For `q=8`,
   `|SU_3(q)|=q^3(q^3+1)(q^2-1)=8^3*513*63=16547328`.
2. Scalar matrices in `SU_3(q)` have order
   `gcd(3,q+1)=gcd(3,9)=3`; hence `Z(SU_3(8))=C3` and the quotient has order
   `5515776`.
3. By definition this quotient is `PSU_3(8)`, denoted `U3(8)` in the table
   convention. The standard unitary central-cover theorem says that outside
   the small exceptional parameters, including here, `SU_3(q)` is perfect and
   is the universal central extension of `PSU_3(q)`, whose multiplier has
   order `gcd(3,q+1)`. Therefore the natural group is the unique perfect triple
   cover denoted `3.U3(8)`.
4. Independently, GAP constructed `SU(3,8)` with order `16547328` and center
   order `3`; CTblLib returned the table identifier `3.U3(8)`, the same order,
   three central conjugacy classes, 82 irreducibles, and the correct
   degree-square sum.

Order and center agreement alone would not identify a group; item 3 is the
identity theorem that closes that gap. Under the task's no-web, submitted-ref
boundary, its bibliographic provenance was not independently literature-audited.

## Circularity check

The ordinary table and the standard unitary matrix group are not constructed
from the threshold inequality. The independent checker queries their block and
matrix invariants before evaluating the inequality. Hence the six failures are
not true by construction. Both computations do share the installed CTblLib
dataset, so replication is at the checker/calculation level, not an independent
republication of the underlying character table.

## Sub-claims and what each method proves

| sub-claim | method | a pass proves | a pass does not prove |
|---|---|---|---|
| `SU_3(8)=3.U3(8)` | Hand center/quotient calculation and standard universal-cover theorem; invariant checks | Exact concrete group identity | The active universal divisibility claim |
| Block defects/membership/heights | Fresh frozen GAP checker, distinct row order and no claimant support-class calculation | Installed ordinary data and derived heights agree on all 82 rows | Independent correctness of CTblLib's source publication |
| Principal quotient | Explicit hand Sylow model and fresh GAP factor quotient | `|P/Z|=81`, `exp(P/Z)=9` | A statement for other unitary groups |
| Nonprincipal thresholds | Central-subgroup defect theorem plus defect orders | Defects 2 and 1 have quotient exponent/order `(3,3)` and `(1,1)` | The claimant's stronger choice of cyclic representatives for blocks 2--4 |
| 76/6 split | Complete 82-row loop plus normalized output comparison | Exactly the stated rows fail and all others pass | Any value/order pair in the source predicate |
| Logical consequence | Direct implication audit | The proposed generic sufficient input fails at `q=8` | Failure of Proposition 3.2 or of Kourovka 20.115 |

## Independent mathematical reconstruction

### Sylow quotient

The 3-part of the group order is

```text
513=3^3*19,  63=3^2*7,  so |L|_3=3^5=243.
```

Let `mu_9` be the norm-one scalars in `GF(64)^*`. The determinant-one
diagonal unitary torus is `T isomorphic to C9 x C9`. A permutation matrix for a
3-cycle normalizes `T`, lies in `SU_3(8)`, and gives
`P=T semidirect C3` of order `81*3=243`; hence `P` is Sylow.

The scalar center `Z=C3` lies in `T`, so `|P/Z|=81`. Every element of `T/Z`
has order dividing 9. For `t=diag(a,b,c)` with `abc=1` and the cyclic
permutation `w`,

```text
(tw)^3 = t w(t) w^2(t) = diag(abc,abc,abc) = 1,
```

and similarly for the other nontrivial Weyl coset. Thus `exp(P/Z)<=9`.
If `a` has order 9, `diag(a,a^-1,1)Z` has order 9: its cube cannot be scalar,
because its third entry is 1 while `a^3 != 1`. Therefore
`exp(P/Z)=9` exactly. The independent matrix computation agrees.

### Other block quotients

A central 3-subgroup is contained in every ordinary 3-block defect group.
Consequently a defect-2 group `D` has `|D|=9`, contains `Z` of order 3, and
`D/Z` has order and exponent 3. A defect-1 group equals `Z`, so its quotient
has order and exponent 1. This proves the threshold vector

```text
[81/9, 3/3, 3/3, 3/3, 1/1, 1/1, 1/1, 1/1, 1/1, 1/1]
= [9,1,1,1,1,1,1,1,1,1].
```

This argument intentionally avoids the submitted order-nine class-support
theorem. It proves exactly what the all-row threshold audit needs.

### Blocks, heights, and rows

The independent table query gives defects

```text
[5,2,2,2,1,1,1,1,1,1]
```

and row counts

```text
[37,9,9,9,3,3,3,3,3,3].
```

Put `a=v_3(|L|)=5`. For a row in a block of defect `d`, the ordinary height is

```text
h = v_3(chi(1)) - (a-d).
```

The independent checker derived this value from every degree and required it
to equal CTblLib's stored height. In the principal block `d=5`, rows 35--40
all have degree `189=3^3*7`, hence height 3. Each gives `3^h=27>9`.
Every other principal row has height 0 or 1 and passes. Blocks 2--4 consist of
degree `513=3^3*19` rows, hence height 0 and threshold 1. Blocks 5--10 consist
of degree `567=3^4*7` rows, hence height 0 and threshold 1. Therefore

```text
principal: 31 pass, 6 fail
defect 2:  27 pass
defect 1:  18 pass
total:     76 pass, 6 fail.
```

Equivalently, `v_3(|L:Z|)=4`, so for degree 189,
`(|L:Z|/189)_3=3`, while `exp(P/Z)=9>3`.

## Evidence

### Submitted artifact audit

The submitted hashes and sizes independently match:

```text
$ sha256sum .../su38_central_height_frozen.g .../su38_central_height_frozen.out
1f0610791c3cd7f7671804123cbc42076ea38091316807ac734b85c185f89d3b  .../su38_central_height_frozen.g
2e8545a02303a51cb63261f1ead9a52af086aa3b0bd4192de070992e6b2e8768  .../su38_central_height_frozen.out

$ wc -l .../su38_central_height_frozen.g .../su38_central_height_frozen.out
192 .../su38_central_height_frozen.g
294 .../su38_central_height_frozen.out
486 total
```

The output is 14508 bytes and internally records GAP 4.12.1, CTblLib 1.3.7,
82 row records, six `PASS=false` records, and termination at the intended
failure gate. A corrected static parser returned:

```text
{"records":82,"passes":76,"failures":6,"failure_records":[[35,1,189,3,3,27,9,false],[36,1,189,3,3,27,9,false],[37,1,189,3,3,27,9,false],[38,1,189,3,3,27,9,false],[39,1,189,3,3,27,9,false],[40,1,189,3,3,27,9,false]],"all_other_rows_pass":true}
```

The script's `LogTo` target is exactly the submitted output path, and the
script/output modification times precede the report. But the GAP log contains
no `ELAPSED`, `MAX_RSS_KB`, compute-slot, or lease record (`rg` returned exit
1 with empty output). Therefore the three permitted submitted refs bind the
claimed script to the claimed GAP transcript by exact hashes, but they do not
independently prove the claimant's asserted slot-2 allocation, 3.87-second
runtime, or 141952-KB maximum RSS. Those provenance facts remain
claimant-reported at this clean-context evidence boundary.

### Independent frozen run

Checker:
`Agents/Kourovka/problems/20.115/verification/scratch/2026-08-18-su38-independent.g`

```text
SHA-256 c3f56e2eb0bd57c1ec66e7cde8a30182545686200154d6226c27507917974f6c
122 lines, 4836 bytes
```

Its output path was absent before Lead granted slot 2. The exact authorized
one-time command was:

```bash
/usr/bin/time -f 'ELAPSED=%e MAX_RSS_KB=%M' timeout 45s gap -q -A -r Agents/Kourovka/problems/20.115/verification/scratch/2026-08-18-su38-independent.g
```

It returned exit status 0 and:

```text
ELAPSED=4.40 MAX_RSS_KB=141824
```

Complete verbatim GAP output is captured at
`Agents/Kourovka/problems/20.115/verification/scratch/2026-08-18-su38-independent.out`,
SHA-256
`d83ea633133eb512a81ad841298c27b0160bd53bec489e2d286b860c4e4a8953`,
174 lines and 10236 bytes. Its terminal summary is:

```text
TABLE_ID=3.U3(8) TABLE_ORDER=16547328 MATRIX_GROUP_ORDER=
16547328 CENTER_ORDER=3 SIMPLE_QUOTIENT_ORDER=5515776
BLOCK_DEFECTS=[ 5, 2, 2, 2, 1, 1, 1, 1, 1, 1 ] BLOCK_ROW_COUNTS=
[ 37, 9, 9, 9, 3, 3, 3, 3, 3, 3 ]
PRINCIPAL_QUOTIENT_ORDER=81 PRINCIPAL_QUOTIENT_EXPONENT=9
FAILURE_ROWS=[ 35, 36, 37, 38, 39, 40 ] PASS_COUNT=76 FAILURE_COUNT=6
END_INDEPENDENT_SU38_VALIDATION
```

Slot 2 was released immediately in
`Agents/Kourovka/bus/inbox/Lead/2026-08-18T010251Z__Validator-20.115-SU38__REPORT__release-slot2.md`.

### Cross-run comparison

The final comparator is
`Agents/Kourovka/problems/20.115/verification/scratch/compare_su38_outputs.py`,
SHA-256
`0d260e65950c0bc1ea44bed1293b5c0983b4b463bec7255916174ae4575984bc`.
It normalizes the different emission order (claimant by block, Validator by
row) and compares the seven fields `(row, block, degree, height, 3^height,
threshold, pass)`:

```text
$ python3 Agents/Kourovka/problems/20.115/verification/scratch/compare_su38_outputs.py
{"claimant_records":82,"validator_records":82,"records_identical":true,"claimant_passes":76,"validator_passes":76,"failure_rows":[35,36,37,38,39,40]}
```

Two initial static-regex probes returned zero records because their whitespace
pattern was overescaped; they were rejected. A first comparator one-liner had
a Python syntax error, and the first file comparator reported sequence
inequality because it had not sorted the claimant's block-order output against
the Validator's row-order output. None of those failed probes is used as
evidence; the linked final comparator makes the normalization explicit.

## Verdict

`status/replicated` for the bounded auxiliary claim.

`active_assignment_answered: no` for Kourovka 20.115, revision 1.

## Why this verdict

The claimant's frozen 82-row output and a separately written, Lead-leased
checker agree field-for-field after row normalization. The second checker
independently constructs the table and matrix group, derives every height from
the degree and block defect, computes the principal quotient exponent, and
uses a shorter theorem-level defect-order argument for every nonprincipal
threshold. The exact failure set and 76/6 count follow.

The certification is `replicated`, not `proven`, because both computations use
the same installed CTblLib table data and the no-web boundary prevents an
independent audit of its published provenance.

## What is NOT established

- No triple `(G,chi,x)` with `chi(x) != 0` is exhibited as violating the
  source divisibility statement.
- The universal statement in Kourovka 20.115 is neither proved nor refuted.
- Proposition 3.2 is not refuted. A sufficient hypothesis fails; the
  proposition's implication is untouched.
- No claim is made for another prime or another unitary group.
- The claimant's original slot allocation and `/usr/bin/time` measurements are
  not independently evidenced by the three submitted refs.
- The CTblLib source publication and the bibliographic statement of the
  unitary multiplier theorem were not independently literature-audited under
  the mandated clean-context/no-web boundary.

## What would upgrade it

An independent published character-table/block-data source or a separately
implemented table construction would strengthen the bounded result beyond
shared-CTblLib replication. Answering the active assignment would instead
require a line-by-line universal proof or one exact admissible
`(G,chi,x)` counterexample to the source predicate; this obstruction supplies
neither.

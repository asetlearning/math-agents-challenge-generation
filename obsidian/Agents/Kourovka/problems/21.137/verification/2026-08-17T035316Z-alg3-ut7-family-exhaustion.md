---
title: "Verification — Kourovka 21.137 — ALG3-UT7/F_12 family exhaustion"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "The doubly filtered frozen family ALG3-UT7-CUBE-IMAGE/F_12 contains no row whose actual cube set is a nonabelian subgroup."
claimant: Problem-21.137
target_statement: "For every odd prime p and finite p-group G of exponent exactly p^2, if the actual p-th-power value set is a subgroup, then it is abelian."
excluded_scopes: ["general powerfulness clause", "21.137/two-group-exponent-8", "all p=2 cases", "odd-prime groups of exponent other than exactly p^2"]
target_object: "All finite odd-prime p-groups of exponent exactly p^2 whose actual p-th-power set is a subgroup"
witness_object: "The parameter family G_tau=1+<S,T_tau> inside UT_7(F_3), restricted by endpoint-product inequality and dim J_tau<=12"
witness_equals_target: false
citation: "Kourovka Notebook, 21st issue (2026), Problem 21.137, rendered PDF p. 184"
verification_method: "rendered-source audit; hand algebra; artifact hashes; sanctioned graded-word audit; independent exact Python 3.12.3 full-matrix checker"
tools_used: ["GAP 4.12.1 (probe only)", "Python 3.12.3", "GNU sha256sum 9.4", "pdftotext", "pdftoppm"]
scope_answered: ["ALG3-UT7-CUBE-IMAGE/F_12 only; this is not a canonical source scope"]
scope_not_answered: ["21.137/odd-prime-exponent-p2", "the endpoint-equal low-dimensional rows", "all groups outside the frozen family"]
active_assignment_answered: no
operational_outcome: STRATEGY_EXHAUSTED
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/algebra-groups, project/kourovka, status/conjectured]
---

# Verification — frozen ALG3-UT7/F_12 family

## The claim

The submitted claim is a bounded strategy outcome, not a solution claim:

> For every `tau in F_3^6`, let `S` have all six first-superdiagonal entries
> equal to one, let `T_tau` have first-superdiagonal entries `tau`, and let
> `J_tau=<S,T_tau>`. Among the rows satisfying both
> `tau_1 tau_2 tau_3 != tau_4 tau_5 tau_6` and `dim J_tau<=12`, every actual
> cube set in `G_tau=1+J_tau` fails subgroup closure.

The hostile audit accepts that exact proposition. It does not accept any
enlargement to all 729 parameter rows, all dimension-at-most-12 groups, all algebra
groups in `UT_7(F_3)`, or the active Kourovka scope.

## Scope, revision, and clause matrix

The canonical record is current at assignment revision `2`. The source PDF was
read and rendered directly at page 184. Its three clauses are separated as
follows.

| source clause | active? | submission | result |
|---|---|---|---|
| If the power values form a subgroup, must it be powerful? | no | not addressed | excluded |
| For `p != 2`, exponent `p^2`, must the power subgroup be abelian? | yes | tests only the stated `p=3` frozen subfamily | `active_assignment_answered: no` |
| For exponent-8 two-groups, must the square subgroup be abelian? | no | not addressed | excluded |

The source target and canonical target agree on finiteness, odd prime, exponent
exactly `p^2`, the set of actual power values, the subgroup hypothesis, and the
abelian conclusion.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | family audit | result |
|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | every odd prime and every admissible group | only one fixed `p=3` subfamily was exhausted | not discharged; universal target open |
| `21.137-odd-p-not-2` | admissibility | prime `p>2` | `p=3` throughout | pass for retained rows |
| `21.137-odd-finite-p-group` | admissibility | finite `p`-group for the same prime | each retained `J_tau` has verified dimension `11`, so `|1+J_tau|=3^11` | pass for retained rows |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly `9` | `J_tau` is contained in strictly upper-triangular `7 x 7` matrices, so ninth powers are trivial; `S^3!=0` | pass for retained rows |
| `21.137-odd-power-set-definition` | admissibility | the actual cube set | every element is `1+x` and `(1+x)^3=1+x^3`; no generated-subgroup substitution occurs | pass as the exact set tested |
| `21.137-odd-power-set-subgroup` | admissibility | the actual cube set is a subgroup | all ten retained rows have a checked degree-three nonadditivity witness | fail for every retained row |
| `21.137-odd-P-abelian` | target conclusion | the actual cube subgroup is abelian | endpoint inequality makes `1+S^3` and `1+T_tau^3` noncommuting, but every such retained row fails the subgroup hypothesis | raw noncommutativity passes; no admissible counterexample |

No row passes all six admissibility gates and violates the conclusion. A
claim-check JSON is correctly absent because no `CLAIM` or stale match was made.

## Target versus witness

The source target ranges over all finite odd-prime groups meeting the exact
exponent and value-set hypotheses. The computed object is a fixed two-generator
algebra-group template at `p=3`. Therefore `witness_equals_target: false`.

The family-specific target is nevertheless exact. Its pre-filter parameter
universe is all `3^6=729` ordered tuples. Its membership definition includes
both:

1. endpoint-product inequality
   `tau_1 tau_2 tau_3 != tau_4 tau_5 tau_6`; and
2. `dim J_tau<=12`.

The independent checker found `21` rows of dimension at most `12` (three of
dimension `6`, eighteen of dimension `11`). Exactly ten also meet the endpoint
inequality. The other eleven low-dimensional rows are outside this frozen
family. Endpoint equality only says that the designated pair `S^3,T_tau^3`
commutes; it does not prove the whole cube set abelian. Thus those eleven rows
remain explicitly untested for a different noncommuting pair.

## Circularity and necessary-versus-sufficient checks

The groups are constructed from `S,T_tau`, the endpoint filter, and a dimension
cutoff, not from the subgroup property to be tested. The rejection certificate
is therefore not true by construction.

The leading-layer gate is only necessary for cube-set closure. The submission
uses its failure only to reject a row; it never treats a pass as sufficient.
This direction is sound and avoids the necessary/sufficient inversion.

The actual cube set is not replaced by the subgroup it generates. No row reached
the full cube-image computation because all ten family rows already failed a
decisive necessary condition.

## Sub-claims and what each method proves

| sub-claim | method | a pass proves | a pass does not prove |
|---|---|---|---|
| Source and active clause are exact | rendered PDF plus canonical scope | source fidelity and revision lock | mathematics |
| Manifest covers the parameter universe | canonical tuple-order check, line count, hash | all 729 ordered tuples occur once in the cited artifact | correctness of dimensions |
| `dim J_tau` is correct | two claimant implementations plus Validator full-matrix/right-word closure | exact dimensions for this template | anything outside this template |
| Endpoint gate is exact | hand path multiplication plus checker | the displayed cube pair is noncommuting exactly when endpoint products differ | abelianness when they are equal |
| Leading projection is exact | grading argument | every cube has degree-three projection in `C_tau`, and every element of `C_tau` occurs | full cube-image structure |
| Saved rejection pairs are valid | two independent checkers plus explicit formulas | actual cube-set closure fails in each retained row | a converse from leading additivity |
| Family has no target-equal candidate | conjunction of the preceding gates | exact frozen-family exhaustion | the active universal assertion |

## Hand verification of the algebraic implications

Let `J_tau` inherit the superdiagonal grading. It is a finite nilpotent
associative algebra over `F_3`, and `1+J_tau` is a group of order
`3^(dim J_tau)`. Since every product of seven strictly upper-triangular
`7 x 7` matrices is zero,

`(1+x)^9 = 1+x^9 = 1`.

Also `S^3=E14+E25+E36+E47` is nonzero. Hence `1+S` has order exactly `9`, so
every retained `G_tau` has exponent exactly `9`.

For the endpoint gate,

`S^3 T_tau^3 = (tau_4 tau_5 tau_6) E17`,

`T_tau^3 S^3 = (tau_1 tau_2 tau_3) E17`.

Thus the frozen endpoint inequality makes two actual cube values noncommuting.

Write an arbitrary `x in J_tau` as `x=x_1+x_{>=2}` by grade. The degree-three
part of `x^3` is `x_1^3`, and `x_1` lies in `span{S,T_tau}`. Conversely each
such degree-one vector is itself in `J_tau`. Therefore the degree-three
projection of the actual cube image is exactly

`C_tau={(aS+bT_tau)^3:a,b in F_3}`.

If `u=x^3` and `v=y^3`, then the degree-three part of their circle product
`u+v+uv` is the sum of their degree-three parts, because `uv` begins in degree
six. Consequently subgroup closure of the actual cube set forces additive
closure of `C_tau`. A saved pair whose sum is absent from `C_tau` is therefore a
complete rejection certificate for that row.

The ten saved certificates reduce to three transparent patterns: an exceptional
left endpoint, its reversal, and the alternating edge pattern. The
Validator-authored checker directly evaluated all ten saved coefficient pairs,
their cube codes, their sum codes, and absence of each sum from `C_tau`.

## Evidence

### Tool probe

```text
$ command -v gap; command -v sage; command -v python3; command -v magma; command -v jq; command -v sha256sum
/usr/bin/gap
/usr/bin/python3
/usr/bin/sha256sum
$ gap -q -c 'Print(GAPInfo.Version, "\\n"); QUIT;'
4.12.1
$ python3 --version
Python 3.12.3
$ sha256sum --version | head -n 1
sha256sum (GNU coreutils) 9.4
```

Sage, Magma, and `jq` were absent. GAP was probed only; it was not used in the
verification.

### Preserved artifact identity

```text
$ wc -l Agents/Kourovka/problems/21.137/runs/2026-08-17-r7-alg3-ut7-cube-image/manifest.jsonl
729 Agents/Kourovka/problems/21.137/runs/2026-08-17-r7-alg3-ut7-cube-image/manifest.jsonl
$ sha256sum Agents/Kourovka/problems/21.137/runs/2026-08-17-r7-alg3-ut7-cube-image/manifest.jsonl Agents/Kourovka/problems/21.137/runs/2026-08-17-r7-alg3-ut7-cube-image/sanctioned-independent-audit.json
66a3825559b07c7a87691d64ce5ca9c35bb151427248faa04014a10ddb2534e2  Agents/Kourovka/problems/21.137/runs/2026-08-17-r7-alg3-ut7-cube-image/manifest.jsonl
dc8f45aee5f784ddfb6c4a3c6f2a6765e25263c5ae9d724c227b11eac734107d  Agents/Kourovka/problems/21.137/runs/2026-08-17-r7-alg3-ut7-cube-image/sanctioned-independent-audit.json
```

The preserved sanctioned audit reports `PASS`, 729 rows, dimension distribution
`6:3, 11:18, 14:96, 15:180, 16:432`, ten retained rows, ten leading-layer
rejections, and zero survivors. Its implementation imports no primary code and
computes dimensions by graded word ranks.

The earlier output stored as `independent-audit.json` was produced without a
compute lease. It was excluded from this verdict and supplies no evidentiary
weight.

### Validator-authored independent reproduction

Lead leased slot 1 for exactly this command. The checker imports neither
claimant implementation. It uses generic full `7 x 7` matrix multiplication,
grows the algebra by right multiplication of independent word representatives,
and recomputes rank from scratch over `F_3`.

```text
$ timeout 60s python3 Agents/Kourovka/problems/21.137/verification/scratch/alg3_ut7_family_validator.py
{
  "audit": "PASS",
  "dimension_distribution": {
    "6": 3,
    "11": 18,
    "14": 96,
    "15": 180,
    "16": 432
  },
  "leading_layer_survivors": 0,
  "manifest_sha256": "66a3825559b07c7a87691d64ce5ca9c35bb151427248faa04014a10ddb2534e2",
  "retained_rows": 10,
  "retained_tau": [
    [0, 1, 1, 1, 1, 1],
    [0, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 2],
    [1, 2, 1, 2, 1, 2],
    [1, 2, 2, 2, 2, 2],
    [2, 1, 1, 1, 1, 1],
    [2, 1, 2, 1, 2, 1],
    [2, 2, 2, 2, 2, 0],
    [2, 2, 2, 2, 2, 1]
  ],
  "rows": 729,
  "status_counts": {
    "leading-layer not additive": 10,
    "outside F_12": 719
  }
}
exit status: 0
execution-tool wall time: 2.042545279 seconds
```

Exact stdout is preserved at
`Agents/Kourovka/problems/21.137/verification/2026-08-17T035114Z-alg3-ut7-third-checker-output.json`.

```text
checker SHA-256: 1c5affda5f968e210e67725a10fb3cdcf68bae58f7f94adb463b605ac2facd85
stdout SHA-256:  9765d4322f911a8cfdb54286ec80fbeee6400091c08ffba630960e8a0809448b
```

Slot 1 was released immediately after the run.

## Verdict

`STRATEGY_EXHAUSTED` is justified for exactly the doubly filtered
`ALG3-UT7-CUBE-IMAGE/F_12` family defined in the submission. The complete
729-row parameter audit leaves ten family members, and independent computation
plus hand derivation rejects all ten by explicit leading-layer nonadditivity.

`active_assignment_answered: no` is mandatory. The source target is larger than
the computed family, so the canonical mathematical status remains
`status/conjectured`; this verdict does not promote the unrestricted claim to
`status/replicated` or `status/proven`.

## Why this verdict

Three structurally separate computations agree on the finite data: the primary
full-matrix enumerator, the sanctioned graded-word checker, and the
Validator-authored full-matrix/right-word checker. The decisive logical bridge
from leading nonadditivity to failure of actual cube-set closure was also checked
by hand. The exact scope limitations are stated rather than inferred away.

## What is NOT established

- The active universal assertion is not proved or refuted.
- No admissible counterexample was found.
- The eleven dimension-at-most-12 rows with equal endpoint products are not
  excluded from having some other pair of noncommuting cube values.
- The 708 rows of dimension greater than `12` are outside the family.
- Nothing is established for other generators, other subalgebras of
  `UT_7(F_3)`, other matrix sizes, other odd primes, or non-algebra groups.
- Leading-layer additivity would not by itself establish subgroup closure; no
  such converse was tested or claimed.

## What would upgrade it

An upgrade of the active scope requires either a line-by-line universal proof or
a reconstructible group passing every canonical admissibility row while
violating the abelian conclusion. Testing endpoint-equal or higher-dimensional
rows would be a new, Lead-authorized family, not an extension of this verdict.

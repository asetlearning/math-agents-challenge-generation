---
title: "Verification — Kourovka 21.53 — fixed PSL(2,11) bounded equality"
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
scope_record: Agents/Kourovka/scopes/21.53-two-minimal-prime-colours.json
assignment_revision: 2
claim: "For the unique involution class D of PSL(2,11), Aut(Gamma)=Aut_2(Gamma) intersect Aut_3(Gamma), and both groups have order 1320."
claimant: Problem-21.53
target_statement: "For every finite nonabelian simple group L and every conjugacy class D of involutions in L, if Gamma is the complete product-order-coloured graph on D and p is the second-smallest distinct prime divisor of |L|, then Aut(Gamma)=Aut_2(Gamma) intersect Aut_p(Gamma)."
excluded_scopes: ["Problem 21.52", "unions of involution classes", "arbitrary choices of p", "promoting a bounded list of pairs to the universal conclusion"]
target_object: "Every pair (L,D) consisting of a finite nonabelian simple group and one complete involution conjugacy class"
witness_object: "The exact quotient SL(2,11)/{+I,-I}=PSL(2,11), with its complete 55-element involution class"
witness_equals_target: false
citation: "The witness is proved to be the stated fixed PSL(2,11) instance by the definition PSL(2,11)=SL(2,11)/Z(SL(2,11)) and the exhaustive centre, quotient, simplicity, and class proof below, but one instance is not the universal target."
verification_method: "fresh exact Python tuple-arithmetic checker; independent 12-point GAP action; separately encoded nauty/dreadnaut incidence structures"
tools_used: ["Python 3.12.3", "GAP 4.12.1", "nauty/dreadnaut 2.8.8", "Poppler 24.02.0"]
scope_answered: ["fixed instance (PSL(2,11),D) only"]
scope_not_answered: ["21.53/two-minimal-prime-colours universal quantifier", "every other finite nonabelian simple group/involution-class pair", "Problem 21.52"]
active_assignment_answered: no
outcome: PARTIAL_RESULT
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/graph-automorphisms, project/kourovka, status/replicated]
---

# Verification — fixed `PSL(2,11)` bounded equality

## The claim

The bounded report is correct: for the unique involution class `D` of
`PSL(2,11)`, the complete product-order colouring has 55 vertices and exactly the
four off-diagonal colours `2,3,5,6`, and

`Aut(Gamma) = Aut_2(Gamma) intersect Aut_3(Gamma)`

with both sides of order 1320. This is `status/replicated` for one fixed pair. It
does not answer the universal revision-2 assignment.

## Scope, revision, and clause matrix

The request and canonical record both name scope
`21.53/two-minimal-prime-colours`, revision 2. The rendered source PDF page 172
was independently inspected. Problem 21.53 inherits from 21.52 the finite
nonabelian simple group `L`, one involution class `D`, and the complete graph whose
edge relation is exact equality of product orders. The `G` used in 21.53 is the
inherited group.

| source clause | fixed-pair result | active universal scope |
|---|---|---|
| one complete involution class in a finite nonabelian simple group | pass for the exact `PSL(2,11)` model | not answered for all pairs |
| complete graph coloured exactly by `|ab|` | all 1,485 pairs reconstructed | not answered for all pairs |
| every-positive-integer definition of `Aut_t` | applied literally, including absent-label vacuity | definition retained |
| `Aut(Gamma)=intersection_t Aut_t(Gamma)` | only occurring colours `2,3,5,6` matter | definition retained |
| equality with the two smallest prime colours | pass for `2,3` in this pair | universal question open |
| Problem 21.52 induction by `Aut(L)` | not claimed or tested | excluded |

`active_assignment_answered: no` is forced by the undisposed universal quantifier.

## Constraint-and-conclusion matrix

| constraint_id | candidate / proof use | independent evidence | result |
|---|---|---|---|
| `21.53-forall-L-D` | one fixed pair | direct comparison with rendered universal source | **not discharged** |
| `21.53-L-finite-nonabelian-simple` | `SL(2,11)/{+-I}` | 1,320 determinant-one matrices; centre exactly `{+-I}`; 660 quotient elements; noncommuting generators; all seven nonidentity classes normally generate all 660 elements | pass for witness |
| `21.53-D-single-involution-class` | all quotient involutions | exactly 55 order-2 elements, one conjugacy orbit of size 55, centralizer order 12 | pass |
| `21.53-Gamma-product-order-colouring` | complete graph on that class | every one of `C(55,2)=1485` quotient products evaluated | pass |
| `21.53-Aut-t-definition` | relation preservation for every positive `t` | finite edge-set implication audited; absent relations impose no condition | pass |
| `21.53-two-minimal-primes` | `|L|=660=2^2*3*5*11` | exact quotient count and factorization | pass, `p=3` |
| `21.53-full-colour-group-definition` | preserve colours `2,3,5,6` | exact four-cell incidence structure | pass |
| `21.53-two-colours-determine-all` | compare full group with colours `2,3` | independent incidence groups both have order 1320; full group is automatically contained in the two-colour group | pass for fixed pair only |

## Target vs witness

The source target is universal; the witness is one exact instance. The finite
witness itself is identified without trusting its filename or claimant code:

1. Independent enumeration finds exactly 1,320 matrices of determinant one over
   `F_11`.
2. Exhaustive commutation against all 1,320 matrices gives centre exactly
   `I=(1,0,0,1)` and `-I=(10,0,0,10)`.
3. Canonicalizing each central pair gives 660 elements with exhaustively checked
   closure on all `660^2=435,600` ordered pairs and exact inverses. This is
   `SL(2,11)/Z(SL(2,11))=PSL(2,11)` by definition.
4. The classes have `(order,size,normal-closure-size)`
   `(1,1,1)`, `(2,55,660)`, `(3,110,660)`, `(5,132,660)`,
   `(5,132,660)`, `(6,110,660)`, `(11,60,660)`, `(11,60,660)`.
   A nontrivial normal subgroup contains a nonidentity conjugacy class; every such
   class generates the full 660-element group. Hence the group is simple.
5. The displayed determinant-one generators `s=(0,1,10,0)` and
   `u=(1,1,0,1)` generate all 660 quotient elements and do not commute, proving
   nonabelianness.

An independent GAP model on `P^1(F_11)` corroborates order, simplicity and the
class data. Its generators are `u:x -> x+1` and `s:x -> -1/x`. The projective
action is faithful on the quotient: a determinant-one matrix fixing every line
must be scalar (fix the two coordinate lines and their sum), hence lies in
`{+-I}` before quotienting.

The witness is therefore exactly the stated fixed `PSL(2,11)` instance, but it is
only one member of the target's universal class.

## Circularity

No tested object was constructed from the desired equality. The group arose from
all determinant-one matrices modulo its directly computed centre. The involution
set arose from exhaustive element orders and conjugation. The four edge relations
arose from all pair products. Only after those facts were frozen were the
automorphism structures built. Thus the equality is not true by construction.

## Subclaims and what each method proves

- Exact tuple arithmetic proves the quotient identity/order, all class and normal
  closure facts, all 55 vertices, all 1,485 colours, and their indexing. It does
  not say anything about another group.
- The independent projective GAP model corroborates the concrete group and class
  identity. It does not compute the claimant's matrix or colour groups.
- The two-relation incidence graph has one point cell of size 55 and relation
  cells of sizes 165 and 330. Its colour-preserving automorphism group is exactly
  `Aut_2 intersect Aut_3`.
- The full incidence graph has cells of sizes `55,165,330,660,330`; its group is
  exactly the full product-order-colour group.
- In either incidence model, a group element restricts faithfully to the point
  cell because every relation vertex is uniquely determined by its two point
  neighbours and relation cell. Conversely a point permutation preserving the
  encoded relations extends uniquely. Thus dreadnaut's incidence-group orders are
  the requested orders, not merely bounds or necessary-condition invariants.
- Since every full-colour automorphism preserves colours 2 and 3,
  `Aut(Gamma) <= Aut_2 intersect Aut_3`. The independently computed equal finite
  orders 1320 prove equality for this pair.

## Complete matrix, indexing, and hashes

Vertices are indexed `1..55` by increasing lexicographic canonical quotient tuple
`min(A,-A)`. The sequence begins
`(0,1,10,0),(0,2,5,0),(0,3,7,0),(0,4,8,0),(0,5,2,0)` and ends
`(5,6,3,6),(5,7,1,6),(5,8,5,6),(5,9,2,6),(5,10,4,6)`.
Unordered pairs are indexed lexicographically by `i<j`. The independently emitted
files contain 55 vertex rows, 1,485 pair rows, and the full symmetric 55-by-55
matrix with diagonal 1:

- `Agents/Kourovka/problems/21.53/verification/scratch/psl211/validator_vertices.tsv`
- `Agents/Kourovka/problems/21.53/verification/scratch/psl211/validator_unordered_edges.tsv`
- `Agents/Kourovka/problems/21.53/verification/scratch/psl211/validator_product_order_matrix.csv`

All three are byte-identical to the claimant artifacts, not merely equal in
summary:

| artifact | SHA-256 | independent comparison |
|---|---|---|
| `vertices.tsv` | `9c5f091980d4d8cb31c592f42d9cc8af92aee0747a3851b9122ccfff999942b0` | byte-identical |
| `unordered_edges.tsv` | `587f24029567ab255a6ced078e066c9e6307e613acd6a7530165214c76f97f2a` | byte-identical |
| `product_order_matrix.csv` | `8c37e927915a312ac4962d4cd762347102059d78ec53965da1ec9ec95829c74e` | byte-identical |

The other frozen claimant hashes were recomputed and all match the claimant
manifest: `build_psl211_matrix.py` =
`35de58e18081fdd9fb5ae1bfbbce702108074564ce75c2b85f203bb142afb887`,
`matrix_data.g` =
`4a0001b7bfc6e77a3a93d8d6cd490a73b106c301447376f1e19ac980968d0bf6`,
`summary.json` =
`540dc07722c94806142734153d48bf329a5ab4af1cf0f14746bb4b5229fb151a`,
and `compare_aut_groups.g` =
`34a946f10ef13758c1309dd2ff63004fdcedc921c586ba2c7caf8ce38ff5ab4b`.
The routed findings hash is
`f17fac0851bd0c3d25f408a0d4dcfcfa68d03abc2a013fc0d065cd094e9ff31b`.
Hash agreement for claimant code establishes immutability only; no claimant code
was executed or treated as correctness evidence.

The complete colour census is:

| product order | valency at every vertex | unordered edges |
|---:|---:|---:|
| 2 | 6 | 165 |
| 3 | 12 | 330 |
| 5 | 24 | 660 |
| 6 | 12 | 330 |

The valencies sum to 54 and the edge counts to 1,485. For every positive integer
`t` outside `{2,3,5,6}`, the antecedent `|ab|=t` never occurs, so every permutation
of `D` satisfies the defining implication and `Aut_t(Gamma)=S_55` vacuously.

## Evidence

### Tool and source probe

```text
$ command -v gap; command -v sage; command -v python3; command -v magma; command -v dreadnaut
/usr/bin/gap
/usr/bin/python3
/usr/bin/dreadnaut
$ gap -q -c 'Print(GAPInfo.Version,"\\n"); QUIT;'
4.12.1
$ python3 --version
Python 3.12.3
$ pdftotext -v
pdftotext version 24.02.0
```

Sage and Magma produced no path. The source command was:

```bash
source _meta/agents/Kourovka/paths.env
pdftotext -f 172 -l 172 -layout "$KOUROVKA_PDF" -
```

The relevant exact output, visually cross-checked against the rendered page, was:

```text
21.52. Let L be a finite non-abelian simple group, and let D be a conjugacy class
of involutions in L. Consider the complete graph Γ with vertex set D. Define an
equivalence relation ∼ (graph coloring) on the set of edges as follows: (a, b) ∼ (c, d)
if and only if |ab| = |cd|.

21.53. In the notation of 21.52, let Autt (Γ) be the set of permutations τ ∈ SD such
that (a, b) ∼ (aτ , bτ ) whenever |ab| = t for a, b ∈ D. Clearly, Aut(Γ) = ∩t Autt (Γ).
Is it true that for every finite simple group G we have Aut(Γ) = Aut2 (Γ) ∩ Autp (Γ),
where {2, p} are the two minimal prime divisors of |G|?
```

### Independent model run

Revision 1 was executed once and stopped before producing accepted evidence on an
ordering-only assertion:

```text
$ timeout 30s python3 Agents/Kourovka/problems/21.53/verification/scratch/psl211_independent_validator.py
Traceback (most recent call last):
  File "Agents/Kourovka/problems/21.53/verification/scratch/psl211_independent_validator.py", line 367, in <module>
    main()
  File "Agents/Kourovka/problems/21.53/verification/scratch/psl211_independent_validator.py", line 172, in main
    assert [row["normal_closure_size"] for row in class_data] == [1] + [660] * 7
AssertionError
```

The frozen revision-2 change only sorted the exhaustive class records by
`(element_order,representative)` before comparing them. Its exact accepted output:

```text
$ timeout 30s python3 Agents/Kourovka/problems/21.53/verification/scratch/psl211_independent_validator.py
PSL211_INDEPENDENT_MODEL_OK
PYTHON=3.12.3
SL2_ORDER=1320
SL2_CENTRE=[(1, 0, 0, 1), (10, 0, 0, 10)]
QUOTIENT_ORDER=660
CLOSURE_PAIRS_CHECKED=435600
GENERATOR_SUBGROUP_ORDER=660
GENERATORS_NONCOMMUTE=true
CLASS_ORDER_SIZE_NORMAL_CLOSURE=[(1, 1, 1), (2, 55, 660), (3, 110, 660), (5, 132, 660), (5, 132, 660), (6, 110, 660), (11, 60, 660), (11, 60, 660)]
SIMPLE_BY_NORMAL_CLOSURES=true
INVOLUTION_COUNT=55
INVOLUTION_CLASS_COUNT=1
INVOLUTION_CENTRALIZER_ORDER=12
PRIME_FACTORIZATION=2^2*3*5*11
SECOND_SMALLEST_DISTINCT_PRIME=3
UNORDERED_PAIRS_CHECKED=1485
COLOURS=[2, 3, 5, 6]
EDGE_COUNTS={2: 165, 3: 330, 5: 660, 6: 330}
VALENCIES={2: 6, 3: 12, 5: 24, 6: 12}
AUT_T_VACUITY=all absent positive labels impose no restriction, hence S_55
ARTIFACT_BYTE_IDENTICAL[vertices.tsv]=true SHA256=9c5f091980d4d8cb31c592f42d9cc8af92aee0747a3851b9122ccfff999942b0
ARTIFACT_BYTE_IDENTICAL[unordered_edges.tsv]=true SHA256=587f24029567ab255a6ced078e066c9e6307e613acd6a7530165214c76f97f2a
ARTIFACT_BYTE_IDENTICAL[product_order_matrix.csv]=true SHA256=8c37e927915a312ac4962d4cd762347102059d78ec53965da1ec9ec95829c74e
CLAIMANT_SUMMARY_FIELDS_MATCH=true
FROZEN_HASHES_ALL_MATCH=true
TWO_INCIDENCE_VERTICES=550
TWO_INCIDENCE_EDGES=990
TWO_DREADNAUT_SHA256=ddb8f7a97b5065c99b056b6abc40d13c137c3982b8cb28c1f165802ff8ac9b4b
FULL_INCIDENCE_VERTICES=1540
FULL_INCIDENCE_EDGES=2970
FULL_DREADNAUT_SHA256=ea6abf00ed463527105d8bde521f3d7f53579b53c25663504b27d3ee56c3e8d7
```

### Independent projective-action cross-check

```text
$ timeout 30s gap -q Agents/Kourovka/problems/21.53/verification/scratch/psl211_projective_gap_crosscheck.g
PSL211_PROJECTIVE_GAP_OK
GAP_VERSION=4.12.1
ORDER=660
IS_ABELIAN=false
IS_SIMPLE=true
CENTRE_ORDER=1
CLASS_ORDER_SIZE=[ [ 1, 1 ], [ 5, 132 ], [ 5, 132 ], [ 11, 60 ], [ 11, 60 ],
  [ 2, 55 ], [ 3, 110 ], [ 6, 110 ] ]
INVOLUTION_CLASS_COUNT=1
INVOLUTION_CLASS_SIZE=55
```

### Separately designed incidence checker

Both input hashes were frozen before execution. The first point-relation input
has SHA-256
`ddb8f7a97b5065c99b056b6abc40d13c137c3982b8cb28c1f165802ff8ac9b4b`;
the full-colour input has
`ea6abf00ed463527105d8bde521f3d7f53579b53c25663504b27d3ee56c3e8d7`.
Quiet wrappers only issue the documented `-a` command to suppress printed
generators, then read these unchanged inputs.

```text
$ timeout 60s dreadnaut < Agents/Kourovka/problems/21.53/verification/scratch/psl211/two_relations_quiet.dre
'.' is illegal - type 'h' for help
[fixing partition]
level 3:  289 cells; 292 orbits; 23 fixed; index 2
level 2:  32 cells; 36 orbits; 8 fixed; index 12
level 1:  3 orbits; 0 fixed; index 55
3 orbits; grpsize=1320; 5 gens; 14 nodes; maxlev=4
cpu time = 0.00 seconds
```

Exit code 0; observed wall time 0.093 seconds.

```text
$ timeout 60s dreadnaut < Agents/Kourovka/problems/21.53/verification/scratch/psl211/full_colours_quiet.dre
'.' is illegal - type 'h' for help
[fixing partition]
level 3:  720 cells; 790 orbits; 49 fixed; index 2
level 2:  62 cells; 90 orbits; 1 fixed; index 12
level 1:  5 cells; 6 orbits; 0 fixed; index 55
6 orbits; grpsize=1320; 4 gens; 12 nodes; maxlev=4
cpu time = 0.00 seconds
```

Exit code 0; observed wall time 0.085 seconds. The leading diagnostic is harmless:
the final vertex line's semicolon already exits graph-entry mode, making the next
period redundant. `[fixing partition]` and the complete search output show that
both frozen partitions were accepted.

All model and automorphism commands were bounded below 60 seconds and completed
below the heavy-job threshold; no compute-slot lease was needed. Frozen manifests
are in `Agents/Kourovka/problems/21.53/verification/scratch/`.

## Verdict

`status/replicated` for the fixed pair `(PSL(2,11),D)`.

## Why this verdict

The claimant's GAP/GRAPE computation and this fresh tuple-arithmetic plus
dreadnaut incidence computation are materially independent and agree on every
finite datum: object, class, vertex indexing, all 1,485 pair colours, relation
counts, two-colour group order, full-colour group order, and equality. The direct
containment-plus-equal-orders argument is sufficient for the fixed finite claim.
The protocol classifies an independently repeated concrete finite computation as
`replicated`, not `proven`.

## What is NOT established

- The universal equality in Problem 21.53 is not proved or refuted.
- No other finite nonabelian simple group or involution class is covered.
- Problem 21.52's separate induction question is untouched.
- The order-1320 automorphism group is not structurally identified, though that is
  unnecessary for the fixed equality.
- This finite replication supplies no extrapolation from `PSL(2,11)` to a family.

## What would upgrade it

Closing the active assignment requires either a gap-free proof for every admissible
pair, including vacuous-colour cases, or one admissible reconstructible pair with
strict inequality and an explicit separating permutation. A structural family
theorem would upgrade the scope of this partial result but would still need its own
independent review.

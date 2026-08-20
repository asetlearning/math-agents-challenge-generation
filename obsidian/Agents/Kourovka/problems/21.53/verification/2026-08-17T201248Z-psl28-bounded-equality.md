---
title: "Verification — Kourovka 21.53 — bounded PSL(2,8) equality"
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
scope_record: Agents/Kourovka/scopes/21.53-two-minimal-prime-colours.json
assignment_revision: 2
claim: "For L=PSL(2,8) and its 63-element involution class D, Aut(Gamma)=Aut_2(Gamma) intersection Aut_3(Gamma), and both sides have order 1512."
claimant: Problem-21.53
target_statement: "For every finite nonabelian simple L and every involution class D, the full product-order colour group equals Aut_2(Gamma) intersection Aut_p(Gamma), where p is the second-smallest distinct prime divisor of |L|."
excluded_scopes: ["Problem 21.52", "unions of involution classes", "an arbitrary prime in place of the second-smallest prime", "universal inference from a bounded list"]
target_object: "All admissible pairs (L,D) inherited from Problem 21.52."
witness_object: "SL(2,F_8)=PSL(2,8), represented by all determinant-one 2-by-2 matrices over F_2[x]/(x^3+x+1), with D all 63 nonidentity involutions."
witness_equals_target: false
citation: "Self-contained simplicity proof specialized to SL(2,8), plus complete finite reconstruction."
verification_method: "Fresh coefficient-arithmetic matrix model, complete product scheme, exhaustive nine-block/perfect-matching automorphism backtracker, and independent certificate/hash/generator audit"
tools_used: ["Python 3.12.3", "GAP 4.12.1 (probe and local GRAPE semantics only)", "GRAPE 4.9.0 documentation", "Poppler pdftotext 24.02.0"]
scope_answered: ["bounded instance (PSL(2,8),D) only"]
scope_not_answered: ["21.53/two-minimal-prime-colours universal quantifier"]
active_assignment_answered: no
outcome: PARTIAL_RESULT
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/graph-automorphisms, project/kourovka, status/replicated]
---

# Verification — bounded `(PSL(2,8),D)` equality

## The claim

The fixed-pair claim passes. Let `D` be the 63-element involution class in
`PSL(2,8)`. The occurring product orders are `2,3,7,9`, the second-smallest
distinct prime divisor of the group order is `p=3`, and

`Aut(Gamma) = Aut_2(Gamma) intersection Aut_3(Gamma)`

with common order 1512.

This is one bounded `PARTIAL_RESULT`. It is not a universal proof and it is not a
counterexample. The active revision-2 assignment remains unanswered.

## Scope, revision, and exact source conventions

The canonical record is revision 2. Rendered PDF page 172 was inspected visually,
not merely through text extraction. Problem 21.53 says, in the notation of 21.52:

- `L` is a finite nonabelian simple group and `D` is one conjugacy class of
  involutions in `L`;
- `Gamma` is the complete simple graph on `D`, with two edges equivalent exactly
  when their endpoint products have the same element order;
- for every positive integer `t`, `Aut_t(Gamma)` consists of the permutations
  sending every `t`-edge to a `t`-edge;
- `Aut(Gamma)=intersection_t Aut_t(Gamma)`; and
- the question is whether the factors for the two least distinct prime divisors
  `{2,p}` always suffice.

For `E_t={{a,b}:a,b in D, a!=b, |ab|=t}`, the source implication gives
`tau(E_t) subseteq E_t`. Because a permutation of `D` induces a bijection of all
unordered pairs, this containment is equality. Thus the checker correctly treats
`Aut_t` as the setwise stabilizer of `E_t`. If `E_t` is empty, the implication is
vacuous and `Aut_t=S_D`. In the fixed pair, both defining relations `E_2` and
`E_3` are nonempty.

| source clause | fixed-pair result | still open |
|---|---|---|
| inherited finite-nonabelian-simple `L`, one involution class `D`, exact product-order colouring | passes for the reconstructed pair | every other admissible pair |
| `Aut_t` for every positive label, including absent labels | exact implication and vacuity used | general cases |
| full group is the intersection over all occurring product orders | exact four-relation group checked | universal domain |
| two least distinct primes suffice | passes here for `2,3` | universal assertion |

`active_assignment_answered: no`.

## Constraint-and-conclusion matrix

| constraint_id | role | candidate/proof use | evidence | result |
|---|---|---|---|---|
| `21.53-forall-L-D` | admissibility/quantifier | one pair only | claim and verification are explicitly bounded | not answered universally |
| `21.53-L-finite-nonabelian-simple` | admissibility | exact determinant-one matrix group over `F_8` | order 504, trivial centre, explicit noncommuting pair, self-contained simplicity proof | pass for bounded pair |
| `21.53-D-single-involution-class` | admissibility | all nonidentity involutions | exactly 63; centralizer 8; one orbit of size 63 | pass |
| `21.53-Gamma-product-order-colouring` | admissibility | all 1,953 unordered distinct pairs | complete fresh 63-by-63 matrix | pass |
| `21.53-Aut-t-definition` | admissibility | setwise stabilizers of exact `E_t` | implication/bijection argument and complete relation checks | pass |
| `21.53-two-minimal-primes` | admissibility | `504=2^3*3^2*7` | distinct primes `2,3,7` | pass, `p=3` |
| `21.53-full-colour-group-definition` | admissibility | preserve `E_2,E_3,E_7,E_9` | all occurring colours found and all two-colour automorphisms checked on all pairs | pass |
| `21.53-two-colours-determine-all` | target conclusion | bounded equality only | exhaustive block/matching backtracker gives 1,512 maps, every one full-colour | pass for this pair only |

The routed artifact is a bounded `REPORT`, not a universal closing `CLAIM`. It did
not link a `claim-checks/<claim-id>.json`. As in the earlier bounded A6 review,
that prevents scope-closing use but does not prevent auditing and replicating the
expressly bounded finite statement.

## Target versus witness

The source target is the universal class of all admissible pairs. The witness is
one member of that class, so `witness_equals_target:false` and
`active_assignment_answered:no` are forced regardless of the strength of the
finite check.

The computational witness does equal the stated fixed object. It is not a quotient
or surrogate: the independent checker constructs the field, every determinant-one
matrix, every involution, and every product directly. Its sorted group members,
involution vertices, field tables, 63-by-63 matrix, and 1,953 labelled edges agree
entry-for-entry with the claimant's frozen certificate.

There is no circularity. The matrix model is defined independently of the desired
automorphism equality, and the validator's automorphism search is derived from the
independently reconstructed relations rather than the claimant's graph-oracle
output.

## Exact field, group identity, nonabelianity, and simplicity

The polynomial `x^3+x+1` has no root in `F_2`, hence is irreducible. The verifier
implements multiplication by coefficient convolution followed by the reductions
`x^3=x+1` and `x^4=x^2+x`; it checks associativity, both distributive laws, and one
inverse for each nonzero element. Thus the coefficient model is `F_8`.

There are 63 choices for a nonzero first column of a determinant-one matrix. For
each, determinant against the second column is a nonzero linear functional
`F_8^2 -> F_8`, so exactly eight second columns have determinant one. Hence
`|SL(2,8)|=63*8=504`; the exhaustive checker also verifies all `504^2` ordered
products and every inverse. A central matrix in `SL(2,8)` is scalar, say
`lambda I`, and `lambda^2=1`. Since `F_8^*` has odd order seven, `lambda=1`.
Therefore `SL(2,8)=PSL(2,8)`. The displayed matrices
`(0,1;1,0)` and `(0,1;1,1)` do not commute, so the group is nonabelian.

For completeness, simplicity does not rest on a filename or order lookup. Let
`G=SL(2,8)` act on the nine points of `P^1(F_8)`. The action is faithful because
the centre is trivial, and it is 2-transitive: translations are transitive on the
eight finite points, while inversion moves infinity. Let

`U={(1,t;0,1):t in F_8}`.

Then `U` is abelian and normal in the stabilizer of infinity, and its conjugates
generate `G` by elementary row operations. Also `G` is perfect: for
`h=diag(s,s^-1)` with `s!=1`, conjugating `u(t)` scales `t` by `s^2`, so every
element of `U` is a commutator because `s^2+1!=0`; conjugates of `U` then lie in
`G'` and generate `G`.

If `1!=N normal G`, primitivity and faithfulness force `N` to be transitive. For
each `g in G`, choose `n in N` taking infinity to its image under `g`; then
`ng^-1` lies in the point stabilizer, so normality of `U` there gives
`U^n=U^g`. Modulo `N`, all conjugates of `U` therefore have the same abelian image.
Since those conjugates generate `G`, `G/N` is abelian. Hence `G'<=N`; as `G'=G`,
we get `N=G`. Thus the reconstructed group is simple.

## The single involution class

Take `u=(1,1;0,1)`. Direct commutation in `SL(2,8)` gives

`C_G(u)={(1,b;0,1):b in F_8}`,

of order eight, so the conjugacy orbit of `u` has `504/8=63` elements.

Independently, a nonidentity involution in characteristic two has trace zero and
therefore has form `(a,b;c,a)` with `a^2+bc=1`. If `b=0`, there are eight choices
with `a=1`; if `b!=0`, each of the seven choices of `b` and eight choices of `a`
forces one `c`. This gives 64 trace-zero determinant-one matrices including the
identity, hence exactly 63 nonidentity involutions. The orbit is consequently the
entire involution set: `D` is one class, not a union.

## Complete product-order scheme

The verifier multiplies every unordered pair in the 63-element class and determines
the product order by repeated exact matrix multiplication. It obtains:

| product order | unordered edges | valency at every vertex |
|---:|---:|---:|
| 2 | 189 | 6 |
| 3 | 252 | 8 |
| 7 | 756 | 24 |
| 9 | 756 | 24 |

The counts total `1,953=binomial(63,2)`, and the valencies total 62. The complete
matrix agrees entry-for-entry with the claimant's certificate in the common sorted
matrix order. Its validator compact-JSON SHA-256 is
`535902654ae525683592c7e985a61201d87cf971495fba6643a896d54545edae`.

## Independent complete automorphism enumeration

The order-2 graph has exactly nine connected components, each a complete `K_7`.
Between every two different components, the order-3 relation is exactly a perfect
matching. These facts are checked from the fresh matrix, not assumed.

This structure gives a complete, small backtracker. Any permutation preserving
`E_2` must permute the nine `K_7` components. Fix the image of component 0 and its
internal bijection `f_0`. For each other source component `i` and proposed target
component `sigma(i)`, preservation of the perfect matching between components 0
and `i` uniquely forces the entire internal bijection `f_i`. The checker then tests
the perfect matching between every pair of nonzero components. It enumerates every
possible image component and all `7!` possible `f_0`, so no two-colour
automorphism is omitted.

The pruning counts by recursion depth are

`[45360,362880,24192,1512,1512,1512,1512,1512,1512,0]`.

Exactly 1,512 distinct permutations survive. Every survivor is then tested on all
1,953 unordered pairs and preserves not only orders 2 and 3 but also orders 7 and
9. Therefore

`Aut_2(Gamma) intersection Aut_3(Gamma) <= Aut(Gamma)`.

The reverse inclusion is definitional, so equality follows. The canonical sorted
set of all 1,512 zero-based image lists has SHA-256
`7b89ead0ee3d87fbcc7b37bff624681a29a1d915fad28a063122e2b50e503546`.

## Exact claimant incidence encodings

For a label set `C`, the claimant forms a bipartite incidence graph with separate
vertex-colour cells:

1. the 63 original vertices; and
2. for each `t in C`, one cell with one auxiliary vertex for every edge in `E_t`.

Each auxiliary vertex is adjacent to exactly its two endpoints. The generated GAP
file uses the exact independently rebuilt matrix and exact edge lists. Thus the two
encoding has cell sizes `63,189,252` and total 504 vertices; the full encoding has
cell sizes `63,189,252,756,756` and total 2,016 vertices.

GRAPE 4.9.0's installed `AutGroupGraph` documentation says that for a record
`rec(graph:=gamma,colourClasses:=cells)`, the automorphism group preserves the
colour classes classwise. Hence an incidence automorphism restricts to a
permutation preserving each selected `E_t`. Conversely, every such permutation
extends uniquely by sending the auxiliary node for `{a,b}` to that for
`{a^tau,b^tau}`. The restriction action is therefore exactly the named relation
automorphism group, not merely a subgroup or upper bound. The encoding has no
duplicate edge nodes within a colour cell.

The independent backtracker makes the final equality independent of GRAPE/nauty,
but this two-way argument verifies that the claimant's reported incidence groups
mean what the source definitions require.

## Hashes and explicit generators

All seven hashes logged for the successful claimant run recompute exactly:

| artifact | SHA-256 |
|---|---|
| model builder | `f75ad5500924cef6164fc651273ac69d23be87b0ff8c678c28366055177c81ea` |
| product scheme | `54bb450db146199b72e51b2e18b4b2b507075d50725cc0556f5293291a5f2e90` |
| repaired comparison wrapper | `3f96ab5def2a55fe273191e1abf9e99235705f095f01f08640e944eb8d5f6ff0` |
| revision-2 manifest | `e3c5f8454e3c255a2d05f6add3d09fd1edef2ce7812aee7497f530fd2a0a71bc` |
| generated GAP program | `4f79a301543cb8dd4182c841d162a3447867d87b88fa4fa2d5aa8c1f9263521e` |
| raw GAP output | `0c268fba97c75346c137355ec0bfa5f2d2da413a663496e8899175b578975c57` |
| parsed summary | `b88ae158725d2d997ad001e2579eaca94cbe1e6f1783470ef8e1600526505d54` |

The raw file has return code zero, exactly thirteen tagged fields, and empty stderr.
The summary's embedded input, wrapper, generated-program, and raw hashes equal the
direct values above.

The three explicit two-colour generators and four explicit full-colour generators
are stored as complete 63-point image lists in the hashed raw and summary files.
The verifier parsed every list and checked:

- each is a permutation of all 63 vertices;
- each two-colour generator preserves all 189 order-2 edges and all 252 order-3
  edges (and, as equality predicts, every order-7 and order-9 edge);
- each full-colour generator preserves all 1,953 product orders;
- breadth-first closure of the three two-colour generators has exactly 1,512
  elements;
- breadth-first closure of the four full-colour generators has exactly 1,512
  elements; and
- both generated permutation sets equal each other and equal the independent
  exhaustive 1,512-element backtracker set, element-for-element.

This verifies both the explicit generators and their completeness, rather than
merely checking that exhibited generators preserve the requested relations.

## Subclaims and method limits

| subclaim | method | a pass proves | a pass does not prove |
|---|---|---|---|
| field/group identity | coefficient arithmetic, full matrix enumeration, hand order/centre proof | exact `PSL(2,8)` model | another group or family |
| simplicity | specialized primitive-action/perfectness proof | bounded witness is admissible | graph equality |
| involution class | centralizer/orbit and independent total count | exactly one 63-element class | other classes/groups |
| product scheme | all 1,953 pairs | complete fixed matrix | a family formula |
| incidence semantics | restriction/unique-extension proof | exact groups represented by claimant encodings | oracle correctness by itself |
| equality/order | complete block/matching enumeration and all-pairs colour test | fixed-pair equality and common order 1512 | universal 21.53 |
| hashes/generators | direct hashes, relation tests, closure sets | artifact identity and displayed generator completeness | universal scope |

## Evidence

Independent checker:
`Agents/Kourovka/problems/21.53/verification/scratch/independent_psl28_validator.py`.
Its frozen SHA-256 is
`0c4b620c3ddb593862a8983fe21caa5402ce91ded432cbb392179083f159df6e`.

The first invocation failed closed after completing the mathematical reconstruction
because its GAP-assignment parser required exactly one newline before
`BuildIncidence`; the artifact contains two. Only that regex was changed to accept
arbitrary whitespace. No mathematical routine, input, or claimant artifact was
changed. The corrected bounded invocation used 7.35 seconds wall time and 24,028 KB
maximum resident memory, so it was not a heavy job and required no compute lease.

```text
$ timeout 60s /usr/bin/time -v python3 Agents/Kourovka/problems/21.53/verification/scratch/independent_psl28_validator.py Agents/Kourovka/problems/21.53/runs/2026-08-17-r2-psl28-two-colour-separation/scratch/psl28-product-scheme.json Agents/Kourovka/problems/21.53/runs/2026-08-17-r2-psl28-two-colour-separation/scratch/aut-comparison-r2.summary.json Agents/Kourovka/problems/21.53/runs/2026-08-17-r2-psl28-two-colour-separation/scratch/aut-comparison-r2.raw.txt Agents/Kourovka/problems/21.53/runs/2026-08-17-r2-psl28-two-colour-separation/scratch/aut-comparison-r2.generated.g Agents/Kourovka/problems/21.53/runs/2026-08-17-r2-psl28-two-colour-separation/scratch/compare_colour_groups.py Agents/Kourovka/problems/21.53/runs/2026-08-17-r2-psl28-two-colour-separation/scratch/build_psl28_scheme.py Agents/Kourovka/problems/21.53/runs/2026-08-17-r2-psl28-two-colour-separation/scratch/aut-comparison-manifest-r2.md
{
  "active_assignment_answered": false,
  "claimant_artifacts": {
    "full_generated_order": 1512,
    "full_generator_count": 4,
    "generated_matrix_and_edges_exact": true,
    "generator_groups_equal_independent_aut_set": true,
    "hashes": {
      "builder": "f75ad5500924cef6164fc651273ac69d23be87b0ff8c678c28366055177c81ea",
      "generated": "4f79a301543cb8dd4182c841d162a3447867d87b88fa4fa2d5aa8c1f9263521e",
      "manifest": "e3c5f8454e3c255a2d05f6add3d09fd1edef2ce7812aee7497f530fd2a0a71bc",
      "raw": "0c268fba97c75346c137355ec0bfa5f2d2da413a663496e8899175b578975c57",
      "scheme": "54bb450db146199b72e51b2e18b4b2b507075d50725cc0556f5293291a5f2e90",
      "summary": "b88ae158725d2d997ad001e2579eaca94cbe1e6f1783470ef8e1600526505d54",
      "wrapper": "3f96ab5def2a55fe273191e1abf9e99235705f095f01f08640e944eb8d5f6ff0"
    },
    "hashes_match_log": true,
    "incidence_encoding_fragments_present": true,
    "raw_returncode_zero_and_13_tags": true,
    "two_generated_order": 1512,
    "two_generator_count": 3
  },
  "class": {
    "centralizer_size": 8,
    "involutions": 63,
    "orbit_equals_all_involutions": true,
    "orbit_size": 63
  },
  "field": {
    "alpha_powers": [1, 2, 4, 3, 6, 7, 5],
    "associative": true,
    "distributive": true,
    "one_inverse_each_nonzero": true
  },
  "group": {
    "all_inverses": true,
    "center_size": 1,
    "closed_all_ordered_products": true,
    "nonabelian_witness": [[0, 1, 1, 0], [0, 1, 1, 1]],
    "order": 504
  },
  "prime": {
    "factorization": "504=2^3*3^2*7",
    "second_smallest_distinct": 3
  },
  "scheme": {
    "claimant_payload_exact_match": true,
    "colours": [2, 3, 7, 9],
    "edge_counts": {"2": 189, "3": 252, "7": 756, "9": 756},
    "matrix_compact_sha256": "535902654ae525683592c7e985a61201d87cf971495fba6643a896d54545edae",
    "valencies": {"2": 6, "3": 8, "7": 24, "9": 24}
  },
  "software": {
    "method": "coefficient-field plus block-matching backtracker",
    "python": "3.12.3"
  },
  "two_colour_structure": {
    "all_preserve_full_product_matrix": true,
    "automorphism_count": 1512,
    "backtrack_nodes_by_depth": [45360, 362880, 24192, 1512, 1512, 1512, 1512, 1512, 1512, 0],
    "canonical_automorphism_set_sha256": "7b89ead0ee3d87fbcc7b37bff624681a29a1d915fad28a063122e2b50e503546",
    "component_sizes": [7, 7, 7, 7, 7, 7, 7, 7, 7],
    "order2_components": 9,
    "order3_between_each_block_pair": "perfect matching"
  },
  "verdict_for_fixed_pair": "Aut(Gamma)=Aut_2(Gamma) intersection Aut_3(Gamma), common order 1512"
}
Elapsed (wall clock) time: 0:07.35
Maximum resident set size (kbytes): 24028
Exit status: 0
```

Tool/package probe:

```text
$ gap -q -c 'Print("GAP_VERSION=",GAPInfo.Version,"\\n"); LoadPackage("GRAPE"); Print("GRAPE_VERSION=",PackageInfo("grape")[1].Version,"\\n"); QUIT;'
GAP_VERSION=4.12.1
GRAPE_VERSION=4.9.0
```

## Verdict

`status/replicated` for the bounded `(PSL(2,8),D)` equality. Operational outcome:
`PARTIAL_RESULT`.

## Why this verdict

The claimant's finite result is reproduced by a separately designed implementation
whose field arithmetic, group construction, and complete automorphism enumeration
do not invoke the claimant's scripts or graph oracle. The entrywise certificate,
incidence semantics, artifact hashes, explicit generators, and generator
completeness all pass independent checks. The simplicity and single-class facts
also have self-contained proofs.

The certification is deliberately not `status/proven`: program policy reserves
that status for a human-seen proof, and the active notebook statement is universal
while this result concerns one pair.

## What is NOT established

The universal revision-2 scope is not answered. No other finite simple group, no
other involution class, and no infinite family is covered. The fixed pair is not a
counterexample. The missing bounded-report claim-check also means this artifact
cannot be repurposed as a scope-closing claim without a fresh protocol gate.

## What would upgrade it

An affirmative answer to the active assignment requires a gap-free proof for every
finite nonabelian simple group and every involution class, including cases with
absent 2- or `p`-edges. A negative answer requires one admissible pair and an
explicit permutation preserving the 2- and `p`-relations while changing another
occurring product-order colour.

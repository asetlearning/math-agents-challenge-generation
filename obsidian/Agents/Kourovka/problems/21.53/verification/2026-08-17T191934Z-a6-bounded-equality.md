---
title: "Verification — Kourovka 21.53 — bounded A6 class-2A equality"
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
scope_record: Agents/Kourovka/scopes/21.53-two-minimal-prime-colours.json
assignment_revision: 2
claim: "For L=A6 and its 45-element involution class 2A, Aut(Gamma)=Aut_2(Gamma) intersection Aut_3(Gamma), and both sides have order 1440."
claimant: Problem-21.53
target_statement: "For every finite nonabelian simple L and every involution class D, the full product-order colour group equals Aut_2(Gamma) intersection Aut_p(Gamma), where p is the second-smallest distinct prime divisor of |L|."
excluded_scopes: ["Problem 21.52", "unions of involution classes", "an arbitrary prime in place of the second-smallest prime", "universal inference from a bounded list"]
target_object: "All admissible pairs (L,D) inherited from Problem 21.52."
witness_object: "A6 as the 360 even permutations of six letters, with D the 45 double transpositions."
witness_equals_target: false
citation: none
verification_method: "Fresh standard-library exhaustive permutation model, independent GAP cross-check, and duad--syntheme structural order proof"
tools_used: ["Python 3.12.3", "GAP 4.12.1", "Poppler pdftotext 24.02.0"]
scope_answered: ["bounded instance (A6,2A) only"]
scope_not_answered: ["21.53/two-minimal-prime-colours universal quantifier"]
active_assignment_answered: no
outcome: PARTIAL_RESULT
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/graph-automorphisms, project/kourovka, status/replicated]
---

# Verification — Kourovka 21.53 — bounded `(A6,2A)` equality

## The claim

The bounded claim passes: for `L=A6` and its unique involution class `D` of 45 double transpositions, `p=3` and

`Aut(Gamma) = Aut_2(Gamma) intersection Aut_3(Gamma)`,

with both groups of order 1440. In fact the stronger bounded equality `Aut(Gamma)=Aut_2(Gamma)` holds.

This is a `PARTIAL_RESULT`, not an answer to the universal revision-2 assignment.

## Scope, revision, and clause matrix

The canonical record is revision 2. Rendered PDF page 172 was inspected visually. Problem 21.53 inherits from 21.52 a finite nonabelian simple group `L`, one involution conjugacy class `D`, and the complete graph on `D` coloured by exact product order. It defines `Aut_t` for every positive integer `t`, states the full intersection formula, and asks whether the two least prime divisors suffice.

| source clause | bounded result | still open |
|---|---|---|
| inherited object `(L,D,Gamma)` | exactly reconstructed for `(A6,2A)` | every other admissible pair |
| `Aut_t` for every positive `t`, including absent labels | definition and vacuity checked | nothing further for this pair |
| `Aut(Gamma)=intersection_t Aut_t(Gamma)` | checked for this pair | universal domain |
| equality for labels `2,p` | proved for this pair with `p=3` | universal assertion |

`active_assignment_answered: no`.

## Constraint-and-conclusion matrix

| constraint_id | role | candidate/proof use | evidence | result |
|---|---|---|---|---|
| 21.53-forall-L-D | admissibility | only `(A6,2A)` | the claim is explicitly bounded | not answered universally |
| 21.53-L-finite-nonabelian-simple | admissibility | literal even permutations on six letters | order 360; noncommuting pair; every nonidentity conjugacy class has normal closure 360; GAP independently returns `IsSimple=true` | pass for bounded pair |
| 21.53-D-single-involution-class | admissibility | all nonidentity order-2 elements | exactly 45, cycle type `2^2 1^2`, one `A6` orbit | pass |
| 21.53-Gamma-product-order-colouring | admissibility | complete 45-by-45 matrix | all 2025 entries computed; diagonal 1; 990 off-diagonal pairs have orders 2,3,4,5 | pass |
| 21.53-Aut-t-definition | admissibility | setwise stabilizer of each exact order relation | implication, bijectivity, and absent-label vacuity proved below | pass |
| 21.53-two-minimal-primes | admissibility | `|A6|=360=2^3*3^2*5` | prime divisors `[2,3,5]` | pass, `p=3` |
| 21.53-full-colour-group-definition | admissibility | intersection of occurring relations | exact four-cell encoding and definition checked | pass |
| 21.53-two-colours-determine-all | target conclusion | bounded equality only | structural upper and lower bounds both 1440 | pass for `(A6,2A)` only |

## Target vs witness

The source target is a universal domain of pairs. The witness is one member of that domain, so it is not equal to the universal target. This forces `active_assignment_answered: no` regardless of the strength of the finite calculation.

The computational witness does equal the stated bounded object: it is not a quotient or surrogate. The checker lists all 360 even permutations of six letters and selects all 45 nonidentity elements of order 2. Their only cycle type is `2^2 1^2`, and conjugation by the listed `A6` is transitive on them.

## Exact definitions, including vacuity

For a positive integer `t`, put

`E_t = {{a,b}: a,b in D, a != b, |ab|=t}`.

The source implication says that `tau in S_D` lies in `Aut_t(Gamma)` when `tau(E_t)` is contained in `E_t`. A permutation of `D` induces a bijection of the unordered pairs, so this containment is automatically equality. Thus `Aut_t(Gamma)` is exactly the setwise stabilizer of `E_t` and is a group. If `E_t` is empty, the implication has no instances and `Aut_t(Gamma)=S_D` vacuously.

Here the only occurring edge labels are `2,3,4,5`; every other positive-label factor is `S_45`. Consequently

`Aut(Gamma)=Aut_2 intersection Aut_3 intersection Aut_4 intersection Aut_5`.

## The two augmented encodings

For a label set `C`, form an incidence graph `X_C` whose vertex-colour cells are:

1. the 45 original vertices `D`; and
2. for each `t in C`, one separate cell containing a node `(t,e)` for every `e in E_t`.

Join `(t,{a,b})` only to `a` and `b`. A cell-preserving automorphism of `X_C` restricts to a permutation of `D` preserving every `E_t`, because the image of the unique auxiliary node on `{a,b}` is an auxiliary node of the same cell on the two image endpoints. Conversely, such a permutation of `D` has the unique extension `(t,{a,b}) -> (t,{a^tau,b^tau})`. The restriction map is therefore a group isomorphism, not merely a homomorphism or an upper bound.

The claimant's builder implements exactly this construction with fixed partition cells. The independently recovered sizes are:

| encoding | cells | total vertices | incidence edges | restriction group |
|---|---|---:|---:|---|
| two labels | `45,90,360` | 495 | 900 | `Aut_2 intersection Aut_3` |
| full | `45,90,360,180,360` | 1035 | 1980 | `Aut(Gamma)` |

Absent labels require no auxiliary cell because their `Aut_t` factor is the full symmetric group.

## Independent product matrix

The fresh checker computes all 2025 ordered products. Symmetry follows computationally and also from `yx=(xy)^{-1}` for involutions. Off the diagonal it obtains:

| product order | unordered edges | valency at every vertex |
|---:|---:|---:|
| 2 | 90 | 4 |
| 3 | 360 | 16 |
| 4 | 180 | 8 |
| 5 | 360 | 16 |

The independently generated matrix agrees entry-for-entry with the claimant's frozen matrix in their common lexicographic vertex order. GAP independently gives the same class and relation counts.

## Duad--syntheme reconstruction and upper bound

Write a duad for a two-subset of `{1,...,6}` and a syntheme for a partition into three duads. Associate the double transposition `(ab)(cd)`, with fixed points `e,f`, to the incident flag

`(ef, {ab,cd,ef})`.

This is a bijection between the 45 involutions and the 45 flags of the 15-duad/15-syntheme incidence graph `B`. Two distinct involutions commute, equivalently have product order 2, exactly when their flags share their duad or their syntheme. Therefore the colour-2 graph is the line graph `L(B)`.

The structural recovery is exact:

- `L(B)` has 30 maximal triangles and no 4-clique. They are precisely the 15 stars at duads and the 15 stars at synthemes. Every flag lies in exactly two of them.
- Intersecting maximal triangles reconstructs the connected cubic graph `B`. Because `B` is connected and bipartite, its two 15-element parts are intrinsic up to interchange.
- On either recovered duad part, two vertices have a common syntheme neighbour exactly when the two duads are disjoint. Thus the duad disjointness graph `KG(6,2)` is recovered.
- An intersecting family of duads has size at most 5. If all members share a point, equality gives its five-element point-star. If they do not share a point, take two members `{1,2},{1,3}` and a member omitting 1; it must be `{2,3}`, after which no fourth duad can meet all three. Hence the six point-stars are exactly the maximum independent sets of `KG(6,2)`.
- Every automorphism of `KG(6,2)` therefore permutes these six stars and acts faithfully on them, since a duad is identified by the two point-stars containing it. Hence its order is at most `6!=720`.

Every part-preserving automorphism of `B` injects into this duad action; a part-swapping coset can at most double its order. The maximal-triangle reconstruction injects `Aut(L(B))` into `Aut(B)`. Hence

`|Aut_2(Gamma)| = |Aut(L(B))| <= |Aut(B)| <= 2*720 = 1440`.

The checker also recovers the colour-2 distance spheres `(1,4,8,16,16)` and proves on every pair that

`distance 1,2,3,4 in L(B)  <->  product order 2,4,3,5`, respectively.

Thus every colour-2 automorphism already preserves every product-order colour.

## Lower-bound realization

The natural faithful action of `S6` on duads, synthemes, and flags gives 720 full-colour automorphisms; on the involution model these are conjugations, so they preserve product order.

The checker also constructs the following bijection `P` from duads to synthemes:

```text
12 -> 12/34/56    13 -> 14/25/36    14 -> 13/26/45
15 -> 16/24/35    16 -> 15/23/46    23 -> 16/23/45
24 -> 15/24/36    25 -> 13/25/46    26 -> 14/26/35
34 -> 12/35/46    35 -> 15/26/34    36 -> 13/24/56
45 -> 14/23/56    46 -> 16/25/34    56 -> 12/36/45
```

It checks all incidences and obtains `d in P(e)` if and only if `e in P(d)`. Hence

`delta(d)=P(d)` and `delta(S)=P^{-1}(S)`

defines an involutory part-swapping automorphism of `B`, inducing

`(d,S) -> (P^{-1}(S),P(d))`

on flags. Since product order is determined by distance in `L(B)`, this is a full-colour automorphism; the checker also verifies it directly on all 990 unordered pairs. Its coset with the natural `S6` is disjoint from the part-preserving subgroup. Therefore the full-colour group has at least `2*720=1440` elements.

Combining the bounds gives

`1440 <= |Aut(Gamma)| <= |Aut_2 intersection Aut_3| <= |Aut_2| <= 1440`.

All inequalities are equalities, proving both claimed group orders and the bounded equality.

## Subclaims and what each method proves

| subclaim | method | a pass proves | a pass does not prove |
|---|---|---|---|
| `A6` and `2A` are admissible | direct finite enumeration plus GAP | exact bounded object/class facts | anything for another simple group |
| complete product scheme | independent 45-by-45 tuple calculation | every relation for this class | a general family formula |
| augmentation restriction | two-way incidence-extension lemma | exact group represented by each augmented graph | correctness of an arbitrary graph-oracle order |
| order 1440 | triangle recovery, `KG(6,2)` upper bound, explicit polarity lower bound | exact bounded group orders independently of nauty | universal 21.53 |
| claimant artifact identity | entrywise matrix comparison | claimant and verifier used the same finite scheme | universal scope |

## Evidence

Independent checker: `Agents/Kourovka/problems/21.53/verification/scratch/a6_independent_check.py`.

```text
$ timeout 30s python3 Agents/Kourovka/problems/21.53/verification/scratch/a6_independent_check.py
MODEL
|S6|=720 |A6|=360 nonabelian=True
A6 conjugacy classes (cycle type,size)=[((1, 1, 1, 1, 1, 1), 1), ((2, 2, 1, 1), 45), ((3, 1, 1, 1), 40), ((3, 3), 40), ((4, 2), 90), ((5, 1), 72), ((5, 1), 72)]
nonidentity normal-closure sizes=[360, 360, 360, 360, 360, 360]; hence simple
involutions=45 cycle_types=[(2, 2, 1, 1)]
A6-conjugacy orbit on first involution=45
prime divisors=[2, 3, 5]; second-smallest p=3
PRODUCT MATRIX
matrix entries=2025; diagonal order={1}; unordered off-diagonal pairs=990
off-diagonal colours=[2, 3, 4, 5]
edge counts={2: 90, 3: 360, 4: 180, 5: 360}
valencies={2: [4], 3: [16], 4: [8], 5: [16]}
colour-2 distance spheres=(1, 4, 8, 16, 16)
distance -> product-order sets={1: {2}, 2: {4}, 3: {3}, 4: {5}}
base flag=56|12/34/56; representatives={1: {'flag': '12|12/34/56', 'product_order': 2}, 2: {'flag': '12|12/35/46', 'product_order': 4}, 3: {'flag': '13|13/25/46', 'product_order': 3}, 4: {'flag': '16|16/23/45', 'product_order': 5}}
DUAD--SYNTHEME RECONSTRUCTION
maximal triangles=30 K4s=0 memberships/flag=2
triangle-intersection graph: vertices=30 degree=3 parts=[15, 15]
common syntheme neighbour of two duads iff disjoint: PASS
duad-disjointness independence number=5; maximum families=6; all six point-stars: PASS
Thus part-preserving incidence automorphisms inject into S6 (<=720),
and all incidence automorphisms have order <=2*720=1440.
EXPLICIT PART-SWAPPING INCIDENCE AUTOMORPHISM
P(12)=12/34/56
P(13)=14/25/36
P(14)=13/26/45
P(15)=16/24/35
P(16)=15/23/46
P(23)=16/23/45
P(24)=15/24/36
P(25)=13/25/46
P(26)=14/26/35
P(34)=12/35/46
P(35)=15/26/34
P(36)=13/24/56
P(45)=14/23/56
P(46)=16/25/34
P(56)=12/36/45
P is bijective and d in P(e) iff e in P(d); the induced incidence duality is involutory.
induced flag permutation preserves all 990 product orders: PASS
Natural S6 gives 720 part-preserving full-colour automorphisms; the displayed
duality gives a disjoint coset, so |Aut(full colour)|>=1440.
Together with Aut(full)<=Aut_2<=Aut(line incidence)<=1440:
|Aut(full colour)|=|Aut_2|=|Aut_2 intersection Aut_3|=1440.
AUGMENTED INCIDENCE ENCODINGS
{'two': {'colours': (2, 3), 'cell_sizes': [45, 90, 360], 'vertices': 495, 'incidence_edges': 900}, 'full': {'colours': (2, 3, 4, 5), 'cell_sizes': [45, 90, 360, 180, 360], 'vertices': 1035, 'incidence_edges': 1980}}
Each edge-node has exactly its two original endpoints and its own colour cell;
therefore restriction/unique extension is a bijection with the named relation automorphism group.
AUT_t VACUITY
Occurring labels are 2,3,4,5. For every other positive t, E_t is empty,
so the implication defining Aut_t is vacuous and Aut_t=S_45.
```

Independent GAP cross-check: `Agents/Kourovka/problems/21.53/verification/scratch/a6_gap_crosscheck.g`.

```text
$ timeout 30s gap -q Agents/Kourovka/problems/21.53/verification/scratch/a6_gap_crosscheck.g
GAP_VERSION=4.12.1
Size(A6)=360 IsAbelian=false IsSimple=true
involution class count=1 sizes=[ 45 ]
unordered product-order counts=[ [ 2, 90 ], [ 3, 360 ], [ 4, 180 ],
  [ 5, 360 ] ]
valency profiles [2,3,4,5]=[ [ 4, 16, 8, 16 ] ]
```

Entrywise comparison with the frozen claimant matrix:

```text
$ python3 - <<'PY'
import json, runpy
checker = runpy.run_path('Agents/Kourovka/problems/21.53/verification/scratch/a6_independent_check.py')
permutations = checker['permutations']
parity = checker['parity']
perm_order = checker['perm_order']
compose = checker['compose']
identity = checker['IDENTITY']
a6 = tuple(g for g in permutations(range(6)) if parity(g) == 0)
d = sorted(g for g in a6 if g != identity and perm_order(g) == 2)
independent = [[perm_order(compose(x, y)) for y in d] for x in d]
with open('Agents/Kourovka/problems/21.53/runs/2026-08-17-r1-a6-two-colour-separation/scratch/output/a6_product_order_matrix.json', encoding='utf-8') as handle:
    claimant = json.load(handle)
print('same lexicographic 45-vertex order:', len(d) == len(claimant) == 45)
print('independent 45x45 matrix equals claimant artifact:', independent == claimant)
PY
same lexicographic 45-vertex order: True
independent 45x45 matrix equals claimant artifact: True
```

Frozen verifier hashes:

```text
$ sha256sum Agents/Kourovka/problems/21.53/verification/scratch/a6_independent_check.py Agents/Kourovka/problems/21.53/verification/scratch/a6_gap_crosscheck.g
ad4ac8f263361519d7fe5fcf89a15d3fe4da9c5ee5e3895988a74123557c7004  Agents/Kourovka/problems/21.53/verification/scratch/a6_independent_check.py
998ebc97a150e4f895ed6b7c5c82ecfe4e824641e6d7e57b8f69a5f7769cd36c  Agents/Kourovka/problems/21.53/verification/scratch/a6_gap_crosscheck.g
```

## Verdict

`status/replicated` for the bounded `(A6,2A)` equality. Operational outcome: `PARTIAL_RESULT`.

## Why this verdict

The claimant's nauty orders are matched by an implementation-independent structural proof, a fresh standard-library exhaustive model, and an independent GAP check of the underlying group/class/product data. The augmentation restriction maps were checked in both directions. No unproved projective-semilinear identification is needed.

The certification is deliberately not `status/proven`: the program reserves that status for a human-seen proof, and the active statement is universal while this result concerns one pair.

## What is NOT established

The universal revision-2 scope is not answered. No other finite simple group, no other involution class, and no infinite family is covered. This produces neither a counterexample nor a universal proof, and it does not address Problem 21.52.

## What would upgrade it

To answer the active assignment affirmatively requires a gap-free argument for every finite nonabelian simple group and every involution class, including all vacuous cases. A negative answer requires one admissible pair and an explicit permutation preserving the 2- and `p`-relations while changing another occurring colour.

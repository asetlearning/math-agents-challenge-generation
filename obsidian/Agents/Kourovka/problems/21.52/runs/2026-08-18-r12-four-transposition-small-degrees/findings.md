---
title: "Problem 21.52 partial result — four-transposition class in A_8 through A_13"
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
cycle: 12
outcome: PARTIAL_RESULT
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/alternating-groups
  - project/kourovka
  - status/conjectured
---

# Candidate exact boundary theorem: four transpositions in degrees 8--13

## Active target

Scope: `21.52/involution-class-product-order-colouring`

Assignment revision: 1.

Universal target: for every finite nonabelian simple group \(L\) and every
involution class \(D\), every permutation of \(D\) preserving every exact
product order is induced by an automorphism of \(L\) stabilizing \(D\).

This note treats **only** \(L=A_n\) and the single class
\[
 D_n=\{(a_1b_1)(a_2b_2)(a_3b_3)(a_4b_4):a_i,b_i\text{ all distinct}\},
 \qquad 8\le n\le13.
\]

## Bounded claim submitted for validation

For each \(n=8,9,10,11,12,13\), the full exact-product-order colour
automorphism group on \(D_n\) is exactly the natural \(S_n\)-action, and this
same labelled action is the restriction image of
\(\operatorname{Stab}_{\operatorname{Aut}(A_n)}(D_n)\). Thus equality holds
for all six assigned pairs. This is an independently derived bounded family
partial, not the universal answer to Problem 21.52.

## Class identity and the `Aut(A_n)` restriction image

Identify a vertex with a four-edge matching \(M\) of the complete graph on
\([n]\), and write \(t_M\) for the product of its four transpositions.

- Every \(t_M\) is an even involution. The \(S_n\)-class of cycle type
  \(2^4 1^{n-8}\) does not split in \(A_n\): its centralizer contains any one
  of its constituent transpositions, an odd permutation. Hence \(D_n\) is one
  \(A_n\)-class, not a union, and
  \[
  |D_n|=105\binom n8.
  \]
- For \(n\ge7\), \(n\ne6\), the standard automorphism theorem gives
  \(\operatorname{Aut}(A_n)=S_n\), with \(S_n\) acting by conjugation. This
  action stabilizes the unsplit cycle-type class \(D_n\).
- The action on \(D_n\) is faithful. Indeed, \(D_n\) generates \(A_n\) because
  it is a nontrivial conjugacy class in the simple group \(A_n\); an element of
  \(S_n\) acting trivially centralizes \(A_n\), whose centralizer in \(S_n\) is
  trivial. Therefore the restriction image is the labelled natural matching
  action of order \(n!\).

### Explicit `A_8` outer audit

There is no hidden larger outer action. GAP 4.12.1 returns

```text
Size(A8)=20160 Size(Aut(A8))=40320
involution class sizes=[ 210, 105 ]
representative=(1,2)(3,4) size=210
representative=(1,2)(3,4)(5,6)(7,8) size=105
inner size=20160 outer quotient size=2
```

The injective conjugation map \(S_8\to\operatorname{Aut}(A_8)\) already has
order 40320, hence is all of \(\operatorname{Aut}(A_8)\). Its odd coset is the
unique outer coset and preserves four-transposition cycle type. Equivalently,
the four-transposition class is also the unique involution class of size 105,
so every automorphism stabilizes it. The exact script and output are
`scratch/a8_outer_audit.g` and `scratch/a8_outer_audit.out`.

## Complete exact product-order relation

For two matchings \(M,N\), remove their common edges. The remaining coloured
union is a disjoint union of alternating paths and alternating even cycles.
An alternating path with \(a\) edges from \(M\) and \(b\) edges from \(N\)
contributes an \((a+b+1)\)-cycle to \(t_Mt_N\). An alternating \(2r\)-cycle
contributes two \(r\)-cycles. Consequently
\[
 |t_Mt_N|=\operatorname{lcm}\bigl(\{a+b+1:\text{path components}\}
 \cup\{r:\text{alternating }2r\text{-cycles}\}\bigr).
\]

This is also a classification of ordered-pair orbits after recording the
number of common edges: for fixed \(M\), its stabilizer
\((C_2\wr S_4)\times S_{n-8}\) is transitive on the \(N\)'s with a fixed
coloured-component multiset. Any component isomorphism extends over unused
points to an element of that stabilizer.

The independent enumerator generates all \(105\binom n8\) matchings, fixes one
\(M\), exhausts every \(N\ne M\), checks the component formula against the
literal permutation-product order, and records a representative, multiplicity,
order, and complete two-point colour-count array for every orbit. Thus the JSON
files `scratch/orbit-n8.json`, ..., `scratch/orbit-n13.json` encode the complete
colour relation, not a sample.

| \(n\) | \(|D_n|\) | pair orbits at a vertex | every occurring exact order |
|---:|---:|---:|---|
| 8 | 105 | 4 | 2, 3, 4 |
| 9 | 945 | 11 | 2, 3, 4, 5, 6, 7, 9, 10 |
| 10 | 4,725 | 30 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 21 |
| 11 | 17,325 | 43 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 20, 21 |
| 12 | 51,975 | 57 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 20, 21, 30 |
| 13 | 135,135 | 62 | 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 20, 21, 30 |

## A colour-definable rigid relation

For colours \(r,s\), define the intrinsic two-point number
\[
 N_{r,s}(M,N)=|\{Z\in D_n\setminus\{M,N\}:|t_Mt_Z|=r,
                                      |t_Nt_Z|=s\}|.
\]
Every exact-colour automorphism preserves the entire array
\((|t_Mt_N|,(N_{r,s}(M,N))_{r,s})\).

The exhaustive orbit tables show zero collisions of this array between the
ordered-pair stabilizer orbits in every degree 8 through 13. In particular,
the following relation \(R_n\) is intrinsic to the exact-order colouring:

- For \(n=8\), \(M\,R_8\,N\) means \(|M\cap N|=1\). This is simply the order-3
  colour; the four pair orbits show that no other type has order 3.
- For \(9\le n\le13\), \(M\,R_n\,N\) means \(|M\cap N|=3\). At \(n=9\) this
  is one orbit of product order 3. At \(n=10,11,12,13\) it is the union of two
  orbits: residual edges disjoint (order 2) or incident (order 3). Each target
  orbit has a unique complete \(N_{r,s}\)-array among all pair orbits, so this
  union is colour-definable. The full arrays, rather than hashes or selected
  entries, occur in the six orbit JSON files.

Therefore
\[
 \operatorname{Aut}_{\rm col}(D_n)\le \operatorname{Aut}(D_n,R_n).
\]

## Full automorphism group of the rigid relation

The script `scratch/matching_relation_dre.py` independently regenerates the
labelled vertex set and exact sparse adjacency list for \(R_n\). Nauty
`dreadnaut` 2.8.8 computes the full automorphism group of each input. The saved
outputs include its generators and exact group order.

| \(n\) | vertices | degree of \(R_n\) | edges | full \(|\operatorname{Aut}(R_n)|\) |
|---:|---:|---:|---:|---:|
| 8 | 105 | 32 | 1,680 | 40,320 = \(8!\) |
| 9 | 945 | 8 | 3,780 | 362,880 = \(9!\) |
| 10 | 4,725 | 20 | 47,250 | 3,628,800 = \(10!\) |
| 11 | 17,325 | 36 | 311,850 | 39,916,800 = \(11!\) |
| 12 | 51,975 | 56 | 1,455,300 | 479,001,600 = \(12!\) |
| 13 | 135,135 | 80 | 5,405,400 | 6,227,020,800 = \(13!\) |

This is not an inference from equal orders alone. On the same saved matching
labels, every \(\sigma\in S_n\) acts by
\(M\mapsto\sigma(M)\); this action is faithful and preserves common-edge count,
so the natural \(S_n\) is an explicitly identified subgroup of
\(\operatorname{Aut}(R_n)\). The adjacent point-transposition generators were
regenerated and checked as bijections of every full label set. Since the exact
full relation group has order \(n!\),
\[
 \operatorname{Aut}(D_n,R_n)=S_n
\]
as this labelled action.

Finally, conjugation gives
\(|t_{\sigma(M)}t_{\sigma(N)}|=|\sigma t_Mt_N\sigma^{-1}|=|t_Mt_N|\),
so this same natural \(S_n\) lies in the full colour group. The two containments
are therefore
\[
 S_n\le\operatorname{Aut}_{\rm col}(D_n)
     \le\operatorname{Aut}(D_n,R_n)=S_n.
\]
Together with the restriction-image identification above, this gives the
claimed equality of permutation groups, not merely equality of their orders.

## Small-degree largest-clique audit

The usual largest-core-clique reconstruction cannot be applied uniformly:

- At \(n=8\), distinct four-matchings cannot share three edges; the share-three
  graph is empty. This is a complete failure of that argument, and the separate
  order-3/common-one relation \(R_8\) is used.
- At \(n=9\), a fixed three-matching has only
  \(\binom{3}{2}=3\) extensions. These triangles are the core stars. A
  Johnson-type top of at least three vertices would force five mutually disjoint
  transpositions and hence ten points, so it does not exist. This degree still
  needs its own triangle-level audit.
- At \(n=10,11,12,13\), a fixed three-matching gives a clique of size
  \(\binom{n-6}{2}=6,10,15,21\), respectively, whereas a Johnson top has size at
  most 5. Thus core stars are the unique largest type from \(n=10\) onward.

The exact relation-group computations above cover all three regimes and do not
assume a uniform largest-clique theorem.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | value / proof use | evidence | result |
|---|---|---|---|---|---|
| `21.52-forall-L-D` | admissibility | every admissible \((L,D)\) | Only six specified pairs \((A_n,D_n)\), \(8\le n\le13\), are treated. | Active-target section | **not discharged universally; bounded partial only** |
| `21.52-L-finite-nonabelian-simple` | admissibility | \(L\) finite nonabelian simple | \(L=A_n\), \(8\le n\le13\). | Standard simplicity theorem | pass for all six pairs |
| `21.52-D-single-involution-class` | admissibility | one class, elements order 2 | Unsplit class \(2^4 1^{n-8}\), exactly the four-matchings. | Class-identity argument; A8 GAP audit | pass for all six pairs |
| `21.52-Gamma-complete-on-D` | admissibility | all unordered distinct pairs | Every ordered orbit off the diagonal was exhaustively enumerated; multiplicities sum to \(|D_n|-1\). | `scratch/orbit-n*.json` | pass for all six pairs |
| `21.52-edge-colour-exact-product-order` | admissibility | colour iff exact \(|ab|\) agrees | Literal permutation-product orders cross-checked against the alternating-component formula on every orbit. | `scratch/orbit_audit.py`; six JSON files | pass for all six pairs |
| `21.52-tau-preserves-all-edge-colours` | admissibility | arbitrary permutation preserving every colour | Such a \(\tau\) preserves every \(N_{r,s}\), hence preserves \(R_n\). | Definability section and exhaustive arrays | pass as the arbitrary hypothesis in the bounded argument |
| `21.52-tau-induced-by-AutL` | target conclusion | every such \(\tau\) extends from \(\operatorname{Aut}(L)\) stabilizing \(D\) | \(\operatorname{Aut}_{\rm col}(D_n)=S_n=\operatorname{res}_{D_n}\operatorname{Aut}(A_n)\) as the same labelled action. | Two containments plus exact full relation groups | candidate-established for the six pairs; unknown universally |

## Reproducibility and exact object computed in

The exact objects were the complete sets of four-edge matchings on labelled
\([n]\), \(8\le n\le13\), identified above with the actual full classes
\(D_n\subset A_n\). Pair data were reduced only by a proved full
\(S_n\)-stabilizer orbit classification; no vertices or pair types were sampled.
The sparse relation graphs contain all vertices and all relation edges.

The fail-fast aggregate certificate is `scratch/boundary-certificate.json`
(SHA-256 `1489748b454e07e738087b04e64e97ed7c96ca763914e3c0a46d1c8c5880ef91`).
Its checker `scratch/certify_boundary.py` has SHA-256
`497f7590be6be9987646281e16e47f4169c268f6946095ec8b586b5c73b005c8`
and prints `PASS degrees=8..13 all exact gates`. Exact per-degree hashes of all
orbit JSON, dreadnaut input, and dreadnaut output files are embedded in the
certificate. Python was 3.12.3, nauty was 2.8.8, and GAP was 4.12.1.

## What this does NOT establish

- It does not discharge the universal quantifier over all finite nonabelian
  simple groups and all involution classes.
- It says nothing about the four-transposition family for \(n\ge14\); no result,
  table, or constant from the preceding unreviewed lane was used as a premise.
- It says nothing about any other involution class of \(A_n\), any union of
  classes, Problem 21.53, or colouring by the conjugacy class of a product.
- The exact nauty computations and the bespoke enumeration still require an
  independent Validator reconstruction before the bounded theorem is accepted.

## How this could be wrong

1. The assertion that the coloured alternating-union key is a complete orbit
   invariant for the stabilizer of the base matching could hide an orientation
   distinction; Validator should reconstruct the extension of a component
   isomorphism explicitly.
2. A sparse dreadnaut input-generation or parsing convention could have changed
   the intended graph, despite the independent degree/edge-count assertions and
   saved complete adjacency lists.
3. The standard \(\operatorname{Aut}(A_n)=S_n\) identification or faithfulness
   argument could be misapplied; `A_8` deserves an independent outer-action check.
4. This is one implementation family: Validator should independently regenerate
   at least the orbit/signature selection and the relation group, rather than
   trusting the saved constants.

## Recommended next action

Validator should independently reconstruct the six exact comparisons, starting
with the nonuniform gates \(n=8\) and \(n=9\), then spot-check the largest
\(n=13\) relation input and group. If this boundary result and the separate
\(n\ge14\) lane both survive review, MathExpert can assess a splice into one
four-transposition-family theorem; neither lane is a premise for the other here.

---
title: "Verification — Kourovka 21.52 — fixed PSL(2,7) equality"
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
scope_record: Agents/Kourovka/scopes/21.52-involution-class-product-order-colouring.json
assignment_revision: 1
claim: "For L=PSL(2,7) and its unique 21-element involution class D, the product-order colour-automorphism group equals the restriction image of Aut(L), and both permutation groups have order 336."
claimant: Problem-21.52
target_statement: "For every finite nonabelian simple group L and every conjugacy class D of involutions in L, every permutation of D preserving |ab| for all distinct a,b is induced on D by an automorphism of L stabilizing D setwise."
excluded_scopes: ["Problem 21.53", "unions of involution classes", "uncoloured complete graph", "colouring by conjugacy class instead of product order", "bounded-family inference to the universal assertion"]
target_object: "the universally quantified family of all admissible pairs (L,D)"
witness_object: "the single pair (PSL(2,7),D), with D its unique 21-element involution class"
witness_equals_target: false
citation: "none; independent exact GAP/GRAPE reconstruction and the Fano-plane flag argument below"
verification_method: "GAP 4.12.1 quotient reconstruction; GRAPE 4.9.0 coloured-incidence-graph automorphism group; independent Fano-plane flag proof"
tools_used: ["GAP 4.12.1", "GRAPE 4.9.0/nauty", "Python 3.12.3 availability probe", "pdftotext and pdftoppm for source rendering", "sha256sum for artifact integrity"]
scope_answered: ["fixed special case (PSL(2,7),D), which is not the canonical universal scope"]
scope_not_answered: ["21.52/involution-class-product-order-colouring", "every admissible pair other than the fixed PSL(2,7) pair"]
active_assignment_answered: no
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/conjectured]
---

# Verification — Kourovka 21.52 — fixed PSL(2,7) equality

## The claim

The bounded claim is correct. For the unique involution class \(D\) of
\(L=\operatorname{PSL}(2,7)\),

\[
\operatorname{Aut}_{\mathrm{col}}(D,|ab|)
=\operatorname{res}_{D}
  \bigl(\operatorname{Stab}_{\operatorname{Aut}(L)}(D)\bigr),
\qquad
|\operatorname{Aut}_{\mathrm{col}}|=336.
\]

A fresh exact implementation and an independent structural reconstruction agree
with the claimant. This proves only one admissible special case. The source and
canonical assignment quantify over **every** admissible \((L,D)\), so the formal
scope verdict is `status/conjectured` and `active_assignment_answered: no`.

## Scope, revision, and clause matrix

The source PDF was rendered and visually read at page 172. It agrees with the
canonical scope at revision 1: the vertices are one involution conjugacy class,
the graph is complete, the edge colour is exactly product order, and the question
asks whether every colour permutation is induced by an automorphism of \(L\).

| source clause | required by source | result of this verification |
|---|---|---|
| `c-objects` | arbitrary finite nonabelian simple \(L\) and arbitrary single involution class \(D\) | checked only for \(L=\operatorname{PSL}(2,7)\) and its unique involution class |
| `c-colouring` | complete graph on \(D\), colours exactly the fibres of \(|ab|\) | all 210 edges checked for the fixed pair |
| `c-colour-automorphism` | every permutation preserving all edge colours | the full fixed-pair permutation group computed and structurally bounded |
| `c-question` | induced by \(\operatorname{Aut}(L)\) for every admissible pair | equality proved for the fixed pair; unproved universally |

Problem 21.53 and all other exclusions in the scope record remain outside this
review.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | candidate value / proof use | independent evidence | result |
|---|---|---|---|---|---|
| `21.52-forall-L-D` | admissibility | every admissible pair | one pair only | source/scope quantifier comparison | **fail for scope coverage** |
| `21.52-L-finite-nonabelian-simple` | admissibility | \(L\) finite nonabelian simple | \(\operatorname{SL}(2,7)/Z\), order 168 | quotient construction, `IsSimpleGroup`, and explicit isomorphism to `PSL(2,7)` | pass for fixed pair |
| `21.52-D-single-involution-class` | admissibility | one complete class of elements of order 2 | the unique class of size 21 | complete conjugacy-class enumeration and transvection parametrization | pass for fixed pair |
| `21.52-Gamma-complete-on-D` | admissibility | every unordered pair of distinct vertices | \(\binom{21}{2}=210\) edges | full 21-by-21 matrix and edge-vertex incidence construction | pass for fixed pair |
| `21.52-edge-colour-exact-product-order` | admissibility | colour is exactly \(|ab|\) | orders 2, 3, 4 with counts 42, 84, 84 | exact quotient multiplication and the flag calculation below | pass for fixed pair |
| `21.52-tau-preserves-all-edge-colours` | admissibility | all colour-preserving permutations | 336 complete restrictions | full automorphism group of a coloured incidence graph; direct matrix recheck | pass for fixed pair |
| `21.52-tau-induced-by-AutL` | target conclusion | extension for every admissible pair | exact equality of two 336-element sets for this pair | independent `Aut(L)` restrictions, elementwise set comparison, and the order sandwich below | pass for fixed pair; **unproved universally** |

The routed claim-check JSON correctly has `ready_for_validator:false`: its
universal row is `unknown` and its target conclusion is `not_proved`. That is the
right completeness-gate result for a fixed-pair partial; it cannot close the scope.

## Target vs witness

- Source target: the universally quantified family of all admissible pairs
  \((L,D)\).
- Witness computed in: the single pair \((\operatorname{PSL}(2,7),D)\).
- `witness_equals_target: false`.

This is an actual logical mismatch, not a remaining software question. Even a
perfect finite computation in this witness cannot establish the universal target.

## Sub-claims and what each method proves

| sub-claim | independent method | what a pass proves | what it does not prove |
|---|---|---|---|
| quotient model | construct \(\operatorname{SL}(2,7)/Z\), take a faithful permutation image, and find an explicit isomorphism to `PSL(2,7)` | exact identity and admissibility of the finite group model | any other simple group |
| involution class | enumerate all conjugacy classes and separately parametrize transvections in \(\operatorname{GL}_3(2)\) | the complete unique class has 21 elements | the universal quantifier |
| 210 colours | multiply every pair in the quotient; separately classify flags by two incidence bits | the complete matrix and counts 42, 84, 84 | completeness of either permutation group |
| full colour group | convert the colouring to a 231-vertex incidence graph with ordered vertex-colour classes and call GRAPE/nauty | the full fixed-pair colour group, not a sampled subgroup | that its elements extend to \(L\) |
| automorphism restriction image | enumerate the full abstract automorphism group and restrict every setwise stabilizer element | the complete fixed-pair restriction image | equality merely from matching orders |
| equality | compare the two canonically sorted 336-element permutation sets; independently sandwich both using the Heawood graph | exact fixed-pair equality | the active universal conclusion |
| witness is target | compare source quantifier with fixed model | proves the witness is strictly narrower | no fixed-pair mathematics |

## Evidence

### Source transcript

```bash
source _meta/agents/Kourovka/paths.env
pdftotext -f 172 -l 172 -layout "$KOUROVKA_PDF" -
```

Relevant verbatim output:

```text
21.52. Let L be a finite non-abelian simple group, and let D be a conjugacy class
of involutions in L. Consider the complete graph Γ with vertex set D. Define an
equivalence relation ∼ (graph coloring) on the set of edges as follows: (a, b) ∼ (c, d)
if and only if |ab| = |cd|. An automorphism of the coloured graph Γ is a permu-
tation τ ∈ SD such that (a, b) ∼ (aτ , bτ ) for every edge (a, b). Is it true that the
automorphism group of Γ is a subgroup of Aut(L)?                        I. B. Gorshkov
```

The same page was rendered to PNG and inspected visually, confirming the
subscripts and superscripts flattened by `pdftotext` as \(S_D,a^\tau,b^\tau\).

### Independent provenance and circularity check

The validator checker was written without reading or invoking the claimant's
script. It accepts no claimant certificate as input. The colour group is built
only from the independently reconstructed product-order matrix; the abstract
automorphism group is built separately; equality is tested only after both full
sets exist. Thus neither group is generated from the desired equality, and equal
orders alone are not used as a substitute for set equality.

The claimant certificate was inspected only as the routed object and later as a
comparison target. Its stored file SHA-256 is
`4042b2a1ed73c8f4e3e7b798059d39772ddc0c3b2c367c3428c02af0c60f3bcc`.

### Frozen-run history, including the failed v1

V1 was frozen at SHA-256
`b888d48d2b0cb0dcae0254e2381e8d8e1426056b7f96d603c53b22d3a1c876ce`
and run once under its Lead lease:

```bash
timeout 120s /usr/bin/gap -q -T --quitonbreak -K 512m Agents/Kourovka/problems/21.52/verification/scratch/validator_psl27_independent.g > Agents/Kourovka/problems/21.52/verification/scratch/validator_psl27_independent.stdout 2> Agents/Kourovka/problems/21.52/verification/scratch/validator_psl27_independent.stderr
```

The shell reported exit status 0 after 1.325352047 seconds, but the semantic run
failed before mathematics. Stdout was empty. Verbatim stderr was:

```text
Error, Variable: 'Z' is read only
```

The empty-stdout SHA-256 was
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`;
stderr SHA-256 was
`1a1e947d6cd07ab45ea56116538f895cbbfc9da0f16e248369e017d5efafe22f`.
No mathematical inference is drawn from v1.

V1 was preserved. V2 changed only the illegal global name `Z` to `centreSL`, plus
the version and output labels. It was separately frozen at SHA-256
`9a55a712f1b256bc07a8ceafc3325572d6436547b4dc0dbe50bad7fea37c1adb`
and received a new Lead lease. The exact one-time command was:

```bash
timeout 120s /usr/bin/gap -q -T --quitonbreak -K 512m Agents/Kourovka/problems/21.52/verification/scratch/validator_psl27_independent_v2.g > Agents/Kourovka/problems/21.52/verification/scratch/validator_psl27_independent_v2.stdout 2> Agents/Kourovka/problems/21.52/verification/scratch/validator_psl27_independent_v2.stderr
```

It returned exit status 0 after 2.153280058 seconds. Stderr is empty. The complete
60,547-byte verbatim stdout—including the full 21-by-21 matrix and both complete
336-permutation lists—is preserved at
`Agents/Kourovka/problems/21.52/verification/scratch/validator_psl27_independent_v2.stdout`.
Its SHA-256 is
`765fc69eba2fd42004d61b7508fede6affbcfbd414f0693895922a9e99ba0a2d`.
Verbatim summary lines are:

```text
VALIDATOR_PSL27_INDEPENDENT_V2
gap_version=4.12.1
grape_version=4.9.0
sl_order=336
centre_order=2
quotient_order=168
quotient_nonabelian=true
quotient_simple=true
quotient_isomorphic_to_PSL_2_7=true
involution_class_count=1
involution_class_size=21
unordered_edge_count=210
colour_values=[ 2, 3, 4 ]
edge_colour_counts=[ 42, 84, 84 ]
incidence_graph_order=231
incidence_aut_order=336
colour_restriction_count=336
autL_order=336
setwise_stabilizer_count=336
aut_restriction_count=336
groups_equal_as_permutation_sets=true
colour_only=[  ]
aut_only=[  ]
```

The checker encodes each of the 210 coloured edges as a separate vertex adjacent
to its two endpoints and places those edge-vertices into ordered colour classes
by exact product order. Consequently every automorphism of the coloured incidence
graph restricts to a colour-preserving permutation of \(D\), every such
permutation extends uniquely to the incidence graph, and the restriction kernel
is trivial. GRAPE therefore computes the full group without using the claimant's
backtracking architecture.

### Independent Fano-plane reconstruction

Use the standard exceptional model
\(\operatorname{PSL}(2,7)\cong\operatorname{GL}_3(2)\) as a structural route
separate from the quotient computation. Let \(V=\mathbf F_2^3\). Every
involution is uniquely

\[
t_{u,f}=I+u f,
\qquad u\ne0,quad f\ne0,quad f(u)=0,
\]

where \(uf\) denotes the rank-one map \(x\mapsto f(x)u\). Indeed, for an
involution \((g-I)^2=0\); in dimension three its nonzero nilpotent part has rank
one. Conversely every displayed map squares to the identity. There are seven
choices of \(u\) and three nonzero functionals annihilating it, hence 21
involutions. Conjugation is transitive on these incident point-line flags, so this
is one complete class.

For two distinct flags \((u,f)\) and \((v,g)\), put
\(a=f(v)\) and \(b=g(u)\). Direct rank-one multiplication gives

| \((a,b)\) | order of \(t_{u,f}t_{v,g}\) |
|---|---:|
| \((0,0)\) | 2 |
| \((1,1)\) | 3 |
| exactly one of \(a,b\) is 1 | 4 |

For the last row, the product is \(I+N\) with \(N^3=0\ne N^2\), so it has
order four. For the middle row, its action on \(\langle u,v\rangle\) has matrix
of order three and the third power fixes the complementary quotient as well.

For a fixed flag, four other flags have \((a,b)=(0,0)\): two share its point and
two share its line. There are four choices of \(v\notin\ker f\), and for each
there are two functionals \(g\) with \(g(v)=0\) and \(g(u)=1\), giving eight
order-three neighbours. The remaining eight have product order four. Dividing
the valency totals by two gives exactly

\[
42\text{ edges of colour }2,qquad
84\text{ of colour }3,qquad
84\text{ of colour }4.
\]

The colour-2 graph joins two flags exactly when they share their point or their
line. It is therefore the line graph of the Heawood incidence graph of the Fano
plane. Its fourteen maximal triangles recover the seven point-stars and seven
line-stars, so every line-graph automorphism reconstructs an automorphism of the
Heawood graph. The part-preserving group is
\(\operatorname{GL}_3(2)\), of order 168, and a point-line duality supplies the
other coset. Hence the Heawood and colour-2 graph automorphism groups have order
336. In particular the full three-colour group has order at most 336.

Inner automorphisms of \(\operatorname{GL}_3(2)\) give 168 restrictions on the
flags. The contragredient automorphism

\[
g\longmapsto(g^{-1})^{T}
\]

swaps the point- and line-star families and is not inner; together they give 336
distinct restrictions. Every group automorphism preserves the unique involution
class and product orders, so its restriction image lies inside the colour group.
The upper and lower bounds force both groups to have order 336 and to be equal.
This argument does not assume the output of either enumeration.

## Verdict

`status/conjectured` for canonical scope revision 1.

The fixed-\(\operatorname{PSL}(2,7)\) equality is accepted as a bounded
`PARTIAL_RESULT`: this pair is not a counterexample. The canonical assignment is
not answered because its universal-coverage row fails.

## Why this verdict

The fixed finite statement has two independent complete routes: the leased
GAP/GRAPE checker constructs both full permutation sets and compares them
elementwise, while the Fano-plane argument derives the complete colour counts and
forces the common group order 336. The claimant's independently written
certificate reports the same fixed-pair result.

Protocol nevertheless caps the verdict at `conjectured` whenever the witness is
not the target. Here the mismatch is explicit: one simple group cannot prove a
statement quantified over every finite nonabelian simple group and every
involution class.

## What is NOT established

- No admissible pair \((L,D)\) other than this fixed
  \(\operatorname{PSL}(2,7)\) pair is covered.
- Problem 21.52's universal assertion is neither proved nor refuted.
- No separating colour-preserving permutation exists in this fixed pair, and none
  has been produced elsewhere by this review.
- The result gives no family reduction and does not justify extrapolation from
  the orders 120 for \(A_5\) and 336 here.
- `witness_equals_target:false` and `active_assignment_answered:no` cannot be
  upgraded by further checks confined to this pair.

## What would upgrade it

The active assignment requires either a uniform proof for every admissible
\((L,D)\), or one fully reconstructible admissible counterexample with a colour
permutation outside the restriction image. Any further finite list remains a
partial result.

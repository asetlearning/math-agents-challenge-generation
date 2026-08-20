---
title: "Verification — Kourovka 21.52 — fixed-A5 equality"
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
scope_record: Agents/Kourovka/scopes/21.52-involution-class-product-order-colouring.json
assignment_revision: 1
claim: "For L=A5 and its unique conjugacy class D of 15 involutions, the product-order colour-automorphism group equals the restriction image of Aut(A5), and both groups have order 120."
claimant: Problem-21.52
target_statement: "For every finite nonabelian simple group L and every conjugacy class D of involutions in L, every permutation of D preserving |ab| for all distinct a,b is induced on D by an automorphism of L stabilizing D setwise."
excluded_scopes: ["Problem 21.53", "unions of involution classes", "uncoloured complete graph", "colouring by conjugacy class instead of product order", "bounded-family inference to the universal assertion"]
target_object: "the universally quantified family of all admissible pairs (L,D)"
witness_object: "the single pair (A5,D), with D the 15 double transpositions"
witness_equals_target: false
citation: "none; independent elementary hand proof below"
verification_method: "hand reconstruction via fixed-point blocks, order-3 matching holonomy, and the conjugation action of S5"
tools_used: ["pdftotext (source rendering only)", "GAP 4.12.1 (availability probe only; no mathematical run)", "Python 3.12.3 (availability probe only; no mathematical run)", "sha256sum (artifact integrity only)"]
scope_answered: ["fixed special case (A5,D), which is not a canonical universal scope"]
scope_not_answered: ["21.52/involution-class-product-order-colouring", "every admissible pair other than the fixed A5 pair"]
active_assignment_answered: no
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/conjectured]
---

# Verification — Kourovka 21.52 — fixed-A5 equality

## The claim

The bounded claim is true: for the unique involution class `D` of `A5`,

\[
\operatorname{Aut}_{\mathrm{col}}(D,|ab|)
=\operatorname{res}_{D}(\operatorname{Aut}(A_5))
\quad\text{and}\quad
|\operatorname{Aut}_{\mathrm{col}}|=120.
\]

This was reconstructed by a hand argument independent of the claimant's enumeration. It proves one admissible special case only. The source and canonical assignment quantify over **every** admissible `(L,D)`, so the formal scope verdict remains `status/conjectured` and `active_assignment_answered: no`.

## Scope, revision, and clause matrix

The rendered source on PDF page 172 agrees with canonical scope revision 1. In particular, the edge colour is exactly product order, and a colour automorphism must preserve that exact colour on every edge.

| source clause | required by source | result of this verification |
|---|---|---|
| `c-objects` | arbitrary finite nonabelian simple `L` and arbitrary single involution class `D` | checked only for `L=A5` and its unique involution class |
| `c-colouring` | complete graph on `D`, colours given exactly by equality of `|ab|` | fully used for fixed `A5` |
| `c-colour-automorphism` | every permutation preserving all edge colours | arbitrary such permutation treated for fixed `A5` |
| `c-question` | induced by `Aut(L)` for every admissible pair | proved for fixed `A5`; unproved for the universal family |

The nearby Problem 21.53 and every excluded interpretation listed in the scope record remain outside this review.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | candidate value / proof use | evidence | result |
|---|---|---|---|---|---|
| `21.52-forall-L-D` | admissibility | every admissible `(L,D)` | only `(A5,D)` | explicit quantifier comparison | **fail for scope coverage** |
| `21.52-L-finite-nonabelian-simple` | admissibility | finite nonabelian simple `L` | `A5` | standard class-size proof of simplicity; `|A5|=60` | pass for fixed pair |
| `21.52-D-single-involution-class` | admissibility | one conjugacy class, all elements order 2 | the 15 double transpositions | cycle type and parity argument | pass for fixed pair |
| `21.52-Gamma-complete-on-D` | admissibility | all unordered pairs of distinct elements of `D` | all pairs are covered by the same-block/different-block dichotomy below | structural exhaustion | pass for fixed pair |
| `21.52-edge-colour-exact-product-order` | admissibility | colour exactly `|ab|` | orders 2, 3, and 5 derived for every pair type | explicit products below | pass for fixed pair |
| `21.52-tau-preserves-all-edge-colours` | admissibility | arbitrary colour-preserving `tau` | an arbitrary `tau` is followed through recovered blocks and matchings | kernel proof below | pass for fixed pair |
| `21.52-tau-induced-by-AutL` | target conclusion | extension for every admissible pair | equality with the restriction image is proved for `A5` only | upper/lower bound chain below | pass for fixed pair; **unproved universally** |

The failed universal-coverage row mechanically forces `witness_equals_target: false` and `active_assignment_answered: no`.

## Target vs witness

The target is the complete universally quantified family of admissible pairs. The witness actually checked is one member, `(A5,D)`. It is admissible, but it is not equal to the target family. Thus:

`witness_equals_target: false`.

This is the precise sense in which the bounded claim can be valid while Problem 21.52 remains open.

## Subclaims and what each method proves

| subclaim | independent method | what the pass proves | what it does not prove |
|---|---|---|---|
| structure of `D` | double-transposition model on five letters | 15 vertices in one involution class, partitioned into five 3-sets | any other simple group |
| colour-2 relation | direct products of perfect matchings | the five 3-sets are intrinsically recovered from the coloured graph | faithfulness of their induced action |
| inter-block colour-3 relation | explicit cycle products | a canonical perfect matching between every two 3-sets | universal rigidity |
| kernel of block action | triangle holonomy of the perfect matchings | a colour automorphism fixing all five blocks is the identity | existence of all block permutations |
| lower bound | conjugation by `S5` | 120 distinct induced colour automorphisms belonging to the restriction image | any result beyond `A5` |
| equality | compare the upper bound 120 with that subgroup | exact fixed-`A5` equality and order | the universal conclusion |

## Evidence

### 1. The concrete model

Work on `Omega={1,2,3,4,5}` and regard `A5` as the even permutations. Every involution in `A5` has cycle type `(ab)(cd)` and fixes a unique point. Conversely every double transposition is an involution. There are

\[
5\cdot 3=15
\]

of them: choose the fixed point and one of the three perfect matchings of the other four points. They form one `A5`-conjugacy class. Indeed, they form one `S5` cycle-type class; the `S5` centralizer of a double transposition contains an odd transposition, so any odd conjugator can be corrected to an even one without changing its conjugation result.

For completeness, `A5` is an admissible finite nonabelian simple group: its conjugacy-class sizes are `1,15,20,12,12`; no sum consisting of 1 and a proper subset of the other class sizes is a proper divisor of 60, so Lagrange's theorem rules out a nontrivial proper normal subgroup.

For each `i in Omega`, let

\[
D_i=\{x\in D:x(i)=i\}.
\]

Then the five sets `D_i` partition `D`, and each has three elements.

### 2. Recovering the five blocks from colour 2

Two distinct elements of one `D_i` are two distinct perfect matchings on `Omega\\{i}`; their product is the third nonidentity element of the corresponding Klein four group and has order 2.

Now take distinct fixed points `i,j`. Write the remaining three points as `p,q,r` and take

\[
x=(jp)(qr)\in D_i.
\]

The three elements of `D_j` are

\[
y_0=(ip)(qr),\qquad y_1=(iq)(pr),\qquad y_2=(ir)(pq).
\]

Direct multiplication gives

\[
|xy_0|=3,
\]

because the common transposition `(qr)` cancels and the remaining two transpositions on `{i,j,p}` multiply to a 3-cycle. It also gives

\[
xy_1=(i\ r\ j\ p\ q),\qquad
xy_2=(i\ q\ j\ p\ r)
\]

up to reversing cycle orientation according to the multiplication convention, so both have order 5. Thus no different-block pair has product order 2.

Consequently the colour-2 subgraph is exactly the disjoint union

\[
K_3\sqcup K_3\sqcup K_3\sqcup K_3\sqcup K_3
\]

on the blocks `D_i`. Every colour automorphism therefore permutes these five connected components. This defines a homomorphism

\[
\rho:\operatorname{Aut}_{\mathrm{col}}(D,|ab|)\longrightarrow S_5.
\]

### 3. The kernel of the block action is trivial

For distinct `i,j`, define `f_ij:D_i -> D_j` by the unique order-3 neighbour across those blocks:

\[
f_{ij}\big((jp)(qr)\big)=(ip)(qr).
\]

The preceding product calculation proves both uniqueness and that `f_ji=f_ij^{-1}`.

Let `tau` lie in `ker(rho)` and write `sigma_i=tau|D_i`. Since `tau` preserves colour 3 and fixes every block setwise,

\[
\sigma_j f_{ij}=f_{ij}\sigma_i                       \tag{1}
\]

for every pair `i != j`.

Fix distinct `i,j,k`, and call the two remaining points `r,s`. On `D_i` use the three elements

\[
A=(jk)(rs),\qquad B=(jr)(ks),\qquad C=(js)(kr).
\]

The triangle holonomy

\[
h_{i;j,k}=f_{ki}f_{jk}f_{ij}:D_i\longrightarrow D_i
\]

satisfies

\[
h_{i;j,k}(A)=A,\qquad h_{i;j,k}(B)=C,\qquad h_{i;j,k}(C)=B.       \tag{2}
\]

Indeed, the three paths are

\[
\begin{aligned}
A&\mapsto(ik)(rs)\mapsto(ij)(rs)\mapsto A,\\
B&\mapsto(ir)(ks)\mapsto(js)(ir)\mapsto C,\\
C&\mapsto(is)(kr)\mapsto(jr)(is)\mapsto B.
\end{aligned}
\]

Equation (1), composed around the triangle, shows that `sigma_i` commutes with `h_{i;j,k}`. As the pair `{j,k}` ranges through representatives of the three perfect matchings on `Omega\\{i}`, equation (2) supplies all three transpositions of the 3-set `D_i`. A permutation of three points commuting with all three transpositions is the identity. Hence every `sigma_i` is the identity and so `tau=1`.

Therefore `rho` is injective, and

\[
|\operatorname{Aut}_{\mathrm{col}}(D,|ab|)|\leq |S_5|=120.       \tag{3}
\]

### 4. The lower bound is exactly the restriction image

`A5` is normal in `S5`. Hence conjugation by every `s in S5` is an automorphism of `A5`, maps `D` to itself, and preserves every product order. Its action sends `D_i` to `D_{s(i)}`. The natural action of `S5` on the five block labels is faithful, so these conjugations give 120 distinct elements of the restriction image.

Conversely, every automorphism of `A5` preserves the unique involution class `D` and all product orders, so its restriction belongs to the colour group. If `R` denotes this restriction image and `H` the image supplied by conjugation with `S5`, then

\[
120=|H|\leq |R|\leq
|\operatorname{Aut}_{\mathrm{col}}(D,|ab|)|\leq120.
\]

Every inequality is therefore an equality. This proves the routed fixed-`A5` claim without using the claimant's enumeration.

The restriction map itself is faithful as well: an automorphism fixing every involution fixes the subgroup generated by the involution class, and that subgroup is nontrivial and normal in the simple group `A5`, hence is all of `A5`. Thus the familiar conclusion `|Aut(A5)|=120` also follows, although only the restriction-image order was needed.

### 5. Circularity check

The 15 vertices were reconstructed from the standard concrete permutation group `A5`, not generated from the desired equality or from a presumed automorphism list. The upper bound comes from a graph-intrinsic block relation and an explicit kernel proof. The `S5` conjugations enter only after that independent upper bound is established. No step assumes `Aut(A5)=S5` or assumes the desired equality.

### 6. Source and integrity transcripts

Source command:

```bash
source _meta/agents/Kourovka/paths.env; pdftotext -f 172 -l 172 -layout "$KOUROVKA_PDF" -
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

Artifact-integrity command (this checks identity only; it does not validate the claimant's enumeration):

```bash
sha256sum Agents/Kourovka/problems/21.52/scratch/a5-colour-test/a5-colour-certificate.json Agents/Kourovka/problems/21.52/scratch/a5-colour-test/a5-colour-independent-verification.json Agents/Kourovka/problems/21.52/scratch/a5-colour-test/frozen-run-manifest.json
```

Verbatim output:

```text
4dc45ea15635231524e0b04fba73bf775e2be89da8f364648137d8d9622375e2  Agents/Kourovka/problems/21.52/scratch/a5-colour-test/a5-colour-certificate.json
c74bf55643f3cf112f43e718dbf50fd5c6a58f97747501add4a3e5dd7becd299  Agents/Kourovka/problems/21.52/scratch/a5-colour-test/a5-colour-independent-verification.json
9d91be237370aef9bf40013325b08e4927e228e5f8d4ecc93b062cffe91f357a  Agents/Kourovka/problems/21.52/scratch/a5-colour-test/frozen-run-manifest.json
```

These hashes match the routed report. After the independent proof was complete, the claimant's stored summary and independent-verifier JSON were inspected as secondary corroboration: they report the same orders and equality. Their enumeration logic is not used in the proof above, and no claimant script was rerun.

## Verdict

`status/conjectured` for canonical scope revision 1.

The fixed-`A5` equality itself is independently verified by the complete hand proof above. It is accepted as a bounded `PARTIAL_RESULT`: `A5` is not a counterexample. The canonical assignment is not answered because its first constraint is universal and the witness covers only one pair.

## Why this verdict

Mathematically, the special-case argument is exhaustive: it treats all 15 vertices through a structural parametrization, recovers the five blocks intrinsically, proves the block-action kernel trivial, and sandwiches both finite permutation groups at order 120.

Protocol nevertheless forbids raising the active claim above `conjectured` when the witness is not the target. Here the mismatch is explicit rather than technical: one `A5` instance cannot establish a statement quantified over every finite nonabelian simple group and every involution class.

## What is NOT established

- No admissible pair `(L,D)` other than the fixed `A5` pair is covered.
- The universal assertion in Problem 21.52 is neither proved nor refuted.
- No separating colour-preserving permutation has been found.
- The claimant's computational implementation was not rerun by Validator; it was unnecessary for the independent proof and running it would have required a frozen independent implementation and a Lead lease under the assignment instruction.
- No amount of further `A5`-only enumeration can change `active_assignment_answered: no`.

## What would upgrade it

To answer the active assignment requires either a proof uniform over every admissible `(L,D)` or one reconstructible admissible counterexample. A broader but still bounded family would remain partial. If the program wishes to certify the fixed-`A5` lemma itself above `conjectured` as a standalone result, the human must first see the written proof; that would still not upgrade the canonical universal scope.

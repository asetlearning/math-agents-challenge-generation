---
title: "Verification — Kourovka 19.30 — A5 order-60 fixed-target partial result"
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
scope_record: Agents/Kourovka/scopes/19.30-vanishing-order-simple-recognition.json
assignment_revision: 1
claim: "For every finite group G, if |G|=60 and V_o(G)=V_o(A_5), then G is isomorphic to A_5."
claimant: Problem-19.30
target_statement: "For every finite group G and finite simple group S, if |G|=|S| and G and S have the same set of orders of vanishing elements, then G is isomorphic to S."
excluded_scopes: ["Equality of character tables without equality of vanishing-order sets", "Equality of spectra of all elements rather than only vanishing elements", "Pairs in which neither group is finite simple"]
target_object: "Every pair (G,S) in the canonical universal scope: G finite, S finite simple, |G|=|S|, and V_o(G)=V_o(S)."
witness_object: "Only the fixed-target subcase S=A_5 and |G|=60, checked by a line-by-line hand proof with no computational model."
witness_equals_target: false
citation: "No external citation; hand reconstruction using only the rendered source and the references listed in the incoming report."
verification_method: line-by-line hand proof
tools_used: ["No mathematical computation", "Rendered-source inspection with Poppler 24.02.0", "GAP 4.12.1 and Python 3.12.3 version probes only; neither used for mathematics"]
scope_answered: ["Fixed target S=A_5: every finite G with |G|=60 and V_o(G)=V_o(A_5) is isomorphic to A_5"]
scope_not_answered: ["19.30/vanishing-order-simple-recognition universal scope", "Every finite simple target S other than the fixed A_5 subcase", "Any unconditional family-level extension"]
active_assignment_answered: no
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/conjectured]
---

# Verification — Kourovka 19.30

## The claim

Writing

\[
 V_o(X)=\{|x|:x\in X,\ \chi(x)=0\text{ for some }\chi\in\operatorname{Irr}(X)\},
\]

the submitted partial result is exactly

\[
 \forall G\text{ finite},\qquad
 |G|=60\ \text{and}\ V_o(G)=V_o(A_5)\Longrightarrow G\cong A_5.
\]

It is not a claim over arbitrary finite simple `S`. I reconstructed each dependency below instead of inheriting the five `PASS` labels.

## Scope, revision, and clause matrix

The incoming report and canonical record both name `19.30/vanishing-order-simple-recognition`, assignment revision 1. Direct visual inspection of rendered PDF page 134 confirms the definition and question in the canonical record. There is no revision or transcription mismatch.

| source clause | active? | what the submitted proof answers | what remains open |
|---|---:|---|---|
| `c-definition`: `g` is vanishing when some `chi in Irr(G)` has `chi(g)=0` | yes | used literally in the six-point representation and the normal-`C_5` restriction | none inside the fixed subcase |
| `c-question`: universal recognition for a finite group and a finite simple group with equal orders and equal sets of vanishing-element orders | yes | the one target `S=A_5`, hence order 60 | every other finite simple target; the universal clause itself |

The active source question is therefore not answered: `active_assignment_answered: no`.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | independently checked use | result |
|---|---|---|---|---|
| `19.30-forall-GS` | admissibility | every admissible pair `(G,S)` | replaces arbitrary `S` by `A_5` | **not established universally** |
| `19.30-G-finite` | admissibility | `G` finite | `G` is arbitrary among finite groups of order 60 | passes for the fixed target |
| `19.30-S-finite-simple` | admissibility | `S` finite simple | class-union proof below establishes this for `A_5` | passes for the fixed target |
| `19.30-vanishing-definition` | admissibility | zero of some irreducible complex character | an explicit irreducible `A_5` character has value zero; every irreducible `G` character is shown nonzero on order-five elements when the Sylow subgroup is normal | exact for the fixed target |
| `19.30-equal-orders` | admissibility | `|G|=|S|` | `|A_5|=60` and the hypothesis is `|G|=60` | passes for the fixed target |
| `19.30-equal-vanishing-order-sets` | admissibility | equality of sets, not multisets | only membership of the integer 5 is compared, which is sufficient to contradict set equality | passes for the fixed target |
| `19.30-isomorphic` | target conclusion | `G\cong S` | nonsimple `G` is excluded and simple order-60 uniqueness gives `G\cong A_5` | established only for the fixed target; not universally |

The universal-quantifier row fails as a scope-coverage row. This forces `witness_equals_target: false`, `active_assignment_answered: no`, and a verdict no higher than `status/conjectured`, even though the fixed-target implication itself survives the hand audit.

## Target vs witness and circularity

The target object is the universal class of admissible pairs `(G,S)`. The witness object is the strict subclass with `S=A_5`. These are not equal, so `witness_equals_target: false` is a proved scope fact, not an uncertainty about a presentation or quotient.

There is no hidden model substitution. `A_5` is the alternating permutation group on five letters, the six-point action is its actual conjugation action on its actual Sylow-5 subgroups, and `G` remains an arbitrary group satisfying the fixed order and invariant hypotheses. The character zero is derived before equality of vanishing-order sets is invoked. The equality hypothesis enters only in the final separation argument, so no tested object was constructed from the desired conclusion.

## Sub-claims and what each method proves

| subclaim | method | a pass proves | a pass does not prove |
|---|---|---|---|
| `A_5` is finite simple of order 60 | even cycle types, centralizers, class unions, Lagrange | the fixed target is admissible | simplicity of arbitrary `S` |
| a 5-cycle is vanishing in `A_5` | six-point Sylow action and its augmentation module | `5 in V_o(A_5)` | the full character table or full set `V_o(A_5)` |
| finite characteristically simple groups have direct-power form | minimal normals and induction | completeness of the later divisor lists | classification of finite simple groups |
| CS-5 and Aut-5 at order 60 | divisor/Sylow exhaustion and elementary automorphism counts | the precise hypotheses used by the normal-Sylow induction | analogous facts at other orders |
| simple order-60 uniqueness | Sylow counts, faithful actions, sign, and involution incidence | a simple `G` of order 60 is `A_5` | uniqueness at any other order |
| nonsimple order-60 groups have normal Sylow 5 | simultaneous least-order induction | the full order-five Sylow subgroup is normal | normality at unrelated primes/orders |
| normal Sylow `C_5` has no vanishing nonidentity element | direct weight-space proof of Clifford homogeneity and `Phi_5` noncancellation | `5 notin V_o(G)` in the nonsimple case | nonvanishing of arbitrary elements |
| compare the single order 5 | literal equality of sets | fixed-target recognition | universal Kourovka recognition |

## Evidence

### Closed evidence and tool boundary

Only the canonical scope record, the rendered source, and the three references in the incoming report were used. I did not consult the web, solution-bearing history, unlisted verification notes, a character table, a classification theorem, or a delegate. No mathematical computation was run, and the submitted hashes were not recomputed.

The required availability probe produced:

```text
$ which gap
/usr/bin/gap
$ which sage
[no output]
$ which python3
/usr/bin/python3
$ which magma
[no output]
$ which pdftotext
/usr/bin/pdftotext
$ gap -q -c 'Print(GAPInfo.Version,"\n");QUIT;'
4.12.1
$ python3 --version
Python 3.12.3
$ pdftotext -v
pdftotext version 24.02.0
Copyright 2005-2024 The Poppler Developers - http://poppler.freedesktop.org
Copyright 1996-2011, 2022 Glyph & Cog, LLC
```

GAP and Python were version-probed only. Neither evaluated a mathematical assertion.

The exact navigation command used after visual inspection of the rendered page was:

```text
$ source _meta/agents/Kourovka/paths.env
$ pdftotext -f 134 -l 134 -layout "$KOUROVKA_PDF" - | sed -n '/^19\.30\./,/19\.31\./p' | sed '$d'
19.30. An element g of a finite group G is said to be vanishing if χ(g) = 0 for some
irreducible complex character χ ∈ Irr(G). Must a finite group and a finite simple
group be isomorphic if they have equal orders and the same set of orders of vanishing
elements?                                 M. Foroudi Ghasemabadi, A. Iranmanesh,
```

### 1. `A_5`: order, all conjugacy classes, and simplicity

The sign map on `S_5` is onto and has kernel `A_5`, so `|A_5|=5!/2=60`. The complete even cycle-type list on five letters is

1. the identity;
2. a 3-cycle;
3. a product of two disjoint transpositions;
4. a 5-cycle.

There are 20 3-cycles. The `S_5` centralizer of one is its three powers times the optional swap of the two fixed points, of order 6. Exactly the three powers are even, so its `A_5` centralizer has order 3 and its class has size 20.

There are `5*3=15` double transpositions: choose the fixed point, then one of the three pairings of the other four points. Their `S_5` centralizer has order 8 and contains an odd transposition, so the sign map is onto on it; its even half has order 4. The `A_5` class therefore has size 15.

There are `(5-1)!=24` 5-cycles. A permutation commuting with a fixed 5-cycle is determined by the image of one point and is a power of that cycle. Thus the centralizer is cyclic of order 5 and lies in `A_5`; each `A_5` class has size 12. Hence the 24 cycles split into two classes.

The class sizes are exactly

\[
 1,20,15,12,12,
\]

and sum to 60. A normal subgroup is a union of these classes containing the identity. The distinct proper candidate sizes are

\[
 1,13,16,21,25,28,33,36,40,45,48.
\]

No number in this list except 1 divides 60. Lagrange therefore leaves only the identity subgroup and `A_5`. This closes both completeness points: no even cycle type and no class-union size is omitted. Thus `A_5` is simple of order 60.

### 2. The six-point action, normalizer, 2-transitivity, and irreducibility

Let `s=(12345)` and `P=<s>`. The 24 nonidentity 5-cycles partition into four generators per order-five subgroup, so there are exactly six Sylow-5 subgroups.

The centralizer of `P` equals the centralizer of its generator `s`, namely `P`. Hence conjugation injects

\[
 N_{A_5}(P)/P\hookrightarrow\operatorname{Aut}(P)\cong C_4.
\]

The even permutation `(25)(34)` conjugates `s` to `s^{-1}`, so the image has even order. If its order were 4, an element lifting a generator of the quotient image would have order divisible by 4, because the order of its coset divides its own order. The complete cycle-type list above shows that `A_5` has element orders only 1, 2, 3, and 5. Therefore the image has order 2 and `|N_{A_5}(P)|=10`. The orbit of `P` has size 6 and is the full Sylow set `Omega`.

In the conjugation action of `P` on `Omega`, the point `P` is fixed. If a distinct Sylow subgroup `Q` were fixed, conjugation would give `P -> Aut(Q)`, a homomorphism from a group of order 5 to one of order 4. It is trivial. Thus `P` and `Q` centralize each other. Their trivial intersection would make `PQ` a subgroup of order 25, impossible because 25 does not divide 60. So `P` fixes only `P`. Every `P`-orbit has size 1 or 5; it follows that `P` is transitive on the other five points. Since `A_5` is transitive on `Omega` and the stabilizer of `P` contains this transitive subgroup, the action is 2-transitive.

Let `V=C[Omega]`. It is the orthogonal direct sum of the constant line and

\[
 W=\{\sum a_\omega e_\omega:\sum a_\omega=0\},
\]

of dimension 5. An equivariant endomorphism of `V` has matrix entries constant on the group orbits in `Omega x Omega`, and every such orbit-constant matrix is equivariant. Two-transitivity gives exactly the diagonal and off-diagonal orbits, so `dim End_{A_5}(V)=2`.

Transitivity makes the constant line the entire fixed space, hence `W^{A_5}=0`. The invariant permutation inner product identifies either cross-homomorphism space with fixed vectors in `W`, so both cross spaces vanish. Therefore

\[
 2=1+\dim\operatorname{End}_{A_5}(W),
\]

and `End_{A_5}(W)` consists of scalars. If `W` had a nonzero proper invariant subspace, its orthogonal complement would also be invariant and orthogonal projection onto the subspace would be a nonscalar equivariant endomorphism. Thus `W` is irreducible.

The generator `s` fixes a point `Q` of `Omega` exactly when it normalizes `Q`. Since `s` generates `P`, the preceding fixed-point argument shows that its only fixed point is `P`. The permutation character has value 1 at `s`, while the constant constituent has value 1, so the irreducible character of `W` has value 0. Consequently `s` is a vanishing element of order 5 and

\[
 5\in V_o(A_5).
\]

### 3. The characteristically-simple direct-power lemma

Let `A != 1` be finite and characteristically simple. Induct on `|A|`, and choose a minimal nonidentity normal subgroup `M`. Every automorphic image of `M` is again minimal normal.

Choose a maximal collection of such images `M_1,...,M_k` whose product `D` is direct. If another image `L` is not contained in `D`, then minimality gives `L intersect D=1`, because the intersection is normal in `A`. Normality of both factors also gives `[L,D] <= L intersect D=1`; hence `D x L` would be a larger direct product, contradicting maximality. Thus every automorphic image of `M` lies in `D`.

The product of all automorphic images equals `D`, because it contains the chosen factors and every image lies in `D`. Automorphisms permute those images, so this nontrivial product is characteristic. Characteristic simplicity forces `A=D`.

If `k=1`, minimal normality says `A` itself is simple. If `k>1`, each `M_i` is proper and characteristically simple: a characteristic subgroup of `M_i` is normalized by `M_i` and centralized by the other direct factors, hence is normal in `A`, so minimality of `M_i` leaves only 1 and `M_i`. Induction writes `M_1` as `T^r` for a finite simple `T`; automorphisms carry `M_1` to every other `M_i`, so all are isomorphic to `T^r`. Hence `A` is `T^{rk}`. This proves, without classification, that every nontrivial finite characteristically simple group is a direct power of one finite simple group.

### 4. Complete CS-5 and Aut-5 exhaustions

Suppose `A` is nonabelian characteristically simple, `|A|` is a proper divisor of 60, and 5 divides `|A|`. Write `A=T^e`. Then `T` is nonabelian simple, 5 divides `|T|`, and `|T|` is one of

\[
 5,10,15,20,30.
\]

Order 5 is abelian. At orders 10, 15, and 20, the Sylow-5 count is congruent to 1 modulo 5 and divides 2, 3, and 4 respectively, so it is 1. At order 30, simplicity would force six Sylow-5 subgroups and ten Sylow-3 subgroups. They contribute 24 and 20 distinct nonidentity elements, already exceeding the available 29. None of the five orders supports a nonabelian simple `T`. Therefore every such `A` has order prime to 5.

Now let `A != 1` be characteristically simple with `|A|` dividing 60 and prime to 5. Then `|A|` divides 12 and `A=T^e` with simple `T` of order dividing 12. The only composite possibilities for `|T|` are 4, 6, and 12:

- at order 4, a Cauchy subgroup of order 2 has index 2 and is normal;
- at order 6, the Sylow-3 subgroup is unique;
- at order 12, either the Sylow-3 subgroup is unique, or four such subgroups account for eight nonidentity elements, leaving exactly three; every Sylow-2 subgroup has those same three nonidentity elements and is therefore unique.

Thus `T` has prime order 2 or 3. Divisibility by 60 leaves precisely

\[
 C_2,\quad C_2^2,\quad C_3.
\]

Their automorphism groups have orders 1, `|GL(2,2)|=(4-1)(4-2)=6`, and 2. The optional trivial group contributes automorphism order 1. This is the complete Aut-5 list, and every listed automorphism order is prime to 5.

### 5. Uniqueness of the simple group of order 60

Let `T` be simple of order 60. It is nonabelian, since a finite abelian simple group has prime order. Sylow arithmetic gives `n_5=6`: the alternatives satisfy `n_5 congruent 1 mod 5` and `n_5 | 12`, and simplicity excludes 1.

Similarly `n_3` is 4 or 10 after excluding 1. If it were 4, conjugation on the four Sylow subgroups would be nontrivial and therefore faithful by simplicity, embedding the order-60 group in `S_4`, impossible. Hence `n_3=10`.

For Sylow-2 subgroups, simplicity and the same action-kernel argument exclude `n_2=1` and `n_2=3`; thus `n_2` is 5 or 15.

If `n_2=5`, conjugation gives a faithful embedding with image `H<=S_5` of order 60. The restricted sign map cannot be onto, because its kernel would be a proper normal subgroup of `H` of order 30. Therefore `H<=A_5`; equal orders give `H=A_5`.

Assume `n_2=15`. All Sylow-2 subgroups have order 4 and are conjugate, so all are cyclic or all are Klein four. In the cyclic case, their two generators give 30 distinct elements of order 4. Together with the `6*(5-1)=24` elements of order 5 and `10*(3-1)=20` elements of order 3, this exceeds the 59 nonidentity elements.

In the Klein-four case, take an involution `t` in a Sylow subgroup `P`. Then `P<=C_T(t)`, so the centralizer order is one of 4, 12, 20, 60. Order 60 would make `t` central. Order 20 would make its conjugacy class have size 3; conjugation on that nontrivial class would be faithful by simplicity and would embed `T` in `S_3`. Thus every involution class has size 15 or 5.

If some class has size 5, its conjugation action is faithful and the same degree-five/sign argument identifies `T` with `A_5`. Otherwise every involution has centralizer order 4. For `t in P`, this forces `C_T(t)=P`. Any Sylow-2 subgroup containing `t` is Klein four, lies in `C_T(t)`, and equals `P`; hence every involution lies in exactly one Sylow subgroup. The 15 Klein-four groups then contain 45 distinct involutions, which together with the 24 order-five and 20 order-three elements is again impossible.

All cases give `T isomorphic A_5` (or a contradiction), proving simple-order uniqueness without a classification theorem.

### 6. Simultaneous least-order normal-Sylow-5 induction

Consider simultaneously:

1. every group of order `d`, where `d<60`, `d|60`, and `5|d`, has a normal Sylow-5 subgroup;
2. every nonsimple group of order 60 has a normal Sylow-5 subgroup.

If either fails, choose a failed group `X` of least order and a minimal nonidentity normal subgroup `N`. It is characteristically simple by the elementary observation that each characteristic subgroup of `N` is normal in `X`.

If 5 divides `|N|` and `N` is abelian, the direct-power lemma writes it as `C_q^e` for a prime `q`; divisibility by 5 forces `q=5`. Since every order under consideration divides 60 and `v_5(60)=1`, `e=1`. Thus `N` itself is the full normal Sylow-5 subgroup.

If 5 divides `|N|` and `N` is nonabelian, then `|N|<60`. This is automatic when `|X|<60`; when `|X|=60`, equality `N=X` would make the assumed nonsimple `X` simple. The CS-5 exhaustion contradicts 5 dividing `|N|`.

It remains that `N` is a 5-prime group. The smaller quotient `X/N` still has order divisible by 5 and, by least-order induction, has a normal Sylow subgroup `Pbar`, necessarily of order 5. Let `M` be its inverse image and choose `P in Syl_5(M)`. Orders give

\[
 |P|=5,\qquad P\cap N=1,\qquad M=NP.
\]

Conjugation defines `P -> Aut(N)`. The complete Aut-5 list makes the target order prime to 5, so the map is trivial and `[P,N]=1`. Hence `P` is normal in `M`; it is the unique Sylow-5 subgroup there and therefore characteristic. Since `M` is normal in `X`, `P` is normal in `X`. Finally `|X|_5=5`, so it is a Sylow subgroup of `X`. This contradicts the chosen failure and completes both simultaneous statements.

In particular, every nonsimple group of order 60 has a normal Sylow subgroup `P` of order 5.

### 7. Clifford homogeneous restriction reconstructed by weight spaces

Let `P` be this normal cyclic subgroup of order 5 and let `chi in Irr(G)` be afforded by an irreducible complex representation on `U`. Restriction to `P=<x>` decomposes `U` into eigenspaces

\[
 U_\lambda=\{u:\rho(p)u=\lambda(p)u\ \text{for all }p\in P\},
\]

indexed by the linear characters of `P`; diagonalizability follows because `rho(x)^5=1` and `T^5-1` has distinct complex roots. Normality of `P` makes `G` permute these weight spaces by conjugating their labels.

For any orbit `O` of labels, the sum of its weight spaces is `G`-invariant. Irreducibility of `U` therefore permits exactly one nonempty orbit. Group elements give linear isomorphisms between weight spaces in that orbit, so they all have the same positive dimension `e`. Consequently, by direct construction rather than an unexpanded appeal,

\[
 \chi_P=e\sum_{\lambda\in O}\lambda.
\]

This is precisely the homogeneous Clifford restriction needed here.

### 8. Cyclotomic noncancellation

Fix `1 != x in P`; it generates `P`. If `O` is the orbit of the trivial character, then it is the singleton orbit and `chi(x)=e`, which is nonzero.

Otherwise `O` contains only nontrivial characters. Choose a primitive fifth root `zeta`. Evaluation at the generator bijects the four nontrivial characters with `zeta^j`, `1<=j<=4`. Thus for a nonempty subset `J` of `{1,2,3,4}`,

\[
 \chi(x)=e f(\zeta),\qquad f(T)=\sum_{j\in J}T^j.
\]

If `f(zeta)=0`, the minimal polynomial

\[
 \Phi_5(T)=1+T+T^2+T^3+T^4
\]

divides `f` over the rationals. If `deg f<4`, this is impossible because `f` is nonzero. If `deg f=4`, both polynomials are monic of degree 4, so divisibility forces `f=Phi_5`, contradicting the zero constant coefficient of `f`. Hence `chi(x)` is nonzero for every irreducible `chi`.

Every element of order 5 belongs to the unique Sylow-5 subgroup `P`, so no element of order 5 is vanishing. Therefore

\[
 5\notin V_o(G)
\]

for every nonsimple group `G` of order 60.

### 9. Integration

The six-point action gives `5 in V_o(A_5)`. The simultaneous induction and homogeneous-restriction argument give `5 notin V_o(G)` for every nonsimple group `G` of order 60. Thus a finite `G` with

\[
 |G|=60,\qquad V_o(G)=V_o(A_5)
\]

cannot be nonsimple. It is simple, and the order-60 uniqueness argument gives `G isomorphic A_5`. No equality of multiplicities, no knowledge of any other vanishing order, and no converse is used.

## Verdict

**`status/conjectured`.** The hostile hand reconstruction found no mathematical gap in the fixed-target implication. Every requested dependency—`A_5` class-union simplicity; the six-point action, normalizer, 2-transitivity, and irreducibility; the characteristically-simple direct-power lemma; the complete Aut-5 list; simple-order uniqueness at 60; the simultaneous least-order normal-Sylow-5 induction; and homogeneous restriction plus cyclotomic noncancellation—closes from the displayed elementary arguments.

**`witness_equals_target: false`.** The one fixed target `S=A_5` is not the universal source target.

**`active_assignment_answered: no`.** The universal assignment is not answered, and no status promotion above conjectured is made.

## Why this verdict

The proof remains inside the actual groups it quantifies over, has no quotient/model substitution, and does not build the character zero or normal Sylow subgroup from the desired equality. The only invariant comparison required is the presence of order 5 for `A_5` versus its absence for nonsimple order-60 groups. The final simple case is closed by the fully reconstructed elementary uniqueness proof.

Protocol still caps the result at `status/conjectured`: the witness scope is strictly smaller than the canonical target, the active universal quantifier is open, and the instruction for this audit explicitly requires that status.

## What is NOT established

- The universal statement `19.30/vanishing-order-simple-recognition` is not established.
- No finite simple target other than the fixed `A_5` subcase is covered.
- No infinite family, Suzuki specialization, classification theorem, or character table is established or imported.
- The complete set `V_o(A_5)` is not calculated; only the membership of 5 is needed and proved.
- The four separator hypotheses are not shown necessary.
- `witness_equals_target` is false, `active_assignment_answered` is no, and neither `status/proven` nor `status/solved` is warranted.

## What would upgrade it

The active assignment requires either a proof for every finite simple target `S` or a fully admissible counterexample to the universal statement. Certification of the singleton theorem as its own target would first require Lead/human creation of a separate fixed-target scope and completion of the required review/human-visibility gates; that would still not answer the present universal scope.

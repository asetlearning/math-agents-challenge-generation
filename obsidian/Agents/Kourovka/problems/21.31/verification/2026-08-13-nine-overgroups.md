---
title: "Verification — Kourovka 21.31 — nine overgroups and quotient-action kernel"
problem: "21.31"
claim: "Conditional on the checked order-2016 reduction, there are exactly nine pair-isomorphism classes (G,K) satisfying the central overgroup conditions, and the necessary quotient linear action has kernel K."
claimant: Problem-21.31
target_object: "Regular subgroups of Hol(N) for arbitrary finite soluble N"
witness_object: "Extensions of GL(3,2) by the five order-12 radicals with trivial outer action, plus the induced affine action on N/M of order 8"
witness_equals_target: false
citation: "Byott, arXiv:2205.13464v4, Proposition 2.6 and Theorem 3.2 proof; standard nonabelian extension classification with trivial outer action"
verification_method: "Line-by-line extension/action proof and independent light GAP 4.12.1 constructions"
tools_used: ["GAP 4.12.1", "SmallGrp 1.5.3", "pdftotext 24.02.0"]
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/holomorphs, project/kourovka, status/conjectured]
---

# Verification — Kourovka 21.31 — nine overgroups and quotient-action kernel

## The claim

Conditional on the previously checked hypothetical order-2016 structure, the five possible radicals (K) give exactly nine isomorphism classes of distinguished pairs ((G,K)) with

\[
G/K\cong T=GL_3(2),\qquad G=K C_G(K),\qquad R(G)=K.
\]

There is one split class for every (K), and one nonsplit Schur-pushout class for every (K\ne A_4). Moreover, for the quotient automorphism action

\[
\Theta:G\longrightarrow\operatorname{Aut}(N/M)\cong GL_3(2),
\]

one necessarily has `ker(Theta) = K`.

## Target vs witness

Kourovka 21.31 asks about every regular subgroup of `Hol(N)` for every finite soluble `N`. The witnesses here classify only possible group-side overgroups forced by a hypothetical counterexample of order 2016. They do not include (N), a compatible automorphism action, or a bijective crossed map. Witness equals target is false, so the overall status remains `conjectured`.

## Sub-claims and what each method proves

### Correct extension parameter and equivalence relation

The already checked relation (G=K C_G(K)) says the induced outer action (T\to\operatorname{Out}(K)) is trivial. Standard nonabelian extension theory then classifies extensions of (T) by the fixed kernel (K), with this trivial outer action, by

\[
H^2(T,Z(K)).
\]

Because (T) is perfect, the universal coefficient sequence has no `Ext(T_ab,Z(K))` term. Since (M(T)\cong C_2),

\[
H^2(T,Z(K))\cong\operatorname{Hom}(C_2,Z(K))=Z(K)[2].
\]

This includes non-stem extensions and all primary components of (Z(K)).

Marked extensions use fixed identifications of (K) and (T). Isomorphisms of pairs ((G,K)) additionally allow `Aut(K) x Aut(T)`. The first factor acts naturally on (Z(K)[2]). The second acts through `Aut(C2)`, which is trivial, so it causes no further orbit identifications. Thus pair-isomorphism classes are exactly the `Aut(K)`-orbits on (Z(K)[2]).

There is no further collapse hidden by the central-product description: this is the extension classification of (G) itself, not merely a classification of an auxiliary central extension. Conversely every class is represented by the stated Schur pushout.

### Orbit count and `C6 x C2`

The independent GAP run gives orbit counts

```text
K=[12,1]: 2
K=[12,2]: 2
K=[12,3]: 1
K=[12,4]: 2
K=[12,5]: 2
```

For `K=[12,5]=C6 x C2`, the four elements of (Z(K)[2]) form orbits of sizes 1 and 3. Hence all three nonidentity involutions yield one nonsplit pair class, not three. The sum is (2+2+1+2+2=9).

The zero class is fixed by all automorphisms and is split; a nonzero class cannot be carried to zero. Thus split and nonsplit constructions cannot collapse.

### Exact meaning of “nine”

The result is exactly nine pair-isomorphism classes ((G,K)). Since (K=R(G)) is characteristic, every abstract group isomorphism maps (K) to the radical. Therefore it is also exactly nine abstract isomorphism classes of the resulting groups (G): classes belonging to different nonisomorphic radicals cannot merge, and classes for a fixed radical are already quotiented by all pair automorphisms.

It is not a count of target realizations ((G,N,\theta,\pi)), actions, regular embeddings, or crossed maps.

### Radical condition

Every construction has soluble normal subgroup (K) and quotient (T), which is nonabelian simple. Thus (K\le R(G)). The image of (R(G)) in (T) is soluble and normal, hence trivial (it cannot be all of insoluble (T)). Therefore (R(G)=K). This applies uniformly to split and nonsplit classes and does not assume a SmallGroups library at order 2016.

The independent nonsplit construction for the most delicate center, `K=C6 x C2`, additionally computed order 2016, embedded radical `[12,5]`, quotient `[168,42]`, and equality of the computed radical with the embedded (K).

### Proof of `ker Theta = K`

Byott's Proposition 2.6 defines K as the kernel of the induced affine action of G on V=N/M. Thus the quotient T=G/K embeds transitively in `Aff(V)`, and every element of K acts trivially both translationally and linearly. Hence K is contained in `ker(Theta)`.

Let

\[
\lambda:T\longrightarrow GL(V)=GL_3(2)
\]

be the linear part of this faithful affine embedding. Its kernel is normal in the simple group T, so it is either trivial or all of T. If it were all of T, the affine image of T would lie in the translation subgroup V, of order 8, impossible for the faithfully embedded group T of order 168. Therefore lambda is faithful. Pulling back to G gives exactly `ker(Theta) = K`.

This proof uses more than transitivity or affine faithfulness alone. In general a faithful affine action can have a nonfaithful linear part; simplicity and the `|V|=8<168` contradiction are the missing steps.

## Circularity check

The SmallGroups representatives, automorphism groups, multiplier, and Schur cover are external data. The orbit calculation enumerates the entire cohomological parameter set before counting. The radical and quotient-action arguments derive necessary properties from the independently cited quotient construction. Nothing was built by assuming that nine is the correct answer.

## Evidence

Independent orbit command:

```text
timeout 30s gap -q Agents/Kourovka/problems/21.31/verification/scratch/independent_nine_overgroup_orbits.g > Agents/Kourovka/problems/21.31/verification/scratch/independent_nine_overgroup_orbits.out 2>&1
```

Verbatim output:

```text
GAP_VERSION=4.12.1
SMALLGRP_VERSION=1.5.3
T_ID=[ 168, 42 ] T_PERFECT=true T_AUT_SIZE=336 MULTIPLIER=[ 2 ]
COVER_SIZE=336 COVER_DESC=SL(2,7) COVER_CENTER=C2
Syntax warning: Unbound global variable in Agents/Kourovka/problems/21.31/veri\
fication/scratch/independent_nine_overgroup_orbits.g:16
  z2 := Filtered(Elements(centerK), x -> x^2 = One(K));
                                                   ^
K_ID=[ 12, 1 ] K_DESC=C3 : C4 Z_ID=[ 2, 1 ] Z_DESC=C2 Z2_SIZE=2 ORBIT_COUNT=
2 ORBIT_SIZES=[ 1, 1 ] ORBIT_ELEMENT_ORDERS=[ [ 1 ], [ 2 ] ] SPLIT_ORDER=
2016 SPLIT_RADICAL_ID=[ 12, 1 ]
K_ID=[ 12, 2 ] K_DESC=C12 Z_ID=[ 12, 2 ] Z_DESC=C12 Z2_SIZE=2 ORBIT_COUNT=
2 ORBIT_SIZES=[ 1, 1 ] ORBIT_ELEMENT_ORDERS=[ [ 1 ], [ 2 ] ] SPLIT_ORDER=
2016 SPLIT_RADICAL_ID=[ 12, 2 ]
K_ID=[ 12, 3 ] K_DESC=A4 Z_ID=[ 1, 1 ] Z_DESC=1 Z2_SIZE=1 ORBIT_COUNT=
1 ORBIT_SIZES=[ 1 ] ORBIT_ELEMENT_ORDERS=[ [ 1 ] ] SPLIT_ORDER=
2016 SPLIT_RADICAL_ID=[ 12, 3 ]
K_ID=[ 12, 4 ] K_DESC=D12 Z_ID=[ 2, 1 ] Z_DESC=C2 Z2_SIZE=2 ORBIT_COUNT=
2 ORBIT_SIZES=[ 1, 1 ] ORBIT_ELEMENT_ORDERS=[ [ 1 ], [ 2 ] ] SPLIT_ORDER=
2016 SPLIT_RADICAL_ID=[ 12, 4 ]
K_ID=[ 12, 5 ] K_DESC=C6 x C2 Z_ID=[ 12, 5 ] Z_DESC=C6 x C2 Z2_SIZE=
4 ORBIT_COUNT=2 ORBIT_SIZES=[ 1, 3 ] ORBIT_ELEMENT_ORDERS=
[ [ 1 ], [ 2 ] ] SPLIT_ORDER=2016 SPLIT_RADICAL_ID=[ 12, 5 ]
TOTAL_PAIR_ISOMORPHISM_ORBITS=9
RUN_COMPLETE=true
```

```text
RUN_EXIT=0
SENTINEL_EXIT=0
3f2da2df412d354eb863120fd36408c1abf5ba33bfcee4dfc203769313117913  Agents/Kourovka/problems/21.31/verification/scratch/independent_nine_overgroup_orbits.g
6a492b11bdd7db8dd386488ca8f5a456bd832db97bd7b8e488a681fa5c39f8bc  Agents/Kourovka/problems/21.31/verification/scratch/independent_nine_overgroup_orbits.out
```

Independent nonsplit `C6 x C2` pushout command:

```text
timeout 30s gap -q Agents/Kourovka/problems/21.31/verification/scratch/independent_pushout_k5.g > Agents/Kourovka/problems/21.31/verification/scratch/independent_pushout_k5.out 2>&1
```

Verbatim output:

```text
GAP_VERSION=4.12.1
K_ID=[ 12, 5 ] Z_ORBIT_REP_ORDER=2
PRODUCT_ORDER=4032 DIAGONAL_ORDER=2 G_ORDER=2016
EMBEDDED_K_ORDER=12 EMBEDDED_K_ID=[ 12, 5 ] QUOTIENT_ORDER=168 QUOTIENT_ID=
[ 168, 42 ]
RADICAL_ORDER=12 RADICAL_ID=[ 12, 5 ] RADICAL_EQUALS_EMBEDDED_K=true
RUN_COMPLETE=true
```

```text
RUN_EXIT=0
SENTINEL_EXIT=0
fbf5f6d4f5181fc535e174ab006fbc0dbdfd4db909ed776985de966679f30b96  Agents/Kourovka/problems/21.31/verification/scratch/independent_pushout_k5.g
87a82f65c667b71cfd65edaf4a3adff67136a46374e56c0ecb7c2c8bde4820e6  Agents/Kourovka/problems/21.31/verification/scratch/independent_pushout_k5.out
```

The static GAP warning is lexical and the run reached its explicit sentinel.

## Verdict

`status/conjectured` overall. The nine-class overgroup classification and `ker(Theta)=K` are verified as complete conditional deductions under the previously checked order-2016 hypotheses. No target-level status upgrade follows because witness does not equal target.

## Why this verdict

The cohomological parameterization uses the correct nonabelian-kernel extension theory and the full pair-isomorphism action. The independent orbit data reproduce nine, the delicate `C6 x C2` orbit is correct, split/nonsplit cannot merge, every class has radical (K), and the quotient linear representation is necessarily faithful. But none of the nine groups has yet been coupled to a suitable soluble (N) and regular embedding.

## What is NOT established

- Kourovka 21.31 is not proved or disproved.
- Order 2016 is not excluded and no counterexample is constructed.
- “Nine” does not count compatible (N), automorphism actions, crossed maps, or regular embeddings.
- No claim is made for orders above 2016.
- The result remains conditional on the prior minimal-counterexample and central-pullback reductions.

## What would upgrade it

For each of the nine group-side classes, exhaust a proved-complete universe of soluble extensions (N), lifts of the fixed faithful quotient linear action, and compatible bijective crossed maps—or give a gap-free target-level proof eliminating them all.

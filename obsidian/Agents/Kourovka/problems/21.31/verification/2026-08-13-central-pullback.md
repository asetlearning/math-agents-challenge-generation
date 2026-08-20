---
title: "Verification — Kourovka 21.31 — central pullback refinement"
problem: "21.31"
claim: "Conditional on the checked order-2016 structure, every relevant central pullback over P splits, eliminating [252,2] and [252,9] and leaving five direct-product pairs."
claimant: Problem-21.31 / MathExpert
target_object: "Regular subgroups of Hol(N) for arbitrary finite soluble N"
witness_object: "Central extensions of GL(3,2) by centers of order-12 radicals, restricted to P=C7:C3, and seven order-252 SmallGroups pairs"
witness_equals_target: false
citation: "Standard classification of central extensions by H^2 and universal coefficient sequence; configured Kourovka PDF p. 169"
verification_method: "Complete cohomological argument plus independent exhaustive GAP 4.12.1 pair check"
tools_used: ["GAP 4.12.1", "SmallGrp 1.5.3", "pdftotext 24.02.0"]
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/holomorphs, project/kourovka, status/conjectured]
---

# Verification — Kourovka 21.31 — central pullback refinement

## The claim

Assume the previously checked conditional order-2016 structure: (K=R(G)), (T=G/K\cong GL_3(2)), (G=K C_G(K)), and (H/K=P\cong C_7:C_3), where (H) is the inverse image of the order-21 point stabilizer. Then the full preimage (D\le C_G(K)) of (P) is (Z(K)\times P), so

\[
H=K*_{Z(K)}D\cong K\times P.
\]

Among the seven prior pairs, this eliminates `[252,2]` and `[252,9]` and leaves exactly `[252,17]`, `[252,19]`, `[252,27]`, `[252,29]`, `[252,38]`.

## Target vs witness

The source target is all regular subgroups of `Hol(N)` for every finite soluble `N` (PDF p. 169). The present witnesses are central extensions and abstract order-252 subgroups forced only by a hypothetical counterexample of order 2016. Witness equals target is false. This is a conditional necessary refinement, not a solution or an exclusion of order 2016.

## Sub-claims and what each method proves

### All relevant central extensions restrict split

Put (Z=Z(K)). The action of (T) on (Z) is trivial because (C_G(K)) centralizes (K). Equivalence classes of central extensions

\[
1\to Z\to C\to T\to1
\]

with the fixed kernel and quotient are (H^2(T,Z)). The universal coefficient exact sequence is

\[
0\to \operatorname{Ext}^1(T_{ab},Z)\to H^2(T,Z)
 \to \operatorname{Hom}(M(T),Z)\to0.
\]

The independent GAP check gives `T_PERFECT=true`, hence (T_{ab}=1), and `MULTIPLIER_INVARIANTS=[2]`, hence (M(T)\cong C_2). Therefore

\[
H^2(T,Z)\cong\operatorname{Hom}(C_2,Z),
\]

so every extension class has order dividing 2. This includes non-stem extensions and centers containing 3-torsion; there is no omitted `Ext` term because (T) is perfect.

Restriction sends the class to (H^2(P,Z)). For any finite group, positive-degree cohomology is annihilated by the group order, so (21H^2(P,Z)=0). The restricted class is killed by both 2 and 21, hence is zero. Thus every pullback over (P) splits. Since the kernel is central, the split semidirect product has trivial action and is (D\cong Z\times P).

This is an exhaustive proof for all relevant central extensions, not a multiplier heuristic or a sample enumeration.

### The central product is direct

The multiplication map from (K\times D) onto (H=KD) has kernel the diagonal copy of (Z=K\cap D). With (D=Z\times P), the quotient

\[
(K\times (Z\times P))/\{(z^{-1},(z,1)):z\in Z\}
\]

is explicitly isomorphic to (K\times P), via ((k,(z,p))\mapsto(kz,p)). This preserves the distinguished copy of (K).

### Pair identifications and falsifier

An independently written GAP script:

- found one conjugacy class of order-21 subgroups in (T), represented by `[21,1] = C7:C3`;
- inspected every prescribed normal `K` in all seven survivor types;
- verified (K\cap C_H(K)=Z(K)) and quotient `[21,1]`;
- compared (C_H(K)) with (Z(K)\times P) and (H) with (K\times P).

The explicit falsifier was any nonsplit pullback allowed by the universal extension argument, any predicted elimination with split centralizer, or any predicted survivor not pair-isomorphic to (K\times P). None occurred.

## Circularity check

The multiplier, subgroup lattice, centers, centralizers, and SmallGroups representatives are external data. The cohomological argument classifies all central extensions before comparing their pullbacks with the seven pairs. The five-pair conclusion was not imposed when constructing the objects.

## Evidence

Successful command:

```text
timeout 30s gap -q Agents/Kourovka/problems/21.31/verification/scratch/independent_central_pullback.g > Agents/Kourovka/problems/21.31/verification/scratch/independent_central_pullback.out 2>&1
```

Verbatim output:

```text
GAP_VERSION=4.12.1
SMALLGRP_VERSION=1.5.3
T_ID=[ 168, 42 ] T_SIZE=168 T_PERFECT=true MULTIPLIER_INVARIANTS=[ 2 ]
ORDER21_SUBGROUP_CLASSES=1 P_ID=[ 21, 1 ] P_DESC=C7 : C3
Syntax warning: Unbound global variable in Agents/Kourovka/problems/21.31/veri\
fication/scratch/independent_central_pullback.g:19
    IdGroup(K) = [12,pair[2]] and IdGroup(FactorGroup(H,K)) = [21,1]);
                                                      ^
PAIR=[ [ 252, 2 ], [ 12, 2 ] ] K_DESC=C12 Z_ID=[ 12, 2 ] Z_DESC=C12 D_SIZE=
252 D_ID=[ 252, 2 ] D_DESC=C4 x (C7 : C9) K_INTER_D_SIZE=
12 K_INTER_D_EQUALS_Z=true D_OVER_Z_ID=
[ 21, 1 ] D_IS_Z_TIMES_P=false DIRECT_PRODUCT_PAIR_H_ID=
[ 252, 19 ] H_IS_K_TIMES_P=false
PAIR=[ [ 252, 9 ], [ 12, 5 ] ] K_DESC=C6 x C2 Z_ID=
[ 12, 5 ] Z_DESC=C6 x C2 D_SIZE=252 D_ID=
[ 252, 9 ] D_DESC=C2 x C2 x (C7 : C9) K_INTER_D_SIZE=
12 K_INTER_D_EQUALS_Z=true D_OVER_Z_ID=
[ 21, 1 ] D_IS_Z_TIMES_P=false DIRECT_PRODUCT_PAIR_H_ID=
[ 252, 38 ] H_IS_K_TIMES_P=false
PAIR=[ [ 252, 17 ], [ 12, 1 ] ] K_DESC=C3 : C4 Z_ID=[ 2, 1 ] Z_DESC=C2 D_SIZE=
42 D_ID=[ 42, 2 ] D_DESC=C2 x (C7 : C3) K_INTER_D_SIZE=
2 K_INTER_D_EQUALS_Z=true D_OVER_Z_ID=
[ 21, 1 ] D_IS_Z_TIMES_P=true DIRECT_PRODUCT_PAIR_H_ID=
[ 252, 17 ] H_IS_K_TIMES_P=true
PAIR=[ [ 252, 19 ], [ 12, 2 ] ] K_DESC=C12 Z_ID=[ 12, 2 ] Z_DESC=C12 D_SIZE=
252 D_ID=[ 252, 19 ] D_DESC=C12 x (C7 : C3) K_INTER_D_SIZE=
12 K_INTER_D_EQUALS_Z=true D_OVER_Z_ID=
[ 21, 1 ] D_IS_Z_TIMES_P=true DIRECT_PRODUCT_PAIR_H_ID=
[ 252, 19 ] H_IS_K_TIMES_P=true
PAIR=[ [ 252, 27 ], [ 12, 3 ] ] K_DESC=A4 Z_ID=[ 1, 1 ] Z_DESC=1 D_SIZE=
21 D_ID=[ 21, 1 ] D_DESC=C7 : C3 K_INTER_D_SIZE=
1 K_INTER_D_EQUALS_Z=true D_OVER_Z_ID=
[ 21, 1 ] D_IS_Z_TIMES_P=true DIRECT_PRODUCT_PAIR_H_ID=
[ 252, 27 ] H_IS_K_TIMES_P=true
PAIR=[ [ 252, 29 ], [ 12, 4 ] ] K_DESC=D12 Z_ID=[ 2, 1 ] Z_DESC=C2 D_SIZE=
42 D_ID=[ 42, 2 ] D_DESC=C2 x (C7 : C3) K_INTER_D_SIZE=
2 K_INTER_D_EQUALS_Z=true D_OVER_Z_ID=
[ 21, 1 ] D_IS_Z_TIMES_P=true DIRECT_PRODUCT_PAIR_H_ID=
[ 252, 29 ] H_IS_K_TIMES_P=true
PAIR=[ [ 252, 38 ], [ 12, 5 ] ] K_DESC=C6 x C2 Z_ID=
[ 12, 5 ] Z_DESC=C6 x C2 D_SIZE=252 D_ID=
[ 252, 38 ] D_DESC=C2 x C6 x (C7 : C3) K_INTER_D_SIZE=
12 K_INTER_D_EQUALS_Z=true D_OVER_Z_ID=
[ 21, 1 ] D_IS_Z_TIMES_P=true DIRECT_PRODUCT_PAIR_H_ID=
[ 252, 38 ] H_IS_K_TIMES_P=true
RUN_COMPLETE=true
```

Shell checks and hashes:

```text
RUN_EXIT=0
SENTINEL_EXIT=0
fc2fb78b35753b90d86d99770f45dd1976fbf55d5392ec93a93bb63721c20387  Agents/Kourovka/problems/21.31/verification/scratch/independent_central_pullback.g
1cb2b2a4d11162b1dc904155f8d75dd52298f95cfa80015744a5fbb59d9651ab  Agents/Kourovka/problems/21.31/verification/scratch/independent_central_pullback.out
```

The static GAP warning concerns lexical analysis of the loop-local variable and does not affect execution; the explicit terminal sentinel was present.

An initial draft of the script aborted because `Z` is a read-only GAP global. It produced no pair evidence, was corrected to use `centerK`, and the successful run above is the evidentiary run.

## Verdict

`status/conjectured` overall. The central-pullback refinement itself is verified as a valid conditional deduction, and the bounded pair identifications independently agree with the predicted five survivors. The status is not raised because the witnesses are not the Kourovka target and all conclusions remain conditional on the prior order-2016 reduction.

## Why this verdict

The universal cohomological argument closes the non-stem and 3-primary loopholes, while the independent finite check supplies exact pair identifications and an executable falsifier. Nevertheless, no actual regular subgroup of an order-2016 holomorph was constructed or excluded.

## What is NOT established

- Kourovka 21.31 is not proved or disproved.
- Order 2016 is not excluded.
- None of the five pairs is shown to lift to compatible (G,N), an action, or a bijective crossed map.
- No order above 2016 is addressed.
- The result remains conditional on the previously checked use of Byott's minimal-counterexample structure.

## What would upgrade it

Enumerate a proved-complete set of compatible overgroups/extensions for the five remaining pairs and then verify the full (N), action, and regularity data, or supply a gap-free universal proof in the actual holomorph target.

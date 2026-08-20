---
title: "Verification — Kourovka 12.15 — central lifting and seven H2 obstructions"
problem: 12.15
claim: "The central-Camina lifting lemma is sound, and every central C2-extension of each of seven named order-256 SMP groups has a central lift outside the kernel."
claimant: Problem-12.15
target_object: "all finite 2-groups satisfying the exact Strong Magnus Property"
witness_object: "central C2-extensions of SmallGroup(256,i), i in {53342,53343,53355,...,53359}"
witness_equals_target: false
citation: "none"
verification_method: "hand proof, independent GAP H2-basis extensions, and complete small positive control"
tools_used: ["GAP 4.12.1", "SmallGrp 1.5.3"]
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/cohomology, project/kourovka, status/replicated]
---

# Verification — Kourovka 12.15

## The claim

Two linked claims were checked:

1. If \(1\to Z=\langle z\rangle\to E\to H\to1\) is central, \(|Z|=2\), every \(x\notin Z\) is conjugate to \(xz\), and \(H\) has exact SMP, then \(E\) has exact SMP.
2. For each ID `53342`, `53343`, and `53355` through `53359`, a fixed central involution `f8` has a central lift in every central extension by \(C_2\). Hence none of those extensions is central Camina with kernel equal to its center.

## Target vs witness

The target is the universal Kourovka problem. The witnesses are seven particular order-256 quotient candidates and their marked central extensions. They do not exhaust order-256 SMP groups or all possible counterexamples, so witness equals target is false.

The seven base groups are external SmallGroups objects. The extension classes are computed independently from the full \(H^2(H,C_2)\) with trivial action; they were not constructed by imposing central Camina or the obstruction.

## Sub-claims and what each method proves

### Central-Camina lifting lemma

Let \(\pi:E\to H\). If \(x\notin Z\), conjugacy of \(x\) and \(xz\) gives \(z=x^{-1}x^g\in\langle x\rangle^E\). Therefore
\[
\langle x\rangle^E=\pi^{-1}(\langle\pi(x)\rangle^H).
\]
If two nonkernel elements have equal normal closures, their images have equal normal closures in \(H\), hence are conjugate by SMP. A lifted conjugator sends one element to either the other or its product with \(z\); central Camina fuses those two lifts. The kernel cases are separate: \(1\) and \(z\) have distinct closures, and no nonkernel element has closure contained in \(Z\). Thus the lemma is sound.

The question used “noncentral” in one sentence although the formal hypothesis says “outside \(Z\).” This causes no gap: a central element outside \(Z\) could not be conjugate to its distinct product with \(z\), so the hypothesis itself forces \(Z(E)=Z\).

### Exhaustiveness of the cohomology rows

- Since \(\operatorname{Aut}(C_2)=1\), every extension by a marked normal kernel \(C_2\) has trivial action and central kernel. The full marked extension space is \(H^2(H,C_2)\).
- For commuting \(h,k\in H\), the commutator of chosen lifts lies in the central kernel and is independent of the lift choices. In cocycle coordinates it is the alternating difference of two cocycle values, so it is a linear functional of the cohomology class.
- For fixed \(h\), the map \(k\mapsto[\widetilde h,\widetilde k]\) on \(C_H(h)\) is a homomorphism into \(C_2\). Checking a generating pc sequence of the centralizer is therefore exhaustive.
- Consequently, if the functional vanishes on every vector of a basis of \(H^2(H,C_2)\), it vanishes on every class.

For each named parent, `f8` is central and nonidentity. The independent run found its lift central in each of the 15 basis extensions. Linearity makes a lift central in every one of the \(2^{15}\) classes. That lift maps to `f8`, so it is outside the kernel; the extension center strictly contains the kernel and central Camina is impossible.

The claimant's phrase “computed all commutator functionals” is broader than the script behavior: the script stops at the first universally regular class representative. It computes exactly enough for the exclusion—every basis coordinate for `f8`—but not rows for later representatives.

## Evidence

### Independent base-group check

Script SHA-256:

```text
38d86316ceeada67b53e6453ce8b088b6f690e75de061d33b951a0a0488a9f15  Agents/Kourovka/problems/12.15/verification/scratch/independent_seven_parent_smp.g
```

Complete output:

```text
GAP_VERSION=4.12.1
BASE=[256,53342] EXACT_SMP=true F8=f8 F8_PC_EXPONENTS=
[ 0, 0, 0, 0, 0, 0, 0, 1 ] F8_CENTRAL=true
BASE=[256,53343] EXACT_SMP=true F8=f8 F8_PC_EXPONENTS=
[ 0, 0, 0, 0, 0, 0, 0, 1 ] F8_CENTRAL=true
BASE=[256,53355] EXACT_SMP=true F8=f8 F8_PC_EXPONENTS=
[ 0, 0, 0, 0, 0, 0, 0, 1 ] F8_CENTRAL=true
BASE=[256,53356] EXACT_SMP=true F8=f8 F8_PC_EXPONENTS=
[ 0, 0, 0, 0, 0, 0, 0, 1 ] F8_CENTRAL=true
BASE=[256,53357] EXACT_SMP=true F8=f8 F8_PC_EXPONENTS=
[ 0, 0, 0, 0, 0, 0, 0, 1 ] F8_CENTRAL=true
BASE=[256,53358] EXACT_SMP=true F8=f8 F8_PC_EXPONENTS=
[ 0, 0, 0, 0, 0, 0, 0, 1 ] F8_CENTRAL=true
BASE=[256,53359] EXACT_SMP=true F8=f8 F8_PC_EXPONENTS=
[ 0, 0, 0, 0, 0, 0, 0, 1 ] F8_CENTRAL=true
RUN_COMPLETE=true
EXIT_STATUS=0
```

### Independent basis-extension check

Script SHA-256:

```text
e4747d668419645a21279366b5a34d9c73ca45469e09acb449c3a6101482f04f  Agents/Kourovka/problems/12.15/verification/scratch/independent_f8_basis_centrality.g
```

GAP emitted three static lexical-binding warnings for variables captured in a local predicate; there was no error. Complete substantive output:

```text
GAP_VERSION=4.12.1
BASE=[256,53342] H2_DIM=15 F8=f8 F8_BASE_CENTRAL=true NONCENTRAL_BASIS_CLASS_INDICES=[  ] ALL_BASIS_LIFTS_CENTRAL=true
BASE=[256,53343] H2_DIM=15 F8=f8 F8_BASE_CENTRAL=true NONCENTRAL_BASIS_CLASS_INDICES=[  ] ALL_BASIS_LIFTS_CENTRAL=true
BASE=[256,53355] H2_DIM=15 F8=f8 F8_BASE_CENTRAL=true NONCENTRAL_BASIS_CLASS_INDICES=[  ] ALL_BASIS_LIFTS_CENTRAL=true
BASE=[256,53356] H2_DIM=15 F8=f8 F8_BASE_CENTRAL=true NONCENTRAL_BASIS_CLASS_INDICES=[  ] ALL_BASIS_LIFTS_CENTRAL=true
BASE=[256,53357] H2_DIM=15 F8=f8 F8_BASE_CENTRAL=true NONCENTRAL_BASIS_CLASS_INDICES=[  ] ALL_BASIS_LIFTS_CENTRAL=true
BASE=[256,53358] H2_DIM=15 F8=f8 F8_BASE_CENTRAL=true NONCENTRAL_BASIS_CLASS_INDICES=[  ] ALL_BASIS_LIFTS_CENTRAL=true
BASE=[256,53359] H2_DIM=15 F8=f8 F8_BASE_CENTRAL=true NONCENTRAL_BASIS_CLASS_INDICES=[  ] ALL_BASIS_LIFTS_CENTRAL=true
RUN_COMPLETE=true
EXIT_STATUS=0
```

### Independent positive control

Script SHA-256:

```text
23315b105e2911d29d082594876c53edd6643e4d6e56cd8bc44f11225e13cdb3  Agents/Kourovka/problems/12.15/verification/scratch/independent_c2square_h2_control.g
```

Complete output:

```text
GAP_VERSION=4.12.1 BASE_ID=[ 4, 2 ] H2_DIM=3 H2_CLASSES=8
CENTRAL_CAMINA_CLASS_COUNT=4 CLASS_INDEX_AND_EXTENSION_ID=
[ [ 3, [ 8, 3 ] ], [ 4, [ 8, 3 ] ], [ 7, [ 8, 3 ] ], [ 8, [ 8, 4 ] ] ]
RUN_COMPLETE=true
EXIT_STATUS=0
```

The control proves the screen is not rejecting central-Camina extensions by construction: it recovers three marked \(D_8\) classes and one \(Q_8\) class over \(C_2^2\).

## Verdict

`status/replicated` for the seven specified parent exclusions. The lifting lemma is gap-free. Problem 12.15 itself remains `status/conjectured`.

## Why this verdict

The claimant's basis-row output and an independently written basis-extension check agree, an independent exact-SMP check confirms the seven base objects, and the positive control passes. The linearity proof upgrades 15 basis checks to the complete \(2^{15}\)-class obstruction for each fixed parent.

## What is NOT established

The seven parents came from a partial order-256 catalogue and do not exhaust possible parents. This note does not certify the catalogue, all order-512 extensions, the later isotropic-family reductions, or the universal Kourovka problem. It also does not require or certify the script's separate `E''=C2` rows, because the central-lift obstruction already rejects every class.

## What would upgrade it

An independently certified complete parent catalogue would allow this exact obstruction to be applied to every surviving parent. It would still be only one stage of a proof of the universal assertion.

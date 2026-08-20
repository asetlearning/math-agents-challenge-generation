---
title: "Verification — Kourovka 21.31 — index-8 centralizer filter"
problem: "21.31"
claim: "Conditional on the order-2016 reduction, H=K C_H(K), eliminating SmallGroups types [252,11] and [252,40] from the nine necessary pairs."
claimant: Problem-21.31
target_object: "Regular subgroups of Hol(N) for arbitrary finite soluble N"
witness_object: "Nine order-252 SmallGroups types and all prescribed normal order-12 subgroups"
witness_equals_target: false
citation: "Configured Kourovka PDF p. 169; prior verification of Byott Theorem 3.2 reduction"
verification_method: "hand proof and independent exhaustive GAP 4.12.1 SmallGroups enumeration"
tools_used: ["GAP 4.12.1", "SmallGrp 1.5.3", "pdftotext 24.02.0"]
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/holomorphs, project/kourovka, status/conjectured]
---

# Verification — Kourovka 21.31 — index-8 centralizer filter

## The claim

Under the previously checked conditional order-2016 reduction, the forced subgroup (H) obeys (H=K C_H(K)); this necessary condition removes `[252,11]` and `[252,40]` and leaves seven of the nine SmallGroups pairs.

## Target vs witness

PDF p. 169 asks whether every regular subgroup of `Hol(N)` is soluble for every finite soluble `N`. The witnesses here are only nine abstract order-252 groups and their prescribed normal order-12 subgroups. Witness equals target is false, so the overall verdict cannot exceed `status/conjectured`.

## Sub-claims and what each method proves

Let (G=K C_G(K)) and let (H/K\le G/K). For (h\in H), write (h=kc), with (k\in K,c\in C_G(K)). Since (K\le H), (c=k^{-1}h\in H), hence (c\in C_H(K)). Thus (H\le K C_H(K)); the reverse inclusion is immediate. This proves the identity under the prior hypotheses only.

The independent script enumerated every prescribed normal subgroup in each `H`, rather than choosing `Ks[1]`. Each pair has exactly one candidate. It independently reproduces the two eliminations and seven survivors. A pass proves only this bounded necessary filter.

The SmallGroups representatives are external library objects, so the test is not true by construction. However, the predicate is only necessary; survivors do not establish lifts.

## Evidence

Command:

```text
timeout 30s gap -q Agents/Kourovka/problems/21.31/verification/scratch/independent_index8_filter.g > Agents/Kourovka/problems/21.31/verification/scratch/independent_index8_filter.out 2>&1
```

Verbatim output:

```text
GAP_VERSION=4.12.1
SMALLGRP_VERSION=1.5.3
Syntax warning: Unbound global variable in Agents/Kourovka/problems/21.31/veri\
fication/scratch/independent_index8_filter.g:9
    IdGroup(K) = [12,pair[2]] and IdGroup(FactorGroup(H,K)) = [21,1]);
                                                      ^
PAIR=[ [ 252, 2 ], [ 12, 2 ] ] CANDIDATE_K=1 KC_ORDERS=[ 252 ] PASSING_K=1
PAIR=[ [ 252, 9 ], [ 12, 5 ] ] CANDIDATE_K=1 KC_ORDERS=[ 252 ] PASSING_K=1
PAIR=[ [ 252, 11 ], [ 12, 5 ] ] CANDIDATE_K=1 KC_ORDERS=[ 84 ] PASSING_K=0
PAIR=[ [ 252, 17 ], [ 12, 1 ] ] CANDIDATE_K=1 KC_ORDERS=[ 252 ] PASSING_K=1
PAIR=[ [ 252, 19 ], [ 12, 2 ] ] CANDIDATE_K=1 KC_ORDERS=[ 252 ] PASSING_K=1
PAIR=[ [ 252, 27 ], [ 12, 3 ] ] CANDIDATE_K=1 KC_ORDERS=[ 252 ] PASSING_K=1
PAIR=[ [ 252, 29 ], [ 12, 4 ] ] CANDIDATE_K=1 KC_ORDERS=[ 252 ] PASSING_K=1
PAIR=[ [ 252, 38 ], [ 12, 5 ] ] CANDIDATE_K=1 KC_ORDERS=[ 252 ] PASSING_K=1
PAIR=[ [ 252, 40 ], [ 12, 5 ] ] CANDIDATE_K=1 KC_ORDERS=[ 84 ] PASSING_K=0
ELIMINATED_H=[ [ 252, 11 ], [ 252, 40 ] ]
SURVIVING_H=[ [ 252, 2 ], [ 252, 9 ], [ 252, 17 ], [ 252, 19 ], [ 252, 27 ], 
  [ 252, 29 ], [ 252, 38 ] ]
```

```text
RUN_EXIT=0
131d0d15585ab64506fa5b8cf7bef6cb2292680cd07355395730a3acaaa50888  Agents/Kourovka/problems/21.31/verification/scratch/independent_index8_filter.g
b8da002f1fece61ae0b627a77ba4160a1e73fdad71d57fff12d98381bdb0e258  Agents/Kourovka/problems/21.31/verification/scratch/independent_index8_filter.out
```

## Verdict

`status/conjectured` overall. The bounded nine-pair computation is independently replicated and the conditional identity is valid, but the witnesses are not the Kourovka target.

## Why this verdict

The finite filter is exact and independently agrees with the claimant. Protocol nevertheless requires the lower status because this is a necessary subobject filter conditional on a hypothetical counterexample, not a check in an actual target holomorph.

## What is NOT established

No counterexample exists; order 2016 is not excluded; none of the seven survivors lifts to compatible groups (G,N), an action, or a regular embedding; and Kourovka 21.31 remains open.

## What would upgrade it

Construct and completely verify a target regular embedding, or exhaust a proved-complete universe of all compatible extension/action data and eliminate it.

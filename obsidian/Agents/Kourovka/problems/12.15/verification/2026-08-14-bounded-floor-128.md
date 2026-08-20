---
title: "Verification — Kourovka 12.15 — bounded SmallGroups floor through 128"
problem: 12.15
claim: "No SmallGroups-library 2-group of order at most 128 is a counterexample to Problem 12.15."
claimant: Problem-12.15
target_object: "all finite 2-groups with equal-normal-closure conjugacy"
witness_object: "all SmallGroups library groups of orders 2, 4, 8, 16, 32, 64, and 128"
witness_equals_target: false
citation: "none"
verification_method: "independent exhaustive elementwise GAP scan"
tools_used: ["GAP 4.12.1", "SmallGrp 1.5.3"]
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, project/kourovka, status/replicated]
---

# Verification — Kourovka 12.15

## The claim

Within the complete SmallGroups library at every 2-power order through 128, no group simultaneously has nonabelian derived subgroup and the exact property that equal normal closures force conjugacy.

## Target vs witness

PDF page 58 quantifies over **all** finite 2-groups. The witness is only the finite library range through order 128, so witness equals target is false. This note certifies a bounded floor only.

## Sub-claims and what each method proves

1. A counterexample must have nonabelian `DerivedSubgroup(G)`, so filtering out metabelian groups is lossless for a counterexample search. It does not catalogue all SMP groups.
2. Normal closure is constant on a conjugacy class. Therefore either conjugacy-class representatives or all elements give an exact SMP test.
3. The claimant iterated every library ID and compared closures of class representatives. The independent script iterated the same complete ID ranges but cached the closure of **every element** and compared all pairs, rejecting equal closures unless GAP's exact conjugacy test passed.
4. Agreement proves the bounded library statement at `status/replicated`. It says nothing about larger orders or the universal assertion.

## Evidence

Independent script SHA-256:

```text
62f5548cdda5e4c170ca726e530b1b00c64d4461347f161a333e29eead2c1fc6  Agents/Kourovka/problems/12.15/verification/scratch/independent_floor_128_elementwise.g
```

Complete command output:

```text
$ timeout 30s gap -q Agents/Kourovka/problems/12.15/verification/scratch/independent_floor_128_elementwise.g
GAP_VERSION=4.12.1
ORDER=2 NUMBER_SMALL_GROUPS=1 NONMETABELIAN=0 COUNTEREXAMPLE_IDS=[  ]
ORDER=4 NUMBER_SMALL_GROUPS=2 NONMETABELIAN=0 COUNTEREXAMPLE_IDS=[  ]
ORDER=8 NUMBER_SMALL_GROUPS=5 NONMETABELIAN=0 COUNTEREXAMPLE_IDS=[  ]
ORDER=16 NUMBER_SMALL_GROUPS=14 NONMETABELIAN=0 COUNTEREXAMPLE_IDS=[  ]
ORDER=32 NUMBER_SMALL_GROUPS=51 NONMETABELIAN=0 COUNTEREXAMPLE_IDS=[  ]
ORDER=64 NUMBER_SMALL_GROUPS=267 NONMETABELIAN=0 COUNTEREXAMPLE_IDS=[  ]
ORDER=128 NUMBER_SMALL_GROUPS=2328 NONMETABELIAN=14 COUNTEREXAMPLE_IDS=[  ]
RUN_COMPLETE=true
EXIT_STATUS=0
```

These counts agree with the claimant's independent class-representative run, including the 14 nonmetabelian order-128 groups and the empty passing list.

## Verdict

`status/replicated` for the explicitly bounded floor through order 128. The universal Problem 12.15 remains `status/conjectured`.

## Why this verdict

Two independently written exact scans agree, one classwise and one elementwise. The filter is sufficient for finding counterexamples because the failed conclusion is exactly nonabelianity of the derived subgroup.

## What is NOT established

No claim is made beyond order 128, about a hybrid minimum-order floor through 256, or about all finite 2-groups. SmallGroups identifiers are library objects; if a future positive candidate appears, it must also be reconstructed independently from a presentation.

## What would upgrade or extend a future floor

For each newly claimed bound, require all of the following:

1. state the exact orders and whether the claim is about every group or only nonmetabelian candidates;
2. record GAP and package versions, `NumberSmallGroups(order)`, the exact ID interval, script hash, timeout, exit status, and a terminal completion sentinel;
3. prove every prefilter is necessary for a counterexample, not merely correlated with one;
4. use an independently written checker—preferably an elementwise formulation if the claimant used class representatives;
5. record stage counts whose totals reconcile with every library ID;
6. do not turn a timed-out prefix into an exhaustive claim;
7. keep the bounded conclusion separate from the universal target.

A completed negative finite scan can reach `status/replicated`; it cannot by itself prove the universal assertion.

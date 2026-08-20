---
title: "Problem 20.49 proof direction — two-minimal-normal subdirect pairing"
problem: "20.49"
scope_id: 20.49/two-generated-same-exponent
assignment_revision: 1
direction: proof
strategy: TWO-MINIMAL-NORMAL-SUBDIRECT-PAIRING
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/exponent
  - topic/subdirect-product
  - project/kourovka
  - status/draft
---

# Working log

## 2026-08-17T13:34:28Z — work start

Cumulative active minutes in this clean proof lane: 0. Absolute allocation: 45
active minutes; strategy kill: 30 active minutes if compatibility is still an
unsupported choice.

Canonical scope revision 1, current proof roster, the newest Lead direction-switch,
and its single linked reviewed verification note were read. No unreviewed
counterexample working note was opened. The reviewed inputs used below are:

- a hypothetical least-order counterexample `G` is finite, nonsoluble,
  directly indecomposable, and has `d(G)=3`;
- every proper subgroup and every nontrivial proper quotient has exponent strictly
  below `exp(G)`;
- the universal statement itself remains unanswered.

Let `M,N` be distinct minimal normal subgroups. Then `M cap N=1`, so the map

`G -> A x B`, where `A=G/M` and `B=G/N`,

is injective. Put `C=G/MN`. The image is the fibre product

`A x_C B = {(a,b): alpha(a)=beta(b)}`,

for the natural quotient maps `alpha:A->C` and `beta:B->C`.

## 2026-08-17T13:41:13Z — exact criterion obtained; strategy stop

Cumulative active minutes in this clean proof lane: 9.

The full argument is frozen in [[findings]]. The key exact facts are:

1. `exp(G)=lcm(exp(A),exp(B))`.
2. Every two-generator pair upstairs is exactly a pair of homomorphisms
   `F_2->A,B` having the same composite to `C`.
3. Its generated subgroup exponent is exactly the least common multiple of its
   two projected subgroup exponents.
4. Therefore full-exponent quotient witnesses pair if their base pairs in `C`
   lie in the same Nielsen orbit.
5. Minimality supplies nonempty sets of full-exponent lift orbits separately in
   `A` and `B`, but supplies no intersection. In a hypothetical counterexample
   those two sets must be disjoint.
6. Disjointness of the full/full sets is not yet the complete obstruction: every
   compatible pair of projected exponent profiles must miss some common maximal
   prime power. This is stated exactly in [[findings]].

This freezes the requested Goursat/fibre obstruction and its exponent effect.
The proposed inference to monolithicity cannot proceed by independently selecting
the two quotient witnesses; a new orbit-intersection or prime-profile theorem is
required. The strategy has yielded a `PARTIAL_RESULT` rather than an answer to the
active scope. No replacement method is started. State: `awaiting_lead`.

## Work stop

Stopped at `2026-08-17T13:41:13Z`; cumulative active minutes in this lane: 9.

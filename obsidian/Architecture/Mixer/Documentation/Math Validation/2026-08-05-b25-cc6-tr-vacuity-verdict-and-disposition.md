---
title: CC6-TR corridor census — vacuity verdict (CONFIRMED, with proof of cause) and route disposition
status: disproven
domain: group-theory
project: b25-infinite-witness
claim: "The mutual-uniqueness corridor graph is vacuous on the frozen 26 survivors; CC6-TR concludes nothing at rung 6."
claimant: B25 Experimenter (census) / Lead (routing)
verification_method: independent derivation of the uniform candidate density from relator periodicity
tools_used: [exhaustive window census over the 26 survivors]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25-infinite-witness, topic/uniformity, status/disproven, proof]
---

# CC6-TR census — verdict and disposition

## 1. Verdict stamp: VACUITY CONFIRMED — and the cause is now proven, not observed

B25 reported 0 mutual-unique edges, 100% branch tokens, exactly 24 candidates per end, perfectly
uniform. I verified the density independently and derived **why** it is uniform:

```
length-5 windows on one relator p^5 (30 positions), over the 26 survivors:
  156 distinct windows, EVERY ONE occurring exactly 5 times      {5: 156}
contacts per (ordered cell pair, shared piece)  kA*kB = 25       (uniform)
candidates visible from any one contact         kA*kB - 1 = 24   (uniform)
```

**The cause is that the relators are fifth powers.** `p⁵` has period 6, so every length-5 window
recurs once per period — exactly 5 times. Two cells sharing a piece therefore admit `5 × 5 = 25`
contacts, and from any one of them the other **24** are candidates. The uniformity is not a property
of these 26 words; it is forced by periodicity.

**Consequence, stronger than the reported result:** mutual-uniqueness cannot fire at *any* threshold,
because the candidate count is a constant independent of the input. B25's "structurally incapable" is
correct, and it now has a proof rather than an observation. **The mechanism is not repairable by
tuning.**

**And it generalises.** For exponent `n` every window recurs `n` times, so candidates `= n² − 1`,
uniform. The degree-≤2-by-construction / mutual-uniqueness mechanism is dead at **every exponent and
every rung**, not only at n=5, ℓ=6. This is the periodicity analogue of the exponent-6 audit, and it
becomes a standing acceptance test (§4 below).

Receipts (`infinite_b25/avenues/cc6_tr/`, pre-reg run-complete, both authority notes pinned) and B25's
conduct are in order: census run first as required by (2-o2), nothing claimed beyond the vacuity, no
positivity, candidate density correctly treated as input rather than result, and the exponent-4/6
control correctly called moot since no lemma was drawn.

## 2. Disposition

**CLOSED-NEGATIVE, with proof — the mechanism.** The mutual-uniqueness corridor construction carries
no corridor content, at this rung or any other. It should not be retried.

**NOT CLOSED — CC6-TR as a route.** Per the no-premature-close bar, the authorized module is
exhausted but the route is not, and here is every untested item:

1. **Branch tokens — 100% of ends, and now the entire object.** §4 defers them as "separate local
   obligations". The vacuity did not destroy the content; it *moved all of it* into a bucket that has
   never been analysed. This is the largest untested item and it is not a leftover.
2. **Cycles.** A cycle has no ends, so it is immune to the branch-token collapse that killed the path
   module — the one structure the census says nothing about. It is also §4's own predicted failure
   mode (closed flat corridor with propagating defect letters). Untested and still unauthorized.
3. **Rank-1 capped modules** — the 16 `(1,1)` arcs.
4. **Corridor-formation rules other than mutual-uniqueness.** The *mechanism* is dead; the *concept*
   of a corridor is not. Any replacement must clear §4 below.

**The close/continue call is not mine.** My verdict is on the mathematics: the mechanism is refuted,
the route is not exhausted. Program direction routes to Maria.

## 3. What this does NOT say

It is not evidence for or against the ℓ=6 barrier, and it must not be stacked with the 26→26
conjugacy result into a program conclusion. Both are negatives about **mechanisms** — root conjugacy
does not dedup the survivors, and mutual-uniqueness does not form corridors. Neither speaks to
whether filtering rescues clause 6. The decisive input remains a certified realized `P_6`, still
blocked on rung-5 `gpaxioms ec=0`.

## 4. New standing acceptance test (periodicity audit)

Any proposed corridor-formation rule, at any rung, must first be checked against the `n² − 1`
uniformity: **if the rule's candidate density is a constant forced by relator periodicity, no
uniqueness or minimality criterion built on it can ever fire.** Cheap, decisive, and it would have
predicted this census before it was run. I will apply it alongside the exponent-4/6 audit to every
such rule routed to me.

## Verdict

- Vacuity: **#status/proven** (cause derived, not merely replicated).
- Mutual-uniqueness corridor mechanism: **#status/disproven**, at all rungs and exponents.
- CC6-TR as a route: **open**, with four enumerated untested modules; close/continue to Maria.

## 5. Corrected edge-stage receipt — every number reconstructs a priori

The complete census reconstructs from the piece oracle alone, before any of it is run. All 72
rank-3/5 pieces are carried by **exactly 2** survivor classes (`carrier-count histogram {2: 72}`),
and each occurs once per period:

```
half-occurrences = 72 x 2 cells x 5 occurrences  =    720    B25:    720
contacts         = 72 x (5 x 5)                  =  1,800    B25:  1,800
contact ends     = 1,800 x 2                     =  3,600    B25:  3,600
candidates / end = 25 - 1                        =     24    B25: {24: 3600}
D4-passing pairs = 3,600 x 24 / 2                = 43,200    B25: 43,200
```

Exact on every line. This is stronger than reproducing the computation: the numbers were **forced
before it ran**. `B_zero_partner = 0` follows from the 2-carrier structure (every occurrence pairs
with all 5 on the other cell), and `B_base_gap = 45,000` is the D4-failing complement, consistent
with the earlier 88,200 = 45,000 + 43,200 split.

**Two of my open flags are discharged by this receipt.** The mandatory D4 negatives now pass on both
sides, so D4 demonstrably rejects and is no longer untested. And the post-D4 ε assertion recorded
0 violations — the Part-6 enforcement mode (assertion, not filter) behaved as intended.

**Correction to ell6 note §4.10.** It records that "only branch-vertex or relative base-gap
continuation repairs remain". That is an **under-count** of the untested space under the
no-premature-close bar: it drops items 2 and 3 of §2 above. **Cycles** in particular are not a repair
of the path module at all — a cycle has no ends, so the end-based collapse cannot reach it, and it is
§4's own predicted failure mode. The remaining space is **four** items, not two.

Scope unchanged: no program-direction claim, no B(2,5)-infinite claim; Kourovka 11.48 open.

Extends [[2026-08-05-b25-stage1-v2-disposition-and-CC6-TR-preruling]],
[[ell6-theory-barrier-analysis-2026-08-05]].

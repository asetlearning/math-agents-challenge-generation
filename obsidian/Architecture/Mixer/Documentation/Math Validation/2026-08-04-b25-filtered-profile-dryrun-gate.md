---
title: Filtered-profile dry run (ℓ=4,5 over G_3 oracle) — Validator gate + duplicate/coincidence ruling
status: replicated
domain: group-theory
project: b25-infinite-witness
claim: "Duplicate-rejection is the correct treatment for point 2 IFF the criterion is genuine G_L-conjugacy; the filtered profile is still ℓ-1 at ℓ=4,5, so filtering does not (yet) rescue clause 6."
claimant: Delta (dry run) / Validator (gate + design-decision ruling)
verification_method: independent G_3-conjugacy check of the flagged AABAB/ABABB coincidence; ε recomputation
tools_used: [G_3 wordreduce, short-conjugator search]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25-infinite-witness, topic/uniformity, status/replicated, proof]
---

# Filtered-profile dry run — gate

Delta built the filtered check to my 5-point pre-ruling, ℓ=4,5, G_3 oracle. **Accept as a valid
methodology pilot (#status/replicated, scope: ℓ=4,5 over G_3).** The one judgment call — the
duplicate-vs-coincidence treatment — I rule **SOUND, with a precise criterion requirement.**

## THE design decision (point b): duplicate-rejection vs coincidence-counting — RULING
The un-deduplicated pilot correctly surfaced the point-2 risk: AABAB / ABABB would create G_3-equal
length-20 realized arcs. Delta rejects them as duplicates. **I verified this is correct:** (AABAB)^5 and
(ABABB)^5 are **G_3-conjugate** — a short conjugator g="ba" gives g·(AABAB)^5·g⁻¹ =_{G_3} (ABABB)^{±5}.
So ⟨⟨(AABAB)^5⟩⟩ = ⟨⟨(ABABB)^5⟩⟩: they are the **same relator**, hence redundant, hence one is a genuine
duplicate. The large realized coincidence is *because they are the same relator*, not a distinct-pair
overlap. **Duplicate-rejection satisfies point 2 for this pair.**

**Requirement (the one thing to nail):** the duplicate criterion must be **genuine G_L-conjugacy of the
relators** (p^5 is G_L-conjugate to q^{±5}, equivalently ⟨⟨p^5⟩⟩=⟨⟨q^5⟩⟩), NOT rotation/cyclic-NF equality
and NOT a shared-arc heuristic. **My rotation-based cyclic-NF proxy MISSED this pair** (they are not
rotation-equal), yet they are conjugate — so a rotation-based filter would wrongly KEEP them and then
falsely count a length-20 overlap (a spurious C'(1/6) catastrophe). Conversely, a shared-arc heuristic
could over-reject a distinct pair that merely overlaps a lot. **Delta must confirm the filter tests
conjugacy** (via the certified oracle: search a conjugator, or decide ⟨⟨·⟩⟩ equality). Correct pipeline =
**(1) dedupe by G_L-conjugacy, then (2) count max G_L-realized overlap among the pairwise-NON-conjugate
remainder.** Both steps are needed; the dry run does step 1 for AABAB/ABABB correctly.

## The load-bearing negative signal: filtered max is STILL ℓ-1
Delta reports filtered max piece = **ℓ-1** at both ℓ=4 (3) and ℓ=5 (4), with ε = 5/6 − (ℓ-1)/ℓ =
1/ℓ − 1/6 (I recomputed: 1/12 at ℓ=4, 1/30 at ℓ=5 — matches), **positive but → 0 at ℓ=6.** So **G_L-
filtering does NOT reduce the profile below ℓ-1 at ℓ=4,5.** After removing genuine conjugate-duplicates,
there remain distinct non-conjugate genuinely-new relators still sharing ℓ-1 geodesic letters. This is a
**negative signal for the clause-6 rescue**: the filtered profile is not sublinear; it tracks ℓ-1, so the
ℓ=6 barrier (ε=0) is unlikely to be rescued by filtering. Per my pre-ruling point 5, if this trend holds
at ℓ=6 → clause-6 route is dead → abandon classical C'(1/6) for a graded large-overlap framework (or cap
the method at ℓ=5).

## The decisive test is ℓ=6-over-G_5, NOT ℓ=5-over-G_4
Important scoping for the staged run: the barrier bites at **ℓ=6** (ε=0). The staged ℓ=5-over-G_4 run
will rigorously **validate ℓ=5** (where ε=1/30>0, method already expected to work) — but it does **NOT
cross the barrier.** The program-direction decision (does filtering rescue the ℓ=6 barrier) needs the
**filtered profile at ℓ=6 over the certified G_5 oracle** — a further rung out. Do not let the ℓ=5 run be
read as deciding the barrier; it confirms the one-more-rung case, not the failure point. The ℓ=4,5
evidence (filtered max = ℓ-1) already *suggests* the barrier will stand, but ℓ=6-over-G_5 is the rigorous
decider.

## Other results
- **Selection cross-check:** ℓ=4 selects EXACTLY the known five G_4 roots — a clean independent
  corroboration of the G_4 setup/ladder. ✓
- **Bookkeeping to reconcile (flag, non-blocking):** ℓ=5 "24 candidates → 14 genuinely new (8
  nongeodesic, 4 trivial-fifth-power, 4 G_3-duplicates)" — 24 − (8+4+4) = 8, not 14. Either 14 is a
  typo for 8, the rejected categories overlap (double-counting), or the base differs. Reconcile so the
  receipt is internally consistent.
- **ℓ=5 cap census clean (0 exotic)** and **zero orientation violations** — support clauses 7 and SO at
  the one-more-rung case. ✓

## Verdict
- Dry run: **#status/replicated** (ℓ=4,5, G_3 oracle). Methodology sound; selection correct.
- Design decision: **duplicate-rejection is SOUND** and satisfies point 2, **contingent on a genuine
  G_L-conjugacy criterion** (verified for the flagged pair; require Delta confirm the filter is
  conjugacy-based, not rotation/arc-based). Pipeline: conjugacy-dedupe, then overlap-count the remainder.
- Signal: **filtered max = ℓ-1 at ℓ=4,5 ⇒ filtering does not rescue clause 6 so far** (ε→0 at ℓ=6).
- **The decisive input remains the FILTERED profile at ℓ=6 over the certified G_5 oracle.** The staged
  ℓ=5-over-G_4 run validates ℓ=5 but does not cross the barrier.

Scope unchanged: no program-direction / no B(2,5)-infinite claim; Kourovka 11.48 open.

## SIGN-OFF (2026-08-04, after Delta's three fixes) — dry-run gate CLOSED
All three fixes independently verified:
1. **Dedup upgraded to certified G_L-conjugacy — VERIFIED.** I re-checked all four ℓ=5 duplicate
   witnesses: `reduce(g·p^5·g⁻¹·target⁻¹)=IdWord` holds for AABBB~AAABB⁻ (g=aa), AAbbb~AAAbb⁻ (g=BB),
   ABABB~AABAB⁻ (g=AB), AbAbb~AAbAb⁻ (g=Ab) — and each pair is **not** already G_3-equal, so the
   conjugator is genuinely required (exactly the conjugate-but-not-rotation-equal case a proxy would
   miss). All four are conjugate-to-INVERSE with 2-letter conjugators. Criterion is now genuine
   conjugacy with explicit certificates. **My core requirement met.**
2. **Bookkeeping reconciled — VERIFIED.** ℓ=5: 8 nongeo + 0 trivial-only + 2 conjdup-only + 14 selected
   = 24; ℓ=4: 4 rejected + 5 selected = 9. Both check.
3. **Decider staged correctly.** ℓ=6-over-G_5 dependency chain (G_4 oracle → rung-5 → G_5 oracle →
   ℓ=6 filtered); G_4/ℓ=5 run labeled "validates one-more-rung only, does not cross the barrier." Matches
   my ruling.
Numerical conclusions unchanged (ℓ=4 max 3 ε=1/12; ℓ=5 max 4 ε=1/30; acid 78/78). **Dry-run gate CLOSED.**

**Forward note for the ℓ=6 decider (not a blocker now):** the dedup is asymmetric — rejection is a
positive certificate (witness g), absence is *bounded-search evidence* (default |g|≤ℓ-1). So the
SELECTED set's pairwise non-conjugacy is bounded-search, not proof: a pair marked "distinct" with
overlap ℓ-1 could be a hidden duplicate via a longer conjugator. This means the reported filtered max is
an **upper bound** on the genuine-distinct max. That is *sufficient for the direction decision* (if the
ℓ=6 upper bound is still ℓ-1 = 5 = 5ℓ/6, filtering does NOT rescue clause 6). But a rigorous
*barrier-confirmation* (a genuine non-conjugate ℓ-1 pair exists) would want the ℓ-1-overlap pairs' non-
conjugacy checked beyond |g|≤ℓ-1, or explicitly labeled bounded-search. Flag it so the ℓ=6 run reports
which reading it supports.

Verifies: `Infiniteness/data/receipts/filtered_oracle_profile_g3_ell4_5_summary_20260804T121850Z.md`
(+ corrected artifacts, timestamp 123456Z). Extends [[2026-08-04-b25-literal-piece-profile-gate]].

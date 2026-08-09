---
title: Gate 2 batch rulings — SEI receipts (i), B/C/U' + Hyp2 (ii), C(3) scan pre-ruling (iii)
status: conjectured
domain: group-theory
project: b25-infinite-witness
claim: "SEI enumeration + orientation theorem close aligned SEI; phase-offset SEI/C(3) still route through Hyp 2."
claimant: Delta (SEI receipts) / Math-expert (U') / Validator (rulings)
verification_method: orientation-theorem proof (no self-inverse) + contour cancellation checks + quantifier audit
tools_used: [G_3 free reduction, cyclic self-inverse check, cap receipt]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25-infinite-witness, status/conjectured, proof]
---

# Batch rulings: SEI receipts + U' + C(3) pre-ruling

## (i) SEI topology-quantifier — PARTIAL ACCEPT (aligned CLOSED; phase-offset pends Hyp 2)

**New certified theorem (a strengthening of Delta's "6.4M zero same-orientation" to a proof):**
No period p_i is cyclically equal to its inverse (verified: inv(p_i) ∉ rotations(p_i), all five). A
length-≥4 shared arc is a p-power; the opposite cell reads its inverse = a p^{-1}-power, which is a
subword only of p^{-5}. **Therefore every long same-period contact forces OPPOSITE orientation — a
THEOREM, not just an empirical count.** So no same-orientation long-contact class can be dropped. ✓
I certify this; it removes one of the two ways the enumeration could have missed a class.

**Aligned local reduction is genuinely global-size-independent — ACCEPT:** an *aligned* opposite pair
sharing p^m has contour p^{5-m}·p^{-(5-m)} = ε (verified for all m) ⇒ area-reducible (drop 2) ⇒
contradicts minimality. This reduction is LOCAL (2 cells), so the bounded enumeration validly covers
**aligned** SEI bands of any global size. The 39,920 case-2 witnesses (`band_contour_free_reduction=''`
literal, 2→0 cells, area_drop=2 — verified not asserted) are legitimate for aligned bands. ✓ (74MB,
no sampling — good discipline.)

**DO NOT yet accept full SEI closure — the phase-offset gap:** a *phase-offset* opposite pair has a
NON-trivial contour (residual phase, verified len 22–24, NOT ε), so it is **not** covered by the
`contour=''` enumeration. Every enumerated record is `contour=''` (aligned). So the topology-quantifier
claim "every SEI band contains a verified `contour=''` reduction" is established **only for aligned
bands**; **phase-offset SEI bands route through Lemma B (phase absorption) ⇒ Hypothesis 2**, still
unproven. **Ruling: SEI = {aligned: CLOSED via the opposite-pair theorem} + {phase-offset: conditional
on Hyp 2}.** Delta must state how phase-offset SEI configs are handled: do they arise, and if so are they
enumerated and reduced (via Lemma B), or is a phase-alignment theorem (= Hyp 2) being invoked to exclude
them? The honest `pending_topology_quantifier_acceptance` flag is right; I accept the aligned part, hold
the phase-offset part on Hyp 2.

## (ii) B/C/U' package + Hypothesis 2 — reaffirm prior verdict; SEI connects to it
Per [[2026-08-02-b25-gate2-unified-lemma-U-review]]: Lemma B VALID (local cell-coordinate argument,
receipt corroborated), Lemma C valid conditional on Hyp 2, and **Hypothesis 2 ("all phase caps are
cell-boundary caps ≤3, never a long internal bridge") is NOT a theorem — the load-bearing gap.** The SEI
result **confirms the connection**: SEI's phase-offset closure depends on exactly Lemma B / Hyp 2. So
**Hyp 2 is the single crux** for the phase-offset case across internal bands + SEI + C(3). Everything now
funnels to it.

## (iii) C(3) two-interval scan — pre-ruling on quantifier coverage (build it right the first time)
Requirements for the C(3) enumeration to be acceptable:
1. **Orientation theorem applies for free** — long contacts are opposite (proved above); C(3) bands
   contain opposite pairs, so aligned C(3) bands reduce by the same `contour=''` local move. Verify the
   witnesses (contour='' literal, area drop) exactly as SEI did — **don't assert.**
2. **Cover BOTH boundary intervals AND internal-sided BRIDGES.** The v0.5/v0.6 scans dropped internal
   bridges (sides internal, both ends on ∂D) and short endpoints — do NOT repeat that. Enumerate the
   two-interval + bridge topology explicitly.
3. **Log the aligned-vs-phase-offset distinction AND the cap-vs-bridge distinction (§10.5).** Aligned →
   local reduction (closes). Phase-offset → routes to Lemma B/Hyp 2 (flag, don't silently reduce). A
   connector that is a LONG internal bridge (not a ≤3 cell-boundary cap) is NOT a phase cap — it must be
   flagged as a potential exceptional object, not fed to the cap receipt.
4. **Provable exhaustiveness.** Either (like SEI) prove "every C(3) band contains a local reducible
   opposite pair," or enumerate to a proven connector bound. State the quantifier and its justification.
5. Same 74MB-style all-records, no-sampling discipline; honest status flag pending my acceptance.

If built this way, aligned C(3) closes (opposite-pair theorem); phase-offset C(3) pends Hyp 2 — same as
SEI. So **C(3) and SEI both reduce to: aligned (CLOSED) + phase-offset (Hyp 2).**

## Net Gate 2 status
- The **orientation theorem** (no self-inverse ⇒ opposite long contacts) is a clean new closure lever: it
  makes ALIGNED SEI, ALIGNED C(3), and aligned internal bands all reduce by the local `contour=''`
  opposite-pair move — **certifiable now.**
- **Everything phase-offset** (SEI, C(3), internal bands) funnels to **Hypothesis 2** (connectors are
  short cell-boundary caps, never long bridges) — the single load-bearing unproven theorem. This is the
  whole ballgame.
- Curvature core (3.1) VALID, transfer (4.1) VALID-cond, annuli CLOSED, ladder DISCHARGED, L2.1/2.2 VALID.

**Gate 2 = CONDITIONAL, gated on Hypothesis 2.** No rung-4 / E7-survival claim.

## Notes
- Certify + reuse: the orientation theorem (no period cyclically self-inverse ⇒ every long same-period
  contact is opposite). It closes ALL aligned cases via the local opposite-pair reduction.
- The one remaining math is **Hypothesis 2**. Prove it (phase connectors are short cell-boundary caps,
  never long internal bridges) and — combined with the orientation theorem + aligned finite checks —
  SEI, C(3), and phase-offset internal bands all close, completing the curvature argument.
- G_4 automatic structure completing still bypasses all of this.

Verifies: `gate2_sei_receipts/gate2_sei_enumeration_20260802T133533Z.json` (sha per Delta),
`band_contraction_core.md §§9–10`. Extends [[2026-08-02-b25-gate2-unified-lemma-U-review]].

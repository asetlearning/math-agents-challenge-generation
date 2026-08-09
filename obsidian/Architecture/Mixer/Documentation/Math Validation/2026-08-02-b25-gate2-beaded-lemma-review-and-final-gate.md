---
title: Gate 2 §11.8 Beaded Lemma review — conclusion ACCEPTED (proof needs fix); H2 complete; final gate = C(3) receipts
status: conjectured
domain: group-theory
project: b25-infinite-witness
claim: "Beaded bridges are C'(1/6)-harmless; H2 complete; composition gated only on aligned C(3) receipts."
claimant: Math-expert (§11.8) / Validator (review)
verification_method: per-piece C'(1/6) analysis; pigeonhole-premise check; composition sweep
tools_used: [free reduction, C'(1/6) arithmetic, orientation theorem, cap receipt]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25-infinite-witness, status/conjectured, proof]
---

# §11.8 Beaded Lemma — review + composition gate

**Ruling: §11.8's CONCLUSION (beaded bridges are C'(1/6)-harmless) is CORRECT and I ACCEPT it — but via
the clean per-piece argument, NOT the written pigeonhole proof, which is flawed (and, fortunately,
unnecessary).** With the beaded case discharged, **H2 is complete** (§11.2 single-cell caps + §11.8
beaded-harmless cover all phase connectors), so the load-bearing Hypothesis 2 is discharged. The
composition is then gated on **exactly one** remaining item: Delta's aligned C(3) receipts.

## Lead's pressure point 1 (claim 4, the face budget) — RESOLVED, and it makes claim 1 unnecessary
The correct argument is **per-piece**: each bead ≤3 (claim 2, sound) ⇒ every bead is a C'(1/6) piece
(3/20 < 1/6), **regardless of how many beads there are**. Lemma 3.1's conclusion is **existential** (SOME
boundary face has ≤3 internal pieces exposing ≥11). Extra beaded pieces — each ≤3 — keep the diagram
C'(1/6), so Greendlinger still finds a good face; no face's account is broken. **So harmlessness needs
ONLY claim (2); the bead-count bound r≤3 (claim 1) is NOT load-bearing.** §11.8's phrasing ("the beaded
connector costs ≤3 pieces / ≤9 letters / same exposure estimate") is the *wrong* framing — it conflates
the beaded connector with Greendlinger's output-face complement and thus leans on the (flawed) claim 1.
**Fix: replace claim (4)'s proof with the per-piece C'(1/6) argument; drop claim (1) and the ≤9-letter
framing.**

## Lead's pressure point 2 (pigeonhole premise) — CONFIRMED FLAWED (but moot after the fix)
Claim (1)'s pigeonhole needs: "a consecutive bead subchain of total length ≡0 (mod 4) is a complete
p-block, hence absorbed by §11.1." **§11.1 as written absorbs genuine periodic p^m subpaths, not arbitrary
length-≡0-mod-4 subchains.** A phase-jumping or distinct-period bead subchain can have length ≡0 (mod 4)
without being a periodic block — e.g. `AB`+`Ab` = `ABAb` (length 4, but ≠ p = ABaB, not a p-block), so
§11.1 does NOT absorb it. Hence the pigeonhole premise is **not enforced**, and claim (1) is not proven as
written. (Also: distinct-period beads don't advance the p-phase by their length, breaking the prefix-sum
setup.) **This is a real flaw — but moot, since claim (1) is unnecessary (pressure point 1).**

## Claims 2 and 3 — SOUND
- **(2) each bead ≤3:** piece bound + pocket maximality (long ≥4 ⇒ same-period ⇒ in the pocket; distinct
  ≥4 forbidden). ✓
- **(3) beads are separate ordinary pieces; false subdivision merges to a still-≤3 arc:** ✓ (a piece is a
  maximal shared edge-arc; merged still ≤3 by the piece bound). The coexistence handling (beads meet long
  contacts only at endpoints; post-surgery contacts re-banded by 2.1) is correct.

## Net on §11.8: ACCEPT the lemma via the corrected proof
Beaded bridges contribute only ≤3 ordinary pieces (each ≤3), so they keep the final realized-piece diagram
C'(1/6), and Lemma 3.1 applies unchanged. **Beaded bridges are harmless.** Required edit: rewrite the proof
per pressure-point-1 (per-piece C'(1/6)); drop the pigeonhole (claim 1). The mathematical content survives.

## H2 is now COMPLETE
Every phase connector is either (i) a single-cell cap ≤3 (§11.2, airtight) or (ii) a multi-cell beaded
bridge (§11.8, harmless ordinary pieces). These are exhaustive. **So Hypothesis 2 is discharged** — the
load-bearing gap I named is closed (single-cell proved + beaded harmless). Lemma B/C then absorb the
single-cell caps; beaded bridges need no absorption (they're already C'(1/6)-ordinary).

## Composition sweep — one gate remains
| component | status |
|---|---|
| annuli | CLOSED (E(p)=⟨p⟩) |
| internal disc contraction (L2.1/2.2) | VALID; phase-offset → aligned via caps + beaded |
| curvature core (L3.1) | VALID |
| strict-arc transfer (L4.1) | VALID (boundary-preserving; folded into aligned checks) |
| orientation theorem (SO) | CERTIFIED — closes all ALIGNED cases via opposite-pair reduction |
| H2 (§11.2 + §11.8) | **COMPLETE** (single-cell + beaded) |
| SEI | **aligned ACCEPTED** (39,920 witnesses); phase-offset → aligned |
| **C(3)** | aligned two-interval receipts **IN FLIGHT** (Delta, (iii) spec) — **the one open gate** |
| ladder | DISCHARGED |

Everything reduces to **aligned pockets**, and aligned pockets reduce by the certified opposite-pair
move — verified for SEI. **The composition is complete the moment Delta's aligned C(3) receipts land clean
at the (iii) spec** (two intervals + bridges + short endpoints covered; beaded class populated; witnesses
verified, not asserted; provable quantifier).

## PREPARED FINAL RULING (to fire when C(3) receipts land)
- **If** Delta's C(3) receipts are clean (every aligned two-interval no-progress pocket has a verified
  zero-contour reduction or strict exposure; zero genuine exceptional/beaded survivors; quantifier
  covers bridges + short endpoints; witnesses literal) **AND** §11.8's proof is corrected to per-piece:
  → **#status/proven: E7 ≠ 1 in G_4** — the first certified period-band step at exponent 5.
- **If** the C(3) receipts surface a genuine exceptional aligned pocket (no reduction, no strict, not
  beaded-harmless): → that is a real obstruction → **Gate 2 closes as bounded-obstruction-frontier**
  (the accepted fallback). No E7-survival claim.

I will do the final composition ruling on receipt of the C(3) data — not before. No rung-4 claim stands
yet. `#status/conjectured`.

## Notes
- Math-expert: rewrite §11.8 claim (4) as per-piece C'(1/6); drop claim (1) pigeonhole (flawed + unneeded);
  add the §11.1 clarification (block boundaries label-canonical).
- Delta: C(3) receipts at the (iii) spec, beaded class explicitly populated; verify witnesses.
- G_4 automatic structure completing still gives an independent E7≠1 route bypassing all of this.

Verifies: `band_contraction_core.md §11.8`. Extends [[2026-08-02-b25-gate2-H2-decisive-review]],
[[2026-08-02-b25-gate2-SEI-receipts-and-batch-rulings]].

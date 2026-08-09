---
title: Gate 2 DECISIVE review — Lemma H2 (§11.2) — NOT yet proven; beaded_phase_bridge is the surviving gap
status: conjectured
domain: group-theory
project: b25-infinite-witness
claim: "Lemma H2 proves every phase connector is a short cell cap ≤3, closing the phase-offset case."
claimant: Math-expert (§11 proof proposal) / Validator (decisive review)
verification_method: line-by-line of §11.2 block-normalization; orientation-theorem certification; beaded-phase feasibility check
tools_used: [cyclic self/cross-inverse check, beaded-phase arithmetic, cap receipt, piece-core]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25-infinite-witness, status/conjectured, proof]
---

# DECISIVE review — Lemma H2 and the Gate-2 composition

**Ruling: I do NOT accept Lemma H2 as a complete proof, and I therefore do NOT issue the final
`#status/proven` ruling on E7≠1 in G_4.** §11.2 genuinely proves the *single-cell* case; but the
**beaded_phase_bridge** class (Lead's pressure point b) is **asserted empty, not proved**, and I verified
it is **arithmetically non-vacuous**. This is now the single surviving mathematical gap. I hold the line —
the convergence is real progress, but not closure.

## Lead's pressure points

### (a) Is block-normalization well-defined diagram-side? — ACCEPT (with one clarification)
Block boundaries are **canonical per cell**: a p^5 cell's label fixes its five p-block boundaries (no free
choice). Each cell lies in **at most one** same-period pocket (pockets are maximal same-period unions;
distinct-period contacts are ≤3, never blocks), so **no cross-pocket block-assignment conflict** arises.
The residual "which adjacent aligned run does a boundary block belong to" choice does **not** change the
connector's residue *length* (|γ| mod 4). So the convention is well-defined. **Clarify in the write-up:**
state that block boundaries are label-determined (canonical), not chosen. Accept.

### (b) The crossing case-analysis — NOT exhaustive; beaded_phase_bridge is the GAP
§11.2 is airtight for a connector lying on a **single** p^5 cell boundary: |γ|=4q+k, the 4q absorbs into
an aligned run, residue k<4 is cell-local. ✓ **But the case analysis considers only a single ≤3 crossing.**
It does **not** rule out a phase change **beaded across multiple cells** via a sequence of ≤3 pieces:
`c_0 (piece_1) c_1 (piece_2) c_2 …`, each contact ≤3, no single absorbable full block, yet a **net** phase
change. I verified this is **arithmetically possible**: short same-period pieces of lengths e.g. (2,2,2)
accumulate net phase 6 ≡ 2 (mod 4); (1,1,1) → 3; (2,3) → 1 — each piece <4, net phase ≠0. So the
`beaded_phase_bridge` class is **not** trivially empty. §11.3 names it precisely but only says "I do not
currently see such an object … but naming the class keeps the verifier honest" — that is an **assertion,
not a proof of emptiness.** **Lemma H2 is therefore not proven.**

**Likely resolution (constructive, but must be WRITTEN):** a beaded phase path made entirely of ≤3
same-period pieces is **ordinary C'(1/6) structure** — every realized piece is ≤3, so it is handled by the
curvature core (Lemma 3.1) and is *not* a long-contact band obstruction; it need not be "absorbed" as a
cap at all. If Math-expert proves: *"any phase connector that is not a single ≤3 cell cap is a
concatenation of ≤3 ordinary pieces, hence C'(1/6)-harmless (introduces no length-≥4 contact and does not
break the Greendlinger count),"* then the beaded class is discharged and H2's role is fulfilled: the only
obstructions are long (≥4) same-period contacts (= pockets), whose end-caps are short by the single-cell
argument. **This is plausibly straightforward but is not in §11 — it is the exact remaining obligation.**
Caution to check when writing it: a beaded path between two sides of a *pocket* (which has long internal
contacts) must be shown not to interact with those long contacts in a way that re-creates an obstruction.

### (c) Does H2 hold for SEI/C(3) external caps identically? — for single-cell caps yes; beaded inherits (b)
The single-cell argument is **boundary-placement-independent** (Lemma B already established a cap on ∂D is
still a cell-boundary subpath), so single-cell external phase caps are ≤3, same as internal. **But beaded
external configurations (SEI/C(3) phase beaded across boundary ≤3 pieces) inherit exactly the (b) gap.** So
H2's SEI/C(3) applicability is as strong — and as incomplete — as the internal case: it stands or falls
with the beaded resolution.

## Lemma SO (§11.6) — VALID, certified
Matches my independently-derived orientation theorem. Certified: **no period is cyclically conjugate to
its inverse, and no cross-pair p_i ~cyc q_j⁻¹** (verified: `inv(q) ∉ rotations(p)` for all ordered pairs
incl. self). So every long same-period contact is opposite-oriented — a **theorem**. (Distinct-period long
contacts are anyway ≤3-forbidden by the piece bound, so the cross-pair extension is belt-and-suspenders,
but correct.) Reuse freely. This is the clean lever that closes all **aligned** cases.

## Composition status — NO final PROVEN ruling
The composition is: annuli CLOSED · L2.1/2.2 VALID · curvature (3.1) VALID · transfer (4.1) VALID-cond ·
ladder DISCHARGED · orientation theorem (SO) CERTIFIED · aligned SEI/C(3) reduced via the local
opposite-pair move · Lemma B VALID for single-cell caps · **H2 = single-cell PROVED, beaded case OPEN.**

**Everything now funnels to one point: the `beaded_phase_bridge` emptiness/harmlessness.** Until it is
proved (beaded ≤3-paths are impossible, or are C'(1/6)-harmless ordinary structure), Lemma U'/H2 rests on
an assertion, and **E7≠1 in G_4 is NOT established.** I decline the final ruling.

**Gate 2 = CONDITIONAL, gated on the beaded case.** No rung-4 / E7-survival claim. When (1) Math-expert
proves beaded bridges impossible-or-harmless AND (2) Delta's C(3) receipts land clean at the (iii) spec,
request the final composition ruling and I will do it.

## Notes for Math-expert / Delta
- **The one remaining proof:** discharge `beaded_phase_bridge` — prove a phase connector that is not a
  single ≤3 cell cap is a concatenation of ≤3 ordinary pieces and hence C'(1/6)-harmless (or impossible).
  I verified the class is arithmetically non-vacuous, so "I don't see it" is not enough.
- Delta's C(3) enumerator MUST populate/scan the `beaded_phase_bridge` class explicitly (per §11.3/§11.4)
  and report it non-empty if found — do not let block-normalization silently drop it.
- SO / orientation theorem is certified — build the aligned checks on it.
- G_4 automatic structure completing still bypasses H2 and the whole band taxonomy.

Verifies: `band_contraction_core.md §11` (esp. §11.2, §11.3). Extends
[[2026-08-02-b25-gate2-SEI-receipts-and-batch-rulings]], [[2026-08-02-b25-gate2-unified-lemma-U-review]].

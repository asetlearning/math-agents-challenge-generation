---
title: Gate 2 FINAL composition verdict — does the period-band meta-theorem prove E7≠1 in G_4?
status: conjectured
domain: group-theory
project: b25-infinite-witness
claim: "Meta-theorem v0.3 skeleton + discharged obligations compose into a complete proof of E7≠1 in G_4."
claimant: Lead / Math-expert / Delta
verification_method: full composition audit — skeleton, three obligations, quantifier match, setup facts
tools_used: [read all Gate-2 receipts+scripts, hashes verified, independent connector/period/geodesic checks]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25-infinite-witness, status/conjectured, proof]
---

# Gate 2 FINAL composition verdict

**VERDICT: CONDITIONAL.** The composition is *not yet* a complete proof of E7≠1 in G_4. Most components
are genuinely in place and verified, but **two genuine mathematical write-ups remain unwritten**, and
they are the load-bearing ones. Asserting `#status/proven` now would be premature and retraction-prone —
exactly the failure my role exists to prevent, and the stakes (first certified period-band step at
exponent 5) demand it be right, not fast.

## The overall logic (sound, if the hypotheses hold)
If E7=1 in G_4 there is a minimal relative diagram D over G_3+{p_i^5} with ∂D = E7-NF (geodesic,
length 128). The meta-theorem would give a boundary cell with a **strict Dehn arc** (exposed ≥12,
complement ≤8) — a subword of E7-NF equal in G_3 to a shorter word, contradicting E7-NF geodesic
(corroborated: E7 has zero strict hits). ⇒ no D ⇒ E7≠1. **This closing logic is sound.** The question
is entirely whether the meta-theorem's hypotheses are *proved* for all minimal E7 diagrams.

## What IS solid (verified, keep)
- **Annulus (obl. 2): CLOSED.** E(p_i)=⟨p_i⟩ to B_ann=24 (only period-power connectors, zero
  inverting) — Delta's scan + my independent |c|≤7 brute-force. Same-period annuli are dipoles ⇒
  excluded. Rigorous.
- **Distinct-period piece bound ≤3: PROVED** (periodicity/pigeonhole, robust to infinite band sides).
- **Axis certificate** (|p_i^k|=4k ∀k): independently verified (DFA pumping + metric cross-check).
- **Threshold 4 tight; 3/20<1/6 ⇒ exposed ≥12; strict-arc⇒contradiction:** all correct.
- **v0.5 "bad objects" were spurious:** correctly caught (else a wrong bounded-frontier close).

## (a) Band-contraction topological write-up — **GAP, not mechanical. Blocks PROVEN.**
The piece-core (no fake long pieces) is proved. But the meta-theorem's **step 4** — that contracting
harmless internal disc bands yields a *valid reduced C'(1/6) disc diagram* D′ with (T1) genuine
[p,q]-map structure, (T2) all realized pieces ≤3, (T3) ∂D′=E7-NF preserved, (T4) a strict arc in D′
transferring to a strict arc on E7-NF — is **not written**, and it is **not a paragraph-fill**:
- There is a real subtlety I flagged: "contract to shorter side" reduces cells/contact-length, which
  interacts with the lexicographic **minimality** of D; the operation must be set up so it doesn't
  either contradict minimality prematurely or fail to transfer the Greendlinger cell back to ∂D.
- The clean rigorous route is likely **not** "contract then classical Greendlinger" but a **direct
  combinatorial-curvature (Gauss–Bonnet) argument** on the band-reduced diagram (bands as generalized
  regions) — the Ol'shanskii/McCammond–Wise style. That is several pages of careful curvature
  bookkeeping for *these* relators and bands, standard-in-spirit but genuinely to-be-done-and-checked.
**I will not dictate this as a few paragraphs and call it proven.** It is the mathematical heart that
remains. Recommendation: write it as a direct curvature argument; I will verify it line-by-line.

## (b) C(3) quantifier match — **MISMATCH. Not rigorously discharged. Blocks PROVEN.**
The meta-theorem's C(3) quantifies over **all** boundary-to-boundary same-period no-progress bands
(equal sides, no strict arc, endpoints compatible with cyclic E7). The v0.6 evidence does **not**
instantiate that quantifier:
- **`gate2_v06_corrected_c3_scan.py`** closes by a length inequality: a band needs a single
  *contiguous phase-coherent* E7 interval `endpoint_1|side_left|endpoint_2` with each contact ≥4
  (⇒ ≥12), but E7's max ABaB/ABab run is 7. **But its band model is narrow** — it enumerates single
  R_i-cell boundary exposures with one contiguous external interval and **endpoints ≥4**. It does
  **not** demonstrably cover: (i) **internal-sided "bridge" bands** (sides internal, only the two ends
  on ∂D), (ii) bands with **short endpoints** (<4), (iii) bands whose two boundary touchings are **not
  contiguous** on E7. The "≥12 required" and "endpoints ≥4" assumptions are not justified for the full
  C(3) class — so the length inequality may under-cover the quantifier (a soundness risk: clearing
  C(3) on too narrow a model).
- **`gate2_v06_holonomy.py`** (my suggested algebraic route) runs on the **v0.5 records — which I
  already ruled spurious** (area-0, hardcoded equal sides, cross-product). Enriching non-bands with
  holonomy data and finding "all killed/period-power" does **not** establish closure for *genuine*
  bands. Wrong input set.
**Rigorous closure needs the GENERAL lemma, not a scan:** *every* same-period no-progress boundary
band has transverse holonomy conjugating p_i^m to p_i^m ⇒ holonomy ∈ E(p_i)=⟨p_i⟩ (already proved) ⇒
band untwists to same-period dipoles ⇒ reducible ⇒ contradicts minimality. This closes C(3) for **all
words**, independent of E7's periodic profile. The open-band (2-endpoint) version of this holonomy
lemma is **not yet written** (it is cleaner for the closed annulus, done). I can take it.

## (c) Additional/unlisted obligations
- **(c1) Ladder/presentation correctness.** The proof needs G_4 = G_3/⟨⟨p_1^5..p_5^5⟩⟩ with **exactly**
  these 5 as the new relators (LADDER.md: "4 of 9 length-4 classes already trivial in G_3"). Not
  independently re-verified by me; must be confirmed (the kbmag `g4` file has 17 relators for all
  length-≤4 w^5 — the 5-new decomposition relative to G_3 must be checked).
- **(c2) Single-external-interval boundary bands.** A boundary band with **one** external interval, no
  strict arc, no shortening, is neither boundary-to-boundary (C(3) as stated) nor internal (contraction
  scope). This taxonomy case must be explicitly covered (or folded into the curvature argument).
- **(c3) Greendlinger on realized pieces.** Step 5 must use the curvature/realized-piece version (not
  the presentation-level C'(1/6) statement) — subsumed into the (a) write-up.
- No independent G_4 automatic-structure cross-check exists (kbprog non-confluent, gpmakefsa failed),
  so the period-band proof is currently the *only* route — the two gaps genuinely gate the result.

## Verdict: CONDITIONAL — exactly what remains
1. **Band-contraction / curvature core (a):** write and verify the direct combinatorial-curvature
   argument that a band-reduced, C(D)-satisfying, no-strict-arc minimal E7 diagram forces a strict
   boundary arc (with realized pieces ≤3, bands handled). **The mathematical heart; unwritten.**
2. **C(3) general holonomy lemma (b):** prove no-progress boundary bands reduce via
   holonomy ∈ E(p_i)=⟨p_i⟩ (open-band case). Current scans are corroborating evidence with a
   quantifier gap, not a proof.
3. **Setup confirmations (c):** ladder correctness (G_4 = G_3 + exactly the 5); single-external-interval
   boundary-band case.

When 1 and 2 are written and I verify them (and c confirmed), this becomes `#status/proven` — a genuine
first certified period-band step at exponent 5. **Until then it is CONDITIONAL, not proven.** No
retraction risk taken. The annulus closure, piece-core proof, and axis certificate stand as real,
reusable results regardless.

## Notes for downstream
- Do NOT tag `#status/proven` or announce "E7 survives in G_4 / rung-4 theorem" until gaps 1 & 2 are
  written and Validator-verified. The finite receipts are inputs, not the proof.
- Route the (a) curvature write-up and (b) holonomy lemma to Math-expert; I will verify both. I can
  draft the (b) open-band holonomy lemma myself if Lead prefers.
- The G_4 automatic structure, if it lands, is a valuable independent cross-check (would corroborate,
  not replace, the period-band proof).

Verifies (composition): `math_expert_R2_full.md` §Gate 2 + v0.3/v0.4 obligations; Delta
`gate2_v05/v06` receipts (hashes verified); prior notes [[2026-08-02-b25-gate2-period-band-metatheorem]],
[[2026-08-02-b25-gate2-annulus-and-C3-proofs]].

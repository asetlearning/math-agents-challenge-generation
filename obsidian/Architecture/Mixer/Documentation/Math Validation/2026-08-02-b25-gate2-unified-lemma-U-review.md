---
title: Gate 2 unified band-reduction package (Lemmas B/C/U') — Validator line-by-line
status: conjectured
domain: group-theory
project: b25-infinite-witness
claim: "Lemmas B+C+U' eliminate phase-offset + SEI + C(3) simultaneously, closing the curvature argument."
claimant: Math-expert (draft) / Lead (cap receipt) / Validator (review)
verification_method: line-by-line lemma audit + independent spot-check of the cap-conjugator receipt
tools_used: [G_3 wordreduce, cap-conjugator exhaustive check, E(p)=⟨p⟩]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25-infinite-witness, status/conjectured, proof]
---

# Unified package (Lemmas B / C / U') — review

Genuine progress: the package **correctly reduces the phase-offset case to the aligned case** via a valid
*local* argument (Lemma B). But it does **not close** the open-band problem — it **relocates** it to two
unproven inputs, one of which is exactly Lead's paranoia flag. **Verdict: U' is a valid REDUCTION,
conditional on Hypothesis 2 (a theorem still to prove) and Hypothesis 4 (aligned checks, in flight).**

## Cap-conjugator receipt — CORROBORATED
Independent spot-check (my own enumeration, all |c|≤3, all 5 periods × k=1,2,3): the canonical conjugator
u_k=p[:k] works everywhere, and **every** solution of `c·rot_k(p)·c⁻¹ =_{G_3} p` lies in `u_k·⟨rot_k(p)⟩`
— **zero exotic** (the 4 extra AABB/AAbb k=2 caps are the power-identities aaa=A², BBB=b², bbb, as
stated). Solid finite input. ✓

## (1) Lemma B (phase-cap transporter) — VALID, incl. external-boundary caps
The **local** argument is airtight *for a genuine short cell-boundary phase cap*: the cap c is a subpath
of ONE p^5 cell boundary; in that cell's coordinate the two incident full-p-blocks read p and rot_k(p),
and c is the basepoint-change u_k, so `c·rot_k(p)·c⁻¹ =_{G_3} p` is forced — a free-group identity for
c=u_k, with the receipt ruling out any other short cap. **§10.2 last para is correct:** even when the cap
lies on ∂D (SEI/C(3)), it is still a cell-boundary subpath, so the equation is forced by the **cell
coordinate, not a global annular conjugacy.** This is a real, correct answer to my route-B objection —
*for short caps*. ✓

## (2) Lemma C (phase absorption / telescoping) — VALID conditional on Hyp 2
Given Lemma B at each cap, absorbing u_k turns a `(rot_k p)^a` side into an aligned `p^a` side (up to
axis powers in ⟨p⟩, harmless); interior phase changes telescope across the cell stack. Correct **provided
every phase transition is a short cell-boundary cap (Hypothesis 2).** ✓ conditional.

## (4) Hypothesis 2 — NOT a theorem; the load-bearing assumption. **Lead's flag CONFIRMED.**
Hyp 2 = "all phase caps of B are actual cell-boundary caps of length ≤3." This is **an assumption, not a
theorem about reduced diagrams.** It requires proving: *in a minimal reduced diagram over G_3+{p_i^5},
every phase connector between phase-shifted periodic sides of a same-period pocket is a short (≤3)
cell-boundary cap — never a long internal bridge.* The package's own **§10.5** and the **receipt
(lines 22–23)** explicitly defer this ("Math-expert's to write"; "if a candidate uses an arbitrary
internal side NF as c, it must be handled by §9 cap-pair or returned as exceptional"). **If a connector
is a long internal bridge, Lemma B does not apply and the exact open-band cell-cancellation difficulty
returns.** Plausibility argument (phase transitions happen intra-cell, hence short) is suggestive but not
a proof. **Until Hyp 2 is a theorem, U' rests on it.** This is precisely the load-bearing step Lead
smelled — correct instinct.

## (3) U' case-completeness — conditional on Hypothesis 4
After phase absorption the 4-case disjunction (aligned-BR2 / shortening / strict / dipole) is exhaustive
**only if** the `exceptional_open_band` case is excluded — i.e. Hypothesis 4 ("aligned SEI/C(3) finite
checks report no genuine exceptional aligned pocket," Delta in flight, my raised bar). And note: even an
**aligned same-orientation** pocket has the non-cancellation `p^4·p^4 = p^8 ≠ 1` (verified earlier), so
Hyp 4 is the **same open-band cancellation, now for aligned pockets** — it must be genuinely *resolved*
(reductions verified, all aligned configs covered), not assumed. So the disjunction is exhaustive modulo
Hyp 4, which is not yet established.

## What the package achieves vs. what remains
**Achieves (real):** reduces {phase-offset, SEI, C(3)} → {aligned SEI, aligned C(3)} via Lemma B/C
(receipt-backed, local, correct). The phase-enumeration is genuinely disposed of.
**Remains (two unproven inputs U' rests on):**
- **(A) Hypothesis 2 as a THEOREM** — every phase connector in a minimal reduced diagram is a short
  cell-boundary cap, never a long internal bridge. Load-bearing; currently a modelling assumption. **This
  is the crux.** My rejected route-B and this both die if long internal bridges can occur.
- **(B) Hypothesis 4** — aligned-pocket finite checks (SEI/C(3) for aligned sides) actually close, with
  reductions verified and the aligned same-orientation p^8≠1 cancellation genuinely resolved. Delta in
  flight; hold the raised bar (verify, don't assert; cover all configs incl. bridges/short-caps).

## Gate 2 status (ledger)
| # | obligation | status |
|---|---|---|
| 1 | annuli | CLOSED |
| 2 | internal-contraction (L2.1/2.2) | lemmas VALID; phase-offset residual now **reduced to aligned** via L B/C, conditional on Hyp 2 |
| 3 | curvature (L3.1) | VALID |
| 4 | strict-arc transfer (L4.1) | VALID conditional |
| 5 | SEI | reduced to aligned SEI finite check (Hyp 4, in flight) |
| 6 | C(3) | reduced to aligned C(3) finite check (Hyp 4, in flight) |
| 7 | ladder | DISCHARGED |
| — | **Hyp 2 (all connectors short caps)** | **NOT a theorem — load-bearing, unproven** |

**Gate 2 = CONDITIONAL.** The package is a genuine reduction (phase → aligned, valid), but E7≠1 in G_4
now rests on **Hyp 2 (theorem needed)** + **Hyp 4 (aligned checks)**. No rung-4 / E7-survival claim.

## Notes for Math-expert / Delta
- **Prove Hyp 2** (the crux): in a minimal reduced diagram, phase connectors are short cell-boundary caps,
  never long internal bridges. Give the diagram-combinatorial argument (why a connector at a long-contact
  endpoint must be intra-cell ≤3), OR show long-bridge connectors reduce/exclude. This is the last real
  math; I will verify it hard (it is where route B died).
- Hyp 4: aligned SEI/C(3) checks — verify reductions, cover bridges + short caps, resolve aligned
  same-orientation cancellation. Raised bar stands.
- Lemma B and the receipt are solid and reusable.
- If the G_4 automatic structure completes + gpaxioms passes, it decides E7-in-G_4 independently and
  bypasses obligations 2–6 and Hyp 2/4 entirely — still the highest-leverage outcome.

Verifies: `band_contraction_core.md §§9–10`, `cap_conjugator_receipt.md` (independently corroborated).
Extends [[2026-08-02-b25-gate2-curvature-core-review]], [[2026-08-02-b25-gate2-C3-candidate-closure-REJECTED]].

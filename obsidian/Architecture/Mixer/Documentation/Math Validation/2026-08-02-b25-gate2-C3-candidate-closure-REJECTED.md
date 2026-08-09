---
title: Gate 2 route-B candidate G1 closure — NOT VERIFIED (exact gap; corrects my own draft)
status: conjectured
domain: group-theory
project: b25-infinite-witness
claim: "Candidate area-reduction/zipper closure of G1 (open-band no-progress ⇒ reducible) is rigorous."
claimant: Math-expert (candidate) / Validator (review)
verification_method: algebra of the asserted boundary form + open vs closed band structure + G3 reducer test
tools_used: [G_3 wordreduce, free reduction, E(p)=⟨p⟩]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25-infinite-witness, status/conjectured, proof]
---

# Route-B candidate G1 closure — NOT VERIFIED

**Verdict: NOT VERIFIED — the candidate has a genuine gap; I do not accept it. Returning the exact
remaining gap. This review also corrects a flaw in MY OWN earlier draft
([[2026-08-02-b25-gate2-C3-holonomy-lemma-draft]], steps 2–3), which shared the same defect — caught on
review.** Maximal paranoia as this is the final rigor step; better to expose the flaw than to certify it.

## What IS correct in the candidate
- **Area-reduction mechanism (valid).** IF the open-band boundary ∂B reads `p^a p^c p^{-a} p^{-c}` (in the
  single p-axis coordinate after alignment), it **freely reduces to the empty word** (verified: p^{a+c}
  p^{-(a+c)} → ε for all tested a,c). Then ∂B bounds an **area-0** diagram, so the band can be excised and
  the hole zipped, **lowering R-cell area ⇒ contradicts minimality.** Correct — and the improvement
  "minimality needs only area reduction, not a literal BR1 dipole" is right.
- **G3 sign − (valid).** The orientation-reversing case is ruled out by the verified **no-inverter**
  fact (E(p)=⟨p⟩ has no c with c p^a c⁻¹ = p^{-a}).

## The gap (load-bearing): the boundary form is ASSERTED, not DERIVED
The whole closure rests on the antecedent **"∂B reads p^a p^c p^{-a} p^{-c} (freely trivial)."** That is
**not established** — it is the conclusion (the m band cells cancel), assumed.

- **Open ≠ closed.** For an OPEN disc band, ∂B =_{G_3} (product of the m cell-relators p^{±5}). This is
  trivial in G_4 but **not** freely trivial / not trivial in G_3 in general, because **p has infinite
  order in G_3**. The clean conjugacy `x_R = p^{-a} x_L p^a` is the **ANNULUS** relation (a closed loop
  where the cells cancel around it — that is why obligation (2) closed cleanly). An open disc band has
  **no such closed-loop conjugacy**; its p^5 cell-relators are present and do not cancel a priori.
- **Concrete witness (G_3 reducer).** Opposite-oriented pairs DO telescope to freely-trivial (m=2
  opposite, shared p^k → ε). But **same-orientation / general-phase corridors do NOT**: e.g. p^4·p^4 =
  p^8 has G_3-NF length 8 (≠ 1). So "∂B freely trivial" holds for the telescoping sub-case, **not in
  general** — it is exactly the cell-cancellation that a real band-reduction lemma must PROVE.
- **G2 (phase-0) unresolved and load-bearing.** `x_L = p^c` needs the end-cap phase ≡ 0 (mod |p|=4). A
  factor of p^∞ of length ≢ 0 mod 4 is `p^k · s` with s a **proper prefix** of p; since p is primitive,
  **s ∉ ⟨p⟩**, so x_L ∉ E(p) and the "x_L ∈ E(p) ⇒ x_L=p^c" step fails. The proposed finite phase-cycle
  check is the right instrument but must be **performed and shown to yield phase 0** — it is not obvious
  and may fail.

## Why the annulus argument does not transfer (root cause)
Obligation (2) closed because an **annulus** gives a genuine conjugacy `x p^a x⁻¹ = p^b` (two boundary
circles cobounding), letting E(p)=⟨p⟩ force x ∈ ⟨p⟩. An **open band** is a disc: its boundary is a
product of non-cancelling p^5 cells, with **no closed-loop conjugacy**, so E(p)=⟨p⟩ has no clean hook.
Route B's slogan silently reused the annulus relation for the open band. That is the error (in both the
candidate and my draft).

## Net: C(3) is GENUINELY OPEN (downgrade from "nearly closed")
Neither route now closes C(3):
- **v0.6 corrected scan:** quantifier gap (models only single contiguous external `endpoint|side|
  endpoint`, endpoints ≥4; misses internal-sided bridges, short endpoints, non-contiguous touchings).
- **Route B (this candidate + my draft):** the freely-trivial-boundary antecedent is unestablished for
  open bands; phase-0 unproven.

**What would actually close C(3):**
1. A genuine **Ol'shanskii-style band-reduction lemma**: a cell-by-cell periodic analysis proving that a
   no-progress p-band's m cells cancel (∂B freely trivial). This is real technical work (the periodic
   small-cancellation core), not a slogan. The area-reduction mechanism + no-inverter are then usable.
   OR
2. A **correctly-scoped finite scan** covering ALL boundary-to-boundary configurations (internal-bridge,
   short-endpoint, non-contiguous), not just the v0.6 contiguous-external model.

I can help formalize (1) or spec (2), but I will not certify C(3) until one is done and verified.

## Gate 2 status (updated)
- Obligation (2) annulus: **CLOSED.**
- Obligation (1) band-contraction/curvature **core**: **OPEN** (gap a).
- Obligation (3) C(3): **OPEN** — route B as sketched is not valid; scan has a quantifier gap.
**CONDITIONAL, with (1) AND (3) open.** More open than the prior composition review indicated —
appropriately, because careful review of the route-B step exposed a real flaw (in the candidate and in
my own draft). **No rung-4 / E7-survival claim. #status/conjectured.**

## Notes
- Own-error disclosure: my draft note's closure relation (step 2) and x_L∈E(p) (step 3) are NOT valid
  for the open band; I retract those steps. The annulus closure (obligation 2) stands unaffected.
- Do not tag C(3) closed on the v0.6 scan or on route B as currently written.
- If the G_4 automatic structure lands (gpmakefsa -h in progress) + gpaxioms passes, that is an
  independent E7≠1-in-G_4 route that would bypass this entire period-band obligation set — worth watching.

Corrects: [[2026-08-02-b25-gate2-C3-holonomy-lemma-draft]]. Extends:
[[2026-08-02-b25-gate2-FINAL-composition-verdict]].

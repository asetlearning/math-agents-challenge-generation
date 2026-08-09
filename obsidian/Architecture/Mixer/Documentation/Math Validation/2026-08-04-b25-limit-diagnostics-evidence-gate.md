---
title: Limit diagnostics (growth-rate trajectory + E7 witness) — Validator evidence gate
status: replicated
domain: group-theory
project: b25-infinite-witness
claim: "Collatz-Wielandt growth brackets λ_1..4 and E7 NF-length stabilization are sound EVIDENCE (pre-gpaxioms), NOT a limit theorem; λ_L is a decreasing upper bound on B(2,5) growth."
claimant: Delta (diagnostics) / Validator (evidence gate)
verification_method: CW-bracket method soundness check; independent derivation of the λ_1=1+√3 anchor; state-count reconciliation
tools_used: [numpy power-iteration sanity, Z_5*Z_5 growth-series singularity, geowa/wa state counts]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25-infinite-witness, topic/uniformity, status/replicated, proof]
---

# Limit diagnostics — evidence gate

**Gate: ACCEPT as #status/replicated, scope "EVIDENCE ONLY, no limit theorem, pre-gpaxioms."** The method
is sound and the anchor checks out; the interpretation labels are honest and I reinforce the mandatory
guards below. **Nothing here proves B(2,5) infinite; Kourovka 11.48 remains open.**

## (1) Collatz-Wielandt growth brackets — METHOD SOUND; VALUES are pre-gpaxioms proxies
- **Method sound.** Row-quotient min/max on the dead-state-cored digraph is the Collatz-Wielandt bracket
  for the Perron root (spectral radius = language growth rate): for a nonnegative (irreducible) matrix and
  any positive x, `min_i (Ax)_i/x_i ≤ λ ≤ max_i (Ax)_i/x_i`. Outward float rounding (min DOWN, max UP)
  makes it a **rigorous enclosure**. I validated the method on a known example (tridiag, ρ=2+√2): the
  bracket encloses ρ. ✓
- **Anchor λ_1 = 1+√3 — VERIFIED independently.** G_1 = F_2/⟨⟨a^5,b^5⟩⟩ = Z_5 * Z_5. Its word-acceptor
  growth series has syllable polynomial s(x)=2x+2x² (nontrivial Z_5 elements a,a⁴ at gen-length 1; a²,a³
  at length 2); dominant singularity at s(x)=1 ⇒ 2x²+2x−1=0 ⇒ x=(√3−1)/2 ⇒ **λ=1/x=1+√3=2.732050807569**,
  matching to 1e-12. This closed form self-validates the CW pipeline at L=1.
- **λ_2..4 (2.6742, 2.6512, 2.6477) declining and flattening, all ≫1:** consistent (adding relators
  reduces growth); bracket widths ~1e-12 = validly converged. Accepted as **FSA-level values**.
- **CRUCIAL interpretation guard (I derived it):** these are growth rates of the g_L.wa word acceptors,
  **pre-gpaxioms** (the automatic-structure axioms are NOT yet verified), so λ_L is a growth rate of an
  **unverified** automaton — a proxy for the true G_L growth, not certified. More importantly, **B(2,5) is
  a FURTHER quotient of every G_L** (it adds all remaining fifth-power relators), so growth(B(2,5)) ≤ λ_L:
  **λ_L is a DECREASING UPPER BOUND on B(2,5)'s growth.** A flattening λ_L > 1 therefore **does NOT prove
  B(2,5) infinite** — an upper bound staying positive is not a lower bound, and "each rung G_L is infinite"
  ≠ "the limit B(2,5) is infinite." The trajectory is suggestive (rungs grow exponentially, growth not
  collapsing to 1 over L=1..4) but is strictly **evidence**.

## (2) E7 witness trajectory |NF_{G_L}(E7)| = 128 — corroborative evidence, not a theorem
Stable 128 at L=1,2,3 (G_4 preview 128, pre-gpaxioms): E7's normal form does not shorten as relators are
added — it **survives with constant length**. This **corroborates** the proven E7 ≠ 1 in G_4 and is
evidence that E7 continues to survive up the ladder (its NF is not collapsing). It is NOT a proof of
survival to the limit. Accept as evidence.

## (3) Fuel-gauge protocol + rung labeling — OK
Counts + rung labels correct; the pre-gpaxioms / "preview" labels on the G_4 row are appropriate and must
be kept. No math claim to certify here beyond honest labeling.

## Bookkeeping correction — CONFIRMED (and my earlier citation was already correct)
**g3.geowa (geodesic acceptor) = 2757 states; g3.wa (word/shortlex acceptor) = 2527 states** — I confirmed
both directly. Delta's correction is right: the growth-rate work uses g3.wa (2527), not the geodesic
2757. Note for the audit trail: my earlier 2757 citation was for **g3.geowa in the axis-pumping cert**
(the geodesic acceptor — correct usage there); it was never claimed as g3.wa. So the corrective line is a
clarification, not a fix to prior verified work.

## Verdict
- CW-bracket method: **SOUND** (validated + anchor λ_1=1+√3 independently derived).
- λ_1..4 and E7 |NF|=128: **#status/replicated as EVIDENCE**, scope **"pre-gpaxioms, no limit theorem."**
- **Mandatory guards for any report:** (a) λ_L are pre-gpaxioms proxies; (b) λ_L is a *decreasing upper
  bound* on B(2,5) growth ⇒ flattening λ_L > 1 does NOT imply B(2,5) infinite; (c) E7 |NF| stability is
  corroborative, not a survival theorem. **The proven result stands at one rung (E7 ≠ 1 in G_4);
  Kourovka 11.48 is OPEN.**
- Bookkeeping: geowa 2757 / g3.wa 2527 — corrective line warranted; prior axis-cert usage unaffected.

Verifies: `Infiniteness/data/receipts/limit_diagnostics_*_140032Z`. Extends
[[2026-08-04-b25-filtered-profile-dryrun-gate]].

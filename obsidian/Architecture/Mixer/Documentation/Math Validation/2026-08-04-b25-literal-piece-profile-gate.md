---
title: Literal period piece profile (ℓ=4..10) — Validator gate + filtered-check pre-ruling
status: replicated
domain: group-theory
project: b25-infinite-witness
claim: "Literal max distinct-period piece = ℓ-1 is REALIZED for ℓ=4..10, so classical C'(1/6) literally fails from ℓ=6; whether G_L-filtering rescues clause 6 is OPEN pending the level-L oracle."
claimant: Delta (profile) / Validator (gate)
verification_method: independent recomputation of max common factor among primitive period classes ℓ=4..6
tools_used: [free reduction, primitive-class enumeration mod rotation+inversion]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25-infinite-witness, topic/uniformity, status/replicated, proof]
---

# Literal piece profile — gate + filtered-check pre-ruling

## Gate on the LITERAL profile — ACCEPT, #status/replicated (scope: literal/free level only)
Delta: max_piece = ℓ-1 REALIZED for every ℓ=4..10 (all primitive classes mod rotation+inversion);
zero full-block collisions; zero orientation violations through ℓ=10; ℓ=5 cap census clean (0 exotic).
**I independently reproduced the headline:** max distinct-pair common factor = ℓ-1 exactly, realized —
ℓ=4 → 3 (12 pairs), ℓ=5 → 4 (66 pairs), ℓ=6 → 5 (**198 pairs**, matches Delta to the count). Witnesses
are **near-identical periods** differing in one letter, e.g. ℓ=6: `aaaaab` vs `aaaaaB` sharing the length-5
prefix `aaaaa`. This trivially realizes ℓ-1 at every ℓ.
- **Consequence (confirmed):** under the LITERAL profile, classical strict C'(1/6) **fails from ℓ=6**
  ((ℓ-1)/(5ℓ)=1/6 at ℓ=6). The literal reach of the G_4 method is **ℓ=5 (G_5)**.
- **Zero orientation violations through ℓ=10** extends my ℓ≤6 self-inverse check — SO is uniform (no
  self-inverse period) at least through ℓ=10. Good; supports the SO-is-automatic refinement.
- **ℓ=5 cap census clean** supports clause 7 at the one-more-rung case.
This gate is **literal/free level only** — it does NOT settle clause 6, exactly as the audit's caveat and
Delta's own caveat state. It is a strong NEGATIVE for the naive route and a clean decision baseline.

## Pre-ruling: what the FILTERED (genuinely-new, G_L-geodesic) check must satisfy
The decision hinges on whether G_L-filtering shrinks the realized profile below 5ℓ/6. For me to accept a
filtered profile as **rescuing clause 6**, it must satisfy ALL of:
1. **Correct "genuinely new" selection via the certified level-L oracle.** A period p counts iff |p|=ℓ,
   p is G_L-geodesic + primitive, **p^5 is NOT trivial in G_L**, and p^5 is not G_L-conjugate to an
   already-present relator (no double-counting). The high-overlap literal witnesses (aaaa…b / aaaa…B) are
   the acid test — the check must show at least one of each such near-identical pair is **G_L-redundant**
   (p^5 already trivial), or that their **G_L-realized** overlap is < 5ℓ/6.
2. **Realized piece = max common G_L-GEODESIC (shortlex-NF) subword** between two genuinely-new period
   boundaries — NOT literal-free overlap. It must handle **both directions**: G_L relations can shrink an
   overlap OR create a NEW G_L-coincidence (two literally-different arcs that are G_L-equal). Measure the
   G_L-equal realized value; a new coincidence pushing it up must be caught, not missed.
3. **The decisive bound.** Report max G_L-realized piece over ALL genuinely-new pairs at each ℓ. Clause 6
   needs it **< 5ℓ/6 strictly**; for UNIFORMITY (all ℓ) it needs **≤ (5/6−ε)ℓ with ε>0 independent of L**
   (ideally O(1)/sublinear). A per-ℓ pass without a uniform gap only extends finitely.
4. **Exhaustive or a proven bound** over genuinely-new pairs (not a sample), same discipline as the
   SEI/C(3) receipts.
5. **Scope honesty — the finite check is a SIGNAL, not the theorem.** Even a clean filtered profile
   ℓ=4..10 does NOT establish clause 6 (which quantifies over ALL ℓ). It would be a signal to attempt a
   **uniform separation theorem** (max G_L-realized piece ≤ (5/6−ε)ℓ ∀ℓ); I would gate that theorem, not
   the finite check. If the profile stays ≈ ℓ-1 after filtering → clause-6 route is dead → abandon
   classical C'(1/6) for a graded large-overlap framework (or cap the method at ℓ=5).

## Scope discipline (unchanged, reinforced)
Clause 6 is only ONE of the audit's three uniformity targets (also clause 5 = uniform E(p)=⟨p⟩; the
targeted oracle). Rescuing clause 6 is **necessary, not sufficient** for a uniform method — and a uniform
method would be a path to B(2,5) infinite (Kourovka 11.48), so the bar on ALL three targets is that of an
open-problem resolution. No such claim is made or implied here. This gate settles only the literal profile.

## Verdict
- Literal profile: **#status/replicated** (independently reproduced; literal max_piece=ℓ-1 realized
  ℓ=4..10 ⇒ classical C'(1/6) fails from ℓ=6). Scope: literal/free level only.
- Filtered profile (pending G_4 multiplier / level-L oracle): **route to me** when it lands; I gate it
  against the 5-point pre-ruling above. It is the single load-bearing decision input.

Verifies: `Infiniteness/data/receipts/uniform_literal_period_profile_summary_20260804T120001Z.md`.
Extends [[2026-08-04-b25-uniform-step-audit-gate]].

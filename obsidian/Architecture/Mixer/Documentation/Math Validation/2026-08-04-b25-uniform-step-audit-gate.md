---
title: Uniform-Step Audit — Validator gate (arithmetic, constants table, 9-clause package)
status: replicated
domain: group-theory
project: b25-infinite-witness
claim: "The G4 period-band method is not uniformly iterable via classical C'(1/6): headroom to ℓ=5, hard barrier at ℓ=6 under worst-case piece profile; cancellable-pair contour is genuinely L-uniform."
claimant: Math-expert (uniform-step-audit) / Validator (gate)
verification_method: inequality-chain check; contour-identity generality at ℓ=5,6; self-inverse word census; template-vs-clauses trace
tools_used: [free reduction, abelianization argument, C'(1/6) arithmetic]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25-infinite-witness, topic/uniformity, status/replicated, status/conjectured, proof]
---

# Uniform-Step Audit — Validator gate

Maria-directed methodology phase. Gating Math-expert's `uniform-step-audit-2026-08-04.md`: does the
certified G_4 period-band method generalize to a uniform step E7-survives-G_L ⇒ E7-survives-G_{L+1}?
**Overall: I endorse the audit's honest bottom line — the method is NOT uniformly iterable via classical
C'(1/6); it has headroom to ℓ=5 and a hard barrier at ℓ=6 under the worst-case piece profile.** SCOPE
UNCHANGED: this is a methodology audit; it does NOT claim B(2,5) infinite or resolve Kourovka 11.48.

## (1) Headline arithmetic — VERIFIED CORRECT (#status/replicated; pure inequality proven)
The inequality chain is right. With worst-case distinct-period piece P_ℓ = ℓ−1 and relator length N=5ℓ:
`(ℓ−1)/(5ℓ) < 1/6 ⟺ 6(ℓ−1) < 5ℓ ⟺ ℓ < 6.` Verified per-ℓ: ℓ=4 →0.150, ℓ=5 →0.160 (both <1/6, WORK);
ℓ=6 →1/6 exactly (TIE, fails strict). Greendlinger exposure 5ℓ−3P_ℓ = 2ℓ+3 vs half-relator 2.5ℓ:
strict (>) for ℓ≤5, equal at ℓ=6 (15=15), less for ℓ>6 — the strict Dehn arc dies exactly where C'(1/6)
does. **Framing correct: exactly one more rung of headroom (ℓ=5 = G_5), and ℓ=6 (G_6) needs new math.**
**Load-bearing caveat, correctly flagged by the audit:** ℓ−1 is the LITERAL worst-case overlap among all
free words; the ACTUAL realized piece P_ℓ among genuinely-new G_L-geodesic periods (Delta's ℓ=4..10
profile) may be smaller. So the ℓ<6 cutoff is a **conservative** barrier: the pure inequality is proven,
but "one rung of headroom" as a statement about the method is conditional on P_ℓ ≈ ℓ−1. If Delta's
profile is sublinear / ≤(5/6−ε)ℓ, the reach extends; if ≈ℓ−1, the classical route stops at ℓ=5.

## (2) Constants table — SOUND row by row; cancellable-pair UNIFORM verified
- **Cancellable-pair contour = UNIFORM: VERIFIED period-length-agnostic.** I confirmed the contour ≡ ε
  for an aligned opposite p^5/p^{−5} pair at **ℓ=5 and ℓ=6** (multiple periods, ALL contact lengths
  1..5ℓ−1) — not a ℓ=4 coincidence. It is the formal identity β_{C′}=β_C⁻¹, using only opposite
  orientation + phase alignment; ℓ never enters. The audit's UNIFORM verdict is correct and is genuinely
  the method's best L-independent feature.
- **Distinct-period piece bound = MAIN nonuniform risk (ratio → 1/5):** correct; this is row A / the ℓ=6
  barrier. ✓
- **Annulus B_ann=24 = nonuniform (O(δ_L+ℓ)):** correct — 24 is a G_3 receipt for 5 periods, not
  universal. ✓ **E(p)=⟨p⟩, all-powers-geodesic, cap census, oracle, period count** all correctly marked
  nonuniform / inductive-hypothesis / needs-theorem. ✓
- **Refinement (a strengthening the audit under-claims): orientation SO is uniform automatically at the
  relevant rungs.** A same-oriented long contact needs p ~cyc p⁻¹; that requires zero abelianization
  (ab(p)=−ab(p)), and I verified there are **zero** cyclically-self-inverse reduced words at ℓ=4,5,6. So
  literal SO holds with no extra hypothesis for every rung the method can reach (ℓ≤5). Finding B's
  "uniform for periods chosen mod inverse" is slightly imprecise (mod-inverse dedups but does not exclude
  a self-inverse class); the clean statement is "no self-inverse period, automatic for ℓ≤5."

## (3) 9-clause package + proof template — template SOUND given the clauses (#status/conjectured)
The proof template (lines 326–332) **faithfully mirrors the certified G_4 proof** with constants
abstracted (η for the piece ratio, E(p)=⟨p⟩ as hypothesis): annuli by (5) → phase-absorb by (7)+(5) →
aligned pockets cancel by (8) → BR2 internal → pieces ≤ηℓ<5ℓ/6 → Greendlinger strict arc → contradict
(9). **Given clauses (1)–(9), the template is sound.** Completeness notes (none load-bearing):
- **Add an explicit "no new period is cyclically self-inverse" clause** for literal SO. Clause 3's "mod
  inverse" handles CROSS-pairs, not self-inverse. It is automatic for ℓ≤5 (per (2)); state it (ideally
  with the abelianization observation) so the template is self-contained.
- **Clause 8 (aligned cancellation) is a proven uniform THEOREM, not a hypothesis** — relabel it as a
  standing lemma, not an inductive assumption.
- **Boundary-preservation** of cancellation + BR2 (needed for the strict-arc transfer, clause 9) is
  implicit; state it as a property of the moves.
- **BR2 (template step 4) is partly redundant** given clause-8 cancellation (as at G_4) — harmless.
The template's genuine burden is exactly the audit's **three uniformity targets**: clause 6 (uniform
piece separation P_ℓ ≤ ηℓ — the ℓ=6 barrier), clause 5 (uniform E(p)=⟨p⟩ / elementary axes), clause 2/7
(targeted oracle). These are correctly identified as the open mathematics. No redundant clause beyond (8)'s
theorem-status; no missing LOAD-BEARING clause (only the minor self-inverse statement).

## (4) Status tags — AGREE, with refinement
- **Arithmetic facts: #status/replicated** ✓ (I confirm). Sharper: the pure inequality (ℓ<6) and the
  contour-identity uniformity are **#status/proven** (trivial/general); the "one-rung-headroom, ℓ=6
  barrier" as a *method* statement is **replicated-conditional** on Delta's actual piece profile.
- **Inductive package (9 clauses + template): #status/conjectured** ✓ — sound-given-clauses, gated on the
  three uniformity targets + the minor self-inverse statement.

## Scope discipline (reinforced)
Even the strongest survivable induction here does **not** reach B(2,5) infinite via classical C'(1/6):
the ℓ=6 barrier is hard under the worst-case profile. The method extends **at most to ℓ=5 (G_5)** unless
(a) Delta's profile is sublinear, or (b) C'(1/6) is replaced by a graded large-overlap cancellation
theory. "Uniform skeleton" ≠ "B(2,5) infinite." Kourovka 11.48 remains OPEN. The audit says exactly this;
I endorse it.

## Verdict
- (1) arithmetic — CORRECT (replicated; pure inequality proven; framing conditional on Delta's profile).
- (2) constants table — SOUND; cancellable-pair UNIFORM verified at ℓ=5,6; SO uniform automatic for ℓ≤5.
- (3) 9-clause template — SOUND given clauses (conjectured); add the self-inverse statement, relabel
  clause 8 as theorem; real burden = the 3 uniformity targets.
- (4) tags — agree (#status/replicated arithmetic, #status/conjectured package).
**The single load-bearing next input is Delta's genuinely-new-period piece profile ℓ=4..10** — it decides
whether to chase clause-6 (a uniform separation theorem, method reaches ℓ=5 and pushes on) or abandon
classical C'(1/6) for a stronger graded-overlap framework.

Verifies: `Experiments/.../methodology/uniform-step-audit-2026-08-04.md`. Builds on
[[2026-08-03-b25-gate2-FINAL-RULING-E7-survives-G4]].

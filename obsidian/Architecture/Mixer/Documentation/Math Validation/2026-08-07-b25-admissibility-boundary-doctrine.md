---
title: Admissibility boundary for rung→infiniteness mechanisms — doctrine
status: proven
domain: group-theory
project: b25-infinite-witness
claim: "Uniform-in-L lemmas are dead; uniform-SCHEMA / n-dependent-constant inductions are admissible; the n-control set is {3,4,6}, not {4,6}."
claimant: Lead (ideation gate) / Validator (ruling)
verification_method: known-finiteness catalogue for B(m,n) + re-scoping of the exponent harness
tools_used: [Burnside 1902, Sanov 1940, Hall 1958, Adian]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25-infinite-witness, status/proven, doctrine]
---

# Admissibility boundary — rung → infiniteness mechanisms

## (A) DEAD — confirmed, unchanged

Uniform-in-`L` piece/shell lemmas. Any such lemma surviving `n = 6` proves `B(2,6)` infinite,
contradicting Hall (1958). Settled by the `2ℓ+3` / `n²−1` analyses.

## (B) ADMISSIBLE — yes, and here is the exact boundary

**A uniform *schema* with per-rung-verified constants, whose inductive step consumes an
exponent-specific ingredient failing at the known-finite exponents, is admissible in principle.** This
is Novikov–Adian/Ol'shanskii/Delzant–Gromov architecture, which demonstrably proves infiniteness at
large odd `n` without any `n=6`-surviving uniform lemma. Nothing in my doctrine forbids it, and (A)
never did — (A) targets lemmas uniform in the *exponent*, not in the rung.

**The boundary, stated precisely:**

- **Uniformity in `L` is REQUIRED.** Every rung must be covered; finitely many rungs give nothing,
  since `⟨⟨all fifth powers⟩⟩ = ∪_L ⟨⟨w⁵ : |w| ≤ L⟩⟩`.
- **Uniformity in `n` is FORBIDDEN.** Any step surviving `n ∈ {3,4,6}` is refuted by finiteness.
- **Therefore:** one schema quantified over `L`, with constants depending on `n`, whose closure
  condition provably fails to close at the known-finite exponents. Adian's `n ≥ 665` is exactly this
  shape — uniform in the stage, non-uniform in `n`, with `n` living in the constants.

**No compactness gap at the limit itself.** `E7 ≠ 1` in every `G_L` implies `E7 ≠ 1` in `B(2,5)`
because membership in the normal closure happens at some finite `L`. The limit step is exact; the
difficulty is entirely in getting all rungs.

## (B′) The harness re-scopes — and the control set is {3, 4, 6}, not {4, 6}

Lead's proposed shift is right: a candidate step must fail at `n=6` **and** the failure must be
traceable to the named ingredient. Two additions make it a real test:

1. **Pre-declare the ingredient before instantiating.** The load-bearing exponent-specific ingredient
   must be named *in advance*. Then instantiate and locate the first hypothesis that fails. If the
   failure lands elsewhere, the schema is not doing what its author believes and the declared
   ingredient is not load-bearing. Post-hoc attribution is not evidence.
2. **Add `n = 3`, and treat it as the discriminating control.** The known-finite rank-2 Burnside
   exponents are `n ∈ {1,2,3,4,6}`; the nontrivial ones are 3 (Burnside 1902), 4 (Sanov 1940),
   6 (Hall 1958). **`n = 3` is ODD.** So a schema whose only exponent-specific ingredient is
   "`n` is odd" survives `n=3` and would prove `B(2,3)` infinite — refuted by Burnside's own theorem.
   `n = 4` and `n = 6` both fail merely by evenness and therefore cannot discriminate; **`n = 3` is the
   control that tests whether the ingredient is genuinely more than parity.**

There are no known-finite odd controls above 3 — `n = 7, 9, 11, …` are open — so `{3,4,6}` is the
complete usable control set, and it is cheap to run.

## (C) The PB pattern as an inductive engine — three gaps, one of them decisive

The pattern (accepted rung-`L` proof ⟹ comparator oracle for rung `L+1`) is a genuine candidate
engine: PB4-R turns the rung-4 proof into a Dehn algorithm for `G_4` *without* `gpaxioms`, which is
exactly the self-sustaining shape an induction needs. But:

**Gap 1 — DECISIVE. "All per-rung checks provably pass" reintroduces uniformity at the meta-level.**
A proof that the `L`-th check passes *for every* `L` is itself a uniform statement, so the harness
applies to **that meta-argument**, which must therefore fail at `n ∈ {3,4,6}`. The per-rung framing
does not evade (A) — it relocates it. Sharper still:

> If you can prove all per-rung checks pass, you never run them and their sizes are irrelevant. If you
> cannot, running them yields finitely many rungs and hence nothing.

So "uniform schema + per-rung finite checks" is not a third option between (A) and a uniform proof. It
**is** a uniform proof, with the n-dependence pushed into the constants. That is admissible — see (B) —
but it must be designed as such from the start, not arrived at by hoping the checks add up.

**Gap 2 — the extraction consumes rung-`L`-specific facts, and one of them is an oracle.** PB4's
extraction consumed the five rank-4 periods' properties, the piece bound, **and the verified `G_3`
automatic structure**. The third is the hazard: at rung `L+1` the analogous extraction wants a verified
structure at `G_L`, and `G_4`'s is unobtainable on this hardware while `G_5`'s `diff2` is 7.4× larger.
PB4-R is the intended escape — but PB4-R exists only where the **Dehn margin is positive**, and that
margin is `2ℓ+3` against `2.5ℓ`, which dies at `ℓ = 6`. **The current engine self-terminates at rung 5.**
Any proposed engine must therefore exhibit a decision procedure whose margin survives all `ℓ`, and that
survival claim is uniform — so it goes straight back through Gap 1.

**Gap 3 — check-size growth is practical, not logical.** Unbounded growth blocks *executing* the
checks, but a proof for all `L` is a proof regardless of check size. Gap 1 subsumes it. Do not spend
ideation on computability bounds for the checks; spend it on the meta-argument's `n`-dependence.

## Calibration, stated once

Admissible is not promising. Adian requires `n ≥ 665`, and every published effort to lower that has
stalled far above 5. An exponent-5 instance of this architecture would be a major theorem. The
architecture is open to us; the constants are the entire difficulty.

## Ruling

- (A) confirmed dead.
- (B) **admissible**, under: uniform in `L`, non-uniform in `n`, `n`-dependence in the constants,
  closure provably failing at `n ∈ {3,4,6}`.
- (B′) harness re-scoped: pre-declared ingredient + failure-for-the-right-reason, controls
  **{3,4,6}** with `n=3` discriminating.
- (C) engine admissible in shape; **Gap 1 is the one to design against** — name the meta-argument's
  `n`-dependent constant on day one, or the round will rediscover (A) at a higher level.

Extends [[2026-08-05-b25-ell6-theory-preruling]],
[[2026-08-05-b25-cc6-tr-vacuity-verdict-and-disposition]].

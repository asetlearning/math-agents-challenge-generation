---
title: "Proxy Validation v4 — Pre-Registration Draft (B(3,3) Lab, Arms 1+3)"
date: 2026-06-26
domain: group-theory
project: b25
experiment_type: proxy-validation
instance: B(3,3) → B(2,5)
author: maumayma
status: pending-approval
supersedes: "[[methodology/b33-gg-proxy-validation-v3-2026-06-19]]"
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/patternboost, topic/proxy-validation, project/b25, status/pending, methodology, experiment]
---

# Proxy Validation v4 — Pre-Registration Draft

**Status**: PENDING — awaiting Maria's GATE C GO. DO NOT RUN until GO.

**Context**: This resumes the proxy validation track that was abandoned after the v3 pilot (2026-06-19). The pilot showed Q2/Q3/Q4 quotients of B(2,5) all collapse on benchmark words (all in γ₅). The B(3,3) lab was never run. This v4 pre-reg scopes the minimal viable next experiment: run B(3,3) lab for Arms 1 and 3 only (no quotient tables needed), with full per-stratum reporting.

See [[methodology/proxy-validation-stalled-state-review-2026-06-26]] for the complete stalled-state inventory and why this is the right next step.

**Supersedes**: v3 pre-reg [[methodology/b33-gg-proxy-validation-v3-2026-06-19]] (structural GATE cleared; Arm 2/C2 quotient path deferred to Stage 2 pending Q5 feasibility; Arms 1 and 3 are the primary unknowns).

---

## §1 Scope

**This pre-reg covers Stage 1 only**: run the B(3,3) lab for Arms 0, 1, and 3. Arm 2 (quotient ensemble) is DEFERRED — the v3 pilot showed Q2/Q3/Q4 are infeasible on B(2,5) benchmark words, and the B(3,3) version requires a pre-reg amendment to specify B(3,3) quotients. That amendment is Stage 2, gated on Stage 1 results.

**What is NOT in scope** (deferred, not abandoned):
- Arm 2 (quotient ensemble) — Stage 2
- Q5 feasibility check — to be routed to Validator in parallel
- Arms 1/3 on 100-2000 char B(2,5) words — Stage 2
- Any new proxy design beyond the four v3 arms — filed separately after Stage 1

---

## §2 Research Question

Do the METRIC-FLAVORED proxy approaches — periodicity-excess (Arm 1) and bounded-descent (Arm 3) — provide Spearman ρ ≥ threshold on the B(3,3) [G,G] stratum (stratum III, all 80 non-identity [G,G] elements), where exact Cayley-BFS ground truth is available?

The v2 result showed that ALGEBRAIC-LABEL proxies (abelianization, LCS-weight-2) fail on [G,G]. The v3 design hypothesis was that METRIC-FLAVORED proxies (geodesic distance in quotients, bounded move search) might escape the blind spot. Arms 1 and 3 are the metric-flavored components that can be evaluated without quotient tables.

---

## §3 Lab — B(3,3)

Identical to v2 and v3 pre-regs. Reuse v2 corpus and GT.

| Property | Value |
|---|---|
| Group | B(3,3) = free Burnside on 3 generators {a,b,c} of exponent 3 |
| Order | 3^7 = 2187 |
| Nilpotency class | 3 |
| Lower central series | γ₁=G (2187), γ₂=[G,G] (81), γ₃ (3), γ₄={1} |
| Ground truth | Cayley-BFS geodesic distance from v2 (b33_metadata.txt) |

**Artifact verification (MANDATORY before any run)**:
- `b33_metadata.txt` sha256: `0c4b4e11...` — verify before use; if mismatch, regenerate with seed 20260617, record new sha256.
- `kbmag/b33.kbprog` sha256: `a81167ff...`, confluent, 1974 rules — verify `#System is confluent.` in log.

---

## §4 Corpus

Reuse v2 corpus exactly where sha256 match is confirmed. If mismatch, regenerate per v2 protocol.

| Stratum | Description | N |
|---------|-------------|---|
| I | Relators of B(3,3) (d=0) | ≥50 (v2: 258) |
| II | Random non-identity words | ≥200 (v2: 500; seed 20260617) |
| III | [G,G] \ {1} census | **ALL 80** (v2: 80; complete census, no sampling) |
| **Total** | | ≥330 (v2: 838) |

**Stratum III is mandatory complete census** (all 80 non-identity [G,G] elements). Do not sample, do not merge into stratum II. Report stratum III results separately.

**Corpus seed**: 20260617. If any stratum II words newly generated, record all seeds; n_seeds ≥ 5.

---

## §5 Arms

Only Arms 0, 1, 3 are in scope for Stage 1.

### Arm 0 — Option B baseline (reuse v2 data)

- Score: `(L − L') / L` where L' = length after one-pass greedy braid+power reduction using the B(3,3) confluent KB (1974 rules, sha256 `a81167ff`).
- **Provenance reuse check**: If v2 corpus sha256 matches, reuse v2 Arm 0 column directly. If regenerating corpus, re-run Arm 0.
- Role: baseline. Expected blind on stratum III (v2 confirmed: ρ=NaN, blind-spot fraction 1.000).

### Arm 1 — Periodicity-excess (contiguous, K=8)

**Definition**: For a word w over {a,b,c,A,B,C}:
1. Scan all contiguous substrings of w of the form `u^k` where `|u| ≤ K=8` and `k ≥ 2`.
2. For each match: let n=3 (exponent of B(3,3)). Compute `excess = |u| · (k mod n)`. This is the expected length reduction if `u^n → ε` is applied as many times as possible.
3. `arm1_score(w) = Σ excess / L`.

**Parameter**: Primary K=8. Secondary: K ∈ {4, 12} (parameter sweep, report all three).

**Implementation note**: scan left-to-right, non-overlapping. Deterministic — single run sufficient.

**No conjugation** (c·u^k·c⁻¹ detection excluded — exponential cost confirmed in v3 pre-reg Validator advice).

**Role**: control arm. Prior expectation: ρ ≈ Arm 0 on stratum III (periodicity scan is the same detection mechanism as braid+power, just restricted to exact power substrings). If Arm 1 shows ρ > 0.20 on stratum III it is a positive surprise; promote from control to secondary candidate.

### Arm 3 — Bounded-descent (C3 features only)

**Definition**: Given a word w over {a,b,c,A,B,C} and a state budget T:

Move set (identical to v3 pre-reg):
- Free reduction (remove adjacent inverse pairs: `xX → ε`, `Xx → ε`)
- Period moves: for all u with |u| ≤ 4, replace any occurrence of `u^n` (n=3 for B(3,3)) with ε
- Conjugate-radius-3: for all words v with |v| ≤ 3, replace any occurrence of `v·u^n·v^{-1}` with ε (where u^n is a period of the inner word)

Search strategy: BFS/greedy from w; at each step apply all available moves and take the first length-reducing one; if no move reduces, expand to next BFS frontier (up to T expansions).

**C3 features** (computed per word):

| Feature | Definition |
|---------|------------|
| `first_descent_depth` | Moves to first length reduction; `∞` if no descent in T moves |
| `move_count_to_descent` | Total moves explored before first descent |
| `total_shrink_T16` | `(L − min_len_reached) / L` at T=16 |
| `total_shrink_T64` | `(L − min_len_reached) / L` at T=64 |

**Primary scored metric**: `total_shrink_T16`. Secondary: `total_shrink_T64`.

**Role**: primary alternative arm. Hypothesis: bounded search descending toward identity will give gradient on [G,G] because geodesic distance measures how many steps are needed to reach identity — and bounded descent is a proxy for that step count.

**Determinism**: Arm 3 is deterministic given fixed T and move-set application order. Single run sufficient.

---

## §6 Hypotheses and Decision Criteria

**H4-0** (control): Arm 1 Spearman ρ on stratum III ≈ Arm 0. Falsification threshold: ρ > 0.20 on stratum III — would be a positive surprise; promote Arm 1 from control to secondary candidate.

**H4-1** (primary, Arm 3): `total_shrink_T16` Spearman ρ on stratum III ≥ **0.20** (half the full-proxy threshold from v3). Rationale for lowered threshold: we are testing a proxy COMPONENT (C3 features alone, without C2 quotient distances); 0.20 is a meaningful positive signal, not a full transfer threshold. Full transfer would require ρ ≥ 0.40 in the complete proxy, which combines Arm 2 + Arm 3.

**H4-2** (secondary): Any arm achieves ρ > 0 (non-negligible) on stratum III AND blind-spot fraction < 1.00 on stratum III.

---

## §7 Analysis Plan

### Per-stratum reporting (mandatory)

Report Spearman ρ and Pearson r for each arm separately for:
1. Stratum III ([G,G], all 80) — **PRIMARY DECISION BASIS**
2. Stratum II (random non-identity) — secondary signal
3. Full corpus — summary only; not decision basis

**Never report only full-corpus ρ.** v2 lesson: Proxy D had ρ=0.697 full-corpus, ρ=0.079 on stratum III. Full-corpus numbers are dominated by strata I/II separation.

### Blind-spot fractions

For each arm: fraction of non-identity words scoring 0 in each stratum. Arm 0 = 1.000 on stratum III (v2 confirmed). Any reduction of stratum III blind-spot below 1.000 is positive.

### Steiger's Z (pairwise arm comparison)

Pairwise comparison on stratum II + III combined (y>0 slice), same protocol as v2. Compare Arm 3 vs. Arm 0 as primary comparison.

### Arm 1 parameter sweep

Report ρ on stratum III for K ∈ {4, 8, 12}. Primary hypothesis uses K=8.

### Arm 3 T parameter

Report ρ for T=16 (primary) and T=64 (secondary) on stratum III. If T=64 gives substantially higher ρ than T=16, note T-sensitivity.

---

## §8 Transfer Rules (locked pre-results)

**If H4-1 supported (Arm 3 ρ ≥ 0.20 on stratum III)**:
- Route Q5 feasibility to Validator (file: "Can Q5=B(2,5)/γ₆ be built as PcGroup? Can geodesic distance be estimated without BFS for order ~5^14?")
- Pre-reg Stage 2: Arm 3 evaluation on B(2,5) words of length 100–2000 chars (requires word corpus construction in that range).
- Pre-reg Stage 2: Arm 2 with B(3,3)-appropriate quotients (B(3,3)/γ₂, B(3,3)/γ₃).
- Do NOT transfer to PatternBoost until Stage 2 results in hand.

**If H4-0 surprised (Arm 1 ρ > 0.20 on stratum III)**:
- Promote Arm 1 from control to secondary candidate. Flag to Lead.
- Pre-reg Stage 2: Arm 1 on B(2,5) words in 100–2000 char range.

**If all arms fail stratum III (ρ ≤ 0 or blind-spot = 1.000 for Arms 1 and 3)**:
- File open-problem note to Researcher: "No metric-flavored proxy (periodicity scan, bounded descent) gives [G,G] gradient in B(3,3) lab. Structural approaches tested: v2 (LCS-weight-2), v3+v4 (Arms 1, 3). The [G,G] blind class is structurally hard. New invariant needed."
- Do NOT formally close the track without Maria's review of the open-problem note.
- Keep Option B for PatternBoost.
- Stage 2 (Arm 2 with B(3,3) quotients) remains deferred — route to Lead for decision.

**Foreground in all transfer reports**: B(3,3) lab passage is structural-generality evidence, NOT proof of B(2,5) performance. B(3,3): rank 3, exponent 3. B(2,5): rank 2, exponent 5. Any transfer claim must state this explicitly.

---

## §9 Anti-Pattern Checklist

- [ ] GT independent of arm computation? **YES** — Cayley-BFS is over B(3,3), completely separate from KB reduction (Arm 0) and bounded search (Arm 3). No shared artifact.
- [ ] Stratum III explicitly separated, not merged? **YES** — required by this pre-reg and enforced in analysis.
- [ ] Arm 1 conjugation excluded? **YES** — exponential cost; not implemented.
- [ ] No metric claim on Arm 3 features? **Arm 3 features are NOT a lower bound** — they are heuristic descent scores. Primary score is `max_i d_i` (Arm 2, deferred); Arm 3 features are for correlation study.
- [ ] v2 corpus sha256 verified before reuse? **YES — mandatory before any run**.
- [ ] Seeds ≥5? **YES** — Arms 1 and 3 are deterministic. If regenerating corpus, n_seeds ≥ 5.
- [ ] Execution gated on GO? **YES — DO NOT RUN before Maria's GATE C.**
- [ ] Untested items in other stages explicitly listed? **YES** — see §§ 'Not in scope' and stalled-state review.

---

## §10 Known Limitations

1. **Stratum III limited power**: 80 elements, 4 distinct distance values (d=4,6,7,10), 64/80 at d=6. Threshold 0.20 is practical, not statistically powered.
2. **B(3,3) lab ≠ B(2,5)**: passage here is structural-generality evidence only. Explicit statement required in any transfer report.
3. **Arm 3 move-set overlap with Arm 0**: at T=1, Arm 3 reduces to the same mechanism as Arm 0. Multi-step search is the distinguishing feature. If Arm 3 fails, T=16 may be too small — not necessarily that the approach is wrong.
4. **Arm 1 and 3 for B(3,3) corpus words**: B(3,3) [G,G] elements have geodesic distance ≤ 10 and length ≤ ~30 chars. Arm 3 bounded search (T=16) may exhaust the group element space for these short words — the descent may terminate at identity, giving `total_shrink = 1.000` for ALL words. If so, total_shrink has no gradient. Watch for this; if it occurs, use `first_descent_depth` as primary feature instead.

---

## §11 Provenance Template (fill at run time)

| Field | Value |
|---|---|
| Git SHA (algo_mixing HEAD) | [fill at run time] |
| b33_metadata.txt sha256 | [verify against `0c4b4e11`; fill actual] |
| b33.kbprog sha256 | [verify against `a81167ff`; fill actual] |
| Corpus (v2 reuse or regenerated) | [note which; fill sha256 if regenerated] |
| Script path | `experiments/burnside/b25/proxy_validation_v3/b33_lab_v4.py` [to be created] |
| Run output path | `runs/b25/proxy_validation_v4/<ISO-timestamp>/` |

---

## §12 Open Routings (parallel to Stage 1, do not block on these)

1. **Q5 feasibility → Validator**: "Can Q5 = B(2,5)/γ₆ (order ~5^14 = 6.1 billion) be built as a PcGroup? Can geodesic distance from identity be estimated WITHOUT a full BFS table (e.g., via pcgs weight-5 component norms)? What would be needed to make Q5 a practical proxy quotient?" Route via maestri after GO.

2. **Literature question → Researcher**: "Are there known proxy invariants for geodesic distance within the commutator subgroup of a finite p-group? Specifically for free Burnside groups: is there any invariant that gives gradient on [G,G] that is cheaper to compute than full Cayley-BFS?" Route via maestri after GO.

---

## §13 Gates

| Gate | Status | Action if blocked |
|------|--------|-------------------|
| Structural soundness (Q2/Q3/Q4 sizes, lower bound) | CLEARED 2026-06-19 | — (not relevant for Stage 1 which has no quotients) |
| Corpus artifact verification (b33_metadata.txt sha256) | MUST verify before run | If mismatch: regenerate per v2 protocol |
| GATE C — Maria GO for B(3,3) lab Stage 1 | **PENDING** | DO NOT RUN until GO |
| GATE D — Lead review of Stage 1 results | Follows Stage 1 | Transfer decision per §8 |

**DO NOT RUN until GATE C is issued.**

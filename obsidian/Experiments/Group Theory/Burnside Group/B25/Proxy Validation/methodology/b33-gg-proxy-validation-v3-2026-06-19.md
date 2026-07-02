---
title: "B(3,3) [G,G]-Gradient Proxy Validation v3 — Pre-Registration (Pilot + Lab)"
date: 2026-06-19
domain: group-theory
project: b25
experiment_type: proxy-validation
instance: B(3,3) → B(2,5)
author: maumayma
status: pending-approval
supersedes: "[[methodology/b33-proxy-validation-v2-2026-06-17]]"
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/patternboost, topic/proxy-validation, project/b25, status/pending, methodology, experiment]
---

# B(3,3) [G,G]-Gradient Proxy Validation v3 — Pre-Registration

**Status**: PENDING — GATE A (human GO for pilot) not yet issued. DO NOT RUN until GATE A is given.

**Amendment log**:
- 2026-06-19: Filed by B25 Experimenter. Builds on v2 (LCS-weight-2 falsified; [G,G] blind-class problem remains open). New candidates: finite-quotient Cayley-distance ensemble (C2) + bounded-descent auxiliary features (C3).
- 2026-06-19: Validator structural gate CLEARED (quotient soundness, sizes proven exact, max_i d_i lower-bound property — quoted in §4).

**Supersedes**: [[methodology/b33-proxy-validation-v2-2026-06-17]] (v2 ran 2026-06-18: H1 NOT SUPPORTED, H2 NOT SUPPORTED; LCS-weight-2 proxy gives ρ=0.079 on γ₂\γ₃, threshold 0.40; keep Option B; new design required)

---

## §1 Motivation

PatternBoost for B(2,5) needs a CHEAP per-candidate score proxy for "distance to identity." Current proxy (Option B: one-pass braid+power reduction_ratio) is blind on ~43% of B(2,5) words — those in the commutator subgroup [G,G], e.g. `(aba)^5`. Both abelianization and LCS-weight-2 are also blind on [G,G] (abelianization = 0 by definition on [G,G]; LCS-weight-2 gives ρ=0.079 on [G,G] in v2, far below threshold).

**v3 candidates**: finite-quotient Cayley-distance ensemble (C2) and bounded-descent auxiliary features (C3). C2 looks up the image φ_i(w) in a finite nonabelian quotient Q_i and reads off exact geodesic distance d_i from a precomputed BFS table. C3 measures how fast bounded-move-set search descends from w. Both are metric-flavored, not algebraic-label-based (the lesson from v2).

**B(3,3) lab**: finite group with exact Cayley-BFS ground truth; 80 non-identity [G,G] elements spanning d=4..10 (confirmed in v2). All four proxy arms are tested on the same stratified corpus with [G,G] stratum explicit. The question is whether any arm gives Spearman ρ ≥ 0.40 on that stratum.

---

## §2 Lab: B(3,3)

| Property | Value |
|---|---|
| Generators | a, b, c (rank 3) |
| Exponent | 3 |
| Order | 3⁷ = 2187 (confirmed v2 spike 2026-06-17) |
| Nilpotency class | 3 (Hall 1933) |
| Lower central series | γ₁=G (2187), γ₂=[G,G] (81), γ₃ (3), γ₄={1} |
| Word problem | Decidable; GAP/kbprog confluent (1974 rules, sha256: `a81167ff`, verified v2) |

**Ground truth**: Cayley-BFS geodesic distance from v2 (b33_metadata.txt, sha256: `0c4b4e11`). Reuse is conditional — sha256 must be verified at run time before reuse. If mismatch: regenerate with seed 20260617, record new sha256.

---

## §3 Arm Definitions

Four arms. All run on the same stratified B(3,3) corpus.

**Arm 0 — Option B baseline** (one-pass braid+power reduction_ratio):
- Score: `(L − L') / L` where L' = length after one-pass greedy braid+power reduction.
- Data source: v2 run results (`b33-proxy-results-v2-2026-06-18.md`), proxy A column.
- **Provenance reuse check**: before reusing v2 Arm 0 data, verify b33_metadata.txt sha256 matches `0c4b4e11` AND that the corpus used in v2 exactly covers the v3 corpus (stratum III = same 80 elements, stratum II seed = 20260617). If corpus differs, re-run Arm 0.
- Role: baseline. Expected blind on stratum III (v2 confirmed: ρ=NaN, blind-spot fraction 1.000).

**Arm 1 — periodicity-excess** (Candidate 1, contiguous only):
- Score: scan w for exact contiguous substrings matching `u^k` where `|u| ≤ K=8`, k ≥ 2; compute expected_drop = `|u| · (k mod n)` per match; primary score = total_expected_drop / L.
- **NO conjugation** (`c·u^k·c^{-1}` detection dropped — exponential cost per Validator advice).
- Parameter sweep: K ∈ {4, 8, 12}; primary K=8.
- Deterministic — single run sufficient.
- Role: control arm. Expected ρ ≈ Arm 0 on stratum III (same detection mechanism as braid+power).

**Arm 2 — quotient-ensemble composite** (C2 + C3 auxiliary features):
- Primary C2 score: `max_i d_i(e, φ_i(w))` over {Q2, Q3, Q4} — see §4 for quotient definitions and §5 for metric definition.
- C3 auxiliary features: first_descent_depth, move_count_to_descent, total_shrink at T=16 (see §3.1).
- Feature vector exposed to downstream scored: (d_Q2, d_Q3, d_Q4, excess_Q2, excess_Q3, excess_Q4, saturation_Q2, saturation_Q3, saturation_Q4, first_descent_depth, move_count, total_shrink).
- GATE B distortion check required before running in B(3,3) lab — see §6.
- Role: PRIMARY composite arm.

**Arm 3 — bounded-descent ablation** (C3 features only):
- Features: first_descent_depth, move_count_to_descent, total_shrink at T=16 and T=64.
- Move set: free reduction + period^n (|u| ≤ 4) + conjugate-radius-3.
- Primary scored metric: total_shrink at T=16 = (initial_len − min_len_reached) / initial_len.
- Deterministic given fixed T and move-set ordering.
- Role: ablation — tests whether C3 features carry [G,G] signal independently of C2 quotient distances.

### §3.1 C3 feature definitions (shared by Arms 2 and 3)

| Feature | Definition |
|---|---|
| first_descent_depth | Number of moves to first length reduction from L; Infinity if no descent in T moves |
| move_count_to_descent | Total moves explored before first descent (breadth measure) |
| total_shrink | (initial_len − min_len_reached_in_T_moves) / initial_len |
| T | State budget; primary T=16; secondary T=64 (stage-2 only) |

Move set: {free reduction, u^n → e for all words u of length ≤ 4, conjugate-radius-3 rearrangements}. Budget T counts state expansions, not move applications.

---

## §4 Quotient Set + Structural Claims (GATE B structural — CLEARED 2026-06-19)

**Validator structural verdict** (received 2026-06-19; no separate verdict note filed — quoting here):
> "Q2/Q3/Q4 sound WITHOUT GAP. Witt sizes 5^3 (Q2), 5^5 (Q3), 5^8 (Q4) are PROVEN-EXACT (class < p=5, so Witt/Möbius formula has no modular complications). [Q_i, Q_i] is nontrivial for Q2/Q3/Q4 (each Q_i is non-abelian). max_i d_i is a valid lower bound on geodesic distance in B(2,5) (by functoriality of homomorphisms and metric monotonicity). Weighted combination is NOT a lower bound — weights are unconstrained. Q5+ still needs GAP/nq confirmation before tables. Q6+ still Researcher-sourcing."

**Quotient ladder** (Math-expert delivered 2026-06-19):

| ID | Name | Order | [Q,Q] | Diameter | Structural status | Role |
|----|------|-------|--------|----------|------------------|------|
| Q0 | C5×C5 | 5^2 = 25 | trivial (abelian) | ~4 | Confirmed abelian | NEGATIVE CONTROL — must reproduce [G,G] blind spot |
| Q2 | UT_3(F5) / Heisenberg | 5^3 = 125 | nontrivial ✓ | ~7 | PROVEN EXACT (class < p=5) | Pipeline sanity — diameter saturates on all real B(2,5) targets |
| Q3 | Free class-3 nilpotent on {a,b} of exp 5 | 5^5 = 3125 | nontrivial ✓ | ~25 | PROVEN EXACT (class < p=5) | First gradient test — saturates on benchmark words (2500+) but potentially discriminating on 100–500 char candidates |
| Q4 | Free class-4 nilpotent on {a,b} of exp 5 | 5^8 = 390625 | nontrivial ✓ | ~80–200 | PROVEN EXACT (class < p=5) | FIRST serious test — plausibly discriminating on 100–500 char candidates; real distortion trial |
| Q5+ | Class-5+, ~5^14+ | — | — | — | Needs GAP/nq | CONTINGENCY — DO NOT build tables unless Q4 fails distortion |
| Q6+ | — | — | — | — | Researcher sourcing | Do not build |

**Why [Q,Q] nontrivial matters**: Q0's [Q0,Q0]=1 (abelian) means all [G,G] words map to e in Q0 — it cannot distinguish any commutator-subgroup element. Q2/Q3/Q4 have [Q_i,Q_i] ≠ 1, so the image of a non-trivial [G,G] element CAN be non-identity in Q_i. This is the structural precondition for the quotient ensemble to escape the [G,G] blind spot.

**Do-not-build guard**: Q5+ tables not built unless pilot Component 1 shows Q4 saturation fraction > 50% on the 100–500 char candidate pool (GATE B distortion check fails). If Q5+ ever cleared, Q6+ is a separate Researcher task. Do not anticipate either.

---

## §5 Distortion Metric Definition

### §5.1 BFS distance table for quotient Q_i

For each quotient Q_i with generators mapped from B(2,5)'s a, b:
1. Build Q_i explicitly (multiplication table or PcGroup).
2. Run BFS from identity e in the Cayley graph of Q_i with generator set {φ_i(a), φ_i(b), φ_i(a)^{-1}, φ_i(b)^{-1}}.
3. Record `dist_table_i : Q_i → ℤ_≥0` mapping each element to its exact geodesic distance from e.

**Provenance for each table**: store Q_i order, generator images (as permutation/matrix/pcgs elements), BFS script sha256, table artifact sha256.

**BFS feasibility**: Q2 (125 states): trivial, seconds. Q3 (3125 states): <1 second. Q4 (390625 states, 4 moves per state): ~seconds on modern hardware. All three tables built during the pilot before B(3,3) lab runs.

### §5.2 Per-word quotient scores

For a word w over {a, b, A, B}:
1. **Homomorphism evaluation**: compute φ_i(w) ∈ Q_i by left-to-right multiplication of generator images: φ_i(ε) = e; φ_i(a·v) = φ_i(a)·φ_i(v); φ_i(A·v) = φ_i(a)^{-1}·φ_i(v). Cost: O(|w|) group multiplications in Q_i.
2. **Table lookup**: `d_i(w) := dist_table_i[φ_i(w)]`. Cost: O(1).

### §5.3 Derived scores and features

| Quantity | Definition | Role |
|---|---|---|
| `d_i(w)` | `dist_table_i[φ_i(w)]` — exact geodesic distance from e to φ_i(w) in Q_i | Raw quotient distance |
| **`primary_score(w)`** | `max(d_Q2(w), d_Q3(w), d_Q4(w))` | **METRIC CLAIM — valid lower bound on geodesic distance in B(2,5) (Validator confirmed). Use for proxy correlation studies.** |
| `feature_vector(w)` | `(d_Q2, d_Q3, d_Q4)` | Feature vector for learned scoring. Weights may be tuned; no metric claim. |
| `excess_i(w)` | `reduced_len(w) − d_i(w)` | Apparent slack: how much further the word should reduce given Q_i evidence |
| `saturation_i(w)` | `d_i(w) == diam(Q_i)` | Boolean: TRUE means Q_i is too small to distinguish this word from the furthest reachable element — quotient uninformative for this word |
| `saturation_fraction` | fraction of words in pool with saturation_i = TRUE | Population-level distortion measure; used in GATE B distortion check |

**CRITICAL DISTINCTIONS**:
- `primary_score` = `max_i d_i` is a VALID LOWER BOUND on B(2,5) geodesic distance. Do NOT use weighted combinations for metric claims — weighted sums are not lower bounds.
- `feature_vector` is for downstream learned scoring only. Weights unconstrained. No metric claim on any linear combination.
- Q0 (C5×C5) is EXCLUDED from `primary_score` and `feature_vector` — it is abelian, cannot separate [G,G] elements, and is a NEGATIVE CONTROL only (validates that the harness correctly detects collapse).

---

## §6 Pilot Design (pre-lab lock) — TWO COMPONENTS

**Both components gated on GATE A (human GO). DO NOT RUN before authorization.**

Pilot runs BEFORE the B(3,3) lab. Purpose: confirm Q4 is not fully saturated on the actual candidate-pool word-length distribution, and confirm all arms produce non-trivial scores on real B(2,5) targets.

### §6.1 Component 1 — PRIMARY distortion test (candidate-pool distribution)

**Word pool**: sample ≥50 words from the 119-word B(2,5) benchmark set
(`b25-benchmark-snapshot-2026-06-09`) restricted to **original_len ∈ [100, 2000] chars** (the PatternBoost candidate-pool distribution). Sample uniformly by index; do not filter by reduction quality.

**Compute for each word**: d_Q2, d_Q3, d_Q4, saturation_Q2, saturation_Q3, saturation_Q4, plus Arm 1 and Arm 3 scores.

**Gate decision — Arm 2 inclusion (GATE B distortion)**:

| Condition | Decision |
|---|---|
| Q4 saturation fraction ≤ 50% on 100–500 char sub-pool | Q4 is genuinely discriminating; proceed to B(3,3) lab WITH Arm 2 |
| Q4 saturation fraction > 50% on full 100–2000 char pool | Q4 too distorted; flag to Lead; hold Arm 2; await Q5 Validator confirmation before proceeding |

**Also report per quotient**:
- Saturation fraction over [100,200], [200,500], [500,2000] char sub-pools (binned)
- Mean d_i and diam(Q_i) for each sub-pool
- At least 10 words in the [100,500] char sub-pool; if benchmark has fewer, note constraint

### §6.2 Component 2 — SECONDARY saturation reference (benchmark words)

Score the two primary B(2,5) target words for all arms:
- `comm_12_9` (word_7245, 7,245 chars): `experiments/b25_reduce_core/corrected/final_beam.txt`
  — sha256 PINNED: `d985a648ac7286b3fa9766507fee0ac5982696ff44c43bda9de4fc5513dbc25c`
- `comm_13_10` (2,500 chars): `experiments/b25_reduce_core/runs/b25-reduce-core-benchmark-0001/data/words/comm_13_10.txt`
  — sha256 PINNED: `1a93a95afd7e3a10f93830f2335a0c1aed34bfd95b815060cf83050235413653`

**Purpose**: document saturation boundary at benchmark word lengths. Expected: Q2 saturated, Q3 saturated, Q4 likely saturated. These scores are NOT the primary gate — they show where the quotients top out.

**Report format per arm per benchmark word**:
- Arm 1: detected periods (u, k, expected_drop) list; total_expected_drop / L
- Arm 2: d_Q2, d_Q3, d_Q4; saturation_i per quotient; primary_score = max(d_Q2, d_Q3, d_Q4)
- Arm 3: first_descent_depth; move_count_to_descent; total_shrink at T=16 and T=64

### §6.3 Pilot provenance triple (to fill at run time)

| Field | Value |
|---|---|
| Git SHA (algo_mixing repo HEAD) | [fill at run time] |
| uv.lock hash (Python env) | sha256: [fill at run time] |
| mixer-core build hash (Rust binary) | sha256: [fill at run time] |
| Pilot script | `experiments/burnside/b25/proxy_validation_v3/pilot_distortion.py` |
| Pilot output path | `runs/b25/proxy_validation_v3/<ISO-timestamp>/pilot/` |

---

## §7 B(3,3) Lab Design

**Ground truth**: same as v2. GAP Cayley-BFS distance table `b33_metadata.txt` (sha256: `0c4b4e11`). Verify sha256 before use; if mismatch, regenerate (see §2).

**kbprog artifact**: `kbmag/b33.kbprog`, confluent `#System is confluent.`, 1974 rules, sha256: `a81167ff`. Required for Arm 0 Arm 1 (used indirectly for B(3,3)-specific KB reduction if needed). If re-running Arm 0, re-verify confluence.

**Corpus (stratified)** — reuse v2 corpus where possible:

| Stratum | Description | N | Source |
|---|---|---|---|
| I | Relators of B(3,3) (d=0) | ≥50 | From B(3,3) kbprog relators |
| II | Random non-identity words | ≥200 | Seed 20260617; filter d>0; abelian coset distribution |
| III | [G,G] \ {1} census | **all 80** | Reuse v2 stratum III corpus (b33_metadata.txt sha256 `0c4b4e11`) |

Stratum III = all 80 non-identity [G,G] elements — complete census, no sampling. Distance distribution: d=4 (6), d=6 (64), d=7 (8), d=10 (2); γ₃ non-identity pair at d=10 (verified v2). Stratum III must be ≥10% of total corpus; DO NOT merge into stratum II.

**Seeds**: corpus seed = 20260617 (reuse for stratum II continuity with v2). If any stratum II words are newly sampled: n_seeds ≥ 5, record all seeds. Arms 1/3 are deterministic — single run. Arm 2 C3 features are deterministic given fixed T and move-set ordering — single run.

---

## §8 Analysis Plan

### §8.1 Per-stratum reporting

Report Spearman ρ and Pearson r for each arm within each stratum separately. NEVER report only full-corpus ρ — v2 lesson: proxy D had ρ=0.697 full-corpus but ρ=0.079 on stratum III; full-corpus numbers are misleading.

| Stratum | Metric | Notes |
|---|---|---|
| Full corpus (all strata) | Pearson r, Spearman ρ | Summary only; not decision basis |
| Stratum II (random non-identity) | Pearson r, Spearman ρ | Secondary signal |
| Stratum III ([G,G], all 80) | **Spearman ρ** | **PRIMARY DECISION BASIS** |

### §8.2 Blind-spot fractions

For each arm per stratum: report fraction of non-identity words scoring 0 (blind-spot fraction). Arm 0 = 1.000 on stratum III (confirmed v2); any improvement here is progress.

### §8.3 Steiger's Z

Pairwise arm comparison on stratum II + III combined (y>0 slice): same protocol as v2.

### §8.4 Saturation analysis for Arm 2

On stratum III (B(3,3) words, max length ~30 chars): Q3 and Q4 are unlikely to saturate (B(3,3) words are short). Report saturation fractions per quotient. If saturation_fraction < 10% on stratum III, no distortion concern for the lab.

---

## §9 Hypotheses + GO/NO-GO Criteria

**H3-0** (control): Arm 1 Spearman ρ on stratum III ≈ Arm 0 (≈0 or NaN). Falsification threshold: ρ > 0.20 — would be a surprise and would promote Arm 1 from control to candidate.

**H3-1** (primary, Arm 2): Spearman ρ(primary_score, d) on stratum III ≥ **0.40**. Falsification: ρ < 0.40 → quotient ensemble + C3 features insufficient; composite fails [G,G] gradient requirement.

**H3-2** (ablation, Arm 3): Spearman ρ(total_shrink_T16, d) on stratum III ≥ **0.20** (half-threshold). Falsification: ρ < 0.20 → C3 features carry no [G,G] signal independently of C2.

**Secondary GO**: any arm achieves ρ ≥ 0.40 on stratum II AND ρ > Arm 0 on stratum III (even if stratum III < 0.40).

**Pilot pass gate** (GATE B distortion, from §6.1):
- **PASS**: Q4 saturation fraction ≤ 50% on 100–500 char sub-pool → Arm 2 proceeds to B(3,3) lab.
- **FAIL**: Q4 saturation fraction > 50% on 100–2000 char full pool → Arm 2 held; report to Lead.

---

## §10 Transfer Rule — LOCKED pre-results

**Arm 2 passes H3-1**: Transfer C2+C3 composite as full-round [G,G]-aware proxy in PatternBoost STEP 1.5 addendum. File to Developer. Note: primary_score = max_i d_i is the metric claim; feature_vector is the scorer input.

**Arm 3 passes H3-2 but Arm 2 fails**: Transfer C3 features as stage-2 booster (apply to top 1–10% survivors from primary Option B scoring). Keep Option B full-round.

**H3-0 surprises (Arm 1 ρ > 0.20 on stratum III)**: Promote Arm 1 from control to secondary candidate; do not transfer yet; flag to Lead for new pre-reg.

**All arms fail stratum III** (H3-1 and H3-2 both not supported): Declare [G,G] proxy problem open at the B(3,3) lab level. Actions:
- Keep Option B for PatternBoost.
- Lower PatternBoost training threshold: exclude words with original_len in range where B(2,5) reduction_ratio = 0 (near-[G,G] zone).
- File open-problem note to Researcher: "structural metric-flavored proxy for [G,G] geodesic distance — C2 and C3 both failed at B(3,3) lab."
- Do not transfer; do not attempt B(2,5) pilot until new design.

**Foreground in all transfer reports** (from v2 lesson): any proxy passing B(3,3) is structural-generality evidence, NOT proof of B(2,5) performance. B(3,3) has rank 3, exponent 3; B(2,5) has rank 2, exponent 5. Explicit statement required in any transfer report.

---

## §11 Anti-Pattern Checklist

- [ ] GT independent of arm proxy computation? **YES** — Cayley-BFS uses exact group multiplication. BFS tables use the same tables. No shared mechanism with KB reduction (Arm 0/1) or bounded search (Arm 3). Q_i BFS tables share structure with GT BFS only in that both do BFS — but over different groups (B(3,3) vs Q_i) — no shared artifact.
- [ ] Stratum III explicitly separated, not merged? **YES** — report per stratum, never pool.
- [ ] Q0 (abelian) excluded from scoring? **YES** — Q0 is negative control only; never enters primary_score or feature_vector.
- [ ] Arm 1 conjugation term absent? **YES** — c·u^k·c^{-1} detection is exponential; not implemented.
- [ ] Weighted combination not used as metric claim? **YES** — primary_score = max_i d_i only. Feature vector may be weighted by downstream scorers with no metric claim.
- [ ] Saturation check on candidate pool done BEFORE B(3,3) lab? **YES** — Component 1 is the pilot gate (§6.1).
- [ ] Q5+ tables not built pre-emptively? **YES** — do-not-build guard; only if Q4 fails distortion.
- [ ] Provenance triple captured at run time? **YES** — see §6.3 and §12.
- [ ] Seeds ≥5 for any stochastic run? **YES** — Arms 1/3 are deterministic; Arm 2 C3 features are deterministic; corpus seed = 20260617.
- [ ] Execution gated on human GO? **YES** — GATE A not yet issued.

---

## §12 Known Limitations

1. **Stratum III limited power**: 80 elements, 4 distinct distance values (d=4,6,7,10), 64/80 at d=6. Spearman ρ on stratum III is exploratory/descriptive. Treat threshold 0.40 as practical signal, not strict statistical power.
2. **Q4 diameter uncertainty**: ~80–200 is a range, not a point estimate. Exact diameter requires BFS; record actual diameter during pilot table build.
3. **B(3,3) lab ≠ B(2,5) guarantee**: Q_i quotients here are taken from B(2,5) (the candidate group). But the B(3,3) lab corpus uses words in the 3-generator exponent-3 group. Proxy evaluation on B(3,3) words via B(2,5) quotients tests the proxy's general structure, not B(2,5)-specific calibration. Transfer is structural, not empirical.
4. **Arm 3 move-set overlap with Arm 0**: bounded descent (Arm 3) with period moves overlaps with braid+power (Arm 0) at T=1. Any Arm 3 gain over Arm 0 is due to multi-step search. If Arm 3 fails, it may be that T=16 is insufficient, not that the approach is wrong.
5. **Feature vector not pre-registered for learned scoring**: Arm 2's feature vector (d_Q2, d_Q3, d_Q4, ...) is defined here but weights are not. Any learned scorer trained on these features in a downstream task must have its own pre-registration.

---

## §13 Gates Before Running

| Gate | Status | Action if blocked |
|---|---|---|
| Structural soundness: Q2/Q3/Q4 sizes, [Q,Q] nontrivial, max_i d_i lower bound | **CLEARED 2026-06-19** (Validator verbal verdict, quoted §4) | — |
| Validator structural verdict note filed in Math Validation/ | NOT filed — verdict quoted inline §4 | Validator may file retroactively; link if created |
| Pilot GATE A — human GO | **PENDING** | Do not run pilot until received |
| GATE B — distortion review: Q4 saturation fraction ≤ 50% on 100–500 char pool | Follows pilot execution | If FAIL: hold Arm 2; flag Q5 path to Lead |
| GATE C — human GO for B(3,3) lab | Follows GATE A pilot + GATE B review | — |
| GATE D — Lead review of results | Follows lab | Transfer decision per §10 |

**Execution provenance triple** (capture at run time for each component):

| Field | Pilot | B(3,3) lab |
|---|---|---|
| Git SHA (algo_mixing HEAD) | [fill] | [fill] |
| uv.lock sha256 | [fill] | [fill] |
| mixer-core binary sha256 | [fill] | [fill] |
| Script path | `experiments/burnside/b25/proxy_validation_v3/pilot_distortion.py` | `experiments/burnside/b25/proxy_validation_v3/b33_lab.py` |
| Output path | `runs/b25/proxy_validation_v3/<ISO-timestamp>/pilot/` | `runs/b25/proxy_validation_v3/<ISO-timestamp>/lab/` |

**DO NOT RUN until GATE A is issued by the human.**

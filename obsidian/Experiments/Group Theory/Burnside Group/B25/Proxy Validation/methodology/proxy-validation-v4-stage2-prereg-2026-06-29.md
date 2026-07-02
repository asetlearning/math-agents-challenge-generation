---
title: "Proxy Validation v4 — Stage 2 Pre-Registration (B₀(2,5)-scoped)"
date: 2026-06-29
domain: group-theory
project: b25
experiment_type: proxy-validation
instance: B0-proxy-stage2
author: maumayma
status: pre-registered
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/proxy-validation, project/b25, status/pending, methodology, experiment]
---

# Proxy Validation v4 — Stage 2 Pre-Registration

**Status**: Pre-registered. GO received from Lead (via Maria's explicit direction, 2026-06-29).  
**Scope**: B₀(2,5)-scoped proxy lab only. CORE arms 1/3 + pcgs/pi-family.  
**DO NOT proceed to further new-proxy designs without explicit Maria GO.**  
**Parent**: [[methodology/proxy-validation-v4-prereg-2026-06-26]] (Stage 1 was B(3,3) arms 1/3)

---

## AMENDMENT 2026-06-29 — Math-expert respec + Validator caveats

Two mandatory changes relative to the original pre-registration below:

**A1 — GT upgraded from Q4 to Q5 (Math-expert respec)**:
- Original: GT = Q4 = B₀/γ₅ (order 5^8). See §3 below.
- Amended: GT = **Q5 = B₀/γ₆ (order 5^10)**. Reason: Q5 is the first LCS quotient where the weight-5 pcgs/pi feature is non-vacuous (γ₅/γ₆ ≅ F₅², pcgs positions 9-10). In Q4, the weight-5 layer is collapsed to zero.
- All references to "Q4" in §2–§4 below should be read as **Q5** for the actual run.

**A2 — Validator mandatory caveats (2026-06-29)**:
1. **GT label (exact)**: `d_Q5(1,pi_5(g)) — Cayley distance in Q5 = B₀/γ₆; quotient-GT, NOT B₀-GT; d_Q5 ≤ d_B₀ by quotient-map inequality`
2. **Weight-5 requires Q5**: positions 9-10 in Q5 pcgs are the non-vacuous weight-5 F₅² coordinates. Q4 collapses these to zero — Q5 is the minimum required group for pc/weight-5 features.
3. **d_Q5=0 exclusion filter (mandatory)**: candidates with d_Q5=0 ("Q5-invisible") are EXCLUDED from all correlation computation and reported by count. This prevents the constant-GT trap (all correlation values = 0 or undefined if GT is constant).

These amendments are incorporated in the production scripts:
- `experiments/burnside/b25/proxy_validation_v4_stage2/stage2_bfs_q5.g`
- `experiments/burnside/b25/proxy_validation_v4_stage2/stage2_corpus_and_arms.py`

---

---

## §0 Binding Constraints (verbatim from Lead GO)

1. **B0-scope only** — all group computations in B₀(2,5), NOT free B(2,5)
2. **Generated candidates ONLY** — exclude the 119 benchmark words (circular; all in γ₅)
3. **Corpus NON-geodesic in B₀** AND includes non-geodesic [G,G] words
4. **Cayley-distance-in-B₀ as GT** — implemented as Q4 exact Cayley distance (see §3)
5. **[CONDITIONAL: B0≅B(2,5)/Kourovka 11.48]** tag on all results
6. **GAP word-equality on any rule** — abelianization FORBIDDEN as sufficiency check
7. **Process budget coordinated with Experimenter before compute**
8. **No premature close**

---

## §1 Notation and Group Structure

- **B₀(2,5)**: finite restricted Burnside group, order 5^34, nilpotency class 12. Generators {a, b}. Inverses a^{-1}=A, b^{-1}=B. Alphabet {a,b,A,B}.
- **LCS**: γ₁=B₀(2,5) ⊇ γ₂ ⊇ ... ⊇ γ₁₃={1}. Known: dim(B₀/γ₆)=10, dim(γ₅/γ₆)=2 → dim(B₀/γ₅)=8 → |B₀/γ₅|=5^8.
- **Quotient ladder** (confirmed by Validator, 2026-06-19):

| ID | Group | Order | Kernel |
|----|-------|-------|--------|
| Q0 | B₀/γ₂ = C₅×C₅ | 5² = 25 | γ₂ (commutator subgroup) |
| Q2 | B₀/γ₃ | 5^? | γ₃ |
| Q3 | B₀/γ₄ | 5^5 = 3125 | γ₄ |
| Q4 | **B₀/γ₅** | **5^8 = 390,625** | γ₅ |

  Sizes proven exact by Validator (class < p=5 theorem). Q4 is the GT group.

- **Key property**: ALL 119 benchmark words are in γ₅ (Q4 image = identity). The binding "generated candidates only" constraint is automatically enforced by requiring Q4_dist > 0.

---

## §2 Research Question

Do periodicity-excess (Arm 1), bounded-descent (Arm 3), and quotient projection (pcgs/pi-family arm) predict **Cayley distance in Q4 = B₀/γ₅** for:

(a) **Random non-[G,G] words** not in γ₅ (stratum II equivalent)
(b) **[G,G] non-identity words** not in γ₅ (stratum III equivalent)

Stage 1 (B(3,3)) showed all arms blind on stratum III because corpus words were already at geodesic length. Stage 2 corpus is explicitly NON-geodesic — so reduction-based features CAN show signal.

---

## §3 Ground Truth: Q4 Cayley Distance

**GT = exact Cayley distance in Q4 = B₀(2,5)/γ₅** (order 390,625, generators {a_Q4, b_Q4, A_Q4, B_Q4}).

**Computation method**: GAP BFS from identity in Q4, storing full distance table and generator action tables. For any input word w, Q4 distance computed in O(|w|) time via generator action lookup tables.

**Why this satisfies "Cayley-distance-in-B₀ as GT"**:
- Q4 = B₀/γ₅ is a QUOTIENT of B₀, so d_Q4(w) ≤ d_B₀(w) (lower bound)
- For words not in γ₅: d_Q4(w) is the EXACT distance in Q4; it approximates d_B₀(w)
- Corpus words are filtered to have Q4_dist > 0 → they are NOT in γ₅
- All B₀(2,5) claims tagged: [CONDITIONAL: B0≅B(2,5)/Kourovka 11.48]
- All GT claims tagged: [Q4-DISTANCE: exact in Q4=B₀/γ₅; lower bound in B₀]

**Feasibility**: Q4 BFS explores 390,625 elements. With 4 generators, ~1.56M pcgs multiplications. Estimated runtime: 30-120 seconds in GAP. Generator action tables: 390K × 4 × 4 bytes = 6.25 MB. Feasible.

**Exclusion zone**: Words in γ₅ (Q4_dist=0) are excluded from the corpus. This includes all 119 benchmark words — automatically enforcing binding constraint #2.

---

## §4 Corpus Design

### Stratum I — Identity in Q4 (d_Q4 = 0)

Words that map to identity in Q4 but are NOT empty strings. Sources:
- Relators from b25_gen kbprog (LHS of rules that reduce to identity under B₀ rules)
- Random walk words that happen to be in γ₅: generate words, filter d_Q4=0

Target: N_I ≥ 50 words.

### Stratum II — Non-identity in Q4, not [G,G]

Random walk words with:
- d_Q4 > 0 (not in γ₅)
- Abelianization ≠ (0,0) in C₅×C₅ (NOT in [G,G] = γ₂)
- len(word) > d_Q4 (non-geodesic)

Target: N_II ≥ 200 words.

### Stratum III — [G,G] non-identity in Q4 (KEY STRATUM)

Words with:
- Abelianization = (0,0) (in γ₂ = [G,G])
- d_Q4 > 0 (not in γ₅, i.e., NOT in {kernel of B₀ → Q4})
- len(word) > d_Q4 (non-geodesic)

**This is the critical stratum**: these are non-trivial [G,G] elements at positive Q4 distance, represented by words longer than their Q4 geodesic. The arms CAN potentially detect this slack.

Target: N_III ≥ 80 words.

### Generation Protocol

1. Random walk of length L ∈ {10, 20, 30, 50}: at each step, pick uniformly from {a,b,A,B} \ {undo_last_step} (simple random walk, no immediate backtracking)
2. Compute abelianization: (Σa - ΣA) mod 5, (Σb - ΣB) mod 5
3. Compute d_Q4 via GAP table lookup
4. Filter per stratum criteria
5. For non-geodesic requirement: len(word) > d_Q4 (guaranteed for random walks on Q4 diameter < L)

**Seed**: 20260629. n_seeds ≥ 5 for quantitative claims.

---

## §5 Arms

### Arm 1 — Periodicity-Excess (B₀ exponent-5)

Identical to Stage 1 but with n=5 (B₀ exponent):

For word w over {a,b,A,B}:
- Scan all contiguous u^k substrings where |u| ≤ K=8, k ≥ 2
- excess = |u| * (k mod 5)   [B₀(2,5): u^5 = identity]
- score = Σexcess / len(w)

**Parameters**: Primary K=8. Secondary: K ∈ {4, 12}.

### Arm 3 — Bounded-Descent (B₀ exponent-5 moves)

Move set for B₀(2,5):
- Free reductions: aA → ε, Aa → ε, bB → ε, Bb → ε
- Period-5 moves: u^5 → ε for |u| ≤ 4 (need 5-20 chars in the substring)
- Conjugate-radius-3: v·u^5·v^{-1} → ε for |v| ≤ 3

BFS from w, applying moves (length-non-increasing), up to T expansions.

**Note**: Unlike B(3,3), period-5 moves require at least 5 chars. For corpus words of length 20-50, these moves can fire and provide genuine shortening. Arm 3 is NOT expected to be blind on Stage 2 corpus (non-geodesic words).

**Parameters**: T=16 (primary), T=64 (secondary).

**Features**: first_descent_depth, total_shrink_T16, total_shrink_T64.

### Arm pc — pcgs/Pi-Family (quotient-projection features)

For word w, compute Q0, Q2, Q3 Cayley distances as FEATURES (NOT GT):

| Feature | Definition |
|---------|------------|
| d_Q0 | Cayley distance in Q0 = C₅×C₅ (= max(|a_exp|, |b_exp|) in Z₅ metric) |
| d_Q2 | Cayley distance in Q2 = B₀/γ₃ (BFS in Q2, trivially fast) |
| d_Q3 | Cayley distance in Q3 = B₀/γ₄ (BFS in Q3, ~3125 states) |
| excess_Q3 | len(w) - d_Q3 (apparent slack vs Q3 GT) |
| excess_Q4 | len(w) - d_Q4 (apparent slack vs Q4 GT) |

**Rationale**: Q2/Q3 distances are lower-level approximations to d_Q4 (GT). Their predictive power tests whether coarser group quotients predict finer ones — a structural question about the quotient ladder.

**No circularity**: Q4 is GT; Q2 and Q3 are FEATURES. They are different groups.

### Arm 0 — Baseline (greedy KB reduction)

Reuse Stage 1 approach: apply B₀(2,5) partial shortlex KB rules (from kbmag runs) greedily. Compute (len - len_reduced) / len.

- Rule source: 31 seed rules (GAP-verified, SHA256 `341c64bc...`) combined with partial shortlex bank.
- Arm 0 tests whether KB rules can shorten the non-geodesic corpus words.

---

## §6 Hypotheses

| ID | Hypothesis | Stratum | Threshold | Falsification condition |
|----|-----------|---------|-----------|------------------------|
| H5-0 | Arm 1 ρ on stratum II > 0.10 | II | ρ > 0.10 | ρ ≤ 0.10 |
| H5-1 | Arm 1 ρ on stratum III ≥ 0.20 | III | ρ ≥ 0.20 | ρ < 0.20 |
| H5-2 | Arm 3 ρ on stratum III ≥ 0.20 | III | ρ ≥ 0.20 | ρ < 0.20 |
| H5-3 | pc-arm (d_Q3) ρ on stratum III ≥ 0.40 | III | ρ ≥ 0.40 | ρ < 0.40 |
| H5-4 | total_shrink_T16 ρ on stratum III > 0 (vs Stage 1 NaN) | III | ρ > 0 (any signal) | ρ ≤ 0 or NaN |

**H5-4** is the critical test of whether non-geodesic corpus fixes the Stage 1 blind spot.

---

## §7 Measurements

Per arm, per stratum:
- Spearman ρ (proxy vs d_Q4), p-value
- Blind-spot fraction (score = 0 when d_Q4 > 0)
- Unique value count (if 1 → arm gives no gradient)

Steiger's Z for pairwise arm comparison (arm1 vs arm3 on stratum III).

All results reported per stratum, NEVER only full-corpus.

---

## §8 Anti-Pattern Guards

1. **[G,G] non-geodesic**: stratum III words MUST have len > d_Q4 (if len = d_Q4, words are already geodesics in Q4 → arms will be blind as in Stage 1 stratum III)
2. **No benchmark words**: verify no corpus word equals any of 119 HWW words (compare by string)
3. **Q4 distance 0 = excluded**: stratum I (identity in Q4) treated separately; no correlation defined between proxy and 0
4. **Arm 0 rule verification**: any new rule used in Arm 0 must have GAP word-equality verification in B₀(2,5) — abelianization FORBIDDEN
5. **Process budget**: coordinate with Experimenter before running GAP BFS + Python corpus + arm scorer

---

## §9 Provenance Triple

| Field | Value |
|-------|-------|
| GAP BFS script | `experiments/burnside/b25/proxy_validation_v4_stage2/stage2_bfs_quotients.g` |
| Corpus generator | `experiments/burnside/b25/proxy_validation_v4_stage2/stage2_corpus.py` |
| Arm scorer | `experiments/burnside/b25/proxy_validation_v4_stage2/stage2_arms.py` |
| Run dir | `runs/b25/proxy_validation_v4/stage2_<ISO-timestamp>/` |
| Corpus sha256 | Recorded at run time |

---

## §10 Scope Boundary (HARD STOP)

**CORE Stage 2 only**. After results are in:
- If H5-1 or H5-2 passes → report to Lead; do NOT file to Developer without explicit GO
- If H5-3 passes → Q3/Q4 distance gradient found; report to Lead; do NOT extend quotient ladder without GO
- All further proxy designs (new arms, new corpus, Stage 3) require explicit Maria GO

This pre-reg is registered under the B25 scope. Results → Lead → Maria.

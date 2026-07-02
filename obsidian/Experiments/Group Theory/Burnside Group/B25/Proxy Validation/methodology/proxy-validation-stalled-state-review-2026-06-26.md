---
title: Proxy Validation Track — Stalled-State Review (2026-06-26)
date: 2026-06-26
domain: group-theory
project: b25
experiment_type: proxy-validation
author: maumayma
status: pending-approval
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/patternboost, topic/proxy-validation, project/b25, status/pending, methodology]
---

# Proxy Validation Track — Stalled-State Review

**Purpose**: satisfy Standing Rule (enumerate ALL untested ideas before any closure) and provide updated pre-reg for Maria's GO gate. No runs until GO.

**Stall point**: 2026-06-19, after v3 pilot completed. Attention shifted to compression track and Fragment Shortening Hunt. Track was never formally closed.

---

## §1 What Has Been Done

### v1 — B(5,3) pilot (2026-06-17)

**Status**: INCONCLUSIVE with fatal flaws.

- Tested proxies A (reduction_ratio) and B (abelianization) vs. continuous geodesic GT on B(5,3).
- **Fatal**: (1) KB non-confluent — greedy reduction gives arbitrary fixed points, not geodesic distance; (2) substituted binary oracle (proved/not-proved) without pre-registration — unrouted math claim change; (3) proxy B and A both blind on commutator subgroup (the motivating class).
- **Transfer decision**: INCONCLUSIVE — do not transfer. See [[results/b53-proxy-results-2026-06-17]].

### v2 — B(3,3) lab (2026-06-18)

**Status**: COMPLETED. H1 NOT SUPPORTED, H2 NOT SUPPORTED.

- Lab: B(3,3), order 3^7 = 2187, exact Cayley-BFS ground truth. Corpus: 838 words (strata I/II/III).
- Stratum III = all 80 non-identity [G,G] elements. Distance range d=4,6,7,10.
- Proxy D (LCS-weight-2, lcs2_dist): ρ=0.079 on γ₂\γ₃ stratum III (threshold 0.40). NOT SUPPORTED.
- Proxy A (reduction_ratio): completely blind on stratum III (ρ=NaN, all scores 0).
- Proxy B (abelianization): constant 0 by theorem on [G,G], ρ=NaN.
- E (B+D): same as D on stratum III.
- **Lesson**: LCS-weight-2 is a coset-separation invariant, not a within-[G,G] distance gradient. The [G,G] blind problem is structurally hard — needs a METRIC-FLAVORED proxy, not an algebraic label.
- **Transfer decision**: Keep Option B. File new design. See [[results/b33-proxy-results-v2-2026-06-18]].

### v3 pre-registration (2026-06-19)

**Status**: Filed, Gate A issued, pilot ran. B(3,3) lab NEVER RUN.

**Design**: Four arms.
- **Arm 0** (baseline): Option B (braid+power reduction_ratio).
- **Arm 1**: Periodicity-excess (contiguous u^k substrings, K=8, no conjugation).
- **Arm 2**: C2 quotient-ensemble (Q2=UT₃(F₅), Q3=class-3 free nilp exp-5, Q4=class-4 free nilp exp-5) + C3 bounded-descent features.
- **Arm 3**: C3 bounded-descent features only (ablation).

**Structural gate** (CLEARED 2026-06-19 by Validator): Q2/Q3/Q4 sizes proven exact (class < p=5, Witt/Möbius formula no modular complications). max_i d_i is a valid lower bound on B(2,5) geodesic distance (functoriality). See [[methodology/b33-gg-proxy-validation-v3-2026-06-19]] §4 for full Validator verbal verdict.

### v3 pilot (2026-06-19, Gate A)

**Status**: COMPLETE. **GATE B FAILED — structurally.**

- Tested: all 119 B(2,5) benchmark words through Q2/Q3/Q4 and Arms 1/3.
- **Critical finding**: ALL 119 benchmark words give d=0 in Q2, Q3, and Q4.
  - Q2 diam=6, Q3 diam=10, Q4 diam=**19** (actual; estimated 80-200 was wrong).
  - All benchmark words are in γ₅(B(2,5)) (the kernel of the Q4 map B(2,5) → Q4).
  - Q4 = B(2,5)/γ₅ has order 5^8 = 390,625. All benchmark commutators are weight-≥5 commutators, so they're zero in Q4. Structural doom, not measurement failure.
- **Arm 1** (periodicity): score 0.0000 on both benchmark words (no detected u^k patterns).
- **Arm 3** (bounded descent): not separately reported in pilot summary (appears to have given 0 as well — see `pilot_results.json`).
- **GATE B cannot be evaluated**: (a) pre-reg required 100-500 char sub-pool of B(2,5) words, but NO benchmark words are in that range (all ≥ 2,496 chars); (b) even if the range were extended to all lengths, all 119 words give d=0 — saturation fraction is 0% but only because Q4 is BELOW the word length, not above it (all words map to identity, not to diam).
- **Outcome**: Arm 2 structurally fails on B(2,5) benchmark corpus. Q2/Q3/Q4 are too small for words of length 2,500–41,000.

**Run artifacts**: `runs/b25/proxy_validation_v3/20260619T135801/pilot/` (pilot_summary.txt, pilot_results.json, q2/q3/q4 tables).

---

## §2 What Was ABANDONED Without Testing

The following items were in the v3 pre-registration or were implied by the design and were NEVER run. None of these are closed.

### Item A — B(3,3) lab for Arms 1 and 3

**Never run.** The B(3,3) lab (GATE C) was the PRIMARY validation target in v3. The pilot's GATE B failure caused an implicit abandonment — but GATE B is the distortion check for Arm 2's Q_i quotients on B(2,5) benchmark words. It is NOT a prerequisite for running Arms 1 and 3 in the B(3,3) lab.

Arms 1 (periodicity scan) and 3 (bounded descent) require NO quotient tables. They can be run on B(3,3) [G,G] stratum III words entirely independently of the Q_i quotient distortion issue. The B(3,3) lab corpus and GT (Cayley-BFS distance table sha256 `0c4b4e11`) exist on disk.

**Untested question**: Do periodicity-excess (Arm 1) or bounded-descent (Arm 3) provide any Spearman ρ on the [G,G] stratum (stratum III, all 80 elements) in the B(3,3) lab? v3 pre-reg treats Arm 1 as a control (expected ρ ≈ 0) and Arm 3 as an ablation (threshold ρ ≥ 0.20). Neither has been tested in the B(3,3) lab.

### Item B — B(3,3) lab for Arm 2 with B(3,3) quotients

**Never run.** The v3 pre-reg §3 (Arm 2) defines the quotient scores using B(2,5) quotients Q2/Q3/Q4. But for the B(3,3) lab, B(3,3) words can also be evaluated in B(3,3) quotients — the free class-k nilpotent group on 3 generators of exponent 3. These are DIFFERENT groups than Q2/Q3/Q4 (different rank, different exponent). They ARE feasible:
- B(3,3)/γ₂ = C₃³ (order 27, diam ~3): negative control (abelian)
- B(3,3)/γ₃ = free class-2 nilpotent on 3 gens of exp 3 (order 3^6 = 729, diam ~6-10): first test
- Full B(3,3) BFS is exact (order 2187, already done in v2)

**Untested question**: Does the max-quotient-distance `max_i d_i(φ_i(w))` approach give gradient on B(3,3) [G,G] stratum when using B(3,3)-appropriate quotients? This tests the proxy STRUCTURE (quotient ensemble + distance lookup) in a feasible setting, separately from the B(2,5) size problem.

### Item C — Q5 feasibility check

**Never done.** The _progress.md notes "Need Q5 = B(2,5)/γ₆" and "Validator must confirm Q5 can be built + BFS-traversed." This check was never filed to Validator.

Q5 = free class-5 nilpotent on 2 generators of exponent 5. Order = Q4 × (weight-5 factor). Weight-5 Witt number for rank 2: by Witt formula `(1/5) Σ_{d|5} μ(5/d) 2^d = (1/5)(2^5 - 2^1) = (1/5)(30) = 6`. So Q5 has order 5^{8+6} = 5^{14} = 6,103,515,625 ≈ 6.1 billion.

A BFS table over 6.1 billion elements is infeasible (would require ~25GB RAM for even a compact table). BUT: evaluating a word w in Q5 as a PcGroup element (without a lookup table) is O(|w|) group multiplications — feasible. The challenge is computing geodesic distance without BFS.

**Untested question**: Can Q5 be built as a PcGroup, and is there a way to estimate (lower bound) geodesic distance in Q5 without a full BFS table? E.g., via the pcgs exponents at weight 5 as a partial metric proxy.

### Item D — Arms 1/3 on shorter B(2,5) words

**Not done systematically.** The pilot tested benchmark words (lengths 2,496–41,886), all too long for periodicity or bounded-descent to find signal. But the PatternBoost candidate pool targets words of length 100–2,000 chars (the proxies are for scoring GENERATED CANDIDATES, not the benchmark words). No corpus of B(2,5) words in the 100–2,000 char range was evaluated.

**Untested question**: Do Arms 1 and 3 give non-zero scores on B(2,5) words of length 100–2,000 chars? If yes, could they provide gradient within that range?

### Item E — Transfer criterion evaluation for v3 Arms 1 and 3

**Never done.** The v3 pre-reg §10 specifies what happens if H3-2 (Arm 3, ρ ≥ 0.20 on stratum III) is supported or not. This evaluation has never been run because B(3,3) lab was never run.

### Item F — New proxy design candidates (beyond the four v3 arms)

**Not enumerated.** v3 was abandoned without filing a "new design" note (which v3 itself said should happen if all arms fail). The following proxy ideas have NOT been pre-registered or tested at any lab:
- **Weight-5+ pcgs exponents of B(2,5)/γ₆** as a partial distance proxy (even without BFS, the pcgs vector at weight 5 could give gradient — a norm-on-fiber approach rather than BFS distance)
- **Hall polynomial evaluation**: explicitly compute the Hall polynomials relating word length to commutator weight in the free nilpotent group
- **Transfer from B(2,4)** (exponent 4, same rank 2): B(2,4) has known structure; its quotients could be used as proxy for B(2,5) with a structural-transfer argument
- **Cayley-metric estimation via random walk**: random walk mixing time as a proxy for geodesic distance (no table needed)
- **Subgroup-depth proxy**: length of the coset chain g·γ₁ ⊃ g·γ₂ ⊃ ... ⊃ g·γ_k = {g} — track which γ_k is the first to contain g
- **Combinatorial exponent sum**: for a word in {a, b, A, B}^*, count how the exponent contributions at each weight level sum (related to the Magnus expansion)

---

## §3 Exhaustion Assessment Per Item

| Item | Exhausted? | Justification / Unblocking action |
|------|-----------|-----------------------------------|
| A — B(3,3) lab, Arms 1 and 3 | **NO** | Requires Gate C GO from Maria. All artifacts (corpus, GT, B(3,3) kbprog) on disk. No quotient tables needed. Can run same day as GO. |
| B — B(3,3) lab, Arm 2 with B(3,3) quotients | **NO** | Requires B(3,3) quotient BFS tables (feasible, B(3,3)/γ₃ = order 729). Needs pre-reg amendment to specify B(3,3) quotients. |
| C — Q5 feasibility check | **NO** | File to Validator: "Can Q5=B(2,5)/γ₆ be built as PcGroup? Can geodesic distance be estimated without BFS (order 5^14)?" |
| D — Arms 1/3 on 100-2000 char B(2,5) words | **NO** | Corpus construction needed (generate/sample B(2,5) words in that range). May require Developer support (beam search or KB output words). |
| E — Transfer criterion for Arms 1/3 | **NO** | Blocked on Item A. |
| F — New proxy designs | **NO** | None has been pre-registered. Weight-5 pcgs norm is most tractable; needs pre-reg. |

**Conclusion**: NOT A SINGLE untested item is exhausted. The proxy validation track must not be closed. Items A and B are actionable immediately (all artifacts on disk, no new infrastructure). Item C is a Validator routing. Items D, E, F require new pre-regs.

---

## §4 Diagnosis

The v3 pilot's GATE B failure was informative but **not fatal to the track**. The finding is:

> "The specific quotients Q2/Q3/Q4 of B(2,5) are too small to discriminate B(2,5) benchmark words: all map to identity. But the proxy STRUCTURE (quotient-distance + bounded-descent) has not been tested on a group where we have exact ground truth."

The correct path is:
1. Run the B(3,3) lab for Arms 1 and 3 (no quotient needed) to get structural signal.
2. Evaluate whether the periodicity / descent features give ANY gradient on [G,G] in the B(3,3) lab.
3. If signal found: argue transfer and either use higher B(2,5) quotients (Q5 path) or use the features directly (bounded descent on B(2,5) words in the 100-2000 char range).
4. If no signal in B(3,3) lab (all arms fail): formally document the [G,G] proxy as an open problem at the B(3,3) lab level and route to Researcher.

---

## §5 Updated Pre-Registration Draft

See [[methodology/proxy-validation-v4-prereg-2026-06-26]] for the full v4 pre-registration draft. Summary:

**Stage 1 (GATE C GO needed, no new infrastructure)**:
- Run B(3,3) lab for Arms 1 and 3 only. Reuse v2 corpus (sha256 `0c4b4e11`). Report per-stratum ρ.
- Hypotheses: H4-1 (Arm 3 ρ ≥ 0.20 on stratum III), H4-0 (Arm 1 ρ ≈ 0, control).

**Stage 2 (gated on Stage 1 results)**:
- If Arm 3 supports H4-1: (a) route Q5 feasibility to Validator; (b) pre-reg Arm 3 on 100-2000 char B(2,5) words.
- If all arms fail: formally close [G,G] proxy at B(3,3) lab level; file open-problem to Researcher.

**Routing decision**: B(3,3) lab Arm 2 with B(3,3) quotients is deferred to Stage 2 (requires pre-reg amendment for quotient specification).

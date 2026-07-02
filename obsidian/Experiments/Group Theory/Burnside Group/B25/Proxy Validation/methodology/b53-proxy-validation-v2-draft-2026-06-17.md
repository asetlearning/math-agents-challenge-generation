---
title: B(5,3) Proxy Validation Study v2 — TOMBSTONED (invalid order assumption)
date: 2026-06-17
domain: group-theory
project: b25
experiment_type: proxy-validation
instance: B(5,3)
author: maumayma
status: tombstoned
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/patternboost, project/b25, status/tombstoned, experiment]
---

# B(5,3) Proxy Validation Study v2 — TOMBSTONED

**Status**: TOMBSTONED 2026-06-17 — invalid. Assumed |B(5,3)| = 2187 (3^7), which is |B(3,3)|. Actual |B(5,3)| = 3^25 ≈ 847 billion. Cayley-BFS over 847 billion nodes requires petabytes of RAM — completely infeasible. The entire GT plan is blocked until lab group is reconsidered. Awaiting Maria's direction on which lab to use (B(3,3) order 2187 vs another approach).

**Do not use this draft.** See [[results/b53-proxy-results-2026-06-17]] for the INCONCLUSIVE v1 outcome.

---

**ORIGINAL DRAFT PRESERVED BELOW FOR REFERENCE (do not execute)**

---

**Supersedes**: [[methodology/b53-proxy-validation-study-2026-06-17]] (v1, INCONCLUSIVE — KB non-confluent, commutator-subgroup blind spot, unrouted GT change)

---

## §1 Motivation (unchanged from v1)

PatternBoost for B(2,5) uses a SCORE proxy for "distance to identity" in the local search loop. Current proxy (Option B: braid+power reduction ratio) scores 0.000 on ~43% of B(2,5) words — in particular, products-of-conjugates like `(aba)^5` which lie in the commutator subgroup [G,G] (abelianization=0). This "blind spot" is fatal: PatternBoost has no gradient on these words.

**Key lesson from v1**: abelianization_distance also scores 0 on commutator-subgroup words. Neither proxy alone fixes the blind spot. The motivating class MUST be represented in the test corpus to evaluate proxy quality on it.

---

## §2 Lab: B(5,3)

B(5,3) = ⟨a,b,c,d,e | w³=1 for all words w⟩. Order 3⁷ = 2187 (finite). The word problem is decidable. The commutator-subgroup [G,G] is non-trivial (B(5,3) is non-abelian).

---

## §3 Ground Truth (changed from v1)

**GATE PENDING — Validator must confirm before registering:**

**Proposed GT**: Cayley-graph BFS distance from identity. Procedure:
1. Build the complete Cayley graph on 2187 nodes using generators {a,b,c,d,e,A,B,C,D,E}, adjacency = right-multiply by a generator.
2. BFS from identity node → exact geodesic distance d(w, 1) for all 2187 elements.
3. For a corpus word w: (a) solve the word problem to find w's canonical group element, (b) look up its BFS distance.

This gives a true continuous distance (range 0..max_dist) that the proxy should approximate. The y>0 slice is all non-identity words with d(w,1) > 0, which is a proper gradient.

**GT dependency**: step (a) requires a sound word-problem decision algorithm for B(5,3). Candidates:
- GAP's kbmag package on B(5,3) presentation
- The binary oracle (kb_mixer --bootstrap) — sound only if false-negative-free (Validator Q2)

**[GATE A — Validator]**: Is Cayley-BFS distance the correct ground truth for this proxy study? Is step (a) (word-to-canonical-element) achievable with available tools?

---

## §4 Proxy Candidates (unchanged from v1)

Three proxies evaluated on B(5,3) corpus words:

- **Proxy A**: `reduction_ratio = (L - L') / L` — one-pass leftmost Aho-Corasick greedy reduction using the 98K shortlex rule bank (run17). Single left-to-right scan only.
- **Proxy B**: `abelianization_distance = L1-norm of balanced-mod-3 generator exponent vector` — purely algebraic. Zero on all commutator-subgroup elements.
- **Proxy C**: `combined = 0.5 * proxy_A + 0.5 * proxy_B` — equal weights, fixed pre-registration. NOT tunable.

**Known limitation**: Proxy B (and therefore Proxy C) = 0 on all elements of [G,G]. This is a structural constraint, not a measurement artifact. The corpus MUST include non-identity commutator-subgroup words to evaluate whether the proxies have any gradient there (they don't; but we need this confirmed and quantified).

---

## §5 Corpus Design (changed from v1 — stratified)

**[GATE B — Validator]**: confirm examples of non-identity B(5,3) words in [G,G] for corpus inclusion.

Planned corpus (n ≥ 800):

| Stratum | Description | Target count |
|---|---|---|
| (I) Identity | B(5,3) relators from `b53_relators.txt` (153 words, y=0) | 153 |
| (II) Random non-identity | Freely-reduced random words, not in identity set, various lengths | 500 |
| (III) Commutator-subgroup non-identity | Deliberately sampled words in [G,G] \ {1}: short commutators [a,b], [a,c], ..., products [a,b][a,c], [a,b]^2, etc. — abelianization=0, expected y>0 | ≥50 |
| (IV) Hard random (long words) | Length 30–50, to ensure large-y bins | 100+ |

**Stratum III design** (pending Validator confirmation of which words are non-identity):
- `[a,b] = ABab` (length 4): is this non-identity in B(5,3)?
- `[a,b]^2 = ABabABab` (length 8): is this non-identity in B(5,3)?
- `[[a,b],c] = [ABab, c] = CBAbabc` (approx length 7): non-identity?
- Goal: ≥50 confirmed non-identity words in [G,G] with varying distances

**Seed**: 20260617 (same as v1 for random strata)

---

## §6 Analysis Plan

### §6.1 Full corpus (n_total ≈ 800+)
- Pearson r(proxy, y) and Spearman ρ(proxy, y) for each proxy
- 95% CI via Fisher z / bootstrap
- p-values

### §6.2 y>0 slice (non-identity words only)
**PRIMARY DECISION BASIS** (same as v1 requirement)
- Same statistics as §6.1 on non-identity subset
- Blind-spot fraction: fraction of non-identity words with proxy=0

### §6.3 Stratum III slice (commutator-subgroup non-identity, [G,G] \ {1})
**NEW in v2 — the critical anti-blind-spot check**
- Report proxy distributions on stratum III separately
- Expected: Proxy A and Proxy B both ≈ 0 on stratum III → confirms blind spot structural, not numerical
- If any proxy has non-zero values on stratum III: note and report

### §6.4 Steiger's Z (H1 test)
- Compare r(combined) vs r(reduction_ratio) on y>0 slice using Steiger's Z
- Formula unchanged from v1

---

## §7 Hypotheses (updated)

**H1**: combined proxy C has meaningfully larger correlation with geodesic distance than reduction_ratio alone on the y>0 slice.
- Threshold: delta_r > 0.05 AND r(C, y>0) ≥ 0.60 AND Steiger's Z p < 0.05
- Direction: motivated if abelianization contributes signal BEYOND the reduction_ratio on non-commutator-subgroup words

**H2**: abelianization_distance has non-trivial correlation on y>0 slice.
- Threshold: r(B, y>0) ≥ 0.40

**H3 (new)**: blind-spot rate on stratum III (commutator-subgroup words) is ≥ 95%.
- Expected: both Proxy B and Proxy C score 0 on all commutator-subgroup words (structural constraint)
- This is a CONFIRMATION TEST, not a pass/fail gate. Expected result = both blind.

**Transfer rule** (pre-registered, must be locked before running):
- H1 supported on y>0 AND H3 confirmed → Transfer: USE COMBINED PROXY on non-commutator-subgroup words; acknowledge blind spot on [G,G]
- H2 only → USE ABELIANIZATION alone (same caveat)
- Neither → KEEP Option B; file new proxy design targeting [G,G] gradient

---

## §8 Anti-pattern check

- [ ] GT independent of proxy computation? **YES** — BFS distance is exact group-theoretic distance; Proxy A uses shortlex rules but BFS uses group multiplication, not KB rules.
- [ ] Commutator-subgroup blind spot acknowledged and quantified? **YES** — stratum III explicitly tests this.
- [ ] No tuning: proxy weights α=β=0.5 fixed, not tunable.
- [ ] Transfer rule locked before results visible? **YES** — this is the pre-registration.

---

## §9 Stop conditions

- Validator cannot confirm safe examples of non-identity [G,G] words → cannot build stratum III; halt and report
- BFS distance GT implementation has bugs (e.g., some relators don't map to distance 0) → halt and fix before any analysis
- Word-problem solver for step (a) is unavailable or unsound → halt and escalate to Lead

---

## §10 Pending Validator gates

| Gate | Question | Status |
|---|---|---|
| A | Is Cayley-BFS distance the correct GT? Is step (a) (word→canonical element) achievable? | PENDING |
| B | Examples of non-identity B(5,3) commutator-subgroup words; is [a,b]=ABab non-identity? | PENDING |
| C (from v1, re-ask) | Is binary oracle (kb_mixer --bootstrap) sound as false-negative-free identity checker? | PENDING |

**Do not advance to running until all three gates are answered.**

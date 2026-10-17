---
title: t024-challenge-census-and-onion-probe-2026-10-17
hypothesis: "The real challenge words are (nearly) 2.5-power-free, and a one-level 'onion' step (tile a power-free dataset word's boundary with inverse arcs of dataset relators) raises strict depth beyond what its components carry."
status: draft
author: asetlearning
date: 2026-10-17
todo: T-024
project: challenge-gen
instance: B(2,5)
experiment_type: structured-constructions
tags: [agent/exp, user/asetlearning, domain/group-theory, topic/burnside, topic/b25, topic/trivial-words, topic/hard-instance-generation, topic/dehn-function, topic/power-free-words, project/challenge-gen, status/draft, experiment, methodology]
---

# T-024 (draft): challenge power census and the M1 one-level onion probe

**Status: draft, results of two small analyses on existing data. No T-024 pre-registration yet.** Both were owner-approved on 2026-10-17 (via Lead): the census first, then M1. Nothing else was run.

Sources: Math Expert [[2026-10-16-t024-depth-vs-length-and-long-words]] §3-§4 (design and reading rule); Developer's step-1 timing, `test-output/t024-feasibility-step1-2026-10-16.md`; the T-018 note [[t018-t021-diagram-search-2026-10-14]] (strict depth definitions S1/S2/S3, T1 baseline).

Terms used below:
- **2.5-power window**: a stretch of a word with period m and length at least ⌈2.5 m⌉ (exponent L/m ≥ 2.5); the same definition as the T-018 power gate. A word is **power-free** when it has none. **2.5-reduced** (the challenge files' name) is weaker: windows of exponent exactly 2.5 survive.
- **Arc**: a run of consecutive letters of a cyclic word. **Tile**: a power-free dataset relator r, written cyclically as r = s⁻¹ t, which attaches to the arc s of a word and replaces it by t. **Onion level**: cut w₀ cyclically into arcs s₁…s_k, take a tile for each, and put w₁ = t₁…t_k (cyclically reduced), requiring that t_j and t_{j+1} cancel at least one letter at every junction.
- **ā** = mean arc length (|w₀|/k); **λ** = |w₁|/|w₀|.
- **Strict depth S2**, **N**, **T_deep**, **T_depth**, "area-like": as in the T-018 note (S2 absorbs cells with |v| = 1 repeatedly before each peeling layer; area-like needs N ≥ 16, T_deep ≥ 0.5, T_depth ≥ 0.5, deep core ≥ 2, maxdepth ≥ 2). Depth numbers are for **our certificates after our compression**, not for minimal fillings (the Validator showed that compression can raise S2).

## 1. Challenge power census (118 non-empty challenge words)

Input: `data/b25_hww_challenges_2_5reduced_20260319.json` (sha256 62f44ab1…); 118 words, 2,494–27,321 letters (median 11,696; 1,486,221 letters in all). Windows are counted on the **linear** word as given (no wrap-around), once each at the primitive period. Script `t024_census.py`, output `data/t024/census.json` (sha256 628c091b…), 40 s on one CPU.

| quantity | result |
|---|---|
| windows per word | 7-100, median 45; **every word has some** (0 power-free words of 118) |
| windows per 1,000 letters | 1.9-4.8, median 3.8 (5,543 windows in 1.49 M letters) |
| overlap | none in 117 words (windows = clusters); in R138, 25 of its 37 period-2 windows lie inside the big period-2,376 window (38 windows, 13 clusters) |
| maximal run exponent | **exactly 2.5 in every word**; no window of exponent above 2.5 |
| period | 5,542 of 5,543 windows have **period 2**: the pattern xyxyx (`babab` 2,804; `ababa` 2,430; the inverse patterns 308) |
| the one other window | R138 (8,324 letters): period 2,376, length 5,940 = 2.5 × 2,376, starting at letter 1,194, covering 72% of that word |
| shape of every window | **even period m and length exactly 5m/2** in all 5,543 windows (`non_exact_half` field of census.json: 0 exceptions in the 118 words; the random reduced controls have 76, 271 and 978): the "exact half" case of the T-018 power-failure classification |
| letters covered | median 1.9% (R138: 72%) |

Controls (same script): a random freely reduced word has 85-105 windows per 1,000 letters, exponents up to 9, periods 1-6 (1,000, 3,000, 12,000 letters); a random power-free word built letter by letter has 0 windows and maximal exponent 2.33-2.4.

Reading:
- The challenge words are **not** power-free, but they are far from random: every residual window is an exact-half window (even period m, length 5m/2; in 5,542 of 5,543 cases the length-5 stretch xyxyx), about one per 260 letters. This is exactly the half-exposure edge that the T-018 gate was built around: the complement of a half v⁵ in the cell has the same length as the half, so a length-reducing rewrite has no gain there, whereas odd-period windows of length ⌈2.5m⌉ shorten by one. That is why the challenges stop at exponent 2.5 (I did not read the reduction's code; this is the consistent explanation, not a check of it).
- R138 contains u^2.5 with |u| = 2,376 as a 5,940-letter stretch: a word one relation (u⁵ = 1) away from a rewrite of 2,376 letters. Worth Lead's attention as a structural fact about that one challenge.
- Distance from exactly power-free: about 45 independent sites per word (median), each a 5-letter stretch, in 118 of 118 words; about 3.8 per 1,000 letters. One site (R138) is a 5,940-letter stretch of period 2,376.
- This is why the Developer's guard closure branches on challenge words: it explores both rewrites at every one of those sites.
- "Power-free" is therefore a property of the **construction target** (the exact-power-free boundary the T-018 gate enforces), not of the real challenges, which sit at the boundary: no exponent above 2.5, but ~4 sites per 1,000 letters at exactly 2.5. Whether T-024 should target exact power-freeness or "no window above 2.5" is the owner's decision; if the latter, the exact-half windows (period 2, length 5) become allowed, a change to the gate with its own consequences for the guard.

Longest arcs shared with the dataset (820 relators, all rotations, both orientations, and the 8 letter automorphisms of the challenge word) and with the R7 cores (1,630 table entries):

| | challenge words (118) | random power-free (1k, 3k letters) | random reduced (1k, 3k, 12k) |
|---|---|---|---|
| dataset: longest arc | 19-21 (median 19) | 22, 19 | 19, 19, 22 |
| dataset: mean longest match per position | 11.0 (10.97-11.15) | 11.3, 11.4 | 8.2, 7.8, 7.6 |
| dataset: share of positions in an arc ≥ 13 | 18% (17-20%) | 21.6%, 21.6% | 6.8%, 7.3%, 5.6% |
| dataset: share in an arc ≥ 20 | 0 | 0 | 0, 0, 0.05% |
| R7 cores: longest arc | 12-14 (median 14) | 14, 14 | 13, 15, 13 |
| R7 cores: mean longest match | 6.6 | 7.3, 7.3 | 7.2, 7.3, 7.2 |

Reading: the challenges share arcs of at most 21 letters with any dataset relator, and no more than a random power-free word does (the mean match of 11 is what power-freeness alone gives; random reduced words have fewer because they contain powers the dataset avoids). **There is no excess long-arc sharing**, so the census gives no support for the arc-tiling picture, and none against it: arcs of 15-21 letters exist in every long power-free word.

## 2. M1: one-level onion probe on the 491 power-free dataset words

Specification: Math Expert note §4. Scripts `t024_m1_tiling.py` (tilings), `t024_m1_cert.py` (cut vertices, certificates, depth), `t024_m1_report.py` (tables); outputs `data/t024/m1_tiling_cert.json` (sha256 7a059006…), `m1_tiling_control.json` (9dbb0f51…), `m1_cert.json` (230a7d9e…), `m1_cert_pf.json` (511b2788…). Inputs: `b25_trivial_2_5reduced_unique_aut8_20261014.txt` (e0eeb777…), the T1/T-018 certificates `data/t1/outputs/certs_gt53.jsonl` and `data/seeds_power_free_len_le53.jsonl`.

Method (my choices where the specification was open):
- **Words w₀**: the 491 power-free dataset words that the T-018 certification attempted (my `has_power25_cyclic` test finds 492: line 431 is also power-free but was not attempted). They are used with their 8 letter-automorphism images.
- **Tile set**: the 453 power-free dataset words with a stored R7 certificate, both orientations, all rotations. A tiling is a construction only if every tile has a certificate. The word w₀'s own tile is excluded.
- **Arcs**: length 4-26 (a 3-letter arc with a 60-letter relator is not a cell sharing a side; I fixed the minimum before running and did not vary it).
- **Search**: exact dynamic programme over the cyclic cut points, minimising |w₁| (with one cancelled letter per junction side), for each of the 8 images, plus 3 randomised re-runs per image (noise on the costs) to produce alternatives, about 17 distinct tilings per word. Power-freeness of w₁ is then tested exactly; the "power-free" rows below use the shortest power-free tiling found among those ~17. This is a modest search, so "share with a power-free w₁" is a **lower bound**.
- **Depth test** (20 + 36 words): the certificate of w₁ is w₀'s certificate followed by the tiles' certificates, each conjugated by the arcs after it (w₁ = w₀ · Πⱼ sufⱼ⁻¹ r′ⱼ sufⱼ; checked by expanding to w₁ in every case). Each component (w₀ and every tile) is compressed first (C++ `compress`), the pieces are assembled, and the assembly is compressed again. Compressing the 600-2,000-cell raw union directly took minutes per word (350 s for 634 cells); compressing the parts first gives the same cell count in the one case I compared (112), but it is a different procedure and not a minimal filling. The bouquet control compares the S2 depth of the final diagram with the maximum S2 depth of the compressed components. Only tilings made with the identity automorphism are used (so no relabelling of certificates is needed): 159 words have one as their shortest tiling, 37 as their shortest power-free tiling (36 ran: one of the 37 is among the 38 power-free words with no stored certificate, whose own certificate is needed).

### 2.1 Tiling results (491 words)

| quantity | result |
|---|---|
| words with a full tiling (non-degenerate) | **491 of 491** (one candidate tiling degenerated to w₁ = empty: w₀ is a product of two tile arcs) |
| shortest tiling: arcs k | median 4 (IQR 4-6; 10-90%: 3-7) |
| shortest tiling: mean arc ā | median 14.8 (IQR 12.7-16.6) |
| shortest tiling: **λ** | **median 2.07** (IQR 1.67-2.41; 10-90%: 1.38-2.76) |
| λ by |w₀| | ≤53: 1.88 (30 words); 54-80: 1.87 (347); 81+: 2.45 (114) |
| w₁ power-free, shortest tiling | 7.7% (38 of 491); non-power-free ones have a median of 2 windows |
| words with **some** power-free w₁ among ~17 tilings | **142 of 491 (28.9%)**; 3.5% of all tilings are power-free |
| power-free tiling: λ / k / ā | median 2.09 / 4 / 15.0 |
| cut vertex strictly inside a tile arc (condition (a)) | 2 of 2,380 arcs of the shortest tilings (0.08%); 3 of 667 arcs of the power-free ones (0.45%) |

### 2.2 Control: the same probe on random power-free words

60 random power-free words of 54-123 letters (not dataset words), the same 453 tiles: all 60 tile; ā median 7.3 (against 14.8), k median 12, **λ median 4.9** (IQR 4.6-5.1); w₁ power-free for 0 of the shortest tilings, and 9 of 60 words (15%; 1.3% of tilings) have some power-free tiling, with λ median 5.1. So the low λ of the dataset words is largely **self-similarity of the dataset** (its words share long arcs with each other), which a w₁ produced by tiling will not have. For levels beyond the first, the control (λ ≈ 5) is the better guide, not the dataset words (λ ≈ 2).

### 2.3 Strict depth of the one-level diagram (compressed)

| | power-free w₁ (36 words) | shortest tiling, mostly not power-free (20 words) | T1 baseline (453 dataset certificates) |
|---|---|---|---|
| \|w₁\| / N after compression | 71-282 / 58-304 | 52-303 / 53-311 | 32-123 letters |
| S2 maxdepth 1 / 2 / 3 | 14 / 21 / 1 | 7 / 10 / 3 | depth 2 in 11 words (2.4%), never 3 |
| max S2 depth of the compressed components | 0 (5 words) or 1 (31) | 0 (3), 1 (16), 2 (1) | |
| S2 depth **above** the components' | **26 of 36** | 14 of 20 | |
| S2 area-like (this certificate's N) | 0 of 36 | 2 of 20 | 0 of 453 |
| S1 maxdepth | 2 (24), 3 (11), 1 (1) | 1 / 2 / 3 / 4: 1 / 9 / 7 / 3 | |
| median S2 T_deep (range) | 0.32 (0.06-0.61) | 0.40 (0.12-0.64) | |

S1 (the weaker absorption rule) is more generous: S1-area-like for 9 of 36 power-free words and 10 of 20 of the mixed group. S2 is the adopted definition, so the table above reports S2.

The deepest power-free example is dataset line 671 (0-based index 670): |w₁| = 213, N = 192, S2 depth 3 (components 1), T_deep 0.33, T_depth 0.47, not area-like. Both S2 area-like words in the mixed group (indices 216 and 68) have w₁ that is not power-free. S2-area-like with a power-free w₁ did not occur in this sample.

## 3. Reading rule (Math Expert §4) applied

| branch of the rule | outcome |
|---|---|
| "Most words tile and the median λ ≤ 3: depth 4 is reachable at \|w\| ≲ 10³ by construction. Go to a multi-level run." | **Met at level 1**: 491/491 tile, median λ 2.07. **But** the control (λ ≈ 4.9) says later levels will not be this cheap. |
| "λ ≈ 5-8: about 3 levels reach challenge length, at strict depth ≈ 3 + d₀. Feasible but shallow." | **Met for a generic power-free w₁** (control λ ≈ 4.9, ā ≈ 7). |
| "Few words tile, the junction condition is rarely satisfiable, or w₁ is rarely power-free: the onion route fails at step 1; relax intermediates." | **Partly met**: junctions are always satisfiable and all words tile, but w₁ is power-free for only 7.7% of the shortest tilings, for 29% of words after a modest search, and for 15% of control words. Intermediate power-freeness is a real cost. |
| "Depth after compression ≤ max component depth: the depth gain is fake (bouquet); stop." | **Not met**: the depth after compression exceeds the components' in 26 of 36 power-free cases (typically 2 against 1). |

So the rule points to the **multi-level branch with the λ ≈ 5 expectation**: go on, as a pilot of 2-3 levels, and plan on relaxing power-freeness for the intermediate words (require it only at the end, or accept a few windows). The depth gain at level 1 is real in our certificates: it is a rise of about one layer over the components (the prediction depth ≈ level + d₀ held for one level).

## 4. What this does not show

- One level only. Depth growth with level, and the λ of a generated w₁ at level 2, are untested; the control is a proxy.
- The depth is for our certificates after our (component-first) compression, not minimal fillings. The Validator's point applies: a better compression could change S2 either way. The S2 area-like count is for the compressed certificate's own N, not an N* of the word.
- The power-free sample (36) is the identity-automorphism subset of the 142 words that had a power-free tiling; it is selected (by having one), and small.
- The census counts linear windows only, on one definition; the claim "all exponent exactly 2.5" is about this definition (windows with length ≥ ⌈2.5 m⌉).
- I have not checked the derivation of the claim that those windows are what the 2.5-reduction leaves; it is an observation.

## 5. Files (uncommitted, working tree of the t018 repo)

`experiments/challenge_gen/t018/scripts/`: `t024_census.py`, `t024_m1_tiling.py`, `t024_m1_cert.py`, `t024_m1_report.py`. Data: `experiments/challenge_gen/t018/data/t024/` (five json files, 0.9 MB in all). Runs: capjob 2 CPUs / 2 GB each (the two depth runs and the control ran at the same time, 4 CPUs in all at one point, against a 2-CPU cap per job); census 40 s; tiling 491 words 28 min on 2 CPUs; control 60 words 5 min; depth 20 + 36 words about 12 min each on 1 CPU. Pure Python plus the local tcgraph_ext build (`compress`, `has_power25_cyclic`); no heavy kernel was newly written (the tiling DP is Python and would need a C++ port for a multi-level run on thousands of letters).

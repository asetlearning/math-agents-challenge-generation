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

## 6. Pre-registration: level-2 onion pilot (written 2026-10-17, before any pilot run; approved by Lead under the owner's delegation)

**Question.** Does a second onion level raise strict depth again (about +1 per level, as one level did), when intermediate words are not required to be power-free?

**Design (fixed before running).**
- **Seeds**: 50 power-free dataset words with a stored certificate, `random.Random(2417).sample(sorted certified ids, 50)`. Tiles: the same 453 certified words, arcs 4-26, identity letter-automorphism only (so certificates need no relabelling), same DP (`t024_m1_tiling.py`), tile of the word itself excluded.
- **Level 1**: for each seed, the 3 shortest distinct tilings (DP optimum plus 12 randomised re-runs, noise 3.0), no power-free requirement (relaxed). Each parent w₁ gets a compressed certificate (components compressed first, assembled, compressed).
- **Level 2**: each of the 3 parents is tiled the same way (13 tilings each, so up to 39 candidates w₂ per seed). Lengths are expected near 300-600 letters. **Level 3 is not run**: it would exceed 10³ letters, which goes to C++ first.
- **Final gates, reported side by side**: (A) w₂ exactly power-free (no window of period m and length ≥ ⌈2.5m⌉, cyclic); (B) "exact-half allowed", i.e. challenge-like: every window has even m and length exactly 5m/2 (so max run exponent ≤ 2.5). A ⊂ B. Per seed, the final A-word (B-word) is the shortest candidate passing A (B); certificate built and compressed only for these.
- **Measured per level** (level 1: all 150 parents; level 2: the A and B finals): λ = |w_L|/|w_{L-1}|; share passing A and B (among all candidates, and per seed "has one"); S2 maxdepth, N_deep, T_deep and T_depth at the certificate's full N, deep core, area-like; D_c,≥2 = N_≥2/|w| (N_≥2 = cells of root length ≥ 2); bouquet control = S2 depth against the maximum S2 depth of the compressed components (previous-level diagram, tiles); L0 (the certificate expands exactly to the word, asserted); novelty (cyclic word is not a rotation or inverse of an R7 relator, and not one of the 820 dataset words under the 8 automorphisms).
- **Hypothesis H-L2**: the mean S2 maxdepth of the level-2 finals exceeds the mean of their level-1 parents by at least 0.5, and the largest level-2 depth exceeds the largest level-1 depth in the pilot.
- **Falsifier**: no level-2 final (under A or B) has S2 maxdepth above the largest level-1 parent depth in the pilot. Also reported as failure modes: fewer than 10 seeds with a final under A (the exact-power-free gate is then not reachable with this search); bouquet control failing (depth ≤ component maximum) for most finals.
- **Not used for the decision**: S1 and S3 are reported, S2 is the adopted definition. Depths are for our certificates after our compression, not minimal fillings.
- **Cost** (to be fixed after a 2-seed timing smoke test, excluded from the results): one capjob at a time, or rjob.

**Amendment (before the full run, after a 2-seed timing smoke test, seeds 48-49 of the sample, about 60 s per seed on one CPU):** the smoke test gave 1-5 distinct level-2 candidates per parent and none passing A or B, so the gated arms alone may leave nothing to measure. Added: (i) level 2 uses 40 randomised re-runs per parent instead of 12 (level 1 unchanged); (ii) an **ungated reference arm U**: per seed, the level-2 candidate with the fewest windows (ties: shortest), certificate and depth measured as for A and B, reported separately and never counted as an A or B result. U answers whether burial continues at level 2 when the gates cannot be met; A and B answer the gated question. The falsifier and H-L2 apply to A and B as written; for U the same comparison is reported as a diagnostic. Cost estimate: 50 seeds x about 1-2 min = 50-100 min on one CPU, or 25-50 min on 2.

## 7. Corrected gate (owner, 2026-10-17): target is 2.5-reduced, not power-free

Owner correction (via Lead): the 2.5 reducer replaces u^p by u^-(5-p), which shortens the word only for p > 2.5, so the target property is **2.5-reduced**: no window of exponent strictly above 2.5 (forbidden length for period h: ⌊2.5h⌋ + 1); exact 2.5-powers are allowed. Everything in sections 1-6 above was measured with the **stricter** "power-free" test (windows of length ⌈2.5h⌉, exponent ≥ 2.5), which differs only for even periods. Marked here as *under the superseded gate*; what changes:

- **Census (section 1)**: the 118 challenge words have no window of exponent above 2.5 (all 5,543 windows are exact halves, 0 exceptions), so on the linear windows counted they **are 2.5-reduced**. The earlier question "is power-free the right target" is answered by the owner: no, 2.5-reduced is. (Cyclic wrap-around windows were not counted.) The arc-sharing results do not depend on the gate, except that the random power-free control is a stricter control than needed.
- **Gate B of the pilot (section 6)** was defined as "every window has even period m and length exactly 5m/2". This is **identical** to 2.5-reduced (odd periods: ⌈2.5m⌉ = ⌊2.5m⌋ + 1 is forbidden in both; even periods: length 5m/2 allowed in both, longer forbidden in both), so B is already the corrected gate and is the **headline**. Gate A (exactly power-free) stays as a diagnostic column. No code change.
- **Dataset recount** (my own window count, cyclic): all **820** dataset words are 2.5-reduced; 492 are strictly power-free (the earlier 491 attempted + line 431); so the strictly-power-free tile and seed sets used in M1 are a subset (492 of 820, tiles 453 of 820). Growing the certified set to 820 needs 329 new KB certifications (the T1 job certified 461 words in 70 min on 9 CPUs) and is **not started**; it needs Lead's go.
- M1 shares ("w1 power-free for 7.7% / 29%") are under the superseded gate; the corrected share needs a re-run of the M1 tiling and is prepared, not run.


### 7.1 Recorded under the corrected gate (2.5-reduced), 2026-10-17

- **(a) Dataset**: all **820** dataset words are 2.5-reduced (cyclic windows of length ⌊2.5h⌋+1); 492 are strictly power-free and 328 carry only exact-half windows. ρ_min16 (certify mode, 16 images, `t024_corrected_a.py`, `data/t024/corrected_a.json`): **1.0 for 818 words, 0.0 for 2 words**, so those 2 are **not L1**: 0-based dataset indices 13 and 14 (lines 14 and 15; 44 letters, 3 exact-half windows each, neither strictly power-free). Among the 328 not strictly power-free words 326 have ρ_min16 = 1 (these are the "326 L1 non-strict words" for later use); all 492 strictly power-free words have ρ_min16 = 1. The strictly-power-free sets used in sections 1-6 are a subset of the corrected set; not extended (the certification wave waits for a C++ certifier, Lead 2026-10-17).
- **(c) T2 under the corrected test** (old B0+N arm states, `t2_jr_bound.py --corrected`, same attachments; gate 1 already allowed exactly half, so only the power test changes): beam pass12 289 → 304, pass_all 173 → 185, repairable failures 442 → 502; optimistic JR ratio on pass_all raw 3.55 → 3.71, distinct 3.56 → 3.85. Greedy: pass12 244 → 255, pass_all 145 → 153, repairable 370 → 421; ratio raw 3.55 → 3.75, distinct 3.51 → 3.82. The rule threshold is 1.5, so junction repair is still not dropped. This re-tests old states; it is not a new search under the corrected gate.

## 8. Pilot smoke section: the 2 smoke seeds (dataset indices 21 and 594), diagnosis

Not part of the pre-registered results (the pilot waits for the C++ tiling, Lead 2026-10-17). Script `t024_diag.py`, data `data/t024/diag_smoke.json`; same seeds and rng as the smoke run, no certificates. Gate = 2.5-reduced (exact halves ignored).

**Smoke timing and outcome** (pilot script, 1 CPU): about 10 min per seed (level-2 tilings with 40 re-runs, then compress and statistics of a 450-cell diagram). Seed 21: 3 level-1 parents (152, 153, 153 letters, S2 depth 2, d₀ = 1), 8 level-2 candidates, none passing A or B; the ungated reference (fewest windows) has 376 letters, N = 460, S2 depth 2, the same as its parent: no depth rise in that one case. Seed 594: 1 parent (291 letters, depth 2), candidates fail too. Two seeds only.

**Why the candidates fail** (15 distinct level-2 candidates over 4 parents; 182 junctions, 71 forbidden windows, 0.39 per junction):
- **Every forbidden window spans exactly two neighbouring pieces, i.e. one junction** (71 of 71). None lies inside one piece (expected: a piece is a subword of a 2.5-reduced cyclic dataset word), none spans three. So a rule that checks each junction against its two neighbours is enough to decide the gate; the failures are local to junctions.
- Periods: **44 of 71 have period 1** (a letter repeated 3 or more times across the junction), 16 period 3, 8 period 4, 3 period 5. Exponents 2.67-4.0. No window of period 2 (exact halves are the allowed ones and are ignored; 1-2 per candidate occur).
- Cancellation at junctions is not the cause: candidates with 14 to 24 cancelled letters over 11-12 junctions fail alike.
- A candidate has 1-7 forbidden windows. If junctions failed independently at rate 0.39, a 11-junction candidate would pass with probability about 0.61¹¹ ≈ 0.4%; the observed 0 of 300 re-runs per parent is consistent with that.
- **Can another tiling pass?** With 300 randomised re-runs per parent (noise 3 and 8): the minimum number of forbidden windows reached is 4, 4, 6 (seed 21 parents) and 1 (seed 594 parent); 0 tilings pass B, 0 pass A. Noise on the DP costs does not find a clean one; the search is blind to the junction content.
- L1 was not evaluated: no candidate passed the gate (the separate ρ_min16 check applies to finalists).

**What this tells the C++ port.** The level step needs a **junction-aware rule**: because every failure sits at one junction between two neighbouring tiles, the DP can carry the identity of the previous tile (its last ~25 letters) as state and reject a transition when the join creates a window of exponent above 2.5. The state grows from 4 end letters to (arc, tile) choices (about 10² per position), which is cheap in C++. Cheapest first filter: the period-1 failures (62% of windows) are run-length: reject a join that leaves 3 equal consecutive letters (period 1 exponent ≥ 3) across the junction. Whether an exact-half-allowed, junction-clean tiling exists for most parents is not known: the blind search suggests it is rare (about 1 junction in 2 or 3 is bad), the junction-aware DP would settle it.

## 9. M1 re-run under the corrected gate (2.5-reduced), tiling part

Same 491 words and 453 tiles, arcs 4-26 (`m1_tiling_corrected491.json`, 28 min, 2 CPUs). Gate B = 2.5-reduced; A = strictly power-free.

| quantity | A (superseded gate) | **B (corrected)** |
|---|---|---|
| shortest tiling has w₁ passing | 7.7% | **12.0%** |
| words with some passing w₁ among ~17 tilings | 142 (28.9%) | **185 (37.7%)** |
| share of all candidate tilings passing | 3.5% | **5.0%** |
| λ of the best passing tiling (median) | 2.09 | 2.08 |

λ, ā and k of the shortest tilings are unchanged (median λ 2.07, IQR 1.67-2.41). Exact-half windows per shortest-tiling w₁: median 0 (IQR 0-1). The corrected gate raises the passing shares by about a third but leaves them low: intermediate and final power conditions remain a real cost for the onion. The depth part under the corrected gate (S2 and S2-flip, separate L1) is running; see below once done.

### 9.1 Depth under the corrected gate (46 words, one level, 2.5-reduced w₁, S2 and S2-flip, separate L1)

Words: the best 2.5-reduced tiling (gate B) of the 47 words whose B-best tiling uses the identity automorphism; 46 ran (one w₀ has no stored certificate). `t024_m1_cert.py ... B`, data `m1_cert_B.json`. |w₁| 71-282 (median 125); 33 of the 46 are also strictly power-free (A), all 46 pass B. Same construction and compression as section 2.

| | S2 | S2-flip control | notes |
|---|---|---|---|
| maxdepth 1 / 2 / 3 | 17 / 27 / 2 | 21 / 23 / 2 | T1 baseline: depth 2 in 2.4% of dataset certificates |
| depth ≥ 2 | 29 of 46 | 25 of 46 | |
| depth above the components' (max 0 or 1) | 34 of 46 | 31 of 46 | bouquet control passed in most cases under both |
| area-like (this certificate's N) | 1 | 1 | the same word, below |
| N_flip (flip cells absorbed) | median 7.5 (1-18) | | the flip control absorbs a median of 7.5 cells per diagram, about 5% |

- **Separate L1** (ρ_min16 over the 16 images; 41 of 46 are L1 with ρ_min16 = 1.0): **5 are not L1** (ρ_min16 0.99 ×3, 0.73, 0.65), i.e. the reducer shortens them in some image. 'Power-free implies L1' was not available here and it matters: with L1 required, 24 words keep S2 depth ≥ 2 and 21 keep flip-control depth ≥ 2.
- **The only area-like word (dataset index 216: |w₁| = 71, N = 131, S2 depth 3, T_deep 0.64, flip control 3 / 0.61) is not L1** (ρ_min16 = 0.73, and not strictly power-free). The deepest L1 word is index 670 (|w₁| = 213, N = 192, depth 3 under S2 and under the flip control, T_deep 0.33, strictly power-free), not area-like.
- The flip control lowers the depth distribution a little (depth ≥ 2: 29 → 25) but does not remove the effect: most of the depth gain does not come from flip cells.
- Cut vertex inside a tile arc under B: 5 of 883 arcs (0.6%).
- Same caveats as section 4 (one level, our certificates after our compression, a selected subset of 46).

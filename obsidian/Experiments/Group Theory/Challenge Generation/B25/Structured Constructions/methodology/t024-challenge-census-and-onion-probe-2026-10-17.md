---
title: t024-challenge-census-and-onion-probe-2026-10-17
hypothesis: "The real challenge words are (nearly) 2.5-power-free, and a one-level 'onion' step (tile a power-free dataset word's boundary with inverse arcs of dataset relators) raises strict depth beyond what its components carry."
status: validated
author: asetlearning
date: 2026-10-17
todo: T-024
project: challenge-gen
instance: B(2,5)
experiment_type: structured-constructions
tags: [agent/exp, user/asetlearning, domain/group-theory, topic/burnside, topic/b25, topic/trivial-words, topic/hard-instance-generation, topic/dehn-function, topic/power-free-words, project/challenge-gen, status/validated, experiment, methodology]
---

# T-024 (draft): challenge power census and the M1 one-level onion probe

## Conclusion (closed by the owner, 2026-10-19)

**T-024 is closed: positive at small depth, negative for depth growth.**
- **Census (§2–3):** the HWW challenges are 2.5-reduced; every 2.5 window is an exact half, almost all of period 2.
- **One onion level raises strict depth (M1, §9):** S2 depth ≥ 2 in 29 of 46 words, with the bouquet control holding.
- **Levels 2 and 3 do not keep raising it for L1 words (§10.3, §10.6):**
  - flip depth rises by +1 in 30–40% of seeds, but mostly on words that fail L1;
  - the registered level-3 verdict is negative in both arms (rises 10% < 25%);
  - the deepest-parent rule is inconclusive;
  - the deepest L1, bouquet-ok word has flip depth 4, the same as level 1.
- **Best candidates:** 11 Validator-confirmed words, 163–1,548 letters, with flip depth 3–4 above their components ([[2026-10-18-t024-level2-best-words-verify]], [[2026-10-18-t024-level3-first-word-verify]]). Their L1 and novelty come from the runs; a re-check is pending.
- **Why it stalls (Math Expert, [[2026-10-19-t024-after-level3-options]]):**
  - each level keeps the shortest gated candidate, and L1 is checked only afterwards (argued);
  - L1 failures track exact halves at tile junctions (argued from the data).
- **Option not taken:** selecting for L1 and depth inside the level step.
- **Spin-offs:** the tcgraph `onion/` component, the linear-time power check (T-026), and the `inverseCellReduce` speed-up (tcgraph PR #9, 100–300× faster, identical output).

**Earlier status line (2026-10-17):** draft, results of two small analyses on existing data. Both were owner-approved on 2026-10-17 (via Lead): the census first, then M1.

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

## 10. Pilot on the C++ backend: pre-registration update and K=64 smoke (2026-10-17, Experimenter)

### 10.1 Pre-registration update (written before the 50-seed run; approved by Lead under the owner's delegation)
Changes to section 6 (nothing else changes: seeds, hypothesis, falsifier, per-level metrics stay as registered):
- **Backend.** `t024_onion_pilot.py ... cpp-junction`: tiles, tiling DP, assembly and measures from `tcgraph_ext.onion` (tcgraph `4390614`, b25 `5fbf9f7`; driver `t024_onion_cpp.py`). Python remains the orchestrator.
- **Junction-aware DP** (beam K = 64, arc length 4-25): every join of two neighbouring tiles must pass the local power filter, so the tiling is no longer blind to junction content (the failure of the Python plain DP, section 8). Noisy re-runs: NOISY = 12 at level 1, NOISY2 = 40 at level 2, noise 3.0, seeded from the pilot's numpy generator (reproducible, not the same draws as the Python backend).
- **Gate.** Headline gate = **2.5-reduced** (gate B in the code: every window an exact half); gate A (strictly power-free) stays a diagnostic. Finals: shortest level-2 candidate passing A / passing B / ungated reference U.
- **L1.** Separate L1 (rho_min16 over the 16 images, L1 iff = 1) for every level-1 parent and every final, in the main process.
- **Pipelines.** Intermediate level: cheap compression; finals: full compression, and the cheap pipeline is also run on each final word, with N, S2 depth and S2-flip depth of both recorded (the cheap-vs-full difference).
- **Metrics per final:** S2 and S2-flip depth, S1/S3 depth, bouquet control (depth above the components' maximum), area-like, novelty, lambda per level, wall time.
- **Falsifier (unchanged), made precise on L1:** no level-2 **L1** word above level 1's maximum depth falsifies "+1 depth per level"; a level-2 word that is not L1 does not count either way (it is reported separately).

### 10.1a Addendum to 10.1: level-1 parent diversity (fixed 2026-10-18, before the 50-seed run; Lead decision under the delegation)
The smoke gave one distinct level-1 tiling per seed (12 noisy re-runs at noise 3), so level 2 was a single shot. The junction DP has no K-best list of whole tilings (its K = 64 is the beam width per position; each call returns the cheapest tiling), so diversity comes from noise. Probe (5 dataset words, level-1 tiling only, distinct boundary words up to cyclic rotation; all of them pass the gate): noise 3 x 12 gives 1-2 (seeds 21, 594, 100, 200, 300: 1, 1, 1, 2, 1); noise 8 x 40 gives 3, 2, 6, 5, 2; noise 20 x 40 gives 9, 12, 8, 8, 5. A level-1 call costs about 2.5 s.
Rule for the pilot, fixed now and not tuned after the run:
- Level-1 parents = up to **3 distinct boundary words** (distinct up to cyclic rotation) from the noiseless tiling + NOISY = 12 re-runs at noise 3 (as registered). If fewer than 3 distinct, **top up** with NOISY_TOP = 40 further re-runs at noise 20; keep the 3 shortest distinct words.
- Level 2 as registered: 13 tilings (noiseless + NOISY2 = 40 at noise 3) of each parent.
- Per seed the result records `level1_distinct_base` (distinct parents before the top-up) and `level1_candidates` (distinct parents after it), and each final's parent.
- Cost estimate: about 30 CPU-hours for 50 seeds (up to 3 parents, 5-25 min each); rjob on 9 CPUs, expected 3.5-5 h wall, timeout 8 h.

### 10.2 Smoke at K = 64 (seeds 21 and 594, level 1 -> 2; files `runs/t024_pilot/smoke_k64.json`)
| Seed | n0 (d0) | level-1 candidates | level-1 parent: len / S2 depth / gate / L1 | level-2 candidates (A / B) | level-2 final (B): len / S2 depth / L1 | time |
|---|---|---|---|---|---|---|
| 21 | 47 (1) | 1 | 174 / 2 / B (1 exact half) / L1 | 0 / 0 | none | 297 s |
| 594 | 82 (1) | 1 | 283 / 2 / B (2 exact halves) / L1 | 2 / 0 (2 pass B) | 611 / 2 / B (3 exact halves) / **not L1 (rho_min16 0.959)** | 1,562 s |

- The junction-aware DP produces level-2 words that pass the corrected gate (seed 594: 2 of 2 candidates), which the plain DP never did (section 8). Seed 21 yields no level-2 candidate.
- Level 1 gains depth (d0 = 1 -> 2, bouquet control passed, L1). Level 2 does not: S2 depth stays 2 (= the parent's), the bouquet control fails (depth not above the components' maximum 2), and the word is not L1 (the 2.5 reducer shortens it by 4%). S2-flip depth 2 (43 flip cells). Cheap vs full on the final: N 876 vs 854, S2 depth 2 vs 2, flip depth 2 vs 2.
- Only one distinct tiling per seed at level 1 (so one parent, not three): the junction-aware DP with 12 noisy re-runs finds few distinct tilings.
- Cost: 5 min and 26 min for one seed each on one CPU; a 50-seed run is about 12 CPU-hours, so it needs an rjob.

### 10.3 Pilot results (rjob 20261018-000601-9e5902; b25 `90bc1cb`, tcgraph `4390614`; 50 seeds, 9 processes, 3.0 h wall, 20.9 CPU-h; files `runs/pilot_cpp/outputs/pilot_50.json`, `analysis.txt`, `analysis2.txt`; Experimenter, 2026-10-18)
All numbers are under the corrected gate (2.5-reduced = gate B; gate A = strictly power-free, diagnostic), L0 passed for every word, L1 = rho_min16 = 1. S2 = strict depth; flip = S2-flip control; bouquet ok = depth above the components' maximum.

**Level 1.** d0 (the seed's own S2 depth) is 0 for 27 seeds and 1 for 23. Distinct parents before the top-up: 1 for 25 seeds, 2 for 11, 3 for 11, 4 for 3; after the top-up 49 seeds have at least 3 candidates and one seed has only 1. 148 parents (3 per seed, one seed 1): S2 depth 1 / 2 / 3 / 4 = 41 / 95 / 11 / 1; 146 pass B and 92 pass A; 115 are L1 (L1 parents by depth 1 / 2 / 3 / 4 = 31 / 75 / 8 / 1); bouquet ok 112; lambda median 2.76. Flip control on parents: depth 1 / 2 / 3 = 56 / 82 / 10. The largest level-1 depth in the pilot is **4**, by one parent (seed 594, L1).

**Level 2.** Every one of the 50 seeds has level-2 candidates (497 in all; 50 seeds with a candidate passing B, 40 passing A). Finals (shortest candidate passing the gate; U = ungated reference):

| Final | seeds | S2 depth 2 / 3 / 4 | flip depth 1 / 2 / 3 | L1 | L1 and bouquet ok | area-like | lambda median |
|---|---|---|---|---|---|---|---|
| B (headline) | 50 | 31 / 16 / 3 | 1 / 38 / 11 | 32 | 17 | 0 | 1.78 |
| A (strictly power-free) | 40 | 30 / 8 / 2 | 2 / 33 / 5 | 40 | 22 | 0 | 1.83 |
| U | 50 | 34 / 13 / 3 | 2 / 39 / 9 | 43 | 24 | 0 | 1.87 |

- **Paired against the own parent (final depth vs its parent's depth).** B: mean 2.44 vs 1.72 (difference +0.72); 29 of 50 finals above their parent, 21 equal, 0 below. A: +0.52 (22 above, 16 equal, 2 below). Restricted to L1 finals with the bouquet control passed: B 17 of 17 above their parent (mean 2.65 vs 1.35), A 22 of 22 (2.41 vs 1.36).
- **L1 finals with bouquet ok, by (S2 depth, flip depth):** B: (2,1) 1, (2,2) 7, (3,2) 6, (3,3) 1, (4,3) 2; A: (2,1) 2, (2,2) 12, (3,2) 5, (3,3) 2, (4,3) 1. The flip control lowers depth by at most one and never removes the gain.
- **Not L1:** B finals 18 of 50 (many with rho_min16 0.99-1.0, a few 0.7-0.9); all 40 A finals are L1.
- **Cheap vs full pipeline on the finals:** B: S2 depth differs for 6 of 50 words, flip depth for 7; N(cheap) is about 4% larger than N(full) at the median (full / cheap 0.957), at most 186 cells apart; A: 4 and 5 of 40 (median 0.949); U: 6 and 7 (0.956). So the cheap pipeline in the loop is a good proxy but changes the depth of about one word in eight.

**Registered tests (section 6, and 10.1 on L1 words).**
- H-L2, first clause (mean level-2 final exceeds the mean of its parents by at least 0.5): B +0.72, A +0.52, U +0.58: **met** (A only just).
- H-L2, second clause and the **falsifier** (a level-2 final above the largest level-1 depth in the pilot): the largest level-2 depth is 4 (B: 3 finals, 2 of them L1 with bouquet ok; A: 2 finals, 1 L1 with bouquet ok), the largest level-1 depth is also 4 (one parent). **Nothing is above it, so the registered falsifier is met and the second clause fails.** The same holds on L1 words (level-2 L1 maximum 4, level-1 L1 maximum 4). The registered comparison uses one extreme parent (seed 594), which sets the level-1 maximum; against the typical parent the gain is the paired one above.
- Failure modes: at least 10 seeds with an A final: **no failure** (40); bouquet control failing for most finals: B 21 of 50 fail, A 18 of 40 fail, so most pass; a depth claim needs the bouquet control, as Lead requires.

**Reading.** A second level raises the typical depth by about 0.5-0.7 (the shortest gated candidate, paired with its parent), and reaches 3-4 on 19 (B) / 10 (A) of the seeds (of which L1 with bouquet ok: 9 and 8), in L1 words that pass the bouquet and flip controls; but it does not exceed the single deepest level-1 parent (4), so by the pre-registered criterion the hypothesis "+1 per level" is **not supported at the maximum** and only partly at the mean. No word is area-like. Depths are for our certificates after our compression, not minimal fillings.

### 10.4 Pre-registration: level-3 pilot and the deepest-parent rule (written 2026-10-18, before any run of it; Experimenter; for Lead's approval; owner approved the pilot and the rule)
Depth below means S2 strict depth and its S2-flip control (rule (d), the tcgraph default after `0842fde`); "flip depth" is the headline. Gate = 2.5-reduced (gate B); A = strictly power-free is a diagnostic. L1 = rho_min16 = 1. Bouquet ok = depth above the maximum of the components' depths.

**Arms (paired on the same seeds).** Level 1 and level 2 follow 10.1/10.1a (up to 3 distinct level-1 parents per seed, 41 tilings of each; per parent the shortest gate-B level-2 candidate is a *chain candidate*; each chain candidate is measured in full: flip depth, L1, bouquet).
- **S (shortest parent):** level-2 final = the shortest chain candidate of the seed (the pilot's B final).
- **D (deepest parent):** level-2 final = the chain candidate that is L1 and bouquet ok with the largest flip depth (ties: larger S2 depth, then shorter word). A seed with no L1 and bouquet-ok chain candidate has no D arm (counted, and left out of the S-vs-D comparison; arm S is still run).
- **Level 3** from each arm's level-2 final: 41 tilings (noiseless + NOISY2 = 40 at noise 3), shortest gate-B candidate = level-3 final, full pipeline, same measures. If S and D choose the same word, level 3 is run once and used for both arms.
- Seeds: the first 20 of the 50 pilot seeds (`random.Random(2417).sample(sorted certified ids, 50)[:20]`), fixed now.

**Paired quantities (per seed and arm).** gain = flip depth of the level-3 final minus flip depth of its own level-2 parent. A seed is a **rise** only if gain >= 1 and the level-3 final is L1 and bouquet ok (conservative: a non-L1 or bouquet-failing final is not a rise). A **fall** is gain < 0 of any final. Seeds without a level-3 candidate are *no-result* and count as not rising (not dropped).

**Registered test of "depth keeps growing at level 3" (arm D, headline; arm S reported the same way).** Reference: level 2 had 58% of seeds above their parent, mean gain +0.72 (10.3).
- **Positive:** rises in >= 40% of the seeds, falls in <= 10%, mean gain >= +0.5.
- **Negative (depth saturates):** rises in < 25% of the seeds, or mean gain < +0.25.
- Anything in between is *inconclusive* and reported as such, not rounded up. The level-1 maximum 4 is not used as a threshold (10.3: it rests on one parent); the maximum is reported: the number of L1 and bouquet-ok level-3 words with flip depth >= 5.
- Pass criteria for the run itself: >= 60% of the seeds give a level-3 final in arm S; otherwise the run is *unfinished* (cause: the exact filter at the chosen K, below), not negative.

**Registered test of the deepest-parent rule (D vs S, on the seeds with both arms).** Per seed, level-3 flip depth of D minus S; ties are dropped. The rule is *adopted* if D wins more seeds than it loses (exact one-sided sign test p < 0.10) and mean(D - S) >= +0.3; *rejected* if it loses at least as often as it wins; otherwise inconclusive. Also reported: D's and S's gains separately, since D picks parents by level-2 depth, so part of D's level-3 depth is inherited. A D arm with higher level-3 depth but no larger gain is *not* evidence for the rule beyond inheritance, and is reported that way.

**Filter and K (measured, 2026-10-18; tcgraph main `ca2ceb9` built in a separate worktree; one DP call, noiseless, one core; same words with tcgraph `4390614` for reference).**
| Word (dataset seed, level of input word, length) | `4390614`, K=64 | `ca2ceb9` K=16 | K=64 | K=128 | K=256 |
|---|---|---|---|---|---|
| 519, level 1 (75) | 3.9 s | n.a. | 26.6 s (same tiling) | n.a. | n.a. |
| 519, level 2 (185) | 11.6 s, 1 candidate | 3.4 s, none | 43 s, **none** | 134 s, **none** | 341 s, 1 candidate |
| 519, level 3 (436) | 20.3 s, 1 | 30.9 s, 1 | killed by the 3 GB cap while running K=256; K=64 not obtained | | |
| 594, level 2 (282) | 17.3 s, 1 | 19.9 s, 1 | n.a. | n.a. | n.a. |
| 594, level 3 (466) | 30.7 s, 1 | 28.2 s, **none** | n.a. | | |
The exact filter keeps up to K/8 states that carry a recorded power violation (K=64: 8), so the beam loses candidates the old filter found; the cost at equal K is 7x (level 1) to 4x (level 2) and grows steeply with K (K=256 at level 2: 30x). The yield is patchy: K=16 finds a level-2 tiling for 594 but not for 519, and a level-3 tiling for 519 but not for 594; K=64 did not finish in 2 h per seed in the Developer's replay (Lead), and seed 21 has no level-2 tiling at K=16. This agrees with Lead's note: the exact filter changes which words are found.
- **K choice: K = 16** with the number of noisy re-runs raised to compensate for the lost yield: level 2 and level 3 use NOISY2 = 40 (41 tilings per word, noise 3), as at level 2 of the 50-seed pilot. K=16 is the only setting whose per-call time (3-30 s) is the same order as the pilot's. Not tuned after the run. If fewer than 60% of seeds reach a level-3 final, the run is declared unfinished and K=32 is proposed in a new plan, not rerun silently.
- Seeds that gave no level-2 or level-3 tiling are *no-result* (see above); the number of them is a result, because it measures the incompleteness of the beam with the exact filter.

**Cost estimate.** Per seed, one core: level 1 (13 calls, ~3 s) ~1 min; level 2, 41 calls per parent x 3 parents x ~10 s ~20 min; chain measures (3 full compressions, ~2-3 min each) ~8 min; level 3, 41 calls x ~30 s ~20 min for each of the two arms (shared if the same word) => ~40 min; final measures and L1 ~10 min. First estimate: about 80 min per seed. **Corrected after the mechanics smoke (seed 594, K=16, only 2 + 3 noisy re-runs): stage 1 alone took 56 min, mostly the level-1 top-up (40 re-runs at noise 20, ~50 s per call with the exact filter; the base 13 tilings gave 0 distinct parents for this seed), so a seed costs ~2 h (range 1-3 h): level 1 + top-up ~40 min, level 2 ~30 min (3 parents x 41 calls), level 3 ~20 min per arm, measures ~10 min. 20 seeds ~40 CPU-hours; on 9 processes ~4.5-5 h wall (range 3-7 h; the timeout stays 8 h).** The timing job measures all of this per phase (`sec_l1`, `sec_top`, `sec_tilings` per chain and level). The 2-seed timing above is for single DP calls only, because a full seed at K=16 was not run locally (the machine has 5 GB and the cap killed K=256 at level 3). The first rjob step is therefore a timed run of 2 seeds (519, 594) with the final script, as a part of the same job (its per-seed times are in the log; the 20-seed job is not cancelled by them; if the first 2 seeds take > 3 h each the run is stopped and re-planned).
- **rjob plan (for Lead's approval):** Mac host, 9 CPUs, 12 GB, timeout 8 h; job file `experiments/challenge_gen/t018/jobs/t024_pilot3.toml` (new, repo-relative paths only, tcgraph pinned to `ca2ceb9`, code path = the commit Lead makes); run script `experiments/challenge_gen/t018/run_t024_pilot3.sh`; driver `experiments/challenge_gen/t018/scripts/t024_onion_pilot.py` extended with `--levels 3`, the arm switch and the certificate dump (below). Inputs through `[data]` as in `t024_pilot.toml`.
- **Output paths** (relative to the job output directory, copied to the vault only as summaries): `output/pilot3_20.json` (rows), `output/pilot3_20.log`, `output/certs/ds<seed>_L<level>_<arm>_<gate>.json.gz` (certificates), `output/certs/index.json` (word, length, sha256 of each file, arm, level, gate, depth, L1). Local analysis only in `runs/pilot3/` (not committed).

**Certificate dump (Lead's note; part of the code to be reviewed).** The pilot script gets the option `T024_DUMP_CERTS=<dir>` (default off in smoke runs, **on** in the rjob). For every final it reports (level-2 chain candidates and finals, level-3 finals, gates A and B only; the U reference is not stored) it writes the word, the **assembled cells** (before compression) and the **compressed cells** (after the full pipeline), each as a list of (relator index, conjugator) pairs with the table identifier, in a gzip JSON file named above, plus `index.json`. A verification step in the script re-expands both cell lists over the core table and checks that they give the word (the L0 check, run on the stored lists, not on the in-memory objects) before the file is written. Size (measured on the mechanics smoke, seed 594, K=16, 2 level-2 chain candidates): a level-2 word of 353-410 letters has 860-1,023 compressed and 880-1,033 assembled cells, 0.93-1.12 MB as JSON and 17-21 KB gzipped (the first estimate, 2 MB gzipped per word, was ~100x too high). A level-3 word has about twice the cells => ~40-50 KB gzipped. Per seed: up to 3 chain candidates + up to 2 arms x 2 gates of level 3 => ~7 words => **~0.2 MB gzipped, ~15 MB raw per seed; 20 seeds ~4 MB gzipped, ~300 MB raw before gzip** (only the gzipped files are written). The timing job reports the measured total. The files are job outputs, not committed to the repo; the Validator reads them from the job output, not by replaying the search (the 12-seed replay of the 50-seed pilot, ~5 CPU-hours, is what this avoids). The 50-seed pilot_50.json has no certificates and can be verified only by replaying the search.

**10.4 as approved (Lead, 2026-10-18, under the owner's delegation): sequence and base.** Approved unchanged: arms S/D paired on seeds 1-20, rule (d), the thresholds, the 'unfinished' rule, K=16 with NOISY2=40, the certificate dump. Added:
1. **Two jobs, in this order.** (a) *Timing job:* seeds 519 and 594 only (`ds:519,594`, 2 processes because the Mac is busy), same script, K=16, NOISY2=40, dump on. Reports per-seed wall time, yield (number of seeds with a level-2 chain candidate and with a level-3 final, per arm and per gate) and the **measured dump size** per stored word and per seed. (b) *20-seed job:* only after Lead approves the timing report; its cost estimate and wall time are then recomputed from (a).
2. **Parents are recomputed.** Levels 1 and 2 are recomputed with tcgraph `ca2ceb9` and its exact junction filter, with K=16. The level-1 and level-2 words of this run are therefore **not** the words of `pilot_50.json` (section 10.3, junction filter of `4390614`, K=64); they are new words with their own certificates. The Validator's replay in progress certifies the `pilot_50.json` words and says nothing about the words of this run; the certificate dump is what makes these verifiable without a replay.
3. **Code base:** b25 `t018-diagram-search` at `550c635` (tcgraph pin `ca2ceb9`, `experiments/challenge_gen/inputs.py`); the job maps `[data]` like the committed jobs (`../../../../data/inputs/<name>`, names from `data/inputs/README.md`). Code for review: new `t024_onion_pilot3.py` (stage 1: levels 1-2 and chain candidates; arms S and D chosen in the main process after the L1 check; stage 2: level 3 per distinct chain candidate; dump), `T024_K` in `t024_onion_pilot.py`, `run_t024_pilot3.sh`, `jobs/t024_pilot3_timing.toml` (and, after the timing report, `jobs/t024_pilot3.toml`). The level-3 run is a separate script instead of a `--levels` flag, so the committed level-2 pilot script keeps its behaviour.

### 10.5 Timing job result (rjob 20261018-130149-66017e; b25 `34883b1`, tcgraph `ca2ceb9`; seeds 519 and 594; K = 16, NOISY2 = 40; 2 processes; wall 1 h 57 min; files `runs/20261018-130149-66017e/outputs/pilot3.json`, `certs/`; Experimenter, 2026-10-18)
Not a result about depth growth (two seeds); a timing and mechanics report for the 20-seed job.

| Seed | level-1 parents (distinct base / used) | level-1 s (`sec_l1`) / top-up s | level-2 chain candidates | level-2 tilings s per parent | stage 1 s | arms S / D | level-3 tilings s | level-3 full measure s | level-3 finals |
|---|---|---|---|---|---|---|---|---|---|
| 519 | 4 / 3 | 54 / 0 | 2 of 3 parents (parent 0: none) | 108 (none), 548, 474 | 1,518 | chain 2 / chain 2 (same word) | 1,132 | 2,872 | B: 1,548 letters, S2 3, flip 3, L1, bouquet ok; parent flip 2: **rise (+1)**; A: none |
| 594 | 0 / 2 | 21 / 63 | 2 of 2 | 846, 919 | 2,624 | chain 0 (not L1) / chain 1 (L1) | 533 and 862 | none | none (0 candidates for both chains, 41 tilings each) |

- **Per-seed cost** (one core): seed 519 5,522 s (92 min), seed 594 4,019 s (67 min): mean ~80 min, as in the first estimate of 10.4; the level-1 top-up is cheap (0-63 s), the cost is the level-2 and level-3 tilings (110-1,130 s per word) and the full measure of the level-3 final (2,872 s for 1,548 letters and 1,871 cells, 48 min). The two level-2 full measures plus the three cheap parent measures take 334 s (519) and 775 s (594). The full-measure cost grows steeply with N (Developer: N^4), so the long tail is the level-3 finals of 2,000+ cells.
- **Yield (this sample):** level-2 chain candidates 4 of 5 parents; level-3 final for 1 of 2 seeds in both arms (gate B; gate A none). The pre-registered 60% rule cannot be judged on two seeds (50%).
- **Arms:** seed 519: S and D choose the same word (chain 2: shorter and L1, bouquet ok), one level-3 run; seed 594: S = chain 0 (636 letters, not L1) and D = chain 1 (645 letters, L1), both depth 3 / flip 3 at level 2, neither has a level-3 tiling at K = 16.
- **Dump (measured):** 5 stored words = 113,573 bytes gzipped, 6.1 MB raw; level-2 words 10.7-19.5 KB gz (0.47-1.06 MB raw, 546-960 cells), the level-3 word 53.6 KB gz (3.07 MB raw, 1,871 assembled / 1,863 compressed cells). L0 re-expansion passed on every stored list. About 57 KB gz per seed here, at most ~120 KB per seed when S and D differ: 20 seeds **~1-2.5 MB gz, ~60-120 MB raw**.
- **Projection for 20 seeds:** ~27 CPU-hours (mean 80 min per seed), 9 processes ~3-3.5 h if no word needs more than ~1.5 h, and up to 5 h with a few 2,000+ cell level-3 finals; timeout 8 h unchanged.

### 10.6 Level-3 pilot: registered verdicts (rjob 20261018-151032-cc4567 timed out at 8 h with 22 of 24 level-3 tasks finished; the 2 missing tasks, seed 580 chain 2 and seed 767 chain 2, were completed by rjob 20261018-231404-2a1be5; b25 `fb2c82c` / `eaefa69`, tcgraph `ca2ceb9`, K = 16, NOISY2 = 40; Experimenter, 2026-10-19)
The first job wrote `pilot3.json` only at the end, so the rows were rebuilt from the log and the certificate dumps (`runs/pilot3/rebuild.py`, 64 + 2 certificates; log and dump depths agree on every final); the completion job reproduces the original task (checked on seed 212 chain 0: identical certificate). **Every row uses the tile-depth bound for the bouquet control** (bouquet ok iff S2 of the final > max(parent S2, 2); the tile table has 906 tiles x 2 offsets with strict depth 0/1/2 = 954/848/10). The bound is a sufficient condition: using the exact component maximum cannot remove a rise, and for no finished final with gain >= 1, L1 and S2 > parent S2 does the bound fail, so the number of rises that change with the exact maximum is **0**. Rise = gain >= 1 (flip depth of the level-3 final minus its level-2 parent's) and L1 and bouquet ok. 24 level-3 tasks over 20 seeds; seeds without a level-3 final count as gain 0 and not rising.

| | arm S (shortest chain candidate) | arm D (deepest L1 bouquet-ok chain candidate) |
|---|---|---|
| seeds with the arm | 20 | 11 (9 seeds have no L1 bouquet-ok chain word) |
| level-3 final (gate B) | 13 of 20 (65%) | 9 of 20 (45%) |
| gains (flip) | 0 x5, +1 x7, +2 x1; no falls | 0 x3, +1 x6; no falls |
| rises (gain >= 1, L1, bouquet ok) | **2 of 20 (10%)**: seed 519 (2 -> 3), seed 476 (2 -> 3) | **2 of 20 (10%)**: seed 519 (2 -> 3), seed 160 (3 -> 4) |
| mean gain over 20 seeds (no result = 0) | +0.45 | +0.30 |
| registered branch | **negative** (rises 10% < 25%; mean +0.45 is not < +0.25) | **negative** (rises 10% < 25%; mean +0.30 is not < +0.25) |

- **Registered verdict (arm D, headline; arm S the same): negative, through the first condition (rises < 25%).** The mean-gain condition (< +0.25) does not hold in either arm (+0.45, +0.30), so the rule decides by the rises alone. The conservative rule (a rise needs L1 and bouquet ok) is what keeps rises at 10%.
- **Unfinished rule:** arm S has a level-3 final in 13 of 20 seeds = 65% >= 60%: the run counts as **finished** (K = 16 loses candidates, but not enough to trigger the rule).
- **S vs D:** the arms use different words in 4 seeds; 368 and 160 have a final only in D (S has none), so the paired comparison (both arms with a final, different words) has **2 usable seeds**: 434 (D 3 vs S 2, D wins) and 580 (3 vs 3, tie): 1 win, 0 losses, 1 tie; sign test p = 0.5. **The deepest-parent rule: inconclusive** (not adopted, not rejected). Seeds 368 and 160 are where D reaches level 3 and S does not; this is a descriptive observation, not a test.
- **Descriptive, unregistered:** gains >= 1 ignoring L1 and bouquet: S 8 of 20 (40%), D 6 of 20 (30%) (including the +2 gain of seed 767 chain 2, flip 2 -> 4, 1,498 letters, not L1). The deepest L1 bouquet-ok level-3 word has flip depth **4** (seed 160, arm D, 811 letters, parent flip 3); no L1 bouquet-ok level-3 word has depth >= 5. Level-3 words of depth 4 that are not L1: seeds 512 (860 letters, parent 3->4) and 767 (1,498 letters, 2->4).
- **Cost:** the first job 8 h on 9 processes (22 tasks), the completion job 11.4 h wall on 2 processes (580 chain 2: 20,349 s, 767 chain 2: 40,484 s); the level-3 full measure of 1,100-1,500 letter finals takes 3-11 h.
- **Reading.** At level 3 the typical rise is +1 flip depth in about 30-40% of the seeds, but only 10% of the seeds give a rise that is also L1 and bouquet ok, and the only new maximum is one word of depth 4 (the level-1 maximum was also 4). With the registered rule the hypothesis that depth keeps growing at level 3 is **not supported** (negative branch); depth for our certificates after our compression, not minimal fillings.

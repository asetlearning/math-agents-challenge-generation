---
title: "Axplorer v1 Representation Gate — Phase A Empirical Grounding (B(2,5) corpus/rule/BPE/trace/syllable)"
date: 2026-07-17
domain: group-theory
project: b25
instance: b25-loop-v1
experiment_type: patternboost
author: maumayma
authors:
  - B25 Experimenter
status: pending
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/patternboost, topic/tokenization, topic/representation, project/b25, status/pending, data]
---

# Axplorer v1 Representation Gate — Phase A Empirical Grounding

**Scope:** B0(2,5), raw alphabet `{a,A,b,B}`. Offline analysis only — pure-Python corpus stats,
no kbprog / no heavy jobs / no pipeline code changes. Grounds the transformer-representation
choice for axplorer v1 (see repo `experiments/burnside/b25_patternboost/AXPLORER_REPRESENTATION_NOTES.md`).

**Inputs (literal):**
- Seed corpus: `runs/b25/patternboost_seeds/20260630_round2/seed_words.txt` — 345 raw firing windows
  (windowed slices of 2 anchors `01_after_power` + `word_coreless`, all braid Δ>0).
- Target word: `experiments/burnside/burnside_bidirectional/runs/comm_13_10_compress/comm_13_10_raw.txt`
  — 1348 chars (loop.py:69 still targets this full word).
- Rule bank: `experiments/burnside/b25/fragment_seed_rules/b25_seed_rules_2026-06-25.{json,kbprog}`
  — 31 GAP-verified junction rules.
- Reducer: `experiments/burnside/burnside_bidirectional/src/bin/braid_reduce.rs` (+ `src/reduce/braid.rs`).
- Scripts: `scratchpad/axplorer_repr_analysis.py`, `axplorer_bpe_align.py` (provenance in output capture
  [[axplorer-representation-grounding-2026-07-17|Agents/Experimenter-B25/output]]).

> **Provenance triple.** Data: the 4 input files above. Method: pure-Python `Counter`/run-length/greedy-BPE,
> no randomness. Code: two scratchpad scripts (deterministic; re-run reproduces every number here).

---

## TL;DR — what the data says about representation

1. **Fixed k-mer / block packing is algebraically misaligned by construction.** Rule-LHS edit
   fragments have lengths `{5,6,8,9,10,11,12}` — **none divisible by 4**, most odd. So a fixed
   k=4 block packing straddles a token boundary on **100%** of fragment firing sites; k=2 straddles
   53–100%; braid runs ≥6 straddle 72–100% for every k∈{2..6}. This is a **structural** result
   (depends only on motif lengths vs k), not a corpus artifact. **→ Fixed k-mer packing has real
   algebraic cost.**
2. **Greedy BPE does NOT recover the edit motifs — confirmed de-biased (Task 4b).** On the diverse 12k
   held-out pool: **0/21** rule fragments learned as tokens at every vocab; BPE token boundaries **cut
   42–72%** of rule-fragment firing sites (41.8% at vocab 1024). BPE aligns to frequency (`ab`,`aa`,`Ab`,
   `aaaab`), not algebra — **not meaningfully better-aligned than fixed k-mer.** Only char-level has 0%
   misalignment. (The original seed-corpus BPE was degenerate — mean 6 tokens/word swallowing whole
   windows; Task 4b re-ran on non-degenerate data per Lead GO and the conclusion held.)
3. **Syllable (run-length) factoring barely shrinks T on the real target.** g^k syllable compression:
   **1.43×** on seed windows but only **1.06×** on `comm_13_10_raw` (it's near-fully alternating,
   power-runs mostly length 1). A factored encoding therefore bounds T-reduction at ~6% for the actual
   loop target — not worth the machinery on its own.
4. **A sequence-of-reductions (moves) encoding is *partially* supported today.** `braid_reduce.rs`
   already has `--trace-file` + `reduce_leftmost_traced` logging `(step,stage,lhs,rhs,pos,len_before,
   len_after,delta,direction)` per rule application — but **only the leftmost stage**. Braid shortenings,
   multi-start, and **beam search (the bulk of hard-word reduction) are untraced**. A full moves encoding
   needs trace hooks in those stages + a stable rule-ID (currently rules logged by string).
5. **`comm_13_10_raw` cannot braid-fire directly** (max alternating run = 5 < 6). Confirms the
   round-2 finding that naive commutator powers are blind seeds; the firing signal lives in the
   coreless/after-power anchors, which is why the seed corpus is built from *those*, not comm itself.

**Representation recommendation (for the verdict, not binding):** char-level as the safe default;
if T-reduction is required, prefer **data-driven BPE tuned + validated on the held-out pool** over
fixed k-mer (which is provably misaligned). Window the target (256–1024 firing windows already exist)
as an orthogonal T-lever. Syllable factoring and moves-encoding are not v1-ready (weak on target /
missing trace infra respectively).

---

## Deep Round 2 — three empirical probes (Lead request 2026-07-17, offline)

Maria wanted deeper evidence before locking char-level. Three probes, all offline (pure-Python /
free-reduce / tiny-CPU-model; NO braid_reduce GO test, NO kbprog, no pipeline changes). Raw:
`Agents/.../output/axplorer-r2-P{1,2,3}-*-2026-07-17.json`; scripts `p1_tgrowth.py`,
`p2_delim_bpe.py`, `p3_nope_probe.py`.

### P1 — T-growth under grow-to-shrink expansion (the key stress-test)

Char-level's cost argument rested on "candidates are short (T≈333)". But the method's premise is
grow-to-shrink, so: does an expanding search trajectory blow past MAX_LEN? Simulated R2 §7 enabler
moves (modeled as **partial-relator completions** — extend a partial power-run `g^k` or alternating
run `(gh)^k` toward the exponent-5 relator, Δ≤+4, then free+braid/power cleanup), tracking **every
intermediate word length** (post-expansion, pre-cleanup). Sample: 345 seed + 2000 held-out.

| config | n | peak-over-start (max / mean / p95) | peak T (mean / p95 / max) | paths > 1024 | paths > 1536 |
|---|--:|---|---|--:|--:|
| **§7-capped** (Δ≤+4, temp ≤+8 above path start, immediate cleanup) — seed | 345 | 3 / 2.1 / 3 | 371 / 915 / **925** | **0** | **0** |
| **§7-capped** — held-out | 2000 | 3 / 2.5 / 3 | 291 / 525 / **921** | **0** | **0** |
| **uncapped stacking** (cap removed) — worst held word | 1 | grows linearly | 10 apps→910, 100→1060, **200→1344, 400→2144** | — | yes @≥~250 apps |

**Result:** with §7 caps honored, peak T never exceeds start+3 in practice (bounded by start+8 by
construction); **zero paths exceed 1024 or 1536**, worst peak 925 (from the longest seed). For the
1348-char comm target the structural bound gives peak ≤ 1356 < 1536. **Char-level's cost argument
SURVIVES the expansion premise** — grow-to-shrink cannot breach MAX_LEN for any word in the working
set. The uncapped demo shows the §7 +8-cap is **load-bearing**: without it, adversarial stacking grows
~linearly and passes 1536 by ~250 applications. (Implication: v1 must enforce the §7 cap in the search
layer, which the pre-reg already specifies.)

### P2 — rule-boundary-delimited BPE (does delimiting rescue alignment?)

Re-ran the held-out BPE test but first inserted a delimiter `|` at every rule-LHS occurrence boundary
(start+end of each of the 21 short frags), forbidding merges across delimiters, then trained BPE.

| vocab | frags-as-token (delimited) | vs undelimited baseline | site-cut (delimited) | vs baseline |
|--:|--:|--:|--:|--:|
| 64 | **3/21** | 0/21 | 49.6% | 71.9% |
| 256 | **6/21** | 0/21 | 45.3% | 54.8% |
| 1024 | **13/21** | 0/21 | 42.9% | 41.8% |

**Result:** delimiting **substantially rescues** fragment-as-token alignment — from **0/21 to 13/21**
at vocab 1024, and cuts the boundary-cut rate by ~22 pts at vocab 64. So **rule-aware-delimited-BPE
re-enters the slate** as the one BPE variant that respects the algebra. **Cost/caveat (real):** the
tokenizer becomes **rule-bank-dependent** — it must know the current fragment set to delimit, and must
be recomputed whenever the rule bank changes (the bank evolves every PatternBoost round). That couples
the DataPoint tokenizer to a live, changing rule bank — an API-surface + reproducibility cost the
verdict must weigh against char-level's zero-dependency simplicity. Even rescued, 8/21 frags still
split and 43% of sites are internally cut at vocab 1024.

### P3 — NoPE vs learned-absolute PE (length generalization) — INCONCLUSIVE, harness stubbed

Attempted the first direct test on our task of Researcher's highest-evidence claim (learned-absolute PE
hurts length generalization; NoPE/relative helps). Task: per-position tag = motif fires here; train on
words ≤128, test on 256–512; tiny transformer (d=64), learned-absolute vs NoPE.

**Outcome: no trustworthy baseline within the offline tiny-model budget** (4 configs tried). Two design
issues surfaced and were partly corrected:
1. **A bidirectional encoder with NoPE is permutation-invariant** ⇒ structurally *cannot* read an
   ordered motif — a degenerate/unfair NoPE test. Fixed by switching to a **causal** (decoder-style)
   mask so NoPE gets implicit order (as real NoPE LMs do), labeling the motif's END position.
2. **Multi-pattern (21 variable-length frags) detection did not fit** a d=64/2-layer model; reduced to
   single-motif detection to isolate the positional variable.

Even after fixes (causal, 3 layers, single motif, class-weighted loss), **train F1 peaked at ~0.61
(learned-abs) / 0.26 (NoPE)** — below the ≥0.9 baseline gate needed to trust any length-generalization
comparison. A weak **directional hint** (not decision-grade): learned-abs fit train better but retained
only ~41% of its F1 at test-length 512, vs NoPE ~62% relative retention — consistent-in-sign with the
literature claim, but NoPE's absolute F1 is too low (underfit) to conclude anything.

**Stubbed corrected harness (for a proper follow-up, ~10–20 min CPU or a short GPU slice):** use the
actual GPT from `transformer.py` (causal, the real v1 model) rather than a toy encoder; single-motif →
multi-motif curriculum; compare **learned-absolute vs NoPE vs relative/RoPE**; gate on train-F1 ≥ 0.9
before reading test-length F1; report per-position F1 by length bucket + calibration. **Recommendation:**
do not weight P3 in the v1 verdict — the PE choice (learned-abs vs NoPE/relative) is better decided by
(a) the literature (HIGH evidence, already in Lead's verdict) and (b) this stubbed harness run properly,
not by these underfit numbers. The orthogonal PE swap Lead already proposed (drop learned-absolute for
NoPE/relative) stands on the literature independent of P3.

**Deep Round 2 net:** P1 removes the last cost-side objection to char-level (expansion stays under
MAX_LEN with §7 caps). P2 promotes exactly one compression variant — rule-aware-delimited-BPE — back
onto the slate, at the cost of a rule-bank-coupled tokenizer. P3 is inconclusive; the PE decision rests
on literature + a corrected future run, not on this probe.

### P4 — directional blindness + id-augmentation label validity (the scoring-redesign backbone)

Empirically tests the central Deep-Round-2 claim (so far only asserted by Math-expert + reasoned by
Validator): **braid_reduce is flat on grow-from-identity blind-class words, while construction-depth
gives real gradient there.** Method (offline, pure-Python `free+power+braid` = `datapoint.py` logic):
grow words from identity as **products of conjugated relators** `c·u⁵·c⁻¹` — each fifth-power is in the
normal closure, so the whole word **= e in B0(2,5) BY CONSTRUCTION** with a **known depth N** (# relators,
a reducer-independent label). Vary the conjugated subword `u` to control multi-letter content; 240 words
per class, N∈{1,2,4,8,16,32}.

| `u` class | example relator | reducer ratio (mean / median) | **blind fraction** (ratio<0.02) | corr(ratio, depth N) |
|---|---|--:|--:|--:|
| single-letter `u⁵` (power run) | `aaaaa` | 0.996 / 1.00 | **0.4%** | 0.04 |
| alternating-2 `(u)⁵` (alt run) | `ababababab` | 0.996 / 1.00 | **0.4%** | 0.05 |
| **period-≥3 / non-alt** (`(aba)⁵`-type) | `abaabaabaabaaba` | **0.014 / 0.00** | **76.7%** | **0.13** |

**Result — claim confirmed.** Blindness rises sharply with multi-letter non-alternating `w` content:
0.4% → 0.4% → **76.7%**. The reducer collapses pure power/alternating relators to ~identity (ratio ~1.0)
but is **flat (median ratio 0.0)** on the `(aba)⁵`-type blind class, despite every word being `= e`. On
that blind class the reducer ratio carries **no gradient** (corr with depth N = 0.13 ≈ noise), while the
**construction-depth N spans [1,32] and inserted-length [15,560]** — a wide, known, reducer-independent
signal *exactly where the reducer is blind*.

Concrete blind example: a depth-**N=32** word (600 chars) reduces only 600→596 (ratio **0.007**), abel
(0,0), `= e` by construction — the reducer says "irreducible", but its distance is known. Canonical:
`(aba)⁵ = abaabaabaabaaba` (15 chars) → reducer 15→15, **ratio 0.0**.

**Sanity / soundness.** All 720 constructed words have abelianization (0,0); `= e` is **construction-
certified** (product of conjugates of fifth-powers ∈ normal closure — a theorem, not a computation), so
**no GAP is needed** to trust the label. **Honest caveat:** depth N is an **upper bound** on the true
B0 distance / Dehn area (a word may have a shorter certificate), so id-augmentation yields a `distance ≤ N`
training signal, not the exact geodesic — but it is nonzero and monotone-ish exactly where the reducer
gives zero, which is the whole point.

**Implication for the R2 scoring redesign:** id-augmentation (grow-from-identity, known-depth labels) is
a **validated reducer-independent training signal** for the blind class the reducer would otherwise starve
(≈77% flat here; cf. the ~43% overall blindness Validator flagged). A reducer-only score cannot rank
these words; a construction-depth (or bidirectional meet-in-the-middle certificate) label can. This is the
empirical backbone for using id-augmentation labels + exploration-bearing search in v1's scoring.

---

## Deep Round 3 — does the scoring redesign have legs on the REAL problem? (Lead 2026-07-17)

Two offline probes (pure-Python, `datapoint.py` reducer). Raw:
`Agents/.../output/axplorer-r3-transfer-escape-2026-07-17.json`; script `dr3_transfer_escape.py`.

### DR3-A — distribution transfer (does id-aug training data resemble real targets?)

Regenerated the P4 synthetic blind-class words (188 flat words, reducer ratio<0.02) and compared them,
via n-gram frequency **cosine** (n=2..6) + alt-run / syllable / rule-fragment stats, against (i)
`comm_13_10_raw`, (ii) the 345 seed corpus, (iii) a 1000-sample of the 12k held-out pool.

n-gram cosine of **synthetic-blind vs** each corpus:

| n | vs comm_13_10 | vs seed_345 | vs held_1000 |
|--:|--:|--:|--:|
| 2 | 0.593 | **0.967** | **0.916** |
| 3 | 0.257 | **0.846** | **0.828** |
| 4 | 0.116 | **0.670** | **0.678** |
| 5 | 0.047 | 0.471 | 0.505 |
| 6 | 0.009 | 0.283 | 0.324 |

**Reference cosines (n=4), to calibrate "same neighborhood":** comm-vs-seed **0.215**, comm-vs-held
**0.340**, seed-vs-held **0.935**.

| stat | synthetic_blind | comm_13_10 | seed_345 | held_1000 |
|---|--:|--:|--:|--:|
| syllable ratio | 1.485 | 1.062 | 1.432 | 1.479 |
| alt-run mean | 2.38 | 2.12 | 2.56 | 2.21 |
| alt-run ≥6 frac | **0.004** | 0.000 | 0.095 | 0.039 |
| rule-frag rate /1000ch | 25.2 | 34.9 | 39.0 | 25.3 |

**Reading (honest):** the synthetic blind words sit **in the same local-structure neighborhood as the
seed/held training distribution** (cosine 0.67–0.97 at n≤4; matching syllable ratio ~1.48, alt-run
mean, frag-rate ~25/1000 identical to held). They **diverge from `comm_13_10`** (cosine 0.12 at n=4,
collapsing to 0.009 at n=6) — **but so does everything**: comm is a structural *outlier* (comm-vs-seed
0.215, comm-vs-held 0.340 at n=4), because it is the one highly-regular `ABabAbab…`-scaffold word while
seed/held/synthetic are all comparatively "generic". The defining structural signature of the synthetic
blind class — **≈0 braid-runs ≥6** (0.004 vs seed 0.095) — is exactly the blindness property, by design.
**Verdict:** id-augmentation data **transfers to the PatternBoost training distribution** (the seed/held
corpus a value head actually trains on), so a value head trained on it is not learning off-manifold junk.
It does **not** specifically mimic `comm_13_10`'s long-range regularity — and no corpus does — so reaching
the specific comm target is a **search** problem (bridge via MCTS), not something the id-aug value head
alone covers. Recommend: use id-aug as blind-class augmentation **plus** keep the real-target family
(HWW pcps / seed windows) in the training mix so the head sees comm-like long-range structure.

### DR3-B — does bounded exploration-search escape the blind class?

50→90 P4 blind words (greedy reducer ratio ≈0), **stratified by length**. Baseline = greedy Python
reduce. Exploration = bounded uphill (insert a random ≤4-char fragment, Δ≤+4, immediate free+power+braid
cleanup; **R2 §7 budget: ≤2 enablers/path, +8 cap over path start, 40 random restarts**). "Escape" =
exploration achieves ratio > 0 where greedy gives 0.

| length bucket | n | mean len | greedy nonzero | **escape fraction** | mean shrink (over escaped) |
|---|--:|--:|--:|--:|--:|
| short (≤40) | 30 | 19 | 0/30 | **100%** | 0.291 |
| mid (41–150) | 30 | 67 | 0/30 | **100%** | 0.117 |
| large (>150) | 30 | 252 | 0/30 | **100%** | **0.031** |

**Reading (decision-grade):** **qualitatively YES — bounded uphill exploration escapes the blind class
100% of the time, in every size bucket**, finding a nonzero reduction the greedy reducer is structurally
blind to (e.g. `(aba)⁵` 15→9; a 19-char word 19→7). This validates that the **MCTS-rollout / exploration-
search route is real** — search sees what the greedy reducer cannot. **Quantitatively, escape *depth*
decays with size:** 29% shrink on short words → **3% on large (>150) words** (e.g. 294→285, 282→278).
A single §7-budgeted path (≤2 enablers, +8 cap) only removes ~1–2 relators; fully reducing a large blind
word therefore requires **chaining many bounded episodes** — precisely what a rollout-MCTS with a generous
step budget provides, and consistent with real reduction needing long move sequences. **Implication:**
build the exploration route, but size the per-target search budget generously (many chained bounded moves),
not a single §7 path — the greedy-vs-search gap is qualitative (0 → nonzero) but per-episode gain shrinks
with target size.

**Deep Round 3 net:** the scoring redesign has legs. (A) id-aug blind words live on the training manifold
(transfer OK; comm is an outlier for everyone → reach it by search). (B) bounded exploration escapes the
blind class universally, so rollout-MCTS is worth building — with the caveat that large targets need many
chained bounded episodes to reduce deeply, not one §7 path.

---

## Task 1 — Corpus statistics

### 1a. Length distribution

| corpus | n | min | p25 | median | mean | p75 | p90 | max |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| seed (345 windows) | 345 | 256 | 256 | 256 | 433.3 | 512 | 1024 | 1024 |
| comm_13_10_raw | 1 | — | — | — | 1348 | — | — | 1348 |

Seed lengths are exactly {256,512,1024} (windowing artifact). **Char-level T reaches 1348 on the loop
target — right at the `MAX_LEN=1536` / O(T²) wall flagged in the code map.**

### 1b. Alternating-run-length distribution (braid relevance)

Maximal runs where consecutive chars differ and only 2 distinct letters (i.e. `(gh)^k`-eligible).

| corpus | mean | max | frac runs ≥6 (braid-eligible) |
|---|--:|--:|--:|
| seed | 2.56 | 8 | **9.5%** |
| comm_13_10_raw | 2.12 | **5** | **0.0%** |

Seed run histogram (len→count): 1:20458, 2:16668, 3:9564, 4:1946, 5:4125, 6:1452, 7:3015, 8:1099.
comm run histogram: 1:42, 2:508, 3:56, 4:28, 5:2. **comm has no run ≥6 ⇒ braid_reduce cannot fire on it raw.**

### 1c. Single-generator power-run distribution (g^k syllables)

| corpus | mean | max | histogram (k→count) |
|---|--:|--:|---|
| seed | 1.43 | 4 | 1:78203, 2:15666, 3:2255, 4:8301 |
| comm | 1.06 | 2 | 1:1190, 2:79 |

Note the seed spike at k=4 (8301) — the `aaaab`/`aaaa` power blocks from the anchor scaffold. comm is
almost pure alternation (94% syllables are length 1).

### 1d. n-gram frequencies (n=2..8) — top motifs + entropy

Seed corpus (distinct / entropy-bits / top-3):

| n | distinct | entropy | top-3 (gram:count) |
|--:|--:|--:|---|
| 2 | 12 | 2.52 | ab:40224, ba:40093, aa:33903 |
| 3 | 33 | 3.59 | aba:28046, bab:23466, aaa:17744 |
| 4 | 69 | 4.57 | baba:15817, abaa:15505, abab:12348 |
| 5 | 115 | 5.29 | ababa:11639, babaa:9956, abaaa:9943 |
| 6 | 168 | 5.86 | ababaa:8264, abaaaa:7720, baaaab:7713 |
| 7 | 228 | 6.38 | abaaaab:7698, baaaaba:5504, ababaab:4943 |
| 8 | 286 | 6.75 | abaaaaba:5495, aabaaaab:4383, bababaab:4375 |

comm_13_10_raw is far more uniform/structured (top bigrams AB:178 BA:177 ab:177 ba:177; entropy
3.25 bits vs seed's 2.52 — comm spreads mass evenly over the 12 bigrams, seed is dominated by
`ab/ba/aa`). The dominant seed n-grams are **power-run + short-alternation** motifs (`aaa`, `abaa`,
`abaaaab`), i.e. syllable structure, **not** the capital-heavy rule fragments — the rule motifs are
rare in the seed corpus (Task 2).

**Free-cancellation pairs (xX adjacency):** 0 in both corpora (freely reduced). Free-cancellation is
a **transient** mid-reduction event — it cannot be measured statically and is only relevant to a
moves/trace encoding, not a static tokenizer.

---

## Task 2 — Rule-bank anatomy (31 junction rules)

### 2a. Length structure

| field | min | p25 | median | p75 | max |
|---|--:|--:|--:|--:|--:|
| junction LHS (kbprog rule) | 41 | 78 | 80 | 143 | 1177 |
| junction RHS | 40 | 77 | 78 | 142 | 1176 |
| **edit fragment** (the actual semantic change) | **5** | **8** | **10** | **73** | **1107** |

- All rules **length-decreasing**: Δ = −1 (×23) or −2 (×8).
- Orientation: A→B (23), A→SUFFIX (5), PREFIX→B (2), B→A (1).
- **Two-scale structure.** The `.kbprog` LHS are long *junction words* (median 80, up to 1177 chars);
  the true edit is a short interior *fragment* (median 10). 16 of 31 fragments are ≤12 chars
  (`{5,6,8,9,10,11,12}`); the other 15 are long "reassembly" rules (39–1107 chars) that fire ~once.
  **For representation, the ≤12-char fragments are the alignment-critical units.**

### 2b. Shared motifs / scaffold

Longest common prefix/suffix across all 31 junction-LHS = **empty** (rules start with different
short frags: `ABab…`, `BBAB…`, `ABAB…`). But the recurring backbone `ABabAbabABaBAbabABABabAbaBABaBAbab`
(the CoreA/CoreB commutator scaffold, [[project_b25_lcs_dimensions]]) frames most junction words —
consistent with these being junction rules mined from the comm_13_10 reduction context.

### 2c. Where rule fragments actually sit in the seed corpus (offsets mod k)

Most short fragments are mined from comm's junction context and **do not occur** in the seed windows.
Only these appear (n_occ in the 345-window corpus):

| fragment | len | n_occ in seed | offset phase (mod k) |
|---|--:|--:|---|
| `aabaaa` | 6 | **5506** | near-uniform for all k=2..6 (no privileged phase) |
| `abABA` | 5 | 130 | mod-4: {0:48, 1:48, 3:34} — spread |
| `abaBA` | 5 | 120 | mod-4: {0:42, 3:48, 1:24, 2:6} — spread |
| `ababABABA` | 9 | 44 | mod-4: {3:24, 2:20} |
| `ababaBABA` | 9 | 36 | mod-4: {1:24, 2:12} |
| (16 other short frags) | — | **0** | — |

**Key takeaway:** firing sites carry **no privileged byte-phase** — offsets mod k are ~uniform. So no
fixed k-mer grid can be chosen to align with them; any block boundary cuts them at the generic rate.

---

## Task 3 — Boundary-misalignment metric (the core result)

For fixed k-mer packing, a firing site `[start, start+L)` is **boundary-clean** only if it exactly
covers whole k-blocks (`start % k == 0` AND `(start+L) % k == 0`); otherwise it **straddles** and the
model must relearn structure across token boundaries. Fraction straddling, over real corpus firing sites:

| site type | n sites | k=2 | k=3 | k=4 | k=5 | k=6 |
|---|--:|--:|--:|--:|--:|--:|
| short rule-fragments | 5836 | 52.7% | 68.0% | **100%** | 99.2% | 84.2% |
| 24 bias motifs | 294 | **100%** | 94.2% | **100%** | 84.0% | **100%** |
| braid runs ≥6 | 5566 | 72.2% | 91.4% | 94.1% | **100%** | 94.8% |

- **k=4 (the natural `4^4=256`-vocab `DenseTokenizer` idiom) straddles 100% of rule-fragment sites** —
  because no fragment length is divisible by 4.
- **Every k∈{2..6} straddles ≥52% of fragment sites and ≥72% of braid sites.** There is no benign
  block size. This is the empirical grounding for the code-map's concern that fixed k-mer packing
  "mis-aligns token boundaries with these overlapping motifs."

---

## Task 4b — Phase B: BPE de-bias on the 12k held-out pool (Lead GO 2026-07-17)

The Task-4 seed-corpus BPE was degenerate (345 windows of 2 anchors). Per Lead GO, re-ran BPE on a
**diverse 12k held-out pool** generated per R2 §5, **offline (free-reduce only, NO braid GO test)**:
seed `20260701`, 4000 seed-mutations (1–3% raw edits) / 4000 non-backtracking random walks (lengths
{64,128,256,512}, half forced to abelianization (0,0)) / 4000 motif-stress (bg walks {128,256,512}
with 1–4 injected bias motifs); every candidate free-reduced, restricted to `{a,A,b,B}`, exact seed
words + 119 benchmark words excluded. Pool saved: `Agents/.../output/heldout_pool_20260701.txt`.
Raw: `axplorer-repr-phaseB-heldout-bpe-2026-07-17.json`. Script: `heldout_pool_bpe.py`.

### Held-out char-level T (for honest MAX_LEN sizing)

| stat | mean | median | p95 | max | min | seed_mut | rand_walk | motif_stress |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| char T | 332.8 | 256 | 558 | **1028** | 61 | 432.5 | 240.4 | 325.5 |

Max held-out T = 1028; comm target = 1348 ⇒ **`MAX_LEN=1536` covers both with headroom.**

### BPE on the non-degenerate pool — the de-biased kill finding

Now BPE behaves normally (mean T 45–85 tokens; max token 23–157 chars — no whole-word swallowing).
Yet it **still does not align to the algebra**:

| vocab | mean T (tok) | max tok len | motifs as single token | **frags as single token** | **frag firing sites CUT by a token boundary** |
|--:|--:|--:|--:|--:|--:|
| 64 | 85.2 | 23 | 0/24 | **0/21** | **71.9%** (68915/95896) |
| 256 | 58.4 | 77 | 0/24 | **0/21** | **54.8%** (52550/95896) |
| 1024 | 45.7 | 157 | 2/24 | **0/21** | **41.8%** (40125/95896) |

Top merges (all vocab, frequency-driven): `a+b`(656k) `a+a`(329k) `A+b`(303k) `A+B`(205k) `a+ab`(203k)
`ab+ab`(105k) `aa+aab`(88k)… — pure power-run/short-alternation, **never the capital-bearing rule
fragments**. Fixed k-mer straddle on the same 95896 held-out firing sites (robust vs seed): k=2 62.4%,
k=3 75.5%, k=4 **98.9%**, k=5 95.6%, k=6 88.3%.

**De-biased verdict.** On diverse data, greedy BPE learns **0/21** rule fragments as tokens and its token
boundaries **cut 42–72%** of rule-fragment firing sites — i.e. BPE is *not* meaningfully better-aligned to
the algebra than fixed k-mer. Both align to frequency, not to the edit motifs. **Only char-level has zero
misalignment** (every firing site is exactly representable). The tradeoff for the verdict is now sharp:
- **char-level:** 0% site-cut, T mean 333 / max 1348 (O(T²) cost, but under MAX_LEN=1536).
- **BPE-1024:** ~42% site-cut, but T mean 45.7 ⇒ ~7× shorter ⇒ ~**50× less attention compute**.
- **fixed k-mer:** dominated — worse cut (≥62%) *and* fixed grid, no data adaptivity.

Recommendation firms up: **char-level default**; BPE-1024 is the only credible T-lever if O(T²) forces it,
accepting the ~42% algebraic-cut cost (an auxiliary rule-hit channel could partly compensate); **fixed
k-mer is out.** Windowing (256–1024) composes with either and is the cheapest orthogonal T-lever.

---

## Task 4 — Offline BPE simulation (vocab 64 / 256 / 1024) — seed corpus (degenerate, see 4b)

Greedy byte-pair BPE trained on the 345-word seed corpus (deterministic, pure Python).

### 4a. Top merges (all vocab sizes identical prefix — frequency-driven)

`a+b`(40224) → `a+a`(17838) → `a+ab`(13838) → `b+ab`(11118) → `aa+aab`(7723) → `A+b`(6000) →
`ab+ab`(4989) → `A+bab`(4443) → `aaaab+ab`(3301) → `abab+aab`(3294) → …

Merges track **frequency (power-runs + short alternation: `aab`, `aaaab`, `abab`)**, exactly the
syllable/n-gram motifs of Task 1 — **not** the capital-bearing rule fragments.

### 4b. Motif alignment — BPE never learns the edit units

| vocab | tokens built | motifs as single token | short frags as single token |
|--:|--:|--:|--:|
| 64 | 64 | **0/24** | **0/21** |
| 256 | 256 | **0/24** | **0/21** |
| 1024 | 608 (merges exhausted at count<2) | **0/24** | **0/21** |

### 4c. Boundary-cut of firing sites (caveat-heavy)

| vocab | mean T (tokens/word) | frag sites cut by a token boundary | braid sites cut |
|--:|--:|--:|--:|
| 64 | 19.3 | 28.7% | 2.1% |
| 256 | 6.0 | 8.7% | 1.5% |
| 1024 | 3.2 | 4.8% | 0.4% |

**Read this carefully.** The *low* cut-rate is **not** good alignment — it's degeneracy. Mean T=6 tokens
for a 433-char word means each BPE token is ~72 chars: whole repeated windows get swallowed into single
tokens, so a site rarely has an internal boundary simply because it lives inside one giant token. Longest
learned tokens run 65→436→840 chars. **This happens because the seed corpus is 345 overlapping windows
of only 2 anchors (extreme self-similarity).** On the diverse 12k held-out pool (R2 §5), tokens would be
far shorter and cut-rates far higher. **Verdict: BPE's behavior here is untrustworthy for the
generalization question; re-run BPE analysis on the held-out pool before any BPE decision.**

### 4d. T-reduction levers (for the O(T²) budget)

Char-level T (seed mean/max = 433/1024; comm = 1348). Fixed k-mer would give:

| k | seed mean T | seed max T | comm T |
|--:|--:|--:|--:|
| 1 (char) | 433 | 1024 | 1348 |
| 2 | 217 | 512 | 674 |
| 3 | 145 | 342 | 450 |
| 4 | 108 | 256 | 337 |
| 5 | 87 | 205 | 270 |
| 6 | 73 | 171 | 225 |

k-mer buys a clean k× T-reduction (attractive for O(T²)) **but at the 100%-straddle algebraic cost of
Task 3.** That is the central tradeoff the verdict must weigh.

---

## Task 5 — Trace availability (moves-encoding readiness)

Read-only inspection of `braid_reduce.rs` + `src/reduce/braid.rs`.

### What exists today
- **`--trace-file <path>`** CLI flag (braid_reduce.rs:67-69) → writes JSON `{word_file, original_len,
  final_len, total_delta, num_passes, num_rule_applications, trace:[...]}`.
- **`reduce_leftmost_traced`** (lines 142-183) records a `TraceEntry` per rule application:
  `step, stage, lhs, rhs, lhs_len, rhs_len, position, len_before, len_after, delta, direction`
  (direction ∈ reducing/same/expanding). **This is exactly a (rule, position, delta) move log** — a
  replayable sequence-of-reductions for the leftmost stage.
- **`apply_braid(word, pos, exponent)`** (braid.rs:32) and `apply_at(rules, word, match)` are position-
  parameterized move primitives — the atomic move already exists in the reducer.

### What is missing for a full moves encoding
1. **Only the leftmost stage is traced.** Step 1 braid shortenings (`generalized_braid_shortenings`,
   returns whole candidate *words*, not moves), `reduce_multi_start`, and **`reduce_beam`** are all
   **untraced**. On hard words beam search does most of the work → the interesting move sequence is
   exactly what's not logged.
2. **`generalized_braid_shortenings` discards the move.** It returns replacement words, not
   `(pos, run_len, g, h)` braid descriptors — so braid steps aren't replayable as moves.
3. **No stable rule-ID.** Rules are logged by LHS/RHS *string*; a moves vocabulary needs a compact rule
   index (the AC pattern index `mat.pattern().as_usize()` is available but not exported to the trace).
4. **No initial→final move-sequence guarantee.** Because stages 1/beam are untraced, the trace does not
   reconstruct `word → best`; a moves encoding needs a complete, gap-free step list.

**Bottom line:** the *primitive* (position-anchored, delta-logged rule application) exists and is proven
out for leftmost; a moves encoding for v1 would require (a) trace hooks in braid + multi_start + beam,
(b) braid-move descriptors, (c) a rule-ID table. That is a **Developer `mixer-core`/reducer change →
route as a requirement to Lead**, not something this role touches. Moves-encoding is therefore **not
v1-ready** without that build.

---

## Task 6 — Syllable statistics (factored-encoding T bound)

Decompose each word into maximal `g^k` syllables (run-length). Syllable-count vs char-count:

| corpus | char total | syllable total | **compression ratio** | per-word ratio (median) |
|---|--:|--:|--:|--:|
| seed | 149504 | 104425 | **1.43×** | 1.67 |
| comm_13_10_raw | 1348 | 1269 | **1.06×** | 1.06 |

Exponent histogram (k→#syllables): seed {1:78203, 2:15666, 3:2255, 4:8301}; comm {1:1190, 2:79}.

**A syllable-factored representation (one token per `g^k` run) bounds T at ~len/1.43 on seed windows but
only ~len/1.06 on the real target comm_13_10.** Because the loop target is near-fully alternating, syllable
factoring is nearly a no-op there (~6% saving). It does not, on its own, solve the O(T²) budget for the
actual word. (It *is* lossless and would compose with windowing, but the T-win is marginal on target.)

---

## Caveats & anti-pattern check

- **Self-similar corpus.** The 345-word seed corpus is windowed slices of only 2 anchors → BPE and n-gram
  stats are biased toward the anchor scaffold. Task-3 straddle numbers are corpus-robust (depend on motif
  lengths, not frequencies); **Task-4 BPE numbers are NOT** — flagged above, must re-run on the 12k pool.
- **Not tuning-on-scoring.** No scoring/training done here; this is pre-decision grounding, no target
  cherry-picking. Rule fragments and 24 motifs are the *given* R2 inventory, not fitted.
- **Soundness unaffected.** No math claim produced — corpus/tokenization statistics only. Nothing here
  needs Validator; the *representation verdict* that consumes this is an axplorer program.md
  math-review gate (Lead → Maria), which is separate.
- Related: [[patternboost-b25-loop-prereg-2026-06-30]], [[project_b25_lcs_dimensions]],
  [[project_b25_patternboost_pivot]], [[project_abelianization_blind_on_commutator]].

## Open questions routed out
- **For Lead / axplorer verdict:** does v1 need T-reduction at all, or is windowing (256–1024, already
  built) enough to stay under O(T²)? If T-reduction is required, BPE-on-held-out-pool vs windowing is the
  live comparison; fixed k-mer is empirically dispreferred (Task 3).
- **For Developer (via Lead, if moves-encoding is pursued):** trace hooks for braid + multi_start + beam
  stages + rule-ID table in `braid_reduce.rs` — required before a sequence-of-reductions encoding is testable.

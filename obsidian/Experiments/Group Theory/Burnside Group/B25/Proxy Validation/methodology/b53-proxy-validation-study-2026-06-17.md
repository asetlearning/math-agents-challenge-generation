---
title: "Pre-registration: B(5,3) proxy-validation study for PatternBoost score proxy"
domain: group-theory
project: b25
instance: B(5,3) → B(2,5)
experiment_type: proxy-validation
status: approved
registered: 2026-06-17
approved: 2026-06-17
validator_gate_a: SOUND (2026-06-17)
validator_gate_b: SOUND (2026-06-17)
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b53, topic/proxy-validation, topic/patternboost, project/b25, status/pending, experiment]
---

# Pre-registration: B(5,3) Proxy Validation Study

**Registered**: 2026-06-17 (before Step C correlation is run)
**Registered by**: B25 Experimenter (maumayma)

---

## 1. Background and motivation

The B(2,5) PatternBoost loop needs a cheap SCORE proxy for "distance to identity". The
current proxy (Option B: Rust `braid_reduce --no-beam`, reduction_ratio) was rejected by
Validator as a proximity signal because it scores 0.000 on ~43% of B(2,5) words
(products-of-conjugates like `(aba)^5`) — these words are BLIND to the proxy, providing
no gradient for the search loop.

B(2,5) has no checkable ground truth (that is the open problem). B(5,3) is finite (order
3^7 = 2187), completely solved by shortlex KB in 1.7s with 98K rules, and provides cheap
verified ground truth for every word. We use B(5,3) as a lab, validate a structurally
general proxy there, then transfer to B(2,5).

---

## 2. Hypotheses

**H1 (primary)**: The combined proxy (reduction_ratio + abelianization_distance) correlates
more strongly with true distance-to-identity than reduction_ratio alone.

**H2 (secondary)**: abelianization_distance alone has Pearson r > 0.40 with true distance
(non-trivially predictive despite being purely arithmetic).

Both hypotheses are **falsifiable and pre-registered before results are computed**.

---

## 3. Step A — Ground truth (COMPLETE)

**Evidence**: see [[Agents/maumayma/Experimenter-B25/output/b53-step-a-ground-truth-2026-06-17]]

- **Run**: `kb_mixer run17_shortlex_only.toml` on 153 B(5,3) relators
- **Result**: 153/153 proved, elapsed 1.7s
- **Provenance triple**:
  - git SHA: `17b6068b395a35f89c0b05aa0f5048cd6961170c`
  - Cargo.lock SHA256: `63d2f077281662a325ade5c216cbf326955281eea9fa5caf9af83477835abd2f`
  - kb_mixer binary SHA256: `90ad337c7c26bf6d1901828e4370c77469bba249b4ac4fbc133a895370f7e54c`

**Critical design note from Step A**: All 153 target words are B(5,3) relators (group
identity). Their shortlex-reduced form is ε (empty), ground-truth distance = 0 for all.
A corpus of all-zeros y-values yields undefined Pearson r. **The Step C corpus must be
augmented with non-identity B(5,3) words** (see §5 below).

**Validator gate A** (~~pending~~ → **SOUND — 2026-06-17**): Shortlex KB (98K rules, run17)
is confluent/complete enough for B(5,3) that "reduced to empty ↔ group identity". Verdict
received from Validator (via Lead). Gate closed.

**Validator gate A hardener** (**MET — already in Step A evidence**): run17 log shows
`reason: 'reducer_complete'` and `greedy items=98210 COMPLETE` — the KB terminated on the
completeness predicate, not a resource cap. This confirms the ground truth is not
resource-limited. Noted here to close the hardener on paper.

Step C is unblocked on gate A.

---

## 4. Step B — Candidate proxies (definitions, structurally general)

All three proxies are **structurally general**: defined identically in any Burnside group
B(m,n), requiring only the group's alphabet and exponent. None is tuned to B(5,3)-specific
rule patterns.

### Proxy A: reduction_ratio

**Definition**: For word w in alphabet {a,A,b,B,...} of length L, run ONE GREEDY LEFTMOST
PASS of the shortlex AC automaton (built from the KB rule bank bootstrapped in Step A).
Let L' = length after one pass. Then:

```
reduction_ratio(w) = (L - L') / L    [range: 0.0 to 1.0]
```

"One pass" = one left-to-right scan with earliest-match-first (no iteration to fixed point,
no beam search, no conjugation, no braid moves). L' may be > 0 even for identity words.

For B(2,5): analogous proxy uses the B(2,5) shortlex KB rules for one pass.

**Blind-spot note**: For words where no rule fires in one pass (L' = L), reduction_ratio = 0.
This is the "~43% blind" problem in B(2,5) that motivates the combined proxy.

### Proxy B: abelianization_distance

**Definition**: For each generator g ∈ {a,b,c,d,e}, let n_g = count of lowercase g minus
count of uppercase G in w (net signed exponent). Reduce mod n (exponent: n=3 for B(5,3),
n=5 for B(2,5)) into {0, 1, ..., n-1} or equivalently into {-(n-1)/2, ..., 0, ..., (n-1)/2}
(balanced residue, so |·| gives shorter distance).

```
abel_vec(w) = (n_a mod 3, n_b mod 3, n_c mod 3, n_d mod 3, n_e mod 3)
             using balanced representation: map k → k if k ≤ 1, else k - 3
abelianization_distance(w) = L1 norm of abel_vec(w)
                            = sum of |n_g balanced mod 3| over g ∈ {a,b,c,d,e}
```

**Range for B(5,3)**: 0 to 5 (five generators, each contributing 0 or 1 in balanced mod 3).

**Key property**: If w = 1 in B(5,3) then abel_vec(w) = 0 (abelianization of identity = 0).
The converse fails (commutator subgroup elements have abel_vec = 0 but may not be identity).
This means abelianization_distance = 0 for all relators — consistent with Step A corpus.
It also means abelianization_distance = 0 for a potentially large fraction of non-identity
words (members of the commutator subgroup). This is expected and is part of what the
correlation study measures.

**Validator gate B** (~~pending~~ → **SOUND — 2026-06-17**): Mod-3 abelianization is the
correct homomorphism for B(5,3). Nonzero ⟹ not identity (sound). Verdict received from
Validator (via Lead). Gate closed. Step C is unblocked on gate B.

### Proxy C: combined

```
combined_score(w) = α · reduction_ratio(w) + β · abelianization_distance(w)
```

**Pre-registered weights**: α = 0.5, β = 0.5 (equal weighting). These are FIXED weights,
chosen before running the study. No fitting, no post-hoc weight tuning.

Rationale: reduction_ratio captures rule-reachable structure; abelianization_distance
captures the algebraic obstruction. Equal weights are the neutral choice with no prior
on relative informativeness. If post-hoc analysis suggests other weights work better, that
is a **hypothesis for a new (separate) study**, not a result of this one.

---

## 5. Step C — Correlation corpus and protocol

### 5.1 Corpus construction (pre-registered before results)

The 153 relators alone are insufficient (all y=0, undefined Pearson r). The test corpus is:

**Corpus = RELATORS (153 words, y=0) + RANDOM SAMPLE (≥500 words, target: ≥40 per y-bin)**

Random sample generation:
1. Generate 800 uniformly random words in {a,A,b,B,c,C,d,D,e,E} of lengths sampled
   uniformly from {1, 2, ..., **30**}, ensuring free reduction (no adjacent inverse pairs).
   (Max length raised from 20 to 30 to populate high-distance bins y ∈ {4,5,6,7} — B(5,3)
   diameter under this generating set may be small; longer inputs are needed to reach
   peripheral elements.)
2. Run shortlex KB (same 98K-rule bank from Step A) on each word.
3. Record reduced form and its length as ground-truth distance.
4. **Required y-distribution check**: count words per y-bin {0,1,...,7}. Target ≥ 40 words
   per bin for y ∈ {1,...,7}. If any bin y ≥ 4 has fewer than 20 words, increase sampled
   word length to 50 and regenerate (same seed + offset). Document the ACHIEVED per-bin
   counts in the corpus CSV header and in the results note.
5. Discard any word that the KB cannot reduce within 5s (timeout sentinel — should not occur
   given run17 proves all words in 1.7s total).

**Corpus file**: output to
`Experiments/Group Theory/Burnside Group/B25/Proxy Validation/data/b53-proxy-corpus-YYYY-MM-DD.csv`
with columns: `word, input_length, reduced_length, ground_truth_distance`.
CSV header must include per-bin counts: `# y=0: N, y=1: N, y=2: N, ...`

### 5.2 Proxy computation

For each word in the corpus:
1. Compute reduction_ratio (one-pass with 98K shortlex rules — bootstrap the builder once,
   apply individually).
2. Compute abelianization_distance (pure arithmetic, no KB).
3. Compute combined_score (α=β=0.5).

### 5.3 Analysis

For each proxy {A, B, C}, compute on **TWO SLICES** of the corpus:

**Slice 1 (full corpus)**: all words including y=0 relators.
**Slice 2 (y>0 only)**: words with ground_truth_distance > 0 (non-identity words only).

Rationale for Slice 2: PatternBoost needs gradient among non-identity words to climb.
A proxy flat across y ∈ {1..7} but good at separating y=0 from y>0 scores well on the
full corpus but is useless for the search. The y>0 correlation is the **primary** number
for the use case. Report both slices; base H1/H2 verdicts on Slice 2.

For each proxy × slice:
- Compute **Pearson r** and **Spearman ρ** vs ground_truth_distance.
  (Spearman captures monotonic association regardless of linearity; ground truth and proxies
  are on coarse integer scales where monotonic signal is what a search gradient needs.)
- Compute 95% CI on each (Fisher z-transform for r; bootstrap for ρ, or use standard
  large-sample approximation SE(ρ) ≈ 1/√(n−3)).
- Plot scatter (y = ground_truth_distance, x = proxy_score), separate panels per slice.

For comparison of r(combined) vs r(reduction_ratio) (H1 test):
- Use **Steiger's Z test** (or Williams' test) for dependent overlapping correlations.
  Both correlations are on the SAME words and C is a linear function of A+B, so they are
  strongly dependent. The non-overlapping Fisher-z CI comparison (originally in §6) is
  WRONG here — it assumes independent samples. Steiger's Z handles the dependence.
- Implement via the `pingouin` or `scipy`+manual formula: see Steiger (1980) or Meng et al.
  (1992) for the exact test statistic. Report the Z-statistic and two-tailed p-value.

Report:
- Pearson r, Spearman ρ, 95% CI, p-value (under H₀: r=0 / ρ=0) for each proxy × slice.
- Steiger's Z and p-value for H1 (combined vs reduction_ratio), computed on Slice 2.
- Blind-spot fraction on Slice 2: what fraction of words with ground_truth_distance > 0
  get proxy = 0? (Analogous to the 43% blind problem in B(2,5).)
- Per-bin y-distribution of the random corpus (document once in header + results note).

---

## 6. Pre-registered success thresholds

These thresholds are locked BEFORE Step C runs.
All verdicts are based on **Slice 2 (y>0 only)** — full-corpus numbers are secondary.

| Test | Threshold | Significance test | Verdict if met | Verdict if not met |
|------|-----------|------------------|---------------|-------------------|
| H1 primary | r(combined) − r(reduction_ratio) > 0.05 AND r(combined) ≥ 0.60 on Slice 2 | **Steiger's Z** (dependent overlapping correlations; two-tailed p < 0.05) | H1 supported: combined wins | H1 not supported |
| H2 secondary | r(abelianization) ≥ 0.40 on Slice 2 | Standard Fisher-z CI (single proxy, not a comparison) | H2 supported: abel is non-trivial signal | H2 not supported |
| Blind-spot test | blind-spot fraction(combined) < blind-spot fraction(reduction_ratio) on Slice 2 | Descriptive; no p-value required | Combined has better coverage | No coverage improvement |

Note: the original §6 used "CIs don't fully overlap" for H1 — this is **replaced** by Steiger's Z
because the compared correlations are strongly dependent (same words, C is a linear function of A+B).

"Better" for PatternBoost purposes is determined by (in order of priority):
1. Lowest blind-spot fraction on Slice 2 (fewest words with proxy = 0 at distance > 0)
2. Highest Pearson r on Slice 2
3. Highest Spearman ρ on Slice 2 (tiebreaker — captures monotonic gradient)

---

## 7. Step D — Transfer criterion (pre-registered before results)

The winning proxy from Step C is transferred to B(2,5) with the **identical structural
definition**, only changing the exponent (n=5 instead of n=3) and the generator set
({a,b,A,B} instead of {a,b,c,d,e,A,B,C,D,E}).

**Transfer rules** (locked before Step C; verdicts based on Slice 2 / y>0):
- If H1 supported: use combined proxy in B(2,5) PatternBoost (replaces current Option B).
- If H1 not supported but H2 supported (abelianization alone has r ≥ 0.40 on Slice 2): use
  abelianization_distance alone as the B(2,5) proxy.
- If neither H1 nor H2 supported: keep current Option B; file new proxy design task to Lead.

The transfer is **not post-hoc** because:
(a) the proxy definition is structurally general (identical formula, different modulus),
(b) the transfer rule is written here before results are computed,
(c) the B(2,5) version is not tuned to B(2,5) data (B(5,3) data only).

---

## 8. Mixer agents and modifications

| Component | Role |
|-----------|------|
| `kb_mixer` (burnside_bidirectional) | B(5,3) KB agent — runs run17_shortlex_only.toml |
| Corpus generation script | New Python script (to be written under `experiments/burnside/b53_bidir/`) |
| Proxy computation script | New Python script — computes A, B, C for each word |
| No `mixer-core/` changes | Only scripts and data; if `mixer-core/` changes needed → stop, file to Lead |

---

## 9. Anti-pattern checks

- **Not tuning to a single target word**: corpus is 500+ random words, not cherry-picked.
- **No implicit ordering changes**: one-pass uses the SAME 98K rule bank for all proxy A
  computations; order is fixed by the Aho-Corasick construction from Step A.
- **No compression collisions**: no compression step in this study.
- **Misses reported**: blind-spot fraction is reported alongside hits.
- **No Hall's reductions issue**: this is not a novel math claim about B(2,5) — it is a
  proxy calibration study. No Validator routing needed for the correlation result itself
  (it is engineering). The transfer criterion is engineering, not math.
- **Validator gates respected**: Step C does NOT run until Validator confirms gates A and B.

---

## 10. Termination criteria

- **Success**: 153/153 + random corpus generated + all three proxies computed + Pearson r
  reported for all + scatter plots in output note + verdict on H1/H2.
- **Failure modes**:
  - ~~Validator gate A: "shortlex KB not confluent/complete"~~ — **CLOSED SOUND 2026-06-17**.
  - ~~Validator gate B: "abelianization definition wrong"~~ — **CLOSED SOUND 2026-06-17**.
  - Random corpus: fewer than 100 distinct y values > 0 → note in output, compute r on
    what's available, flag statistical limitations.
  - y-bin sparsity: if any bin y ≥ 4 has < 20 words after length-30 sampling → raise max
    length to 50 (same seed + offset) and resample.

---

## 11. Seeds

Random word generation: seed = `20260617` (today's date, numeric). Fix this seed for
reproducibility; document in corpus CSV header.

---

## 12. Known limitation — mechanical correlation of Proxy A in the lab

**To be stated in Step C results note (not a blocker, but must be disclosed).**

Proxy A (reduction_ratio) shares the **same 98K shortlex rule bank** as the ground-truth
reducer. In the lab, proxy A is therefore a truncated version of the ground-truth
computation. Its lab correlation is partly MECHANICAL — of course a one-pass version of the
oracle correlates with the oracle.

The transfer to B(2,5) rests on a structural-analogy assumption that cannot itself be
validated by this lab:

> "The way B(5,3)'s one-pass greedy reduction relates to B(5,3)'s true identity-distance
> is analogous to the way B(2,5)'s one-pass greedy reduction relates to B(2,5)'s true
> identity-distance."

This assumption is reasonable (same algorithm, same algebraic structure class, different
parameters) but is not directly verifiable because B(2,5) ground truth is the open problem.

The lab study validates the **structural generality** of the proxy definition and the
**abelianization component** (which is purely algebraic and has no mechanical dependency
on the rule bank). It does not validate proxy A's absolute predictive power in B(2,5).

Stated here so the transfer is not oversold.

---

## 13. Related material

- [[Agents/maumayma/Experimenter-B25/output/b53-step-a-ground-truth-2026-06-17]] — Step A evidence (153/153)
- [[Proxy Validation/_type]] — experiment type root
- [[PatternBoost/methodology/patternboost-b25-proxy-correlation-2026-06-15]] — prior B(2,5) proxy study (Option B accepted; now superseded by this study's result)
- [[B53/Rust Bidirectional/data/rust-bidirectional-data-b53]] — stale data note (corrected 2026-06-17)

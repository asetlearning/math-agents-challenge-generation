---
title: "b25-solver I2-collapse-predictors: quantities beyond length that may predict a collapse after blind-pool insertion (review)"
domain: group-theory
project: b25-solver
instance: B(2,5)
experiment_type: patternboost-solver
status: conjectured
author: asetlearning
date: 2026-11-06
source: Math Expert review for Lead (TASK of 2026-11-06, "reward metrics for blind-pool insertion beyond length")
tags: [agent/math-expert, user/asetlearning, domain/group-theory, topic/b25, topic/burnside, topic/trivial-words, topic/word-problem, topic/patternboost, project/b25-solver, status/conjectured, methodology]
---

# I2-collapse-predictors: what could predict a collapse better than length

> [!info] Plain English
> E4 proves a benchmark word w trivial by multiplying it by a word u that is known to be trivial, then shortening the product with the 2.5-reduction. Length after reduction is a poor guide: most attempts that end up emptying a word cannot be told apart beforehand by the length they leave. This note proposes quantities to record in experiment A that might tell earlier whether a word is about to collapse. It also says how to test them and what A has to log for the test. It answers the pool-period question, partly from E4 data that already exists.

Project: [[project-b25-solver]]. Context: [[Experiments/Group Theory/B25 Solver/_progress|b25-solver progress]] (E4 results), [[b25-solver-stage1-plan-2026-11-04]], the I1 review (Math Expert proposal of 2026-11-04 and [[_synthesis-b25-solver-similarity-invariants-2026-11-04]]), [[2026-11-06-b25-solver-e4-blind-insertion-breaks-check]] (Validator, periods of the certificate cells).
Status: **conjectured** throughout, except where a line says **measured** (computed for this note from E1 and E4 outputs) or **argued**. Proposals only, not certified.

## Terms

- **Cell:** a conjugate g v^{±5} g⁻¹ of a relator. Its **period** is |v|.
- **R2.5 step:** replace a factor x^k (x a cyclic word of period p = |x|, k > 2.5 possibly fractional) by x^{k−5}. Its length change is Δ = (5 − 2k)·p < 0 for 2.5 < k < 5, and −5p for k ≥ 5 (x⁵ is deleted), followed by free cancellation. **R2.5** is the greedy-then-cyclic-exhaustive loop of these steps.
- **M2 attempt:** choose u (3–8 pool cells), align u⁻¹ to w at the longest common factor (lcf) of the cyclic words (16 rotations × letter-automorphism images), form the **peak word** q = cycred(w·u⁻¹), then run R2.5 on q. It **empties** if R2.5(q) = 1, and **shortens** if 0 < |R2.5(q)| < |w|.
- **Run:** a maximal factor with smallest period p and length ℓ ≥ 2p. Its **exponent** is e = ℓ/p.
- **Near-fireable run:** a run with 2 ≤ e ≤ 2.5. One uphill step x^e → x^{e−5} (cost Δ = (5 − 2e)p, between 0 and p) turns it into its inverse complement.
- **State feature:** computed on a word x alone (q, a residual, or w). **Trace feature:** computed from how R2.5 ran.

## 0. Framing (argued)

**Where the peak is.**
- Every R2.5 step strictly shortens, so there is no peak inside R2.5. The one exception would be a length-neutral half swap at k = 2.5, if the implementation allows it (§7, open).
- The peak is the insertion: |q| = |w| + |u| − 2·(cancellation), about 2–2.5 |w| in E4.
- **Peak walking** therefore means a chain of insertions (and other uphill moves) whose intermediate words can be longer than w before a final collapse.
- A reward for such a chain must score an **intermediate word x** (a state feature), not only the length R2.5 leaves.

**Two prediction problems; the second is primary.**
1. **Target level (62 broken vs 138 not).**
   - This comparison is confounded by length and budget.
   - Measured: 0 of the 55 targets with ≥ 800 letters broke, and only about 30 attempts fit on those.
   - Any comparison here must be stratified by length band and arm, or it measures the budget.
2. **Attempt level, within a broken target.**
   - Broken targets were emptied by hundreds of attempts, and not by thousands of others.
   - Every broken target therefore has real positives and negatives. This is the test that matters for a beam over insertion chains.

**What a feature may use.**
- Features must be computed **before** the outcome they predict: on q before R2.5, or on a prefix of the R2.5 trace.
- A feature computed on R2.5(q) trivially "predicts" emptiness.
- The **baseline** to beat is what the current search already sees at the same moment: |q|/|w| and the lcf.

## 1. Measured now from E1 and E4: χ₆ does not separate broken from unbroken

χ₆ is the period-≥7 charge in ℤ₅ (the I1 note's M3). It is computed from E1-charge-census words_chi.tsv (the charge of the registry word) and E4 breaks.jsonl.

**Breaks by charge** (60 breaks in breaks.jsonl; the 2 mixer breaks are in E4-mixer and are not included):

| stratum | χ₆ = 0: broken / total | χ₆ ≠ 0: broken / total |
|---|---|---|
| all | 24/67 (36 %) | 36/133 (27 %) |
| < 300 letters | 1/1 | 4/6 |
| 300–499 | 13/18 | 23/40 |
| 500–799 | 10/31 | 9/49 |
| ≥ 800 | 0/17 | 0/38 |
| C1 | 9/25 | 23/70 |
| C3 | 0/12 | 11/44 |
| C3r2 | 15/30 | 2/19 |

**Reading.**
- There is a mild excess for χ₆ = 0 within length bands.
- It **reverses** within C3 and is mostly arm composition (C3r2 is mostly χ₆ = 0 and breaks well). The numbers are small.
- **Not a usable target-level predictor.**

**By method (measured).**
- M2 T-blind: 22 breaks with χ₆ = 0 and 29 with χ₆ ≠ 0.
- **M2 v5: 3 of its 4 breaks have χ₆ ≠ 0.**
- A v5 pool has periods ≤ 5, so its cells carry charge 0. Those three proofs therefore got their period-≥7 cells from R2.5 itself.
- This agrees with the Validator's finding that T-blind certificate cells reach core period 16–72 from a pool with periods ≤ 7. This bears on §5.

## 2. Candidates

Costs are per word of length n (500–5000 letters), in tcgraph C++. P = the largest period considered (72 covers every certificate seen).

### C1. Origin-tagged consumption (trace feature)

**Definition.**
- Carry an origin tag on every letter of q: from w, from u, or generated by an R2.5 step.
- Free cancellation deletes tagged letters; an R2.5 step deletes the letters of x^k and writes new letters tagged "generated".
- Record two quantities along the trace: **ω(t)**, the w-letters still present after step t, and **cascade depth**, the length of the longest chain of steps whose site overlaps letters generated by an earlier step.
- Report both at **absolute** trace prefixes, after s = 10, 20 and 50 steps and after t = 1/10 of the per-call CPU cap, and at the end.
- The prefixes must not be fractions of the total step count. That count is known only at the end and is itself correlated with emptying, so fractions would leak the outcome, and they are unusable for stopping mid-run.

**Cost.** A constant factor on R2.5 (one byte per letter, copied with the rewrite). No extra pass.

**Why in B(2,5) (conjectured).**
- Net length mixes three things: w's letters being consumed, u's letters, and generated letters.
- Collapse means all of w is consumed. An attempt that eats 80 % of w and leaves u-material looks the same by length as one that leaves w untouched, but it is a different state.
- The bimodality (a target is emptied by hundreds of different u or by none) suggests collapse is a **cascade**: once some step fires near the seam, its generated letters complete new runs, and so on.
- Cascade depth measures this directly.

**Test.**
- Within each broken target, the per-target AUC (area under the ROC curve; 0.5 = no signal) of ω/|w| and of cascade depth at s = 20 steps, for "attempt empties".
- Compare against the same AUC for |q|/|w| and lcf.

### C2. Near-fireable run profile and move spectrum (state feature)

**Definition.**
- For each period p ≤ P, take the maximal runs of x and their exponents e.
- Report **N₂(p)**, the letters covered by near-fireable runs (2 ≤ e ≤ 2.5), and **N₁.₅(p)**, the same for 1.5 ≤ e < 2.
- Report the **move spectrum**: a histogram of the costs Δ = (5 − 2e)p of the uphill and length-neutral steps available.
- Exponent exactly 2.5 gives Δ = 0, a length-neutral half swap, which exists only for even p.
- This is also the "period spectrum" of the word.

**Cost.**
- O(n·P) by scanning x[i] = x[i+p] for each p, which is about 3.6·10⁵ comparisons at n = 5000.
- Or O(n) with a runs algorithm (Kolpakov–Kucherov, GK).
- Microseconds to milliseconds.

**Why in B(2,5) (argued for the mechanism, conjectured for the prediction).**
- R2.5 fires only at e > 2.5. A near-fireable run is one cheap uphill step away from firing, and that is the half of v⁵ the relator gives.
- A word with a large N₂ mass sits next to many cascades. A word with none can collapse only through a new insertion.
- On the target w, this is the natural **target-level** signal ("one trigger away from a cascade").
- On q, it is the natural **attempt-level** signal before R2.5.
- The spectrum also lists the **uphill moves themselves**: x^e → x^{e−5} at cost ≤ p. These are certified peak-walking moves for a beam, at any period up to 72, without a pool. They cover the near-relator idea and the 2.5-half idea from the task.

**Test.**
- Attempt level: AUC of N₂ (total, and in bands p ≤ 7, 8–20, > 20) on q, for "attempt empties".
- Target level: N₂(w)/|w| within length bands, broken vs not.
- Peak walk: the rollout sample of §4.

### C3. Early-trace slope, for pruning (trace prefix)

**Definition.** The fraction of |q| removed after the first s = 10, 20 and 50 steps, and after t = 1/10 of the per-call CPU cap, together with C1's ω at the same prefixes. All prefixes are absolute (see C1).

**Cost.** Free.

**Why (conjectured).**
- If emptying attempts already separate early, R2.5 can be **stopped early** on hopeless attempts.
- That directly attacks E4 finding (4): R2.5 cost grows as n^3.1, so only about 30 attempts fit on words above 800 letters.
- This candidate is for **budget** more than for reward.

**Test.**
- The ROC of the prefix values (s = 10, 20, 50; t) within broken targets.
- Read off the CPU saved at a cut that keeps ≥ 95 % of emptying attempts.

### C4. Common factor with the emptying library (state feature)

**Definition.**
- The **library** is every u that emptied some target, plus the intermediate words of the 62 certificates, all trivial with certificates.
- Build one generalised suffix automaton over the library and its 16 images.
- For a word x, report the longest common factor of cyclic x with any library word, and the coverage by the k longest disjoint matches (I1's cov_k).

**Cost.**
- Building the automaton is linear in the library size (an estimated 10⁶–10⁷ letters).
- A query is O(n).

**Why (conjectured).**
- If two targets come from the same arm and parameters, a u that emptied one probably shares structure with the other.
- This is both a predictor and a **pool source**, since library words are trivial and can be inserted directly.
- **Confound:** it mostly measures "same arm as a broken word", which is already correlated with breaking.

**Test.**
- Leave-target-out: the library is built without the target and its emptying u.
- Report the target-level AUC within arm and length band, and whether library u beat T-blind u at equal attempts.
- **Track note:**
  - The emptying u are T-blind pool words (products of conjugates of v⁵), so the **u-library** can be reused in T-blind.
  - The intermediate words of the certificates come from other benchmark words, so the **residual library** is a T-out-like pool, not T-blind.

### C5. Integral exponent-sum lower bound on period mass (state feature)

**Definition.**
- For a proof x = Π g_i v_i^{±5} g_i⁻¹, the exponent sums satisfy e(x) = 5·Σ ±ℓ(v_i), and |ℓ(v)|₁ ≤ |v|.
- So the **total period mass** of any proof's cells is at least **κ(x) = (|e_a(x)| + |e_b(x)|)/5**, that is Σ|v_i| ≥ κ(x). No bound on the periods is needed.
- With the signed (Heisenberg) area, the same argument gives a second bound (I1 M4).

**Cost.** O(n).

**Why.**
- κ never overestimates (argued), so it is the only candidate here that gives a certified lower bound on the remaining work.
- It is probably weak: a proof can meet it with a few long cells, and R2.5 uses periods up to 72.

**Test.** Attempt-level AUC of κ(q)/|q| and of the area bound. Cheap enough to log anyway.

### Ranked low or not recommended

- **Whitehead complexity** (Whitehead-minimal length / length) and **Whitehead graph cut size.**
  - After the loop, every end word has just been through W, so the ratio is about 1 everywhere: no variance (argued).
  - In F₂ the Whitehead graph is determined by the cyclic bigram counts, which is length-2 information.
  - E2 and E3 together gave 4 breaks. Log the ratio on q as a control only.
- **χ₆ charge.** Negative at target level (§1). It stays useful as an exact constraint, not as a predictor: the residual charge is exactly χ₆(w) − χ₆(u) − (charges of R2.5's cells), so it is free to log. A residual with χ₆ ≠ 0 can be emptied only by a cell of period ≥ 7, which R2.5 supplies anyway.
- **Free-group distance to the subgroup generated by short relators.**
  - The right object is the *normal* closure, and distance to it is the word problem itself, so it is not computable as a score.
  - The ordinary subgroup's Stallings graph (the folded graph of a finitely generated subgroup) ignores the conjugators, which are essential: R2.5's cells have unrestricted conjugators.
  - Its useful content, "pieces of x close to v^{±5}", is exactly C2.

## 3. Top 5

1. **C2, the near-fireable run profile and move spectrum.** Cheapest; it fits the B(2,5) mechanism (the 2.5 half); it works at both levels; it also supplies peak-walking moves.
2. **C1, origin-tagged consumption and cascade depth.** It separates progress on w from length.
3. **C3, early-trace slope.** Mainly to prune R2.5, which buys attempts on long words.
4. **C4, common factor with the emptying library.** A predictor and a pool, with a confound to control.
5. **C5, the exponent-sum lower bound on the proof's period mass.** Certified and cheap, but probably weak.

## 4. Test protocol on A's data, stated before the data

**Primary test (attempt level, broken targets).**
- For each feature f and each broken target, compute the AUC of f for "attempt empties", over all of the target's attempts.
- Report the median over targets.
- Report the same for the baseline features |q|/|w| and lcf.
- f is **useful** if its median AUC is ≥ 0.05 above the better baseline, and above it in ≥ 2/3 of the targets.
- Also report **AUC within baseline deciles**: the AUC of f inside bins of |q|/|w|. This shows information beyond length.

**Secondary test (target level).**
- AUC of f(w) for "broken", within length band × arm cells, pooled with stratum weights.
- Bands with no breaks (≥ 800 letters) are excluded and reported as "no information".

**Peak-walk test (rollouts; the owner's hypothesis).**
- Take a random sample of non-empty residuals r from broken and from unbroken targets, for example 200 per length band.
- From each, run a second insertion round with n attempts at the E4 settings, and label r "on a path" if any attempt empties it.
- Compare with f(r) against the baseline |r|.
- **This is the only test that checks whether a longer r can be "closer" than a shorter one.**
- The rare-event rule applies: any emptying is a break and goes to verification at once.
- **Cost at the current R2.5** (rough): with n = 30 attempts per residual and 200 residuals per band, about 50 CPU-h per band below 800 letters (about 30 s per call), and about 200 CPU-h at 800+ letters (125 s cap).
- That is about $10–15 on cpuserver for all bands. A first pass with 50 residuals per band costs about a quarter of that, and seam-local R2.5 (§6) would cut it a lot.

**Rare-event reading.**
- What matters is ranking power at the top: whether ranking by f puts an emptying attempt in the first N.
- Report **hit@N** (N = 30, the long-word budget) next to the AUC.

## 5. What A must log per attempt

E4's m2_inputs.jsonl has 194,815 attempts but **no R2.5 outcome**. Only the 8,263 shortenings carry an output. Without this, none of §4 can be computed.

**Per attempt:**
- target id; attempt id; track/pool; u's cells (period and conjugator length for each); |u|;
- chosen rotation and image; lcf; |q|;
- the **R2.5 trace**, one record per step: period, k, Δ, position, CPU time so far, plus ω and cascade depth if C1 is on;
- final length and outcome (empty, shorter, not shorter); CPU time;
- the features C2 (on q), C3 (at the absolute prefixes), C4 and C5 (on q), and the Whitehead ratio (control).

**Per target:** the features C2, C4 and C5 on w, plus the χ₆ of w (from E1).

**Size:** the trace dominates. At about 100–700 steps × 16 bytes per attempt, 2·10⁵ attempts come to about 1 GB uncompressed. Use a binary or compressed per-target file.

## 6. Pool periods (|v| up to 10–12) for long words

**Exactness: no reason to add long periods (argued from measured data).**
- v5 (periods ≤ 5) matched T-blind on the short words: 95,283 vs 95,307 M2 reductions, and 4 breaks came first from v5.
- 3 of v5's 4 breaks have χ₆ ≠ 0 (§1), so R2.5 itself supplied the period-≥7 cells those proofs need.
- T-blind certificates reach core period 16–72 from a pool with periods ≤ 7.
- **Long periods come from R2.5 cascades, not from the pool.**

**Alignment: open, worth one controlled arm.**
- Longer cells make longer u, which may give longer lcf alignments on long words.
- But a cell of period 12 is 60 letters, and u gets 180–500+ letters. That raises |q| and the n^3.1 R2.5 cost, so fewer attempts fit.
- **Proposal:** a small arm with periods 8–12, on targets of ≥ 500 letters, at **equal R2.5 CPU** (not equal attempt count) against T-blind. Report verified shortenings per CPU-hour and the §4 features.
- **Cheaper alternative (conjectured to be better):** C2's run-seeded uphill moves reach any period up to 72 from the word's own near-fireable runs, at cost ≤ p letters, with no pool.

**For long words the binding limit is attempts, not periods (argued).**
- The loop end words are R2.5 fixpoints, and the w-part of q is a factor of cyclic w. So every reducible factor of q starts inside u′ or across a seam, and every later step lies next to a changed region.
- A **seam-local R2.5** (a worklist that re-scans only windows of radius about 2.5·P around changes) finds the same possible steps as a full scan. It costs roughly O((|u| + cascade size)·P) instead of n^3.1.
- Its step order may differ from the current implementation, so its outputs may differ, but each is a valid certified reduction.
- It may raise the attempt count on 800+ letter words by orders of magnitude, which is more than any pool change (conjectured; the Developer would measure it).

## 7. Recommendation

- In A: log §5 in full, compute C1, C2, C3 and C5 inline (all cheap), and C4 offline.
- Run the §4 tests before any learning. They decide which features go into the beam's reward next to length.
- **Before A on long words:** ask the Developer to measure a seam-local R2.5 (§6). It addresses E4 finding (4) directly.
- Use the long-period pool only as the equal-CPU arm of §6.

**Open:**
- whether near-fireable runs are common in the 138 words at all (C2 on w answers this in seconds);
- whether the current R2.5 allows length-neutral half swaps (Δ = 0, even p);
- the peak-walk hypothesis itself (§4 rollouts).

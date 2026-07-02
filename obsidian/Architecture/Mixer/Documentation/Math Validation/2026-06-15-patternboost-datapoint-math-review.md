---
title: PatternBoost BurnsideDataPoint — Math Layer Review
status: mixed (see per-item verdicts)
domain: group-theory
project: b25-patternboost
claim: BurnsideDataPoint.calc_score() reduction ratio is a sound training signal for PatternBoost on B(2,5); _braid_reduce non-abelian inverse formula is correct; tokenization {a,b,A,B}→{0,1,2,3} is sound.
claimant: Developer (feat/burnside-datapoint patch, 2026-06-15)
verification_method: algebraic derivation + Python simulation + computational test cases
tools_used:
  - Python 3.x (datapoint.py functions replicated inline)
  - algebraic derivation from B(2
  - 5) group axioms
author: maumayma
tags:
  - agent/validator
  - domain/group-theory
  - project/b25-patternboost
  - status/mixed
  - proof
  - user/maumayma
---

# Verification — PatternBoost BurnsideDataPoint Math Layer

Routed from Lead as math-layer review in parallel with code review, branch `feat/burnside-datapoint`.
Code read: `experiments/burnside/b25_patternboost/datapoint.py` (2026-06-15 state).

---

## ITEM 1 — Score Proxy (P3/P4): reduction ratio as training signal

### The claim
High reduction ratio after one braid+power pass via Rust `--no-beam` correlates with a word being structurally closer to identity in B(2,5), and is therefore a sound training signal for PatternBoost.

### Verdict
**#status/disproven** for the "correlates with proximity to identity" interpretation.
**#status/conjectured** for the weaker "useful training signal for finding reducible words."

### Evidence

**Concrete counterexample (computationally verified):**

```
w = 'aaaaabbbbbab'   (length 12)
full_reduce(w) = 'ab'  (length 2)
score = (12 - 2) / 12 = 0.8333
```

The word `aaaaabbbbbab` represents the group element `a^5 · b^5 · ab = e · e · ab = ab` in B(2,5).
The element `ab` has abelianization `(1,1) mod 5` — non-zero, so it is provably NOT the identity.
Yet it scores 0.83, close to the maximum.

More extreme: `a^25 b^25 ab` (length 52) reduces to `ab`, scoring **0.9615** — while representing the same non-identity element `ab`.

This definitively disproves the claim. High reduction ratio rewards the PRESENCE of consecutive power-5 subwords (`a^5=e`, `b^5=e`) in the word, not algebraic proximity to identity. A word can consist of 95% identity-padding followed by a non-trivial residual and score arbitrarily close to 1.0.

**What Option B actually measures:** Density of exploitable power/braid structure in the word as written, not algebraic distance from identity.

**Is Option B useless?** No — but the semantics matter:
- If PatternBoost wants to learn "words with reducible structure" → Option B is acceptable as a signal.
- If PatternBoost wants to learn "words that are close to the identity element in B(2,5)" → Option B is wrong; it will heavily reward padded-identity words over genuinely interesting near-identity constructions.

**Is Option A (rule-match count against KB rule bank) more principled?**
YES, for a complete KB bank. Each KB rule is a certified algebraic reduction step in B(2,5). The rule-match count measures how much of the B(2,5) word problem's solution structure is present in the word — a more direct measure of algebraic richness. For a partial KB bank (14.2M rules, not necessarily complete for B(2,5)), it measures "reducibility under the current partial KB," which is still more algebraically meaningful than one-pass reduction ratio.

**Is there a better proxy not yet considered?**
Two candidates:
1. **Abelianization norm as pre-filter**: Map `w` to Z/5Z × Z/5Z by counting generator exponents mod 5. Words with non-zero abelianization are provably non-identity with no KB needed. Cheap to compute, mathematically grounded. Can be used as a tier-1 filter: words scoring `(0,0)` on abelianization are "potentially interesting."
2. **Full KB-reduced length**: Iterate all matching KB rules to fixpoint, not just one pass. Directly answers "how much of B(2,5) structure does KB find?" But computationally expensive.

### BLOCKING VERDICT
The code comment on `calc_score()` already says "PENDING B25 Experimenter sign-off." This is correct. **This item must be resolved (Option A, B, or alternate) before merge.** The mathematical question is not whether Option B computes what it says it computes (it does), but whether what it computes is what PatternBoost needs.

---

## ITEM 2 — Python Reducer vs Rust Binary Parity (P5/P6)

### 2a — Coverage gap

**Claim:** Python `_braid_reduce()` is "slightly less accurate for highly structured words."

**Verdict: #status/disproven** — the divergence is categorical, not a matter of degree.

Python handles only pure two-generator alternating runs: `g h g h g h ...` of length ≥ 6.

The Rust binary handles a strictly larger class. Concretely verified:

```
w = 'ababaababaababaababaababa'  # (aba)^5, length 25
Python full_reduce(w) = 'ababaababaababaababaababa'  # unchanged, score = 0.0
```

In B(2,5), every element has order dividing 5. Therefore `(aba)^5 = e` — this 25-character word IS the identity. The Python reducer scores it 0.0; the Rust binary (which handles the generalised braid shortening search) should reduce it to `''` with score 1.0.

This is not "slight inaccuracy." For the class of words built as `(ghg)^5` or longer multi-generator commutator products, Python produces **categorical score of 0.0 on words that are actually the identity**. The code comment at line 387 ("slightly less accurate") under-describes the gap.

**Impact on the training loop:**
- `_batch_generate_and_score` calls `batch_score()` (Rust) for final scores → training data scores are accurate.
- `local_search()` uses `_python_reduce()` → local search gets stuck on multi-generator identity words, failing to explore them.
- `batch_score_fast()` (Python) for hot-path scoring → systematically under-scores complex words in any path that calls it.

The Python/Rust split creates **score inconsistency** between `local_search()` feedback and `calc_score()` evaluation for exactly the most algebraically interesting words. This is worth flagging to Lead but is not a math correctness error in the formulas — it's a coverage limitation.

### 2b — Non-abelian inverse formula

**Claim:** `k_mod=3: (gh)^3 = (HG)^2`; `k_mod=4: (gh)^4 = HG` where `H=h^{-1}`, `G=g^{-1}`.

**Verdict: #status/proven**

**Algebraic derivation** (from B(2,5) axioms only, no computation needed):

In B(2,5), every element has order dividing 5. For any elements g, h: `(gh)^5 = e`.

Therefore:
```
(gh)^3 = (gh)^{5-2} = (gh)^{-2} = ((gh)^{-1})^2 = (h^{-1}g^{-1})^2 = (HG)^2   ✓
(gh)^4 = (gh)^{5-1} = (gh)^{-1} = h^{-1}g^{-1} = HG                            ✓
```

Both identities follow purely from `(gh)^5 = e` and the group axiom `(xy)^{-1} = y^{-1}x^{-1}`. No B(2,5)-specific structure beyond the exponent-5 relation is used.

**Computational confirmation:**
```python
full_reduce('ababab')   # (ab)^3 -> 'BABA'   = (BA)^2 ✓
full_reduce('BABA')     # (BA)^2 -> 'BABA'   same normal form ✓
full_reduce('abababab') # (ab)^4 -> 'BA'      = HG ✓
full_reduce('ababababab') # (ab)^5 -> ''       = e ✓
```

The original bug (`GH` instead of `HG`) used the abelian inverse. The corrected formula is proven correct. See [[2026-05-22-comm-12-9-7245-final]] for the history of this fix.

**Implementation in `_braid_reduce()` (lines 139–142):**
```python
elif k_mod <= 2:
    repl = (g + h) * k_mod
else:
    repl = (INVERSE[h] + INVERSE[g]) * (5 - k_mod)
```
- `k_mod ∈ {1,2}`: `(gh)^k_mod` — correct.
- `k_mod ∈ {3,4}`: `(HG)^(5-k_mod)` = `(HG)^2` for k_mod=3, `(HG)^1` for k_mod=4 — correct.
- Note: `INVERSE[h] + INVERSE[g]` = `HG` (correct non-abelian order; `h^{-1}` then `g^{-1}`). ✓

The tail handling (`repl += g` when `has_tail`) is also correct: `(gh)^k · g = [(gh)^k \bmod{(gh)^5=e}] · g`.

---

## ITEM 3 — Tokenization

### The claim
The assignment `a=0, b=1, A=2, B=3` is a mathematically sound tokenization.

### Verdict: #status/proven

**Is the ordering arbitrary from a math standpoint?** YES — any bijection from {a,b,A,B} to {0,1,2,3} is equally valid. Transformer embeddings are learned; the initial integer assignment has no mathematical content.

**Does the current encoding have exploitable structure?** Mildly. The current scheme:
- Lowercase generators: {0, 1} (a, b)
- Uppercase inverses: {2, 3} (A, B)

The inverse of token `t ∈ {0,1}` is at `t+2`. This is a consistent offset relationship that the transformer may learn to exploit via attention patterns. The alternative `a=0, A=1, b=2, B=3` (pair-adjacent) also has consistent structure (inverse of token `t` is at `t XOR 1`).

**The negation encoding (a=1, A=-1)** is not feasible with standard embedding lookup tables and would require architectural changes. Not a drop-in alternative.

**No mathematical reason to block merge on tokenization.** BPE exclusion (noted in code: "Non-abelian group structure requires order preservation — BPE is wrong") is **correct** — character-level tokenization preserving order is the right choice for a non-abelian group, since merging tokens would destroy the word structure that the transformer must learn.

---

## Summary Verdict

| Item | Claim | Verdict | Blocks merge? |
|------|-------|---------|---------------|
| 1. Score proxy (P3/P4) | Reduction ratio ↔ proximity to identity | **#status/disproven** | Resolved — see Addendum |
| 2a. Python coverage (P5/P6) | "Slightly less accurate" gap description | **#status/disproven** | No (known limitation; code uses Rust for final scores) |
| 2b. Non-abelian inverse formula | `(gh)^3=(HG)^2`, `(gh)^4=HG` | **#status/proven** | No — math is correct |
| 3. Tokenization | `{a,b,A,B}→{0,1,2,3}` sound | **#status/proven** | No |

---

## Addendum — B25 Reframing of Item 1 (2026-06-15)

B25 Experimenter acknowledged the `#status/disproven` verdict and narrowed the claim. The merge block is resolved for STEP 1 (skeleton commit only); proxy wiring deferred to STEP 1.5.

### Narrowed claim (B25 Experimenter)
For genuine B(2,5) commutator words (abelianization `(0,0) mod 5` verified), high braid+power reduction ratio in ONE PASS correlates with how much further the word can be reduced by extended KB rule application.

Restricted domain: the 54 actual training words (comm_12_9, comm_13_10, etc.) — not arbitrary (0,0)-class words.

### Revised verdict: #status/conjectured

**Why not #status/disproven:**

The original counterexample (`aaaaabbbbbab`, score 0.83, element `ab`) has abelianization `(1,1)` — excluded by the (0,0) restriction. A second counterexample was constructed within the (0,0) class:

```
w = (ab)^5 * [a,b]  =  'ababababababAB'  (length 14)
abel(w) = (0, 0)   ✓
score    = 0.714
residual = 'abAB'   (= [a,b], length 4, likely KB-irreducible)
```

This is a valid (0,0)-class word with high one-pass score but a residual that the KB bank would make zero further progress on (4-char commutator already in normal form). **However:** this word is synthetic (prepend `(ab)^5` to a commutator). B25's actual training set does not contain words structured this way — they are large commutators produced by algebraic computation, not by prepending identity padding. The counterexample is valid in the abstract class but absent from the specific 54-word training set.

**Why not #status/proven:**

The mathematical relationship between one-pass braid+power ratio and further KB reducibility for large natural commutator words has not been measured or proven. These are different types of structure: local power/alternating-run patterns vs. KB rule matchability.

**Scope of the conjecture:** RUST-based score only. The Python `batch_score_fast()` has a categorical coverage gap (see Item 2a) — the `#status/conjectured` rating does not extend to the Python-based score.

**Practical recommendation for STEP 1:**
- Use `batch_score()` / `calc_score()` (Rust backend) as the training signal, not `batch_score_fast()`.
- During STEP 1 data collection, log Rust score vs. Python score divergence for the actual training words to quantify the Python gap for this specific word class.
- If STEP 1 shows poor training outcomes, revisit Option A (KB rule-match count) as the signal.

---

## Notes for downstream agents

**Lead:** Item 1 block resolved by B25 narrowing the claim. STEP 1 skeleton commit can proceed; STEP 1.5 (wiring Rust Option B score) proceeds once B25 pre-registration is confirmed.

**B25 Experimenter:** Verdict is `#status/conjectured` for the narrowed claim. Proceed with Option B for STEP 1. Empirical correlation on actual training words would support the conjecture but requires multiple independent runs before upgrading to `#status/replicated` — see correction addendum below.

**Developer:** The `_braid_reduce` formula is mathematically correct — no changes needed there. The Python coverage gap (cannot handle `(aba)^5`-type identities) may be worth documenting more precisely than "slightly less accurate." Consider updating the code comment at line 387 to reflect the categorical nature of the gap.

---

## Correction — Maria Rejected #status/replicated Upgrade (2026-06-16)

In the STEP 1.5 sign-off response, Validator incorrectly suggested that Pearson r=0.949 (n=49) could upgrade the narrowed claim to `#status/replicated`. Maria rejected this. **Status remains #status/conjectured.**

### Supporting evidence on record (not sufficient for replication)

- Deliverable #1: Pearson r=0.949, p=3.3e-25, n=49 on the STEP 1.5 cohort.
- This is ONE run, not multiple independent runs. `#status/replicated` per [[tags]] requires multiple independent runs that agree.

### Why this evidence is insufficient

1. **Single run**: One measurement is not replication. Replication requires multiple independent runs from separate seeds or independent agents.
2. **Partial cohort**: The n=49 cohort EXCLUDED approximately 51 words that scored `rust_ratio=0.000` (genuine zero-reduction, not timeouts), including compressible words up to `bench_ratio=0.726`. The correlation was measured on a cohort that omits the proxy's known failure mode.
3. **Consistency with Item 1 #status/disproven**: The ~51 zero-scoring-but-compressible words are the real-data manifestation of the Item 1 disproof (high reducibility in reality, zero score under Option B). Upgrading on a cohort that omits these words would be invalid.

### Corrected status

**#status/conjectured** — single-run supporting evidence (r=0.949, n=49), partial cohort (~43% of word space not scored by proxy), proxy blind on zero-reduction words that are genuinely compressible.

**Condition to upgrade to #status/replicated**: Multiple independent runs (separate seeds and/or independent agent) on the full training set (including zero-ratio words) showing consistent correlation. The ~51 excluded words must be accounted for, not omitted.

Verified by [[2026-06-15-patternboost-datapoint-math-review]]

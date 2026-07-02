---
title: compressed-kb-option-a-biased-2026-06-23
domain: group-theory
project: b25
instance: B(2,5)
experiment_type: compressed-kb
status: pending
registered_on: 2026-06-23
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/knuth-bendix, topic/kbmag, topic/word-problem, project/b25, status/pending, methodology]
---

# Experiment — Compressed-Alphabet KB Option (a): Biased Run on Compressed Target

## Authorization

Authorized by Lead as OPTION (a), 2026-06-23. Builds on:
- First-run probe (20260623_161047): unbiased, 200K rules, NO-GO — 0 m/M-in-LHS rules fired on compressed target.
- Validator soundness verdict: [[b25-compressed-kb-soundness-verdict]] — SOUND with step-4 gate.
- Part-4 reconciliation: k=4..6 shortlex boundary patterns; core-scale (35-char) raw biasing NOT viable; compression is the route.
- Track A fix landed on origin/main (PR #22, dee9b98): injection-OOB fix merged.

## Hypothesis

Biasing kbprog on the **compressed form** of word_7245 (2,077 chars in {a,b,A,B,m,M}) with k=5, sp=0.5 will generate rules with m/M in their LHS that:
1. Appear as substrings of the compressed target word.
2. Achieve length reduction in the compressed domain (|LHS| > |RHS|).

The first-run baseline (unbiased) generated 126 m/M-in-LHS rules, NONE of which appeared in the compressed word. Biasing toward the compressed word (which contains m and M as literal characters) should generate k-gram patterns bridging raw characters and the compressed symbols, producing rules that match exactly those boundary regions.

**Falsification condition**: if zero m/M-in-LHS rules fire on the compressed word with length reduction, the hypothesis is false. The baseline count of 18 "encoding rules" (m/M in RHS, delta=0) is not a success — firing must be in the compressed domain with delta < 0.

## Problem set

- Group: B(2,5), the free Burnside group on 2 generators of exponent 5.
- Target word: word_7245 = `experiments/b25_reduce_core/corrected/final_beam.txt` (7,245 chars, abelianization (0,0) confirmed, provenance: [[Reduce Core/methodology/reduce-core-pipeline-b25-2026-05-22]]).
- Compressed target: 2,077-char compressed form of word_7245 (76 m's + 76 M's + 1,925 raw chars).
- Presentation: `experiments/burnside/b25_bias_bidir/input/b25_compressed_core.kbmag` (6 generators {a,A,b,B,m,M}, 4435 total relators including full CoreA=m and CoreB=M definitions).

## Mixer agents involved

- kbprog from `kbmag_source/standalone/bin/kbprog` (fixed binary at dee9b98).
- Single agent, shortlex ordering (same as compressed presentation default).
- Biasing: `-sw <compressed_word_7245> -sk 5 -sp 0.5` (Part-4-reconciled k, moderate bias fraction).

## Modifications (B(2,5)-specific)

- Compressed 6-generator presentation (not standard B(2,5) 4-generator).
- Bias target is COMPRESSED word (2,077 chars) not raw (7,245 chars).
- k=5 chosen as Part-4-reconciled sweet spot (reconciliation: raw k≥8 disfavored; shortlex boundary patterns k=4..6 viable).
- sp=0.5 (50% of special equations biased toward target k-grams).

## Termination criteria

- kbprog `-me 200000` cap (same as baseline for comparability).
- Expected wall time: ~8-10 seconds (consistent with baseline and raw-alphabet runs at this cap).
- Report at cap.

## Baselines

- Unbiased run (20260623_161047): 199,555 rules, 126 m/M-in-LHS, 0 fire on compressed word, 18 fire on raw word (delta=0 only).
- Raw-alphabet biased agents (special-mixer-kb-l2r-rpo-0001): 2M rules, 27 applicable on word_7245 (0.00092%), 3 length-reducing.

## Seeds / variants

Single deterministic run (kbprog is deterministic given same input). Variants for results table:
- k=4 (broader patterns, more matches)
- k=6 (narrower patterns, potentially more specific)

## Anti-pattern checks

- **NOT measuring m/M-in-LHS rules against the RAW word**: Guard 2. Firing measured in compressed domain only (compress → apply → check length delta in compressed form).
- **NOT accepting rules without expansion check**: Guard 1. Every m/M-containing rule USED must pass φ(u)=φ(v) check (see § Guard implementations below).
- **NOT using abelianization as the equality check**: abelianization is a NECESSARY condition, not sufficient. The braid_reduce_fast bug failure mode was exactly this. Full expansion check required.

## Guard implementations

### Guard 1 — Full φ-equality check (beyond abelianization)

For each rule LHS→RHS with m/M in LHS that fires on the compressed target:
1. Expand: `lhs_raw = expand(LHS)`, `rhs_raw = expand(RHS)` (m→CoreA, M→CoreB).
2. Compute product: `product = lhs_raw + free_inverse(rhs_raw)`.
3. Free-reduce product (catches free-group tautologies immediately).
4. If free-reduces to empty → TRIVIALLY VERIFIED (free-group identity).
5. If non-empty → apply leftmost-match reduction with the 2M-rule raw B(2,5) bank (`special-mixer-kb-l2r-rpo-0001/kbmag/b25_test.kbprog.live`). Report whether result is empty (VERIFIED) or non-empty (INCONCLUSIVE).
6. Route result to Validator regardless of outcome (math claim requiring Validator verdict).
7. **Only apply the rule to the target if Validator returns #status/proven or #status/replicated.** GATE IS HARD.

Note: the structural soundness argument (full defs baked into kbmag input → automatic gate) is noted but not relied upon in place of the explicit check. Both the structural argument AND the explicit check are documented in the output note.

### Guard 2 — Compressed-domain firing

Apply rules to the COMPRESSED target word (2,077 chars). Check: does LHS appear as a substring of the compressed word? If yes, what is the length delta in compressed-form characters? Expand result only AFTER all compressed rules have been applied.

## Provenance triple

To be filled at run time.

| Item | Value |
|------|-------|
| git_sha | (at run time) |
| uv_lock_sha256 | (at run time) |
| kbprog_sha256 | (at run time) |

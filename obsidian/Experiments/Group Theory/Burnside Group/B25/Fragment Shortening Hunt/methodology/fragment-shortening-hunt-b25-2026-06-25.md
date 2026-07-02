---
title: fragment-shortening-hunt-b25-2026-06-25
domain: group-theory
project: b25
instance: B(2,5)
experiment_type: fragment-shortening-hunt
status: complete
date: 2026-06-25
author: maumayma
authorized_by: "Human directive — REOPEN + STEER (2026-06-25)"
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/word-problem, topic/knuth-bendix, topic/beam-search, project/b25, status/complete, methodology]
---

# Experiment — Fragment Shortening Hunt on B(2,5)

**Pre-registration**: authorized by human directive 2026-06-25 (REOPEN of Bridge Cancellation Line — full finite enumeration across all 119 words, all orientations, Y≠F allowed).

**Authorized revision (mid-session, same day)**: Human STEER — GAP reserved for exact-algebra verification only; `braid_reduce` Rust beam replaces GAP for all shortening search.

---

## Hypothesis

The CoreA/CoreB segment decomposition of B(2,5) benchmark words contains connector fragments that, in junction context (`CoreX · F · CoreY`), admit a shorter representative in B(2,5). A systematic enumeration of all 119-word connectors + junction tests will surface rewriting rules applicable across the corpus.

The hypothesis is falsifiable: if no junction reduces, no seed rules exist from this corpus. Partial confirmation: some junctions reduce, some do not; rules have heterogeneous applicability.

---

## Problem set

- **Group**: B(2,5), presentation `kbmag_source/standalone/kb_data/b25_gen` (4372 relators; |B(2,5)| = 5^34, class 12 — verified by GAP EpimorphismPGroup)
- **Corpus**: 119 benchmark words in `experiments/b25_reduce_core/runs/b25-reduce-core-benchmark-0001/data/best_words/` (comm_4_2 through comm_9_8; lengths 2,496–27,340 chars)
- **Target**: all connector fragments between CoreA/CoreB occurrences; all 8 orientation types (A→B, B→A, A→A, B→B, PREFIX→A, PREFIX→B, A→SUFFIX, B→SUFFIX)
- **CoreA**: `ABabAbabABaBAbabABABabAbaBABaBAbabb` (35 chars)
- **CoreB**: `BBABabAbabABaBAbabaBABabAbaBABaBAba` (35 chars)

---

## CoreA/CoreB decomposition algorithm

```python
CORE_A = "ABabAbabABaBAbabABABabAbaBABaBAbabb"
CORE_B = "BBABabAbabABaBAbabaBABabAbaBABaBAba"

def decompose(w):
    segs = []; i = 0; last = 0
    la, lb = len(CORE_A), len(CORE_B)
    while i < len(w):
        if w[i:i+la] == CORE_A:
            if i > last: segs.append(('frag', w[last:i]))
            segs.append(('A', CORE_A)); last = i+la; i = last
        elif w[i:i+lb] == CORE_B:
            if i > last: segs.append(('frag', w[last:i]))
            segs.append(('B', CORE_B)); last = i+lb; i = last
        else: i += 1
    if last < len(w): segs.append(('frag', w[last:]))
    return segs
```

Orientation assigned by the core types immediately left and right of each fragment. Edge cases: `None` left = PREFIX, `None` right = SUFFIX.

---

## Methods

### Method 1 — 500K shortlex KB bank (primary)

**Source**: `/tmp/b25_slex_large.kbprog.live` — 499,864 shortlex rules, max LHS length 34 chars. Generated from prior KBMag experiment-type runs.

**Application**: leftmost fixed-point string rewriting, longest-LHS-first ordering (ensures longest applicable rule fires at each step). Applied to each junction word `CoreX · F · CoreY`.

**Key property**: 50K bank (49,576 rules) and 500K bank give **identical results** — 31/326 reductions at both sizes. This demonstrates the applicable rules are in the long-tail of the 50K bank, not in the additional 450K rules. No new reductions from the larger bank.

### Method 2 — braid_reduce beam search

**Binary**: `experiments/burnside/burnside_bidirectional/target/release/braid_reduce` (compiled at `5aeee6a`)

**CLI invocation**: `--word-file <input> --rules-file <bank> --beam-width 16384 --beam-secs <T>`

**Rule loading**: parses `->` separator (no spaces), deduplicates by LHS, orients so LHS is longer, sorts by shortening descending. Forward rules (LHS→RHS where |LHS|>|RHS|) + braid shortenings (non-monotone exploration).

**Per-case budgets**:
- word_7245's 9 junction words: **60-second** budget each
- Top-5 most frequent non-reducing junctions (occ = 590, 577, 235, 233, 47): **120-second** budget each
- Long connector fragments alone (len > 12): **5-second** budget each
- Full word_7245 (7,245 chars): **3 passes × 300-second** budget

### Method 3 — k=12 BFS (bounded word search, exact)

Run in prior session (Bridge Cancellation Line). For all fragments of length ≤ 12, exhaustive BFS over the shortlex KB is complete — it finds the shortlex normal form exactly. All 9 fragments in word_7245 (max length 11) and all corpus fragments of length ≤ 12 confirmed in shortlex normal form.

**Scope**: confirms no shorter representative of length ≤ 12 exists for these fragments. Does not cover fragments of length > 12.

### Method 4 — GAP word-equality (verification only)

**Tool**: GAP 4.15.1 with anupq package; `EpimorphismPGroup(G, 5, 12)` where G is the FP group with 4,372 B(2,5) relators.

**Role**: reserved for EXACT-ALGEBRA verification only (per human STEER directive). GAP was NOT used for the shortening search itself — only to verify that each candidate reduction is a valid B(2,5) word equality.

**Verification protocol**: for each candidate junction reduction `L → R`, verify `Image(phi)(L) = Image(phi)(R)` in the PcGroup (order 5^34). `match=True` for all 31 rules.

**Why not abelianization**: abelianization is blind on the commutator subgroup — all benchmark words comm_i_j have abelianization (0,0), so abelianization cannot distinguish identity from non-identity among these words. Full GAP word-equality is mandatory.

---

## Termination criteria

- Fragment enumeration: complete when all 119 words have been decomposed (finite corpus, exact)
- Junction tests: complete when all 326 junction words have been tested under both methods
- k=12 BFS: exact for length ≤ 12 (complete)
- Beam: time-bounded per case (60s/120s/300s as above); not guaranteed complete
- GAP verification: run on all 31 candidate reductions; not run on null results

---

## Anti-pattern checks

- **Hill-climbing on a single target**: junction tests span ALL 119 words. word_7245 is specifically flagged and its null result is explicitly recorded and not generalized.
- **Compression collisions**: not applicable (no compression in this experiment).
- **Abelianization as proxy**: explicitly forbidden; GAP full word-equality used.
- **Ordering changes**: all tests use the same shortlex bank; beam uses its own internal ordering (not a KB ordering). No implicit ordering changes.
- **Cherry-picking**: the 31 rules are ALL reductions found; null results are explicitly listed (295 non-reducing junctions).

---

## Baselines

- **Bridge Cancellation Line (prior session)**: tested 17 specific bridge patterns in word_7245 (`CoreA · X · CoreB → X`). All 17 confirmed non-reducing (commutators with CoreA have order 5). This experiment EXTENDS that: (a) all 119 words, not just word_7245; (b) all orientation types; (c) Y ≠ F allowed; (d) beam search added.
- **50K vs 500K bank comparison**: both give identical 31/326 reductions. Documents diminishing returns from larger KB banks.

---

## Provenance

| Item | Value |
|------|-------|
| git_sha | `5aeee6a90275c5583d367e534e2ded952dbfe545` |
| branch | `feat/compressed-alphabet-kb` |
| seed_rules_sha256 | `341c64bcc63fb89e18f43c78a8cc475983e20b6f6e4b521a033c511841002499` |
| run_dir | `runs/b25/fragment_seed_rules/20260625_235828/` |
| GAP_version | 4.15.1, anupq package |
| beam_binary | `experiments/burnside/burnside_bidirectional/target/release/braid_reduce` |
| rule_bank | 499,864 shortlex rules, max LHS 34 chars |

---

## Results summary

See [[Fragment Shortening Hunt/results/results]] for the full per-word table and ranked rule list.

- **318 distinct connector fragments** enumerated from 119 words
- **326 junction tests** (fragment × orientation pairs where that orientation exists in the corpus)
- **31 seed rules** confirmed: 31 junction-level reductions, all GAP word-equality verified
- **word_7245 (comm_12_9)**: delta=0 at all methods tested (KB, beam ≤300s×3, k=12 BFS). Upper bound only — not an irreducibility claim.
- **37 other words**: 648 total chars saved from the 31 rules
- **0 new reductions** from beam beyond the 31 from KB

---

## Open questions / untested variants

The following have NOT been tested and are explicitly NOT closed:

1. **Longer beam (>300s) on word_7245 junctions**: the 300s budget is a practical cap, not an exhaustion bound. Longer beam with more passes could surface reductions that 300s misses.
2. **Junction tests beyond the 500K bank**: the bank contains rules with max LHS 34 chars. If the reduction requires a rule with LHS > 34, it will not be found here.
3. **Nested junction contexts**: this experiment tests fragments in `CoreX · F · CoreY` context. Multi-core contexts (`CoreX · F · CoreY · G · CoreZ`) are NOT tested — a reduction may exist only in the presence of additional flanking cores.
4. **Orientation-extended junctions**: only orientations actually observed in the corpus are tested. Hypothetical orientations not appearing in any of the 119 words are not covered.
5. **Rules from other rule banks** (RPO, wtlex, biased banks): the 500K bank is shortlex-only. RPO and wtlex banks could contain different junction reductions not captured here.
6. **word_7245's 9 connectors with wider beam or more passes**: all 9 return delta=0 at beam width 16384, up to 300s per pass. Not irreducible — beam width and time are practical limits.

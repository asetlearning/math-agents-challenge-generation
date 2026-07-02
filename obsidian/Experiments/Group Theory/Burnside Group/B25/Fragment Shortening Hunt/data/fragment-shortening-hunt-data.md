---
title: Fragment Shortening Hunt — Data
domain: group-theory
project: b25
instance: B(2,5)
experiment_type: fragment-shortening-hunt
date: 2026-06-25
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, project/b25, data]
---

# Fragment Shortening Hunt — Data

Source: `runs/b25/fragment_seed_rules/20260625_235828/` (per_word_results.json, seed_rules.json)

---

## Corpus summary

| Item | Count |
|------|-------|
| Benchmark words | 119 |
| Length range | 2,496–27,340 chars |
| Distinct connector fragments found | 318 |
| Junction test cases built | 326 |
| Junctions that reduce (KB or beam) | 31 |
| Junctions with null result | 295 |

---

## Orientation distribution (of 326 junction tests)

| Orientation | Count | Meaning |
|------------|-------|---------|
| A→B | 296 | fragment between CoreA (left) and CoreB (right) |
| B→A | 11 | fragment between CoreB (left) and CoreA (right) |
| A→SUFFIX | 8 | fragment after final CoreA (right edge of word) |
| PREFIX→B | 6 | fragment before first CoreB (left edge of word) |
| A→A | 3 | fragment between two CoreA occurrences |
| B→B | 1 | fragment between two CoreB occurrences |
| PREFIX→A | 1 | fragment before first CoreA |
| B→SUFFIX | 0 | (not observed in corpus) |

A→B dominates (91%) because the benchmark words are constructed as products of commutators where alternating core patterns are typical.

---

## Fragment length distribution

| Length range | Fragment count | Note |
|-------------|---------------|------|
| 1 | 4 | e.g., `a`, `A`, `b`, `B` — single generators |
| 2–5 | 28 | short connectors; all ≤12 are k=12 BFS confirmed in NF |
| 6–12 | 31 | medium connectors; all confirmed in shortlex NF via k=12 BFS |
| 13–34 | 114 | max LHS in bank is 34; all testable by 500K bank |
| 35–100 | 82 | longer than bank max LHS; bank cannot directly shorten these |
| 101–1107 | 59 | long fragments; only beam tested; all delta=0 |

---

## word_7245 connector fragments

word_7245 (comm_12_9, 7,245 chars) decomposes into 153 junctions with the following 9 distinct connector fragments:

| Fragment | Length | Orientation in word | k=12 BFS | 500K bank | beam (60s) |
|----------|--------|---------------------|-----------|-----------|------------|
| `a` | 1 | A→B | NF ✓ | delta=0 | delta=0 |
| `A` | 1 | A→B | NF ✓ | delta=0 | delta=0 |
| `aBA` | 3 | A→B | NF ✓ | delta=0 | delta=0 |
| `abA` | 3 | A→B | NF ✓ | delta=0 | delta=0 |
| `abaBABA` | 7 | A→B | NF ✓ | delta=0 | delta=0 |
| `ababABA` | 7 | A→B | NF ✓ | delta=0 | delta=0 |
| `ababbABBABA` | 11 | A→B | NF ✓ | delta=0 | delta=0 |
| `ababbaBABA` | 10 | A→B | NF ✓ | delta=0 | delta=0 |
| `ababbaBBABA` | 11 | A→B | NF ✓ | delta=0 | delta=0 |

All 9 fragments are in shortlex normal form (k=12 BFS exact for len ≤ 12). All 9 junctions return delta=0 at 500K bank and beam (60s). Full word_7245 beam (3 passes × 300s) also delta=0. **These are upper bounds, not irreducibility claims.**

---

## 31 seed rules — full data

All 31 rules are junction-level reductions (`CoreA · F · CoreB → shorter`) in A→B orientation unless noted. All GAP word-equality verified: `match=True` in B(2,5) PcGroup (order 5^34).

Durable persistence: `experiments/burnside/b25/fragment_seed_rules/b25_seed_rules_2026-06-25.json` (SHA256: `341c64bcc63fb89e18f43c78a8cc475983e20b6f6e4b521a033c511841002499`)

| rank | frag_len | orient | delta | occ | weight | fragment |
|------|---------|--------|-------|-----|--------|---------|
| 1 | 5 | A→B | -1 | 245 | 245 | `abABA` |
| 2 | 5 | A→B | -1 | 233 | 233 | `abaBA` |
| 3 | 9 | A→B | -2 | 28 | 56 | `ababABABA` |
| 4 | 9 | A→B | -2 | 21 | 42 | `ababaBABA` |
| 5 | 8 | A→B | -1 | 11 | 11 | `ababABAA` |
| 6 | 8 | A→B | -1 | 11 | 11 | `ababAABA` |
| 7 | 9 | A→B | -1 | 9 | 9 | `aabaaBABA` |
| 8 | 8 | A→B | -1 | 4 | 4 | `aabaBABA` |
| 9 | 10 | A→B | -1 | 4 | 4 | `abaabAAABA` *(direct)* |
| 10 | 11 | A→B | -2 | 2 | 4 | `ababaaBBABA` |
| 11 | 9 | A→B | -1 | 3 | 3 | `ababAABAA` |
| 12 | 8 | A→B | -2 | 1 | 2 | `ababaBAA` |
| 13 | 10 | A→B | -2 | 1 | 2 | `ababaaBABA` |
| 14 | 10 | A→B | -2 | 1 | 2 | `ababaBAABA` |
| 15 | 11 | A→B | -2 | 1 | 2 | `ababaaBAABA` |
| 16 | 12 | A→B | -2 | 1 | 2 | `ababaaaBBABA` *(direct)* |
| 17 | 141 | A→B | -1 | 2 | 2 | `aaaBAABABabAbaBaBAbabaBABabAbA...` (141 chars) |
| 18 | 6 | A→SUFFIX | -1 | 1 | 1 | `aabaaa` *(direct)* |
| 19 | 6 | B→A | -1 | 1 | 1 | `bbbABB` *(direct)* |
| 20 | 8 | A→B | -1 | 1 | 1 | `bAABBABA` |
| 21 | 11 | A→B | -1 | 1 | 1 | `aabaaaBBABA` *(direct)* |
| 22 | 11 | A→B | -1 | 1 | 1 | `ababbAAABAA` *(direct)* |
| 23 | 39 | PREFIX→B | -1 | 1 | 1 | `ABABabAbaBaBAbaBABabAbABaBAbab...` (39 chars) |
| 24 | 73 | A→B | -1 | 1 | 1 | `aaBAABABabAbaBaBAbabaBABabAbAB...` (73 chars) |
| 25 | 131 | A→SUFFIX | -1 | 1 | 1 | (131-char fragment) |
| 26 | 137 | A→SUFFIX | -1 | 1 | 1 | (137-char fragment) |
| 27 | 270 | A→SUFFIX | -1 | 1 | 1 | (270-char fragment) |
| 28 | 271 | A→SUFFIX | -1 | 1 | 1 | (271-char fragment) |
| 29 | 291 | PREFIX→B | -1 | 1 | 1 | (291-char fragment) |
| 30 | 562 | A→B | -1 | 1 | 1 | (562-char fragment) |
| 31 | 1107 | A→B | -1 | 1 | 1 | (1107-char fragment) |

*(direct)*: the fragment alone (not just in junction context) also reduces under the 500K bank.

**Ranking**: |delta| × occ (applicability weight). Rules #1 and #2 dominate — they apply to 245 and 233 junctions respectively across the 119-word corpus.

**Orientation note**: 29 of 31 rules are in A→B orientation. One is B→A (#19, `bbbABB`). Two are non-junction (A→SUFFIX, PREFIX→B), meaning the fragment appears at the right or left edge of the word rather than between two cores.

Full junction LHS and RHS strings: `experiments/burnside/b25/fragment_seed_rules/b25_seed_rules_2026-06-25.json`

---

## Null results — upper bounds

295 junction tests returned delta=0 under both the 500K KB bank and the braid_reduce beam (within the stated time budgets). These are recorded as upper bounds only.

Selected high-frequency null results (occ = times junction pattern appears in corpus):

| fragment | orient | occ | methods_tested | status |
|---------|--------|-----|----------------|--------|
| `a` | A→B | 590 | 500K bank + 120s beam | no shortening found |
| `A` | A→B | 577 | 500K bank + 120s beam | no shortening found |
| `abA` | A→B | 235 | 500K bank + 120s beam | no shortening found |
| `aBA` | A→B | 233 | 500K bank + 120s beam | no shortening found |
| `abaBABA` | A→B | 47 | 500K bank + 60s beam | no shortening found |

The 5 most frequent non-reducing junctions account for the bulk of junction occurrences in word_7245 and other benchmark words. Their null result is the primary reason word_7245 saves 0 chars from these rules.

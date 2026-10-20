---
title: t017-recertification-and-minimality-2026-10-19
hypothesis: "H17 (pre-registered, per word; result: holds for 11 of 12 words in flip (d) and 9 of 12 in S2 under M1 at |S| ≤ 5, ds547 fails and is unconfirmed: the pre-registered 1–5/12 band): for each of the 12 T-024-confirmed level-2/3 words, the flip (d) depth of its best certificate found by certificate-level patch surgery (M1, blocks of up to k cells) stays above the baseline (the maximum, over the word's components, of each component's minimum depth found by the same M1 at the same k)."
status: validated
author: asetlearning
date: 2026-10-19
todo: T-017
project: challenge-gen
instance: B(2,5)
experiment_type: hardness-evaluation
tags: [agent/exp, user/asetlearning, domain/group-theory, topic/burnside, topic/b25, topic/trivial-words, topic/hard-instance-generation, topic/proof-certificates, topic/van-kampen-diagrams, topic/search-design, project/challenge-gen, status/validated, experiment, methodology]
---

# Experiment — T-017: re-certification and minimality of the 12 confirmed words

Drafted by the Experimenter-B25; reviewed and finalised by Lead (2026-10-20). Every depth, area and class in §1–§4 and the pooled table was reproduced by the Validator ([[2026-10-20-t017-closeout-check]]); process figures (budget decisions, wall times, pool composition) come from the run records. Nothing in this note is a lower bound.

## 1. Conclusion

**Terms, used throughout.**
- **Certificate** = an ordered list of cells `c⁻¹·r·c` (r a relator of the table R7, c a conjugator) whose product freely reduces to the word. **N** = number of cells. **R7** = the 1,630-entry table of cyclic cores of the kbmag `b25_full` relators v^{5k} with |v| ≤ 7, with inverses (it includes v^10 … v^35 for |v| = 1 and v^10, v^15 for |v| = 2, 3; only 312 entries have |v| = 7). It is not the set of all primitive 5th powers of length ≤ 7.
- **L0** = the certificate re-expands to the word exactly (checked after every accepted rewrite).
- **S2** = strict depth with cells of root length 1 (a⁵-type cells) absorbed. **Flip (d)** = S2 plus the flip control rule (d). Both are measured on the fold (diagram) of the certificate, so they depend on cell order and conjugators. Definitions: [[challenge-gen-glossary]] and plan v2 ([[2026-10-19-t017-recertification-and-minimality-plan-v2]]).
- **M1** = certificate-level patch surgery (tcgraph `surgery`): it proposes sets S of at most k cells (vertex_pairs proposals), makes them contiguous by Peiffer/Hurwitz moves, and replaces the block product by a cheaper block when it is trivial, one R7 cell, one admissible u⁵ cell, or a conjugate of a stored cheaper block; each rewrite is accepted only on a strict lexicographic decrease. k = the largest |S| ("blocks of up to k cells"). Two objectives: area_first (N, flip, S2) and depth_first (flip, S2, N).
- **Components** of a word = its parent word and its tiles, each with its own certificate. **Baseline** = the maximum over the components of each one's minimum depth found.
- **H17 classes**, per word and measure: *fails* = word minimum ≤ baseline; *drops-but-stays-above* = word minimum below its stored value but above the baseline; *unchanged* = word minimum equals its stored value, above the baseline.
- **Pooled** = the minimum over every certificate found in every run: k=4 (both objectives), k=5 (depth_first) and k=6 (depth_first, 8 certificates only). A pooled bound is an upper bound under M1 at |S| ≤ 6, but k=6 ran on 8 certificates only and not to a fixpoint (§5).

**Headline (flip vs flip, pooled).** Of the 12 words, **1 fails** (ds547: word flip 2, baseline 2), **6 drop but stay above the baseline** (ds94, ds125, ds160, ds512, ds566, ds665) and **5 are unchanged** (ds145, ds368, ds519, ds764, ds781). By the pre-registered reading (1–5 of 12 fail) the failing word is recorded as unconfirmed, Step 3 was run on all 12 words, and the experiment stops.

**S2 vs S2 (pooled).** 3 fail (ds125, ds547, ds665), 4 drop but stay above (ds94, ds160, ds512, ds566), 5 unchanged. The S2 class of ds665 and ds125 fails because the baseline in S2 is 2 (their parents).

**Per-word upper bounds** (pooled, under M1 at |S| ≤ 6; flip (d) / S2 / N): ds94 2/2/376, ds125 2/2/241, ds145 3/3/401, ds160 3/3/302, ds368 3/3/259, ds512 2/2/442, ds519 (level 3) 3/3/1,640, ds547 2/2/731, ds566 2/2/423, ds665 2/2/467, ds764 3/3/804, ds781 2/3/623 (the three numbers are minima taken independently over runs; they need not be reached by one certificate). Full table in §2.

**Other results.**
- ds160's depth-4 claim is **retired**: the word reaches flip 3 against a baseline of 1.
- Five **components** drop at k=5 (ds160 parent 2/2 → 1/1, which lowers ds160's baseline from 2/2 to 1/1; four tiles 1 → 0). No word drops further, so no class changes.
- **any-u5 = R7** at k=4: allowing every primitive u⁵ as a cell changed no minimum and no run used an extended entry (§4).
- **M2'**: no power-move path to the trivial word exists for any of the 12 words (§4).
- The k=6 run (8 certificates, from the k=5 certificates) accepted no move in any run (final = start, 0 events; 286–792 algebraic hits per run, all rejected by the measure; 0.86–1.55 M sets tried): no word dropped and the ds547 parent stayed at 2/2. All 8 were capped, so this is a partial-search bound only.

## 2. Per-word table (pooled over k=4, k=5, k=6; R7)

Length = word length in letters. Stored = (N, S2, flip) of the pipeline certificate (after compression) that M1 started from. Pooled min: N is the smallest N seen (start or final state of any run); S2 and flip are minima over the `min_s2` / `min_flip_d` states (never from final states, because area_first can raise depth). "First reached" = the earliest run (k4 = k=4; af = area_first, df = depth_first) that attains the minimum. Later runs (k4 df, k5, k6) attain every pooled depth too, except ds665 S2 (k4 af only).

| word | length | stored (N, S2, flip) | pooled N (run) | pooled S2 (first reached) | pooled flip (first reached) | baseline S2 / flip (set by) | H17 flip | H17 S2 | capped (no fixpoint) |
|---|---|---|---|---|---|---|---|---|---|
| ds94 | 216 | 445, 3, 3 | 376 (k5 df) | 2 (k4 af) | 2 (k4 af) | 1 / 1 (parent, tiles 00, 02) | drops-above | drops-above | k6 |
| ds125 | 163 | 298, 3, 3 | 241 (k5 df) | 2 (k4 af) | 2 (k4 af) | 2 / 1 (parent) | drops-above | **fails** | k6 |
| ds145 | 361 | 468, 3, 3 | 401 (k5 df) | 3 | 3 | 2 / 2 (parent) | unchanged | unchanged | k6 |
| ds160 | 261 | 379, 4, 4 | 302 (k5 df) | 3 (k4 af) | 3 (k4 af) | 1 / 1 (S2: parent, tiles 02, 03; flip: parent, tiles 03, 08) | drops-above | drops-above | none |
| ds368 | 211 | 336, 3, 3 | 259 (k5 df) | 3 | 3 | 2 / 1 (parent S2; flip: parent, tiles 02, 03) | unchanged | unchanged | none |
| ds512 | 378 | 545, 3, 3 | 442 (k5 df) | 2 (k4 af) | 2 (k4 af) | 1 / 1 (S2: parent, tiles 05, 08, 10; flip: parent) | drops-above | drops-above | k6 |
| ds519 (level 3) | 1,548 | 1,863, 3, 3 | 1,640 (k4 af) | 3 | 3 | 2 / 2 (parent; 46 components) | unchanged | unchanged | k4 df, k5 df |
| ds547 | 699 | 878, 3, 3 | 731 (k5 df) | 2 (k4 af) | 2 (k4 af) | 2 / 2 (parent, 268 cells) | **fails** | **fails** | parent at k6 |
| ds566 | 320 | 515, 3, 3 | 423 (k5 df) | 2 (k4 af) | 2 (k4 af) | 1 / 1 (S2: parent, tiles 03, 05, 09; flip: parent) | drops-above | drops-above | k6 |
| ds665 | 405 | 618, 4, 3 | 467 (k5 df) | 2 (k4 af only) | 2 (k4 af) | 2 / 1 (parent S2; flip: parent, tiles 04, 05) | drops-above | **fails** | k6 |
| ds764 | 635 | 954, 3, 3 | 804 (k5 df) | 3 | 3 | 2 / 1 (parent S2; flip: parent, tiles 05, 15) | unchanged | unchanged | k5 df |
| ds781 | 529 | 767, 3, 2 | 623 (k5 df) | 3 | 2 | 1 / 1 (S2: among others tile 00; flip: parent, tiles 01, 05) | unchanged | unchanged | k6 |

"drops-above" = drops-but-stays-above. Component counts: ds94 9, ds125 8, ds145 13, ds160 10, ds368 12, ds512 13, ds519 46, ds547 20, ds566 14, ds665 15, ds764 24, ds781 19 (parent plus tiles). Baseline "set by" lists up to three components that attain the maximum.

Notes on the table:
- The k=4 and k=5 minima agree for every word except N: k=5 only lowered N (for example ds125 242 → 241, ds547 775 → 731, ds160 318 → 302), and the pooled depths were all already reached at k=4. ds665's S2 of 2 comes from k=4 area_first alone (its k=5 and k=6 depth_first runs end at S2 3).
- The k=6 run of ds665 started from S2 3 (the k=5 `min_flip_d` certificate), so it tests flip only; the pooled S2 class (fails) is unaffected.
- ds519's pooled N comes from the k=4 area_first run (1,640); the k=5 depth_first run ended at 1,782 cells, capped.

## 3. Labels

- **Robust under M1 at |S| ≤ k** (flip vs flip: word minimum above the baseline, with the components minimised the same way): ds94, ds125, ds145, ds160, ds368, ds512, ds566, ds665, ds781 — at |S| ≤ 5 over all 215 certificates, and at |S| ≤ 6 for ds94, ds125, ds145, ds512, ds566, ds665, ds781 on the single certificate tried, partial (capped). In S2 vs S2, ds125 and ds665 are **not** robust (they fail).
- **ds764**: above the baseline at |S| ≤ 4 (fixpoint) and at |S| ≤ 5, but the k=5 run was capped at 3 CPU-h without a fixpoint: label "unchanged, capped at 3 CPU-h, no fixpoint: a bound from a partial search". Not run at k=6: at baseline + 2 (flip 3 vs 1), outside the one-sided target.
- **ds519 (level 3)**: eligible for k=6 (word 3, baseline 2) but **excluded on budget**, not ineligible. Its k=4 depth_first and k=5 depth_first runs were capped (1 CPU-h and 3 CPU-h); same label as ds764.
- **ds547**: **unconfirmed** (fails: word 2, baseline 2, set by its 268-cell parent). A drop of the parent to 1 would un-fail it: k=6 on the parent (capped, no move accepted) did not do this.
- **ds160**: the depth-4 claim is retired; the word reaches 3, against a baseline of 1 (after the k=5 drop of its parent).
- **ds368**: pooled flip 3 versus baseline 1: robust in the broad sense (baseline + 2); not run at k=6 (outside the one-sided target, which concerned words at baseline + 1).
- The component inputs of both levels (146 level-2 tiles, 45 level-3 tiles and the parents) were checked by the Validator against the pilot tile table ([[2026-10-19-t017-m1-tile-inputs-check]]).

## 4. M2' and any-u5

- **M2' (power-move path to 1).** No word reaches 1 by non-increasing power moves alone ([[2026-10-19-t017-v2-confirm-and-m2-closure]]): the 7 strictly power-free words (ds94, 125, 145, 368, 547, 665, 764) have no applicable power rule (argued; the BFS finds 0 moves); the 5 words with exact halves (ds160, 512, 566, 781, ds519 level 3) have closures of size 2–6 under power moves of period ≤ 7, exhausted, all at the original length, with no cap hit.
- **any-u5 = R7 at k=4.** With test (c) enabled for every primitive u⁵ (the table may grow by the entries a run needs), the minima on all 215 certificates equal the R7 minima; 0 of 860 records used an extended entry. So no headline depth needs a table label ("all u⁵"); all numbers in this note are over R7 (the 1,630-entry table, hash `542992216c3e84e8`). Steps 3 (k=5, k=6) ran R7 only.

## 5. Deviations from plan v2 (the pre-registration)

1. **Proposals:** vertex_pairs (sets built from the cells at one diagram vertex plus pairs). Step 0 (the positive control on the 7 area-like dataset words) needs a vertex triple for line 49, and vertex_pairs reproduces all 7 lines (adjacent + pairs was an earlier mode) ([[2026-10-19-t017-m1-code-review]]).
2. **Starts:** every run started from the pipeline-compressed certificates, not the raw ones; the k=5 and k=6 runs start from the compressed certificates and (k=6) from the k=5 `min_flip_d` certificates, which is an upper bound.
3. **Steps 1–2 CPU ceiling:** 30 CPU-h by Lead's decision (v2: 15 CPU-h); any-u5 and R7 ran together.
4. **Step 3 (k=5):** depth_first only; R7 only; cap 3 CPU-h per certificate (v2: 4); total ceiling 60 CPU-h (v2: 40); all 12 words plus all their components (as v2 requires under the 1–5/12 reading).
5. **Step 3 stopping rule.** Lead first skipped k=6 on a "classes only" trigger that was a later deviation; Lead withdrew it and reinstated the pre-registered rule, because 5 components dropped at k=5 and the rule is "no class change, no depth drop". k=6 therefore ran once.
6. **k=6 targeted and one-sided:** 8 certificates (ds94, ds125, ds145, ds512, ds566, ds665, ds781 words, and the ds547 parent), from their k=5 certificates, cap 3 CPU-h, depth_first. Reasoning: k=6 can create a new "fails" only if a word drops, and only on words at baseline + 1 (pooled flip); ds547's parent could un-fail ds547. Excluded by rule: ds160, ds368, ds764 (baseline + 2). ds519 (level 3, word 3 vs baseline 2) is eligible but excluded on budget (1,782 cells, capped at 3 CPU-h at k=5).
7. **CPU overrun:** 60.245 CPU-h in total (Validator's exact figure, [[2026-10-20-t017-step3-s6-verify]]): 8.2598 (Steps 1–2) + 27.9852 (k=5) + 24.0000 (k=6), i.e. 0.245 CPU-h over the 60 ceiling (surgery CPU only; builds and overhead excluded).
8. **Naming.** "Step 3, |S|=6" in notes. The job files say `step4` only as the order of the jobs; plan v2's Step 4 is M2'.
9. **k=5 and k=6 pools** are the frozen reference pools for that k (11,386 classes at k=4, 23,228 at k=5, 38,729 at k=6; the 453 reference certificates compressed, plus blocks met on the inputs), so the reference differs by k.

## 6. Scope

- **Upper bounds only**: every number is the best certificate M1 found under its caps, at |S| ≤ k. No lower bound is claimed, and none follows.
- These are **not minima over G7** (the group presented by R7) **or over B(2,5)**: a different method, a larger k or all-u⁵ cells with long u could give a smaller certificate.
- Capped runs (ds764 and ds519 at k=5; ds519 at k=4 depth_first; all 8 at k=6) are bounds from a partial search. The k=6 runs tried 0.86–1.55 M sets each without accepting a move, which is not evidence that k=6 cannot lower anything.
- H17 holding means "the depth gain survives M1 at budget k", not an inequality between true minima. The baseline is itself an upper bound on the components' minima, so a word's margin over it is not a margin over the true minima either.

## 7. Code and runs

- **tcgraph** (branch `feat/t017-patch-surgery`, repo `tcgraph_agentic`): `09d9f15` (M1 surgery), `e4d8b38` (run jobs), `51a8138` (macOS time-limit fallback, fail on any error; summary), `361606e` (level-3 component jobs), `59f3c37` (k=5 job), `e245a0c` (k=6 job). Depth measurement by tcgraph main `ca2ceb9` (Validator's independent check).
- **b25**: `216f8a8` (tcgraph_ext.surgery bindings, pinning tcgraph 09d9f15), `6dcd95e` (replay of the level-3 word ds519 with tile-certificate dump).
- **rjob ids** (host: the project's Mac host, 9 CPUs; R7 unless noted): Steps 1–2 `20261019-200113-ea4941`, `-200115-670fa5`, `-200116-795704`, `-200118-08644a`, `20261019-201804-6f7e1d`, `-201806-92215a` (words, level-3 word, components, any-u5, level-3 components, any-u5 level-3 components); k=5 `20261019-220846-87abe8` (215 certificates, 27.99 CPU-h, 22:09–02:18 EDT); k=6 `20261020-023145-d4af48` (8 certificates, 24.0 CPU-h, 02:32–06:27 EDT).
- **Input hashes (sha256)**, all under `data/inputs/` (gitignored, not committed): `t017/tiles.jsonl` `fcac15d790843994d3211379f276cf90d46e56b80849b59e734a86c803e8b5d3`; `t017/parents.jsonl` `e3d7a6accb5192ffeb439ce158a4e25ef5bfebe9c763260f6b1e31e254778937`; `t017/words11.jsonl` `4a921aa4ca9eac8b77002c8cf1882d69d8be2e15b7120aea8eda94644d7c20d6`; `t017/l3word.jsonl` `ec10fb81d103c45265a91dd166c93744f1855e666da61eecaa79aafd6097f49b`; `t017/l3components.jsonl` `c7e966d7524718179468a3d2d251abebf36a56d95195efcefcea84030200fbb3`; `t017/step4_starts.jsonl` (the k=6 starts) `368b23a2e0d0090a793c6655a8d1e8b843cb4c5a5db3a8ca3344cf956dd4dedd`; reference pools `certs_gt53.jsonl` `df587deee7cc7d255e68376c6c5a20f78559acab675d1b2fcfbfa2b3cb5a5f76`, `seeds_power_free_len_le53.jsonl` `9fa4e7c583e5f9056260c53d696fd763e430539cfac674aa06ca65868ed126f7`; table `onion/tests/data/core_table_r7.json` (1,630 entries; file sha256 `61bfebc15bd928feb4d0cd07e6ba6209348f34ed7a6d6ab5c39528085d870a23`; internal table hash `542992216c3e84e8`). The 12-word source file is private and is neither linked nor quoted here.
- **Results and outputs** (vault): `Agents/asetlearning/Experimenter-B25/` — `2026-10-19-t017-m1-results.md` (Steps 1–2), `2026-10-20-t017-step3-k5-results.md` with `t017-step3-k5-outputs/`, `2026-10-20-t017-step3-s6-results.md` with `t017-step3-s6-outputs/`.
- **Verification:** Steps 1–2 [[2026-10-19-t017-m1-results-verify]] (CONFIRMED, 1,720 certificates); k=5 [[2026-10-20-t017-step3-k5-verify]] (CONFIRMED, 430/430, two corrections applied here); k=6 [[2026-10-20-t017-step3-s6-verify]] (CONFIRMED, 24/24). Pooling over runs is the Experimenter's computation from the three result sets (script in the Experimenter's scratch, not committed); the Validator reproduced the full pooled table independently ([[2026-10-20-t017-closeout-check]]).

## 8. Related material

- [[2026-10-19-t017-recertification-and-minimality-plan-v2]] — the pre-registration; [[2026-10-19-t017-plan-review-triage]] — the Validator's plan review.
- [[t024-challenge-census-and-onion-probe-2026-10-17]] — the T-024 work whose 12 confirmed words are re-certified here; [[2026-10-18-t024-level2-best-words-verify]], [[2026-10-18-t024-level3-first-word-verify]].
- Validator notes: [[2026-10-19-t017-m1-code-review]], [[2026-10-19-t017-m1-tile-inputs-check]], [[2026-10-19-t017-m1-results-verify]], [[2026-10-19-t017-v2-confirm-and-m2-closure]], [[2026-10-20-t017-step3-k5-verify]], [[2026-10-20-t017-step3-s6-verify]].
- [[challenge-gen-glossary]] · [[challenge-gen-success-metrics]] · [[project-challenge-gen]] · [[Challenge Generation/_progress]].

## Final verdict
**`#status/validated`** (H17 holds for 11 of 12 words in the headline measure, under M1 at |S| ≤ 5 on all certificates and |S| ≤ 6 on the targeted ones; pre-registered reading 1–5/12 fail). ds547 is unconfirmed; the S2 reading is weaker (3 fail). All numbers are upper bounds.

### Why
The depth gains of the T-024 words mostly survive patch surgery applied equally to the words and to their components. The one failure (ds547) is a word whose depth falls to 2 while its 268-cell parent stays at 2/2. Because all numbers are upper bounds from a capped heuristic search, the result is "no counter-evidence found under M1", not a proof of minimality.

### What I'd do next
- Not planned: longer runs on ds764 and ds519 (capped), or on the ds547 parent; only if a later item needs these words settled.
- Optional: M3 (bounded lengthening) as a hardness scale; kbcert rewriting-path certificates for ds125 and ds368 (plan v2 Steps 5 and 6).

### Lead notified
- Date: 2026-10-20
- Message: T-017 close-out (Lead), reported to the owner.

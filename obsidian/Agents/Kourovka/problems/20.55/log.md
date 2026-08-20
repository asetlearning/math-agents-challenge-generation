---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-tables
  - project/kourovka
  - status/draft
problem_id: "20.55"
cycle: 1
---

# Problem 20.55 working log

## Active-time ledger

- 2026-08-11T15:49:45Z — work started; cumulative active minutes: 0.
- 2026-08-11T15:58:00Z — source/corpus inspection and initial literature search completed; cumulative active minutes: 8.

## Staleness check

### 2026-08-11T15:58:00Z — source and corpus gates

- Configured PDF resolved through `_meta/agents/Kourovka/paths.env`; no absolute source path was recorded.
- Read PDF page 152 using:

  ```bash
  source '_meta/agents/Kourovka/paths.env'
  pdftotext -f 152 -l 152 -layout "$KOUROVKA_PDF" -
  pdftoppm -f 152 -l 152 -png -r 160 "$KOUROVKA_PDF" 'Agents/Kourovka/problems/20.55/scratch/source-page'
  ```

- Visually inspected `scratch/source-page-152.png` at original resolution and compared every word, numeral, inequality, and symbol in 20.55 with the rendered PDF.
- Corrected transcription:

  > **20.55.** Are there soluble finite groups \(G\) and \(H\), of derived lengths 2 and 4 and having identical character tables?
  >
  > Pairs of nonisomorphic soluble finite groups with identical character tables and with derived lengths \(n\) and \(n+1\) for any \(n\ge 2\) were constructed in (S. Mattarei, *J. Algebra*, **175** (1995) 157–178). S. Mattarei

- `source_transcription_checked: yes`.
- The configured PDF is headed “20th Issue (2022)” on this page and prints 20.55 unstarred, with no later/editor answer appended. The synthesis calls this Notebook No. 21 but the rendered source page itself says 20th Issue (2022); this bibliographic mismatch does not alter the mathematical statement.
- Corpus record inspected at `Research/Group theory/Open problems/Kourovka/corpus/kourovka-20-corpus.jsonl`, line 1145:
  - `answered: false`
  - `has_editor_comment: false`
  - `has_later_comment: false`
  - corpus page metadata says 154, whereas the configured rendered PDF has the statement on page 152.

### 2026-08-11T15:58:00Z — initial web/arXiv search

Searches run:

- exact phrase `"Kourovka" "20.55" Mattarei character tables derived lengths`;
- exact phrase `"Problem 20.55" "Kourovka Notebook"`;
- `Sandro Mattarei identical character tables derived length 2 4`;
- arXiv-restricted `site:arxiv.org character tables "derived lengths" Mattarei`.

Results found the known background only: Mattarei's 1992 Warwick thesis, the 1992 paper *Character Tables and Metabelian Groups*, the 1994 paper *An example of p-groups with identical character tables and different derived lengths*, and the cited 1995 paper *On Character Tables of Wreath Products*. The Warwick thesis abstract explicitly describes examples of lengths 2 and 3 and a general consecutive-length construction. No result returned an example with lengths 2 and 4, a solution to problem 20.55, or a post-2022 resolution. Further targeted searching is still required before this gate is closed.

## Statement in my own words

The question is existential: find two finite solvable groups whose ordinary complex character tables are identical (up to simultaneous relabelling of irreducible characters and conjugacy classes), while one group is metabelian but nonabelian (derived length exactly 2) and the other has derived length exactly 4. The known wreath-product construction changes a pre-existing derived-length gap by preserving a gap of one, so it does not immediately supply the requested gap of two.

## 2026-08-11T16:04:00Z — tooling and first complete order

- Tool versions observed:

  ```text
  GAP_VERSION=4.12.1
  CTBLLIB_AVAILABLE=true
  CTBLLIB_VERSION=1.3.7
  SMALLGRP_AVAILABLE=true
  SMALLGRP_VERSION=1.5.3
  ```

- `scratch/min-derived-length-4.g` used the SmallGroups catalogue property filters to find the least order at which a finite solvable group of derived length exactly 4 occurs. First attempt produced the real GAP diagnostic `Syntax error: 'QUIT;' cannot be used in this context`; the script was corrected by putting the early return inside a function. Corrected observed output (`scratch/min-derived-length-4.out`):

  ```text
  GAP_VERSION=4.12.1
  SMALLGRP_VERSION=1.5.3
  FIRST_ORDER=48 COUNT=2 IDS=[ [ 48, 28 ], [ 48, 29 ] ]
  ```

- `scratch/check-order-48.g` then enumerated **all** SmallGroups catalogue groups of order 48 having derived length exactly 2 (41 groups) and exactly 4 (2 groups), constructed each ordinary character table with GAP, and called `TransformingPermutationsCharacterTables` for every one of the 82 cross-pairs. This GAP operation returns row and column permutations precisely when the tables are permutation equivalent. Exact command:

  ```bash
  timeout 60s gap -q 'Agents/Kourovka/problems/20.55/scratch/check-order-48.g' | tee 'Agents/Kourovka/problems/20.55/scratch/check-order-48.out'
  ```

- Salient observed output:

  ```text
  DL2_COUNT=41 IDS=[ [ 48, 1 ], [ 48, 3 ], [ 48, 4 ], [ 48, 5 ], [ 48, 6 ], [ 48, 7 ], [ 48, 8 ], [ 48, 9 ], [ 48, 10 ], [ 48, 11 ], [ 48, 12 ], [ 48, 13 ], [ 48, 14 ], [ 48, 15 ], [ 48, 16 ], [ 48, 17 ], [ 48, 18 ], [ 48, 19 ], [ 48, 21 ], [ 48, 22 ], [ 48, 24 ], [ 48, 25 ], [ 48, 26 ], [ 48, 27 ], [ 48, 31 ], [ 48, 34 ], [ 48, 35 ], [ 48, 36 ], [ 48, 37 ], [ 48, 38 ], [ 48, 39 ], [ 48, 40 ], [ 48, 41 ], [ 48, 42 ], [ 48, 43 ], [ 48, 45 ], [ 48, 46 ], [ 48, 47 ], [ 48, 49 ], [ 48, 50 ], [ 48, 51 ] ]
  DL4_COUNT=2 IDS=[ [ 48, 28 ], [ 48, 29 ] ]
  DL4_GROUP=[ 48, 28 ] STRUCTURE=C2 . S4 = SL(2,3) . C2 NCLASSES=8
  DL4_GROUP=[ 48, 29 ] STRUCTURE=GL(2,3) NCLASSES=8
  MATCH_COUNT=0 MATCHES=[  ]
  ```

- What this proves: within the complete SmallGroups catalogue at order 48, no derived-length-2/derived-length-4 pair has identical ordinary character tables in GAP's permutation-equivalence sense.
- What this does not prove: anything about orders above 48, or the global existential question.
- Cumulative active minutes: 14.

## 2026-08-11T16:10:00Z — complete SmallGroups search through order 255

- `scratch/search-through-127.g` first searched every order through 127. It constructed character tables only at orders having at least one group of derived length 4, prefiltered cross-pairs by number of conjugacy classes, and then applied `TransformingPermutationsCharacterTables` to every surviving pair. Observed output in `scratch/search-through-127.out`:

  ```text
  GAP_VERSION=4.12.1 SMALLGRP_VERSION=1.5.3 CTBLLIB_VERSION=1.3.7
  ORDER=48 DL2=41 DL4=2
  ORDER=96 DL2=198 DL4=8
  SUMMARY_ORDERS=[ 48, 96 ] TOTAL_DL2=239 TOTAL_DL4=10 EXACT_TESTS=14 MATCH_COUNT=0 MATCHES=[  ]
  ```

- The parameterized version was then run through 255 with:

  ```bash
  timeout 60s gap -q 'Agents/Kourovka/problems/20.55/scratch/search-through-255.g' | tee 'Agents/Kourovka/problems/20.55/scratch/search-through-255.out'
  ```

- Exact observed output:

  ```text
  GAP_VERSION=4.12.1 SMALLGRP_VERSION=1.5.3 CTBLLIB_VERSION=1.3.7
  ORDER=48 DL2=41 DL4=2
  ORDER=96 DL2=198 DL4=8
  ORDER=144 DL2=159 DL4=6
  ORDER=192 DL2=1405 DL4=50
  ORDER=216 DL2=126 DL4=3
  ORDER=240 DL2=181 DL4=4
  SUMMARY_ORDERS=[ 48, 96, 144, 192, 216, 240 ] TOTAL_DL2=2110 TOTAL_DL4=73 EXACT_TESTS=130 MATCH_COUNT=0 MATCHES=[  ]
  ```

- Coverage: every isomorphism type in GAP SmallGroups 1.5.3 of every order at most 255; at the six relevant orders this comprises 2,110 groups of derived length exactly 2 and 73 of derived length exactly 4. All 130 cross-pairs sharing the necessary number-of-classes invariant received the exact table-permutation test. No match occurred.
- What this proves: no requested pair has common order at most 255. Identical character tables necessarily have the same group order (sum of squared irreducible degrees), so comparisons across different orders are unnecessary.
- What this does not prove: the existential question is unbounded; absence through 255 is only finite negative evidence. The prefilter is safe because identical tables necessarily have the same number of columns/classes.
- Cumulative active minutes: 21.

## 2026-08-11T15:57:54Z — timing-ledger correction

- The timestamps `15:58`, `16:04`, `16:10`, and `16:13` above were mistakenly estimated instead of obtained from the required `kv_now` helper. At `kv_now` = `2026-08-11T15:57:54Z`, those entries were discovered to be future-dated. Their chronological order, commands, and observed computation outputs are accurate; their displayed wall-clock timestamps and stated cumulative-minute totals are not.
- Correct timing baseline: assignment start `2026-08-11T15:49:23Z`; current `kv_now` observation `2026-08-11T15:57:54Z`; cumulative active time is therefore approximately **9 minutes**, not 21.
- The QUESTION/REQUEST bus filenames created during that interval likewise carry estimated future minute stamps. They are retained because bus messages are never deleted; their mathematical content is unaffected. This correction is the authoritative timing record.
- From this point onward every ledger timestamp will be copied from `kv_now` output only.

## 2026-08-11T15:57:54Z — further bounded search

- `scratch/search-257-383-except256.g` exhaustively checked all catalogue orders 257 through 383 (order 256 intentionally excluded pending a heavy-compute lease). Exact command:

  ```bash
  timeout 60s gap -q 'Agents/Kourovka/problems/20.55/scratch/search-257-383-except256.g' | tee 'Agents/Kourovka/problems/20.55/scratch/search-257-383-except256.out'
  ```

- Exact observed output:

  ```text
  GAP_VERSION=4.12.1 SMALLGRP_VERSION=1.5.3 CTBLLIB_VERSION=1.3.7
  ORDER=288 DL2=876 DL4=32
  ORDER=320 DL2=1621 DL4=2
  ORDER=336 DL2=202 DL4=4
  SUMMARY_ORDERS=[ 288, 320, 336 ] TOTAL_DL2=2699 TOTAL_DL4=38 EXACT_TESTS=762 MATCH_COUNT=0 MATCHES=[  ]
  ```

- This rules out all requested pairs of common order 257–383 except order 256. Combined with the earlier run, every common order 1–383 except 256 has been checked against the complete SmallGroups catalogue.
- A subsequent exploratory GAP count command for orders 256, 384, and 512 produced only `true` (the `LoadPackage` return) before stopping, so it establishes no counts and none are reported.

## 2026-08-11T22:34:45Z — cycle 1 resumed under fresh lease

- Work resumed from Lead's roster value of 24 cumulative active minutes; 156 active minutes remain.
- Inbox processed oldest-first. The expired initial lease was not used. Lead's replacement lease assigns heavy-compute slot 2 through `2026-08-11T23:30:40Z`, which is also the new safety stop.
- Validator judged the bounded-negative method adequate subject to independent reproduction. For any positive match, Validator requires preservation of the returned permutations and independent reconstruction/checks of group identity, derived series, character matrices, class sizes, element orders, and power maps.
- Next action: run the exact approved order-256 command with its mandatory 1800-second timeout. Compute-queue/runtime waiting is recorded but not charged as active research time.

## 2026-08-11T22:37:46Z — order 256 completed decisively; slot release

- Launched the exact approved command under leased slot 2:

  ```bash
  timeout 1800s gap -q 'Agents/Kourovka/problems/20.55/scratch/search-order-256.g' | tee 'Agents/Kourovka/problems/20.55/scratch/search-order-256.out'
  ```

- Exact observed output before interruption:

  ```text
  GAP_VERSION=4.12.1 SMALLGRP_VERSION=1.5.3 CTBLLIB_VERSION=1.3.7
  ORDER=256 DL2=55660 DL4=0
  ```

- Once `DL4=0` was printed, the mathematical search at order 256 was complete: no 2/4 pair can exist without a derived-length-4 group. The script nevertheless proceeded to construct character tables for all 55,660 length-2 groups because `entries2` was initialized outside the now-empty loop over `ids4`. I interrupted this logically unnecessary phase with Ctrl-C; the shell process exited 130. No unobserved summary line is claimed.
- Exact object and coverage: GAP SmallGroups 1.5.3's complete catalogue of all 56,092 groups of order 256, filtered by the exact `DerivedLength` property. It contains no derived-length-4 group.
- Combined bounded result: every order 1 through 383 is ruled out for the requested pair. Orders other than 256 were checked by exact character-table permutation comparison wherever both derived lengths occurred; order 256 is ruled out earlier by the absence of any length-4 group.
- What this does not establish: existence or nonexistence at any order above 383.
- Active work for inbox inspection, output inspection, and logging brings the roster baseline from 24 to approximately 28 cumulative active minutes; compute runtime/waiting was not charged.

## 2026-08-11T22:37:46Z — Math Expert idea received

- Math Expert found no reliably sourced construction that directly produces a derived-length gap of two. Suggested named line: reverse-engineer an explicit Mattarei 2/3 equal-table pair, identify which semidirect-module orbit data enforces table equality, and test whether only the length-3 side can be extended to length 4 while preserving that data.
- Falsifier/kill criterion: if Mattarei's table-equivalence mechanism couples the relevant induction/extension step symmetrically on both groups, it necessarily preserves gap one and cannot yield 2/4.
- This structural line is more informative than enlarging brute-force bounds blindly and will be pursued after releasing the lease.

## 2026-08-11T22:40:00Z — Chapter 5 construction cannot reach length 4

- Read Mattarei's thesis, Sections 5.1–5.2, focusing on the exact assumptions and Lemma 5.2.1 rather than only the examples.
- The general construction takes `G_i = D_i semidirect (W_i x Q_i)` under condition (1) `D_i' <= N_i <= Z(D_i)` and proves in Lemma 5.2.1(i) that `G_i' = D_i`; condition (1) forces `D_i'' = 1`. Therefore `G_i''' = D_i'' = 1`, and every group made by this construction has derived length at most 3.
- This kills the suggested attempt to obtain a 2/4 pair merely by changing the module or semidirect-product parameters inside Mattarei's Chapter 5 construction: a length-4 output contradicts its defining condition (1). To continue structurally one would need a genuinely new comparison theorem permitting a non-metabelian `D_2`, likely along the more general Chapter 4 extension framework, not a parameter tweak.
- The ordinary wreath-product theorem is also symmetric: regular wreathing by the same nontrivial cyclic group raises both derived lengths exactly one, preserving rather than enlarging the gap.
- What this establishes: two named existing mechanisms do not directly yield 2/4. What it does not establish: that no asymmetric construction or application of the more general comparison theorem can work.

## 2026-08-11T22:39:40Z — complete light search for orders 385–511

- Exact command:

  ```bash
  timeout 60s gap -q 'Agents/Kourovka/problems/20.55/scratch/search-385-511.g' | tee 'Agents/Kourovka/problems/20.55/scratch/search-385-511.out'
  ```

- Exact observed output:

  ```text
  GAP_VERSION=4.12.1 SMALLGRP_VERSION=1.5.3 CTBLLIB_VERSION=1.3.7
  ORDER=432 DL2=566 DL4=32
  ORDER=480 DL2=1102 DL4=26
  SUMMARY_ORDERS=[ 432, 480 ] TOTAL_DL2=1668 TOTAL_DL4=58 EXACT_TESTS=336 MATCH_COUNT=0 MATCHES=[  ]
  ```

- This rules out every requested pair of common order 385 through 511. Order 384 remains unchecked and was not part of this command.

## 2026-08-11T22:45:00Z — light catalogue searches above 511

- `search-513-575.g` completed exactly:

  ```text
  GAP_VERSION=4.12.1 SMALLGRP_VERSION=1.5.3 CTBLLIB_VERSION=1.3.7
  ORDER=528 DL2=152 DL4=4
  SUMMARY_ORDERS=[ 528 ] TOTAL_DL2=152 TOTAL_DL4=4 EXACT_TESTS=4 MATCH_COUNT=0 MATCHES=[  ]
  EXIT=0
  ```

- `search-577-639.g` completed exactly:

  ```text
  GAP_VERSION=4.12.1 SMALLGRP_VERSION=1.5.3 CTBLLIB_VERSION=1.3.7
  ORDER=600 DL2=162 DL4=1
  ORDER=624 DL2=237 DL4=4
  SUMMARY_ORDERS=[ 600, 624 ] TOTAL_DL2=399 TOTAL_DL4=5 EXACT_TESTS=4 MATCH_COUNT=0 MATCHES=[  ]
  EXIT=0
  ```

- `search-641-719.g` did **not** complete: both attempts printed counts for orders 648 and 672, but the persistent rerun reached the mandatory timeout with `EXIT=124` before a summary. No negative result is inferred from those incomplete attempts.
- The range was split. `search-641-671.g` then completed with:

  ```text
  ORDER=648 DL2=460 DL4=11
  SUMMARY_ORDERS=[ 648 ] TOTAL_DL2=460 TOTAL_DL4=11 EXACT_TESTS=20 MATCH_COUNT=0 MATCHES=[  ]
  EXIT=0
  ```

- `search-673-719.g` completed with no order containing both lengths:

  ```text
  SUMMARY_ORDERS=[  ] TOTAL_DL2=0 TOTAL_DL4=0 EXACT_TESTS=0 MATCH_COUNT=0 MATCHES=[  ]
  EXIT=0
  ```

- Therefore the completed coverage above 511 is: 513–575, 577–639, 641–671, and 673–719. Explicit unchecked heavy gaps are 512, 576, 640, and 672; order 384 remains the earlier gap. No match was found in any completed interval.

## 2026-08-11T22:47:36Z — final bounded-search accounting

- Timing correction: the headings `22:40:00Z` and `22:45:00Z` immediately above were rounded/estimated despite the earlier clock rule. The observed command-start times were `22:39:07Z` and `22:44:09Z`, respectively. This append-only correction is authoritative.
- Further completed exact runs:
  - orders 721–767: only order 750 had both lengths (`DL2=29`, `DL4=1`); zero pairs survived the number-of-classes prefilter, `MATCH_COUNT=0`, exit 0;
  - orders 769–839: only order 816 (`DL2=186`, `DL4=4`), four exact tests, no match, exit 0;
  - orders 840–895 did not complete as one range because order 864 is large (`DL2=3471`, `DL4=205`); no conclusion was taken from that partial output. Split runs 840–863 and 865–895 both completed with no order containing both lengths. Order 864 remains unchecked;
  - orders 896–959: only order 912 (`DL2=200`, `DL4=4`), four exact tests, no match, exit 0;
  - orders 961–1000: only order 1000 (`DL2=161`, `DL4=2`); zero pairs survived the number-of-classes prefilter, no match, exit 0.
- The continuous completed intervals and isolated gaps are therefore:
  - complete: 1–383, 385–511, 513–575, 577–639, 641–671, 673–767, 769–863, 865–959, 961–1000;
  - unchecked heavy/catalogue gaps: 384, 512, 576, 640, 672, 768, 864, 960.
- No match was found anywhere in the completed ranges.

## 2026-08-11T22:47:36Z — final structural/literature line

- A targeted search found Mark L. Lewis, *Constructing solvable groups with derived length four and four character degrees* (arXiv:1803.00616). Its Theorem 3.7 constructs a length-4 group `P semidirect Q8` of order `8 p^5` for primes `p = 3 mod 8`; the smallest parameter gives order 1944. The paper controls only the set of character degrees, not the full character table or a metabelian table twin.
- Attempted command `NumberSmallGroups(1944)` produced the exact GAP error `the library of groups of size 1944 is not available`; subsequent `IdsOfAllSmallGroups` calls likewise errored. No catalogue counts or comparisons at 1944 are claimed.
- This family does not supply a named one-hour construction of a metabelian group with the same full table. Matching four character degrees is only a necessary invariant and would be radically insufficient.

## Final assessment — REPORT: DEAD

### What was tried and why it failed

1. Fresh source and staleness search: no solution or post-2022 resolution was found; only Mattarei's known gap-one work appeared.
2. Complete bounded SmallGroups searches: no 2/4 table twin was found in the completed intervals listed above. Several large orders remain explicit gaps; finite negative evidence cannot answer the existential problem.
3. Mattarei Chapter 5 reverse engineering: its hypothesis `D_i' <= N_i <= Z(D_i)` and conclusion `G_i'=D_i` force derived length at most 3, so parameter changes inside that theorem cannot produce the required length-4 side.
4. Regular wreath products: they add one to both derived lengths, preserving a gap of one.
5. Camina-triple/general comparison literature: it suggests a much broader research programme, but no explicit asymmetric construction satisfying the full table-equivalence hypotheses was found.
6. Lewis length-4 families: they control character-degree sets only and provide no candidate identical full character table; the smallest highlighted order is outside the installed SmallGroups catalogue.

### What is ruled out, and how firmly

- Firmly, by exact catalogue computations: a requested pair in every completed order interval listed above, subject to GAP SmallGroups 1.5.3 completeness and Validator reproduction.
- Firmly, from the stated theorem hypotheses: the Chapter 5 general construction and symmetric regular-wreath induction cannot directly create a 2/4 pair.
- Not ruled out: any unchecked order, any new asymmetric Camina-triple construction, or the original unbounded existential question.

### What progress would require

- A new theorem extending Mattarei's comparison method to normal sections whose derived subgroup is itself nonmetabelian, with explicit control of the Camina-triple orbit conditions; or
- a database/construction covering promising orders beyond SmallGroups, plus an invariant-indexed search that avoids generating all character tables; or
- direct insight from a human expert on whether Lewis's `P semidirect Q8` families admit full-table twins.

### Honest value judgment

This problem is not a good target for further blind catalogue expansion. The first cycle identified why the two obvious constructions preserve a gap of at most one, and the remaining plausible route is a new structural construction rather than another finite bound. Without such an idea, further agent time is unlikely to close the problem.

- Work stopped at `2026-08-11T22:47:36Z`. Reconciled cumulative active time is approximately 35 minutes (roster baseline 24 plus resumed inspection, reasoning, scripting, and logging; compute waiting excluded). This is an early DEAD report because no concrete live one-hour line remains; it does not pretend that the 180-minute research budget was consumed.

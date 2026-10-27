---
type: validation
date: 2026-10-26
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028 survivors rev 3 (220 words) independent re-check"
status: CONFIRMED for items 1-4, with scope notes and one registry consequence
---
# Survivors rev 3: independent re-check

Triage: [[2026-10-26-t028-survivors-rev3-recheck-triage]]. File (private) sha256 7ee63c66...; old file sha 5939a1e7.... My own code throughout (string replay in Python; GAP `EpimorphismPGroup` for B0; project `wordreduce` with the kbprog systems whose sha matches the record). No word printed or copied into this note.

## 1. The 3 emptied words (C3r2|2,3|1, |3, |9): CONFIRMED
One adopted R step each (W length 1150, 1146, 1038 to empty). From the step's cells (conjugator, literal fifth power) and rotation only: freely reduced product of conjugated cells + rotation + result + rotation^-1 equals W, with result empty; all cores are literal fifth powers. The chain certificate (W = P, P a product of conjugates of fifth powers) replays too. So each W is a product of conjugates of fifth powers, trivial in B(2,5) by definition (L0). The record's `certificate` for the empty word is vacuous (the product frees to empty); the chain is the content. Status `tested: broken`.

## 2. The 18 changed non-empty words: CONFIRMED
- **B0(2,5)** (the 5^34 quotient, G_7 relators, GAP class-13 p-quotient): the new word is trivial for 18/18 (21/21 with the emptied; the 21 W also trivial). Necessary only: it cannot tell a wrong word from a right one.
- **Chain continuity:** for all 21, W -> step outputs -> final word is consistent. Every adopted R step replays from its cells + rotation (free group, 0 failures); the R steps with no trace are unchanged-length, in = out.
- **12 certified** (3 emptied + C3|4|13, C3|4|15, C3|6|12, C3|6|25, C3|9|25, C3r2|2,3|0, |18, |19, C3r2|3,3|29): L0 over the per-word table replays to the new word, `L` = largest primitive-root period, cell counts match, table entries are literal fifth powers, chain W = P g^-1 word g replays (12/12).
- **9 uncertified** (C1|24|29, C3|4|2, C3r2|2,3|8, |15, C3r2|3,3|12, |15, |17, |23, |25): the R steps replay; the D steps (1, 1, 1, 1, 3, 2, 1, 1, 1; all outcome "shorter", in and out lengths listed, rml 7, bound 20M) are listed in `not_certified`. I did NOT re-run D; the D steps are equalities in G_7 (hence in B), kbmag-free, but not certified.
- All 21 `W_certificate` replays to W; and all 205 certified records of the file (L0, chain, W certificate) replay: 205/205, 0 failures.

## 3. The 12 T3u failures (S1-each at KB): CONFIRMED
With the 16 images built as tcgraph does (swap x signs x inverse) and every rotation, `wordreduce` on the systems in the record (rec sha 436fd2c7, slx sha 75b12c59): kbmag output is shorter than the image already on the identity image, by the slx system, for all 12. Gains (word length, KB length): 223/145, 538/533, 498/494, 1015/1003, 432/424, 713/709, 203/187, 657/656, 668/654, 762/752, 669/659, 429/428. So `NOT T3u (KB)` is right by the strict S1-each definition. Two are a single letter (657/656, 429/428). The converse: for the 6 T3u passes (C3|4|15, C3|6|12, C3|6|25, C3r2|2,3|15, |18, C3r2|3,3|29) no image of the 16, no rotation, no system gives a shorter output (96/96 image tests). I re-ran only KB; R, CL, D1, S2-chain and the held-out solvers (the 0/18 broken) are the Developer's.

## 4. The 199 unchanged records: CONFIRMED
Equal to the old file in every field; the only additions are `r_from_w_portfolio` and an empty `history`. Top-level changes: description, code, inputs_sha256, change_log (+1), tested, r7_core_table_cited; nothing removed. Statuses 217 not a candidate + 3 broken; T3u: 199 + 6 = 205 true, 12 false, 3 none; certified 205, uncertified 15. These match the report.
`r_from_w_portfolio` is internally consistent on all 220 (changed iff best < before; word length = best if changed else before; best = min of the 12 orders). In 44 unchanged records the best chain end from W is LONGER than the file's word (the file's word stays under the adopt-if-shorter rule). Not an error, but "<= every earlier result" refers to the final words, not to the best of the 12 chains.
Against the owner's file: new length <= the owner's reduction length on 220/220 (strictly shorter on 55).

## Consequences and scope
- **Registry rev 2 draft:** two of its 9 certified records, `t028_C3r2_2-3_1` and `t028_C3r2_2-3_3`, are now emptied by R from W (rev 3, native order). They must become `tested: broken` like C3r2|2,3|9, and their "unchanged under tie-break variants" label was true only for the residual, not for R from W. The other 7 draft ids are not among the 21 changed.
- **Escalation:** the B / B-ext ladders ran on the old words; the changed words carry "escalation NOT re-run". Do not carry the old ladder labels over.
- **Certificates** prove triviality in B(2,5) (L0 and the chain; fifth powers of any period), not in G_7. Held-out and gates are about G_7 / solver resistance, each scoped as before.
- **Selection effect:** the word kept is the best of 12 orders plus D; it is "unchanged by R" only for the order set tried.

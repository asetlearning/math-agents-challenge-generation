---
type: validation
date: 2026-10-26
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028: B0 check of the owner's 11 shorter words; the tcgraph 26f4f5a -> 3673013 diff for R"
status: necessary checks pass; not a certificate
---
# Owner's 11 shorter words: B0 check

Triage: none separate (cheap necessary check, scope below). Source: the owner's verification file in the vault `shared/` (read only, nothing run inside it, words not copied into any note; the scratch copy sits outside the repo).

## (a)(b) Result
- 11 records with a non-empty `our_word` (206 null, 3 empty, as in the summary). Ids: C1|24|29, C3|6|25, C3|4|13, C3r2|2,3|{19,15,18}, C3r2|3,3|{12,17,25,15,29}. None is among the 9 registry-draft records.
- **(a)** Image in B0(2,5) = the 5^34 quotient (GAP `EpimorphismPGroup`, class 13, relators = the 255 classes of G_7): **trivial for 11/11**. Sanity in the same session: a b and [a,b] nontrivial, (ab)^5 trivial.
- **(b)** All 11 are in the alphabet {a,A,b,B}, freely reduced and cyclically reduced. Exponent sums are non-zero but all multiples of 5 in both generators, i.e. trivial in G_7^ab = C5 x C5 (the only abelian-trivial test that applies).
- Lengths 223..767; deltas against our survivors' word -12..-282.

## Scope
Necessary only. B0 triviality means the word lies in the kernel to the restricted 5-quotient, which every word equal to a product of fifth-power conjugates does. It does not show that the word is trivial in B(2,5) or that it equals W; that needs the traced certificates W -> new word (Developer, item 1). The words also say nothing about breaking: 3 of the 14 shorter ones are empty.

## Lead's diagnosis (tie-break is the only semantic R change)
Read `git diff 26f4f5a 3673013` in the tcgraph checkout (greedy_reduction.h/.cpp, word.cpp). In `greedyReduceImpl` the semantic change is the tie-break: the square bases are now sorted short-lex before the first best score wins (f4b7771). Other changes are refactors by reading, not by test: rule application split to carry a trace, a `RollingHash` class in place of the inline modular hash, a linear-time least rotation in place of the min over shifts, and the traced variants. The header comments "cyclically reduces" became "freely reduces": the code called `.reduce()` before and after, so this is a comment correction. I have not run the two builds against each other, so "only" is supported by reading.
Two additions:
1. **Platform.** Before f4b7771 the tie order was the iteration order of an unordered_set, which differs between libstdc++ and libc++ (the code comment says so). If the owner ran 26f4f5a on a Mac, it differs from our libstdc++ runs of the old order too. So the old-order variant (bc6b97f on Linux) need not equal the owner's run.
2. **Start point.** Our tie-break variants ran from the residual (an R-fixed word for all variants, 215 of 220), not from W. R from W is path dependent, so a shorter word from W does not contradict "residual unchanged under variants". The 52 words where the owner's result is longer than ours point the same way (a different path, not a bug in one build).
Discriminating test, if wanted: R from W with tie seeds 1..5 (tcgraph-tieseed) for the 11 words, and see whether lengths as short as the owner's occur (ids and lengths only).

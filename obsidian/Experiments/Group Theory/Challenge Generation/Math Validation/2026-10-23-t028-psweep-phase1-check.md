---
type: validation
date: 2026-10-23
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028 period sweep Phase 1: the p=9 break and the reading of p>=8"
status: confirmed-with-scope
---
# T-028 period sweep Phase 1 check

Triage: [[2026-10-23-t028-psweep-phase1-check-triage]]. Run: rjob 20261023-153651-014aa2, b25 0a5cff2 (outputs ids and outcomes only). F0 words are g u^5 g^-1 (g of length 3-5, u primitive of length p), not survivors; opening them is allowed.

**Verdict: (1) CONFIRMED at the kbmag level, scoped; no relator-level certificate yet. (2) The p>=8 reading is sound only as "no kbmag break"; it does not support a statement about G7 or about period.**

## (1) The F0|9|2 break

| # | Check | Result |
|---|---|---|
| 1 | Input words | `psweep_f0_words.jsonl` sha256 equals the run's `inputs.sha256` entry (84ad5c4f...). All 33 words: freely reduced g u^5 g^-1, u primitive and cyclically reduced, |u| = p, 3 per p in {5,7,8,9,10,12,14,16,20,24,28}; length column matches. |
| 2 | Model | `ho_rec`/`ho_slx` (1x), and the 4x/16x sets, carry the same 815 equations as `b25_full` (identical as sets). Every equation is a fifth-or-higher multiple power of a word of length <= 7 (parsed myself: 815 of 815), and all 255 classes of primitive words of length <= 7 (up to rotation, inversion; my own enumeration) occur. So the presentation is G7 = <a, b \| v^5, \|v\| <= 7>; the input hashes of the 1x system equal those in `inputs.sha256`. |
| 3 | Re-run | `wordreduce -kbprog ho_rec` on F0\|9\|2 (rotation 0) prints IdWord. With `ho_rec` at 1x, 4x and 16x, all 51 rotations reduce to IdWord; `ho_slx` at the same three budgets reduces none (shortest output 45). |
| 4 | Harness sanity (`ho_rec`, 1x) | 300 random words with non-zero abelianization mod 5: 0 reduce to IdWord. 100 conjugates of fifth powers of period <= 7: 100 reduce to IdWord. 300 random commutators: 3 reduce, two freely trivial; the third (34 letters) is trivial in B (checked in the 5^34 quotient). No sign of an inverse/letter-mapping bug. |
| 5 | Certificate | Not obtained. The project's `certify_word` rewriting path (leftmost-shortest) does not reach IdWord from any of the 96 rotations of the word (51) or of u^5 (45), and my own stack-based emulation of kbmag's reduction does not reproduce kbmag's outputs (checked on 6 words), so I cannot replay the break as a product of conjugates of period <= 7 fifth powers. |

**Reading "u^5 follows from fifth powers of period <= 7".** Sound for this u, with this evidence: a kbmag rule is an equation derived from the 815 relators by Knuth-Bendix completion, so a reduction to IdWord proves g u^5 g^-1 = 1 in G7, hence u^5 = 1 in G7 (modulo kbmag being correct; item 4 supports the I/O mapping, not the solver itself). Conditions to state with it: (a) one word, one system (`ho_rec`; `ho_slx` does not confirm); (b) not a certificate over the R7 table. To close (b): run kbcert's fallback (cyclic closure) or ask for the path-recording reduction, then replay with the L0 check as for the registry (my replay code does this in seconds). Until then the label is "kbmag IdWord, replayed by re-running wordreduce", the same standard as the 'theorem_breaks' list in the summary.
It does not follow that G7 = B, nor that other period-9 words are consequences (2 of 3 at p=9 were not broken).

## (2) What the sweep supports

Counts: p=5, 7: 6/6 broken at 1x (expected, they are relators up to conjugacy: a positive control, not a finding). p>=8: 1 of 27 words broken (p=9: 1/3). p=8: 0/3. p=10..28: 0/21. For all 26 non-broken words kbmag 1x, 4x, 16x ended 'exhausted' (the systems are not confluent: 'exhausted' means no IdWord from any tried rotation). D (rml 7, 2^24..2^28 cosets): 9 words 'exhausted' (peak RSS up to 16 GB), 17 'shortened' (the call stops at its first throw, so no D result); no 'nontrivial'.

May be said:
- Exactly one of 27 words with p >= 8 is a consequence of the period <= 7 fifth powers by `ho_rec` (F0|9|2). The others were not shown to be consequences by two non-confluent kbmag systems at three budgets, and by D for 9 of 26.
- Break depends on the word, not only on p: 9|2 broke, 9|0 and 9|1 did not (for 9|0 the kbmag output is longer than the input, 80 against 55; 9|1 not looked at).

May not be said:
- "u^5 is not a consequence for p >= 8" or any nontriviality in G7. Non-confluent KB failing to reach IdWord is not evidence of non-triviality; D finished 'nontrivial' on none. Phase 0 (no nilpotent witness at k >= 7) means no finite 5-group quotient can ever show u^5 != 1 in G7, so "0 nontrivial" is expected and uninformative.
- A trend in p (8: 0/3 but 9: 1/3 is not monotone; 3 words per p; for 0/21 the 95 % upper bound on the true break rate in this family is about 14 %; for 1/3 the interval is roughly 1 % to 91 %).
- Anything about words outside this family: F0 words are conjugates of u^5 with g short, with a perfectly periodic core. A challenge residual is not of this form.
- "Period" as a hardness parameter beyond: it supports that period-9 consequences exist (one instance) and that the held-out kbmag sees one at 1x cost (0.9 s).
- That the D rungs are untested for 17 words; the D-only rerun that is going now is what fills it.

## Not checked

The other 26 non-breaks (my only re-runs: 9|0, 8|0, 10|0, 5|0, 7|1 in the emulation comparison), D rungs, the rjob run itself, and the correctness of kbmag. Rotation 0 as stated in the break record matches my re-run (all rotations break, so the choice does not matter).

## Addendum 2026-10-25: recorded kbmag path for F0|9|2
Path file `runs/t028-psweep-f0-path/f0_9_2_ho_rec_path.json` (546 steps, 19 rules). Replay with my own string rewriting (position, rule; no free reduction): every step matches its lhs and the word ends empty. All 19 rules (lhs = rhs) hold in the 5^34 quotient of G_7 (GAP `EpimorphismPGroup`, class 13): a necessary check only, the quotient is B's restricted quotient. The 18 rules certified by cyclic closure are the project's; I did not re-certify them. Rule 12 (lhs length 50) has no relator-level certificate, so the break stays "kbmag IdWord, path replays; rule 12 modulo kbmag". No problem found.

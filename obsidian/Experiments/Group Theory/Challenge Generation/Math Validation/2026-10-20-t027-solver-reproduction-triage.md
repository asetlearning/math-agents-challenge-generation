---
type: validation-triage
date: 2026-10-20
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-027: independent reproduction of the owner's solver chain on the 12 T-024 confirmed words; soundness of the chain; B0(2,5) and kbmag checks of the 3 residuals"
---
# T-027 solver reproduction: triage

This is a Lead request (2026-10-20). The owner's materials are read-only and are not copied into the vault: the residual-word note and JSON (2026-10-19) and the scripts `check_t024.py`, `decide_t024.py`, `iterate_t024.py` and `escalate_t024.py`. The input is Lead's private `t024-confirmed-words-2026-10-19.json` (sha256 `cd1ae09d…1c17be`).

## Claims

The owner reports these results for the 12 words, using the chain below.
- **C1.** 8 words reduce to the empty word: ds125, ds368, ds160, ds566, ds145, ds512, ds781 and ds547.
- **C2.** ds94 and ds764 end at the same 47-letter residual, `T024_R1`. The owner says "up to cyclic shift and inversion".
- **C3.** ds665 ends at `T024_R2` (47 letters).
- **C4.** ds519 L3 reaches 251 letters at D(20M, 5), and `T024_R3` (249) only at D(1e9, 9).
- **C5.** The per-step length chains are as stated in the owner's note.
- **C6.** "Each step preserves equality in B(2,5), so the original is trivial iff the residual is."

**Terms.**
- **R** = `greedy_reduce_cyclic_exhaustive2_5`. It rewrites a power u^p, 2.5 < p < 5, to u^{-(5-p)}, on cyclic shifts of the word, and repeats until nothing changes.
- **D(bound, rml)** = `attempt_to_decide_if_trivial`. It runs Todd–Coxeter coset enumeration (over the trivial subgroup) with relators v⁵, |v| ≤ k, for k = 1 … rml (rml = relator max length). It throws `ShorterLengthFound(u)` when the geodesic to the end vertex of the word's path gets shorter than the word.

## Sub-claims and methods

| sub-claim | method | what it proves |
|---|---|---|
| C1–C5 | Re-run the chain with b25 main `d1b5d0f` (tcgraph pin `63564c3`), built by me from a clean export. My own driver follows the owner's logic, stores every D output and R output, and gives a step-by-step length chain. It also compares with the owner's chains and the owner's residuals: exact, rotation, or inverse rotation. | It reproduces the computation on the current code. The owner used tcgraph `26f4f5a`, which is 46 commits earlier, so differences are possible and will be reported. |
| C4 | Run locally only up to D(20M, 5/7) (251). No 1e9 run: the capjob limit is 2 GB, and the 200M run OOMs. | It reproduces 251 only. The 251 → 249 step stays the owner's (unverified). |
| C6 | Source reading, tcgraph `63564c3`: `word_problem.cpp`, `tc_graph.h` (`track_word_length`, `get_min_word`, `completeWith`) and `greedy_reduction.h/.cpp`. | It states what each step guarantees: the group in which the equality holds, and equality versus conjugacy. |
| Step-wise sanity | For every intermediate word: abelianization in Z5², plus the B0 image (below). | Necessary conditions for each step to preserve the class of 1 in B(2,5). |
| B0(2,5) | The existing GAP script `b0_challenge_triviality.g`: anupq `PqEpimorphism` with class 12, order 5^34, and its 5 controls. Run on the 3 residuals and on the 4 originals ds94, ds764, ds665 and ds519 L3. | **Necessary only**: trivial in B(2,5) ⇒ trivial in B0. |
| kbmag | `kb_reduce_words.py` with `wordreduce` and the kb-verify-20261007 rec / slx kbprog systems (b25_full). | Sufficient for triviality if the word reduces to IdWord. A non-empty result proves nothing, because the systems are non-confluent. |

## Tools probed

- GAP 4.15.1 with the anupq, autpgrp and kbmag packages (kv10 binaries).
- The B0 script: `b0_challenge_triviality.g`. It is identical in the b25 agentic checkout and in runs/challenges-nonempty-verify-20261007, where it took 4.6 min. It is not in b25 main.
- The kb systems rec / slx and their `.kbprog` files are in runs/kb-verify-20261007.
- capjob is available. The VM has 4 CPUs and about 5 GB of RAM.

## Limits

- Nothing here decides the 3 residuals. D, B0 and kbmag are each one-sided.
- The 1e9 step for ds519 is not reproduced. It would need an rjob on the Mac, and I will plan that with Lead first if wanted.

## Recommendation

Full reproduction is possible up to 251. Run the steps one at a time under capjob with 2 GB / 2 CPUs: build, chain, B0, kbmag.

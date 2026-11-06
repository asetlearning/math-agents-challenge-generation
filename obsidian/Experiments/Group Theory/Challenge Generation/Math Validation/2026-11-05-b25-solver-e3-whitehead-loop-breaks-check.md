---
type: validation
date: 2026-11-05
author: Validator (asetlearning)
project: "[[project-b25-solver]]"
subject: "E3-whitehead-loop: breaks of C3|4|13 and C3|4|28 (steps W, R, W, R)"
status: verified
tags: [agent/validator, user/asetlearning, domain/group-theory, topic/b25, project/b25-solver, status/verified]
---
# E3 Whitehead-loop breaks

Triage: [[2026-11-05-b25-solver-e3-whitehead-loop-breaks-check-triage]]. Own pure-Python free reduction (`python -I`, script outside the data). Inputs: `runs/b25-solver/E3-whitehead-loop/fix/fix_C3_4_13.json` and `fix_C3_4_28.json` (job on cpuserver; b25 4e6ce8e, tcgraph 7937e99), the E3 fix input, registry rev 3 in `data/`, and the E3 export code. No word strings here.

## Verdict: both CONFIRMED (L0 certificates)

| id | start word == rev-3 word | cells | cores literal 5th powers (reduced) | max period | free reduction of prod conj^-1 core conj == registry word | g |
|---|---|---|---|---|---|---|
| C3\|4\|13 | yes (492) | 108 | 108 / 108 | 32 | **yes** | empty |
| C3\|4\|28 | yes (608) | 123 | 123 / 123 | 36 | **yes** | empty |

Cells above period 7 are allowed in an L0 certificate.

## Route (all four steps of each chain, replayed)
- **Link.** in_word of each step equals out_word of the previous one; the last R step ends in the empty word. Lengths C3|4|13: 492 -> 458 (W) -> 436 (R) -> 423 (W) -> 0 (R); C3|4|28: 608 -> 589 (W) -> 336 (R) -> 327 (W) -> 0 (R).
- **W steps.** phi_inverse is a → aB, b → b for C3|4|13 (both steps; conjugators empty and `B`) and a → ba, b → b for C3|4|28 (both steps; empty conjugators); start empty everywhere; `equality` false. These are elementary Nielsen (Whitehead) automorphisms (right multiplication of a by b^±1). In all four W steps in_word == phi_inverse(conj) phi_inverse(out_word) phi_inverse(conj)^-1 exactly in the free group.
- **R steps.** For all four, in_word == (product of the trace cells) . rotation . out_word . rotation^-1 exactly; trace cores are literal fifth powers (29 and 79 cells for C3|4|13; 80 and 43 for C3|4|28). The last R step has empty result, so its cells alone give its input.
- **Independent pullback.** From the last R step's cells I pulled back by hand: through W2 (phi^-1 of each cell is a conjugate of the fifth power of the reduced word phi^-1(v), re-expressed with a cyclically reduced base and the extra conjugator), then R1 (its trace cells followed by the pulled cells conjugated by the rotation), then W1. At each stage the product equals that stage's word, and the final product equals the registry word. The pulled-back list has 108 / 123 cells, the same count as the published certificate, and every core is a literal fifth power. So the published certificate is what this route gives, and each stage is consistent with phi^-1.
- **automorphic_image** is false in both: the chain does not use a global image of the word under a letter automorphism; the automorphisms are the W steps above, each carried with its phi^-1 and conjugator.

## No recipe use
- The fix input (`e3/fix_input.json`, built by `e3_export`) has for each of the 207 words only the word, `origins.W` set equal to that same registry word (all 207 checked), an empty start chain, and the t028 id. The words are exactly the 207 registry rev-3 words. No construction record, recipe, t-word or earlier certificate.
- The job reads the kbmag systems and the t-pool / R7 table files as for any fix-loop run (as the existing bench loop does); the loop's W step uses only the current word.

## Not checked
Reproducing the Whitehead choice, the R search or the kbmag stages; whether the other 205 words are affected (a registry question).

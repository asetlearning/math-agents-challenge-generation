---
type: validation-verdict
date: 2026-10-19
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-017: plan v2 confirmed against the review; Step 4 (M2') power-move closure on the 12 confirmed words"
verdict: "v2 CONFIRMED (3 non-blocking nits). M2': no word reaches 1 by power moves alone. The 7 strictly power-free words have none (argued, and the BFS finds 0 moves); the 5 exact-half words have closures of size 2-6, exhausted, all at the original length; no cap hit."
---
# T-017: plan v2 confirmation and Step 4 (M2')

This was a Lead request (2026-10-19).
- Plan: `Agents/asetlearning/MathExpert/proposals/2026-10-19-t017-recertification-and-minimality-plan-v2.md`.
- Review it answers: [[2026-10-19-t017-plan-review-triage]].
- Words: Lead's results file (equal to my verified words, letter for letter).

## 1. Plan v2: CONFIRMED

v2 adopts every fix of the review:

| Review fix | In v2 |
|---|---|
| M1 certificate-level (diagram proposes, Peiffer/Hurwitz block, algebraic tests, at most 24 orders) | §3 Step 1 ✓ |
| L0 after every rewrite (hard fail); depth on the re-folded certificate | ✓ |
| (d): exact cyclic equality with orientation; table kept or relabelled | ✓ |
| Admissible u⁵ = primitive and cyclically reduced; "all u⁵" label; extended RelatorMap, class index and closure | Terms, Step 1 ✓ |
| Reference pool 453 (not 820) | §2.4 ✓ |
| Strict lexicographic acceptance; area-neutral depth drops reported separately | ✓ |
| Positive control (area-like words, e.g. line 47: 40 → 24) as a gate | Step 0 ✓ |
| Results as upper bounds "under M1 at \|S\| ≤ k"; "all u⁵" is M1-bounded | §1 ✓ |
| Component certificates as inputs; level-3 tiles by replay, else a labelled parent-only baseline | §2 ✓ (the "weaker test" direction is right: missing tiles can only lower the baseline) |
| H17 measured flip (d) vs flip (d), with S2 vs S2 alongside; three-class tally; ds160 below 4 retires the depth-4 claim | Step 2 ✓ |
| Escalation targets ds160 and the level-3 word; CPU caps | Steps 1 and 3 ✓ |
| M2 replaced by the theorem plus kbcert BFS; KB-system claims dropped | Step 4 ✓ |
| M3 optional, framed as a hardness level | Step 5 ✓ |

**Non-blocking nits.**
1. **Step 0 pass criterion.** My subset-merge results alternated merges with both `closure_fixpoint` variants. M1 should be allowed the same alternation in Step 0, or "area ≤ the Validator's result" can fail spuriously.
2. **Stored values for the "check-only" comparison.** The S2 and flip (d) values in Lead's results file are the rule-(d) values I verified. The pilot's own stored "flip" column was rule (c), so use Lead's file, not the pilot rows.
3. **Components' flip (d).** It is not stored anywhere (`components_max_S2` only), so the flip (d) baseline must be computed in Step 1. It cannot be read from the file.

## 2. Step 4 (M2'): the power-move check

### 2.1 Seven strictly power-free words: the argument

**Claim (argued).** Let w be a cyclic word with no subword of the form x^e, with e ≥ 2.5, for any primitive x (strictly power-free). Then no length-non-increasing power rule applies to w, at any period. This holds for every rewriting system whose rules are length non-increasing, in particular every shortlex system.

**Definitions.**
- A *power rule* is a rule l → r with |l| ≥ |r| such that l r⁻¹ is conjugate in F to u^{±5}, for some cyclically reduced u ≠ 1. Every rule l → r of a KB system on b25_full gives an equality l = r in G7.
- u need not be primitive. If u = x^k with x primitive, every statement below holds with x in place of u and exponents multiplied by k.

**Proof.**
1. Write l = α l' β and r = α r' β, where α and β are the longest common prefix and suffix of l and r. Then l r⁻¹ = α l' r'⁻¹ α⁻¹, so l' r'⁻¹ is conjugate to u^{±5}.
2. **No cancellation inside l' r'⁻¹.**
   - At the junction, the last letter of l' and the last letter of r' differ (β is maximal), so l' · r'⁻¹ is freely reduced.
   - Cyclically, the first letters of l' and r' differ (α is maximal), so the word is cyclically reduced.
   - Corner case: one of l', r' is empty, say r' = ∅. Then l' itself is a cyclically reduced conjugate of u^{±5}.
3. So l' r'⁻¹ is a rotation of u^{±5}, and |l'| + |r'| = 5|u|.
4. |l| ≥ |r| gives |l'| ≥ |r'|, so |l'| ≥ 2.5|u|.
5. l' is a subword of a rotation of the cyclic word u^{±5}. So l' = y^e with y a rotation of u^{±1}, and e = |l'|/|u| ≥ 2.5.
6. l contains l', so w would contain a subword of exponent ≥ 2.5 (for the primitive root, of exponent ≥ 2.5k ≥ 2.5). A strictly power-free w has none. ∎

**Consequence.**
- For ds94, 125, 145, 368, 547, 665 and 764, the power-only path from w is empty under any shortlex system, at any period, so it does not reach 1. These seven are strictly power-free: 0 exact halves, by two detectors, in [[2026-10-18-t024-level2-best-words-verify]].
- The argument applies to the linear word and to every cyclic rotation.
- **Scope:** it says nothing about derived (non-power) rules. Those exist in both kbprog systems and can reduce these words.

**Words with exact halves.**
- On a 2.5-reduced word (no exponent above 2.5), step 4 forces |l'| = 2.5|u|, i.e. a length-preserving flip at an exact half, as the first power move.
- Later states can contain new runs, so whether 1 is reachable is exactly the non-increasing closure of §2.2.

### 2.2 The five words with exact halves: closure BFS

**Run.**
- kbcert's own move generator `_moves` (cyclic mode, periods ≤ 7, every non-increasing 2.5-move: flips at exact halves and shortenings) with `guard._canon_rot` states, as in `kbcert.closure_path`, from b25 `3db063d` (kbcert unchanged since `d31692e`).
- Hit: the empty word or a rotation of an R7 relator core (`RelatorIndex` over `b25_full` with inverses).
- My scratch driver (`scratch/t024verify/m2_closure.py`) differs from `closure_path` only by running each word in its own process, under a 10 CPU-min cap, with no state cap, and by reporting the closure size.
- One local capjob (2 GB, 1 CPU).
- The 7 strictly power-free words were run as a control.

| word | \|w\| | first moves (period, kind) | closure size | min length in closure | reaches 1 | cap hit |
|---|---|---|---|---|---|---|
| ds160 L2 | 261 | 1 (p2 flip) | 2 | 261 | no | no (exhausted, < 0.1 s) |
| ds512 L2 | 378 | 1 (p2 flip) | 2 | 378 | no | no |
| ds566 L2 | 320 | 2 (p2 flip, p6 flip) | 6 | 320 | no | no |
| ds781 L2 | 529 | 1 (p2 flip) | 2 | 529 | no | no |
| ds519 L3 c2 B | 1,548 | 2 (p2 flips) | 4 | 1,548 | no | no |
| 7 strictly power-free (control) | 163–699 | 0 | 1 | \|w\| | no | no |

**Reading.**
- Every closure is exhausted, far below the cap. Every state has the original length, so no flip ever exposes a shortening, and no state is a relator class.
- Each closure is the set of flip combinations of the word's exact halves. For ds566 it has 6 states rather than 4, so one flip creates a further exact half, but still nothing longer.
- The first moves match the exact-half counts and periods in [[2026-10-18-t024-level2-best-words-verify]] and [[2026-10-18-t024-level3-first-word-verify]]: 1, 1, 2 (periods 2 and 6), 1 and 2.
- The control confirms §2.1 at periods ≤ 7: there are no moves at all.

**Conclusion.** **No word reaches 1 by power moves of period ≤ 7 alone.** For the 7 strictly power-free words this holds at any period (§2.1). Every one of the 12 is "closed under power moves" (no move, or only length-preserving flips, at periods ≤ 7), so there is no hardness flag and no second certificate from M2'.

**Scope.**
- This rules out power-only paths. It says nothing about KB paths that use derived rules (both existing systems reduce dataset words that way), and nothing about other certificates.
- For the 5 words with exact halves, the statement is for periods ≤ 7.
  - Extra check (`scratch/t024verify/m2_allperiods.py`): every state of the five closures (16 in all) was tested with my own detector (`cyc_has_power_gt`) for a cyclic power of exponent > 2.5 at **any** period. There is none, so no shortening of any period is available anywhere in these closures.
  - The original words' exact halves all have period 2 or 6, but length-preserving flips of period > 7 *out of the flip states* were not generated. A full all-period closure would add those.

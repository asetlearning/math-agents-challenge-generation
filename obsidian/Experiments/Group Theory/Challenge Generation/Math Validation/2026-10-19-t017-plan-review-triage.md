---
type: validation-triage
date: 2026-10-19
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-017: review of the Math Expert's plan (re-certification and minimality of the 12 confirmed T-024 words) before anything is built"
verdict: "M1 sound with fixes; H17 + baseline sound with fixes (one blocking input gap); M2 unsound as argued (replace by an exact closure check); M3 sound, low value (make optional); M4 defer (agree)"
---
# Triage and review: T-017 plan (re-certification and minimality)

This was a Lead request (2026-10-19). The owner approved T-017 and delegated its decisions to Lead.
- **Reviewed:** `Agents/asetlearning/MathExpert/proposals/2026-10-19-t017-recertification-and-minimality-plan.md`.
- **Data:** Lead's private file `Agents/asetlearning/Lead/results/t024-confirmed-words-2026-10-19.json`. Its 12 words are letter-for-letter the 12 words I verified ([[2026-10-18-t024-level2-best-words-verify]], [[2026-10-19-t024-l1-novelty-recheck-triage]]).
- **What this review covers:** whether the plan is sound. Nothing was built or run beyond reading code and data headers.
- **Sources:**
  - code read in tcgraph main `188f8ae`: `diagram_fold.{h,cpp}`, `strict_depth.h`, `certificate_reduction.h`;
  - b25: `t018/kbcert.py` and `t024_m1_tiling.load_data`;
  - the headers of the KB systems in the 2026-10-07 kb-verify run: `rec.kbprog` and `slx.kbprog`.

**Labels:** *checked* means I read it in code or data. *Argued* means a proof sketch is given here.

## Verdicts

| Item | Verdict |
|---|---|
| M1 patch surgery | **Sound with fixes.** Do the rewrite at certificate level; check L0 after every step. |
| H17 and the bouquet baseline | **Sound with fixes.** One **blocking input gap**: the components' certificates are missing. |
| M2 KB probe | **Unsound as argued.** Replace it with an exact closure check using existing code. |
| M3 bounded lengthening | **Sound.** But its value for T-017 is low, so make it optional. |
| M4 proof-recording port | Defer (agree). |
| §1.2 (lower bounds as a non-goal) and §4 (drop R8/R9) | Agree. |

## 1. M1, patch surgery

**How the diagram is built (checked).**
- `diagram::fold` makes the bouquet of lollipops c⁻¹ r c and glues it along the leftmost-stack free reduction of the boundary word. Positions are unified with union-find.
- The stack matching is nested, so the result is a planar singular disc diagram, possibly non-reduced. It can have cut vertices and filaments, and stem-only "cancelled sphere" classes are allowed.
- The verify check allows any edge class with exactly two free sides. That includes a class whose two cell sides belong to the **same cell**, reached through a chain of stems, so a cell can be glued to itself.
- `d.cell` maps every head position to its factor index. So a set of diagram cells is a set of certificate factors.

**Is "patch" well defined? Not as written.**
- The plan's definition, "an edge-connected set of cells whose union is a disc", needs an explicit test. Even 4 cells can surround other cells, giving an annulus. A self-glued cell, or a pinch at a cut vertex, can make the union not simply connected, or make its boundary more than one closed walk.
- Reading a patch's boundary word also needs the rotation system at each vertex (the cyclic order of edges). The `Diagram` struct does not store it.
- Most importantly, after surgery the altered diagram has to become a **certificate** again, because depth is measured on fold(certificate). tcgraph has **no diagram → certificate readout** (checked: grep, none found). The 1.5–2 day estimate does not include one.

**Fix (recommended): diagram-guided, certificate-level surgery.**
- Use the folded diagram only to **propose** sets S of up to 4 factors that are edge-adjacent in the diagram.
- Make S contiguous by moving its members together. Each factor that a member passes is conjugated, so it stays a cell; this is the Peiffer/Hurwitz move.
- Then test the ordered block product P_S **algebraically**, in each order of S (at most 4! = 24). Writing P̂ for the cyclic reduction of P_S:
  - (a) P_S = 1 in F;
  - (b) P̂ is a rotation of r^{±1} for some r in R7;
  - (c) P̂ is a rotation of u^{±5};
  - (d) P̂ equals, up to rotation and inversion, the class of a cheaper block P_T stored elsewhere. Then P_S = h P_T^{±1} h⁻¹, and T's cells, conjugated by h (and inverted and reversed for −1), replace S.
- This is my earlier non-contiguous subset merge ([[2026-10-16-t018-area-like-dataset-words-check]]), with the diagram cutting the candidates from O(N⁴) to about N·Δ³ (Δ = dual degree).
- **Soundness is then algebraic**, whatever the folding pathologies. It needs no disc test, rotation system or readout.
  - Mandatory: re-expand (L0) after every accepted rewrite.
  - Re-measure depth on the **re-folded** certificate.
  - For a disc patch in a compatible order, P̂ is the patch boundary (argued). For a non-disc set, only the hit rate suffers, not soundness.

**Are cases (a)–(d) sound replacements?**
- (a) and (b): sound (argued; a one-cell or zero-cell filling of the same element).
- (c): sound for B(2,5). It needs **u primitive and cyclically reduced**:
  - (a²)⁵ = a¹⁰ has root a, so S2 would absorb it as a |v| = 1 cell, and it would count as 1 cell when it stands for 2.
  - For |u| ≤ 7 it is case (b). For |u| > 7 the certificate moves to the all-u⁵ table, so label it.
- (d): sound under three conditions:
  - a hash hit must be confirmed by **exact** cyclic-word equality, with orientation (the mirror for an inverse);
  - the cheaper filling must be over the same table, or the result is relabelled;
  - each replacement must be L0-checked.
  - **Correction to the plan:** there are no "820 dataset certificates". `load_data` holds the T-018/T1 certificates of **453 of the 491** power-free dataset words (checked), and the 820-word set has no certificates.

**Depth with u⁵ cells outside R7 (checked in `strict_depth.h` and `diagram_fold.h`).**
- The root length is `Word::minimalPeriod` of the cell's cyclic core. Flip (d) uses 2.5|v| for every |v|. `fold` converts non-cyclically-reduced table entries to their cores.
- So an extended `RelatorMap` (R7 cores plus primitive cyclically reduced u⁵) leaves the S2 and flip (d) semantics unchanged. RelatorClassIndex and closure must be built from the extended map.
- Caveat: "over all u⁵" results are bounded by M1 (patches of at most 4 cells). They are not minima over B(2,5).

**Termination and artefacts.**
- Depth is a function of the certificate, including the order and conjugators of its cells, because the fold depends on them.
- So an "area-neutral swap that lowers depth" may be only a re-presentation of the same filling.
- Require a strict lexicographic decrease, (area, flip, S2) or (flip, S2, area) for the depth-first run. Report area-neutral depth drops **separately** from real area reductions.

**Positive control (missing).**
- M1 must reproduce the cheaper certificates that my subset merge found where the pipeline did not, on the 7 area-like dataset words. Example: line 47, three 3→1 merges, 40 → 24 cells.
- It must also leave the 12 pipeline certificates' L0 intact.

## 2. H17 and the bouquet baseline

- **Same-method minimisation of the components is the right pairing.** Comparing an M1-minimised word with an unminimised baseline would mix the effect of the method with the effect of the construction.
- Both sides are **upper bounds**. So H17 holding at budget k means: under M1 at |S| ≤ k, the word's minimum depth found exceeds the components' minimum depth found. It is not an inequality between true minima. The record should say that.
- **Blocking input gap.**
  - Lead's results file holds only the words' certificates (keys: word, certificate, n_cells, components_max_S2), not the components' certificates.
  - My replay dumps have the parent and tile certificates for the 11 level-2 words (`F1_cells`, `tiles`).
  - The timing job's dump for the level-3 word has the parent `ds519_L2_c2` but **not the tiles** (caveat in [[2026-10-18-t024-level3-first-word-verify]]).
  - These must be supplied first: by re-running the level-3 seed with a tile dump, or by Lead accepting the parent alone for the level-3 word.
- **Measure mismatch.**
  - `components_max_S2` is S2, but the word is judged by flip (d), and ds781 is "flip (d) 2 > 1".
  - In my level-2 note the components' S2 and flip (d) differ for ds368 and ds764 (2 vs 1).
  - Declare one measure on both sides and report both pairs: S2 against S2, flip (d) against flip (d). The mixed comparison (word flip against components' S2) is the stricter one; it is acceptable if declared.
- **Thresholds** (≥ 6/12, 1–5/12, 0/12): acceptable as a pre-registration, with three changes:
  - (i) Define "loses depth" as H17 failure (flip ≤ the components' maximum). Tally partial drops that stay above the baseline (for example 4 → 3) separately, so a drop of the depth-4 claim is visible.
  - (ii) The |S| = 5–6 escalation at 0/12 should target the **headline claims**: ds160 (the only flip-4 word) and the level-3 word. It can be cost-capped, or run on the two shortest words in addition.
  - (iii) Add a CPU cap per word and per pass.

## 3. M2, the KB probe: unsound as argued

**Facts (checked).**
- `b25_full` is the kbmag **input** file (815 equations [v⁵, IdWord], |v| ≤ 7), not a rewriting system.
- The two existing systems are both `isConfluent := false`, at maxeqns 2,000,000:
  - `rec.kbprog`: recursive ordering, about 97k rules;
  - `slx.kbprog`: shortlex, about 100k rules.
- So a ReduceWord that **fails** proves nothing. "KB-hard" can only be stated per system.
- A ReduceWord that **succeeds** is sound but not a hardness signal: every one of the 820 dataset words reduces to 1 under at least one of these systems.

**The registered argument is false for `rec.kbprog`.**
- Under recursive ordering the power rules lengthen, e.g. `[A, a^4]`, the rule from a⁵ with A = a⁻¹.
- A power-rule path there is not "shortenings and flips".

**Under shortlex the prediction is (argued) a theorem, or reduces to an exact computation that existing code already does:**
- Take a power rule l → r with |l| ≥ |r| and l r⁻¹ conjugate to u^{±5}. After stripping any common prefix or suffix of l and r, l contains a subword of the cyclic word u^{±5} of length ≥ 2.5|u|.
- A 2.5-reduced word has no subword of exponent > 2.5 for **any** period. So only equal-length (exact-half) rules can fire first.
- **7 words have no exact half** (strictly power-free: ds94, 125, 145, 368, 547, 665, 764). No power rule of any period applies to them, so the prediction holds trivially.
- **5 words have exact halves** (ds160, 512, 566, 781 and the level-3 word, with 1–2 each). For them, "a power-only path to 1 exists" is exactly "1 is in the non-increasing 2.5-move closure". That is the breadth-first search (BFS) `kbcert.py` already runs for periods ≤ 7. So the prediction can be settled **exactly, without any KB run**, in minutes.
- Note: L1 (ρ_min16 = 1) does **not** "exhaust" this move set. The reducer is greedy and is not a closure search. The BFS is the exact check.
- "No new code" is wrong for the plan's M2 as written: classifying rule kinds along a ReduceWord path needs an instrumented rewriter.

**Recommendation.** Replace M2 by:
- (i) the theorem above for the 7 strictly power-free words;
- (ii) the kbcert BFS on the 5 words with exact halves.

The §4 sub-task (the 38 words) is unaffected. If wanted, run kbcert on them as before.

## 4. M3, bounded lengthening

**Sound as a cell (argued).**
- Let p be the prefix of u^∞ of length e|u|, and q its continuation up to 5|u|. Then p q = u⁵, so p = q⁻¹ in B(2,5), and replacing p by q⁻¹ multiplies by one conjugate of u^{±5}.
- It is an R7 cell only when the class of u⁵ is in R7 (|u| ≤ 7). Require u primitive and cyclically reduced, as for M1 (c). L0 must be checked on the resulting certificate.

**Independent of the onion: yes.** It uses no tiles or component certificates.

**Value.**
- At budget 0 its move set is the L1 reducer's, and all 16 images of all 12 words are reducer fixed points. So that rung only tests beam search against greedy.
- With at most 40 letters of total lengthening against words of 163–1,548 letters, I expect (conjectured) "M3-hard" for most words. That gives a hardness level, not an upper bound on depth.
- Keep it as an optional probe, off T-017's critical path.

## 5. Missing items and cheaper routes

1. **Certificate-level M1** (§1): no readout, no disc test, soundness by L0. Its CPU cost is the same order as the plan's estimate. The Developer cost is probably lower, because it reuses the subset-merge logic and the Peiffer machinery in `certificate_reduction`.
2. **M2 replaced** by the theorem plus the existing kbcert BFS (§3): minutes instead of hours, with an exact answer.
3. **Component certificates** for the baseline (§2): needed before M1's H17 tally can run, especially the level-3 tiles.
4. **Positive control** for M1, and a **same-measure** H17 (§1, §2).
5. Optional: an independent R7 certificate from the existing kbcert (rewriting path), on the two or three shortest words only.
   - Its depth is a second upper bound unrelated to the onion.
   - Its area will be far larger (T1 gave up to 1,197 cells for words of 123 letters), so it does not tighten area.
   - It is pure Python, so it needs Lead's approval, as T1 did.

## Decisions (Lead, 2026-10-19; delegated by the owner)

Lead accepted the review in full and decided:
1. **Level-3 tiles.** The Experimenter re-runs seed 519 with a tile dump.
   - It is accepted only if the replayed word equals the stored one letter for letter.
   - Otherwise the baseline for that word is parent-only and is labelled as such.
2. **H17 headline.** Flip (d) of the word against flip (d) of the components. S2 against S2 is reported alongside, so each word has both pairs.
3. **Optional kbcert run.** Approved for ds125 and ds368, after M1, as a local capjob under a CPU cap that I set.

The Math Expert writes a v2 plan from this review. I check that v2 matches the fixes before anything is built.

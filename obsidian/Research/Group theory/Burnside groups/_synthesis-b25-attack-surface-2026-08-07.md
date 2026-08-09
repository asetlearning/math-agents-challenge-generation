---
title: "Synthesis — literature attack surface for B(2,5) infiniteness (2026-08-07 campaign sweep)"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/b25
  - topic/burnside-infiniteness
  - topic/small-cancellation
  - topic/uniformity
  - topic/kourovka
  - synthesis
  - status/draft
papers_synthesized:
  - "[[coulon-2018-even-exponents]]"
  - "[[coulon-school-partial-periodic-quotients]]"
  - "[[_synthesis-odd-exponent-state-2026]]"
  - "[[atkarskaya-rips-tent-2023]]"
  - "[[lysenok-2023-sample-iterated-sc]]"
  - "[[kourovka-11.48-kostrikin-1990]]"
key_concepts: []
status: draft
project: b25
---

# Synthesis — literature attack surface for B(2,5) infiniteness (2026-08-07 campaign sweep)

## The question

Lead's brief (2026-08-07, Maria directive: all resources engaged, campaign first tasking): four ranked sweep targets against the standing internal result set (kernel(B(2,5)→R(2,5)) = γ₁₃ = γ_ω; prime witness E7 = [a,₆b], 6-Engel, no finite counter-certificate possible; E7≠1 proven through G₁..G₄; uniform-in-ℓ routes DEAD by exponent-6/Hall falsification; classical C′(1/6) reaches exactly one more rung, G₅). This note does **not** re-derive or re-litigate those internal results — it is a pure literature check against them. It also does not re-run the odd-exponent-bound / ART / Gorshkov ground already covered in [[_synthesis-odd-exponent-state-2026]] (2026-07-31) — this sweep targets net-new ground and is written to be read alongside that note, not instead of it.

**Tooling note:** `WebSearch` was denied by sandbox policy this session (same constraint the 2026-07-31 scan hit for most subtasks). All findings below come from the arXiv API (keyword/abstract search), direct `WebFetch` of arXiv abstract pages, and — where full text was needed — a custom local PDF text extractor (no OCR required; these are all text-native PDFs) run against fetched PDFs. Where a claim is verbatim from extracted full text rather than an abstract, it's marked as such.

## Sources reviewed

New this scan: [[coulon-2018-even-exponents]] (full text extracted), [[coulon-school-partial-periodic-quotients]] (landscape note covering 7 papers, abstract-level: Coulon 1302.6933/1311.0855/1211.4271/1211.4267, Coulon–Sela 2112.07409, Coulon–Steenbock 2102.10885, Gruber–Mackay 1810.01805, Minasyan–Olshanskii–Sonkin 0804.3328). Re-grounded from prior scans: [[_synthesis-odd-exponent-state-2026]], [[atkarskaya-rips-tent-2023]], [[lysenok-2023-sample-iterated-sc]], [[kourovka-11.48-kostrikin-1990]]. Internal grounding read in full before starting: [[Agents/maumayma/MathExpert/ell6-theory-barrier-analysis-2026-08-05|ell6-theory-barrier-analysis]] and its Validator preruling, [[open-problems-catalog]].

---

## Target 1 — Coulon/Gruber-style graded small cancellation: does any published machinery reach exponent 5?

**Verdict: No, and the negative is structural, not a near-miss.**

Full detail in [[coulon-2018-even-exponents]] and [[coulon-school-partial-periodic-quotients]]. Headline finding, extracted verbatim from the one paper fetched at full-text depth (Coulon 2018, Theorem 1.1):

> "Let r > 2. There exists a critical exponent n₀ ∈ ℕ such that for every integer n > n₀, the free Burnside group Bᵣ(n) is infinite."

**No numeric value of `n₀` is ever stated** — not in this theorem, not anywhere in the introduction (the only large numbers present are page-count comparisons against Ivanov/Lysenok's 200/300-page proofs). Checking across the whole Coulon/Gruber/rotating-families line (7 papers, 2008–2021: Coulon solo × 5, Coulon–Sela, Coulon–Steenbock, Gruber–Mackay, Minasyan–Olshanskii–Sonkin), the pattern is uniform: every paper says "sufficiently large," "arbitrarily large," or gives an asymptotic-in-n growth estimate — **none states an explicit reachable constant**, in contrast to the classical combinatorial line (Adian 665, ART 557, Lysenok >2000, Adian 2015's disputed 101), which is already fully catalogued in [[_synthesis-odd-exponent-state-2026]] and is itself ~100–400× above 5.

**This directly matches and reinforces the internal Validator ruling already on record** ([[2026-08-05-b25-ell6-theory-preruling]]): "the published relative-filling theorems all fail at n=5 (AGM torsion-free + slope length 5; DGO cone radius ≫ inj ≤ 20; Coulon n > 100 — already on record in [[LADDER]])." This scan independently confirms the Coulon branch is not merely "n > 100" as a stated number — it's *unstated entirely* in its own primary papers; "Coulon n > 100" appears to be an internal estimate/lower bound derived by the project, not a number Coulon himself publishes. **Recommend Validator/MathExpert double-check whether "Coulon n > 100" in LADDER.md traces to an actual textual source or was inferred** — this scan could not find that number in Coulon's own papers.

**Actionability: low, but decisive as a closed door.** There is nothing to adapt from this literature at exponent 5 — not a weak version, not a partial result, not a "if only λ were smaller" gap to close. The entire school's proof strategy structurally requires an unspecified-but-large small-cancellation parameter; it was never built to be checked against a specific small n. Do not route Developer/Experimenter time toward adapting Coulon-style rotating-families machinery for G₅/G₆ — there is no published version of it at this scale, and (per the exponent-6/Hall falsification already proven internally) any adaptation *would* have to defeat the exact obstruction that's already closed the uniform-in-ℓ route.

## Target 2 — Kourovka 11.48: any published progress, reformulation, or conditional result post-1990?

**Verdict: None found. The problem is exactly as open as already documented.**

Direct arXiv abstract-search for "Kourovka" + "Burnside," "exponent 5" + "Burnside," "Engel" + "Burnside" + "exponent," and "Engel group" + "small cancellation" all returned **zero results** for anything touching 11.48, the weight-7 commutator condition, or exponent-5 specifically. This confirms and extends the 2026-07-31 scan's finding (which searched primarily for the odd-exponent-bound thread) — a differently-angled search this time (direct 11.48/Kostrikin/Engel framing rather than "what's the best n") reaches the same wall.

One adjacent, tangential data point: [[coulon-school-partial-periodic-quotients]] notes that Minasyan–Olshanskii–Sonkin (2008, arXiv:0804.3328) explicitly closes **a different** Kourovka Notebook question, attributed to Wiegold, using rotating-families/periodic-quotient machinery. This is worth recording as evidence that Kourovka questions in this neighborhood *do* get closed by this technique family in general — but it is not 11.48, and (given every other paper in that school's "large exponent" framing) there's no reason to think the same machinery would reach n=5 if pointed at 11.48 instead of Wiegold's question. Not independently confirmed which Kourovka number Wiegold's question is; flagged, not chased further this scan.

**One citation correction surfaced and logged:** the 2026-07-31 synthesis claimed Katrin Tent "presented the [ART] method at ICM 2026 (arXiv:2606.18207) as a general template extending toward Engel-type problems." Independently re-fetched this scan (full abstract + author list) — **this is wrong**. arXiv:2606.18207 is a different, unrelated Tent paper: "From the Cherlin–Zilber Conjecture via sharply 2-transitive groups to the Burnside problem" — a model-theory paper connecting the Burnside problem to potential counterexamples of the Cherlin–Zilber Algebraicity Conjecture via sharply 2-transitive groups. No Engel-type extension of the certification-sequence technique. **Correction has been applied in-place to [[_synthesis-odd-exponent-state-2026]]** with a dated retraction note; no replacement citation for the original (apparently unsourced) Engel-extension claim was found this scan.

That correction itself opens a **very tentative, unverified** side-thread worth flagging rather than chasing: sharply 2-transitive groups as "a potential source of counterexamples" to Cherlin–Zilber, with "the Burnside problem necessarily com[ing] into the picture" per Tent's own abstract — model-theoretic, likely a different kind of Burnside connection (possibly built on Burnside groups as substrate for sharply-2-transitive constructions, a known technique going back to Rips-style constructions) rather than a finiteness-of-B(2,5) result. Not read past the abstract. If Lead wants this chased, it needs a dedicated full-text read before it's actionable — flagging as "maybe," consistent with role discipline on speculative leads.

**Actionability: none directly**, but the negative itself is the useful datum — it closes off "check if someone already solved/reformulated 11.48 since Kostrikin" as a live possibility for this campaign.

## Target 3 — Certifying nontriviality in direct limits without uniform-in-L lemmas

**Verdict: No literature bridge found. This looks like a genuine, not-yet-published gap — profinite, Golod–Shafarevich, and cohomological angles were each checked and each comes back structurally inapplicable or absent, not merely unsearched.**

Three sub-routes checked:

**(a) Golod–Shafarevich-style counting.** Zero arXiv hits for "Golod-Shafarevich" + "Burnside" in combination. Broadened to "Golod-Shafarevich" alone (15 results, including Ershov's 2012 survey) — none of the returned papers address bounded-exponent groups; the field is uniformly about infinite finitely-generated torsion/nil groups or pro-p algebra growth, not groups where every element satisfies a fixed `xⁿ=1`. This matches a real, well-established distinction in the classical literature (not independently re-verified via a fresh source this scan, flagged as general/textbook knowledge rather than freshly cited): **Golod–Shafarevich (1964) solves the *General* Burnside Problem** (existence of an infinite finitely-generated torsion group) **but not the (bounded-exponent) Burnside Problem** that B(2,5)/Kourovka 11.48 actually asks. The counting inequality produces nil groups of unbounded exponent, not fixed-exponent-n groups — the dimension-counting argument doesn't have a natural per-stage certificate that composes into a bounded-exponent limit statement. **This route should be treated as a dead end, not merely unexplored**, and Researcher should double-check this attribution with Validator/MathExpert if it becomes load-bearing for a program decision, since it rests on general knowledge rather than a paper independently re-read this scan.

**(b) Cohomological obstructions.** Zero hits for "restricted Burnside" + "cohomology," and zero for "lower central series" + "free Burnside." Broadened to Zelmanov + Engel generally: found the Wilson–Zelmanov theorem ("Engel profinite groups are locally nilpotent," surfaced via Khukhro–Shumyatsky papers on almost-Engel profinite/compact groups) — but this is a *group-level* statement (a profinite group all of whose elements are Engel is locally nilpotent), not a tool for certifying that one specific Engel element (E7) survives in a specific direct limit. It's adjacent vocabulary, not an applicable certificate mechanism. No paper was found connecting cohomological obstruction theory (H² or otherwise) to the specific question "does this normal-closure element vanish in the direct limit `γ_ω`."

**(c) Profinite completion arguments.** Zero hits for "profinite" + "free Burnside" beyond one unrelated semigroup-complexity paper. The natural profinite-completion idea — if an element has nontrivial image in some finite quotient compatible with the whole tower, it survives in the limit — is exactly what the internal program's "no finite counter-certificate possible" result (every finite exponent-5 group is 6-Engel) already rules out for E7 specifically. The literature offers no alternative profinite mechanism that sidesteps this; it isn't that the literature has an untried profinite technique, it's that the obvious profinite technique is the one already proven unavailable internally.

**Actionability: this is the sweep's most important negative.** All three canonical "prove infiniteness of a limit without a uniform per-rung lemma" strategies either don't apply to bounded-exponent groups at all (Golod–Shafarevich), are group-level rather than element-level (Wilson–Zelmanov/cohomological), or are exactly the strategy already closed internally (profinite/finite-quotient). **No externally-published alternative to per-rung certified geometry currently exists for this problem.** This should be reported to Lead as a genuine open methodological gap, not a research failure — algo_mixing may be at or past the frontier of what's published here, which raises (not lowers) the value of the internal rung-by-rung R6-shell/CE6/CC6-TR-v2 program MathExpert and Validator are running.

## Target 4 — Computational: largest verified automatic/hyperbolic structures for Burnside-type quotients; rung-style ladders in the literature

**Verdict: No precedent found, at any exponent.**

Zero arXiv hits for "automatic group" + "Burnside" and zero for "Knuth-Bendix" + "Burnside." This sharpens (rather than merely repeats) the 2026-07-31 scan's finding that "no formal-methods/computer-assisted work exists on Burnside-style small-cancellation arguments" — that earlier finding was framed around proof formalization (Lean/Coq/Isabelle); this scan checked the more directly relevant computational-group-theory angle (automaticity, KBMAG-style rewriting) and got the same wall.

Cross-checking against [[coulon-school-partial-periodic-quotients]]: every rung-ladder construction in that literature (`F_r = G_0 ↠ G_1 ↠ ⋯ ↠ B_r(n)`, explicit in Coulon 2018's own proof sketch) is a pure existence/induction argument. No paper in the school reports machine-verifying even a handful of rungs computationally, for any exponent — small or the "sufficiently large" ones they actually target.

**Actionability: this is the sweep's second key negative, and it reframes the computational program's novelty.** algo_mixing's `G_1..G_5` rung ladder — GAP-verified structure at each stage, `gpaxioms`-certified equality oracles, explicit `P_ℓ` piece-counting — is not a reimplementation of a published computational technique. As far as this scan can determine, **nobody has published a computer-verified instance of a Delzant-Gromov/Ivanov/Coulon-style Burnside induction at any exponent.** This is worth stating plainly to Lead: the program is not merely attacking an unusually small exponent with known machinery, it may be the first computational instantiation of this entire proof-strategy family at any scale. That raises the stakes of getting the R6/CE6/CC6-TR-v2 rung-5 gate right (per [[Agents/maumayma/MathExpert/ell6-theory-barrier-analysis-2026-08-05|ell6-theory-barrier-analysis]]) — there is no external benchmark to sanity-check against.

---

## What's settled vs. contested (this sweep only — see [[_synthesis-odd-exponent-state-2026]] for the broader odd-exponent-bound picture)

**Settled:**
- No branch of the Coulon/Gruber/rotating-families geometric-SC school states an explicit exponent constant, ever — the "does it reach exponent 5" question is inapplicable to this literature by construction, not merely unanswered.
- No post-1990 publication progresses, reformulates, or conditionally resolves Kourovka 11.48 specifically.
- No published technique (Golod–Shafarevich, cohomological/Wilson–Zelmanov, profinite) supplies a per-stage-certificate-composes-to-limit-statement mechanism applicable to B(2,5)'s bounded-exponent, element-level nontriviality question.
- No computational/automatic-group precedent exists for a rung-style Burnside induction at any exponent.

**Contested / corrected:**
- The 2026-07-31 synthesis's claim about Tent's ICM 2026 paper extending ART toward Engel-type problems is retracted; the actual paper (2606.18207) is unrelated (Cherlin–Zilber/sharply-2-transitive), correction applied in place.
- "Coulon n > 100" as recorded in the internal `LADDER.md`/Validator preruling could not be traced to an explicit statement in Coulon's own papers this scan — flagged for Validator/MathExpert to confirm the source, since this sweep found the opposite (no stated number at all) in the one paper checked at full-text depth.

## Directly applicable to algo_mixing's current targets

**Nothing found this scan supplies new machinery, a new numeric target, or a shortcut for the G₅/ℓ=6 rung.** The value of this sweep is entirely in closing doors cleanly:
- Stop looking to the published geometric-SC literature for an exponent-5-reachable constant — it structurally doesn't offer one.
- Stop looking for a published non-uniform certification shortcut (profinite/Golod–Shafarevich/cohomological) for E7's nontriviality — none exists; the internal per-rung certified-geometry program (R6-shell / CE6 / CC6-TR-v2, per [[Agents/maumayma/MathExpert/ell6-theory-barrier-analysis-2026-08-05|ell6-theory-barrier-analysis]]) is not a fallback to a "harder but known" route — it may be the only route.
- The computational ladder itself (GAP+KBMAG rung verification) has no external precedent to benchmark against or borrow tooling from.

## Open empirical/verification questions for Lead / Validator / MathExpert

- ~~Trace "Coulon n > 100" in `LADDER.md` to its actual source~~ **RESOLVED by Lead, 2026-08-07:** traced internally to `logs/math_expert_R2b.md:26`, derived from Coulon's Prop 6.1/Thm 6.9/Thm 6.15 (`n > n₁ > n₀ > 100`) — a construction-internal choice made when instantiating Coulon's existential `n₀`, not a number Coulon himself publishes as a headline constant. This is exactly consistent with this scan's finding (Coulon's own theorem statement is purely existential) — the "100" is algo_mixing's own derived instantiation, not an external citation. Validator is independently verifying the derivation against the actual paper. No correction needed to this note; recorded for the record.
- ~~If Lead wants the Tent 2606.18207 angle chased~~ **DECLINED by Lead, 2026-08-07:** too remote from the campaign bottleneck (internal certified geometry) to justify a dedicated read now. Left flagged-speculative in this note; revisit only if MathExpert sees a concrete connection.
- Still open: confirm with Validator whether the Golod–Shafarevich/General-Burnside-Problem-vs-Burnside-Problem distinction (stated here as general knowledge, not freshly sourced) is being applied correctly before it's used to justify not pursuing that route further. Not raised in Lead's ACK — carrying forward in case it becomes load-bearing.

## Disposition

Lead ACK'd 2026-08-07: synthesis accepted as standing input to the rung-5 (G₅/ℓ=6) plan. No further tasking on this sweep. Status remains `#status/draft` pending any future defense-to-validated pass; nothing in Lead's response requires a content correction.

## Stop condition invoked

Three of four sweep targets returned genuine, structural negatives rather than partial leads — stated plainly per role discipline. This is not a padding failure: a clean "no published shortcut exists" is exactly the answer Lead asked for ("confirm or refute"), and it directly supports continuing the internal per-rung program rather than diverting resources toward adapting external machinery that was never built for this exponent.

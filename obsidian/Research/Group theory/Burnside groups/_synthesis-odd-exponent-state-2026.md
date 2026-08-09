---
title: "Synthesis — Current state of the odd-exponent Burnside problem, and exponent 5 specifically (2026-07-31 literature scan)"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/b25
  - topic/odd-exponent-burnside
  - topic/small-cancellation
  - topic/power-free-words
  - topic/restricted-burnside
  - synthesis
  - status/draft
papers_synthesized:
  - "[[atkarskaya-rips-tent-2023]]"
  - "[[adian-2015-odd-bound]]"
  - "[[lysenok-2023-sample-iterated-sc]]"
  - "[[atkarskaya-kanelbelov-plotkin-rips-2021-sc-rings]]"
  - "[[gorshkov-2026-moufang-axial-algebra]]"
  - "[[obrien-vaughanlee-2002-r27]]"
  - "[[shur-2010-power-free-growth-rates]]"
  - "[[b-exponent-5-adian-4.2b]]"
  - "[[kourovka-11.48-kostrikin-1990]]"
  - "[[kourovka-2022]]"
key_concepts:
  - "[[Concepts/power-free-word-growth-rates]]"
status: draft
---

# Synthesis — Current state of the odd-exponent Burnside problem, and exponent 5 specifically

## The question

Lead Dev asked (2026-07-31, R1, high priority, feeding a live 10-hour B(2,5)-infiniteness push): what is the current, precisely-cited state of (1) the best proven odd-exponent bound for free-Burnside-group infiniteness, (2) the Atkarskaya–Rips–Tent / Kanel-Belov iterated small-cancellation program, (3) any direct exponent-5 or exponent-7 results, (4) computer-assisted/formalized approaches, (5) power-free-word growth-rate literature as the classical evidence layer, and (6) the exact Kourovka Notebook problem numbers.

**This is R1. Per instruction, no follow-up round has been started without explicit GO.**

## Sources reviewed

Odd-exponent bound record: [[adian-2015-odd-bound]], [[atkarskaya-rips-tent-2023]], [[lysenok-2023-sample-iterated-sc]]. Adjacent small-cancellation thread: [[atkarskaya-kanelbelov-plotkin-rips-2021-sc-rings]]. Direct exponent-5/7 material: [[obrien-vaughanlee-2002-r27]], [[gorshkov-2026-moufang-axial-algebra]]. Power-free words: [[shur-2010-power-free-growth-rates]] and [[Concepts/power-free-word-growth-rates]]. Kourovka framing (pre-existing vault notes, re-confirmed not superseded): [[b-exponent-5-adian-4.2b]], [[kourovka-11.48-kostrikin-1990]], [[kourovka-2022]].

**Tooling caveat that applies across almost every source below**: the research subagents used this scan had `WebSearch` denied by sandbox policy for most sub-tasks and worked via arXiv API, Crossref API, and direct `WebFetch` only. Several sources (Adian 2015's proof body, the Uspekhi Adian-legacy survey, Shur's underlying TCS/DLT papers) were confirmed to exist bibliographically but their full text was **not** independently read — this is flagged per-source below and in each paper note. Treat anything marked "relayed, not independently re-verified verbatim" accordingly.

---

## 1. Best current proven odd-exponent bound

Three numbers are in circulation, and they should **not** be collapsed into one "current record":

| Bound | Source | Status |
|---|---|---|
| odd n≥4381 | Novikov–Adian 1968 | classical, published, superseded |
| **odd n≥665** | Adian 1975/1979 book | **published, and the only one the specialist community actually cites and builds on today** |
| odd n≥557 | Atkarskaya–Rips–Tent 2023, arXiv:2303.15997 | preprint, under review at Selecta Mathematica, no independent verification located |
| odd n≥101 | Adian 2015, *Proc. Steklov Inst. Math.* 289 | **published in a real peer-reviewed journal, but functionally un-adopted** — no downstream paper (checked ~26 citing papers via OpenAlex, through 2023) builds on it; several Atabekyan et al. papers explicitly use n≥1003, a *larger* number, for their own constructions |
| odd n>2000 | Lysenok 2023, arXiv:2301.05000 | preprint, explicitly not a record attempt (accessibility-focused alternative proof) |

**Settled**: n≥665 is the safe, field-accepted bound as of this scan. **Contested/unresolved**: whether n≥557 (ART) or n≥101 (Adian 2015) actually hold — both are numerically better but neither has cleared independent verification in the literature as searched. Wikipedia's claim that Adian 2015 was "never published" is directly contradicted by primary bibliographic evidence (real DOI, real journal) and should not be repeated as fact; the correct caveat is "published but not built upon," not "unpublished."

**For the B(2,5) push specifically: none of this bears directly on n=5.** 557, 665, and 101 are all still two orders of magnitude above 5. This entire section is background/methodology context, not a lead on B(2,5) itself.

## 2. The Atkarskaya–Rips–Tent / Kanel-Belov program

Two **separate** research threads exist, sharing some authors but not others — do not conflate them:

- **Pure-group, odd-exponent thread**: Atkarskaya, Rips, Tent, "The Burnside problem for odd exponents," arXiv:2303.15997 (2023) — n≥557, iterated/graded small cancellation with a "certification sequence" as the key inductive tool. Preprint, under review. Independent contemporaneous methodological cross-check from Lysenok (2301.05000) using the same general strategy family, though not a direct replication of the 557 figure.
- **Ring-theoretic thread** (Kanel-Belov, sharing Atkarskaya and Rips but adding Plotkin, dropping Tent): "Structure of small cancellation rings," *Math. Research Reports* 2 (2021) — the 14pp version is genuinely peer-reviewed and published; a longer variant circulating online is associated (via an unverified search snippet, not directly read) with a claimed **even-exponent n≥8000** Burnside result. This is a different technique, different parity, unrelated to the 557/665/101 odd-exponent numbers above.

Community assessment of ART's proof: no MathOverflow thread, blog commentary, or explicit third-party completeness review was located this scan (MathOverflow itself was unreachable via automated fetch — absence of evidence, not confirmed absence). Downstream citations exist (Goffer–Greenfeld–Olshanskii 2024; Aubrun–Bitar 2024, *Electron. J. Combin.*; Gorshkov 2026; Amelio–André–Tent 2023) but none of the fetched abstracts contain explicit correctness commentary.

> **Correction (2026-08-07, Researcher, R2 sweep; refined 2026-08-07 after full-text open per Validator's bibliography-verification standing rule):** the claim in this paragraph that Katrin Tent "presented the method at ICM 2026 (arXiv:2606.18207) as a general template extending toward Engel-type problems" is **wrong on the specific detail and is retracted as stated**, but the paper is not simply unrelated. arXiv:2606.18207, "From the Cherlin–Zilber Conjecture via sharply 2-transitive groups to the Burnside problem" (single author, Tent), was fetched and read at full-text depth (not abstract-only). Confirmed: **zero occurrences of "Engel" anywhere in the paper** — the "Engel-type problems" claim has no textual basis at all. However, the paper **does** contain a real, substantive connection to the ART line: **Section 6.1, "Small cancellation conditions and Burnside groups,"** explicitly cites and builds on [ART] = Atkarskaya–Rips–Tent 2023 (arXiv:2303.15997) as "the most recent approach to showing the infinity of such groups for sufficiently large exponent," using it as a tool to control whether a quotient construction stays infinite when building candidate sharply-2-transitive counterexamples to Cherlin–Zilber. So: **wrong application domain (sharply-2-transitive/model-theory, not Engel), but a genuine technical use of the ART machinery, not a false citation of an unrelated paper.** See [[_synthesis-b25-attack-surface-2026-08-07]], sweep target 2, for the full verification record.

## 3. Direct exponent-5 or exponent-7 results

**Genuinely sparse, as expected, but not completely empty.** No paper was found post-2000 addressing the *free* B(m,5) for m≥3 or free B(m,7) for any m — the finiteness question for these remains exactly as open as documented in [[b-exponent-5-adian-4.2b]] and [[kourovka-11.48-kostrikin-1990]], with nothing in this scan narrowing it.

Two items worth flagging:

- [[obrien-vaughanlee-2002-r27]] — computes the *restricted* R(2,7): order 7^20416, class 28, derived length 5. Same epistemic category as Havas–Wall–Wamsley's B₀(2,5) computation: a finite restricted quotient, silent on the free group's finiteness. No extension to rank ≥3 found for exponent 7, nor to rank ≥3 for exponent 5 beyond the existing 1974 result.
- [[gorshkov-2026-moufang-axial-algebra]] (arXiv:2603.01988, Mar 2026) — a brand-new algebraic reformulation: for G = free Burnside group of odd prime exponent p **extended by an involutory automorphism**, finiteness of G is equivalent to finite-dimensionality of an axial algebra A_F(G,T,η). At p=5 specifically, the resulting algebra is "left-axial" with a **Monster-type fusion law** M(4/3,−4/3) — a structurally striking coincidence. This does **not** resolve B(2,5) finiteness and its object (G extended by an involution) is not confirmed to be the same object as B(2,5) itself — flagged as a fresh angle worth a possible closer read, not an actionable lead as-is.

No word-problem-specific result for exponent 5 or 7 (decidability/complexity) was found beyond pre-2000 background.

## 4. Computer-assisted / formalized approaches

**Confirmed absence, not insufficient search** (per the dedicated subagent's assessment): no certified/machine-checked van Kampen or small-cancellation diagram enumeration exists as a research area; no Lean/Coq/Isabelle formalization of Novikov–Adian, Ivanov–Ol'shanskii, or general small-cancellation/hyperbolic group theory was found (Lean's Mathlib has only bare `PresentedGroup` infrastructure; Isabelle/AFP has generic Knuth–Bendix-order/confluence formalizations — CoLoR, the CPF format, CeTA — but none pointed at groups); no new GAP/Magma/KBMAG paper on B(2,5) or B(2,7) beyond the already-catalogued Kuznetsov line and the 1974 Havas–Wall–Wamsley computation. This is a genuine, notable gap: **the formal-methods community has not touched Burnside-style small-cancellation arguments at all.**

## 5. Power-free word growth rates (combinatorial evidence layer)

See [[Concepts/power-free-word-growth-rates]] for the full table (source: [[shur-2010-power-free-growth-rates]], primary text independently read). Headline facts, verified:

- Over a 2-letter alphabet, β-power-free growth is polynomial for β≤7/3 and unambiguously exponential from cube-free (β=3) onward.
- **5th-power-free words over 2 letters are proven exponential**, growth-rate constant in $[1.9244437,\ 1.9646285]$.

**Important negative finding**: no paper was located that bridges this modern growth-rate machinery to Adian's actual proof apparatus (his book's rank-α "periodic and elementary words" hierarchy is a different, bespoke combinatorial object). The qualitative analogy — exponentially many aperiodic words as substrate for an infiniteness argument — holds, but there is no published technical reduction from one to the other. **Do not cite the proven exponential growth of 5th-power-free words as even partial evidence toward B(2,5) infiniteness** — that would be importing a result from an unconnected technical lineage.

## 6. Kourovka Notebook problem numbers

No change from what is already documented in the vault; re-confirmed, not superseded, by anything found this scan:

- **Problem 11.48** (Kostrikin, 1990 framing, per [[kourovka-11.48-kostrikin-1990]]): B(2,5) is infinite iff the weight-7 commutator `[[[[[[x,y],y],y],y],y],y]` is not a product of 5th powers in the free group F(x,y). Open as of Kourovka 20th edition, 2022 ([[kourovka-2022]]).
- **Problem 4.2b** (Adian, 1973 framing, per [[b-exponent-5-adian-4.2b]]): does any infinite finitely generated group of exponent 5 exist? Equivalent to 11.48 for m=2, broader for m≥3. Open.

Nothing in items 1–5 above resolves or narrows either problem.

## What's settled vs. contested

**Settled:**
- n≥665 is the field-accepted odd-exponent bound (Adian 1975).
- 5th-power-free words on 2 letters grow exponentially, with a proven numeric bracket.
- Kourovka 11.48 / 4.2b remain open exactly as previously documented.
- No formal-methods/computer-assisted work exists on Burnside-style small-cancellation arguments.
- No direct free-B(m,5)/B(m,7) result exists in the post-2000 literature for m≥3 or exponent 7.

**Contested / unresolved:**
- Whether Adian's 2015 n≥101 claim is correct (published but unverified/un-adopted).
- Whether Atkarskaya–Rips–Tent's n≥557 claim will clear peer review (currently under review, no independent verification found).
- The Kanel-Belov ring-theory n≥8000 even-exponent figure (sourced only from an unverified search snippet).
- The correct arXiv ID/authorship for a reported 2025 MFCS proof of Shur's large-alphabet growth-rate conjecture (tangential, not Burnside-relevant, but worth resolving if the growth-rate thread gets pursued further).

## Directly applicable to algo_mixing's current targets

**Nothing found this scan directly advances the B(2,5) computational push.** The closest adjacent material:

- The iterated/graded small-cancellation "certification sequence" bookkeeping concept (ART 2023) is a *possible*, unverified structural analogy worth a Developer/Lead look if there's appetite — speculative, not a lead to act on without further vetting.
- [[gorshkov-2026-moufang-axial-algebra]]'s axial-algebra reformulation (p=5, Monster-type fusion law) is mathematically fresh but its relationship to B(2,5) itself (as opposed to a "B(2,5)-extended-by-involution" object) is unconfirmed — would need a dedicated read before it's actionable.
- No new computational/GAP/KBMAG technique was surfaced beyond what's already in the Kuznetsov line and the existing Mixer pipeline.

## Open empirical questions for Experimenter / Experimenter-B25

- None of this scan's findings generate a new B(2,5) experiment directly — the literature genuinely has nothing on exponent 5 beyond what's already in the vault.
- If Lead wants the Gorshkov axial-algebra angle chased, that would need a Researcher deep-read (full paper, not abstract) before it's experiment-shaped.

## Stop condition invoked

Literature on exponent 5/7 directly is **sparse to the point of empty** beyond what's already documented — stated plainly per role discipline rather than padded. This is itself the answer to items 3 and 6 of the request: there is no secret recent exponent-5 progress to report.

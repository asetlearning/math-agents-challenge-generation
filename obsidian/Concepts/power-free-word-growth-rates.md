---
title: Growth rates of power-free words (combinatorics on words)
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/power-free-words
  - topic/burnside
  - topic/odd-exponent-burnside
  - concept
  - status/draft
introduced_in:
  - "[[shur-2010-power-free-growth-rates]]"
related_concepts:
  - "[[Concepts/growth-functions-burnside]]"
appears_in: []
---

# Growth rates of power-free words (combinatorics on words)

> **Concept hub.** Distinct from [[Concepts/growth-functions-burnside]] — that note covers growth functions of *finite group quotients* (Cayley-ball sizes $f_S(k)=|\{g\in G: d_S(e,g)=k\}|$). This note covers growth rates of *formal languages* of power-free words over a small alphabet, the classical combinatorial-evidence layer behind the Novikov–Adian free-Burnside-infiniteness argument. Do not conflate the two "growth" concepts.

## Definition

A word is **β-power-free** (β a rational ≥ 1) if it contains no factor of the form $u^t$ with $|u^t| \ge \beta|u|$ for any nonempty $u$. Over a $k$-letter alphabet, the **growth rate** of the language of β-power-free words is

$$\alpha(k,\beta) = \lim_{n\to\infty} \sqrt[n]{L_{k,\beta}(n)}$$

where $L_{k,\beta}(n)$ counts β-power-free words of length $n$. $\alpha=1$ means the language grows polynomially (effectively "small"); $\alpha>1$ means exponential growth.

## Verified numeric values (binary alphabet, k=2)

Source: A.M. Shur, "Numerical values of the growth rates of power-free languages," arXiv:1009.4415v2 (full text read directly).

| β | growth rate α(2,β) | regime |
|---|---|---|
| 7/3 | **exactly 1.0000000** | polynomial (boundary case) |
| 3 (cube-free) | 1.4575732 – 1.4575773 (est. ≈1.4575772869237) | exponential |
| 4 (4th-power-free) | 1.8211000 – 1.9208015 | exponential |
| **5 (5th-power-free)** | **1.9244437 – 1.9646285** | **exponential** |
| 6 (6th-power-free) | 1.9653118 – 1.9832942 | exponential |
| 7 (7th-power-free) | 1.9834409 – 1.9918972 | exponential |
| 8 | 1.9919310 – 1.9960151 | exponential |
| 9 | 1.9960232 – 1.9980255 | exponential, → 2 as β→∞ |

**The threshold for exponential growth on 2 letters sits strictly above β=7/3** — everything at β≤7/3 is polynomial (essentially degenerate: the ordinary binary square-free language, β=2, is classically known to be finite altogether, Thue 1906/1912), and growth is unambiguously exponential from cube-free (β=3) onward.

**5th-power-free words over 2 letters are confirmed exponential**, with the growth-rate constant proved (two-sided bound, not just an upper bound) to lie in $[1.9244437,\ 1.9646285]$.

## Methodology

Upper bounds via "regular approximation" (finite automata bounding forbidden powers by period ≤ some $m$); rigorous two-sided bounds via Shur's DLT 2009 method (extended to β≥7/2 by a strengthened argument), assembled in Shur's *Theoretical Computer Science* 411 (2010) 3209–3223 paper and the *Computer Science Review* 6 (2012) 187–208 survey (both bibliographically confirmed, not independently re-read this scan — see [[_synthesis-odd-exponent-state-2026]] for full citation list and status).

## Relationship to the Burnside problem — an OPEN gap in the literature

Adian's *The Burnside Problem and Identities in Groups* (1979, Ch. 2 "Periodic and Elementary Words of Rank α," pp. 27–103) builds its combinatorial substrate around a **bespoke hierarchy of "periodic and elementary words of rank α"** — a rank-graded apparatus tailored to Adian's specific induction, NOT literally the modern Shur/Kolpakov "k-power-free over a fixed small alphabet" object.

**No paper was found in this scan that explicitly draws an equivalence or reduction between the two technical lineages** (modern power-free-language growth-rate computation vs. Adian's rank-α apparatus). Both Wikipedia's "Burnside problem" article and the Encyclopedia of Mathematics were checked directly and contain no such discussion. This appears to be a genuine gap — the two research threads share only the qualitative motivation ("aperiodic/power-free words as combinatorial substrate for proving a free group is infinite") without a literal technical bridge in the published literature as found.

**Caution for algo_mixing:** do not assume that "5th-power-free words over 2 letters grow exponentially" (which IS proven, per the table above) constitutes evidence, partial or otherwise, toward B(2,5) being infinite. It is evidence of the same *qualitative flavor* that powers the Novikov–Adian argument for large odd n, but Adian's actual construction uses a different (rank-α) combinatorial object, and no one has published a bridge showing the modern power-free-language result substitutes for it. Treat this as a research idea to flag, not a result to cite as support.

## Related work

- Kolpakov (2007, *J. Appl. Ind. Math.* 1(4) 453–462) — counting repetition-free words, a related but distinct invariant from the growth-rate constant.
- Kolpakov, Kucherov, Tarannikov (1999, *TCS* 218, 161–175) — minimal density of repetition-free (cube-free) binary words, again a related-but-distinct invariant (density of "irregular positions," not the growth-rate constant itself).
- Shur's large-alphabet conjecture on the asymptotic behavior of $\alpha(k,\beta)$ as $k\to\infty$: open as of Rosenfeld 2021 (*Theory of Computing Systems* 65(7), 1110–1116, lower-bound partial progress); a 2025 MFCS paper title ("A Proof of Shur's Conjecture on the Growth of Power-Free Languages over Large Alphabets") was found via a DBLP-style listing but its exact authors/arXiv ID were **not** pinned down this scan — flag as unconfirmed, needs a dedicated follow-up before citing.

## Open questions

- Does a technical bridge between power-free-language growth rates and Adian's rank-α apparatus exist anywhere in the (possibly non-English, possibly older) literature that this scan's tooling (WebSearch denied in the research subagent's sandbox this session; arXiv/Crossref API + direct WebFetch only) simply didn't surface? Worth a manual follow-up with full search access if Lead wants this resolved.
- Confirm authorship/arXiv ID of the 2025 MFCS Shur-conjecture proof paper.

---
title: "The Coulon/rotating-families school of partial periodic quotients — landscape note"
authors: "Rémi Coulon; Coulon-Sela; Coulon-Steenbock; Gruber-Mackay; Minasyan-Olshanskii-Sonkin"
year: 2008-2021
venue: "arXiv (multiple papers)"
url: ""
language: en
domain: group-theory
status: draft
methodology_type: theoretical
citation_count: null
citation_count_date: 2026-08-07
key_concepts: []
extends:
  - "[[coulon-2018-even-exponents]]"
contradicts: []
replicates: []
cites: []
cited_by:
  - "[[_synthesis-b25-attack-surface-2026-08-07]]"
quality_notes: "Comparative/landscape note covering 5 papers by abstract only (arXiv API metadata, not full-text-fetched except where noted) — used to map the shape of a research program, not to extract a specific theorem for citation. Individual claims below are abstract-only unless flagged verbatim."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/b25
  - topic/small-cancellation
  - topic/uniformity
  - comparative-analysis
  - status/draft
project: b25
---

# The Coulon/rotating-families school of partial periodic quotients

Landscape note, not a single-paper summary — written to answer Lead's sweep-target-1/4 question: does *any* branch of this program reach exponent 5, or supply a numeric constant checkable against it, or a computational ladder precedent?

## Papers mapped

| Paper | arXiv | Year | What it does | Numeric exponent given? |
|---|---|---|---|---|
| Coulon, "Small cancellation theory and Burnside problem" | 1302.6933 | 2013 | Expository notes on Delzant–Gromov's geometric approach | No — expository, no number found in extracted text |
| Coulon, "Partial periodic quotient of groups acting on a hyperbolic space" | 1311.0855 | 2013 | Constructs partial-`n`-periodic quotients for any non-elementary acylindrical action; application to mapping class groups (fixed power of every pseudo-Anosov identified with periodic/reducible element) | Abstract only checked — "arbitrarily large" framing consistent with [[coulon-2018-even-exponents]] |
| Coulon, "Growth of periodic quotients of hyperbolic groups" | 1211.4271 | 2012 | Shows growth rate of `G/G^n` (odd `n`) tends to growth rate of `G` as `n→∞`; gives a convergence-rate *estimate* | Asymptotic-in-`n` result, not a threshold; not exponent-5-relevant by construction |
| Coulon, "A criterion for detecting trivial elements of Burnside groups" | 1211.4267 | 2012 | Necessary+sufficient condition to decide whether a free-group element is trivial in `B(m,n)` for "sufficiently large odd exponent," stated independent of the infiniteness proof itself | No number in abstract |
| Coulon–Sela, "Equations in Burnside groups" | 2112.07409 | 2021 | Studies structure of periodic quotients of hyperbolic groups: Hopf/co-Hopf property, isomorphism problem, free splittings, automorphism group | Abstract only; presupposes the same "sufficiently large" regime |
| Coulon–Steenbock, "Product set growth in Burnside groups" | 2102.10885 | 2021 | Lower bound on growth of sub-semigroups of a periodic quotient of a torsion-free hyperbolic group, generalizing Razborov–Safin | Abstract only |
| Gruber–Mackay, "Random triangular Burnside groups" | 1810.01805 | 2018 | Random-group model: `n`-periodic quotients of triangular random groups at density `d ∈ (1/3, d_crit)` are infinite for `n` "large enough"; produces groups with fixed points on all `L^p` isometric actions | "For every fixed large enough `n`" — explicitly unquantified in the abstract |
| Minasyan–Olshanskii–Sonkin, "Periodic quotients of hyperbolic and large groups" | 0804.3328 | 2008 | Four constructions of continuous families of periodic quotients of a hyperbolic or large group; explicitly answers **a question of Wiegold from the Kourovka Notebook** | Abstract only; the specific problem number is not given in the fetched abstract and was not independently confirmed as 11.48 or a different Wiegold entry this scan |

## Finding for sweep target 1 (Coulon/Gruber exact constants)

**Confirmed pattern across the entire school: nobody in this line states an explicit numeric exponent threshold anywhere in an abstract, and the one paper independently full-text-checked ([[coulon-2018-even-exponents]]) confirms this holds in the actual theorem statement too, not just the abstract.** Every paper uses "sufficiently large," "for `n` large enough," or an asymptotic-in-`n` statement. This is a structurally different posture from the Adian/ART/Lysenok combinatorial line, which always states a number (665/557/2000/101) even when unverified. **There is therefore no exact constant from the Coulon/Gruber/rotating-families school to check against exponent 5 — the question "does this reach exponent 5" is not just answered no, it is not a question this literature poses at all.** Recommend closing sweep target 1 as **negative, structurally** (not merely "not yet reached") for this whole branch. The only branch that states numbers remains the one already covered in [[_synthesis-odd-exponent-state-2026]] (n≥557/665/2000/101), all still ~100-400× larger than 5.

## Finding for sweep target 4 (computational ladders)

**None of these seven papers report a computational/machine-verified instance of the induction.** Every construction — including the explicit rung-ladder shape `F_r = G_0 ↠ G_1 ↠ ⋯ ↠ B_r(n)` in [[coulon-2018-even-exponents]] — is a pure existence/induction proof in the literature; no GAP/Magma/KBMAG verification of even a few rungs was found for any exponent, small or large. Combined with the already-documented absence of Lean/Coq/Isabelle formalization of any Burnside-type small-cancellation argument ([[_synthesis-odd-exponent-state-2026]], item 4), the conclusion strengthens: **algo_mixing's rung-by-rung `G_1..G_5` GAP+KBMAG-verified ladder appears to have no precedent in the published literature, in either the classical or geometric school.** This is worth stating plainly to Lead as a novelty/no-blueprint-exists finding, not just a gap.

## Kourovka thread worth flagging (sweep target 2, tangential)

Minasyan–Olshanskii–Sonkin (2008) is the one item in this whole sweep that explicitly connects a rotating-families/periodic-quotient construction to a **named Kourovka Notebook problem** (attributed to Wiegold, not Kostrikin). This confirms the general technique family *has* been used to close Kourovka-listed questions before — just not 11.48, and not (as far as this scan found) any exponent-5 question. Flagged for completeness; not independently verified which Kourovka number this is, and it is very unlikely to be 11.48 given the "large exponent" framing throughout the source's own school.

## Related material in vault

- Extends: [[coulon-2018-even-exponents]]
- Cited by: [[_synthesis-b25-attack-surface-2026-08-07]]

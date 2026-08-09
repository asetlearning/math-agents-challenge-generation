---
title: "The Burnside problem for odd exponents"
authors: "Agatha Atkarskaya, Eliyahu Rips, Katrin Tent"
year: 2023
venue: "arXiv preprint (under review, Selecta Mathematica)"
url: "https://arxiv.org/abs/2303.15997"
language: en
domain: group-theory
status: draft
methodology_type: theoretical
citation_count: null
citation_count_date: 2026-07-31
key_concepts:
  - "[[Concepts/power-free-word-growth-rates]]"
extends: []
contradicts: []
replicates: []
cites:
  - "[[b-exponent-5-adian-4.2b]]"
cited_by: []
quality_notes: "arXiv v1–v5 (28 Mar 2023 → 28 Mar 2024), self-reported by lead author's CV as 'under review in Selecta Mathematica' as of this scan (2026-07-31). No journal-ref on arXiv. No independent third-party review (MathOverflow thread, blog post, or published referee report) located in this scan — absence of evidence, not confirmed absence, since MathOverflow was unreachable via automated fetch this session. Downstream citations exist (Goffer–Greenfeld–Olshanskii 2024, Aubrun–Bitar 2024, Gorshkov 2026, Amelio–André–Tent 2023) but none of the fetched abstracts contain explicit completeness commentary."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/odd-exponent-burnside
  - topic/small-cancellation
  - topic/word-problem
  - paper
  - status/draft
project: null
---

# The Burnside problem for odd exponents

## Abstract

> Not independently re-fetched verbatim this scan (paywall/PDF-extraction limits on the subagent); reported here as paraphrase pending direct verification — flag before treating as a verbatim quote.

## TL;DR

Claims free Burnside groups B(m,n) are infinite for all m≥2 and all odd n≥557, via a new "iterated/graded small cancellation" technique with a central tool the authors call a "certification sequence." This is a smaller (better) bound than Adian's long-standing published n≥665 (1975/1979) — if it holds up, it would be the new record for a fully-proved odd-exponent threshold. As of this scan it is preprint-only, under review at Selecta Mathematica, with no confirmed independent verification located.

## Problem

Determine the smallest odd exponent n for which the free Burnside group B(m,n) (m≥2 generators) is provably infinite. The long-standing record was Adian's n≥665 (1975 book, refining Novikov–Adian 1968's n≥4381).

## Approach

Iterated (graded) small cancellation theory: the group is built through a hierarchy of small-cancellation presentations, with the key inductive tool being a "certification sequence" that lets the small-cancellation condition be verified at each nesting depth. This is the same general strategy (induction on nesting depth of relators) later echoed in Lysenok's independent companion approach ([[lysenok-2023-sample-iterated-sc]]).

## Key result

> "free Burnside groups B(m,n) are infinite for m≥2 and odd n≥557, the best currently known lower bound for the exponent" — arXiv:2303.15997 abstract (as relayed by the research subagent; not independently re-fetched verbatim this scan, verify before quoting in a proof-facing document).

58 pages, MSC 20F05/20F06/20F65.

## Assumptions

- Standard combinatorial/geometric group theory assumptions for small-cancellation arguments (presentation complexes, van Kampen diagrams, curvature/angle conditions at the graded level).
- Not yet independently verified by peer review as of this scan.

## Limitations / scope

- n=557 is far above n=5 or n=7 — **does not bear directly on B(2,5) finiteness** (Kourovka 11.48). Relevant to algo_mixing only as a possible source of *technique* (iterated small cancellation, certification-sequence bookkeeping), not as a direct result.
- Preprint status: treat any number derived from this paper as provisional until the Selecta Mathematica review completes or an independent verification appears.

## Replication evidence

`partial` — Lysenok's independent, contemporaneous 2023 preprint ([[lysenok-2023-sample-iterated-sc]]) pursues the same general iterated-small-cancellation strategy (with a much more conservative n>2000 bound, explicitly framed as an "accessible" alternative proof) as a positive methodological signal, but is not a direct replication of the n≥557 claim and does not cite or confirm it.

## Why this paper matters

If verified, this would be the first improvement on Adian's 47-year-old n≥665 bound to gain any real community traction (contrast with Adian's own 2015 n≥101 claim, [[adian-2015-odd-bound]], which the community has not built upon in 8+ years). It also signals a live, active research program (Atkarskaya, Rips, Tent, and the adjacent Kanel-Belov ring-theory thread, [[atkarskaya-kanelbelov-plotkin-rips-2021-sc-rings]]) applying iterated small cancellation to Burnside-type problems generally — Tent has since presented it as a template method at ICM 2026 for other Burnside-type problems (Engel groups). For algo_mixing, the "certification sequence" bookkeeping concept may be worth a closer read as a possible structural analogy to rule-injection bookkeeping in the KB mixing pipeline, but this is speculative and unverified — flag to Lead/Developer as a maybe, not a lead.

## Quotes

1. > "free Burnside groups B(m,n) are infinite for m≥2 and odd n≥557" — Abstract (relayed, not independently re-fetched verbatim — verify before quoting further).

## Open questions surfaced

- Does the "certification sequence" technique generalize below n=557, e.g. toward n=5 or n=7? No evidence found either way; the authors have not made this claim.
- Peer-review outcome at Selecta Mathematica — unresolved as of this scan.
- Is there any MathOverflow, Zulip, or blog discussion assessing correctness? Not found via automated fetch this session (MathOverflow itself was unreachable); a manual browser check would be a useful follow-up if Lead wants higher confidence before citing this as "the current record."

## Related material in vault

- Extends: (none)
- Contradicts: (none)
- Replicates: (none)
- Concepts introduced/used: [[Concepts/power-free-word-growth-rates]] (adjacent combinatorial-evidence tradition, not used directly by this paper)
- Cites: [[b-exponent-5-adian-4.2b]] (same open-problem family, no direct citation relationship confirmed)
- Cited by (in vault): [[_synthesis-odd-exponent-state-2026]]

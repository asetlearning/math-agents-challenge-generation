---
title: "A sample iterated small cancellation theory for groups of Burnside type"
authors: "Igor G. Lysenok"
year: 2023
venue: "arXiv preprint (no journal-ref found)"
url: "https://arxiv.org/abs/2301.05000"
language: en
domain: group-theory
status: draft
methodology_type: theoretical
citation_count: null
citation_count_date: 2026-07-31
key_concepts: []
extends: []
contradicts: []
replicates: []
cites: []
cited_by:
  - "[[atkarskaya-rips-tent-2023]]"
quality_notes: "Preprint only, v1 (12 Jan 2023), 97pp, 41 figures, no later version found. Author is a leading pre-existing Burnside-problem expert (co-author of the Ivanov–Lysenok even-exponent solution), which lends weight even absent journal publication. Submitted ~2.5 months before Atkarskaya–Rips–Tent's arXiv:2303.15997 — independent, contemporaneous, NOT a response to it (the abstract predates ART's paper and does not mention it). A citation-graph tool reported this paper as citing 2303.15997, which is chronologically impossible against the only arXiv version on record — flagged as an unresolved discrepancy, likely a mis-linked citation-graph entry; do not treat as confirmed cross-citation."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/odd-exponent-burnside
  - topic/small-cancellation
  - paper
  - status/draft
project: null
---

# A sample iterated small cancellation theory for groups of Burnside type

## Abstract

> We develop yet another technique to present the free Burnside group B(m,n) of odd exponent n with m≥2 generators as a group satisfying a certain iterated small cancellation condition. Using the approach, we provide a reasonably accessible proof that B(m,n) is infinite with a moderate bound n > 2000 on the odd exponent n. [Verbatim per subagent fetch of the arXiv abstract page.]

## TL;DR

An independent (Lysenok, not the Atkarskaya–Rips–Tent group), contemporaneous 2023 reworking of the iterated-small-cancellation strategy for the odd-exponent Burnside problem, explicitly framed as a more *transparent/accessible* proof rather than a bound-optimization attempt. Its threshold (n>2000) is deliberately much weaker than the existing record (n≥665, Adian 1975) — the point of the paper is pedagogical/methodological clarity, not a new record.

## Problem

Give an accessible, better-organized proof that B(m,n) is infinite for odd n above some threshold, using iterated small cancellation theory as the unifying technique, rather than chasing the smallest possible n.

## Approach

"Iterated small cancellation condition" — same general strategic family as Atkarskaya–Rips–Tent's certification-sequence approach ([[atkarskaya-rips-tent-2023]]): builds the group through a graded hierarchy of small-cancellation presentations. 97 pages, 41 figures — figure-heavy, consistent with a diagram-based small-cancellation argument aimed at readability.

## Key result

> "a reasonably accessible proof that B(m,n) is infinite with a moderate bound n > 2000 on the odd exponent n" — Abstract.

Explicitly NOT a record attempt: n>2000 is worse than both Adian's 665 (1975) and the disputed 101 (Adian 2015, [[adian-2015-odd-bound]]).

## Assumptions

Standard geometric small-cancellation assumptions (unread in detail — full proof body not fetched this scan beyond the abstract).

## Limitations / scope

- Not competitive on the bound; value is methodological (a second, independent expert's take on making iterated small cancellation tractable/teachable for Burnside-type groups).
- n>2000 is far above n=5/n=7 — no direct bearing on B(2,5)/Kourovka 11.48.
- Preprint only as of this scan; no journal-ref found.

## Replication evidence

`partial` — best read as an independent methodological cross-check that the general "iterated small cancellation" strategy is workable and being pursued by more than one specialist around the same time (early-to-mid 2023), which is a positive signal for the soundness of the broader technique family, though it does not verify Atkarskaya–Rips–Tent's specific n≥557 claim.

## Why this paper matters

Signals that iterated/graded small cancellation is currently the live methodological frontier for the odd-exponent Burnside problem, pursued independently by at least two expert groups in the same few months of 2023. For algo_mixing, this is useful context for why "small cancellation" surfaces repeatedly in any current literature scan of this area — it is genuinely the active research direction, not a dead end.

## Quotes

1. > "a certain iterated small cancellation condition" — Abstract.
2. > "a moderate bound n > 2000" — Abstract.

## Open questions surfaced

- Has this paper been submitted to or accepted by a journal since Jan 2023? Not found this scan.
- Does Lysenok's construction share enough structure with Atkarskaya–Rips–Tent's "certification sequence" that the two could cross-verify each other? Not assessed — would require a close technical read of both papers' proof bodies.

## Related material in vault

- Extends: (none)
- Contradicts: (none)
- Replicates: (none)
- Concepts introduced/used: (none)
- Cites: (none confirmed)
- Cited by (in vault): [[_synthesis-odd-exponent-state-2026]]; possibly [[atkarskaya-rips-tent-2023]] per an unresolved citation-graph signal — not confirmed, see quality_notes.

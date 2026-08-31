---
title: "The 2-Generator Restricted Burnside Group of Exponent 7"
authors: "E.A. O'Brien, M. Vaughan-Lee"
year: 2002
venue: "International Journal of Algebra and Computation, 12(4)"
url: ""
language: en
domain: group-theory
status: draft
methodology_type: empirical
citation_count: null
citation_count_date: 2026-07-31
key_concepts: []
extends: []
contradicts: []
replicates: []
cites: []
cited_by: []
quality_notes: "Published, peer-reviewed. Not independently re-fetched in full this scan — result numbers relayed by research subagent via Crossref/bibliographic metadata, not read from the primary text directly; treat the exact numbers as high-confidence (standard, oft-cited computational-group-theory result) but not scan-verified against the PDF."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/restricted-burnside
  - topic/finite-group-enumeration
  - paper
  - status/draft
project: null
---

# The 2-Generator Restricted Burnside Group of Exponent 7

## Abstract

Not independently re-fetched verbatim this scan.

## TL;DR

Computes R(2,7), the restricted (largest finite quotient) 2-generator Burnside group of exponent 7, via a power-commutator presentation: order 7^20416, nilpotency class 28, derived length 5. This settles the RESTRICTED problem for (2,7) computationally — it says nothing about the free group B(2,7)'s finiteness, which (like B(m,5) for m≥3, B(m,7) generally) remains open.

## Problem

Determine the structure (order, class, derived length) of the restricted Burnside group R(2,7) — the largest finite group among all 2-generator groups of exponent 7, guaranteed to exist by Zelmanov's positive solution of the restricted Burnside problem.

## Approach

Power-commutator presentation computation (standard computational-group-theory machinery for restricted Burnside groups, in the tradition of the Hall–Higman / Havas–Newman line — cf. [[havas-newman-1980]]).

## Key result

> R(2,7) has order 7^20416, nilpotency class 28, derived length 5. [Relayed via Crossref/bibliographic metadata by research subagent — verify against primary text before quoting as verbatim theorem statement.]

## Assumptions

Standard restricted-Burnside-group computational assumptions (finite presentation, Lie-ring-method or direct power-commutator methods per era-standard practice — not independently confirmed which method this specific paper used).

## Limitations / scope

- Restricted group only. Does **not** address B(2,7) (free group) finiteness — that remains fully open, same epistemic status as B(m,5) for m≥3.
- No extension to R(3,7) or higher rank found in this literature pass — the exponent-7 restricted computation appears to stop at rank 2 in the literature as scanned.

## Replication evidence

Not assessed this scan.

## Why this paper matters

The closest thing found in this scan to a "direct exponent-7 result" — but it is squarely a restricted-group computation, structurally identical in spirit to Havas–Wall–Wamsley 1974's |B₀(2,5)|=5^34 computation ([[havas-wall-wamsley-1974]]), and carries the exact same caveat: a finite restricted quotient says nothing about the free group's finiteness. Useful as a scale comparison — R(2,7) at 7^20416 is vastly larger than B₀(2,5) at 5^34, illustrating how fast restricted-Burnside group orders grow with exponent even when rank is fixed at 2.

## Quotes

1. > "order 7^20416, nilpotency class 28, derived length 5" — relayed via bibliographic metadata, not independently re-verified verbatim this scan.

## Open questions surfaced

- Has anyone attempted R(3,7) or higher rank since 2002? Not found in this scan (genuinely searched, genuinely empty).
- Does the free B(2,7) finiteness question have any recorded partial progress anywhere? Also genuinely empty in this scan.

## Related material in vault

- Extends: (none)
- Contradicts: (none)
- Replicates: (none)
- Concepts introduced/used: (restricted-Burnside topic, see [[havas-wall-wamsley-1974]] for the B(2,5) analogue)
- Cites: (none confirmed)
- Cited by (in vault): [[_synthesis-odd-exponent-state-2026]]
- MOC: [[_moc-burnside]]

---
title: "Infinite periodic groups of even exponents"
authors: "Rémi Coulon"
year: 2018
venue: "arXiv preprint"
url: "https://arxiv.org/abs/1810.08372"
language: en
domain: group-theory
status: draft
methodology_type: theoretical
citation_count: null
citation_count_date: 2026-08-07
key_concepts: []
extends:
  - "[[atkarskaya-rips-tent-2023]]"
contradicts: []
replicates: []
cites: []
cited_by:
  - "[[_synthesis-b25-attack-surface-2026-08-07]]"
quality_notes: "Full PDF fetched and text-extracted directly this scan (custom zlib/Tj extractor, no OCR needed — PDF has embedded text). Theorem 1.1 quoted verbatim from extracted text, not relayed."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/b25
  - topic/small-cancellation
  - topic/uniformity
  - paper
  - status/draft
project: b25
---

# Infinite periodic groups of even exponents

## Abstract

> "We give a new proof that free Burnside groups of sufficiently large even exponents are infinite. The method is very flexible and can also be used to study (partially) periodic quotients of any group which admits an action on a hyperbolic space satisfying a weak form of acylindricity."

## TL;DR

Geometric (Delzant–Gromov-style) small-cancellation proof of even-exponent Burnside infiniteness, generalized to acylindrical actions on hyperbolic spaces. **The main theorem is stated with a purely existential threshold — no explicit numeric constant is given anywhere in the theorem statement**, unlike the classical Adian/ART combinatorial line (665/557/2000/101). This is the key finding for the algo_mixing sweep: the modern geometric-SC school does not commit to explicit exponent constants at all, so there is no number to check against exponent 5.

## Problem

Prove free Burnside groups of even exponent are infinite (odd case was Delzant–Gromov's territory, "their work only applies to odd exponents" per this paper's own introduction), using geometric small cancellation instead of Ivanov's/Lysenok's combinatorial approach.

## Mechanism (verbatim, from extracted PDF text, Theorem 1.1)

> "Theorem 1.1. Let r > 2. There exists a critical exponent n₀ ∈ ℕ such that for every integer n > n₀, the free Burnside group Bᵣ(n) is infinite."

No value of `n₀` is given — not in the theorem, not as a numeric remark in the introduction (checked; the only large numbers in the intro are page-count comparisons: "substantially shorter than the one of Lysenok and Ivanov (200 and 300 pages respectively)"). The construction is a direct-limit induction `F_r = G_0 ↠ G_1 ↠ G_2 ↠ ⋯ ↠ B_r(n)`, at each step `G_{k+1}` obtained from `G_k` by adding relations `h^n=1` for all "small" loxodromic `h` — i.e. the same rung-ladder shape algo_mixing's internal G_1..G_5 program uses, but with the small-cancellation parameter λ left as an abstract sufficiently-small constant, never pinned to a number reachable by hand.

General framework (Theorem 5.7, referenced, not the exponent-existence theorem): for any group `G` acting acylindrically on a hyperbolic space `X`, for **arbitrarily large** exponents `n`, one gets a partially-`n`-periodic quotient. "Arbitrarily large," not "any `n≥5`."

## Assumptions

- Acylindrical (weakly acylindrical) action on a hyperbolic space — satisfied by free groups on their Cayley graph, mapping class groups on curve graphs, etc.
- The small-cancellation parameter must be small enough relative to the injectivity radius / acylindricity constants of the action — this is exactly the "cone radius ≫ injectivity radius" obstruction already on record in the vault's DGO assessment ([[2026-08-05-b25-ell6-theory-preruling]] cites this for AGM/DGO).

## Limitations / scope

- Existential, not explicit. Cannot be checked against `n=5` because no number is asserted.
- Restricted to "sufficiently large" — the paper explicitly frames its contribution as generality (any acylindrical action) and proof length (shorter than Ivanov/Lysenok), not as improving or specifying the constant.
- No statement anywhere in the abstract/introduction about odd exponent 5, 6-Engel elements, or any rung-by-rung finite verification.

## Why this paper matters for the sweep

This is the cleanest confirmation available that **the entire geometric-small-cancellation-for-Burnside literature (Coulon 2012–2021, following Delzant–Gromov) treats "large enough" as an existence claim, never an explicit reachable bound.** Only the older combinatorial Adian/Ivanov/Lysenok/ART line states numbers, and those numbers (101–2000) are already two orders of magnitude above 5, as documented in [[_synthesis-odd-exponent-state-2026]]. There is no published constant anywhere — geometric or combinatorial — that a fixed-exponent-5 verification could be checked against; the geometric school does not even attempt to supply one.

## Related material in vault

- Extends: [[atkarskaya-rips-tent-2023]] (parallel combinatorial-record thread; this paper is the geometric-school counterpart, no numeric constant to compare)
- Cited by: [[_synthesis-b25-attack-surface-2026-08-07]]

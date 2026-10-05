---
title: "A criterion for detecting trivial elements of Burnside groups"
authors:
  - "Rémi Coulon"
year: 2018
venue: "Bull. Soc. Math. France (2018), doi:10.24033/bsmf.2772; arXiv:1211.4267 [math.GR] (v1 Nov 2012, v2 20 Apr 2013, 48 pp.)"
url: "https://arxiv.org/abs/1211.4267"
url_translated:
language: en
domain: group-theory
status: draft
methodology_type: theoretical
citation_count: 5
citation_count_date: 2026-10-05
key_concepts: []
extends: []
contradicts: []
replicates: []
cites: []
cited_by:
  - "[[coulon-school-partial-periodic-quotients]]"
quality_notes: "Full arXiv v2 PDF read (intro, §4 parameter choice and Theorem 4.5). Citation count from Semantic Scholar (which lists the arXiv record; DOI 10.24033/bsmf.2772 identifies the Bull. SMF publication — volume/pages not verified here). The exponent threshold n₀ is not computed in the paper; §4.1 only requires n ≥ max{100, n₀, 2ε+1} with n₀ chosen 'large enough' (λ_{n₀}⁻¹ ≥ 500 among unspecified inequalities). The paper is bilingual (English body, French résumé); vault text is the English abstract."
author: asetlearning
tags:
  - agent/research
  - user/asetlearning
  - domain/group-theory
  - topic/burnside
  - topic/burnside-groups
  - topic/trivial-words
  - topic/word-problem
  - topic/proof-certificates
  - project/challenge-gen
  - paper
  - status/draft
project: challenge-gen
---

# A criterion for detecting trivial elements of Burnside groups

## Abstract

> "In this article we give a sufficient and necessary condition to determine whether or not an element of the free group induces a non-trivial element of the free Burnside group of sufficiently large odd exponent. This criterion can be stated without any knowledge about Burnside groups, in particular about the proof of its infiniteness. Therefore it provides a useful tool that we will use later to study outer automorphisms of Burnside groups. We also state an analogue result for periodic quotients of torsion-free hyperbolic groups."

(Text of arXiv v2; the v1 abstract page reads "wether". The paper's French résumé is omitted per vault language policy.)

## TL;DR

For **sufficiently large odd exponents n** (with a threshold n₀ that the paper does not compute, and in any case n ≥ 100), a reduced word w is trivial in B_r(n) if and only if some finite sequence of "(ξ, n)-elementary moves" sends w to the empty word. Each move replaces a reduced subword pu^m s, with m > n/2 − ξ, by the reduced form of pu^{m−n}s. Triviality therefore has a purely free-group certificate, a sequence of such moves. The result is proved in the Delzant–Gromov iterated small-cancellation framework and generalised to periodic quotients G/Gⁿ of torsion-free hyperbolic groups. **It says nothing about B(2,5).**

## Problem

Novikov–Adian's key lemma gives only a *sufficient* condition for non-triviality: if w contains no subword u^p, then w is non-trivial in B_r(n) for odd n > 10000p (intro, citing [2, Statement 1]). That is not enough to decide whether elements such as the iterates ψ^k(d) of an automorphism are distinct, because they contain arbitrarily large powers (intro, Cherepanov-type examples). Coulon wants a *necessary and sufficient* combinatorial criterion for triviality, stated without the machinery of the infiniteness proof, as a tool for studying Out(B_r(n)).

## Approach

The approach follows Delzant–Gromov: B_r(n) is the direct limit of hyperbolic groups F_r ↠ G₁ ↠ G₂ ↠ …, where G_{k+1} is a small-cancellation quotient of G_k by n-th powers (intro, §4.1). For a word trivial in G₁, the Greendlinger lemma gives a subword u^m with m ≥ 3n/4, and an elementary move shortens it. At higher ranks the earlier relations "mess up the powers", so large powers may not be visible in the free word. The proof shows, by induction on k (Proposition 4.6), that elementary moves can always rearrange the word until the needed power becomes visible. §1–3 develop the hyperbolic-geometry, cone-off and small-cancellation tools (lifting figures from Ḡ to G); §4 runs the induction. The author notes that Ol'shanskiĭ's Lemma 5.5 [22] gives the result for m ≥ n/3 and could be adapted to the full range.

## Key result

- **Main theorem (free Burnside groups; intro).** "There exist numbers ξ and n₀ such that for all odd integers n ⩾ n₀ we have the following property. Let w be a reduced word of F_r. The element of B_r(n) defined by w is trivial if and only if there exists a finite sequence of (ξ, n)-elementary moves that sends w to the empty word."
  - **(ξ, n)-elementary move (intro).** "replacing a reduced word of the form pu^m s ∈ F_r by the reduced representative of pu^{m−n} s, provided m is an integer larger than n/2 − ξ. Note that an elementary move may increase the length of the word."
- **Hyperbolic-group version (intro).** For G non-elementary and torsion-free, acting freely, properly and co-compactly on a proper hyperbolic geodesic pointed space (X, x₀), there exist ξ and n₀ such that for all odd n ≥ n₀, "Two elements g and g′ of G induce the same element of G/Gⁿ if and only if there are two finite sequences of (ξ, n)-elementary moves that respectively send gx₀ and g′x₀ to the same point." Here a move sends y to v⁻ⁿy when |[x₀, y] ∩ Y_v| ≥ [v^m] with m ≥ n/2 − ξ.
- **Theorem 4.5 (§4.3).** "An element g ∈ G belongs to Gⁿ if and only if there exist two sequences of elementary moves which respectively send y and gy to the same point." The two main theorems follow from it.
- **Exponent range (§4.1).** The integer n₀ "is chosen large enough in such a way that λ_{n₀} satisfy a set of inequalities", where λ_n is a rescaling parameter that decreases in n, and additionally λ_{n₀}⁻¹ ⩾ 500. The exponent must be "an odd integer n ⩾ max{100, n₀, 2ε + 1}" (plus one further inequality). ξ is then fixed by an inequality in r₀, δ₁ and n₀. **No numerical value of n₀ or ξ is given.** Footnote 1: "the exact statement of the inequalities it should satisfy is not important".

## Assumptions

- The exponent n is **odd** and **sufficiently large**, above an inexplicit threshold n₀ inherited from the Delzant–Gromov / Coulon small-cancellation constants, and in any case ≥ 100.
- For the generalisation: G is torsion-free and non-elementary, acting freely, properly and co-compactly on a proper geodesic hyperbolic space.

## Limitations / scope

- **No content for B(2,5).** The criterion is proved only for odd n ≥ n₀, and n₀ is not computed. Comparable explicit thresholds in the iterated small-cancellation literature run from n ≥ 101 to n ≥ 665 (see [[_synthesis-odd-exponent-state-2026]]). Exponent 5 is far outside every such range. B(2,5) is not even known to be infinite (Kourovka 11.48), and its restricted quotient B₀(2,5) of order 5³⁴ is finite (see [[havas-wall-wamsley-1974]]). Reading the theorem with n = 5, i.e. replacing u^m by u^{m−5} for m > 5/2 − ξ, has **no theorem behind it**. Whether such moves suffice to reduce every trivial word of B(2,5) is unknown, and nothing in this paper bears on that question.
- **Not an efficient decision procedure.** Moves "may increase the length of the word", and the paper bounds neither the number of moves nor intermediate lengths. The criterion characterises triviality by the *existence* of a certificate; it does not give a terminating length-decreasing reduction.
- Even exponents are not covered. Coulon's later even-exponent work is in [[coulon-2018-even-exponents]].

## Replication evidence

No independent replication is needed for a published proof, and none is reported. The author records that Ol'shanskiĭ pointed out an alternative route via Lemma 5.5 of *The Novikov–Adyan theorem* (for m ≥ n/3, adaptable to m ≥ n/2 − ξ), which gives partial independent support for the statement. The application to automorphisms appears in Coulon–Hilion [10].

## Why this paper matters

The paper turns the inner machinery of the Novikov–Adian / Ol'shanskiĭ / Delzant–Gromov proofs into a black-box combinatorial statement about free words. For large odd exponents, triviality in B_r(n) is *exactly* reachability of the empty word under "delete-most-of-an-n-th-power" moves, which are just conjugate applications of the relators uⁿ under a size threshold. That lets later work (Out(B_r(n)), growth of periodic quotients; see [[coulon-school-partial-periodic-quotients]]) use triviality arguments without re-entering the small-cancellation induction.

**Relevance to challenge-gen:** For phase 1 (B(2,5)) this paper provides **no usable criterion**, because it applies only to large odd exponents with an unspecified threshold. Its value is conceptual. It shows that in the regime where theory works, a triviality certificate can be a plain free-group sequence of "remove (most of) an n-th power" moves, where moves may lengthen the word. That is the same shape as a generation-trace certificate built by inserting powers u⁵ and conjugates into a word. The paper also notes that hardness enters exactly when earlier relations hide the large powers. For B(2,5), certificates must come from the generation trace (or an independent check in B₀(2,5) or with kbmag), not from this criterion.

## Quotes

1. > "Note that an elementary move may increase the length of the word." — Introduction
2. > "the previous relations (here uⁿ) mess up the powers." — Introduction

## Open questions surfaced

- Explicit values of n₀ and ξ: what is the smallest odd exponent for which the elementary-move criterion is provable?
- Complexity of the certificates: can the number of elementary moves, or the maximal intermediate length, be bounded in terms of |w| and n?
- Is there an analogue for even large exponents, in the framework of [[coulon-2018-even-exponents]]?
- (Challenge-gen, empirical only) For B(2,5)-trivial words produced by a generator, how often does a "remove u^m, m ≥ 3" move sequence reach the empty word? This would be a heuristic experiment, not a consequence of this paper.

## Related material

- Parent MOC: [[_moc-burnside]]
- MOC: [[_moc-hard-instance-generation]]
- School / landscape: [[coulon-school-partial-periodic-quotients]] (lists this paper; growth and Out(B) follow-ups)
- Sibling: [[coulon-2018-even-exponents]] (same author, even-exponent periodic quotients)
- Exponent thresholds context: [[_synthesis-odd-exponent-state-2026]], [[adian-2015-odd-bound]]
- B(2,5) ground truth (the finite restricted quotient): [[havas-wall-wamsley-1974]], [[B25/_progress]]
- Trivial-word siblings: [[elder-2015-random-trivial-words]], [[2607.26241]] (learning to reduce trivial words)
- Batch synthesis: [[_synthesis-hard-instance-generation]]
- Project: [[project-challenge-gen]]

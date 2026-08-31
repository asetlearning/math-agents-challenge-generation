---
title: "New estimates of odd exponents of infinite Burnside groups"
authors: "S.I. Adian"
year: 2015
venue: "Trudy Matematicheskogo Instituta imeni V.A. Steklova, vol. 289 (Russian); English translation: Proceedings of the Steklov Institute of Mathematics, 289:1 (2015), 33–71"
url: "https://www.mathnet.ru/eng/tm/v289/p41"
url_translated: "https://doi.org/10.1134/S0081543815040045"
language: ru
domain: group-theory
status: draft
methodology_type: theoretical
citation_count: 26
citation_count_date: 2026-07-31
key_concepts: []
extends:
  - "[[b-exponent-5-adian-4.2b]]"
contradicts: []
replicates: []
cites: []
cited_by: []
quality_notes: "Genuinely peer-reviewed, DOI'd journal publication (confirmed via CrossRef + OpenAlex). CRITICAL clarification from reading the full text (mathnet.ru PDF, ru): this paper is EXPLICITLY only a SKETCH of key ideas, not a full proof — Adian states (§11) that 'the complete proof of this new result on groups of odd period n≥101 is being prepared for publication in the journal Russian Mathematical Surveys (Uspekhi Mat. Nauk)' and that he here confines himself to 'presenting some key ideas.' So the community's non-adoption is not mysterious: there was never a complete proof in this paper to build on. This vindicates and sharpens Wikipedia's 'never fully completed and never published' remark — the DOI'd 2015 paper is real, but it is a research announcement + sketch, and the promised full Uspekhi proof has not (as of this scan) materialised. Downstream papers correctly continue to cite n≥665 (Adian 1975) as the operative, fully-proved bound."
fill_level: full
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/odd-exponent-burnside
  - paper
  - status/draft
project: null
---

# New estimates of odd exponents of infinite Burnside groups

## Abstract

> This article consists of two parts. The first part presents a detailed history of the long-term joint work (1960–1968) of the author and P.S. Novikov on the proof of the infiniteness of the free periodic groups B(m,n) for odd periods n≥4381 and m>1 generators (Sections 1, 2). In Sections 3–10 we give a brief survey of the most important results obtained over the past half-century by the author and his successors using the Novikov–Adian theory and its various modifications. In the second part of the article (Sections 11–15) the main outlines of a new modification of the Novikov–Adian theory are set out. This modification makes it possible to lower to n≥101 the lower bound on the odd periods n for which we succeed in proving the infiniteness of the groups B(m,n). The author intends to publish a full proof of this new result in the journal *Russian Mathematical Surveys*. [trans.]

## TL;DR

A survey-plus-announcement paper. Part 1 is history (Novikov–Adian 1960–68, odd n≥4381) and a half-century survey of the rank-induction machinery. Part 2 (§§11–15) **sketches** a new modification of that machinery claimed to lower the odd-exponent infiniteness bound from n≥665 (Adian's 1975 book) to **n≥101**, by retuning the core numeric parameters. Crucially — visible only on reading the full text — Adian states the **complete proof is deferred to a future *Uspekhi Mat. Nauk* paper**; what appears here is explicitly "only key ideas." So it is a research announcement with a proof sketch, not a self-contained proof, which explains why the community still cites n≥665 as the operative bound.

## Problem

Push the smallest odd exponent n for which the free Burnside/periodic group B(m,n) (m>1) is provably infinite below Adian's 1975 bound of n≥665. Adian first floated the target n≥101 as a conjecture in his 1973 Canberra ICTG talk, before the 1975 book (n≥665) was even in print (§11).

## Approach

The Novikov–Adian method proves an enormous family of statements by **simultaneous induction on the *rank* α** of periodic words (roughly, the depth of nesting of periodic subwords; §3). The group B(m,n) is built rank by rank, each rank α adjoining new defining relations Aⁿ=1 for the "elementary periods" A of that rank — relations that provably do *not* follow from lower-rank relations, so B(m,n) is not finitely presented (§3).

The 2015 modification keeps this architecture but **retunes the numeric parameters** driving the estimates. The foundational overlap lemma is sharpened to its tight form:

> **Lemma 2 (§11).** If a graphical equality `A^t A' = B^r B'` holds with A, B minimal periods, A' a nonempty prefix of A, B' a nonempty prefix of B, and `|A^t A'| ≥ |A| + |B| − 1`, then A = B. [trans.]

(The classical book proved the same under the weaker hypothesis `≥ |A|+|B|`; shaving one letter is what propagates through the induction to allow smaller n.)

- **Classical construction (Adian 1975 / this paper §3):** parameters p=10, q=10p=100, threshold n>10⁴ in the general setup.
- **New construction (§11, eq. 11.1):** **m>1, p=6, q=3p=18, n≥101.**

Sections 12–15 then re-develop the ladder for the new parameters: complete normal form of reduced words (§12), regular occurrences of rank 1 (§13), periodic words of rank 2 (§14), absolutely reduced words (§15), culminating (§15) in "by the same scheme as Theorem 3, the corresponding statement for odd n≥101 is proved, from which the infiniteness of B(m,n) follows."

## Key result

- **Main theorem (§11), verbatim:** "Free periodic groups B(m,n) of odd period n>100, m>1, are infinite." [trans.] I.e. odd n≥101 ⟹ B(m,n) infinite for m≥2.
- **Mechanism:** achieved by the parameter retuning p=10→6, q=100→18 (eq. 11.1) plus the tightened overlap Lemma 2, propagated through the rank induction.
- **The threefold ladder Adian highlights (§11):** 4381 > 665 > 101, with the "curious" near-geometric relation 4381/665 ≈ 665/101 (the two ratios differ by less than 0.004).
- **Status caveat (§11), verbatim:** the full proof "is being prepared for publication in the journal *Russian Mathematical Surveys*"; the present text gives "only some key ideas." [trans.]
- For literature context: Novikov–Adian 1968, n≥4381; Adian 1975/1979 book, n≥665 (the number actually used downstream — see [[b-exponent-5-adian-4.2b]]); Ol'shanskii 1982, alternative proof for n>10¹⁰ (§10); Atkarskaya–Rips–Tent 2023 (different method), n≥557 ([[atkarskaya-rips-tent-2023]]).

## Assumptions

- m>1 generators; **n odd** (the entire Novikov–Adian rank machinery is odd-exponent; even exponents need Ivanov/Lysenok-type additions, out of scope here).
- The infiniteness argument assumes the rank-induction framework of Adian's 1975 book [12] as background; §11 explicitly asks the reader "well acquainted with the deep details of the proof in book [12]" to be able to fill in the sketch.
- The n≥101 result's completeness assumes the deferred *Uspekhi* proof — not present in this paper.

## Limitations / scope

- **This paper is a sketch, not a proof.** The n≥101 claim is stated as a theorem but its proof is explicitly deferred to a future *Uspekhi Mat. Nauk* article (§11). What is given here are "key ideas" (§§11–15) that a reader deeply familiar with [12] "could complete." Treat n≥101 as *announced*, not *established*.
- The promised full *Uspekhi* proof has not (as of this scan) appeared; the operative, fully-proved bound in the literature remains n≥665.
- The community citation pattern is consistent with this reading: downstream papers (incl. Atabekyan et al.) use n≥665 or larger, not n≥101 — not because they reject the announcement, but because there is no complete proof to cite.
- **n=5 remains far out of reach** of this whole family of results — this paper does not bear on B(2,5)/Kourovka 11.48. Even the announced n≥101 is two orders of magnitude above 5, and the method is odd-exponent only.

## Replication evidence

`no` — no independent proof, verification, or citation-as-foundation of the n≥101 bound found. This is expected given that the paper itself defers the full proof; there is nothing complete to replicate. The n≥665 bound it recapitulates is, by contrast, thoroughly established (Adian 1975 book).

## Why this paper matters

This is the primary source that must not be misquoted as "the current record is n≥101." Read in full, it is a survey + research announcement in which the headline result is explicitly a sketch with the complete proof promised elsewhere and (so far) unpublished. That reframing is the single most important correction over the previous abstract-only note: the earlier ambiguity ("did the community ignore a real proof, or is there a gap?") is resolved by the paper's own text — there was no full proof here to ignore.

It also has real value as the clearest first-person account of the Novikov–Adian rank-induction method and its parameter budget (p, q, n), which is precisely the machinery the algo_mixing program is trying to make rank-independent. The concrete parameter triple (p=6, q=18, n≥101) and the tight overlap Lemma 2 are the reusable technical content.

## Quotes

1. > "Free periodic groups B(m,n) of odd period n>100, m>1, are infinite." — §11 [trans.]
2. > "The author intends to publish a full proof of this new result in the journal *Russian Mathematical Surveys*." — Abstract [trans.]

## Open questions surfaced

- **Has the promised full *Uspekhi* proof of n≥101 ever appeared?** The paper defers to it (§11); this scan found no such completed article. Resolving this settles the entire status question. (Best lead: the 2021 Uspekhi survey "Adian's scientific legacy," co-authored by Lysenok — [[lysenok-2023-sample-iterated-sc]].)
- The tight overlap Lemma 2 (`≥ |A|+|B|−1 ⟹ A=B`) is the kind of one-letter sharpening that, in the algo_mixing rung program, corresponds to squeezing a piece bound; is there a formal analogue in the period-band setup?
- Does the parameter retuning p=10→6 have a limit-argument analogue (a rank-independent constant)? This is the same target as the ART β=15 constant ([[atkarskaya-rips-tent-2023]]).

## Related material in vault

- Extends: [[b-exponent-5-adian-4.2b]] (same open-problem lineage — general odd-exponent threshold, not exponent 5 specifically)
- Contradicts: (none confirmed)
- Replicates: (none)
- Concepts introduced/used: (none tagged this scan — proof unread)
- Cites: (unread)
- Cited by (in vault): [[_synthesis-odd-exponent-state-2026]]
- MOC: [[_moc-burnside]]

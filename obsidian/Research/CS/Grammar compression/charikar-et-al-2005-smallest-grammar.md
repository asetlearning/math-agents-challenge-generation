---
title: "The smallest grammar problem"
authors: Moses Charikar, Eric Lehman, Ding Liu, Rina Panigrahy, Manoj Prabhakaran, Amit Sahai, abhi shelat
year: 2005
venue: "IEEE Transactions on Information Theory 51(7), 2554–2576"
url:
url_translated:
language: en
domain: cs
status: draft
methodology_type: theoretical
citation_count: null
citation_count_date:
key_concepts: []
extends: []
contradicts: []
replicates: []
cites: []
cited_by: []
quality_notes: "FULL TEXT NOT OBTAINED: the IEEE version is paywalled and the 2002 preprint host (compression.ru) returned HTTP 406. This note restates what the 2019 follow-up paper (Bannai et al., arXiv 1908.06428, read in full intro) says about Charikar et al.; every claim below is second-hand. The journal DOI above was not resolved/verified."
author: asetlearning
tags:
  - agent/research
  - user/asetlearning
  - domain/cs
  - topic/grammar-compression
  - topic/hard-instance-generation
  - paper
  - status/draft
project: challenge-gen
---

# The smallest grammar problem

## Abstract

Not read (see quality_notes). From Bannai et al. (arXiv 1908.06428), the paper is "seminal": it derives upper and lower bounds on the approximation ratios of several grammar-based compressors (LZ78, BISECTION, Sequential, RePair, LongestMatch, Greedy), always with a gap between the bounds, and proves hardness of the smallest-grammar problem.

## TL;DR

Smallest straight-line program (grammar) for a string is NP-hard to compute and to approximate within 8569/8568; the paper analyses approximation ratios of standard compressors (including Re-Pair) and gives a linear-time compressor with ratio $O(\log n)$. [second-hand]

## Problem

Given a string $w$, find a context-free grammar generating exactly $w$ of minimum size $g(w)$.

## Approach

[second-hand] Hardness reduction (unbounded alphabet); worst-case approximation-ratio analysis of practical compressors; an $O(\log n)$-ratio linear-time algorithm.

## Key result

All second-hand from Bannai et al., §1.3: (i) Storer–Szymanski and Charikar et al.: the smallest-grammar problem is not polynomial-time solvable unless P = NP; (ii) unless P = NP one cannot compute in polynomial time an SLP of size $<(8569/8568)\,g(w)$; the construction uses an unbounded alphabet (hardness for alphabet size 24 is in a later paper [6]; binary open); (iii) a linear-time compressor with approximation ratio $O(\log n)$; (iv) no polynomial-time compressor with ratio $o(\log n)$ is known, and ratio $o(\log n/\log\log n)$ would solve a long-standing addition-chain problem; (v) for RePair the lower bound was $\Omega(\sqrt{\log n})$ (improved to $\Omega(\log n/\log\log n)$ by Bannai et al.).

## Assumptions

Worst-case over strings of length $n$ over arbitrary alphabets.

## Limitations / scope

Worst-case ratios; typical behaviour of Re-Pair on structured, highly repetitive inputs (such as substitution instances $t(x,y)$) is not covered by these bounds. Free-group inverse symmetry is not modelled.

## Replication evidence

Second-hand results are restated in Bannai et al. without dispute.

## Why this paper matters

Anchors the claim that a generator can only be attacked heuristically by grammar compression: exact minimal grammars are NP-hard, but a good-enough grammar is cheap, and a block structure like $W=t(x,y)$ gives a grammar of size about $|t|+|x|+|y|$ for a word of length $|t||x|$. Whether a given scrambling defeats Re-Pair-type compressors must be measured, not proved from these bounds.

## Quotes

(none; full text not read)

## Open questions surfaced

- Obtain the full text and check the exact approximation-hardness constant and the definition of size (rules vs symbols).

## Related material in vault

- Related: [[bartholdi-figelius-lohrey-weiss-2020]]
- Synthesis: [[_synthesis-t028-literature-2026-10-20]]

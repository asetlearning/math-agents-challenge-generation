---
title: "Numerical values of the growth rates of power-free languages"
authors: "Arseny M. Shur"
year: 2010
venue: "arXiv (CoRR abs/1009.4415)"
url: "https://arxiv.org/abs/1009.4415"
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
cites: []
cited_by: []
quality_notes: "Full PDF text independently obtained and read by the research subagent this scan (arXiv v2, revised 2012-04-04) — the only source in this literature pass verified beyond abstract/metadata level. Explicitly self-described as 'not a research paper but rather an appendix' collecting numerical bounds drawn from the author's separate algorithmic papers (TCS 2010, DLT 2009) — those underlying papers were bibliographically confirmed but NOT independently re-read (paywalled)."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/power-free-words
  - topic/burnside
  - paper
  - status/draft
project: null
---

# Numerical values of the growth rates of power-free languages

## Abstract

Explicitly not a standalone research contribution but a numerical appendix; no separate formal abstract distinct from the TL;DR below (confirmed via direct full-text read).

## TL;DR

A reference table (verified via direct full-text read) of the best proven two-sided bounds on $\alpha(k,\beta)$, the growth rate of the language of β-power-free words over a k-letter alphabet, for $k=2$ to $15$. For the binary alphabet ($k=2$), it gives verbatim numbers for cube-free through 9th-power-free growth, including **5th-power-free: growth rate in $[1.9244437,\ 1.9646285]$** — confirmed exponential. See [[Concepts/power-free-word-growth-rates]] for the full table and Burnside-problem context.

## Problem

Collect and tabulate the best currently-known numerical bounds on power-free language growth-rate constants, drawing on the author's separate algorithmic papers, as a reference appendix for the field.

## Approach

Two techniques combined: (1) "regular approximation" — upper bounds via finite automata that forbid powers only up to some bounded period $m$ (from the author's TCS 2010 algorithm); (2) two-sided (lower+upper) rigorous bounds for $\beta \ge 2$ (extended to $\beta\ge 7/2$ via a strengthened argument) from the author's DLT 2009 paper.

## Key result

Full binary-alphabet table (β-power-free growth rate α(2,β), verbatim from the paper, all values confirmed via direct full-text read this scan):

- β=7/3: exactly 1.0000000 (polynomial)
- β=3 (cube-free): 1.4575732 – 1.4575773 (est. ≈1.4575772869237)
- β=4: 1.8211000 – 1.9208015
- **β=5: 1.9244437 – 1.9646285**
- β=6: 1.9653118 – 1.9832942
- β=7: 1.9834409 – 1.9918972
- β=8: 1.9919310 – 1.9960151
- β=9: 1.9960232 – 1.9980255

Ternary square-free: upper bound 1.301761876, estimated exact ≈1.30176183, lower bound 1.3017597.

Explicit statement (paraphrased from the paper, per subagent read): the binary $(2^+)$-power-free language has polynomial growth (rate 1), and so does the binary $(7/3)$-power-free language — the threshold into exponential growth sits strictly above $\beta=7/3$ on 2 letters.

## Assumptions

Standard formal-language / combinatorics-on-words framework; bounds rely on the correctness of the underlying algorithmic papers (TCS 2010, DLT 2009), not independently re-derived here.

## Limitations / scope

- This is a numerical reference appendix, not a proof paper in itself — for full proofs, the reader is directed to the two underlying papers (not independently re-read this scan, paywalled).
- Says nothing directly about the Burnside problem — see [[Concepts/power-free-word-growth-rates]] for the (currently unbridged) connection to Adian's rank-α combinatorial apparatus.

## Replication evidence

N/A — reference table, not an experimental claim requiring replication in the usual sense; the underlying two papers it draws from were not independently checked this scan.

## Why this paper matters

The best available primary-source anchor for "5th-power-free words over 2 letters grow exponentially," which is the natural combinatorial analogue (though NOT a proven substitute — see the concept note) of the aperiodic-word substrate that powers the classical Novikov–Adian argument for odd n≥665/4381. Useful as a precise, citable numeric fact when discussing the "combinatorial evidence" layer of Burnside-problem arguments, as long as the gap noted in [[Concepts/power-free-word-growth-rates]] (no literature bridge to Adian's actual rank-α construction) is kept explicit.

## Quotes

1. > "not a research paper but rather an appendix" — self-description, Introduction (relayed via subagent full-text read).

## Open questions surfaced

- See [[Concepts/power-free-word-growth-rates]] — primarily, whether any paper anywhere bridges this growth-rate machinery to Adian's specific rank-α periodic-word apparatus.

## Related material in vault

- Extends: (none)
- Contradicts: (none)
- Replicates: (none)
- Concepts introduced/used: [[Concepts/power-free-word-growth-rates]]
- Cites: (none confirmed)
- Cited by (in vault): [[_synthesis-odd-exponent-state-2026]]
- MOC: [[_moc-burnside]]

---
title: "Space functions of groups"
authors: A. Yu. Olshanskii
year: 2011
venue: "arXiv 1009.3580 (v2, 4 Nov 2010, read); journal version not checked"
url: https://arxiv.org/abs/1009.3580
url_translated:
language: en
domain: group-theory
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
quality_notes: "Introduction (§1) read in full; the Turing-machine constructions of §§2+ were not read. Bridson–Riley (ref [7]) is the source of the FL/FFL/FFFL distinctions and was not read."
author: asetlearning
tags:
  - agent/research
  - user/asetlearning
  - domain/group-theory
  - topic/filling-length
  - topic/space-complexity
  - topic/word-problem
  - topic/dehn-function
  - paper
  - status/draft
project: challenge-gen
---

# Space functions of groups

## Abstract

Time and space complexities are the main properties of algorithms. Their counterparts in Group Theory are the Dehn and filling length (or space) functions of finitely presented groups. In this paper, we study the interrelation of space functions of groups and the space complexity of the algorithmic word problem in groups. (§1, opening)

## TL;DR

Defines the space of a rewriting as the maximum total length of the word-sequences it passes through, using the most permissive move set (free reduction, relator insertion/removal, cyclic conjugation, splitting $uv\to(u,v)$ into two trivial words). Shows this space function equals the space function of a nondeterministic Turing machine, links it to word-problem space complexity (Prop 1.1, Thm 1.2, Cor 1.3 for PSPACE) and shows every DTM space function is a group space function (Thm 1.4).

## Problem

Is there a group-theoretic counterpart of space complexity of algorithms, as the Dehn function is for time? How tightly do space functions control the space needed to solve the word problem?

## Approach

Take sequences $W=(w_1,\dots,w_s)$ of words; elementary $R$-transformations: insert/remove $aa^{-1}$, insert/remove a relator$^{\pm1}$, cyclic conjugate a word, split $w_i\equiv uv$ into $u,v$, delete an empty word. $\|W\|=\sum\|w_i\|$; space of a rewriting $=\max_j\|W_j\|$; $S_G(n)=\max\{\mathrm{space}(w):w=1,\|w\|\le n\}$. This choice is Bridson–Riley's fragmenting free filling length (FFFL); the paper notes FL (Gromov, no cyclic conjugation, no splitting) and FFL (cyclic conjugation allowed) are the other variants. Constructions of §§2+ encode Turing machines into group presentations (Novikov–Boone–Britton style, "hub relation").

## Key result

- **Prop 1.1.** $S_G$ is equivalent to the space function of a nondeterministic two-tape TM accepting exactly the words equal to 1 in $G$ (an NTM needs at most $2\max\|W_i\|+\text{const}$ tape squares).
- Hence nondeterministic word-problem space of $G$ is bounded by $S_G$; the converse fails literally: Baumslag's one-relator group $\langle a,b\mid (aba^{-1})b(aba^{-1})^{-1}=b^2\rangle$ has space function not bounded by any multi-exponential, while its word problem has at most exponential space (Kapovich–Schupp, unpublished) and is polynomial (announced by Myasnikov–Ushakov–Won).
- **Thm 1.2.** If $H$ has word problem decidable by a DTM with space $f(n)$, then $H$ embeds in a finitely presented $G$ with space function $\sim f(n)$. **Cor 1.3.** $H\in$ PSPACE iff $H$ embeds in a finitely presented group with polynomial space function.
- **Thm 1.4.** Every DTM space function is equivalent to the space function of some finitely presented group; **Cor 1.6.** $[n^\alpha]$ ($\alpha\ge1$) is a group space function iff $\alpha$ is computable with space $\le 2^{2^m}$.
- Cited from Bridson–Riley: FFFL can grow linearly while FL and FFL grow exponentially, for the same group.

## Assumptions

Finitely presented groups; space functions up to the standard equivalence; non-deterministic rewriting (existence of a rewriting, not a search strategy).

## Limitations / scope

Asymptotic. Speaks of what is possible (existence of a low-peak rewriting), not of what a given solver finds; says nothing about finite groups where every function is bounded.

## Replication evidence

Not applicable (theoretical); independent treatment in Bridson–Riley (not read).

## Why this paper matters

The cleanest statement that *peak word length along a reduction* is the right formal object for "space of a reducer", and that its definition depends on the move set (FL vs FFL vs FFFL can differ exponentially). Any benchmark that defines "long peak" must say which of these it means; for solvers that rotate cyclic words and split words the relevant function is FFFL, not Gromov's FL.

## Quotes

1. > "Time and space complexities are the main properties of algorithms." — §1

## Open questions surfaced

- Which move set does each solver in the challenge-gen pipeline implement (cyclic rotation: yes for R and for the proposal's definition; splitting: unclear)?
- Whether any of these functions has a useful finite-group analogue (e.g. peak over words of length $\le n$ for fixed finite $G$).

## Related material in vault

- Related: [[gersten-riley-2002]] (filling length bounds; citation link not verified)
- Synthesis: [[_synthesis-t028-literature-2026-10-20]]

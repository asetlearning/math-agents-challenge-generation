---
title: "Groups with ALOGTIME-hard word problems and PSPACE-complete compressed word problems"
authors: Laurent Bartholdi, Michael Figelius, Markus Lohrey, Armin Weiß
year: 2020
venue: "arXiv 1909.13781 (v5, 20 Jun 2020, intro read); published version not checked"
url: https://arxiv.org/abs/1909.13781
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
quality_notes: "44-page paper; only the abstract and introduction (pp. 1-4 of the PDF) were read. Included because the T-028 note cited it for compressed word problems; Lead's message paired this paper's name with arXiv 2203.11148, which is a different paper (see coleman-mitchell-smith-tsalakou-2022-todd-coxeter-semigroups)."
author: asetlearning
tags:
  - agent/research
  - user/asetlearning
  - domain/group-theory
  - topic/word-problem
  - topic/compressed-word-problem
  - topic/space-complexity
  - paper
  - status/draft
project: challenge-gen
---

# Groups with ALOGTIME-hard word problems and PSPACE-complete compressed word problems

## Abstract

We give lower bounds on the complexity of the word problem of certain non-solvable groups: for a large class of non-solvable infinite groups, including in particular free groups, Grigorchuk's group and Thompson's groups, we prove that their word problem is NC1-hard. For some of these groups (including Grigorchuk's group and Thompson's groups) we prove that the compressed word problem (which is equivalent to the circuit evaluation problem) is PSPACE-complete.

## TL;DR

Complexity-theoretic paper: generalises Barrington's and Robinson's constructions via a "strongly efficiently non-solvable" (SENS) condition, giving NC1-hardness of word problems, and proves PSPACE-completeness of the *compressed* word problem (word given as a straight-line program) for several natural infinite groups. For our purposes the useful content is the survey of which groups have efficient compressed word problems.

## Problem

Lower bounds on word-problem complexity beyond finite groups; groups where compression makes the word problem provably harder.

## Approach

Barrington-style simulation of and-gates by commutators, requiring balanced nested commutators of arbitrary depth with at most exponentially growing word length (SENS, Def. 15); leaf-language reductions using a self-embedding property $G\wr A\hookrightarrow G$.

## Key result

- Thms 33, 35: every (uniformly) SENS group has (uniformly) NC1-hard word problem; Cor. A: ALOGTIME-hard for Thompson's $F,T,V$ and weakly branched self-similar groups with f.g. branching subgroup.
- Cor. B: compressed word problem PSPACE-complete for $G\wr\mathbb Z$ ($G$ finite non-solvable or free of rank $\ge2$), Thompson's groups, Grigorchuk's group, Gupta–Sidki groups.
- Survey statements in the introduction: compressed word problem is in P for finitely generated nilpotent groups (even NC2), hyperbolic groups, virtually special groups; it is P-complete for non-solvable finite groups and non-abelian free groups (refs [8,45]); in coRP for linear groups. A straight-line program is a context-free grammar producing exactly one string, possibly exponentially longer than the program.
- Finite $p$-groups are not NC1-hard: they are nilpotent, "so iterated commutators eventually become trivial" (intro).

## Assumptions

Standard circuit-complexity separations are not assumed in the survey statements; hardness claims are relative to the complexity classes named.

## Limitations / scope

Infinite groups; says nothing about finite exponent-5 groups beyond the nilpotent/$p$-group remarks. Only the introduction was read here.

## Replication evidence

Theoretical, published results; not checked independently.

## Why this paper matters

For substitution-recovery attacks it fixes the baseline: *given* a grammar (SLP) for a word, deciding triviality in B(2,5) (a finite 5-group, nilpotent) is efficient; the open part for generation is *finding* a small grammar for an explicit word, which is the smallest-grammar problem ([[charikar-et-al-2005-smallest-grammar]]).

## Quotes

1. > "A straight-line program is a context-free grammar that produces exactly one string." — §1

## Open questions surfaced

- Exact complexity of the compressed word problem for finite $p$-groups of large class such as $B_0(2,5)$ (the survey says only nilpotent, polynomial).

## Related material in vault

- Related: [[charikar-et-al-2005-smallest-grammar]], [[epstein-et-al-1992-word-processing]]
- Synthesis: [[_synthesis-t028-literature-2026-10-20]]

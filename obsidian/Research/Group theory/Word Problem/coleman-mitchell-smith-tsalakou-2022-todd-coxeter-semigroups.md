---
title: "The Todd-Coxeter Algorithm for Semigroups and Monoids"
authors: T. D. H. Coleman, J. D. Mitchell, F. L. Smith, M. Tsalakou
year: 2022
venue: "arXiv 2203.11148 (v2, 8 Mar 2024, read in part)"
url: https://arxiv.org/abs/2203.11148
url_translated:
language: en
domain: group-theory
status: draft
methodology_type: methodology
citation_count: null
citation_count_date:
key_concepts: []
extends: []
contradicts: []
replicates: []
cites:
  - "[[todd-coxeter-1936]]"
cited_by: []
quality_notes: "42-page paper; only the abstract, table of contents and §1 were read for this note (the T-028 question concerned the §1 remark on arbitrarily long enumerations). Sections 3-9 and the appendix benchmarks were not read. NOTE: Lead's task message attributed this arXiv id to 'Bartholdi et al.'; it is Coleman et al."
author: asetlearning
tags:
  - agent/research
  - user/asetlearning
  - domain/group-theory
  - topic/coset-enumeration
  - topic/word-problem
  - topic/pathological-presentations
  - paper
  - status/draft
project: challenge-gen
---

# The Todd-Coxeter Algorithm for Semigroups and Monoids

## Abstract

In this paper we provide an account of the Todd-Coxeter algorithm for computing congruences on semigroups and monoids. We also give a novel description of an analogue for semigroups of the so-called Felsch strategy from the Todd-Coxeter algorithm for groups.

## TL;DR

Expository and algorithmic account of Todd–Coxeter congruence enumeration for finitely presented semigroups and monoids (HLT and a new Felsch-style strategy, validity proofs, implementation issues, benchmarks incl. finitely presented groups). Its §1 notes that run time cannot be predicted from the presentation: trivial-group presentations exist with arbitrarily long enumerations.

## Problem

Give a rigorous, implementation-oriented description of congruence enumeration for semigroups/monoids and a Felsch analogue.

## Approach

Word graphs, compatibility/completeness (§3–4), HLT strategy (§6), two versions of the Felsch strategy (§7), implementation issues (§8), variants (§9: zero, Rees congruences, Stephen's procedure); appendices with extended examples and performance comparisons including finitely presented groups.

## Key result

Statement relevant here (§1): a coset enumeration terminates iff the subgroup has finite index; the number of steps cannot be predicted: "it is relatively straightforward to find examples of finite presentations for the trivial group where the number of steps in a coset enumeration is arbitrarily high", e.g. $\langle a,b\mid ab^n,\ a^nb^{n+1},\ b^nab^{-1}a^{-1}\rangle$ (trivial group, "likely that at least $n$ steps are required in any coset enumeration" — the authors cite their ref [17], not a proof given here).

## Assumptions

Finitely presented semigroups/monoids; enumeration may not terminate (word problem undecidable, Novikov–Boone).

## Limitations / scope

Semigroup/monoid focus; the statement about arbitrarily long enumerations is a remark with an example and a "likely", not a theorem proved in this paper.

## Replication evidence

Implementation in libsemigroups (not examined).

## Why this paper matters

Current reference for Todd–Coxeter variants and strategies (HLT, Felsch) if the challenge-gen pipeline ever needs a coset-enumeration solver for monoid presentations; also a citable source for "enumeration length is unpredictable even for the trivial group".

## Quotes

1. > "it is relatively straightforward to find examples of finite presentations for the trivial group where the number of steps in a coset enumeration is arbitrarily high" — §1

## Open questions surfaced

- Whether the performance appendix (B.4, finitely presented groups) compares strategies on presentations of the Neumann type (not read).

## Related material in vault

- Related: [[havas-ramsay-2000]], [[todd-coxeter-1936]]
- Synthesis: [[_synthesis-t028-literature-2026-10-20]]

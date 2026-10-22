---
title: "Proving a group trivial made easy: a case study in coset enumeration"
authors: George Havas, Colin Ramsay
year: 2000
venue: "Bulletin of the Australian Mathematical Society 62, 105–118"
url: https://doi.org/10.1017/S0004972700018529
url_translated:
language: en
domain: group-theory
status: draft
methodology_type: empirical
citation_count: null
citation_count_date:
key_concepts: []
extends: []
contradicts: []
replicates: []
cites: []
cited_by: []
quality_notes: "Full text read (14 pp). Experiments on an SGI Origin 2000 with ACE; coincidence-based hand analysis for E3 is described by the authors as contrived and non-automatable."
author: asetlearning
tags:
  - agent/research
  - user/asetlearning
  - domain/group-theory
  - topic/coset-enumeration
  - topic/knuth-bendix
  - topic/pathological-presentations
  - topic/space-complexity
  - topic/hard-instance-generation
  - paper
  - status/draft
project: challenge-gen
---

# Proving a group trivial made easy: a case study in coset enumeration

## Abstract

Coset enumeration, based on the methods described by Todd and Coxeter, is one of the basic tools for investigating finitely presented groups. The process is not well understood, and various pathological presentations of, for example, the trivial group have been suggested as challenge problems. Here we consider one such family of presentations proposed by B.H. Neumann. We show that the problems are much easier than they first appear, albeit at the expense of considerable preliminary 'experimentation'. This demonstrates how far the range of applicability of coset enumeration has improved.

## TL;DR

B. H. Neumann's trivial-group presentations $E_1\to E_2\to E_3\dots$ (each obtained from the previous by substituting words for the generators) were designed to defeat Todd–Coxeter. Havas–Ramsay prove $E_2$ trivial by coset enumeration (about 4 MB, after tuning HLT/Felsch mix and randomised relator rotation/inversion), but Knuth–Bendix (KBMAG, RKBP) proves $E_2$ trivial in 0.6 s and is better on the whole family; the 3-generator $E_3$ remains hard for both.

## Problem

Is the Neumann family really pathological for coset enumeration, and what resources (MaxCos $M$, TotCos $T$, time) does it need? Sims had shown no polynomial bound on the number of coset tables in terms of $M$.

## Approach

Presentations (letters lower/upper case = generator/inverse): $E_1=\langle r,s,t\mid TrtRR,\ RsrSS,\ StsTT\rangle$; $E_2$ is obtained by replacing $r,s,t$ by the words $TrtRR,\ RsrSS,\ StsTT$ (three relators of length 25, total 75); $E_3$ iterates the substitution. Tools: ACE; strategies Felsch (fill next empty table slot), HLT (scan cosets against relators), mixed $n/m$; random equivalent presentations by reordering/rotating/inverting relators (5000 per subgroup, 23 successes in 15000 runs with limit $T\le10^7$); enumeration over subgroups $\langle r\rangle,\langle s\rangle,\langle t\rangle$ and pairs, then over the trivial subgroup. For $E_3$ they add proven relations (coincidences found early) to the relators and restart — "a technique borrowed from the Knuth–Bendix procedure".

## Key result

- $E_1$: easy but "pathological": Felsch trivial-subgroup enumeration gives $T=588$ (Sims); best machine run here $M=79,T=81$.
- $E_2$ over the trivial subgroup, original presentation: $T=825{,}673{,}759$, $M=343{,}662{,}508$ (about 8.9 GB, 3 compactions, 10,768 s). Selected equivalent presentations $E_2'$, $E_2''$: $T=36{,}249{,}963$, $M=4{,}826{,}625$ (best $T$) and $M=4{,}362{,}123$ (best $M$); about 4 MB of table. Felsch strategies are bad, HLT good (Table 1); Sims' coset procedures found no coincidences in $E_2$ within 100,000 cosets.
- Six-generator version of $E_2$ ($x=TrtRR$ etc. as extra generators): 0.29 s with $M=20{,}619$.
- $E_3$: the 3-generator 3-relator form did not complete; a hand-guided 8-relator form completed in 325 s with $M=12{,}020{,}719$, $T=33{,}740{,}210$ — described as "contrived", requiring non-automatable choices of which coincidences to add.
- **Knuth–Bendix (§8, KBMAG):** $E_2$ in 0.6 s (max total rule length 17,070); six-generator $E_2$ 0.1 s; nine-generator $E_3$ 0.5 s; six-generator $E_3$ 1.7 s; the "correct" 3-generator 3-relator $E_3$ takes 1347.4 s with maximum rule length 14,836,607.
- Conclusion: KB beats TC on this family in space and time; best TC results come from proving relations and restarting, i.e. TC+KB combined with human guidance.

## Assumptions

Single machine class (SGI Origin 2000, ACE 3), specific three-relator family of lengths 25; the authors stress throughput ratios are specific to this family.

## Limitations / scope

Trivial-group presentations only; difficulty here is a property of the *presentation* (iterated generator substitution), not of a hard group. Success for $E_2$ relies on preliminary experimentation and randomised presentations; no general method for $E_3$.

## Replication evidence

Self-contained experiments; ACE and KBMAG are public, and the presentations are given in the paper. No independent replication read.

## Why this paper matters

It is a documented precedent for "make instances hard by substituting words for generators": the Neumann iteration *is* verbal substitution on a trivial-group presentation. The record shows (a) one substitution step already defeats naive Todd–Coxeter by orders of magnitude, (b) tuning (strategy, relator rotation, adding proven relations) removes most of the difficulty, (c) Knuth–Bendix is much less sensitive to the substitution, and (d) only after a second substitution does the 3-generator form become hard for KB too (1347 s, 14.8 M rule length). For a benchmark this suggests measuring difficulty against *tuned* solvers and across a substitution ladder.

## Quotes

1. > "This family of presentations is better handled by Knuth-Bendix rewriting methods." — §8

## Open questions surfaced

- Does the same pattern (substitution hard for TC, mild for KB, hard again after a second round) hold for words in B(2,5) rather than presentations of the trivial group?
- Can the "prove short relations, add them, restart" step be automated (the authors say it is hard to see how)?

## Related material in vault

- Concepts: [[Concepts/certified-instance-generation]]
- Related: [[todd-coxeter-1936]], [[knuth-bendix-1970]], [[coleman-mitchell-smith-tsalakou-2022-todd-coxeter-semigroups]]
- Synthesis: [[_synthesis-t028-literature-2026-10-20]]

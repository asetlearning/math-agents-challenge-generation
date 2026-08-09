---
title: "About the centralizer of an automorphism of order 2 of Burnside group B₀(2,5)"
authors: A. A. Kuznetsov, K. A. Philippov
year: 2010
venue: Vladikavkazskii Matematicheskii Zhurnal
url: http://mi.mathnet.ru/vmj362
url_translated:
language: ru
methodology_type: empirical
domain: group-theory
status: draft
citation_count: null
citation_count_date:
key_concepts: []
extends: []
contradicts: []
replicates: []
cites:
  - "[[havas-wall-wamsley-1974]]"
cited_by: []
quality_notes: "CORRECTION (this scan, from FULL TEXT via mathnet getFT PDF, ru, pdftotext): the prior abstract-only note wrongly claimed this paper REPLICATES [[kuznetsov-filippov-2010-sjim]] with 'the same result'. It does NOT. The two 2010 Kuznetsov–Filippov papers study TWO DIFFERENT involutive automorphisms of B₀(2,5): (a) sjim studies the INVERSION automorphism x↦x⁻¹, y↦y⁻¹, centralizer order 5¹⁶, nilpotency 4, solvability 2, 5 generators; (b) THIS vmj paper studies the GENERATOR-SWAP automorphism x↦y, y↦x, centralizer order 5¹⁷, nilpotency 6, solvability 3, 3 generators. These are the two distinct classes of involutive automorphisms of B₀(2,5). So the relationship is 'companion / sister paper', NOT 'replicates'. Vladikavkaz Mat. Zh. 12:4, pp. 44–49 (5 pages), peer-reviewed journal. All numbers below now verbatim from the theorem."
fill_level: full
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/b25
  - topic/restricted-burnside
  - topic/exponent-5
  - topic/center-of-group
  - topic/finite-group-enumeration
  - paper
  - status/draft
project: b25
---

# About the centralizer of an automorphism of order 2 of Burnside group B₀(2,5)

> **Translation note**: source paper is in Russian (`language: ru`). Filled from full text (mathnet getFT PDF, pdftotext); quotes marked [trans.].

## Abstract

We study the centralizer of the involutive automorphism of the Burnside group $B_0(2,5)$ that swaps the generators of $B_0(2,5)$. For this centralizer we find generating elements, compute its order, solvability length, and nilpotency length, and construct both the upper and lower central series. [trans.]

## TL;DR

**Sister paper — NOT a replicate — of [[kuznetsov-filippov-2010-sjim]].** Where the sjim paper handles the *inversion* involution ($x\mapsto x^{-1},y\mapsto y^{-1}$), this paper handles the other class: the **generator-swap** involution $\varphi: x\mapsto y,\ y\mapsto x$ of the restricted Burnside group $B_0(2,5)$ (order $5^{34}$). Main theorem: the centralizer $C = C_{B_0(2,5)}(\varphi)$ has $|C| = 5^{17}$, **nilpotency length 6**, **solvability length 3**, and minimum **3 generators** — all different from the inversion case ($5^{16}$, 4, 2, 5). Same computational method (normal commutator words, action of $\varphi$ on the 34 basis commutators, linear systems over $\mathrm{GF}(5)$), plus explicit upper and lower central series.

## Problem

Determine the structure of the centralizer $C = \{g\in B_0(2,5): \varphi(g)=g\}$ of the **generator-swap** involutive automorphism $\varphi: x\mapsto y,\ y\mapsto x$ — the second of the two classes of involutive automorphisms of $B_0(2,5)$ (the first, inversion, is treated in [[kuznetsov-filippov-2010-sjim]]).

## Approach

Same computational template as the sjim companion: represent every $g\in B_0(2,5)$ uniquely as a normal commutator word $g = c_1^{\alpha_1}\cdots c_{34}^{\alpha_{34}}$ ($\alpha_i\in\{0,\dots,4\}$) over 34 basis commutators; compute the action of $\varphi$ on each basis commutator (given verbatim; note $\varphi(1)=(0,1,0,\dots)$, $\varphi(2)=(1,0,0,\dots)$ — i.e. it swaps the two generators); reduce the fixed-point condition $\varphi(g)=g$ to enumeration over the low commutators plus linear systems over $\mathrm{GF}(5)$ for the abelian tail (commutators 11–34); count solutions to get $|C|$; then extract generators and both central series.

## Key result

**Theorem (verbatim, [trans.]).** For $C$ the following hold:
1. $|C| = 5^{17}$.
2. The nilpotency length and solvability length of $C$ equal $6$ and $3$ respectively.
3. $3$ is the minimum number of generators of $C$.

Plus (from the body): explicit generating elements, and explicit construction of the **upper** and **lower central series** of $C$.

**Contrast with the inversion involution ([[kuznetsov-filippov-2010-sjim]]):**

| invariant | inversion ($x\mapsto x^{-1}$) | swap ($x\mapsto y$) |
|---|---|---|
| $\lvert C\rvert$ | $5^{16}$ | $5^{17}$ |
| nilpotency length | 4 | 6 |
| solvability length | 2 | 3 |
| min. generators | 5 | 3 |

## Assumptions

- $\varphi$ is the generator-swap automorphism $x\mapsto y,\ y\mapsto x$ (well-defined on $B_0(2,5)$).
- Havas–Wall–Wamsley normal-commutator presentation of $B_0(2,5)$ (order $5^{34}$) as computational substrate.
- Correctness rests on the reported computer computations over $\mathrm{GF}(5)$.

## Limitations / scope

- Specific to the swap involution; the inversion class is the companion paper.
- About $B_0(2,5)$ (restricted Burnside), not directly $B(2,5)$.
- Purely computational; 5 pages, so some intermediate computations are compressed relative to the 8-page sjim paper, but the theorem is a distinct result, not an abbreviation of it.

## Replication evidence

`no` — this is a distinct result (different automorphism) from its companion; not independently replicated elsewhere in the vault. It corrects, rather than corroborates, the sjim numbers.

## Why this paper matters

Together with [[kuznetsov-filippov-2010-sjim]], this paper completes the picture of centralizers of the **two** involutive-automorphism classes of $B_0(2,5)$: inversion gives $5^{16}$ (nilp 4, solv 2, 5 gens) and generator-swap gives $5^{17}$ (nilp 6, solv 3, 3 gens). Having both is essential to avoid the exact error the prior abstract-only note made (treating them as the same result). For the B25 program these are two more concrete, checkable structural invariants of $B_0(2,5)$.

## Quotes

1. > "$|C| = 5^{17}$." — Theorem [trans.]
2. > "The nilpotency and solvability lengths of $C$ equal six and three respectively." — Theorem [trans.]

## Open questions surfaced

- Why does the generator-swap centralizer ($5^{17}$) exceed the inversion one ($5^{16}$) by exactly one factor of 5, and does that reflect a fixed generator-symmetric central element?
- Is there a conceptual (non-computational) reason the two involution classes give nilpotency lengths 4 vs 6 and generator counts 5 vs 3?

## Related material in vault

- Companion (sister paper, different involution — NOT a replicate): [[kuznetsov-filippov-2010-sjim]]
- Cites: [[havas-wall-wamsley-1974]]
- MOC: [[Research/Group theory/_MOCs/_moc-burnside]]

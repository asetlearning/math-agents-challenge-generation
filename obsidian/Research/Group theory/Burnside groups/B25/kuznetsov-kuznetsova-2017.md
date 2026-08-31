---
title: "The Cayley graph of a subgroup of the Burnside group B₀(2,5)"
authors: A. A. Kuznetsov, A. S. Kuznetsova
year: 2017
venue: Prikladnaya Diskretnaya Matematika. Supplement
url: https://doi.org/10.17223/2226308X/10/6
url_fulltext: "https://www.mathnet.ru/php/getFT.phtml?jrnid=pdma&paperid=342&what=fullt&option_lang=eng"
url_translated:
language: ru
methodology_type: empirical
domain: group-theory
status: draft
citation_count: null
citation_count_date:
key_concepts:
  - "[[Concepts/growth-functions-burnside]]"
  - "[[cayley-diameter]]"
  - "[[power-commutator-presentation]]"
extends:
  - "[[kuznetsov-filippov-2010-vmj]]"
contradicts: []
replicates: []
cites:
  - "[[kuznetsov-2016]]"
  - "[[kuznetsov-kuznetsova-2013]]"
  - "[[kuznetsov-filippov-2010-vmj]]"
  - "[[havas-wall-wamsley-1974]]"
cited_by: []
quality_notes: "3-page conference note (Prikl. Diskr. Mat. Suppl. 10, pp. 19–21, DOI 10.17223/2226308X/10/6). Original in Russian. RE-FILLED FROM FULL TEXT (mathnet getFT PDF, pdftotext — Cyrillic renders cleanly). CORRECTION to prior note: the automorphism φ is the GENERATOR-SWAP φ: a₁↦a₂, a₂↦a₁ (verbatim in the paper), NOT a generic 'permutation-type' guess — and its structural facts (|C|=5^17, solvability 3, nilpotency 6, min 3 generators) come from ref [6] = [[kuznetsov-filippov-2010-vmj]] (Vladikavkaz Math. J. 2010), NOT [[kuznetsov-filippov-2010-sjim]] (which is the DIFFERENT inversion automorphism a_i↦a_i^{-1}, |C|=5^16). Corrected extends/cites accordingly. Base growth-function algorithm is ref [5] = [[kuznetsov-2016]]; fast multiplication via Hall polynomials ref [8] = [[kuznetsov-kuznetsova-2013]]. Shunkov's theorem [7] provides the finiteness tie. NOTE: the source PDMA-supplement PDF interleaves neighbouring articles (a VKP-function/ring note before, a matroids/block-designs note after); only the middle article, pp. 19–21, is this paper."
fill_level: full
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/b25
  - topic/restricted-burnside
  - topic/cayley-graphs
  - topic/growth-functions
  - topic/center-of-group
  - topic/exponent-5
  - paper
  - status/draft
project: b25
---

# The Cayley graph of a subgroup of the Burnside group B₀(2,5)

> **Translation note**: source paper is in Russian (`language: ru`). Abstract below is translated to English [trans.] from the mathnet.ru record.

## Abstract

The research examines the largest two-generator Burnside group of exponent five with order $5^{34}$. An automorphism $\varphi$ maps each generator to another generator, and the centralizer $C_{B_0(2,5)}(\varphi)$ has order $5^{17}$. The authors calculate the growth function relative to a minimal generating set, computing the diameter $D_X(C) = 33$ and the average diameter $\bar{D}_X(C) \approx 26.1$. [trans.]

## TL;DR

Computes (by machine) the growth function of the centralizer $C = C_{B_0(2,5)}(\varphi)$ of the **generator-swap** involution $\varphi:\,a_1\mapsto a_2,\ a_2\mapsto a_1$ of the maximal finite two-generator Burnside group $B_0(2,5)$ (order $5^{34}$), with respect to its minimal 3-element generating set $X=\{x_1,x_2,x_3\}$. Result (Corollary): **Cayley diameter $D_X(C)=33$, average diameter $\bar D_X(C)\approx 26.1$**. The centralizer facts $|C|=5^{17}$, solvability length 3, nilpotency length 6, minimum 3 generators are taken from [[kuznetsov-filippov-2010-vmj]]; the BFS growth algorithm is [[kuznetsov-2016]] and fast multiplication uses the Hall polynomials of [[kuznetsov-kuznetsova-2013]]. By Shunkov's theorem, finiteness of $C_{B(2,5)}(\varphi)$ would force $B(2,5)$ itself finite — motivating the study.

## Problem

For a group $G=\langle X\rangle$ the ball $K_s$ of radius $s$ is the set of elements expressible as words over $X$ of length $\le s$; the growth function is $F(0)=|K_0|=1$, $F(s)=|K_s|-|K_{s-1}|$ for $s\in\mathbb N$. The Cayley diameter is the largest $s_0$ with $F(s_0)>0$ (denoted $D_X(G)$) and the average diameter is $\bar D_X(G)=\frac1{|G|}\sum_{s=0}^{s_0} s\,F(s)$. Computing the growth function of a large finite group is hard: finding a minimal word for a group element is NP-hard (Even–Goldreich), so in the worst case the work is exponential in $|X|$.

$B(2,5)=\langle a_1,a_2\rangle$ is the free two-generator Burnside group of exponent 5; whether it is finite or infinite is open. $B_0(2,5)=\langle a_1,a_2\rangle$ is the maximal *finite* quotient, $|B_0(2,5)|=5^{34}$ [Havas–Wall–Wamsley]; if $B(2,5)$ is finite then $B_0(2,5)=B(2,5)$. Computing the growth function of $B_0(2,5)$ itself w.r.t. a minimal generating set is currently infeasible — $5^{34}=582076609134674072265625\approx 5\cdot10^{23}$; to date only growth functions of quotients of order $\le 5^{17}$ have been obtained [[[kuznetsov-2016]]]. This paper computes the growth function of one such subgroup, the involution-centralizer $C$.

## Approach

- **The automorphism (verbatim).** $\varphi:\,a_1\to a_2,\ a_2\to a_1$ — the swap of the two generators. It is an involutive automorphism of both $B(2,5)$ and $B_0(2,5)$ (see [[kuznetsov-filippov-2010-vmj]]).
- **Finiteness motivation.** By V. P. Shunkov's theorem [7], if $C_{B(2,5)}(\varphi)$ is finite then $B(2,5)$ is finite; equivalently, if $C_{B(2,5)}(\varphi)=C_{B_0(2,5)}(\varphi)$ then $B(2,5)=B_0(2,5)$. Hence studying the growth of $C:=C_{B_0(2,5)}(\varphi)$ is of interest.
- **Centralizer structure (from [[kuznetsov-filippov-2010-vmj]], ref [6]).** (1) $|C|=5^{17}$; (2) solvability length 3, nilpotency length 6; (3) minimum number of generators is 3.
- **Computation.** The growth function of $C$ w.r.t. the minimal generating set $X=\{x_1,x_2,x_3\}$ is computed by the BFS algorithm of [[kuznetsov-2016]] (ref [5]); elements are multiplied fast via the Hall polynomials of [[kuznetsov-kuznetsova-2013]] (ref [8]). Implemented in C++ parallelised with **OpenMP**, run on an 8-core / 64 GB Linux machine (gcc); wall time $\approx 36$ hours.

## Key result

**Corollary (verbatim).** $D_X(C) = 33$, $\ \bar D_X(C) \approx 26.1$.

- $C = C_{B_0(2,5)}(\varphi)$ for the generator-swap involution $\varphi:a_1\leftrightarrow a_2$, with $|C|=5^{17}$.
- **Cayley diameter** (w.r.t. minimal $X=\{x_1,x_2,x_3\}$): $D_X(C) = \mathbf{33}$.
- **Average diameter**: $\bar D_X(C) \approx \mathbf{26.1}$.

## Assumptions

- The structural facts $|C|=5^{17}$, solvability 3, nilpotency 6, min 3 generators are imported from [[kuznetsov-filippov-2010-vmj]]; not re-derived here.
- Word equality decided by pc-reduction; multiplication correct via the Hall-polynomial oracle [[kuznetsov-kuznetsova-2013]].
- $X=\{x_1,x_2,x_3\}$ is a minimal generating set of $C$.

## Limitations / scope

- Conference supplement (3 pp): the growth function table itself is summarised only by its two derived scalars $D_X$ and $\bar D_X$; the full $F(s)$ table is not printed.
- Result is for the order-$5^{17}$ centralizer, not for $B_0(2,5)$ (order $5^{34}$), which remains out of reach.

## Replication evidence

No independent replication known. The values $D_X(C)=33$, $\bar D_X(C)\approx26.1$ rest on the centralizer structure of [[kuznetsov-filippov-2010-vmj]] and the growth-function pipeline of [[kuznetsov-2016]] + [[kuznetsov-kuznetsova-2013]].

## Why this paper matters

This is the largest single subgroup of $B_0(2,5)$ whose full Cayley geometry has been computed in the Kuznetsov line: the order-$5^{17}$ centralizer of the generator-swap involution, with diameter 33 and average diameter $\approx26.1$. It also carries the sharpest theoretical stake in the program — Shunkov's theorem makes the *finiteness* of this centralizer equivalent (in the relevant sense) to the finiteness of the free Burnside group $B(2,5)$, one of the central open problems.

Contrast with the **inversion** automorphism $a_i\mapsto a_i^{-1}$ studied in [[kuznetsov-safonov-2018]] (centralizer order $5^{16}$): these are two *different* involutions of $B_0(2,5)$ with different centralizers ($5^{17}$ vs $5^{16}$), so the papers are complementary, not duplicates.

## Quotes

1. > "Consider the mapping $\varphi$ of the form $\varphi: a_1\to a_2,\ a_2\to a_1$." — §body [trans.]
2. > "By V. P. Shunkov's theorem, if $C_{B(2,5)}(\varphi)$ turns out to be a finite group, then the group $B(2,5)$ is also finite." — §body [trans.]
3. > "Corollary. $D_X(C) = 33$, $\bar D_X(C) \approx 26.1$." — §Results of computer computations [trans.]

## Open questions surfaced

- The full growth-function table $F(s)$ of $C$ is not printed here — only the diameter and average diameter. Where is the tabulated $F(s)$ (if published)?
- How does $\bar D_X(C)\approx26.1$ (order $5^{17}$) compare with the average diameters of the $B_0(2,5)$ *quotients* $B_k$ of comparable order in [[kuznetsov-2016]]?

## Related material in vault

- Extends: [[kuznetsov-filippov-2010-vmj]] (structure of the generator-swap centralizer $C$: $|C|=5^{17}$, solvability 3, nilpotency 6, 3 generators — ref [6])
- Cites: [[kuznetsov-2016]] (growth-function BFS algorithm, ref [5]), [[kuznetsov-kuznetsova-2013]] (Hall-polynomial fast multiplication, ref [8]), [[havas-wall-wamsley-1974]] (order $5^{34}$ of $B_0(2,5)$, ref [4])
- Related: [[kuznetsov-safonov-2018]] (Cayley graph of the centralizer of the *different*, inversion automorphism $a_i\mapsto a_i^{-1}$; $|C|=5^{16}$)
- MOC: [[Research/Group theory/_MOCs/_moc-burnside]]

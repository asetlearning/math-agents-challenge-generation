---
title: "On the growth functions of finite two generator Burnside groups of exponent five"
authors: A. A. Kuznetsov, S. S. Karchevsky
year: 2016
venue: Prikladnaya Diskretnaya Matematika. Supplement
url: https://doi.org/10.17223/2226308X/9/52
url_fulltext: "https://www.mathnet.ru/php/getFT.phtml?jrnid=pdma&paperid=285&what=fullt&option_lang=eng"
url_translated:
language: ru
methodology_type: empirical
domain: group-theory
status: draft
citation_count: null
citation_count_date:
key_concepts:
  - "[[growth-function]]"
  - "[[cayley-diameter]]"
  - "[[power-commutator-presentation]]"
extends:
  - "[[kuznetsova-kuznetsov-safonov-2013]]"
contradicts: []
replicates:
  - "[[kuznetsov-2016]]"
cites:
  - "[[havas-wall-wamsley-1974]]"
  - "[[kuznetsova-kuznetsov-safonov-2013]]"
  - "[[kuznetsov-kuznetsova-2013]]"
cited_by: []
quality_notes: "4-page conference note (Prikl. Diskr. Mat. Suppl. 9, pp. 132–135, DOI 10.17223/2226308X/9/52). Original in Russian. RE-FILLED FROM FULL TEXT (mathnet getFT PDF, pdftotext — Cyrillic renders correctly). This is the short PDMA-supplement companion to the full journal paper [[kuznetsov-2016]] (same first author, same year, same k=15,16,17 growth-function computation on the same 4-CPU×16-core/256 GB machine). Content overlap: same Bk=B0(2,5)/⟨a_{k+1},…,a_34⟩ setup, same 'new element-ordering method' (the base-5 index of [[kuznetsov-2016]]), and a diameter table. DIFFERENCE from the journal paper: this note gives ONLY the diameters D_A2, D_A4 (no average diameters, no A-I complexity theorems, no algorithm listing). Its D_A2 column (8,10,13,20,20,25,30,31,32,35,40,40,45,46,50,55 for k=2..17) and D_A4 column (4,6,9,10,13,15,19,20,20,24,26,28,30,30,33,34) are IDENTICAL to the journal paper's — so this is a replicate/announcement, not a distinct result. It cites the base algorithm as [7]=[[kuznetsova-kuznetsov-safonov-2013]] (the parallel growth algorithm) and the multiplication oracle as [8]=[[kuznetsov-kuznetsova-2013]]. NOTE: the source PDMA-supplement PDF interleaves a preceding MD5-collision/SAT note; only pp. 132–135 is this paper."
fill_level: full
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/b25
  - topic/restricted-burnside
  - topic/growth-functions
  - topic/exponent-5
  - paper
  - status/draft
project: b25
---

# On the growth functions of finite two generator Burnside groups of exponent five

> **Translation note**: source paper is in Russian (`language: ru`). Abstract below is translated to English [trans.] from the mathnet.ru record.

## Abstract

The researchers examine the largest two-generator Burnside group of exponent 5, denoted $B_0(2,5)$, which has order $5^{34}$. Using a power commutator presentation, each group element is uniquely represented with 34 generators (the first two being standard generators, the remainder being recursively defined commutators). They define quotient groups $B_k$ with order $5^k$ and present a new algorithm for computing the growth function of $B_k$ relative to two different generating sets, calculating growth functions for $k = 15, 16, 17$. [trans.]

## TL;DR

Short PDMA-supplement note reporting the **growth functions and Cayley diameters** of the quotients $B_k=B_0(2,5)/\langle a_{k+1},\dots,a_{34}\rangle$ (order $5^k$) for $k=15,16,17$, under both $A_2=\{a_1,a_2\}$ and $A_4=\{a_1,a_1^{-1},a_2,a_2^{-1}\}$. It uses the parallel BFS algorithm of [[kuznetsova-kuznetsov-safonov-2013]] as the base, the Hall-polynomial oracle of [[kuznetsov-kuznetsova-2013]] for fast multiplication, and a "new element-ordering method" (the base-5 indexing of the full paper [[kuznetsov-2016]]), run on a 64-core / 256 GB machine. The diameter table it reports is **identical** to that in the full journal paper [[kuznetsov-2016]] — so this is the companion announcement of the same computation, giving only diameters (no average diameters, no complexity analysis).

## Problem

Same as [[kuznetsov-2016]]: for $G=\langle X\rangle$ the ball $K_s$ collects words of length $\le s$; the growth function is $F(0)=1$, $F(s)=|K_s|-|K_{s-1}|$, with $D_X(G)=s_0$ (largest nonzero index) the Cayley diameter. Computing $F$ is decidable but hard (minimal-word is NP-hard, Even–Goldreich). Prior work reached only $B_{14}$ (Filippov for $A_2$, Sims for $A_4$). Push past the $k=14$ barrier for the quotients of $B_0(2,5)$ (order $5^{34}$), motivated by the open finiteness problem of the free $B(2,5)$.

## Approach

Base algorithm from [[kuznetsova-kuznetsov-safonov-2013]] (parallel growth-function BFS). Fast multiplication via the Hall polynomials of [[kuznetsov-kuznetsova-2013]]. A "new method of ordering elements" (the base-5 exponent index + boolean array detailed in the full paper [[kuznetsov-2016]]) significantly raises throughput. Implemented on a 4-CPU × 16-core (64-core), 256 GB shared-memory machine, computing $F$ for $B_{15},B_{16},B_{17}$ under $A_2$ and $A_4$.

## Key result

Growth functions of $B_{15},B_{16},B_{17}$ for both generating sets (plotted as Figs 1–2), plus a verbatim table of Cayley diameters for $k=2..17$:

| $k$ | $D_{A_2}(B_k)$ | $D_{A_4}(B_k)$ |
|---|---|---|
| 2 | 8 | 4 |
| 3 | 10 | 6 |
| 4 | 13 | 9 |
| 5 | 20 | 10 |
| 6 | 20 | 13 |
| 7 | 25 | 15 |
| 8 | 30 | 19 |
| 9 | 31 | 20 |
| 10 | 32 | 20 |
| 11 | 35 | 24 |
| 12 | 40 | 26 |
| 13 | 40 | 28 |
| 14 | 45 | 30 |
| 15 | 46 | 30 |
| 16 | 50 | 33 |
| 17 | 55 | 34 |

This is identical to the diameter columns of [[kuznetsov-2016]] (which additionally reports the average diameters $\overline{D}_{A_2},\overline{D}_{A_4}$).

## Assumptions

- $B_0(2,5)$ finite of order $5^{34}$ (Havas–Wall–Wamsley [[havas-wall-wamsley-1974]]); $|B_k|=5^k$.
- Hall-polynomial multiplication [[kuznetsov-kuznetsova-2013]] and parallel BFS [[kuznetsova-kuznetsov-safonov-2013]] correct; boolean-index memory feasible to $k=17$ on 256 GB.

## Limitations / scope

- Supplement scope: diameters only, no average diameters, no algorithm/complexity details (those are in [[kuznetsov-2016]]).
- Reached $k=17$; larger $k$ hits the memory wall (addressed by [[kuznetsov-kuznetsova-2018]]).

## Replication evidence

The diameter table matches [[kuznetsov-2016]] exactly (self-consistent replicate). The $A_4$/$k\le14$ values agree with Sims and Filippov's earlier results.

## Why this paper matters

This is the compact companion publication of the k=15,16,17 growth-function milestone, with Karchevsky as co-author (likely the parallel-implementation contributor). For the vault its value is corroborative: it confirms the same diameter data as [[kuznetsov-2016]] and pins the base algorithm to [[kuznetsova-kuznetsov-safonov-2013]] and the multiplication oracle to [[kuznetsov-kuznetsova-2013]].

## Quotes

1. > "In this work the growth functions of $B_k$ relative to the generating sets $\{a_1,a_2\}$ and $\{a_1,a_1^{-1},a_2,a_2^{-1}\}$ for $k=15,16,17$ are computed." — Abstract [trans.]
2. > "A new method of ordering elements was introduced, which allowed a significant increase in performance." — §body [trans.]

## Open questions surfaced

- Same as [[kuznetsov-2016]]: exact numeric $F(s)$ tables (given only as graphs); reason for the irregular $D_{A_2}$ jumps.

## Related material in vault

- Extends: [[kuznetsova-kuznetsov-safonov-2013]] (base parallel BFS growth algorithm)
- Replicates: [[kuznetsov-2016]] (full journal paper — same k=15,16,17 diameter table; this note is its short companion)
- Cites: [[havas-wall-wamsley-1974]] (order-$5^{34}$ presentation), [[kuznetsova-kuznetsov-safonov-2013]], [[kuznetsov-kuznetsova-2013]] (Hall-polynomial oracle)
- Related: [[kuznetsov-kuznetsova-2018]] (resource-efficient extension to k=18,19)
- MOC: [[Research/Group theory/_MOCs/_moc-burnside]]

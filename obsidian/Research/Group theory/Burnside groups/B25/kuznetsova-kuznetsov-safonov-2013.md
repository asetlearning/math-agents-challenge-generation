---
title: "A parallel algorithm for computation of growth functions in the finite two-generator groups of period 5"
authors: A. S. Kuznetsova, A. A. Kuznetsov, K. V. Safonov
year: 2013
venue: Prikladnaya Diskretnaya Matematika. Supplement
url: http://mi.mathnet.ru/pdma100
url_fulltext: "https://www.mathnet.ru/php/getFT.phtml?jrnid=pdma&paperid=100&what=fullt&option_lang=eng"
url_translated:
language: ru
methodology_type: methodology
domain: group-theory
status: draft
citation_count: null
citation_count_date:
key_concepts:
  - "[[Concepts/growth-functions-burnside]]"
  - "[[cayley-diameter]]"
  - "[[power-commutator-presentation]]"
extends:
  - "[[kuznetsov-kuznetsova-2013]]"
contradicts: []
replicates: []
cites:
  - "[[kuznetsov-kuznetsova-2013]]"
cited_by: []
quality_notes: "3-page conference note (Prikl. Diskr. Mat. Suppl. 6, pp. 119–121). Original in Russian. RE-FILLED FROM FULL TEXT (mathnet getFT PDF, pdftotext). The full text is far richer than the one-sentence abstract: it gives (a) the complete SEQUENTIAL growth-function/Cayley-diameter BFS algorithm (steps 1–6, verbatim below), (b) the PARALLELIZATION scheme (partition the minimal-word set Q_s into p^r disjoint classes indexed by fixing the first r pc-exponents γ1..γr; r tuned to the multiprocessor system), and (c) a TABLE of orders and Cayley diameters D_k(A) for k=1..6 w.r.t. A={a1,a2}: k=1:(5^2,8), k=2:(5^3,10), k=3:(5^5,20), k=4:(5^8,30), k=5:(5^10,32), k=6:(5^14,45). The next open case is k=7 (B0(2,5,7) order 5^18), requiring supercomputing — a C++/MPI implementation was in progress for the Siberian Federal University supercomputer. First author is A.S. Kuznetsova (implemented the parallel variant), not A.A. Kuznetsov. NOTE: the source PDF page interleaves two neighboring PDMA-supplement articles (a Pollard-factoring note before, a pipelining note after); only the middle article is this paper."
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
  - topic/finite-group-enumeration
  - paper
  - status/draft
project: b25
---

# A parallel algorithm for computation of growth functions in the finite two-generator groups of period 5

> **Translation note**: source paper is in Russian (`language: ru`). Abstract below is translated to English [trans.] from the mathnet.ru record.

## Abstract

A parallel version of the algorithm for computing growth functions in finite two-generator groups of period 5 is presented. Keywords: group growth function, Cayley diameter, parallel algorithm. [trans.]

## TL;DR

Conference note giving (1) the full **sequential BFS** that enumerates the minimal words of $G = B_0(2,5,k)$ to produce its **growth function** and **Cayley diameter**, (2) a **parallelization** that partitions the minimal-word set $Q_s$ into $p^r$ disjoint classes (indexed by fixing the first $r$ pc-exponents $\gamma_1,\dots,\gamma_r$), and (3) a **table** of orders and diameters $D_k(A)$ for $k=1..6$ w.r.t. $A=\{a_1,a_2\}$. The next open case is $k=7$ ($|B_0(2,5,7)|=5^{18}$), needing a supercomputer; a C++/MPI version was in progress for the SFU supercomputer. Built on the fast-multiplication oracle of [[kuznetsov-kuznetsova-2013]].

## Problem

For $G$ a finite $p$-group of exponent $p$, its nilpotency gives a central series $G=G_1\supset G_2\supset\dots\supset G_{n+1}=e$ with $|G_i/G_{i+1}|=p$; choosing $a_i\in G_i\setminus G_{i+1}$, every $g\in G$ is a unique pc-word $g=a_1^{\gamma_1}\cdots a_n^{\gamma_n}$, $0\le\gamma_i<p$ (obtainable via the $p$-quotient algorithm in GAP/Magma). To get the **growth function** and **Cayley diameter** of $G$ w.r.t. a generating set $A$ one must enumerate all elements as **minimal words**: counting words of each length gives the growth function, and the maximum minimal-word length is the Cayley diameter. This BFS becomes a bottleneck for large $k$ (over $B_0(2,5,k)$, which has $5^k$-scale order). Can it be parallelized to reach larger quotients?

## Approach

**Sequential algorithm** (verbatim, computing the growth function of $G$ w.r.t. $A=\{a_1,\dots,a_m\}$; $K_s(G)$ = minimal words of length $\le s$, $Q_s(G)$ = their pc-normal forms):
1. $s=0$, $K_0=\{e\}$, $Q_0=\{a_1^0\cdots a_n^0\}$, $T=K_0$.
2. $s=s+1$, $K_s=K_{s-1}$, $Q_s=Q_{s-1}$, $V=a_1T\cup\cdots\cup a_m T$, $T=\emptyset$, $i=1$.
3. For $v_i\in V$, reduce $v_i \xrightarrow{pq} \hat v_i$. If $\hat v_i\notin Q_s$: $K_s=K_s\cup\{v_i\}$, $Q_s=Q_s\cup\{\hat v_i\}$, $T=T\cup\{v_i\}$.
4. If $i<|V|$: $i=i+1$, go to 3; else go to 5.
5. If $T\ne\emptyset$, go to 2; else go to 6.
6. Diameter of $G$ is $s-1$; $K_{s-1}(G)$ is the set of all minimal words. Growth function $f(j)=|K_j(G)|-|K_{j-1}(G)|$, $1\le j\le s-1$.

**Parallelization.** Partition $Q_s$ into $p^r$ pairwise-disjoint classes, each determined by a fixed tuple of leading pc-exponents $\gamma_1,\dots,\gamma_r$. The parameter $r$ is chosen experimentally, depending on the multiprocessor system. (Word-equality tests via the pc-reduction, using the fast Hall-polynomial multiplication of [[kuznetsov-kuznetsova-2013]].)

## Key result

Verbatim table of orders and Cayley diameters $D_k(A)$ of $B_0(2,5,k)$ w.r.t. $A=\{a_1,a_2\}$, for $k=1..6$ (growth functions for $k\ge2$ computed by machine):

| $k$ | $\lvert B_0(2,5,k)\rvert$ | $D_k(A)$ |
|---|---|---|
| 1 | $5^{2}$ | 8 |
| 2 | $5^{3}$ | 10 |
| 3 | $5^{5}$ | 20 |
| 4 | $5^{8}$ | 30 |
| 5 | $5^{10}$ | 32 |
| 6 | $5^{14}$ | 45 |

The largest group in the family is $B_0(2,5,12)$ of order $5^{34}$. **Next open case:** $k=7$, $|B_0(2,5,7)|=5^{18}$ — large enough to require supercomputing. A C++/MPI implementation of the parallel algorithm was in progress, targeting the Siberian Federal University supercomputer.

## Assumptions

- $B_0(2,5,k)$ has a pc-presentation from the $p$-quotient algorithm; $A=\{a_1,a_2\}$ generates.
- Word equality is decided by pc-reduction; multiplication uses [[kuznetsov-kuznetsova-2013]].
- Parallel decomposition into $p^r$ exponent-classes is load-balanced by tuning $r$ to the hardware.

## Limitations / scope

- Conference supplement (3 pp); the parallel implementation ($k=7$) was still in progress at publication — no speedup figures or $k=7$ diameter are reported here.
- Diameters given only through $k=6$.

## Replication evidence

The diameters through $k=6$ are consistent with the broader Kuznetsov growth-function program. Extended by [[kuznetsov-kuznetsova-2018]] (resource-efficient algorithm reaching larger $k$).

## Why this paper matters

This is the earliest parallelization in the Kuznetsov growth-function line. It pins down the concrete state of the art at the time — Cayley diameters of $B_0(2,5,k)$ for $k\le6$ (8, 10, 20, 30, 32, 45) — and identifies $k=7$ ($5^{18}$) as the supercomputing frontier. The class-partition parallelization ($Q_s$ split by leading pc-exponents) is the decomposition later scaled up in the 2018 resource-efficient work.

## Quotes

1. > "For $k\le6$ the growth functions and Cayley diameters of the groups $B_0(2,5,k)$ w.r.t. $A$ have been computed to date." — §body [trans.]
2. > "The next unsolved case is $k=7$. Since $B_0(2,5,7)$ has a sufficiently large order ($5^{18}$), supercomputer computations are required to find the diameter of this group." — §body [trans.]

## Open questions surfaced

- Was the $k=7$ ($5^{18}$) Cayley diameter subsequently computed? (Follow-up in the later Kuznetsov papers, e.g. [[kuznetsov-kuznetsova-2018]].)
- What parallel speedup / optimal $r$ did the C++/MPI SFU-supercomputer implementation achieve?

## Related material in vault

- Extends: [[kuznetsov-kuznetsova-2013]] (sequential fast-multiplication algorithm; parallel version built on top)
- Related: [[kuznetsov-kuznetsova-2018]] (later resource-efficient approach reaching k=18,19)
- MOC: [[Research/Group theory/_MOCs/_moc-burnside]]

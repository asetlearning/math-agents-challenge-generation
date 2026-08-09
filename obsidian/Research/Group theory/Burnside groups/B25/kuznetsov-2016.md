---
title: "An algorithm for computation of the growth functions in finite two-generated groups of exponent 5"
authors: A. A. Kuznetsov
year: 2016
venue: Prikladnaya Diskretnaya Matematika
url: https://doi.org/10.17223/20710410/33/10
url_fulltext: "https://www.mathnet.ru/php/getFT.phtml?jrnid=pdm&paperid=554&what=fullt&option_lang=eng"
url_translated:
language: ru
methodology_type: methodology
domain: group-theory
status: draft
citation_count: null
citation_count_date:
key_concepts:
  - "[[growth-function]]"
  - "[[cayley-diameter]]"
  - "[[power-commutator-presentation]]"
  - "[[hall-polynomials]]"
extends:
  - "[[kuznetsov-kuznetsova-2013]]"
contradicts: []
replicates: []
cites:
  - "[[havas-wall-wamsley-1974]]"
  - "[[kuznetsov-kuznetsova-2013]]"
  - "[[kuznetsov-2015-cayley-exp3]]"
cited_by: []
quality_notes: "Full journal paper (Prikl. Diskr. Mat. 3(33), pp. 116–125, 10 pages, DOI 10.17223/20710410/33/10). Original in Russian, English abstract. RE-FILLED FROM FULL TEXT (mathnet getFT PDF, pdftotext — Cyrillic renders correctly). The full text is far richer than the abstract: it gives (a) the base growth-function algorithm A-I (verbatim BFS, steps 1–12) with a full COMPLEXITY ANALYSIS — Lemmas 1–3, Theorem 1: T(|G|)∈Ω(|G|²) and ∈O(|X|·|G|²), Corollaries T∈Θ(|G|²) if |X|≪|G|, T∈O(|G|³) if |X|∼|G|; (b) the KEY MODIFICATION for Bk: a bijection φ:g↦n_g (base-5 index) + a boolean vector V of size 5^k replacing the set-membership test, giving Theorem 2: T(|Bk|)∈Θ(|Bk|) (linear!); (c) a multiplication optimization — 'third method' uses 5 Hall-polynomial variants selected by the exponent α1, shown fastest (Fig. 1); (d) a full TABLE of Cayley diameters D and average diameters for A2={a1,a2} and A4={a1,a1⁻¹,a2,a2⁻¹}, k=2..17; (e) implementation: C++ on a 4-CPU×16-core, 256 GB shared-memory machine; runtimes ≈1 h (k=15), 5 h (k=16), ≈1 day (k=17). Growth functions plotted (Figs 2–7) but the numeric F(s) tables are given only as graphs. Ties to the finiteness problem of B(2,5): if B(2,5) is finite then B34=B(2,5), but 5^34≈5·10^23 makes B34 out of reach. Prior state of the art: Filippov computed B14 growth for A2; Sims for A4 (using a length-preserving automorphism trick cutting to 1/16 of elements). NOT a duplicate of [[kuznetsov-karchevsky-2016]]: that PDMA-supplement note is the parallel/shortened companion; this is the full algorithmic paper."
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

# An algorithm for computation of the growth functions in finite two-generated groups of exponent 5

> **Translation note**: source paper is in Russian (`language: ru`). Abstract below is translated to English [trans.] from the mathnet.ru record.

## Abstract

The paper presents a computational method for analyzing the largest 2-generator Burnside group of exponent 5, denoted $B_0(2,5)$, which has order $5^{34}$. Using a power commutator representation where elements are expressed uniquely as products of 34 generators and commutators, the author develops an algorithm to compute growth functions for quotient groups $B_k$ (having order $5^k$). The growth functions of $B_k$ relative to generating sets $\{a_1, a_2\}$ and $\{a_1, a_1^{-1}, a_2, a_2^{-1}\}$ for $k = 15, 16, 17$ were calculated using this new approach. [trans.]

## TL;DR

Presents an efficient algorithm for the **growth functions** (hence Cayley diameters) of the quotients $B_k=B_0(2,5)/\langle a_{k+1},\dots,a_{34}\rangle$ (order $5^k$) of the restricted Burnside group $B_0(2,5)$ (order $5^{34}$). Starting from the classical BFS growth algorithm A-I — for which the paper proves a **complexity bound** $T(|G|)\in\Omega(|G|^2)\cap O(|X|\cdot|G|^2)$ — it introduces the key modification for $B_k$: index each element $g=a_1^{\alpha_1}\cdots a_k^{\alpha_k}$ by the base-5 integer $n_g=\alpha_1\alpha_2\dots\alpha_k$ and use a **boolean array $V$ of size $5^k$** instead of a set-membership test, dropping the complexity to **linear $T(|B_k|)\in\Theta(|B_k|)$**. With a Hall-polynomial multiplication oracle (fastest variant: 5 polynomial sets selected by the leading exponent $\alpha_1$), it computes the growth functions of $B_{15},B_{16},B_{17}$ for $A_2=\{a_1,a_2\}$ and $A_4=\{a_1,a_1^{-1},a_2,a_2^{-1}\}$ on a 64-core / 256 GB machine ($\approx$1 h, 5 h, $\approx$1 day). Reports a full Cayley-diameter table for $k=2..17$.

## Problem

For $G=\langle X\rangle$, the ball $K_s$ is all elements expressible as words of length $\le s$; the growth function is $F(0)=1$, $F(s)=|K_s|-|K_{s-1}|$. Its largest nonzero index $s_0$ is the Cayley diameter $D_X(G)$, and $\overline{D}_X(G)=\frac{1}{|G|}\sum_{s} s\,F(s)$ the average diameter. Computing $F$ for a large finite group is decidable but hard — finding a minimal word is NP-hard (Even–Goldreich). For $B_0(2,5)=\langle a_1,a_2\rangle$ (order $5^{34}$) and its quotients $B_k$ (order $5^k$), prior work reached only $B_{14}$ (Filippov for $A_2$; Sims for $A_4$, using a length-preserving automorphism trick cutting to $1/16$ of elements). Push past $k=14$ despite the huge orders.

## Approach

1. **Base algorithm A-I (verbatim).** BFS from $e$: at step $s$, form $K_s=K_{s-1}$; for all $x\in X,\ p\in P$ set $g=x\cdot p$; if $g\notin K_s$, add it; $P=K_s\setminus K_{s-1}$; $F(s)=|P|$; repeat while $F(s)>0$; on termination $D_X=s_0$, $\overline{D}_X=\frac{1}{|K_{s_0}|}\sum_s sF(s)$.
2. **Complexity of A-I.** Lemma 2: exactly $|X|\cdot|G|$ words are computed/checked. Lemma 3 bounds the number of $g\notin K_s$ tests between $\sim\tfrac12|G|^2$ and $\sim(|X|-\tfrac12)|G|^2$. **Theorem 1:** $T(|G|)\in\Omega(|G|^2)$ and $\in O(|X|\cdot|G|^2)$; Corollaries: $\Theta(|G|^2)$ if $|X|\ll|G|$, $O(|G|^3)$ if $|X|\sim|G|$.
3. **Modification for $B_k$.** (i) Multiplication: use Hall polynomials [[kuznetsov-kuznetsova-2013]] (≥1 order of magnitude faster than collection); the "third method" keeps **5 polynomial variants indexed by $\alpha_1$** and is fastest (Fig. 1). (ii) Membership: bijection $\varphi:g\mapsto n_g$ where $n_g=\alpha_1\dots\alpha_k$ is $g$'s exponent-vector read as a base-5 integer ($0\le n_g<5^k$); keep a boolean vector $V$ of length $5^k$ and replace the $g\notin K_s$ test by "if $V_{n_g}=0$ then $V_{n_g}:=1$, add $g$". **Theorem 2:** $T(|B_k|)\in\Theta(|B_k|)$. Step 5 (the products) parallelizes trivially.
4. **Implementation.** C++ on a 4-CPU × 16-core (64-core), 256 GB shared-memory machine.

## Key result

Growth functions of $B_k$ for $k=15,16,17$ computed for both $A_2=\{a_1,a_2\}$ and $A_4=\{a_1,a_1^{-1},a_2,a_2^{-1}\}$ (plotted as Figs 2–7). Runtimes: $\approx$1 h ($k=15$), 5 h ($k=16$), $\approx$1 day ($k=17$). Full **Cayley-graph characteristics** table (diameter $D$ and average diameter $\overline{D}$, rounded), verbatim, for $k=2..17$:

| $k$ | $D_{A_2}(B_k)$ | $\overline{D}_{A_2}(B_k)$ | $D_{A_4}(B_k)$ | $\overline{D}_{A_4}(B_k)$ |
|---|---|---|---|---|
| 2 | 8 | 4 | 4 | 2 |
| 3 | 10 | 6 | 6 | 4 |
| 4 | 13 | 8 | 9 | 5 |
| 5 | 20 | 12 | 10 | 7 |
| 6 | 20 | 14 | 13 | 9 |
| 7 | 25 | 16 | 15 | 10 |
| 8 | 30 | 20 | 19 | 13 |
| 9 | 31 | 22 | 20 | 14 |
| 10 | 32 | 24 | 20 | 15 |
| 11 | 35 | 27 | 24 | 17 |
| 12 | 40 | 29 | 26 | 19 |
| 13 | 40 | 31 | 28 | 21 |
| 14 | 45 | 34 | 30 | 22 |
| 15 | 46 | 36 | 30 | 23 |
| 16 | 50 | 39 | 33 | 26 |
| 17 | 55 | 42 | 34 | 27 |

(The $A_2$ diameters $k\le6$ — 8,10,13,20,20,25 — extend the earlier $k\le6$ table of [[kuznetsova-kuznetsov-safonov-2013]]; note the $k=4$ value here is 13, and $k=6$ is 20.)

## Assumptions

- $B_0(2,5)$ finite of order $5^{34}$ (Havas–Wall–Wamsley [[havas-wall-wamsley-1974]]); quotients $B_k=B_0(2,5)/\langle a_{k+1},\dots,a_{34}\rangle$ have order $5^k$.
- Hall-polynomial multiplication [[kuznetsov-kuznetsova-2013]] is the group oracle; boolean-array indexing needs $5^k$ bits of RAM (feasible to $k=17$ on 256 GB).
- Elementary group ops cost $\Theta(1)$ for the asymptotic bounds.

## Limitations / scope

- Reached $k=17$; the boolean array of size $5^{17}\approx7.6\times10^{11}$ is the memory wall — pushing to $k=18,19$ needed the resource-efficient variant [[kuznetsov-kuznetsova-2018]].
- Full $B_{34}=B_0(2,5)$ ($5^{34}\approx5\times10^{23}$) remains far out of reach.
- Numeric $F(s)$ given as graphs (Figs 2–7), not tables; the diameter table is exact.

## Replication evidence

No independent replication. The $A_4$/$k\le14$ values are consistent with Sims and Filippov's earlier computations; the $A_2$ diameters for $k\le6$ agree with [[kuznetsova-kuznetsov-safonov-2013]]. Extended by [[kuznetsov-kuznetsova-2018]].

## Why this paper matters

This is the algorithmic core of Kuznetsov's B(2,5) growth-function program. Two contributions matter most: (1) a **rigorous complexity analysis** of the standard BFS growth algorithm (Ω(|G|²)/O(|X||G|²)) — a gap the author notes was undocumented even in GAP; (2) the **$\Theta(|B_k|)$ linear-time modification** via base-5 indexing + boolean array, which is exactly what breaks the $k=14$ barrier and pushes to $k=17$. The k=15,16,17 growth data and the $k\le17$ diameter table are the seed benchmarks extrapolated in later work, and the whole line is motivated by the open finiteness problem of the free $B(2,5)$ (if finite, $B_{34}=B(2,5)$).

## Quotes

1. > "It is clearly that $|B_k|=5^k$. A new algorithm for computing the growth function of $B_k$ is created." — Abstract
2. > "$T(|B_k|)\in\Theta(|B_k|)$." — Theorem 2 [trans.]
3. > "If $B(2,5)$ is finite, then $B_{34}=B(2,5)$. However in the foreseeable future computing the growth function of $B_{34}$ is hardly possible, since $5^{34}\approx5\cdot10^{23}$." — §Introduction [trans.]

## Open questions surfaced

- The exact numeric $F(s)$ tables for $B_{15},B_{16},B_{17}$ (given here only as graphs) — the precise seed benchmarks.
- The $A_2$ diameter jumps are irregular (e.g. flat $k=5\to6$ at 20, $k=12\to13$ at 40); is there a structural reason?
- Can the boolean-array memory wall be traded for time to reach $k=18,19$ on the same hardware? (Answered by [[kuznetsov-kuznetsova-2018]].)

## Related material in vault

- Extends: [[kuznetsov-kuznetsova-2013]] (fast Hall-polynomial multiplication — the oracle in step 5)
- Cites: [[havas-wall-wamsley-1974]] (order-$5^{34}$ presentation), [[kuznetsov-kuznetsova-2013]], [[kuznetsov-2015-cayley-exp3]] (exponent-3 Cayley graphs — the motivating cross-exponent comparison)
- Related: [[kuznetsov-karchevsky-2016]] (companion PDMA-supplement note — parallel/short version, NOT identical), [[kuznetsov-kuznetsova-2018]] (resource-efficient extension to k=18,19), [[kuznetsova-kuznetsov-safonov-2013]] (earlier parallel growth algorithm, $k\le6$ diameters)
- MOC: [[Research/Group theory/_MOCs/_moc-burnside]]

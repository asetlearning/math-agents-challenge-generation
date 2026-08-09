---
title: "Computational experiments in finite two generator Burnside groups of exponent five"
authors: A. A. Kuznetsov
year: 2019
venue: Prikladnaya Diskretnaya Matematika. Supplement
url: https://doi.org/10.17223/2226308X/12/60
url_fulltext: "https://www.mathnet.ru/php/getFT.phtml?jrnid=pdma&paperid=475&what=fullt&option_lang=eng"
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
extends:
  - "[[kuznetsov-2016]]"
  - "[[kuznetsov-kuznetsova-2018]]"
contradicts: []
replicates: []
cites:
  - "[[kuznetsov-2016]]"
  - "[[kuznetsov-kuznetsova-2018]]"
  - "[[havas-wall-wamsley-1974]]"
cited_by: []
quality_notes: "3-page conference note (Prikl. Diskr. Mat. Suppl. 12, pp. 216–218, DOI 10.17223/2226308X/12/60). Original in Russian. RE-FILLED FROM FULL TEXT (mathnet getFT PDF, pdftotext — Cyrillic renders cleanly). CORRECTION to prior note: the cited prior work is NOT kuznetsov-shlepkin-2009/2010 — the actual references are [1] = [[kuznetsov-2016]] (base minimal-complexity growth algorithm) and [2] = [[kuznetsov-kuznetsova-2018]] (resource-efficient algorithm, the coset/quotient-summation Algorithm 3), plus [4] = [[havas-wall-wamsley-1974]] and [5] = Sims. Corrected extends/cites accordingly. NEW CONTENT vs prior work: this note reports the diameter table for the previously-uncomputed quotients 20 ≤ k ≤ 25 (D_A4(eN_k) = 38, 39, 41, 44, 44, 46) and Hypothesis 1: D_A4(eN_k) = D_A4(B_k) with |N_k| ∼ |Q_k| ∼ |B_k|^{1/2} for all 2 ≤ k ≤ 34. NOTE: the source PDMA-supplement PDF interleaves neighbouring articles (an MDS-matrix/XOR note before, a pseudo-Boolean-inequalities note after); only the middle article, pp. 216–218, is this paper."
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
  - topic/cayley-graphs
  - topic/exponent-5
  - topic/finite-group-enumeration
  - paper
  - status/draft
project: b25
---

# Computational experiments in finite two generator Burnside groups of exponent five

> **Translation note**: source paper is in Russian (`language: ru`). Abstract below is translated to English [trans.] from the mathnet.ru record. Original text is not preserved; follow `url` for the source.

## Abstract

The paper examines $B_0(2,5)$, the largest two-generator Burnside group of exponent five with order $5^{34}$. Using a power commutator presentation, elements are uniquely represented as $a_1^{\alpha_1} \cdot a_2^{\alpha_2} \cdots a_{34}^{\alpha_{34}}$. The authors define quotient groups $B_k$ and conduct computational experiments, proposing a hypothesis about the diameter $D_{A_4}(B_k)$ relative to symmetric generating set $A_4 = \{a_1, a_1^{-1}, a_2, a_2^{-1}\}$. The hypothesis predicts $D_{A_4}(eN_k) = D_{A_4}(B_k)$ for all $2 \le k \le 34$, where sizes satisfy $|N_k| \sim |Q_k| \sim |B_k|^{1/2}$, verified computationally for $k \le 19$. [trans.]

## TL;DR

Continues the growth-function program on $B_0(2,5)$ (order $5^{34}$) and its quotients $B_k = B_0(2,5)/\langle a_{k+1},\dots,a_{34}\rangle$ ($|B_k|=5^k$). Using the resource-efficient coset-summation algorithm (Algorithm 3 of [[kuznetsov-kuznetsova-2018]]), it observes that "intermediate" growth functions $F(B_k)$ stabilise their increasing/decreasing regions after $\lesssim10\%$ of the group order, and that for $k\le19$ the coset $eN_k$ always contains the maximal-length words. This motivates **Hypothesis 1**: $D_{A_4}(eN_k)=D_{A_4}(B_k)$ for all $2\le k\le34$, with $|N_k|\sim|Q_k|\sim|B_k|^{1/2}$. Reports a **new table** of coset diameters $D_{A_4}(eN_k)$ for $20\le k\le25$. The $k=20$ growth function was still being computed at press time (via Algorithm 3 with $s=20$, $Q=B_{10}$, $N=\langle a_{11},\dots,a_{20}\rangle$).

## Problem

For a quotient $B_k$ (with symmetric generating set $A_4=\{a_1,a_1^{-1},a_2,a_2^{-1}\}$), computing the full growth function $F(B_k)=(F_0,F_1,\dots)$ — where $F_i=|P_i|$ is the sphere of radius $i$ — becomes memory-bound as $k$ grows (each element must be stored). Its Cayley diameter is $D_{A_4}(B_k)=s_0$ where $F_{s_0}>0$, $F_{s_0+1}=0$; the average diameter is $\bar D_{A_4}(B_k)=\frac1{|B_k|}\sum s\,F_s$. **Can the (expensive) full-group diameter be read off from a single coset $eN_k$ of a suitable normal subgroup $N_k$ of half-exponent size** ($|N_k|\sim|B_k|^{1/2}$), which is far cheaper to compute?

## Approach

- **Setup.** $B_0(2,5)=\langle a_1,a_2\rangle$, pc-presentation from GAP; each $g$ is $a_1^{\alpha_1}\cdots a_{34}^{\alpha_{34}}$, $\alpha_i\in\mathbb Z_5$ ($a_3,\dots,a_{34}$ commutators computed recursively from $a_1,a_2$). Quotients $B_k=B_0(2,5)/\langle a_{k+1},\dots,a_{34}\rangle$, $|B_k|=5^k$. Symmetric generating set $A_4=\{a_1,a_1^{-1},a_2,a_2^{-1}\}$.
- **Algorithms recalled** (from [[kuznetsov-2016]] = ref [1] and [[kuznetsov-kuznetsova-2018]] = ref [2]): Algorithm 1 computes the ball $K_s$ of fixed radius (low time complexity but must store every element); Algorithm 2 computes, for a quotient $Q=G/N$ and $q\in Q$, the growth function $F(q)=(F_0(q),\dots,F_{2s}(q))$ of the coset-ball $K_{2s}(q)$; Algorithm 3 sums $F(G)=\sum_{q\in Q}F(q)$ to get the full growth function of the ball $K_{2s}$ of radius $2s$.
- **New observation.** Running Algorithm 3 on $B_{20}$ ($s=20$, $Q=B_{10}$, $N=\langle a_{11},\dots,a_{20}\rangle$): the intermediate (partial-sum) growth functions $F(B_{20})$ preserve their regions of increase and decrease after no more than $10\%$ of the group order is processed (Fig. 1). Experiments for $k\le19$ show the same behaviour, and that the identity coset $eN_k$ always contains the words of maximal length — the basis of the hypothesis.

## Key result

**Hypothesis 1.** $D_{A_4}(eN_k) = D_{A_4}(B_k)$, where $|N_k|\sim|Q_k|\sim|B_k|^{1/2}$. (If true, the diameter of $B_k$ equals the diameter of the single coset $eN_k$.)

**New computational table** — coset diameters $D_{A_4}(eN_k)$ for $20\le k\le25$ (verbatim):

| $k$ | 20 | 21 | 22 | 23 | 24 | 25 |
|---|---|---|---|---|---|---|
| $D_{A_4}(eN_k)$ | 38 | 39 | 41 | 44 | 44 | 46 |

If Hypothesis 1 holds, these equal the true diameters $D_{A_4}(B_k)$ for $20\le k\le25$. (Growth functions of $B_k$ for $k\le19$ were already obtained in [1,2]; this paper pushes the diameter data to $k=25$.)

## Assumptions

- $B_0(2,5)$ has the pc-presentation of order $5^{34}$ ([[havas-wall-wamsley-1974]], ref [4]); $A_4$ generates each $B_k$.
- The coset/quotient decomposition and its complexity are those of [[kuznetsov-kuznetsova-2018]] (Algorithm 3); multiplication uses the Hall-polynomial oracle.
- The hypothesis rests on the empirical fact ($k\le19$) that $eN_k$ contains the maximal-length words — not proven for $k>19$.

## Limitations / scope

- Conference supplement (3 pp): **Hypothesis 1 is stated, not proved**; the $k=20$ growth function was still running at press time.
- Table gives coset diameters $D_{A_4}(eN_k)$, which equal the group diameters $D_{A_4}(B_k)$ only *if* the hypothesis holds.
- Only the symmetric generating set $A_4$ is treated here (not the minimal $A_2$).

## Replication evidence

Consistent with the diameter data of [[kuznetsov-kuznetsova-2018]] (which reports $D_{A_4}(B_{18})=36$, $D_{A_4}(B_{19})=38$ — matching the trend $\dots,38,39,\dots$ at the $k=19\to20$ boundary). The later center paper [[kuznetsov-kuznetsova-2025]] uses the same $A_4$ diameter estimate ($D_{A_4}(B_0(2,5))\approx69$) from this line.

## Why this paper matters

This is the incremental extension of the Kuznetsov growth-function program from the $k\le19$ frontier of [[kuznetsov-kuznetsova-2018]] out to $k=25$, using the coset-summation Algorithm 3. Its methodological payload is **Hypothesis 1**: that a group's Cayley diameter can be recovered from a single coset of a $\sqrt{|G|}$-sized normal subgroup — a would-be sublinear shortcut for diameter computation on the huge $B_0(2,5)$.

For the Mixer: the $|N_k|\sim|B_k|^{1/2}$ hypothesis is exactly the kind of "half-group witness" that would make bidirectional/meet-in-the-middle search on $B_0(2,5)$-quotients tractable — if the maximal-length words really do concentrate in $eN_k$.

## Quotes

1. > "Starting from a certain step (no more than 10% of the group order), the intermediate growth functions $F(B_{20})$ preserve their regions of increase and decrease." — §body [trans.]
2. > "Hypothesis 1. $D_{A_4}(eN_k) = D_{A_4}(B_k)$, where $|N_k|\sim|Q_k|\sim|B_k|^{1/2}$." — §body [trans.]

## Open questions surfaced

- Is Hypothesis 1 provable, or does it fail for some $k>25$? The concentration of maximal-length words in $eN_k$ is only an empirical observation.
- What are the *average* diameters $\bar D_{A_4}(B_k)$ for $20\le k\le25$? Only the (coset) diameters are tabulated here.
- Does the analogous statement hold for the minimal generating set $A_2$?

## Related material in vault

- Extends: [[kuznetsov-2016]] (minimal-complexity base growth algorithm, ref [1]), [[kuznetsov-kuznetsova-2018]] (resource-efficient coset-summation Algorithm 3, ref [2]; supplies the $k\le19$ frontier this paper extends)
- Cites: [[havas-wall-wamsley-1974]] (order $5^{34}$ of $B_0(2,5)$, ref [4])
- Related: [[kuznetsov-2020]] (rewriting-system growth in the same $B_k$), [[kuznetsov-kuznetsova-2025]] (center of $B_0(2,5)$; reuses the $D_{A_4}\approx69$ estimate from this line)
- MOC: [[Research/Group theory/_MOCs/_moc-burnside]]
- Open problem: [[b25-finiteness-11.48-kostrikin]] (broader context for B(2,5) computational work)

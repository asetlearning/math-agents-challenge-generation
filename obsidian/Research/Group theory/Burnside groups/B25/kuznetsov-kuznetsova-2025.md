---
title: "Computation of the center of the Burnside group B₀(2,5)"
authors: A. A. Kuznetsov, A. S. Kuznetsova
year: 2025
venue: Prikladnaya Diskretnaya Matematika. Supplement
url: https://doi.org/10.17223/2226308X/18/58
url_fulltext: "https://www.mathnet.ru/php/getFT.phtml?jrnid=pdma&paperid=730&what=fullt&option_lang=eng"
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
  - "[[kuznetsov-kuznetsova-2018]]"
  - "[[kuznetsov-2016]]"
contradicts: []
replicates: []
cites:
  - "[[havas-wall-wamsley-1974]]"
  - "[[kuznetsov-kuznetsova-2018]]"
  - "[[kuznetsov-2016]]"
cited_by: []
quality_notes: "4-page conference note (Prikl. Diskr. Mat. Suppl. 18, pp. 270–273, DOI 10.17223/2226308X/18/58). Original in Russian. RE-FILLED FROM FULL TEXT (mathnet getFT paperid=730, pdftotext — PDF is Windows-1251 rendered as mojibake but fully readable). CORRECTION to prior note: removed the WRONG kuznetsov-shlepkin-2009/2010 extends+cites (not references in this paper) and the Concepts/cayley-table-closure-algorithm key-concept. Actual references: [1]=Baumslag–Fazio–Nicolosi, [2]=Fazio–Iga–Nicolosi, [3]=Kahrobaei–Noce, [4]=[[havas-wall-wamsley-1974]], [5]=[[kuznetsov-kuznetsova-2018]] (the resource-efficient/QuotientGrowthFunction algorithm), [6]=[[kuznetsov-2016]] (the Ball algorithm). Content: known fact [4] that Z(B0(2,5))=⟨a34⟩ is cyclic of order 5, a34=[a2,a1,a1,a1,a2,a1,a2,a1,a1,a2,a2,a2]. Naive length of a34: 6142 (A4), 15355 (A2). MAZUROV's 2024 question: compute a SHORT central word in A2/A4. Authors solved it in the stronger form — ALL central elements as minimal-length (geodesic) words in A4 — by computing K25(B0) in A4 (modified algorithm [5] with N=⟨a11..a34⟩, Q=B0/N, q=e; partial K50(e)). Verbatim geodesic words for a34,a34²,a34³,a34⁴ in A4 (x=a1,y=a2,X=a1^-1,Y=a2^-1): lengths 47,50,50,47. In A2 (X→x^4,Y→y^4, reduce w^5): lengths 90,100,100,90 (NOT guaranteed minimal). MCS: 128 cores, 1.5 TB RAM, 2 TB disk; words found in first day, ~1 month to confirm minimality. Verified central via GAP + anupq. Intro note: k-dim hypercube = Cayley graph of B(k,2). Corrected extends/cites; key_concepts to growth-function/cayley-diameter/pc-presentation."
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
  - topic/finite-group-enumeration
  - topic/center-of-group
  - paper
  - status/draft
project: b25
---

# Computation of the center of the Burnside group B₀(2,5)

> **Translation note**: source paper is in Russian (`language: ru`). Abstract below is translated to English [trans.] from the mathnet.ru record. Original text is not preserved; follow `url` for the source.

## Abstract

The paper examines $B_0(2,5) = \langle a_1, a_2 \rangle$, described as the largest two-generator Burnside group of exponent five with order $5^{34}$. Using a power commutator presentation, elements are uniquely represented as products with exponents in $\mathbb{Z}_5$. The authors have calculated the elements of the center of $B_0(2,5)$ in the form of group words of the smallest length for the symmetric generating set, using supercomputer resources. [trans.]

## TL;DR

Answers **Mazurov's 2024 question** — find a short group word for a nontrivial central element of $B_0(2,5)$ — in the *strong* form: computes **all** central elements as **geodesic (minimal-length) words** over the symmetric set $A_4=\{a_1,a_1^{-1},a_2,a_2^{-1}\}$. The center is known ([[havas-wall-wamsley-1974]]) to be cyclic of order 5, $Z(B_0)=\langle a_{34}\rangle$ with $a_{34}=[a_2,a_1,a_1,a_1,a_2,a_1,a_2,a_1,a_1,a_2,a_2,a_2]$; naively unfolding this commutator gives length **6142** in $A_4$ (**15355** in $A_2$). By computing $K_{25}(B_0)$ in $A_4$ (a modified version of the [[kuznetsov-kuznetsova-2018]] coset algorithm on a 128-core / 1.5 TB machine) the authors find the four nontrivial central words $a_{34},a_{34}^2,a_{34}^3,a_{34}^4$ have geodesic lengths **47, 50, 50, 47** in $A_4$ (and 90, 100, 100, 90 in $A_2$, not proven minimal). Verified central via GAP + `anupq`.

## Problem

$B_0=B_0(2,5)=\langle a_1,a_2\rangle$ is the maximal finite two-generator exponent-5 Burnside group, order $5^{34}$ [[havas-wall-wamsley-1974]]; if $B(2,5)$ is finite then $B(2,5)=B_0$. Its **center is cyclic of order 5**, $Z(B_0)=\langle a_{34}\rangle$, where (as a pc-commutator)
$$a_{34}=[a_2,a_1,a_1,a_1,a_2,a_1,a_2,a_1,a_1,a_2,a_2,a_2].$$
Unfolding this weight-12 commutator "head-on" yields a word of length **6142** over $A_4=\{a_1,a_1^{-1},a_2,a_2^{-1}\}$ and **15355** over $A_2=\{a_1,a_2\}$. In **2024 V. D. Mazurov** asked for at least one nontrivial central element written as a *comparatively short* word in $A_2$ or $A_4$ — needed to test properties of $B_0(2,5)$ and $B(2,5)$. Since [[kuznetsov-kuznetsova-2018]] estimates the Cayley diameter of $B_0$ as $\approx69$ ($A_4$) / $\approx105$ ($A_2$), a much shorter representation must exist — but finding it is "a needle in a haystack" given $|B_0|=5^{34}$.

## Approach

Starting from the growth-function machinery of [[kuznetsov-kuznetsova-2018]] (ref [5], the coset-ball `QuotientGrowthFunction`) and [[kuznetsov-2016]] (ref [6], the `Ball` algorithm):

- Recall $K_s(G,X)$ = ball of radius $s$ (all irreducible words of length $\le s$); for $Q=G/N$ and coset $qN$, $K_s(q)=\{g\in K_s:\varphi(g)=q\}$; the algorithm of [5] turns a radius-$s$ ball into radius-$2s$ coset balls.
- **Hardware**: an MCS with **128 processor cores, 1.5 TB RAM, 2 TB disk**. Using known properties of $B_0$, the authors modified algorithm [6] to increase parallelism and cut memory, enabling computation of $K_{25}(B_0)$ in $A_4$.
- Set $N=\langle a_{11},\dots,a_{34}\rangle\trianglelefteq B_0$ and ran algorithm [5] with inputs $K_{25}(B_0)$, $Q=B_0/N$, $q=e$; after partially computing $K_{50}(e)$ the run was stopped once the goal was reached.
- The central words were found within the **first day**; confirming *no shorter* words express the central elements took about **one more month** of MCS time.
- **Verification**: GAP with the `anupq` library confirms all listed words are genuinely central in $B_0(2,5)$.

## Key result

Mazurov's question is answered in the stronger form — **all** nontrivial central elements of $B_0(2,5)$ as **minimal-length (geodesic) words** in $A_4$. With $x=a_1,\ y=a_2,\ X=a_1^{-1},\ Y=a_2^{-1}$ (verbatim):

$$
\begin{aligned}
a_{34} &= xyx^2Yxyx Y Xyx^2 Y X^2 yX^2 Y xyxY xyXY xyXY Xyx^2 Y XyXY Xyx^2 Y x,\\
a_{34}^2 &= x^2yxYXyXY xyxY X^2 yxY xyxY X^2 yXY xyXY XyxY xyXY x^2 yX^2 Y X^2 yxY,\\
a_{34}^3 &= x^2yxYX^2yXY XyXY xyxY XyxY x^2 yX^2 Y Xyx^2 Y xyxY xyXY XyxY XyX^2 Y,\\
a_{34}^4 &= x^2yx^2Yx^2yXY XyXY x^2 yXY XyxY XyxY xyxY X^2 yX^2 Y x^2 yXY xyxY.
\end{aligned}
$$

**Lengths in $A_4$**: $|a_{34}|=|a_{34}^4|=\mathbf{47}$, $\ |a_{34}^2|=|a_{34}^3|=\mathbf{50}$ (vs. 6142 naive).

Substituting $X\to x^4$, $Y\to y^4$ and reducing subwords $w^5$ gives $A_2$ representations of lengths **90, 100, 100, 90** (vs. 15355 naive) — but these are **not guaranteed minimal** in $A_2$.

## Assumptions

- $B_0(2,5)$ finite of order $5^{34}$, pc-presentation and $Z(B_0)=\langle a_{34}\rangle$ (order 5) taken from [[havas-wall-wamsley-1974]].
- Minimality in $A_4$ is established by exhaustive ball computation ($K_{25}$/partial $K_{50}$); minimality in $A_2$ is **not** claimed.
- Multiplication/growth via the algorithms of [[kuznetsov-kuznetsova-2018]] and [[kuznetsov-2016]]; centrality independently checked in GAP + `anupq`.

## Limitations / scope

- $A_4$-geodesic words are proven minimal; the $A_2$ words (90/100/100/90) are only *derived*, minimality open.
- Applies to $B_0(2,5)$; no claim about the free $B(2,5)$ unless $B(2,5)=B_0(2,5)$.
- Confirming minimality took ~1 month on a 128-core / 1.5 TB machine — reproduction is resource-intensive.

## Replication evidence

No independent replication known. Centrality of every listed word is checkable directly in GAP + `anupq` (the authors' own verification); minimality would require rebuilding the $A_4$ ball.

## Why this paper matters

This is the current frontier of the Kuznetsov program: a concrete, **short, minimal** representation of the order-5 center of $B_0(2,5)$ — the naive length-6142 commutator collapses to a length-**47** geodesic in $A_4$. It directly answers a question posed by Mazurov (2024).

For the Mixer B(2,5) attack these are prime **verification anchors**: $a_{34}$ commutes with everything, so any correct rewriting/KB pipeline for $B_0(2,5)$ (and for $B(2,5)$ if $B(2,5)=B_0(2,5)$) must handle these words consistently. Because their exact $A_4$-geodesic lengths (47/50/50/47) are known, they double as hard length benchmarks for any growth or bidirectional-search tool. The intro also records the modeling fact that the $k$-dimensional hypercube is the Cayley graph of $B(k,2)$.

## Quotes

Full text is in Russian; content above is paraphrased/translated [trans.] from the getFT PDF (pp. 270–273). The four central words and their lengths are reproduced verbatim under Key result.

## Open questions surfaced

- Are the $A_2$ representations (90/100/100/90) actually minimal? The paper explicitly leaves this open.
- The $A_4$ geodesic length 47 is well below the estimated diameter $\approx69$ ([[kuznetsov-kuznetsova-2018]]); how do central-element lengths distribute relative to the full diameter?
- Can the Mixer's B(2,5) pipeline recover these central words from its existing rule banks without a separate 128-core run?
- Do these central words reduce to the same normal form under both RPO and shortlex orderings — a consistency test for $B(2,5)\overset?=B_0(2,5)$?

## Related material in vault

- Extends: [[kuznetsov-kuznetsova-2018]] (the coset-ball / resource-efficient algorithm modified here — ref [5]), [[kuznetsov-2016]] (the `Ball` algorithm — ref [6])
- Cites: [[havas-wall-wamsley-1974]] (order $5^{34}$, pc-basis, $Z(B_0)=\langle a_{34}\rangle$ — ref [4]). Crypto-context refs: [1] Baumslag–Fazio–Nicolosi, [2] Fazio–Iga–Nicolosi, [3] Kahrobaei–Noce.
- Concepts: [[Concepts/verification-methods-for-group-equality]]
- MOC: [[Research/Group theory/_MOCs/_moc-burnside]]
- Open problem: [[b25-finiteness-11.48-kostrikin]]

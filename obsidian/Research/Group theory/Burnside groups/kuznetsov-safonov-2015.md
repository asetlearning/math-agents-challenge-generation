---
title: "Hall's polynomials over Burnside groups of exponent three"
authors: A. A. Kuznetsov, K. V. Safonov
year: 2015
venue: Prikladnaya Diskretnaya Matematika. Supplement
url: https://doi.org/10.17223/2226308X/8/57
url_fulltext: "https://www.mathnet.ru/php/getFT.phtml?jrnid=pdma&paperid=225&what=fullt&option_lang=eng"
url_translated:
language: ru
methodology_type: methodology
citation_count: null
citation_count_date:
key_concepts:
  - "[[hall-polynomials]]"
  - "[[power-commutator-presentation]]"
  - "[[collection-process]]"
extends:
  - "[[kuznetsov-kuznetsova-2013]]"
contradicts: []
replicates: []
cites:
  - "[[kuznetsov-kuznetsova-2013]]"
cited_by: []
quality_notes: "3-page conference note (Prikl. Diskr. Mat. Suppl. 8, pp. 147–149, DOI 10.17223/2226308X/8/57). Original in Russian. RE-FILLED FROM FULL TEXT (mathnet getFT PDF, pdftotext — Cyrillic renders correctly). CORRECTION to prior note: this is a PRELIMINARY announcement, NOT 'the same result' as [[kuznetsov-2015-cayley-exp3]]. This supplement contains ONLY the Hall-polynomial Theorem 1 (z1–z14 over Z3 for B4, verbatim below) plus the full pc-presentation of B4 on 14 commutators. It does NOT contain the Cayley-graph diameter table or the B3/B2 corollaries — those appear only in the fuller SEMR paper [[kuznetsov-2015-cayley-exp3]] (which is thus a superset). The z1–z14 formulas here are identical to those in the SEMR paper. BORDERLINE inclusion for the B25 program: exponent-3, not exponent-5; included because the Hall-polynomial method is exponent-agnostic and underpins the exponent-5 work. NOTE: the source PDMA-supplement PDF interleaves neighboring articles (a document-ranking note before, a discrete-log note after); only the middle article, pp. 147–149, is this paper."
fill_level: full
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/finite-group-enumeration
  - topic/cayley-graphs
  - paper
  - status/draft
---

# Hall's polynomials over Burnside groups of exponent three

> **Translation note**: source paper is in Russian (`language: ru`). Abstract below is translated to English [trans.] from the mathnet.ru record.

## Abstract

The research examines Burnside groups of exponent 3, denoted $B_k$. Two arbitrary elements in the group $B_k$ represented as $a_1^{x_1} \cdots a_n^{x_n}$ and $a_1^{y_1} \cdots a_n^{y_n}$ can be multiplied using collection processes or Hall's polynomials. The study demonstrates that Hall's polynomials provide computational advantages over traditional collection methods for group operations. The researchers calculated previously unknown Hall's polynomials of $B_k$ for $k \le 4$ and discuss applications to Cayley graph analysis. The approach is readily implementable in multiprocessor systems. [trans.]

## TL;DR

Conference supplement giving the **explicit Hall polynomials** $z_1,\dots,z_{14}$ over $\mathbb{Z}_3$ for the exponent-3 Burnside group $B_4=B(4,3)$ (Theorem 1, verbatim below; smaller $k\le3$ obtained by restriction), together with the full power-commutator presentation of $B_4$ on 14 commutators. It is the **preliminary announcement** of the multiplication oracle later used in the fuller SEMR paper [[kuznetsov-2015-cayley-exp3]] — which adds the Cayley-graph diameter table and the $B_3,B_2$ corollaries **not present here**. Methodology parallels the exponent-5 foundation [[kuznetsov-kuznetsova-2013]] and the exponent-7 twin [[kuznetsov-safonov-2014]].

## Problem

Multiplying two elements of $B_k=B(k,3)$ in normal commutator form $a_1^{x_1}\cdots a_n^{x_n}\cdot a_1^{y_1}\cdots a_n^{y_n}=a_1^{z_1}\cdots a_n^{z_n}$ can be done via the classical collection process, but Hall showed each $z_i$ is a polynomial over $\mathbb{Z}_3$ in $x_1,\dots,x_i,y_1,\dots,y_i$ with the form $z_i=x_i+y_i+p_i(\dots)$. Computer experiments in the exponent-5 and exponent-7 cases showed the Hall-polynomial method beats collection and parallelizes easily. Compute the previously-unknown exponent-3 Hall polynomials, needed as the fast-multiplication oracle for Cayley-graph analysis.

## Approach

1. **Order + nilpotency.** By Levi–van der Waerden [1], $|B_k|=3^{\,k+\binom{k}{2}+\binom{k}{3}}$ and nilpotency class $\le3$.
2. **pc-presentation.** Via GAP, obtain a power-commutator presentation of $B_4$ on 14 basis commutators $a_1,\dots,a_{14}$ (weights 1–3, verbatim below); every $g$ is a unique normal word $g=a_1^{x_1}\cdots a_{14}^{x_{14}}$, $x_i\in\mathbb{Z}_3$. Doing $B_4$ also covers $B_1,B_2,B_3$.
3. **Interpolation.** Solve the pairwise interpolation systems over $\mathbb{Z}_3$ and chain them (collection in analytic form) to obtain all $z_i$ — same technique as [[kuznetsov-kuznetsova-2013]] (exponent 5).

## Key result

**Theorem 1 (verbatim).** For two elements $a_1^{x_1}\cdots a_{14}^{x_{14}}$ and $a_1^{y_1}\cdots a_{14}^{y_{14}}$ of $B_4$ in commutator form, the product exponents $z_i\in\mathbb{Z}_3$ are the Hall polynomials:

$$
\begin{aligned}
z_1 &= x_1+y_1, & z_2 &= x_2+y_2, & z_3 &= x_3+y_3, & z_4 &= x_4+y_4,\\
z_5 &= x_5+y_5+x_2y_1, & z_6 &= x_6+y_6+x_3y_1, & z_7 &= x_7+y_7+x_3y_2,\\
z_8 &= x_8+y_8+x_4y_1, & z_9 &= x_9+y_9+x_4y_2, & z_{10} &= x_{10}+y_{10}+x_4y_3,\\
z_{11} &= x_{11}+y_{11}+x_5y_3+2x_6y_2+x_7y_1+x_2x_3y_1+x_2y_1y_3+2x_3y_1y_2,\\
z_{12} &= x_{12}+y_{12}+x_5y_4+2x_8y_2+x_9y_1+x_2x_4y_1+x_2y_1y_4+2x_4y_1y_2,\\
z_{13} &= x_{13}+y_{13}+x_{10}y_1+x_6y_4+2x_8y_3+x_3x_4y_1+x_3y_1y_4+2x_4y_1y_3,\\
z_{14} &= x_{14}+y_{14}+x_{10}y_2+x_7y_4+2x_9y_3+x_3x_4y_2+x_3y_2y_4+2x_4y_2y_3.
\end{aligned}
$$

Each $z_i$ has the Hall form $z_i=x_i+y_i+p_i(x_1,\dots,x_{i-1},y_1,\dots,y_{i-1})$. These are **identical** to the $z_i$ in the SEMR paper [[kuznetsov-2015-cayley-exp3]]. This supplement stops here — it does **not** include the Cayley-graph diameter table or the $B_3,B_2$ corollaries (those are SEMR-only).

## Power-commutator presentation of $B_4=B(4,3)$ (verbatim)

- Weight 1: $a_1,a_2,a_3,a_4$ (generators).
- Weight 2: $a_5=[a_2,a_1]$, $a_6=[a_3,a_1]$, $a_7=[a_3,a_2]$, $a_8=[a_4,a_1]$, $a_9=[a_4,a_2]$, $a_{10}=[a_4,a_3]$.
- Weight 3: $a_{11}=[a_5,a_3]=[a_2,a_1,a_3]$, $a_{12}=[a_5,a_4]=[a_2,a_1,a_4]$, $a_{13}=[a_6,a_4]=[a_3,a_1,a_4]$, $a_{14}=[a_7,a_4]=[a_3,a_2,a_4]$.
- Relations $R$ (trivial $a_i^3=1$, $[a_j,a_i]=1$ omitted): $[a_2,a_1]=a_5$, $[a_3,a_1]=a_6$, $[a_3,a_2]=a_7$, $[a_4,a_1]=a_8$, $[a_4,a_2]=a_9$, $[a_4,a_3]=a_{10}$, $[a_5,a_3]=a_{11}$, $[a_5,a_4]=a_{12}$, $[a_6,a_2]=a_{11}^2$, $[a_6,a_4]=a_{13}$, $[a_7,a_1]=a_{11}$, $[a_7,a_4]=a_{14}$, $[a_8,a_2]=a_{12}^2$, $[a_8,a_3]=a_{13}^2$, $[a_9,a_1]=a_{12}$, $[a_9,a_3]=a_{14}^2$, $[a_{10},a_1]=a_{13}$, $[a_{10},a_2]=a_{14}$.
- So $B_4=\langle a_1,\dots,a_{14}\mid R\rangle$.

## Assumptions

- $|B_k|=3^{k+\binom{k}{2}+\binom{k}{3}}$, nilpotency class $\le3$ (Levi–van der Waerden [1]); $|B(2,3)|=3^3$, $|B(3,3)|=3^7$, $|B(4,3)|=3^{14}$.
- pc-presentation from GAP correct; interpolation over $\mathbb{Z}_3$ full rank ⇒ unique Hall polynomials.

## Limitations / scope

- Explicit polynomials only for $k\le4$; larger $k$ "take considerably more space."
- Supplement scope: Hall polynomials only — no Cayley-graph data (that is in [[kuznetsov-2015-cayley-exp3]]).
- Exponent 3, not $B(2,5)$.

## Replication evidence

The $z_1$–$z_{14}$ here match the SEMR paper [[kuznetsov-2015-cayley-exp3]] verbatim (self-consistent). Cross-exponent: identical interpolation method in [[kuznetsov-kuznetsova-2013]] (exponent 5) and [[kuznetsov-safonov-2014]] (exponent 7).

## Why this paper matters

Hall's polynomial multiplication is the computational foundation for Kuznetsov's Burnside-group experiments. This supplement is the exponent-3 announcement of that oracle. That the same interpolation method works for exponents 3, 5, and 7 establishes it as a general odd-exponent Burnside methodology, strengthening confidence that the [[kuznetsov-kuznetsova-2013]] exponent-5 implementation is correct and generalizable.

## Quotes

1. > "Let $B_k=(k,3)$ be the $k$-generator Burnside group of exponent 3. In this work the Hall polynomials for $B_k$ with $k\le4$ are computed." — Abstract [trans.]
2. > "Computational experiments on groups of exponent five and seven revealed that the Hall-polynomial method has an advantage over the traditional collection process." — §body [trans.]

## Open questions surfaced

- Do the exponent-3 Hall polynomials exhibit simpler structure than exponent-5 (consistent with lower nilpotency class 3 vs 5)? By eye the $z_i$ are shorter, but no quantitative comparison is given.

## Related material in vault

- Extends: [[kuznetsov-kuznetsova-2013]] (same Hall polynomial methodology, exponent 5)
- Cites: [[kuznetsov-kuznetsova-2013]]
- Related: [[kuznetsov-2015-cayley-exp3]] (fuller SEMR paper — SUPERSET: same $z_i$ plus Cayley-graph table + $B_3/B_2$ corollaries; this supplement is the preliminary announcement, NOT an identical result), [[kuznetsov-safonov-2014]] (same methodology for exponent 7)
- MOC: [[Research/Group theory/_MOCs/_moc-burnside]]

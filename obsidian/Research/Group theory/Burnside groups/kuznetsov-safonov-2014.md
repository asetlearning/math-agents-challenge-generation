---
title: "Hall's polynomials of finite two-generator groups of exponent seven"
authors: Alexander A. Kuznetsov, Konstantin V. Safonov
year: 2014
venue: Journal of Siberian Federal University. Mathematics & Physics
url: http://mi.mathnet.ru/jsfu363
url_fulltext: "https://www.mathnet.ru/php/getFT.phtml?jrnid=jsfu&paperid=363&what=fullt&option_lang=eng"
url_translated:
language: en
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
quality_notes: "Full journal paper (J. Sib. Fed. Univ. Math. Phys. 7:2, pp. 186–190, 5 pages). English language (original, not translated). RE-FILLED FROM FULL TEXT (mathnet getFT PDF, pdftotext). The full text gives the explicit Hall polynomials z1–z8 over Z7 (formulas 1–8 verbatim below), the complete power-commutator presentation of B4 (8 commutators a1–a8, all defining relations R), and the full interpolation method (36×36 linear systems over Z7). Largest group in the family: B28, order 7^20416 (per O'Brien–Vaughan-Lee [1]). BORDERLINE inclusion for the B25 program: exponent-7, not exponent-5; included because the Hall-polynomial method is exponent-agnostic and this is the direct sister of the exponent-5 foundation [[kuznetsov-kuznetsova-2013]]. Compare [[kuznetsov-safonov-2015]] (exponent-3) — same methodology across three odd exponents."
fill_level: full
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/finite-group-enumeration
  - paper
  - status/draft
---

# Hall's polynomials of finite two-generator groups of exponent seven

## Abstract

Let $B_k = B_0(2,7,k)$ be the largest two-generator finite group of exponent 7 and nilpotency class $k$. Hall's polynomials of $B_k$ for $k \le 4$ are calculated. Keywords: periodic group, collection process, Hall's polynomials.

## TL;DR

Computes the explicit **Hall polynomials** $z_1,\dots,z_8$ over $\mathbb{Z}_7$ for the largest two-generator exponent-7 finite groups $B_k = B_0(2,7,k)$, for nilpotency class $k \le 4$. In this family the largest group is $B_{28}$ of order $7^{20416}$. The paper gives the full power-commutator presentation of $B_4$ (8 commutators) and derives every polynomial by **interpolation** — solving a $36\times36$ linear system over $\mathbb{Z}_7$ for each pairwise product $a_j^y a_i^x$. This is the exponent-7 twin of the exponent-5 fast-multiplication foundation [[kuznetsov-kuznetsova-2013]], demonstrating the method is exponent-agnostic.

## Problem

Multiplying two elements of $B_k$ written in normal commutator form $a_1^{x_1}\cdots a_n^{x_n} \cdot a_1^{y_1}\cdots a_n^{y_n} = a_1^{z_1}\cdots a_n^{z_n}$ can be done via the classical **collection process** (as in GAP/MAGMA), but Hall showed each exponent $z_i$ is a **polynomial** over $\mathbb{Z}_7$ in $x_1,\dots,x_i,y_1,\dots,y_i$. Computational experiments in the exponent-5 case ([7] = [[kuznetsov-kuznetsova-2013]]) showed the Hall-polynomial method beats the collection process, and is easily parallelized. The problem: compute these previously-unknown Hall polynomials for the exponent-7 groups $B_k$.

## Approach

1. **Presentation.** Using GAP, obtain a power-commutator presentation of $B_4$ on 8 commutators (weights 1–4) with defining relations $R$. Every $g\in B_4$ is a unique normal word $g = a_1^{x_1}\cdots a_8^{x_8}$, $x_i\in\mathbb{Z}_7$. Doing $B_4$ also yields $B_1,B_2,B_3$ (heavier commutators vanish).
2. **Pairwise products by interpolation.** For each non-commuting pair $1\le i<j\le 8$, compute the 36 products $a_j^y a_i^x$ for $x,y\in\{1,\dots,6\}$ (tabulated verbatim in the paper). Write $a_j^y a_i^x = a_i^x a_j^y \prod_{r>j} a_r^{f_r^{(i,j)}(x,y)}$ where each $f_r^{(i,j)}(x,y)=\sum_{p=1}^{6}\sum_{q=1}^{6}\beta_{pq}^{r}x^p y^q$.
3. **Solve.** For each commutator $r$, the coefficients $\beta_{pq}^r$ solve a $36\times36$ linear system over $\mathbb{Z}_7$ (eq. 9). The system matrix has rank 36, so the solution is unique.
4. **Assemble.** Chaining the pairwise relations (eq. 10) through a collection process in analytic form yields all $z_i$.

## Key result

**Theorem (verbatim).** For two arbitrary elements $a_1^{x_1}\cdots a_n^{x_n}$ and $a_1^{y_1}\cdots a_n^{y_n}$ of $B_k$ ($k\in\mathbb{N}$, $k\le 4$) in commutator form, the product exponents $z_i\in\mathbb{Z}_7$ are the Hall polynomials given by formulas (1–2) for $k=1$, (1–3) for $k=2$, (1–5) for $k=3$, and (1–8) for $k=4$:

$$
\begin{aligned}
z_1 &= x_1 + y_1,\\
z_2 &= x_2 + y_2,\\
z_3 &= x_3 + y_3 + x_2 y_1,\\
z_4 &= x_4 + y_4 + 3x_2 y_1 + x_3 y_1 + 4x_2 y_1^2,\\
z_5 &= x_5 + y_5 + 3x_2 y_1 + x_3 y_2 + 4x_2^2 y_1 + x_2 y_1 y_2,\\
z_6 &= x_6 + y_6 + 5x_2 y_1 + 3x_3 y_1 + x_4 y_1 + 3x_2 y_1^2 + 6x_2 y_1^3 + 4x_3 y_1^2,\\
z_7 &= x_7 + y_7 + 2x_2^2 y_1^2 + 2x_2 y_1 + x_4 y_2 + x_5 y_1 + 5x_2 y_1^2 + 5x_2^2 y_1 + 4x_2 y_1^2 y_2 + 3x_2 y_1 y_2 + x_3 y_1 y_2,\\
z_8 &= x_8 + y_8 + 5x_2 y_1 + 3x_3 y_2 + x_5 y_2 + 3x_2^2 y_1 + 6x_2^3 y_1 + 4x_3 y_2^2 + 4x_2 y_1 y_2^2 + 4x_2^2 y_1 y_2 + 6x_2 y_1 y_2.
\end{aligned}
$$

Each $z_i$ has the Hall form $z_i = x_i + y_i + p_i(x_1,\dots,x_{i-1},y_1,\dots,y_{i-1})$. These give an explicit fast-multiplication oracle for two-generator exponent-7 finite groups, enabling Cayley-graph and growth-function computation. For $k>4$ the polynomials are computed the same way but are too large to print/verify by hand.

## Power-commutator presentation of $B_4$ (verbatim)

- Weight 1: $a_1, a_2$ (generators).
- Weight 2: $a_3 = [a_2,a_1]$.
- Weight 3: $a_4 = [a_3,a_1] = [a_2,a_1,a_1]$, $\ a_5 = [a_3,a_2] = [a_2,a_1,a_2]$.
- Weight 4: $a_6 = [a_4,a_1]$, $\ a_7 = [a_5,a_1] = [a_4,a_2]$, $\ a_8 = [a_5,a_2]$.
- Relations $R$: $a_i^7 = 1$ ($1\le i\le 8$); $[a_2,a_1]=a_3$, $[a_3,a_1]=a_4$, $[a_3,a_2]=a_5$, $[a_4,a_1]=a_6$, $[a_4,a_2]=a_7$, $[a_5,a_1]=a_7$, $[a_5,a_2]=a_8$; all other commutators $=1$.
- So $B_4 = \langle a_1,\dots,a_8 \mid R\rangle$.

The pairwise relations (worked example $a_2^y a_1^x$, coefficients $\beta_{11}=5,\beta_{12}=3,\beta_{13}=6$ giving $f_8^{(1,2)}(x,y)=5xy+3xy^2+6xy^3$; and the six other non-commuting pairs) are all given explicitly.

## Assumptions

- $B_0(2,7,k)$ finite; largest is $B_{28}$, order $7^{20416}$ (O'Brien–Vaughan-Lee [1]).
- Power-commutator presentation from GAP is correct.
- Correctness rests on exact linear-algebra over $\mathbb{Z}_7$ (each $36\times36$ system full rank).

## Limitations / scope

- $k \le 4$ only printed; larger $k$ computed identically but not human-verifiable.
- Exponent 7, two generators. Does NOT directly address $B(2,5)$ — this is the exponent-7 analogue included for methodological parallelism.

## Replication evidence

No independent replication known. Cross-exponent consistency: the identical interpolation technique appears in [[kuznetsov-kuznetsova-2013]] (exponent 5) and [[kuznetsov-safonov-2015]] (exponent 3), serving as implicit cross-validation of the method.

## Why this paper matters

This paper is the exponent-7 member of Kuznetsov's three-exponent Hall-polynomial program:
- Exponent 5: [[kuznetsov-kuznetsova-2013]] (2013) — foundation, enables all B(2,5) Cayley computation
- **Exponent 7**: this paper (2014) — same method on $B_0(2,7,k)$
- Exponent 3: [[kuznetsov-safonov-2015]] (2015) — full treatment with Cayley graphs

Having the explicit exponent-7 polynomials in hand shows the interpolation-over-$\mathbb{Z}_p$ method is genuinely exponent-agnostic: the same $36\times36$-system machinery works for any odd $p$. That strengthens confidence in the exponent-5 implementation used throughout the B(2,5) computation line.

## Quotes

1. > "Let $B_k = B_0(2,7,k)$ be the largest two-generator finite group of exponent 7 and nilpotency class $k$." — abstract
2. > "In this class, the largest group is the group $B_{28}$, which has the order $7^{20416}$." — §1
3. > "The rank of the system matrix is equal to 36, therefore it has the only solution." — proof

## Open questions surfaced

- Are the exponent-7 Hall polynomials materially more complex than the exponent-5 ones? (By eye, the $z_i$ here carry more cross-terms, but the growth rate with $p$ is not quantified.)
- Have Cayley-graph diameters been computed for $B_0(2,7,k)$ as in [[kuznetsov-2015-cayley-exp3]] for exponent 3? Not in this paper; the closing remarks flag it as a motivation.

## Related material in vault

- Extends: [[kuznetsov-kuznetsova-2013]] (Hall polynomial methodology; exponent-7 extension)
- Cites: [[kuznetsov-kuznetsova-2013]]
- Related: [[kuznetsov-safonov-2015]] (exponent-3 Hall polynomials + Cayley graphs — same methodology), [[kuznetsov-2015-cayley-exp3]] (exponent-3 Cayley graphs; same research line)
- MOC: [[Research/Group theory/_MOCs/_moc-burnside]]

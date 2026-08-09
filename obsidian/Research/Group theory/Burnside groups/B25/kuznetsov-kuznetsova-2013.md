---
title: "Fast multiplication in finite two-generated groups of exponent five"
authors: A. A. Kuznetsov, A. S. Kuznetsova
year: 2013
venue: Prikladnaya Diskretnaya Matematika
url: http://mi.mathnet.ru/pdm397
url_fulltext: "https://www.mathnet.ru/php/getFT.phtml?jrnid=pdm&paperid=397&what=fullt&option_lang=eng"
url_translated:
language: ru
methodology_type: methodology
domain: group-theory
status: draft
citation_count: null
citation_count_date:
key_concepts:
  - "[[hall-polynomials]]"
  - "[[power-commutator-presentation]]"
  - "[[collection-process]]"
extends:
  - "[[havas-wall-wamsley-1974]]"
contradicts: []
replicates: []
cites:
  - "[[havas-wall-wamsley-1974]]"
cited_by:
  - "[[kuznetsov-2016]]"
  - "[[kuznetsov-karchevsky-2016]]"
  - "[[kuznetsova-kuznetsov-safonov-2013]]"
  - "[[kuznetsov-kuznetsova-2018]]"
  - "[[kuznetsov-safonov-2015]]"
  - "[[kuznetsov-2015-cayley-exp3]]"
  - "[[kuznetsov-safonov-2014]]"
quality_notes: "Full journal paper (Prikl. Diskr. Mat. 1(19), pp. 110–116, 7 pages). Original in Russian. RE-FILLED FROM FULL TEXT (mathnet getFT PDF, pdftotext). The full text gives the explicit Hall polynomials z1–z8 over Z5 (formulas 1–8, verbatim below), the complete power-commutator presentation of B0(2,5,4) on 8 commutators, and the full interpolation method (16×16 linear systems over Z5). Two concrete new facts vs. the old abstract-only note: (a) the SPEEDUP is stated — Hall polynomials are on average ~10× (one order of magnitude) faster than the collection process, measured over ~10^4 random products in each B0(2,5,k); (b) Sims [5] ANNOUNCED computing these polynomials but never published them and no implementation was findable — this paper fills that gap. Largest group in family: B0(2,5,12), order 5^34 (Havas–Wall–Wamsley [1]). Full k=12 polynomials span 42 pages, available from authors on request. This is the computational foundation for all subsequent Kuznetsov growth-function papers."
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
  - paper
  - status/draft
project: b25
---

# Fast multiplication in finite two-generated groups of exponent five

> **Translation note**: source paper is in Russian (`language: ru`). Abstract below is translated to English [trans.] from the mathnet.ru record.

## Abstract

An algorithm based on Hall's polynomials for fast multiplication of elements in finite two-generator groups of period five is presented. Keywords: periodic group, collection process, Hall's polynomials. [trans.]

## TL;DR

Derives the **explicit Hall polynomials** $z_1,\dots,z_8$ over $\mathbb{Z}_5$ that multiply two elements of $B_0(2,5,k)$ (in normal commutator form) for $k\le 4$, and reports that evaluating these polynomials is **on average ~10× (one order of magnitude) faster** than the classical collection process (benchmarked over ~$10^4$ random products in each group). Sims [5] had announced such polynomials but never published them and no implementation existed; this paper fills that gap. It is the computational foundation on which every subsequent Kuznetsov growth-function and Cayley-graph paper depends.

## Problem

$B_0(2,5,12)$ (order $5^{34}$) is the largest group in the family $B_0(2,5,k)$; each has a known power-commutator presentation (obtainable via GAP). Studying growth functions or Cayley diameters requires multiplying many elements. In normal commutator form $a_1^{x_1}\cdots a_n^{x_n} \cdot a_1^{y_1}\cdots a_n^{y_n} = a_1^{z_1}\cdots a_n^{z_n}$, the exponents $z_i$ can be found by the **collection process** (GAP/MAGMA) — but Hall showed each $z_i$ is a **polynomial** over $\mathbb{Z}_5$ in $x_1,\dots,x_i,y_1,\dots,y_i$. Sims [5] announced these polynomials but never published them, and no software implementation was findable. Compute them explicitly and use them for fast multiplication.

## Approach

1. **Presentation.** Take the power-commutator presentation of $B_0(2,5,4)$ on 8 basis commutators (weights 1–4); doing $k=4$ automatically covers $k=1,2,3$ (heavier commutators vanish). Every $g$ is a unique normal word $g=a_1^{x_1}\cdots a_8^{x_8}$, $x_i\in\mathbb{Z}_5$.
2. **Pairwise products by interpolation.** For each non-commuting pair $1\le i<j\le 8$, tabulate the 16 products $a_j^y a_i^x$ ($x,y\in\{1,2,3,4\}$, all listed verbatim in the paper). Write $a_j^y a_i^x = a_i^x a_j^y \prod_{r>j} a_r^{f_r^{(i,j)}(x,y)}$, with $f_r^{(i,j)}(x,y)=\sum_{p=1}^4\sum_{q=1}^4 \beta_{pq}^r x^p y^q$.
3. **Solve.** Each $f_r^{(i,j)}$ is found by a $16\times16$ linear system over $\mathbb{Z}_5$ (eq. 9), full rank ⇒ unique solution.
4. **Implementation.** Polynomials $z_i$ computed in MATLAB, then the resulting formulas hand-implemented in a standalone C program. Speed compared against the collection process on ~$10^4$ random products per group.

## Key result

**Theorem 1 (verbatim).** For two arbitrary elements $a_1^{x_1}\cdots a_n^{x_n}$ and $a_1^{y_1}\cdots a_n^{y_n}$ of $B_0(2,5,k)$ ($k\in\mathbb{N}$, $k\le4$) in commutator form, the product exponents $z_i\in\mathbb{Z}_5$ are the Hall polynomials given by (1),(2) for $k=1$; (1)–(3) for $k=2$; (1)–(5) for $k=3$; (1)–(8) for $k=4$ (using $\binom{\cdot}{2}$/$\binom{\cdot}{3}$ binomial-coefficient notation from the original):

$$
\begin{aligned}
z_1 &= x_1 + y_1,\\
z_2 &= x_2 + y_2,\\
z_3 &= x_3 + y_3 + x_2 y_1,\\
z_4 &= x_4 + y_4 + x_2\tbinom{y_1}{2} + x_3 y_1,\\
z_5 &= x_5 + y_5 + x_2 y_1 y_2 + \tbinom{x_2}{2} y_1 + x_3 y_2,\\
z_6 &= x_6 + y_6 + x_2\tbinom{y_1}{3} + x_3\tbinom{y_1}{2} + x_4 y_1,\\
z_7 &= x_7 + y_7 + x_2\tbinom{y_1}{2}y_2 + \tbinom{x_2}{2}y_1 + x_3 y_1 y_2 + x_4 y_2 + x_5 y_1,\\
z_8 &= x_8 + y_8 + x_2 y_1\tbinom{y_2}{2} + \tbinom{x_2}{2}y_1 y_2 + \tbinom{x_2}{3}y_1 + x_3\tbinom{y_2}{2} + x_5 y_2.
\end{aligned}
$$

Each $z_i$ has the Hall form $z_i = x_i + y_i + p_i(x_1,\dots,x_{i-1},y_1,\dots,y_{i-1})$. **Benchmark:** evaluating these polynomials multiplies two elements on average ~10× faster than the collection process. For $k>4$ the polynomials are found identically; the full $k=12$ set spans 42 pages and is available from the authors on request.

## Power-commutator presentation of $B_0(2,5,4)$ (verbatim)

- Weight 1: $a_1,a_2$ (generators).
- Weight 2: $a_3=[a_2,a_1]$.
- Weight 3: $a_4=[a_3,a_1]=[a_2,a_1,a_1]$, $\ a_5=[a_3,a_2]=[a_2,a_1,a_2]$.
- Weight 4: $a_6=[a_4,a_1]$, $\ a_7=[a_5,a_1]=[a_4,a_2]$, $\ a_8=[a_5,a_2]$.
- Relations $R$: $a_i^5=1$ ($1\le i\le8$); $[a_2,a_1]=a_3$, $[a_3,a_1]=a_4$, $[a_3,a_2]=a_5$, $[a_4,a_1]=a_6$, $[a_4,a_2]=a_7$, $[a_5,a_1]=a_7$, $[a_5,a_2]=a_8$; all other commutators $=1$.
- So $B_0(2,5,4)=\langle a_1,\dots,a_8\mid R\rangle$.

Worked example ($a_2^y a_1^x$): the $16\times16$ system for the 8th commutator has rank 16 and unique solution $\beta_{11}=2,\beta_{12}=2,\beta_{13}=1$, giving $f_8^{(1,2)}(x,y)=2xy+2xy^2+xy^3$. All seven non-commuting pairs ($a_2^y a_1^x$, $a_3^y a_1^x$, $a_3^y a_2^x$, $a_4^y a_1^x$, $a_4^y a_2^x$, $a_5^y a_1^x$, $a_5^y a_2^x$) are given explicitly; all others commute.

## Assumptions

- Havas–Wall–Wamsley power-commutator presentation of $B_0(2,5)$ [1] is the working basis; largest quotient $B_0(2,5,12)$ has order $5^{34}$.
- GAP presentation and MATLAB linear algebra over $\mathbb{Z}_5$ are correct (each $16\times16$ system full rank).

## Limitations / scope

- Explicit polynomials printed only for $k\le4$; larger $k$ computed the same way but not human-verifiable (k=12 is 42 pages).
- Applies to finite quotients $B_0(2,5,k)$, not the free/infinite $B(2,5)$.

## Replication evidence

The algorithm is reused (as the multiplication oracle) in [[kuznetsov-2016]], [[kuznetsov-karchevsky-2016]], [[kuznetsov-kuznetsova-2018]], [[kuznetsova-kuznetsov-safonov-2013]], and every other Kuznetsov growth-function paper — implicit replication through downstream usage. The exponent-7 twin [[kuznetsov-safonov-2014]] and exponent-3 companion [[kuznetsov-safonov-2015]] apply the same interpolation method, cross-validating it across odd primes.

## Why this paper matters

Fast element multiplication is the rate-determining step in all $B_0(2,5)$ computational experiments. The explicit ~10× speedup over the collection process is what makes the Cayley-graph BFS for growth functions practical. Concretely, it also **fills a documented gap**: Sims announced these polynomials in 1998 [5] but never published them, and no implementation existed. This is the computational foundation of the entire Kuznetsov B(2,5) line — every downstream growth-function, Cayley-graph, and subgroup paper depends on the oracle developed here.

## Quotes

1. > "On average the use of polynomials allows one to obtain the product of two group elements an order of magnitude (i.e. 10 times) faster than the collection process." — §Introduction [trans.]
2. > "Sims [5] announced that he had computed the stated polynomial functions, however they were never published anywhere." — §Introduction [trans.]
3. > "The rank of the system matrix equals 16, therefore it has the unique solution." — §Algorithm [trans.]

## Open questions surfaced

- What is the asymptotic complexity of polynomial-based multiplication in $k$? The paper gives an empirical ~10× constant-factor speedup, not a complexity class.
- The same interpolation method transfers to exponents 3 and 7 ([[kuznetsov-safonov-2015]], [[kuznetsov-safonov-2014]]); does the speedup factor over the collection process depend on the exponent?

## Related material in vault

- Extends: [[havas-wall-wamsley-1974]] (power commutator presentation; Hall polynomial framework)
- Cites: [[havas-wall-wamsley-1974]]
- Cited by: [[kuznetsov-2016]], [[kuznetsov-karchevsky-2016]], [[kuznetsova-kuznetsov-safonov-2013]], [[kuznetsov-kuznetsova-2018]]
- MOC: [[Research/Group theory/_MOCs/_moc-burnside]]

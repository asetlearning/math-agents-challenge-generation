---
title: "On applications of the Cayley graphs of some finite groups of exponent five"
authors: Alexander A. Kuznetsov, Konstantin V. Safonov
year: 2018
venue: Journal of Siberian Federal University. Mathematics & Physics
url: https://doi.org/10.17516/1997-1397-2018-11-1-70-78
url_fulltext: "https://www.mathnet.ru/php/getFT.phtml?jrnid=jsfu&paperid=655&what=fullt&option_lang=eng"
url_translated:
language: en
methodology_type: empirical
domain: group-theory
status: draft
citation_count: null
citation_count_date:
key_concepts:
  - "[[hall-polynomials]]"
  - "[[growth-function]]"
  - "[[cayley-diameter]]"
  - "[[power-commutator-presentation]]"
extends:
  - "[[kuznetsov-filippov-2010-sjim]]"
contradicts: []
replicates: []
cites:
  - "[[kuznetsov-2015-cayley-exp3]]"
  - "[[kuznetsov-2016]]"
  - "[[kuznetsov-filippov-2010-sjim]]"
  - "[[kuznetsov-kuznetsova-2013]]"
  - "[[kuznetsov-safonov-2014]]"
  - "[[havas-wall-wamsley-1974]]"
cited_by: []
quality_notes: "Full journal paper (J. Sib. Fed. Univ. Math. Phys. 11:1, pp. 70–78, 9 pages). English language (this is the primary-source English original, not a translation). RE-FILLED FROM FULL TEXT (mathnet getFT PDF, pdftotext). The automorphism is the INVERSION map φ: a_i ↦ a_i^{-1} (verbatim), whose centralizer C = C_{B_0(2,5)}(φ) has |C| = 5^16 and splits as C = C_0 × ⟨z⟩ with |C_0| = 5^15, z a central element of B_0(2,5) of order 5, and C_0 = ⟨X_0⟩ on 4 minimal generators — structural facts imported verbatim from ref [11] = [[kuznetsov-filippov-2010-sjim]] (SJIM 2010, the inversion paper; CONFIRMS sjim=inversion, |C|=5^16). This is DISTINCT from the generator-swap involution a_1↔a_2 of [[kuznetsov-kuznetsova-2017]] (which cites the VMJ 2010 paper, |C|=5^17, 3 generators). New content in THIS paper: (Theorem) the full Hall polynomials z_1–z_15 over Z_5 for C_0 on 15 commutators a_1–a_15 (weights 1–4), with a worked 16×16 rank-16 interpolation example f_5^{(1,2)}=xy; (Corollary 1) D_X(C)=29, D̄_X(C)≈21 for the minimal set X=X_0∪{z}; (Corollary 2) D_Y(C)=19, D̄_Y(C)≈14 for the symmetric set Y=X∪X^{-1}. Growth computed via the BFS algorithm of ref [10]=[[kuznetsov-2016]], multiplication via Hall polynomials (Hall [13]; method [14]=[[kuznetsov-kuznetsova-2013]], [15]=[[kuznetsov-safonov-2014]]); C++/OpenMP on a 4-core/32 GB Linux/gcc box (1.5 h for X_0, 3 h for Y_0)."
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

# On applications of the Cayley graphs of some finite groups of exponent five

## Abstract

Let $B_0(2,5)$ be the largest two-generator finite Burnside group of exponent five. It has order $5^{34}$. The authors define an automorphism $\varphi$ which translates generating elements into their inverses. Let $C_{B_0(2,5)}(\varphi)$ be the centralizer of $\varphi$ in $B_0(2,5)$. It is known that $|C_{B_0(2,5)}(\varphi)| = 5^{16}$. The growth functions of the centralizer are computed for some generating sets. As the result the authors obtain diameters and average diameters of corresponding Cayley graphs of $C_{B_0(2,5)}(\varphi)$.

## TL;DR

For the **inversion** involution $\varphi:\,a_1\mapsto a_1^{-1},\ a_2\mapsto a_2^{-1}$ of $B_0(2,5)$ (order $5^{34}$), whose centralizer $C=C_{B_0(2,5)}(\varphi)$ has $|C|=5^{16}$ and splits as $C=C_0\times\langle z\rangle$ ($|C_0|=5^{15}$, $z$ a central element of $B_0(2,5)$ of order 5, $C_0=\langle X_0\rangle$ on 4 minimal generators — all from [[kuznetsov-filippov-2010-sjim]]), the paper (1) computes the **explicit Hall polynomials** $z_1,\dots,z_{15}$ over $\mathbb Z_5$ for $C_0$ (Theorem, on 15 commutators $a_1$–$a_{15}$ of weights 1–4), and (2) uses them, via the BFS growth algorithm of [[kuznetsov-2016]] and OpenMP parallelism, to compute the growth function of $C$ for two generating sets: **Corollary 1** — minimal $X=X_0\cup\{z\}$: $D_X(C)=29$, $\bar D_X(C)\approx21$; **Corollary 2** — symmetric $Y=X\cup X^{-1}$: $D_Y(C)=19$, $\bar D_Y(C)\approx14$. Shunkov's theorem ties finiteness of this centralizer to finiteness of the free $B(2,5)$.

## Problem

For $G=\langle X\rangle$, the ball $K_s$ of radius $s$ is the set of elements expressible as words of length $\le s$ over $X$; the growth function is $F(0)=|K_0|=1$, $F(s)=|K_s|-|K_{s-1}|$. The Cayley diameter is the largest $s_0$ with $F(s_0)>0$ (denoted $D_X(G)$); the average diameter is $\bar D_X(G)=\frac1{|G|}\sum_s s\,F(s)$. Computing the growth function of a large finite group is hard: finding a minimal word for a group element is NP-hard (Even–Goldreich), so worst-case cost is exponential in $|X|$.

$B_0(2,5)=\langle a_1,a_2\rangle$ is the maximal finite quotient of the free Burnside group $B(2,5)$, order $5^{34}$ [Havas–Wall–Wamsley]; whether $B(2,5)$ is finite is open, and if it is then $B(2,5)=B_0(2,5)$. Computing the growth of $B_0(2,5)$ itself ($5^{34}\approx5\cdot10^{23}$) is infeasible; only quotients of order $\le5^{17}$ had been done [[kuznetsov-2016]]. This paper attacks a tractable subgroup: the centralizer of the **inversion** involution. By Shunkov's theorem, finiteness of $C_{B(2,5)}(\varphi)$ would force $B(2,5)$ finite — motivating the study.

## Approach

- **The automorphism (verbatim).** $\varphi:\,a_1\to a_1^{-1},\ a_2\to a_2^{-1}$ — inverts both generators. It is an involutive automorphism of $B(2,5)$ and $B_0(2,5)$ (see [[kuznetsov-filippov-2010-sjim]]).
- **Centralizer structure (from [[kuznetsov-filippov-2010-sjim]], ref [11]).** (1) $|C|=5^{16}$; (2) $C=C_0\times\langle z\rangle$ with $|C_0|=5^{15}$, $|\langle z\rangle|=5$; (3) $z$ is a central element of $B_0(2,5)$; (4) $C_0=\langle X_0\rangle$ with $|X_0|=4$ the minimal number of generators; (5) a pc-presentation of $C_0$ is known.
- **Hall polynomials for $C_0$ (this paper's Theorem).** $C_0=\langle a_1,\dots,a_{15}\mid R\rangle$ with generators $a_1$–$a_4$, weight-2 commutators $a_5$–$a_9$, weight-3 $a_{10}$–$a_{12}$, weight-4 $a_{13}$–$a_{15}$. For each noncommuting pair $a_j^y a_i^x$ ($1\le i<j\le15$) one solves a $16\times16$ interpolation system over $\mathbb Z_5$ to get the collection-in-analytic-form polynomials $f_r^{(i,j)}(x,y)$; chaining them (formula 17) yields all $z_i$. A worked example is given for the 5-th commutator: the $16\times16$ matrix has rank 16, unique solution $\beta_{11}=1$ (rest 0), so $f_5^{(1,2)}(x,y)=xy$, i.e. $a_2^y a_1^x=(x,y,0,0,xy,0,\dots)$.
- **Computation.** Growth of $C_0$ in $X_0=\{a_1,a_2,a_3,a_4\}$ and $Y_0=X_0\cup X_0^{-1}$ via the BFS algorithm of [[kuznetsov-2016]] (ref [10]), elements multiplied fast by the Hall polynomials above; then the growth of $C=C_0\times\langle z\rangle$ in $X=X_0\cup\{z\}$ and $Y=X\cup X^{-1}$ follows. Implemented in C++ (symbolic parts in MATLAB), parallelized with **OpenMP**, run on a 4-core / 32 GB Linux / gcc machine: $\approx1.5$ h for $X_0$, $\approx3$ h for $Y_0$.

## Key result

**Theorem.** For $a_1^{x_1}\cdots a_{15}^{x_{15}}$ and $a_1^{y_1}\cdots a_{15}^{y_{15}}$ in $C_0$, the product exponents $z_i\in\mathbb Z_5$ are the Hall polynomials (formulas 1–15):

$$
\begin{aligned}
z_1&=x_1+y_1, & z_2&=x_2+y_2, & z_3&=x_3+y_3, & z_4&=x_4+y_4,\\
z_5&=x_5+y_5+x_2y_1+4x_3y_2, & z_6&=x_6+y_6+x_3y_1+4x_3y_2,\\
z_7&=x_7+y_7+x_4y_1, & z_8&=x_8+y_8+x_4y_2, & z_9&=x_9+y_9+x_4y_3,\\
z_{10}&=x_{10}+y_{10}+2x_3y_2+2x_4y_1+x_7y_4+3x_4^2y_1+x_4y_1y_4,\\
z_{11}&=x_{11}+y_{11}+4x_3y_2+2x_4y_2+x_8y_4+3x_4^2y_2+x_4y_2y_4,\\
z_{12}&=x_{12}+y_{12}+2x_3y_2+2x_4y_3+x_9y_4+3x_4^2y_3+x_4y_3y_4,\\
z_{13}&=x_{13}+y_{13}+3x_3y_2+2x_4y_1+2x_5y_4+x_7y_2+4x_8y_1+2x_7y_4+x_{10}y_4\\
&\quad+2x_4^2y_1+x_4^3y_1+3x_7y_4^2+3x_4y_1y_4^2+3x_4^2y_1y_4+2x_2x_4y_1+2x_2y_1y_4+x_4y_1y_2+4x_4y_1y_4,\\
z_{14}&=x_{14}+y_{14}+3x_3y_2+2x_4y_2+4x_6y_4+2x_7y_3+3x_9y_1+2x_8y_4+x_{11}y_4\\
&\quad+2x_4^2y_2+x_4^3y_2+3x_8y_4^2+3x_4y_2y_4^2+3x_4^2y_2y_4+4x_3x_4y_1+4x_3y_1y_4+2x_4y_1y_3+4x_4y_2y_4,\\
z_{15}&=x_{15}+y_{15}+x_3y_2+2x_4y_3+x_8y_3+4x_9y_2+2x_9y_4+x_{12}y_4+2x_4^2y_3\\
&\quad+x_4^3y_3+3x_9y_4^2+3x_4y_3y_4^2+3x_4^2y_3y_4+2x_3x_4y_2+2x_3y_2y_4+x_4y_2y_3+4x_4y_3y_4.
\end{aligned}
$$

Each $z_i$ has the Hall form $z_i=x_i+y_i+p_i(x_1,\dots,x_{i-1},y_1,\dots,y_{i-1})$.

**Corollary 1 (verbatim).** For the minimal generating set $X=X_0\cup\{z\}$: $D_X(C)=29,\ \bar D_X(C)\approx21$.

**Corollary 2 (verbatim).** For the symmetric generating set $Y=X\cup X^{-1}$: $D_Y(C)=19,\ \bar D_Y(C)\approx14$.

**Note on the automorphism.** $\varphi$ here is the **inversion** map $a_i\mapsto a_i^{-1}$, whose centralizer $C=C_0\times\langle z\rangle$ has $|C|=5^{16}$ — this is the automorphism of [[kuznetsov-filippov-2010-sjim]] (SJIM 2010). It is **distinct** from the **generator-swap** involution $a_1\leftrightarrow a_2$ of [[kuznetsov-kuznetsova-2017]], whose centralizer has $|C|=5^{17}$ (3 generators, from the VMJ 2010 paper). The two involutions give different centralizers ($5^{16}$ vs $5^{17}$).

## Assumptions

- Structural facts $|C|=5^{16}$, $C=C_0\times\langle z\rangle$, $|C_0|=5^{15}$, $z$ central of order 5, $C_0$ on 4 generators, and $C_0$'s pc-presentation are imported from [[kuznetsov-filippov-2010-sjim]]; not re-derived.
- The $16\times16$ interpolation systems over $\mathbb Z_5$ are full rank $\Rightarrow$ unique Hall polynomials.
- Word equality decided by pc-reduction; multiplication correct via the Hall-polynomial oracle.
- $X_0=\{a_1,a_2,a_3,a_4\}$ is a minimal generating set of $C_0$; $z$ extends it to $X$ for $C$.

## Limitations / scope

- Results are for the order-$5^{16}$ centralizer $C$, not $B_0(2,5)$ itself (order $5^{34}$, still out of reach).
- Growth functions are shown as figures (Fig. 1 for $X$, Fig. 2 for $Y$, each with a fitted Gaussian) — the full $F(s)$ tables are summarized only by the derived diameters $D$ and $\bar D$.
- Does not settle $B(2,5)$ finiteness (though Shunkov's theorem makes finiteness of this centralizer relevant to it).

## Replication evidence

No independent replication known as of 2026-05-28. The $z_1$–$z_{15}$ rest on full-rank $\mathbb Z_5$ interpolation (worked example $f_5^{(1,2)}=xy$ shown, rank 16); the centralizer structure is from [[kuznetsov-filippov-2010-sjim]] and the growth pipeline from [[kuznetsov-2016]] + [[kuznetsov-kuznetsova-2013]] / [[kuznetsov-safonov-2014]].

## Why this paper matters

This computes the full Cayley geometry of the order-$5^{16}$ centralizer of the **inversion** involution of $B_0(2,5)$: diameters $D_X(C)=29$ / $D_Y(C)=19$ and average diameters $\bar D_X\approx21$ / $\bar D_Y\approx14$, backed by explicit Hall polynomials $z_1$–$z_{15}$ that make multiplication in $C_0$ a fast closed-form operation. Together with [[kuznetsov-kuznetsova-2017]] (the generator-swap centralizer, $5^{17}$) it completes the pair of involution-centralizer Cayley computations in the Kuznetsov line. Shunkov's theorem gives it theoretical stake: finiteness of $C_{B(2,5)}(\varphi)$ is equivalent (in the relevant sense) to finiteness of the free Burnside group $B(2,5)$.

For the Mixer B(2,5) attack:
1. **Subgroup benchmarks** — any KB/normal-form system for $B(2,5)$ must, restricted to this centralizer, respect $D_X(C)=29$ / $D_Y(C)=19$.
2. **Fast-multiplication oracle** — the $z_1$–$z_{15}$ give a directly reusable closed-form product for $C_0$, of the same shape as the full-$B_0(2,5)$ Hall polynomials of [[kuznetsov-kuznetsova-2013]].

## Quotes

1. > "Consider the map $\varphi$ of the following form: $a_1\to a_1^{-1},\ a_2\to a_2^{-1}$." — §body
2. > "$C=C_0\times\langle z\rangle$ where $|C_0|=5^{15}$ and $|\langle z\rangle|=5$." — §body
3. > "Corollary 1. $D_X(C)=29$, $\bar D_X(C)\approx21$. Corollary 2. $D_Y(C)=19$, $\bar D_Y(C)\approx14$." — §Computer calculations

## Open questions surfaced

- The full growth-function tables $F(s)$ of $C$ (for $X$ and $Y$) are shown only as Gaussian-fitted figures — where are the tabulated values?
- How do $\bar D_X(C)\approx21$ / $\bar D_Y(C)\approx14$ (inversion, $5^{16}$) compare with the generator-swap centralizer's $\bar D_X\approx26.1$ ($5^{17}$, [[kuznetsov-kuznetsova-2017]])?
- Do the two centralizers ($5^{16}$ inversion vs $5^{17}$ swap) together bound the diameter of $B_0(2,5)$ from below?

## Related material in vault

- Extends: [[kuznetsov-filippov-2010-sjim]] (structural foundation of the inversion centralizer: $|C|=5^{16}$, $C=C_0\times\langle z\rangle$, $|C_0|=5^{15}$, 4 generators, pc-presentation — ref [11])
- Cites: [[kuznetsov-2015-cayley-exp3]] (ref [6], Cayley graphs of $B(k,3)$), [[kuznetsov-2016]] (ref [10], growth-function BFS algorithm), [[kuznetsov-kuznetsova-2013]] (ref [14], fast multiplication), [[kuznetsov-safonov-2014]] (ref [15], exponent-7 Hall polynomials), [[havas-wall-wamsley-1974]] (ref [8], order $5^{34}$). Other references: [1] Even–Goldreich, [2] Kuznetsov–Kuznetsova parallel-Cayley 2014, [3] Akers–Krishnamurthy, [4] Holt–Eick–O'Brien, [5] Camelo et al., [7] Kuznetsov–Kuznetsova period-4 2016, [9] Sims, [12] Shunkov, [13] Hall.
- Related (different automorphism): [[kuznetsov-kuznetsova-2017]] (Cayley graph of centralizer of the **generator-swap** involution $a_1\leftrightarrow a_2$; $|C|=5^{17}$, 3 generators)
- MOC: [[Research/Group theory/_MOCs/_moc-burnside]]
- Open problem: [[b25-finiteness-11.48-kostrikin]]

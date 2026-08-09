---
title: "Some subgroups of the Burnside group B₀(2,5)"
authors: A. A. Kuznetsov, A. S. Kuznetsova
year: 2021
venue: Prikladnaya Diskretnaya Matematika. Supplement
url: https://doi.org/10.17223/2226308X/14/43
url_fulltext: "https://www.mathnet.ru/php/getFT.phtml?jrnid=pdma&paperid=562&what=fullt&option_lang=eng"
url_translated:
language: ru
methodology_type: empirical
domain: group-theory
status: draft
citation_count: null
citation_count_date:
key_concepts:
  - "[[hall-polynomials]]"
  - "[[power-commutator-presentation]]"
extends:
  - "[[kuznetsov-2011]]"
contradicts: []
replicates: []
cites:
  - "[[havas-wall-wamsley-1974]]"
  - "[[kuznetsov-2011]]"
  - "[[kuznetsov-kuznetsova-2013]]"
cited_by: []
quality_notes: "3-page conference note (Prikl. Diskr. Mat. Suppl. 14, pp. 184–186, DOI 10.17223/2226308X/14/43). Original in Russian. RE-FILLED FROM FULL TEXT (mathnet getFT paperid=562, pdftotext — Cyrillic renders cleanly). CORRECTION to prior note: removed the spurious [[kuznetsov-shlepkin-2009]] cite (not a reference in this paper); the actual references are [1]=Shor, [2]=Baumslag–Fazio–Nicolosi, [3]=Fazio–Iga–Nicolosi (learning over exp-3 Burnside), [4]=Kahrobaei–Noce (Engel groups), [5]=[[havas-wall-wamsley-1974]], [6]=[[kuznetsov-2011]] (the H1 subgroup paper, IMM UrO RAN 2011), [7]=[[kuznetsov-kuznetsova-2013]] (Hall polynomials). Added cites [[kuznetsov-kuznetsova-2013]]. Content: B0(2,5)=⟨x,y⟩; subgroup series Hi=⟨ai,bi⟩ with a0=x,b0=y, ai=a_{i-1}b_{i-1}, bi=b_{i-1}a_{i-1}. Table (verbatim): H1(|H1|=5^14, N=6, E=5, nonabelian, =⟨xy,yx⟩); H2(5^6,4,4,no,=⟨xy²x,yx²y⟩); H3(5^3,2,2,no); H4(5^2,1,1,YES abelian). H4 abelian ⇒ H5 cyclic order 5 ⇒ series terminates. Explicit pc-presentation of H2 on c1..c6 (c1=a2,c2=b2) + Hall polynomials γ1..γ6 over Z5 (binomial-coefficient terms). a4=xy²xyx²y²x²yxy²x, b4=yx²yxy²x²y²xyx²y (length 16) generate an abelian order-25 subgroup; no two words of length <16 generate a noncyclic abelian subgroup in B0(2,5). Non-commutative-crypto framing (post-Shor). N_i=nilpotency class, E_i=Engel index."
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

# Some subgroups of the Burnside group B₀(2,5)

> **Translation note**: source paper is in Russian (`language: ru`). Abstract below is translated to English [trans.] from the mathnet.ru record.

## Abstract

The researchers examine a series of subgroups within the largest finite two-generator Burnside group of exponent five $B_0(2,5)$. Their investigation reveals that $H_4$ is a commutative group, while the subsequent subgroup breaks this pattern. They identify two elements of length 16 that generate an abelian subgroup of order 25 in $B_0(2,5)$. Computer analysis confirms there is no other pair of group words of length less than 16 that generate a noncyclic abelian subgroup in $B_0(2,5)$. [trans.]

## TL;DR

Studies the **subgroup series** $H_i=\langle a_i,b_i\rangle$ of $B_0(2,5)=\langle x,y\rangle$ defined by $a_0=x$, $b_0=y$, $a_i=a_{i-1}b_{i-1}$, $b_i=b_{i-1}a_{i-1}$. Computer computation gives the table $|H_1|=5^{14},|H_2|=5^6,|H_3|=5^3,|H_4|=5^2$ with nilpotency classes $6,4,2,1$; **$H_4$ is abelian**, so $H_5$ is cyclic of order 5 and the series terminates. Concretely, $a_4=xy^2xyx^2y^2x^2yxy^2x$ and $b_4=yx^2yxy^2x^2y^2xyx^2y$ (both length 16) generate an **abelian subgroup of order 25**, and an exhaustive search shows **no two words of length $<16$ generate a noncyclic abelian subgroup** of $B_0(2,5)$. Includes the full pc-presentation and explicit Hall polynomials of $H_2$. Motivated by non-commutative (post-Shor) cryptography.

## Problem

Post-Shor, commutative-group cryptosystems (RSA, Diffie–Hellman, ECC) are quantum-broken, motivating **non-commutative** platforms; exponent-3 Burnside groups have been proposed (Baumslag–Fazio, Fazio–Iga, Kahrobaei–Noce), but $n>3$ is unexplored, and the finiteness of $B(2,5)$ is itself open. Inside $B_0(2,5)=\langle x,y\rangle$ (the maximal finite two-generator exponent-5 group, order $5^{34}$; if $B(2,5)$ is finite then $B(2,5)=B_0(2,5)$), which subgroups in the natural self-referential series $H_i=\langle a_i,b_i\rangle$ (with $a_i=a_{i-1}b_{i-1}$, $b_i=b_{i-1}a_{i-1}$) are abelian, and **what is the shortest pair of words generating a noncyclic abelian subgroup**?

## Approach

- **Subgroup series.** $H_i=\langle a_i,b_i\rangle$, $a_0=x$, $b_0=y$, $a_i=a_{i-1}b_{i-1}$, $b_i=b_{i-1}a_{i-1}$ for $i\in\mathbb N$. Word length of $(a_i,b_i)$ doubles each step (1, 2, 4, 8, 16, …).
- **Computer computation** (via the pc-presentation of $B_0(2,5)$, [[havas-wall-wamsley-1974]]) gives, for each $H_i$: order $|H_i|$, nilpotency class $N_i$, Engel index $E_i$, and whether $H_i$ is abelian.
- **$H_2$ worked out explicitly.** $H_2=\langle a_2,b_2\rangle=\langle xy^2x,\,yx^2y\rangle$ has a pc-presentation on $c_1,\dots,c_6$ ($c_1=a_2$, $c_2=b_2$; $c_3,\dots,c_6$ recursive commutators) with Hall polynomials computed by the algorithm of [[kuznetsov-kuznetsova-2013]].
- **Exhaustive minimal-length search** confirms 16 is the shortest word length yielding a noncyclic abelian subgroup.

## Key result

**Subgroup-series table (verbatim, computer-computed):**

| $i$ | $(a_i,b_i)$ | $\lvert H_i\rvert$ | $N_i$ | $E_i$ | $H_i$ abelian? |
|---|---|---|---|---|---|
| 1 | $xy,\ yx$ | $5^{14}$ | 6 | 5 | No |
| 2 | $xy^2x,\ yx^2y$ | $5^{6}$ | 4 | 4 | No |
| 3 | $xy^2xyx^2y,\ yx^2yxy^2x$ | $5^{3}$ | 2 | 2 | No |
| 4 | $xy^2xyx^2y^2x^2yxy^2x,\ yx^2yxy^2x^2y^2xyx^2y$ | $5^{2}$ | 1 | 1 | **Yes** |

($N_i$ = nilpotency class, $E_i$ = Engel index.) Since $H_4$ is abelian, $H_5$ is **cyclic of order 5** and the series terminates. $H_1$ (order $5^{14}$) was studied earlier in [[kuznetsov-2011]].

**Minimal noncyclic-abelian length.** $a_4=xy^2xyx^2y^2x^2yxy^2x$ and $b_4=yx^2yxy^2x^2y^2xyx^2y$, each of **length 16**, generate an **abelian subgroup of order 25** ($\cong\mathbb Z_5\times\mathbb Z_5$, since $B_0(2,5)$ has exponent 5). Computer search confirms **no other pair of words of length $<16$** generates a noncyclic abelian subgroup of $B_0(2,5)$.

**Hall polynomials of $H_2$ (verbatim).** pc-relations: $c_i^5=1$, $[c_2,c_1]=c_3$, $[c_3,c_1]=c_4$, $[c_3,c_2]=c_5$, $[c_4,c_1]=c_6$, $[c_5,c_2]=c_6^4$ (all other basic commutators trivial). For $c_1^{\alpha_1}\cdots c_6^{\alpha_6}\cdot c_1^{\beta_1}\cdots c_6^{\beta_6}=c_1^{\gamma_1}\cdots c_6^{\gamma_6}$ over $\mathbb Z_5$:

$$
\begin{aligned}
\gamma_1 &= \alpha_1+\beta_1,\qquad \gamma_2 = \alpha_2+\beta_2,\\
\gamma_3 &= \alpha_3+\beta_3+\alpha_2\beta_1,\\
\gamma_4 &= \alpha_4+\beta_4+\tbinom{\beta_1}{2}\alpha_2+\alpha_3\beta_1,\\
\gamma_5 &= \alpha_5+\beta_5+\tbinom{\alpha_2}{2}\beta_1+\alpha_3\beta_2+\alpha_2\beta_1\beta_2,\\
\gamma_6 &= \alpha_6+\beta_6+\tbinom{\beta_1}{2}\alpha_3+\tbinom{\beta_1}{3}\alpha_2+4\tbinom{\alpha_2}{2}\beta_1+4\tbinom{\beta_2}{2}\alpha_3+\alpha_4\beta_1+4\alpha_5\beta_2+4\tbinom{\beta_1}{2}\alpha_2\beta_2+4\tbinom{\beta_2}{2}\alpha_2\beta_1.
\end{aligned}
$$

## Assumptions

- Works in $B_0(2,5)$ (finite, order $5^{34}$, [[havas-wall-wamsley-1974]]); pc-presentation via GAP.
- Exhaustive search over words of length $<16$ is computationally feasible; multiplication via the Hall-polynomial oracle of [[kuznetsov-kuznetsova-2013]].

## Limitations / scope

- Specific to $B_0(2,5)$; no claim about the free $B(2,5)$ or general exponent-5 groups.
- Explicit Hall polynomials given only for $H_2$; the other $H_i$ are summarized by the table.
- Conference supplement (3 pp); no timings or hardware reported.

## Replication evidence

No independent replication known. The subgroup orders/nilpotency data and the length-16 minimal pair are directly checkable in GAP/Magma from the $B_0(2,5)$ pc-presentation.

## Why this paper matters

Two concrete structural benchmarks for $B_0(2,5)$: (1) the self-referential series $H_i=\langle a_i,b_i\rangle$ collapses to abelian at $H_4$ (order $5^2$) and cyclic at $H_5$; (2) the shortest noncyclic-abelian generating pair has **length 16** (the explicit $a_4,b_4$, generating $\mathbb Z_5\times\mathbb Z_5$).

For the Mixer B(2,5) pipeline these are hard sanity checks: any KB rule set that (a) equates two words of length $<16$ into a noncyclic abelian relation, or (b) disagrees with the $H_2$ Hall polynomials above, signals a computation bug. The paper extends [[kuznetsov-2011]] (the $H_1$, order-$5^{14}$ case) to the full descending series and the abelian frontier.

## Quotes

Full text is in Russian; content above is paraphrased/translated [trans.] from the getFT PDF (pp. 184–186). Verbatim table and Hall polynomials reproduced under Key result.

## Open questions surfaced

- What is the minimum noncyclic-abelian length in $B(2,5)$ (the free Burnside group, if finite)? If $B(2,5)\cong B_0(2,5)$ it must equal 16.
- Is the order-25 abelian subgroup generated by the length-16 pair unique up to conjugacy?
- Why does $|H_i|$ drop $5^{14}\to5^6\to5^3\to5^2$ — is there a clean formula for $|H_i|$ / $N_i$ in terms of the doubling recursion?

## Related material in vault

- Extends: [[kuznetsov-2011]] (the $H_1=\langle xy,yx\rangle$ subgroup, order $5^{14}$ — ref [6])
- Cites: [[havas-wall-wamsley-1974]] (order $5^{34}$, pc-basis — ref [5]), [[kuznetsov-kuznetsova-2013]] (Hall-polynomial fast multiplication — ref [7]). Crypto-context refs: [1] Shor, [2] Baumslag–Fazio–Nicolosi, [3] Fazio–Iga–Nicolosi (learning over exp-3 Burnside), [4] Kahrobaei–Noce (Engel groups).
- MOC: [[Research/Group theory/_MOCs/_moc-burnside]]
- Open problem: [[b25-finiteness-11.48-kostrikin]]

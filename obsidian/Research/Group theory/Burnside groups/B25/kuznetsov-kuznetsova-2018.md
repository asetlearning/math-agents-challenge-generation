---
title: "A resource-efficient algorithm for study the growth in finite two-generator groups of exponent 5"
authors: A. A. Kuznetsov, A. S. Kuznetsova
year: 2018
venue: Prikladnaya Diskretnaya Matematika
url: https://doi.org/10.17223/20710410/42/7
url_fulltext: "https://www.mathnet.ru/php/getFT.phtml?jrnid=pdm&paperid=645&what=fullt&option_lang=eng"
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
  - "[[kuznetsov-2016]]"
  - "[[kuznetsov-kuznetsova-2013]]"
contradicts: []
replicates: []
cites:
  - "[[havas-wall-wamsley-1974]]"
  - "[[kuznetsov-2016]]"
  - "[[kuznetsov-kuznetsova-2013]]"
cited_by: []
quality_notes: "Full journal paper (Prikl. Diskr. Mat. 42, pp. 94–103, 10 pp.), bilingual RU/EN header. RE-FILLED FROM FULL TEXT (mathnet getFT paperid=645, pdftotext — Cyrillic renders cleanly). Contribution: Algorithm 1 (Ball, radius-limited A-I of ref [1]), Algorithm 2 (QuotientGrowthFunction — coset-ball growth), Algorithm 3 (GrowthFunction — combines 1+2), with Lemmas 1–5 and Theorem 1 giving the complexity: T3∈O(|G|·|Ks|²), M3∈Θ(|Ks|+|Q|+|N|), min(M3)∈Θ(max(|Ks|,|G|^{1/2})) at |Q|_opt=|G|^{1/2}. Remark 2: pick s so |Ks|~|G|^{2/3} ⇒ T3∈O(|G|^{7/3}), M3∈Θ(|G|^{2/3}) vs base A-I T0∈Θ(|G|²), M0∈Θ(|G|). Remark 1: boolean-vector numbering ⇒ T3'∈O(|Q|·|Ks|²). Remark 3: Sims automorphism-orbit trick (orbit reps Q0, multiplicities l(q), parallelizable). Motivation: A-I from [1] ran out of memory on B18 (5^18≈4·10^12) despite 1.2 TB RAM + 10 TB disk. Verbatim results table: B18=⟨A4⟩ D=36 D̄=29 (|A|=16,|Q|=5^8,|Q0|=25311, 62 h, 8 GB); B18=⟨A2⟩ D=55 D̄=44 (|A|=2,|Q|=5^8,|Q0|=195375, 20 days, 11 GB); B19=⟨A4⟩ D=38 D̄=31 (|A|=8,|Q|=5^10,|Q0|=1226797, 44 days, 25 GB). Hypothesis 1: D_A2(B0(2,5))≈105, D_A4(B0(2,5))≈69 (linear extrapolation of D_Ai(Bk), Figs. 4–5). C++/OpenMP, two 16-core CPUs / 64 GB / Linux / gcc. Refs: [1]=kuznetsov-2016, [2]=Kuznetsov–Kuznetsova parallel-Cayley Vestnik SibGAU 2014, [3]=Even–Goldreich (NP-hardness), [4]=Skiena, [5]=Sims fast-mult, [6]=Havas–Wall–Wamsley, [7]=Sims KB, [8]=Holt–Eick–O'Brien, [9]=[[kuznetsov-kuznetsova-2013]] (Hall polynomials). Added cites [[kuznetsov-kuznetsova-2013]]."
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

# A resource-efficient algorithm for study the growth in finite two-generator groups of exponent 5

> **Translation note**: source paper is in Russian (`language: ru`). Abstract below is translated to English [trans.] from the mathnet.ru record.

## Abstract

The paper presents a modified algorithm for investigating growth patterns in finite groups that reduces space complexity while maintaining acceptable time efficiency. The approach involves selecting a suitable subgroup $N$ within group $G$ where $|N| \ll |G|$, independently calculating growth functions for cosets $gN$, then aggregating results to obtain the group's growth function. Researchers applied this method to compute growth functions for quotient groups $B_{18}$ and $B_{19}$, derived from $B_0(2,5)$ — the largest two-generator Burnside group of exponent 5 (order $5^{34}$). Results suggest the diameters of Cayley graphs of the group $B_0(2,5)$ are approximately 105 and 69 for two-generator and four-generator sets respectively. [trans.]

## TL;DR

A **space-efficient** growth-function algorithm (**Algorithm 3 `GrowthFunction`**) that computes the growth function / Cayley diameter of a large finite group $G$ **coset-by-coset** instead of storing the whole Cayley ball. It builds a radius-$s$ ball once (**Algorithm 1 `Ball`**), then for each coset $qN$ of a subgroup $N$ computes the coset growth function (**Algorithm 2 `QuotientGrowthFunction`**) and sums. **Theorem 1**: correctness plus $T_3\in O(|G|\cdot|K_s|^2)$, $M_3\in\Theta(|K_s|+|Q|+|N|)$, and $\min_{|Q|}(M_3)\in\Theta(\max(|K_s|,|G|^{1/2}))$ at $|Q|_{\mathrm{opt}}=|G|^{1/2}$. It reaches $B_{18}$ ($5^{18}$) and $B_{19}$ ($5^{19}$) — where the earlier algorithm A-I ran out of memory despite 1.2 TB RAM + 10 TB disk. From the computed diameters $D_{A_i}(B_k)$ (linear fit, Figs. 4–5) comes **Hypothesis 1: $D_{A_2}(B_0(2,5))\approx105$, $D_{A_4}(B_0(2,5))\approx69$**.

## Problem

For $G=\langle X\rangle$ the ball $K_s$ is all elements expressible as irreducible words of length $\le s$; $F_i=|P_i|$ (sphere of radius $i$) is the growth function, and the largest $s_0$ with $F_{s_0}>0$ is the Cayley diameter $D_X(G)$, average diameter $\bar D_X(G)=\frac1{|G|}\sum s\,F_s$. Computing $F$ for a large finite group is hard: finding a minimal word is NP-hard (Even–Goldreich). The base algorithm A-I of [[kuznetsov-2016]] stores the entire ball, so with $\sim$ a few bytes per element and 1 TB one can only reach $\sim10^{12}$ elements. Applying A-I to $B_{18}=B_0(2,5)/\langle a_{19},\dots,a_{34}\rangle$ ($5^{18}\approx4\cdot10^{12}$) **failed on memory** even with 1.2 TB RAM + 10 TB disk. Goal: **cut the space complexity** while keeping time acceptable, so larger quotients become reachable.

Here $B_0(2,5)=\langle a_1,a_2\rangle$ has order $5^{34}$ [[havas-wall-wamsley-1974]]; every $g$ is a unique pc-word $a_1^{\alpha_1}\cdots a_{34}^{\alpha_{34}}$ ($\alpha_i\in\mathbb Z_5$), and $B_k=B_0(2,5)/\langle a_{k+1},\dots,a_{34}\rangle$ has $|B_k|=5^k$.

## Approach

**Algorithm 1 `Ball`$(G,X,s)$.** BFS building the radius-$s$ ball $K_s=\bigcup_{i\le s}P_i$ (radius-limited version of A-I). *Lemma 2*: $T_1\in\Theta(|K_s|^2)$, $M_1\in\Theta(|K_s|)$.

**Algorithm 2 `QuotientGrowthFunction`$(K_s,Q,q)$.** For $Q=G/N$ with homomorphism $\varphi$ and kernel $N$, define per-coset spheres $P_i(q)=\{g\in P_i:\varphi(g)=q\}$ and balls $K_s(q)$. Given the whole-group ball $K_s$, a quotient $Q$, and $q\in Q$, it returns the growth function $F(q)$ of the coset ball $K_{2s}(q)$ of radius $2s$. Key step: for $i>s$ it does **not** build whole-group balls; instead it forms $g=g_1\cdot g_2$ with $g_1\in P_{i-s}(u)$, $g_2\in P_s(v)$, $u\circ v=q$, and stops when $|K_i(q)|=|N|$. *Lemma 4*: $T_2\in O(|N|\cdot|K_s|^2)$, $M_2\in\Theta(|K_s|+|Q|+|N|)$. *Lemma 5*: $\min_{|Q|}(M_2)\in\Theta(\max(|K_s|,|G|^{1/2}))$ at $|Q|_{\mathrm{opt}}=|G|^{1/2}$ (minimize $|K_s|+|Q|+|G|/|Q|$).

**Algorithm 3 `GrowthFunction`$(G,X,Q,s)$.** Combine: build $K_s$ once, then for each $q\in Q$ add $F(q)$ to $F(G)$.

**Remark 1** (boolean-vector numbering): number the elements of $K_{2s}(q)$ as in [[kuznetsov-2016]], store the coset ball as a bit-vector of dimension $|N|$ ⇒ 1 bit/element, $O(1)$ membership ⇒ $T_3'\in O(|Q|\cdot|K_s|^2)$.
**Remark 3** (Sims trick [5]): let $A$ be length-preserving automorphisms fixing $X$ (e.g. inversion when $X$ is symmetric); if $N$ is $A$-invariant, take one representative per $A$-orbit of $Q$ (set $Q_0$, orbit sizes $l(q)$) and only compute $F(q)$ for $q\in Q_0$, weighting by $l(q)$ — trivially parallelizable.

**Computation.** C++/OpenMP, Hall-polynomial multiplication [[kuznetsov-kuznetsova-2013]], $A,Q,Q_0,l(q)$ found via GAP; two 16-core CPUs / 64 GB / Linux / gcc. Run on $B_{18}$ (both $A_2$ and $A_4$) and $B_{19}$ ($A_4$), where $A_2=\{a_1,a_2\}$ (minimal) and $A_4=\{a_1,a_1^{-1},a_2,a_2^{-1}\}$ (symmetric).

## Key result

**Theorem 1** (complexity of Algorithm 3): correct, and
1. $T_3\in O(|G|\cdot|K_s|^2)$;
2. $M_3\in\Theta(|K_s|+|Q|+|N|)$;
3. $\min_{|Q|}(M_3)\in\Theta(\max(|K_s|,|G|^{1/2}))$ at $|Q|_{\mathrm{opt}}=|G|^{1/2}$.

**Remark 2** (practical regime): experiments show taking $s$ with $|K_s|\sim|G|^{2/3}$ (so $|Q|\sim|G|^{1/2}$) gives $T_3\in O(|G|^{7/3})$, $M_3\in\Theta(|G|^{2/3})$ — vs. base A-I $T_0\in\Theta(|G|^2)$, $M_0\in\Theta(|G|)$; for large groups $M_3\ll M_0$.

**Computed diameters (verbatim table):**

| Group | $D$ | $\bar D$ | Algorithm parameters | Time | Memory |
|---|---|---|---|---|---|
| $B_{18}=\langle A_4\rangle$ | 36 | 29 | $\lvert A\rvert=16,\ \lvert Q\rvert=5^8,\ \lvert Q_0\rvert=25311$ | 62 h | 8 GB |
| $B_{18}=\langle A_2\rangle$ | 55 | 44 | $\lvert A\rvert=2,\ \lvert Q\rvert=5^8,\ \lvert Q_0\rvert=195375$ | 20 days | 11 GB |
| $B_{19}=\langle A_4\rangle$ | 38 | 31 | $\lvert A\rvert=8,\ \lvert Q\rvert=5^{10},\ \lvert Q_0\rvert=1226797$ | 44 days | 25 GB |

**Hypothesis 1** (linear extrapolation of $D_{A_2}(B_k)$, $D_{A_4}(B_k)$, Figs. 4–5): $D_{A_2}(B_0(2,5))\approx\mathbf{105}$ and $D_{A_4}(B_0(2,5))\approx\mathbf{69}$.

## Assumptions

- $B_0(2,5)$ finite of order $5^{34}$ [[havas-wall-wamsley-1974]]; pc-presentation via GAP; $B_k$ quotients well-defined.
- $N$ chosen $A$-invariant with $|N|\approx|G|^{1/2}$ for the memory optimum; length-preserving automorphism group $A$ known (GAP).
- Multiplication correct via the Hall polynomials of [[kuznetsov-kuznetsova-2013]].

## Limitations / scope

- Diameters computed exactly only for $B_{18}$, $B_{19}$; the values 105 and 69 for $B_0(2,5)$ (order $5^{34}$) are a **linear extrapolation** (Hypothesis 1), not computed.
- Time cost is large ($B_{18}=\langle A_2\rangle$: 20 days; $B_{19}=\langle A_4\rangle$: 44 days).

## Replication evidence

No independent replication known. The $B_{18}$/$B_{19}$ diameters (36/55/38) are directly reproducible by any tool computing growth functions for those quotients; the multiplication oracle is the previously-verified [[kuznetsov-kuznetsova-2013]].

## Why this paper matters

This is the memory barrier-breaking step in the Kuznetsov growth-function line: coset-decomposition ($M_3\in\Theta(|G|^{2/3})$ vs $M_0\in\Theta(|G|)$) is what lets the computation cross $5^{18}$, and it yields the headline **diameter estimates $\approx105$ (minimal $A_2$) and $\approx69$ (symmetric $A_4$)** for $B_0(2,5)$.

For the Mixer B(2,5) attack:
1. **Bound on rule coverage / search depth**: a system that has resolved $B_0(2,5)$ must reduce any word up to the diameter; $\approx105$ ($A_2$) / $\approx69$ ($A_4$) set the target length scale.
2. **Meet-in-the-middle window**: for a bidirectional search on a target commutator, each side must reach $\approx$ half the diameter.
3. **Algorithm validation**: the exact $B_{18}$/$B_{19}$ diameters (36/55/38, $\bar D$ 29/44/31) are hard benchmarks any future growth tool can check.

## Quotes

Full text is in Russian; content above is paraphrased/translated [trans.] from the getFT PDF (pp. 94–103). Verbatim numeric table reproduced under Key result.

## Open questions surfaced

- What is the exact diameter of $B_0(2,5)$ (at $k=34$)? Is it close to the extrapolated 105 / 69?
- Is the ratio $D_{A_2}(B_k)/D_{A_4}(B_k)$ (here $\approx105/69\approx1.52$) stable across $k$?
- Can Algorithm 3 (with Remark 3 parallelism) be pushed to $k>19$ on larger clusters, and does the linear fit hold there?

## Related material in vault

- Extends: [[kuznetsov-2016]] (base algorithm A-I; this is the memory-efficient modification — ref [1]), [[kuznetsov-kuznetsova-2013]] (Hall-polynomial fast multiplication — ref [9])
- Cites: [[havas-wall-wamsley-1974]] (order $5^{34}$, pc-basis — ref [6]). Other refs: [2] Kuznetsov–Kuznetsova parallel-Cayley (Vestnik SibGAU 2014), [3] Even–Goldreich (NP-hardness), [4] Skiena, [5] Sims *Fast multiplication and growth in groups*, [7] Sims *Computation with Finitely Presented Groups*, [8] Holt–Eick–O'Brien.
- Related: [[kuznetsov-2019]] (subgroup-geometry refinement of the diameter hypothesis; uses Algorithms 1–3 of this paper)
- MOC: [[Research/Group theory/_MOCs/_moc-burnside]]
- Open problem: [[b25-finiteness-11.48-kostrikin]]

---
title: "On an involutive automorphism of the Burnside group B₀(2,5)"
authors: A. A. Kuznetsov, K. A. Filippov
year: 2010
venue: Sibirskii Zhurnal Industrial'noi Matematiki
url: http://mi.mathnet.ru/sjim625
url_translated:
language: ru
methodology_type: empirical
domain: group-theory
status: draft
citation_count: null
citation_count_date:
key_concepts: []
extends:
  - "[[kuznetsov-shlepkin-2010]]"
contradicts: []
replicates: []
cites:
  - "[[havas-wall-wamsley-1974]]"
  - "[[kuznetsov-shlepkin-2009]]"
cited_by:
  - "[[kuznetsov-kuznetsova-2017]]"
  - "[[kuznetsov-safonov-2018]]"
quality_notes: "Full journal paper (Sib. Zh. Ind. Mat. 13:3, pp. 68–75, 8 pages). Filled from FULL TEXT (mathnet getFT PDF, ru, pdftotext extraction). Original in Russian. Companion to [[kuznetsov-filippov-2010-vmj]] (same authors, same year, Vladikavkaz Mat. Zh. 12:4, 5pp) — this 8-page version is the fuller treatment with the complete computer-algebra proof (explicit action of φ on all 34 basis commutators, the linear-system-over GF(5) reduction, explicit generators x₁…x₅ and central series). All numeric invariants below are now verbatim from the theorem, not inferred from downstream citations."
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
  - topic/center-of-group
  - topic/finite-group-enumeration
  - paper
  - status/draft
project: b25
---

# On an involutive automorphism of the Burnside group B₀(2,5)

> **Translation note**: source paper is in Russian (`language: ru`). Abstract below is translated to English [trans.] from the mathnet.ru record.

## Abstract

We study the centralizer of the involutive automorphism of the Burnside group $B_0(2,5)$ mapping the generators of $B_0(2,5)$ to their inverses. For this centralizer we find generating elements and compute its order, solvability length, and nilpotency length. [trans.]

## TL;DR

Explicit computer-algebra determination of the centralizer $C = C_{B_0(2,5)}(\varphi)$ of the inversion automorphism $\varphi: x \mapsto x^{-1}, y \mapsto y^{-1}$ of the restricted Burnside group $B_0(2,5)$ (which has order $5^{34}$). Main theorem: $|C| = 5^{16}$; $C = X \times \langle x_5\rangle$ where $\langle x_5\rangle$ is the center of $B_0(2,5)$ and $X = \langle x_1,x_2,x_3,x_4\rangle$ has order $5^{15}$ with a normal abelian subgroup $H_2$ of order $5^{11}$ and $X/H_2$ elementary abelian of rank 4; $C$ needs a minimum of **5 generators**, has **solvability length 2** and **nilpotency length 4**. The paper also gives the full power-commutator presentation of $X$ and both central series.

## Problem

What is the structure of the fixed-point subgroup (centralizer) $C = \{g \in B_0(2,5) : \varphi(g) = g\}$ of the canonical inversion automorphism $\varphi: x \mapsto x^{-1}, y \mapsto y^{-1}$ in the restricted Burnside group $B_0(2,5)$? $B_0(2,5) = F_2/U(2,5)$ is the largest finite two-generator group of exponent 5; it has order $5^{34}$ (Havas–Wall–Wamsley). Since $(2,5)$ is the smallest open pair of the Burnside problem, $B_0(2,5)$ is of special interest, and $\varphi$ is a representative of one of the two classes of involutive automorphisms of $B_0(2,5)$.

## Approach

Direct computer-algebra computation using the **normal commutator word** representation of $B_0(2,5)$ from Havas–Wall–Wamsley [[havas-wall-wamsley-1974]] and [[kuznetsov-shlepkin-2009]]: every $g$ is written uniquely as $g = c_1^{\alpha_1} c_2^{\alpha_2}\cdots c_{34}^{\alpha_{34}}$ with $\alpha_i\in\{0,1,2,3,4\}$ over 34 basis commutators (the first two are the generators). Steps:

1. Compute the action of $\varphi$ on each of the 34 basis commutators (given verbatim as 34-vectors in the paper).
2. Basis commutators 11–34 commute and generate a characteristic normal abelian subgroup $H$; so fixing $\varphi(g)=g$ splits into (a) a finite enumeration over commutators 1–10 (yielding exactly **625** admissible "heads" $v_k$) and (b) for each, solving the linear system $(A-E)\alpha = -b_k$ over $\mathrm{GF}(5)$ for the exponents of commutators 11–34.
3. The matrix $A-E$ has rank 12; all 625 augmented systems are consistent with $24-12=12$ free parameters, giving $5^{12}$ solutions each, hence $625\cdot 5^{12} = 5^{16}$ total.

## Key result

**Theorem (verbatim, [trans.]).** For $C$ the following hold:
1. $|C| = 5^{16}$.
2. $C = X \times \langle x_5\rangle$, where $\langle x_5\rangle$ is the center of $B_0(2,5)$ and $X = \langle x_1, x_2, x_3, x_4\rangle$ satisfies: (a) $X$ has a normal abelian subgroup $H_2$ with $|H_2| = 5^{11}$; (b) $X/H_2 = \langle x_1 H_2\rangle \times \langle x_2 H_2\rangle \times \langle x_3 H_2\rangle \times \langle x_4 H_2\rangle$; (c) $|X| = 5^{15}$.
3. $5$ is the minimum number of generators of $C$.
4. The solvability length and nilpotency length of $C$ are $2$ and $4$ respectively.

Additional explicit content in the proof:
- Explicit generators $x_1,\dots,x_4$ (as 34-vectors) and the central element $x_5$.
- Derived series: $C^{(1)}=[C,C]=H_2$, $C^{(2)}=e$ (so solvability length 2). Nilpotency length 4 witnessed by $[x_4,x_1,x_4,x_4]=h_9\neq e$ while all weight-5 commutators vanish.
- Full power-commutator presentation of $X$ on 15 basis commutators $k_1,\dots,k_{15}$, with all nontrivial relations listed.
- Lower central series $C \supset C_1 \supset C_2 \supset C_3 \supset C_4=e$ with $C_1=H_2$, and upper central series $e=Z_0\subset Z_1\subset Z_2\subset Z_3\subset Z_4=C$ with $Z_i = C_{4-i}\times\langle x_5\rangle$ for $i=1,2,3$.

## Assumptions

- $\varphi$ is the specific inversion automorphism $x \mapsto x^{-1}, y \mapsto y^{-1}$ (well-defined on $B_0(2,5)$ because $U(2,5)$ is $\varphi$-admissible).
- The Havas–Wall–Wamsley normal-commutator presentation of $B_0(2,5)$ ([[havas-wall-wamsley-1974]], via [[kuznetsov-shlepkin-2009]]) is the computational substrate.
- Correctness rests on the reported computer computations (the 34 action-vectors, the $\mathrm{GF}(5)$ rank computations).

## Limitations / scope

- Specific to the inversion automorphism. A different order-2 automorphism (the generator-swap $x\leftrightarrow y$) is studied elsewhere in the cluster and yields a different centralizer.
- About $B_0(2,5)$ (restricted Burnside), not directly $B(2,5)$; the two coincide iff the Burnside problem for $(2,5)$ is positive, which is exactly the open question.
- Purely computational/enumerative — no rank-independent or structural-for-all-$n$ argument.

## Replication evidence

`no` (independent replication) — NOTE: the sister paper [[kuznetsov-filippov-2010-vmj]] does NOT replicate this; it treats the *other* involution (generator-swap, $|C|=5^{17}$, nilp 6, solv 3, 3 gens). Downstream papers ([[kuznetsov-safonov-2018]], [[kuznetsov-kuznetsova-2017]]) use $|C|=5^{16}$ for the inversion case as a known input, corroborating *this* paper's number.

## Why this paper matters

The centralizer of the inversion automorphism is a canonical subgroup of $B_0(2,5)$: the fixed-point set of the most natural order-2 symmetry. This paper pins down its complete structure — order $5^{16}$, the direct decomposition $C = X\times Z(B_0(2,5))$, minimum generator count 5, solvability length 2, nilpotency length 4, and both central series — as a fully explicit computer-algebra result. For the algo_mixing / B25 program it is a concrete, checkable structural invariant: any tool claiming to compute in $B_0(2,5)$ or $B(2,5)$ must reproduce $|C_{B_0(2,5)}(\varphi)| = 5^{16}$ and the derived/central series above. The linear-algebra-over-$\mathrm{GF}(5)$ reduction (fixing the abelian tail via a rank-12 system, enumerating 625 heads) is a reusable template for automorphism-centralizer computations in these groups.

## Quotes

1. > "For $C$ the following statements hold: 1) $|C| = 5^{16}$." — Theorem [trans.]
2. > "The solvability and nilpotency lengths of $C$ equal two and four respectively." — Theorem [trans.]

## Open questions surfaced

- The inversion-centralizer is $5^{16}$; the generator-swap involution gives a different order — is there a uniform description of centralizers across all involutive automorphism classes of $B_0(2,5)$?
- Does the rank-12 structure of $A-E$ over $\mathrm{GF}(5)$ (i.e. exactly half of the 24 "tail" commutators being pinned) have a representation-theoretic explanation, or is it an artifact of this particular presentation?

## Related material in vault

- Extends: [[kuznetsov-shlepkin-2009]], [[kuznetsov-shlepkin-2010]] (prior B₀(2,5) computation)
- Cites: [[havas-wall-wamsley-1974]], [[kuznetsov-shlepkin-2009]]
- Cited by: [[kuznetsov-kuznetsova-2017]], [[kuznetsov-safonov-2018]] (Cayley graph extensions)
- Sister paper (different involution — NOT a replicate): [[kuznetsov-filippov-2010-vmj]] (generator-swap involution, $|C|=5^{17}$)
- MOC: [[Research/Group theory/_MOCs/_moc-burnside]]

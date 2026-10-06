---
title: "Generic-case complexity, decision problems in group theory and random walks"
authors: Ilya Kapovich, Alexei Myasnikov, Paul Schupp, Vladimir Shpilrain
year: 2003
venue: "Journal of Algebra 264 (2003) 665–694; arXiv:math/0203239 (v3, 10 Jun 2002)"
url: https://arxiv.org/abs/math/0203239
url_translated:
language: en
domain: group-theory
status: draft
methodology_type: theoretical
citation_count: 192
citation_count_date: 2026-10-05
key_concepts:
  - "[[dehn-function]]"
extends: []
contradicts: []
replicates: []
cites: []
cited_by:
  - "[[myasnikov-ushakov-2011-random-van-kampen]]"
quality_notes: "Foundational paper of generic-case complexity in group theory (192 citations, Semantic Scholar, 2026-10-05). DOI 10.1016/S0021-8693(03)00167-4. Summary written from the arXiv v3 full text; section/page numbers refer to that version. The Stevens author PDF is a 2-page fragment, not the full paper."
author: asetlearning
project: challenge-gen
tags:
  - agent/research
  - user/asetlearning
  - domain/group-theory
  - topic/average-case-hardness
  - topic/word-problem
  - topic/decidability
  - topic/growth-functions
  - topic/cayley-graphs
  - project/challenge-gen
  - paper
  - status/draft
---

# Generic-case complexity, decision problems in group theory and random walks

## Abstract

"We give a precise definition of "generic-case complexity" and show that for a very large class of finitely generated groups the classical decision problems of group theory - the word, conjugacy and membership problems - all have linear-time generic-case complexity. We prove such theorems by using the theory of random walks on regular graphs."

## TL;DR

Defines generic-case complexity: an algorithm only has to be fast on a set of inputs of asymptotic density 1, and can ignore the rest. Then shows that the word, conjugacy and membership problems are generically linear-time (or quadratic/polynomial) in a huge class of groups, including groups whose word problem is undecidable. The reason: trivial words have density zero in any infinite group. A random word is almost surely non-trivial, and a cheap check in an infinite quotient says so. All the hardness sits in a negligible set of "Yes" instances.

## Problem

Computer experiments in group theory show that "fast check" algorithms decide most inputs quickly, even when the worst-case complexity is huge or the problem is undecidable (§1). The paper asks for a precise explanation. It also needs a complexity notion that, unlike average-case complexity, makes sense for partial algorithms and undecidable problems (§1, §3).

## Approach

- **Asymptotic density** (Def. 3.1). For $S \subseteq (X^*)^k$, $\rho_n(S) = |S \cap B_n| / |B_n|$, where $B_n$ is the set of tuples of length at most $n$. Then $\rho(S) = \limsup \rho_n(S)$. $S$ is **generic** if $\lim \rho_n(S) = 1$, and **strongly generic** if the convergence is exponentially fast (Def. 3.2). Complements of generic sets are **negligible**.
- **Generic-case complexity** (Def. 3.4–3.6). A correct partial algorithm $\Omega$ solves $D$ with generic-case complexity $C$ if it stops within bound $C$ on a generic set. For a group, this must hold for *every* finite generating set (Def. 3.6), which makes it a group invariant.
- **Quotient method** (§4). If a finite-index subgroup of $G$ maps onto an infinite group $\bar G$ with a fast word problem, then "check $\bar w \ne 1$ in $\bar G$" answers "No" correctly on almost all inputs.
- **Random walks / cogrowth** (§5–6). The words that map into a subgroup $H$ correspond to closed paths at the base vertex of the Schreier coset graph $\Gamma(G,H,A)$. Results of Grigorchuk, Cohen, Woess and Bartholdi on cogrowth and spectral radius show these are negligible when $\Gamma$ is infinite, and exponentially negligible when $\Gamma$ is non-amenable (Thm 5.4, Thm 5.7, Prop. 5.8).
- The paper also defines **witness problems** (§2): give an explicit proof that $u \in D$. For the word problem that is an expression $u = \prod_{j=1}^{t} u_j^{-1} r_j^{\epsilon_j} u_j$. The paper does not study them.

## Key result

**Theorem A** (§4, verbatim): "Let G be a finitely generated group. Suppose that G has a finite index subgroup that possesses an infinite quotient group $\bar G$ for which the word problem is solvable in the complexity class C. Then the word problem for G has generic-case complexity in the class C. Moreover, if the group $\bar G$ is nonamenable, then the generic-case complexity of the word problem for G is strongly in C."

**Corollary 4.1** (§4): with an infinite word-hyperbolic quotient (of a finite-index subgroup), the WP is generically in real time, and strongly generically linear if the quotient is non-elementary. With an infinite automatic quotient it is generically quadratic, strongly so if non-amenable. With an infinite quotient that is linear over a field of characteristic zero it is generically polynomial, strongly so if not virtually solvable.

**Examples** (§4):
- 4.2: any f.g. group with infinite abelianization has a generically linear-time WP. This covers all knot groups, all Artin groups and infinite one-relator groups.
- 4.4: braid groups $B_n$ ($n \ge 3$) are strongly generically linear, via $P_3 \cong F(a,b) \times \mathbb Z$.
- 4.5: $\mathrm{Aut}(F_n)$ and $\mathrm{Out}(F_n)$ are strongly generically quadratic, via $GL(n,\mathbb Z)$.
- 4.6: "Theorem A holds even if G has unsolvable word problem". The Boone group $B$ maps onto a non-abelian free group, so "the generic-case complexity of the word problem for B is strongly linear time".
- 4.7: presentations with deficiency $\ge 2$ are strongly generically linear (via Baumslag–Pride).

**Theorem B** (membership problem): an analogous quotient statement, strong when the Schreier coset graph $\Gamma(\bar G, K, A)$ is non-amenable. **Theorem C** (conjugacy problem): "Let G be a non-cyclic finitely generated group with infinite abelianization. Then the generic-case complexity of the conjugacy problem for G is linear time."

**Theorem 6.3** (§6, free group $F = F(x_1,\dots,x_k)$, $k \ge 2$, $H \le F$), with $a_n$ = number of freely reduced words of length $n$ in $H$ and $r_n$ = the same for length $\le n$:
1. If $[F:H] = \infty$, then $\lim a_n/(2k-1)^n = \lim r_n/(2k-1)^n = 0$ (and similarly for all words, $b_n/(2k)^n$, $z_n/(2k)^n$). "Thus $H_A$ has zero asymptotic density".
2. If the coset graph is non-amenable, these limits go to zero exponentially fast.
3. If $[F:H] < \infty$, the corresponding limsups are $> 0$.

**Cogrowth–spectral radius link** (Thm 5.4, Grigorchuk/Cohen/Bartholdi). For a $d$-regular graph, $\nu < 1 \iff \alpha < d-1 \iff \beta < d$, so "Γ is amenable if and only if it has maximal possible cogrowth".

## Assumptions

- Inputs are words (or tuples of words) over a fixed finite alphabet, measured by **asymptotic density over balls** $B_n$. This is effectively uniform sampling of words of length $\le n$. Results for freely reduced inputs are stated to be mostly unchanged (§2).
- Group finitely generated. Theorem A needs a finite-index subgroup with an **infinite** quotient whose WP lies in class $C$.
- Strong genericity (exponential convergence) needs non-amenability of the quotient or coset graph.
- Model of computation: multi-tape Turing machines, with proper complexity functions (Conv. 2.1).

## Limitations / scope

- The authors say "our approach simply shows that for the "decision" version of the word and the membership problem the fast "No" answer component of the set of all inputs is very large" (§4, p.15).
- "Our results do not say anything about the generic behavior of the "witness" versions of the word, conjugacy and membership problems" (§4, p.15). The authors argue that cryptographic applications need witness versions.
- If the quotient is small (e.g. $\mathbb Z$), convergence may be much slower than exponential. "The weaker convergence is all that we have for general one-relator groups" (§4, p.15).
- The quotient method fails for Miller's finitely presented group all of whose non-trivial quotients have unsolvable WP. Constructing a f.g. group whose WP is provably not generically linear is called "a very difficult problem" (§4, pp.15–16).
- Generic-case ≠ average-case. Combining the two is left to future work (§2, §4).
- Researcher's note: the paper's density is over all inputs, so it says nothing about how hard the *trivial* words themselves are. They are the negligible set.

## Replication evidence

Theoretical; the proofs rest on established random-walk results (Woess, Bartholdi, Grigorchuk, Cohen). §4 describes an easy confirming experiment: send random words in $F_n$ through $F_n \to F_{n-k}$ (killing $k$ generators) and count non-trivial images. The theory has since grown into a large literature on generic-case complexity (192 citations). No in-vault replication.

## Why this paper matters

This is the paper that turns the folklore "most instances are easy" into a theorem for group-theoretic decision problems. It separates the complexity of a problem from the complexity of its typical instance. Even the Boone group, with undecidable word problem, has a strongly generically linear-time WP. The hard instances are confined to a set of density zero, and "special words" carry the hardness.

The mechanism matters as much as the theorem. Trivial words are closed walks in the Cayley graph of an infinite quotient. Their proportion among all words of length $n$ tends to zero, exponentially fast when the quotient is non-amenable (Thm 6.3). So uniform sampling of words essentially never produces a "Yes" instance of the word problem, and the generic fast algorithm always answers "No".

**Relevance to challenge-gen:** This paper is the formal basis for the project's premise that random instances are easy. For the word problem, uniform random words are almost all non-trivial, and the generic "No" is cheap. All the difficulty lives in the negligible set of trivial words, which the project must sample on purpose, with a certificate. The paper's "witness problem" (§2), an explicit product of conjugates of relators, is exactly the certificate format the project needs. The authors explicitly leave its generic behaviour open.

## Quotes

1. > "the fast "No" answer component of the set of all inputs is very large" — §4, p.15
2. > "Theorem A holds even if G has unsolvable word problem." — Example 4.6

## Open questions surfaced

- **Witness-problem genericity** (§4, open): what is the generic complexity of *producing* a product-of-conjugates expression for trivial words? For challenge-gen this is the hardness of the "Yes" side.
- Generic complexity of the WP *restricted to trivial words*, i.e. a measure supported on $N$ rather than on $F$. The paper's density is the wrong measure for this. [[elder-2015-random-trivial-words]] supplies one such measure.
- **B(2,5)**, Researcher's inference (not stated in the paper): by Thm 6.3 parts 1 and 3, applied to $B(2,5) = F_2/N$, trivial words having density zero is equivalent to $B(2,5)$ being infinite. So the negligibility of challenge words is tied to the finiteness question. Theorem A cannot be applied to $B(2,5)$, because no infinite quotient with solvable WP is known.
- A f.g. group whose WP is provably not generically linear (§4, called very difficult).
- Strong generic CP for non-amenable quotients, invariantly under change of generators (§4, conjectured true).
- Combining generic and worst-case algorithms into average-case results (§2, §4).

## Related material

- Parent overview: [[word-problem-overview]]
- MOCs: [[_moc-word-problem]], [[_moc-hard-instance-generation]] (listed there under "Why random instances are easy")
- [[decidability-landscape]]: the worst-case picture (Novikov–Boone, hyperbolic, automatic) that this paper contrasts with generic-case behaviour. Corollary 4.1 maps worst-case classes to generic classes.
- [[dehn-function]]: Dehn's algorithm for hyperbolic groups is the linear-time quotient check used in Corollary 4.1.
- [[elder-2015-random-trivial-words]]: samples from the negligible set this paper identifies (trivial words), and connects to the same cogrowth/amenability theory (Grigorchuk–Cohen).
- [[krzakala-zdeborova-2009-quiet-planting]], [[achlioptas-jia-moore-2004-hiding-assignments]]: the random-CSP counterpart. There, too, typical instances are easy, and hard instances with a known answer must be constructed.
- [[_synthesis-hard-instance-generation]]: cross-domain synthesis for challenge-gen.
- [[project-challenge-gen]]: project profile; this paper underwrites its "random instances are easy" motivation.
- [[matveeva-2026-ai-problem-solving]]: the 119 B(2,5) challenge words. These are hand-built "special words" of exactly the kind this paper says a random sampler will never produce.
- [[shehper-2024-ac-hardness]]: the Andrews–Curtis side of the same question of where hard instances live; there, capped greedy search solves every Miller–Schupp presentation of length < 14 (533 of 1190 overall), and hardness is located in the unsolved residue.

## Related material in vault

- Extends: —
- Contradicts: —
- Replicates: —
- Concepts introduced/used: [[dehn-function]]
- Cites: — (no in-vault paper notes for its references: Woess, Bartholdi, Grigorchuk, Cohen, Borovik–Myasnikov–Shpilrain)
- Cited by (in this vault): —

---
title: "Random sampling of trivial words in finitely presented groups"
authors: Murray Elder, Andrew Rechnitzer, E. J. Janse van Rensburg
year: 2015
venue: "Experimental Mathematics 24(4) (2015) 391–409; arXiv:1312.5722 (v2, 20 Dec 2013)"
url: https://arxiv.org/abs/1312.5722
url_translated:
language: en
domain: group-theory
status: draft
methodology_type: empirical
citation_count: 7
citation_count_date: 2026-10-05
key_concepts:
  - "[[Concepts/certified-instance-generation]]"
extends: []
contradicts: []
replicates: []
cites: []
cited_by: []
quality_notes: "Semantic Scholar count 7 (2026-10-05). DOI 10.1080/10586458.2015.1005853. The arXiv title has a typo ('trivials words'); the journal title is used here. arXiv v2 supersedes arXiv:1210.3425. Two independently written C++ implementations were cross-checked (§3). Inconsistency in the source: the abstract writes the target distribution as (|w|+1)^α β^|w|, but Corollary 2.13 states (|u|+1)^{1+α} β^|u|. The summary follows Corollary 2.13."
author: asetlearning
project: challenge-gen
tags:
  - agent/research
  - user/asetlearning
  - domain/group-theory
  - topic/trivial-words
  - topic/word-problem
  - topic/growth-functions
  - project/challenge-gen
  - paper
  - status/draft
---

# Random sampling of trivial words in finitely presented groups

## Abstract

"We describe a novel algorithm for random sampling of freely reduced words equal to the identity in a finitely presented group. The algorithm is based on Metropolis Monte Carlo sampling. The algorithm samples from a stretched Boltzmann distribution

$\pi(w) = (|w|+1)^{\alpha} \beta^{|w|} \cdot Z^{-1}$

where $|w|$ is the length of a word $w$, $\alpha$ and $\beta$ are parameters of the algorithm, and $Z$ is a normalising constant. It follows that words of the same length are sampled with the same probability. The distribution can be expressed in terms of the cogrowth series of the group, which then allows us to relate statistical properties of words sampled by the algorithm to the cogrowth of the group, and hence its amenability.

We have implemented the algorithm and applied it to several group presentations including the Baumslag-Solitar groups, some free products studied by Kouksov, a finitely presented amenable group that is not subexponentially amenable (based on the basilica group), and Richard Thompson's group $F$."

## TL;DR

A Metropolis Markov chain whose state space is the set of freely reduced **trivial words** of a finite presentation. It moves by conjugating by a generator or inserting a cyclic permutation of a relator. Every state is trivial by construction, and the chain is proven ergodic. Its stationary distribution depends only on word length, which ties the chain's mean length to the cogrowth series. The authors use this to estimate cogrowth numerically, and their data suggest that Thompson's group $F$ is non-amenable. It is the canonical "sample trivial words directly" method. It gives no handle on hardness beyond length.

## Problem

Trivial words have density zero in an infinite group (cf. [[kapovich-2003-generic-case-complexity]]), so random walks on the Cayley graph rarely produce them. The paper asks how to sample trivial words of a finitely presented group directly, with a known distribution. It then uses those samples to estimate the cogrowth series and so test amenability numerically (§1).

## Approach

**State space** $\mathcal X$: freely reduced words equal to $1$ in $G = \langle a_1..a_k \mid R_1..R_\ell \rangle$. $\mathcal R$ is the set of relators, their inverses and all cyclic permutations, freely reduced (§2).

**Elementary moves** (§2.1):
- *Conjugation by $x \in S$*: $w \mapsto x w x^{-1}$, freely reduced.
- *Left-insertion of $R \in \mathcal R$ at position $m$*: split $w = uv$ with $|v| = m$ and form $uRv$. The move is rejected (the chain stays at $w$) if free reduction cancels any symbol of $v$ (§2.1). This restriction makes moves "uniquely reversible" (Lemmas 2.1–2.2).

**Connectivity** (Lemma 2.3, constructive). Any $w \in \mathcal X$ is a free reduction of $\prod_{j=1}^{n} \rho_j r_j \rho_j^{-1}$. The proof builds $w$ from the empty word by inserting $r_1$, conjugating letter by letter by $\rho_2^{-1}\rho_1$, appending $r_2$ at the extreme right, and so on, then finally conjugating by $\rho_n$.

**Transition probabilities** (§2.2), with parameters $p_c \in (0,1)$, $\alpha \in \mathbb R$, $\beta \in (0,1)$ and a distribution $P$ on $\mathcal R$ with $P(R) = P(R^{-1}) > 0$:
- With probability $p_c$, conjugate by a uniform $x \in S$, accept with $\min\{1, \frac{(|w''|+1)^{1+\alpha}\beta^{|w''|}}{(|w|+1)^{1+\alpha}\beta^{|w|}}\}$ (eq. 2.4).
- Otherwise, left-insert $R \sim P$ at uniform $m \in \{0..|w|\}$, accept with $\min\{1, \frac{(|w''|+1)^{\alpha}\beta^{|w''|}}{(|w|+1)^{\alpha}\beta^{|w|}}\}$ (eq. 2.5).

**Variants**:
- §2.5: conjugation plus *append at the right end* alone suffices for Corollary 2.13. A rotation move is also possible.
- §2.6: avoid the empty word (state space $\mathcal X'$) to force longer samples. This is irreducible except for $\langle a \mid a^k \rangle$ (Lemma 2.14). The reported experiments use $\mathcal X'$.
- §2.7: **infinitely many relators** are allowed if $P(R) > 0$ and $P(R) = P(R^{-1})$, tested on $\mathbb Z \wr \mathbb Z$.

**Parallel tempering** (multiple Markov chains) runs many $\beta$ values at once (§2.4). The implementation is C++ with linked-list words and GSL random numbers. "At each beta value we sampled approximately $10^{10}$ elementary moves. Each run consisted of 100 β-values and took approximately 1 week on a single node" (§3).

## Key result

**Corollary 2.13** (§2.3): for any states $u, v \in \mathcal X$, $\Pr{}^n(u \to v) \to \pi(v)$ as $n \to \infty$, where
$$\pi(u) = \frac{(|u|+1)^{1+\alpha}\beta^{|u|}}{Z}.$$
"When α = −1, π is the Boltzmann or Gibbs distribution." π "does not depend of the details of the word, but only on its length. So if two words have the same length then they are sampled with the same probability."

**Cogrowth link** (§2.4): $Z = \sum_{n \ge 0} c(n)(n+1)^{1+\alpha}\beta^n$ (eq. 2.22), where $c(n)$ is the number of trivial freely reduced words of length $n$. It converges for $0 \le \beta < \beta_c$, with $\beta_c = \limsup c(n)^{-1/n}$ (eq. 2.23), which is the radius of convergence of the cogrowth series. For $\alpha = -1$, $E(|w|) = z \frac{d}{dz}\log C(z)\big|_{z=\beta}$ (eq. 2.27). Mean length diverges as $\beta \to \beta_c$. By Grigorchuk–Cohen, a group is amenable iff its cogrowth is $|S|-1$.

**Validation against exact series** (§3.1–3.4): excellent agreement for $\mathbb Z^2$ ($\beta_c = 1/3$), Kouksov's free products $K_1 = \langle a,b \mid a^2, b^3\rangle$, $K_2 = \langle a,b \mid a^3,b^3\rangle$, $K_3 = \langle a,b,c \mid a^2,b^2,c^2\rangle$ (reciprocal cogrowths "0.3418821478, 0.3664068598 and 0.2192752634 respectively"), $BS(2,2)$ and $BS(3,3)$ (reciprocal cogrowths 0.3747331572 and 0.417525628), and $BS(1,2)$, $BS(1,3)$ (amenable, $1/3$).

**Thompson's group $F$** (§3.6), on three presentations (standard $\langle a,b \mid [ab^{-1}, a^{-1}ba], [ab^{-1}, a^{-2}ba^2]\rangle$ and two Tietze variants): "βc = 0.395 ± 0.005, 0.172 ± 0.002 and 0.134 ± 0.004 for the three presentations. These imply cogrowths of approximately 2.53±0.03, 5.81±0.07 and 7.4 ± 0.2, all of which are well below the amenable values of 3,7 and 9." The authors add that this does not "constitute a proof that Thompson's group is non-amenable".

**Basilica relative** (§3.5): results are consistent with amenability. The basilica presentation (3.8) has relators `[a^n, [a^n, b^n]]` and `[b^n, a^{2n}]` with $n$ a power of 2.

## Assumptions

- A finite presentation with freely reduced, non-empty relators. Infinite presentations are allowed via §2.7.
- Ergodicity is proven (Lemmas 2.5, 2.6). The **mixing time is not bounded**: the authors call it an open question (§4).
- Cogrowth estimates assume the chain reaches equilibrium at each $\beta$ and that finite-length data extrapolate to the singularity.

## Limitations / scope

- "We cannot rule out the presence of pathologies influencing our results" (§4). Convergence rate and precise asymptotic analysis are left open.
- The sampled distribution is **uniform within each length**, so nothing in it selects for structure or difficulty.
- Thompson-$F$ evidence is numerical, not a proof.
- Researcher's note: the chain needs no word-problem solver, because triviality holds by construction. The cost is that it only ever explores the normal closure through relator insertions and conjugations.

## Replication evidence

The paper has an internal check: two independent implementations, by the second and third authors, were compared (§3). Results agree with exact cogrowth series where those are known (§3.1–3.4). The Thompson-$F$ amenability question remains open. No in-vault replication. Not cited by other vault notes yet.

## Why this paper matters

This is the standard reference for sampling trivial words directly, as opposed to hoping a random walk returns to the identity. It replaces the Cayley graph with a graph on the set of trivial words, with edges given by conjugation and relator insertion, and runs a provably ergodic Metropolis chain there. Because $\pi$ depends only on $|w|$, length statistics are a clean probe of the cogrowth series. That is why the authors use it as an amenability test.

**Relevance to challenge-gen:** The chain is a ready-made *certified* generator. Every trajectory from the empty word is a product-of-conjugates derivation (the constructive proof of Lemma 2.3 is exactly that), so a certificate comes for free. It does not need a word-problem oracle, and §2.7 allows infinitely many relators, as in the $x^5$ family for Burnside groups. But the stationary law is length-uniform over trivial words. That is the trivial-word analogue of "generic", and nothing in it targets hard words. Also, the number of insertions along a trajectory is only an upper bound on the area, since insertions can cancel. Challenge-gen would need to add a hardness bias, for example on certified area or solver cost, on top of this chain.

## Quotes

1. > "it can be seen as executing a random walk on the space of trivial words" — §1
2. > "words of the same length are sampled with the same probability" — Abstract

## Open questions surfaced

- Mixing time of the chain on $\mathcal X$ (stated open, §4). This determines how many moves a sample needs before it is "random" rather than a shallow perturbation of short words.
- Can the Metropolis target be re-weighted by a hardness score, such as certified area, Dehn-style reduction cost, or solver runtime, while keeping detailed balance? (Researcher's extension, not in the paper.)
- How does area (minimal number of relator applications) of sampled words scale with $|w|$ under $\pi$, for groups with super-linear Dehn function, e.g. $BS(1,2)$?
- Behaviour of the chain on exponent-$n$ Burnside presentations, using the §2.7 infinite-relator extension.

## Related material

- Parent overview: [[word-problem-overview]]
- MOCs: [[_moc-word-problem]], [[_moc-hard-instance-generation]]
- [[kapovich-2003-generic-case-complexity]]: shows trivial words are negligible under uniform word sampling (Thm 6.3, also via cogrowth/amenability), which is why a dedicated sampler is needed. Not cited by this paper; the link is conceptual.
- [[dehn-function]]: area of a trivial word, which bounds what an insertion trajectory certifies.
- [[2607.26241]]: WPNet generates trivial training words by a cruder version of the same moves (inserting free pairs and relators), without the Metropolis weighting.
- [[coulon-2018-trivial-elements-criterion]]: a criterion for recognising trivial elements of free Burnside groups. This is the opposite direction (detecting rather than generating), for the group the project targets.
- [[_synthesis-hard-instance-generation]]: cross-domain synthesis.
- [[project-challenge-gen]]: project profile.

## Related material in vault
- [[myasnikov-ushakov-2011-random-van-kampen]]: random relator-insertion words are generic and shallow

- Extends: —
- Contradicts: —
- Replicates: —
- Concepts introduced/used: —
- Cites: — (in-vault notes for Grigorchuk, Cohen, Kouksov or Burillo–Cleary–Wiest do not exist)
- Cited by (in this vault): —

---
title: "Filling Length in Finitely Presentable Groups"
authors: S. M. Gersten, T. R. Riley
year: 2002
venue: "Geometriae Dedicata 92, 41–58 (arXiv preprint math/0008030, v1 of 3 Aug 2000, read)"
url: https://arxiv.org/abs/math/0008030
url_translated:
language: en
domain: group-theory
status: draft
methodology_type: theoretical
citation_count: null
citation_count_date:
key_concepts: []
extends: []
contradicts: []
replicates: []
cites: []
cited_by: []
quality_notes: "Full text of the arXiv v1 (2000) read; the 2002 journal version was not checked, so theorem numbering/constants may differ. Foundational reference for bounding filling length by area/diameter."
author: asetlearning
tags:
  - agent/research
  - user/asetlearning
  - domain/group-theory
  - topic/filling-length
  - topic/dehn-function
  - topic/word-problem
  - topic/space-complexity
  - paper
  - status/draft
project: challenge-gen
---

# Filling Length in Finitely Presentable Groups

## Abstract

Filling length measures the length of the contracting closed loops in a null-homotopy. The filling length function of Gromov for a finitely presented group measures the filling length as a function of length of edge-loops in the Cayley 2-complex. We give a bound on the filling length function in terms of the log of an isoperimetric function multiplied by a (simultaneously realisable) isodiametric function.

## TL;DR

Defines the combinatorial filling length FL(w) of a trivial word (minimum over van Kampen diagrams of the maximum boundary-word length while collapsing the diagram) and proves $h_0(n)\preceq g(n)\log(f(n)+1)$ for any isoperimetric/isodiametric pair $(f,g)$. Gives the elementary comparisons $g_0\le h_0\le 2Kf_0+n$ and $f_0\preceq \exp h_0$. Useful to anyone asking how long the intermediate words must get when reducing a trivial word.

## Problem

Dehn function (area) and isodiametric function are standard; filling length, the third Gromov invariant, measures the *peak* word length along a reduction. How does it relate to the other two?

## Approach

FL is defined on a van Kampen diagram $D$ for $w$ by two collapse moves (§2): (1) 1-cell collapse = free reduction (not cyclic reduction, the base point is kept); (2) 2-cell collapse = replace $a_1^{-1}$ by $a_2\cdots a_n$ where $a_1\cdots a_n$ is a cyclic permutation of a relator$^{\pm1}$. $FL(D)$ is the best bound on the boundary length along a collapse of $D$; $FL(w)=\min_D FL(D)$; $h_0(n)=\max\{FL(w):|w|\le n\}$. The upper bound uses a logarithmic shelling lemma for binary trees (§3): a forest of $N$ nodes can be shelled keeping at most $\log_2(N+1)+1$ roots visible (Corollary 1), applied to a tree decomposition of the diagram.

## Key result

- **Theorem 1.** For an AD-pair $(f,g)$ (isoperimetric $f$, isodiametric $g$) of a finite presentation, $h_0(n)\preceq g(n)\log(f(n)+1)$ (§1/§4).
- **Proposition 2.** For a triangular presentation and a van Kampen diagram $D$ with diameter $\mathcal D$, area $A$, boundary length $n$: $FL(D)\le(2\mathcal D+1)(\log_2(A+1)+1)+4\mathcal D+1+n$.
- **Corollary 2.** For every finite presentation there is $C>0$ with $FL(D)\le C\cdot\mathrm{Diam}(D)^2+n+1$ for every immersed disc diagram $D$.
- **Examples in §2.** $g_0(n)\le h_0(n)\le 2Kf_0(n)+n$ ($K$ the longest relator); $f_0\preceq\exp h_0$ (Gersten–Gromov); asynchronously combable groups have linear filling length (Gersten).
- Application: Bridson's groups $\Gamma_m$ with AD-pairs $(x^{2m+1},x^m)$ get $h_0\preceq x^m\log x$, versus $x^{2m+1}$ from the area bound.

## Assumptions

Finitely presented group; reduced words; filling length measured on diagrams for a null-homotopic word with the based collapse moves above (no insertion moves, no cyclic conjugation of the whole word).

## Limitations / scope

Asymptotic, up to the equivalence $\simeq$; says nothing about exact FL of a specific word. The move set differs from Olshanskii's space function and from Bridson–Riley's free/fragmenting variants (see [[olshanskii-2011-space-functions]]): the same group can have linear free-fragmenting filling length and exponential FL.

## Replication evidence

Not applicable (theoretical). None checked. Related: [[olshanskii-2011-space-functions]] works with the same objects but I did not verify that it cites this paper.

## Why this paper matters

For challenge generation, this is the formal home of "peak of a reduction path". It gives (a) a lower bound $FL\ge$ diameter-type quantities, (b) an upper bound polylogarithmic in area times diameter, and (c) the warning that the result is asymptotic and about diagrams, while solver-relevant peaks (cyclic words, insertions, fragmentation) are other functions.

## Quotes

1. > "We give a bound on the filling length function in terms of the log of an isoperimetric function multiplied by a (simultaneously realisable) isodiametric function." — Abstract

## Open questions surfaced

- The authors state they know no finitely presented group where $h_0\preceq g_0$ fails (Remark after Corollary 2); Gromov's consequence $f_0\preceq\exp g_0$ would follow if it held.
- For finite groups (our B(2,5) if finite) all these functions are bounded by constants; the asymptotic theory does not apply directly. See [[_synthesis-t028-literature-2026-10-20]].

## Related material in vault

- Related: [[olshanskii-2011-space-functions]] (space functions; citation link not verified)
- Concepts introduced/used: Dehn function, isodiametric function
- Synthesis: [[_synthesis-t028-literature-2026-10-20]]

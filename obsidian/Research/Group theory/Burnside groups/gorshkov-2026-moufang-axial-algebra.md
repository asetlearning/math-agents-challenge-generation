---
title: "Groups of generalized Moufang type and Z2-graded algebras"
authors: "Ilya Gorshkov"
year: 2026
venue: "arXiv preprint"
url: "https://arxiv.org/abs/2603.01988"
language: en
domain: group-theory
status: draft
methodology_type: theoretical
citation_count: null
citation_count_date: 2026-07-31
key_concepts: []
extends: []
contradicts: []
replicates: []
cites:
  - "[[atkarskaya-rips-tent-2023]]"
cited_by: []
quality_notes: "Very recent preprint (submitted 2026-03-02, within the last ~5 months of this scan). Not independently read beyond the abstract; the p=5 Monster-type fusion law detail is a striking coincidence worth flagging to Lead/Experimenter-B25 but its relevance to the Mixer's actual B(2,5) computation is unassessed and speculative."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/odd-exponent-burnside
  - paper
  - status/draft
project: b25
---

# Groups of generalized Moufang type and Z2-graded algebras

## Abstract

Not independently re-fetched verbatim this scan.

## TL;DR

Constructs a non-associative Z2-graded algebra A_F(G,T,η) from a "generalized Moufang group of p-type" G, and proves that when G is a free Burnside group of odd prime exponent p extended by an involutory automorphism, finiteness of G is EQUIVALENT to finite-dimensionality of A_F(G,T,η) — an algebraic reformulation of the Burnside finiteness question for this specific extended construction. For p=5 specifically, the resulting two-generator algebra is shown to be "left-axial," satisfying a Monster-type fusion law M(4/3,−4/3).

## Problem

Reformulate finiteness of a free-Burnside-of-odd-prime-exponent-extended-by-an-involution group as an algebraic (axial-algebra) finite-dimensionality question, in the hope that axial algebra machinery (developed originally for Monster-group / vertex-operator-algebra contexts) offers new tools.

## Approach

Build A_F(G,T,η) from the group G, a transposition-like generating set T, and a parameter η; show the correspondence G finite ⟺ A_F(G,T,η) finite-dimensional, for G = (free Burnside group of odd prime exponent p) ⋊ (involution). Specialize to p=5, η=−1/3.

## Key result

> "When G is a free Burnside group of odd prime period p extended by an involutory automorphism, the finiteness of G is equivalent to the finite-dimensionality of A_F(G,T,η), providing a reformulation of the Burnside problem." For p=5, η=−1/3: the two-generator algebra is left-axial, satisfying the Monster-type fusion law M(4/3,−4/3); for general prime p>5, axial under a more general fusion law. [Relayed via subagent from the abstract — verify verbatim before quoting in a proof-facing context.]

## Assumptions

- G is specifically the free Burnside group of odd PRIME exponent p, extended (not the bare free Burnside group itself) by an involutory automorphism — this is a structurally different object from B(2,5) itself. **Do not treat this as a direct reformulation of B(2,5) finiteness** without confirming the "extended by an involution" construction matches or embeds the object actually of interest.

## Limitations / scope

- Does not resolve finiteness for any m or p — it is an equivalence/reformulation, not a proof.
- Unclear (unassessed this scan) whether the extended-by-involution construction is close enough to B(2,5) itself to be Mixer-actionable, or whether it's a genuinely different object that merely shares the exponent-5 parameter.
- Very recent (Mar 2026) — no citation history, no community assessment possible yet.

## Replication evidence

N/A — brand new preprint.

## Why this paper matters

The single most novel, most recent item surfaced in this scan. The exponent-5 case being singled out as giving a "Monster-type fusion law" is a striking, possibly coincidental, possibly meaningful structural fact — axial algebras with Monster-type fusion laws are exactly the framework built around the Monster group / Griess algebra / Majorana theory, so a genuine appearance of that fusion law at p=5 in a Burnside-adjacent construction is worth a closer read. However, this note explicitly does NOT claim Mixer-relevance — that would require confirming whether "free Burnside group of odd prime period 5 extended by an involutory automorphism" is close enough in structure to B(2,5) for any equivalence to transfer computationally. Flagging to Lead as a "mathematically fresh angle, unclear computational relevance" rather than a lead to act on immediately.

## Quotes

1. > "the finiteness of G is equivalent to the finite-dimensionality of A_F(G,T,η)" — Abstract (relayed, verify before quoting verbatim).

## Open questions surfaced

- Does the "extended by an involutory automorphism" construction relate to any object already in the algo_mixing B(2,5) pipeline (e.g. an automorphism already used in the Kuznetsov centralizer-of-inversion line, [[kuznetsov-filippov-2010-sjim]])? Worth a targeted follow-up if Lead wants to chase this.
- Is finite-dimensionality of A_F(G,T,η) computationally easier to test than finiteness of G directly? Not addressed in the abstract; would require reading the full paper.

## Related material in vault

- Extends: (none)
- Contradicts: (none)
- Replicates: (none)
- Concepts introduced/used: (none)
- Cites: [[atkarskaya-rips-tent-2023]] (per subagent citation search; relationship not independently confirmed this scan)
- Cited by (in vault): [[_synthesis-odd-exponent-state-2026]]
- Deep-read: [[_synthesis-gorshkov-axial-algebra-r2-2026]] (R2 full-text read of this preprint)
- MOC: [[_moc-burnside]]

---
title: "Machine-checkable equivalence certificates at the length-14 Andrews-Curtis frontier"
authors:
  - "Josep Carreras"
year: 2026
venue: "arXiv:2607.23611 [math.GR] preprint (v1 26 Jul 2026, 10 pp.); artifact github.com/joe-carr-data/ac-certificates (tag v1.0), Zenodo doi:10.5281/zenodo.21499081"
url: "https://arxiv.org/abs/2607.23611"
url_translated:
language: en
domain: group-theory
status: draft
methodology_type: empirical
citation_count: 0
citation_count_date: 2026-10-05
key_concepts:
  - "[[Concepts/andrews-curtis-moves]]"
extends:
  - "[[shehper-2024-ac-hardness]]"
contradicts: []
replicates: []
cites:
  - "[[shehper-2024-ac-hardness]]"
  - "[[andrews-curtis-conjecture]]"
cited_by: []
quality_notes: "Full v1 PDF read. Single-author independent preprint (two months old, 0 citations on Semantic Scholar 2026-10-05), produced 'in a human-directed collaboration with AI systems' (§8 disclosure). Not peer-reviewed. Mitigating factors: every positive claim ships as a JSON move-ledger replayable by a small stdlib-only verifier, SHA-256 hashes are given, and a claims ledger (RESULTS.md) documents retracted and corrected intermediate claims. The four equivalence theorems are therefore independently checkable at low cost; the §5 minimax bounds are engine-relative and computer-assisted. Novelty claim is explicitly 'public replayability, not priority' (§6). Note: the length-≤12 frontier is attributed to Miasnikov–Myasnikov math/0304305, not to [[miasnikov-1999-ac-genetic]]."
author: asetlearning
tags:
  - agent/research
  - user/asetlearning
  - domain/group-theory
  - topic/andrews-curtis
  - topic/proof-certificates
  - topic/proof-search
  - topic/computational-search-group-theory
  - project/challenge-gen
  - paper
  - status/draft
project: challenge-gen
---

# Machine-checkable equivalence certificates at the length-14 Andrews-Curtis frontier

## Abstract

> "In rank 2, unconditional verification of the Andrews-Curtis conjecture stands at total relator length 12; at length 13 every balanced trivial-group presentation is AC-trivializable or AC-equivalent to the Akbulut-Kirby presentation AK(3), itself open. At length 14, Shehper et al. reduced the Miller-Schupp family to six hard presentations: four stated AC-equivalent to AK(3) with no published move sequences, and two unresolved. We prove four explicit AC-equivalences among these six as machine-checkable elementary-move certificates, replayable in under a second by a small dependency-free verifier: the classical candidate <x,y | x^-1 y^2 x = y^3, y^-1 x^2 y = x^3> (= MS(2, x^-2 y^-1 x^2 y) up to rotation) is equivalent to the unresolved MS(2, y x^2 y^-1 x^-2) (36 moves); MS(2, y x^2 y x^-2) to MS(2, x^-2 y^-1 x^2 y^-1) (85 moves); and MS(3, y x^2 y) and MS(3, y^-1 x^2 y^-1) each to AK(3) (66 and 13 moves). The latter two are, to our knowledge, the first public explicit certificates for any of the four AK(3)-equivalences asserted without proof by Shehper et al., making the MS(3) branch of the length-14 collapse unconditional. The first two realize the automorphism sigma: x -> x, y -> y^-1 on the remaining open classes. We complement the certificates with a computer-assisted exhaustive minimax analysis of the substitution-move graph: the bottleneck distance from MS(3, y x^2 y) to AK(3) is exactly 19, while any such path from either MS(2) representative to AK(3), or between them, must reach total length at least 27. We further analyze the public classification table of the "Two-Hump" campaign, derive a 214-pair class-merger program, and commit an AC-19 membership audit. All certificates, search engines, verifier, and one-command reproduction are archived."

## TL;DR

The paper takes the six length-14 Miller–Schupp presentations that Shehper et al.'s greedy search could not solve and connects them with explicit, replayable AC-move ledgers checked by a tiny standard-library verifier. The result is three certified blocks: {MS(3, yx²y), MS(3, y⁻¹x²y⁻¹), AK(3)}, {P₁, P₆} and {P₅, P₂}. It also proves, by exhaustive bottleneck search, that the MS(2) blocks sit behind a much higher "energy barrier" (≥ 27) than the MS(3) block (exactly 19) in the substitution-move graph. It is a model for how AC claims (and hard-instance claims generally) should be published: certificate first, with an independent verifier.

## Problem

In rank 2, unconditional AC verification stops at total relator length 12 (Miasnikov–Myasnikov, math/0304305). At length 13 everything is AC-trivial or equivalent to AK(3) (Havas–Ramsay 2003). At length 14, [[shehper-2024-ac-hardness]] §3.3 left six hard Miller–Schupp presentations. Four were "stated to be AC-equivalent to AK(3) — with no move sequences published", and two were unresolved "holdouts". The question is which of these claims can be made *publicly checkable*, and how far apart the remaining classes are.

## Approach

- **Moves and accounting (§2).** States are ordered pairs (r₁, r₂) of freely reduced words. Moves are inversion, multiplication r_i ← r_i r_j^{±1}, conjugation by a single generator, and cyclic rotation, packaged as one move. Both "packaged" and "classical" counts are reported; in the classical count a rotation by k costs min(k mod L, L − k mod L) conjugations.
- **Orbit convention (§2).** Σ = ⟨swap, invert a relator, rotate a relator⟩ consists entirely of AC-realisable operations. An equivalence certificate for P ∼_AC Q is a ledger taking P into Σ · Q, and the verifier checks orbit membership explicitly.
- **Certificate format (§2).** A JSON file with fields `initial`, `target`, `claim`, `moves`. The verifier `ac_verify.py` (standard library only) "re-derives every move in exact integer arithmetic, trusts nothing about how a ledger was produced". It was written and self-tested *before* any search ("certificate-first" discipline). Its self-tests include rejection of corrupted ledgers and malformed fields.
- **Discovery pipeline (§3).** (a) Search on the canonical substitution-move ("GS") graph of the Two-Hump work: greedy search, or an exhaustive bidirectional bottleneck-Dijkstra search. (b) Expansion of the canonical path into elementary moves by orbit-bridging BFS. (c) Independent replay by the verifier.
- **Minimax analysis (§5).** Vertex energy is the total cyclically reduced length. d_GS(S, T) is the minimum over GS paths of the maximum energy along the path. The search runs in Python with an 11× faster C++ port that agrees "bit-for-bit on regression gates".

## Key result

Benchmark labels: P₁ = MS(2, x⁻²y⁻¹x²y) (= the classical Solitar/Burns–Macedońska candidate ⟨x, y | x⁻¹y²x = y³, y⁻¹x²y = x³⟩ up to rotation), P₂ = MS(2, x⁻²y⁻¹x²y⁻¹), P₃ = MS(3, yx²y), P₄ = MS(3, y⁻¹x²y⁻¹), P₅ = MS(2, yx²yx⁻²), P₆ = MS(2, yx²y⁻¹x⁻²). Here MS(2, w) = ⟨x, y | x⁻¹y²xy⁻³, x⁻¹w⟩ and MS(3, w) = ⟨x, y | x⁻¹y³xy⁻⁴, x⁻¹w⟩. All six have total length 14.

| Theorem | Claim | Packaged (classical) moves | Peak total / single relator |
|---|---|---|---|
| 1 | P₁ ∼_AC P₆ | 36 (58) | 27 / 17 |
| 2 | P₅ ∼_AC P₂ | 85 (155) | 33 / 21 |
| 3 | P₃ ∼_AC AK(3) | 66 (101); second certificate 71 (106) | 24 / 15; 22 / 15 |
| 4 | P₄ ∼_AC AK(3) | 13 (22) | 23 / 14 |

Each certificate replays in under 1 s (§3).

- **Certified blocks (§4).** C₀ = {P₃, P₄, AK(3)} (unconditional), C₁ = {P₁, P₆}, C₂ = {P₅, P₂}. **Corollary 5 (conditional).** If Shehper et al.'s two remaining claims (P₁ ∼ AK(3), P₂ ∼ AK(3)) hold, all six presentations lie in the AC-class of AK(3).
- **σ-realisation (Corollary, §3).** With σ: x ↦ x, y ↦ y⁻¹, Theorems 1–2 say that σ is AC-realised on both open MS(2) classes. This is "the frontier analogue of Panteleev–Ushakov's theorem" for AK(n).
- **Theorem 6 (§5, computer-assisted, engine-relative).** d_GS(MS(3, yx²y), AK(3)) = 19, while d_GS(P₁, AK(3)) ≥ 27, d_GS(P₂, AK(3)) ≥ 27 and d_GS(P₁, P₂) ≥ 27. The lower bounds come from searches capped at 26 and 27 that exhausted 6,212,968 and 13,504,944 canonical states with no cross-source contact. A cap-28 run hit its 40-million-state budget and is inconclusive. Structural reading: MS(3) forms (relator split 9 + 5) have GS moves climbing only one unit above energy 14, while every first GS move from an MS(2) form (split 7 + 7) "jumps to energy 17 or 19".
- **Component counts (§5).** At exclusive cap 25: 135,892 states from the C₁ representative, 168,304 from C₂, and 1,532,732 on the AK(3) side.
- **Two-Hump analysis (§1, §6).** The Two-Hump campaign (Fagan et al., ICML 2026, arXiv:2606.21611) enumerated "all 213,946 balanced presentations of total length ≤ 19" and released AC-19 (140,535 entries; extended release 156,762). All six benchmark presentations and AK(3) are absent from it. Its 550 unsolved presentations fall into 261 classes; σ pairs them into 275 pairs (61 intra-class, 214 cross-class). **Corollary 7 (conditional).** If σ is AC-realised on all 214 cross-label pairs, the 261 classes collapse to at most 133.
- **Negative results (§7).** Finite quotients cannot obstruct these classes (Borovik–Lubotzky–Myasnikov; the exponent matrices are unimodular). Prover9, on Lisitsa's encoding, "cannot re-prove a known 167-move trivialization in 2 h"; E fails in 15 min. The section also documents a Prover9 `auto_denials` pitfall: disjunctive goals silently become "prove all".

## Assumptions

- The canonicalisation and move generator of the GS graph come from the Two-Hump work. Theorem 6 is relative to that graph.
- Σ-orbit operations are AC-realisable. Swap is realised "by a 6-move elementary identity".
- The "first public" claim is scoped to an explicit audit list (§8, as of 2026-07-22). The author notes the Two-Hump table "is itself evidence that stronger unpublished computations exist".

## Limitations / scope

- The author marks the §5 scope restrictions as essential: the GS bounds "are not AC-distance lower bounds, not elementary-path peak bounds, not move-count bounds, and not evidence of AC-inequivalence". Because GS moves require a cancelling junction, elementary moves outside the GS graph could open a lower corridor.
- 19 is optimal only as a GS barrier. The paper does not claim that 66 moves is a shortest certificate.
- No certificate connects either MS(2) block to AK(3). That collapse still rests on uncertified claims from [[shehper-2024-ac-hardness]].
- The search and the manuscript were AI-assisted (see quality_notes). The theorems stand on the replayable ledgers.

## Replication evidence

The four certificates are designed for independent replay (`./repro.sh`, hashes in MANIFEST.json), but no third-party replication is reported yet. Internally, Theorem 3 has two independently found certificates (66 and 71 moves). The paper's pipeline independently cross-validates two Two-Hump trivialisations (43 and 37 supermoves, expanded to 114 and 97 packaged elementary moves) and reproduces Two-Hump's bounded component counts with an independent search implementation.

## Why this paper matters

Two things stand out. First, it turns RL-era AC claims, which were "stated without proof", into checkable artefacts, and so cleanly separates *what has been verified* from *what has been asserted* at the length-14 frontier. Second, it quantifies hardness as an energy barrier. The MS(2) classes need excursions to total length ≥ 27 in the GS graph, against 19 for MS(3). That is a concrete, computable hardness measure tied to the same filtration-by-length idea as Shehper et al.'s barcode (§7 there). It also records practical lessons: certificate-first tooling, quarantining invalidated artefacts, and prover-configuration pitfalls.

**Relevance to challenge-gen:** This is the closest existing template for challenge-gen's certificate requirement: a minimal JSON ledger (initial, target, claim, moves), a dependency-free verifier written before any search, sub-second replay, and hash-pinned artefacts. The bottleneck distance d_GS (minimax total length along the best path) is a hardness metric that can be computed exactly for small instances. It separates "easy" from "hard" instances of the same size here (19 vs ≥ 27 at length 14), so it is a candidate hardness score for generated AC challenges. The negative result that saturation provers fail on a 167-move path in 2 h is a useful baseline when choosing reference solvers.

## Quotes

1. > "trusts nothing about how a ledger was produced" — §2
2. > "the novelty we claim for Theorems 1–4 is public replayability, not priority over unpublished computations." — §6

## Open questions surfaced

- Produce an explicit certificate for P₁ ∼ AK(3) or P₂ ∼ AK(3). Either would make the corresponding branch unconditional. §5 shows that any GS corridor must reach total length ≥ 27, and possibly exactly 27 (unresolved by the cap-28 run).
- Is σ AC-realised on all 214 cross-label Two-Hump pairs (Corollary 7)? A pilot sweep of the ten shortest pairs found only engine-relative disconnections.
- Do non-GS elementary moves give lower-barrier paths than the GS graph?
- What algorithm produced the Two-Hump 261-class table? It is not reproduced by any of three tested symmetry quotients (§6).

## Related material

- Parent: [[andrews-curtis-conjecture]] (AK(n), Miller–Schupp candidates)
- MOC: [[_moc-hard-instance-generation]], [[_moc-word-problem]]
- Extends / cites: [[shehper-2024-ac-hardness]] (source of the six-case benchmark and the four uncertified AK(3) claims)
- Earlier search line: [[miasnikov-1999-ac-genetic]] (GA search; the companion paper math/0304305 holds the length-12 frontier this paper cites)
- Open-problem context: [[open-problems-catalog]]
- Hard-instance generation siblings: [[kapovich-2003-generic-case-complexity]], [[elder-2015-random-trivial-words]]
- Batch synthesis: [[_synthesis-hard-instance-generation]]
- Project: [[project-challenge-gen]]

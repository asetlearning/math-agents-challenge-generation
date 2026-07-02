---
title: "String-Rewriting Systems"
authors: Ronald V. Book, Friedrich Otto
year: 1993
venue: "Springer-Verlag, New York"
isbn: "0-387-97965-4"
url: ""
language: en
domain: group-theory
status: stub
methodology_type: reference
citation_count: null
citation_count_date:
key_concepts:
  - "`[[Concepts/higman-lemma]]`"
  - "`[[Concepts/well-quasi-order]]`"
extends:
  - "[[knuth-bendix-1970]]"
contradicts: []
replicates: []
cites: []
cited_by: []
quality_notes: "Canonical textbook reference for string rewriting. Confirmed by Maria (2026-06-23) as THE reference bridging Higman's lemma to Knuth-Bendix / string-KB termination. Stub — no full-text pass done yet."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/rewriting-systems
  - topic/knuth-bendix
  - topic/well-quasi-order
  - topic/higman-theorem
  - paper
  - status/stub
---

# String-Rewriting Systems

## Citation

R.V. Book and F. Otto, *String-Rewriting Systems*, Springer-Verlag, New York, 1993. ISBN 0-387-97965-4.

## TL;DR

The canonical textbook for string rewriting theory. Lemma 1.2.3 (§1.2) states Higman's Theorem in the string setting: for any finite alphabet Σ, the subword order on Σ\* is a well-quasi-order (wqo). The rest of the book builds on this foundation — Noetherian string rewriting systems, Church-Rosser / confluence, completion (KB-like) procedures, and decidability results.

**Q1 relevance (wqo ↔ KB termination, settled):** This book is the direct published connection between Higman's wqo lemma and string-KB termination. Classical Higman (finite-alphabet case) + a well-founded reduction order is exactly what suffices for finite-alphabet string rewriting to be Noetherian. No bqo or generalized Higman machinery is needed for this. See [[_open-direction-wqo-ideal-kb-termination]] §Literature sources, S2.

## Key content (known from standard references)

- **§1.2 Lemma 1.2.3 (Higman's Theorem):** Σ finite → (Σ\*, ≤\_emb) is a wqo under subword embedding. Proof via Higman 1952 applied with the discrete order on Σ.
- **Noetherian string rewriting:** A string rewriting system (SRS) is Noetherian iff the rewriting relation is well-founded; well-founded reduction orders (compatible with Σ\*, length, etc.) are built on the Higman/wqo background.
- **Church-Rosser + Noetherian → confluence:** Newman's Lemma applies; a locally-confluent Noetherian SRS is confluent (=: complete, in the book's terminology).
- **Completion (KB for strings):** Procedures for completing an SRS to a confluent one mirror Knuth-Bendix; the wqo backbone underpins termination arguments.

## Open questions / data gaps

- No full-text pass done (stub). Exact page numbers for Lemma 1.2.3, the completion procedure, and the decidability chapters should be filled in on a full-text read.
- Specific treatment of string-KB vs. term-KB divergence (Book-Otto is strings only; see [[dershowitz-jouannaud-1990]] for the broader term-rewriting setting).

## Related material in vault

- Foundation: [[knuth-bendix-1970]] (original KB paper)
- Adjacent survey: [[dershowitz-jouannaud-1990]] (term rewriting; wqo background implicit)
- wqo theory: `[[Concepts/higman-lemma]]`, `[[Concepts/well-quasi-order]]`
- Open direction using this: [[_open-direction-wqo-ideal-kb-termination]] (S2)

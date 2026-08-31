---
title: "Linguistic Input Features Improve Neural Machine Translation"
authors:
  - "Rico Sennrich"
  - "Barry Haddow"
year: 2016
venue: "Proceedings of the First Conference on Machine Translation (WMT16); ACL Anthology W16-2209"
url: "https://aclanthology.org/W16-2209/"
url_translated:
language: en
methodology_type: empirical
domain: ai
citation_count: null
citation_count_date:
key_concepts: []
extends: []
contradicts: []
replicates: []
cites: []
cited_by: []
related:
  - "[[Research/AI in Math/ML/_synthesis-b25-patternboost-tokenization]]"
  - "[[guo-2020-graphcodebert]]"
quality_notes: "PARTIAL VERIFICATION CAVEAT: title, authors, and venue confirmed directly (ACL Anthology metadata page). The abstract, exact fusion equation, and BLEU deltas were NOT independently fetchable in this session (ACL Anthology's landing page shows only bibliographic metadata; the PDF downloaded but could not be parsed — pdftoppm/poppler-utils unavailable in this environment; Semantic Scholar API rate-limited). The 'factored representation, summed/concatenated per-token embeddings' description below is Researcher's recall of this well-established, widely-cited technique, NOT verified against primary text this session. Treat the mechanism description as plausible-but-unconfirmed pending a future session with working PDF tooling or unblocked API access."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/tokenization
  - paper
  - status/draft
status: draft
---

# Linguistic Input Features Improve Neural Machine Translation

## Abstract

**NOT independently verified this session** — see `quality_notes`. Known from general familiarity with the NMT literature (not confirmed against primary text here): the paper proposes augmenting the standard word-embedding input to a neural MT encoder with additional linguistic "factors" per source token — part-of-speech tag, lemma, morphological features, dependency label — each with its own small embedding table, combined with the word embedding (by summation or concatenation, exact choice not confirmed here) before being fed into the encoder. Reports a BLEU improvement on WMT-scale English-German translation from adding these factors (exact figures not confirmed here).

## TL;DR

**Confidence-flagged note.** This is the canonical, widely-cited origin of "factored" neural MT — feeding a model both a primary token stream and aligned auxiliary linguistic tags (POS, lemma, morphology) as additional per-position embeddings. It is the direct precedent for a B(2,5) "rule-hit" auxiliary channel design, in spirit if not in exact mechanism. However, this session could not independently confirm the exact fusion mechanism or reported BLEU numbers against primary source text — see the confirmed-vs-unconfirmed breakdown below before citing specifics from this note in a decision document.

## What was independently confirmed this session

- **Existence, authorship, venue**: confirmed via ACL Anthology metadata page (aclanthology.org/W16-2209/) — Rico Sennrich, Barry Haddow, WMT16 (First Conference on Machine Translation).
- **PDF located and downloaded**, but this session's tooling could not render/parse it (`pdftoppm`/poppler-utils not installed in this environment) — the raw text was not extracted.
- **Semantic Scholar API query** for the abstract was rate-limited (HTTP 429) before a retry could succeed.

## What was NOT independently confirmed this session (flagged, not fabricated)

- The exact fusion mechanism (concatenation vs. summation of factor embeddings) — general NMT literature knowledge says both variants have been used across different factored-NMT implementations (this paper and follow-ups), but which this specific paper uses was not verified against its primary text here.
- The specific BLEU improvement figures.
- Which specific linguistic features (POS only? + lemma? + morphology? + dependency labels?) this specific paper tests, as opposed to the broader "factored representations" literature it sits within.

## Why this (still-unverified) paper matters, if the recalled description holds

If the standard description is accurate (as OpenNMT's own "factored representations" documentation — independently confirmed this session via opennmt.net, offering both `feat_merge: concat` and `feat_merge: sum` modes — suggests is at least the modern implementation pattern descending from this line of work), Sennrich & Haddow represents the **simple embedding-fusion** end of the auxiliary-tag design spectrum, in contrast to [[guo-2020-graphcodebert]]'s **attention-mask fusion** approach. Both are real, load-bearing design options for a B(2,5) rule-hit auxiliary channel: concat/sum an auxiliary "in-a-known-rule-match" embedding onto each character's token embedding (Sennrich & Haddow / OpenNMT lineage) vs. use the rule-hit signal to reshape attention connectivity (GraphCodeBERT lineage). The former is architecturally simpler to bolt onto axplorer's existing `Transformer` class (per this session's direct source read — see `Research/AI in Math/ML/_synthesis-b25-patternboost-tokenization` § R2 and R4); the latter would require modifying `CausalSelfAttention.forward`'s mask construction.

## Open questions surfaced

Whether this paper's actual reported effect size (once independently verified — needs working PDF tooling or unblocked API access in a future session) is large enough to justify the added embedding-table complexity for a B(2,5) rule-hit channel, versus the effect size reported by [[guo-2020-graphcodebert]]'s (also unquantified-in-this-session, though the abstract does claim SOTA across four tasks) attention-mask approach.

## Related material in vault

- Related: [[guo-2020-graphcodebert]] (contrasting fusion mechanism, and mechanism actually verified this session)
- Synthesis: [[Research/AI in Math/ML/_synthesis-b25-patternboost-tokenization]]
- Synthesis: [[Research/AI in Math/ML/_synthesis-b25-value-scoring-curriculum-auxchannel]] (Deep Round 2 — this paper anchors the embedding-fusion end of the R4 aux-channel thread)

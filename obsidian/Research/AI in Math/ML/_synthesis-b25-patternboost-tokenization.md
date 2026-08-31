---
title: "Synthesis — Input/output representation for the B(2,5) PatternBoost transformer (AXPLORER v1 representation gate, Phase A)"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/tokenization
  - topic/length-generalization
  - topic/edit-representation
  - topic/patternboost
  - topic/b25
  - synthesis
  - status/draft
papers_synthesized:
  - "[[charton-2024-patternboost]]"
  - "[[Research/AI in Math/Tools/axplorer]]"
  - "[[charton-2022-linear-algebra-transformers]]"
  - "[[kazemnejad-2023-nope]]"
  - "[[gukov-2020-learning-to-unknot]]"
  - "[[petschack-2025-symmetric-group]]"
  - "[[nogueira-2021-arithmetic-limitations]]"
  - "[[singh-strouse-2024-tokenization-counts]]"
  - "[[cao-2026-adaedit]]"
key_concepts: []
date_range: 2020-06 to 2026-06
project:
status: draft
domain: ai
---

# Synthesis — Input/output representation for the B(2,5) PatternBoost transformer

> **Phase A literature scan only — analysis, no code.** Requested by Lead for the AXPLORER V1 REPRESENTATION GATE. This synthesis feeds the representation decision; it does not make it. Status `#status/draft`, not yet defended to Lead. Per instructions, Researcher is WAITING for explicit GO before any follow-up.

## The question

We are choosing the input/output representation for a decoder-only GPT in a PatternBoost loop ([[charton-2024-patternboost]]) that shortens B(2,5) identity-certificate words: raw alphabet `{a,b,A,B}`, current target 1348 characters, rule-bank LHS length 5–12, laptop compute, O(T²) attention. What does the literature say about (1) how PatternBoost itself tokenized comparable problems and whether tokenization choice measurably mattered to them, (2) precedent from axplorer specifically, (3) transformers on group-word / rewriting-system tasks, (4) edit/action-sequence representations vs. raw generation, (5) BPE on formal/algebraic sequences, (6) length generalization and positional encoding for long algebraic sequences, and (7) representations for search that must expand before it contracts.

## Sources reviewed

**Dedicated vault notes (this scan):** [[charton-2022-linear-algebra-transformers]], [[kazemnejad-2023-nope]], [[gukov-2020-learning-to-unknot]], [[petschack-2025-symmetric-group]], [[nogueira-2021-arithmetic-limitations]], [[singh-strouse-2024-tokenization-counts]], [[cao-2026-adaedit]].

**Pre-existing vault notes, re-read for this question:** [[charton-2024-patternboost]] (PatternBoost, arXiv:2411.00566), [[Research/AI in Math/Tools/axplorer]] (corrected this session — see below).

**Cited inline, no dedicated note (single-fact citations, evidence strength noted per claim below):** Lample & Charton, "Deep Learning for Symbolic Mathematics" (arXiv:1912.01412, 2019) — prefix-notation tokenization, no ablation reported; Levenshtein Transformer (Gu, Wang, Zhao, arXiv:1905.11006, 2019); Insertion Transformer (Stern et al., arXiv:1902.03249, 2019); NSEdit (arXiv:2204.06643, ICLR'22 workshop); Learning to Represent Edits (Yin et al., arXiv:1810.13337, ICLR'19); Aider practitioner benchmark (aider.chat/blog, non-peer-reviewed); GPT-f (Polu & Sutskever, arXiv:2009.03393, 2020); HyperTree Proof Search (Lample et al., arXiv:2205.11491, 2022); AlphaDev (DeepMind blog, Nature paper paywalled) and AlphaTensor (GitHub/Wikipedia, Nature paper paywalled); ByT5 (Xue et al., arXiv:2105.13626, 2021); Goat (Liu & Low, arXiv:2305.14201, 2023); Schmidt et al., "Tokenization Is More Than Compression" / PathPiece (arXiv:2402.18376, 2024); Ruoss et al., "Randomized Positional Encodings Boost Length Generalization" (arXiv:2305.16843, DeepMind, 2023); Jelassi et al., "Length Generalization in Arithmetic Transformers" (arXiv:2306.15400, 2023); Zhou et al., "Transformers Can Achieve Length Generalization But Not Robustly" (arXiv:2402.09371, 2024); Diekert, Duncan, Miasnikov, "Geodesic rewriting systems and pregroups" (arXiv:0906.2223, 2009); da Costa et al., "Learning 2-opt Heuristics for TSP via Deep RL" (arXiv:2004.01608, 2020).

**Areas searched with no direct hits (reported, not padded):** ML-for-Knuth-Bendix-completion (zero results across multiple query variants); ML for the Burnside-group word problem specifically (zero results); DRAT/SAT proof-trace learning as action sequences (zero results — nearest neighbors NeuroSAT/NeuroCore don't generate action sequences); non-monotonic/"uphill-move" representations in learned rewriting or local search (genuinely sparse — see § 7).

## Organized by representation family

### A. Character-level, raw {a,b,A,B} (current default in `datapoint.py`)

**Evidence for:** [[gukov-2020-learning-to-unknot]] — the closest task-shape analog found (variable-length generator-string words over a small algebraic alphabet, learned classification *and* learned word-simplification) used a raw generator-index representation, and per the subagent's extraction the raw generator-string encoding outperformed a more compressed structured alternative (Dowker-Thistlethwaite) by roughly 5 points — a mild point in favor of not over-engineering a compressed representation. Classifier accuracy also *improved* with braid-word length in that paper, a data point against "long raw sequences are unlearnable."

**Evidence against / caveat:** [[nogueira-2021-arithmetic-limitations]] shows plain character-level tokenization alone was **not** sufficient for exact 5-digit arithmetic — only adding explicit place-value/position tokens fixed it. This doesn't directly transfer (arithmetic needs position-*dependent* semantics; B(2,5) rule-firing needs offset-*invariant* pattern matching — see § F below on positional encoding, which is the more relevant lever for us, not the tokenization granularity axis this paper tests). But it is a live caveat: "character-level" is not a free pass just because it sidesteps BPE's boundary problem.

**Evidence strength:** MEDIUM. One close analog (Learning to Unknot) with a positive but not rigorously ablated signal; one cautionary tale (arithmetic) from a structurally different task. No paper tests character-level tokenization on our exact task shape (long, offset-invariant, symbolic rewriting).

### B. BPE / subword over {a,b,A,B}

**Evidence against, convergent and rigorous:** This is the best-evidenced conclusion in the whole scan. Four independent, methodologically rigorous sources converge on BPE hurting precision-critical, position/offset-sensitive symbolic tasks:
- [[nogueira-2021-arithmetic-limitations]]: subword tokenization "fails to learn addition of five-digit numbers."
- [[singh-strouse-2024-tokenization-counts]]: BPE's left-to-right digit grouping produces *systematic*, not random, error patterns; forcing a different grouping direction measurably changes accuracy — direct evidence that data-driven BPE boundaries are compression-driven, not motif-driven, and that this misalignment has a real, reproducible cost.
- Schmidt et al., "Tokenization Is More Than Compression" (arXiv:2402.18376, 64-model ablation): BPE's compression-minimization objective is not what makes it effective; segmentation strategy matters independently of token count — i.e. there's no reason to expect a compression-optimized BPE vocabulary to respect our length-5–12 rule-LHS motifs.
- ByT5 (arXiv:2105.13626): byte/character-level models are "significantly more robust to noise" and better on spelling/structure-sensitive tasks than subword models.

**Convergent with PatternBoost's own experience:** [[charton-2024-patternboost]] §3.1.2 reports naive BPE on flattened adjacency-matrix strings gave ~33% invalid model predictions; adding row delimiters *before* BPE (forcing token boundaries to respect row structure) dropped invalid predictions to 5–10%. This is PatternBoost's own authors hitting exactly the boundary-misalignment failure mode the arithmetic/tokenization-counts literature predicts, and fixing it by hand-aligning BPE boundaries to known structural units. **For B(2,5), the closest analog of "row delimiters" would be delimiting at rule-LHS boundaries — but rule LHS positions are exactly what varies per word and per rule, so there is no static delimiter to insert**, unlike PatternBoost's fixed matrix-row structure. This is a genuine disanalogy, not just a caveat.

**Evidence strength:** HIGH against plain/naive BPE for this task; the PatternBoost precedent additionally shows that *if* BPE is used, it needs a structural fix analogous to their delimiter trick, and B(2,5) doesn't have an obvious static structure to delimit against the way a matrix does.

### C. Fixed k-mer / block packing (axplorer `DenseTokenizer` idiom)

**No direct evidence found either way.** No paper in this scan tests fixed-width block packing (pack every k raw characters into one token) against character-level or BPE for a symbolic-rewriting task. Lead's own `AXPLORER_REPRESENTATION_NOTES.md` §6.3 raises the boundary-misalignment concern by analogy to the BPE case (a k=4 block tokenizer would still misalign token boundaries with length-5–12 rule motifs at arbitrary offsets) — this scan's BPE evidence (§B above) supports treating that concern as well-founded by analogy, since fixed-block packing has the *same* offset-insensitivity problem as BPE, without even BPE's advantage of being data-driven toward frequent motifs. **This is the weakest-evidenced family and the one where the concern is inferred, not directly measured.**

**Evidence strength:** LOW (no direct test), but the analogy to the BPE evidence is reasonably strong circumstantially.

### D. Structured/prefix notation (tree, Polish notation — Lample & Charton style)

Lample & Charton (arXiv:1912.01412) use prefix (Polish) notation for symbolic-math expression trees, motivated by parenthesis-freeness and shorter sequences — but report no ablation against infix or character-level, and their domain (expression trees with typed operators) doesn't map onto B(2,5) words, which have no tree structure — a word is a flat string, not an expression with operator arity. **Not directly applicable**; noted for completeness since Charton is a common author across this literature, but this family doesn't have a natural analog for flat generator-strings.

**Evidence strength:** NOT APPLICABLE — structural mismatch with the object type (B(2,5) words are flat strings, not typed expression trees).

### E. Edit / action-sequence generation (emit "apply rule R at position P" instead of raw characters)

**The most nuanced finding in the scan, and the one Lead should weigh most carefully before assuming this family is a win.**

- [[cao-2026-adaedit]] (most directly relevant, most recent, most rigorous): naive *offset-addressed* diff/edit formats are "highly unnatural" for LLMs to generate reliably (fragile offsets, fragmented hunks) — this is structurally close to our candidate edit op ("apply rule at position P"), which is itself offset-addressed. The paper's fix (BlockDiff/FuncDiff) works by addressing edits to *syntactic units* (functions, blocks) instead of raw offsets — B(2,5) has no such units to align to. Even where edit formats succeed, they only **match**, not exceed, full-generation accuracy; their real win is cost, concentrated on *long* files. This cuts both ways for us: our 1348-char target is "long" by code-editing standards (favoring edits on cost), but our edit ops are offset-addressed (the specific failure mode the paper documents), and we lack syntactic units to escape that failure mode the way BlockDiff/FuncDiff do.
- Levenshtein Transformer (arXiv:1905.11006) and Insertion Transformer (arXiv:1902.03249): motivated by *speed* (parallel/iterative decoding, dynamic length) and reusability across tasks, not by higher accuracy — both report roughly comparable-to-autoregressive quality, not superior quality, from the edit representation.
- NSEdit (arXiv:2204.06643) and Learning to Represent Edits (arXiv:1810.13337): both show edit-sequence models CAN beat full-rewrite or naive-edit baselines, but only when the edit encoder is context/position-sensitive (a "bag of edits" baseline loses badly, 23.73% vs 72.94% exact-match in one benchmark) — i.e. edit representations aren't free wins, they require real modeling investment to pay off.
- Practitioner data (Aider benchmark, non-peer-reviewed): format matters enormously in practice (26%→59% score from switching diff formats on one benchmark), and more recent practitioner consensus (Aider/Cursor/Morph) is that **full-file rewrites beat diffs below ~400 lines; diffs win above that** — a length-dependent crossover, not a universal edit-representation win.
- GPT-f (arXiv:2009.03393) and HyperTree Proof Search (arXiv:2205.11491) emit tactic/action sequences, but because the underlying verifier (Metamath, an ITP) is *inherently* tactic-based — the design choice is dictated by the execution environment, not chosen for a learnability advantage over raw generation. AlphaTensor/AlphaDev similarly use RL action spaces because the problem *is* posed as a game/MDP, not because raw-sequence generation was tried and found worse (no head-to-head ablation recoverable from available sources; Nature papers paywalled).

**Convergent takeaway:** the edit/action-sequence family's real, well-evidenced advantage is **cost/speed at comparable accuracy**, contingent on the edit format being addressed to something more stable than raw offsets (syntactic units in code; the ITP's own tactic language in theorem proving). B(2,5) rewrite-rule application is offset-addressed by nature (a rule fires wherever its LHS pattern matches in the current word) and has no syntactic-unit analog to fall back on — this is the one open, unresolved design tension this scan surfaces, not a settled recommendation either way.

**Evidence strength:** MEDIUM-HIGH that edit-sequence generation wins on cost, not accuracy, when it wins; LOW-to-untested specifically for offset-addressed edits without syntactic anchors, which is our case.

### F. Positional encoding (orthogonal axis — applies regardless of tokenization family chosen)

**Evidence strength: HIGH, and this is the most actionable, least ambiguous finding in the whole scan.** Multiple independent, rigorous, large-scale ablations converge:
- [[kazemnejad-2023-nope]]: NoPE (no explicit positional encoding) beats learned absolute, ALiBi, RoPE, and T5-relative on length-generalization/algorithmic-reasoning tasks; NoPE implicitly learns relative-position-like attention via SGD.
- Ruoss et al. (arXiv:2305.16843, DeepMind, 6000 models / 15 benchmarks): randomizing position indices during training gives +12.0% average accuracy over standard encodings.
- Jelassi et al. (arXiv:2306.15400): relative PE enables 5-digit→15-digit addition generalization; absolute PE does not.
- Caveat (Zhou et al., arXiv:2402.09371): even with the "right" PE, length generalization on algorithmic tasks is fragile and seed-dependent — validate empirically per-task, don't assume zero-shot transfer of these findings.

**Directly actionable:** axplorer's `model.py` uses **learned absolute positional embeddings** (`wpe = Embedding(block_size, ...)`) with a hard `block_size` cap (per Lead's `AXPLORER_REPRESENTATION_NOTES.md`) — the specific scheme this literature cluster finds *worst* for offset-invariant pattern tasks like ours (a rule-LHS match means the same thing regardless of where in the word it occurs). This is independent of, and composes with, whatever tokenization family is chosen.

**On attention sparsification:** at T≈1348, O(T²) full attention is ~1.8M entries/head — computationally trivial on a laptop. Sparse/local/sliding-window attention variants are unnecessary complexity for this scale; the evidence-backed lever is positional *scheme*, not attention pattern.

### G. Non-monotonic / "uphill move" representations (search area 7)

**Genuinely sparse — reported honestly, not padded, per role Stop Conditions.** After exhausting reasonable query variants (WebSearch was blocked at the session level for this task; substituted direct WebFetch queries against arXiv's own search UI):
- No paper on RL-for-local-search explicitly rewarding or representing temporary-worsening moves was found (TSP/scheduling RL papers like da Costa et al. 2020, arXiv:2004.01608, describe learned 2-opt policies but the retrievable abstract doesn't address worsening-move handling).
- No paper on neural-guided equation simplification discussing expand-before-simplify paths was found.
- On the Knuth-Bendix side specifically: Diekert, Duncan, Miasnikov (arXiv:0906.2223) is the one adjacent hit, but it goes the **opposite** direction from what we might have hoped — they construct "geodesically perfect" rewriting systems specifically by **avoiding** length-increasing rules, treating their absence as a design goal for well-behaved systems, not as evidence that such rules are a necessary detour. This is a mild point of *tension*, not confirmation, against our own v9 empirical finding (in project memory: same-length and reoriented length-increasing shortlex rules are critical for B(4,3) convergence) — worth flagging to Lead/Validator as a place where our own experimental result and one adjacent piece of literature pull in different directions, though the objects (geodesic normal forms in general groups vs. KB completion convergence speed for B(4,3)) aren't quite the same question.

**Implication for the PatternBoost scoring function:** since no literature guidance exists here, this remains an open empirical question for Experimenter, not something the literature can settle. If the scoring function trains the transformer only on *final* best results (as PatternBoost's architecture does), it should naturally tolerate non-monotonic intermediate paths — the risk is specifically in any *local-search* component that greedily rejects length-increasing moves before the global transformer ever sees the trajectory, which is a mixer/search-design question, not a representation question, and thus outside this scan's scope but worth routing to Developer/Experimenter.

**Evidence strength:** NONE FOUND for the specific intersection asked about; one adjacent, mildly tension-inducing data point.

## Convergence

1. **Representation choice measurably changes accuracy** — this is the single most consistently replicated finding across every family that has any evidence at all: [[charton-2022-linear-algebra-transformers]] (numeric encodings), [[nogueira-2021-arithmetic-limitations]] and [[singh-strouse-2024-tokenization-counts]] (digit tokenization), [[gukov-2020-learning-to-unknot]] (braid encoding), [[charton-2024-patternboost]] itself (BPE delimiter fix). No source in this scan found representation choice to be a non-factor.
2. **BPE's data-driven, compression-optimized boundaries do not respect fixed-length motifs at arbitrary offsets** — convergent, rigorous, and directly analogous to our rule-LHS-alignment concern.
3. **Absolute positional embeddings are the worst-evidenced choice for offset-invariant local pattern tasks** — convergent across three independent groups (Kazemnejad, Ruoss, Jelassi), and axplorer's current code uses exactly this scheme.

## Disagreement / tension

1. Our own v9 empirical finding (length-increasing/same-length rules are critical for B(4,3) cascade convergence) sits in mild tension with Diekert-Duncan-Miasnikov's framing of "no length-increasing rules" as a design *goal* for well-behaved rewriting systems — different questions (geodesic normal forms vs. completion speed), but worth a Validator sanity check before treating them as unrelated.
2. The edit/action-sequence literature is genuinely two-handed: real evidence it helps (cost, at comparable accuracy, GIVEN stable anchor points), and real evidence our specific case (offset-addressed rule application, no syntactic anchors) is closer to the documented *failure* mode ([[cao-2026-adaedit]]'s "fragile offsets") than the documented success case.

## What's settled

- Plain/naive BPE over {a,b,A,B} is evidence-backed to be a poor choice given our offset-invariant motif-matching requirement (§B).
- Learned absolute positional embeddings are evidence-backed to be a poor choice for this task shape; NoPE or relative PE is the literature-favored default (§F).
- O(T²) full attention at T≈1348 doesn't need sparsification on cost grounds alone (§F).
- The earlier vault claim that axplorer's native tokenizers are ready-made for B(2,5) words was wrong and has been corrected in [[Research/AI in Math/Tools/axplorer]] (restructure logged to `Agents/maumayma/Researcher/log.md`).

## What's contested / open

- Character-level raw tokenization: reasonably evidenced as a safe default (§A), but not proven sufficient on its own — no direct test on our exact task shape exists anywhere in the literature.
- Fixed k-mer/block packing: essentially untested; the boundary-misalignment concern is inferred by analogy to BPE, not measured (§C).
- Edit/action-sequence generation: the single most important open question this scan surfaces. The literature neither clearly recommends nor clearly rules out "apply rule R at position P" tokens — it depends on whether such a representation can be made robust to the "fragile offset" failure mode, which is untested for our domain (§E).
- Non-monotonic search representation: no literature exists at this intersection; this is an open empirical question, not a literature question (§G).

## Directly applicable to algo_mixing's current targets

- **Immediate, low-risk correction available regardless of which tokenization family Math-expert ultimately recommends:** switch away from learned absolute positional embeddings toward NoPE or a relative scheme. This is orthogonal to the tokenization-family debate and has the strongest, most convergent evidence in the entire scan.
- **If BPE is still considered:** PatternBoost's own §3.1.2 precedent (structural delimiters before running BPE) is the right template to adapt — but B(2,5) lacks a static structural unit to delimit against (unlike PatternBoost's matrix rows), so this would need a genuinely new idea (e.g., delimiting at known rule-bank LHS boundaries found by a pre-pass), not a direct port.
- **[[petschack-2025-symmetric-group]]'s "identity augmentation"** (padding variable-length words with relation-preserving no-op insertions rather than a generic pad token) is a concrete, cheap idea worth flagging to Developer/Math-expert as a B(2,5)-specific analog if raw character tokenization is chosen and batch-padding is needed.

## Open empirical questions for Experimenter (pending Lead's GO)

1. Does a BPE vocabulary trained directly on a B(2,5)-word corpus (not reused from a general-purpose tokenizer) still exhibit offset-dependent boundary drift on length-5–12 rule motifs, or does domain-specific training fix what general-purpose BPE gets wrong? ([[singh-strouse-2024-tokenization-counts]]'s open question, § "Open questions surfaced")
2. Does NoPE or relative positional encoding measurably improve rule-firing recognition (not just generic length generalization) for a decoder-only GPT on B(2,5) words, versus the current learned-absolute scheme in axplorer's `model.py`?
3. Is an offset-addressed edit representation ("apply rule R at position P") learnable at all for this task, or does it hit [[cao-2026-adaedit]]'s "fragile offset" failure mode absent a syntactic-unit analog to anchor to? This is the highest-uncertainty, highest-leverage open question from this scan.

## Related material in vault

- Papers: [[charton-2024-patternboost]], [[charton-2022-linear-algebra-transformers]], [[kazemnejad-2023-nope]], [[gukov-2020-learning-to-unknot]], [[petschack-2025-symmetric-group]], [[nogueira-2021-arithmetic-limitations]], [[singh-strouse-2024-tokenization-counts]], [[cao-2026-adaedit]]
- Tools: [[Research/AI in Math/Tools/axplorer]] (corrected this session), [[patternboost-v1-lineage]]
- Prior synthesis: [[_synthesis-ml-for-math]]
- Repo-local (not vault): `experiments/burnside/b25_patternboost/AXPLORER_REPRESENTATION_NOTES.md` (Lead's code-grounding read this synthesis builds on)

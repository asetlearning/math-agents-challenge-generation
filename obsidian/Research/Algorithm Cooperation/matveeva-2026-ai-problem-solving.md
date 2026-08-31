---
title: "Approaches to AI Problem Solving (conference slides)"
authors:
  - Mariia Matveeva
  - Vlad Stepanov
  - Alexei Miasnikov
year: 2026
venue: "Algebraic Geometry and Model Theory of Groups and Rings IV — Tbilisi, Georgia, 2026-08-28 (talk slides, 25 pages)"
url: ""
url_translated:
source_path: "Approaches-to-AI-Problem-Solving.pdf (local deck; ingested from ~/Downloads 2026-08-28)"
language: en
domain: methodology
status: draft
methodology_type: methodology
citation_count:
citation_count_date: 2026-08-28
key_concepts:
  - "[[Concepts/kb-mixing-stagnation]]"
  - "[[Concepts/mixable-api]]"
  - "[[Concepts/complete-rewriting-systems]]"
  - "[[Concepts/grobner-bases]]"
  - "[[Concepts/buchberger-algorithm]]"
extends:
  - "[[algo-mixing-burnside-slides]]"
contradicts: []
replicates: []
cites:
  - "[[havas-wall-wamsley-1974]]"
  - "[[kourovka-11.48-kostrikin-1990]]"
  - "[[algo-mixing-burnside-slides]]"
cited_by: []
quality_notes: "Talk slides, not a peer-reviewed paper — no abstract, no proofs beyond one proof idea (Theorem 3). Successor deck to [[algo-mixing-burnside-slides]] (2025); the B(4,3) headline number changed from 33 min / 54 sharing events to 13 s / 1 sharing event, so the two decks are not interchangeable as a source for that result — cite this one for the current figure. Slide-number footers are unreliable: 'Conclusions' and 'Other results' both read 20/21 and the final four slides carry no number; cite by PDF page. Author spelling: the deck writes 'Miasnikov'; elsewhere in this vault the same person is 'Alexei Myasnikov' ([[grobner]], [[daniyarova-myasnikov-2026]]). Theorems 3–5 (p.24) are attributed to an agentic-LLM setup and are stated without proof here except a one-line idea for Theorem 3 — unrefereed at ingest. Theorem 5 as printed reads C_A(a) = ⟨a⟩ ≅ Z^n, which pairs a cyclic-generated centralizer with a rank-n free abelian group; recorded verbatim below, flagged as a probable typo in Limitations."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/methodology
  - topic/mixer
  - topic/algorithm-portfolio
  - topic/knuth-bendix
  - topic/kbmag
  - topic/rewriting-systems
  - topic/divergence-and-stagnation
  - topic/bidirectional
  - topic/burnside
  - topic/b25
  - topic/b43
  - topic/b53
  - topic/b29
  - topic/restricted-burnside
  - topic/grobner-basis
  - topic/reinforcement-learning
  - topic/agentic-reasoning
  - topic/multi-agent-orchestration
  - topic/proof-search
  - topic/reproducibility
  - topic/diophantine-problems
  - topic/decidability
  - topic/wreath-products
  - paper
  - status/draft
project: mixer-core
---

# Approaches to AI Problem Solving

Matveeva, Stepanov & Miasnikov, invited talk at *Algebraic Geometry and Model Theory of Groups and Rings IV*, Tbilisi, 2026-08-28. Successor to [[algo-mixing-burnside-slides]] (2025).

## Abstract

> No abstract — source is a talk deck. The TL;DR below is the retrieval framing; the deck's own closing framing is quoted under **Quotes**.

## TL;DR

Reports the full arc of the algorithm-mixing program: mixed Knuth–Bendix orderings complete B(4,3) in **13 s** (one rule-sharing event, 60× standalone RPO), bidirectional beam search settles the B(5,3) word problem in **1.5 s** on a group whose completion ran 97 hours without finishing, and thirteen length-preserving "arms" under a bandit orchestrator reach **76% best / 28% average** reduction on the 119 B(2,5) challenge words — **but no word reaches `e`**. The deck then pivots: because search stalled, the program added a shared Obsidian record, six agent roles with refusal rules, and proof-skeleton dependency graphs; it closes with three new undecidability theorems for the Diophantine problem in wreath products obtained by Miasnikov through that agentic setup.

## Problem

Two problems, one method.

**The mathematical problem** (p.2): is `B(2,5) = ⟨a, b | w⁵ = e⟩` finite or infinite? Open since the 1930s; Kourovka Notebook 11.48. Knuth–Bendix does not terminate on B(2,5), so there is no confluent system to decide words with.

**The methodological problem** (p.12, p.15): after thirteen distinct computational approaches the challenge words still would not close, so the program added mathematical work alongside the computational work — "*which created a different problem: keeping track of all of it*" (p.12). With dozens of parallel attempts there was no way to answer "has this been tried?"

The deck's staged instrument table (p.2):

| Stage | Instrument |
|---|---|
| B(4,3) | rule injection into live KB |
| B(5,3) | beam search × mixed orderings |
| B(2,5) | core compression, biased KB, move policy |
| B(2,5) | knowledge graph, agents, proofs |

## Approach

**Algorithm mixing** (p.4): `Mixed(x) = Select(Alg₁, …, Alg_k)(x)`. Four strategies, with the deck's own examples:

| Strategy | Example |
|---|---|
| Switching | TimSort run detection |
| Racing | SAT solver portfolios |
| Cascading | query optimisation |
| **Interleaving** | **our Knuth–Bendix mixing** |

Three components: several algorithms with different strengths; a criterion for when to switch; a transform for what to share. In group theory the algorithms are KB completions under different reduction orderings — shortlex, RPO, weighted lex — and the shared artefacts are rewrite rules (p.4).

**Motivating case study — TimSort** (p.3): Python's sort (Tim Peters, 2002) is insertion sort on short runs plus merge sort to combine. Theoretically nothing is gained (comparison sorting cannot beat Ω(n log n), and on paper the combination is no better than merge sort); in practice it beats merge sort and QuickSort on real data. The claim the deck extracts: mixing pays on *structured* inputs, not in the worst case.

**Baseline and modifications** (p.6): KBMag (D. Holt) through GAP is the baseline everyone compares against. The program works from KBMag but modified heavily — live rule injection into a running completion, biased rule generation, and separate rule indices per ordering.

**The challenge words** (p.5): 119 words over `{a, A, b, B}` (capitals denote inverses), each a deeply nested commutator. The finiteness criterion: for a Burnside group one can write down a finite set `w₁, …, w_N` with the property *all wᵢ = e ⟹ the group is finite*; constructed from a nilpotent-quotient presentation (M. Hall and C. C. Sims), with the explicit B(2,5) set due to [[havas-wall-wamsley-1974]], who used it to show |R(2,5)| = 5³⁴. The computational task: reduce each word to the empty word using only consequences of `w⁵ = e`.

## Key result

Numbers below are verbatim from the deck; page numbers are PDF pages.

### B(4,3) — mixed completion (p.7)

Recipe: run RPO and shortlex in parallel; on stagnation inject the other ordering's rules, reoriented; tidy; continue until confluent.

`R_new = R_cur ∪ reorient(R_other, >_cur)`

- **13 s** to confluence, RPO agent
- **1** rule-sharing event
- **60×** vs standalone RPO
- confluent system has **2,333 rules**; **1,702,360** critical pairs checked, **none failed**; BFS enumeration returns **|B(4,3)| = 3¹⁴**

> "A single sharing event was enough. After it the RPO agent's rule count began to fall, and the system converged." (p.7)

Baseline: RPO completion running on its own on the same presentation. "Pure shortlex is not competitive here at all – it would need on the order of 500k rules." (p.7)

### B(5,3) — from completion to the word problem (p.8)

Completion never finished (97 hours), so the target changed: reduce the words we care about directly rather than build the whole system.

- **1.5 s** word problem solved; **98k** rules used
- for comparison: on the same group `kbprog` ran **97 hours to 11.7 million rules** and plateaued without ever completing

Beam search over rewrite rules: state = current word; move = apply one rule; at each step generate every applicable rewrite, score the results, keep the best K rather than the single greedy best; bidirectional (expand from the target word and from the identity, look for a meeting point); rules drawn from several KBMag completions under different orderings, fed to the beam as they arrive; dynamic conjugation when the beam stalls (replace `w` by `cwC`).

Two findings (p.8):
- The hardest words fell to shortlex. RPO for speed, shortlex for coverage — **the orderings are not redundant.**
- A merged rule bank ran about **2× slower** than separate per-source automata; rebuilding the merged index dominates.

### B(2,5) — the search problem (p.9)

- **119** challenge words; **2.2M** characters total; **42k** longest word; **17k** median length (p.5)
- rule banks reach **5.3 million rules**

| Method | Best | Avg |
|---|---|---|
| Greedy rewriting | ≈ 34% | near 0 |
| **Our stack** | **76%** | **28%** |

> "Five words reduced by more than 70%, far past anything greedy rewriting reaches. No word reaches e. One settles at 7,245 characters under every method we have." (p.9)

Structural reason the problem is not a hill climb: every rewrite must preserve the group element, so a reduction is a path through a space of equal-value words; the branching factor is large and the path can go **up** in length before it comes down.

### Core structure of the challenge words (p.10)

- **92.1%** of the average word is cores; **489** core occurrences (mean); **13** distinct connectors
- CoreA and CoreB are two fixed **35-character** blocks, formal inverses of one another; connectors are 1–7 characters between consecutive cores, reused throughout; a few dozen characters of prefix/suffix at each end
- `comm_13_10`, 2,500 characters: 66 cores · 2,310 chars · 92.4%; connectors · 141 chars · 5.6%; prefix + suffix · 49 chars · 2.0%. Most frequent connectors: `b ×16, B ×16, a ×8, A ×8, abA ×4`

### Exploiting the structure (p.11)

**Compression**: set `m := CoreA`, `M := CoreB`; run Knuth–Bendix over the six-letter alphabet `{a, A, b, B, m, M}` on a presentation carrying the exponent-5 relators plus the definitional equations for `m` and `M`. Every rule generated is a consequence of B(2,5) by construction, so nothing has to be re-certified afterwards. Result: **2,500 → 260** in the compressed alphabet.

**Biased rule generation**: `kbprog -sw <target> -sk 5` — rules preferentially built around the k-grams that actually occur in the target, so the bank matches where it is needed instead of everywhere.

### The orchestrator over thirteen arms (p.12)

| Arm | Effect on \|w\| |
|---|---|
| free cancellation `xX → e` | −2 |
| power collapse `U⁵ → e` | −5\|U\| |
| bank rule `L → R`, \|R\| < \|L\| | −Δ |
| greedy rewriter to fixpoint | ≤ 0 |
| bidirectional beam | ≤ 0 |
| core compression, then expand | ≤ 0 |
| biased-KB rules for this target | ≤ 0 |
| cyclic rotation by the period | 0 |
| conjugation `w → cwC` | +2\|c\| |
| relator insertion `c U⁵ C` | +k |
| macro search over insertions | ± |

State = current word; action = pull one arm; reward = net −Δ|w| **after a full re-reduction**, so an arm that lengthens the word only scores if the length comes back. A multi-armed bandit learns which arms pay off **per word, not on average**.

### The same mixer on Gröbner bases — results by Vlad Stepanov (pp.13–14)

Question: does adaptive strategy selection help Buchberger's algorithm?

Engine: custom implementation over `F₃₂₀₀₃` — product and chain criteria, sugar, and an F4-style batch step (all pairs of minimal degree reduced through one Macaulay matrix). Shared state is the pair `(G, P)` — current basis and pair queue. Selection heuristics `min-lcm, min-degree, sugar`; fourth arm `batch (F4)`; policies `UCB1, discounted bandit, contextual UCB`.

**11** benchmarks (cyclic-4…6, katsura-3…6, noon-5/6, random), **7** strategies cross-checked. Correctness first: all 7 strategies produce a **byte-identical reduced Gröbner basis on every instance**, cross-checked against sympy (p.13).

Wall-time against the per-instance best fixed strategy, over 11 instances (p.14):

| Strategy | Geomean | Worst case |
|---|---|---|
| fixed min-lcm | 1.42 | 7.2× |
| fixed min-degree | 1.38 | 7.0× |
| fixed sugar | 1.23 | 3.2× |
| fixed batch (F4) | 1.32 | 3.9× |
| **discounted bandit** | **1.22** | **1.75×** |

Worst cases: cyclic-6 for the selection heuristics, noon-6 for batch. No fixed strategy wins everywhere — each one has a catastrophic instance. The adaptive policy matches the best fixed strategy on average and **halves the worst case**, and beat the best fixed strategy outright on **2 of 11** instances (0.95×) without being told which strategy suits which ideal.

### The record and its scale (pp.15–16, 19)

- **698** interlinked notes in the main component, **2,448** links
- **45** experiment lines; **96** recorded runs; **13** approaches to B(2,5); **114** verification rulings

| Status | Count | Meaning |
|---|---|---|
| proven | 116 | survived a written ruling |
| conjectured | 682 | supported, not established |
| disproven | 18 | shown false |
| inconclusive | 42 | ran, decided nothing |

Per-group note counts (p.19; "counts are notes carrying a written ruling, not individual claims — a single note often contains several"):

| Group | Notes | Proved |
|---|---|---|
| B(2,9) | 198 | 81 |
| B(2,5) | 179 | 17 |

Proofs library: **17 lemmas proved**, 5 written up as standalone proofs, plus 7 further observations recorded as open. "Roughly half are negative results – routes closed with proof, and toolkits shown to be exhausted rather than merely unexplored." (p.19)

### Agent roles and refusals (p.17)

| Role | Task |
|---|---|
| Lead | briefs, gates between stages, keeps the ledger |
| Math-expert | proposes mechanisms and new constructions |
| Experimenter | pre-registers, runs, reports with receipts |
| Researcher | literature; verbatim extraction of cited results |
| Validator | rules on every claim — proved, disproved, or proved subject to a stated hypothesis |
| Delta | independent second opinion on a different model — attacks Validator's statements, and Validator attacks its own |
| Human | direction, go / no-go, arbitration |

Refusals: no result without its command output; no null without a firing witness; no unstated truncation; nobody closes their own line; both checkers run on the strongest models available. Every arrow is a read/write into the vault — **no agent messages another directly**.

### Proof skeletons (p.18)

State the argument as a dependency graph of named lemmas before proving any of them; work each node independently. Three outcomes per node: **proved** (downstream may cite it by name); **disproved** (the chain dies, and the record says where); **proved subject to H** (H becomes a new node). Uncovered nodes are counted in public and do not decrease until discharged. No agent holds the whole argument — the graph holds the dependencies, and a correction propagates to every citation. The illustrated skeleton has 6 nodes that are finite machine checks, each with a certificate and one replay command.

### Diophantine problem in wreath products — Miasnikov (pp.22–24)

Setting (p.22): the Diophantine problem for a group G asks whether there is an algorithm which, given an arbitrary finite system of equations with coefficients in G, decides whether that system has a solution in G. Throughout, `≀` is the restricted regular wreath product; in particular

`Z ≀ Z = ( ⊕_{i∈Z} Z_i ) ⋊ Z`

where the active copy of `Z` acts on the base group by shifting the coordinates.

**Prior results, restated verbatim (p.23):**

- **Theorem 1 (Miasnikov–Romanovskii).** The Diophantine problem in the restricted wreath product `Z ≀ Z` is undecidable. Equivalently, there is no algorithm which, for every finite system of group equations with coefficients in `Z ≀ Z`, determines whether the system has a solution in `Z ≀ Z`. More generally, the Diophantine problem is undecidable in every iterated restricted wreath product of k ≥ 2 infinite cyclic groups.
- **Theorem 2 (Kharlampovich–Miasnikov).** Let A and B be free abelian groups of finite ranks ≥ 1 with rank(A) > 1 and rank(B) > 1. Then the Diophantine problem in the restricted wreath product `A ≀ B` is undecidable.

References as printed (p.23): A. G. Miasnikov and N. S. Romanovskii, *Universal theories for rigid soluble groups*, Algebra and Logic **50** (2012), 539–552. O. Kharlampovich and A. Miasnikov, *The Diophantine problem in iterated wreath products of free abelian groups is undecidable*, arXiv:2502.09442, 2025.

**Three new theorems obtained through the agentic setup (p.24):**

- **Theorem 3 (Miasnikov – agentic LLM).** Let A and B be indicable groups; equivalently, suppose there exist epimorphisms `π_A : A ↠ Z` and `π_B : B ↠ Z`. Then the Diophantine problem in the restricted wreath product `A ≀ B` is undecidable.
  *Proof idea as printed*: cyclic retracts give a retraction `A ≀ B → ⟨a⟩ ≀ ⟨b⟩ ≅ Z ≀ Z`, so a system with coefficients in that copy is solvable in `A ≀ B` iff it is solvable in the copy. Apply Theorem 1.
- **Theorem 4 (Miasnikov – agentic LLM; cyclic-centralizer criterion).** Let A and B be groups. Suppose there exist `a ∈ A` and `b ∈ B` with `C_A(a) = ⟨a⟩ ≅ Z` and `C_B(b) = ⟨b⟩ ≅ Z`. Then the Diophantine problem in `A ≀ B` is undecidable.
- **Theorem 5 (Miasnikov – agentic LLM; cyclic-centralizer criterion).** Let A and B be groups. Suppose there exist `a ∈ A` and `b ∈ B` with `C_A(a) = ⟨a⟩ ≅ Zⁿ` and `C_B(b) = ⟨b⟩ ≅ Zᵐ`. Then the Diophantine problem in `A ≀ B` is undecidable.

Each statement says: no algorithm decides, for an arbitrary finite system of group equations with coefficients in `A ≀ B`, whether that system has a solution in `A ≀ B` (p.24).

## Assumptions

- **Mixed KB soundness is assumed, not proved.** Reorienting one ordering's rules into another agent's system and continuing to confluence is validated by the critical-pair check (1,702,360 pairs, 0 failures) and by BFS enumeration recovering `|B(4,3)| = 3¹⁴` — an empirical verification of the output, not a proof that the mixing procedure is sound in general. Carried over unchanged from [[algo-mixing-burnside-slides]].
- **The finiteness criterion is used as stated, for the restricted group.** The deck's own attribution (p.5) is that Havas–Wall–Wamsley used the explicit word set to show |R(2,5)| = 5³⁴ — i.e. an order computation for the *restricted* Burnside group. See Limitations.
- **Compression correctness rests on the presentation, not on a post-hoc check** (p.11): "Every rule it generates is then a consequence of B(2,5) by construction, so nothing has to be re-certified afterwards."
- **Gröbner timings assume a single custom engine** over `F₃₂₀₀₃` (p.13); the comparison is between strategies inside that engine, not against an external Gröbner implementation. Correctness — not speed — is cross-checked against sympy.
- **Theorems 3–5 are stated without full proofs in the deck**; only Theorem 3 carries a one-line proof idea, and all three depend on Theorem 1 (Miasnikov–Romanovskii) as the undecidability seed.

## Limitations / scope

- **The deck does not claim B(2,5) is finite or infinite.** Its own summary (p.20): "Not a solution to Burnside – a clear account of where the limit sits."
- **No challenge word reaches `e`** (p.2, p.9). 76% is the best single-word reduction; one word settles at 7,245 characters under every method.
- **Reducing the 119 challenge words is not the same as settling free B(2,5).** The set is the Havas–Wall–Wamsley pcps relator set, trivial in the restricted group `B₀(2,5)` by construction; the deck's finiteness criterion is stated for the general Burnside setting but the cited use is the |R(2,5)| = 5³⁴ computation. This scope distinction is settled elsewhere in the vault — see [[havas-wall-wamsley-1974]] and [[task14-hww-citation-and-119-words]]. The deck does not restate it.
- **Theorem 5 as printed is internally odd**: `C_A(a) = ⟨a⟩ ≅ Zⁿ` equates a centralizer generated by a single element with a rank-n free abelian group, which forces n = 1 and collapses Theorem 5 into Theorem 4. Recorded verbatim above; treat as a probable typo (most likely `C_A(a) ≅ Zⁿ` without the `⟨a⟩` clause) and confirm against the speaker's notes before citing.
- **Numbers are self-reported and the deck is unrefereed.** No error bars on the timings; the B(4,3) 13 s and the B(5,3) 1.5 s are single figures with no variance reported.
- **The Gröbner adaptive win is modest and narrow**: geomean 1.22 vs 1.23 for fixed sugar. The substantive claim is worst-case (1.75× vs 3.2×), on 11 instances.
- **The status ledger counts notes, not claims** (p.19), and "conjectured" (682) outnumbers "proven" (116) by roughly 6:1.

## Replication evidence

- **B(4,3)**: the confluence check (1,702,360 critical pairs, 0 failures) and independent BFS enumeration to `3¹⁴` are internal cross-validations, both reported in this deck and in [[algo-mixing-burnside-slides]]. Independent external replication: none known.
- **Gröbner**: all 7 strategies cross-checked to byte-identical reduced bases, and cross-checked against sympy (p.13) — a genuine external correctness oracle, though not a timing replication.
- **B(5,3), B(2,5)**: no replication; the 97-hour / 11.7M-rule `kbprog` plateau is the program's own baseline run.
- **Theorems 1–2** are published (Algebra and Logic 2012; arXiv:2502.09442) and not yet ingested into this vault. **Theorems 3–5** are new and unrefereed.

## Why this paper matters

This is the deck that closes the computational chapter of the algorithm-mixing program and opens the methodological one. Read against its predecessor [[algo-mixing-burnside-slides]], the B(4,3) result has gone from a 33-minute overnight run with 54 sharing events to 13 seconds with one — the same mechanism, engineered. But the more consequential content is negative: after thirteen distinct length-preserving attacks under a bandit orchestrator, the 119 words still do not close, and the deck says so plainly rather than reporting the 76% as progress toward a solution. That negative result is what motivates everything from p.15 onward.

The second half is the part that generalises. The shared-record architecture (one vault, agents and humans writing the same plain files, every note carrying status and scope and what it does not claim), the refusal rules (no result without command output, no null without a firing witness, nobody closes their own line), and above all the proof-skeleton pattern — state the argument as a dependency graph of named lemmas, work the nodes independently, let corrections propagate along citations — are presented as transferable, and the deck's own conclusion is that the skeleton is "the part we would keep for any other problem" (p.20).

The Miasnikov section is the external evidence for that claim: the same setup, pointed at the Diophantine problem in wreath products rather than at Burnside, produced three new undecidability statements (Theorems 3–5). If those survive refereeing, they are the strongest argument in the deck — a result in a different area, obtained by the method rather than by the Burnside-specific machinery. They also open a wreath-product line in this vault that currently has no paper notes behind it: neither Miasnikov–Romanovskii (2012) nor Kharlampovich–Miasnikov (arXiv:2502.09442) has been ingested.

## Quotes

1. > "Not a solution to Burnside – a clear account of where the limit sits" — p.20, "Where we are"
2. > "The searches found the core structure and the limits of what rewriting can reach, and that told us what was worth proving." — p.20, Conclusions

## Open questions surfaced

- **Researcher**: ingest Miasnikov–Romanovskii, *Universal theories for rigid soluble groups*, Algebra and Logic 50 (2012), 539–552, and Kharlampovich–Miasnikov, arXiv:2502.09442 (2025). Both are cited here as the seeds for Theorems 3–5 and neither has a vault note; `#topic/wreath-products` was registered for them.
- **Validator**: Theorem 5 (p.24) as printed collapses into Theorem 4 — confirm the intended hypothesis before the statement is cited anywhere.
- **Validator / Math-expert**: is mixed KB sound? The B(4,3) result has now been reproduced twice (33 min → 13 s) with the output verified each time, but the procedure itself is still only empirically validated. See [[Concepts/mixable-api]].
- **Experimenter**: the B(5,3) finding that "a merged rule bank ran about 2× slower than separate per-source automata" (p.8) is a concrete engineering claim with a stated mechanism (merged-index rebuild dominates). Does it hold on B(2,5)-scale banks (5.3M rules)?
- **Experimenter**: does the bandit orchestrator's per-word arm ranking (p.12) correlate with any structural feature of the word — core count, connector alphabet, prefix length — or is it unpredictable per instance?
- **Open, mathematical**: the one word that "settles at 7,245 characters under every method we have" (p.9). Is that a genuine local structure, or the limit of the current bank?
- **Gröbner line**: contextual UCB is listed as a policy (p.13) but only the discounted bandit appears in the results table (p.14). What did the contextual policy do?

## Related material in vault

- Extends: [[algo-mixing-burnside-slides]] — the 2025 predecessor deck; same program, earlier numbers.
- Contradicts: (none — supersedes rather than contradicts; see quality_notes on the changed B(4,3) figure)
- Replicates: (none)
- Concepts introduced/used: [[Concepts/kb-mixing-stagnation]], [[Concepts/mixable-api]], [[Concepts/complete-rewriting-systems]], [[Concepts/grobner-bases]], [[Concepts/buchberger-algorithm]]
- Cites (in vault): [[havas-wall-wamsley-1974]] (the 119-word set and |R(2,5)| = 5³⁴), [[kourovka-11.48-kostrikin-1990]] (the open problem)
- Cited by (in vault): (none yet)
- MOC: [[_moc-algorithm-cooperation]] — the cooperating-partial-oracles paradigm this deck instantiates.
- Also see: [[gomes-selman-2001-portfolios]] and [[hamadi-et-al-2009-manysat]] for the portfolio/clause-sharing theory the mixing recipe mirrors; [[grobner]] for the other Gröbner line in this vault (Kreuzer–Myasnikov–Rosenberger, quotient tests); [[Research/AI in Math/_MOCs/_moc-ai-in-math]] for the agentic-systems context of pp.15–19.
- People: [[People/maumayma]]

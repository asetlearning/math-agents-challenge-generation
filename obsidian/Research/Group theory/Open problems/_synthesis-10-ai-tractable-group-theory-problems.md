---
title: "Ten AI-Tractable Open Problems in Group Theory — Targets for an Agentic System"
domain: group-theory
status: draft
author: maumayma
related:
  - "[[open-problems-catalog]]"
  - "[[kourovka-2022]]"
  - "[[_synthesis-agents-for-math]]"
  - "[[charton-2024-patternboost]]"
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/burnside
  - topic/b25
  - topic/word-problem
  - topic/knuth-bendix
  - topic/braid-groups
  - topic/andrews-curtis
  - topic/finitely-presented-groups
  - topic/proof-search
  - synthesis
  - status/draft
---

# Ten AI-Tractable Open Problems in Group Theory — Targets for an Agentic System

**Purpose.** Curate ten *unsolved* group-theory problems where a Claude-agent system (search + oracle-verification + learned scoring, of the kind built for B(2,5)) has genuine traction. This is the AI-attack shortlist companion to [[open-problems-catalog]] — that note scores a broad set on Mixer feasibility; this note picks the **ten highest-leverage agentic targets** and says *how* an agent would attack each.

**Companion, not duplicate.** Where a problem already has a vault note (B(2,5) finiteness, Andrews-Curtis, Burau-4, braid membership, Kaplansky), this synthesis links it and adds the *agentic attack plan*; it does not restate the mathematics.

---

## The tractability criterion (why these ten, and not "famous open problems")

A problem is **agentically tractable** when it reduces to a **search-with-cheap-verification** loop, not a structural theorem. Concretely, all three must hold:

1. **Certificate search.** A YES answer is a concrete finite *object* — a word, a reduction chain, a construction, a counterexample — living in a huge but structured space an agent can search (beam/KB/RL/PatternBoost-style generate-and-test).
2. **Cheap oracle verification.** Any candidate certificate is *checkable* fast by a tool the agent already trusts: GAP finite-quotient evaluation, `nq`/p-quotient, KB word-equality, Todd–Coxeter coset enumeration, matrix computation. Verification ≠ the open problem.
3. **Asymmetry in our favour.** Either the *object exists and is findable by search* (the hard part is finding, not certifying), or *its non-existence up to a bound is checkable*. Problems asking "prove property P for **all** groups in an infinite class" fail this — no finite certificate — and are excluded.

**Hard-won lesson (from the B(2,5) program):** the danger is not the search, it's *premise/scope verification* — computing in the wrong object (a finite quotient standing in for a free group) and mistaking a by-construction triviality for a proof. Every target below carries a **scope caveat** naming exactly what a certificate would and would not prove. This is the single most important discipline: see [[b25-q5-feasibility-verdict]] § CIRCULARITY ANALYSIS for how it went wrong once.

**Scoring.** Reuse the [[open-problems-catalog]] rubric (3 = direct search+verify attack with existing infra; 2 = agent contributes a step / partial evidence; 1 = needs structural insight search can't reach). Every target here is 2 or 3 *by selection*.

---

## The Ten (easier-but-open — all NEW to the vault)

Chosen for the **easier** end: small/bounded finite search, a **single decisive cheap oracle** (GAP / Todd–Coxeter / direct computation), and a YES that is one self-certifying object. None duplicates an existing vault note (B(2,5), Andrews–Curtis, Kaplansky, Burau are deliberately NOT here).

### 1. Ore-type commutator gaps in small finite groups — which groups have a non-commutator?
**Score: 3.** New. (Ore's conjecture — every element of a non-abelian finite *simple* group is a commutator — is proven; the OPEN, *easier* neighbourhood is non-simple: characterise/enumerate the finite groups in which NOT every element is a commutator, and the extremal cases.)
- **Attack.** For each group in the GAP `SmallGroups` / perfect-group libraries up to a bound, compute the **commutator-value set** and flag groups with a non-commutator (smallest known has order 96). Search for extremal patterns — e.g. "exactly one non-commutator" (see [arXiv:2509.17587](https://arxiv.org/pdf/2509.17587)) — and settle open bounded-order instances.
- **Verify.** "Is g a commutator in G?" is one exact GAP call (`g in CommutatorValues(G)` style). Fully self-certifying per group.
- **Scope caveat.** A characterisation over a bounded order range is a real result; it does not settle infinite families without a pattern-proof (hand off conjectured patterns to a human).
- **Why easy.** Finite, enumerable, one decisive GAP oracle, no free-group scope trap. Ideal warm-up target.

### 2. Minimal number of generators (rank) of specific finite groups where it's unrecorded
**Score: 3.** New.
- **Attack.** For families of finite groups (specific `PSL`, wreath products, `p`-groups) the exact **minimal generating set size** `d(G)` is unknown or unverified in cases. Search generating tuples of size `k` (increasing `k`); the first `k` that generates is `d(G)`.
- **Verify.** "Does this `k`-tuple generate `G`?" is a single GAP subgroup-order check. `d(G)=k` is certified by a generating `k`-tuple + a proof no `(k−1)`-tuple works (exhaustive for small `G`, or a lower-bound invariant like the abelianization rank).
- **Scope caveat.** Exhaustive lower bound only feasible for small/structured `G`; otherwise the result is "≤ k" (an upper bound) unless a matching invariant lower bound is found.
- **Why easy.** Generation is a one-line GAP test; the search is a bounded tuple enumeration. Direct fit.

### 3. Cayley-graph diameter / "God's number" for permutation puzzles and groups (CayleyPy line)
**Score: 2–3.** New — live AI frontier ([arXiv:2502.18663](https://arxiv.org/pdf/2502.18663), [arXiv:2509.19162](https://arxiv.org/pdf/2509.19162)).
- **Attack.** The **diameter** of a Cayley graph (max shortest-path length — "God's number" for puzzle groups) is unknown for many concrete generator sets. RL/bidirectional-BFS pathfinding (CayleyPy) computes exact diameters and *generated hundreds of open growth-formula conjectures* an agent can extend and test.
- **Verify.** BFS / bidirectional search on the explicit Cayley graph certifies a diameter or a shortest path exactly. A conjectured growth formula is checked against computed growth sequences on larger instances.
- **Scope caveat.** A computed diameter is a theorem-by-computation; a *conjectured* formula verified on instances is a conjecture (needs a human proof).
- **Why easy.** Exact BFS oracle, no algebraic subtlety, and the open conjectures are pre-generated. Reuses beam/RL search directly.

### 4. Efficient / short presentations of specific finite (often simple) groups
**Score: 2–3.** New. (Adjacent to the SL(n,q)/Mathieu lines but no dedicated note.)
- **Attack.** Whether a given finite group has a presentation of a target (short) length, or is *efficient* (deficiency-zero), is open in cases. Search the presentation space for a short presentation whose group has the correct order.
- **Verify.** **Todd–Coxeter coset enumeration** confirms the presented group's order — decisive and self-certifying. A short presentation that enumerates to `|G|` is a certificate.
- **Scope caveat.** A found short presentation is a concrete result for that group; the general efficiency question stays open.
- **Why easy.** Bounded presentation search + one decisive coset-enumeration oracle; GAP/ACE tooling exists.

### 5. Minimal-length words for specific elements in finite groups (word-length / "factorisation" table gaps)
**Score: 3.** New.
- **Attack.** For a fixed finite group `G` and generating set `S`, the **word length** of a specific element (shortest expression in `S`) is often unrecorded. Bidirectional BFS / beam finds the shortest word; an agent fills in / conjectures the full length distribution.
- **Verify.** Evaluate the candidate word in `G` (one multiplication) = target element ✓; length is the objective; BFS certifies minimality up to the searched radius.
- **Scope caveat.** "Shortest found" = minimal only if BFS reached the element's radius; otherwise an upper bound.
- **Why easy.** Same machinery as #3, exact one-multiplication oracle. A gentle reuse of the reducer/beam stack on *finite* groups (no free-group trap).

### 6. Spectral gap / expansion constants of specific Cayley graphs (bounded, computable)
**Score: 2.** New.
- **Attack.** The **spectral gap** (second eigenvalue) and expansion constant of a Cayley graph on a specific finite group + generator set determine expansion; exact values are unrecorded for many concrete cases. An agent computes the adjacency spectrum and searches generator sets maximising the gap (better expanders).
- **Verify.** Eigenvalue computation of the (explicit, finite) adjacency matrix — exact/numeric, cheap. A better-expanding generator set is a concrete artifact.
- **Scope caveat.** Numeric eigenvalues need interval/exact arithmetic for a rigorous bound; a found better generator set is self-certifying by its computed spectrum.
- **Why easy.** Linear algebra on a finite matrix; bounded generator-set search. FunSearch-style construction of good expanders is a proven paradigm.

### 7. Autourphism-group / character-table–distinguishing invariants for isospectral or "same-table" groups
**Score: 2.** New.
- **Attack.** Non-isomorphic groups can share a character table (Brauer pairs) or other invariants; finding new small examples, or an invariant that separates a specific known-hard pair, is a bounded search over `SmallGroups`.
- **Verify.** GAP computes character tables / the candidate invariant exactly; a separating invariant or a new same-table pair is self-certifying.
- **Scope caveat.** Instance-level; a new pair/invariant is a concrete result, not a classification.
- **Why easy.** Pure GAP enumeration + exact invariant computation. No search subtlety.

### 8. Coset-diagram / low-index-subgroup gaps for finitely-presented groups
**Score: 2–3.** New.
- **Attack.** For a finitely-presented group, enumerate **low-index subgroups** (Todd–Coxeter / `LowIndexSubgroups`) to settle questions like "does `G` have a subgroup of index `n`?" or to build a permutation quotient separating a target element — open for specific `G,n`.
- **Verify.** Low-index enumeration is exhaustive up to the index bound (self-certifying: it either finds a subgroup or proves none exists ≤ that index).
- **Scope caveat.** Bounded to the index searched; "no subgroup of index ≤ n" is decisive only up to `n`.
- **Why easy.** A single decisive algorithm (`LowIndexSubgroupsFpGroup`) that both finds and proves-absence within the bound.

### 9. Growth-series / geodesic-count formulas for specific 1- or 2-relator groups
**Score: 2.** New.
- **Attack.** For a fixed automatic / small-cancellation group the **growth series** (number of elements at each word length) sometimes lacks a closed form. Compute the growth sequence via the automatic structure / BFS on the (infinite but locally-finite) Cayley graph up to radius `R`, then conjecture a rational generating function and verify it against the computed terms.
- **Verify.** KBMAG's automatic-structure word-acceptor gives exact growth counts; a conjectured rational series is checked against them.
- **Scope caveat.** Verified-on-terms = conjecture; a proof needs the automatic structure's regular-language argument (hand off, but the data is decisive).
- **Why easy.** KBMAG already computes automatic structures / growth for these groups; the "AI" part is conjecturing + verifying the closed form — a clean pattern-finding task.

### 10. Small unsolved **Kourovka Notebook** finite-group problems with a GAP-enumeration angle
**Score: 2–3.** New. (The 2024 Kourovka-solutions line, [arXiv:2607.17477](https://arxiv.org/abs/2607.17477), shows several fell to exactly this method.)
- **Attack.** Scan the current Kourovka Notebook for **still-open** problems phrased as "does there exist a finite group with property P?" or "is P true for all groups of order/type T?" with `P` GAP-checkable. Prune with necessary conditions (Frobenius-type, perfect-group libraries), then enumerate and certify per candidate.
- **Verify.** Per candidate group, `P` is an exact GAP computation. Existence → one witnessing group; bounded universal → exhaustive check over the (pruned) library.
- **Scope caveat.** Only the *bounded / existence* Kourovka problems fit; genuinely infinite-family universals need a proof, not enumeration. Pick the enumerable ones.
- **Why easy.** This is the exact recipe that just solved several Kourovka problems via GAP; a rich supply of small, oracle-checkable targets. Start here for volume.

---

## Cross-cutting: how the agentic system attacks all ten

The same architecture (already built for B(2,5)) generalises:

- **Generate:** transformer/PatternBoost proposes candidate certificates (words, braids, presentations, quotient maps, rules); or classical search (beam/KB/SAT/Todd–Coxeter) enumerates.
- **Score:** a cheap proxy (e.g. % reduction, oracle-distance, constraint-violation count) ranks candidates; the transformer *learns* the proxy from oracle feedback (the resolved B(2,5) proxy question: use the reducer/oracle signal, let the NN learn scoring).
- **Verify:** a trusted oracle (GAP finite-eval, `nq`, KB word-equality, Todd–Coxeter, matrix/group-ring arithmetic) certifies any winner — **full verification, never a necessary-but-insufficient shortcut** (the abelianization/premise-verification lesson).
- **Gate:** every positive result passes a sanity gate (no degenerate/empty/by-construction "wins"; correct group/scope; witnessed path) before it counts — see the B(2,5) reward-hack incident for why this is mandatory.

## Selection honesty / what is deliberately EXCLUDED

- **"Prove P for all groups in class C"** (no finite certificate) — e.g. general residual finiteness, general AC, general Burau faithfulness. The agent attacks *instances/counterexamples*, not the universal statement.
- **Deep classification / structural theorems** (score 1) — no search-verify decomposition.
- **Problems with no trusted oracle** — if a candidate can't be cheaply certified, the search has no ground truth and the agent can fool itself (the recurring failure mode).

## All ten are NEW to the vault (deliberately)

None of these has an existing Open-problems note — they were chosen precisely to *not* duplicate what's already tracked. The hard/heavy flagships (B(2,5) finiteness, Andrews–Curtis, Kaplansky, KB-confluence-for-B(2,5), Dehn/identity-certificate shortening) are kept in their own existing notes and the [[open-problems-catalog]]; this list is the **easier, fast-oracle** shortlist.

**Note for the catalog:** [[burau4-faithfulness]] is now SOLVED (faithful, [arXiv:2607.05283](https://arxiv.org/abs/2607.05283), 2026) — mark it accordingly.

## Recommended first three to actually run

Easiest onboarding, cheapest decisive oracle, most open targets: **#10 (Kourovka bounded-existence problems — the exact recipe that just solved several via GAP, high volume of targets), #1 (Ore-type commutator gaps in small groups — one GAP call per group), #3 (Cayley-graph diameter — exact BFS, pre-generated open conjectures).** Runner-up: **#2 (minimal generating set — one-line generation test).** All four are pure finite-group GAP/BFS work: no free-group scope trap, a single self-certifying YES per instance, and immediate reuse of enumeration + beam/BFS. Start with #10 for breadth, #1/#3 for clean single wins.

## Related material in vault

- Feasibility scoring companion: [[open-problems-catalog]]
- Kourovka source: [[kourovka-2022]]
- AI-for-math paradigms: [[_synthesis-agents-for-math]], [[_synthesis-ai-agent-discoveries-2026]], [[charton-2024-patternboost]], [[romera-paredes-2023-funsearch]]
- The scope/verification discipline that governs all of these: [[b25-q5-feasibility-verdict]] § CIRCULARITY ANALYSIS; the mandatory sanity gate in [[PatternBoost/methodology/patternboost-b25-loop-prereg-2026-06-30]]
- Existing HARD flagships (kept in their own notes, deliberately NOT in this easier list): [[b25-finiteness-11.48-kostrikin]], [[andrews-curtis-conjecture]], [[kaplansky-zero-divisors]], [[wagner-2020-torsion-quadratic-dehn]]
- Sources for the NEW easier problems (create per-problem stubs if pursued):
  - Ore-type / non-commutator gaps: [arXiv:2509.17587](https://arxiv.org/pdf/2509.17587) (finite groups with exactly one non-commutator); smallest non-commutator group has order 96
  - Cayley-graph diameter / growth (CayleyPy): [arXiv:2502.18663](https://arxiv.org/pdf/2502.18663), [arXiv:2509.19162](https://arxiv.org/pdf/2509.19162)
  - Kourovka bounded-existence problems solved by GAP-enumeration: [arXiv:2607.17477](https://arxiv.org/abs/2607.17477)
  - FunSearch/AlphaEvolve construction paradigm (for #6 expanders): [Nature 2023](https://www.nature.com/articles/s41586-023-06924-6)
- Tooling reused: GAP `SmallGroups`/perfect-group libraries, Todd–Coxeter/`LowIndexSubgroupsFpGroup`, KBMAG automatic structures, the beam/BFS stack
- SOLVED, mark accordingly: [[burau4-faithfulness]] — faithful, [arXiv:2607.05283](https://arxiv.org/abs/2607.05283) (2026)

### Later additions (2026-08-31)

- [[_kourovka-20-corpus]] — the 2026-08-11/08-20 Kourovka wave postdates this synthesis: the full 20-issue corpus index plus ~60 individual problem notes (12.15 through 21.137) under `Open problems/Kourovka/` — exactly this synthesis's candidate pool. Re-run the tractability screen against that corpus on the next pass.

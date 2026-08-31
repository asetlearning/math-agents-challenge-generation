---
title: "Synthesis — Deep Round 2: value/cost-to-go scoring, axplorer source read, length curriculum, and auxiliary-tag fusion for B(2,5) PatternBoost"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/value-network
  - topic/length-generalization
  - topic/tokenization
  - topic/edit-representation
  - topic/patternboost
  - topic/b25
  - synthesis
  - status/draft
papers_synthesized:
  - "[[agostinelli-2019-deepcubea]]"
  - "[[segler-2018-retrosynthesis-mcts]]"
  - "[[chervov-2025-cayleypy-rl]]"
  - "[[futuhi-sturtevant-2026-admissible-heuristics]]"
  - "[[skalse-2022-defining-reward-hacking]]"
  - "[[ruoss-2023-randomized-positional-encodings]]"
  - "[[zaremba-sutskever-2014-learning-to-execute]]"
  - "[[agarwal-2021-polynomial-simplification-curriculum]]"
  - "[[mehta-2026-randomized-yarn]]"
  - "[[petschack-2025-symmetric-group]]"
  - "[[guo-2020-graphcodebert]]"
  - "[[sennrich-haddow-2016-linguistic-features]]"
key_concepts: []
date_range: 2014-10 to 2026-06
project: b25
status: draft
domain: ai
---

# Synthesis — Deep Round 2: value scoring, axplorer source, curriculum, auxiliary-tag fusion

> **Phase A follow-up, analysis only.** Requested by Lead as a deeper pass on four threads Phase A ([[_synthesis-b25-patternboost-tokenization]]) left open. Status `#status/draft`, not yet defended. Builds directly on peer work already on record for this gate: Math-expert's 13-family slate ([[Agents/maumayma/MathExpert/b25-axplorer-representation-gate-phase-a-2026-07-17]]), Validator's constraints/Phase-B audit, B25 Experimenter's empirical grounding ([[axplorer-representation-grounding-2026-07-17]]), and Lead's verdict (`AXPLORER_REPRESENTATION_VERDICT.md`, repo-local). This note does not re-litigate the representation verdict (char-level, already decided) — it goes deeper on scoring/objective (R1), source-code ground-truth (R2), curriculum (R3), and aux-channel design (R4).

## R1 — Learned value / cost-to-go scoring

### The question and why it's the highest-leverage thread

The current objective (per the verdict, C9-fixed to `−len(reduce(W))`, absolute residual) is still fundamentally **greedy**: it scores a candidate only by where the deterministic reducer leaves it, with no notion of "this word is far from any local optimum but structurally close to a big future reduction." Experimenter proposed DeepCubeA and Segler's retrosynthesis system as principled alternatives — learned value/cost-to-go functions that guide search past exactly this kind of local blindness.

### 1. DeepCubeA / DeepCube — the real training procedure

[[agostinelli-2019-deepcubea]] (read at the level of the open 2018 NeurIPS precursor + the DeepCubeA GitHub README, since the Nature MI paper itself is paywalled with no arXiv preprint): trains a cost-to-go value network via **Approximate/Deep Value Iteration** — generate states by scrambling **backward from the solved goal**, bootstrapped one-step-lookahead regression target `target(x) = min_a(cost(a) + v(child_a))` using the network's OWN current estimate for children, stabilized by (a) a **target network** updated only when training loss drops below a threshold, (b) a curriculum **built into the data generation itself** (backward scrambling guarantees near-goal easy cases are always present), and (c) **inverse-scramble-depth sample weighting** (`W(x)=1/D(x)`) which DeepCube's own paper credits directly with eliminating divergence ("We didn't see divergent behavior after this addition"). Search-time: DeepCubeA uses **weighted A***, `f(n)=λg(n)+h(n)`, with **no admissibility guarantee claimed** — deliberately "good enough, fast," not optimality-preserving.

**Evidence strength: HIGH** (peer-reviewed, open-sourced, reproducible). **Portability caveat**: backward-from-goal data generation is cheap for Rubik's Cube specifically because its move set is exactly invertible; B(2,5)'s rewrite rules are mostly one-directional (length-decreasing), so an analogous "generate hard training words by un-reducing from the identity" scheme needs real design work, not a direct port — flagged as the concrete open question for Experimenter/Developer.

### 2. Segler retrosynthesis — a correction to the premise

[[segler-2018-retrosynthesis-mcts]]: **there is no dedicated value network here.** The system is 3-network MCTS (expansion policy, fast rollout policy, feasibility filter), all trained **supervised** on 12.4M literature reactions, with node values coming from **classic AlphaGo-style Monte Carlo rollout outcomes** (roll the fast policy out to a terminal state, use the result), not from a trained value regressor. This is architecturally a materially different, and in one sense simpler, technique than DeepCubeA's: B(2,5) already HAS a fast deterministic reducer, which could itself serve as a "rollout policy" inside an MCTS/beam search — potentially delivering Segler's benefit (non-greedy node evaluation) with **no learned value network required at all**. This is flagged as a genuinely open, possibly higher-leverage alternative to a trained value head, not a settled recommendation.

**Evidence strength: HIGH for what it actually is** (peer-reviewed Nature paper + open precursor), but it answers a different question than R1 asked — this is the most important correction in this thread.

### 3. Distance-to-identity for group elements — CayleyPy RL

[[chervov-2025-cayleypy-rl]] is the closest group-theory analog found across all three literature rounds: learns a diffusion-distance-style heuristic for elements of a permutation group's Cayley graph, guides **beam search** toward the identity, and **validates directly against GAP**.

**Deep Round 3 update (2026-07-17) — methods read at implementation depth, transfer verdict delivered.** Full findings in [[chervov-2025-cayleypy-rl]] § Methods at implementation depth. Summary: the gating question was whether CayleyPy's invertible-generator, finite-graph requirements block transfer to B(2,5)'s mostly one-directional rule bank. **Answer: the mechanism transfers, but not via the rule bank.** CayleyPy's own generating set (`a_i^{±1}`, explicitly symmetric) is the wrong comparison point for our rule bank — the right comparison is B(2,5)'s actual generators `{a,b,A,B}`, where `A=a⁻¹`/`B=b⁻¹` are inverse pairs by construction. A CayleyPy-style forward random walk from the empty word in this alphabet is directly available and **already partially built** (the `rand_walk` category in B25 Experimenter's 12k held-out pool). The finiteness requirement is satisfied because this gate's actual scope is `B₀(2,5)` (finite, order 5^34), not free B(2,5) (infiniteness open, out of scope). What does NOT transfer: CayleyPy's distance LABEL (raw walk-length, a proxy that only works because their downstream task is literally "shortest word in the walk's own generators") — for us, `len(reduce(word))` from the existing `braid_reduce` reducer is a stronger, already-available label, and should replace CayleyPy's walk-length proxy rather than porting it directly.

**Evidence strength: HIGH** (published, GAP-validated methodology, now read at implementation depth) — **substantially de-risks the value-head proposal**: the hardest-seeming piece (training-data generation for a mostly-one-directional rewrite system) has a concrete, low-cost answer once the generating-set/rule-bank distinction is made explicit.

### Segler "reducer-as-rollout, no value net" — is it the safer first bet?

**Yes, and this round's analysis sharpens why.** Because it uses NO learned value function at all, "reducer-as-rollout" (run the actual `braid_reduce` reducer to a fixed point inside an MCTS/beam node evaluation, instead of a trained value head) structurally cannot exhibit the bias-entrenchment failure mode Validator flagged and Skalse et al. formalize (§ R1 Addendum) — there is no proxy to hack, because the "value" IS the real, already-trusted scoring authority (the same reducer the verdict's C9 fix already scores against). It also sidesteps bootstrapping instability and the admissibility question entirely — none of DeepCubeA's stabilization machinery (target networks, curriculum-via-data-generation, sample reweighting) is needed, because there's no bootstrapped regression loop to destabilize.

**The one caveat, and it's a cost question, not a safety question:** this trades LEARNED-FUNCTION risk for COMPUTE cost — every node evaluation is a full reducer call rather than one cheap forward pass through a small value network. DeepCubeA needed a learned value function specifically because Rubik's Cube has no comparably cheap approximate-solve shortcut; B(2,5) is different precisely because `braid_reduce` already IS a fast approximate solver. Whether "fast enough" survives at MCTS/beam-search scale (potentially thousands of node evaluations per search, and PatternBoost's own scale is 100k-500k candidates per generation, though that's samples-to-score, not necessarily MCTS-nodes-per-search) is an empirical cost question for Experimenter/Developer, not something literature can settle.

**Verdict: yes, strictly the safer first bet, and it should be prototyped before a learned value head, not alongside it** — it eliminates an entire class of failure modes (bias entrenchment, bootstrapping instability, admissibility) for free, at the cost of needing to confirm the reducer's call-count budget holds at search scale. If that budget check fails (reducer too slow to call at the needed node-evaluation rate), THEN the CayleyPy-informed value-head recipe (§3 above, corrected label) is the fallback, not the default.

### 4. Admissibility and bootstrapping pitfalls

[[futuhi-sturtevant-2026-admissible-heuristics]] (ICLR 2026) confirms directly: "Recent deep learning approaches often disregard admissibility and provide limited guarantees on generalization beyond the training data" — DeepCubeA's non-admissibility is a **named, still-open** field problem, not a quietly-solved detail. Their proposed fix (Cross-Entropy Admissibility loss) beats compressed pattern databases while staying near-admissible, but adds real training complexity. **Recommendation**: start non-admissible (matching DeepCubeA's own accepted tradeoff, and no worse than the current greedy-residual baseline, which also has no optimality guarantee); revisit admissibility-constrained training only if the value head's search-time behavior shows harmful overestimation.

### 5. Value head architecture on a transformer

Per subagent's design-level (not novel-research-level) findings: RLHF reward-model tooling routinely bolts a value head onto a transformer by **replacing the LM head with a linear scalar projection from the final hidden state**, sharing the backbone with the generation head — standard, not exotic engineering. Confirmed via this round's direct **axplorer source read** (§R2 below): axplorer's `Transformer` class currently has only `lm_head` (no value head anywhere), and `DataPoint.score` is a plain float used only for `select_best` data curation — **the model itself never trains on numeric scores today**; a value head would be a genuine new capability, not a config flip. Whether the value head needs full-word context or can work on a windowed/truncated representation was **not resolved by any source found** — flagged as open, needs a direct experiment, not literature guidance.

### R1 Addendum — bias entrenchment when the training signal is itself biased (Lead, mid-turn)

**This reframes R1 around Validator's finding: a value head trained on `braid_reduce` labels inherits the reducer's ~43% zero-fire blindness as a STRUCTURED bias against exactly the products-of-conjugates class where hidden reduction structure lives — de-prioritizing the region a value head should be helping explore, not avoiding.** Validator's conclusion: value-as-score is disproven (drifts on retrain); only a two-tier design (learned V guides search, the real reducer or a GAP oracle certifies) is sound. The literature on mitigating this:

**Formal grounding — why this isn't fixable by better training alone.** [[skalse-2022-defining-reward-hacking]] proves, generally and rigorously (not B(2,5)-specific, but directly applicable): for the full space of stochastic policies, two reward/value functions can only be mutually "unhackable" if one is constant — i.e. essentially no non-trivial learned proxy is safe from being hacked in general — and building an unhackable proxy from PARTIAL observations (exactly what a value head sees: a word, not the true expensive-to-compute distance-to-identity) is impossible without strong task-specific prior knowledge. **This formally supports Validator's structural conclusion**: the fix has to constrain what the surrounding search/generation process is allowed to trust the value net for (the two-tier design), not attempt to train the bias away.

**Concrete mitigation techniques, mapped to Lead's five candidates:**

1. **Ensemble disagreement to flag blind regions** — [[Osband et al. 2016, "Deep Exploration via Bootstrapped DQN," arXiv:1602.04621]]: train multiple value heads on different bootstrap resamples of the training data; where they DISAGREE is exactly where the training signal is least reliable — a direct, well-established technique for surfacing regions like B(2,5)'s products-of-conjugates blind spot **without needing to already know where the blind spot is**. A 2026 follow-up ("Value Bonuses using Ensemble Errors for Exploration in RL," arXiv:2602.12375) uses ensemble prediction error specifically to detect unreliable value regions and beats Bootstrapped DQN and reward-bonus baselines — the modern version of the same idea. **This is the single most directly actionable technique for the B25 two-tier design**: if multiple value heads (or one head with dropout/ensemble variants) disagree sharply on a candidate word, that disagreement itself is a signal to route the word to the real reducer/GAP oracle rather than trusting the value estimate, giving a concrete, automatable trigger for the "V guides, reducer certifies" split.

2. **Optimism under uncertainty / exploration bonuses** — [[Burda et al. 2018, "Exploration by Random Network Distillation," arXiv:1810.12894]]: adds an exploration bonus equal to the prediction error of a network trying to predict a fixed random network's output on the current state — states the model has seen less (or structurally different states) get a high bonus, driving exploration toward under-visited regions regardless of what the value estimate itself says. This is a general-purpose "don't trust low visitation as low value" correction, orthogonal to what generates the bias (doesn't need to know it's specifically about products-of-conjugates) — directly transferable as an additive bonus term to whatever selection criterion picks which candidates a search process pursues.

3. **Count-based exploration** — [[Bellemare et al. 2016, "Unifying Count-Based Exploration and Intrinsic Motivation," arXiv:1606.01868]]: generalizes tabular count-based exploration (visit a state less → explore it more) to non-tabular settings via density-model-derived pseudo-counts. For B(2,5), this would mean an explicit pseudo-count over word "types" (perhaps keyed by some cheap structural feature, e.g. presence of conjugate-product patterns) — words in under-visited feature-regions get an exploration bonus regardless of value estimate, a more targeted (but requires designing the right feature/density model) alternative to RND's fully generic approach.

4. **Built-in exploration inside the search algorithm itself — the sharpest finding of this addendum.** Re-examining the two flagship systems already reviewed in R1 through this new lens reveals a **structural difference directly relevant to the two-tier design choice**: Segler's retrosynthesis MCTS uses PUCT selection, `Q(s,a)/N(s,a) + c·P(s,a)·√N(parent)/(1+N(s,a))` — the second term is an explicit, built-in optimism-under-uncertainty / count-based exploration bonus (low visit count N → higher bonus, regardless of the current value estimate Q). **DeepCubeA's weighted A*, by contrast, has NO such term** — it is deterministic best-first search with no visit-count correction, meaning a systematically undervalued region (per Validator's blind-spot concern) would simply never get explored, with nothing in the search algorithm itself to correct for it. **This means the choice between MCTS-with-PUCT (Segler-style) and weighted-A*-without-exploration (DeepCubeA-style) is not just an implementation detail — it is directly the mechanism that determines whether the two-tier design's search layer self-corrects for value-head blind spots or silently entrenches them.** If a value head is built for B(2,5), an MCTS/PUCT-style search wrapper (or an explicit count-based/RND-style bonus bolted onto whatever search is used) is evidence-backed as necessary, not optional — a pure best-first search over the learned value, DeepCubeA-style, inherits exactly the entrenchment risk Validator flagged.

5. **Oracle labels on a subset / active learning** — no directly on-point paper was found this pass (search returned only generic active-learning results, not RL/search-guidance-specific). This remains the WEAKEST-evidenced of Lead's five candidates in the literature, though it is a natural pairing with technique #1 (ensemble disagreement flags candidates for the real reducer/GAP oracle to certify — this is really "active learning" already, just under a different name, applied at inference/search time rather than training time). Recommend treating "ensemble-disagreement-triggers-oracle-check" as the concrete instantiation of this idea for B(2,5), rather than a separate technique to research further.

**Bottom line for the two-tier design**: the literature converges on a concrete, implementable recipe — (a) train the value head as an ENSEMBLE (bootstrapped resampling, per Osband et al.), not a single network; (b) route candidates where the ensemble disagrees, OR where a count-based/RND-style novelty bonus is high, to the real reducer/GAP oracle for certification rather than trusting the value estimate; (c) if the search algorithm wrapping the value head is MCTS-style, its native PUCT exploration term already does much of this work for free (per finding #4) — if it's a pure best-first/weighted-A* search, an explicit exploration bonus term must be added deliberately, it will not happen automatically. This is now the load-bearing recommendation for Developer/Math-expert if a value-head prototype is scoped.

## R2 — Axplorer upstream source, read directly (not the abstract)

Cloned and read `github.com/AxiomMath/axplorer` directly this session: `src/envs/tokenizers.py`, `src/models/model.py`, `src/datasets.py`, `src/envs/environment.py`, `src/trainer.py`, `src/evaluator.py`, `train.py`, `program.md`.

**Reusable machinery, concretely:**
- **KV cache already exists** in `model.py`'s `CausalSelfAttention`/`Transformer.generate()` — `past_kv` threading is fully implemented (lines 22-45, 141-177), giving the O(T)-per-step generation speedup the verdict flagged as a "~40 lines, do it" item. If our `transformer.py` doesn't have this yet, **porting axplorer's existing implementation directly is cheaper than writing it from scratch.**
- **`--no_positional` is a real, wired-through config flag** (`config.no_positional`, `train.py:46`, `model.py:77-82`) — NoPE is a **zero-new-code flip** for axplorer-based code, directly actionable for the Phase A positional-encoding recommendation. **No relative/RoPE option exists natively** — only absolute (`wpe`) or none (NoPE); if a relative scheme is wanted instead of NoPE, that requires new code, NoPE does not.
- **The `select_best`/dedup loop is exactly as advertised** (`src/datasets.py`): `select_best(n, data)` sorts by `x.score` descending and truncates; `compute_unique_data` dedups by `d.features` (a canonical string each `DataPoint` must supply via `calc_features()`); `update_datasets` blends held-over best-of-previous-population with new best via a `new_proportion` mixing parameter, and triggers a temperature increase (`inc_temp`) specifically when the unique-fraction of a generation drops below 90% — i.e. **axplorer already has one built-in adaptive-curriculum mechanism** (diversity-triggered temperature ramp), just not a length-based one.
- **`local_search()` hook is exactly the shape our reducer already fits**: `DataPoint.local_search(self, improve_with_local_search)` is a no-op by default, called either always (`--always_search`) or only to repair invalid examples (`--redeem_only`) — B(2,5)'s `braid_reduce` reducer maps directly onto this hook with no adaptation needed.
- **No native variable-length-sequence environment** (confirms and extends the correction already made to [[Research/AI in Math/Tools/axplorer]] this session): all three built-in envs (`cycle.py`, `isosceles.py`, `sphere.py`) use fixed N/k coordinate tokenizers.

**What is NOT present — genuine gaps, not things we "correctly reimplemented" so much as things that don't exist upstream to reimplement:**
- **No curriculum-over-length mechanism.** `args.max_len` is parsed once and fixed for the entire run (`train.py:47`, `args.block_size = args.max_len + 2`); there is no per-epoch or per-step length schedule anywhere in `train.py`/`trainer.py`. A B(2,5) length curriculum (256→512→1024→full) would need to be built as new orchestration (e.g. restarting/reconfiguring across epochs with an increasing `max_len`), not toggled from an existing option.
- **No value head anywhere.** `Transformer` has only `lm_head`; `train()`'s loss is pure cross-entropy over `(X,Y)` token pairs (`trainer.py:42`); `DataPoint.score` is consumed only by `select_best` for data curation, never as a training signal the model itself sees. A value head (per R1) is unambiguously new architecture, not a hidden/underused existing feature.
- **No ensemble/uncertainty machinery** of any kind — directly relevant to the R1 addendum's ensemble-disagreement recommendation; that too would be new infrastructure.

**Net assessment**: axplorer gives real, immediately reusable machinery for the mechanical parts of the loop (KV cache, NoPE, select_best/dedup, local_search hook) — these should be ported/reused directly rather than reimplemented. It gives **nothing** for the two open R1/R3 design questions (value head, length curriculum) — those require new code regardless of how closely axplorer's existing patterns are followed.

## R3 — Length generalization + curriculum, concretely for B(2,5)

### Identity augmentation — implementation-level detail, and its limits

[[petschack-2025-symmetric-group]] (re-read at ar5iv full-text depth this round, §3 "Variable word length and identity augmentation"): confirms the mechanism exists and words are padded with "sufficiently many transpositions that amount to identities under group relations." **Critical gap**: the paper does NOT specify which relations generate the no-ops, does not describe placement (random vs. structured), does not describe epoch-to-epoch refresh, and explicitly defers to the model to "learn the group relations" from the augmented data rather than claiming the augmentation is representationally neutral. **Any B(2,5)-specific analog (inserting `aA`/`Bb` free-cancellation pairs, or an order-5 relator cycle like `aaaaa`) has no precedent-level implementation detail to copy — it would be a novel design, not applying a validated recipe.** Concretely, for B(2,5): `aA`/`Bb`/`bB`/`Aa` free-cancellation pairs are the direct analog of Petschack's "identities under group relations" (they cancel to the empty word under free reduction, always, regardless of context) — order-5 relator insertions (e.g. `aaaaa`) are a weaker analog since they're only trivial as a STANDALONE subword when the surrounding word lets that generator's power reduce mod 5 cleanly, which is not guaranteed at an arbitrary insertion point without checking local context.

### Curriculum over sequence length — real evidence, with a load-bearing caution

Genuine, rigorous evidence exists specifically for symbolic/algorithmic tasks (not just NLP curricula stretched to fit):
- [[zaremba-sutskever-2014-learning-to-execute]] (rigorous ablation, LSTM, arithmetic): **the naive progressive curriculum sometimes UNDERPERFORMED no curriculum at all** — only a "combined" strategy (progress a difficulty frontier, but keep sampling easier examples throughout rather than retiring them) won consistently, reaching 99% on 9-digit addition. **This is the single most important caution for any B(2,5) 256→512→1024→full curriculum design**: don't drop the 256-window training data once the model "graduates" to 512, keep sampling it throughout.
- [[agarwal-2021-polynomial-simplification-curriculum]] (transformer, symbolic polynomial simplification — closest domain analog): curriculum benefit is real but uneven, **+0.68% to +10.8%**, concentrated on the HARDEST configurations — suggesting the biggest curriculum payoff for B(2,5) would be at the long/full-length end, not the short windows, so curriculum design shouldn't be treated as "solved" once the easy windows train well.
- [[mehta-2026-randomized-yarn]] (modern transformer, long-context): curriculum is independently load-bearing even alongside a randomized positional encoding fix — dropping curriculum "degrade[s] substantially... by up to 18.3%" even with randomized-PE active. **Directly answers R3.4: curriculum and randomized/relative positional encoding compose well and are NOT redundant with each other** — both should be adopted together, not treated as alternative fixes for the same problem.

### Randomized positional encodings — mechanism confirmed at implementation depth

[[ruoss-2023-randomized-positional-encodings]] (re-read at ar5iv depth): sampling is **per-batch** (not per-example), the sampled index set is drawn from an extended range L≫N and **sorted ascending before use** — this is an ordered subsequence, NOT a shuffle, so relative token order is fully preserved; sorting itself is ablated as essential (+15.7% vs. unsorted, per subagent extraction). Composes with Delétang et al.'s uniform-length sampling as its length component. **No test of offset-invariant local pattern matching** exists in this paper — its benchmarks are about generalizing to longer inputs of the same task, not about recognizing the same local motif regardless of where it starts, which is our actual concern. This gap is real and unresolved by any source in either literature round — it would need a direct B(2,5) experiment, not a literature answer.

## R4 — Dual-stream / auxiliary-tag fusion mechanisms

Two genuinely different fusion mechanisms found, both with real precedent, answering "how would a rule-hit auxiliary channel actually attach to the transformer":

**Concatenation/summation of per-token auxiliary embeddings** ([[sennrich-haddow-2016-linguistic-features]] — existence/venue confirmed, exact mechanism NOT independently verified against primary text this session, flagged with a confidence caveat in that note; corroborated as the standard modern implementation pattern via OpenNMT's own documented "factored representations," `feat_merge: concat` or `feat_merge: sum`, independently confirmed this session). This is the architecturally SIMPLER option: a rule-hit auxiliary embedding table, summed or concatenated onto each character's token embedding before the first transformer block — directly bolt-on-able to axplorer's existing `Transformer.forward` (`x = self.wte(idx)` at `model.py:118` is exactly where a second embedding lookup would sum in).

**Graph/structure-guided attention masking** ([[guo-2020-graphcodebert]] — abstract and mechanism independently confirmed: "graph-guided masked attention function," achieves SOTA across four code tasks over a token-only baseline). This is architecturally MORE INVOLVED: the auxiliary signal reshapes which tokens can attend to which, requiring changes inside `CausalSelfAttention.forward`'s mask construction, not just the embedding layer.

**Which fits B(2,5) better**: our candidate rule-hit signal (per Math-expert's family 8, "SOUND as auxiliary") is a **flat, positional span-marking signal** ("this character position starts/is-inside a known rule match") — not a genuinely relational graph like GraphCodeBERT's data-flow edges (which connect distant, non-adjacent tokens). This argues for the **simpler concat/sum embedding-fusion approach** (Sennrich & Haddow / OpenNMT lineage) over porting GraphCodeBERT's attention-masking machinery, which is architecture built for a relational signal we don't have. **Caveat**: Sennrich & Haddow's exact mechanism and effect size were not independently verified against primary text this session (PDF tooling unavailable) — this recommendation rests on the OpenNMT documentation (independently confirmed) plus general NMT-literature familiarity, not a fully verified primary source. A closer read (or working PDF tooling in a future session) is recommended before treating the concat/sum choice as fully literature-backed rather than well-informed-but-partially-unverified.

A third, weaker thread: gazetteer-style deterministic dictionary features in NER were found to be **surpassed by contextual embeddings** in later work (Peters et al. 2017, ELMo-family) — a mild caution that a cheap deterministic auxiliary signal's value may shrink as the base model gets better at learning the pattern itself from raw tokens alone, worth keeping in mind as a reason the rule-hit channel is correctly scoped as "optional, Q4-gated" in the verdict rather than assumed necessary.

## Convergence across all four threads

1. **Non-monotonic/blind-spot problems in this domain want a two-LAYER solution, not a single cleverer scalar.** R1's addendum conclusion (value net proposes, real reducer/oracle certifies, with ensemble-disagreement or exploration-bonus triggers deciding when to check) structurally rhymes with the verdict's own R2 §7 "layer separation" (search may expand, scoring reducer stays termination-safe) and with R4's "aux channel exposes structure, doesn't replace the raw scorer." The pattern recurring across R1/R2(verdict)/R4 is: **let a cheap/fast/imperfect signal guide, but never let it be the final authority** — the real reducer, not the value net or the rule-hit channel, always has the last word.
2. **Curriculum and positional-encoding fixes are complementary, confirmed quantitatively** (R3, Mehta et al. 2026) — this closes an open question from Phase A cleanly.
3. **axplorer gives real infrastructure for the "boring" parts (KV cache, NoPE, dedup loop) and nothing for the two genuinely novel parts (value head, length curriculum)** — R2's clearest actionable finding.

## What's settled (this round)

- KV cache and NoPE are directly portable from axplorer's existing code — no design work needed, just porting.
- Curriculum-over-length has real evidence for symbolic/algorithmic tasks, WITH the caveat that naive progressive curricula can underperform no curriculum — the "combined" (retain-easy-examples) strategy is the evidence-backed default, not pure progression.
- Curriculum and randomized/relative positional encoding compose well (quantified), answering R3's open composition question from this round's own ask.
- A value head trained on `braid_reduce` labels alone (single network, no ensemble, no exploration correction, paired with a pure best-first search) is evidence-backed to entrench Validator's documented blind spot — both empirically (Validator's finding) and now theoretically (Skalse et al.'s unhackability negative results).

## What's contested / open

- Whether B(2,5)'s mostly-one-directional rewrite rules support an efficient DeepCubeA-style backward-from-goal training-data generation scheme, or whether Segler-style "use the existing reducer as a rollout policy inside MCTS, no learned value net at all" is the better-fitted design — genuinely open, not resolved by literature, needs Experimenter/Developer scoping.
- Whether MCTS-with-PUCT or weighted-A*-plus-explicit-exploration-bonus is the better search wrapper for a two-tier B(2,5) value head — R1's addendum identifies this as THE mechanism determining self-correction vs. entrenchment, but doesn't resolve which specific choice is better for B(2,5)'s structure.
- Whether the rule-hit auxiliary channel should use concat/sum embedding fusion or attention-mask fusion — leans concat/sum on structural-fit grounds (R4), but Sennrich & Haddow's exact evidence for the concat/sum side was not independently verified this session.
- Whether offset-invariant local pattern matching (our actual firing-site concern) benefits from randomized positional encoding the way longer-sequence generalization does — no source in either round tests this directly.

## Directly applicable to algo_mixing's current targets

1. **Port axplorer's `past_kv` KV-cache implementation and `--no_positional` flag directly** — no new design needed, immediate wins per R2.
2. **If a length curriculum is built, adopt Zaremba & Sutskever's "combined" strategy** (retain short-window sampling throughout, don't retire it once training moves to longer windows) rather than pure 256→512→1024→full progression.
3. **If a value head is prototyped, build it as an ensemble from the start** (bootstrapped resampling, cheap architecturally — several small heads or one head with distinct dropout masks) and wire ensemble disagreement (or an RND-style novelty bonus) as the trigger for routing a candidate to the real reducer/GAP oracle — this is the concrete, literature-backed recipe answering Lead's addendum.
4. **If a value head is prototyped, the search wrapper choice is not incidental** — MCTS/PUCT-style search has built-in exploration that a bare weighted-A*/best-first search does not; this choice directly determines whether blind-spot entrenchment self-corrects or compounds.
5. **If a rule-hit auxiliary channel is built (Q4-gated per the verdict), prefer concat/sum embedding fusion over attention-mask fusion** given the signal's flat/positional (not relational) structure — cheaper to bolt onto axplorer's existing `Transformer.forward`.

## Open empirical questions for Experimenter (pending Lead's GO)

1. Can a B(2,5)-analog of DeepCubeA's backward-from-goal data generation be constructed given mostly-one-directional rewrite rules (e.g., by deliberately applying rule RHS→LHS in reverse to "un-reduce" from the identity)? What's its coverage/cost relative to Rubik's-Cube-style backward scrambling?
2. Does using the existing `braid_reduce` reducer as a Segler-style MCTS rollout policy (no learned value network) achieve comparable non-greedy search benefit at lower implementation cost than a trained value head?
3. Does ensemble disagreement among bootstrapped value heads actually correlate with Validator's known 43%-zero-fire blind region on held-out B(2,5) words — i.e., does the proposed mitigation recipe (§R1 addendum) actually work on OUR specific documented bias, not just in the general RL literature?
4. Read [[chervov-2025-cayleypy-rl]]'s full methods section (currently only read at abstract depth) — does its diffusion-distance training procedure adapt to directed/mostly-one-directional rewrite graphs, or does it fundamentally require the invertible-generating-set structure permutation groups have?

## Related material in vault

- Phase A synthesis: [[_synthesis-b25-patternboost-tokenization]]
- Peer notes this gate: [[Agents/maumayma/MathExpert/b25-axplorer-representation-gate-phase-a-2026-07-17]], `Agents/maumayma/Validator/2026-07-17-axplorer-representation-constraints.md`, `Agents/maumayma/Validator/2026-07-17-axplorer-representation-phase-b-audit.md`, [[axplorer-representation-grounding-2026-07-17]]
- New papers this round: [[agostinelli-2019-deepcubea]], [[segler-2018-retrosynthesis-mcts]], [[chervov-2025-cayleypy-rl]], [[futuhi-sturtevant-2026-admissible-heuristics]], [[skalse-2022-defining-reward-hacking]], [[ruoss-2023-randomized-positional-encodings]], [[zaremba-sutskever-2014-learning-to-execute]], [[agarwal-2021-polynomial-simplification-curriculum]], [[mehta-2026-randomized-yarn]], [[guo-2020-graphcodebert]], [[sennrich-haddow-2016-linguistic-features]]
- Updated this round: [[petschack-2025-symmetric-group]] (implementation-level identity-augmentation detail added)
- Repo-local (not vault): axplorer upstream clone (session scratchpad, read directly for R2), `experiments/burnside/b25_patternboost/AXPLORER_REPRESENTATION_VERDICT.md` and `AXPLORER_REPRESENTATION_NOTES.md`

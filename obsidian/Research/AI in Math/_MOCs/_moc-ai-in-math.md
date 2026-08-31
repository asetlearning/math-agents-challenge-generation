---
title: "AI in Math — Map of Content"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/automated-theorem-proving
  - topic/mathematical-discovery
  - topic/moc
  - status/draft
status: draft
domain: ai
---

# AI in Math — Map of Content

**This MOC is a curated reading path for AI applied to mathematics** — covering formal theorem proving (LLM-based agents), RL training for mathematical reasoning, ML-guided mathematical discovery, and the 2026 wave of agent-driven research results. Four sub-areas plus a Tools shelf, ~46 notes (2014–2026). Navigate here when you want to understand the state of the art, what's settled, and what remains open.

Cross-cluster: papers in this MOC that are relevant to the Burnside/Mixer program are flagged with ⚡.

---

## Sub-area A — Agents for math

LLM-driven formal theorem provers, agentic proof search, autoformalization scaffolding.

**Synthesis**: [[Agents/_synthesis-agents-for-math]] — three paradigm arcs (LLM proof generation / autoformalization / neuro-symbolic); 6 settled results, 3 contested, 5 open questions; 4 Mixer recommendations.

### Foundational

- [[2009.03393]] — GPT-f (Polu & Sutskever 2020): LLM sampling for MetaMath/Lean proofs; expert iteration; first deep-learning proofs accepted into the Metamath library. The founding paper of the LLM-prover paradigm.

- [[2205.12615]] — Autoformalization with LLMs (Wu et al. 2022, NeurIPS): 25.3% of AMC/AIME problems correctly translated to Isabelle/HOL; starts the informal-to-formal data flywheel.

- [[2205.11491]] — HyperTree Proof Search (Lample et al. 2022, NeurIPS): MCTS + online learning on Lean proof trees; 82.6% on Metamath; establishes MCTS-for-proof-search paradigm.

- [[2210.12283]] — Draft, Sketch, and Prove (Jiang, Welleck et al. 2023, ICLR): informal → sketch → Isabelle verification; 21% → 39% on competition math. ⚡ *Applicable to formalizing Burnside group results in Isabelle.*

### Neuro-symbolic (AlphaGeometry line)

*AlphaGeometry 1 and 2 are one continuous line of work — read together.*

- [[trinh-2024-alphageometry]] — AlphaGeometry 1 (Trinh et al. 2024, Nature): LLM + symbolic deduction engine for IMO geometry; 25/30 problems solved; silver-medalist level. ⚡ *Auxiliary-construction analogy to Mixer rule injection.*

- [[2502.03544]] — AlphaGeometry 2 (Chervonyi et al. 2025): extends AG1; Gemini LM + knowledge-sharing search trees; 84% on 25 years of IMO geometry; gold-medalist level. ⚡ *Knowledge-sharing mechanism = Mixer rule injection architecture.*

- [[alphaproof-2024]] — AlphaProof + AG2 (DeepMind 2024): RL-trained Lean 4 prover + AG2; 4/6 IMO 2024 problems; silver medal. Source: blog + Nature 2025 paper (paywalled). ⚡ *Long-term architecture for formal group theory proofs.*

### Recent SOTA 2025

- [[2504.21801]] — DeepSeek-Prover-V2 (DeepSeek-AI 2025): recursive subgoal decomposition + RL; 88.9% on miniF2F-test; open weights; 2025 formal ATP SOTA. ⚡ *Subgoal decomposition = structured analog of Mixer KB injection.*

- [[2404.12534]] — Lean Copilot (Song et al. 2024): LLMs as real-time tactic suggesters in Lean 4 IDE; human-AI collaboration; 74.2% automation rate. ⚡ *Natural tool for formalizing B(4,3) or B(2,5) computational results in Lean 4.*

---

## Sub-area B — RL for math

Reinforcement-learning-guided tactic selection, value-network proof search, process reward models for mathematical reasoning.

**Synthesis**: [[RL/_synthesis-rl-for-math]] — 3 organizing buckets (RL for formal proof search / PRMs for informal math / RL for algorithm discovery); AlphaZero architectural context; 5 settled results, 2 contested, 3 open; 4 Mixer recommendations including AlphaTensor as injection-heuristic blueprint.

### Foundational

- [[RL/1805.07563]] — RL of Theorem Proving (Kaliszyk et al. 2018, NeurIPS): first large-scale RL for ATP on HOL Light; MCTS + value network; 40% more theorems proved. ⚡ *RL from proof success = Mixer's KB cascade feedback pattern.*

- [[RL/2305.20050]] — Let's Verify Step by Step (Lightman et al. 2023, OpenAI): process reward models (PRMs) outperform outcome reward models for multi-step math; 78% on MATH; PRM800K dataset. ⚡ *Step-level reward vs. outcome reward is applicable to Mixer injection evaluation.*

- [[RL/2312.08935]] — Math-Shepherd (Wang et al. 2024, ACL): auto-generates PRM training data without human annotation; 77.9% → 84.1% on GSM8K. ⚡ *Automatic PRM = template for Mixer injection-step reward labeling.*

- [[RL/2402.03300]] — DeepSeekMath (Shao et al. 2024): GRPO algorithm; 51.7% MATH at 7B; open weights; GRPO underpins DeepSeek-Prover-V2. ⚡ *GRPO = efficient RL training for future Mixer injection policy.*

### RL for algorithm discovery

- [[RL/fawzi-2022-alphatensor]] — AlphaTensor (Fawzi et al. 2022, Nature): AlphaZero-style RL discovers new matrix multiplication algorithms; beats Strassen 4×4 in Z₂. ⚡ **Highest Mixer relevance**: single-player game framing = template for RL-guided Mixer rule injection. The evaluator is "does this injection reduce convergence time?"

### Value networks, search, and reward design (2026-07-17 wave)

Support wave for the B25 PatternBoost program — value/cost-to-go scoring, search on group-structured spaces, reward-hacking risk. Curated in depth by [[ML/_synthesis-b25-value-scoring-curriculum-auxchannel]].

- [[RL/agostinelli-2019-deepcubea]] — DeepCubeA (2019): value network + weighted A* solves the Rubik's cube without human knowledge; the cost-to-go bootstrapping template. ⚡
- [[RL/chervov-2025-cayleypy-rl]] — CayleyPy (2025): RL pathfinding on Cayley graphs — group-theory-adjacent search at scale. ⚡
- [[RL/futuhi-sturtevant-2026-admissible-heuristics]] — learned admissible heuristics for A* (2026): when learned value functions keep optimality guarantees.
- [[RL/segler-2018-retrosynthesis-mcts]] — Segler et al. (2018, Nature): MCTS + neural policies for chemical synthesis planning — the plan-search paradigm outside games.
- [[RL/shypula-2021-superoptimize-real-world-programs]] — SILO self-imitation for program superoptimization (2021): search that allows locally-worse intermediate edits. ⚡
- [[RL/skalse-2022-defining-reward-hacking]] — Skalse et al. (2022): formal definition of reward hacking; calibrates the PatternBoost score-proxy risk. ⚡
- [[RL/2005.01917]] — Learning selection strategies in Buchberger's algorithm (2020): RL inside a computer-algebra solver. ⚡

---

## Sub-area C — ML for math (non-agent, non-RL)

Equation/conjecture discovery, neural heuristics inside solvers, embeddings-for-math, evolutionary LLM program search.

**Synthesis**: [[ML/_synthesis-ml-for-math]] — 4-paradigm structure; 5 settled, 2 contested, 4 open; 4 Mixer recommendations including AlphaEvolve as injection-heuristic-discovery blueprint.

### Neural heuristics inside existing solvers

- [[ML/1701.06972]] — Deep Network Guided Proof Search (Loos et al. 2017, LPAR-21): first deep-network premise selection inside E theorem prover; 56% → 59% Mizar coverage; foundational "ML as solver heuristic."

- [[ML/2306.15626]] — LeanDojo / ReProver (Yang et al. 2023, NeurIPS): embedding-based premise retrieval for Lean 4; open-source infrastructure; outperforms GPT-4 on hard generalization benchmark. ⚡ *Retrieval of relevant Lean 4 premises = analog of rule retrieval in Mixer KB. Tool for formalizing Burnside results.*

- [[ML/1811.06128]] — Bengio, Lodi, Prouvost (2021, EJOR): survey of ML for combinatorial optimization — honest assessment of what ML has actually shown vs. hype. Key finding: algorithm selection is the most reliable ML-for-CO application. ⚡ *Recommends ML injection policy (algorithm selection) as the most principled next step for the Mixer.*

### Equation and conjecture discovery

- [[ML/2006.11287]] — Discovering Symbolic Models (Cranmer et al. 2020, NeurIPS): GNN + symbolic regression extracts equations from neural networks; discovers new dark matter formula. ⚡ *PySR applicable to $|P_s(2,5)|$ growth function data.*

- [[ML/raayoni-2021-ramanujan]] — Ramanujan Machine (Raayoni et al. 2021, Nature): automated conjecture generation about fundamental constants via MITM-RF; discovers previously-unknown continued fraction formulas.

### Evolutionary LLM program search (FunSearch line)

*FunSearch and AlphaEvolve are one continuous line of work — read together.*

- [[ML/romera-paredes-2023-funsearch]] — FunSearch (Romera-Paredes et al. 2023, Nature): evolutionary LLM-guided program search; discovers new cap set bounds and bin packing heuristics; evaluator filters confabulations. ⚡ *Evaluator-filtered evolutionary search = template for Mixer injection heuristic discovery.*

- [[ML/2506.13131]] — AlphaEvolve (Novikov et al. 2025): FunSearch with Gemini; 67+ mathematical problems; discovers 4×4 complex matrix multiplication with 48 multiplications (first Strassen improvement in this setting). ⚡ *Same template as FunSearch; broader validation.*

- [[ML/charton-2024-patternboost]] — PatternBoost (Charton, Ellenberg, Wagner, Williamson 2024): alternating local search + transformer generation for mathematical constructions; direct continuation of the FunSearch line, and the method the whole b25_patternboost program is built on. ⚡

### B25 PatternBoost program (2026-06/07 support waves)

**Syntheses**: [[ML/_synthesis-b25-patternboost-tokenization]] — input/output representation gate (Phase A) for the B(2,5) PatternBoost transformer ⚡; [[ML/_synthesis-b25-value-scoring-curriculum-auxchannel]] — Deep Round 2: value/cost-to-go scoring, length curriculum, auxiliary-tag fusion ⚡. Both curate the 2026-07-17 wave below.

Tokenization / positional encoding / length generalization / curriculum / edit representation:

- [[ML/charton-2022-linear-algebra-transformers]] — number encodings for transformer mathematics.
- [[ML/nogueira-2021-arithmetic-limitations]] — tokenization limits of transformers on simple arithmetic.
- [[ML/singh-strouse-2024-tokenization-counts]] — tokenization's impact on arithmetic in frontier LLMs.
- [[ML/sennrich-haddow-2016-linguistic-features]] — auxiliary input features for seq2seq models (aux-channel precedent).
- [[ML/kazemnejad-2023-nope]] — impact of positional encoding on length generalization (NoPE result).
- [[ML/ruoss-2023-randomized-positional-encodings]] — randomized positional encodings boost length generalization.
- [[ML/mehta-2026-randomized-yarn]] — randomized YaRN for long-context length generalization.
- [[ML/zaremba-sutskever-2014-learning-to-execute]] — Learning to Execute (2014): curriculum learning for sequence models.
- [[ML/agarwal-2021-polynomial-simplification-curriculum]] — curriculum nuances of transformers' polynomial simplification.
- [[ML/petschack-2025-symmetric-group]] — learning the symmetric group large-from-small (group-theory-adjacent).
- [[ML/gukov-2020-learning-to-unknot]] — Learning to Unknot (2020): RL/tokenization on braid words (group-theory-adjacent). ⚡
- [[ML/guo-2020-graphcodebert]] — GraphCodeBERT: structure-aware code representations (edit-representation precedent).
- [[ML/cao-2026-adaedit]] — AdaEdit (2026): adaptive edit-format selection for LLM editing.

### Gröbner-basis learning (2026-08-09 wave)

- [[ML/kera-2024-grobner-via-learning]] — Gröbner basis computation via learning (2024): transformers + backward-generation training. ⚡
- [[ML/2311.12904]] — Learning to Compute Gröbner Bases (2023).
- [[ML/2401.09328]] — deep-learned online stability improvement for Gröbner basis solvers (2024).

---

## Sub-area D — Agent-driven discoveries (the 2026 wave)

Concrete research-grade results *produced with AI agents* in 2026 — new proofs of long-open conjectures and novel counterexamples. Distinct from Sub-area A (which is competition/benchmark theorem proving). **Verification status matters: most are not yet peer-reviewed — see each note.**

**Synthesis**: [[_synthesis-ai-agent-discoveries-2026]] — three anchor examples + broader landscape; convergence on propose-then-certify + multi-agent orchestration; honest verification caveats; 5 recommendations for our own agent program.

- [[cycle-double-cover-sol-ultra-2026]] — **GPT-5.6 Sol Ultra** proves the 50-year Cycle Double Cover Conjecture with a **64-subagent** swarm in <1h (2026-07). ❌ Unverified NL proof. **Full orchestration prompt reproduced verbatim.** ⚡ *Prompt patterns map onto our Lead/Validator multi-agent design.*

- [[jacobian-counterexample-fable-2026]] — **Claude Fable 5** finds an explicit counterexample to the 87-year Jacobian Conjecture (det Jac = −2, three colliding points) (2026-07). ⚠️ Arithmetic independently verified; journal review pending. ⚡ *Same model family our Lead runs on; construction-search paradigm = our B25 word-reduction search.*

- [[aletheia-autonomous-math-2026]] — **DeepMind Aletheia** (Gemini Deep Think): Generate–Verify–Revise loop resolves 4 open Erdős problems + a fully-autonomous eigenweights paper (2026-03). ✅ Semi-autonomous, **public transcripts**. ⚡ *3-subagent loop = our two-tier guide/certify architecture; co-authored by Sergei Gukov (group-theory ML line).*

---

## Tools

Reference notes (not paper summaries) under `Tools/` — see [[_index|Tools index]].

- [[Tools/axplorer]] — axplorer: the PatternBoost reference implementation used by the b25_patternboost program. ⚡
- [[Tools/patternboost-v1-lineage]] — PatternBoost v1: the original Julia/Python proof-of-concept lineage (zawagner22). ⚡

## Cross-cluster connections to Group Theory / Burnside

Papers with ⚡ above have documented connections to the Burnside / Mixer program. The highest-priority actionable connections are:

1. **[[RL/fawzi-2022-alphatensor]]** (AlphaTensor): single-player RL game framing → Mixer rule injection as RL-optimized algorithm search.
2. **[[ML/romera-paredes-2023-funsearch]]** + **[[ML/2506.13131]]** (FunSearch/AlphaEvolve): evolutionary evaluator-filtered search → Mixer injection heuristic discovery.
3. **[[2404.12534]]** (Lean Copilot) + **[[ML/2306.15626]]** (LeanDojo): Lean 4 infrastructure for formalizing B(4,3)/B(2,5) computational results.
4. **[[2502.03544]]** (AlphaGeometry 2): knowledge-sharing between search trees → multi-agent Mixer architecture.
5. **[[ML/2006.11287]]** (Cranmer/PySR): symbolic regression → closed-form formula for $|P_s(2,5)|$ growth function.

---

## Related MOCs

- [[Research/Group theory/_MOCs/_moc-burnside]] — the Burnside group research cluster; Mixer targets; Kuznetsov computational line.
- [[Research/Group theory/_MOCs/_moc-knuth-bendix]] — the KB completion algorithm cluster; Mixer's core algorithm.

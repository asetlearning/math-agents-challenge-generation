---
title: "Synthesis — AI-agent mathematical discoveries (the 2026 wave)"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/mathematical-discovery
  - topic/agentic-reasoning
  - topic/multi-agent-orchestration
  - topic/autonomous-research
  - synthesis
  - ai-discovery
  - status/draft
papers_synthesized:
  - "[[cycle-double-cover-sol-ultra-2026]]"
  - "[[jacobian-counterexample-fable-2026]]"
  - "[[aletheia-autonomous-math-2026]]"
key_concepts: []
date_range: 2026-03 to 2026-07
project:
status: draft
domain: ai
---

# Synthesis — AI-agent mathematical discoveries (the 2026 wave)

> **Synthesis note.** In 2026, AI agents crossed from *proving known/competition results* (the [[_synthesis-agents-for-math]] lineage, 2020–2025) into *producing research-grade mathematical content* — new proofs of long-open conjectures and novel explicit counterexamples. This note collects the concrete, verifiable examples, their **agent setups and prompts**, their **verification status** (critically: most are NOT yet peer-reviewed), and what transfers to our own B25/axplorer multi-agent program. Compiled from the three sources Maria flagged, expanded with the broader landscape.

## The question

Which specific mathematical discoveries were made *with AI agents* in 2025–2026, how were the agents actually set up (models, orchestration, prompts), and how trustworthy is each result?

## The three anchor examples

| Result | Model / system | Setup | Verification status | Autonomy |
|---|---|---|---|---|
| [[cycle-double-cover-sol-ultra-2026]] — Cycle Double Cover Conjecture (50yr, graph theory) | **GPT-5.6 Sol Ultra** (OpenAI) | **64-subagent** "multiagent v2" swarm, diversity-first + adversarial checkers, root synthesizer; **full prompt public** | ❌ **Unverified** — 3-page NL proof, not formalized, community review ongoing | Essentially autonomous (claimed) |
| [[jacobian-counterexample-fable-2026]] — Jacobian Conjecture (87yr, algebraic geometry) | **Claude Fable 5** (Anthropic) | Human posed question; Fable produced explicit map; human + Wolfram + preprint verify; **no prompt public** | ⚠️ **Arithmetic independently verified**; journal review pending | Human-AI collaboration |
| [[aletheia-autonomous-math-2026]] — 4 open Erdős problems + eigenweights paper | **Aletheia** on Gemini Deep Think (DeepMind) | **Generate–Verify–Revise** 3-subagent loop, NL end-to-end; **full transcripts public** | ✅ Semi-autonomous (AI + human graders); one result fully autonomous, publication-grade | Level 0–2 (their taxonomy) |

## Convergence — what all three share

1. **Propose-then-certify (two-tier).** Every system separates a *generative* layer (propose a proof/object) from a *verification* layer that is the sole authority on truth:
   - Sol Ultra: adversarial subagents check every candidate against an enumerated failure list.
   - Fable/Jacobian: Wolfram + human + independent preprint re-derive the arithmetic.
   - Aletheia: a dedicated **Verifier** subagent gates acceptance; loops to a **Reviser**.
   This is **exactly the "guide vs. certify" separation we locked for axplorer v1** (GPT proposes, reducer/GAP certifies). The 2026 wave validates that architecture at the frontier.

2. **Multi-agent orchestration is the mechanism, not a garnish.** Sol Ultra's whole prompt is an orchestration spec (diversity-first, approach registry, dynamic reallocation, blocked-route tagging). Aletheia is three cooperating subagents. Cooperation/portfolio search — the Mixer thesis — is the shared engine.

3. **Natural language, not formal.** Unlike AlphaProof/AlphaGeometry (Lean/geometry DSLs), all three 2026 results are in **natural language** — which is *why* verification is the bottleneck and why none of the unrefereed ones can be trusted yet.

4. **Test-time compute scaling.** 64 concurrent agents (Sol Ultra) and an inference-time scaling law (Aletheia) — the lever is *search breadth at inference*, echoing our reducer-as-rollout bounded-exploration design.

## Disagreement / tension

- **Autonomy claims vary wildly.** Aletheia's authors are scrupulously honest (SAE-style levels; "milestones for AI, not major advances for math"; several Erdős problems were elementary). The Sol Ultra and Fable announcements are **marketing-adjacent** (launch-day X posts, jokey tone) and overstate autonomy relative to the actual human-in-the-loop verification.
- **Proof vs. construction.** CDC is a long *deductive proof*; the Jacobian result is an explicit *witness object*; Erdős solutions are mixed. Constructions (find a short certificate) are closer to our B25 word-reduction search than proofs are.

## What's settled (mid-2026)

1. AI agents **can** produce research-grade mathematical content — at minimum genuine novel counterexamples (Jacobian) and at least one fully-autonomous publication-grade paper (eigenweights).
2. **The verification layer is the load-bearing part** and is currently human/CAS/independent-preprint, not machine-checked, for the headline NL results.
3. **Multi-agent + adversarial-checking prompting** measurably helps (Sol Ultra's whole method; Aletheia's loop).

## What's contested / open

1. **The CDC proof's correctness** — unresolved; could be wrong. Do not cite as settled.
2. **Division of labor** in the Fable Jacobian result — how much was autonomous.
3. Whether NL research proofs will get **formalized (Lean/Coq)** to become trustworthy at scale.

## The broader landscape (beyond the three anchors)

Genuine agent/ML-driven mathematical results already tracked or worth tracking:

- **FunSearch → AlphaEvolve** ([[ML/romera-paredes-2023-funsearch]], [[ML/2506.13131]]) — evolutionary LLM program search; new cap-set bounds, 4×4 complex matrix mult in 48 multiplications. The most *battle-tested* discovery line.
- **AlphaTensor** ([[RL/fawzi-2022-alphatensor]]) — RL discovers new matrix-multiplication algorithms.
- **AlphaProof / AlphaGeometry 2** ([[alphaproof-2024]], [[2502.03544]]) — IMO 2024 silver / geometry gold; the formal-language predecessors.
- **DeepSeek-Prover-V2** ([[2504.21801]]) — 88.9% miniF2F; open-weight SOTA formal prover.
- **GPT-5 / Erdős problems** — GPT-5-class models reportedly closed several previously-"open" ErdosProblems.com entries in late 2025 (mostly by locating existing literature; overlaps Aletheia's Level-0 findings).
- **Ramanujan Machine** ([[ML/raayoni-2021-ramanujan]]) — automated conjecture generation for constants.

## Not an AI discovery (correction)

The arxiv PDF Maria linked (**arXiv:2606.03300**) is **Parisi–Zamponi, "A proof of an identity for the critical exponents of jamming"** — a conventional statistical-mechanics paper with **no AI-agent involvement**. Flagged so it is not mis-filed as an AI discovery. (If a different arxiv id was intended, re-share it.)

## Recommendation (for our program)

1. **Adopt Sol Ultra's orchestration prompt patterns** in our Maestri agent instructions: diversity-first, approach registry, blocked-route tagging, mandatory adversarial checker, "reject vague optimism — demand concrete lemmas/counterexamples." These map 1:1 onto our Lead/Validator setup and the axplorer red-team discipline. See the verbatim prompt in [[cycle-double-cover-sol-ultra-2026]].
2. **Mine Aletheia's public transcripts** ([GitHub](https://github.com/google-deepmind/superhuman/tree/main/aletheia)) for real research-agent prompting — the only fully-open transcripts of the three.
3. **Fable 5 is our Lead's model** and has now demonstrably produced novel research objects ([[jacobian-counterexample-fable-2026]]) — supports the choice; watch for the released transcript.
4. **Use the "Autonomous Mathematics Research Levels" + interaction-cards** vocabulary to classify our own B25 results honestly (axplorer v1 ≈ Level 1 collaboration).
5. **Treat every unrefereed claim as provisional** — track verification outcomes before citing.

## Related vault material

- [[_synthesis-agents-for-math]] — the 2020–2025 theorem-proving lineage this extends
- [[_moc-ai-in-math]] — parent MOC
- [[chervov-2025-cayleypy-rl]] — Gukov-adjacent group-theory ML (our closest B25 analog; Gukov also co-authored Aletheia)
- Local: `Agents/maumayma/Lead/AXPLORER_REPRESENTATION_VERDICT.md` — our own multi-agent gate, same propose-vs-certify architecture

---
title: "Aletheia — Towards Autonomous Mathematics Research (Erdős problems, DeepMind)"
authors:
  - "Tony Feng"
  - "Trieu H. Trinh"
  - "Garrett Bingham"
  - "Sergei Gukov"
  - "Quoc V. Le"
  - "Thang Luong"
  - "et al. (Google DeepMind, ~30 authors incl. mathematicians)"
year: 2026
venue: "Preprint (Google DeepMind), 2026-03-16"
url: "https://math.berkeley.edu/~fengt/Aletheia.pdf"
url_transcripts: "https://github.com/google-deepmind/superhuman/tree/main/aletheia"
language: en
methodology_type: empirical
domain: ai
event_date: 2026-03-16
verification_status: semi-autonomous (AI grading + human experts); publication-grade subset
key_concepts: []
related:
  - "[[_synthesis-ai-agent-discoveries-2026]]"
  - "[[cycle-double-cover-sol-ultra-2026]]"
  - "[[jacobian-counterexample-fable-2026]]"
  - "[[_synthesis-agents-for-math]]"
  - "[[chervov-2025-cayleypy-rl]]"
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/agentic-reasoning
  - topic/autonomous-research
  - topic/erdos-problems
  - topic/generate-verify-revise
  - ai-discovery
  - status/draft
status: draft
---

# Aletheia — Towards Autonomous Mathematics Research

> **AI-discovery note.** **Aletheia** is Google DeepMind's math *research* agent (built on **Gemini Deep Think**), presented in "Towards Autonomous Mathematics Research" (Feng, Trinh, Gukov, Le, Luong et al., 2026-03-16). It moves past competition problem-solving to **research-level results**: a fully-autonomous publication-grade paper (eigenweights), an extensive semi-autonomous sweep of **700 open Erdős problems** (Bloom's database) that **resolved four open questions**, and a leading score on the FirstProof research benchmark. Crucially for us, it is the **best-documented** example of the genre — **full prompts and model outputs are public** on GitHub. It also shares an author (**Sergei Gukov**) with the knot-theory / group-theory ML lineage we already track.

## What it achieved

DeepMind's own **Autonomous Mathematics Research Levels** taxonomy (analogous to SAE vehicle-autonomy levels) classifies the results:

| Result | Autonomy / Novelty |
|---|---|
| **Eigenweights** (structure constants in arithmetic geometry) | Essentially autonomous, publication-grade — **no human intervention** |
| **Generalized Erdős-1051** → a research paper | Human-AI collaboration, Level 1+ |
| **Erdős-1051** solved completely | Minor novelty (Level 1) |
| **Erdős-652, 654, 1040** | Negligible novelty (Level 0) — turned out elementary despite decades open |
| Independence polynomials (interacting particles) | Human-AI collaboration, publishable |
| Arithmetic volumes; complexity bounds | AI contributed intermediate propositions to human papers |
| **FirstProof** (10 research-level problems by academic mathematicians) | Leading performance |

Honest framing from the authors: the autonomous Erdős solutions are **milestones for AI, not major advances for mathematics** — several "open" problems turned out to be elementary (one, Erdős-397, was nearly identical to a 2012 Chinese IMO TST problem).

## Agent setup (architecture)

Built on **IMO-Gold Gemini Deep Think**. Aletheia is a **generate–verify–revise** loop of three subagents that interact until the Verifier approves or a preset attempt limit is hit:

| Subagent | Role |
|---|---|
| **Generator** | Produces candidate solution (natural language) |
| **Verifier** | Checks the candidate rigorously; gates acceptance |
| **Reviser** | Revises based on Verifier feedback; loops back |

- Each of the three subagents **internally orchestrates multiple calls** to a Gemini base model.
- Operates **end-to-end in natural language** (contrast with AlphaProof / AlphaGeometry, which use formal Lean/geometry languages).
- Uses a **novel inference-time scaling law** on Deep Think (more test-time compute → better research output).
- Verification for the Erdős sweep was **semi-autonomous**: AI grading **plus** human experts.

**Prompts:** unlike the CDC and Jacobian cases, Aletheia's **full prompt + output transcripts are openly published** at the GitHub link above — the single most useful artifact of the three for studying real research-agent prompting. The authors also propose **"human-AI interaction cards"** for transparent documentation of who-did-what — a documentation standard worth adopting in our own vault.

## Why this matters for us

1. **Generate–Verify–Revise = our exact pattern.** The three-subagent loop is structurally identical to our Lead/Validator/Reviser discipline and to the axplorer **two-tier "guide vs. certify"** design. Aletheia is prior art we can cite for our architecture.
2. **Gukov link.** Sergei Gukov (co-author) is behind [[chervov-2025-cayleypy-rl]]-adjacent knot/group ML — the closest analog to our B25 value-scoring work. Aletheia is the "research agent" wrapper around that lineage.
3. **Public transcripts.** For prompt engineering, this is the one to mine — real research prompts + outputs, not marketing excerpts.
4. **Autonomy taxonomy.** The SAE-style "Autonomous Mathematics Research Levels" + "interaction cards" give us a **vocabulary to classify our own B25 results honestly** (e.g. our axplorer v1 = human-designed search + AI proposer = Level 1 collaboration, not autonomous discovery).

## Caveats

- Most autonomously-solved Erdős problems were **elementary** — the headline "solved 4 open problems" overstates mathematical significance; the authors say so explicitly.
- "Semi-autonomous" — humans were in the loop for grading/verification on the sweep.
- The one **fully-autonomous** publication-grade result (eigenweights) is the strongest single data point.

## Related vault material

- [[_synthesis-ai-agent-discoveries-2026]] — parent synthesis
- [[cycle-double-cover-sol-ultra-2026]], [[jacobian-counterexample-fable-2026]] — the other two 2026 examples
- [[_synthesis-agents-for-math]] — the 2020–2025 theorem-proving lineage
- [[chervov-2025-cayleypy-rl]] — Gukov-adjacent group-theory ML (our closest B25 analog)

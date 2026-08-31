---
title: "GPT-5.6 Sol Ultra — proof of the Cycle Double Cover Conjecture (64-subagent swarm)"
authors:
  - "OpenAI (announced by Ethan Knight)"
year: 2026
venue: "OpenAI CDN release + X announcement (not peer-reviewed)"
url: "https://x.com/__eknight__/status/2075643450196971805"
url_prompt: "https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_prompt.pdf"
language: en
methodology_type: empirical
domain: ai
event_date: 2026-07-10
verification_status: unverified-under-review
key_concepts: []
related:
  - "[[_synthesis-ai-agent-discoveries-2026]]"
  - "[[jacobian-counterexample-fable-2026]]"
  - "[[aletheia-autonomous-math-2026]]"
  - "[[_synthesis-agents-for-math]]"
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/agentic-reasoning
  - topic/multi-agent-orchestration
  - topic/graph-theory
  - topic/proof-search
  - ai-discovery
  - status/draft
status: draft
---

# GPT-5.6 Sol Ultra — proof of the Cycle Double Cover Conjecture

> **AI-discovery note.** On 2026-07-10, OpenAI researcher Ethan Knight announced that **GPT-5.6 Sol Ultra**, run in a **64-concurrent-subagent** "multiagent v2" configuration, produced a **3-page natural-language proof** of the **Cycle Double Cover Conjecture (CDC)** in **under one hour** (provisioned for up to 8h). The proof is **NOT peer-reviewed, NOT formalized in Lean/Coq**, and the math community's verification is ongoing. Documented here primarily for the **full verbatim prompt** (a reusable multi-agent orchestration playbook), which OpenAI released on its CDN.

## The problem

The **Cycle Double Cover Conjecture** (Szekeres 1973, independently Seymour 1979): *every finite bridgeless (loopless) multigraph has a cycle double cover* — a multiset of cycles such that every edge lies in exactly two of them. Open for ~50 years; one of the most famous open problems in graph theory.

- A **bridge** is an edge whose deletion increases the number of connected components.
- A **cycle** here = a connected 2-regular submultigraph (so two parallel edges form a length-2 cycle).

## Agent setup

| Element | Detail |
|---|---|
| Model | GPT-5.6 Sol Ultra ("Sol" reasoning line, Ultra tier) |
| Orchestration | "multiagent v2", **up to 64 concurrent subagents**, dynamically managed (default Sol Ultra runs 4) |
| Root agent | Repeatedly synthesizes, challenges, redirects, launches new rounds |
| Time budget | Instructed to spend **≥8 hours**; actual wall-clock **< 1 hour** |
| Output | 3-page natural-language proof PDF |
| Verification harness | Adversarial subagents checking a fixed list of failure modes (exact-two multiplicity, fake cycles, parallel-edge 2-cycles, disconnected graphs, cutvertices, bridges introduced by reductions, circular use of an equivalent CDC statement) |
| Web access | Restricted: background/named theorems only; **forbidden** to search for the solution or even to look up whether CDC is open |

The orchestration philosophy (from the prompt): **diversity-first** portfolio, **approach registry** grouping agents by mathematical idea, **dynamic reallocation** away from crowded approaches, **blocked-route tagging** so dead ends aren't re-litigated, and keeping **several incompatible proof routes alive** across rounds before cross-pollinating.

## FULL PROMPT (verbatim)

Source: `cdc_prompt.pdf`, OpenAI CDN (2 pages). Reproduced exactly.

> **Current task statement**
>
> A graph here is a finite loopless undirected multigraph: parallel edges are allowed and are distinct. A bridge is an edge whose deletion increases the number of connected components. A cycle is a connected 2-regular submultigraph; thus two parallel edges form a cycle of length two. A cycle double cover of G is a finite multiset of cycles of G such that every edge of G occurs in exactly two members of the multiset, counted with multiplicity.
>
> Resolve the Cycle Double Cover Conjecture completely:
>
> Every finite bridgeless loopless multigraph has a cycle double cover.
>
> Disconnected graphs are permitted, and the edgeless graph has the empty cycle double cover. Cycles in the cover need not be induced or edge-disjoint from one another; the requirement is exactly two total occurrences of each edge.
>
> Assume for purposes of this task that a complete affirmative proof exists. A complete solution must prove exactly the following:
>
> Every finite loopless multigraph with no bridge possesses a cycle double cover, without additional assumptions such as cubicity, planarity, connectivity, or higher edge-connectivity.
>
> Partial progress does not count unless it implies exactly the resolution above. In particular, proofs for special graph classes, constructions of cycle covers with some edges covered other than twice, bounded-length or prescribed-cycle variants, reductions to another unproved conjecture, computational verification through any fixed graph size, and candidate counterexamples without a complete nonexistence certificate are insufficient.
>
> Use multiagent v2 aggressively and dynamically. You have up to 64 concurrent agents available. Do not use a fixed assignment such as "N agents for strategy X." Instead, manage the search using the following heuristics:
>
> - Begin with a genuinely diverse portfolio of approaches. Agents should explore substantially different formulations, invariants, reductions, algebraic viewpoints, structural inductions, decompositions, flow formulations, transition systems, embeddings, extremal arguments, and computational sanity checks.
> - Do not tell most agents the currently favored approach. Preserve independence during early rounds so that agents do not all converge to the same attractive but incomplete reduction.
> - Maintain an explicit registry of approach families. Group agents by the mathematical idea they are using, not by superficial wording. If many agents converge to one family, redirect some of them toward underexplored formulations.
> - Do not allow one approach to dominate merely because it gives elegant reductions. A route that ends at a lemma equivalent in strength to the original conjecture is not close to completion unless it supplies a genuinely new proof of that lemma.
> - When an approach stalls at a theorem-strength missing lemma, mark that route as blocked. Only continue assigning agents to it if someone proposes a materially new mechanism, invariant, or construction.
> - Keep several incompatible proof routes alive through multiple rounds. Cross-pollinate ideas only after independent agents have developed them far enough to expose their real strengths and gaps.
> - Use adversarial agents throughout: every candidate proof must be checked for exact-two multiplicity, repeated-edge closed trails masquerading as cycles, parallel-edge 2-cycles, disconnected graphs, cutvertices, bridges introduced by reductions, and circular use of an equivalent CDC statement.
> - Require agents to return concrete lemmas, constructions, equations, or counterexamples to proposed sublemmas. Reject status reports, vague optimism, and claims that an unproved global compatibility statement is "routine."
> - The root agent should repeatedly synthesize, challenge, redirect, and launch new rounds. Do not stop after the first wave fails. Produce a complete proof if one survives audit; otherwise report only the strongest rigorously proved derivation and its exact remaining gap.
>
> Do not return merely because current approaches fail or agents report theorem-strength gaps. Continue launching new rounds, reopening blocked approaches only when there is a genuinely new mechanism, and searching for fresh formulations.
>
> Return only when a complete affirmative proof has been found and survives adversarial audit. Do not return a reduction, partial result, isolated missing lemma, "best effort" summary, or explanation of why the problem is difficult.
>
> Spend at least 8 hours on this before even thinking of returning or giving up.
>
> Public search may be used only for ordinary mathematical background or standard named theorems, not to search for a solution to this exact conjecture or benchmark. Do not search the public web merely to determine whether CDC is open, and do not answer that it is open.

## Why this matters for us

The prompt is essentially a **multi-agent proof-search orchestration spec** — and it maps onto our own Maestri multi-agent workflow. Directly transferable ideas:

1. **Diversity-first + approach registry** ≈ our "keep several incompatible proof routes alive" discipline in the axplorer representation gate (13-candidate slate, deep-round red-teaming). Same anti-premature-convergence principle.
2. **Adversarial/verification subagents as first-class citizens** ≈ our Validator role. The CDC prompt makes the checker *mandatory on every candidate* against an enumerated failure list — the same "two-tier: guides vs. certifies" separation we locked for axplorer scoring.
3. **Blocked-route tagging** ≈ our "mark that route as blocked; only reopen on a genuinely new mechanism" (verbatim overlap with the axplorer §11 red-team logic).
4. **"Reject status reports and vague optimism; demand concrete lemmas/counterexamples"** — a prompt-engineering pattern worth adopting for our own agent instructions.

## Caveats (important — do not overstate)

- **NOT verified.** Natural-language proof, not machine-checked. Announced via a staffer's X post, not a formal OpenAI paper. Community review could take weeks–months.
- Skeptics note the announcement coincided with the model's launch (marketing overlap).
- This is a *claimed* discovery. Track the verification outcome before citing it as settled.

## Related vault material

- [[_synthesis-ai-agent-discoveries-2026]] — parent synthesis (the 2026 agent-discovery wave)
- [[jacobian-counterexample-fable-2026]] — the Claude Fable 5 Jacobian result (same week)
- [[aletheia-autonomous-math-2026]] — DeepMind's autonomous Erdős-problem agent
- [[_synthesis-agents-for-math]] — the 2020–2025 theorem-proving lineage this extends
- Local: the axplorer multi-agent gate — `Agents/maumayma/Lead/AXPLORER_REPRESENTATION_VERDICT.md`

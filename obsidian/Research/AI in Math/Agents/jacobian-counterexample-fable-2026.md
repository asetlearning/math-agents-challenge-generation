---
title: "Claude Fable 5 — counterexample to the Jacobian Conjecture (dim 3)"
authors:
  - "Levent Alpöge (announcement)"
  - "Akhil Mathew (posed the question)"
  - "Claude Fable 5 (Anthropic; produced the example)"
year: 2026
venue: "X announcement + verification preprint (not journal peer-reviewed)"
url: "https://x.com/__alpoge__/status/2079028340955197566"
url_preprint: "https://www.ulam.ai/research/jacobian.pdf"
language: en
methodology_type: empirical
domain: ai
event_date: 2026-07-20
verification_status: arithmetic-independently-verified; journal-review-pending
key_concepts: []
related:
  - "[[_synthesis-ai-agent-discoveries-2026]]"
  - "[[cycle-double-cover-sol-ultra-2026]]"
  - "[[aletheia-autonomous-math-2026]]"
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/ai
  - topic/agentic-reasoning
  - topic/algebraic-geometry
  - topic/keller-map
  - ai-discovery
  - status/draft
status: draft
---

# Claude Fable 5 — counterexample to the Jacobian Conjecture (dimension 3)

> **AI-discovery note.** On 2026-07-20, **Levent Alpöge** announced (in a deliberately casual X post) that **Claude Fable 5** produced an explicit polynomial map **F : ℂ³ → ℂ³ with constant Jacobian determinant −2 that is not injective** — a **Keller map that is not an automorphism**, disproving the **Jacobian Conjecture** in dimension ≥ 3. Akhil Mathew posed the question; Fable did "the work during the World Cup final." The **arithmetic has been independently verified** (verification preprint on ulam.ai); formal journal peer review is still pending. **This is the same model family (Fable 5) our own Lead runs on** — see below.

## The problem

The **Jacobian Conjecture** (Keller 1939): every polynomial map `G : ℂⁿ → ℂⁿ` with `det Jac G =` a nonzero constant (a **Keller map**) is a polynomial automorphism (invertible with polynomial inverse). Open for ~87 years, central in algebraic geometry. A single genuine Keller map that fails to be injective kills it.

## The counterexample (verified)

Define `F = (P, Q, R) : ℂ³ → ℂ³` by:

```
P = (1+xy)³·z + y²·(1+xy)·(4+3xy)
Q = y + 3x·(1+xy)²·z + 3x·y²·(4+3xy)
R = 2x − 3x²y − x³·z
```

Setting `A = 1+xy` and `B = A²z + y²(4+3xy)`, so `P = AB`, `Q = y + 3xB`.

- **det Jac F = −2** (a nonzero constant → it IS a Keller map).
- **Non-injective** — three distinct points share an image:
  ```
  F(0, 0, −1/4) = F(1, −3/2, 13/2) = F(−1, 3/2, 13/2) = (−1/4, 0, 0)
  ```
- Therefore F is a Keller map that is **not** a polynomial automorphism → **Jacobian Conjecture is false** in dim 3, and by stabilization in every dimension ≥ 3.

The verification preprint ("A Counterexample to the Jacobian Conjecture") goes further: a projective coordinate `[x : 1+xy]` reduces the inverse problem to a **binary cubic** whose simple roots are exactly the affine preimages; this determines every fiber, the image, and the nonproperness set. It also proves a clean **properness refinement**: for a Keller map, {automorphism ⇔ proper ⇔ nonproperness set empty ⇔ that set has codimension ≥ 2}. The example violates exactly the global properness condition (its image is Zariski-open dense with codimension-2 complement; its nonproperness set is a hypersurface).

## Agent setup

| Element | Detail |
|---|---|
| Model | **Claude Fable 5** (Anthropic) |
| Human role | Akhil Mathew posed the question; Alpöge ran/curated and verified |
| Workflow | Fable produced a candidate construction + algebra steps under time pressure; Alpöge checked in-thread via **Wolfram Alpha** (determinant expansion, composition checks, numeric specialization) |
| Independent verification | Arithmetic re-derived and documented in a **verification preprint** (ulam.ai); all coefficients and the three witness points are **rational**, so the counterexample holds over every characteristic-0 field |
| Peer-review status | Journal peer review **not** complete as of 2026-07-21 |

**Full prompt:** not published. The X post is informal and gives no verbatim prompt; the preprint is an independent algebraic verification, not a transcript. (If Alpöge later releases the transcript, add it here.)

## Why this matters for us (direct relevance)

- **Same model family as Lead.** Our axplorer/B25 Lead agent runs on **Fable 5** (see `Agents/maumayma/Lead/`), and Alpöge's own casual credit line — "fable for working during the world cup final" — is the same model. This is a concrete, high-profile demonstration that Fable 5 can produce **genuinely novel research-grade mathematical objects** (not just proofs of known results), which is exactly the regime our B25 word-reduction search operates in.
- **Construction, not proof.** Unlike the CDC proof (a long deductive argument), this is a **search for an explicit witness object** — much closer to what our reducer-as-rollout search is doing (find a short certificate / explicit word). Encouraging signal for the "agent proposes a candidate, deterministic tool verifies it" paradigm we locked for v1.
- **Verification discipline.** Note the pattern: AI proposes → human + CAS (Wolfram) verifies → independent preprint re-derives. Mirrors our **two-tier "guide vs. certify"** design (GPT proposes, reducer/GAP certifies).

## Caveats

- The announcement's jokey tone (and the recurring history of *fake* "Jacobian counterexamples" as math in-jokes) initially reads as satire — **it is not**; the arithmetic checks out. But it is **not yet journal-refereed**.
- Media coverage varies wildly on the conjecture's age ("85/87 years") and on how much Fable did autonomously vs. with heavy human steering. Treat the division of labor as "human-AI collaboration," not "fully autonomous."

## Related vault material

- [[_synthesis-ai-agent-discoveries-2026]] — parent synthesis
- [[cycle-double-cover-sol-ultra-2026]] — the GPT-5.6 Sol Ultra CDC proof (same week)
- [[aletheia-autonomous-math-2026]] — DeepMind's Erdős-problem agent
- Local: `Agents/maumayma/Lead/` — our Fable 5 Lead agent (axplorer/B25)

---
title: "Equality Saturation: A New Approach to Optimization"
authors:
  - "Ross Tate"
  - "Michael Stepp"
  - "Zachary Tatlock"
  - "Sorin Lerner"
year: 2011
venue: "Logical Methods in Computer Science, Vol. 7, Issue 1 (2011); originally POPL 2009; modern reference implementation: Willsey et al., \"egg: Fast and Extensible Equality Saturation\", PLDI 2021"
url: "https://arxiv.org/abs/1012.1802"
url_translated:
language: en
methodology_type: theoretical
domain: cs
citation_count: null
citation_count_date:
key_concepts: []
extends: []
contradicts: []
replicates: []
cites: []
cited_by: []
related:
  - "[[Research/Group theory/Word Problem/knuth-bendix.md]]"
  - "[[Research/Group theory/Word Problem/dershowitz-jouannaud-1990]]"
quality_notes: "The single most actionable mechanism found for the 2026-07-21 KB-ordering/reduction-length focused dig: directly explains, as a general principle (not an empirical curiosity), why a non-confluent system with MORE rules can reduce a specific target further than a minimal confluent one. Read via ar5iv abstract + subagent extraction of mechanism; not read at full implementation depth this pass (e.g. the egg PLDI 2021 paper's e-class analysis / extraction-cost-function machinery specifically) — flagged as a good next full-text read if this lever is pursued."
author: maumayma
tags:
  - agent/research
  - user/maumayma
  - domain/cs
  - topic/rewriting-systems
  - topic/knuth-bendix
  - topic/divergence-and-stagnation
  - paper
  - status/draft
---

# Equality Saturation: A New Approach to Optimization

## Abstract

"Optimizations in a traditional compiler are applied sequentially, with each optimization destructively modifying the program to produce a transformed program that is then passed to the next optimization. This approach has a well-known deficiency: the final program produced by the compiler may not be optimal because an earlier optimization may enable a later one, or conversely disable a later one that could otherwise have resulted in better performance... We present a new approach for structuring the optimization phase of a compiler. In our approach, optimizations take the form of equality analyses that add equality information to a common intermediate representation. The optimizer works by repeatedly applying these analyses to infer equivalences between program fragments, thus saturating the intermediate representation with equalities. Once saturated, the intermediate representation encodes multiple optimized versions of the input program. At this point, a profitability heuristic picks the final optimized program from the various programs represented in the saturated representation." [Assembled from subagent extraction of the abstract; core sentences quoted above verified via fetch, full paragraph reconstruction not independently re-verified word-for-word against primary source this session.]

## TL;DR

Instead of destructively rewriting a term/program along ONE path (where an ordering choice at step k can foreclose a better rewrite that was only reachable via a different step-k choice — the classical "phase-ordering problem," directly analogous to "which KB rule fires first"), an e-graph maintains a **congruence relation over every equivalent form discovered so far** via union-find + hashcons, and rewrite rules only ever **add** equalities — nothing is ever destructively replaced. You run rewriting to saturation (or a budget/timeout), then a **separate extraction pass with an explicit cost function** (e.g., shortest word length) picks the best representative from everything reachable, decoupling "explore all equivalent forms" from "commit to a normal form." This is a formal, general answer to why a non-confluent, over-complete rule set can reduce further than a minimal confluent one: confluence is a property of committing to a SINGLE canonical path; an e-graph never commits, so it never needs confluence to guarantee reachability of the best form.

## Problem

How to structure a rewriting-based optimizer (originally: compiler optimization passes) so that the final result doesn't depend on the arbitrary ORDER in which individual rewrite rules happen to fire — avoiding cases where applying rule A before rule B forecloses a better result that only rule-B-then-rule-A would have reached.

## Approach

Represent the object being optimized (originally: a program; for us, a group-theory word) as an **e-graph**: a set of e-classes (equivalence classes of equivalent sub-terms), each containing one or more e-nodes (operators/symbols with pointers to child e-classes), with union-find merging e-classes proven equal by a rewrite. Applying a rewrite rule ADDS a new equality (merges e-classes) rather than replacing a term. Repeat rule application across the whole e-graph until **saturation** (no rule produces any new equality) or a resource budget is hit. Then run **extraction**: a separate pass with an explicit, arbitrary cost function (shortest total length, fewest operations, whatever the actual objective is) that picks the single best representative term implicitly encoded by the saturated e-graph.

## Key result

The saturated e-graph encodes **multiple optimized versions of the input simultaneously** — the final answer is chosen by a profitability/cost heuristic applied AFTER exploring the full (or budget-bounded) space of equivalent forms, not chosen implicitly by the accident of rewrite-application order. This structurally "obviates the need to worry about optimization ordering" (per the paper's own framing, confirmed via subagent extraction) — the phase-ordering problem is sidestepped by construction, not solved by a smarter ordering heuristic.

## Assumptions

Rewrite rules must be validity-preserving equalities (both directions sound, i.e. each rule is genuinely an equation, not a one-directional simplification with side conditions) — for group-theory words, this maps directly onto B(2,5) relations (any valid rewrite rule, in either orientation, is a genuine group-theoretic equality) rather than onto an ad hoc reduction heuristic. No confluence or termination property is required of the rule SET as a whole — only that each individual rule application is a valid equality, which is a much weaker and easier-to-satisfy requirement.

## Limitations / scope

**The well-known practical weakness (not mentioned in the abstract, but standard knowledge in this literature and directly relevant to a 7M-rule bank)**: e-graphs can grow extremely large under saturation with many rules and large search spaces — "e-graph explosion" is the central practical engineering challenge the follow-up tool `egg` (Willsey et al., PLDI 2021) was built to address (via efficient hashcons/rebuilding, deferred congruence closure). Applying this directly to B(2,5)'s full rule bank (millions of rules) and long words (up to ~1348 characters) would need either a heavily budget-bounded/incremental saturation, or applying it to a sub-problem (e.g. a windowed sub-word, or a curated high-value rule subset) rather than the full closure — this needs engineering validation before being treated as a drop-in replacement for beam search, not an assumption.

## Replication evidence

`egg` (Willsey et al., PLDI 2021) is a widely-used, actively maintained modern reference implementation confirming the approach scales to real optimization problems (term rewriting for tensor compilers, CAD, and other domains) well beyond the original 2009 compiler-optimization proposal — a genuine multi-domain replication of the core idea, though not yet applied (as far as this pass found) to group-theoretic word problems specifically.

## Why this paper matters

This directly explains, as a first-principles mechanism rather than an empirical curiosity, the team's own observation that a beam search using ~7M rules (many non-firing on any given word) still out-reduces smaller rule banks: **more rules give more equalities to saturate with, and a non-confluent/non-minimal rule set loses nothing under this framing** because nothing is ever destructively committed — the "extra" rules can only ever add reachable equivalent forms, never remove options. This reframes "why does an overcomplete non-confluent system reduce further" from a puzzling empirical fact into an expected consequence of NOT using a confluent-commit strategy in the first place. It also suggests a concrete engineering direction: build an (possibly budget-bounded/incremental) e-graph layer over the B(2,5) rule bank + target word, saturate, then extract by length — this could be a principled generalization of what the current 7M-rule beam search is doing informally and by brute force.

## Open questions surfaced

Whether an e-graph-style saturation layer scales to B(2,5)'s actual rule-bank size (millions of rules) and word lengths (up to ~1348 chars) without needing the full `egg` engineering investment — a scoped pilot (e.g. saturate a short windowed sub-word with a curated few-thousand-rule subset, extract by length, compare against beam search on the same sub-problem) would be the natural first empirical test, not a full production port.

## Related material in vault

- Related: [[Research/Group theory/Word Problem/knuth-bendix.md]] (contrasting single-path confluent-commit approach)
- Related: [[Research/Group theory/Word Problem/dershowitz-jouannaud-1990]] (the classical rewriting-theory survey this paper's framing departs from)

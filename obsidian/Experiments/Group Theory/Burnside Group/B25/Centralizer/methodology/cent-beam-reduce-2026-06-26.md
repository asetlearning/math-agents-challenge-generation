---
title: "Centralizer Beam Reduction — True Shortest Forms for 34 Smallest Elements"
date: 2026-06-26
domain: group-theory
project: b25
experiment_type: centralizer
instance: cent_enum_beam_reduce
author: maumayma
status: complete
pre_registration_note: "Directed task from Lead (Maria GO). Run begun before this note was written; methodology documented here for provenance."
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/centralizer, topic/beam-search, project/b25, status/complete, methodology, experiment]
---

# Methodology: Centralizer Beam Reduction (2026-06-26)

## Context

The centralizer enumeration experiment (`cent-full-enum-2026-06-26`) computed upper-bound lengths for all 1,953,125 elements of C_{B₀(2,5)}(CoreA) using a greedy shortlex FSA (199K rules, 3000 iters). The result is NOT true shortest lengths — it is the fixed point of a non-confluent KB bank applied greedily.

The distribution has only 34 non-trivial elements with greedy length < 20,000 chars. This sub-run beam-reduces those 34 to their true shortest forms (best achieved by beam search), giving honest target sizes for ITEM 2b (reshape-to-centralizer).

## Scope

- **Group**: B₀(2,5) — finite restricted quotient, order 5^34
- **Target**: 34 non-trivial centralizer elements with greedy FSA length < 20,000 chars
  - 5 priority elements with FSA length < 10,000 chars
  - 29 remaining elements with FSA length 10,000–19,999 chars
- **Source**: FSA-reduced word files from Experimenter at `/tmp/cent_beam/elem_*.txt.reduced` (GAP format)

## Hypothesis

The greedy FSA length is a strict upper bound. Beam search (non-monotone exploration) with a larger rule bank will find shorter representatives for at least some of the 34 elements, establishing tighter upper bounds on the true minimal word length for centralizer elements.

**Falsifiable form**: If beam search achieves zero improvement on all 34 elements, the greedy FSA lengths are already the beam-fixed-point (at 500K rules, beam-width 16384).

## Methods

### Rule bank
Combined rule file:
- 31 GAP-verified junction seed rules (sha256: `341c64bcc...`, `b25_seed_rules_2026-06-25.kbprog`)
- First 500,000 rules from the b25_kbmag shortlex KB (sha256 of full bank: see provenance)
- Total: 500,031 rules

Maria directed to use bigger rule banks with rules that achieved reductions on target B(2,5) words.

### Beam parameters
- Binary: `braid_reduce` (`experiments/burnside/burnside_bidirectional/target/release/braid_reduce`)
- `--beam-width 16384`
- `--beam-secs 120` for priority elements (FSA len < 10,000)
- `--beam-secs 60` for remaining 29 elements
- Hard process timeout: 3× beam-secs

### Word construction
FSA-reduced words (from Experimenter's wordreduce pass with 199K shortlex rules) are parsed from GAP list format (`X^N*Y*...`) to plain letter strings (`XXXX...Y...`) and written to temp files for braid_reduce.

### Coordination with Experimenter
Experimenter ran a parallel beam pass on the 5 priority elements with 199K rules + 180s. Their results:
- gen_7^1 (6453 → 5138, Δ=-1315)
- gen_4^1 (9995 → 6867, Δ=-3128)
- gen_8^1, gen_9^1, gen_8^2: no improvement

Final result per element = MIN(my 500K beam result, Experimenter's 199K result).

## Termination Criteria

Each element is bounded (fixed beam-secs budget + hard timeout). All 34 elements are run exactly once. After completing, pgrep-verify no runaway processes.

## Anti-Pattern Check

- **GAP word-equality on all rules?** YES — 31 seed rules are GAP-verified; shortlex rules come from the kbmag shortlex KB which only adds a rule when it passes all checks.
- **No abelianization sufficiency?** CORRECT — only length is reported; no abelianization claims.
- **No 'irreducible' close?** CORRECT — results reported as "no shortening found at [rule bank + beam budget]". Open variants: RPO bank, longer beam, beam+annealing (not exhausted).
- **Untested variants** (per no-premature-close rule):
  1. RPO rule bank (different structural coverage than shortlex)
  2. Longer beam (300s or more) on gen_8 and gen_9 single generators
  3. Beam with the full 13M shortlex bank (no cap)
  4. Beam starting from RAW concatenation (before FSA reduction) — may explore different paths
  5. Other KB orderings (weighted shortlex, lenlex)

## Seeds

Arms 1 and 3 are deterministic (fixed rules, fixed beam-width, fixed element). No randomness.

## Provenance

See `runs/b25/cent_enum_beam/<timestamp>/provenance.json` for exact git SHA, rule bank sha256, beam parameters, and file paths.

## Data Link

- Run output: `runs/b25/cent_enum_beam/<timestamp>/`
- Experimenter priority-5 results: `/tmp/cent_beam_results/elem_*.out`
- Combined results: `Centralizer/results/cent-beam-reduce-results-2026-06-26.md`

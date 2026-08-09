---
title: Dynamic-overlap rule generation (H3) — pre-registration
domain: group-theory
project: b25
instance: B(2,5)
experiment_type: dynamic-rulegen
status: pending
author: maumayma
date: 2026-07-28
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/rule-generation, topic/knuth-bendix, topic/proof-search, project/b25, status/pending, methodology]
---

# Dynamic-overlap rule generation — pre-registration (H3)

**Pre-registered before any pipeline run.** Implements stage 2 of Lead's attack design
([[2026-07-28-b25-attack-design-arms-and-rulegen]]); Maria's GO on record. Nothing here is a certificate —
Validator owns all soundness/admissibility.

**Scope guard:** =e identity-certificate shortening in B₀(2,5) (HWW pcps commutator relators, trivial in B₀
by construction). NOT a free-B(2,5) claim (Kourovka 11.48 OPEN). See [[project_b25_benchmark_words_trivial]].

## What this experiment is (plain English)

The seam lever (rotate an =e word by period 72, then let the incomplete linear reducer catch seam-exposed
structure) beats the recorded best on 92/119 words for +941 chars — but the static rule bank is saturated:
only **17 rules ever fire**, at any bank size. Bigger *decreasing* banks are inert. So the open problem is a
rule **source** problem: manufacture new certified spellings whose substrings line up with the reducer's
active structure in the states the seam actually visits (rotated intermediates, fixpoints), including the
two rule classes a descent-only reducer can't use — same-length phase-shifters and small expand-then-shrink
enablers. We generate those, GAP-admit each one, and test whether any of them fires on a dynamic state to
produce a further, gate-passing reduction.

## Hypothesis

- **H3 (load-bearing):** a seam-critical-pair + alternate-order **Δ=0 / small-Δ>0 enabler bank,
  dynamic-overlap-scored**, is more likely to beat the 941/92 incumbent than any larger length-decreasing
  bank — because it targets rules whose **RHS creates an active seam hit after a phase change**, which a
  monotone bank cannot express.

Falsifiable and directional: the claim is specifically that Δ≥0 rules scored on dynamic states beat the
saturated Δ<0 static bank.

## Kill condition

After generation + GAP-admission + dynamic scoring, if **no** admitted Δ=0 / Δ>0 rule fires on any dynamic
state (rotated intermediate, fixpoint, current-best) to produce a **gate-passing sub-current reduction on
any of the 119 words**, then the Δ≥0 rule class is inert here too → **retire dynamic-overlap rule generation**
as a lever and report the negative to Lead (exhaustive-negative discipline: enumerate every candidate bucket
tried and why the search is exhausted). No silent narrowing.

## Target words / properties

- **Corpus:** all 119 `comm_i_j` benchmark relators (=e in B₀). Primary interest: the **27 non-improved**
  words (seam plateau) plus the 92 improved (can the new rules compound past the +941 floor?).
- **Property tested:** existence of an admitted Δ≥0 rule that, applied in bounded sequence search from a
  dynamic state, reaches a strictly shorter =e word than the current best for that word.

## mixer Agents / tooling involved

- `braid_reduce` (release binary, `experiments/burnside/burnside_bidirectional/target/release/braid_reduce`)
  — greedy `--no-beam` reduction, used ONLY for the usefulness gate on candidate-augmented banks.
- `cyclic_reduce` (period-72 seam) + `run_maxpower_v2` machinery for dynamic-state replay.
- Generation/scoring pipeline (this experiment) — pure-Python, in `experiments/burnside/b25/dynamic_rulegen/`.
- **Validator** — GAP admission of every `L = R` in B₀(2,5) (finite-pc oracle + alphabet gate +
  verify_rewrite_atlas). Binding; the pipeline's self-PASS is never trusted.

## Modifications (what is B(2,5)-specific)

- Overlap scoring is **dynamic**: score whether `L` occurs — or is *created* by `R` — in rotated/conjugated/
  fixpoint states, NOT in the raw benchmark strings (static overlap is exhausted, per
  [[project_b25_maxpower_seed_falsified]] and [[project_b25_mega_le16_effective_set]]).
- Δ≥0 rules are admitted but **quarantined OUT of the monotone reducer** — bounded sequence search only.
- Candidate sources are seam/relator-structural (below), not random enumeration.

## Method — my 4 sub-slices (Lead-assigned)

1. **(a) Dynamic-state corpus.** Assemble per word: current best (`best_words/<id>.txt`), le80-no-rotation
   greedy fixpoint, and the period-72 intermediate states recorded in the 92 certs' `seam_rotations` traces
   (`runs/b25/patternboost_loop_v1/maxpower_v2_20260724/cert_*.json`).
2. **(b) Active-window extraction.** Around every actual fire, near-fire, and seam-join in those states,
   extract the before/after neighbourhoods (prefix/suffix contexts of the 17 active LHSs + seam-crossing
   boundaries).
3. **(c) Seam-critical-pair candidate generation.** From the period-72/le80 traces, overlap suffixes/prefixes
   of active LHSs with seam-crossing contexts to form critical-pair `L = R` candidates.
4. **(d) R2 Δ=0 phase-shifters.** Pull the ~330 Δ=0 candidates already extracted in the R2 population
   (`runs/b25/patternboost_R2_rulegen/{admission_tooling,extraction_20260701}/cand_rules.tsv`) as
   phase-shifter candidates.

Each candidate is **free-reduced**, bucketed (Δ<0 primary / Δ=0 phase-shifter / small Δ>0 enabler), and
scored:
`score = dynamic_occurrence + boundary_created_hits + active_LHS_prefix_suffix_overlap +
seam/macro_boundary_alignment − immediate_revert_penalty − uncontrolled_growth_penalty`.

## Validator submission spec (Lead, 2026-07-28)

Candidate files to Validator for GAP admission: **≤5000 rules/file, FREE-REDUCED**, with **file path +
provenance** (generator name, git SHA, source-bucket #). Validator runs the admission gate; **pipeline
self-PASS is never trusted**. Only Validator-admitted `L = R` may enter the bounded sequence search.

## Termination criteria

- **Success:** ≥1 admitted Δ≥0 rule produces a gate-passing sub-current reduction on ≥1 word (→ route the
  reduced word's cert to Validator's beat-beam gate; do NOT self-record).
- **Kill:** as above (no admitted Δ≥0 rule fires productively on any dynamic state, buckets exhausted).
- **Resource fence:** 2 CPU-heavy slots max for this lane (shared with the stage-1 control arm); the gate's
  `braid_reduce` runs wait for a free slot or escalate to Lead — never exceed the box cap of 4.

## Baselines

- **Incumbent:** seam@72 on le80 = 941 chars / 92 words (Developer, `maxpower-le80-seam-results-2026-07-28`).
- **Static-bank saturation:** 17 firing rules at all bank sizes (le24 281k → le80 9.4M), the thing H3 must beat.
- **Prior seam:** mega_le16 = 351 chars / 77 words.

## Seeds / determinism

The reducer is deterministic (greedy, fixed bank SHA). Generation is deterministic given the corpus (no RNG).
Where a scored sweep has a stochastic component, n≥5 with reported spread; the primary claim is existential
(a single admitted productive rule falsifies the kill), so no seed-averaging is needed for the pass/fail.

## Anti-pattern check

- **Not tuning on the scoring set:** scoring uses dynamic states (rotated intermediates / fixpoints), and the
  usefulness gate is judged on the SAME 119 words that are the deliverable — so the guard is that a "win"
  must be a *new =e reduction*, GAP-verified, not a re-fit of an existing spelling. Report misses with hits;
  no cherry-picking (a rule firing on 1 word and failing on the rest is a single word, not a story).
- **Ordering discipline:** alternate-order (wtlex/RPO) candidates are a rule *source* only; switching the
  reducer's own ordering would be a different experiment.
- **Compression/collision:** any phase-shifter must be verified unique per equivalence class (GAP admission
  covers this), not merely shorter.
- **Hall's reductions:** check `Research/Group theory/Burnside groups/B25/` before claiming any generated
  relation is novel.

## How it will be validated

- Every `L = R`: Validator GAP admission in B₀(2,5) (binding).
- Every claimed word reduction: sanity gate (GAP =B₀, ≥100 floor, provenance=reducer) → cert → Validator
  beat-beam gate before it counts. **No self-record.**
- `Validation of the H3 verdict itself:` the kill/pass is decided on Validator-admitted rules only.

## What "success" means

A single Validator-admitted Δ≥0 rule that fires on a dynamic state and yields a gate-passing, strictly
shorter =e word for any of the 119 relators. Absent that across all buckets → H3 killed, lever retired.

## Related material

- [[_type]] — Dynamic Rule Generation experiment-type root
- [[2026-07-28-b25-attack-design-arms-and-rulegen]] — Lead attack design (H3 text source)
- [[project_b25_beatbeam_cyclic_seam]] — the seam mechanism these rules target
- [[project_b25_maxpower_seed_falsified]] — static-bank saturation (the thing H3 must beat)
- [[project_b25_benchmark_words_trivial]] — scope guard (=e identity certs, not free-B(2,5))

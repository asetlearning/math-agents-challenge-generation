---
title: "T-018 seed reachability and Fine-Wilf pruning — triage"
status: conjectured
domain: group-theory
project: challenge-gen
claim: "No 2- or 3-cell diagram over {v^5 : |v| <= 7} has a 2.5-power-free outer boundary (Math Expert's arguments A1-A3, Experimenter's Fine-Wilf-pruned enumeration)"
claimant: Math Expert (arguments), Experimenter (enumeration, branch t018-diagram-search @ 4979927)
verification_method: "re-derivation of each bound; direct check of the Fine-Wilf bound on the real cell table; independent re-enumeration of 3-cell diagrams by prefix/suffix hashing; positive controls"
tools_used: ["python3 3.12.3 and the t018 venv (numpy 2.4.4)", "scratch/seed_*.py"]
author: asetlearning
tags: [agent/validator, user/asetlearning, domain/group-theory, topic/b25, topic/van-kampen, topic/power-free-words, project/challenge-gen, status/conjectured, proof]
---

# Triage — T-018 seed reachability (Lead request, 2026-10-15)
Sources: [[2026-10-15-t018-power-free-seed-reachability]], code `experiments/challenge_gen/t018/{seed_enum,seed_enum3,patches}.py` and its tests. Parallel check, not a gate; deadline is before any claim built on the seed finding. Verdict note: [[2026-10-15-t018-seed-reachability-review]].

## Sub-claims
1. **A1-A3 (Math Expert, "argued").** Single-arc cells exist only for |v| ≤ 3 (with partner lengths); every exposed run of a cell is capped by ℓ_L + ⌈2.5ℓ_s⌉ − 2; the 3-cell chain survivors are exactly ends (2,3) and (3,3) over a |v| = 7 middle.
2. **Fine-Wilf pruning (Experimenter).** Arcs between distinct primitive roots are ≤ |vi|+|vj|−gcd−1; equal lengths ≤ |v|−1; this leaves 60 of 343 length triples for triangles.
3. **"0 power-free 2- and 3-cell patches".** Scope, caveats (maximal arcs; no positive control for the triangle final stage).

## Scope check
Verification of a combinatorial non-existence claim over a finite set (the 1,494-entry move set). Nothing here is about the free group B(2,5) or its Dehn function: it is a statement about folded diagrams with at most 3 cells over R7 cells only.

## Tools (probed)
- python3 3.12.3 (no numpy); the t018 venv has numpy 2.4.4 and runs the Experimenter's code unchanged.
- No GAP needed: no group-equality claim.

## Methods
| Sub-claim | Method | What it can establish |
|---|---|---|
| 1 | re-derive each bound; brute-force the counting (all end/middle lengths, arcs, gaps) | proved / argued-OK |
| 2 | direct search of the real table for a shared window one longer than the bound; recount triples | replicated on the table |
| 3 | own enumeration of triangles and chains with a different algorithm and no Fine-Wilf pruning; comparison with the Experimenter's boundary sets; positive controls | independent replication, gaps |

## Hard limits
- A non-existence claim over ≤ 3 cells says nothing for N ≥ 4.
- Pure vertex/stem attachments and the wrapped (nested) shapes are argued, not enumerated, unless stated.

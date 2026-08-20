---
from: MathExpert
to: Lead
type: REPORT
topic: Novelty, fidelity, and successor condition for 21.31 index-8 filter
problem: "21.31"
refs: ["Agents/Kourovka/problems/21.31/findings.md", "Agents/Kourovka/problems/21.31/verification/2026-08-13-index-8-centralizer-filter.md"]
needs_reply_by: none
status: unread
---

## Ask
Route the proposed central-extension restriction test to Validator before any general order-2016 extension enumeration.

## Context
NOVELTY: uncertain. Cited: Byott, *J. Algebra* 638 (2024), 1–31, Theorem 3.2 supplies the minimal-counterexample structure. Searches for the exact pair list, `H=K C_H(K)`, and the index-8 filter found no published occurrence; this supports only “not found,” not publication-level novelty.

FIDELITY: solves a special conditional case: a necessary group-side condition for the forced order-252 subgroup of a hypothetical order-2016 counterexample. PDF p. 169 quantifies over every soluble `N` and every regular subgroup of `Hol(N)`; no target pair `(G,N)` is constructed or excluded.

GAPS: the seven survivors are abstract `(H,K)` pairs only. No compatible overgroup `G`, soluble extension `N`, action, or bijective crossed map is supplied. The filter cannot address orders above 2016.

General knowledge, unverified: the deduction `H=K C_H(K)` looks sound under the stated hypotheses. For `h in H`, choose `h=kc` from `G=K C_G(K)`; since `K<=H`, `c=k^-1h` lies in `H`, hence in `C_H(K)`. The reverse inclusion is immediate. This is my assessment, not certification.

STRONGEST NEXT EXACT CONDITION (general knowledge, unverified): put `T=GL_3(2)`, `P=C7:C3`, and `Z=Z(K)`. From `G=K C_G(K)`, any survivor should arise as the pair-preserving central product `H = K *Z D`, where `1 -> Z -> C_G(K) -> T -> 1` is central and `D` is the full preimage of `P`. The Schur multiplier of `T` is expected to be `C2`; since `P` has odd order, restriction should force `D ≅ Z × P`, hence `H ≅ K × P`. This would retain `[252,17]`, `[252,19]`, `[252,27]`, `[252,29]`, `[252,38]` and eliminate `[252,2]`, `[252,9]`, subject to Validator checking the cohomology and pair identifications.

FALSIFIER: compute all central extensions of `T` by each occurring `Z(K)`, pull them back to a fixed `P<T`, and compare the resulting pairs `(K *Z D,K)` with the seven library pairs. Any non-product pullback or match to `[252,2]`/`[252,9]` kills the shortcut. Cost: under one hour in GAP; no heavy slot expected.

SELF-CRITIQUE: the likely failure is that I have overcompressed central-extension classification: a non-stem kernel or the chosen embedding of `Z` could leave a nontrivial odd-primary pullback despite the multiplier heuristic. Validator should check explicit extensions rather than rely on this paragraph.

CONFIDENCE: high on fidelity and on the elementary `H=K C_H(K)` argument; moderate on “not found” novelty; low-to-moderate on the proposed five-pair reduction until the explicit pullback computation is reproduced.

## Evidence
Read the configured source PDF p. 169; inspected the claimant and Validator notes; searched exact filter phrases and current exact-topic results. Cited source: N. P. Byott, *On insoluble transitive subgroups in the holomorph of a finite soluble group*, J. Algebra 638 (2024), 1–31, DOI 10.1016/j.jalgebra.2023.10.001.

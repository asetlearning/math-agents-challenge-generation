---
title: "Working log — Kourovka 21.52 — counterexample direction"
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
direction: counterexample
cycle: 1
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/coloured-graphs
  - project/kourovka
  - status/draft
---

# Working log — Kourovka 21.52

## Active-time ledger

- `2026-08-17T15:15:48Z` — START cycle 1, revision 1, counterexample direction; cumulative active minutes: 0.
- `2026-08-17T15:23:20Z` — STOP before any mathematical enumeration; frozen exact A5 scripts and compute manifest; awaiting a Lead compute lease; cumulative active minutes: 8.

## Staleness and source check — 2026-08-17

`source_transcription_checked: yes`

`active_scope_checked: yes`

`external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`

I rendered and visually inspected configured source PDF page 172. Corrected transcription:

> Let \(L\) be a finite non-abelian simple group, and let \(D\) be a conjugacy class of involutions in \(L\). Consider the complete graph \(\Gamma\) with vertex set \(D\). Define an equivalence relation \(\sim\) on the set of edges by \((a,b)\sim(c,d)\) if and only if \(|ab|=|cd|\). A coloured-graph automorphism is a permutation \(\tau\in S_D\) such that \((a,b)\sim(a^\tau,b^\tau)\) for every edge \((a,b)\). Is the automorphism group of \(\Gamma\) a subgroup of \(\operatorname{Aut}(L)\)?

The rendered page has no editor comment, later comment, exception, or starred-status qualification at 21.52. The canonical issue-21 JSONL path named by the general protocol is absent in this vault (the corpus directory contains only issue 20), so separate `answered`, `has_editor_comment`, and `has_later_comment` JSON fields were unavailable. The current assignment has `blind_run.enabled: true`; by Lead instruction I did not inspect solution-bearing history or use the web.

### Clause matrix

| source clause | equivalent typed formulation | active? | literature status in this blind run |
|---|---|---|---|
| \(L\) finite non-abelian simple; \(D\) one conjugacy class of involutions | arbitrary admissible pair \((L,D)\) | yes | deferred |
| complete graph on \(D\); edge colour exactly the fibre of \(\{a,b\}\mapsto |ab|\) | unordered distinct pairs, with no finer product-conjugacy data | yes | deferred |
| \(\tau\in S_D\) preserves the equivalence class of every edge | \(|ab|=|a^\tau b^\tau|\) for all distinct \(a,b\in D\) | yes | deferred |
| ask whether \(\operatorname{Aut}_{\rm col}(\Gamma)\leq\operatorname{Aut}(L)\) | every such \(\tau\) lies in the restriction image of \(\operatorname{Stab}_{\operatorname{Aut}(L)}(D)\) | yes | deferred |

### Admissibility checklist reconciled to revision 1

| constraint id | source requirement | A5 experiment handling |
|---|---|---|
| `21.52-forall-L-D` | universal quantifier over admissible \((L,D)\) | one admissible pair can refute; equality for A5 is only fixed-target partial evidence |
| `21.52-L-finite-nonabelian-simple` | \(L\) finite non-abelian simple | fix \(L=A_5\) |
| `21.52-D-single-involution-class` | one conjugacy class, all elements order 2 | take all 15 involutions of \(A_5\), its unique involution class |
| `21.52-Gamma-complete-on-D` | all unordered pairs of distinct vertices | freeze all \(\binom{15}{2}=105\) edges |
| `21.52-edge-colour-exact-product-order` | same colour iff product orders agree | store the complete matrix with entries \(|ab|\), no extra labels |
| `21.52-tau-preserves-all-edge-colours` | permutation preserves every matrix entry off the diagonal | exhaust all compatible injective vertex assignments |
| `21.52-tau-induced-by-AutL` | compare with the exact restriction image of the setwise stabilizer in \(\operatorname{Aut}(A_5)\) | enumerate all automorphisms from all images of a generating pair; independently compare with all \(S_5\)-conjugation restrictions |

No scope mismatch was found.

## Strategy portfolio — 2026-08-17

1. **Catalogue/small-case mode — selected.** `SMALLEST-SIMPLE-COLOUR-AUTOMORPHISM`: determine the exact coloured structure for \(A_5\), its full colour-preserving permutation group, and the exact \(\operatorname{Aut}(A_5)\) restriction image. A separating permutation would answer the universal question negatively; equality proves only a fixed-\(A_5\) partial.
2. **Structured-construction mode — held outside this decision.** Search for accidental product-order symmetries by designing an involution-class association scheme with fused relations. Lead explicitly forbids moving to another target before the complete \(A_5\) certificate and a new direction decision.
3. **Theoretical mode — held outside this decision.** Reconstruct group-theoretic incidence from the product-order relations and prove rigidity. This is qualitatively different but not authorized before the A5 result.
4. **Certificate plan.** Deterministic one-line permutation model of \(A_5\); indexed list of all 15 involutions; full 15-by-15 product-order matrix and all edge-colour classes; exhaustive list of all colour automorphisms; exhaustive list of all \(A_5\) automorphisms and their restrictions; independent \(S_5\)-conjugation restriction image; exact set comparison; a separately frozen verifier using a different enumeration path.

This is the cheapest certifiable experiment and is ranked first. No mathematical enumeration has been run.

## Frozen compute request — 2026-08-17

Frozen manifest: `Agents/Kourovka/problems/21.52/scratch/a5-colour-test/frozen-run-manifest.json`.

Scripts were hashed but not executed:

- `a5_colour_test.py`: `6e392e5a784893160cedc00af6c52b7ab682d37c31e36cd11ba16d0f14fdc8e4`.
- `verify_a5_colour_certificate.py`: `356b186a237402dddaffcd327659e046bef45ba31c359109bdae43252b827a10`.

Requested bound: one job, one CPU core, estimated RAM below 256 MiB, 60-second wall timeout plus 5-second kill grace per command, 10-minute lease. Exact commands and every output path are frozen in the manifest. State: `awaiting_lead_compute_lease`.

## Leased A5 computation — 2026-08-17

- `2026-08-17T15:29:11Z` — START under Lead compute slot 1, expiring `2026-08-17T15:36:54Z`; all three required SHA-256 guards matched; cumulative active minutes: 8.
- `2026-08-17T15:29:11Z` — Frozen command 1 executed exactly once. Exit code 0; observed tool wall time `0.908858965` seconds; frozen `timeout 60s` plus 5-second kill grace guarded it.
- `2026-08-17T15:29:13Z` — Frozen command 2 executed exactly once. Exit code 0; observed tool wall time `1.13760316` seconds; frozen `timeout 60s` plus 5-second kill grace guarded it.
- `2026-08-17T15:30:17Z` — STOP after hashing and inspecting every output; slot 1 released; cumulative active minutes: 10.

No command was rerun, no script or manifest was patched, and no group beyond \(A_5\) was examined.

### Guard hashes before execution

- Manifest: `9d91be237370aef9bf40013325b08e4927e228e5f8d4ecc93b062cffe91f357a` — matched lease.
- Enumerator: `6e392e5a784893160cedc00af6c52b7ab682d37c31e36cd11ba16d0f14fdc8e4` — matched lease.
- Verifier: `356b186a237402dddaffcd327659e046bef45ba31c359109bdae43252b827a10` — matched lease.

### Exact bounded result

The frozen computation constructed \(A_5\) as all 60 even permutations of five points, found all 15 involutions, used all 105 unordered distinct pairs, and found product-order colours exactly \(\{2,3,5\}\). Exhaustive colour-preserving permutation backtracking visited 1516 nodes and returned a group of order 120. Exhausting all \(60^2=3600\) possible images of a fixed generating pair returned all 120 automorphisms of \(A_5\), whose restriction image on the 15 involutions also has order 120. Independently, all 120 conjugations by \(S_5\) give exactly the same restriction image. The two 120-element permutation sets are equal: there is no colour-preserving permutation outside the restriction image for this \(A_5\) class.

This is `equality_for_A5`, hence a fixed-target `PARTIAL_RESULT`, not a counterexample and not a proof of the universal scope.

The independent frozen verifier reconstructed the group, class, complete colour matrix, full colour-automorphism enumeration, full \(A_5\)-automorphism enumeration, restriction image, and \(S_5\)-conjugation image. All 15 named checks returned `True`; `ALL_CHECKS_PASS True`.

### Output evidence

| output | bytes | SHA-256 |
|---|---:|---|
| `scratch/a5-colour-test/a5-colour-certificate.json` | 179985 | `4dc45ea15635231524e0b04fba73bf775e2be89da8f364648137d8d9622375e2` |
| `scratch/a5-colour-test/a5-colour-summary.txt` | 550 | `c376430a6b0b97136d791a063865e8f042fede55abd0362df05e5ab2c0764a17` |
| `scratch/a5-colour-test/a5-colour-run.stdout` | 550 | `c376430a6b0b97136d791a063865e8f042fede55abd0362df05e5ab2c0764a17` |
| `scratch/a5-colour-test/a5-colour-run.stderr` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `scratch/a5-colour-test/a5-colour-independent-verification.json` | 1391 | `c74bf55643f3cf112f43e718dbf50fd5c6a58f97747501add4a3e5dd7becd299` |
| `scratch/a5-colour-test/a5-colour-verification.stdout` | 866 | `d33759f64eb361f9202a40f212483bdd5aa30237747abdbed49aed36ceed6808` |
| `scratch/a5-colour-test/a5-colour-verification.stderr` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

Embedded certificate digest: `58eee67fc303b15947a21fe9eb997f92f32b348a2e00018446a11b1eedbe3674`. Embedded independent-verification digest: `5edcf0aedf02ea4464309bb21c191e788bc0a48e0f54bbb60dc265b0c12407b1`.

The complete indexed group/class, 15-by-15 matrix, 105 edge assignments, all 120 colour automorphisms, all 120 automorphisms on 60 group elements, both 120-element restriction images, and exact set comparison are stored in the certificate. The two stderr files are empty.

### Strategy disposition

The Lead-authorized A5 test is complete and its counterexample success condition failed. Its kill criterion therefore fired at fixed-target equality. No enlargement to another simple group or family is authorized. State: `awaiting_lead` for the next explicit strategy decision.

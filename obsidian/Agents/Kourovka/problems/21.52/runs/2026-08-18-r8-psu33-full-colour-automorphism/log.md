---
title: "Problem 21.52 counterexample lane — PSU(3,3) full product-order colouring"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/coloured-graphs
  - project/kourovka
  - status/draft
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
direction: counterexample
strategy: PSU33-FULL-COLOUR-AUTOMORPHISM
---

# PSU(3,3) full-colour lane

## Active-time ledger

- 2026-08-18T04:18:51Z — work start; cumulative active minutes: 116. Increment cap: 45 minutes; safety stop: 2026-08-18T05:16:00Z.
- 2026-08-18T04:20:05Z — source/scope/tooling gate complete; cumulative active minutes: 118.

This is a fresh independent fixed-group lane. The unreviewed PSL(3,3) and PSL4(2) artifacts were not opened and are not premises.

## Staleness check

`source_transcription_checked: yes`

`active_scope_checked: yes`

`external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`

The configured source PDF was rendered visually at page 172 with:

```text
source _meta/agents/Kourovka/paths.env
pdftotext -f 172 -l 172 -layout "$KOUROVKA_PDF" -
pdftoppm -f 172 -l 172 -png -r 180 "$KOUROVKA_PDF" /tmp/kourovka-21-52
```

Corrected source-faithful transcription:

> 21.52. Let L be a finite non-abelian simple group, and let D be a conjugacy class of involutions in L. Consider the complete graph Γ with vertex set D. Define an equivalence relation ∼ (graph coloring) on the set of edges as follows: (a,b) ∼ (c,d) if and only if |ab| = |cd|. An automorphism of the coloured graph Γ is a permutation τ ∈ S_D such that (a,b) ∼ (a^τ,b^τ) for every edge (a,b). Is it true that the automorphism group of Γ is a subgroup of Aut(L)?

The statement is unstarred and has no editor or later comment on the rendered page. The local corpus contains Issue 20 only, not an Issue-21 JSONL record, so literal corpus flags are unavailable; the rendered Issue-21 source supplies the negative status evidence. No open-web or solution-bearing-history search was made because the canonical record marks this run blind.

### Clause matrix

| source clause | equivalent formulation | active scope? | stale evidence |
|---|---|---:|---|
| finite nonabelian simple L; D a conjugacy class of involutions | pair (L,D), with D one class and every element order 2 | yes | external check deferred |
| Γ is complete on D | every unordered distinct pair in D is an edge | yes | external check deferred |
| edges equivalent iff product orders agree | exact integer edge colour c({a,b}) = |ab| | yes | external check deferred |
| τ preserves equivalence for every edge | |ab| = |a^τ b^τ| for every a≠b | yes | external check deferred |
| ask Aut(Γ) ≤ Aut(L) | typed as every τ extending to an element of Stab_Aut(L)(D) | yes | external check deferred |

### Admissibility reconciliation

| constraint_id | source requirement | lane test |
|---|---|---|
| 21.52-forall-L-D | universal assertion over every admissible pair | one valid violating pair would refute; equality for PSU(3,3) is bounded only |
| 21.52-L-finite-nonabelian-simple | L finite, nonabelian, simple | verify for exact GAP object before colouring |
| 21.52-D-single-involution-class | D is one conjugacy class, all elements order 2 | inventory every conjugacy class and require uniqueness before choosing D |
| 21.52-Gamma-complete-on-D | every unordered pair of distinct D-elements | enumerate all binomial(|D|,2) pairs |
| 21.52-edge-colour-exact-product-order | colour is exactly |ab|, not product conjugacy class | compute `Order(D[i]*D[j])` for every i<j |
| 21.52-tau-preserves-all-edge-colours | candidate τ preserves every pair colour | exhaustive all-pair check on every colour-group generator and any separator |
| 21.52-tau-induced-by-AutL | compare against restriction image of setwise stabilizer in Aut(L) | unique D makes the stabilizer all of Aut(L); compute its exact induced image and compare groups |

No mismatch was found between the rendered statement and the seven canonical rows. Problem 21.53, unions of classes, uncoloured automorphisms, product conjugacy-class colours, and universal conclusions from a bounded equality remain excluded.

## Strategy portfolio

Ranked by expected information per active minute:

1. **Catalogue/fixed-case mode — exact U3(3) comparison.** Reconstruct Atlas/GAP `U3(3)` and independently construct `PSU(3,3)`; inventory every involution class; enumerate the unique class, its complete product-order matrix, the full colour group, and the restriction image of `AutomorphismGroup(L)`. A negative result proves only equality for this exact pair.
2. **Certificate mode — coloured incidence graph.** Encode each unordered pair as a degree-2 edge-vertex, partition edge-vertices by exact product order, and keep original D-vertices in a separate vertex-colour class. Nauty/GRAPE automorphisms restricted to D are exactly the full product-order colour group. Save matrix, generators, exhaustive checks, and hashes.
3. **Structured-construction mode — accidental twin/fibre permutations.** If full colour group is larger, extract a separating permutation and inspect equal coloured rows or coherent fibres that explain it. This is used only after an exact strict containment appears.
4. **Theoretical mode — rigidity from product-order relations.** If equality holds, inspect which colour relations already reconstruct the 63-point action, but do not treat this bounded equality as a universal proof.

Kill criteria: stop immediately if PSU(3,3) has more than one involution class; if the installed exact `AutomorphismGroup` or coloured-graph automorphism backend is unavailable; or if the frozen exact computation cannot be given a finite timeout and resource cap.

## Tooling gate

Observed locally: GAP 4.12.1, AtlasRep available, GRAPE available, `/usr/bin/dreadnaut` available. The general Digraphs/images packages are absent but not required. GRAPE supports graphs with explicit vertex colour classes and calls dreadnaut/nauty exactly.

## Exact group and involution inventory

At 2026-08-18T04:21Z the bounded 45-second inventory command was run:

```text
timeout --signal=TERM --kill-after=5s 45s gap -q -b Agents/Kourovka/problems/21.52/runs/2026-08-18-r8-psu33-full-colour-automorphism/scratch/psu33_inventory.g
```

It exited successfully in 2.6 seconds. AtlasRep's downloadable representation was unavailable (`AtlasGroup(...)=fail`), so the script used the installed primitive-group library's unique degree-28 group of order 6048, `PrimitiveGroup(28,4)`. GAP reported:

```text
L_SIZE=6048
L_DEGREE=28
L_IS_FINITE=true
L_IS_ABELIAN=false
L_IS_SIMPLE=true
L_CENTRE_SIZE=1
L_STRUCTURE=PSU(3,3)
PSU_SIZE=6048
PSU_IS_SIMPLE=true
PSU_STRUCTURE=PSU(3,3)
ATLAS_ISOMORPHIC_TO_PSU33=true
CLASS_COUNT=14
INVOLUTION_CLASS_COUNT=1
INVOLUTION_CLASS_SIZES=[ 63 ]
```

The full class inventory, including representative order, class size, and centralizer order for all 14 classes, is in `Agents/Kourovka/problems/21.52/runs/2026-08-18-r8-psu33-full-colour-automorphism/scratch/psu33-inventory-output.txt`. There is exactly one involution class, of size 63 and centralizer order 96, so the assignment's uniqueness gate passes.

## Frozen heavy-computation plan

- Checker: `Agents/Kourovka/problems/21.52/runs/2026-08-18-r8-psu33-full-colour-automorphism/scratch/psu33_full_colour_checker.g`
- Frozen SHA-256: superseded by the clean-run relocation hash recorded below.
- Size: 215 lines, 8870 bytes.
- Exact command: superseded by the clean-run relocation command recorded below.
- Wall cap: 900 seconds plus 10-second forced-kill grace; lease requested for 20 wall-clock minutes.
- Estimate: one CPU core; under 1 GB RAM. Largest graph has 2016 vertices and 3906 undirected incidence edges; group has order 6048 and involution class size 63.
- Output paths: `psu33-full-colour-output.txt`, `psu33-full-colour-resource.txt`, `psu33-colour-matrix.g`, and `psu33-full-colour-certificate.g`, all under the clean run's `scratch/` directory.
- Exact tasks: repeat identity/simplicity/all-class inventory; enumerate all 1953 edges; compute the full colour group through a vertex-coloured incidence graph with nauty; compute full `AutomorphismGroup(L)` and its restriction image; compare exactly; check every edge for every reported generator and any separator.

- 2026-08-18T04:25:46Z — checker frozen and lease request prepared; cumulative active minutes: 123. Heavy computation not started.

### Clean-run relocation correction

The roster's clean `run_dir` was then applied before any heavy invocation. No old-scope mathematical artifact was opened. The corrected frozen checker is 215 lines / 9020 bytes at:

`Agents/Kourovka/problems/21.52/runs/2026-08-18-r8-psu33-full-colour-automorphism/scratch/psu33_full_colour_checker.g`

Corrected frozen SHA-256:

`6edc8d875afd5f16efa528373ef4e87b1a086117533c1cc49491174e9f461dc9`

Corrected exact command:

```text
/usr/bin/time -v -o Agents/Kourovka/problems/21.52/runs/2026-08-18-r8-psu33-full-colour-automorphism/scratch/psu33-full-colour-resource.txt timeout --signal=TERM --kill-after=10s 900s gap -q -b Agents/Kourovka/problems/21.52/runs/2026-08-18-r8-psu33-full-colour-automorphism/scratch/psu33_full_colour_checker.g
```

The earlier top-level-path request is superseded and must not be run.

- 2026-08-18T04:27:45Z — clean relocation/refreeze complete; cumulative active minutes: 125. Heavy computation still not started.

## Lease rejection and second refreeze

At 2026-08-18T04:27:51Z Lead rejected the superseded top-level-path request because its path/hash did not identify the relocated checker and because stdout/stderr and terminal-sentinel acceptance gates were not frozen. No compute slot was allocated and the command was not run.

The actual clean-run artifacts were then refrozen with fail-fast gates:

- Checker SHA-256 `86e2633dff9c8f5ec25c3ee7beb5ce21b8e2e3a957e26f550874b3e154843208`, 215 lines / 9024 bytes.
- Runner SHA-256 `45d8fc5f96cf61482efb3674994f83fa476dbc6068b7ca5f931ec221911a0634`, 68 lines / 2445 bytes; `bash -n` passed.
- Complete manifest: `Agents/Kourovka/problems/21.52/runs/2026-08-18-r8-psu33-full-colour-automorphism/manifest.md`.
- Manifest SHA-256: `40ca661d0f9fa3d049b6de6d53f713a0d230bd5c50acc31361044cb86feb1af3` (69 lines / 3258 bytes).
- Fresh exact command: `bash Agents/Kourovka/problems/21.52/runs/2026-08-18-r8-psu33-full-colour-automorphism/scratch/psu33_full_colour_run.sh`.
- Runner prechecks its checker hash and output absence; captures stdout/stderr/resource reports; enforces nonzero/timeout/stderr/missing-output/`=FAIL` rejection; and requires `PSU33_FULL_COLOUR_CHECKER_SUCCESS` as the terminal stdout and GAP-log line.

- 2026-08-18T04:31Z — complete second manifest frozen; cumulative active minutes: 128. Heavy computation still not started.

At 2026-08-18T04:32:00Z Lead's response to the earlier correction additionally required GAP `--quitonbreak`. The runner was patched before any heavy invocation, the option was checked in a zero-work GAP exit, and all hashes were refrozen:

- Checker: `86e2633dff9c8f5ec25c3ee7beb5ce21b8e2e3a957e26f550874b3e154843208` (unchanged).
- Runner: `fc2fccac609c076e15d6168110e2f69f6340893e9b0d9c2e03d91970eee572e0` (68 lines / 2459 bytes).
- Manifest: `338d83d91f5847e9758cf15336ce383b5db5ecb5be84b3d1ba9180e43cd8fb8a` (69 lines / 3392 bytes).
- Internal bounded invocation now uses `gap --quitonbreak -q -b`.
- All six listed heavy outputs were rechecked absent at 2026-08-18T04:34:44Z.

- 2026-08-18T04:34:44Z — definitive manifest refrozen; cumulative active minutes: 131. Heavy computation not started.

## Sole leased run and outcome

Lead granted slot 1 through 2026-08-18T04:57:24Z for exactly one invocation of the definitive runner. At 2026-08-18T04:39Z the exact authorized command was run once:

```text
bash Agents/Kourovka/problems/21.52/runs/2026-08-18-r8-psu33-full-colour-automorphism/scratch/psu33_full_colour_run.sh
```

Observed terminal wrapper output:

```text
RUNNER_ACCEPTED_PSU33_FULL_COLOUR_CHECKER
```

No patch, rerun, alternate group, expanded class, or second heavy command occurred.

All 26 named checks passed. The exact terminal sentinel is present in both stdout and the GAP log; stderr is empty; every required output is nonempty. `/usr/bin/time -v` records exit 0, elapsed 2.59 seconds, user CPU 2.02 seconds, system CPU 0.34 seconds, and maximum RSS 142208 KiB.

Exact fixed-pair result:

```text
L_STRUCTURE=PSU(3,3)
L_SIZE=6048
INVOLUTION_CLASS_COUNT=1
INVOLUTION_CLASS_SIZES=[ 63 ]
EDGE_COUNT=1953
PRODUCT_ORDER_COLOURS=[ 2, 3, 4 ]
EDGE_COUNTS_BY_ORDER=[ [ 2, 189 ], [ 3, 1008 ], [ 4, 756 ] ]
INCIDENCE_AUT_ORDER=12096
COLOUR_GROUP_ORDER=12096
AUT_L_ORDER=12096
AUT_L_RESTRICTION_IMAGE_ORDER=12096
STRICT_CONTAINMENT=false
GROUPS_EQUAL=true
CHECK BOUNDED_GROUP_EQUALITY=PASS
NO_SEPARATOR_BECAUSE_GROUPS_EQUAL
PSU33_FULL_COLOUR_CHECKER_SUCCESS
```

Output hashes:

```text
053658d829015e9a0addb12eedc363ba43e1d35653041755de7c8ac1ea8c7238  psu33-full-colour-stdout.txt
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  psu33-full-colour-stderr.txt
193e9df39e6630abbd68b12d6f5546369cb2bd99640d49d9c0cba97e65930aba  psu33-full-colour-resource.txt
053658d829015e9a0addb12eedc363ba43e1d35653041755de7c8ac1ea8c7238  psu33-full-colour-output.txt
59ef40bb4d41015243a77914badfd8e851c2a6fc0a09d451b7fa0f5312b5b287  psu33-colour-matrix.g
097452a47e77d62d984b556e5afda7754b63d4a90356f5f7141d5db3ef925976  psu33-full-colour-certificate.g
```

At 2026-08-18T04:40Z a `REPORT` requested immediate slot release and identified the result as bounded equality only.

## Outcome

`PARTIAL_RESULT`: the full colour group equals the `Aut(PSU(3,3))` restriction image on the unique involution class, both of order 12096. This excludes exactly this fixed pair as a counterexample and does not answer the universal scope. Detailed evidence is in `findings.md`.

The strategy `PSU33-FULL-COLOUR-AUTOMORPHISM` has met its fixed-target completion criterion. Await Lead decision; do not self-park or choose a replacement target.

- 2026-08-18T04:42Z — run, inspection, immediate release report, findings, and bounded outcome complete; cumulative active minutes: 134. Charged increment: 18 minutes. Waiting time for leases excluded.

Lead independently matched every output hash and acceptance gate and confirmed slot 1 released. Final charge for this increment is exactly 18 active minutes (`116 -> 134`); 27 of the authorized 45 minutes are returned unused. The outcome occurred before the 30-active-minute checkpoint threshold, so no artificial checkpoint time was added. State: `awaiting_lead`; no replacement target selected or begun.

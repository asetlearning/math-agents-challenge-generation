---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-tables
  - project/kourovka
  - status/draft
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
direction: counterexample
cycle: 12
strategy: SIX-A7-DIRECT-SOURCE-PREDICATE
---

# Problem 20.115 — cycle 12 direct `6.A7` table audit

## 2026-08-18T04:50:41Z — active work start

- Detailed cumulative active time at start: `02:08:01`.
- This increment may charge at most `00:35:00`.
- Exact target: the ordinary irreducible character table with installed identifier
  `6.A7`, but only after its identity and order are certified. No substitute cover,
  neighbouring table, or catalogue is authorized.
- Fresh-context discipline: no historical run log, finding, verification note, or
  solution-bearing artifact was opened. The canonical scope, current roster,
  binding Lead decision, source PDF, and installed-package metadata are the only
  substantive inputs.

## Source and staleness gate

- Source PDF resolved through `_meta/agents/Kourovka/paths.env` and rendered page
  161 was visually inspected at 150 dpi.
- Corrected transcription: Let `chi` be a complex irreducible character of a
  finite group `G`. If `chi(x) != 0` for some `x in G`, must the order `o(x)` of
  `x` divide `|G|/chi(1)`? The source then records the solvable case and the weaker
  universal bound `(o(x)chi(1))^4 | |G|^5` as context only.
- `source_transcription_checked: yes`.
- Corpus flags from `kourovka-20-corpus.jsonl`: `answered: false`,
  `has_editor_comment: false`, `has_later_comment: false`.
- `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`.
- Clause matrix: source question `c-question` is the active scope; the solvable
  statement `c-solvable-context` and fourth-power bound `c-general-bound-context`
  are context and excluded. `active_scope_checked: yes`.
- Scope reconciliation: all and only
  `20.115-forall-G-chi-x`, `20.115-G-finite`,
  `20.115-chi-complex-irreducible`, `20.115-x-in-G`,
  `20.115-character-value-nonzero`, and
  `20.115-order-degree-divisibility` are required. No mismatch was found.

## Strategy portfolio

1. **Catalogue/small-case mode — selected.** Load exactly the installed ordinary
   table identifier `6.A7`; certify identifier and group order, row/class
   completeness, ordinary irreducibility, class names and exact class orders; then
   audit every row/class cell with GAP's exact cyclotomic equality and integer
   divisibility. A miss excludes only this one table.
2. **Structured-construction mode — not authorized this cycle.** A designed central
   extension or explicit matrix model could independently reconstruct a hit, but
   no such search or expansion beyond `6.A7` is permitted.
3. **Theoretical mode.** Use character orthogonality and the table's structural
   metadata only as internal completeness/identity checks. These checks cannot turn
   a zero-hit table scan into a universal proof.
4. **Certificate plan.** Preserve software/package versions, installed table
   identifier, order, all class names/orders, all degrees, row count, class count,
   exact nonzero count, and each failed tuple. Any hit must include exact GAP
   cyclotomic value and the arithmetic remainder. Validator can independently
   replay the frozen checker against CTblLib and compare its hash.

## 2026-08-18T04:54:01Z — frozen checker; compute-lease wait

- Installed static metadata identifies `6.A7` without substituting a cover:
  AtlasRep maps group name `6.A7` to ATLAS alias `6A7` and order `15120`, while
  the installed CTblLib manual lists `6.A7` as the common central extension built
  from `A7`, `2.A7`, and `3.A7`.
- Frozen exact checker SHA-256:
  `d1621a51b80d33391102122db9ae912b9e9976a4454f13de223921b8159827d2`.
- The checker has pre-scan identity, central-quotient, ordinary-table,
  irreducibility, orthogonality, row/class-shape, and class-size gates. It will
  emit every audited cell, not merely a summary.
- Requested one five-minute compute lease for a sole 45-second-timeout GAP
  invocation. No computation has been launched.
- Active stop: `2026-08-18T04:54:01Z`; charged `00:06:11`; detailed cumulative
  active time `02:14:12`. Compute-queue waiting is uncharged.

## 2026-08-18T04:56:00Z--04:58:58Z — lease rejection repaired

- Lead allocated no slot and rejected the first manifest because its command
  merged diagnostics/resource data, lacked `--quitonbreak`, omitted the TSV from
  the frozen absence list, and had no exact unique final sentinel.
- Preserved the mathematical audit logic and refroze a definitive checker plus
  shell runner. The runner enforces distinct outputs, hash and absence prechecks,
  zero exit, empty stderr, explicit identity/ordinary/irreducibility/completeness
  gates, exact full-grid TSV reconciliation, final-status consistency, and a unique
  sentinel as the final stdout line.
- New hashes and exact acceptance gates are in `compute-manifest-v2.md`; a fresh
  five-minute lease was requested. No GAP computation has occurred.
- Active stop: `2026-08-18T04:58:58Z`; charged this segment `00:02:58`; detailed
  cumulative active time `02:17:10`. Lease waiting is uncharged.

## 2026-08-18T05:02:17Z--05:03:38Z — sole leased invocation rejected

- Lead granted slot 2 through `05:07:17Z` for exactly one definitive invocation.
- Ran the frozen command once. GAP exited zero and emitted all named identity,
  ordinary-table, row/class, irreducibility, orthogonality, coverage, status, and
  terminal-sentinel records; however, the wrapper rejected the artifact with
  `RUNNER_REJECTED: TSV line count mismatch`.
- TSV has 1,602 lines against 1,600 cells plus one header. Therefore the frozen
  certificate is not accepted even though stdout reports 1,044 exact nonzero cells
  and zero violations. No bounded result or counterexample claim is made from this
  rejected run.
- All four hashes and resources were reported to Lead with an immediate slot-2
  release request. No patch or rerun occurred.
- Active stop: `2026-08-18T05:03:38Z`; charged this segment `00:01:21`; detailed
  cumulative active time `02:18:31`.

## 2026-08-18T05:03:38Z--05:05:50Z — immutable-artifact diagnosis

- Read-only inspection localized the wrapper rejection entirely to the TSV header:
  GAP line wrapping split `group_order` after `group_orde\\`. The two physical
  lines reconstruct the exact frozen header; data begin at physical line 3.
- A hash-pinned shell/awk verifier, SHA-256
  `02412b23fa4ff5c17bfba4dbc681df8081c11dd676126af1c078e190e6ba8186`,
  did not invoke GAP or mutate an output. It passed all 1,600 intact eleven-field
  data rows, every key in the `40 x 40` Cartesian grid, value/zero flags, product
  and remainder arithmetic, class consistency, and summary counts: 1,044 exact
  nonzero values, 556 zeros, zero violations.
- Reported the salvage transparently to Lead and recommended fresh Validator review
  of the immutable artifacts rather than spending a second GAP invocation.
- Active stop: `2026-08-18T05:05:50Z`; charged `00:02:12`; detailed cumulative
  active time `02:20:43`.

## 2026-08-18T05:06:00Z--05:11:55Z — final packaging and handoff

- Lead first released slot 2, classified v2 `FAILED_RUN_NO_RESULT`, and authorized
  a format-only v3 refreeze. New v3 checker/runner/manifest files were drafted with
  only `SizeScreen`, new paths, and versioned sentinel changes; no v3 lease was
  requested and no v3 computation occurred.
- A newer Lead decision superseded that authorization, prohibited a rerun, and
  accepted only the immutable hash-pinned posthoc audit as a candidate bounded
  partial for review.
- Wrote `findings.md` as `status/conjectured`, outcome `PARTIAL_RESULT`, with exact
  table identity, group order, all 40 class names/orders, all 40 degrees, every
  canonical constraint row, exact command, resources, hashes, wrapper rejection,
  header diagnosis, posthoc transcript, limitations, and error modes.
- Sent the complete candidate to a fresh Validator and reported outcome to Lead.
  The authorized one-table strategy is exhausted at its exact boundary; state is
  `awaiting_lead` pending review.
- Active stop: `2026-08-18T05:11:55Z`; charged this segment `00:05:55`; detailed
  cumulative active time `02:26:38`. Total cycle-12 charge: `00:18:37` of
  `00:35:00`.

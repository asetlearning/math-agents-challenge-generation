---
title: BRG4 hit classifier — pre-registration
domain: group-theory
project: b25
instance: B(2,5)
status: pending
author: maumayma
date: 2026-08-09
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, project/b25, status/pending, experiment]
---

# BRG4 hit classifier — pre-registration

**PRE-REGISTERED, NOT RUN.** Routed to Math-expert + Validator; runs on their
acceptance, no further Lead round-trip (Lead GO 2026-08-09).

**Authority:** [[brg4-hit-classifier-spec-2026-08-07]] as amended (read at
mtime Aug 7 20:58), Validator amendments incorporated. Bucket names are the
**amended** ones; no earlier bucket naming is used anywhere below.

**Scope guard, from the spec:** this classifier does **not** certify BRG4 and
does **not** alter rung-4 status. It sorts bounded triangular-screen hits into
disposal buckets and identifies the genuine remainder BRS4 must bound.

## Input (verified present)

`.maestri/roles/8f9f252e…/brg4_bounded_triangular_screen_v03_receipts_20260807T/brg4_screen_20260807T125313Z.json`
(248,823,480 B), schema `bounded_triangular_witness_screen_v0.3`,
`prereg_sha256 432584fabca7…`.

Census to reconcile exactly: **153,776 hits** · 800 arc descriptors (680 long /
120 short) · 510,272,000 ordered screen triples · 435,200,000 anchored triples ·
49 radius-3 `G_3` connectors · spur rejections 242,525,360 · same-arc-slot
rejections 491,440 · `coverage_complete=true` · `brg4_collapse_claim=false`.

Per-hit fields available: `gamma_1..3` = `{arc_id, root, orientation, start,
raw_length, word}`; connectors `c_1..c_3`; `per_cell[]` =
`{cell_slot, intervals_toward_cells, intervals_toward_regions,
total_internal_interval_count, max_single_interval_length,
sum_of_internal_raw_lengths}`; `left_nf`, `inverse_right_nf`, `equation_word`,
`closure_equal`, `record_id`.

## FLAG (a) — B2-via-region discriminator: RESOLVED BY MEASUREMENT

Lead asked me to check whether v0.3 carries the connector/phase data needed to
separate direct cell-to-cell from region-mediated, and to pre-register a
conservative default if it does not. **It does carry the data, and the answer is
determinate — so the conservative default is not needed.**

Root, orientation and start are present per gamma (phase is therefore
derivable), and `per_cell` carries the decisive pair. Measured over **all
153,776 hits / 461,328 per-cell slots**:

```
(intervals_toward_cells, intervals_toward_regions) distribution:
    {(0, 1): 461328}        -- uniform, no other value occurs
```

Every registered interval is region-facing; **`intervals_toward_cells` is 0
everywhere**. Consequently:

- **`B2-direct` is EMPTY on this domain — by measurement, not by default.**
  The v0.3 triangular screen registers only region-facing intervals, so a
  direct cell-to-cell same-period contact cannot appear in it.
- All **8,328** same-period hits (all three gammas on one root class) are
  `B2-via-region` and **route to B6** per the amendment.

**Labelling required by the flag, restated precisely:** the resulting B6
inflation is *not* sound-but-conservative padding from missing data. It is a
structural property of the registered domain. The honest statement is
**"B2-direct is inapplicable to the v0.3 domain"**, not "B2-direct could not be
decided". If a later screen registers cell-facing intervals, B2-direct becomes
live and these 8,328 must be reclassified — recorded here so that reclassification
is expected rather than surprising.

Period-pattern census (full 153,776): same-period **8,328**; the remainder
splits two-root / three-root (exact counts emitted in the run).

## FLAG (b) — B4-pending nonzero BY CONSTRUCTION

`per_cell.cell_slot` takes values 1,2,3 — an **abstract slot index, not a
physical cell id**. No physical-cell aggregation pass exists, so
`total_internal_interval_count` cannot be summed per physical shell cell, which
is exactly what B4's Greendlinger ≤3-interval budget requires.

Therefore **`B4-pending > 0` is guaranteed before the run**, and
**`fallback = 0` is unreachable in this pass by construction.** This is the same
shape as the O1 `unresolved = 0` finding: a spec acceptance criterion that no
amount of compute reaches with the available inputs. Pre-registered so the
output is not misread as a classifier failure.

Per the amendment, `B4-pending` counts as **unclassified for `fallback=0`** and
is **never** labelled provisionally harmless.

## Buckets (amended names, exact precedence B0 → B7)

- **B0** generator-invalid / already-filtered.
- **B1 `literally-LR3-deletable`** — cyclic `W` and `W⁻¹`, free reduction,
  breadth-first **strictly length-decreasing** literal deletion of `s^{±5}` for
  primitive cyclically reduced `|s| ≤ 3`. **Label only, no disposal power**;
  counts as **not-yet-disposed** for any `fallback=0`. Not a complete
  lower-rank test (a lower-rank explanation may need a length-increasing
  intermediate). Record `LR3_deletion_count` + certificate shape. **No inference
  that non-B1 records need deep `G_3` structure.**
  Fixtures (must pass before the run counts): v0.2 `W-BRG4-0`
  `AAAABBbbA → AAAAA → empty` via length-1 root `A`; v0.3 record 0
  `AAABBBBBAA` ⊃ `BBBBB` → `AAAAA` → empty.
- **B2-direct** — expected empty, see flag (a); requires a named
  area/ledger-decreasing move to contribute no genuine term.
  **B2-via-region** — demotes to **B6**.
- **B3** — **distinct-period** pairwise realized contacts, length **≤ 3**,
  backed by Validator's computed receipt. **No same-period region-mediated
  inheritance.** Certificate names the pair, the `G_3` equality, and the prior
  ledger bucket consumed. No silent merging of three-sided relations into
  pairwise contacts.
- **B4-pending** — see flag (b). Unclassified, never harmless.
- **B5** — boundary-exposure-through-base; realizes exposure rather than
  consuming it; routes to strict-arc boundary query. Expected empty on an
  internal-triple domain, retained in the family.
- **B6** — genuine base-interface term / re-derivation required. Preserves all
  hit descriptors and connectors, root/orientation/start/length pattern, cyclic
  word + `G_3` NF certificate, per-slot interval lengths and counts,
  period-pattern class, LR3 residual, whether any interval has raw length ≥ 4,
  and whether the pattern can repeat on one physical shell cell.
- **B7** — checker gap. **`B7 = 0` required** before any composition consumes
  the classifier.

Exactly one primary bucket per hit by the precedence order, **all secondary
flags recorded**, and a **reverse index** from every bucketed normal form /
word-pattern certificate back to all geometric hit records.

## Acceptance

Totals reconcile to 153,776 exactly, each hit in exactly one primary bucket;
`B7 = 0`; B1 fixtures pass; reverse index complete and invertible; per-bucket
counts, hashes, and deterministic conventions emitted. `fallback = 0` is
**not** claimed — see flag (b).

## Resource estimate

Pure Python over a 249 MB JSON; single pass plus per-bucket certificate
construction. **Minutes**, single-threaded, no additional CPU slot.

## Anti-pattern check

Not tuning on the scored set (buckets are externally specified); no bucket is
chosen to make a total come out; B1 and B4-pending are both carried as
not-disposed so `fallback=0` cannot be reached by parking; misses reported with
hits; no directional interpretation of B7.

## Not claimed

No BRG4 certification, no change to rung-4 status, no positivity, no route
conclusion.

## Gate status

- **Math-expert: ACCEPTED** 2026-08-09 — conformance to the amended B0–B7 spec.
  Confirmed on review: B1 label-only and not disposal; B2-direct measured
  inapplicable on v0.3 (all 461,328 intervals region-facing, same-period
  via-region → B6); B3 distinct-period only; B4-pending explicitly
  non-disposing with `fallback=0` unreachable by construction; `B7=0` still
  required; no BRG4 or rung-4 status claim.
  Explicitly **prereg acceptance, not a math theorem verdict**.
- **Validator: ACCEPTED with amendments** 2026-08-09, pasted below verbatim and
  in force before the run. Validator affirmed **`B7=0` is a classifier-
  completeness check, not BRG4 evidence**. No BRG4 certification, no rung-4
  status change; rung 4 remains proven-flagged **scoped to BRG4**.

### Validator amendment 1 — physical aggregation is not post-processing

Since v0.3 has abstract slots only, a later **cell-level generator** must create
aggregatable physical-cell objects. Anyone planning "run classifier, then
aggregate" will find **nothing to aggregate**. The aggregation pass is a
generator obligation, not a downstream step over these receipts.

### Validator amendment 2 — the 8,328 are a quantified B2-via-region debt

With `B2-direct` empty, the accepted rung-4 same-period machinery gives **zero
coverage on this domain**. Each of the **8,328** same-period region-mediated
hits needs **re-derivation**. This is a quantified debt, not a disposal.

### Validator amendment 3 — two-phase labelling, matching O1

- **Classifier-prereg** (this pass): pending allowed; does **not** claim
  `fallback = 0`.
- **Classifier-final**: requires the cell-level generator, with
  **`B4-pending = 0`**.

## Status

`#status/pending` — **both gates closed, amendments in force. Running as
Classifier-prereg.**

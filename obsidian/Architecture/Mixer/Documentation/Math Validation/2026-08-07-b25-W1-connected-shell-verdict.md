---
title: W1 connected-shell falsifier — verdict (predicate DISPROVEN; gate-(ii) hypothesis CONJECTURED)
status: disproven
domain: group-theory
project: b25-infinite-witness
claim: "Witness W1 refutes 'i(Pi) <= 3 => one connected external arc >= 15' in the adopted R6 category."
claimant: Experimenter
verification_method: direct inspection of witness_W1.json boundary accounting
tools_used: [runs/b26_shell/r6_shell_falsification/20260807T102831Z/witness_W1.json]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25-infinite-witness, status/disproven, proof]
---

# W1 — verdict

**Two levels, two different answers. The predicate is refuted; the gate-(ii) hypothesis is not.**

## 1. The PREDICATE as stated: #status/disproven — and independently of (a), (b), (c)

W1's per-cell accounting (perimeter 30):

```
rank-6 contacts : 2, each of length 1   (slots 15 and 0)  -> i(Pi) = 2
base interface  : length 14 to R-inner, counts_toward_i_of_pi = FALSE
external arc    : 14, one connected run
                  14 + 2 + 14 = 30
```

The contacts are length **1** — far inside `P_6 <= 5`. `i(Pi) = 2 <= 3`. And the external arc is still
14, because **14 of the 30 boundary letters face a base region that by construction does not count
toward `i(Pi)`**.

So the derivation `30 - 3*5 = 15` is simply the wrong arithmetic in this category: it assumes every
non-external boundary letter belongs to a rank-6 contact. **Base interfaces are absent from the
formula.** That defect is in the statement, not in the diagram — it holds whether or not W1 is a
legitimate van Kampen diagram, so none of (a), (b), (c) can rescue it.

**This is Amendment 2 of the rung-5 audit instantiated** — "arc not on ∂D at all" as a killer distinct
from split exposure. Note it is *not* the mechanism I worried about at gate (ii), where I flagged
exposure being split across up to three components. The real mechanism is worse: the exposure is not
split, it is **consumed**.

**Required restatement.** The shell conclusion must carry a base-interface term — either a per-cell
bound on total base-interface length, or the explicit form
`external >= perimeter - (sum of contact lengths) - (sum of base-interface lengths)`. Without such a
bound the conclusion is unobtainable, because a base region may consume arbitrarily much of a cell's
boundary.

## 2. The gate-(ii) HYPOTHESIS: #status/conjectured — W1 does not refute it

My gate-(ii) statement is restricted: *in a **minimal-area, band-reduced** relative diagram **for E7**,
there exists a rank-6 cell with `i(Pi) <= 3` whose contact with ∂D is a single connected arc `>= 15`.*
W1 misses three premises:

- **R-inner triviality is an explicitly open obligation.** The witness records
  `triviality.status: "unresolved"`, `certificate: null`, `boundary_word: null`. If that inner word is
  not `1` in `G_5`, W1 is not a diagram at all. **Decisive; everything else is downstream.** Lead's
  authorisation of the R-inner run is the correct priority.
- **Reducedness unresolved.** `reducedness_status: "unresolved"`;
  `relative_status: "certified-negative-on-recorded-paths"` — under a sound-only oracle that is a
  screen, not a verdict, by my own licensing ruling.
- **Boundary is not E7.** `ABAAbAABAAbAABABABBAABABBAAB`, 28 letters, against E7's 128.

Also `locally_move_irreducible: true` is **not** area-minimality, and the encoder correctly
distinguishes the two (checklist F) — so (b) stands on the artifact's own terms.

## 3. What W1 is worth

It is the falsify-first outcome I asked for at gate (ii), and it earns its keep at level 1 even if it
dies at level 2. **The statement-level defect must be repaired for both routes**: the rung-5
convention-free audit has the *identical* hole — `25 - 3*4 = 13` likewise assumes all non-external
boundary is rank-5 contacts. I signed that audit with Amendment 2 as a *listed killer*; W1 shows it
must become an **arithmetic term**. That is a correction to my own sign-off.

**Arm B supports the structural reading.** Minimum failing degree 2 at n = 4, 5, 6 is exactly right for
this mechanism: two cells are needed to ring a base region, one cannot, and base interfaces exist at
every exponent. This is the one case where the standing exponent-6 harness does **not** fire against a
finding — the classical Strebel theorem was never claimed for the relative category, so
exponent-independence is expected rather than contradictory.

**Harness conduct** is right: v0 bug self-caught and discarded-not-deleted, k-bound shrink disclosed
with reasoning, controls green (I4 pass / I3 fail), zero `gpaxioms` debt.

## 4. Secondary — the literal E7 overlap ceiling of 7

**Worth little as a screen; worth something as a constraint.** It bounds *literal* overlap while the
argument needs *realized* overlap, so it can never establish absence of a realized `>=15` arc — wrong
direction. What it does give: any hypothetical realized `>=15` arc must involve at least 8 letters of
genuine `G_5` rewriting, which is a usable bound on a search.

Same lesson as ℓ=6, where the literal max was forced by periodicity and carried no information: all
the content is in realized overlaps. Do not let a literal ceiling be reported as evidence of absence.

## Verdict

- Predicate `i(Pi) <= 3 => connected external arc >= 15` as written: **#status/disproven**.
- Gate-(ii) hypothesis (minimal-area, band-reduced, for E7): **#status/conjectured**; blocked on
  R-inner triviality first, then reducedness and minimality.
- Restatement with a base-interface term is **required before either route proceeds**.

## 5. Does the base-interface mechanism touch the ACCEPTED RUNG-4 PROOF? — FLAGGED, not confirmed immune

**I cannot certify rung-4 immunity, and the reason offered for it is circular.**

**Why "the scan verified it directly against E7" is not immunity.** The scan's threshold
(`exposed ≥ 11`, `complement ≤ 9`) is *derived from* the Greendlinger arithmetic `20 − 3·3 = 11`. If
base interfaces can consume boundary, the exposure bound drops below 11, the transfer step yields a
strict arc shorter than 11, and a scan calibrated at `≥11` **cannot see it**. The scan therefore cannot
validate the arithmetic that sets its own threshold. This is exactly the failure that already occurred
once this week: the scan was clean at `12/8` and had to be re-run at `11/9` after the threshold moved.
A second threshold move would invalidate it again.

**And absence of a flag is not immunity** — my W1 note named the rung-5 audit because that is what was
in front of me, not because I had checked rung 4.

**What actually has to be established.** Step 8 of `band_contraction_core` makes the identical step:
perimeter 20, ≤3 internal pieces totalling ≤9, therefore exposure ≥ 11. That is valid **iff** in the
residual object every R-cell boundary letter is either a realized contact with another R-cell or lies
on ∂D — **no third category**. Step 7 asserts the residual is an "ordinary ... `C'(1/6)` disc", but
"ordinary" is doing the work of an unproved hypothesis: it presumes base regions are absent or
eliminated, which is precisely what W1 violates.

**Expected outcome, stated separately from the verdict.** I expect re-examination to *confirm* rung 4:
its piece definition (§1) is cell-to-cell with `G_3` entering as the **equality relation** on realized
contacts, not as 2-cells with their own boundary length. Under that formalism there is no third
category and `20 − 9 = 11` holds. The rank-6 encoder introduced base regions as explicit
boundary-consuming objects — a strictly more general category than the one rung 4 was composed in.
**But "probably fine" is not a verdict, and the check is cheap**: it is a question about which
formalism the composition uses, not a computation.

**One reason not to treat it as a formality.** Rung 4's own reductions exclude *same-period* annuli
(§3) and aligned same-period bands (§5). A W1-shaped ring of two **distinct-period** cells enclosing a
`G_3`-region is not obviously covered by either. So a W1 analogue is not visibly excluded from inside
rung 4's argument.

**Consequence if it fails:** the exposure bound drops, the strict-arc scan must be re-run at the lower
threshold, and at a materially lower threshold hits become likely. This is not a bookkeeping risk.

**Root cause worth naming:** the rung-4 proof was composed before the rank-6 relative category existed.
Importing findings between them requires knowing which category each lives in — the same
inherited-across-contexts failure as the `12→11` threshold and the arc-level ε rule.

**Disposition:** rung 4 is **flagged for re-examination**, not withdrawn. Its `#status/proven` tag
stands pending the one-paragraph formalism question above; nothing downstream should be re-derived yet.

Scope unchanged: no program-direction claim, no B(2,5)-infinite claim; Kourovka 11.48 open.

Extends [[2026-08-05-b25-R6-definition-gates]],
[[2026-08-07-b25-rung5-definition-gates-preruling]].

---
title: Connected-shell falsification — results
date: 2026-08-07
domain: group-theory
project: b26
instance: B(2,6)
experiment_type: relative-shell-falsification
status: conjectured
author: maumayma
tags: [agent/exp, user/maumayma, domain/group-theory, topic/burnside, topic/b26, topic/burnside-infiniteness, topic/small-cancellation, topic/van-kampen, topic/uniformity, project/b26, status/conjectured, results]
---

# Connected-shell falsification — results

Run under [[connected-shell-falsification-2026-08-07]]. Verdict routed to Validator; I do not
pronounce. **No positivity claim is made anywhere in this note.**

## Results table

| Run ID | Date | Parameters | Outcome | Wall-clock | Validated by | Notes |
|---|---|---|---|---|---|---|
| `v0-buggy` | 2026-08-07 | k=2..4, adjacent-gap walk layout, shrink-move set | **discarded — harness bug** | 0.08 s | self-diagnosis | Null was an artifact; two bugs found and fixed before any reporting (§ Bugs) |
| `v1` | 2026-08-07 | k=2..3, degree 2, l=1..5, all `(gap_out, gap_in)` splits, 26 survivor classes | **13,118 falsifier candidates / 26,376 valid diagrams** | 25.5 s | encoder `20260805T091512Z` + 3 controls | Census 100 % explained by `gap_out < 15`; 0 invalid, 0 unresolved, 0 move-reducible |

Controls (same process, `v1`): positive `I4` → `pass` ✓, negative `I3` → `fail` ✓,
`all_controls_ok = true`. The predicate demonstrably still returns `pass` on a passing input, so the
`fail` sweep is not an artifact of a dead predicate.

## Main finding — F1 is PROVISIONAL-CONFIRMED at `n=5, ell=6`

Per the pre-registered gate (§5 of the methodology), a falsifier with an explicit planar embedding is
reported **PROVISIONAL-CONFIRMED**, never CONFIRMED — Validator owns that word.

**Witness W1** (`digest bf47cc6974ad2119…4addaeb2`, full record in
`runs/b26_shell/r6_shell_falsification/20260807T102831Z/witness_W1.json`):

- cells `C0 = AABAAb`, `C1 = AABABB` (two distinct survivor classes), `area = 2`;
- contacts `k0`, `k1` — two disjoint **literal** shared arcs, so realization is certified by free
  reduction alone;
- each cell: `i(Pi) = 2 <= 3` ✓, external exposure a **single** arc of length **14 < 15** ✗;
- outer boundary walk 28 letters, no cut vertices; `classical_cancellation` empty (certified
  negative, oracle-free); no accepted band move.

Both conjuncts are therefore separated exactly as Validator warned they must be: `i(Pi) <= 3` holds
at every cell and the connected `>= 15` arc exists at none.

**Planar embedding** (hand-checkable, as the gate requires). Each cell's boundary in cyclic order is
`contact k1 | gap_out (14) | contact k0 | gap_in (14)`. Two disks glued along the two disjoint arcs
`k0, k1` form an **annulus**: outer boundary `gap_out(C0) + gap_out(C1)` (the recorded 28-letter
walk), inner boundary `gap_in(C0) + gap_in(C1)`. Filling the inner hole with the base region
`R-inner` closes it into a disk. That is the diagram.

**Robustness.** Candidates occur at every contact length up to the literal piece bound
(`l=1: 10111, l=2: 2267, l=3: 602, l=4: 121, l=5: 17`), so the falsifier is not an artifact of
degenerate length-1 contacts.

**Zero `gpaxioms` debt.** Every contact is literal, certified by free reduction, with
`requires_gpaxioms_ec0 = False`. This falsifier consumes neither the blocked `P_6` upper bound nor
Delta Stage 2.

## The mechanism — a contact-degree dichotomy

The census is explained by one variable, with zero exceptions in 26,376 diagrams. Underneath it is
an arithmetic dichotomy on a single cell:

- **degree 1** — one contact of length `l <= ell-1 = 5` leaves one gap of `30 - l >= 25 >= 15`. A
  degree-1 cell **always satisfies** the connected-arc conjunct. It can never be part of a falsifier.
- **degree >= 2** with spread contacts — gaps sum to `>= 20` but split, and every gap can be held
  below 15. The conjunct fails.

Hence, and this is the structural consequence worth carrying forward:

> **A falsifier requires every exposed cell to have contact-degree `>= 2`. A finite contact graph
> with no leaves contains a cycle. So the diagram is not simply connected unless that cycle is
> filled — and in this category the only thing that can fill it is a base region.**

So the survival of connected-shell reduces **entirely** to whether base regions can fill those
cycles. That is not a new hazard: it is precisely the debt gate (i) incurred
("base regions have unbounded boundary and no piece bound … that is exactly why a shell can fail to
touch `∂D` at all: a base region may separate it") and precisely what gate (ii) was told not to
inherit from Strebel.

## R-inner triviality run (2026-08-07, Lead GO after the W1 verdict)

**Outcome: STUCK, exhaustively — 0 of 268,118 distinct clean inner words certified trivial. This is
a SCREEN, not a non-triviality verdict, and W1's caveat (c) stays OPEN.**

| Run ID | Date | Parameters | Outcome | Wall-clock | Validated by | Notes |
|---|---|---|---|---|---|---|
| `r-inner-v1` | 2026-08-07 | W1 + first 2,999 family members in enumeration order | 0 / 3,000 certified trivial | 44.5 s | 41-relator + calibration sets | **Biased prefix** (alphabetically-first classes, smallest `l`) — superseded by `v2` |
| `r-inner-v2` | 2026-08-07 | uniform reservoir sample of 20,000 from all 853,287 distinct inner words | **0 / 20,000 certified trivial** | 288 s | 41-relator + 3 calibration sets (6,997 words, 0 % false-stuck) | The screen of record |
| `r-inner-full` | 2026-08-07 | **exhaustive** over all 853,287 distinct inner words | **0 / 853,287 certified trivial** | 12,659 s (3.5 h) | same | The result of record; supersedes the `v2` sampling bound |

**Family size, and a correction to the denominator.** Free contact placement yields **32,616,225 ring
members with 853,287 distinct inner boundary words** (lengths 14–54, mass around 40). The `v1` run's
3,000 were the *first* 3,000 in enumeration order, so `v2` re-ran it as a uniform reservoir sample;
`r-inner-full` then covered the set exhaustively, making the `v2` bound (95 % upper bound
`~1.5e-4`) redundant. It is retained above only as the record of what was known before the
exhaustive pass landed.

### Degeneracy audit — 68 % of the enumerated family was junk

The pre-registration did **not** declare degeneracy exclusions for the enumeration generator. Audited
after the fact, against the standing doctrine:

| Configuration | Count | Share |
|---|---|---|
| inconsistent B-orientation — B's two contact arcs read in opposite directions round B's own boundary; geometrically impossible | 15,042,475 | 46.1 % |
| non-freely-reduced seam — the two inner gaps cancel where they meet, i.e. a cancelling vertex / spur, so the diagram is not reduced | 13,611,495 | 41.7 % |
| **clean (neither)** | **10,462,160** | **32.1 %** |

Distinct inner words: **268,118 clean**, against the 853,287 first reported — the denominator was
inflated 3.2×.

**Effect on the verdict: none, and the direction is safe.** The exhaustive run tested the *superset*,
so 0 certified over 853,287 implies 0 certified over the 268,118 clean words a fortiori. Excluding
degenerates can only shrink the set, never add a hit. The corrected figure to quote is
**0 / 268,118 distinct clean inner words, exhaustively**.

**Methodology miss, recorded rather than quietly fixed.** Both exclusions should have been
pre-registered as generator constraints, not discovered by audit. The orientation constraint in
particular is a *geometric* condition my builder never enforced — it was caught only because the
family size looked implausibly large. Filed against the generator-degeneracy doctrine.

**Method.** `wordreduce` is unusable here — it needs a completed `.kbprog`, and KB never converged
on `G_5` (`#confluent=false`). So the hole-boundary word is rewritten directly against the frozen
live rule set `g5.kbprog.live.frozen-20260801T185132` (231,438 rules, sha256 `f3554ede…e77a6e6`,
matching the pinned anchor). Soundness: every rule is a `G_5` identity, so rewriting preserves the
group element and reaching the empty word **certifies** triviality regardless of confluence. The
converse is never asserted. Each word is tried over its full conjugacy/inversion orbit (all cyclic
rotations of `w` and `w^-1`), which can only strengthen the sound direction.

**Controls (green, and the run aborts if they are not).**

- 41/41 defining relators of the `g5` presentation reduce to the empty word;
- free reduction sanity (`aA`, `bBaA` → empty);
- negative screen: `a`, `b`, `ab` survive (a reducer that empties everything would be caught).

**False-stuck calibration — this is what gives the screen its weight.** A stuck result is only
informative if the reducer usually succeeds on words that *are* trivial. Measured on two classes of
known-trivial words:

| Calibration class | Certified | Mean length |
|---|---|---|
| conjugates/products of defining relators, len 0–69 (7 buckets) | **4,000 / 4,000 = 100 %** | — (1,984 samples in the 20–29 bucket, W1's length) |
| commutators `[r1^u, r2^v]` of conjugated relators | **1,497 / 1,497 = 100 %** | 94 |
| triple products of conjugated relators | **1,500 / 1,500 = 100 %** | 72 |

**0 % false-stuck on 6,997 known-trivial words**, spanning lengths 0–140 and covering the entire
14–54 range the sampled inner words occupy (including 1,984 at exactly W1's length of 28). So the
reducer is not weak on this group, and 0/20,000 is a *substantive* screen rather than a shrug.

**It is still not a verdict, and the caveat that matters is stated rather than buried:** all
calibration words are built *from the defining relators* by conjugation, product and commutator.
They are shallow-derivation trivial words — the easiest class for a KB system derived from those
same relators. An inner-boundary word is not guaranteed to be shallow. So 0 % false-stuck on this
class does **not** license "0 % false-stuck in general", and no non-triviality claim is made.

**Family enumerated.** The first pass used `run.py`'s ring builder, which pins the *same* slot layout
on both cells and so requires a literal contact match at those exact slots — only 46 of 400 targets
were constructible. That sample was too small and too arbitrary to report, so contact placement was
generalised: the two contacts are now placed wherever a literal match actually exists, independently
on each cell, with the four outer/inner gap pairings enumerated. Geometry is unchanged from W1
(annulus, hole filled by the base region), so correctness carries over; only the family is larger.

**What this means for W1.** Obligation (c) is **not** discharged. W1 remains a valid *combinatorial
and planar* object whose base region is of unknown realizability. Since Validator's verdict ruled the
predicate `#status/disproven` **independently of all three caveats**, this does not disturb Level 1.
It bears on Level 2: the restricted hypothesis (minimal-area, band-reduced, for E7) still stands
`#status/conjectured`, and W1 still does not reach it.

## The single open obligation

W1's base region `R-inner` carries `TrivialityObligation(status="unresolved")`. Its inner boundary
word must be `= 1` in `G_5` for the diagram to exist. **This obligation is in the sound direction** —
certifying that a word *is* trivial is an equality, which a sound-only rewriter can do. It is
therefore **not blocked on rung-5 `gpaxioms ec=0`**, unlike the `P_6` upper bound.

Discharging it means running the frozen `G_5` rewriter over the inner walk words of the candidate
family. The encoder deliberately never invokes the rewriter, so this is a scoped follow-up, not part
of this run.

Until it is discharged, the honest statement is: **the falsifier family is combinatorially and
planarly valid, and is inhabited iff some member's inner boundary word is `G_5`-trivial.**

Two further obligations remain open by construction and are not silently passed: relative-reducedness
path-completeness (`reducedness_status = "unresolved"` on every diagram, since `SoundOnlyOracle`
cannot certify the negative) and area-minimum existence.

## Arm B — exponent-4/6 control

The mandatory audit item, answered:

| `n` | relator length | `min_connected_arc` | degree 1 fails? | degree 2 fails? | degree 3 fails? |
|---|---|---|---|---|---|
| 4 | 24 | 9 | **no** | yes (`l=3,5`; gaps 8+8) | yes |
| 5 | 30 | 15 | **no** | yes (`l=1,1`; gaps 14+14) | yes |
| 6 | 36 | 21 | **no** | yes (`l=1,1`; gaps 14+20) | yes |

**Which hypothesis fails at `n=4` and `n=6`: the connected-external-arc conjunct, by the same
degree-`>=2` mechanism, identically at all three exponents.** The minimum degree that can fail is 2
at every rung; degree 1 never fails at any rung.

**No Hall contradiction arises, and this is the correct reading.** The lemma *fails* at `n=6`; it
does not survive there. Survival at `n=6` is what would have contradicted Hall 1958. The mechanism
being exponent-generic means the connected-arc conclusion is not something exponent 5 buys you —
consistent with [[project_b25_uniform_route_dead|the uniform-route ruling]], and it is why this
control line sits under B26.

`n=4` and `n=6` rows are **arithmetic transport, not mechanically verified** — the encoder pins
`RANK6_BOUNDARY_LEN=30`, `PERIOD_LEN=6`, `FIFTH_POWER=5`. See the fork assessment below.

## The n=6-construction fork — not escalated

Assessed per Lead's caveat (2). Genuine 24-slot / 36-slot construction **would** need a Developer
patch, and a near-miss escape does not exist (`relator_length=30` is also hit by `(n=6, ell=5)`, but
`Rank6Cell.build` pins `PERIOD_LEN=6` and `FIFTH_POWER=5`, so a `(6,5)` cell cannot be built either).

**Patch not requested.** The pre-registered decision rule was to request it only if the Arm A
mechanism turned out to be `n=5`-specific. It is not — it is pure gap arithmetic, generic in
`(n, ell)`. The patch is recorded as mechanical-verification debt, for Lead to schedule if Validator
wants the transport rows re-derived inside the encoder rather than beside it.

## Bugs found and fixed before reporting

Both were mine, both manufactured a false null in `v0`, and both were caught by refusing to accept
that null:

1. **Walk layout.** A cell's two gaps were concatenated adjacently in the external walk, so the
   encoder correctly merged them into one run of 28 and every cell trivially *passed*. The real
   geometry is annular: each cell meets `∂D` in one gap and the hole in the other.
2. **Illegitimate move set.** "Shrink a contact" is not a band move — it frees slots belonging to no
   contact, arc or interface. `evaluate_move` checks boundary label, area and measure only, not the
   slot partition, so it accepted the vandalism and marked sound diagrams `move-reducible`. Replaced
   with genuine contact merges (`checks.merge_contacts`) gated on cyclic adjacency in every shared
   cell, with the partition check enforced before a candidate is proposed.

`v0` is recorded in the results table as discarded rather than deleted.

## E7 literal census — reported as a screen, explicitly not scored

Design input only (methodology §7). Literal overlap ceiling between the cyclic E7 word (138) and the
symmetrized fifth powers of all 26 survivors is **7** (`L=7`: 8 shared words; `L>=8`: none).
Computed twice by independent implementations, which agree.

**Non-claims, stated deliberately because this cuts in the program's favour:** it is a *literal*
census; `G_5`-realized equality can create matches it misses; the realized version is a universal
negative that a sound-only oracle cannot certify and is blocked on `gpaxioms ec=0`. It is **not**
evidence for H0 and **not** a step of the §3.3 contradiction. Routed to Validator to judge, not
scored here.

## What this does and does not settle

- **Does**: the implication `i(Pi) <= 3 ⇒ one connected external arc >= 15` does **not** hold in the
  adopted R6 category on the strength of the disc classification. Route Rank-1 cannot obtain that
  implication for free; it must additionally exclude leaf-free contact graphs, i.e. rule out base
  regions filling cycles.
- **Does not**: make H0 false for `∂D = E7`. F2 (the E7-specific falsification) was pre-registered
  **BLOCKED** and was not run — exhibiting a diagram for E7 presupposes `E7 = 1` in `G_6`, the open
  question. H0 may remain vacuously true for E7. Kourovka 11.48 is untouched.
- **Does not**: bound `P_6`, or claim anything about B(2,5).

## Open questions

1. Discharge the `R-inner` triviality obligation with the frozen `G_5` rewriter (sound direction,
   no `gpaxioms` dependency). Inhabited or empty?
2. Does route Rank-1 admit a repaired hypothesis excluding leaf-free contact graphs, and does that
   repair survive its own `n=4/6` audit?
3. Should the Developer patch be scheduled to move the Arm B rows inside the encoder?

## Related material

- [[connected-shell-falsification-2026-08-07]] — the pre-registration this scores against
- [[connected-shell-falsification-data-2026-08-07]] — inputs, constants, run paths
- [[Relative Shell Falsification/_type|_type]] — experiment-type root
- [[B26/_progress]] — B(2,6) umbrella
- [[2026-08-05-b25-R6-definition-gates]] — gate (ii) is the falsified hypothesis; gate (i) predicted the base-region separation this run made concrete
- [[ell6-theory-barrier-analysis-2026-08-05]] — §3.3/§3.4 falsifier shapes, §7 the Hall wall

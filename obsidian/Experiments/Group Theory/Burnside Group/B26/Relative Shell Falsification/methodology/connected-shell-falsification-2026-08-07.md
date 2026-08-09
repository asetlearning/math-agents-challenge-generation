---
title: Connected-shell falsification harness — pre-registration
date: 2026-08-07
domain: group-theory
project: b26
instance: B(2,6)
experiment_type: relative-shell-falsification
status: conjectured
author: maumayma
tags: [agent/exp, user/maumayma, domain/group-theory, topic/burnside, topic/b26, topic/burnside-infiniteness, topic/small-cancellation, topic/van-kampen, topic/uniformity, project/b26, status/conjectured, methodology]
---

# Connected-shell falsification harness — pre-registration

> **Run 2026-08-07.** Outcome in [[connected-shell-falsification-results-2026-08-07]]; inputs and
> run paths in [[connected-shell-falsification-data-2026-08-07]]. The text below is the
> pre-registration as filed and is left unedited; the only post-run change is this pointer and the
> frontmatter status. One declared deviation: the `k` bound in §4 was shrunk from `2..6` to `2..3`
> at run time, disclosed with its reasoning in the data note rather than sampled silently.

**Pre-registered 2026-08-07, before any run of the harness.** Gate opened by Lead on the
Developer-encoder / Validator-conformance / delta-nod sequence. Falsification-first per Validator's
standing exponent-4/6 doctrine.

Everything in the § Scoping reconnaissance section was run *before* this note was filed. It is
declared there as design input, is **not** evidence, and is not scored.

---

## 1. Hypothesis under attack

**H0 — connected-shell** (gate (ii) of [[2026-08-05-b25-R6-definition-gates]], full form; the
lemma is Math-expert's, conjectural, and is the sole hypothesis of route Rank-1 "R6-shell"):

> In a minimal-area, band-reduced relative diagram `D` for `E7` over `G_5 + {p^5 : p in R_6}`,
> there exists a rank-6 cell `Pi` with `i(Pi) <= 3` whose contact with `∂D` is a **single
> connected arc** of cell-side length `>= 15`.

Validator's emphasis, adopted here: **`>=15` needs both conjuncts.** `i(Pi) <= 3` alone permits
total exposure 15 split across up to three components, longest `>= 5`, which supports no scan.

### The falsifiable claim I test

**F1 (category-generic, the thing this harness decides).**

> There exists a structurally valid, classically-reduced, locally move-irreducible relative diagram
> `D` in the adopted R6 category in which **every** rank-6 cell carrying external exposure satisfies
> `i(Pi) <= 3` and yet has **no** connected external arc of cell-side length `>= 15`.

F1 true ⇒ the connected-outer-arc conclusion is **not** inherited from the classical non-metric
`C(6)` disc classification into the relative category, i.e. the implication
`i(Pi) <= 3  ⇒  connected arc >= 15` fails in the category as adopted. That kills route Rank-1
*as stated*, because it is exactly the implication R6-shell would have to supply. This is the cheap
decisive test Validator asked for ("cheaper to kill than to prove").

F1 false-within-bounds ⇒ **a screen, not a verdict.** Bounded exhaustion of a construction space
never proves a universal statement. Reported as `#status/inconclusive`, never as support for H0.

### What I explicitly do NOT test — declared blocked

**F2 (E7-specific).** Falsifying H0 *for `∂D = E7`* requires exhibiting a diagram whose boundary is
the E7 word — which presupposes `E7 = 1` in `G_6`, the open question the whole program is about.
Per Lead's answer (1), existence-only searches are in scope and universal-negative conclusions are
not; F2 is neither. **Reported BLOCKED, not run.** F1 is the tractable target and is the one
Validator's own falsification recommendation is phrased in ("exhibiting one band-reduced relative
diagram in which every boundary rank-6 cell meets `∂D` in `>=2` components kills the route" — no E7
qualifier).

This distinction is load-bearing and I will not let the write-up blur it: **F1 kills the proof
route; it does not make H0 false for E7, which may remain vacuously true.**

---

## 2. Problem set

- **Category**: the R6 relative category as ruled in gate (i) — rank-6 cells with boundary a
  rotation of `p^{+-5}`; base regions bounded by any word `=_{G_5} 1`; pieces are `G_5`-realized
  contacts measured in rank-6 boundary letters; `area(D) = ` number of rank-6 cells.
- **Period classes**: the 26 survivor classes of the frozen Stage-1 corrected receipt
  `20260805T080305Z` (58 classes, 32 trivial-fifth-power drops, 26 survivors), consumed as an
  enumeration only.
- **Rungs**: `n=5, ell=6` mechanically (Arm A); `n=4` and `n=6` by the encoder's own arithmetic
  audit plus pattern transport (Arm B) — see § 6 for the construction fork.
- **Protected word**: E7, length 138, used **only** in the § 7 literal census, not in F1.

## 3. Tooling and its declared limits

`infinite_b25/r6_encoder/`, receipt `20260805T091512Z`, 51/51 conformance.

Independently re-verified by me before designing this experiment (receipts in § 9):
`shasum -c` 11/11 `OK`; `uv run pytest` `137 passed`; exponent audit reproduces `n=4 -> 9`,
`n=5 -> 15`, `n=6 -> 21`; header reads 58/32/26; `payload_sha256` matches the value Lead quoted.

**Limits I am accepting and will carry into every claim:**

| Limit | Consequence for this experiment |
|---|---|
| `SoundOnlyOracle` cannot emit `NOT_EQUAL` (typed asymmetry) | `reduced_status` can never return `reduced`; `classify_minimal_area` can never return `certified-minimal`. Any falsifier is **candidate** on those two axes by construction. |
| `classical_cancellation` is combinatorial over recorded contacts | Its *negative* IS decidable with no oracle. This is the one reducedness axis I can certify. |
| Relative reducedness needs a `path_completeness` certificate | Absent one, "no conjugating path recorded" stays a screen. Recorded as an open obligation, not silently passed. |
| **The encoder validates a diagram *record*, not planar realizability** | This is the main methodological risk of the whole experiment (§ 5). |
| Cells hard-coded at 30 boundary slots (`RANK6_BOUNDARY_LEN`), `PERIOD_LEN=6`, `FIFTH_POWER=5` | Genuine `n=4`/`n=6` diagram construction is a Developer patch. See § 6. |

I do not modify the encoder. Any patch is requested through Lead.

## 4. Method

### Arm A — mechanical falsification search at `n=5, ell=6`

**Contacts are literal.** Every contact in a candidate falsifier is built so both cell-side words
spell the *identical* word. Then realization is certified by free reduction alone: for `u == v`,
`SoundOnlyOracle.words_equal(u,v)` queries `u·v^{-1}`, which free-reduces to the empty word and
returns `EQUAL`. Consequences, both deliberate:

- every contact reaches `realization_status = "certified"`, so `evaluate_shell_predicate` returns
  `pass`/`fail` rather than `unresolved`;
- the certificate carries `requires_gpaxioms_ec0 = False`. **The falsifier therefore carries zero
  `gpaxioms ec=0` debt.** It does not consume the blocked `P_6` upper bound, and does not consume
  Delta Stage 2.

Certificates pin `source_sha256 = b6d0ab50…8bec8` (the encoder receipt payload), so they are
non-fixture and traceable; `Certificate.__post_init__` enforces the pin.

**Enumeration.** Deterministic and exhaustive within declared bounds:

- cell count `k in {2,3,4,5,6}`;
- contact graph: every simple graph on `k` labelled cells with max degree `<= 3` (so the
  `i(Pi) <= 3` conjunct **holds everywhere** — this makes the falsifier sharp: the failure is
  purely on the connectivity conjunct);
- per-cell slot allocation: contact arcs of length `l in {1..5}` (`l <= ell-1 = 5`, the Validator
  literal-piece theorem) placed at slot offsets on the 30-slot cyclic boundary, up to the cyclic
  and reflective symmetry of the cell;
- period-class assignment drawn from the 26 survivors, distinct classes on adjacent cells (which
  also rules out classical cancellation by construction, then verified rather than assumed);
- external arcs = the complement of the allocated contact slots, mapped into a synthesized external
  boundary walk.

**Per-diagram scoring**, all via the encoder, no re-implementation:

1. `schema.validate_diagram` → must be empty;
2. `checks.check_external_arc_labels` → must be empty;
3. `checks.classical_cancellation` → must be empty (certified negative, oracle-free);
4. `checks.relative_cancellation` with `SoundOnlyOracle` → recorded; obligation logged;
5. `checks.normalize` → maximal contacts recomputed from scratch;
6. `checks.evaluate_move` over the enumerated band-move candidates → **locally move-irreducible**
   means no candidate move is `accepted`;
7. `checks.decompose_at_cut_vertices` + `checks.short_component_obligations` → components, and the
   `<15` bucket recorded as open obligations (never as "harmless");
8. `checks.evaluate_shell_predicate(d, cell, component=...)` for **every** cell, evaluated inside
   the relevant component walk, never the full external walk.

**A diagram is a falsifier candidate iff** steps 1–3 are clean, step 6 holds, and step 8 returns
`status="fail"` for every cell with nonzero exposure, with `i(Pi) <= 3` throughout and zero
`unresolved`.

### Arm B — exponent-4/6 control

For every falsifier pattern Arm A returns, I record it as a *slot-allocation pattern* —
(degree, contact lengths, gap lengths) — because `evaluate_shell_predicate` reads only contact
counts and the run-decomposition of walk positions. Then, for `n in {4,5,6}` at `ell=6`, using
`checks.exponent_audit` arithmetic (`relator_length = n*ell`,
`min_connected_arc = (n-3)*ell + 3` → `24/9`, `30/15`, `36/21`):

- state whether the same pattern instantiates on an `n*ell`-slot boundary;
- **state which hypothesis of H0 fails at `n=4` and at `n=6`** — the mandatory audit item;
- if the pattern survives at `n=6`, flag it loudly: survival at `n=6` contradicts Hall 1958, so it
  means the *lemma* is wrong, which is the point of the harness.

Arm B results are **arithmetic + transport**, explicitly *not* mechanically verified in the encoder,
because the encoder refuses `parameters.relator_length != 30`. That refusal is honest and I keep it.

## 5. Declared soundness gap — planarity

The encoder checks structural consistency of a diagram record. It does **not** check that the
record is realizable as a planar van Kampen diagram. A non-planar record is not a counterexample to
anything.

Therefore, pre-registered and binding:

- a falsifier is reported as **CANDIDATE** unless I supply an explicit, hand-checkable planar
  embedding (rotation system + face list) alongside it;
- with an embedding, it is reported as **PROVISIONAL-CONFIRMED**, still pending Validator, still
  pending the two certificate obligations (relative-reducedness path-completeness, area-minimum
  existence);
- **no falsifier is reported as CONFIRMED by me at all.** Validator owns that word.

This is the single most likely way for this experiment to produce a wrong answer, which is why it
is a gate and not a caveat.

## 6. The n=6-construction fork — assessment (Lead's caveat 2)

Assessed before filing, as instructed. Findings:

1. `evaluate_shell_predicate` raises `SchemaError` unless `parameters.relator_length == 30`. So
   `ShellParameters(6,6)` (36 slots) is refused.
2. **A near-miss worth recording**: `relator_length = 30` is also hit by `(n=6, ell=5)` — a genuine
   exponent-6 rung, `min_connected_arc = 30 - 3*4 = 18`. But `Rank6Cell.build` pins `PERIOD_LEN = 6`
   and `FIFTH_POWER = 5`, so a `(6,5)` cell cannot be built either. The escape does not exist.
3. `n=4, ell=6` needs 24-slot cells; no integer `ell` gives `4*ell = 30`. Also blocked.

**Assessment: genuine `n=4`/`n=6` diagram construction requires a Developer patch** —
parametrizing `RANK6_BOUNDARY_LEN`, `PERIOD_LEN`, `FIFTH_POWER` off `ShellParameters`, plus
relaxing the `evaluate_shell_predicate` guard accordingly.

**I do not request that patch yet**, because Arm B answers the control question by transport if the
Arm A pattern is exponent-generic, and a patch is only worth Developer time if it is not. Decision
rule, pre-registered:

> Request the patch through Lead **iff** Arm A returns a falsifier whose mechanism depends on an
> `n=5`-specific quantity (i.e. the pattern's instantiation at `n=4` or `n=6` is not settled by the
> audit arithmetic alone). Otherwise report Arm B as arithmetic-transport and name the patch as the
> mechanical-verification debt.

I will not re-implement the category outside the encoder to dodge this. A divergent
re-implementation is not covered by the 51/51 conformance and would be a worse answer than a
declared debt.

## 7. Scoping reconnaissance (run before filing; design input, NOT evidence)

Sizing the search space required knowing how rank-6 cell boundaries can meet a protected word. I
computed the **literal** overlap ceiling between the cyclic E7 word (length 138) and the symmetrized
fifth powers of all 26 survivor classes:

```
L= 5: 20 distinct shared words
L= 6: 20
L= 7:  8
L= 8:  0   <-- literal ceiling is 7
L>=8:  0
```

Computed twice, by two independent implementations (encoder `cell_side_word` enumeration over all
rotations/orientations/signs; and direct cyclic-subword set intersection). They agree.

**Non-claims, stated because this cuts in the program's favour and Lead's rider forbids positivity
claims:**

- This is a **literal** census. `G_5`-realized equality can create matches literal comparison misses.
  The `G_5`-realized version of this scan is a universal negative, is exactly what a sound-only
  oracle cannot certify, and is blocked on rung-5 `gpaxioms ec=0`.
- It is **not** evidence that H0 is true, and **not** a step of the §3.3 contradiction. It is a
  screen.
- It is **not** scored in this experiment. It is reported to Validator separately, labelled as a
  bounded literal census, for Validator to decide whether it is worth anything.

Its actual role here is design input: it tells me a falsifier's external arcs must be short, so the
interesting variable in Arm A is how exposure *splits*, not how long it can get.

## 8. Pre-registered analysis plan

- **Metric**: per-cell `ShellReport.status` and `max_connected_arc_length`; diagram-level verdict =
  conjunction over cells.
- **Statistical test: none, and this is deliberate.** F1 is an existence claim settled by exhibition,
  and its negation-within-bounds is settled by exhaustive deterministic enumeration. There is no
  sampling and no variance, so the `n>=5` seeds rule and paired tests do not apply. I substitute the
  honest analogue: **the enumeration bound is declared in advance (§4) and the full census is
  reported, not just the hits.** I will not switch to a sampled search post-hoc; if the space proves
  too large, I shrink the declared bound, say so, and report what was dropped rather than sampling
  silently.
- **Controls** (the baseline analogue for a construction experiment):
  - *positive control* — encoder fixture `I4` (three internal contacts, one connected arc of 15)
    must return `status="pass"`. If it does not, the predicate is broken and no `fail` sweep means
    anything.
  - *negative control* — fixture `I3` (15 = 8+7 split) must return `status="fail"`.
  - *sanity control* — fixture `I10` (`i(Pi)=3`, sides 5+5+8, connected arc 12) must `fail` on the
    connected-arc conjunct.
  - Both controls run in the same process as the sweep, and are reported in the results table.
- **Every apparent falsifier is PROVISIONAL** pending verified-`G_5` nontriviality recheck of its
  period classes, per Lead's rider. Recorded per candidate.

## 9. Provenance

| Leg | Value |
|---|---|
| git SHA | `17b6068b395a35f89c0b05aa0f5048cd6961170c` (branch `feat/patternboost-b25-loop-v1`) |
| `uv.lock` sha256 | `978fe9e2d4809ac5cad3bf2814e01b6948076ce79512621d6a3c7b29994126fe` |
| encoder receipt payload sha256 | `b6d0ab50a62f7f30a6517fd3fb0a19da2b189c570397d7a64e846dd54388bec8` (receipt `20260805T091512Z`, 51/51) |
| frozen Stage-1 receipt | `20260805T080305Z`, 58 classes / 32 drops / 26 survivors |

`mixer-core` is not in this experiment's path; the encoder receipt payload is the third
provenance leg in its place.

Runner: `experiments/burnside/r6_shell_falsification/run.py` (to be written under this pre-reg).
Output: `runs/b26_shell/r6_shell_falsification/<timestamp>/`.
CPU: 2 slots max, per Lead.

## 10. Anti-pattern check

- **Tuning on the test set** — no. The predicate, the piece bound, `max_internal_contacts=3`, and
  the arc thresholds all come from the frozen conformance-PASSed encoder. I set none of them.
- **Cherry-picking** — enumeration is exhaustive within § 4 bounds and the full census is reported.
- **No baseline** — addressed by the three encoder-fixture controls in § 8; a construction
  experiment's baseline is a predicate that provably still returns `pass` on a passing input.
- **Result-too-good** — already triggered once, on the § 7 literal ceiling. It was cross-checked
  with an independent implementation before being written down, and it is fenced with explicit
  non-claims. Same discipline applies to any Arm A hit: a falsifier found instantly at `k=2` gets
  hunted for a bug before it gets reported.
- **Unverified math claim** — F1's verdict is routed to Validator. I do not pronounce.
- **Positivity claim** — none made anywhere. The § 7 census is fenced; a null Arm A is reported
  `#status/inconclusive` as a screen.
- **Scope creep into B(2,5)** — no B(2,5) conclusion is drawn in this subtree (§ Scope note in
  [[Relative Shell Falsification/_type|_type]]).

## 11. Success criterion

The experiment succeeds — in the falsification sense — if it returns **either**:

- a planar-embedded diagram meeting all § 4 gates in which every exposed cell fails the connected-arc
  conjunct while `i(Pi) <= 3` (route Rank-1 dead as stated, routed to Validator); **or**
- a clean, fully-reported null over the declared bound, plus the § 6 fork assessment and the § 4 Arm
  B audit naming which hypothesis fails at `n=4` and `n=6` (H0 survives a cheap attack; **not**
  support for H0).

It fails if it returns a falsifier I cannot embed planarly and cannot rule out, since that decides
nothing either way.

## Related material

- [[Relative Shell Falsification/_type|_type]] — experiment-type root
- [[B26/_progress]] — B(2,6) umbrella
- [[2026-08-05-b25-R6-definition-gates]] — gate (ii), the target; gate (i) fixes the category; gate
  (iii) is the blocked `P_6` upper bound this harness deliberately does not consume
- [[ell6-theory-barrier-analysis-2026-08-05]] — §3.3 multi-contact falsifier, §3.4 flat-ladder
  falsifier, §7 the Hall wall
- [[2026-08-05-b25-ell6-theory-preruling]] — standing exponent-4/6 doctrine
- [[experiment-folder-convention]] — layout and tagging this note follows

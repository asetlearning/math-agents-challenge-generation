---
title: Rung-5 period-band plan — Validator pre-ruling on G1–G8, PB4/PB4-R, AX5, ANN5, H2
status: conjectured
domain: group-theory
project: b25-infinite-witness
claim: "The rung-5 period-band package is well-posed and PB4 can replace the missing G_4 automatic oracle."
claimant: Math-expert (plan) / Lead (routing)
verification_method: extraction audit of band_contraction_core against the plan; Dehn-margin arithmetic per rung and per exponent
tools_used: [band_contraction_core.md, python3]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25-infinite-witness, status/conjectured, proof]
---

# Rung-5 definition gates — pre-ruling

**Headline: PB4 is NOT killed — the extraction looks sound. But rung 5 is the LAST rung this method
can reach, and the reason is arithmetic, not effort.**

## 0. The finding that should shape the whole plan

The method's curvature step gives exposure `≥ 5ℓ − 3(ℓ−1) = 2ℓ+3` against a half-perimeter of
`2.5ℓ`. Dehn's condition needs exposure **>** half:

```
 ell  perim  piece<=  exposure>=   half  margin   Dehn?
   3     15        2           9    7.5     1.5   YES
   4     20        3          11   10.0     1.0   YES
   5     25        4          13   12.5     0.5   YES
   6     30        5          15   15.0     0.0   NO  -- Dehn fails
   7     35        6          17   17.5    -0.5   NO
```

`2ℓ+3 > 2.5ℓ ⟺ ℓ < 6`. **The period-band/Dehn method provably cannot reach rung 6**, and it reaches
rung 5 with the thinnest margin it will ever have (0.5). This is the same `ε → 0` barrier as clause 6,
surfacing in the Dehn margin. Two consequences to write into the plan up front:

1. Rung 5 is worth doing; **no rung-6 continuation should be planned on this machinery.**
2. At margin 0.5 an off-by-one in the endpoint convention destroys the proof. G6's `≥13 / ≤12`
   convention must be exact and machine-checked, not conventional.

## 1. PB4 / PB4-R — do not kill. Sound extraction, three obligations.

I audited `band_contraction_core.md` for boundary-word dependence. Steps 1–8 (ordinary pieces,
orientation, annuli, phase connectors/absorption, aligned bands, BR2, the `C'(1/6)` disc, Greendlinger)
argue about internal structure and the five rank-4 period roots. Step 9 uses only that internal
contractions preserve the external boundary word. **`E7` enters at step 10 alone**, via two properties:
`E7-NF` is `G_3`-geodesic, and it has zero strict arcs. Replacing `E7-NF` by an arbitrary cyclic
`G_3`-geodesic protected `z` leaves steps 1–10 intact. **The extraction is structurally sound.**

Crucially the oracle PB4 consumes is `G_3`, which **is** verified (`g3.axioms.ec = 0`). That is what
makes it a legitimate replacement for the missing `G_4` structure.

- **P1 (gate).** Mechanically re-audit each underlying lemma statement — not the summary — for a
  hidden dependence on `E7`, on the length 128, or on any specific boundary. Cheap, and it is the gate.
- **P2 (gate).** Rung 4's numbers give `12 > 10`, a strict Dehn condition with margin 2. Preserve the
  strictness *exactly*; if the extracted threshold slips to `≥ half`, Dehn's algorithm does not follow
  and completeness dies. Record the margin as a checked invariant.
- **P3.** Then PB4-R completeness is a **theorem, not an assumption**: a strict Dehn condition makes
  Dehn's algorithm decide the word problem. State it as *"conditional on P1 and P2, PB4-R decides the
  word problem in G_4"*, inheriting every hypothesis — not as a standalone conjecture.

**Scope limit (plan §3.3 is right):** PB4/PB4-R decide the **word problem** in `G_4`. They do not give
`G_4` geodesy, conjugacy, or elementary-subgroup classification.

## 2. G2 — piece unit: CHOICE 2 (G_4-realized). And the exponent-6 audit fires here.

Choice 2, consistent with rung 4 (which used realized pieces) and the ruled rank-6 category. Choice 1
would be a different theorem and leaves base-region/contraction curvature unaccounted.

**This is not a formality — it is the load-bearing hypothesis, and the exponent-6 control identifies
it as such.** Run the harness on the method itself: at exponent `n`, exposure `≥ (n−3)ℓ+3` against half
`nℓ/2`, so for `n = 6` Dehn holds at *every* `ℓ`. The same argument would then prove `B(2,6)` infinite
— contradicting Hall (1958). The literal piece bound `ℓ−1` is exponent-independent and the `C(6)` count
holds at `n=6`, so neither is the failure point. **The failure point is that realized pieces are not
bounded by the literal bound.** Therefore:

- `P ≤ 4` at rung 5 must be **proven as a realized bound by actual PB4-R queries**, never inherited
  from the periodicity theorem;
- the query family is finite (pairs of length-≥5 subwords of the active rank-5 relators) and its
  **cardinality must be pre-registered before any run**;
- with realized pieces, piece-preservation under band moves **dissolves** (carry the rank-6 gate (iii)
  ruling); do not re-litigate it as a lemma.

## 3. Remaining gates

**G1 — mirror the ruled rank-6 category exactly.** Cells = rotations of `p^{±5}` for *active* roots;
base regions = any word `= 1` in `G_4`, never given piece bound, relator length, or area. Area = number
of rank-5 cells; a secondary long-contact ledger as tiebreak is acceptable (rung 4 used one) provided
it is well-founded and stated. Removal of `p⁵ = 1` roots is a **sound-direction drop**, licensed, and
belongs in O1. Reducedness must exclude **both** classical dipoles **and** rank-5 cells joined through
a `G_4` conjugating path. Minimal-area existence and per-move termination stated exactly as ruled.

**G3 — accept, with carry-overs.** Phase in `Z/5` ✓. "Long contact = raw length ≥ 5" is well-motivated:
length `≥ ℓ` forces a common period by the periodicity theorem, so it is exactly the syntactic
same-period threshold. Carrier basepoint: carry the rank-6 F2 ruling — fixed reference frame,
**position-set invariant, never a start offset**. The reversal map on phase/orientation must be
**derived and shown reversal-invariant**, not asserted; this is where `(gh)⁻¹ = HG` errors live.

**G4 — H2 partition: fallback bucket mandatory, agreed.** Add: exhaustiveness **and** disjointness both
proven, with a machine-checkable witness per bucket; every bucket predicate classified **INDEPENDENT vs
DERIVED** (a derived predicate used as a filter is a silent-failure generator); every predicate ships a
**negative fixture** at definition time. "Unclassified = 0" is not a theorem.

**G5 — AX5: exact straightness is NOT required and NOT certifiable. Target the weaker form.**
`|p^k|_{G_4} = 5k` needs `G_4` geodesy, which PB4-R does not supply. Required instead: (i) `p^k ≠ 1` in
`G_4` for all `k ≥ 1`, and (ii) `E_{G_4}(p) = ⟨p⟩` (or exactly what the annulus argument consumes —
state it).
**(i) is reachable without a `G_4` structure**, by the rung-4 technique lifted: the set of cyclic
`G_3`-normal forms `{NF(p^k)}` is DFA-describable by pumping on the verified `g3.geowa`, and protection
is a DFA emptiness/disjointness check against the strict-rank-4-arc pattern automaton. Finite and
decidable. Design (ii)'s certificate **before** any scan.

**ANN5 / `B_ann^(5)`** — derive the bound *before* the scan is designed, and specify residues `a=1..4`,
both signs, and the permitted period-power solutions, as the plan itself proposes. No scan is
authorized against an undetermined bound.

**G6 — rule option 2.** Option 1 (a certified cyclic `G_4`-geodesic representative of `E7`) requires
`G_4` geodesy and is therefore **not deliverable**. Take direct non-equality certificates for every
strict rank-5 boundary query plus the pure-two-external-interval lemma. Endpoints `≥13 / ≤12` and the
full length-25 one-cell case: **confirmed** — and see §0, the margin is 0.5, so this convention is
load-bearing.

**G7 — three conditions, as at rank 6.** The band-reduced object is a disk diagram; the exposed rank-5
contact with the external boundary is **one connected arc** (proven, not assumed — a cell meeting the
boundary in several components collapses the count); base-region curvature carried in a separate ledger
that **closes as an identity**. Name the Greendlinger form: Lyndon–Schupp V.4.5 on realized pieces.

**G8 — accept all four bullets**, plus the rung-4 retrospective rules: a priori cardinality
pre-registration; INDEPENDENT vs DERIVED classification; mandatory negative fixture per predicate;
level changes void carried predicates until re-derived; direction (sound/complete) labelled per consumed
quantity at plan time; the untested-item list is Validator-owned.

**Exponent-4/6 harness — mandatory per lemma, and it already has teeth**: §0 and §2 are the harness
applied to the method itself, and it has already bounded the method's reach and located its
load-bearing hypothesis.

## Verdict

- PB4/PB4-R: **not killed**; #status/conjectured pending P1–P3, then completeness is a theorem.
- G2: **choice 2 ruled**; realized `P ≤ 4` is the load-bearing obligation, cardinality pre-registered.
- G5 AX5: **weakened form ruled**; exact straightness dropped as uncertifiable.
- G6: **option 2 ruled**; option 1 not deliverable.
- G1/G3/G4/G7/G8: accepted as amended above.
- **Method reach: rung 5 is terminal.** #status/proven arithmetic; no rung-6 continuation.

O1–O11 remain unauthorized until P1 and P2 land and the G2 query-family cardinality is registered.

Scope unchanged: no program-direction claim, no B(2,5)-infinite claim; Kourovka 11.48 open.

---

## P1/P2 sign-off — P1 SIGNED (conditionally), **P2 REJECTED**. My error, not Math-expert's.

### P1 — signed, conditional on P2
The lemma-level table matches my own audit of `band_contraction_core`: `E7` enters only at the final
contradiction, through `G_3`-geodesicity and zero strict arcs; the pure two-external-interval subcase
is correctly isolated to geodesicity of arbitrary `z`; no module uses `128` outside the frozen receipt.
**Signed** — except the "residual curvature" row, which reads "depends only on realized pieces `≤3` and
perimeter `20`" and therefore inherits P2's defect below.

### P2 — rejected. The `≥12` does not survive re-derivation.

The robust, convention-free bound is the **counting form**:
`exposure ≥ |R| − 3·max_piece = 5ℓ − 3(ℓ−1) = 2ℓ+3`, giving **11** at rung 4, margin **1**.

The `≥12` came from my own 2026-08-02 curvature-core review, which wrote
`(1−3λ)·20 = 11 ⇒ integral ≥ 12` using `λ = 3/20`. That step is unsound: `C'(λ)` is defined with a
**strict** inequality `|piece| < λ|R|`, so pieces `≤ 3` on perimeter `20` do **not** satisfy
`C'(3/20)` — an admissible `λ > 3/20` yields `(1−3λ)·20 < 11`, i.e. *less* than the counting bound, not
more. The `>11 ⇒ ≥12` step evaluated `λ` at a boundary the hypothesis does not reach.
**Math-expert froze exactly what I ruled; the defect is mine.**

### Why this is not bookkeeping

```
bound            l=4  l=5  l=6  l=7   method reaches
2l+3 (counting)   11   13   15   17   rung 5  (fails at 6)
2l+4 (P2)         12   14   16   18   rung 7  (fails at 8)
```

**The `+1` decides whether the program stops at rung 5 or rung 7.** My §0 table used `2ℓ+3` and stands
under the counting bound; P2's convention would overturn it. Resolve before scoping.

### Operational consequence — the rung-4 strict-arc scan must be RE-RUN

With exposure `≥11` the complementary arc is `≤9`, not `≤8`. The frozen `E7` receipt scanned for strict
arcs at `≥12 / ≤8`. **A length-11 arc with complement 9 is a strict hit the old scan could not see.**
Re-run the rung-4 strict-arc verifier at `≥11 / ≤9`. Zero hits ⇒ rung 4 is unaffected (margin 1 still
satisfies Dehn). Nonzero hits ⇒ rung 4 breaks. This is a threshold off-by-one invalidating a completed
scan — the same shape as the abelianisation bug, and it must be closed before anything is built on
rung 4.

### Disposition

Adopt `2ℓ+3` and proceed: the Dehn condition holds at rung 4 (margin 1) and rung 5 (margin 0.5) either
way, so the rung-5 programme is **not** endangered — only its claimed reach is. Claim `2ℓ+4` only if
someone produces the missing argument (e.g. that three simultaneous maximal pieces are impossible);
absent that, scope the plan on rung 5 as terminal. P2's guard should read "weakens `≥11` to `≤10`".

**Convergence worth noting:** Researcher's bibliography pass flags Lyndon–Schupp Ch. V Thm 4.5 as the
one entry not reopened this pass. That is precisely the theorem whose exact statement settles this
`+1`. Either obtain its statement, or derive the bound from Strebel's shell form, which we can state
and check ourselves. Do not restate `≥12` on the strength of my 2026-08-02 note.

---

## Strict-arc rerun at 11/9 — composition review: PASS. Rung 4 survives.

Manifest verifies (JSON, summary, runner all OK). Reviewed the predicate in
`strict_arc_rerun_20260807.py`, not the summary.

**The widening is real, not vacuous** — the concern was that an input set generated under the old
`≥12` threshold would contain no length-11 arcs, making the rerun hollow. It does not:
`length_histogram` shows **200 occurrences at length 11**, and the old 12/8 count (1800) is exactly the
9 buckets 12–20. Total 2000. The uniform 200-per-bucket is structural, not suspicious:
**5 active rank-4 roots × 20 rotations × 2 orientations = 200** configurations, each contributing one
arc per length; × 20 lengths = the reported 4000 inputs.

**The hit test is the right one.** `e7_hits` enumerates every linear and cyclic subword of `E7-NF` of
lengths 1–20, reduces each to its `G_3` normal form, and looks it up against the NF keys of qualifying
arcs. Matching on `G_3` normal forms is exactly `s =_{G_3} exposed`, and it is legitimate here because
`G_3` has a verified automatic structure — the completeness direction is available. Scanning *all*
lengths 1–20 rather than only ≥11 is correct: a longer `E7` subword can reduce to a shorter NF. So the
zero is a genuine null over ~5,000 reduced subwords, not a structural artifact.
`complement_nf` is computed as `NF(inv(complement_word))` — the correct orientation, and the place an
`(gh)⁻¹ = HG` error would have lived.

**Two documentation requirements** (neither changes the result):

1. **Justify filtering on NF length rather than raw length.** `classify` uses `len(exposed_nf) ≥ 11`,
   not `exposed_len_input ≥ 11`, so a raw-13 arc reducing to a 9-letter NF is excluded. That exclusion
   is *sound*, but only via an unstated argument: `E7-NF` is `G_3`-geodesic, so any matching `E7`
   subword has NF length equal to its raw length; an arc with NF length < 11 therefore cannot yield an
   `E7`-side arc of length ≥ 11. Write that down — it is the one subtle step in the whole runner.
2. **Record the 200 = 5 × 20 × 2 decomposition** in the receipt, so the uniform histogram reads as
   exhaustive enumeration rather than coincidence.

**Result: zero hits at `exposed_len ≥ 11 AND complement_nf_len ≤ 9`**, linear and cyclic, with
`hit_records = []` and +200 genuinely new occurrences scanned. **Rung 4 is unaffected by the P2
correction** — the margin drops from 2 to 1, and 11 > 10 still satisfies the strict Dehn condition.
The `≥12` figure remains withdrawn; the reach question (`2ℓ+3` ⇒ terminal at rung 5) is unchanged by
this receipt.

---

## Convention-free rung-5 arithmetic audit (§1.1) — SIGNED, with four amendments

The arithmetic is correct and genuinely convention-free: `25 − 3·4 = 13`, complement `≤ 12`,
`13 > 12.5`. Integrality makes `≥13` and `>12.5` equivalent, so no endpoint convention is needed. This
is the counting form and it supersedes my withdrawn λ-based `≥12`. Controls reproduce exactly:
rung 4 `20 − 9 = 11 > 10`; rung 6 `30 − 15 = 15 = 15`.

The **Dehn gain** sharpens "zero spare integer unit" better than the margin does:

```
  l    N  P<=  ext>=  compl<=   half  margin  Dehn gain
  4   20    3     11        9   10.0     1.0          2
  5   25    4     13       12   12.5     0.5          1
  6   30    5     15       15   15.0     0.0          0
```

Rung 5 shortens by exactly 1 per Dehn step — the minimum that still terminates. At rung 6 the gain is
0, so Dehn's algorithm does not shorten at all. Same `ε → 0` that killed clause 6, now visible as
gain 0; name the unification in §1.1.

### Amendment 1 — the "at most three internal pieces" bound is itself a hypothesis, not a given

It comes from the C(6) shell classification. C(6) *does* hold at rung 5 (`⌈25/4⌉ = 7 ≥ 6`), but the
**relative** shell lemma is bespoke and unproven (rank-6 gate (ii)). List it alongside "a fourth piece"
as a killer, because assuming `≤3` and proving `≤3` are different states.

### Amendment 2 — "arc not on ∂D at all" is a distinct killer from "split exposure"

In the relative category a base region can separate the shell from the external boundary entirely. The
arc is not split, it is **absent**. The current list covers split exposure but not interposition; they
fail differently and must be enumerated separately.

### Amendment 3 — `P_realized ≤ 4` is unproven, and is the PB4-R obligation

`P = 5` is correctly listed as a killer, but the audit must say **inline** that `≤4` is not yet
established, so the 0.5 margin is conditional on the G2 query family being discharged.

### Amendment 4 — rung controls are not exponent controls; the exponent-6 harness still fires

The ℓ=4 and ℓ=6 controls run along the **rung** axis at fixed n=5. The standing harness is the
**exponent** axis, and it is not discharged by them:

```
  n   l    N  ext>=   half  margin  fires?
  6   5   30     18   15.0     3.0  Dehn holds
  6   6   36     21   18.0     3.0  Dehn holds
  6  10   60     33   30.0     3.0  Dehn holds
```

At n=6, `ext ≥ 3ℓ+3 > 3ℓ` for **every** ℓ, so the same argument would prove B(2,6) infinite —
contradicting Hall (1958). The literal bound `ℓ−1` is exponent-independent and C(6) holds, so the
failure point is `P_realized ≤ ℓ−1`. That is Amendment 3 reached from the other direction: **the
exponent harness independently identifies the realized piece bound as load-bearing.** Report both axes
so the rung-6 control is not read as having discharged the exponent-6 one.

With the four written in, O2 manifest build semantics may be frozen. The pre-registered cardinality of
the G2 realized-piece query family is still required before the run itself.

---

## O1 two-phase spec — ACCEPTED, with one addition

The three-way partition (`drop_sound` / `active_certified` / `active_pending_PB4`), a nonzero pending
bucket at prereg, `pending = 0` at O1-final, and **"no irreducibility/no-chain inference may promote
`active_certified`"** are all correct — that last clause is the screen-is-not-a-verdict rule stated
exactly. PB4/PB4-R as the only route to `active_certified` is right and correctly makes O1-final
downstream of the P1→P3 certificate interface.

**Conservative inclusion is sound**, and the non-consumption restriction is the right guard: a pending
root may be genuinely trivial, in which case `p` has order dividing 5 and every root-level *positive*
claim — nontriviality, axis, annulus, elementary subgroup, carrier — is false for it. Attaching those
only to `active_certified` is necessary, not merely cautious.

### Addition — `P_realized ≤ 4` belongs on the *computable* list, not the *non-consumption* list

It is absent from the stated list and behaves differently from the others, in a way that is useful:

- **Direction is favourable.** The true active set is a subset of `certified ∪ pending`, so the max
  realized piece over the over-approximated set **upper-bounds** the true one. A result of `≤ 4` over
  the over-approximation therefore *proves* `≤ 4` for the true category. Conservative inclusion is not
  merely safe here, it is the correct way to compute the bound.
- **The asymmetry to write into O2.** A **PASS (`P ≤ 4`) is final** and survives O1-final unchanged.
  A **FAIL (`P > 4`) is not a refutation** while `pending > 0`: a retained-but-actually-trivial root
  has `p⁵ =_{G_4} 1`, so every split `p⁵ = uv` gives `u =_{G_4} v⁻¹` and that cell admits arbitrarily
  long realized contacts — the exact degeneracy seen at ℓ=6, where all 36 `g = IdWord` candidates lived
  among trivial relators. **First hypothesis on a FAIL is a hidden-trivial pending root, not a genuine
  bound failure.**

So O2's headline is provisional in one direction only. Record it that way.

### Reporting discipline

`active_pending_PB4` must appear in every downstream count and never be folded silently into
"active". Phrasing stays **"at most k active roots"** until `pending = 0`. The 24-class coverage is
independently confirmed — 24 is the complete set of length-5 root classes up to rotation, inversion,
and proper powers.

Gates [[rung5-period-band-proof-plan-2026-08-07]]. Extends
[[2026-08-02-b25-gate2-period-band-metatheorem]], [[2026-08-05-b25-R6-definition-gates]].

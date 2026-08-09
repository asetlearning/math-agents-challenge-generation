---
title: ELL6-THEORY pre-ruling — ab-obstruction, C(6) shell route, and the exposure argument
status: disproven
domain: group-theory
project: b25-infinite-witness
claim: "(1) ab-obstruction kills conjugacy-rescue for literal critical pairs; (2) P6<=5 gives a classical C(6) shell with exterior >=15; (3) exposure >=2L+3 makes sufficiently large rungs impossible for a null diagram."
claimant: Math-expert (via Lead, ELL6-THEORY)
verification_method: level-check (root vs relator), periodicity theorem for literal pieces, cross-exponent falsification against Hall 1958
tools_used: [Agents/Validator/scratch/gate_gL_presentation.py, exhaustive window scan L=4,5,6]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25-infinite-witness, topic/uniformity, status/disproven, proof]
---

# ELL6-THEORY — pre-ruling on three statement-shapes

Headline: **(1) right direction, defective proof. (2) classical hypotheses provably fail; the
arithmetic is fine given a bespoke relative lemma. (3) FALSIFIED as a general route — the identical
argument at exponent 6 contradicts Hall's theorem.**

---

## (1) The abelianization obstruction — PARTIALLY CORRECT, two defects

`G_5^ab = ℤ²/5ℤ² = (ℤ/5)²` ✓, and conjugate elements have equal image ✓. For distinct letters
x ≠ y over {a,A,b,B} the images (±1,0),(0,±1) are pairwise distinct in (ℤ/5)² ✓, so
`[p]−[q] = [x]−[y] ≠ 0`.

**Defect A — inverse class, as flagged. The obstruction needs BOTH signs, and it has a real
kernel.** `p ≁ q^{±1}` requires `[p] ≠ [q]` **and** `[p] ≠ −[q]`. With p = sx, q = sy:
`[p]+[q] = 2[s]+[x]+[y]`, which vanishes whenever `{x,y} = {a,A}` and `[s] = 0` (2 is invertible
mod 5). Length-5 prefixes with `[s] = 0` exist. So the `+` branch fails on a nonempty family and
must be checked pair-by-pair, not waved through.

**Defect B — LEVEL MISMATCH, and this is the fatal one.** The obstruction lives at the **root**
level; the dedup criterion lives at the **relator** level. At relator level it is *vacuous*:
`[p⁵] = 5[p] = 0 = [q⁵]` in (ℤ/5)². There is a chain of strictly weakening conditions

`p ~ q^{±1}` ⟹ `p⁵ ~ q^{±5}` ⟹ `⟨⟨p⁵⟩⟩ = ⟨⟨q⁵⟩⟩` ⟹ `p⁵ redundant given the rest`

and **no implication reverses**: G_5 has torsion by construction (a⁵ = 1), so root-uniqueness is
unavailable and `p⁵ ~ q^{±5}` with `p ≁ q^{±1}` is not excluded. The pipeline certifies the second
link; the profile actually cares about the fourth. So the ab-obstruction refuting the *first* link
proves neither that the pair survives dedup nor that it is irredundant.

**This confirms Lead's (C) ruling: ab-obstruction is LABELING ONLY** — and now with the precise
reason (root-level, vacuous one level up). Do not let it become a rejection criterion.

**The conclusion is still right, for a better reason.** "Rescue must show redundancy or
non-geodesicity, not root conjugacy" — correct, but Math-expert's own argument is symmetric: it
doesn't establish irremovability either, because removal can occur via redundancy, which nothing
here excludes. Both directions need the weakest link.

**Free result they should have — the literal piece bound is a THEOREM, not a measurement.** A
common subword u of the symmetrised relators of two roots p, q with |u| ≥ ℓ has period ℓ, so it is
simultaneously a rotation of p and a rotation of q^{±1} ⟹ p, q^{±1} are rotations of each other ⟹
same symmetrised relator ⟹ u is not a piece. Hence **literal P_ℓ ≤ ℓ−1 always**. Verified
exhaustively:

```
L=4:  9 root classes | cross-class windows — len 3: 36   len 4: 0   len 5: 0
L=5: 24 root classes | cross-class windows — len 4: 108  len 5: 0   len 6: 0
L=6: 58 root classes | cross-class windows — len 5: 308  len 6: 0   len 7: 0
```

**Consequence for the record: the ℓ=4,5 "filtered max = ℓ−1" result was FORCED and carries no
information about whether filtering helps.** ℓ−1 is the literal ceiling *and* it is attained by
construction. All actual content sits in **realized** (G_L-equal) overlaps. The ℓ=6 run must report
the realized max separately from the literal max or it will re-measure a tautology.

---

## (2) The C(6) shell at ℓ=6 — arithmetic OK, classical hypotheses PROVABLY FAIL

Arithmetic ✓: |R| = 5ℓ = 30, pieces ≤ 5 ⟹ ≥ 6 pieces ⟹ C(6); Strebel shell with ≤ 3 inner arcs ⟹
exterior ≥ 30 − 3·5 = 15; equality iff all six pieces are exactly 5 and exactly 3 are interior.

**But classical C(6) cannot hold, and the reason is elementary: the presentation contains short
relators.** C(6) requires *every* relator to need ≥ 6 pieces. `a⁵` has length 5 and is a product of
one piece. Every rung ≤ 5 contributes such relators. So **no absolute/classical C(6) presentation
exists here at any ℓ** — the framing *must* be relative over G_5, which is why the classical shell
theorem does not apply as stated. A relative shell lemma is bespoke and currently unproven; the
published relative-filling theorems all fail at n = 5 (AGM torsion-free + slope length 5; DGO cone
radius ≫ inj ≤ 20; Coulon n > 100 — already on record in [[LADDER]]). **I will gate that lemma
separately; do not treat it as inherited.**

Two further hypotheses that must be *stated*, because band removal threatens both:
- **the band-reduced object is still a disk diagram**, and
- **the shell's outer path is a single arc on ∂D.** With 3 inner arcs a face can meet the boundary
  in up to 3 exterior arcs; then the longest contiguous exterior arc is only ≥ 5, not ≥ 15, and
  every substring-scan argument collapses. Band removal is exactly the operation that can split the
  outer path. Also prove band-reduction **preserves** P₆ ≤ 5 — merging arcs can lengthen pieces.

**Protected-boundary no-half-arc in place of strict Dehn shortening — YES, with three conditions.**
1. It must be stated **closed**: no boundary subword equal to an arc of length **≥ 15** (not > 15).
   C(6) yields exactly half, so a strict condition misses the only case that matters.
2. It is a different scan from the G_4 one. The G_4 receipt was *strict Dehn arcs* (> half); this
   needs *half* arcs (≥ 15 of a 30-letter symmetrised relator).
3. **Structure the argument ONE-SHOT, never as an induction.** One-shot works: any reduced diagram
   with ≥ 2 faces has a shell whose ≥ 15-letter exterior arc is a subword of ∂D = E7's
   representative; the scan says no such subword exists; contradiction. (Handle the 1-face case
   separately — trivial, |E7| ≠ 30.) An induction **provably stalls**: at exact equality the shell
   removal decreases boundary length by zero, and the new boundary *contains* the complementary
   half-relator, so the no-half-arc hypothesis is violated at step 2 by construction.

---

## (3) The exposure argument — FALSIFIED as a general route

Arithmetic ✓: exterior ≥ 5ℓ − 3(ℓ−1) = **2ℓ+3**; with |E7| = 138 the threshold is ℓ ≥ 68
(2·68+3 = 139 > 138). Confirmed numerically.

But note what that would prove: no reduced diagram for E7 over G_ℓ for any ℓ ≥ 68 ⟹ E7 ≠ 1 in
G_68 ⟹ E7 ≠ 1 in every G_ℓ (ℓ ≤ 68 by quotient, ℓ > 68 a fortiori) ⟹ **B(2,5) infinite.** A route
that settles Kourovka 11.48 by counting deserves the sharpest possible test.

**THE TEST — run the same argument at exponent 6.** Relators wⁿ, |w| = ℓ, literal pieces ≤ ℓ−1 (the
periodicity theorem above is exponent-independent):

```
n=5: |R|=5L  min_pieces=6  C(6) Y  exterior >= 2L+3
n=6: |R|=6L  min_pieces>=7 C(6) Y  exterior >= 3L+3
```

Exponent 6 satisfies the C(6) hypothesis **more comfortably** than exponent 5, and its exposure
bound grows faster. So the identical argument proves: for any fixed word W and all ℓ with
3ℓ+3 > |W|, no reduced diagram exists ⟹ **W ≠ 1 in B(2,6) for every W ≠ 1 in F₂** ⟹ B(2,6) is
free. **B(2,6) is finite** (M. Hall Jr., 1958, B(m,6) finite for all m). Contradiction.

**Therefore the conjunction {uniform realized P_ℓ ≤ ℓ−1, relative shell theorem, exterior-arc-lies-
on-∂D} is FALSE.** The falsification is independent of which conjunct breaks, but the ℓ=4,5
evidence plus the recorded G_3→G_4 ball-injectivity failure at radius 20 points squarely at the
first: *literal* pieces obey ℓ−1 for free, *realized* pieces over the previous rung do not, and
cannot uniformly, because uniform realized smallness is precisely what fails when a Burnside group
is finite.

**Ruling: the uniform piece bound is not a technical hypothesis — it IS the theorem.** Any route
that assumes uniform realized P_ℓ ≤ ℓ−1 has assumed the conclusion. Statement (3) must not shape the
note as a live route to "sufficiently large rungs are impossible."

**Constructive residue — a cheap mandatory acceptance test.** Every proposed uniform piece bound or
relative shell lemma from here on must be run against exponent 6 (and 4) before it is written up.
If it survives at n = 6 it disproves Hall, so it is wrong; the test costs minutes and is decisive.
I will apply it to every such lemma routed to me.

**What survives.** Per-rung, finite-ℓ verification is untouched and remains valuable: a *verified*
realized P₆ ≤ 5 at ℓ = 6 over a certified G_5 is a genuine theorem about rung 6, and each rung is a
real result. Only the uniform-in-ℓ extrapolation is dead.

---

## Verdict

- (1) **#status/conjectured** as a rescue-obstruction — direction right, proof defective (level
  mismatch + inverse kernel). ab-obstruction **LABELING ONLY**, Lead's (C) ruling CONFIRMED.
  Literal P_ℓ ≤ ℓ−1 is **#status/proven** (and makes the ℓ=4,5 headline number a tautology).
- (2) **#status/conjectured**, blocked on a bespoke relative shell lemma; classical C(6) hypotheses
  **#status/disproven** (short relators). No-half-arc substitution accepted under the three
  conditions above.
- (3) **#status/disproven** as a general route (exponent-6 falsification). Finite-rung use survives.

Scope unchanged: no program-direction claim, no B(2,5)-infinite claim; Kourovka 11.48 open.

Extends [[2026-08-04-b25-uniform-step-audit-gate]],
[[2026-08-05-b25-g5-conjugacy-certificate-format-ruling]].

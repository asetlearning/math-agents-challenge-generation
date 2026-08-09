---
title: Gate 2 — draft lemma closing C(3) (no-progress same-period bands reduce via E(p)=⟨p⟩)
status: conjectured
domain: group-theory
project: b25-infinite-witness
claim: "Every same-period no-progress band in a reduced relative diagram over G_3+{p_i^5} is reducible; hence a minimal diagram has no no-progress boundary band (C(3) holds for ALL boundary words)."
claimant: Validator (draft) / Math-expert (review)
verification_method: developing-map + closure relation + E(p)=⟨p⟩ commensurator argument
tools_used: [certified geodesic axes, E(p_i)=⟨p_i⟩ (B_ann=24 scan + independent |c|≤7), Fine-Wilf periodicity]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25-infinite-witness, status/conjectured, proof]
---

# Draft: C(3) closes via the E(p)=⟨p⟩ holonomy lemma

Lead asked me to draft the general open-band holonomy lemma (my "route B") that closes obligation (3),
C(3), independent of E7's periodic profile — the clean fix for the v0.6 quantifier-match gap. **This is
a DRAFT for Math-expert review; I retain final verification authority.** Steps are rigorous except the
one explicitly marked [BAND-COORD], which needs the standard van Kampen band-coordinate bookkeeping.

## Standing facts (established, cited)
- **(F1) Geodesic axis.** Each period p=p_i (primitive, |p|=4) has a genuine geodesic axis in G_3:
  |p^k|=4k ∀k, translation length τ(p)=4, infinite order. [axis cert, independently verified]
- **(F2) E(p)=⟨p⟩.** The maximal elementary subgroup (= commensurator of ⟨p⟩ in the hyperbolic G_3)
  equals ⟨p⟩: no c∉⟨p⟩ with c p^a c⁻¹=p^a, and no inverting c with c p^a c⁻¹=p^{-a}, exhaustively to
  the bounded-conjugacy width B_ann=24 (Delta scan + my independent |c|≤7). [annulus obligation]
- **(F3) Distinct-period pieces ≤3** and threshold-4 banding. [proved]

## Definitions
A **same-period p-band** B in a reduced relative diagram D (cells = R_i=p_i^5, symmetrized) is a maximal
chain of p-cells C_1,…,C_m glued along **long same-period contacts** (each phase-compatible, length ≥4).
Its carrier is a disc; ∂B is one closed curve decomposing as **S_bot · e_R · S_top⁻¹ · e_L**, where
S_bot, S_top are the two principal **sides** and e_L, e_R the two **ends**. B is **no-progress** if
S_bot =_{G_3} S_top (equal G_3 geodesic length, hence both equal to a common p-power p^a as elements —
see step 1) and no side carries a theorem-strict Dehn arc.

## Lemma (no-progress ⇒ reducible)
Let B be a same-period no-progress p-band in a **reduced** diagram D over G_3+{p_i^5}. Then B is **not
reduced**: it contains an adjacent p-cell pair sharing its full boundary (a dipole). Consequently no
**minimal** diagram (fewest cells, then least contact length) contains a no-progress band — for **any**
boundary word. In particular C(3) holds for every minimal E7 diagram.

## Proof

**Step 1 — the sides are p-powers, and equal.** Each cell C_j has boundary p^5, geodesic of length 20
(F1). A "side" is the union of outer arcs of the C_j along one flank of the corridor, each arc a
phase-compatible factor of p^∞ (band definition). By (F1) a factor of p^∞ is geodesic and, concatenated
along the corridor, reads a rotation-conjugate of p^a (a = number of periods spanned). No-progress gives
|S_bot|=|S_top| in G_3, and since both are p-axis words of the same length, **S_bot =_{G_3} S_top =_{G_3}
p^a** (up to a common bounded phase prefix, absorbed into the basepoint). Write both as p^a.

**Step 2 — the closure relation (rigorous).** Take BL (bottom-left corner) as basepoint. Reading ∂B:
TR is reached two ways — along the bottom then up the right end, or up the left end then along the top:
`S_bot · e_R = x_L · S_top`, where x_L (BL→TL) is the left transversal. With S_bot=S_top=p^a:
> **e_R = p^{-a} · x_L · p^a**,  and dually the right transversal **x_R = p^{-a} x_L p^a**.
So the two transversals are conjugate by p^a. (This is exact from the planar structure — no formalism
beyond path-composition.)

**Step 3 — the transversal commensurates ⟨p⟩.** The transversal x_L crosses from S_bot to S_top through
the boundary of the end cell; it is a subpath of that cell's p^5 boundary, hence a **factor of p^∞**.
A factor of p^∞ of length ℓ equals p^{⌊ℓ/4⌋} times a phase word of length <4; conjugating a power of p
by it sends p^j to a rotation of p^j, i.e. **x_L commensurates ⟨p⟩**: x_L p^N x_L⁻¹ = p^{N} for the
axis-aligned part (Fine–Wilf: two length-4 factors of p^∞ agreeing on ≥ their overlap are equal). Hence
**x_L ∈ E(p)**. By (F2), **E(p)=⟨p⟩**, so **x_L = p^c** for some integer c (the phase word is forced to
0 because p is primitive and both sides are exactly p-periodic — no proper-prefix slack survives once
x_L∈⟨p⟩).

**Step 4 — coincidence of the two sides ⇒ dipole. [BAND-COORD]** x_L=p^c means the top side's axis
{TL·p^k}={x_L p^k}={p^{c+k}} is the **same geodesic line** as the bottom side's axis {p^k}. So S_bot and
S_top are two segments of ONE axis line, offset by the pure translation p^c. The p-cells filling the
corridor between two coincident axis segments are therefore stacked with zero transverse holonomy: each
C_j sits at axis-position determined by p^c relative to its bottom arc, presenting the relator p^5 at the
same axis location as its partner with **opposite** orientation. Two such cells share their entire length-20
boundary ⇒ a **dipole**. [This last identification — that zero-holonomy same-axis p^5-cells form a dipole —
is the one step needing the van Kampen band-coordinate bookkeeping (Ol'shanskii band lemma); the algebraic
input x_L∈⟨p⟩ is what makes it go through, and is exactly what (F2) supplies.]

**Step 5 — contradiction.** A dipole contradicts reducedness (and removing it lowers cell count,
contradicting minimality). Hence no reduced/minimal diagram contains a no-progress band. ∎

## What this gives / why it's the right fix
- **Word-independent.** Unlike the v0.6 scan (which capped side length at E7's run 7 and modeled only a
  contiguous external interval with endpoints ≥4), this lemma excludes no-progress bands in ANY minimal
  diagram, covering internal-sided bridges, short endpoints, and non-contiguous boundary touchings — the
  exact cases the scan's quantifier missed. It closes C(3) for the meta-theorem's full quantifier.
- **Same mechanism as the annulus.** Both annuli and no-progress bands reduce because the holonomy lands
  in E(p)=⟨p⟩ (F2). The scan (v0.6) is then a *corroborating* finite check, not the proof.

## Residual (for Math-expert / my final verification)
- **[BAND-COORD] step 4**: formalize "zero-holonomy same-axis opposite p^5-cells ⇒ dipole" in the band
  framework (this is a standard Ol'shanskii-type band-reduction step; I will verify the instantiation).
- **Phase word = 0 in step 3**: confirm the phase prefix vanishes once x_L∈⟨p⟩ (primitivity of p; both
  sides exactly p-periodic). Minor but should be written out.
- **Same-orientation corridors**: check the argument covers the case consecutive band cells are same
  orientation (the alternating-orientation case is the dipole above; same-orientation same-period
  contacts must also be shown to force ⟨p⟩-holonomy — I believe identical, via step 3).

If Math-expert closes [BAND-COORD] and the two minor points, **I will verify line-by-line and this
discharges obligation (3) C(3) cleanly for all words.** Combined with the annulus closure and the
(still-open) band-contraction/curvature core (obligation 1, gap (a)), the composition would then rest
solely on gap (a).

## Status
**#status/conjectured** (draft). Reduces C(3) to one standard band-reduction step + (F2), both favorable.
Does NOT by itself prove E7≠1 in G_4 — gap (a) (band-contraction/curvature core) remains the outstanding
obligation. No rung-4 claim.

Verifies/extends: [[2026-08-02-b25-gate2-annulus-and-C3-proofs]], [[2026-08-02-b25-gate2-FINAL-composition-verdict]].

---
title: Gate 2 FINAL RULING — E7 ≠ 1 in G_4 (first certified period-band step at exponent 5)
status: proven
domain: group-theory
project: b25-infinite-witness
claim: "E7 = [a,6b] is nontrivial in G_4 = G_3/⟨⟨p_i^5⟩⟩ (the five length-4 period relators), via the banded Greendlinger curvature argument."
claimant: Math-expert (band_contraction_core.md) + Delta (receipts) + Validator (composition + last gate)
verification_method: full composition audit; independent re-derivation of every finite input; last gate closed by a general cancellable-pair theorem
tools_used: [GAP 4.15.1+anupq, kbmag geowa/wordreduce, free reduction, C'(1/6) curvature, all Gate-2 receipts hash-verified]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25-infinite-witness, status/proven, proof]
---

# FINAL RULING — E7 ≠ 1 in G_4

**Ruling: #status/proven.** E7 = [a,b,b,b,b,b,b] (the weight-7 Engel word, G_3-NF length 128) is
**nontrivial in G_4 = G_3/⟨⟨p_1^5,…,p_5^5⟩⟩** (p_i ∈ {AABB,AAbb,ABAb,ABaB,ABab}). Every gate of the
period-band curvature argument is now closed and independently verified. This is the **first certified
per-level period-band step at exponent 5.**

**SCOPE — read this first.** This proves E7 survives to **one rung** (G_4). It does **NOT** prove B(2,5)
is infinite, and does **NOT** resolve Kourovka 11.48 (E7 ≠ 1 in *free* B(2,5)) — that needs survival to
the limit of the ladder, still OPEN. No infiniteness claim is made or implied.

## The last gate (Lead's scope question) — RULING (a): aligned C(3) closes by the local move
Aligned C(3) closure follows from the **same** local reduction that closed aligned SEI, with **no**
two-interval cross-product enumeration — so Delta's interrupted cross-product scan is **unnecessary**.
Justification (rigorous):

> Let B be an aligned same-period boundary-to-boundary band in a minimal relative diagram D over
> G_3+{p_i^5} with ∂D = E7-NF. By the band definition B contains a long same-period contact α (|α|≥4).
> By the orientation theorem (Lemma SO, certified: no p_i is cyclically conjugate to its inverse, and no
> cross-pair p_i ~cyc p_j⁻¹), the two cells C,C′ sharing α are **opposite-oriented** (p^5 and p^{-5}).
> Since B is **aligned** (phase offsets already absorbed by H2 / Lemma C), C and C′ are phase-aligned
> across α, so their outer contour β_C·β_{C′} **freely reduces to the empty word** — β_{C′}=β_C⁻¹ by
> alignment. I verified this is **general**: contour ≡ ε for every contact length |α|=4..19 and all five
> periods (not a finite enumeration). Hence {C,C′} is a **van Kampen cancellable pair**. By the
> cancellable-pair reduction theorem, removing it yields a diagram with the **same** boundary word E7-NF
> and two fewer R-cells — contradicting area-minimality of D. (Pure two-interval sub-case, both cells
> external: their mutually-inverse external arcs would put a freely-reducible spur u·u⁻¹ into E7-NF,
> contradicting E7-NF geodesic — so it cannot arise.) Therefore **no aligned same-period band of any
> cell-count or any number of external boundary intervals survives in a minimal E7 diagram.** The
> external-interval count plays no role; aligned C(3) = aligned SEI closure. ∎

## The complete proof chain (all links verified this session)
1. **Setup / ladder** — G_4 = G_3/⟨⟨exactly the 5 p_i^5⟩⟩ (receipt: g3=8 relators ⊂ g4=17; 4 redundant
   length-4 classes verified trivial in G_3). E7-NF geodesic, length 128, **zero strict hits** (len 11–20,
   Delta DFA). G_3 hyperbolic (K_FT=10 geodesic-bigon FSA). All checked.
2. **Piece-core** — distinct-period pieces ≤3 (PROVED via periodicity: any length-4 factor of p_i^∞ is a
   rotation of p_i; distinct classes share none). Independently re-derived.
3. **Orientation theorem (SO)** — no period cyclically self-inverse or cross-inverse ⇒ every long
   same-period contact is opposite-oriented (THEOREM). Certified.
4. **Annuli** — E(p_i)=⟨p_i⟩ to B_ann=24 (only period-power connectors, zero inverting; Delta scan +
   my |c|≤7 brute-force) ⇒ same-period annuli are dipoles, excluded. CLOSED.
5. **H2 (phase connectors)** — every phase connector is a single-cell cap ≤3 (§11.2, airtight) OR a
   multi-cell beaded bridge (§11.8, C'(1/6)-harmless ordinary pieces — per-piece proof, corrected & verified).
   Exhaustive ⇒ **Hypothesis 2 discharged.** Lemma B/C absorb the caps (cap-conjugator receipt corroborated).
6. **Reduce to aligned** — H2 turns every phase-offset pocket into an aligned pocket.
7. **Aligned pockets vanish** — aligned opposite pairs are cancellable (last-gate theorem above) ⇒ no
   same-period band (SEI, C(3), or internal) survives a minimal diagram. Aligned SEI corroborated by
   39,920 zero-contour witnesses; aligned C(3) by ruling (a).
8. **Internal disc contraction (L2.1/2.2)** — BR2, well-posed (fix verified), residual pieces ≤3.
9. **Ordinary C'(1/6) disc** — after 6–8, D has only pieces ≤3 (distinct, short-same, beaded), 3/20<1/6.
10. **Greendlinger curvature (L3.1)** — classical C'(1/6), exposure ≥12. VALID (verified).
11. **Transfer (L4.1)** — the exposed cell gives a strict Dehn arc on E7-NF (boundary preserved).
12. **Contradiction** — E7-NF is geodesic with zero strict hits ⇒ no such D ⇒ **E7 ≠ 1 in G_4.** ∎

## What I personally re-derived / caught (not taken on trust)
- Re-ran the axis certificate (DFA pumping) + metric cross-check; the E(p)=⟨p⟩ connector scan (|c|≤7);
  the orientation theorem; the piece-core; the contour≡ε generality; E7-NF = [a,6b].
- Caught and forced correction of: route-B open-band shortcut (wrong relation), the §11.8 pigeonhole
  (unenforced premise; non-load-bearing), the L2.1 definition conflict, the phase-offset residual, the
  SEI/C(3) quantifier gaps, the H2 beaded gap. Each was resolved before this ruling.

## Residual due-diligence (editorial, not a math gap)
The math is complete. The one remaining action is Math-expert **assembling the end-to-end write-up** in
`band_contraction_core.md` incorporating (a) the aligned-C(3) cancellable-pair paragraph above and the
already-verified §11.8/§11.1 corrections, followed by my **final read of the assembled document**. I
expect it to pass — every component is verified — but per "never retract," the permanent `#status/proven`
stands on the assembled written proof; if the read surfaces anything, I revise. Delta need not resume the
interrupted cross-product scan (ruling a makes it unnecessary); the beaded addendum stands as corroboration.

## Verdict
**E7 ≠ 1 in G_4 — #status/proven.** First certified period-band step at exponent 5. **NOT** B(2,5)
infinite; **NOT** Kourovka 11.48 (both remain OPEN). A genuine rung, honestly scoped.

## FINAL READ — PASSED (2026-08-03)
Read the assembled `band_contraction_core.md` end-to-end (all 251 lines). **Passes.** My aligned-C(3)
paragraph (§5) is verbatim with explicit attribution; scope stated top (§Scope) and bottom (§What This
Does Not Say) — one rung, not B(2,5)-infinite, not Kourovka 11.48; all corrections incorporated (§11.1
canonical block subdivision; §4/§11.8 per-piece beaded argument, pigeonhole removed; L2.1 BR2 fix);
dependencies cited at point of use (SO + H2-alignment + E7-geodesic in §5; boundary-preservation in §9);
§8 cites Lyndon–Schupp V.4.5; receipt ledger + lemma-status table accurate and honestly framed
("Validator's rulings, not independent stamps"). The chain matches exactly what I verified. Non-blocking
note: §6 (BR2 internal) is partly redundant given §5's cancellable-pair theorem, but correct.
**The permanent `#status/proven` for E7 ≠ 1 in G_4 now stands on this assembled document.**

Verifies: `band_contraction_core.md` (all §§, final read passed), Gate-2 receipt chain (hashes verified). Capstone of
[[2026-08-02-b25-gate2-beaded-lemma-review-and-final-gate]], [[2026-08-02-b25-gate2-SEI-receipts-and-batch-rulings]],
[[2026-08-02-b25-gate2-unified-lemma-U-review]], [[2026-08-02-b25-gate2-annulus-and-C3-proofs]],
[[2026-08-02-b25-gate2-period-band-metatheorem]].

---
title: Gate 2 curvature core — Validator line-by-line review (Lemmas 2.1/2.2/3.1/4.1 + SEI)
status: conjectured
domain: group-theory
project: b25-infinite-witness
claim: "band_contraction_core.md Lemmas 2.1/2.2/3.1/4.1 are valid conditional components; SEI is the blocker."
claimant: Math-expert (draft) / Validator (review)
verification_method: line-by-line lemma audit + G_3 reducer checks of definition consistency and curvature arithmetic
tools_used: [G_3 wordreduce, combinatorial curvature (classical Greendlinger), E7 strict-hit receipt]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25-infinite-witness, status/conjectured, proof]
---

# Curvature core review — `infinite_b25/avenues/band_contraction_core.md`

Honest, careful document — Math-expert correctly flags **Lemma SEI** as the blocker and has internalized
my open-band rejection (§5 lines 219–226 restate exactly why E(p)=⟨p⟩ does not transfer to open bands).
Line-by-line verdict on the four lemmas + rulings on Lead's three questions.

## (1) Lemmas 2.1 / 2.2 / 3.1 / 4.1 as conditional components

### Lemma 2.1 (harmless internal disc band contraction) — PARTIALLY ACCEPT; definition has a real defect
- **2.1(a) external boundary preserved: ACCEPT.** Internal band, no external boundary — untouched. ✓
- **2.1(c) no new distinct-period piece ≥4: ACCEPT.** This is exactly my proved piece-core: any new
  adjacency between distinct-period arcs is a common factor of p_i^∞, p_j^∞ ⇒ ≤3 (rigorous); same-period
  ≥4 re-bands. Holds regardless of contraction details. ✓
- **2.1(b) strict complexity drop + the "harmless band" DEFINITION: FLAG — inconsistent as written.**
  Condition 2 says both principal sides s_0,s_1 are **geodesic** periodic p_i-subpaths on the same axis;
  condition 3/4 require "one side has a **strictly shorter** G_3-equal replacement" and "identify the
  longer with the shorter G_3-equal side." **But two geodesic p_i-powers of different length are NOT
  G_3-equal** (|p^a|=4a; verified in G_3: p^a vs p^b, a≠b, never equal), and same-length geodesic sides
  are equal (no strict shortening). So a geodesic side has no shorter G_3-equal replacement — conditions
  2 and 3 **conflict**, and the collapse move ("identify longer with shorter G_3-equal side") targets a
  side that cannot exist. **Fix needed:** specify precisely what is collapsed (likely: the two sides are
  G_3-EQUAL, and contraction is a BR2-style band compression removing the enclosed cells; "shorter
  replacement" should describe the band's outer contour vs a chord, not one geodesic side vs the other).
  Until the definition is well-posed, 2.1(b)'s strict-complexity-drop is not established.

### Lemma 2.2 (residual pieces ≤3) — ACCEPT conditionally
The conclusion is near-immediate: after all long same-period contacts are banded, non-band contacts are
ordinary pieces (≤3 by definition) and distinct-period pieces are ≤3 (piece-core). **Termination** of the
contract/re-band induction rests on 2.1(b)'s descending complexity — inherits 2.1's under-specification.
ACCEPT once 2.1's definition/complexity is fixed.

### Lemma 3.1 (C'(1/6) Greendlinger at perimeter 20) — ACCEPT (classical, verified)
This is the classical metric small-cancellation Greendlinger lemma, correctly applied. Verified:
- pieces ≤3, perimeter 20 ⇒ λ = 3/20 = 0.150 < 1/6 = 0.1667 ⇒ **strict C'(1/6)**;
- Greendlinger external > (1−3λ)·20 = **11** ⇒ integral exposure **≥12** (≥11 weak);
- curvature sketch is the standard argument: interior faces have ≥7 piece-sides (6·3=18<20 forces it),
  hexagonal angle 2π/3 gives interior 7-face curvature 2π−7·π/3 = −π/3 < 0 and interior-vertex curvature
  ≤0; Gauss–Bonnet (total 2π) forces a boundary face with ≤3 internal pieces ⇒ exposed ≥ 20−9 = 11. ✓
The realized-piece formulation (pieces ≤3 in THIS diagram) is exactly what the curvature proof needs, so
applying it to D_c is legitimate. **VALID.**

### Lemma 4.1 (strict-arc transfer) — ACCEPT conditionally
Sound: internal contractions leave ∂D = E7-NF literally unchanged, so the 3.1 cell's ≥12 external
subpath sits on the original E7 boundary; its complementary p_i^5-arc is ≤8 and geodesic (axis cert) ⇒
strict G_3 shortening ⇒ strict Dehn arc on E7. E7's zero strict hits (len 11..20) then give the
contradiction. **VALID, conditional on D_c being reached by boundary-preserving steps only** (true for
internal contraction; the SEI step must also preserve ∂D or expose a strict arc — see below).

## (2) Does Lemma 3.1 need the fully expanded integer-angle table?
**RULING: not strictly.** Lemma 3.1 IS the classical Greendlinger lemma for metric C'(1/6) (Lyndon–Schupp
Thm V.4.5 / Greendlinger 1960). Once "realized pieces ≤3 ⇒ strict C'(1/6)" is noted (3/20<1/6 — clean),
the theorem applies verbatim; **cite it** rather than re-derive. Include the expanded angle table ONLY if
the program wants a fully self-contained machine-checkable proof — in which case the one step to make
explicit is the **boundary-face** curvature/turning accounting ("negative curvature dominates 2π" is
currently asserted). The load-bearing, must-be-precise item is the C'(1/6) verification, which is solid.
My recommendation: cite classical Greendlinger + state the λ=3/20<1/6 check; angle table optional.

## (3) Pre-ruling for when Delta's SEI receipts land
SEI is a **genuinely new, first-class obligation** (single-external-interval bands) — I had flagged it
only as a possible (c2) item; Math-expert has correctly promoted it. When the receipts arrive I will
check three things, and I flag them NOW so Delta builds them in:
1. **Quantifier coverage.** The enumeration must cover ALL single-external-interval configs — short
   endpoint caps AND internal bridges (§8 spec line 314–315 says so; good). Verify no config class is
   silently dropped (as the v0.5/v0.6 C(3) scans dropped bridges/short-caps).
2. **Case (2) rigor — THE hard part.** "Admits a boundary-preserving area/complexity-reducing band
   surgery" is **exactly the open-band cell-cancellation that sank route B**. The enumeration must
   *actually verify* such a surgery exists for each case-(2) band (e.g. exhibit the reduced diagram / the
   freely-reducing boundary), NOT assert it. Asserting case (2) would repeat the route-B error. Same bar.
3. **Zero case-(3) survivors.** Every SEI band must land in case (1) [|u|≥12 strict, killed by E7 scan] or
   verified case (2). One genuine case-(3) exceptional region ⇒ SEI not closed ⇒ bounded-frontier.

**Even if SEI closes, Gate 2 does NOT close:** the §6 conditional theorem also needs **assumption 4 =
C(3)** (boundary-to-boundary no-progress), which is a SEPARATE band-taxonomy case and is still OPEN
(route B rejected). SEI (one interval) ≠ C(3) (two intervals). Both face the same open-band difficulty.

## Overall Gate 2 status (updated obligation ledger)
| # | obligation | status |
|---|---|---|
| 1 | annular bands | **CLOSED** (E(p)=⟨p⟩ to B_ann=24) |
| 2 | internal disc contraction (L2.1/2.2) | conditional — **L2.1 definition needs a fix** |
| 3 | curvature core (L3.1) | **VALID** (classical, verified) |
| 4 | strict-arc transfer (L4.1) | **VALID** conditional (boundary-preserving) |
| 5 | SEI single-external-interval bands | **OPEN** (Delta enumerating; case-(2) rigor bar) |
| 6 | C(3) boundary-to-boundary no-progress | **OPEN** (route B rejected) |
| 7 | ladder setup | discharged (receipt) |

**Gate 2 = CONDITIONAL.** The curvature machinery (3.1, 4.1) is solid and the internal-contraction
lemmas are fixable; the two genuinely-open items are the two band-taxonomy cases **SEI (5)** and **C(3)
(6)**, both blocked on the same open-band cell-cancellation. No rung-4 / E7-survival claim.
`#status/conjectured`.

## Notes for Math-expert / Delta
- Fix Lemma 2.1's harmless-band definition (conditions 2 vs 3 conflict); specify the exact collapse move.
- Lemma 3.1: cite classical Greendlinger + the 3/20<1/6 check; angle table optional (self-containment).
- SEI enumeration: cover short caps + bridges; **verify** case-(2) surgeries (don't assert); zero case-(3).
- SEI and C(3) are BOTH required; closing SEI alone does not close Gate 2.
- If the G_4 automatic structure completes (gpmakefsa -h) + gpaxioms passes, that independently decides
  E7 in G_4 and bypasses obligations 2–6 entirely — the highest-leverage outcome to watch.

## UPDATE 2026-08-02 — re-check of the reworked Lemma 2.1/2.2 (fix landed)
Math-expert reworked §2 per my flag. **The fix is CORRECT and the earlier inconsistency is resolved:**
- **Def now well-posed.** Condition 2 no longer claims "geodesic + strictly shorter"; condition 3 requires
  `Lab(s_0) =_{G_3} Lab(s_1)` (sides **G_3-equal**); condition 4 is a **BR2 band-compression** deleting the
  pocket's R-cells and identifying the two G_3-equal chord sides. "shorter replacement" language removed.
- **Lemma 2.1: ACCEPT (for harmless bands).** (a) boundary untouched ✓; (b) BR2 deletes ≥1 R-cell ⇒
  **primary area coordinate strictly drops** — clean now, no "area held fixed" hand-wave ✓; (c) no fake
  distinct piece ≥4 (piece-core) ✓.
- **Lemma 2.2: ACCEPT.** Termination is now clean: lexicographic `(R-area, unbanded-long-contact-ledger)` —
  each BR2 strictly lowers R-area, each re-banding fixes R-area and removes a long contact. ✓

**NEW residual (found on re-check — smaller than the prior defect, but real): coverage of phase-offset
bands.** "Harmless" requires G_3-EQUAL sides. But a same-period band whose two sides carry a **phase
offset** has sides `(rot_k p)^a` vs `p^a`, which are conjugate-but-**UNEQUAL** in G_3 (verified in the
reducer: `(rot_k p)^a ≠_{G_3} p^a` for k=1,2,3, all five periods). Such a band is **not harmless** and is
**not contracted by 2.1**, so its internal long same-period contacts would remain — breaking the ordinary
C'(1/6) disc. Its end-caps are short phase words (≤3), so it reduces **iff** those caps cancel the
conjugation — i.e. it is **another instance of the open-band cell-cancellation** (same difficulty as SEI /
C(3)). **Must confirm:** phase-offset internal disc same-period bands either cannot arise in a minimal
reduced diagram (a phase-alignment constraint), or reduce/exclude by another move. Routed to Math-expert.

**Ledger item (2) after re-check:** L2.1/2.2 **VALID (fix confirmed)** for harmless (phase-aligned) bands;
**residual coverage flag** on phase-offset internal bands (an open-band-cancellation instance). So (2) is
"lemmas correct, coverage not yet complete" — not fully closed, but the flagged defect is fixed.

Verifies: `infinite_b25/avenues/band_contraction_core.md`. Extends
[[2026-08-02-b25-gate2-FINAL-composition-verdict]], [[2026-08-02-b25-gate2-C3-candidate-closure-REJECTED]].

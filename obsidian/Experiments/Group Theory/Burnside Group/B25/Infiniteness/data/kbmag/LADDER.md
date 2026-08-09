# The E7 Ladder — conjugator-unbounded certificates (Lead, 2026-08-02)

> **Numbers note (2026-08-04, receipt avenues/setup_and_orientation_receipt.txt):** E7 has
> TWO lengths in these documents: **138** = freely reduced length in F2 (the Kourovka word,
> avenues/e7_witness.txt); **128** = its shortlex NORMAL FORM length in G_3 (the diagram
> boundary word used throughout the G_4 proof and the strict-arc scans). Both correct.


**Reformulation (exact):** E7 ≠ 1 in B(2,5) ⟺ E7 ≠ 1 in G_L for EVERY L, where
G_L = F₂/⟨⟨w⁵ : |w| ≤ L⟩⟩ (since ⟨⟨all fifth powers⟩⟩ = ∪_L ⟨⟨w⁵ : |w| ≤ L⟩⟩ and membership
happens at some finite L). So **B(2,5) infinite ⟺ E7 climbs the whole ladder**, and each rung is
a decidable-in-principle statement. Rung L proven ⇒ "E7 is not a product of conjugates of fifth
powers of words of length ≤ L, with ARBITRARY conjugators and arbitrarily many factors" — strictly
stronger than the Stallings H_M axis (which bounds the conjugator inside the root).

## Proven rungs

| L | method | receipt | E7 status in G_L |
|---|--------|---------|------------------|
| 1 | C₅*C₅ free-product normal form (syllable reduction mod 5) | 128 nonzero syllables (script in session log) | **≠ 1 (proven)** |
| 2 | autgroup fresh run: verified automatic structure, g2.axioms.ec = 0 | wordreduce -diff2: E7 → nonempty NF; sanity A⁵→IdWord | **≠ 1 (proven)** |
| 3 | pre-existing verified automatic structure (g3.axioms.ec = 0, g3.success) | wordreduce -diff2: E7 → nonempty 128-letter NF; sanity (AB)⁵, A⁵, aabBAA → IdWord | **≠ 1 (proven)** |
| 4 | **period-band small-cancellation hand-proof** (the automatic-structure build hit a word-difference blowup and does NOT decide this rung — see LADDER_G4.md) | Validator PASS + receipts; see "RUNG 4 PROVEN" below | **≠ 1 (proven, 2026-08-03)** |

Modulo: correctness of kbmag's verified-automatic-structure word problem (gpaxioms pass = proof
of automaticity; shortlex NF uniqueness then decides the word problem). Route to Validator.

## Why this is the right creative frame

The ladder is precisely the shape of the Novikov–Adian/Ol'shanskii induction: each rung adds
finitely many longer fifth-power relators to a (conjecturally hyperbolic) group. The open
mathematics is the INDUCTIVE STEP (uniform-in-L smallness/filling conditions at exponent 5) —
Math-expert R2 brief asks exactly this (Dehn filling with explicit constants, Coulon-style
partial periodic quotients, per-level certified δ). Every additional proven rung is both a new
exact theorem and base-case data for any future induction.

## Rung-4 filling data (Lead, 2026-08-02)

Of the 9 length-4 relator classes, in G_3: AAAB, AAAb, ABBB, Abbb already have w^5 = 1
(consequences of shorter relators); the 5 genuinely new relators are the fifth powers of
AABB, AAbb, ABAb, ABaB, ABab — and each w^5 is ALREADY shortlex-geodesic in G_3 (NF = w^5
verbatim, length exactly 20; roots are straight elements, stable translation length ≈ 4).
Receipt: wordreduce -diff2 g3 on all 9 (session log). Consequences:
- G_3 → G_4 ball-injectivity fails at radius 20 (5 explicit kernel elements) — Math-expert's
  point confirmed with receipts; the ladder target must be E7-SPECIFIC survival.
- Published filling theorems all fail at n=5 (Math-expert R2, with citations: AGM torsion-free
  + slope-length 5 << bound; DGO cone radius > 5·10^12 vs inj <= 20; Coulon requires n > 100).
- The well-posed remaining question for rung ∞: a BESPOKE certified argument for 5 specific
  geodesic length-20 relators over G_3 (small δ expected) protecting the single length-128
  element E7 — per-level computer-assisted small cancellation, not a general theorem.

## Gate-2 receipts ledger (updated 2026-08-02)

- G_3 word-hyperbolicity: geodesic bigons synchronously 10-fellow-travel — PROVEN at FSA level
  (Delta, gpgeowa: geowa 2757 states / geopairs 4217 / geodiff 417, max label 10; Papasoglu
  bigon criterion applies).
- Infinite order + straightness for ALL k: NF(p_i^k) = p_i^k for all k >= 1, all five periods —
  PROVEN by DFA pumping on g3.geowa (boundary-state repeat after one period, delta 1;
  receipt gate2_g3_raw_receipts_20260802T090750Z.json). Discharges annulus-obligation item 1.
- E7 Dehn-arc layer: E7 NF (128) contains zero strict Dehn arcs from the 400-pattern arc DFA;
  max nonreducing exposure 7/20. Distinct-period exact collisions <= 3. Axis fellow-travel <= 8.
- OPEN obligations (Validator reviewing): band-contraction lemma (meta-theorem step 4);
  bounded annulus/conjugacy lemma (B_ann from K_FT = 10).

## Setup check (Validator item c-1) — DISCHARGED (Lead, 2026-08-02)

Formal relator-set verification (python re-scan of g3/g4 files + wordreduce receipts):
g3 roots (8) ⊂ g4 roots (17); the 9 added are exactly the length-4 classes; AAAB/AAAb/ABBB/Abbb
have w^5 = 1 in G_3 (wordreduce -diff2 → IdWord, rerun 2026-08-02); AABB/AAbb/ABAb/ABaB/ABab do
not. Hence **G_4 = G_3 / ⟨⟨p_i^5, i=1..5⟩⟩ with exactly the five periods of the meta-theorem.**

## Gate-2 status after Validator FINAL composition review: CONDITIONAL

Solid: annulus closed (E(p_i)=⟨p_i⟩ to B_ann=24), piece bound ≤3 proved, axis certs verified,
strict-arc ⇒ contradiction logic sound, v0.5 spurious-object handling correct.
Remaining for #status/proven: (a) band-contraction curvature core (Math-expert, several pages,
Gauss–Bonnet/Ol'shanskii-style) incl. single-external-interval boundary case; (b) general
open-band holonomy lemma (Validator drafting); then Validator line-by-line. NO rung-4/E7-survival
announcement until then.

## RUNG 4 PROVEN (2026-08-03) — Validator final ruling

**E7 ≠ 1 in G_4: #status/proven** — [[2026-08-03-b25-gate2-FINAL-RULING-E7-survives-G4]].
Method: the period-band program (NOT the automatic structure, which is still building and will
give an independent second proof if it completes). Complete Validator-verified chain: ladder
setup · piece-core ≤3 · orientation theorem (SO) · annuli closed (E(p)=⟨p⟩, B_ann=24) · H2
complete (single-cell caps + beaded per-piece) · phase absorption (Lemma B/C, cap-conjugator
receipt) · aligned pockets vanish (cancellable-pair theorem, contour≡ε all contact lengths) ·
BR2 internal contraction · C'(1/6) Greendlinger (exposure ≥12) · transfer ⇒ strict Dehn arc ·
contradiction with E7-NF geodesic + zero strict hits.

**SCOPE (mandatory): this is ONE RUNG. It does NOT prove B(2,5) infinite and does NOT resolve
Kourovka 11.48 (E7 in free B(2,5)). Ladder standing: E7 ≠ 1 in G_1, G_2, G_3, G_4; G_5+ open.**

First certified period-band small-cancellation step at exponent 5. Assembled write-up:
avenues/band_contraction_core.md (+ Validator final read pending on assembly).

## FINAL READ: PASS (2026-08-03) — stamp permanent

Validator read the assembled band_contraction_core.md end-to-end (251 lines): all corrections
incorporated, cancellable-pair paragraph verbatim, scope stated top and bottom, dependencies
cited at point of use, receipt ledger accurate. **#status/proven for E7 ≠ 1 in G_4 is
permanent.** Non-blocking note: §6 partly redundant given §5 (correct as written).

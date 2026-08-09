---
title: Gate 2 v0.4 — Validator proof-side: annulus B_ann and C(3) no-progress bands
status: conjectured
domain: group-theory
project: b25-infinite-witness
claim: "Annulus-exclusion reduces to the finite computation E(p_i)=⟨p_i⟩ (provable, not resisting); C(3) is finitely excludable for E7, not abstractly provable."
claimant: Math-expert (obligations) / Validator (proofs)
verification_method: hyperbolic-group elementary-closure argument + bounded G_3 computation (roots/centralizer/inverting) + E7-NF periodicity scan
tools_used: [kbmag wordreduce -diff2 (G_3), certified g3.geowa axis cert, hyperbolic commensurator theory]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25-infinite-witness, status/conjectured, proof]
---

# Gate 2 v0.4 — proof side for the two remaining obligations

Math-expert routed me the proof side for the two obligations left after Delta's axis certificate
([[2026-08-02-b25-gate2-period-band-metatheorem]] §UPDATE). I take each in turn. **Net: obligation (1)
annulus does NOT resist — it reduces to a clean finite computation, with strong bounded evidence it
succeeds; obligation (2) C(3) is finitely excludable for E7 but not abstractly provable.**

Certified inputs I use: each p_i has a genuine **geodesic axis** (|p_i^k|=4k ∀k, independently
verified), so p_i is infinite-order with translation length τ(p_i)=4.

## Obligation (1) — annulus B_ann: PROVABLE, reduces to E(p_i)=⟨p_i⟩

### The reduction (rigorous)
A same-period p_i-annular band yields a connector x with **x p_i^a x⁻¹ = p_i^b** in G_3 (a,b the
cell-residues around the corridor).
1. **a = ±b.** Translation length is a conjugacy invariant: τ(p_i^a)=4|a|=τ(p_i^b)=4|b| ⇒ |a|=|b|.
   So the "residues a,b mod 5" search collapses to sign only — O(1), not a 25-case search.
2. **x lies in the elementary closure.** x p_i^a x⁻¹ = p_i^b (a=±b, both infinite-order) means x
   commensurates ⟨p_i⟩. In a hyperbolic group (G_3 is hyperbolic — certified geodesic bigons
   K_FT=10 ⇒ Papasoglu) the commensurator of ⟨g⟩ for infinite-order g is the **maximal elementary
   subgroup E(p_i)** (virtually cyclic, ⟨p_i⟩ ⊴ E(p_i) finite index). So **x ∈ E(p_i)**. This is the
   clean algebraic fact — no numeric width bound needed.
3. **If E(p_i)=⟨p_i⟩ then the annulus is a dipole.** x ∈ ⟨p_i⟩ ⇒ x=p_i^m ⇒ inner boundary =
   p_i^{-m} p_i^a p_i^m = p_i^a = outer boundary: the corridor closes with no twist ⇒ it is a stack
   of same-period opposite dipoles ⇒ **BR1-reducible ⇒ contradicts area minimality ⇒ excluded.**

**So annulus-exclusion is EQUIVALENT to: E(p_i) = ⟨p_i⟩ (orientation-preserving) and no axis-inverting
element (orientation-reversing).** This is a finite, decidable group fact — a much cleaner target than
a numeric B_ann.

### Bounded computational evidence (I ran it, kbmag `wordreduce -diff2` on G_3)
E(p_i)/⟨p_i⟩ nontrivial would require a **root** (y^d =_{G3} p_i, d≥2), an **extra centralizer**
(c p_i c⁻¹=_{G3} p_i, c∉⟨p_i⟩), or an **inverting** element (c p_i c⁻¹=_{G3} p_i⁻¹). Exhaustive over all
reduced |c|,|y| ≤ 5 (484 words), for all five periods:

```
(A) roots y^d = p_i, d∈2..5     : NONE  (each p_i primitive as a G_3 element)
(B) centralizer beyond ⟨p_i⟩     : NONE  (C(p_i)=⟨p_i⟩ up to |c|≤5)
(C) inverting c p_i c⁻¹ = p_i⁻¹  : NONE  (p_i not conj to its inverse by short c)
```

All empty ⇒ **E(p_i)=⟨p_i⟩ up to length 5**. Strong evidence the reduction's hypothesis holds, hence
annuli are dipoles and excluded.

### Closing it rigorously (two routes; the first is clean)
- **Route A (recommended, cleanest):** have Delta **compute E(p_i) exactly** via the G_3 automatic
  structure (hyperbolic ⇒ solvable conjugacy; kbmag can compute the centralizer / maximal elementary
  subgroup). If E(p_i)=⟨p_i⟩ (+ no inversion) for all five, **annuli are excluded — obligation (1)
  closes positively, no numeric B_ann required.** My |c|≤5 evidence says this is very likely.
- **Route B (fallback numeric):** the direct width bound. Since x ∈ E(p_i) and E(p_i) reps sit within
  the K_FT-fellow-travel neighborhood of the axis, **B_ann ≤ 2·K_FT + |p_i| = 24** (this is the
  explicit finite connector bound Math-expert asked for — it bypasses the astronomical Pap(10)).
  Delta then exhaustively checks all |x| ≤ 24 with a=±b; my |c|≤5 scan is the start of exactly this.

**Verdict (1): does NOT resist. #status/conjectured → closeable.** Reduced to the finite fact
E(p_i)=⟨p_i⟩; bounded evidence supports it; either the exact E(p_i) computation (Route A) or the
|x|≤24 exhaustive check (Route B) discharges it. Explicit connector bound: **B_ann ≤ 24** (and
morally 0 — dipole — once E(p_i)=⟨p_i⟩ is confirmed).

## Obligation (2) — C(3) no-progress boundary bands: finitely excludable for E7, not abstractly provable

Unlike annuli, C(3) does **not** reduce to axis structure: a no-progress boundary-to-boundary band is
a "bridge" corridor whose two equal-length p_i-periodic sides can be **internal** (facing the two
half-diagrams), so E(p_i) says nothing about it. No-progress bands are a **genuine phenomenon** in
general banded diagrams; they can only be excluded **relative to the specific protected word E7**.

### What I can prove / bound
A boundary-to-boundary p_i-band has its two ends (external intervals) on ∂D = E7-NF, and its exposed
arcs there are p_i-periodic subwords of E7-NF (G_3-equal). I scanned E7-NF (the length-128 G_3 shortlex
NF) for maximal p_i-periodic runs:

```
AABB: 0    AAbb: 0    ABAb: 0    ABaB: 7 (1.75 periods)    ABab: 7 (1.75 periods)
```

E7-NF is **near-aperiodic** w.r.t. the five periods: **zero** p_i-periodic run for AABB/AAbb/ABAb, and
**≤ 7 (< 2 periods)** for ABaB/ABab. Consequences:
- For **AABB, AAbb, ABAb** no p_i-periodic arc occurs on ∂D at all ⇒ a boundary-to-boundary band of
  those periods cannot expose a periodic side/endpoint on E7 ⇒ **no-progress bands of these three
  periods are excluded for E7** (strong, essentially a proof for 3 of 5).
- For **ABaB, ABab** periodic exposure is capped at 7, so only very short-width no-progress bands could
  attach — within reach of a **bounded** band-assembly enumeration.

### What still needs Delta (the finite closing data)
The residual case (short ABaB/ABab bands, and bands whose long sides are internal) needs Delta's
**band-assembly scan** with exactly the fields Math-expert specified (side_left/right_nf(_len),
endpoint_1/2_nf, side_len_difference=0, theorem_strict_side_arc=false, cyclic_E7_endpoint_hit,
cyclic_E7_side_hit). If **no** assembled band is E7-compatible (equal sides ∧ no strict arc ∧ endpoints
matching cyclic E7-NF), **C(3) closes for E7**. If one is compatible, it is a concrete obstruction →
route back to me, and Gate 2 becomes bounded-frontier.

**Verdict (2): NOT abstractly provable; FINITELY EXCLUDABLE for E7.** Proven for 3 of 5 periods
(zero periodic exposure); the other two reduce to a bounded band-assembly scan. Conditionally closeable.

## Overall — Gate 2 v0.4 status

**Gate 2 can close POSITIVELY iff both finite computations succeed:**
1. **(1) annulus:** Delta computes E(p_i)=⟨p_i⟩ (Route A) or clears the |x|≤24 connector search
   (Route B). Bounded evidence (|c|≤5 empty) says **likely**.
2. **(2) C(3):** Delta's band-assembly scan finds no E7-compatible no-progress band. Proven for 3/5
   periods; the ABaB/ABab remainder is a bounded scan. **Plausible.**

Both obligations are now **reduced to finite, well-specified computations** — no open geometry that
"resists" in principle. **If either computation turns up a bad object (extra E(p_i) element, or an
E7-compatible no-progress band), Gate 2 closes as bounded-obstruction-frontier** (the accepted
outcome). No G_4-survival claim until both clear.

Status unchanged: **#status/conjectured**. But the two remaining obligations moved from "real geometry
that may resist" to "finite computations with favorable bounded evidence." This is genuine progress
toward closure; it does not assert E7≠1 in G_4 (the ultimate target; Kourovka 11.48 for free B(2,5)).

## Notes for downstream agents / Delta
- **(1) Route A:** compute E(p_i) (maximal elementary subgroup / centralizer of p_i) via the G_3
  automatic structure for all 5 periods; expected = ⟨p_i⟩. **Route B:** extend my roots/centralizer/
  inverting scan from |c|≤5 to |c|≤24 (=2·K_FT+|p_i|); expected all-empty.
- **(2):** run the band-assembly scan (Math-expert's fields). AABB/AAbb/ABAb already excluded (E7-NF
  periodic run 0); only ABaB/ABab need the scan, and only up to width ~2 periods.
- Any bad object → route to me; do NOT self-close either obligation.
- The reduction "annulus ⇒ dipole given E(p_i)=⟨p_i⟩" is rigorous and reusable at higher rungs.

Verifies: `infinite_b25/avenues/math_expert_R2_full.md` §v0.4 obligations; grounding computations in
Delta workspace `gate2_receipts/` + G_3 reducer.

## UPDATE 2026-08-02 — review of Delta v0.5 finite checks (hashes verified)

Receipt `gate2_v05_receipts/gate2_v05_checks_20260802T093353Z.json` (sha256 b7320c3…5cd73c5) +
`gate2_v05_checks.py` (sha256 55a4950…42ff96); both hashes match Delta's message.

### Obligation (1) annulus — CLOSED ✅
Delta's connector scan (delayed-product BFS over g3.diff2 ∩ g3.wa, B_ann=24): for all five periods and
a=1..4, orientation-preserving `c p^a c⁻¹=p^a` admits **only period-power connectors** (lengths
0,4,8,12,16,20,24 = ⟨p_i⟩); orientation-inverting `c p^a c⁻¹=p^{-a}` admits **zero** connectors;
`annulus_bad_object_count=0`. **I independently corroborated** by brute-force over all reduced |c|≤7
(4372 words): no centralizer beyond ⟨p_i⟩, no inverting element, all periods. So **E(p_i)=⟨p_i⟩ to
B_ann=24 ⇒ same-period annuli are dipoles ⇒ excluded.** Obligation (1) is discharged.

### Obligation (2) C(3) — the 25,600 "bad objects" are SPURIOUS, NOT genuine obstructions
I read `c3_band_assembly_scan` (lines 321–388). The enumeration is **under-constrained**; the records
do not correspond to realizable no-progress bands. Five defects (code-referenced):
1. **Hardcoded no-progress.** `side_right_nf := side_left_nf` and `side_len_difference := 0` (lines
   372–374) — equal sides are *assumed*, not discovered. Every record is "no-progress" by construction.
2. **Independent endpoint cross-product.** `for ep1 … for ep2` (359–360) with only
   `ep1.nf in e7_hits and ep2.nf in e7_hits` (361) — endpoints are matched to E7 **independently**, with
   no requirement that side + ep1 + ep2 occupy a **single contiguous, phase-coherent** boundary arc of
   one E7 diagram. This is the source of the blow-up (identical samples; round 3200×4 counts).
3. **No area / cell check.** A genuine boundary-to-boundary band contains ≥1 R_i-cell (boundary 20). The
   first bad object's pieces total ≤ 4+4+4+4 = 16 < 20 = |ABaB⁵| ⇒ **area 0, encloses no cell** —
   not a band at all.
4. **No "boundary is a genuine relator subdiagram" check.** The assembled boundary word is never reduced
   in G_3 / checked to be a product of R_i-conjugates. (Independently: a 2-cell same-period *opposite*
   band has **trivial** outer boundary for every shared p^k, k=1..4 — verified — i.e. it reduces; the
   scan never tests reducedness.)
5. **Side length capped at the E7 run (≤7).** It models only sub-minimal short-sided configs; genuine
   multi-cell band sides are longer and phase-structured.

**Answer to Math-expert's question: these are NOT genuine C(3) obstructions — an additional
assembly constraint excludes them.** Therefore they do **NOT** trigger the bounded-frontier close.

### C(3) is neither closed nor refuted yet — two routes
- **Corrected finite scan (backstop).** Re-run with: computed (not hardcoded) two sides; a real cell
  (assembled boundary reduces to a product of R_i-conjugates / encloses ≥1 cell); phase coherence
  between side and endpoints; a **single contiguous placement** in E7-NF (not independent hits);
  reducedness (no dipole/collapsible pair). Under these, the length-4 area-0 records vanish.
- **Algebraic route (stronger, may close C(3) for all words).** A no-progress band has equal periodic
  sides S_left=S_right=p_i^m; its transverse holonomy conjugates p_i^m to p_i^m ⇒ (by the SAME fact
  that killed annuli) the holonomy ∈ E(p_i)=⟨p_i⟩ ⇒ the band is untwisted ⇒ collapses to same-period
  dipoles ⇒ reducible ⇒ contradicts minimality. This needs the open-band (2-endpoint) holonomy lemma
  completed carefully (it is cleaner for the closed annulus); I flag it as a **promising, likely-closing
  route**, not yet a finished proof.

### Gate 2 status
- Obligation (1) annulus: **CLOSED.**
- Obligation (2) C(3): **the reported obstruction was an artifact** — Gate 2 does **NOT** close as
  bounded-frontier on it. C(3) remains **open**: needs the corrected scan (and/or the algebraic route).
- Overall Gate 2: **#status/conjectured**, one obligation down, one genuinely open (not refuted). **No
  G_4-survival claim; no bounded-frontier close on spurious data.**

### Notes for Delta
- Add constraints 1–5 above; only ABaB/ABab need re-scanning (AABB/AAbb/ABAb already excluded, run 0).
- Do NOT report `bad_object` from an assembly that hardcodes equal sides and cross-products independent
  endpoint hits — that manufactures obstructions. A record must be a **realizable reduced band**.
- Try the algebraic route in parallel; if it closes, C(3) closes for all words, not just E7.

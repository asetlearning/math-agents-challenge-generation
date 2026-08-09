---
author: maumayma
tags: [agent/lead, user/maumayma, domain/group-theory, project/b25-infinite-witness, mirror]
---

> **MIRROR (2026-08-04).** Read-only copy for vault readability. Authoritative source:
> `algo_mixing/infinite_b25/avenues/band_contraction_core.md` (repo). If they diverge, the repo file wins.

# Assembled Proof: E7 Survives To G_4

> **Numbers note (2026-08-04, receipt avenues/setup_and_orientation_receipt.txt):** E7 has
> TWO lengths in these documents: **138** = freely reduced length in F2 (the Kourovka word,
> avenues/e7_witness.txt); **128** = its shortlex NORMAL FORM length in G_3 (the diagram
> boundary word used throughout the G_4 proof and the strict-arc scans). Both correct.


Date: 2026-08-03
Assembler role: Math Expert, #agent/math-expert
Validator final ruling: `[[2026-08-03-b25-gate2-FINAL-RULING-E7-survives-G4]]`
Validator status recorded there: `#status/proven`

## Scope

This document records the end-to-end period-band proof, as Validator ruled it:

`E7 != 1 in G_4`.

This is one ladder rung only. It does not prove `B(2,5)` infinite. It does
not resolve Kourovka 11.48. The open limit problem still requires survival
through all later `G_L`.

The group at this rung is

`G_4 = G_3 / << p_i^5 : i=1,...,5 >>`

with

`p_1=AABB`, `p_2=AAbb`, `p_3=ABAb`, `p_4=ABaB`, `p_5=ABab`.

The protected word is the weight-7 Engel word

`E7 = [a,b,b,b,b,b,b]`,

with `G_3` normal form length `128`.

## Receipt Ledger

These are the receipt pointers used in the assembled proof.

1. **Final Validator ruling.**
   `Architecture/Mixer/Documentation/Math Validation/2026-08-03-b25-gate2-FINAL-RULING-E7-survives-G4.md`.
   This ruling records the final `#status/proven` verdict for `E7 != 1 in G_4`.
2. **Ladder/setup ledger.**
   `infinite_b25/avenues/a6_bounded/kbmag/LADDER.md`.
   This records the setup check that `G_4` adds exactly the five displayed
   length-4 period relators to `G_3`, with the other four length-4 classes
   already trivial in `G_3`.
3. **Cap-conjugator finite receipt.**
   `infinite_b25/avenues/cap_conjugator_receipt.md`.
   This exhaustively checks all five periods, rotations `k=1,2,3`, and caps
   `|c|<=3`, and finds only canonical rotation conjugators up to axis powers.
4. **G_3 geodesic/axis receipts.**
   Delta `gpgeowa`/`geopairs`/`geodiff` receipts recorded in `LADDER.md`:
   geodesic bigons synchronously `10`-fellow-travel; all powers `p_i^k`
   are geodesic by DFA pumping.
5. **E7 strict-arc receipt.**
   Delta Gate-2 verifier receipt recorded in the session and `LADDER.md`:
   `E7` normal form length `128`, accepted by `g3.geowa`, has zero strict
   Dehn-arc hits for the relator exposure patterns, and max nonreducing
   exposure `7/20`.
6. **Annulus receipt.**
   Delta/Validator connector checks to `B_ann=24`, recorded in the Gate-2
   verdict chain: orientation-preserving connectors are period powers, and
   inverting connectors are absent. Validator records this as
   `E(p_i)=<p_i>` for this gate.
7. **SEI aligned receipt.**
   Delta `gate2_sei_receipts/gate2_sei_enumeration_20260802T133533Z.json`
   (sha prefix recorded by Lead as `2cbb72fe...`): `39,920` aligned SEI
   records, all with literal zero-contour two-cell reduction witnesses,
   no exceptional aligned SEI survivors.
8. **Aligned C(3) ruling.**
   Validator final ruling, quoted verbatim below: aligned boundary bands close
   by the same local cancellable-pair theorem; no separate cross-product scan
   is required.

## Lemma Status Summary

The statuses in this table are Validator's rulings, not independent stamps by
Math Expert.

| Link | Statement | Validator status / receipt |
| --- | --- | --- |
| Setup | `G_4 = G_3/<<p_i^5>>` for exactly the five listed periods | Discharged in `LADDER.md` and final ruling |
| E7 data | `E7` is `G_3`-geodesic, length `128`, zero strict hits | Verified by Delta strict-arc DFA; final ruling |
| Axis data | all powers `p_i^k` geodesic in `G_3` | DFA pumping receipt; final ruling |
| Piece core | distinct-period realized pieces have length `<=3` | Validator proved from periodicity |
| SO | long same-period contacts are opposite-oriented | Validator certified |
| Annuli | same-period annuli reduce to dipole/period-power cases | Closed via `E(p_i)=<p_i>` to `B_ann=24` |
| H2 | phase connectors are single-cell caps or beaded ordinary pieces | Discharged after Section 11.8 correction |
| Lemma B/C | cap transporters are canonical and phase offsets absorb | Lemma B validated; Lemma C valid after H2; cap receipt |
| Aligned bands | aligned same-period bands contain a cancellable pair | Final ruling paragraph below |
| Internal contraction | BR2 contraction and ledger termination | Lemma 2.1/2.2 accepted after fix |
| Curvature | ordinary realized-piece `C'(1/6)` Greendlinger | Lemma 3.1 accepted |
| Transfer | boundary exposure transfers to strict `E7` arc | Lemma 4.1 sound conditional; conditions met |

## Proof

Assume for contradiction that `E7=1` in `G_4`. Choose a minimal relative disc
diagram `D` over `G_3 + {p_i^5}` with boundary label the `G_3` normal form of
`E7`. Minimality is by number of `R`-cells first, then by the long-contact
ledger used in the band-reduction argument.

Each `R`-cell is a cyclic conjugate of `p_i^5` or `p_i^{-5}` and has perimeter
`20`. The all-powers geodesic certificate gives geodesic axes for the five
periods.

### 1. Ordinary Pieces

A realized piece means a shared edge-arc between two relator cells after the
same-period band structure is accounted for. Validator's piece-core theorem
says distinct-period pieces have length at most `3`: every length-4 factor of
`p_i^infinity` is a cyclic rotation of `p_i`, and the five periods are
primitive and pairwise distinct up to cyclic shift/inverse.

Thus any realized contact of length at least `4` is same-period.

### 2. Orientation

Validator certified the orientation theorem (SO): every long same-period
contact is opposite-oriented. Along a shared edge, the two incident cell
boundaries read inverse labels. A same-oriented long contact would force some
rotation of `p_i` to equal a rotation of `p_i^{-1}`; the cyclic-inverse checks
exclude this for all five periods and cross-pairs.

Therefore every long same-period contact is between a `p^5` cell and a
`p^{-5}` cell.

### 3. Annuli

Same-period annuli are excluded. The routed connector computation to
`B_ann=24`, corroborated by Validator, gives `E(p_i)=<p_i>` for the five
periods at this gate: preserving connectors are period powers and no inverter
exists. A same-period annulus is therefore a period-power/dipole stack and
contradicts minimality.

### 4. Phase Connectors And Phase Absorption

The block subdivision of each `p^5` cell is label-determined and canonical:
once the cyclic conjugate of `p^5` is fixed, the five length-4 `p`-blocks are
the consecutive copies in the cyclic label.

Validator discharged H2 in two parts.

First, a genuine phase cap at the end of a long same-period contact is a
single cell-boundary cap of length `0`, `1`, `2`, or `3`. Lemma B says such a
cap satisfies the local transporter equation

`c rot_k(p) c^{-1} =_{G_3} p`

or the orientation-reversed variant. The cap-conjugator receipt checks all
caps `|c|<=3` and finds only the canonical rotation conjugator coset
`u_k <rot_k(p)>`, with the listed short axis-power duplicates. Lemma C then
absorbs phase offsets into the `p`-axis coordinate.

Second, a beaded bridge is not a phase cap. It is a path made of ordinary
realized pieces. Each bead has length at most `3`; otherwise it would be a
forbidden distinct-period piece of length at least `4`, or a same-period long
contact already belonging to the band ledger. Thus each bead is individually
a `C'(1/6)` piece because `3/20 < 1/6`. Beaded paths do not combine with
long pocket contacts into new ordinary pieces: long contacts remain charged
to the band ledger, while beads are edge-arcs between vertices. Validator's
final beaded ruling accepts this per-piece argument.

Consequently every phase-offset pocket reduces to an aligned pocket plus
ordinary `C'(1/6)` pieces.

### 5. Aligned Same-Period Bands Vanish

The last gate is the aligned boundary-band closure. The following paragraph is
quoted verbatim from Validator's final ruling
`[[2026-08-03-b25-gate2-FINAL-RULING-E7-survives-G4]]`:

> Let B be an aligned same-period boundary-to-boundary band in a minimal relative diagram D over G_3+{p_i^5} with ∂D = E7-NF. By the band definition B contains a long same-period contact α (|α|≥4). By the orientation theorem (Lemma SO, certified: no p_i is cyclically conjugate to its inverse, and no cross-pair p_i ~cyc p_j⁻¹), the two cells C,C′ sharing α are opposite-oriented (p^5 and p^{-5}). Since B is aligned (phase offsets already absorbed by H2 / Lemma C), C and C′ are phase-aligned across α, so their outer contour β_C·β_{C′} freely reduces to the empty word — β_{C′}=β_C⁻¹ by alignment. I verified this is general: contour ≡ ε for every contact length |α|=4..19 and all five periods (not a finite enumeration). Hence {C,C′} is a van Kampen cancellable pair. By the cancellable-pair reduction theorem, removing it yields a diagram with the same boundary word E7-NF and two fewer R-cells — contradicting area-minimality of D. (Pure two-interval sub-case, both cells external: their mutually-inverse external arcs would put a freely-reducible spur u·u⁻¹ into E7-NF, contradicting E7-NF geodesic — so it cannot arise.) Therefore no aligned same-period band of any cell-count or any number of external boundary intervals survives in a minimal E7 diagram. The external-interval count plays no role; aligned C(3) = aligned SEI closure. ∎

This single local move covers aligned SEI, aligned C(3), and aligned internal
same-period pockets. The SEI enumeration gives additional witnessed
corroboration for the one-external-interval aligned case, but Validator's
final ruling makes the aligned C(3) cross-product scan unnecessary.

Therefore no same-period band survives in the minimal diagram `D`.

### 6. Internal BR2 Contraction

The corrected Lemma 2.1 applies to harmless internal disc bands with
`G_3`-equal chord sides. The contraction is BR2 band-compression: delete the
banded pocket and identify the equal chord sides. This preserves the external
boundary and reduces `R`-area.

Lemma 2.2 uses lexicographic termination by `(R-area, unbanded long-contact
ledger)`: BR2 lowers area; re-banding removes unbanded long same-period
contacts from the ledger. The fix explicitly avoids the invalid side-vs-side
shortening language.

Together with the aligned cancellable-pair theorem, this removes the remaining
long same-period contacts from a minimal counterexample or contradicts its
minimality.

### 7. The Ordinary `C'(1/6)` Disc

After the previous reductions, any remaining realized internal piece has
length at most `3`:

1. distinct-period pieces have length at most `3`;
2. same-period contacts of length at least `4` would be a band, already
   removed or impossible;
3. beaded bridges are ordinary pieces of length at most `3`.

Since all relator cells have perimeter `20`, every realized piece has length
less than `20/6`. Thus the remaining nonempty diagram is an ordinary reduced
realized-piece `C'(1/6)` disc.

### 8. Greendlinger

By Lyndon-Schupp, Combinatorial Group Theory, Chapter V, Theorem 4.5, applied
to the realized pieces in this band-reduced disc, some relator cell has a
boundary exposure containing the complement of at most three internal pieces.
Those pieces have total length at most `9`, so the exposed boundary arc has
length at least `11`; in Validator's endpoint convention this gives the
strict theorem threshold `>=12`, with complementary path length at most `8`.

Validator accepted this curvature step as Lemma 3.1.

### 9. Transfer To E7

Internal contractions and cancellable-pair reductions preserve the external
boundary word `E7-NF`. Therefore the Greendlinger boundary exposure transfers
back to a strict Dehn arc on the original `E7` boundary: a subword of `E7-NF`
of length at least `12` equal in `G_3` to a complementary relator path of
length at most `8`.

Validator accepted this as Lemma 4.1 once the boundary-preservation hypotheses
above were verified.

### 10. Contradiction

Delta's strict-arc verifier reports that cyclic `E7-NF` has zero such strict
hits. The same receipt records `E7-NF` as a `G_3` geodesic word of length
`128`.

Thus the minimal counterexample diagram `D` cannot exist. Hence, as Validator
ruled in the final composition note,

`E7 != 1 in G_4`.

## What This Does Not Say

This proof does not establish `E7 != 1` in the free Burnside group `B(2,5)`.
It does not establish infiniteness of `B(2,5)`. It establishes survival of
`E7` through the fourth ladder quotient only:

`G_4 = F_2 / << w^5 : |w| <= 4 >>`.

The ladder reformulation says the limit problem would require survival through
all later rungs. Those rungs remain open.


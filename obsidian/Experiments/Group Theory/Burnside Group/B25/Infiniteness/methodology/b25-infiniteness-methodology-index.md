---
title: "B25 Infiniteness — methodology index (how the E7 ladder proof works)"
date: 2026-08-04
domain: group-theory
project: b25
instance: b25-infinite-witness
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/burnside-infiniteness, topic/small-cancellation, topic/van-kampen, project/b25, methodology]
---

# Methodology index — the E7 ladder and the G4 period-band proof

This folder holds the *methods* behind [[e7-survives-g4-2026-08-03]]. Two documents carry the
mathematics; this note is the reading order and the map between them.

- [[ladder]] — the ladder reformulation and the rung-by-rung record (G1–G4).
- [[assembled-proof]] — the full assembled G4 proof (`band_contraction_core.md` mirror).

For the evidence and receipts behind every claim, see the results synthesis:
[[b25-infiniteness-results-synthesis]]. Raw logs & code: [[b25-infiniteness-data-index]].

---

## 1. The reformulation (why a "ladder")

The open problem is: **is B(2,5) infinite?** The reduction chain turns this into a single-word
survival question, then splits that question into a countable tower of finite-in-principle rungs.

1. **Kernel.** `ker(B(2,5) -> R(2,5)) = gamma_13`, and R(2,5) has order 5^34, class 12. So
   **B(2,5) infinite <=> gamma_13 != 1**.
2. **Witness.** `E7 = [a,b,b,b,b,b,b]` lives in gamma_13 and is `= 1` in R(2,5) but not below the
   Engel boundary. So **E7 != 1 in B(2,5) => B(2,5) infinite** (Kourovka 11.48, still open).
3. **Ladder.** `E7 != 1 in B(2,5) <=> E7 != 1 in G_L for EVERY L`, where
   `G_L = F2 / <<w^5 : |w| <= L>>`. Each rung is decidable-in-principle; the *limit* is the open
   problem.

Full statement and the rung table: [[ladder]].

## 2. The rungs, and where each is proven

| rung | method | where the method lives | trust basis |
|---|---|---|---|
| G1 | C5 * C5 free-product normal form | [[ladder]] §"Proven rungs" | elementary |
| G2 | verified automatic structure (KBMag) | [[ladder]] · data: [[g2.success]] | standard tool |
| G3 | verified automatic structure (KBMag) | [[ladder]] · data: [[g3.success]] | standard tool |
| **G4** | **period-band small-cancellation (new)** | **[[assembled-proof]]** | hand proof + receipts + Validator |
| G5+ | — | — | open |

G1–G3 fall to Knuth–Bendix. At G4 the automatic-structure build hits a word-difference blowup
(see data: [[LADDER_G4]], [[autgroup_g4_large.log]]), so G4 needed a new mathematical argument —
that argument is [[assembled-proof]].

## 3. The G4 argument in one screen (map into the assembled proof)

Proof by contradiction over van Kampen diagrams. Assume `E7 = 1` in G4; take a **minimal**
diagram D over `G3 + {p_i^5}` with boundary = the G3 normal form of E7 (length 128).

| step | what it establishes | section in [[assembled-proof]] |
|---|---|---|
| Setup | G4 = G3 / 5 period relators; E7-NF geodesic | §Scope, §1 |
| Piece-core | distinct-period overlaps <= 3 (below C'(1/6)) | §2 |
| Orientation (SO) | every long same-period contact is opposite-oriented | §3 |
| Annuli | E(p_i) = <p_i>; same-period annuli are dipoles, excluded | §4 |
| Phase absorption (H2) | every phase connector is a short cap or a harmless beaded bridge | §11.1, §11.8 |
| **Aligned bands vanish (crux)** | **aligned opposite pairs cancel — a van Kampen cancellable pair** | **§5** |
| Internal contraction (BR2) | internal discs compress; residual pieces <= 3 | §6 |
| Ordinary C'(1/6) disc | every realized piece <= 3, and 3/20 < 1/6 | §7 |
| Greendlinger | some cell exposes >= 12 consecutive relator letters | §8 (Lyndon–Schupp V.4.5) |
| Transfer + contradiction | exposure transfers to a strict Dehn arc on E7-NF — but E7-NF has zero strict arcs | §9 |

The single hardest move is **§5 (aligned bands vanish)** — it is what replaces classical small
cancellation, which provably fails on Burnside presentations because of same-period overlaps. Its
finite computational core (all 8,000 opposite gluings cancel) is receipt
[[cancellable_pair_receipt.py]] / [[cancellable_pair_receipt.txt]].

## 4. Why the standard theorems do not apply at exponent 5

This is a regime where the published filling/small-cancellation theorems provably do not reach —
which is why a bespoke, computer-checked argument was needed:

- Agol–Groves–Manning requires **torsion-free**; B(2,5) is all torsion.
- Dahmani–Guirardel–Osin needs cone radius ~5e12; here injectivity radius <= 20.
- Coulon requires exponent **> 100**; here it is 5.

Citations and the receipts confirming ball-injectivity fails at radius 20 (5 explicit kernel
elements) are in [[ladder]] §"Rung-4 filling data" and data-file [[setup_and_orientation_receipt.txt]].

## 5. What is proven vs what is open (read before sharing)

- **Proven:** `E7 != 1 in G_4`. First certified per-level period-band step at exponent 5.
- **Open:** B(2,5) infinite; Kourovka 11.48 (E7 in *free* B(2,5)). Climbing rungs one-by-one is a
  treadmill — the real theorem is a **uniform-in-L inductive step**. See
  [[e7-survives-g4-2026-08-03]] §"What next".

## Verification

Every load-bearing step maps to an openable verdict and/or a replayable receipt. The end-to-end
map claim -> log -> code is the synthesis: [[b25-infiniteness-results-synthesis]]. The Validator's
final ruling is [[2026-08-03-b25-gate2-FINAL-RULING-E7-survives-G4]].

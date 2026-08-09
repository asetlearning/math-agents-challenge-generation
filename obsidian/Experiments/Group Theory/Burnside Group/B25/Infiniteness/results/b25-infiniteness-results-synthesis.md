---
title: "B25 Infiniteness — results synthesis (every claim -> its log & code)"
date: 2026-08-04
domain: group-theory
project: b25
instance: b25-infinite-witness
author: maumayma
status: proven
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/burnside-infiniteness, topic/engel-word, topic/small-cancellation, project/b25, status/proven, results, synthesis]
---

# Results synthesis — E7 survives to G4

> **One-line result.** `E7 = [a,b,b,b,b,b,b]` is **nontrivial in G4 = G3/<<p_i^5>>** (five length-4
> periods). First certified period-band small-cancellation step at exponent 5.
> **Scope:** one rung. It does **NOT** prove B(2,5) infinite and does **NOT** resolve Kourovka 11.48.

This note is the readable audit trail. **Every "we checked X" sentence links to the actual output
log and the code that produced it** — either copied into this experiment's `data/` folder (linked)
or, for large binaries, given by local repo path. Reading order for the math itself:
[[b25-infiniteness-methodology-index]] -> [[ladder]] -> [[assembled-proof]].

---

## A. The reduction chain (GAP) — checked facts

These establish *why E7 is the right word*: the kernel is gamma_13, the Engel boundary is exactly
6, and E7 vanishes in R(2,5) under both commutator conventions.

| we checked... | verdict (quoted from log) | log | code |
|---|---|---|---|
| R(2,5) has order 5^34, nilpotency **class 12** (not folklore 13) | `Size = 5^34`, `NilpotencyClass = 12` | [[02_r25.out]] | [[02_r25.g]] |
| Homomorphism phi into R(2,5) is sane | see log | [[03_phi_sanity.out]] | [[03_phi_sanity.g]] |
| Candidate witnesses enumerated | 128-entry candidate list | [[04_candidates.out]] · [[candidates.txt]] | [[04_candidates.g]] |
| Candidates verified against R(2,5) | see log | [[06_verify_candidates.out]] | [[06_verify_candidates.g]] |
| **Engel boundary = 6:** `[a,6b]=1`, `[a,5b]!=1` in R(2,5) | `[a,5*b] trivial ... : false` / `[a,6*b] trivial ... : true` | [[07_engel.out]] | [[07_engel.g]] |
| **E7 = 1 in R(2,5) under BOTH conventions** | `Conv1 ... E7 trivial ... : true` / `Conv2 ... E7 trivial ... : true` | [[08_convention.out]] | [[08_convention.g]] |

Narrative: [[gap/SUMMARY|SUMMARY]] (in `data/gap/`). Full index: [[b25-infiniteness-data-index]] §1.

## B. The ladder rungs G1–G3 (KBMag) — checked facts

E7 reduces to a nonempty normal form at each of the first three rungs, so it is nontrivial there.

| we checked... | verdict | log | code / flag |
|---|---|---|---|
| G2 is a verified automatic structure | `gpaxioms` pass | [[ladder]] §"Proven rungs" | flag: [[g2.success]] |
| G3 is a verified automatic structure | `gpaxioms` pass, `g3.axioms.ec = 0` | [[ladder]] §"Proven rungs" | flag: [[g3.success]] |
| E7 reduces to a nonempty 128-letter NF in G3 | `reduces to: A*b*a*b*...` (128 letters) | [[e7_diff2_result.txt]] | inputs: [[e7_input.txt]] · [[e7_kb.txt]] |
| G4 automatic build hits word-difference blowup (why G4 needed new math) | build did not converge | [[autgroup_g4_large.log]] | attempt log: [[LADDER_G4]] |

> **Two methods, don't confuse them.** The KBMag *automatic-structure build* for G4 did **not**
> finish (row above). That is the only thing "in progress." **G4 is nonetheless proven** — by the
> period-band hand-proof in §C below (`#status/proven`, Validator PASS). If the build ever
> completes it would give a *second, independent* confirmation of the already-proven rung; it is
> not needed for the result.

## C. The G4 proof — the load-bearing receipts

Each row is a step in [[assembled-proof]]; the receipt is the finite computation that closes it.

| claim in the proof | verdict (quoted from receipt) | log | code |
|---|---|---|---|
| **Setup:** G4 adds exactly 5 genuinely-new relators; 4 length-4 classes redundant in G3; **zero** cyclic-inverse collisions; E7 lengths 138 (F2) / 128 (G3-NF) | `added: 9 ...`, 5 `genuinely new`, `cyclic-conjugacy collisions ... : NONE`, `138` / `128` | [[setup_and_orientation_receipt.txt]] | — (scan) |
| **Aligned bands vanish (crux, §5):** all opposite gluings cancel, no offset gluing does | `aligned ... contour==empty 8000, contour!=empty 0` · `VERDICT: PASS` | [[cancellable_pair_receipt.txt]] | [[cancellable_pair_receipt.py]] |
| **Cap-conjugator census (H2, §11.1):** only trivial rotation caps, **zero exotic** | `caps enumerated: 53` · `solutions: 34; EXOTIC ... : NONE` | [[cap_conjugator_check.txt]] | [[cap_conjugator_check.py]] |
| E7 as a freely-reduced F2 word (138 chars) | the witness word | [[e7_witness.txt]] | — |

Cap census narrative: [[cap_conjugator_receipt]].

## D. Large machine receipts (Delta Gate-2) — local repo only

Too large to copy into the vault; hash-frozen, replayable. Paths are in the local repo under
`DW = algo_mixing/.maestri/roles/8f9f252e-bccd-4cb9-b836-6cf90167b5ea`.

| corroborates... | local path | size |
|---|---|---|
| Aligned-SEI (39,920 zero-contour witnesses) — corroborates the §5 crux | `DW/gate2_sei_receipts/gate2_sei_enumeration_20260802T133533Z.json` | 77 MB |
| Dehn-arc DFA: E7-NF has zero strict hits (step 9/10) | `DW/gate2_receipts/dehn_arc_dfa_*.json` | 86 KB ea |
| Annulus / E(p)=<p> checks (B_ann=24, step 4) | `DW/gate2_v05_receipts/gate2_v05_checks_*.json` | 34 MB |
| Replay chain + sha256 | `DW/REPLAY.md` | 13 KB |

Full listing with every receipt: [[b25-infiniteness-data-index]] §4.

## E. Evidence layer (first night, Stallings foldings) — supporting, not load-bearing

E7 is **not** a product of fifth powers with roots up to length 15 (a ~1e9-edge computation,
Rust/Python cross-validated). This is corroboration for the ladder, not part of the G4 proof.

| we checked... | verdict (quoted from log) | log | code |
|---|---|---|---|
| E7 not a product of fifth powers, roots <= 15 | `MEMBER=False M=15 E7` (460M folded vertices) | [[out_M15.txt]] | [[fold.py]] · [[fold.rs]] |
| same, roots <= 11..14 | `MEMBER=False` at every M | [[out_M11.txt]] … [[out_M14.txt]] | [[fold.py]] |

Timings [[time_M11.txt]] … [[time_M15.txt]]. Summary [[stallings/SUMMARY|SUMMARY]] (in `data/stallings/`).
Binary (local only): `AV/stallings/rust/fold` (416 KB).

## F. The verification record (Validator)

The proof passed a multi-gate Validator review; each gate is a note where a specific defect was
caught and fixed. The final ruling stands on the assembled written proof.

- **Final ruling (PASS):** [[2026-08-03-b25-gate2-FINAL-RULING-E7-survives-G4]]
- Review chain (defects caught, in order): [[2026-08-02-b25-gate2-period-band-metatheorem]] ·
  [[2026-08-02-b25-gate2-curvature-core-review]] · [[2026-08-02-b25-gate2-unified-lemma-U-review]] ·
  [[2026-08-02-b25-gate2-annulus-and-C3-proofs]] · [[2026-08-02-b25-gate2-SEI-receipts-and-batch-rulings]] ·
  [[2026-08-02-b25-gate2-H2-decisive-review]] · [[2026-08-02-b25-gate2-beaded-lemma-review-and-final-gate]] ·
  [[2026-08-02-b25-gate2-FINAL-composition-verdict]]
- Lemma -> receipt map: [[provenance-map]].

## G. Honest caveats (state these when sharing)

1. The verification **record** is complete and machine-receipted. The **mathematical correctness**
   of the argument still deserves a human referee's read — especially the crux §5 (aligned bands
   vanish) and its "all contact lengths 4..19" generality.
2. This is **one rung**. Never frame G4 as progress toward infiniteness beyond the four proven
   rungs. Headline: *E7 survives to G4* — nothing more.

## What next

The only route that closes B(2,5) is a **uniform-in-L inductive step** ("E7 survives to G_L =>
survives to G_{L+1}" with L-independent constants). Climbing rungs one-by-one is a treadmill.
Second confirmation of G4 would come from letting the independent automatic-structure build finish.
Detail: [[e7-survives-g4-2026-08-03]] §"What next".

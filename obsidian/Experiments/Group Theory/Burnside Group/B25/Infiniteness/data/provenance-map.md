---
author: maumayma
tags: [agent/lead, user/maumayma, domain/group-theory, project/b25-infinite-witness, mirror]
---

> **MIRROR (2026-08-04).** Read-only copy for vault readability. Authoritative source:
> `algo_mixing/infinite_b25/PROVENANCE.md` (repo). If they diverge, the repo file wins.

# PROVENANCE — every load-bearing component of "E7 survives to G₄", with openable files

Compiled by Lead 2026-08-04 at Maria's request. Ground rule applied: a component counts as
**proven** only if backed by an openable written verdict and/or machine receipt; anything
verified only in conversation was re-receipted on 2026-08-04 (marked NEW below) before this
table was written. After the 2026-08-04 additions, **no load-bearing component is
conversation-only.**

Paths: `MV` = `~/Documents/Obsidian/Math/obsidian/Architecture/Mixer/Documentation/Math Validation`,
`AV` = `algo_mixing/infinite_b25/avenues`, `KB` = `AV/a6_bounded/kbmag`,
`DW` = `algo_mixing/.maestri/roles/8f9f252e-bccd-4cb9-b836-6cf90167b5ea` (Delta workspace).

> **Vault copies.** Small readable artifacts (GAP scripts+outputs, receipt code+txt, KBMag logs,
> Stallings summary+code, agent logs) are copied into this experiment's `../data/` subfolders —
> see [[b25-infiniteness-data-index]]. Large binaries (77 MB SEI JSON, 14 MB kbprog.live, the Rust
> `fold` binary) stay in the local repo at the `AV`/`DW` paths above and are linked, not copied.

| # | Component (role in proof) | Written verdict (file) | Machine receipt (file) |
|---|---|---|---|
| 1 | Setup: G₄ = G₃ + exactly {AABB,AAbb,ABAb,ABaB,ABab}⁵ | `MV/2026-08-03-…FINAL-RULING…` (ladder discharged) | `AV/setup_and_orientation_receipt.txt` (NEW 08-04; relator scan + 9 wordreduce verdicts) |
| 2 | Piece bound: distinct-period pieces ≤ 3 | `MV/2026-08-02-b25-gate2-annulus-and-C3-proofs.md` (Validator proof) | `DW/gate2_receipts/gate2_g3_raw_receipts_*.json` (arc-collision scans) |
| 3 | Orientation theorem (long same-period contacts opposite) | `MV/2026-08-02-…SEI-receipts-and-batch-rulings.md` (certified) | input: `AV/setup_and_orientation_receipt.txt` (NEW; zero cyclic-inverse collisions, all pairs); corroboration: SEI receipt (0 same-orientation in 6.4M) |
| 4 | Annuli closed: E(pᵢ)=⟨pᵢ⟩ to B_ann=24 | `MV/2026-08-02-…annulus-and-C3-proofs.md` | `DW/gate2_v05_receipts/gate2_v05_checks_20260802T093353Z.json` |
| 5 | Axis theorem: NF(pᵢᵏ)=pᵢᵏ all k, all ten rays | `MV/2026-08-02-…period-band-metatheorem.md` §UPDATE (independent verification) | `DW/gate2_receipts/gate2_g3_raw_receipts_20260802T091555Z.json` (v0.4 pumping) |
| 6 | Cap-conjugator: zero exotic caps ≤3 | `MV/2026-08-02-…unified-lemma-U-review.md` (independently corroborated) | `AV/cap_conjugator_receipt.md` + `AV/cap_conjugator_check.py/.txt` (NEW replay 08-04: 34 solutions, 0 exotic — matches) |
| 7 | Lemma B (phase-cap transporter) + Lemma C (absorption) | `MV/2026-08-02-…unified-lemma-U-review.md` (B VALID incl. external caps) | finite input = row 6 |
| 8 | H2 single-cell case (§11.2, block-normalization) | `MV/2026-08-02-…H2-decisive-review.md` (airtight; canonical-blocks clarification ordered+landed) | — (pure math, verdict-backed) |
| 9 | H2 beaded case (§11.8, per-piece) | `MV/2026-08-02-…beaded-lemma-review-and-final-gate.md` (conclusion accepted, per-piece; pigeonhole rejected+removed) | census: `DW/gate2_c3_two_interval_receipts/gate2_c3_beaded_phase_bridge_addendum_20260802T164815Z.json` (corroborative, not load-bearing) |
| 10 | SEI aligned closure | `MV/2026-08-02-…SEI-receipts-and-batch-rulings.md` (aligned accepted, size-independent) | `DW/gate2_sei_receipts/gate2_sei_enumeration_20260802T133533Z.json` (74MB, 39,920 exhibited witnesses) |
| 11 | Cancellable-pair theorem (aligned bands vanish; closes C(3)) | `MV/2026-08-03-…FINAL-RULING…` (Validator's paragraph + their m=4..19 check) | `AV/cancellable_pair_receipt.py/.txt` (NEW 08-04: exhaustive 8,000 gluings, all aligned cancel; **no exact phase-offset gluing exists at contact ≥ 4**) |
| 12 | BR2 internal contraction (L2.1/2.2, fixed defn) | `MV/2026-08-02-…curvature-core-review.md` §UPDATE (fix confirmed) | — (pure math, verdict-backed) |
| 13 | Greendlinger (L3.1, C′(1/6), exposure ≥ 12) | `MV/2026-08-02-…curvature-core-review.md` (ACCEPT—VALID) | classical: Lyndon–Schupp Ch.V Thm 4.5 |
| 14 | Transfer (L4.1, strict arc back to ∂D) | `MV/2026-08-02-…curvature-core-review.md` (ACCEPT cond., discharged in composition) | — |
| 15 | E7 zero strict Dehn arcs; exposure ≤ 7/20 | ruling relies on it; reviewed in SEI batch | `DW/gate2_receipts/dehn_arc_dfa_*.json` + `gate2_g3_raw_receipts_*.json` |
| 16 | Final composition + FINAL READ PASS of assembled doc | `MV/2026-08-03-b25-gate2-FINAL-RULING-E7-survives-G4.md` (incl. §final read, line 78) | — |

## Numbers reconciliation (Maria item 2)

Both numbers are correct; they measure different things (receipt: `AV/setup_and_orientation_receipt.txt`):
- **138** = length of E7 = [a,b,b,b,b,b,b] as a **freely reduced word in F₂** (`AV/e7_witness.txt`).
  This is the object of Kourovka 11.48 and of the Stallings/expansion certificates.
- **128** = length of E7's **shortlex normal form in G₃** (wordreduce -diff2 g3). This is the
  boundary word of the van Kampen diagrams in the G₄ proof and the word scanned for strict arcs.
Documents have been annotated accordingly; any sentence calling E7 "138-letter" refers to F₂,
any "128-letter" to the G₃ normal form.

## Evidence-chain freeze

`DW/REPLAY.md` (13.1K) lists the Delta receipt chain with sha256 hashes and replay commands.

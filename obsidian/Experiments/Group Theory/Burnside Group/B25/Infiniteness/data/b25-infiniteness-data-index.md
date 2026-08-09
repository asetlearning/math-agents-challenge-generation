---
title: "B25 Infiniteness — data & artifact index (E7 survives to G4)"
date: 2026-08-04
domain: group-theory
project: b25
instance: b25-infinite-witness
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/burnside-infiniteness, project/b25, status/proven, data]
---

# Data & artifact index — E7 survives to G4

Every artifact behind [[e7-survives-g4-2026-08-03]]. Small readable files are copied into this
`data/` folder (linked below). Large binaries stay in the local repo (path given, not copied).

**Repo root:** `algo_mixing/infinite_b25/` — abbreviated `AV = .../avenues`,
`DW = algo_mixing/.maestri/roles/8f9f252e-bccd-4cb9-b836-6cf90167b5ea` (Delta workspace).

Lemma → receipt map (authoritative): [[provenance-map]].

---

## 1. GAP — kernel, Engel boundary, convention checks

Folder: `gap/`. These establish the reduction chain (class 12, E7 = 1 in R(2,5), Engel boundary = 6).

| what was checked | script | output log |
|---|---|---|
| GAP packages load | [[01_packages.g]] | [[01_packages.out]] |
| Build R(2,5), size 5^34, class 12 | [[02_r25.g]] | [[02_r25.out]] |
| Homomorphism phi sanity | [[03_phi_sanity.g]] | [[03_phi_sanity.out]] |
| Candidate witnesses | [[04_candidates.g]] | [[04_candidates.out]] |
| Calibration | [[05_calibration.g]] | [[05_calibration.out]] |
| Verify candidates | [[06_verify_candidates.g]] | [[06_verify_candidates.out]] |
| **Engel boundary = 6** ([a,6b]=1, [a,5b]!=1 in R(2,5)) | [[07_engel.g]] | [[07_engel.out]] |
| **E7 = 1 in R(2,5) under both commutator conventions** | [[08_convention.g]] | [[08_convention.out]] |

Narrative summary: [[gap/SUMMARY|SUMMARY]] (in `gap/`). Candidate list: [[candidates.txt]].

## 2. Ladder rungs G1–G3 (KBMag automatic structures)

Folder: `kbmag/`. G2, G3 are verified automatic structures; E7 reduces to a nonempty normal form.

| artifact | file | note |
|---|---|---|
| Ladder record (rungs 1–4, receipts) | [[ladder]] (methodology) | full rung table |
| G4 attempt log | [[LADDER_G4]] | word-difference blowup (why G4 needed new math) |
| G2 confluence success flag | [[g2.success]] | gpaxioms pass |
| G3 confluence success flag | [[g3.success]] | gpaxioms pass |
| E7 -diff2 reduction result | [[e7_diff2_result.txt]] | E7 → 128-letter NF |
| E7 kbmag input | [[e7_input.txt]] · [[e7_kb.txt]] | |
| autgroup logs | [[autgroup_g4.log]] · [[autgroup_g4_large.log]] | G4 build attempts |

**Large binaries (local repo only, not copied):** `AV/a6_bounded/kbmag/g3.kbprog.live` (1.0 MB),
`.../backup_prev_run/g4.kbprog.live` (14 MB), `g3.gm` / `g3.diff2` word-difference machines.

## 3. G4 proof receipts (the finite inputs, replayable)

Folder: `receipts/`. Each is standalone-runnable; verdicts quoted in the synthesis.

| claim in proof | code | output |
|---|---|---|
| **Aligned bands vanish** (crux): all 8,000 opposite gluings cancel, no offset gluing exists | [[cancellable_pair_receipt.py]] | [[cancellable_pair_receipt.txt]] |
| **Cap-conjugator census:** 34 solutions, 0 exotic caps | [[cap_conjugator_check.py]] | [[cap_conjugator_check.txt]] · [[cap_conjugator_receipt]] |
| **Setup + orientation:** G4 adds exactly 5 relators; zero cyclic-inverse collisions; 138 vs 128 lengths | — | [[setup_and_orientation_receipt.txt]] |
| E7 as a freely-reduced F2 word (138 chars) | — | [[e7_witness.txt]] |

## 4. Delta Gate-2 machine receipts (large JSON, local repo only)

Folder: `DW/` in the local repo. Hash-frozen; replay commands in `DW/REPLAY.md`.

| receipt | local path | size |
|---|---|---|
| Aligned-SEI enumeration (39,920 zero-contour witnesses) | `DW/gate2_sei_receipts/gate2_sei_enumeration_20260802T133533Z.json` | 77 MB |
| G3 raw receipts (axis pumping, arc collisions) | `DW/gate2_receipts/gate2_g3_raw_receipts_*.json` | ~3.5 MB ea |
| Dehn-arc DFA (E7 zero strict hits) | `DW/gate2_receipts/dehn_arc_dfa_*.json` | 86 KB ea |
| Annulus / E(p)=<p> checks (B_ann=24) | `DW/gate2_v05_receipts/gate2_v05_checks_*.json` | 34 MB |
| Holonomy scan | `DW/gate2_v06_receipts/gate2_v06_holonomy_*.json` | 4.3 MB |
| Beaded phase-bridge census (corroborative) | `DW/gate2_c3_two_interval_receipts/*.json` | ~2 MB |
| Replay chain + sha256 | `DW/REPLAY.md` | 13 KB |

Human-readable summaries of each are in each receipt folder's `latest_summary.md` (local repo).

## 5. Evidence layer — Stallings foldings (first night)

Folder: `stallings/`. E7 not a product of fifth powers with roots <= 15 (~1e9-edge computation).

| artifact | file |
|---|---|
| Summary | [[stallings/SUMMARY|SUMMARY]] (in `stallings/`) |
| Python folder | [[fold.py]] |
| Rust folder source | [[fold.rs]] · [[README]] |
| Outputs M11–M15 | [[out_M11.txt]] … [[out_M15.txt]] |
| Timings M11–M15 | [[time_M11.txt]] … [[time_M15.txt]] |

**Binary (local only):** `AV/stallings/rust/fold` (416 KB compiled).

## 6. Agent working logs

Folder: `agent-logs/`. Round-by-round working notes.

- [[b25exp_R1]] · [[math_expert_R1]] · [[math_expert_R2b]] · [[researcher_R1]]

Full briefs and R1/R2 math-expert write-ups remain in the repo: `AV/math_expert_R1_full.md`
(36 KB), `AV/math_expert_R2_full.md` (81 KB), `AV/brief_*.md`.

---

## Not copied — why

Vault stays lean: files > ~100 KB or compiled binaries (SEI JSON 77 MB, kbprog.live 14 MB, v05
34 MB, Rust `fold`) live in the local repo and are linked by path above. Everything a reader needs
to follow the proof — GAP scripts+outputs, the three G4 receipt scripts, KBMag logs, Stallings
code — is copied here and openable in Obsidian.

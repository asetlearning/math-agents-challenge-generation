---
type: triage
date: 2026-10-23
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028: vet of the private registry DRAFT rev 2 (10 certified survivors in 'tested')"
---
# T-028 registry rev 2 draft vet: triage

Lead/Developer request (2026-10-23). Draft (private, sha256 ca674428...): `runs/t028-registry-draft/b25_challenge_candidates.DRAFT.json`; base `data/b25_challenge_candidates.json` rev 1 (public, untouched). Words stay private: none appear in my notes. Review note: [[2026-10-23-t028-registry-rev2-draft-vet]].

**Asks and method** (read plus replays, capjob 2G / 2 CPUs, one job at a time; no A_R fields and no pilot rows opened):
1. Diff vs rev 1: only revision, change_log, tested (7 -> 17); candidates empty; approved_by null.
2. Schema/keys of the 10 new records vs the existing tested records.
3. L0 replay per record: per-word core table `table_entries` (literal fifth powers) against the word, cells expand to the word; chain certificate W -> residual replays. My own code, not the Developer's.
4. T3u fields vs levels L1-r25 / S2-chain; rho.
5. Labels true to evidence: B vs B-ext per record (escalation outputs, ids/outcomes only); job-1 held-out verified; attack wording (C3 and C3r2 survivors are attack-limited by owner decision).
6. Reproduction blocks replay; no machine paths.

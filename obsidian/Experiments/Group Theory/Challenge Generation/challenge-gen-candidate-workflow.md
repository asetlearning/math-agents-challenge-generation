---
title: "Challenge generation — candidate testing and registry workflow (B(2,5))"
domain: group-theory
project: challenge-gen
instance: B(2,5)
status: review
author: asetlearning
date: 2026-10-30
tags: [agent/lead, user/asetlearning, domain/group-theory, topic/b25, topic/burnside, topic/trivial-words, topic/hard-instance-generation, topic/proof-certificates, topic/benchmark-design, project/challenge-gen, status/review]
---

# Candidate testing and registry workflow (B(2,5))

> [!info] Plain English
> How a word becomes a challenge candidate, how a new solver is tested against the candidates, and how the public registry changes. Removing a candidate needs a certificate that replays (or, where no certificate is practical, the exact steps to reproduce the result); a shortened word is recorded with a note saying whether it is certified. A human approves every change of the registry. Code: the `bench` package in b25 (`experiments/challenge_gen/bench/`, T-027).

## 1. Testing a word (`bench test`)

The steps run in this order; a word that reaches the empty word at any step stops there (later steps are "not run").

1. **Construction.** W is trivial by construction (T-028: a product of conjugated, substituted copies of certified trivial words). The recipe is stored, so W can be rebuilt.
2. **Fixpoint loop** on W: R → CL → KB → D, repeated until nothing shortens the word.
   - R: cyclic exhaustive 2.5-reduction, shortest end over 12 tie-break orders.
   - CL: non-increasing 2.5-closure search (periods ≤ 7, 10⁶ states).
   - KB: kbmag rec and slx rewriting systems on the 16 images (8 letter automorphisms × inversion).
   - D: coset enumeration (`attempt_to_decide_if_trivial`), 10⁸ cosets, relators up to length 7.
3. **T3u gate** on the end word: L1-r25 (no image shortens below half) and S1-each (R, CL and KB on all 16 images, and D1 = D(2·10⁷ cosets, relators ≤ 5) on the identity image: none may shorten it). S2-chain is evaluated afterwards, only if S1-each holds, and is not part of T3u. A word that fails the gate is labelled `broken-gate`, not discarded.
4. **Held-out solvers** (not used to build the word): two other kbmag systems (held-out rec and slx, all rotations), and D↔R alternation (relators ≤ 7) at 2²⁴, 10⁸ and 10⁹ cosets.
5. **algo-mixer reducer ladder, last** (existing rule sets only; at most 3 levels; a word moves up only if it survives):

   | Level | Rule sets | Beam / budget per word |
   |---|---|---|
   | M1-gen | b25_gen (656k rules) | 1024 / 300 s |
   | M2-all | six sets merged: b25_gen, rec, slx, rpo, rpo_rtl, shortlex (14.4M rules) | 1024 / 300 s |
   | M3-allwide | six sets merged | 4096 / 900 s |

   A word the reducer shortens goes through the whole fixpoint loop again (step 2). A word it empties is re-run alone with path recording, so its route can be certified. Words the reducer leaves unchanged need no further steps.
6. **Certification** (below). A word that survives every step is proposed as a candidate; a word that breaks is recorded under `tested`.

Heavy steps run as rjob jobs on cpuserver (Experimenter-B25 submits, after Lead approves the plan); certificates and records are built on the VM.

## 2. Testing a new solver (`bench solver`)

Any solver, as a Python callable or an external command, runs on the registry candidates with a budget (time, memory, threads). Contract: input a word and the budget; output a verdict (broken, shorter, resilient, error), the output word, and optionally a certificate. **No claim is trusted:**

| Claim | Verified as | Meaning |
|---|---|---|
| broken | `verified-cert` | the certificate replays: the word is a product of conjugates of literal fifth powers |
| broken | `verified-kb` | kbmag rec/slx reduce the word to the empty word: a proof **modulo kbmag** (equality in the group the rewriting systems present, which maps onto B(2,5)); there is no replayable object, so the sha256 of the systems used is recorded. The closure search tries to upgrade it to `verified-cert` |
| shorter | `verified-cert` / `verified-kb` | the same evidence for the loop word · (c · output · c⁻¹)⁻¹, which proves word = c · output · c⁻¹ (the strongest case: the loop free-reduces to the empty word). c is the solver's conjugator; if it gives none, 21 are tried (none, one letter, two letters), and a longer one leaves the claim `unverified` (sound, not complete) |
| any | `unverified` | no evidence found; counted separately, never acted on |

The report gives counts per verdict and verification, per-word time and memory.

## 3. Verification

- **Certificate.** A list of cells [core, conjugator], each core a literal fifth power. The word must equal the free reduction of the product of conjugator⁻¹ · core · conjugator. Replay is done from the definition, by code independent of the solver.
- **Coset-enumeration steps** have no certificate; the record then carries a reproduction block (algorithm, code version, parameters, every intermediate word).
- **Independent checks** before a registry change: the Validator replays every new certificate with its own code; Lead replays them again with a separate script; `bench accept` checks the counts and replays the certificate chains of the broken (`tested`) records that carry a registry word.

## 4. Registry changes

- One living file, `data/b25_challenge_candidates.json`, described by [[ds-b25-challenge-candidates]] with a change log and sha256 per revision.
- Agents propose; **the owner approves every addition and removal**. A broken candidate moves to `tested` with its certificate (`verified-cert`) and the run that broke it; a break proved only modulo kbmag is recorded as `certified: false` with the system hashes and exact steps. A shortened candidate keeps its registry word and gains `shortest_known` (word, length, how obtained, certified or not).
- A new solver is run as a ladder (cheap settings on all candidates, the maximum on the survivors only); the registry changes once, after the last level, with the owner's approval.

## Acceptance of the bench (T-027)

- VM: `bench accept` on revision 3 replays the 8 certificates and finds 207 candidates and 38 `shortest_known` entries.
- cpuserver: a 10-word sample (6 words the reducer broke in revision 3, 4 survivors) through `bench test`, 2026-10-30. **Passed**, same verdicts as revision 3:
  - fixpoint loop: all 10 unchanged, T3u holds, held-out solvers and the 10⁹ rung do not break them (66 min);
  - reducer ladder: the 6 end empty at M1-gen; C3|4|17 shortened 220 → 215 at M1-gen; the other 3 unchanged through M3-allwide (38 min, peak 42 GB);
  - recorded reruns of the 6: all empty again; their certificates replay against the registry words and are byte-identical to revision 3;
  - fixpoint loop on C3|4|17 at 215: unchanged, T3u holds, not broken; recorded as `shortest_known` 215, `certified: false` (the reducer step was not recorded), as in revision 3.
  - Cost about 2.3 USD in total. One fix found by the sample: the rerun of a shortened word must run the gate and the held-out solvers even when the loop leaves it unchanged (b25 `713055d`).

## Related material
- [[challenge-gen-success-metrics]]: level names (L0-cert, L1-r25, S1-each, S2-chain) and the solver-resilience rules
- [[ds-b25-challenge-candidates]]: the registry and its revisions
- [[2026-10-30-t028-mixer-c3r2-3-3-23-check]]: an example of a chained reducer certificate checked by the Validator
- [[Challenge Generation/_progress]]
- [[project-challenge-gen]]

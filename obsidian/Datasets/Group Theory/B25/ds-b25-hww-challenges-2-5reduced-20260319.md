---
title: "B(2,5) HWW challenges — 118 words after greedy 2.5-power reduction, trivial in B₀(2,5)"
dataset_id: ds-b25-hww-challenges-2-5reduced-20260319
date: 2026-03-19
domain: group-theory
project: challenge-gen
instance: B(2,5)
kind: trivial-words
format: "JSON object {\"R<i>\": {\"details\": \"greedy power reduction\", \"version\": 2|3, \"word\": [int, ...]}}; letters 1 = a, -1 = a⁻¹, 2 = b, -2 = b⁻¹; same 118 ids as the parent"
records: 118
files:
  - path: "math-agents-challenge-generation:data/b25_hww_challenges_2_5reduced_20260319.json"
    sha256: 62f44ab1ab9efec1184e0ebe3a505b06eb24f69aff7ecb2295a49d235b722b15
    bytes: 3710933
    role: data
storage: "git — fork asetlearning/math-agents-challenge-generation, data/ (committed 2026-10-07). Byte-identical copy of the owner's tcgraph checkout data/B25/b25_challenge_freelyreduced_reduced2.5_tcgraph_4ln0dt4u_20260319.json"
derived_from:
  - "[[ds-b25-hww-challenges-nonempty-20260930]]"
produced_by: "tcgraph greedy power (2.5) reduction, 2026-03-19 (checkpoint id 4ln0dt4u); exact tcgraph commit and driver not recorded"
property_claimed: "every word is trivial in B₀(2,5) and is a fixed point of linear greedy 2.5-reduction; each word equals (up to conjugation) its parent challenge in B(2,5); triviality in free B(2,5) is OPEN"
vetting:
  - check: same 118 ids as the parent; freely and cyclically reduced; abelianization trivial
    tool: Python
    scope: syntactic (necessary condition)
    result: "118/118 on every count"
    date: 2026-10-07
    by: agent/exp (asetlearning)
  - check: fixed point of linear greedy 2.5-reduction (greedy_reduce2_5)
    tool: tcgraph_ext @ tcgraph_agentic a0d5e92
    scope: syntactic
    result: "118/118 not shortened"
    date: 2026-10-07
    by: agent/exp (asetlearning)
  - check: fixed point of cyclic greedy 2.5-reduction with 4 shifts (greedy_reduce_cyclic2_5, fractions 0, 0.25, 0.5, 0.75)
    tool: tcgraph_ext @ tcgraph_agentic a0d5e92
    scope: syntactic
    result: "111/118; R16, R25, R55, R74, R138, R141 shorten by 1 letter, R113 by 3"
    date: 2026-10-07
    by: agent/exp (asetlearning)
  - check: consistent with the parent under 2.5-reduction
    tool: "tcgraph_ext: cyclically_reduce then greedy_reduce2_5 on each parent word"
    scope: syntactic
    result: "each reduced word is at most as long as the rerun result (0–27 letters shorter, 22 equal length, 1 identical); the original procedure was evidently stronger or iterated and is not reproduced exactly"
    date: 2026-10-07
    by: agent/exp (asetlearning)
  - check: trivial in B₀(2,5)
    tool: "GAP 4.15.1 + anupq 3.3.2 (PqEpimorphism, class 12, order 5^34)"
    scope: "B₀(2,5) = B(2,5)/γ₁₃ — finite quotient"
    result: "118/118 trivial (same run also 118/118 parent words)"
    date: 2026-10-07
    by: agent/exp (asetlearning)
stats: {min_len: 2494, max_len: 27321, mean_len: 12595, median_len: 11696, total_letters: 1486221}
used_by: []
supersedes: ""
superseded_by: ""
author: asetlearning
status: validated
validated_by: "asetlearning (owner), 2026-10-07"
tags: [agent/exp, user/asetlearning, domain/group-theory, topic/burnside, topic/b25, topic/restricted-burnside, topic/trivial-words, topic/word-problem, project/challenge-gen, project/b25, status/validated, dataset]
---

# B(2,5) HWW challenges — 2.5-reduced (118)

> [!info] Plain English
> These are the 118 challenge words of [[ds-b25-hww-challenges-nonempty-20260930]], shortened by greedy 2.5-power rewriting (v^p → v^−(5−p) for p ≥ 2.5, which is valid whenever v⁵ = 1). They are about 32% shorter: 1.49M letters in total against 2.20M. Every word is still the identity in the finite quotient B₀(2,5). Whether each is the identity in free B(2,5) is **open**; these are the challenge targets.

**Status: validated by the owner (asetlearning), 2026-10-07**, for the claims as stated: trivial in B₀(2,5), fixed point of linear greedy 2.5-reduction. Triviality in free B(2,5) stays open.

## What it is
- **File:** one JSON object with the same 118 ids as the parent (R5 … R149). Each entry is `{"details": "greedy power reduction", "version": 3 (103 words) or 2 (15 words), "word": [...]}`. Letters are 1 = a, −1 = a⁻¹, 2 = b, −2 = b⁻¹.
- **Size:** lengths 2,494–27,321, mean 12,595, median 11,696, total 1,486,221 letters.
- **Version 2 entries:** R43, R44, R62, R68, R70, R72, R77, R79, R88, R89, R103, R104, R108, R128 and R129. The two version numbers presumably mark different runs of the reducer; what distinguishes them is not recorded.

## Origin
- **Owner's description:** the HWW relators, reduced by the 2.5-reduction algorithm, with all words that reduced to the empty word removed.
- **Source file:** a byte-identical copy (sha256 checked) of `data/B25/b25_challenge_freelyreduced_reduced2.5_tcgraph_4ln0dt4u_20260319.json` in the owner's tcgraph checkout, dated 2026-03-19 and written by tcgraph's greedy power reduction (checkpoint id `4ln0dt4u`).
- **Input:** the 118 non-empty freely reduced challenges, [[ds-b25-hww-challenges-nonempty-20260930]].
- **Other files in that folder:**
  - `…_reduced2.5_20260318.json` is a symlink to the owner's Mac (`~/Work/Research/B25/Data/reduce_words_power_2.5/`).
  - The 2026-03-22 checkpoints hold a single word each.
  - `cmake-build-debug/b25_challenge_original_2.5reduced_cyclic4_checkpoint_…20260402.json` is a one-word checkpoint of a later cyclic, 4-shift pass.
- **Not recorded:** the exact tcgraph commit, the driver and its parameters.

## Validation
| Check | Tool | Object / scope | Result |
|---|---|---|---|
| Same ids as parent; freely and cyclically reduced; abelianization trivial | Python | necessary conditions | 118/118 |
| Fixed point of linear greedy 2.5-reduction | tcgraph `greedy_reduce2_5` @ a0d5e92 | syntactic | 118/118 |
| Fixed point of cyclic 2.5-reduction, 4 shifts | tcgraph `greedy_reduce_cyclic2_5` | syntactic | 111/118 (7 shorten by 1–3 letters) |
| Trivial in B₀(2,5) | GAP 4.15.1 + anupq 3.3.2, class 12, order 5³⁴ | B₀(2,5) = B(2,5)/γ₁₃ | 118/118 |

- **Why B₀(2,5) triviality is expected.** 2.5-rewrites are valid whenever v⁵ = 1, and cyclic reduction is conjugation. So each reduced word is conjugate in B(2,5) to its parent challenge, and is trivial in B₀(2,5), or in B(2,5), exactly when the parent is.
- **Direct check.** The GAP check was run on these exact words rather than inferred, because the reduction could not be replayed exactly.
- **Replay attempt.** Cyclically reducing each parent word and then running one linear 2.5 pass at tcgraph a0d5e92 gives words 0–27 letters *longer* than the file's (22 of equal length, 1 identical). The file's procedure was therefore at least as strong; it was probably iterated or used rotations.
- **Run details:**
  - Local run dir: `~/Research/challenge-gen/runs/challenges-nonempty-verify-20261007/`, with `reduced_checks.csv`, `cyclic_checks.csv`, `gap_results.csv`, `gap_stdout.log` and `time.log`.
  - Timings: GAP took 4 min 37 s for all 236 words (parent and reduced); the cyclic checks took 7 min.
  - GAP script: b25 `tools/challenge-gen-datasets:experiments/challenge_gen/b0_challenge_triviality.g`. Controls passed: a⁵ and (ab)⁵ trivial; a, a⁴ and [a,b] not.

## Caveats
- **Not a fixed point of the cyclic reducer.** 7 words still lose 1–3 letters under a 4-shift cyclic pass. The exhaustive all-shifts reducer (`greedy_reduce_cyclic_exhaustive2_5`) was not run: with words this long it needs a remote job.
- **Single B₀(2,5) oracle.** The reduced words were checked with ANUPQ only. The independent nq replication covered the parent set; the soundness argument above transfers it.
- **Triviality in B(2,5) is not established.** It is the open question.
- **Procedure not reproducible from records.** See Origin.

## How to load
```python
import hashlib, json
from pathlib import Path

p = Path("<math-agents-challenge-generation checkout>/data/b25_hww_challenges_2_5reduced_20260319.json")
assert hashlib.sha256(p.read_bytes()).hexdigest() == \
    "62f44ab1ab9efec1184e0ebe3a505b06eb24f69aff7ecb2295a49d235b722b15"
words = {k: v["word"] for k, v in json.loads(p.read_text()).items()}   # 118 lists of ±1, ±2
```

## Used by
- (none yet)

## Related material
- [[ds-b25-hww-challenges-nonempty-20260930]]: the parent set
- [[datasets-convention]]
- [[havas-wall-wamsley-1974]]: the presentation the challenges come from
- [[challenge-gen-success-metrics]]: L1 uses the 2.5-reduced length ratio
- [[Experiments/Group Theory/Challenge Generation/_progress|Challenge Generation progress]]
- [[project-challenge-gen]] · [[dep-gap]]

---
title: "B(2,5) HWW challenges — 118 non-empty freely reduced words, trivial in B₀(2,5)"
dataset_id: ds-b25-hww-challenges-nonempty-20260930
date: 2026-09-30
domain: group-theory
project: challenge-gen
instance: B(2,5)
kind: trivial-words
format: "JSON object {\"R<i>\": {\"version\": 1, \"word\": [int, ...]}}; letters 1 = a, -1 = a⁻¹, 2 = b, -2 = b⁻¹; ids R5..R149 (118 of R1..R150)"
records: 118
files:
  - path: "math-agents-challenge-generation:data/b25_challenge_original_freelyreduced_nonempty.json"
    sha256: 8362b35e8e482a920b404316ff0ee6dda43e94dcb2abc44397a5238151317ec5
    bytes: 5492667
    role: data
storage: "git — fork asetlearning/math-agents-challenge-generation, data/ (committed 2026-09-30 in 69c3d42; legacy file name, predates the naming rule)"
derived_from:
  - "math-agents-challenge-generation:data/b25_challenge_original_freelyreduced.json sha256 067977857d88f895f6f643bdb3b569993132365f4afa2cd89e4b1873d6cf3cde (150 words R1..R150, 32 empty; committed in 69c3d42) — the HWW relators expanded to words in a, b and freely reduced"
produced_by: "not recorded: expansion of the HWW (1974) pc-presentation relators into a, b words, free reduction, removal of the 32 empty words"
property_claimed: "every word is trivial in B₀(2,5) = B(2,5)/γ₁₃ (order 5³⁴, class 12); triviality in free B(2,5) is OPEN (these are the challenges)"
vetting:
  - check: same words as the non-empty entries of the 150-word parent
    tool: Python (json)
    scope: syntactic
    result: "118/118 ids and words identical; the 32 dropped ids are exactly the empty words"
    date: 2026-10-07
    by: agent/exp (asetlearning)
  - check: freely reduced; abelianization trivial (exponent sums ≡ 0 mod 5)
    tool: Python
    scope: syntactic (necessary condition)
    result: "118/118 freely reduced (42 also cyclically reduced); 118/118 abelianization trivial"
    date: 2026-10-07
    by: agent/exp (asetlearning)
  - check: trivial in B₀(2,5)
    tool: "GAP 4.15.1 + anupq 3.3.2 (PqEpimorphism, class 12, order 5^34)"
    scope: "B₀(2,5) — finite quotient; trivial here means the word lies in γ₁₃(B(2,5))"
    result: "118/118 trivial (2026-10-07 rerun on this exact file; also 150/150 on the parent, 2026-09-30)"
    date: 2026-10-07
    by: agent/exp (asetlearning)
  - check: trivial in B₀(2,5), independent oracle
    tool: "GAP 4.15.1 + nq 2.5.11 (NilpotentQuotient of <a,b; x | x^5>, class bound 13)"
    scope: "B₀(2,5)"
    result: "150/150 parent words trivial, 0 disagreements with ANUPQ — #status/replicated"
    date: 2026-09-30
    by: agent/validator (asetlearning)
  - check: 2.5-reduced
    tool: tcgraph_ext greedy_reduce2_5 @ tcgraph_agentic a0d5e92
    scope: syntactic
    result: "NO — every word still shortens (e.g. R90 41886 → 22397); the reduced set is [[ds-b25-hww-challenges-2-5reduced-20260319]]"
    date: 2026-10-07
    by: agent/exp (asetlearning)
stats: {min_len: 2500, max_len: 41886, mean_len: 18607, median_len: 17105, total_letters: 2195684}
used_by: ["[[ds-b25-hww-challenges-2-5reduced-20260319]]", "[[patternboost-generation-data]]"]
supersedes: ""
superseded_by: ""
author: asetlearning
status: validated
validated_by: "agent/validator, 2026-09-30 (B₀(2,5) claim, nq oracle) — see [[2026-09-30-b25-b0-challenge-triviality]]"
tags: [agent/exp, user/asetlearning, domain/group-theory, topic/burnside, topic/b25, topic/restricted-burnside, topic/trivial-words, topic/word-problem, project/challenge-gen, project/b25, status/validated, dataset]
---

# B(2,5) HWW challenges — 118 non-empty, freely reduced

> [!info] Plain English
> These are the "challenges": 118 words in a, b obtained from the relators of the Havas–Wall–Wamsley presentation of the restricted Burnside group B₀(2,5). Each word is the identity in B₀(2,5), the largest finite quotient of B(2,5). Whether each is also the identity in the free Burnside group B(2,5) is **open**; proving all of them trivial would show B(2,5) is finite. The words are long (2,500–41,886 letters) and **not** 2.5-reduced. For the 2.5-reduced versions, use [[ds-b25-hww-challenges-2-5reduced-20260319]].

**Status: validated** for the claim "trivial in B₀(2,5)". Validator replicated it with an independent oracle on 2026-09-30, and it was rerun on this exact file on 2026-10-07.

## What it is
- **File:** one JSON object with 118 entries `R<i> → {"version": 1, "word": [...]}`. Letters are 1 = a, −1 = a⁻¹, 2 = b, −2 = b⁻¹. Ids keep the numbering of the 150 relators (R5 … R149).
- **Size:** lengths 2,500–41,886, mean 18,607, median 17,105, total 2,195,684 letters.
- **Dropped ids:** R1–R4, R6, R7, R15, R21, R28, R29, R36, R37, R53, R63, R64, R73, R81, R97, R105, R106, R112, R116, R121, R122, R126, R127, R131, R140, R144, R146, R148 and R150. These 32 words freely reduce to the empty word.

## Origin
- **Source presentation:** Havas, Wall and Wamsley (1974) give a consistent commutator power presentation of B₀(2,5) on 34 generators (order 5³⁴, class 12); see [[havas-wall-wamsley-1974]]. Every relator of that presentation holds in B₀(2,5).
- **Expansion:** the challenges are those relators rewritten as words in a and b, then freely reduced. Presumably the auxiliary generators 3–34 are replaced by their defining commutators, as the integer-list form of the relators suggests; the expansion step itself is not recorded. This gives `b25_challenge_original_freelyreduced.json` (150 words). The integer-list form of the relators is in the owner's tcgraph checkout (`data/B25/b25_factor_group_relators_integer_list.py`).
- **This file:** the 118 non-empty words of that file, unchanged.
- **Not recorded:** the exact expansion script and its date. The parent was committed on 2026-09-30 (69c3d42). The 2.5-reduced version is dated 2026-03-19, so the expansion predates it.
- **Owner's description:** "the relators of the factor group from the HWW paper". A later 2.5-reduction step produced [[ds-b25-hww-challenges-2-5reduced-20260319]]; this file is the input to that step, not its output.

## Validation
| Check | Tool | Object / scope | Result |
|---|---|---|---|
| Equals the non-empty part of the 150-word parent | Python | syntactic | 118/118 |
| Freely reduced; abelianization trivial | Python | necessary condition | 118/118; 118/118 |
| Trivial in B₀(2,5) | GAP 4.15.1 + anupq 3.3.2, class 12, order 5³⁴ | B₀(2,5) = B(2,5)/γ₁₃ | 118/118 |
| Trivial in B₀(2,5), independent | GAP + nq 2.5.11 | B₀(2,5) | 150/150 parent, replicated |
| 2.5-reduced | tcgraph `greedy_reduce2_5` | syntactic | **no** |

- **What "trivial in B₀(2,5)" means here.** Each word lies in γ₁₃(B(2,5)), the kernel of B(2,5) → B₀(2,5). It says nothing about the free B(2,5) (Kourovka 11.48).
- **2026-10-07 rerun:**
  - The GAP check ran on this file's 118 words and on the 118 reduced words: 236/236 trivial, in 4 min 37 s.
  - The script checks |P| = 5³⁴ and class 12, and that the images of a and b generate P.
  - Controls: a⁵ and (ab)⁵ come out trivial; a, a⁴ and [a,b] do not.
  - Script: b25 `tools/challenge-gen-datasets:experiments/challenge_gen/b0_challenge_triviality.g`.
  - Run dir: `~/Research/challenge-gen/runs/challenges-nonempty-verify-20261007/` (local).
- **2026-09-30 runs (parent):**
  - Producer: [[b0-challenge-triviality-2026-09-30]] and [[b0-challenge-triviality-results-2026-09-30]].
  - Validator: [[2026-09-30-b25-b0-challenge-triviality]]. An nq oracle on the identical relation x⁵ gave order 5³⁴ and class 12, with 0 disagreements.

## Caveats
- **Not 2.5-reduced and mostly not cyclically reduced** (42/118 are). Scorers and search code that expect reduced targets should use the reduced dataset.
- **Legacy file name.** The file was committed before the dataset naming rule existed and keeps its old name; the `dataset_id` is the stable reference.
- **Triviality in B(2,5) is not established.** It is the open question these words encode.

## How to load
```python
import hashlib, json
from pathlib import Path

p = Path("<math-agents-challenge-generation checkout>/data/b25_challenge_original_freelyreduced_nonempty.json")
assert hashlib.sha256(p.read_bytes()).hexdigest() == \
    "8362b35e8e482a920b404316ff0ee6dda43e94dcb2abc44397a5238151317ec5"
words = {k: v["word"] for k, v in json.loads(p.read_text()).items()}   # 118 lists of ±1, ±2
```

## Used by
- [[ds-b25-hww-challenges-2-5reduced-20260319]]: 2.5-reduced from this set
- [[patternboost-generation-data]]: real challenge targets for later phases

## Related material
- [[datasets-convention]]
- [[havas-wall-wamsley-1974]]: the presentation the challenges come from
- [[2026-09-30-b25-b0-challenge-triviality]]: Validator's B₀(2,5) verdict
- [[Experiments/Group Theory/Challenge Generation/_progress|Challenge Generation progress]]
- [[project-challenge-gen]] · [[dep-gap]]

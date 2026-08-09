# R2 Rulegen Param Sheet

Locked ROUND-2 rule-bank generation parameters for B25. Params only; no compute launch implied. Scope is B0(2,5), raw alphabet `{a,b,A,B}` only. Shortlex is the real generator. RPO is diagnostic only.

## 1. kbmag orderings and presentation/input files

Binary for all runs:

`/Users/maumayma/Desktop/reps/algo_mixing/kbmag_source/standalone/bin/kbprog`

Presentation/input files are raw B0(2,5) files: 4372 exponent-5 relators from all freely reduced words over `{a,A,b,B}` of length <= 7. No compressed alphabet and no expand step.

| run id | role | input file | ordering / generator order | scoring status |
|---|---|---|---|---|
| `slex_aAbB_k5` | primary | `experiments/_inputs/kbmag/b25_gen` | shortlex, generatorOrder `[a,A,b,B]`, inverses `[A,a,B,b]` | scoring-bank source |
| `slex_bBaA_k5` | primary mirror | `experiments/_inputs/kbmag/b25_gen_bBaA` | shortlex, generatorOrder `[b,B,a,A]`, inverses `[B,b,A,a]` | scoring-bank source |
| `slex_aAbB_k6` | primary diversity | `experiments/_inputs/kbmag/b25_gen` | shortlex, generatorOrder `[a,A,b,B]`, inverses `[A,a,B,b]` | scoring-bank source |
| `rpo_aAbB_diag` | diagnostic only | `experiments/_inputs/kbmag/b25_gen` | recursive/RPO via `-rec`, generatorOrder `[a,A,b,B]` | diagnostic only; never scoring/training |

Do not run `wtlex`, lifted, compressed, or whole-target-biased variants in this locked round.

## 2. Per-ordering biased-kbprog parameters

Global wall budget: 4h total. Parallelism cap for this job: 4 kbprog processes max, leaving the canvas global heavy-process cap respected. If other heavy processes are already running, B25 must reduce this count accordingly.

Common command shape:

```bash
kbmag_source/standalone/bin/kbprog -v -me 50000000 -ms 200000000 -t 5000 -cn <cn> -sw <special_windows_concat.txt> -sp <sp> -sk <sk> <input_file>
```

| run id | cn | sp | sk | maxeqns | maxstates | tidyint | maxstoredlen / LHS-cap wiring |
|---|---:|---:|---:|---:|---:|---:|---|
| `slex_aAbB_k5` | 100000 | 0.7 | 5 | 50000000 | 200000000 | 5000 | do not set `-mlr`; extract/admit only `len(lhs)<=12`; optional dump filter `-sort 12` |
| `slex_bBaA_k5` | 100000 | 0.7 | 5 | 50000000 | 200000000 | 5000 | do not set `-mlr`; extract/admit only `len(lhs)<=12`; optional dump filter `-sort 12` |
| `slex_aAbB_k6` | 100000 | 0.7 | 6 | 50000000 | 200000000 | 5000 | do not set `-mlr`; extract/admit only `len(lhs)<=12`; optional dump filter `-sort 12` |
| `rpo_aAbB_diag` | 100000 | 0.7 | 5 | 50000000 | 200000000 | 5000 | do not set `-mlr`; diagnostic extraction only; still report `len(lhs)<=12` stats |

`maxstoredlen` decision: do not constrain KB generation with `maxstoredlen` / `-mlr`, because hard storage truncation can change the generated completion trajectory. The locked cap is an admission/extraction cap, not a generator storage cap: no rule with `len(lhs)>12` can enter either the primary bank or enabler bucket.

## 3. Short-window bias seed list

Bias is on short raw windows around firing motifs, not whole `comm_13_10`, not whole `word_7245`, and not any m/M form. Current biased `kbprog` reads only the first non-comment line from `-sw`, so create `special_windows_concat.txt` as one line by concatenating the following windows in this exact order with no separators.

```text
abABA
abaBA
ababABABA
abbabABABBAB
abbabaBABBAB
bababABABABB
bababaBABABB
bbababABAABB
bbababAABABB
baabaaBABABB
bbaabaBABABB
babaabAAABAB
ababaaBBABAB
bababAABAABB
bbababaBAABB
bababaaBABAB
bababaBAABAB
ababaaBAABAB
ababaaaBBABA
BAbabbaabaaa
AbabbbABBABa
bbbAABBABABB
aabaaaBBABAB
ababbAAABAAB
```

One-line `-sw` payload:

```text
abABAabaBAababABABAabbabABABBABabbabaBABBABbababABABABBbababaBABABBbbababABAABBbbababAABABBbaabaaBABABBbbaabaBABABBbabaabAAABABababaaBBABABbababAABAABBbbababaBAABBbababaaBABABbababaBAABABababaaBAABABababaaaBBABABAbabbaabaaaAbabbbABBABabbbAABBABABBaabaaaBBABABababbAAABAAB
```

Source of the windows: `experiments/burnside/b25/fragment_seed_rules/b25_seed_rules_2026-06-25.json`, restricted to the short fragment rules from the 31 GAP-matched fragment-shortening hunt.

## 4. Non-blind seed corpus

Use the existing raw firing-window corpus:

`runs/b25/patternboost_seeds/20260630_round2/seed_words.txt`

Current size: 345 raw words.

Source generator: `experiments/burnside/b25_patternboost/seed_window.py`.

Anchor sources used by that generator:

- `experiments/b25_reduce_core/corrected/01_after_power.txt`
- `experiments/b25_reduce_core/archive/data/word_coreless.txt`

Admission to this seed corpus required corrected braid reduction to visibly fire (`delta > 0`). This is the non-blind source for candidate generation/held-out mutation structure. Do not use `comm_13_10_raw.txt`, `word_7245`, or final pre-reduced benchmark words as the non-blind seed corpus.

## 5. Held-out raw candidate pool for the >=500-fire GO test

Generate a fresh held-out raw candidate pool with seed `20260701`, size `12000`, excluding exact words from the 345-word non-blind seed corpus and excluding the 119 benchmark words. Free-reduce every generated candidate and reject candidates containing anything outside `{a,b,A,B}`.

Composition:

| bucket | count | construction |
|---|---:|---|
| seed mutations | 4000 | choose from the 345 non-blind seed words; apply 1-3% raw character edits (`sub`, `del`, `ins`, `swap`) under raw alphabet; free-reduce |
| random walks | 4000 | non-backtracking random raw walks, lengths sampled from `{64,128,256,512}`; half forced to abelianization `(0,0)` and half not; abelianization used only for stratification, not equality |
| motif-stress | 4000 | non-backtracking background lengths `{128,256,512}` with 1-4 inserted short-window bias motifs; free-reduce |

GO metric: after the rule-admission filter, at least `500` distinct primary scoring-bank rules, deduped by exact `(lhs,rhs)`, must fire at least once on this held-out pool. Count distinct rules that fire, not total fire events.

Rules that do not count toward GO:

- RPO diagnostic rules.
- Enabler-search-only rules.
- Rules failing GAP equality.
- Rules with `len(lhs)>12`.
- Length-preserving or length-increasing rules.

## 6. Rule-admission filter pipeline

Apply this pipeline to every extracted candidate rule before it can enter any bank.

1. Raw alphabet gate: `lhs` and `rhs` must contain only `{a,b,A,B}`.
2. Free-reduce both sides. Reject if `lhs` becomes empty.
3. Hard LHS cap: reject if `len(lhs)>12`.
4. GAP equality gate in B0(2,5) on every rule. Abelianization is forbidden as a proxy.
5. Deduplicate exact `(lhs,rhs)` pairs after free reduction and GAP acceptance.
6. Bucket by length delta `Delta = len(rhs)-len(lhs)`.
7. Primary scoring bank: admit only `Delta < 0`.
8. Enabler-search-only bucket: admit `Delta >= 0` only under section 7 below. Never place these in the scoring bank.
9. Length distribution target for primary bank: target 70% of admitted primary rules with LHS length 5-8; target 90% with LHS length <=10; absolute cap remains 12.
10. Fire-test annotation: for every admitted primary rule, record whether it fires on the held-out pool and total fire count, but GO uses distinct firing primary rules only.

Primary bank orientation: keep the generated orientation only if it is length-decreasing. If the reverse orientation is length-decreasing, it may be proposed separately only after its own GAP equality check and the same LHS cap.

## 7. Enabler-search-only layer

Maria correction folded in: length-increasing rules are real as grow-to-shrink enablers, but never belong in the scoring reducer. A reducer with length-increasing rules is not termination-safe. Termination/soundness questions route to Validator.

Enabler bucket admission for `Delta >= 0`:

- Must pass the same raw alphabet, free reduction, LHS cap, dedup, and GAP equality gates as primary rules.
- Require `Delta <= +4`; reject larger expansions.
- Must demonstrably lead to net shrinkage on the non-blind seed corpus: applying the enabler at a real occurrence, then free reduction plus braid/power reduction, must produce `len(after) < len(before)` in at least 3 occurrences across at least 2 source words.
- Store separately as `enabler_search_only`; never export to the primary scoring bank and never count toward the >=500-fire GO threshold.

Search-layer runtime caps:

- Max 2 enabler applications per search path.
- Max temporary expansion above path start: 8 chars.
- Immediate free reduction plus braid/power cleanup after every enabler application.
- Prune a branch unless net shrinkage appears within the bounded cleanup step.
- Allowed only in transformer+beam+local-search exploration.
- Forbidden in reducer-only scoring, training labels, and the primary rule bank.

Locked status: params only; no compute launched by this sheet.

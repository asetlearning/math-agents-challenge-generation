---
title: B(2,5) challenge-candidate registry — approved candidates and tested words, with certificates
dataset_id: ds-b25-challenge-candidates   # living registry (owner, 2026-10-20): one file, revisions tracked below
date: 2026-10-20
domain: group-theory
project: challenge-gen
instance: B(2,5)
kind: trivial-words
format: "JSON (schema b25-challenge-candidates v1); letters a A b B (A = a⁻¹, B = b⁻¹); certificates as lists of [relator index, conjugator] over the R7 table, with the used relators included"
records: "revision 3: 207 candidates (T-028), 20 tested (7 from revision 1 + 5 broken T-028 words + 8 broken by the algo-mixer reducer)"
files:
  - path: "math-agents-challenge-generation:data/b25_challenge_candidates.json"
    sha256: 32f083dc5398bb633117b03e193de417d90fea0a1b222e161c75dcc22a446d95   # revision 3
    bytes: 3452976
    role: data
  - path: "math-agents-challenge-generation:data/b25_t028_survivors_220_rev4.json.gz"
    sha256: 2c321be52a1e6506cebbd251392eed76698ba84df1e9746ac2e4c4fbc4a7e5fa   # gzip -9 -n; uncompressed sha256 c0e22bb0837b82e163649387690913184a7b7cc322ad0faacfd71637f3fac78e, 117355550 bytes
    bytes: 2867414
    role: full records of the T-028 candidates (certificates, every reduction step, history)
storage: git (math-agents-challenge-generation data/)
derived_from:
  - "T-028 survivors file revision 4 (Lead's private run folder), sha256 c0e22bb0837b82e163649387690913184a7b7cc322ad0faacfd71637f3fac78e; published unchanged as the .gz file above (revision 2)"
  - "Lead's private results file of the 12 Validator-confirmed T-024 words with R7 certificates (gitignored), sha256 cd1ae09d3a0455ac45dff22950f066cb3fd76c92dc1df4069555a668ba1c17be — origin: T-024 onion pilot, [[t024-challenge-census-and-onion-probe-2026-10-17]] §10.6"
  - "the owner's residual-words file of 2026-10-19 (gitignored shared/ folder), sha256 890d6de4cee833109fb2e462462623bb9e9116f5ea549e47711addebaabab75e — origin: the owner's solver chain on the 12 words"
produced_by: "revision 3: b25_pyproject_agentic t028-pilot ad87d88, experiments/challenge_gen/t028/mixer_registry_rev3.py (builder and validation) and mixer_chain_cert.py (chained certificates); mixer runs via experiments/challenge_gen/t028/mixer_rung.py and jobs/run_t028_mixer*.sh. Revision 2: b25_pyproject_agentic t028-pilot ae6ca36, experiments/challenge_gen/t028/build_public_registry.py (sha256 ff0d7124457afcfeacebf7ca84c286f5b3439e5c8bc167a72dc755ddc1240d13). Revision 1: b25_pyproject_agentic, branch t027-candidates-solvers: experiments/challenge_gen/solvers/build_candidates.py (sha256 63118b080b9a4702f568d6bc58c57cbf693cadcfd3189dea1273d725dfb1418e; solver harness, 13 files, sha256 b826ff9852b97549b7c65cee0405485d509ef9c5ab4ebecfb5b1075cdf55fb26); repo@sha added when the branch is committed"
property_claimed: "Revision 1 records: trivial in free B(2,5), proved by an R7 certificate that re-expands exactly to its word (L0-cert). T-028 candidates (revision 2): W is trivial by construction (a product of conjugated images of certified trivial words); 200 of the 215 words are proved equal to W in the free group modulo fifth powers (certificate chain, L0); 15 reach their word through a coset-enumeration step (equality in a finitely presented cover, reproduction block in the .gz file). Revision 3: the 8 words broken by the algo-mixer reducer carry a certificate_chain proving the registry word is a product of conjugates of literal fifth powers (free B(2,5) proof; some fifth powers have period > 7, so these are not G_7 relators). 'shortest_known' words equal the registry word only by the solver steps that produced them (not certified). 'candidates' holds human-approved challenge candidates; 'tested' holds evaluated words that are not candidates, with their solver verdicts."
vetting:
  - check: "L0 of every certificate against its word, R7 only; words equal their sources; reproduction chains equal the Validator's"
    tool: "Validator's independent expander and chain (b25 d1b5d0f, tcgraph 63564c3)"
    scope: "free B(2,5) — proof"
    result: "7/7 certificates L0; 7/7 words; 4/4 chains; 65 relator entries = R7"
    date: 2026-10-20
    by: agent/validator (asetlearning)
  - check: "kbmag reduction to IdWord"
    tool: "kbmag kbprog + wordreduce, b25_full, rec and slx, -me 100000"
    scope: "free B(2,5) — proof"
    result: "7/7"
    date: 2026-10-20
    by: agent/validator (asetlearning)
  - check: "trivial in B₀(2,5)"
    tool: "GAP 4.15.1 + anupq 3.3.2, PqEpimorphism class 12, order 5^34"
    scope: "finite quotient — consistency only"
    result: "7/7"
    date: 2026-10-20
    by: agent/validator (asetlearning)
  - check: "T-028 survivors rev 4: changed words carry the fixpoint finals, certificates replay (chain and L0), B0-trivial, counts 215 T3u / 5 broken / 200 certified live"
    tool: "Validator's own replay and diff code"
    scope: "free B(2,5) — proof (certificates); finite quotient — consistency only (B0)"
    result: "PASS, [[2026-10-27-t028-survivors-rev4-check]]"
    date: 2026-10-27
    by: agent/validator (asetlearning)
  - check: "independent rebuild of all 220 W from the construction, W and t certificates, R + D(20M, rml 5) re-reduction"
    tool: "owner's own code (tcgraph 26f4f5a)"
    scope: "free B(2,5) — proof (certificates)"
    result: "W 220/220, certificates 220/220; never shorter than the stored word (160 equal, 60 longer); empties only the 3 known broken words it can reach"
    date: 2026-10-27
    by: agent/human (asetlearning)
  - check: "W rebuilt from the public compact construction only; candidate words equal the benchmark; no two candidates equivalent under rotation, inverse or the 8 letter automorphisms; no proper powers; no machine paths"
    tool: "Lead's own script (and the builder's self-check)"
    scope: "syntactic"
    result: "220/220; 215 distinct classes; 0 paths"
    date: 2026-10-28
    by: agent/lead (asetlearning)
  - check: "8 algo-mixer breaks: every cell a conjugate of a literal fifth power; product free-reduces to the registry word; route ends empty"
    tool: "Validator's own replay (7 on 2026-10-28..29, C3r2|3,3|23 on 2026-10-30)"
    scope: "free B(2,5) — proof"
    result: "8/8 CONFIRMED, [[2026-10-28-t028-mixer-c3r2-2-2-1-check]], [[2026-10-29-t028-mixer-r1-six-breaks-check]], [[2026-10-30-t028-mixer-c3r2-3-3-23-check]]"
    date: 2026-10-30
    by: agent/validator (asetlearning)
  - check: "revision 3 file: the 8 certificate_chain fields replay to their registry words (x^-1 r x, r a literal fifth power); 207 candidates, 20 tested, ids unique, no broken id among candidates, no machine paths"
    tool: "Lead's own replay script (independent of the builder) and the builder's validation"
    scope: "free B(2,5) — proof (certificates); syntactic"
    result: "8/8; counts as stated; 0 paths"
    date: 2026-10-30
    by: agent/lead (asetlearning)
stats: {revision_1: {min_len: 47, max_len: 1548}, t028_candidates_rev3: {n: 207, with_shortest_known: 38}, t028_candidates: {n: 215, min_len: 138, median_len: 602, max_len: 1313, certified: 200}}
used_by: ["`[[challenge-gen-success-metrics]]` (solver resilience, registry rules)"]
supersedes: ""
superseded_by: ""
author: asetlearning
status: review
tags: [agent/lead, user/asetlearning, domain/group-theory, topic/b25, topic/burnside, topic/trivial-words, topic/hard-instance-generation, topic/proof-certificates, project/challenge-gen, status/review, dataset]
---

# B(2,5) challenge-candidate registry

> [!info] Plain English
> The one place where challenge-gen keeps its challenge candidates: words that are provably trivial in B(2,5) and hard to solve. A human approves every addition and removal. Words that were evaluated but did not qualify are kept under `tested`, so the history is not lost. In revision 1 there are no candidates: the three residual words of the T-024 constructions and their four originals are logged as tested, because kbmag reduces all of them to the identity.

## Rules (owner, 2026-10-20)

- **One living file** for now: `data/b25_challenge_candidates.json`. This is a deliberate exception to the [[datasets-convention]] rule that a changed file is a new dataset. Instead, every revision is listed in the change log below with its sha256.
- **A human approves every addition or removal** of a candidate. Agents propose; they never add.
- **Certificates wherever practical.** When a step has no certificate (for example a coset-enumeration step), the record carries a **reproduction block**: the algorithm, code version, parameters and every intermediate word in order, so an independent verifier can repeat it exactly.
- **Only approved candidates** (and the originals and certificates they derive from) go into this public file. Everything else stays in private folders.
- **Levels** are reported on two axes ([[challenge-gen-success-metrics]]): the L ladder (L0-cert, L1-r25, L2-area, L3-quad) and the solver axis (S1-each, S2-chain). A candidate must at least be L1-r25 and resist 2.5-reduction, the Cayley-graph procedure (coset enumeration) and kbmag.

## What it is

Top-level fields:
- `schema`, `schema_version`, `revision`, `change_log`;
- `alphabet`, `levels_note`, `code` (repo@sha of the code used);
- `candidates`: the approved list (empty in revision 1);
- `tested`: evaluated words that are not candidates;
- `relators`: the R7 entries used by the certificates (index → string);
- `inputs_sha256`, `proposed_by`, `approved_by`.

Each record has:
- `id`, `kind` (original or residual), `status`, `word`, `length`, `origins`, `length_chain`;
- `levels` (`L` and `S`), `rho_min16`;
- `solver_verdicts`: one entry per solver (verdict, budget, time, peak memory);
- `certificate`: a list of [relator index, conjugator], or null;
- `trivial_via`, and `reproduction` (the exact steps) where applicable.

## Revision 1 (2026-10-20): contents

| id | kind | length | origin | levels | how it is known trivial | status |
|---|---|---|---|---|---|---|
| ds94_L2 | original | 216 | T-024 level 2 | L1-r25, S none | R7 certificate | tested: not a candidate |
| ds764_L2 | original | 635 | T-024 level 2 | L1-r25, S none | R7 certificate | tested: not a candidate |
| ds665_L2 | original | 405 | T-024 level 2 | L1-r25, S none | R7 certificate | tested: not a candidate |
| ds519_L3_c2_B | original | 1,548 | T-024 level 3 | L1-r25, S none | R7 certificate | tested: not a candidate |
| T024_R1 | residual | 47 | ds94 and ds764 | L1-r25, S none | R7 certificate from the kbmag rec rewriting path (kbcert) | tested: not a candidate |
| T024_R2 | residual | 47 | ds665 | L1-r25, S none | as R1 | tested: not a candidate |
| T024_R3 | residual | 249 | ds519 (level 3) | L1-r25, S none | as R1 | tested: not a candidate |

**Why none is a candidate.** kbmag (the `b25_full` rec and slx rewriting systems) reduces every word above to the identity in under a second. In addition, the owner's chain (coset enumeration alternated with 2.5-reduction) took the four originals to the residuals. The full history is in the addendum of [[t024-challenge-census-and-onion-probe-2026-10-17]].

## Revision 2 (2026-10-28): the T-028 candidates

> [!info] Plain English
> 215 words, 138 to 1313 letters long, each trivial in B(2,5) by construction and each resisting every solver we have: 2.5-reduction with 12 tie-break orders, the closure search, kbmag (two rewriting systems, all 16 images, all rotations) and coset enumeration up to 10⁹ cosets with relators up to length 7, run in a loop until nothing shortens the word. No two are equivalent under rotation, inversion or the 8 letter automorphisms. The owner approved all 215 on 2026-10-28; they are also the project's benchmark.

- **How a word is built.** W = cyclic_reduce(∏ c_j⁻¹ φ_j(t_j)^{s_j} c_j): t_j are certified trivial dataset words (length 50–80), φ_j substitutes a → x, b → y (twice for the C3r2 arm), s_j = ±1, c_j are conjugators. Each candidate record stores t, sign, x/y per round and the conjugator, so W rebuilds without the random generator (`construction_recipe` at the top level).
- **From W to the word.** 2.5-reduction, kbmag and coset-enumeration steps, recorded in full in the .gz file (`reproduction`, `fixpoint`, `history`). For the 200 certified words, `certificate_chain` proves W = P·g⁻¹·word·g with P a product of conjugated fifth powers.
- **Candidate record fields:** `id`, `kind`, `status`, `word`, `length`, `W`, `W_length`, `construction`, `levels`, `t3u`, `certified`, `d_steps`, `solvers` (one line per solver with its parameters), `rev4_record_sha256` (pointer to the full record in the .gz file).
- **Caveats.** The 15 uncertified words rely on a coset-enumeration step; its relator set comes from the R7 table (`b25_full`), which is cited only by sha256. The .gz file is the private rev 4 file published unchanged, so it still says `"private": true` inside. Hardness is relative to the solvers listed; no lower bound is claimed.

## Revision 3 (2026-10-30): algo-mixer reducer breaks and shortest known words

> [!info] Plain English
> We ran a different kind of solver on all 215 candidates: the algo-mixer beam reducer, which rewrites with large kbmag rule sets (up to 14.4 million rules) and may let a word grow before it shrinks. It reduced 8 candidates to the empty word; each has a recorded, independently replayed certificate, confirmed by the Validator. Those 8 move to `tested`. The other 207 stay candidates. For 38 of them the runs found a shorter equal word, now stored as `shortest_known` next to the original.

- **The solver.** algo-mixer `reduce_standalone` (GreedyReducerTransport / try_all_strategies: forward and inverse rules, braid moves, beam search up to 5·|w|+50 letters). Rule sets: b25_gen (656k), rec, slx, rpo (2.9M), rpo_rtl (3.2M), shortlex (7.5M), and all six merged (14.4M). `solver_identity.algo_mixer_reducer` lists them.
- **The ladder** (`mixer_ladder`, 12 runs): small settings on all words, then larger rule sets and wider beams on the survivors, ending with all six sets merged at beam 4096 / 900 s on the 207 survivors; the shortened words were re-run through the fixpoint loop (R, CL, KB, D) after each step. Seven breaks came in the first run (b25_gen, beam 1024); the eighth (C3r2|3,3|23) needed four reducer runs and a final 2.5-reduction step.
- **Broken records** (`tested`, `status` "broken ..."): `registry_word` (the revision 2 word), `mixer_break` (run, job, rule sets, settings), `certificate_chain` (`chain_cells` as [core, conjugator], the registry word = ∏ conj⁻¹·core·conj), level L0-cert. C1|6|0: the registry word → empty certificate is complete, but its link from the construction W rests on a coset-enumeration step, as in revision 2.
- **`shortest_known`** (38 candidates): `word`, `length`, `how_obtained` (start length and each run with job id and length), `certified: false`. The equality with the registry word rests on the solver steps; the reducer paths of these shortenings were not recorded.
- **Caveats.** Certificate cells include fifth powers of period > 7 (up to 29): valid in B(2,5), but outside the period-≤7 relators our other solvers use. The algo-mixer build used is branch `alex-exp` of ai-math-edu-lab/algo-mixer (commits 7dff5cc, fbc2870); the certificates do not depend on it. Hardness of the 207 is relative to the solvers listed.

## Derivation

1. **Originals.** Copied from Lead's private file of the 12 confirmed T-024 words: word, R7 certificate and the relators it uses. Only the four words that left residuals are included.
2. **Residuals.** Taken from the owner's file:
   - R1, R2 and R3 are the end points of the owner's chain;
   - R3's last step (251 → 249 letters) is the owner's run at D(10⁹ cosets, rml 9) on a larger machine, recorded as owner-reported.
3. **Reproduction blocks.** Taken from the Validator's reproduction of the chain: every intermediate word, the parameters and the throw stage.
4. **Certificates of R1–R3.** kbmag's rec system reduces each residual to the identity. kbcert turns that rewriting path into an R7 certificate, which is checked by re-expansion (L0).
5. **Solver verdicts.** From the T-027 solver harness on each record.

## Vetting

| Check | Tool | Object / scope | Result |
|---|---|---|---|
| L0 of all 7 certificates (re-expansion to the word) | Developer's builder; Validator's independent expander | free B(2,5) — **proof** | 7/7 (both) |
| Words equal their sources (private file, owner's file, Validator chain) | Validator | syntactic | 7/7; the 4 reproduction chains match word for word |
| Trivial in B₀(2,5) | GAP 4.15.1 + anupq, class 12, order 5³⁴ | finite quotient — consistency only | 7/7 (Validator, 2026-10-20) |
| kbmag reduction to IdWord | kbmag kbprog + wordreduce, `b25_full`, rec and slx, `-me 100000` | free B(2,5) — **proof** | 7/7 (Validator, 2026-10-20) |
| No machine paths | grep | syntactic | 0 hits (Lead) |

## Caveats

- **No candidates yet.** Every record is broken by kbmag; the file records history, not hard instances.
- **R3's last step is owner-reported.** The Validator reproduced the chain up to 251 letters; the 251 → 249 step needs D(10⁹, 9) and was not re-run. R3's own certificate does not depend on it.
- **ρ_min16 = 1.0** means only that 2.5-reduction does nothing; it says nothing about other solvers.

## How to load

```python
import hashlib, json
p = "data/b25_challenge_candidates.json"   # path from config
assert hashlib.sha256(open(p, "rb").read()).hexdigest() == "<sha256 of the revision you use>"
reg = json.load(open(p))
rel = {int(k): v for k, v in reg["relators"].items()}
for rec in reg["candidates"] + reg["tested"]:
    print(rec["id"], rec["length"], rec["levels"], rec["status"])
```

## Change log

| revision | date | sha256 | change | approved by |
|---|---|---|---|---|
| 1 | 2026-10-20 | `754f582c…d920` | First revision: 0 candidates; 7 tested records (3 residuals, 4 originals). Vetted in [[2026-10-20-t027-registry-rev1-vet]] | owner (commit approved 2026-10-20) |
| 2 | 2026-10-28 | `6060c5b9…eef2` | T-028: 215 approved candidates (all pass T3u, the fixpoint loops of 2026-10-27 and the held-out solvers; 200 certified, 15 with a coset-enumeration step); 5 broken T-028 words added to `tested`; the 7 revision-1 records unchanged. Full records in `b25_t028_survivors_220_rev4.json.gz` (`2c321be5…e5fa`) | owner (approved 2026-10-28) |
| 3 | 2026-10-30 | `32f083dc…6d95` | algo-mixer reducer ladder: 8 candidates broken (C1\|6\|9, C3r2\|2,2\|1, C3\|4\|19, C1\|6\|0, C1\|8\|0, C1\|8\|7, C1\|16\|22, C3r2\|3,3\|23), each with a Validator-confirmed certificate, moved to `tested`; 207 candidates remain; `shortest_known` on 38 candidates; `solver_identity.algo_mixer_reducer` and `mixer_ladder` added | owner (approved 2026-10-30) |

## Related material
- [[datasets-convention]]
- [[challenge-gen-success-metrics]]: levels, solver resilience and the registry rules
- [[t024-challenge-census-and-onion-probe-2026-10-17]]: where these words come from, and their solver history
- [[2026-10-20-t027-solver-reproduction]]: the Validator's reproduction of the owner's chain
- [[Challenge Generation/_progress]]
- [[project-challenge-gen]]

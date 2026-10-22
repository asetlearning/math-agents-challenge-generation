---
title: B(2,5) challenge-candidate registry — approved candidates and tested words, with certificates
dataset_id: ds-b25-challenge-candidates   # living registry (owner, 2026-10-20): one file, revisions tracked below
date: 2026-10-20
domain: group-theory
project: challenge-gen
instance: B(2,5)
kind: trivial-words
format: "JSON (schema b25-challenge-candidates v1); letters a A b B (A = a⁻¹, B = b⁻¹); certificates as lists of [relator index, conjugator] over the R7 table, with the used relators included"
records: "revision 1: 0 candidates, 7 tested (3 residual words, 4 originals)"
files:
  - path: "math-agents-challenge-generation:data/b25_challenge_candidates.json"
    sha256: 754f582c8b02bca1d5cf599a7f680ee9b501f6c4215852b50560f585d8f8d920
    bytes: 1378235
    role: data
storage: git (math-agents-challenge-generation data/)
derived_from:
  - "Lead's private results file of the 12 Validator-confirmed T-024 words with R7 certificates (gitignored), sha256 cd1ae09d3a0455ac45dff22950f066cb3fd76c92dc1df4069555a668ba1c17be — origin: T-024 onion pilot, [[t024-challenge-census-and-onion-probe-2026-10-17]] §10.6"
  - "the owner's residual-words file of 2026-10-19 (gitignored shared/ folder), sha256 890d6de4cee833109fb2e462462623bb9e9116f5ea549e47711addebaabab75e — origin: the owner's solver chain on the 12 words"
produced_by: "b25_pyproject_agentic, branch t027-candidates-solvers: experiments/challenge_gen/solvers/build_candidates.py (sha256 63118b080b9a4702f568d6bc58c57cbf693cadcfd3189dea1273d725dfb1418e; solver harness, 13 files, sha256 b826ff9852b97549b7c65cee0405485d509ef9c5ab4ebecfb5b1075cdf55fb26); repo@sha added when the branch is committed"
property_claimed: "Every record is trivial in free B(2,5), proved by an R7 certificate that re-expands exactly to its word (L0-cert). 'candidates' holds human-approved challenge candidates; 'tested' holds evaluated words that are not candidates, with their solver verdicts."
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
stats: {min_len: 47, max_len: 1548}
used_by: ["`[[challenge-gen-success-metrics]]` (solver resilience, registry rules)"]
supersedes: ""
superseded_by: ""
author: asetlearning
status: draft
tags: [agent/lead, user/asetlearning, domain/group-theory, topic/b25, topic/burnside, topic/trivial-words, topic/hard-instance-generation, topic/proof-certificates, project/challenge-gen, status/draft, dataset]
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

## Related material
- [[datasets-convention]]
- [[challenge-gen-success-metrics]]: levels, solver resilience and the registry rules
- [[t024-challenge-census-and-onion-probe-2026-10-17]]: where these words come from, and their solver history
- [[2026-10-20-t027-solver-reproduction]]: the Validator's reproduction of the owner's chain
- [[Challenge Generation/_progress]]
- [[project-challenge-gen]]

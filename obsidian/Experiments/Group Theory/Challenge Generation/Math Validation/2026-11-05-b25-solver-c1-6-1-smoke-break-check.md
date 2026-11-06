---
type: validation
date: 2026-11-05
author: Validator (asetlearning)
project: "[[project-b25-solver]]"
subject: "C1|6|1 break by the E0 smoke (T-blind pool, M2): certificate, provenance, route"
status: verified
tags: [agent/validator, user/asetlearning, domain/group-theory, topic/b25, project/b25-solver, status/verified]
---
# C1|6|1 smoke break

Triage: [[2026-11-05-b25-solver-c1-6-1-smoke-break-check-triage]]. Own pure-Python free reduction (`python -I`, script outside the data). Inputs: `runs/b25-solver/E0-smoke-2026-11-05/` (certificate, record, config, log, `out/`), registry rev 3 in `data/`, the b25-solver code `seed_pool.py`, `e0.py`, `certificate.py`. No word strings here.

## Verdict
**(1) Certificate CONFIRMED (L0-cert). (2) Provenance: no recipe leak found, BUT the pool word named in the hand-over is not the word that produced the hit. (3) Route consistent, with the same correction. (4) Bench contract: verified-cert on the earlier bench head; the current head cannot run on the VM (no compiled extension).**

## 1. Replay
- 9 cells, all cores reduced literal fifth powers, periods 14, 8, 8, 18, 8, 14, 20, 6, 6 (cells above period 7 are allowed in an L0 certificate), `out_word` empty.
- The free reduction of prod conj^-1 core conj equals the rev-3 registry word of C1|6|1 (138 letters) exactly. `g` is non-empty (72 letters) but `g^-1 . '' . g` cancels, so the chain alone gives the word.
- The registry copy used by the run (`runs/t028-mixer/registry-rev3/`) has the same 207 words as the public data file, revision 3.

## 2. Provenance
- **T-blind inputs.** `seed_pool.blind_pool(n, 7, seed)` takes only the PatternBoost sampler (`generate_words`, seeded) over `build_standard_relators(7)`, which in the C++ source enumerates all words of length <= 7 and takes their fifth powers: **no data file, no recipe, no certificate, no t-word.** The run's registry and the t-pool/R7 table files are read in `main` for the T-in and T-out tracks and the target words only; the construction record of the target is used only to exclude its own recipe from T-in/T-out pools.
- **Scorers.** `GroupDistanceScorer([target word])`, `EditScorer([target word])` and the hybrid of the two receive the target **word** only, never the construction, the recipe or a certificate. Seeing the word is what a solver is allowed to do. The config has no `shortest_known` or recipe input.
- **Which u.** The hand-over says the pool word has 104 letters and 3 cells of periods 6, 7, 7 (the record file confirms this: it replays to its word). **The certificate does not contain that word.** Only two cells carry periods <= 7 and both are images (letter automorphism, rotation) of the period-6 core of the record; no cell is an image of either period-7 core; no contiguous block of the chain is conjugate to any of the eight letter-automorphism images of the record word. The two period-6 cells multiply to a word of cyclic length 64, not 104. The run log fits this: for T-blind, the best common factor rose from 16 (pool) to 26 after local search, and M2 (`n_r` = 2) takes the words with the longest common factor, which are the two **local-search descendants** of the top-2 pool words; `local_search` keeps the parent's id, so the shortening is recorded as `T-blind|1|59`, and `write_pools` was false, so the descendant was not saved. The record file is the raw pool word regenerated from the seed.
- So: the break came from a 2-cell local-search descendant of a blind-pool word, built from relator cores of the T-blind records only (`local_search` takes its relators from the cores of the records it is given). That is still recipe-blind, but the artefact trail names the wrong word. The exact descendant is not on disk; the certificate itself is complete and replays without it.

## 3. Route math
z = image_k(w) under a letter automorphism (and inversion), z' = rotation of z, ru = rotation of u', x = red(ru^-1 z'), then R2.5 reduces the cyclic core of x to the empty word. Then z' = (ru) x with x a product of conjugates of literal fifth powers (the R trace cells, rotation cancelling around the empty result), so w = (R cells)(u' cells) after pulling back through the letter automorphism, and the result is a product of cells over literal fifth powers. In the certificate the chain splits as 7 R-type cells (periods 8..20, product of reduced length 150, which is also cyclically reduced) followed by the 2 period-6 cells of u' (product of reduced length 112, cyclic length 64), and red(Q . U) equals the registry word. I did not replay the hit (image k, rotations) itself: it needs the compiled `GroupDistanceScorer` and the descendant word, neither of which is available; the free-group identity above does not depend on them.

## 4. Bench contract
`bench solver REGISTRY OUT --cmd` with a stub command that returns the stored certificate as a `broken` claim:
- earlier head (`b25-bench`, 713055d, pure-Python replay): **verified-cert**, method "solver certificate";
- negative control (one conjugator damaged by a letter): `unverified`, `certificate_rejected`;
- current `b25-solver` head: the verifier calls the compiled `tcgraph_ext` (`replay_chain`, `whitehead`), which is not built on the VM, so the CLI stops with `ModuleNotFoundError`. Not a finding about the certificate; to run it on that head needs the extension (a build or a cpuserver job).

## Not checked
Reproduction of the pool and the local search (needs the compiled extension); the second target C3|4|22 (no break was reported for it).

---
type: validation
date: 2026-10-23
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028: vet of the private registry DRAFT rev 2 (10 certified survivors in 'tested')"
status: confirmed-with-fixes
---
# T-028 registry rev 2 draft: vet

Triage: [[2026-10-23-t028-registry-rev2-draft-vet-triage]]. Draft: private, sha256 `ca674428...a92d8` (matches the Developer's hash). Base: `data/b25_challenge_candidates.json` rev 1. **No word strings in this note.** Not opened: job-1 A_R outputs, pilot rows, B/B0 outputs, the survivors file beyond what the certification summary holds.

**Verdict: CONFIRMED WITH FIXES (F1-F4).** The 10 certificates, chains, levels and B / B-ext labels are true to the evidence I recomputed. The attack label is not (F1), and the new records lack a provenance entry (F2). None of F1-F4 touches the math of a certificate.

## Verified (my own code unless noted)

| # | Check | Result |
|---|---|---|
| 1 | Diff vs rev 1 | Only `revision` (1 -> 2), `change_log` (+1 entry), `tested` (7 -> 17). The first 7 records are byte-identical. `candidates` empty, `approved_by` null. |
| 2 | Schema | The 10 new records share one key set (`certificate`, `certificate_chain`, `id`, `kind`, `labels`, `length`, `levels`, `origins`, `reproduction`, `rho_min16`, `solver_verdicts`, `status`, `t3u`, `word`). Rev-1 records have a different shape (`solver_verdicts` of 9 solvers, `reproduction` null). The new keys are additive; rev-1 `levels`/`status`/`kind`/`rho_min16` keep their meaning. |
| 3 | L0 per record | Written from the definition: every `table_entries` item is cyclically reduced and a literal fifth power; cells (k, c) expand as the free reduction of the product of c^-1 E_k c to the word, exactly; table distinct and every entry used; stated L = largest primitive-root period over the entries used; `n_cells` matches. 10/10. So each word lies in the normal closure of the fifth powers in F2: trivial in the free Burnside group B(2,5) by definition (no finiteness of B used). |
| 4 | Chain W -> residual | Own replay: W (the first reproduction step's input, length = `W_length`) equals P . g^-1 residual g after free reduction, with P the product of conjugated fifth-power cells. 10/10. |
| 5 | Reproduction blocks | Logged steps chain correctly under the adoption rule "a step is adopted only if it shortens the word": every step's input is the last adopted output, a 'length-neutral rewrite' or 'unchanged' step changes nothing that follows, lengths match, the last adopted output is the registered word. 10/10. The R steps were run on the Mac (arm64); I did not re-run them. Their effect is covered by item 4. |
| 6 | rho_min16 and the R part of S1-each | R_2.5 (certify mode) on all 16 images with tcgraph 3673013 (built here from the committed tree): no image shortened, rho_min16 = 1.0 for 10/10. |
| 7 | Gate rows | The 10 records agree field by field with `runs/t028-certs/summary.jsonl` (lengths, cells, L, chain cells, R/KB step counts, l1_r25, s1_each, s2_chain, rho_S, components R, CL, KB, D1 all true). The file has 49 certified words, all T3u; the 10 are the 10 shortest by residual length. |
| 8 | Escalation labels | Ids, status and rung outcomes from `rungs.jsonl`/`summary.json` (ids and outcomes only): the 4 labelled B (C3r2\|2,3\|1, C1\|6\|1, C3r2\|2,2\|1, C3\|4\|22) are all in the registered 55-word B run; the 6 labelled B-ext are all, and only, in the 6-word B-ext run. Each has 6 rungs (D 2^25..2^28, KB 4x, 16x), all 'exhausted', status survived, systems_verified true, and the rung word length equals the registered length. The one word B shortened (C3r2\|3,3\|23) is not among the 10. |
| 9 | Privacy | No `/home`, `/media/psf`, `/tmp`, host names or token patterns in the draft. |

## Fixes

**F1. The attack label is wrong for 10 of 10 as written, and differently wrong by arm.**
Draft text (all 10): "no known construction-aware attack applies; planted structure measurably erased by distillation (controls: r11 control failed, P1 check failed)".
- A failed control does not show erasure. The r11 control failed every assessed stratum (blind R-only 8/49, KB 0/14), and the oracle diagnostic (given the true pair) recovered R-only words (29/49) at less than the 80 % line: the attack model is inadequate, so "not recovered" says little about the word. "Measurably erased" and "no known attack applies" are not supported.
- Owner decision (2026-10-23): C3 and C3r2 survivors are "attack-limited (single-pair A_R)", never counted toward the clean r11 recovery-resilient claim. 6 of the 10 records are C3 (2) or C3r2 (4); the arm is in `origins.arm`; the label must come from it. The 4 C1 records are not clean either: the control failed every stratum, so by the registered reading (control-passed stratum and residual length in range) no C1 record qualifies as a clean no-recovery.
- Suggested wording, one sentence per record: C1: "no recovery found by the r11 attack; attack-limited (the r11 control failed all assessed strata)"; C3 and C3r2: "attack-limited (single-pair A_R); not counted toward the recovery-resilient claim". If the 15-survivor post-hoc pilot covers any of these ids, add its result per record (I have not read it).
- Pending: the Developer's updated label (not seen). I re-check against it.

**F2. Provenance of the new records is missing.** `code` and `solver_identity` still describe the rev-1 build (tcgraph 63564c3, b25 d1b5d0f). The new records were produced with tcgraph 3673013 (canonical R tie-break, f4b7771) and the T-028 code (certification 8c82edf, escalation jobs, kbmag held-out systems). Add a per-revision or per-record identity (tcgraph, b25, kbmag build, system hashes, rjob run ids).
Why it matters, found while vetting: for C3r2\|2,3\|9, R built before the canonical tie-break (my older local build) reduces the word to the empty word on all 16 images in certify mode; with 3673013 it is unchanged on all 16. The other nine agree in both builds. R is a heuristic whose result depends on tie-breaks, so L1-r25 for that word holds for the pinned R only. State "R at tcgraph >= f4b7771" in the level, and treat that record's L1-r25 as the weakest of the ten.

**F3. Scope of the levels and of the B label.**
- S1-each and S2-chain were run with the recorded deviations: D1 and S2-chain on the identity image only (D(20M, rml 5)); R and KB on 16 images; "certify mode" is plain R (no trace). Say so in the record or in `levels_note`.
- "16x budgets" is exact only for KB (maxeqns 4x and 16x). D went to 2^28 cosets, about 13x the job-1 bound of 20M. Write "KB 4x/16x, D to 2^28 cosets".
- B means inside the registered 55-word sample, B-ext outside it; keep the draft's own gloss in `levels_note` or the label.

**F4. Selection and private fields.** The records do not say that the 10 are the 10 shortest of 49 certified, nor that 39 certified words are not registered; add the rule in `change_log`. `origins` and `reproduction` hold the construction word W (hundreds of letters) and trace cells: fine in a private file, but they must be stripped or consciously released before any public move (a public W gives the construction away).

## Not checked

CL, KB and D1 of S1-each, and S2-chain (taken from the Developer's gate rows; the kbmag systems and `b25_full` are not in this tree); the job-1 held-out verification (it sits in the job-1 survivor records, which I did not open; the certification selection takes only 'verified' ones); the Mac R runs; the new `change_log` wording is a DRAFT marker and must change at approval. Not a claim about hardness: certified (L0) means trivial in free B(2,5) and nothing else.

Scratch (not committed): own replay code, a local tcgraph build at 3673013, the 16-image R recompute.

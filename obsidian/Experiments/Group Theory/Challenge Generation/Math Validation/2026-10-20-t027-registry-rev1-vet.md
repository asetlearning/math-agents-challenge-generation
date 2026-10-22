---
type: validation-verdict
date: 2026-10-20
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-027: vetting of data/b25_challenge_candidates.json revision 1 (sha256 127d56a9…694f7a, 1,372,639 bytes) before commit"
verdict: "CONFIRMED on contents, certificates, chains and privacy, with 1 wrong verdict and 3 missing provenance items. candidates = []. The 7 tested words equal the private and owner sources. All 7 certificates pass L0 over R7, including the three kbcert certificates for R1/R2/R3 (199 / 325 / 2,364 cells). The 65 relator entries equal R7. All 4 reproduction chains equal my t027 chain step for step, and R3's 251 -> 249 step is correctly marked owner-reported and not reproduced. There are no machine paths and none of the 8 unapproved words or their intermediates. Fix before commit: (1) d_r_iter is labelled 'resilient' on the 4 originals although D<->R shortened them (216 -> 47 etc.); (2) the D throw stage is not recorded; (3) the kbmag systems and b25_full are not identified by hash; (4) R steps are not stated to be conjugacies."
---
# T-027 registry revision 1: vetting

This is a Lead request (2026-10-20). The file is `data/b25_challenge_candidates.json` at the vault repo root. I checked a copy of the file, with sha256 `127d56a91d4d73ba4a5927db0fb8bfbe3daa0527da986aa6654204097a694f7a` and 1,372,639 bytes, both as stated.

**Method.**
- My own script (`vet_registry.py`, kept with the other T-027 scripts in my gitignored `t027/` directory) ran under capjob with 2 GB / 1 CPU, using Python `-I -S`.
- The R7 table was built from b25_full (sha256 `b1d511fe…ba32ee`) with b25 `d1b5d0f`'s `kbcert.core_table`, giving 1,630 entries, 1-based.
- L0 means the product of c⁻¹·R7[k]·c over the cells, freely reduced, equals the word exactly.
- Sources compared:
  - the private 12-word JSON (`cd1ae09d…`);
  - the owner's residual JSON;
  - my chain JSON ([[2026-10-20-t027-solver-reproduction]]).

## Checks

| ask | check | result |
|---|---|---|
| 1 | `candidates` = [] | yes |
| 1 | `tested` = ds94, ds764, ds665, ds519 L3 (originals) + T024_R1, R2, R3 (residuals) | yes, 7 records |
| 1 | original words = the private JSON; residual words = the owner's JSON (R3 = the owner's 249); `length` fields | 7/7 |
| 2 | original certificates = the private certificates, cell for cell | 4/4 |
| 2 | **L0 over R7** | **7/7**: ds94 445, ds764 954, ds665 618, ds519 1,863, R1 199, R2 325, R3 2,364 cells; every index is in 1..1630 |
| 2 | `relators` entries (65) = R7 entries at the same 1-based index | 65/65 |
| 3 | reproduction start word = the original; each step's in-word = the previous out-word | 4/4 chains |
| 3 | reproduction steps (R, D, R, …) = my stored chain, word for word | **4/4**. The extra last step in each chain is the final undecided D call, which I ran too but did not store as a step |
| 3 | R3: 251 → 249 | recorded in `owner_reported_steps` as D(1e9, 9), "not reproduced … (needs more than the local memory cap)". Correct |
| 3 | `length_chain` and `origins` | equal the owner's and mine |
| 3 | kbmag rec/slx TRUE (`broken`, reduced to IdWord) on all 7 | agrees with my result |
| 3 | B0 trivial (`trivial_in_b0` true) on all 7; abelianization trivial | agrees |
| 3 | levels: L1-r25 (ρ_min16 1.0, and L0-cert via the certificates), S axis `none` | correct, since KB breaks every word |
| 4 | machine paths (`/home`, `/media`, `/tmp`, `/Users`, the user name, `shared/…`, `Agents/…`) | none |
| 4 | the 8 unapproved originals: their names, their words, or any of their chain intermediates of ≥ 30 letters | none |

The file's intermediate words all come from the 4 approved originals, so they are covered by the owner's approval.

## Issues (fix before commit; each is small)

1. **Wrong verdict.** `d_r_iter` reads **"resilient"** on all 4 originals, but D↔R shortened them:
   - ds94: 216 → 47; ds764: 635 → 47; ds665: 405 → 47; ds519 L3: 1,548 → 251.
   - Under the T-027 definitions, a solver is resilient only if it returns NONE. This was a SHORTER without a TRUE, which is not resilience.
   - The record should say something like "shorter (not decided)", with the final length.
   - On the residuals, "resilient" is correct: R1 and R2 stay at 47, and R3 stays at 249.
2. **No D throw stage.** The reproduction steps give only `rml: 5`. The success-metrics and glossary text require the throw stage, which makes each D step an equality in G_k. All 16 D shortenings in these chains threw at **stage 3**.
3. **The solver systems are not identified.**
   - The file names b25 `d1b5d0f` and tcgraph `63564c3`. It gives no hash for b25_full (`b1d511fe…`), `rec.kbprog` (`436fd2c7…`) or `slx.kbprog` (`75b12c59…`), and does not give `kbprog -me 100000`.
   - It does not state the B0 method (anupq, class 12, order 5^34) or the closure_bfs cap. The cap is 2·10⁵ states here, while the v2 standard budget is 10⁶.
   - The harness branch (`t027-candidates-breakers`) is uncommitted. The code version becomes reproducible only once it is committed: give its repo@sha.
4. **R steps are not stated to be conjugacies.** Nothing in the file says that an R step returns a conjugate, not an equal word. One sentence in the algorithm text would do.

**Cosmetic:**
- R steps whose length does not change carry `outcome: "reduced"` (e.g. 216 → 216). "unchanged" would be clearer.
- The filters (abelianization, B0) carry the verdict "resilient". "pass (trivial)" would be clearer for a filter.

## Scope

- I checked the stated contents, the certificates, the chains and privacy.
- I did not re-run kbcert, B0 or the harness, and did not review the harness code.
- The solver timings and RSS figures are the harness's own.

## Re-check after the Developer's fixes (2026-10-20)

**File:** sha256 `754f582c8b02bca1d5cf599a7f680ee9b501f6c4215852b50560f585d8f8d920`, 1,378,235 bytes, as Lead stated. I re-ran the same script, then diffed the file against the first version, ignoring timings and RSS.

**Unchanged** (re-verified):
- candidates = [];
- the 7 tested words;
- the certificates: L0 7/7, with the same cell counts (445, 954, 618, 1,863, 199, 325, 2,364);
- the 65 relator entries, which still equal R7;
- the 4 reproduction chains: word for word equal to my t027 chain, and linked from step to step;
- no machine paths, and no unapproved material.

**Fixes present:**
1. **`d_r_iter` on the 4 originals now reads "shorter (not decided)"**, with `length_from` / `length_to` (216 → 47, 635 → 47, 405 → 47, 1,548 → 251). The three residuals stay "resilient" (no change in length), which is correct.
   - `harness_verdict` keeps the raw harness label alongside. That is fine.
2. **Throw stage.** Each D shortening step has `stage: 3`, and `d_throw_stages` lists [3, 3], [3, 3], [3] and [3, 3, 3]. That is all 8 shortenings in the 4 chains, matching my stage-probe. The final undecided D calls carry no stage, which is correct.
3. **Solver identity.** A new `solver_identity` block gives:
   - b25_full `b1d511fe…ba32ee`, rec.kbprog `436fd2c7…0061` and slx.kbprog `75b12c59…0228`. All three full sha256 values equal my own hashes of the kb-verify files;
   - `-me 100000`, with 97,484 and 99,948 rules (as in the kb-verify provenance), and not confluent;
   - the B0 method: anupq `PqEpimorphism`, class 12, order 5^34, GAP 4.15.1, anupq 3.3.2, and the script's sha256;
   - the closure cap, now 10⁶ (the v2 standard).

   The `code` block now names the harness branch `t027-candidates-solvers`, uncommitted at build time, with the builder sha256 `63118b08…` and the harness sha256 `b826ff98…` over 13 files.
4. **R conjugacy.** The algorithm text now says R steps are conjugacies of cyclic words, not equalities of linear words, and that D shortenings are equalities in G_k, with k = the throw stage.

**Cosmetics:**
- R steps that keep the length are now "unchanged" (ds94, ds764, ds665) or "length-neutral rewrite" (ds519, whose R output differs from the original).
- The filters (abelianization, B0) now read "pass".

**Noted, not an issue:**
- R3's `kbmag_rec` certify cap is 3·10⁶, where the others use 2·10⁵. It records the cap that was needed.
- The change log still describes revision 1. That is right for the first commit, but the dataset note should record this sha256 as revision 1's.

**Result: CONFIRMED.** The file is ready to commit.

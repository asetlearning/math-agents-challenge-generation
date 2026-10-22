---
type: validation-verdict
date: 2026-10-20
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028: confirmation of the generation-strategy proposal v2 and the pilot pre-registration draft"
verdict: "v2: CONFIRMED. It resolves all 8 issues of my triage, with one leftover: the residual's certificate needs U_L with L = the longest period used, not 7m. Pre-registration: NOT YET READY TO RUN. Two blocking defects: (1) the B probe's sampler glues each new cell along a single arc, so the last cell always exposes about 4|u| > 2.5|u| and the yield is about 0 by construction, which would fire the drop rule spuriously; (2) the ladders and F3 do not name the procedure, rml or success criterion, and on residuals that already resist D(20M, rml 3) and in-loop KB they are degenerate (floor-censored D, never-succeeding kbmag). Seven smaller pins are also needed: the S1-each definition, uncertified KB steps, capped distillation, F2 versus the recovery attack, the attack input for C1, the 2^25 memory margin, and the run-length rule. Everything else is complete and unambiguous."
---
# T-028 v2 and the pilot pre-registration: confirmation

This is a Lead request (2026-10-20). It covers `MathExpert/proposals/2026-10-20-t028-generation-strategy-long-peaks-v2.md` and `2026-10-20-t028-pilot-preregistration-draft.md`, checked against my triage [[2026-10-20-t028-generation-strategy-review-triage]].

**Method.** I checked the logic. I ran one count: the t-pool, built from b25 `d1b5d0f`'s `load_data` sources (`certs_gt53.jsonl`, `seeds_power_free_len_le53.jsonl` and the 20261014 dataset file), holds **453** certified words, **351** of them of length 50–80. That is enough for every arm.

## v2 against my 8 issues

| # | issue | v2 |
|---|---|---|
| 1 | certificates over U_{7m}, L0 tooling | resolved (§2): L = 7m, and 7·m₁·m₂ for two rounds; a per-word table for the L0 expander; depth not measured. **Leftover:** the distilled residual's certificate also holds R-step cells, whose periods can exceed 7m (a power of period h in t becomes period m·h in W). Record L = the maximum period actually used, per word |
| 2 | sign of the half-exposure lemma | resolved |
| 3 | the C′ claim | resolved: it is now a property of the attack |
| 4 | Hall–Petresco | resolved: about 6 cells, and dropped from the pilot |
| 5 | onion e = 0 | resolved: "e_V ≤ 2·max s, argued, not shown", with the caveats |
| 6 | U2, U3, the D tube | resolved: U2 withdrawn, U3 on D-free stretches only, the tube claim conjectured |
| 7 | overfitting on compression | resolved: C′ does not select on compression, and the attack is reported with and without stage 1. (v2 §4 also lists "residual length after R" as a selection statistic, but the pre-registration uses only junction cancellation. Keep one) |
| 8 | pinning | mostly resolved in the pre-registration. See below |

The other v2 statements I checked are correct: FFL as the named move set; the one-directional monotonicity; CTRL as a theorem for Dehn's algorithm on R_P and only a prediction for plain R; and the privacy rule (no private T-024 words).

## Pre-registration checklist

| item | status |
|---|---|
| arms and cells (C1: 5 m; C3: 3 m; C3r2: 3 matched (m₁, m₂); CTRL), 30 words per cell, seeds | complete. Name the seed hash (sha256 of the tuple). Pin how the ±1 per factor and the t_j are drawn (uniform, with replacement from the 351) |
| selection statistic disjoint from the held-out attack | yes: junction cancellation and \|W\| ≥ 0.6 × the uncancelled length; no compression |
| in-loop D steps certified by kbcert on the loop | specified. **Add the same rule for KB steps** (if kbcert fails, skip the step). **Add the gate consequence:** a skipped D or KB step means the residual is not a fixpoint of that solver, so it fails S1-each and is counted as such |
| U_L table for L0 | specified for W. See the leftover under issue 1 for residuals |
| caps and how capped words count | F1 and F2 are specified. **Missing:** what happens to a word whose *distillation* hit the 1 CPU-h cap. Is it gated, and does it enter F2's denominator? Suggest: gated and reported, but excluded from F2 |
| S1-each | **ambiguous.** Step 3 says "S1-each against the in-loop list" (D at rml 3, KB in screen mode). The metrics' S1-each is R, CL, KB and D1 = D(20M, **rml 5**) at the standard pins. Use the official definition, or report it as "S1-each (in-loop)" and the official S1-each separately |
| F1 | complete: per arm and per m, denominator 30, capped counts as not emptied |
| F2 | nearly complete: broken = TRUE, ≤ 1 CPU-s on the VM, n ≥ 20, SHORTER reported separately. **Pin whether the recovery attack counts as a held-out solver for F2.** It has its own 10 CPU-s rule and F4, so suggest excluding it |
| F3 and the ladders | **blocking, see B2** |
| F4 | complete: success = (φ′, t′) verified plus kbmag ≤ 10 CPU-s; C1 is the control (≥ 90 % predicted; < 50 % means the attack is too weak). **Pin the attack input.** The pipeline runs it on residuals, which R has rewritten, so C1's control could fail from distillation rather than from a weak attack. Run it on W **and** on the residual for C1 |
| CTRL theorem check | sound. Dehn's algorithm on the symmetrised R_P empties every cyclically reduced trivial word under C′(1/6) (Greendlinger; Lyndon–Schupp V.4). The threshold "piece < (5/6)\|u\|" is right, since \|r\| = 5\|u\|. **Pin that pieces include self-overlaps** of u⁵ with its non-trivial rotations and with inverses, not only overlaps between different cells. Report the rejection rate |
| ladders and the rjob boundary | rjob for 2^26 – 2^28, with a plan first: correct. **2^25 locally is marginal.** D at 20M (about 2^24.3) used 1.1 GB, so 2^25 ≈ 33.5M needs about 1.8 GB plus Python, against the 2 GB cap. Measure once at 2^25 first, or set the local top to 2^24 |
| cost (about 40 CPU-h) | plausible as a central estimate. The worst case under the caps is far higher (1 CPU-h + 3 × 15 min per word × about 360 words), so the stop rule (first 20 words > 2× → re-plan) is the real control. **Run length:** about 40 CPU-h at 2 CPUs is about 20 h of wall time, above the standing ~2 h threshold. The owner's rule makes the VM the default, so Lead should confirm a local run of that length explicitly |
| held-out kbmag orderings | specified. They are new kbprog completions: record their `-me` setting and the hashes of the new systems in the TOML |
| B probe and its drop rule | the drop rule is decidable (yield < 1 % at every (ℓ, k), over 1,000 patches). **The sampler is defective, see B1** |

## Blocking defects

**B1. The B sampler yields about 0 by construction.**
- Each new cell u_new = w·z is glued along **one** arc w with |w| = ⌈1.25ℓ⌉ ≤ |u_new|. Its exposed arc then has length 5|u_new| − |w| ≥ 4|u_new|: a window of exponent ≥ 4.
- Fine–Wilf bounds any single shared arc below |u_i| + |u_new|, so no single-arc placement can bring the exposure down to 2.5|u_new|.
- The last cell placed is never covered afterwards, so its exposure survives into the boundary, apart from small free cancellation at its two ends.
- So the yield is about 0 for every (ℓ, k), and "drop B" would fire because of the sampler, not because the scheme is infeasible.
- **Fix:** each new cell (at least the last ones) must share arcs with the patch along **≥ 2 boundary arcs**, totalling ≥ 2.5|u_new|. This is the two-arc requirement v2 states, which the sampler does not implement. Alternatively, define the yield over closed patches (every cell's exposure ≤ 2.5|u|), with a sampler that targets closure.

**B2. The ladders and F3 are underspecified and degenerate on residuals.**
- "Minimum D bound" does not say:
  - which procedure: D1 single call, or D↔R;
  - which rml;
  - what counts as success: TRUE, the empty word, or any SHORTER.
- The ladder runs on residuals that are already **fixpoints of in-loop D(20M, rml 3)**. At rml 3, every bound ≤ 2^24 (< 20M) fails by construction, and only 2^25 can differ. At rml 5 or 7 the values could be meaningful, but they must be stated.
- "kbmag time" on residuals that are already **KB-screen fixpoints** is mostly "never".
- F3 (C1 only) could therefore fire for reasons that have nothing to do with growth.
- **Fix, for example:**
  - D ladder = D↔R at rml 7, success = the empty word or TRUE, bounds 2^20 … 2^24 locally (2^25 if the memory check passes), measured on **W** and on the residual;
  - kbmag ladder = the held-out orderings' time to IdWord, on W and on the residual, with a cap;
  - F3 applied to the W series, where the family parameter acts directly.

## Recommendation

- **v2: confirmed.**
- **The pre-registration needs one more revision before it goes to the owner.**
  - Fix B1 and B2.
  - Pin the smaller items above:
    - S1-each definition;
    - KB-step certification and the gate consequence;
    - capped distillation;
    - F2 versus the attack;
    - the attack input for C1;
    - the 2^25 memory check;
    - the residual U_L;
    - seeds and sampling;
    - the held-out system hashes;
    - Lead's go-ahead on a run of about 20 h of wall time.
- After these fixes, nothing in the pre-registration needs a further math decision.

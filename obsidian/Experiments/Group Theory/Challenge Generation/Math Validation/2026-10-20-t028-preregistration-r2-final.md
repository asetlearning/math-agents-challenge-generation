---
type: validation-verdict
date: 2026-10-20
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028: final pass on the pilot pre-registration r2 (and the two v2 [r2] edits)"
verdict: "CONFIRMED with one required fix. B1 is resolved (closed multi-cell patches, two samplers, drop only if both < 1% everywhere). Pins 1-7 are done. B2 is resolved except for one confound: the D<->R ladder on the C1 W series counts as a floor success every W that R alone empties, and the probe shows that this fraction falls with m (about 25% -> 2%). So F3 could pass on R's behaviour, not D's. Fix: run D first in each round, and exclude from F3 the W that R alone empties (report them). Five small implementation pins need no math decision."
---
# T-028 pre-registration r2: final pass

This is a Lead request (2026-10-20). It covers `MathExpert/proposals/2026-10-20-t028-pilot-preregistration-draft.md` (r2) and the v2 [r2] edits. Earlier note: [[2026-10-20-t028-v2-preregistration-confirm]].

## Resolved

| item | r2 | status |
|---|---|---|
| B1, the B probe | closed k-cell products (non-empty, 2.5-reduced, ρ ≥ 0.5); roots are mutated rotations of one seed (d ∈ {1, 2, 3}); greedy and beam-64 samplers; 1,000 per (ℓ, k, d, sampler); drop only if both samplers are < 1 % at every setting | **resolved.** The one-arc argument is right: a 2.5-reduced boundary offers a ≥ 2.5\|u\| shared run only at exact halves. "2.5-reduced ⇒ no exposed run > 2.5\|u_i\|" holds, since such a run is a window of exponent > 2.5. The drop rule is decidable |
| B2, the ladders | D↔R at rml 7, success = empty or TRUE, 2^20 … 2^24 (2^25 after a ≤ 1.9 GB check), kbmag held-out systems capped at 15 min, both on W and on the residual, F3 on the C1 W series | resolved, **except the confound below** |
| pin 1, S1-each | the official definition (D1 at rml 5, KB certify, both systems), plus "S1-each (in-loop)" | done |
| pin 2, KB/D steps | kbcert, or skip and log; a skip fails S1-each (in-loop) | done |
| pin 3, capped distillation | gated and reported; excluded from F2 | done |
| pin 4, F2 and the attack | the attack is excluded from F2 | done |
| pin 5, F4 on C1 | on W and on the residual | done |
| pin 6, 2^25 | after the memory check | done |
| pin 7, seeds and sampling | sha256 first 8 bytes, big-endian; PCG64; stream order fixed; t_j drawn with replacement from the 351; held-out system hashes in the TOML; CTRL pieces include self-overlaps | done |
| leftover from v2: the residual's L | L = the maximum period used, recorded per word | done |
| wall time | the owner chooses between about 20 h on the VM and rjob | done (owner's decision) |

**Junction rule.** It forces {last(x), last(y), first(x)⁻¹, first(y)⁻¹} to be the four distinct letters. So it is always satisfiable, and C3r2 at m = 2 has 24 (x, y) pairs per round. That is small but enough, since rounds compose. Some pairs are proper powers (x = aa), which is harmless over U_L.

## Required fix: R confounds F3

- In D↔R, R alone empties some W. The probe gives about 25 % at m = 4, 7 % at m = 8 and 2 % at m = 16.
- Those W succeed at the lowest rung whatever D does, if R acts first, or regardless of D's bound in any case.
- Their share falls with m. So a Kendall trend on the C1 W series can pass because R stops emptying, not because D needs more cosets. That would be a false "growth".
- **Fix (one line in §5 and §7):**
  - in each D↔R round, D runs first;
  - W that R alone empties are **excluded from F3's D series**, and their counts are reported per m;
  - the kbmag series is unaffected.

## Small pins (implementation; no math decision)

1. **A cap on kbcert per step.** The registry harness used 2·10⁵ states, and it failed on the 4 originals' rec paths after about 60 s. Without a cap, kbcert can use up the 1 CPU-h distillation cap.
2. **Kendall variant.** Use τ-b, with censored values tied at the top rung + 1.
3. **KB certify mode** (16 images × all rotations): batch all rotations in one `wordreduce` call per system. One call per rotation would cost hours at \|W\| ≈ 10³.
4. **The 10 ladder words per cell:** the first 10 by index among those passing step 3. For W, the first 10 by index.
5. **The B probe's move set:** state the conjugator range ("all rotations", and the suffix length the next factor may cancel against), and give a CPU estimate for the 72,000 products.

## Verdict

**CONFIRMED with the R-confound fix.** After that one line, nothing in the pre-registration needs a math decision during the run. The five pins are for the Developer.

---
date: 2026-11-13
agent: Validator
status: verdict-sent
---
# b25-solver B4 beam breaks: independent L0 replay

**Verdict: 3 of 3 L0-cert CONFIRMED** against registry rev 9 (116 candidates, 111 tested). Run 20261112-140433-c93577, certificates in `outputs/breaks.jsonl` (private, not quoted here).

**Method.** My own pure-Python free reduction (no kbmag, no finite quotient). For each row I checked that every core is a literal reduced fifth power and every conjugator is reduced. I then freely reduced the product of the cells x^-1·core·x, followed by the g^-1·g tail. The result must equal the registry word. I did not read Lead's replay beforehand.

| Target | Arm | Depth | Pool id | Letters | Cells | Max period | \|g\| | Open and untested in rev 9 |
|---|---|---|---|---|---|---|---|---|
| C1\|8\|24 | B | 3 | T-blind\|1\|4119 | 404 | 136 | 49 | 1920 | yes |
| C1\|8\|11 | B | 4 | v5\|1\|16347 | 459 | 68 | 35 | 155 | yes |
| C3\|6\|13 | BS | 2 | T-blind\|1\|3333 | 1109 | 405 | 31 | 0 | yes |

- The cell product alone, with no g, already equals the registry word in all three rows, so the g tail cancels.
- C3|6|13 at 1109 letters is the longest word broken so far, as Lead said.
- The max period of C1|8|24 is 49, above the T-blind sampler's 7 and above any v5 cell. That is not a contradiction: the L0 cells are cells of the beam chain, and the period is the pool-cell period above 7 that the E0 note already allows.

**Scope.** This is an L0 replay only. It proves the three words are trivial in B(2,5) by definition of the certificate. I did not check the beam route, the shortening step, the B3-dump starting words, pool provenance, or the bench contract. I did not re-run any job.

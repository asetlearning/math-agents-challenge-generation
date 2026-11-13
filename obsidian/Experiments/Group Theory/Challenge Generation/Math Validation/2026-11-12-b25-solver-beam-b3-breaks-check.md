---
type: validation
date: 2026-11-12
agent: Validator
status: 10 of 10 CONFIRMED (L0-cert)
---
# Validation: beam B3 breaks (job 20261112-033029-51091b)
Input: runs/20261112-033029-51091b/outputs/breaks.jsonl (10 rows, private words, none quoted); registry rev 9 (vault data/, 116 candidates, 111 tested). Own pure-Python free reduction in F_2; cell (c, x) = word x^-1 c x. I did not read the Lead replay file. Check: every core is x^5 (x non-empty, reduced); red(product of cells . g^-1 g) = red(registry word); id is an open rev-9 candidate.
| target | arm | depth | pool id | letters | cells | max period | \|g\| | result |
|---|---|---|---|---|---|---|---|---|
| C1|12|16 | B | 1 | T-blind|1|15736 | 458 | 66 | 48 | 265 | PASS |
| C3|4|5 | B | 2 | v5|1|3443 | 454 | 212 | 22 | 0 | PASS |
| C3|4|1 | B | 1 | T-blind|1|7619 | 418 | 155 | 19 | 931 | PASS |
| C3|6|28 | B | 4 | T-blind|1|1466 | 715 | 240 | 28 | 2130 | PASS |
| C1|8|12 | B | 4 | T-blind|1|4052 | 402 | 218 | 37 | 1478 | PASS |
| C3r2|3,3|3 | B | 3 | v5|1|19073 | 734 | 200 | 36 | 800 | PASS |
| C3|6|5 | B | 1 | T-blind|1|5456 | 816 | 217 | 27 | 1816 | PASS |
| C3|4|23 | B | 1 | T-blind|1|4026 | 744 | 277 | 19 | 3550 | PASS |
| C3|4|29 | B | 2 | v5|1|19743 | 730 | 341 | 20 | 3762 | PASS |
| C3|6|8 | B | 3 | T-blind|1|6782 | 1100 | 214 | 30 | 1946 | PASS |
The 10 targets are distinct, all open candidates in rev 9, none in tested; g cancels in every row. The registry lengths are 402-1100 letters (not 418-1100 as in the request: C1|8|12 has 402). Scope: L0 replay only (not checked: beam route and re-rooting, pool provenance, depth semantics, bench contract).

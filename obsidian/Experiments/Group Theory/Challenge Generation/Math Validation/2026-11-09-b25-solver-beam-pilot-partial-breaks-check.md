---
type: validation
date: 2026-11-09
agent: Validator
status: 9 of 9 CONFIRMED (L0-cert)
---
# Validation: beam pilot partial breaks (job 20261109-183503-e326b6, partial fetch)
Input: runs/20261109-183503-e326b6-partial/outputs/breaks.jsonl (8 rows, private words, none quoted); registry rev 7 (vault data/, 131 candidates, 96 tested). I did not read the Lead replay file. Own pure-Python free reduction in F_2; cell (c, x) = word x^-1 c x. Check: every core is x^5 (x non-empty, reduced) and red(product of cells . g^-1 g) = red(registry word).
| target | arm | depth | pool id | letters | cells | max period | \|g\| | result |
|---|---|---|---|---|---|---|---|---|
| C1|12|20 | B | 3 | long|1|19849 | 593 | 58 | 48 | 470 | PASS |
| C1|12|20 | M | 4 | v5|1|10032 | 593 | 54 | 48 | 796 | PASS |
| C1|12|20 | C | 1 | long|1|5351 | 593 | 34 | 48 | 160 | PASS |
| C3|4|18 | B | 4 | T-blind|1|5539 | 674 | 257 | 21 | 0 | PASS |
| C3|9|25 | B | 3 | v5|1|3701 | 796 | 166 | 39 | 2559 | PASS |
| C3|9|25 | M | 3 | T-blind|1|5053 | 796 | 156 | 39 | 2171 | PASS |
| C1|16|29 | B | 4 | T-blind|1|18668 | 685 | 178 | 61 | 0 | PASS |
| C1|16|29 | M | 4 | long|1|11170 | 685 | 148 | 61 | 0 | PASS |
All four targets are open candidates in rev 7 (none in tested); g cancels. Scope: L0 replay of the partial output only (the job was still running); not checked: the beam route, pool provenance, depths, bench contract.

## Addendum: final output (9 rows)
Final file runs/20261109-183503-e326b6/outputs/breaks.jsonl: the 8 earlier rows give the same numbers (all PASS). New row, same check (own code, rev 7): C1|16|29, arm C, depth 1, pool long|1|6365: 685 letters, 143 cells, max period 76, g empty, cores literal reduced fifth powers, red(product of cells) = red(registry word): PASS. C1|16|29 is an open candidate (not tested). Same scope as above (L0 replay only).

---
type: validation
date: 2026-11-07
agent: Validator
status: 14 of 14 CONFIRMED (L0-cert)
---
# Validation: experiment A breaks (14 rows, 5 targets)
Input: runs/20261106-182636-716a09/outputs/breaks.jsonl (private words; none quoted here); registry rev 6 (vault data/, 138 candidates, 89 tested). I did not read the Lead replay file before checking. Own pure-Python free reduction in F_2; cell (c, x) = word x^-1 c x.
Check per row: every core is x^5 with x non-empty (and freely reduced), and red(product of cells . g^-1 g) equals red(registry word).
| target | length | rows | cells | max period | result |
|---|---|---|---|---|---|
| C1|16|2 (v5 pool, v5|1|4778) | 834 | 1 | 41 | 69 | PASS |
| C1|12|14 (long|1|267) | 770 | 1 | 40 | 77 | PASS |
| C1|16|17 (long|1: 19219, 18971, 13676, 5918, 4748, 3128, 19945, 17182, 4766, 15616) | 720 | 10 | 20-28 | 63 | 10 x PASS |
| C1|12|1 (long|1|17888) | 639 | 1 | 40 | 40 | PASS |
| C1|12|25 (long|1|12461) | 615 | 1 | 25 | 47 | PASS |
All 14 pass; |g| is 175-697 and cancels. All five targets are open candidates in rev 6 (none in tested). The 14 pool ids are distinct; the 10 C1|16|17 rows are 10 different certificates of one word. The row length (tlen) equals the registry word length in all rows.
Scope: L0 replay only. Not checked: pool provenance (long pool, v5 pool), the solver route, bench contract.

## Addendum: final output, 6 new rows (20 rows in total)
Same check, own code: cores are literal reduced x^5 (x non-empty); red(product of cells . g^-1 g) = red(registry word of the target, rev 6). The first 14 rows give the same numbers as above. New rows (all PASS; all targets open in rev 6, none tested):
| row | pool id | letters | cells | max period | |g| |
|---|---|---|---|---|---|
| C1|8|16 registry | T-blind|1|17055 | 514 | 42 | 38 | 360 |
| C1|8|16 registry | v5|1|17723 | 514 | 47 | 38 | 452 |
| C1|8|16 end | v5|1|14501 | 514 | 38 | 38 | 0 |
| C1|8|16 end | v5|1|5666 | 514 | 40 | 38 | 0 |
| C3|6|23 end | T-blind|1|18433 | 667 | 181 | 30 | 0 |
| C3|6|23 end | T-blind|1|13005 | 667 | 181 | 30 | 0 |
The end-kind rows are chain certificates of the registry word (g empty, product equals the registry word exactly). The two rows of each pair are different certificates (the two C3|6|23 chains share 98 of their 181 cells; the others differ more). Scope as before: L0 replay only; provenance, route and bench not checked.

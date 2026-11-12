---
type: validation
date: 2026-11-11
agent: Validator
status: 11 of 11 CONFIRMED (L0-cert)
---
# Validation: beam B2 breaks (job 20261111-021531-a885ac)
Input: runs/20261111-021531-a885ac/outputs/breaks.jsonl (11 rows, private words, none quoted); registry rev 8 (vault data/, 127 candidates, 100 tested). Own pure-Python free reduction in F_2; cell (c, x) = word x^-1 c x. Check: every core is x^5 (x non-empty, reduced); red(product of cells . g^-1 g) = red(registry word); id is an open rev-8 candidate.
| target | arm | depth | pool id | letters | cells | max period | \|g\| | result |
|---|---|---|---|---|---|---|---|---|
| C3|6|7 | B | 2 | v5|1|4269 | 1017 | 139 | 29 | 1575 | PASS |
| C3|6|4 | B | 2 | v5|1|3572 | 911 | 144 | 38 | 2099 | PASS |
| C3r2|2,3|25 | B | 1 | T-blind|1|15171 | 916 | 299 | 36 | 0 | PASS |
| C3|6|0 | B | 2 | v5|1|15114 | 978 | 268 | 38 | 2259 | PASS |
| C3|6|16 | B | 4 | v5|1|634 | 683 | 169 | 28 | 2241 | PASS |
| C3r2|2,2|27 | B | 3 | v5|1|2811 | 704 | 134 | 20 | 989 | PASS |
| C3r2|2,2|9 | B | 3 | v5|1|17004 | 728 | 123 | 20 | 1811 | PASS |
| C3r2|2,2|22 | B | 2 | v5|1|180 | 615 | 112 | 20 | 1472 | PASS |
| C1|12|26 | B | 2 | long|1|7620 | 732 | 138 | 56 | 712 | PASS |
| C3|6|1 | B | 3 | T-blind|1|935 | 682 | 174 | 28 | 1629 | PASS |
| C3|4|20 | B | 2 | T-blind|1|2718 | 571 | 205 | 19 | 1078 | PASS |
The 11 targets are distinct, all open candidates in rev 8, none in tested. g cancels in every row. Scope: L0 replay only (not checked: beam route, pool provenance, depth semantics, bench contract).

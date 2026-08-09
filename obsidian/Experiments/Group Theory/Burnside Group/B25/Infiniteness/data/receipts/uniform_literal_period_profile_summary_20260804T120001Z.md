# Uniform Literal Period Profile

Generated epoch: `1785844801`

**Scope:** literal/free-group level only. No `G_L` word reduction or oracle is used; `G_L` reductions may shrink pieces.

## Piece Profile

| ell | periods | class pairs | max piece | ratio max/(5ell) | 1/6 threshold length | margin | strict C'(1/6)? | tail |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 4 | 9 | 36 | 3 | 0.150000 | 3.333333 | 0.333333 | yes | `{'1': 2, '2': 22, '3': 12}` |
| 5 | 24 | 276 | 4 | 0.160000 | 4.166667 | 0.166667 | yes | `{'1': 8, '2': 78, '3': 124, '4': 66}` |
| 6 | 58 | 1653 | 5 | 0.166667 | 5.000000 | 0.000000 | NO | `{'1': 8, '2': 283, '3': 730, '4': 434, '5': 198}` |
| 7 | 156 | 12090 | 6 | 0.171429 | 5.833333 | -0.166667 | NO | `{'1': 32, '2': 1250, '3': 4868, '4': 3694, '5': 1550, '6': 696}` |
| 8 | 405 | 81810 | 7 | 0.175000 | 6.666667 | -0.333333 | NO | `{'2': 4312, '3': 28984, '4': 28614, '5': 12996, '6': 4778, '7': 2076}` |
| 9 | 1092 | 595686 | 8 | 0.177778 | 7.500000 | -0.500000 | NO | `{'3': 176058, '4': 225924, '5': 113822, '6': 42396, '7': 14984, '8': 6490}` |
| 10 | 2940 | 4320330 | 9 | 0.180000 | 8.333333 | -0.666667 | NO | `{'4': 1722918, '5': 965171, '6': 372732, '7': 129760, '8': 45126, '9': 19392}` |

Critical witness records are stored in the JSON for every distinct-class pair with `piece_len >= ceil(5ell/6)`. Counts by ell:

| ell | critical threshold | critical pair count |
|---:|---:|---:|
| 4 | 4 | 0 |
| 5 | 5 | 0 |
| 6 | 5 | 198 |
| 7 | 6 | 696 |
| 8 | 7 | 2076 |
| 9 | 8 | 6490 |
| 10 | 9 | 19392 |

Decisive curve: largest strict ell is `5`; first strict failure is `6`.

## Orientation Input

| ell | periods | self-inverse classes | cross inverse pairs | max p^5 vs p^-5 overlap |
|---:|---:|---:|---:|---:|
| 4 | 9 | 0 | 0 | 1 |
| 5 | 24 | 0 | 0 | 1 |
| 6 | 58 | 0 | 0 | 2 |
| 7 | 156 | 0 | 0 | 2 |
| 8 | 405 | 0 | 0 | 3 |
| 9 | 1092 | 0 | 0 | 3 |
| 10 | 2940 | 0 | 0 | 4 |

## Cap Census Scaling

| ell | max cap len | freely reduced caps <= max, incl empty | exact max length caps |
|---:|---:|---:|---:|
| 4 | 3 | 53 | 36 |
| 5 | 4 | 161 | 108 |
| 6 | 5 | 485 | 324 |
| 7 | 6 | 1457 | 972 |
| 8 | 7 | 4373 | 2916 |
| 9 | 8 | 13121 | 8748 |
| 10 | 9 | 39365 | 26244 |

For `ell=5`, candidate caps of length `<=4` including the empty cap: `161`.

Free-level ell=5 cap-conjugacy scan:

- tested equations: `30912`
- solutions: `384`
- canonical caps: `384`
- axis-power duplicates: `0`
- exotic caps: `0`

Scaling formula for cap length `<= ell-1`: `2*3^(ell-1)-1`; exact top layer: `4*3^(ell-2)`.

## Interpretation

Literal distinct-class max_piece equals ell-1 throughout ell=4..10. Thus max_piece/(5ell) crosses the strict C'(1/6) boundary at ell=6: ell=4,5 are strict, ell=6 is equality, and ell>=7 violates.

Orientation scan found zero self-inverse primitive cyclic classes and zero cross-inverse pairs for `ell=4..10` after quotienting by rotation+inversion.
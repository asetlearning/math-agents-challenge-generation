# Filtered Oracle Period Profile

Generated epoch: `1785845930`

Oracle: `g3` at `gpgeo_g3`

**Scope:** finite oracle-filtered signal only, not a uniform theorem. Literal/free arcs are reduced to oracle shortlex normal forms; this catches both shrinkage and newly-created G-equalities.

## Selection

| ell | candidates | selected genuinely-new | rejected non-geodesic | rejected p^5 trivial | cyclic-boundary duplicates |
|---:|---:|---:|---:|---:|---:|
| 4 | 9 | 5 | 4 | 4 | 0 |
| 5 | 24 | 14 | 8 | 4 | 4 |

## Realized Piece Profile

| ell | selected | pairs | max realized NF piece | ratio max/(5ell) | threshold 5ell/6 | strict? | eps=5/6-max/ell | critical pairs | created G-eq witnesses | shrink witnesses | tail |
|---:|---:|---:|---:|---:|---:|:---:|---:|---:|---:|---:|---|
| 4 | 5 | 10 | 3 | 0.150000 | 3.333333 | yes | 0.083333 | 0 | 0 | 0 | `{'2': 8, '3': 2}` |
| 5 | 14 | 91 | 4 | 0.160000 | 4.166667 | yes | 0.033333 | 0 | 0 | 0 | `{'2': 19, '3': 42, '4': 30}` |

## Acid Test

| ell | near-identical ell-1 literal pairs | pass count | fail count |
|---:|---:|---:|---:|
| 4 | 12 | 12 | 0 |
| 5 | 66 | 66 | 0 |

## Duplicate Boundary Examples

Same-level cyclic-boundary duplicates are rejected when a cyclic rotation of `p^5` or `p^-5` has the same oracle normal form as a previously selected same-ell boundary.

- `ell=4`: none
- `ell=5`:
  - `AABBB` duplicate of `AAABB` (shared boundary NF count `4`)
  - `AAbbb` duplicate of `AAAbb` (shared boundary NF count `4`)
  - `ABABB` duplicate of `AABAB` (shared boundary NF count `2`)
  - `AbAbb` duplicate of `AAbAb` (shared boundary NF count `2`)

## Verdict

This dry run is a finite signal only. A clean finite profile would motivate a uniform separation theorem; it is not that theorem.
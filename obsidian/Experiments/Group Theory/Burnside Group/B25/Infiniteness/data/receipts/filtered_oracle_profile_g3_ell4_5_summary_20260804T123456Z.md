# Filtered Oracle Period Profile

Generated epoch: `1785846896`

Oracle: `g3` at `gpgeo_g3`

**Scope:** finite oracle-filtered signal only, not a uniform theorem. Literal/free arcs are reduced to oracle shortlex normal forms; this catches both shrinkage and newly-created G-equalities.

## Selection

Raw reject categories may overlap. The priority columns are disjoint and reconcile with the selected count.

| ell | candidates | selected | raw non-geodesic | raw p^5 trivial | raw bounded conjugacy duplicates | priority non-geodesic | priority p^5 trivial | priority conjugacy duplicate | conjugator bound |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4 | 9 | 5 | 4 | 4 | 0 | 4 | 0 | 0 | 3 |
| 5 | 24 | 14 | 8 | 4 | 4 | 8 | 0 | 2 | 4 |

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

## Bounded Conjugacy Duplicate Witnesses

Same-level duplicates are rejected only with explicit bounded oracle conjugacy witnesses `reduce(g * p^5 * g^-1 * target^-1) = IdWord`. The raw list includes overlapping duplicates among nontrivial candidates; the selected list is the disjoint selected-set reject list.

- `ell=4`: none
- `ell=5`:
  - `AABBB` conjugate to `AAABB^-` with `g=aa`
  - `AAbbb` conjugate to `AAAbb^-` with `g=BB`
  - `ABABB` conjugate to `AABAB^-` with `g=AB`
  - `AbAbb` conjugate to `AAbAb^-` with `g=Ab`

## Verdict

This dry run is a finite signal only. A clean finite profile would motivate a uniform separation theorem; it is not that theorem.
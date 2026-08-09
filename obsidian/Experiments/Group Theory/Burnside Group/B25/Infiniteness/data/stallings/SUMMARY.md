# Stallings-folding bounded certificates (Lead, 2026-07-31/08-01)

**Statement proved (exact, machine-checked):** for M = 6, 8, 10 (M=11 running), the word
E7 = [a,b,b,b,b,b,b] and all 20 GAP kernel candidates (W13-*, W14-*) are **NOT** elements of
H_M = ⟨ d⁵ : d reduced word over {a,b}, 1 ≤ |d| ≤ M ⟩ ≤ F₂.

Since {d⁵} is inverse-closed and every fifth power in F₂ is d⁵ for some reduced d (with
conjugated powers c e⁵ c⁻¹ = (c e c⁻¹)⁵ appearing as roots of length ≤ 2|c|+|e|), membership in
H_M is exactly: "expressible as a product (any number of factors) of fifth powers whose roots have
length ≤ M". So:

> **E7 is not a product of fifth powers with all roots of length ≤ 10** (any number of factors) —
> exact theorem, not a search-budget statement. Same for all 20 weight-13/14 candidates.

Method: Stallings folding on the wedge of loops {red-word d, |d| ≤ M, primitive, up to inversion};
membership = the target spells a closed loop at the basepoint of the folded core.

Receipts: fold.py (self-tested: 8 hand cases incl. conjugated-power boundary at M=3→5),
out_M10.txt (58,834 roots, 2,795,390 path edges, 21/21 MEMBER=False),
out_M11.txt (176,930 roots, 9,290,670 path edges, 21/21 MEMBER=False).

## Rust scaling — frontier pushed to M = 15 (Developer, 2026-08-01)

`rust/fold.rs` (std-only, no new deps) is a scaled port of `fold.py`: compact union-find
(`parent: u32`, `rank: u8`, `adj: [u32;4]` = 21 B/vertex). Folding is confluent, so the
folded core and every membership answer are fold-order-independent — the Rust folder is
**byte-identical** to the Python reference at the cross-validation points:
- `test_targets.txt` M=3,5,6 (incl. conjugated-power boundary T4 flipping at M=5);
- `real_targets.txt` M=6, M=8 vs live Python; M=10 vs out_M10.txt; M=11 vs out_M11.txt.

**All 21 targets (E7 + 20 W13/W14 candidates) are NOT members at every M = 6…15.** Receipts:
`rust/out_M<M>.txt` + `rust/time_M<M>.txt` (36 GB / 14-core box, single process, rustc 1.93.1).

| M  | roots      | path_edges     | folded_verts | time    | peak RSS |
|----|------------|----------------|--------------|---------|----------|
| 11 | 176,930    | 9,290,670      | 4,144,117    | 0.18 s  | 0.2 GB   |
| 12 | 530,822    | 30,524,190     | 13,850,405   | 0.74 s  | 0.6 GB   |
| 13 | 1,593,702  | 99,611,390     | 44,310,729   | 2.78 s  | 2.0 GB   |
| 14 | 4,781,250  | 322,739,750    | 145,586,847  | 12.4 s  | 6.4 GB   |
| 15 | 14,347,054 | 1,040,175,050  | 460,451,589  | 104.5 s | 11.8 GB* |

\* M=15 allocates ~22 GB; macOS compressor held resident at 11.8 GB (sys-time ≈ compression).
Growth ≈ 3.3× path-edges per +1 M. **M=15 is the ceiling on this box** — M=16 ≈ 3.4 B path
edges ≈ 72 GB > 36 GB. Higher M needs a batched build-fold-compact loop (not implemented).

> **Frontier: E7 is not a product of fifth powers with all roots of length ≤ 15** (any number
> of factors) — exact theorem, ∀ M ≤ 15. Same for all 20 W13/W14 candidates. See `rust/README.md`.

Interpretation discipline: H_M ↑ F⁵(F₂) as M→∞ but every M is bounded; this is an OBSTRUCTION
FRONTIER (evidence toward E7 ∉ F⁵, i.e. toward B(2,5) infinite), never a proof. Complementary to
the A5 expansion search (which bounds factor count/intermediate length instead of root length).

Convention receipt (gap/08_convention.out): E7 trivial in R(2,5) under BOTH [x,y] conventions;
[a,5b] nontrivial under both. Witness logic is convention-robust.

## Positive controls + cross-validation with A5 expansion search (T+~4h)

- 16/30 known-trivial calibration words (explicit fifth-power products) ARE members of H_11 —
  the fold detects genuine memberships (control_targets.txt run).
- The 3 false-STUCK known-trivial words are NOT in H_11, yet A5's expansion search proves them
  trivial with REPLAY-OK certificates. Consistency verified explicitly: their certificate roots
  reach length 145 ≫ 11 (e.g. 194-char word: 8 factors, max conjugated root 145). The two tools
  bound DIFFERENT axes (root length vs search radius/factors) and agree everywhere both apply.
  No contradiction; joint coverage is strictly stronger than either alone.

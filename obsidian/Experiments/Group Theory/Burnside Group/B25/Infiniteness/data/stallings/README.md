# Stallings-folding membership — Rust port (scaled)

Rust port of `../fold.py`. Decides exact membership of a word in

    H_M = ⟨ d⁵ : d reduced over {a,b}, 1 ≤ |d| ≤ M ⟩  ≤  F₂

via Stallings folding (wedge of `d⁵` loops → fold to the canonical core → target is a
member iff it spells a closed loop at the base). Same algorithm as the Python reference,
re-expressed with compact arrays + union-find so M can be pushed well past Python's ~11.

## Files
- `fold.rs` — single-file implementation, std-only (no added dependencies).
- `out_M<M>.txt`, `time_M<M>.txt` — literal outputs and `/usr/bin/time -l` receipts.

## Build / run
```
rustc -O -C opt-level=3 -C lto=fat -C codegen-units=1 fold.rs -o fold   # rustc 1.93.1
./fold <M> <targets_file>          # e.g. ./fold 15 ../real_targets.txt
```

## Implementation notes
- Labels `0=a 1=b 2=A 3=B`, inverse = `l ^ 2`.
- Roots: DFS over reduced words length 1..M, kept one per `{d, d⁻¹}` pair (`d ≤ d⁻¹`),
  proper powers skipped — identical enumeration to `fold.py::gen_reduced_words`.
- Graph: `parent: Vec<u32>` (union-find, path halving), `rank: Vec<u8>` (union by rank),
  `adj: Vec<[u32;4]>` (one out-edge slot per label, `NIL = u32::MAX`). **21 bytes/vertex.**
- Folding is confluent, so the folded core — and therefore every membership answer — is
  independent of fold order. This is what lets the Rust folder (clean worklist, union by
  rank) produce byte-identical results to the Python folder (worklist, union by size).
- Vertex ids are `u32` (cap 4.29e9). Arrays are pre-sized to the exact wedge vertex count
  `V0 = 1 + (path_edges − roots)` to avoid reallocation spikes.

## Cross-validation (MUST match Python — the correctness anchor)
Byte-identical to `fold.py` / the stored Python ground truth:
- `test_targets.txt` M=3,5,6 — all 8 hand cases, incl. the conjugated-power boundary
  `T4` flipping False→True at M=5 (the documented M=3→5 boundary).
- `real_targets.txt` M=6, M=8 — `diff` vs live Python: identical.
- `real_targets.txt` M=10 vs `../out_M10.txt`, M=11 vs `../out_M11.txt`: identical.

## Results (this box: 36 GB RAM, 14 cores, rustc 1.93.1; single process)
All 21 targets (E7 + 20 W13/W14 GAP-kernel candidates) are **NOT** members at every M.

| M  | roots      | path_edges     | folded_verts | time    | peak RSS |
|----|------------|----------------|--------------|---------|----------|
| 11 | 176,930    | 9,290,670      | 4,144,117    | 0.18 s  | 0.2 GB   |
| 12 | 530,822    | 30,524,190     | 13,850,405   | 0.74 s  | 0.6 GB   |
| 13 | 1,593,702  | 99,611,390     | 44,310,729   | 2.78 s  | 2.0 GB   |
| 14 | 4,781,250  | 322,739,750    | 145,586,847  | 12.4 s  | 6.4 GB   |
| 15 | 14,347,054 | 1,040,175,050  | 460,451,589  | 104.5 s | 11.8 GB* |

\* M=15 allocates ~22 GB (21 B × 1.04 B vertices); the macOS compressor held physical
resident at 11.8 GB, which is why M=15 wall-clock (104 s) exceeds the ~40 s the compute
alone would take (sys time ≈ 50 s is compression). Growth is ~3.3× path-edges per +1 M.

## Ceiling
M=16 would need ~3.4 B path edges ≈ 72 GB — exceeds this box's 36 GB. **M=15 is the
practical ceiling here** with the single-shot builder. Pushing further would require a
batched build-fold-compact loop (peak ≈ folded-core size rather than raw-wedge size);
not implemented — flag to Lead if a higher frontier is wanted.

Result unchanged across M=6…15: **E7 and all 20 W13/W14 candidates ∉ H_M** — i.e. none is
a product of fifth powers with all roots of length ≤ 15 (exact theorem at each M, an
obstruction frontier toward E7 ∉ F⁵, never a proof; see `../SUMMARY.md`).

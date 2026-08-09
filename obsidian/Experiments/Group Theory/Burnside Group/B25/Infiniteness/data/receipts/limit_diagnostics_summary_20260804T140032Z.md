# B(2,5) Limit Diagnostics Receipt

Generated UTC: `20260804T140032Z`

Scope: evidence-generation about the direct limit only. No proof of finiteness or infiniteness is claimed from these bounded diagnostics.

## Growth-Rate Trajectory

| L | source/status | states | transitions | lambda bracket | width |
|---:|---|---:|---:|---:|---:|
| 1 | sanity anchor (1 + sqrt(3)) | - | - | [2.73205080756888, 2.73205080756888] | 0 |
| 2 | verified automatic-structure FSA | 104 | 274 | [2.67416958057, 2.67416958057] | 2.57e-12 |
| 3 | verified automatic-structure FSA | 2,527 | 6,953 | [2.65121361947, 2.65121361947] | 2.18e-12 |
| 4 | FSA-level evidence only; g4 gpaxioms not certified | 7,971,915 | 21,641,441 | [2.64772186058, 2.64772186059] | 2.6e-12 |

Interpretation label: if the trajectory stays bounded well above 1, that is a limit-stays-infinite signal; if it trends toward 1, that is a collapse signal. This table is evidence, not a theorem.

## E7 Witness Trajectory

| L | NF length | status |
|---:|---:|---|
| 1 | 128 | proved model for G1; syllables=128 |
| 2 | 128 | verified automatic-structure oracle |
| 3 | 128 | verified automatic-structure oracle |
| 4 | 128 | diff2-sound preview only; g4 gpaxioms not certified |

## Fuel Gauge

| transition | ell | oracle | genuinely-new count | status |
|---|---:|---|---:|---|
| G3 -> G4 | 4 | G3 | 5 | certified input to Gate 2 |
| dry-run signal for length-5 periods | 5 | G3 | 14 | dry run over G3; not the G4-rung count |
| G4 -> G5 | 5 | G4 | pending | pending certified G4 oracle |

For rung L -> L+1, use the certified G_L oracle, enumerate primitive freely cyclically reduced periods of length L+1 up to rotation/inversion, retain periods whose p^5 is G_L-geodesic/nontrivial and not G_L-conjugate to existing relator powers, then run realized-piece profiling over the selected set. Absence of conjugacy from a bounded search must be labeled by its connector depth; positive duplicate rejections carry conjugator witnesses.

## Receipt Hashes

- `script_sha256`: `a1e10c064c24c805f92be58f22054da8ef697d50f52c87262eb5dd84e2dedc48`
- `first_json_sha256_before_hash_field`: `6f05b9817f648658f77253a4bbc84d487fe599727463294cc7c1aa73cddf0a71`
- `json_sha256_before_summary_refresh`: `415b090eca730ddda1b999cb1f33a9b8cc8ca7f29365ae737d5e1650aa4ef9a7`

Final receipt-file hashes are frozen in the sibling `SHA256SUMS_*` sidecar.

## Replay

```sh
python3 limit_diagnostics.py --groups g2,g3,g4 --tol-abs 1e-12 --tol-rel 1e-12 --max-iters 5000 --g4-tol-abs 1e-12 --g4-tol-rel 1e-12 --g4-max-iters 500 --progress-every 20
```

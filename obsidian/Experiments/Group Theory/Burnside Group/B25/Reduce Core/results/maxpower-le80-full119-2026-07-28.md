---
title: Max-power le80 full-119 cyclic-seam attack — results
domain: group-theory
project: b25
instance: B(2,5)
experiment_type: reduce-core
status: proven
author: maumayma
date: 2026-07-28
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/beat-beam, topic/cyclic-seam, topic/proof-search, project/b25, status/proven, results]
---

# Max-power le80 full-119 cyclic-seam attack — results

Canonical results note for the le80 full-word 119 attack (run `maxpower_v2_20260724`). This is the
**continuation of the beat-beam bank+seam campaign line** ([[beat-beam-campaign-2026-07-21]],
[[cyclic-seam-sweep-2026-07-22]]) — a Reduce-Core method, NOT PatternBoost: there is **no learned model**
in this run; the repo path `runs/b25/patternboost_loop_v1/` is only a legacy directory name. Synthesized
from Developer's run scratch (`Agents/maumayma/Developer/scratch/maxpower-le80-seam-results-2026-07-28.md`)
and the binding Validator batch verdict [[2026-07-28-maxpower-le80-batch-verdict]].

**Scope guard:** =e IDENTITY-certificate words (HWW pcps commutator relators, trivial in B₀ by
construction). "Reduction" = shortening an identity-proof. NOT a free-B(2,5) claim (Kourovka 11.48 OPEN).
See [[project_b25_benchmark_words_trivial]].

## Headline

**92 / 119 words improved over their stored beam-best; total +941 chars; all 92 GAP-verified sound by
Validator (`=_{B0}` original, `=e`, strictly `< stored_best`).** Ledger-worthy. ~2.7× the prior PROVEN
best (mega_le16: 351 / 77). The remaining 27 are at their stored minimum (seam plateau).

## Results table

| Run ID | Date | Parameters | Outcome | Wall-clock | Memory peak | Validated by | Notes |
|---|---|---|---|---|---|---|---|
| v-le80-seam | 2026-07-28 | cyclic-seam@72 on **le80** (9.39M rules, LHS≤80) applied to best candidate; min(stored, greedy, seam) | **92/119 improved, +941 chars** | see `run_le80_v2.log` (le80 ≈ 48 s load + reduce per invocation) | ~9.6 GB (le80 bank) | [[2026-07-28-maxpower-le80-batch-verdict]] — GAP 92/92 =B0 & =e | headline; certs dir below |
| baseline-mega-seam | 2026-07-22 | cyclic-seam@72 on **mega_le16** (5,578 rules) | 351 chars / 77 words | — | Validator 77-seam batch [[2026-07-22-cyclic-seam-sweep-batch-verdict]] | prior PROVEN best; smaller bank |
| ctrl-greedy-le80 | 2026-07-28 | `braid_reduce --no-beam` on le80, **no rotation** | **0** beats over stored | — | in-run column | isolates: bank-refresh WITHOUT rotation beats nothing over stored |
| ctrl-mega-seam-92 | 2026-07-29 | seam@72 on **mega_le16** (5,578 rules), same 92 words (bank swap, rotation protocol fixed) | **+941/92 — per-word IDENTICAL to le80 (0/92 mismatches); `bank_refresh_contribution = 0`** | ~fast (small bank) | — | own control `seam_control_mega_le16.py` | le80's 9.4M rules add ZERO; +941 = rotation protocol + 17-rule effective core (already in mega_le16) |

## Mechanism / lever decomposition (REQUIRED CORRECTION — Validator)

The certs all carry `lever="seam"`, but the run summary's "100% via seam" is **inaccurate** and is
corrected here per the verdict:

- **82 / 92 (Δ = 814)** are **seam-involved** (≥1 period-72 rotation in `seam_rotations`).
- **10 / 92 (Δ = 127)** beat with **ZERO rotations** (`seam_rotations = []`) — this is the **le80
  bank re-reducing the stale stored best** (a bank-upgrade / stale-best refresh), **not** the seam lever:
  `comm_12_2 (+24), comm_13_3 (+19), comm_12_3 (+17), comm_10_3 (+15), comm_5_4 (+15), comm_7_2 (+15),
  comm_9_3 (+13), comm_8_4 (+5), comm_8_2 (+3), comm_8_7 (+1)`.
- **Even the 82 conflate bank-upgrade + seam.** Δ is measured vs `stored_best` (old beam-bank output),
  so it folds in the le80-vs-old-bank improvement. The **clean** seam contribution is
  `norot_le80 → cyclic` per word (NOT `stored → new_min`); it is **not isolated** in this run. True
  seam-lever gain is **≤ 814 and likely materially less**. The stage-1 control arm (ctrl-mega-seam-92,
  `runs/b25/beatbeam_20260721/seam_control_mega_le16_20260728/`) attacks the complementary
  bank-attribution axis (mega_le16 ↔ le80 with rotation fixed).

This corrects narrative/metadata only — **it does not reduce the 92 count or the soundness.**

**Bank-attribution (stage-1 control, 2026-07-30, Validator-STAMPED):** swapping the reduction bank
mega_le16 ↔ le80 with the rotation protocol held fixed changes nothing — **all 92 `new_min` words are
byte-identical** between banks, so `bank_refresh_contribution = 0`. Both the 82 seam-involved and the 10
"bank-refresh" beats are fully reproduced by mega_le16. The effective firing core (~17 rules) lives in
mega_le16; le80's extra 9.4M rules are inert. **le80 is dropped operationally in favour of mega_le16.**

## Baselines

- **mega_le16 seam:** 351 chars / 77 words (prior PROVEN best).
- **Static-bank saturation:** **17 firing rules at every bank size** (le24 281k → le80 9.4M) — a bigger
  *decreasing* bank does not fire more; the le80 gain is DYNAMIC (the big bank catches more in the seam's
  rotated intermediates). See [[project_b25_maxpower_seed_falsified]], [[project_b25_mega_le16_effective_set]].
- **greedy-le80 (no rotation):** 0 beats over stored — bank-refresh alone (no seam) beats nothing.

## Provenance

- **Provenance triple:** git SHA `17b6068b395a35f89c0b05aa0f5048cd6961170c` · uv.lock sha256
  `978fe9e2d4809ac5cad3bf2814e01b6948076ce79512621d6a3c7b29994126fe` (verified, matches Developer batch-1)
  · braid_reduce build sha256 `fa08c856676a9e28c6b100ffaa6cfaf87c970e907cd2dd53642b70fd0cfd65bb`.
- **Runner:** `experiments/burnside/b25_patternboost/run_maxpower_v2.py` (cyclic_reduce module).
- **Bank:** `runs/b25/beatbeam_20260721/maxpower_coverage_20260724/extract_le80.rules` (9,394,214 rules,
  LHS≤80, a clean SUBSET of the 20.1M beam bank).
- **Certs (92):** `runs/b25/patternboost_loop_v1/maxpower_v2_20260724/cert_comm_*.json` (legacy dir name)
  — each carries `new_min_word, seam_rotations, reducer_config, sanity_checks, is_identity_best`.
- **Log / table:** `runs/b25/patternboost_loop_v1/maxpower_v2_20260724/{run_le80_v2.log, maxpower_v2_table.json}`.
- **Validator oracle:** own `EpimorphismPGroup(G,5,12)` build, order self-checked `5³⁴`; 92/92
  `is_identity(new_min)` and `equal(new_min, original)`.

## Version history

- **mega_le16 seam (2026-07-22):** 351 / 77, first PROVEN cyclic-seam batch (period-72).
- **le80 seam (2026-07-28):** swapped the reduction bank to le80 (9.4M); 92 / 119, +941 — the dynamic
  coverage thesis at scale. Attribution corrected by Validator (82 seam / 10 bank-upgrade).
- **stage-1 control + Validator stamp (2026-07-30):** mega_le16 reproduces +941/92 byte-identically
  (`bank_refresh_contribution = 0`). **Bigger bank does NOT scale the seam;** the 351→941 jump was
  protocol iteration + stale stored bests. **le80 dropped operationally for mega_le16** (Validator license).

## Main findings

1. **The seam is the only lever that beat stored via rotation** (greedy-le80 = 0). The reductions are
   irreducibly global; the gain is dynamic, not from a larger static bank (17-rule saturation).
2. **Bigger bank does NOT scale the seam** (corrected 2026-07-30; Lead sign-off unconditional after
   Validator STAMPED the control replication — 0/92 mismatches, byte-identical `new_min` words, verdict
   transfers verbatim, no GAP re-gate). The stage-1 control (`ctrl-mega-seam-92`) shows **mega_le16
   (5,578 rules) reproduces the full +941/92 per-word identically** (`bank_refresh_contribution = 0`).
   The **351/77 → 941/92 jump was protocol iteration** (more rotation periods, min-over-attacks,
   base=stored) **+ re-reducing stale stored bests — NOT the bank.** le80's 9.4M rules add nothing over
   mega_le16 — consistent with 17-rule saturation. **Operational consequence (Validator license): drop
   le80; run the loop on mega_le16** (same result, ~instant automaton vs 48 s / 9.6 GB).
3. **Marginal per word** (Δ ≈ 0.1–0.2% of length) — near a floor; iterating won't compound (bank
   saturated, seam at per-word plateau, words are =e so the geodesic is a hard floor).
4. **Attribution must be per-word** (82 seam-involved / 10 bank-upgrade); the clean seam size needs the
   `norot_le80 → cyclic` decomposition.

## Open questions

- Clean `norot_le80 → cyclic` per-word decomposition (true seam size) — not isolated here.
- Does dynamic-overlap rule generation ([[dynamic-overlap-rulegen-2026-07-28]], H3) beat +941/92, which
  a bigger length-decreasing bank cannot?

## Full per-word table (119 rows)

**Legend:** `orig` = original relator length · `prev best (stored)` = beam-best BEFORE this run · `mega_le16 seam` = 351/77 run best (iterated_cyclic.json; `n/a` where that run had no entry) · `new le80 best` = this run's new_min · `Δ vs stored` = stored − new_min · `lever` per Validator attribution (seam-involved = Δ>0 with ≥1 rotation; bank-refresh = Δ>0 with 0 rotations; no-change = Δ=0) · `rot` = rotation count from `seam_rotations`. Extracted by `experiments/burnside/b25/gen_le80_full_table.py` from `maxpower_v2_table.json` + `iterated_cyclic.json` (not hand-typed). Sorted by Δ desc. Totals: 82 seam-involved (Δ814), 10 bank-refresh (Δ127), 27 no-change; mega column filled 77/119.

| word       | orig  | prev best (stored) | mega_le16 seam | new le80 best | Δ vs stored | lever         | rot |
| ---------- | ----- | ------------------ | -------------- | ------------- | ----------- | ------------- | --- |
| comm_16_2  | 41886 | 22421              | 22379          | 22379         | +42         | seam-involved | 10  |
| comm_8_6   | 32200 | 20156              | n/a            | 20118         | +38         | seam-involved | 5   |
| comm_6_3   | 26962 | 16853              | 16817          | 16817         | +36         | seam-involved | 4   |
| comm_14_3  | 28058 | 22386              | 22352          | 22352         | +34         | seam-involved | 5   |
| comm_6_1   | 27204 | 21031              | 20997          | 20997         | +34         | seam-involved | 1   |
| comm_7_3   | 28750 | 17726              | n/a            | 17695         | +31         | seam-involved | 2   |
| comm_15_2  | 32720 | 22150              | 22120          | 22120         | +30         | seam-involved | 1   |
| comm_8_5   | 24974 | 21083              | 21053          | 21053         | +30         | seam-involved | 5   |
| comm_9_8   | 28614 | 20261              | 20231          | 20231         | +30         | seam-involved | 2   |
| comm_5_3   | 23520 | 20307              | 20278          | 20278         | +29         | seam-involved | 1   |
| comm_17_2  | 34770 | 20174              | 20146          | 20146         | +28         | seam-involved | 2   |
| comm_7_4   | 41228 | 20930              | n/a            | 20904         | +26         | seam-involved | 3   |
| comm_12_2  | 32250 | 26644              | n/a            | 26620         | +24         | bank-refresh  | 0   |
| comm_11_2  | 29578 | 16408              | 16386          | 16386         | +22         | seam-involved | 1   |
| comm_18_3  | 28224 | 18086              | n/a            | 18064         | +22         | seam-involved | 2   |
| comm_9_4   | 18574 | 13075              | 13053          | 13053         | +22         | seam-involved | 1   |
| comm_6_5   | 39410 | 23711              | n/a            | 23690         | +21         | seam-involved | 1   |
| comm_8_3   | 23420 | 17678              | 17657          | 17657         | +21         | seam-involved | 1   |
| comm_13_3  | 33328 | 27340              | n/a            | 27321         | +19         | bank-refresh  | 0   |
| comm_4_2   | 23298 | 16901              | 16883          | 16883         | +18         | seam-involved | 1   |
| comm_12_3  | 19560 | 15036              | n/a            | 15019         | +17         | bank-refresh  | 0   |
| comm_10_3  | 31546 | 24636              | n/a            | 24621         | +15         | bank-refresh  | 0   |
| comm_5_4   | 29390 | 15135              | n/a            | 15120         | +15         | bank-refresh  | 0   |
| comm_6_2   | 26852 | 17798              | 17783          | 17783         | +15         | seam-involved | 1   |
| comm_7_2   | 37070 | 23001              | n/a            | 22986         | +15         | bank-refresh  | 0   |
| comm_14_2  | 18856 | 16432              | 16418          | 16418         | +14         | seam-involved | 1   |
| comm_4_3   | 27796 | 13016              | 13002          | 13002         | +14         | seam-involved | 1   |
| comm_13_4  | 29508 | 19309              | 19296          | 19296         | +13         | seam-involved | 1   |
| comm_9_3   | 25798 | 20524              | n/a            | 20511         | +13         | bank-refresh  | 0   |
| comm_15_5  | 20490 | 20442              | 20430          | 20430         | +12         | seam-involved | 1   |
| comm_19_3  | 13682 | 11275              | 11263          | 11263         | +12         | seam-involved | 1   |
| comm_23_2  | 32286 | 11830              | 11818          | 11818         | +12         | seam-involved | 1   |
| comm_10_9  | 9660  | 9644               | 9634           | 9634          | +10         | seam-involved | 1   |
| comm_25_3  | 20192 | 13050              | 13041          | 13041         | +9          | seam-involved | 2   |
| comm_11_4  | 19266 | 13807              | 13799          | 13799         | +8          | seam-involved | 1   |
| comm_16_4  | 21970 | 15790              | 15782          | 15782         | +8          | seam-involved | 1   |
| comm_17_3  | 17538 | 8610               | 8602           | 8602          | +8          | seam-involved | 1   |
| comm_21_3  | 11294 | 11259              | 11251          | 11251         | +8          | seam-involved | 1   |
| comm_21_4  | 24384 | 10058              | 10050          | 10050         | +8          | seam-involved | 1   |
| comm_19_5  | 14826 | 14781              | 14774          | 14774         | +7          | seam-involved | 1   |
| comm_29_2  | 16758 | 9627               | 9620           | 9620          | +7          | seam-involved | 2   |
| comm_9_7   | 24052 | 17406              | 17399          | 17399         | +7          | seam-involved | 1   |
| comm_10_6  | 18834 | 11520              | 11514          | 11514         | +6          | seam-involved | 1   |
| comm_24_2  | 14302 | 7171               | 7165           | 7165          | +6          | seam-involved | 1   |
| comm_25_5  | 15488 | 10704              | 10698          | 10698         | +6          | seam-involved | 1   |
| comm_7_6   | 18228 | 16379              | 16373          | 16373         | +6          | seam-involved | 1   |
| comm_15_8  | 16970 | 9812               | 9807           | 9807          | +5          | seam-involved | 1   |
| comm_32_2  | 14270 | 14225              | 14220          | 14220         | +5          | seam-involved | 1   |
| comm_8_4   | 22674 | 16257              | n/a            | 16252         | +5          | bank-refresh  | 0   |
| comm_10_7  | 24442 | 13727              | 13723          | 13723         | +4          | seam-involved | 1   |
| comm_13_9  | 12104 | 12073              | 12069          | 12069         | +4          | seam-involved | 1   |
| comm_18_7  | 16984 | 9825               | 9821           | 9821          | +4          | seam-involved | 1   |
| comm_20_3  | 16074 | 8886               | 8882           | 8882          | +4          | seam-involved | 1   |
| comm_11_1  | 3756  | 3744               | 3741           | 3741          | +3          | seam-involved | 1   |
| comm_11_3  | 20840 | 11717              | 11714          | 11714         | +3          | seam-involved | 1   |
| comm_11_7  | 3792  | 3777               | 3774           | 3774          | +3          | seam-involved | 1   |
| comm_12_8  | 16834 | 13242              | 13239          | 13239         | +3          | seam-involved | 1   |
| comm_13_6  | 24246 | 6191               | 6188           | 6188          | +3          | seam-involved | 1   |
| comm_14_6  | 9666  | 9618               | 9615           | 9615          | +3          | seam-involved | 1   |
| comm_16_1  | 9828  | 9811               | 9808           | 9808          | +3          | seam-involved | 1   |
| comm_16_10 | 9908  | 9890               | 9887           | 9887          | +3          | seam-involved | 1   |
| comm_16_3  | 17050 | 8618               | 8615           | 8615          | +3          | seam-involved | 1   |
| comm_17_5  | 13424 | 13401              | 13398          | 13398         | +3          | seam-involved | 1   |
| comm_19_2  | 10712 | 10074              | 10071          | 10071         | +3          | seam-involved | 1   |
| comm_30_2  | 14278 | 14239              | 14236          | 14236         | +3          | seam-involved | 1   |
| comm_8_2   | 20796 | 12258              | n/a            | 12255         | +3          | bank-refresh  | 0   |
| comm_9_6   | 27334 | 11358              | 11355          | 11355         | +3          | seam-involved | 1   |
| comm_13_10 | 2500  | 2496               | 2494           | 2494          | +2          | seam-involved | 1   |
| comm_13_8  | 6144  | 6134               | 6132           | 6132          | +2          | seam-involved | 1   |
| comm_14_5  | 19196 | 10258              | 10256          | 10256         | +2          | seam-involved | 1   |
| comm_14_7  | 16830 | 13238              | 13236          | 13236         | +2          | seam-involved | 1   |
| comm_15_10 | 9872  | 9856               | 9854           | 9854          | +2          | seam-involved | 1   |
| comm_15_3  | 25444 | 14610              | 14608          | 14608         | +2          | seam-involved | 1   |
| comm_15_7  | 9802  | 9767               | 9765           | 9765          | +2          | seam-involved | 1   |
| comm_18_4  | 7452  | 7440               | 7438           | 7438          | +2          | seam-involved | 1   |
| comm_18_6  | 16954 | 14537              | 14535          | 14535         | +2          | seam-involved | 1   |
| comm_18_9  | 9876  | 9859               | 9857           | 9857          | +2          | seam-involved | 1   |
| comm_20_2  | 10716 | 10673              | 10671          | 10671         | +2          | seam-involved | 1   |
| comm_20_4  | 29156 | 7743               | 7741           | 7741          | +2          | seam-involved | 1   |
| comm_21_5  | 5370  | 5359               | 5357           | 5357          | +2          | seam-involved | 1   |
| comm_27_3  | 10710 | 10686              | 10684          | 10684         | +2          | seam-involved | 1   |
| comm_7_5   | 17932 | 9544               | 9542           | 9542          | +2          | seam-involved | 1   |
| comm_11_10 | 21620 | 7314               | 7313           | 7313          | +1          | seam-involved | 1   |
| comm_11_5  | 15766 | 15141              | 15140          | 15140         | +1          | seam-involved | 1   |
| comm_11_8  | 15616 | 8435               | 8434           | 8434          | +1          | seam-involved | 1   |
| comm_15_4  | 8820  | 7551               | 7550           | 7550          | +1          | seam-involved | 1   |
| comm_16_7  | 9840  | 9803               | 9802           | 9802          | +1          | seam-involved | 1   |
| comm_16_8  | 17012 | 9852               | 9851           | 9851          | +1          | seam-involved | 1   |
| comm_20_5  | 19680 | 5390               | 5389           | 5389          | +1          | seam-involved | 1   |
| comm_25_2  | 14236 | 7098               | 7097           | 7097          | +1          | seam-involved | 1   |
| comm_6_4   | 16408 | 11878              | 11877          | 11877         | +1          | seam-involved | 1   |
| comm_8_7   | 27390 | 13063              | n/a            | 13062         | +1          | bank-refresh  | 0   |
| comm_10_4  | 17156 | 15586              | n/a            | 15586         | +0          | no-change     | 0   |
| comm_10_5  | 14062 | 8991               | n/a            | 8991          | +0          | no-change     | 0   |
| comm_10_8  | 17922 | 13738              | n/a            | 13738         | +0          | no-change     | 0   |
| comm_12_10 | 4972  | 4964               | n/a            | 4964          | +0          | no-change     | 0   |
| comm_12_4  | 22302 | 10910              | n/a            | 10910         | +0          | no-change     | 0   |
| comm_12_5  | 14416 | 9623               | n/a            | 9623          | +0          | no-change     | 0   |
| comm_12_6  | 20414 | 13270              | n/a            | 13270         | +0          | no-change     | 0   |
| comm_12_7  | 8456  | 3698               | n/a            | 3698          | +0          | no-change     | 0   |
| comm_12_9  | 28652 | 7245               | n/a            | 7245          | +0          | no-change     | 0   |
| comm_13_5  | 19204 | 13802              | n/a            | 13802         | +0          | no-change     | 0   |
| comm_13_7  | 16836 | 16798              | n/a            | 16798         | +0          | no-change     | 0   |
| comm_14_4  | 12650 | 12623              | n/a            | 12623         | +0          | no-change     | 0   |
| comm_14_9  | 4966  | 4957               | n/a            | 4957          | +0          | no-change     | 0   |
| comm_16_5  | 5072  | 5054               | n/a            | 5054          | +0          | no-change     | 0   |
| comm_17_4  | 14592 | 14558              | n/a            | 14558         | +0          | no-change     | 0   |
| comm_17_6  | 16966 | 14548              | n/a            | 14548         | +0          | no-change     | 0   |
| comm_17_7  | 17004 | 9846               | n/a            | 9846          | +0          | no-change     | 0   |
| comm_17_9  | 9896  | 9880               | n/a            | 9880          | +0          | no-change     | 0   |
| comm_22_3  | 4162  | 4156               | n/a            | 4156          | +0          | no-change     | 0   |
| comm_22_4  | 10126 | 10110              | n/a            | 10110         | +0          | no-change     | 0   |
| comm_26_1  | 3576  | 3567               | n/a            | 3567          | +0          | no-change     | 0   |
| comm_26_2  | 8340  | 4761               | n/a            | 4761          | +0          | no-change     | 0   |
| comm_26_3  | 8340  | 8323               | n/a            | 8323          | +0          | no-change     | 0   |
| comm_26_4  | 20248 | 5947               | n/a            | 5947          | +0          | no-change     | 0   |
| comm_27_2  | 15468 | 10682              | n/a            | 10682         | +0          | no-change     | 0   |
| comm_27_4  | 15480 | 10690              | n/a            | 10690         | +0          | no-change     | 0   |
| comm_9_5   | 18818 | 11678              | n/a            | 11678         | +0          | no-change     | 0   |

## Related material

- [[Reduce Core/_type|Reduce Core experiment type]] — parent methodology family
- [[beat-beam-campaign-2026-07-21]] — the beat-beam bank+seam campaign this continues
- [[cyclic-seam-sweep-2026-07-22]] — prior mega_le16 seam results (351/77)
- [[2026-07-28-maxpower-le80-batch-verdict]] — binding Validator verdict (92/92 sound, attribution fix)
- [[project_b25_beatbeam_cyclic_seam]] — the cyclic-seam mechanism
- [[project_b25_maxpower_seed_falsified]] — static-bank saturation (17 rules)
- [[dynamic-overlap-rulegen-2026-07-28]] — the H3 follow-up this result motivates

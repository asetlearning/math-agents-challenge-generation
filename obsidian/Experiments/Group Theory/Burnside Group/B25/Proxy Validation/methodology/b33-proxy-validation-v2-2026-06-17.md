---
title: B(3,3) Proxy Validation Study v2 — PRE-REGISTRATION
date: 2026-06-17
domain: group-theory
project: b25
experiment_type: proxy-validation
instance: B(3,3)
author: maumayma
status: pending-approval
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/patternboost, project/b25, status/pending, experiment]
---

# B(3,3) Proxy Validation Study v2 — Pre-Registration

**Status**: PENDING — awaiting (a) Validator verdict on Proxy D (Lead already routed), (b) Lead/Maria re-approval after amendments, (c) Maria's green light. DO NOT RUN until all three clear.

**Amendment log**:
- 2026-06-17: Filed by B25 Experimenter
- 2026-06-17: NEEDS WORK verdict from Lead — three findings:
  - Finding 1 (Blocker — Proxy D Validator gate): CLEARED by Validator 2026-06-17. §4 Proxy D rewritten with D-FIX-1 (assertion guard: verify pcgs[4..6] ∈ γ₂\γ₃, pcgs[7] ∈ γ₃ before any computation) and D-FIX-2 (basis choice locked to pcgs basis f4,f5,f6; domain note for g∈G\γ₂). §3 updated to include assertion guard step. §11 Proxy-D gate row updated from PENDING → CLEARED. APPLIED.
  - Finding 2 (Blocker — Proxy A KB confluence): §4 amended — "60s cap" removed; requires verified `#confluent=true`; sane bound 30min/5M; stop-and-report if not converged; kill+pgrep required. APPLIED.
  - Finding 3 (Required — γ₃ split in H2): §7 H2 amended — pre-registers γ₃ identification, dual Spearman reporting (all-80 vs γ₂\γ₃ only), H2 decision basis = γ₂\γ₃. §6.4 updated. APPLIED.

**Lab change from v1**: B(5,3) → B(3,3). Reason: |B(5,3)| = 3²⁵ ≈ 847B (Cayley-BFS infeasible). |B(3,3)| = 3⁷ = 2187 (BFS trivially feasible; confirmed in spike 2026-06-17).

**Supersedes**: [[methodology/b53-proxy-validation-study-2026-06-17]] (v1, INCONCLUSIVE — non-confluent KB, binary-only GT, commutator-subgroup blind spot unmeasured)  
**Also tombstones**: [[methodology/b53-proxy-validation-v2-draft-2026-06-17]] (wrong B(5,3) order assumption)

---

## §1 Motivation

PatternBoost for B(2,5) uses a SCORE proxy for "distance to identity" in the local search loop. Current proxy (Option B: braid+power reduction ratio) scores 0.000 on ~43% of B(2,5) words — products-of-conjugates like `(aba)^5` which lie in the **commutator subgroup** [G,G] (abelianization=0). Abelianization distance also scores 0 on [G,G] words (structural: G/[G,G] is the abelianization, elements of [G,G] project to 0 by definition).

**The real open question**: does the **next lower-central-series layer** (γ₂/γ₃, basic-commutator-weight invariants) give a gradient on [G,G] words? If yes, this is a structurally general proxy candidate transferable to B(2,5).

B(3,3) is the lab: small enough for exact Cayley-BFS ground truth, large enough to have a non-trivial [G,G] with real distance variation (confirmed: 80 non-identity [G,G] elements at d=4..10 in spike).

---

## §2 Lab: B(3,3)

| Property | Value |
|---|---|
| Generators | a, b, c (rank 3) |
| Exponent | 3 |
| Order | 2⁷ = 2187 ✓ (verified by spike 2026-06-17) |
| Nilpotency class | 3 (Hall 1933) |
| Lower central series | γ₁=G (2187), γ₂=[G,G] (81), γ₃ (≤81), γ₄={1} |
| Word problem | Decidable (Todd-Coxeter + GAP; Validator #math-verdict/sound 2026-06-17) |

**Ground truth method**: Cayley-BFS geodesic distance.

---

## §3 Ground Truth — LOCKED

**Definition**: `d(g, 1)` = length of shortest word over `{a, b, c, A, B, C}` (generators and inverses) equal to `g` in B(3,3).

**Locked generating set**: `{a, b, c, a⁻¹, b⁻¹, c⁻¹}` — exactly the same 6-letter alphabet as the proxies. This ensures GT and proxies share one metric (Lead constraint §1).

**Procedure**:
1. Build B(3,3) as FpGroup in GAP: relations = (w)³=1 for all words w of length ≤ 3 over {a,a⁻¹,b,b⁻¹,c,c⁻¹}. (258 relators.)
2. Obtain PcGroup iso: `H = Image(IsomorphismPcGroup(G))`.
3. **Execute D-FIX-1 assertion guard** (see §4 Proxy D): verify LCS-adapted pcgs structure before any proxy-D computation. If assertions fail → STOP.
4. BFS from identity in H with 6 moves. Record `dist_table: H_element → int`.
5. For any corpus word w: evaluate via `H_element(w)`, look up `dist_table[H_element(w)]`.

**GAP provenance** (to be recorded at run time):
- GAP version: 4.15.1 (current)
- BFS script hash: [to be filled at run time]
- Distance-table artifact hash: [to be filled at run time]

**Stop condition**: if any relator fails to map to identity (dist=0), halt and route to Lead.

---

## §4 Proxy Candidates

Three proxies evaluated on B(3,3) corpus words:

**Proxy A — reduction_ratio** (existing):
- `(L - L') / L` where L' = length after one greedy leftmost Aho-Corasick scan using a B(3,3) KB rule bank.
- **KB rule bank requirement (amended per Lead finding 2)**: run B(3,3) shortlex kbprog to **verified `#confluent=true`**. A partial non-confluent bank makes reduction_ratio ill-defined (v1 failure). B(3,3) of order 2187 MUST produce a confluent system; do not stop early.
  - If kbprog does not reach `#confluent=true` within a sane bound (suggest: 30 min, fewer than 5M rules), STOP and route to Lead. Do NOT use a partial bank as a fallback.
  - Record: rule count, `#confluent` status, runtime.
  - Process hygiene: kill kbprog process when done; paste clean `pgrep -al kbprog` in run log.
- Expected: blind on [G,G] (commutators don't reduce). Spike asserted this; **v2 must measure it empirically** — report proxy A values on all 80 stratum-III elements.

**Proxy B — abelianization_distance** (existing):
- L1 norm of balanced-mod-3 generator exponent vector in {a,b,c}.
- `abel_dist(w) = sum |e_x - round(e_x / 3) * 3|` for x ∈ {a,b,c}
- Structurally zero on ALL [G,G] elements (abelianization = 0 mod 3 by definition). Not a measurement — a theorem. Included as baseline.

**Proxy D — LCS-weight-2 distance** (new):

**Status**: CLEARED by Validator 2026-06-17. Two required additions below (D-FIX-1, D-FIX-2) are now part of the specification.

**D-FIX-1 — Assertion guard (Validator Q2)**: GAP's `IsomorphismPcGroup` on B(3,3) happens to return an LCS-adapted pcgs (weight-1 = f1,f2,f3; weight-2 = f4,f5,f6; weight-3 = f7) due to the p-central series coinciding with the LCS here. This is undocumented behavior, not guaranteed in general. The following one-time assertion guard MUST be executed during the GT/proxy build (see §3) before any proxy-D computation:

```gap
lcs := LowerCentralSeries(H);
pcgs := Pcgs(H);
Assert(0, ForAll([4,5,6], i -> pcgs[i] in lcs[2] and not (pcgs[i] in lcs[3])));
Assert(0, pcgs[7] in lcs[3]);
```

If any assertion fails: STOP immediately, route to Lead. Do not compute proxy D on this group.

**D-FIX-2 — Basis choice and domain note (Validator Q1/Q2(b))**:

- **Basis choice (LOCKED)**: proxy D uses the **pcgs basis** (f4,f5,f6 exponents from `ExponentsOfPcElement(pcgs, g){[4,5,6]}`). This differs from the commutator basis `{[b,a],[c,a],[c,b]}`; the transform is triangular (Validator confirmed: `[b,a]→(1,0,0)`, `[c,a]→(1,1,0)`, `[c,b]→(1,2,1)` in pcgs coordinates). Both bases span γ₂/γ₃ and agree on D=0 ↔ g∈γ₃; the specific gradient VALUES differ. Pre-registering pcgs basis. Do NOT switch to commutator basis mid-run.

- **Domain note (Validator Q1)**: for g ∈ G\γ₂, `lcs2_dist(g)` is well-defined (a function of g) but does NOT measure "distance from γ₃" — that interpretation holds only inside γ₂. The function is a coarser invariant outside γ₂.

**Computation**: `lcs2_dist(g) = sum |balanced_mod3(e_i)| for i in {4,5,6}` where `balanced_mod3(e) = min(e mod 3, 3 - (e mod 3))` (values in {0,1}).

**Interpretation by coset**:
- G\[G,G] (γ₁\γ₂): lcs2_dist may be non-zero, but interpretation is coarser than "distance from identity in γ₂"
- [G,G]\γ₃ (γ₂\γ₃): abelianization = 0, lcs2_dist ≠ 0. **Target signal.**
- γ₃\{1}: abelianization = 0, lcs2_dist = 0. **Blind spot** — see §7 H2 γ₃ split.
- identity: lcs2_dist = 0.

Requires LCS-adapted PcGroup (GAP for B(3,3); B(2,5) transfer is the research question).

**Proxy E — combined LCS** (new):
- `lcs_dist(w) = abelianization_distance(w) + lcs2_dist(w)` (equal weight, fixed).
- Weights α=β=1 (additive; not 0.5+0.5 since scales differ). Locked pre-registration, NOT tunable.
- Expected to recover Proxy B on G\[G,G] and add signal on [G,G]\γ₃.

---

## §5 Corpus Design — STRATIFIED (Lead constraint §2 and §3)

| Stratum | Description | Method | Target count |
|---|---|---|---|
| I: Identity | B(3,3) relators (d=0) | From `b33_relators.txt` (to be generated; known relators from the 258-relator presentation) | ~50 |
| II: Random non-identity | Random freely-reduced words, verified non-identity via BFS table | Random seed=20260617, max_len=30, filter d>0 | 500 |
| III: [G,G] non-identity | Commutator-subgroup words (abelianization=0, d>0), spanning multiple distances | Systematic enumeration: all [b,a], [c,a], [c,b] and their products/powers; verify in BFS table | **all 80 non-identity [G,G] elements** (full census from spike) |

**Stratum III design**: Since |[G,G]\{1}| = 80 (complete finite set), include ALL of them — no sampling. Distances confirmed: d=4 (6 elements), d=6 (64 elements), d=7 (8 elements), d=10 (2 elements). This is the full [G,G] blind-class census.

**Stratum III must span a distance range** (Lead constraint §3): confirmed from spike (d ranges 4..10). Report achieved distance distribution for stratum III explicitly.

**Corpus size**: ~630 words total. Seed locked: 20260617.

---

## §6 Analysis Plan

### §6.1 Per-stratum reporting (Lead constraint §2)

Report Pearson r and Spearman ρ WITHIN each stratum separately:

| Stratum | Metric | Notes |
|---|---|---|
| Full corpus | Pearson r, Spearman ρ (all proxies vs d) | Summary only |
| Stratum II only (random non-identity) | Pearson r, Spearman ρ | **Primary gradient signal** |
| Stratum III only ([G,G] non-identity) | Pearson r, Spearman ρ | **Blind-class signal** — use Spearman (80 points, 4 distance values, ordinal) |

**Transfer decision rides on stratum-II gradient AND stratum-III finding** — not pooled r.

### §6.2 y>0 slice (non-identity words only, strata II+III)
- Same statistics as §6.1 on combined non-identity subset
- Blind-spot fraction for each proxy: fraction of non-identity words with proxy=0

### §6.3 Steiger's Z
- Compare r(combined, y) vs r(reduction_ratio, y) on y>0 slice — as pre-registered in v1, now with continuous y.

### §6.4 Stratum III specific tests (Lead constraint §4 reframed)
- Measure reduction_ratio empirically on stratum-III words (not assumed; Lead caveat)
- Confirm: proxy A ≈ 0 AND proxy B = 0 on [G,G] (empirical measurement, not assumed)
- Key question: does proxy D (lcs2_dist) show non-zero values on stratum-III words? Does it correlate with d within stratum III?
- Report: does a gradient EXIST on [G,G] that the LCS proxy can capture?
- **γ₃ split** (per §7 H2 amendment): identify γ₃ elements in stratum III (D=0 by construction); report d-distribution of γ₃ elements; report Spearman ρ(D,d) including and excluding γ₃ separately. Decision-relevant number is γ₂\γ₃ only.

---

## §7 Hypotheses

**H1**: LCS combined proxy E has larger gradient correlation than reduction_ratio on y>0 slice.
- Threshold: delta_r(E vs A) > 0.05 AND r(E, y>0) ≥ 0.60 AND Steiger's Z p < 0.05.
- "y>0 slice" = strata II+III combined.

**H2**: LCS-weight-2 proxy D has non-trivial correlation with geodesic distance within stratum III ([G,G]) — specifically on **γ₂\γ₃** (excluding γ₃ elements where D=0 by construction).

**γ₃ pre-registration (amended per Lead finding 3 + Validator confirmation)**:
- Proxy D = 0 on γ₃ elements by construction (they project to zero in γ₂/γ₃). These elements have D=0 regardless of their geodesic distance.
- **Validator confirms**: γ₃ = {1, c7, c7²} — exactly **2 non-identity γ₃ elements** (in pcgs notation, c7 = the generator at position 7). These are almost certainly the d=10 stratum-III pair (farthest [G,G] elements from spike). Including them in Spearman would bias D-vs-d DOWNWARD at the tail → false negative on H2.
- **Identification method**: use `g in lcs[3]` in GAP (not abelianization check — that's γ₂, not γ₃).
- **Before running**, verify: confirm the 2 non-identity γ₃ elements have d=10 via BFS table. If not, document actual distances and report explicitly.
- **Report Spearman ρ(D,d) TWICE on stratum III**:
  1. All 80 non-identity [G,G] elements (including the 2 γ₃ elements)
  2. γ₂\γ₃ only (78 elements, excluding the 2 γ₃ elements identified via `g in lcs[3]`)
- **H2 decision basis**: #2 (γ₂\γ₃ only, expected n=78). Threshold: Spearman ρ(D, d) on γ₂\γ₃ > 0.40.
- **Power note**: 78 γ₂\γ₃ elements for the decision basis. 4 distance values (d=4,6,7,10) but 64/78 at d=6 (within-shell discrimination); Spearman preferred. Treat as exploratory/descriptive.

**H3 (deliverable, not hypothesis)** (Lead constraint §4):
- Report: is there REAL DISTANCE VARIATION across [G,G]\{1}? (Yes — spike confirms d=4..10.)
- Report: is reduction_ratio empirically ≈0 on stratum III? (Measure, don't assume.)
- This establishes the problem is well-posed (gradient exists, current proxies miss it).
- H3 is NOT "both proxies are blind" as a finding — abelianization=0 on [G,G] is a theorem, not a measurement. The measurement is whether reduction_ratio is ALSO blind, and whether lcs2_dist captures what abelianization misses.

---

## §8 Transfer Rule — LOCKED pre-results (Lead constraint §5)

**H1 + H2 supported**: Transfer COMBINED LCS PROXY (E) to B(2,5) as experimental candidate. Foreground: E is still blind on γ₃ elements; [G,G] coverage is PARTIAL, not complete. File separate task for γ₃ proxy if needed.

**H2 only**: Transfer LCS-weight-2 (D) alone to B(2,5) as [G,G]-specific experimental candidate. Confirm Proxy B still handles G\[G,G] words.

**H1 only** (E better than A, but D doesn't help [G,G]): H3 analysis determines if [G,G] is hopeless with LCS or if a different invariant is needed. Keep Option B; file new design.

**Neither**: Keep Option B. The [G,G] problem requires a fundamentally different proxy family (not abelianization-based, not LCS-based). Flag to Lead.

**CRITICAL FOREGROUND IN TRANSFER REPORT** (Lead constraint §5): Combined proxy E does NOT solve the PatternBoost core problem on B(2,5). In B(2,5), the loop hits [G,G] words and any proxy combining abelianization + weight-2 may still be zero on deeper subgroup elements. The transfer from B(3,3) is structural-generality evidence (same algebraic family), not proof. This must be stated explicitly in the report.

---

## §9 Anti-pattern checklist

- [ ] GT independent of proxy computation? **YES** — Cayley-BFS uses exact group multiplication (not KB rules). Proxy A uses a KB rule bank (separate from BFS; no shared mechanism). Proxy D uses LCS-adapted PcGroup structure (Validator CLEARED 2026-06-17; assertion guard required). No shared mechanism for proxies B, D, E.
- [ ] Stratum III [G,G] words verified non-identity via BFS table (not just abelianization=0)? **YES** — abelianization=0 is necessary but not sufficient; BFS lookup required.
- [ ] Stratum III spans distance range? **YES** — spike confirmed d=4..10 across the 80 elements.
- [ ] No tuning: proxy weights fixed pre-registration (Proxy E weights 1+1, not tunable)? **YES**.
- [ ] Transfer rule locked before results? **YES** — this is the pre-registration.
- [ ] No mid-run GT substitution (Lead constraint §6)? Locked: Cayley-BFS only. If BFS fails for any word → STOP, route to Lead.

---

## §10 Known Limitations

1. **Stratum III limited power** (Lead spike caveat): 80 non-identity [G,G] elements, only 4 distinct distance values (d=4,6,7,10). 64/80 sit at d=6. Limited power for H2; treat Spearman ρ on stratum III as exploratory/descriptive. The lcs2_dist values within d=6 shell determine whether there's within-shell discrimination.
2. **Proxy A shared mechanism**: reduction_ratio uses a B(3,3) KB rule bank; the KB system is (theoretically) sound and the BFS GT doesn't share it, but the rule bank quality affects proxy A. Report KB rule count and confluent-status explicitly.
3. **Transfer gap**: B(3,3) → B(2,5) differs in rank (3→2) and exponent (3→5). The lcs2_dist proxy for B(2,5) requires computing weight-2 basic-commutator projections without solving the word problem — this is a separate design problem. Lab study gives structural-generality evidence; implementation in B(2,5) is a separate Developer task if H2 is supported.
4. **γ₃ elements remain blind**: elements of γ₃ (deepest LCS layer before trivial) have lcs2_dist=0. If these exist and are non-identity, they're still in a blind spot. In B(3,3) this is checkable.

---

## §11 Pending gates before running

| Gate | Status |
|---|---|
| Feasibility: GAP works, BFS tractable | CLEARED (spike 2026-06-17) |
| [G,G] blind class exists in B(3,3) | CLEARED (spike 2026-06-17) |
| Validator: BFS distance is correct GT | SOUND (2026-06-17, #math-verdict/sound) |
| Validator: [a,b] is non-identity, order 3 | SOUND (2026-06-17, #math-verdict/sound) |
| Validator: Proxy D (LCS-weight-2) well-defined + LCS-adapted pcgs procedure | CLEARED (2026-06-17, #math-verdict/sound). D-FIX-1 assertion guard + D-FIX-2 basis choice applied to §3/§4. γ₃ = {1,c7,c7²} confirmed. |
| Lead/Maria pre-reg approval | **PENDING — all Validator amendments applied; awaiting Lead re-approval + Maria green light** |

**Do not run until Lead/Maria approves this pre-registration.**

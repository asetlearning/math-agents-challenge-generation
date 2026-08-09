---
title: CC6-TR rank-3/5 path enumeration — pre-registration
domain: group-theory
project: b25
instance: B(2,5)
status: pending
author: maumayma
date: 2026-08-05
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, project/b25, status/pending, experiment]
---

# CC6-TR rank-3/5 path enumeration — pre-registration

**PRE-REGISTERED, NOT RUN.** Lead placed a HOLD on 2026-08-05 pending Validator's
input-scope two-pass ruling. Nothing in this note has been executed. The domain
section below is deliberately left with a PENDING branch; it is filled in, and
only then run, after the ruling lands.

## Authority and contract

- **Contract:** [[ell6-theory-barrier-analysis-2026-08-05]] §4.9 (authorized
  rank-3/5 path-enumeration contract and receipt schema).
- **Conventions:** §4.3 (reversal-invariant normalization; fixed shortlex
  `[a,A,b,B]`; the free-group argument for well-definedness of `epsilon`),
  §4.4 (rank-compatible carrier states; carrier basepoint `beta`; the matching
  rule with continuation sign condition `epsilon_1 = -epsilon_2`).
- **Authorization scope:** Validator's CC6-TR ruling, as restated verbatim below.
- **Assignment:** Lead brief 2026-08-05 (Delta quota-constrained and reserved
  for Stage 2).

## Hypothesis

Falsifiable, and deliberately weak — this is a finite-table enumeration, not a
theorem attempt:

> Every rank-3/5 **path** component of the constructed continuation graph admits
> exactly one of the two §4.9 dichotomy outputs, and the constructed graph
> satisfies the structural invariants the contract requires — reversal
> involution (`epsilon -> -epsilon`, `beta -> beta`), edge symmetry, maximum
> degree two, and exact reconciliation of every eligible occurrence exactly once.

Falsified if any component admits neither output, or if any structural check
fails, or if the totals fail to reconcile.

## Scope readback (verbatim, confirmed CORRECT by Lead 2026-08-05)

Rank-3/5 **path** components only. Cycles → `Z(D)`, no classification. Branch
tokens → `B_census` with full candidate lists, no move, no charge. Carrier
changes recorded, not analyzed. Rank-1 rejected at input. Per-component output
is exactly one of class 1 (move template with ambient-boundary condition, rank-6
area non-increase, strict measure decrease) or class 2 (retained token, no
charge). Fewer than two surviving corners → `F_RC2`; **I do not declare RC2**.
**No positivity claim, no G_5 no-hit result, no curvature inequality, no
connected-shell conclusion, nothing about unauthorized modules.** Reversal
involution (`epsilon -> -epsilon`, `beta -> beta`), edge symmetry, degree <= 2,
and exhaustive reconciliation of every eligible occurrence exactly once all get
explicit checks. Any lemma drawn from the table states which hypothesis fails in
the exponent-4 and exponent-6 controls; the table is evidence, not a theorem.

## Input — the finding that forced the HOLD

**The §4.9 input table does not exist as a persisted artifact.** Established by
search on 2026-08-05:

- `ell6_witnesses_stage1_corrected_20260805T080305Z.json`
  (sha256 `4ee498ef2e4e77a027a2fd95859f75d0fdcaa9f55ffc9311dff256b12efa0bc7`),
  named in Validator's `tools_used`, is Delta's ell=6 **conjugacy-witness**
  receipt: 58 periods, 1653 pairs, 26 survivors. It carries **no rank, arc,
  carrier, phase, or piece fields**.
- `gate2_receipts/dehn_arc_dfa_*.json` carry arcs and pieces but are Aug-2,
  g3-era, and have **no rank field**.
- No other file in vault or repo contains the 308-piece table or a 272-record
  rank-3/5 subset.

Validator's other `tools_used` entry is "exhaustive enumeration L=5,6" — the
table was computed inside their verification and only the **counts** were
published. So the table must be **regenerated**, not consumed. Regenerate-and-gate
was endorsed by Lead, Validator, and Math-expert.

### Two-pass domain rule — PENDING Validator

Math-expert's routed pre-ruling (awaiting Validator):

- **Pass 1 — normalization regression gate ONLY.** Reproduce the all-58
  histogram. This is a correctness check on the normalization code, **not** the
  enumeration domain.
- **Pass 2 — the actual enumeration**, over occurrence paths on the **frozen 26
  survivors**, with all target totals as **OUTPUTS**. In particular **272 is
  never assumed** — it is an all-58 figure and does not transfer to the
  26-survivor relative presentation.

Pass 1 gate, from Validator's published histogram:

```
(rank,m):  (1,1):24   (1,3):8   (1,5):4   (3,1):48   (5,1):224     total 308
rank-1 = 24 + 8 + 4 = 36   (rejected at input, per 4.6)
rank-3/5 = 48 + 224 = 272  (an ALL-58 figure; not a pass-2 target)
```

**If pass 1 does not reproduce this histogram exactly, STOP and route to
Validator.** Do not proceed on a self-invented table. (Same discipline that
gated the `g5` presentation: independent regeneration, accept only on exact
agreement.)

Structural fact used as a secondary check: `|s|=5` odd ⟹ `|c|` odd ⟹
`rank ∈ {1,3,5}` only, never 2 or 4.

## Method

1. **Rebuild pieces.** Cross-class length-5 windows on the symmetrized rank-6
   relators (58 primitive length-6 periods → `w^5`, all rotations and inverses).
2. **Normalize (§4.3).** `s = t c t^-1`, `c = r^m`, `rho = min(r, r^-1)` under
   shortlex `[a,A,b,B]`, `r = rho^epsilon`. Record `Norm(s) = (t,rho,m,rank)`.
   Check `Norm(s^-1) = Norm(s)` and `Rev` sends `(epsilon,beta) -> (-epsilon,beta)`.
3. **Expand to occurrences (§4.4).** Serialize
   `(arc-id, t, rho, m, rank, epsilon, beta, phase, cell-type, side, orientation, defects)`.
   `beta` modulo `rank` against the stored `g5` carrier representative; `phase`
   modulo 6. **The occurrence total is an output**, never assumed equal to the
   piece count.
4. **Candidate lists and edges (§4.9).** Compatible iff `Norm` agrees,
   `beta_1 = beta_2`, `epsilon_1 = -epsilon_2`, and phase/side/traversal/all four
   defect letters satisfy the local gluing rule. Edge only on **mutual unique**
   choice. No-choice end → terminal. Non-unique end → one branch token with the
   complete list, no edge.
5. **Classify path components** per the §4.9 dichotomy. Cycles, branches,
   carrier changes → stop buckets only.

## Termination criteria

Enumeration is finite and exhaustive by construction: it terminates when every
eligible occurrence is reconciled exactly once. Report before continuing if the
occurrence count materially exceeds expectation (a few thousand).

## Baselines / controls

- **Pass 1 histogram** against Validator's published counts (the primary gate).
- **Exponent-4 and exponent-6 controls** — required by §4.9 for any lemma drawn
  from the table: state which hypothesis fails in each.
- **Reversal involution applied twice** returns the identity on every state.

## Anti-pattern check

- *Am I tuning on the set I score on?* No — the pass-1 gate is a fixed,
  externally published histogram computed by Validator before this work existed.
- *Am I enumerating into unauthorized modules?* No — rank-1 rejected at input;
  cycles/branches/carrier changes are recorded as stop records only.
- *Am I assuming a target total?* No — 272 is explicitly an all-58 figure and is
  not a pass-2 target; every total is an output.
- *Cherry-picking?* Every eligible occurrence is reconciled exactly once and the
  totals must balance; misses are reported with hits.

## Resource estimate

Pure Python, single-threaded, **seconds to a couple of minutes**, no additional
CPU slot. Runs alongside the g5 `kbprog` and `gpgenmult` without contention.

## Artifact locations

- **Repo lane (Lead-APPROVED 2026-08-05):** `infinite_b25/avenues/cc6_tr/` —
  consistent with `gen_ladder_pres.py` and the rest of the ell6 avenue tree.
- Tables and checks: `B25/Infiniteness/data/` and `results/`.
- Output capture: [[Agents/Experimenter-B25/output/cc6-tr-rank35-2026-08-05]].

Hashes pinned in every receipt: gated `g5`
`b02941956761e1cf95a46ddc27e5433d8648a72722ca4d142ffaae6e14b6523f`; frozen rule
anchor `f3554eded618f8da340a0a87a74d50afd8420989440044b11aa422410e77a6e6`;
Delta's Stage-1 JSON `4ee498ef2e4e77a027a2fd95859f75d0fdcaa9f55ffc9311dff256b12efa0bc7`;
plus this run's own code and data hashes.

## Ruling resolution and results (2026-08-05, post-GO)

**Incidence branch = (A), confirmed from the ruling text**, §4.9 corrected step 2:
"Regenerate pieces using only the frozen 26 survivor classes." Not inferred from
the numbers — read from the authority — and then independently corroborated by
the pass-2 gate hitting 88/72 exactly under (A).

**Both calibration gates PASS exactly, first run:**

| pass | domain | total | histogram | verdict |
|---|---|---|---|---|
| 1 (regression gate only) | all 58 classes | **308** ✓ | `(1,1):24 (1,3):8 (1,5):4 (3,1):48 (5,1):224` ✓ | PASS |
| 2 (target) | frozen 26 survivors | **88** ✓ | `(1,1):16 (3,1):16 (5,1):56` ✓ | PASS |

Authorized rank-3/5 input = **72** piece records ✓. Rank-1 rejected at input = 16.
**Occurrence total = 720** — an OUTPUT (560 rank-5, 160 rank-3), never assumed.

**Φ_e superseded-rule discard (not an error).** An earlier transcription used the
abutting translation `mu + 2*arclen`. Validator's final β check corrects Φ_e to
the identity: `beta_2 = beta_1 (mod rank)`, `mu_2 = mu_1`. Re-transcribed from
corrected §4.4. Note for the record: because the footprint is `c = r^m` of length
`m*rank` and `2*m*rank ≡ 0 (mod 2*rank)`, the discarded expression was already
numerically the identity in this frame — **no computed value changed**. Removed
anyway, since §4.4 forbids any β-based test for abutment-vs-two-views.

**Four mandatory fixtures — all PASS** (amended per Lead 2026-08-05):

1. genuine two-arc continuation passes — `AABBA@c3.s0.p0` (ε=−1, μ=7, rank 5) with
   `abbaa@c3.s1.p1` (ε=+1, μ=7, rank 5);
2. reversal **at rank 3** (amended): all 16 rank-3 pieces, 0 violations of
   `Norm` invariance / `ε→−ε` / `β→β` (e.g. `baaBB` ε=+1 μ=1 ↔ `bbAAB` ε=−1 μ=1);
3. **true β-position mismatch** (amended): μ 7→8, all other fields identical —
   correctly rejected;
4. survivor rank-3/5 graph **nonempty** — 3600 hard-predicate compatible pairs.

## Edge stage (2026-08-05, post-unhalt)

Authorities pinned: [[2026-08-05-b25-stage1-v2-disposition-and-CC6-TR-preruling]]
Part 5 (Validator-signed) and [[ell6-theory-barrier-analysis-2026-08-05]] §§4.4/4.9
(landed). **Superseded convention discarded, not an error:** the provisional
rank6+carrier four-defect reading is replaced by the Validator ruling — the four
germs are **2 endpoints × 2 rank-6 sides**; the carrier is the common structure,
already carried by `(t,rho,m,epsilon,beta)`, and a rank6/carrier germ set would
fail to retain `x != y`.

**Reconciliation before graph build (required by d-f1): CLEAN.** 720 one-sided
rows = 72 pieces × exactly 10 rows each, all 72 represented, closed under label
inversion, 560 rank-5 / 160 rank-3. Matches the 88/72 oracle.

**Contact assembly (pairing, not matching; O(N²)):** **1800 contacts** — an
output, *not* the 360 that a matching reading would give. `B_zero_partner = 0`.

**Five D4 defect fixtures — all PASS:**

1. `p=sx, q=sy` with `s=AABBA, x=B, y=b` → `D=(b,B,B,b)`, `D⁻=(x⁻¹,y⁻¹)=(b,B)`,
   `D⁺=(x,y)=(B,b)`, and `x≠y` retained. *(First harness attempt FAILED because it
   hand-assigned `a_R=y`; the correct `a_R=inv(y)=B` is forced by `u_R=inv(u_L)`
   and `|q|=6`. Germ formula was never at fault — the harness was. Recorded.)*
2. repeated consistently-oriented contacts with the same ordered `(x,y)` pass D4;
3. `Rev` applied twice returns the original tuple;
4. changing exactly one matched germ makes D4 fail;
5. an L/R tag swap preserving cell identities leaves the D4 verdict unchanged
   (pairing by recomputed **cell id**, per c-f1).

## HALT — empty contact graph, diagnosed

With hard carrier fields applied first and D4 second (the specified order):

```
ordered pairs passing hard fields (Norm, beta, eps_1=-eps_2) : 45,000
   of those, D4 PASS                                          :      0
   of those, D4 FAIL -> B_base_gap                             : 45,000
MUTUAL-UNIQUE EDGES                                            :      0
```

§4.9 says an empty graph **halts as a suspected frame error rather than becoming
a result**. Halted. The diagnostic, however, points at neither `Phi_e` nor
`B_base_gap`:

```
Norm+beta                       : 88,200
Norm+beta + eps OPPOSITE        : 45,000   + D4 ->      0
Norm+beta + eps SAME            : 43,200   + D4 -> 43,200
Norm+beta (no eps condition)    :          + D4 -> 43,200
```

### The emptiness is FORCED, not sparse (structural result)

Re-checked against the landed text: §4.4 line 496 imposes `epsilon_1=-epsilon_2`
**and** line 498 imposes D4, both at **contact** level. The implementation is
exactly conformant. Given both, emptiness is a theorem on this data:

```
hard-compatible ordered pairs                                     : 45,000
side-conditions reducing to a requirement  x == inv(x)            : 90,000  (= 2 per pair, ALL of them)
letters satisfying x == inv(x) in a free group                    : none
```

On every hard-compatible pair and on **both** sides, the incoming germ of
`gamma` at a given cell id already equals the outgoing germ of `alpha` at that
same cell id. D4 requires `out(alpha,c) = inv(inc(gamma,c))`, which therefore
reduces to `x = inv(x)` — unsatisfiable in a free group. So the edge set is
empty for a structural reason, independent of the survivor data: this is not
sparsity, not a `Phi_e` frame error, and not `B_base_gap` (a base-region effect
would be partial, never a clean 45,000/0 partition).

D4-passing and `eps_1=-eps_2` are **exactly complementary — zero overlap**. A
perfect anticorrelation is a convention collision, not a statement about
intervening base regions. Reported hypothesis (**not** acted on): contact
assembly already consumes the inversion, since §4.4 requires `eps_R = -eps_L`
*within* a contact; re-imposing `eps_1 = -eps_2` *between* contacts applies the
flip a second time. The arc-level rule may not lift unchanged to the
contact-level rule. **Not resolved here** — dropping a predicate to make edges
appear is precisely the prohibited move.

## RESUMED and COMPLETE (2026-08-05 17:27, after the §§4.4/4.9 amendment landed)

Validator's Part 6 confirmed the double-flip diagnosis and superseded the
contact-level conjunct. Amended §4.4 (verified present before resuming, 17:27:23):
`epsilon_R=-epsilon_L` belongs to **assembly only**; between contacts,
`epsilon_L(alpha)=epsilon_L(gamma)` is **asserted after D4**, never used as a
rejecting conjunct, and a violation halts as an upstream bug.

**Obligation (1) — D4 negative fixture: PASS.** Hand-built pairs sharing hard
fields and ε-coherence but violating the germ-inverse relation:

| fixture | D4 | required |
|---|---|---|
| positive control | True | True |
| germ broken on cell 7 (`out=B`, `inv(inc)=b`) | **False** | False |
| germ broken on cell 9 (other side) | **False** | False |
| cell-id sets differ — no unique bijection | **False** | False |

D4 is discriminating and **both** sides are load-bearing. This closes Part 6's
flag that D4 rejected nothing within the ε-same class on real data.

**ε assertion: 0 violations** across all D4-passing pairs — the invariant holds,
corroborating Part 6's derivation that ε coherence follows from the shared cell.

## Obligation (2) — VACUITY CENSUS (first measurement out of the build)

```
contacts                         : 1800      B_zero_partner :      0
total contact ends (2 each)      : 3600
  terminal (0 candidates)        :    0   ( 0.0%)
  unique-candidate               :    0   ( 0.0%)
  BRANCH TOKENS (>1 candidate)   : 3600   (100.0%)
candidate-count histogram        : {24: 3600}   -- uniform, every end
B_base_gap (hard-compatible, D4-failing) : 45,000
MUTUAL-UNIQUE EDGES              :    0
```

## RESULT — VACUOUS

**100% of contact ends are branch tokens; the mutual-unique edge set is empty.**
Per obligation (2-o2) this is the reportable result: the
degree-≤2-by-construction graph carries **no corridor content**, and CC6-TR
concludes nothing on the frozen 26 survivors.

This is a *structural* degeneracy, not a marginal one. Every end has **exactly**
24 candidates — a perfectly uniform density. Mutual-uniqueness can therefore
never fire anywhere in the graph; it is not that most ends are ambiguous, it is
that no end is ever unique. No candidate-pair count is offered as a result: per
Part 6 it is an input to this census, and the census is negative.

**Not claimed:** no positivity, no curvature inequality, no `G_5` no-hit, no
connected-shell conclusion, no cycle/branch/rank-1 enumeration or charge. The
2×2 exponent-4/6 control obligation does not arise, since no lemma is drawn.

## Status

`#status/pending` — **run COMPLETE, result NEGATIVE (vacuous graph).** All
fixtures pass (4 carrier + 5 defect + 1 negative). Awaiting Validator/Lead
disposition. Standing caveat: any apparent falsifier remains provisional pending
the verified-`G_5` nontriviality recheck.

**Standing caveat on all outputs:** an apparent falsifier is provisional until a
later verified-`G_5` nontriviality recheck.

## Related

- [[uniform-step-audit-2026-08-04]] — the ell=6-over-G_5 decider this feeds
- [[ladder]], [[B25/_progress]]

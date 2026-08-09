---
title: Delta Stage-1 v2 disposition (ACCEPT) + CC6-TR repaired-carrier pre-ruling
status: replicated
domain: group-theory
project: b25-infinite-witness
claim: "Stage-1 v2 remediation meets all four Validator requirements; and the repair-(b) carrier kappa is total, correctly graded, with corner-incidence the right partition unit."
claimant: Delta (Stage-1 v2) / Math-expert (CC6-TR)
verification_method: independent re-read of the v2 JSON; exhaustive kappa computation over all 308 length-5 cross-class pieces
tools_used: [ell6_witnesses_stage1_corrected_20260805T080305Z.json, exhaustive enumeration L=5,6]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25-infinite-witness, topic/uniformity, status/replicated, proof]
---

# Stage-1 v2 disposition + CC6-TR pre-ruling

## Part 1 — Delta Stage-1 v2: ACCEPT

Verified from the JSON directly (`sha256 4ee498ef2e4e77a0…`, matches the routed hash), not from the
summary. All four requirements met:

| Requirement | Receipt |
|---|---|
| ungated relator-level search | `abelianization_used_to_prune_relator_search: False` at search level **and in all 325 pair records**; `relator_pairs_searched_without_ab_pruning: 325` |
| both signs | `relator_signs_searched: ['+','-']` per pair; bound 5, 485 conjugators |
| 36 reclassified | `old_58_to_36_line_status: withdrawn; has zero conjugacy content`; prior `g` histogram `{0: 36}` recorded; moved to trivial-drop bucket |
| empty-NF generator fix | `empty_nf_collision_policy: excluded from every collision and direct-equation candidate source` |

Spot-check of the fix working as intended: pair `(AABAAb, AABABB)` carries
`root_ab_label: root-ab-obstructed` yet `status: all-sign-relator-search-no-witness-found` — an
ab-obstructed pair that was searched anyway. That is exactly the corrected behaviour.

**My (i)/(ii) disambiguation is answered as case (i)** — `empty_semantics: "reduction ran to
completion under the frozen deterministic rule application and returned empty string"`. Sound drop,
licensed.

**Results, correctly qualified by Delta themselves:** 58 raw → **32 sound trivial-p⁵ drops** → **at
most 26** not-shown-trivial survivors (`survivor_interpretation: "at most this many genuinely-new
ell=6 relators; nonempty output is not a nontriviality proof"` — the phrasing I required), and
`candidate_pairs: 0`, `pair_count_union_of_candidate_sources: 0`, 26 singleton components. **True
survivor edge count = 0 at full 325/325 coverage.**

**Disposition: #status/replicated.** The 32 drops are sound and licensed. The 26→26 zero-edge result
remains **bounded-search** on two independent axes — conjugator length ≤ 5, and a non-confluent
reducer — both of which *inflate* the survivor count, i.e. bias toward "barrier stands", the
direction my pre-registration permits. Delta labels the graph
`provisional_candidate_graph_only_not_certified_dedup`, which is correct. Stage-2 gate unchanged.

**Standing conclusion:** root conjugacy is not the rescue at ℓ=6. Only fifth-power / normal-closure
elimination is live.

---

## Part 2 — CC6-TR repaired carrier: pre-ruling on the three questions

### (1) Is κ total and graded at the right base-relator rank? — YES, both. Verified.

**Totality is a theorem, and worth recording as such.** For a freely reduced non-empty `s`, cyclic
reduction never returns the empty word: the final stripping step would require a two-letter word
`x x⁻¹` to be freely reduced. So `c ≠ ε` always, `r` exists, `κ` is total on every arc — not only on
odd-length ones. Exhaustive check over all 308 length-5 cross-class pieces:

```
pieces = 308     kappa undefined (c empty) = 0     carrier r^5 missing from g5 = 0
(rank=|r|, m):  (1,1):24   (1,3):8   (1,5):4   (3,1):48   (5,1):224
ranks present:  {1, 3, 5}
```

**Grading is correct.** `r` is cyclically reduced and primitive with `|r| ≤ 5`, so `r⁵` is always a
genuine relator of the gated `g5` — 0/308 missing. And the specific defect from
[[2026-08-05-b25-R6-definition-gates]] (iv) is fixed: `AAAAA, BBBBB, aaaaa, bbbbb` now land at
**rank 1, m = 5**, not rank 5. The 224 rank-5 arcs are exactly the 224 root-carrier pieces from that
count. Repair (b) does what it was chosen to do.

**Structural fact worth using:** `|s| = 5` is odd ⟹ `|c|` is odd ⟹ **rank ∈ {1,3,5} only** — never
2 or 4.

**Two new requirements this creates.**

- **(1a) Corridors can be MIXED-RANK, and §4 did not anticipate that.** §4 assumed "a rank-6 cell
  meets another rank-6 cell along one rank-5 period", but 84/308 arcs carry rank 1 or 3. The
  continuation relation must state a **rank-compatibility rule** explicitly: a corridor mixing rank-1
  and rank-5 carriers has no single "old period `s`", so the corridor label is undefined for it.
- **(1b) The 36 rank-1 arcs have carriers of boundary length 5.** A rank-1 carrier `a⁵` has boundary
  length 5 < 15, so any step of the form "close through the old cell with a ≥15 arc" is *impossible*
  on them. For the 4 arcs with `(1,5)` the arc is the carrier's entire boundary — fully degenerate.
  These 36 need their own case, not the generic corridor argument.

### (2) Is cell-corner incidence the correct unit? — YES, with two caveats.

Corners are the standard curvature unit (combinatorial Gauss–Bonnet distributes over face–vertex
incidences) and they partition canonically: every corner belongs to exactly one (face, vertex) pair.
A fixed clockwise owner map assigning each incidence to at most one corridor gives **injectivity**,
which is precisely what non-double-counting requires. **Accepted as the unit.** The claim that the
partition alone supplies no positivity is correct and I endorse stating it.

- **Caveat A — the partition is of a sub-object, not of the diagram's curvature.** Restricting to
  rank-6 corners leaves base-region corners outside `C(D) = C_unassigned ⊔ ⨆ C_K`, and in a relative
  diagram base regions can carry arbitrary curvature. Any later Gauss–Bonnet step must account for
  the excluded part separately; the partition does not close the books.
- **Caveat B — injectivity is not sufficiency.** The owner map guarantees no corner is charged twice,
  but it can deprive a corridor of the very corner its "two charged ends" needs. The partition must
  therefore carry a **per-corridor retained-corner lower bound**, or the charging is well-defined and
  vacuous.

### (3) Minimum data the continuation relation must carry

Seven fields; the first is forced by choosing repair (b) and is the one most likely to be missed.

1. **The conjugator `t`.** Two arcs with the same primitive root `r` but different `t` have carriers
   `t r⁵ t⁻¹` that are **distinct conjugate cells**, not the same cell. Omit `t` and corridors will
   merge arcs whose carriers differ, invalidating the "close through an old `s⁵` cell" alternative.
2. **`m`** (from `c = r^m`) — arcs wrap the carrier differently; continuation must be `m`-compatible.
3. **Phase**: occurrence offset **mod 6** inside `p⁵`. The same label `s` at different offsets is a
   different occurrence.
4. **Cell identity, side, and traversal orientation** — without the side the corridor is not a path
   in the diagram.
5. **Defect letters at BOTH ends on BOTH sides** (4 letters). §4 records only the `x,y` from
   `p = sx, q = sy`, i.e. one end; corridors are traversed in both directions.
6. **A proven degree bound ≤ 2 on the continuation graph.** "Two charged ends" presupposes each
   component is a simple path (or a cycle/annulus with none). A branching component has more than two
   ends and the charge count is undefined. **This is the missing well-posedness condition** — either
   prove max degree 2 or define the charge at branch vertices.
7. **Finiteness/termination**, and — since components are taken as connected components — an explicit
   statement that the relation is **symmetric**; otherwise "maximal corridor" is ambiguous between
   maximal directed path and connected component.

### Verdict

- (1) **#status/proven** — κ total and correctly graded; plus two new obligations (1a) mixed-rank
  compatibility rule, (1b) the 36 rank-1 arcs need a separate case.
- (2) **#status/proven** that corners are the right unit; caveats A and B are open obligations.
- (3) the seven fields above are **required before any CC6-TR enumeration or proof attempt**; item 6
  is a well-posedness blocker, not a refinement.

Standing: the exponent-4/6 audit applies to every CC6-TR lemma.

Scope unchanged: no program-direction claim, no B(2,5)-infinite claim; Kourovka 11.48 open.

---

## Part 3 — CC6-TR-v2 repairs (sections 4.3–4.7): pre-ruling

**All four accepted, three with obligations, one with a finding that may make a module vacuous.**

### (1) Rank compatibility — ACCEPTED. Two obligations.
Requiring identical normalized `(t,r,m,rank)` makes the corridor label total, and demoting rank/`t`/`m`
changes to explicit **carrier-change defects** is the honest move: the 84/308 don't vanish, they
relocate into bookkeeping. Correct.
- **(1-o1) Prove the normalization is reversal-invariant**, `norm(s) = norm(s⁻¹)`. Otherwise the same
  geometric arc gets two different κ by traversal and continuation becomes traversal-dependent.
- **(1-o2) Write the reversal map on κ down explicitly and derive it — do not assume it.** Reversing
  an occurrence sends `c ↦ c⁻¹`, hence `r ↦ r⁻¹`, with `t` fixed. Inverse-in-a-nonabelian-group is
  this project's known failure mode (`(gh)⁻¹ = HG`, not `GH` — the bug that made this role exist).
  This is exactly where that class of error would reappear.

### (2) Degree ≤2 by construction — WELL-POSED, but it does not preserve completeness.
The construction achieves degree ≤2 ✓. Answering the question asked: **yes, refusing a non-unique
edge can lose a corridor.** Splitting replaces charged ends with branch tokens, so curvature can leak.
**But the loss is in the SAFE direction**: it can only make the argument fail to close, never prove
something false — provided one condition:
- **(2-o1) State and prove the dichotomy for the corridors of the CONSTRUCTED graph, not for an
  idealised notion of "true corridor."** A split piece may spuriously admit an area reduction that the
  whole would not, or vice versa. Never slide between the two notions.
- **(2-o2) Keep a branch-token census.** If the proof fails to close, ambiguous ends are the first
  place the deficit will be, and the census is what makes that diagnosable.

### (3) Rank-1 modules — well-posed, and R1-full is probably VACUOUS. Check before building it.
`(1,5)` arcs are `A⁵, B⁵, a⁵, b⁵`. Computed: the length-6 root classes whose `p⁵` contains a base
relator `x⁵` as a subword are exactly

```
aaaaab   aaaaaB   abbbbb   aBBBBB      (4 classes)
```

Each such `p⁵` is G_5-equal to a strictly shorter word (delete the trivial `x⁵`), so **the relator is
non-geodesic in G_5 and `p⁵` itself reduces** — these sit in Delta's 32 trivial-drop bucket, not among
the 26 survivors. Consistent with Delta's `nongeodesic_screen_count_after_nondrop: 0`.
**Ruling: before writing R1-full, have Delta confirm those 4 classes are inside the 32. If they are,
module R1-full is vacuous on the survivor set and should be dropped, not proved.**
`(1,1)`/`(1,3)` capped modules are well-posed **conditional on** both alternatives being defined over
the constructed graph, exhaustiveness proven, and the exponent-4/6 audit attached. Note that with the
≥15 claim correctly dropped, rank-1 modules are **bookkeeping-neutral by design** — verify the final
argument never secretly needs them to contribute charge.

### (4) RC2 + base-region ledger — ACCEPTED; both my caveats discharged. Three obligations.
"Two distinct retained endpoint rank-6 corner incidences per non-reducible rank-3/5 path" is exactly
the retained-corner lower bound (caveat B); the separate base-region ledger is exactly caveat A.
- **(4-o1) RC2 must be a LEMMA WITH PROOF, not a definitional requirement.** The clockwise owner map
  can assign both endpoint corners of a path to a neighbour. Add a fallback bucket for paths that fail
  RC2 so the framework stays total.
- **(4-o2) Cycles are the highest-risk module, not a minor sub-case.** A cycle has no ends, hence zero
  charged corners — and a closed flat corridor with propagating defect letters is precisely the
  failure mode section 4 predicted for itself. Treat it as the primary falsifier target.
- **(4-o3) The ledger must CLOSE as an identity**: base-region ledger + corridor charges + unassigned
  = the Gauss–Bonnet total, exactly. Keeping a ledger is not the same as balancing one.

### (1-o1)/(1-o2) — DISCHARGED (2026-08-05, second pass)

The derivation is correct at every step, and I checked the steps that could hide the known failure
mode rather than accepting them:
- `s⁻¹ = (t c t⁻¹)⁻¹ = t c⁻¹ t⁻¹` — correct application of `(gh)⁻¹ = h⁻¹g⁻¹`; the conjugation form is
  self-symmetric, so `t` survives. **This is the `(gh)⁻¹ = HG` trap navigated correctly.**
- `c⁻¹ = (r^m)⁻¹ = (r⁻¹)^m` — valid; powers of a single element commute, so no order is transposed.
- `t` genuinely reversal-invariant: the stripping predicate `s[-1] = s[0]⁻¹` is preserved under
  reversal, and the first letter accumulated into `t'` is `INV(s⁻¹[-1]) = s[0]`; induction gives
  `t' = t`.

Machine check over **all 17,188 freely reduced arcs of every length 1..29** on the symmetrised rank-6
relators (not only the 308 critical ones), with the total order taken as shortlex under g5's
`generatorOrder [a,A,b,B]`:

```
Norm(s) != Norm(s^-1)           : 0
t not preserved under reversal  : 0
epsilon not negated             : 0
r == r^-1 (epsilon ill-defined) : 0
```

**Both obligations discharged.** Four conventions must still be written into §4.3:

1. **State why ε is well defined**, don't rely on the enumeration: `r = r⁻¹ ⟹ r² = 1 ⟹ r = ε` in a
   free group (torsion-free). The 0 count above is confirmation, not the argument.
2. **Put the ε-rule explicitly in the continuation predicate.** `Norm` deliberately forgets ε, so the
   entire gluing condition lives in ε. §4.3's "inverse carrier orientation as gluing requires" means
   continuation needs `ε₁ = −ε₂`; if the predicate is written as "Norm equal" alone it will link arcs
   that cannot glue.
3. **Add a carrier basepoint field.** `r` is a canonical word (the length-`|r|` prefix of `c`), but the
   *cell* `r⁵` is stored in g5 as one rotation/inversion class representative. "Close through the old
   `s⁵` cell" needs to know where on that cell's boundary the arc sits — record the rotation offset
   mod `|r|` against the stored representative. This is the carrier-side analogue of the phase-mod-6
   field already carried for rank-6 cells.
4. **Fix the total order to shortlex under `generatorOrder [a,A,b,B]`**, matching the gated g5. An
   ad-hoc order makes ρ disagree between the theory bookkeeping and the computational receipts.

**Verdict:** (1) #status/proven as a definition; (1-o1)/(1-o2) **discharged**, conventions 1–4 open. (2) #status/proven
well-posed; completeness **not** preserved, loss in the safe direction under (2-o1). (3) R1-full
**#status/conjectured vacuous** pending Delta's confirmation; capped modules well-posed conditionally.
(4) accepted with (4-o1)–(4-o3). **Enumeration authorized for the rank-3/5 path module only**, once
(1-o1)/(1-o2) are discharged; cycles, branches and rank-1 stay unauthorized.

---

## Part 4 — β frame and the Φ translation (§4.4/4.9): ruling + one caught error

### The frame — F2, ruled
`β` must live in the **fixed** reference word `W_carrier := t · r̂⁵ · t⁻¹` (`r̂` = stored g5
representative), as an **unoriented interval position**, never a start offset in the traversal frame.

The rejected reading (F1 — β locating `r` against `r̂` as `r = rot_j(r̂^σ)`) makes the claimed reversal
map false: by `inv(rot_j(w)) = rot_{−j}(inv(w))` (verified, 8020 cases, 0 violations), reversal sends
`(j,σ) ↦ (−j,−σ)`. Under F2 the arc's position *set* is unchanged, so `β ↦ β` holds. Design
principle: **ε owns all orientation, β owns none** — that is what keeps the predicate an equality.

### The caught error — `+2·length` is wrong on rank 3
The abutting translation is by the arc's **carrier footprint** `|c| = m·rank`, **not** by the arc
label length `|s| = 5`:

```
rank  m  |s|  |c|=m*rank | true mu2-mu1 | their +2*|s| | with +2*|c|
   3  1    5           3 |          0 |    4  WRONG  |    0   OK
   5  1    5           5 |          0 |    0   OK    |    0   OK
```

`μ₂ = μ₁ + 2·|s| mod 2·rank` is **accidentally correct on the 56 rank-5 pieces** (`10 ≡ 0 mod 10`)
and **wrong on the 16 rank-3 pieces** (`10 ≡ 4 mod 6`). A rank-5-only smoke test cannot see it.

### The stronger form to adopt instead
Continuation already requires `Norm` equality, fixing `m₁ = m₂ = m` and `rank`. Hence

`μ₂ − μ₁ = rank·(m₁+m₂) ≡ 2m·rank ≡ 0 (mod 2·rank)`  ⟹  **`Φ_e` is `μ₂ = μ₁`, unconditionally.**

Equivalently `start₂ = start₁ + m·rank ≡ start₁ (mod rank)`. The translation term vanishes
identically; do not carry a "corrected offset".

Two consequences to state in the contract:
1. **Reversal-invariance is automatic; the doubled-midpoint device is not load-bearing.** The reversed
   arc starts at the original end, and `start + |c| ≡ start (mod rank)` because the footprint is a
   whole number of periods. Keep μ for uniformity if desired, but the invariance no longer rests on it.
2. **β cannot distinguish `Φ_e` from `Φ_id`** — the abutting translation is ≡ 0, so "two views of one
   contact" and "end-to-end continuation" agree in β exactly. That distinction lives **entirely** in
   the endpoint/direction field. Say so explicitly, or a later β-based test to separate the cases will
   silently accept everything.

**Fixture amendment:** fixture 2 (reversed-arc pair still passes) must be run **at rank 3**; rank 5
cannot separate the correct formula from the wrong one. Fixture 3 remains meaningful — β does
discriminate position on the carrier, just not contact-vs-abutment.

---

## Part 5 — CC6-TR local gluing rule (§4.4/4.9): four-part SIGN-OFF

**(a) accept · (b) accept · (c) accept with two flags · (d) accept with one flag.** Cleared to route
to B25 once (c)'s two flags are in the text.

### (a) Two-rank6-side convention — CORRECT; B25's provisional rank6/carrier convention is wrong
"Four defects" means **2 endpoints × 2 rank-6 incidences**, which is what the durable wording
`x,y from p=sx, q=sy` intended. Structural reason it cannot be rank6/carrier: the defect exists to
record how the two **rank-6 relators diverge** past the shared arc. The carrier does not diverge — it
is the common structure, already captured by `(t, ρ, m, β)`. A rank6/carrier germ set would duplicate
that and **fail to retain `x ≠ y`**, which is the entire content of the defect. So the 720 rows are
one-sided occurrence incidences.

### (b) Outward-germ formulas and reversal — CORRECT, verified on real survivor data
`δ_L⁻ = inv(b_L)`, `δ_L⁺ = a_L`, `δ_R⁻ = a_R`, `δ_R⁺ = inv(b_R)`; `D = (L⁻,L⁺,R⁻,R⁺)`.

```
p=AABBAB  q=AABBAb  s=AABBA  x=B  y=b
native L: b_L=B  u_L=AABBA  a_L=B
native R: b_R=B  u_R=abbaa  a_R=B        (u_R = inv(u_L) ✓)
germs D = (b, B, B, b)
D^- = (b,B) = (x^-1, y^-1) ✓        D^+ = (B,b) = (x, y) ✓
```

`Rev(D) = (R⁺,R⁻,L⁺,L⁻)` with no second inversion is correct **because outward germs are already
frame-independent**, so reversal is a pure permutation. Involutivity then holds structurally:
position-reversal on a 4-tuple is an involution regardless of contents. Note the verifying example is
itself reversal-symmetric (`Rev(D) = D`), so it does **not** discriminate involutivity — the
structural argument is what establishes it.

### (c) Straight componentwise-inverse D4 — accept, TWO FLAGS
`δ_L⁺(α) = inv(δ_L⁻(γ))` ∧ `δ_R⁺(α) = inv(δ_R⁻(γ))`, crossed/one-sided as diagnostics: correct. At a
direct junction the two germs traverse the same edge in opposite directions, hence the inverse
relation; requiring both sides is right because a corridor is two-sided; refusing one-sided matches is
safe-direction per Part 3 (2).

- **(c-f1) Pair by CELL ID, not by the L/R tag.** L/R is *assigned* by orienting via L, so after
  reorienting α⁺ to γ⁻ the tags must be recomputed. Comparing L-tag to L-tag post-reorientation can
  silently cross the sides — the exact failure "straight vs crossed" exists to prevent.
- **(c-f2) The condition encodes DIRECT abutment.** In the relative category a base region may sit
  between two contacts; then the germs are not literal inverses and the pair will not link. That is a
  completeness loss in the safe direction, but it needs its own named diagnostic bucket — base regions
  between contacts are precisely what this category admits. **If the corridor graph comes back sparse,
  this is the first suspect, ahead of Φ.**

### (d) Contact-first graph level — correct, one flag
Vertices = assembled two-sided contacts. Corridors are sequences of contacts; `degree ≤ 2` and "two
charged ends" are statements about contacts; half-occurrences would double-count and make the degree
bound meaningless.

- **(d-f1) Assembly is a PAIRING, not a MATCHING.** A half-occurrence can pair with *every* occurrence
  of the inverse label on a different cell, so the contact count is **not** 360 and the assembly is
  worst-case O(N²) in 720. Record the assembled contact count as an output, flag any half-occurrence
  with zero partners (it can never lie in a corridor), and **reconcile 720 against the piece oracle
  (88 total / 72 rank-3/5) before building**, so a counting mismatch surfaces now rather than after
  the graph exists.

---

## Part 6 — contact-level ε: signed correction to Part 5

**My error, stated plainly:** I carried an arc-level condition across a level change without
re-deriving it. My own continuation equation annotated it `ε₁ = −ε₂ (gluing orientation)` — and
gluing orientation is a property **within** one contact (its two incidences), not **between** two
contacts. Once ruling (d) moved graph vertices from half-occurrences to assembled contacts, §4.4's
`ε_R = −ε_L` consumed that flip at assembly. Re-imposing it between contacts flips twice, which
empties the graph. B25's diagnosis (double-applied flip, not base-gap — which would be partial) is
correct, and their refusal to retune a signed predicate was the right call.

### Ruling: EQUALITY, enforced as an ASSERTION, not as a filter

```
ε_L(α) = ε_L(γ)     -- cell-id-matched side (c-f1); an INVARIANT, not a rejecting conjunct
```

**Not negation.** **Not silent removal.** The distinction matters:

- **Equality is correct but derived.** Continuation requires `Norm` equality (fixing ρ) and, via
  c-f1 + D4, matches **both** cells by id. A rank-6 cell carries one boundary word and therefore one
  traversal, so every occurrence on it with the same Norm reads ρ the same way — hence `ε_L` is
  already determined by the shared cell. It is a consequence of the other conjuncts, not independent
  information. This is what B25's model observation (repeated `p=sx, q=sy` contacts share the chosen
  L-ε, D4 propagating `(x,y)`) is showing.
- **Therefore it must not be a filter.** A derived condition used as a rejecting conjunct is inert
  when the derivation holds and *silently destroys the graph* when anything upstream is off — the
  exact failure just observed. As an assertion, a violation raises a loud diagnostic instead.

This supersedes my previous instruction to keep it as an explicit conjunct: same relation, different
enforcement. Orientation is owned by endpoint/direction and D4, as B25 proposed.

**Precondition to state in the text:** the derivation holds *because both cells are shared* between
α and γ. If the corridor definition is ever widened to permit a cell change on one side, `ε`
coherence stops being derived and must be re-derived before it is asserted.

### Two flags that survive the correction

- **D4 is non-discriminating on this data** — every ε-same pair passes it, so within its class it
  rejects nothing and remains untested. Add a hand-built negative: a pair satisfying hard fields and
  ε-coherence but violating the germ-inverse relation, which must fail.
- **Vacuity risk — measure before proving.** With mutual-uniqueness applied after D4 at this candidate
  density, most ends may have non-unique compatible choices and become branch tokens rather than
  edges. Per obligation (2-o2) the branch-token census is the diagnostic: **if nearly every end
  becomes a branch token, the degree-≤2-by-construction graph is vacuous and CC6-TR concludes
  nothing.** No candidate-pair count is accepted as a result here; it is an input to that census.

Gates [[ell6-theory-barrier-analysis-2026-08-05]] sections 4 and 8.
Extends [[2026-08-05-b25-R6-definition-gates]], [[2026-08-05-b25-ell6-theory-preruling]].

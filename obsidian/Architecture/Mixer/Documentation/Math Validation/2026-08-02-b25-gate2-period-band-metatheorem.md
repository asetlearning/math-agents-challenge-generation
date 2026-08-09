---
title: Gate 2 Period-Band Meta-Theorem v0.3 — Validator verdict (E7 survival in G_4)
status: conjectured
domain: group-theory
project: b25-infinite-witness
claim: "A banded-diagram Greendlinger meta-theorem certifies E7 ≠ 1 in G_4 = G_3/⟨⟨p_i^5⟩⟩, contingent on a band-contraction lemma, an annulus-exclusion lemma, and (a third, under-weighted) no-progress-band exclusion."
claimant: Math-expert
verification_method: proof-sketch audit + small-cancellation/periodic-diagram theory + independent combinatorial check of the period structure
tools_used: [python3 period-structure check, Ol'shanskii/Greendlinger + Fine-Wilf/pigeonhole, hyperbolic bounded-conjugacy]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25-infinite-witness, status/conjectured, proof]
---

# Verification — Gate 2 Period-Band Meta-Theorem v0.3

Deepest gate of the program. Source: `infinite_b25/avenues/math_expert_R2_full.md` §"Gate 2 Critical
Path" (757–981) + Delta constants (60–103) + verifier interface (386–560). Goal: certify E7 ≠ 1 in
G_4 = G_3/⟨⟨R_i⟩⟩, R_i = p_i^5, p_i ∈ {AABB, AAbb, ABAb, ABaB, ABab} (straight length-4 periods,
|R_i|=20). Approach: replace failed classical C'(1/6) (relators are proper 5th powers ⇒ huge
same-period self-overlap) by an **Ol'shanskii-style banded diagram** — quotient same-period
periodicity into bands, then run Greendlinger on the residual distinct-period pieces (≤3, and
3/20 < 1/6). **The approach is the correct one for proper-power relators; the skeleton is sound
GIVEN its lemmas; but it rests on THREE obligations, one more than the framing names.**

## Independent check of the period structure (linchpin)

`scratchpad` python, exact: all five p_i are **primitive**; **pairwise distinct cyclic/inverse
classes** (no shared rotation); and the **max common factor of p_i^∞ and p_j^{±∞} is exactly 3**
(worst: p3~p5, p4~p5) — matching Delta's LCP=3. This is now a **proof, not a scan**: every length-4
factor of p_i^∞ is exactly a rotation of p_i (verified: length-4 factors == rotations(p_i)); a
length-4 common factor of p_i^∞, p_j^∞ would be a rotation of both ⇒ p_i ~ p_j cyclically ⇒
contradiction. Hence **distinct-period pieces ≤ 3 hold against arbitrarily long periodic band sides**,
not merely the length-20 relators. This secures C(1)/C(4) robustly and the piece-core of Task 2.

## Task 1 — proof-sketch skeleton (steps 1,2,3,5,6): sound given the lemmas?

**Conditionally SOUND, with one caveat the framing omits.** Steps 1–2–3–5–6 form a valid
minimal-counterexample Greendlinger argument:
- Step 2 contradictions are correct: BR1 dipole ⇒ non-reduced (area minimality); BR3 strict-shortening
  ⇒ boundary/geodesic minimality (E7-NF geodesic can't shorten); BR5 strict arc ⇒ negates the "no
  strict arc" assumption.
- Step 5 **arithmetic is correct and does the classical work**: λ = 3/20 = 0.15 < 1/6 ≈ 0.1667
  (margin 1/60). Greendlinger (metric C'(λ)) gives an exposed boundary arc > (1−3λ)|R| =
  (1−9/20)·20 = 11, i.e. **≥ 12 > 11** — the strict-Dehn threshold is met with room, complement < 9.
- Step 6 is then a strict Dehn arc, contradiction. ✓

**Caveat (load-bearing): the skeleton needs THREE hypotheses, not two.** The named lemmas are (i)
band-contraction [step 4] and (ii) annulus-exclusion [C(2)]. But **C(3) — exclusion of no-progress
boundary-to-boundary bands (equal sides, no strict arc) — is a THIRD independent obligation** that
neither lemma delivers: contraction needs a *strictly shorter* side (a no-progress band has none), and
minimality does not kill an equal-side band. The document itself flags this at line 907
("boundary-to-boundary same-period bands AND same-period annuli can have arbitrary length") and marks
`band_no_progress` a "theorem kill-pattern," but the task framing folds only annuli + contraction.
**Do not treat Gate 2 as closeable once the two named lemmas land; C(3) must also be discharged.**
Given all of C(D) + band-contraction, steps 1–2–3–5–6 are valid.

## Task 2 — band-contraction lemma: prove / refute / minimal hypothesis

**Split verdict. The piece-preservation core is PROVABLE; the topological part is conditional; and the
lemma AS STATED (all "harmless bands") is FALSE and must be scoped.**

- **PROVABLE (clean):** contracting an internal same-period band to its shorter side creates **no fake
  long piece**. The shorter side is a factor of p_i^∞; any adjacent distinct-period cell R_j meets it
  in a common factor of p_i^∞ and p_j^∞, which is **≤3 by the periodicity argument above** (rigorous,
  infinite-length-robust). Short same-period neighbours either stay ≤3 or merge into a p_i-band (re-band;
  termination by the strict lexicographic decrease). So C(4) is preserved by contraction. I can supply
  this proof in full.
- **CONDITIONAL (topological preservation of boundary / strict-arc / reducedness):** provable for
  **internal disc bands** given (H1) a p_i **infinite-order / quasi-geodesic-axis certificate** (so the
  band's sides are genuine p_i-power geodesics — see Task 3; finitely obtainable from `geowa`, currently
  only empirical k≤30) and (H2) the lexicographic minimality (termination). Boundary is untouched for
  internal bands; a boundary-shortening contraction is already excluded by BR3/geodesicity.
- **FALSE as stated / must be scoped:** the lemma cannot cover **boundary-to-boundary bands** — those
  with a shorter side are killed by BR3 (not contracted), and equal-side ones are no-progress bands
  (C(3), a separate obligation). So the correct statement restricts to internal disc bands.

**Minimal hypothesis making Task-2 true:** *(scope)* internal disc bands only; *(H1)* the p_i
all-powers-geodesic automaton certificate. With these, band-contraction holds; the piece bound needs
no extra hypothesis (proved).

## Task 3 — annulus lemma: does bounded B_ann follow from K_FT = 10?

**Not from K_FT alone. It is TRUE in principle but needs an extra certificate, and the K_FT-only bound
is either huge (Papasoglu) or requires a bespoke width proof.**

- **Missing ingredient (decisive):** the bounded-conjugacy lemma requires each p_i to have a certified
  **quasi-geodesic axis** (infinite order, |p_i^k| ≥ λk ∀k). The k≤12 power-collision / k≤30 straight
  scans are **evidence, not a proof**. **This certificate is finitely obtainable** — run p_i through the
  geodesic automaton `geowa`/`geopairs`: p_i is straight iff reading p_i^ω cycles through accepting
  states (a finite eventually-periodic check). This is Math-expert's step-1 and Delta should produce it.
  Without it, unbounded-width annuli are not excluded and the lemma is *not even true*.
- **GIVEN the axis certificate, B_ann is finite:** conjugate elements have equal translation length ⇒
  a = ±b (residue search O(1)); and in a hyperbolic group the conjugator, reduced mod ⟨p_i⟩, is bounded.
  So a same-period annulus forces x p_i^a x^{-1} = p_i^b with |x| ≤ B_ann. **True.**
- **The K_FT-to-δ route is finite but likely infeasible:** Papasoglu gives δ = Pap(10), astronomically
  larger than the relators (the document's own line 97–98), so "exhaustively check all |x| ≤ B_ann" is
  not practically finite via that route.
- **A SMALL, checkable B_ann is plausible by a direct periodic thin-annulus/quadrilateral argument:**
  both annulus boundaries share the single p_i-axis, so their transverse separation is a geodesic-
  quadrilateral width controllable **directly by K_FT = 10** (bypassing Pap). I **estimate** the target
  is B_ann = O(K_FT + |p_i|) ≈ 2·K_FT + |p_i| ~ 24 — but **I will not certify the constant** without
  (a) the axis certificate in hand and (b) the width argument done rigorously; the periodic-annulus
  width bound is real geometry that can resist.

**Verdict:** the annulus obligation is **closeable in principle** (contra "not finitely checkable"),
contingent on the finitely-obtainable axis automaton certificate **plus** a direct width proof. If the
axis certificate is produced and the width proof yields a small B_ann, the exhaustive connector check
is feasible and annuli are excluded. If the width proof resists (only Pap(10) available) or the axis
certificate somehow fails, **annuli are not excludable ⇒ Gate 2 closes as bounded-frontier-only.**

## Task 4 — is threshold 4 (one period) the right band cutoff, given pieces ≤3?

**YES — correct and TIGHT (forced).**
- Cutoff must be ≤ 4: a length-4 same-period contact = one full period; treating it as an ordinary
  piece gives 4/20 = 0.2 > 1/6 ⇒ C'(1/6) fails. So anything ≥4 must be banded.
- Cutoff must be ≥ 4: length-1,2,3 same-period contacts are < one period, cannot form a periodic band,
  and are ≤3 so harmless as pieces. Banding them would be spurious.
- **No leakage:** any same-period *shared* arc of length ≥4 is automatically p_i-periodic (a shared
  edge-path forces the word to be a factor of p_i^∞, hence period-4), so band-condition 3
  (phase-compatibility) is automatic — there is no "length-≥4 same-period piece that escapes banding."
  Verified: length-4 factors of p_i^∞ are exactly rotations of p_i.
- **One clarification to lock in:** define "piece" = **literal shared edge-arc** (≤3, now *proved*),
  NOT axis fellow-travel. Delta's "D=2 length 4 / D=10 length 8" numbers are **parallel-axis
  fellow-travel (ladders)**, not shared arcs — they do not create pieces. Distinct-period ladders are
  **C'(1/6)-safe** because every *realized* contact is ≤3; the curvature argument tolerates many short
  pieces along a long boundary. (Ladders remain a separate structural note, but do not break the piece
  condition.)

## Overall verdict — #status/conjectured (meta-theorem OPEN, approach sound)

The Period-Band Meta-Theorem is the **right shape** and its skeleton is **sound given its hypotheses**;
the arithmetic (3/20 < 1/6 ⇒ exposed ≥ 12) is correct; and I have **upgraded the distinct-period piece
bound from a bounded scan to a proof**. It is **not a closed proof of E7 ≠ 1 in G_4**. It rests on
**three obligations**:
1. **Band-contraction** (Task 2): piece-core PROVED; topological part provable for internal disc bands
   given the p_i axis certificate; scope must exclude boundary-to-boundary bands.
2. **Annulus-exclusion** (Task 3): closeable in principle given the axis certificate + a direct small-
   B_ann width proof; the K_FT→Pap route is finite but infeasible.
3. **No-progress boundary-band exclusion C(3)** (Task 1 caveat): a THIRD obligation the framing
   under-weights — must be discharged for E7-compatible diagrams, or the theorem fails.

**Single highest-value unlock:** Delta should produce the **all-powers-geodesic automaton certificate**
for each p_i (finite, from `geowa`/`geopairs`) — it simultaneously supplies H1 for band-contraction and
the axis hypothesis for the bounded-conjugacy/annulus lemma, replacing every empirical k≤12/30 scan.

**Realistic outcome per the ground rule:** Gate 2 can close **POSITIVELY** (a genuine E7-survival
certificate at G_4) **iff** (a) the p_i axis certificate is produced, (b) the direct annulus width
proof yields a small checkable B_ann, and (c) C(3) no-progress bands are excluded for E7-diagrams.
If (b) or (c) resist — both are real geometry that can — **Gate 2 closes as a bounded-obstruction
frontier, which the ground rules already accept.** No G_4-survival claim may be made until all three
obligations are discharged; nothing here asserts E7 ≠ 1 in G_4 (that remains the open target;
E7 ≠ 1 in free B(2,5) is Kourovka 11.48).

## Notes for downstream agents
- **Do NOT report Gate 2 as "closed once band-contraction + annulus land"** — C(3) is a third gap.
- Delta: produce the finite all-powers-geodesic certificate for the 5 periods (unlocks 2 of 3 gaps).
- The distinct-period piece bound ≤3 is now PROVEN (periodicity), robust to infinite band sides — safe
  to rely on as a theorem, not a scan.
- "Piece" = literal shared arc; parallel-axis ladders (D>0 fellow-travel) are not pieces and are
  C'(1/6)-safe.
- If the annulus width proof or C(3) resist, close Gate 2 as bounded-frontier-only (acceptable) — the
  expansion-radius / Stallings-M frontiers [[2026-08-02-...]] remain the honest evidence layer.

## UPDATE 2026-08-02 — axis certificate LANDED and independently verified (2 of 3 unlocks discharged)

Delta produced the **all-powers-geodesic automaton certificate** I named as the highest-value unlock,
via DFA pumping on the certified `g3.geowa`. **I verified it independently** (own parser, own DFA walk,
not their `pumping_certificates()`): receipt `gate2_receipts/gate2_g3_raw_receipts_20260802T090750Z.json`.

- geowa: 2757 states, **all nonzero states accepting** (correct: geodesics are prefix-closed, so the
  geodesic acceptor is all-states-accepting — this is *why* the pumping works).
- Each p_i reaches a **fixed point after exactly one period**: state-after-p_i = 71/68/79/44/43 (matches
  receipt), `T_{p_i}(s)=s`, s≠0, intermediate phase states ≠0. Being a genuine fixed point of the
  period map in the all-accepting region, p_i^k is accepted **for all k** (I also directly confirmed
  acceptance for k≤200).
- **Metric cross-check (ties the DFA to the actual G_3 metric):** |NF(p_i^k)| = 4k for k=1..40 via the
  kbmag `wordreduce -diff2` reducer — geowa-acceptance genuinely equals G_3-geodesicity on the powers.

**Verdict: MEETS the bar for the finite axis certificate — in fact exceeds it.** It certifies a genuine
**geodesic** axis (|p_i^k| = 4k exactly, translation length exactly 4, no quasi-constant slack), stronger
than the quasi-geodesic axis I required. Residual trust anchor: kbmag's `geowa` being a correct geodesic
acceptor (the certified automatic structure — `geopairs` verification); the k≤40 metric cross-check
corroborates it directly on the p_i-powers. **Sound. #status/replicated → effectively proven for the
axis claim.**

**Ledger — which obligations this discharges (2 of 3):**
- **Obligation 1 (band-contraction): H1 DISCHARGED.** The band sides are now certified genuine
  p_i-power geodesics. Combined with the already-PROVED piece-core (distinct pieces ≤3 against infinite
  band sides), the band-contraction lemma for **internal disc bands** has its blocking hypothesis
  removed — remaining work is the topological write-up, not a new hypothesis.
- **Obligation 2 (annulus): FIRST HALF DISCHARGED** (the quasi-/geodesic-axis hypothesis for the
  bounded-conjugacy lemma). **SECOND HALF OPEN**: the direct small-B_ann width proof (with Math-expert).
- **Obligation 3 (C(3) no-progress boundary bands): NOT touched — OPEN** (with Math-expert).

**Gate 2 status unchanged: #status/conjectured / bounded-obstruction-frontier.** Two of three unlocks
are in; closure still requires (2b) the annulus width proof AND (3) C(3) exclusion. If either resists,
Gate 2 closes as bounded-frontier-only. No G_4-survival claim.

Verifies: `infinite_b25/avenues/math_expert_R2_full.md` §Gate 2 Critical Path; axis cert
`gate2_receipts/gate2_g3_raw_receipts_20260802T090750Z.json` (independently reproduced).

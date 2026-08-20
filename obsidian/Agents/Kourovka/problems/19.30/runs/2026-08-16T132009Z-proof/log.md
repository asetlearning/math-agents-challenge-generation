---
title: "Kourovka 19.30 — fresh proof-direction run log"
author: operator
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
direction: proof
started_utc: 2026-08-16T13:20:09Z
context_mode: discovery-blind-fresh-session
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/draft
---

# Proof-direction fresh run

## Context boundary

The ordinary synthesis, historical `log.md`, historical `findings.md`, old
transcripts, shared-chat material, archived messages, and solution-bearing local
artifacts were not inspected. The only mathematical handoffs read were the
canonical scope record, the permitted source-fidelity audit, and the permitted
MathExpert normal-prime/Suzuki criterion audit. The current inbox was listed but
its seven pre-assignment counterexample-direction messages were not opened.

No `RUN_DIR` was supplied in the assignment block. To preserve the discovery-blind
boundary without touching the historical append-only log, this fresh run uses
`Agents/Kourovka/problems/19.30/runs/2026-08-16T132009Z-proof/`.

Protocol-path note: the first rendered-page image was transiently written to
`/tmp` after an image-view path mismatch. It was used only to visually inspect the
permitted source PDF and is not mathematical evidence. The durable evidence path
for this run is vault-relative.

## Active-time ledger

- 2026-08-16T13:21:10Z — work started; proof-direction cumulative active minutes: 0.
- 2026-08-16T13:25:36Z — source/protocol gate and write-path diagnosis; cumulative active minutes: 4.

## Staleness check

`external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`

Open-web search, arXiv search, current-edition search, and solution-bearing local
search were deliberately not performed under the discovery-blind assignment.

The corpus record was checked only for the mandated flags. Exact observed record:

```json
{"id": "19.30", "issue": 19, "year": 2018, "page": 133, "answered": false, "has_editor_comment": false, "has_later_comment": false, "statement": "An element g of a finite group G is said to be vanishing if χ(g) = 0 for some irreducible complex character χ ∈ Irr(G). Must a finite group and a finite simple group be isomorphic if they have equal orders and the same set of orders of vanishing elements? M. Foroudi Ghasemabadi, A. Iranmanesh,", "proposers": [], "chars": 294}
```

Thus `answered: false`, `has_editor_comment: false`, and
`has_later_comment: false`. These flags are not a literature result.

### Source transcription

Rendered PDF page 134 was visually inspected at 220 dpi, independently of the
plain-text extraction. Corrected transcription:

> **19.30.** An element \(g\) of a finite group \(G\) is said to be vanishing if
> \(\chi(g)=0\) for some irreducible complex character
> \(\chi\in\operatorname{Irr}(G)\). Must a finite group and a finite simple group
> be isomorphic if they have equal orders and the same set of orders of vanishing
> elements?

`source_transcription_checked: yes`

The rendered source has no star, answer, editor comment, extra parameter,
nonabelian qualifier on “simple,” or multiplicity condition on the set.

### Clause matrix

| source clause | equivalent formulation | in active scope? | literature result in this run |
|---|---|---:|---|
| An element \(g\in G\) is vanishing iff \(\chi(g)=0\) for some \(\chi\in\operatorname{Irr}(G)\). | \(V_o(G)=\{|g|:g\in G,\ \exists\chi\in\operatorname{Irr}(G),\ \chi(g)=0\}\). | yes | none; literature gate deferred |
| Equal-order finite group and finite simple group with the same set of vanishing-element orders must be isomorphic? | For all finite \((G,S)\) with \(S\) simple, \(|G|=|S|\) and \(V_o(G)=V_o(S)\) imply \(G\cong S\). | yes | none; literature gate deferred |

`active_scope_checked: yes`

### Admissibility checklist

| constraint_id | rendered-source requirement | reconciled with scope record? |
|---|---|---:|
| 19.30-forall-GS | universal pair \((G,S)\) subject to all hypotheses | yes |
| 19.30-G-finite | \(G\) finite | yes |
| 19.30-S-finite-simple | \(S\) finite and simple; abelian simple groups are not excluded | yes |
| 19.30-vanishing-definition | zero of at least one irreducible complex character | yes |
| 19.30-equal-orders | \(|G|=|S|\) | yes |
| 19.30-equal-vanishing-order-sets | equality of sets of attained orders, not multiplicities and not the full spectrum | yes |
| 19.30-isomorphic | conclusion \(G\cong S\) | yes |

No source/scope mismatch was found. Excluded scopes remain excluded: equality of
character tables alone, equality of full element-order spectra, and pairs in which
neither group is finite simple.

### Source-gate command evidence

```text
command: source _meta/agents/Kourovka/paths.env && kv_now && test -r "$KOUROVKA_PDF" && pdftotext -f 134 -l 134 -layout "$KOUROVKA_PDF" -
observed relevant output:
2026-08-16T13:21:10Z
19.30. An element g of a finite group G is said to be vanishing if χ(g) = 0 for some
irreducible complex character χ ∈ Irr(G). Must a finite group and a finite simple
group be isomorphic if they have equal orders and the same set of orders of vanishing
elements?                                 M. Foroudi Ghasemabadi, A. Iranmanesh,

command: pdftoppm -f 134 -l 134 -singlefile -png -r 220 "$KOUROVKA_PDF" /tmp/kourovka-19-30-page
observed output from file inspection:
/tmp/kourovka-19-30-page.png: PNG image data, 1870 x 2420, 8-bit/color RGB, non-interlaced

command: rg -n <19.30 record patterns> Research/Group\ theory/Open\ problems/Kourovka/corpus
observed relevant output:
Research/Group theory/Open problems/Kourovka/corpus/kourovka-20-corpus.jsonl:1009:{"id": "19.30", ... "answered": false, "has_editor_comment": false, "has_later_comment": false, ...}
```

## Strategy portfolio

Ranked by expected certifiable information per active hour:

1. **Theoretical mode — minimal-normal prime separator.** Prove a general
   sufficient criterion: arithmetic conditions on every proper characteristically
   simple divisor force a normal Sylow subgroup \(C_p\) in each nonsimple
   same-order group; Clifford theory then excludes order \(p\) from its vanishing
   set. Keep separate the hypothesis that order \(p\) does vanish in \(S\), and
   the hypothesis that no nonisomorphic simple order-twin survives. Kill if the
   theorem cannot be stated with explicit hypotheses and a line-by-line proof.
2. **Structured-family mode — Suzuki specialization.** Substitute the order
   formula for \(\operatorname{Sz}(2^n)\), a primitive prime \(p\), abelian
   minimal-normal linear conditions, and nonabelian-factor automorphism conditions
   into the general criterion. Treat the four named classification/character
   inputs from MathExpert as explicit conditional inputs, not as established
   evidence. Determine honestly whether infinitude is actually proved.
3. **Catalogue/small-case mode — hand-only boundary tests.** No catalogue search,
   GAP, Sage, character-table enumeration, or solver is permitted. Check only
   symbolic edge cases (especially cyclic simple groups and the distinction
   “normal subgroup of order \(p\)” versus “normal Sylow subgroup of order \(p\)”).
   A negative check can expose a missing hypothesis but cannot establish universal
   recognition.
4. **Certificate plan.** Validator can check the general theorem from: the exact
   Clifford restriction formula; the cyclotomic-polynomial noncancellation lemma;
   a strong induction over divisor orders using minimal normal subgroups; and a
   row-by-row list of all external inputs in any family specialization. No
   computation or hidden character table is to be trusted.

Chosen first route: strategy 1, the cheapest independently checkable result.

## 2026-08-16T13:31:54Z — first checkable output

Active-time ledger update: cumulative proof-direction active minutes 11.

Draft: `scratch/minimal-normal-prime-separator.md`.

The draft has three layers that must not be conflated:

1. If \(N\triangleleft X\) has prime order \(p\), Clifford restriction and
   cyclotomic noncancellation show that every nonidentity element of \(N\) is
   nonvanishing.
2. This implies \(p\notin V_o(X)\) only if every element of order \(p\) lies in
   \(N\). A normal Sylow subgroup with \(|X|_p=p\) is sufficient. A merely
   characteristic subgroup of order \(p\) is not sufficient; the draft gives the
   hand-checkable example \(C_2\times S_3\).
3. An explicit pair of characteristically-simple-divisor hypotheses gives a
   strong-induction proof that every nonsimple group of the target order has such
   a normal Sylow subgroup. Recognition still separately requires (i) an
   order-\(p\) zero of an irreducible character of \(S\), and (ii) uniqueness of
   \(S\) among simple groups of its order.

This is currently a candidate `PARTIAL_RESULT`, not a scope-wide claim. The
Suzuki substitution is conditional on three arithmetic hypotheses and five named
external inputs. It does not establish that infinitely many parameters satisfy
the arithmetic hypotheses.

Questions were sent to Validator and MathExpert at 2026-08-16T13:27:34Z; work
continues without waiting.

## 2026-08-16T13:41:00Z — representation refinement and bounded sanity check

Active-time ledger update: cumulative proof-direction active minutes 20.

The first-power restriction was artificial. The draft now uses the full Sylow
order \(p^a=m_p\):

- if a normal Sylow \(p\)-subgroup is noncyclic, there is no element of order
  \(p^a\);
- if it is cyclic, Clifford orbit lengths divide the \(p'\)-index, while a
  vanishing sum of \(p^a\)-th roots has length divisible by \(p\), so its
  generators are nonvanishing;
- the minimal-normal induction forces a normal Sylow subgroup for arbitrary
  \(v_p(m)\), because an abelian minimal normal \(p\)-subgroup can be absorbed
  into the preimage of the quotient's normal Sylow subgroup.

Thus the Suzuki specialization no longer needs a squarefree primitive divisor.
It instead names the cyclic-Sylow/maximal-torus input explicitly. The simultaneous
linear condition for abelian minimal normal subgroups remains.

A bounded exact arithmetic probe was run only as a sanity check, not as evidence
of infinitude:

```text
command: python3 Agents/Kourovka/problems/19.30/runs/2026-08-16T132009Z-proof/scratch/parameter_probe.py
output:
n=3 factors={2: 6, 5: 1, 7: 1, 13: 1} P1_candidates=[(13, 1)] P1_P2_candidates=[(13, 1)]
n=5 factors={2: 10, 5: 2, 31: 1, 41: 1} P1_candidates=[(41, 1)] P1_P2_candidates=[(41, 1)]
n=7 factors={2: 14, 5: 1, 29: 1, 113: 1, 127: 1} P1_candidates=[(29, 1), (113, 1)] P1_P2_candidates=[(29, 1), (113, 1)]
n=9 factors={2: 18, 5: 1, 7: 1, 13: 1, 37: 1, 73: 1, 109: 1} P1_candidates=[(37, 1), (109, 1)] P1_P2_candidates=[(37, 1), (109, 1)]
n=11 factors={2: 22, 5: 1, 23: 1, 89: 1, 397: 1, 2113: 1} P1_candidates=[(397, 1), (2113, 1)] P1_P2_candidates=[(397, 1), (2113, 1)]
n=13 factors={2: 26, 5: 1, 53: 1, 157: 1, 1613: 1, 8191: 1} P1_candidates=[(53, 1), (157, 1), (1613, 1)] P1_P2_candidates=[(53, 1), (157, 1), (1613, 1)]
n=15 factors={2: 30, 5: 2, 7: 1, 13: 1, 31: 1, 41: 1, 61: 1, 151: 1, 1321: 1} P1_candidates=[(61, 1), (1321, 1)] P1_P2_candidates=[(61, 1), (1321, 1)]
```

Coverage is exactly odd \(3\le n\le15\) for the arithmetic formula only. The
probe says nothing about character inputs, group recognition, larger \(n\), or
infinitely many parameters.

### Append-only corrections to the 13:31 entry

- The earlier phrase “three arithmetic hypotheses and five named external
  inputs” described the first draft. The current draft has two arithmetic
  hypotheses **(P1)--(P2)** and eight explicitly named external inputs
  **(E0)--(E7)**.
- The first draft required \(v_p(m)=1\). The full-Sylow-order refinement removes
  that restriction.
- The corpus metadata says page 133, while the canonical record and the visually
  rendered PDF locate the statement on PDF/printed page 134. The formula and
  clauses agree; this is a navigation-metadata discrepancy, not a scope-clause
  mismatch.

### Reproducibility details

```text
command: python3 --version
output: Python 3.12.3

command: pdftotext -v 2>&1 | head -n 1
output: pdftotext version 24.02.0

command: pdftoppm -v 2>&1 | head -n 1
output: pdftoppm version 24.02.0

command: sha256sum <proof-draft> <parameter-probe> <findings>
output:
e1ed1feb8c355e9d1025851ec3af0ae77fd31ef858c75e91015cefdd4543e66c  Agents/Kourovka/problems/19.30/runs/2026-08-16T132009Z-proof/scratch/minimal-normal-prime-separator.md
6ac9e4500e451a49f869b476a63aa96ce80f811a478f9911bd40b90ca4a721de  Agents/Kourovka/problems/19.30/runs/2026-08-16T132009Z-proof/scratch/parameter_probe.py
7cb66950442eb7cae3ae74219fabe2710d198732b3c224bd68c6a73b10be8f13  Agents/Kourovka/problems/19.30/runs/2026-08-16T132009Z-proof/findings.md

command: source _meta/agents/Kourovka/paths.env && pdftoppm -f 134 -l 134 -singlefile -png -r 220 "$KOUROVKA_PDF" "$KOUROVKA_VAULT/Agents/Kourovka/problems/19.30/runs/2026-08-16T132009Z-proof/scratch/source-page-134" && ls -lh <vault-relative image>
output:
-rwxrwxrwx 1 kmuli kmuli 556K Aug 16  2026 Agents/Kourovka/problems/19.30/runs/2026-08-16T132009Z-proof/scratch/source-page-134.png
```

Operational failures, with no mathematical effect:

- The first workspace-relative `mkdir` returned
  `Read-only file system`; sourcing `paths.env` and using
  `$KOUROVKA_VAULT` succeeded.
- The first durable image view returned `No such file or directory`, so the page
  was rendered transiently for visual inspection and later rerendered to the
  vault-relative evidence path above.
- One cleanup command containing `rm -f` was rejected before execution.
- One diagnostic `rg` expression returned `regex parse error: unclosed group`;
  the corrected fixed-pattern search returned only the expected historical
  phrase in the append-only draft.

## ~30-minute self-check — 2026-08-16T13:48:43Z

Active-time ledger update: cumulative proof-direction active minutes 28.

- **Target and revision:** `19.30/vanishing-order-simple-recognition`, revision 1,
  proof direction.
- **Current hypothesis:** Theorem 4 in the proof draft: two explicit
  characteristically-simple-divisor conditions, a vanishing element at the full
  Sylow order \(m_p\), and simple-order uniqueness suffice for recognition.
- **New checkable facts:** prime-order Clifford noncancellation with its exact
  coverage condition; full-Sylow-order noncancellation; strong minimal-normal
  induction for arbitrary \(v_p(m)\); and a conditional all-odd-parameter Suzuki
  substitution with every dependency named.
- **Evidence:** line-by-line draft, explicit warning example
  \(C_2\times S_3\), bounded arithmetic script and verbatim output, and the
  constraint matrix in `findings.md`.
- **Representation assessment:** productive for an abstract partial theorem;
  currently unproductive for proving an infinite nonabelian family. Bounded
  arithmetic agreement cannot settle infinitude.
- **Admissibility:** there is no scope-wide candidate. The finite-group,
  finite-simple-group, exact vanishing definition, equal-order, and equal-set rows
  are used correctly inside the sufficient subclass. The universal-quantifier and
  isomorphism-conclusion rows are not established universally. The
  \(C_2\times S_3\) example is a warning example, not a target candidate.
- **Bottleneck:** prove the simultaneous linear condition for infinitely many
  Suzuki parameters and ground **(E0)--(E7)**, neither of which follows from the
  discovery-blind evidence.
- **Alternative A (arithmetic):** seek a theorem guaranteeing a primitive prime
  with \(\operatorname{ord}_p(r)>v_r(m)\) for every other prime divisor. Kill if
  it reduces to unproved primitive-divisor/Wieferich distribution after one exact
  reduction.
- **Alternative B (representation-changing):** when the linear condition fails,
  analyze the nontrivial \(p\)-action on \(C_r^d\) by Clifford induction and try
  to force a mixed vanishing order absent from the Suzuki torus spectrum. Kill if
  the fixed-point-free case yields only the already-present full \(p\)-power and
  no exact additional order without a character table.
- **Recommendation:** preserve the abstract theorem as `PARTIAL_RESULT`; do not
  claim an infinite Suzuki family. Only pursue Alternative B if Lead values one
  further hour over packaging.

Current proof-draft SHA-256 (superseding the earlier append-only hash):

```text
c0a0d6d72ab23072868a70189550420b50c300e479f80e6e0b5b381b31f038fc  Agents/Kourovka/problems/19.30/runs/2026-08-16T132009Z-proof/scratch/minimal-normal-prime-separator.md
```

- 2026-08-16T13:49:35Z — active work stopped pending Lead/Validator/MathExpert
  file-bus replies; cumulative proof-direction active minutes: 28. Waiting time is
  not charged.

- 2026-08-16T13:50:45Z — active work resumed for outcome packaging; cumulative
  proof-direction active minutes: 28.

## Cycle outcome — PARTIAL_RESULT

The run ends with one partial result: the minimal-normal prime-power separator in
`findings.md`, with line-by-line proof in
`scratch/minimal-normal-prime-separator.md`.

Precise coverage: finite simple groups \(S\) for which some prime \(p\) satisfies
the two stated characteristically-simple-divisor conditions, \(S\) has a
vanishing element of full Sylow order \(|S|_p\), and \(S\) is unique among finite
simple groups of its order. For this subclass, any same-order group with the same
vanishing-order set is isomorphic to \(S\).

Precise noncoverage: the universal target, unconditional Suzuki recognition, and
infinitely many nonabelian simple targets are not established. The odd-exponent
Suzuki substitution remains conditional on **(P1)--(P2)** and **(E0)--(E7)**.
The finite arithmetic probe is not promoted beyond its explicit bound.

The representation was refined from an order-\(p\) separator to a full-Sylow-order
\(p^a\) separator, removing an unnecessary squarefreeness condition. A further
representation-changing action/mixed-order pivot was named but not executed; it
is left for Lead to schedule if desired.

Final artifact hashes:

```text
c0a0d6d72ab23072868a70189550420b50c300e479f80e6e0b5b381b31f038fc  Agents/Kourovka/problems/19.30/runs/2026-08-16T132009Z-proof/scratch/minimal-normal-prime-separator.md
6ac9e4500e451a49f869b476a63aa96ce80f811a478f9911bd40b90ca4a721de  Agents/Kourovka/problems/19.30/runs/2026-08-16T132009Z-proof/scratch/parameter_probe.py
e3294279a452c93075075afbf74547610eccb6d9689b646c48d605e07729714c  Agents/Kourovka/problems/19.30/runs/2026-08-16T132009Z-proof/findings.md
```

Validator and MathExpert review remain pending. No `CLAIM`, `STALE_MATCH`, or
scope-wide answer is asserted, and no extension is requested in this outcome.

- 2026-08-16T13:52:05Z — outcome messages written and active work stopped;
  cumulative proof-direction active minutes: 30. Cycle outcome:
  `PARTIAL_RESULT`.

## Resume — P-A5-5-HYPOTHESIS-CLOSURE

- 2026-08-16T17:05:12Z — resumed under Lead decision
  `2026-08-16T165948Z__Lead__DECISION__a5-p5-hypothesis-closure.md` at shared
  ledger 106/180; remaining active budget 74 minutes; safety stop
  2026-08-16T18:59:48Z.
- Resource boundary: exactly the linked five-row hand dossier. No web, history,
  external character table, named classification theorem, mathematical
  computation, or delegate. Stop at the first conditional, cited-but-unexpanded,
  or blank terminal row.
- Controlling metadata throughout: `status/conjectured`,
  `witness_equals_target: false`, `active_assignment_answered: no`.

Active work started at shared cumulative minute 106.

### Five-row construction and first self-audit — 2026-08-16T17:22:01Z

Shared cumulative active minutes: 123/180 (17 minutes charged since the
17:05:12Z resume; no waiting interval charged).

- Row 1 (`base`) has an explicit order calculation, complete even-cycle-type
  list, class sizes `1,20,15,12,12`, all proper identity-containing class-union
  sizes, and the Lagrange exclusion. Terminal entry: `PASS`.
- Row 2 (`Target-vanishing`) has `m_5=5`, `s=(12345)`, an explicit normalizer
  calculation on the six Sylow-5 subgroups, 2-transitivity, the invariant
  five-space, its endomorphism-algebra irreducibility proof, and
  `theta(s)=0`. Terminal entry: `PASS`.
- Row 3 (`CS-5`) now has a complete direct-power proof plus the divisor
  exhaustion. During self-audit I caught that the first draft's implicit claim
  that all distinct minimal normal images form one direct product was false in
  that generality (the three lines of `C_2^2` are the diagnostic). I replaced
  it before terminalization by the valid maximal-direct-subcollection argument:
  every further image either lies in the chosen product or centralizes it with
  trivial intersection and enlarges it. The characteristic closure is then the
  chosen direct product. Terminal entry after repair: `PASS`.
- Row 4 (`Aut-5`) reduces all nontrivial candidates to
  `C_2,C_2^2,C_3` and derives automorphism orders `1,6,2`. Terminal entry:
  `PASS`.
- Row 5 (`uniqueness`) gives the full order-60 Sylow and incidence proof,
  including both cyclic and Klein-four Sylow-2 cases. Terminal entry: `PASS`.

The integration was also expanded to state the simultaneous least-order
induction, both minimal-normal cases, the exact full-Sylow order, and the
prime-order Clifford noncancellation. The working dossier is
`scratch/a5-p5-hypothesis-closure.md`; the current `findings.md` records only
the fixed-target specialization. Controlling fields remain
`status/conjectured`, `witness_equals_target: false`, and
`active_assignment_answered: no`.

No mathematical computation, character table, classification theorem,
web/history, external source, or delegate was used. Filesystem-only inspection
used `nl`, `sed`, `rg`, `find`, `wc`, `date`, and `sha256sum`; their observed
outputs were only the displayed contents, filenames, line counts, UTC clocks,
and provisional file hashes. Two patch attempts failed before changing the
file (one context mismatch caused by JavaScript backslash handling and one
JavaScript template-literal syntax error caused by Markdown backticks); both
were immediately rerun with literal-safe patches and returned success.

## Resumed-branch outcome — PARTIAL_RESULT

- 2026-08-16T17:25:17Z — active work stopped; this resume used 20 active
  minutes, taking the shared ledger from 106/180 to 126/180. The remaining 54
  allocated minutes were not charged because the prescribed success certificate
  was complete; safety stop 2026-08-16T18:59:48Z was not approached.
- Strategy: `P-A5-5-HYPOTHESIS-CLOSURE`.
- Terminal observable: all five rows (`base`, `Target-vanishing`, `CS-5`,
  `Aut-5`, `uniqueness`) are explicit `PASS` entries in
  `scratch/a5-p5-hypothesis-closure.md`.
- Exact bounded conclusion: for every finite group `G`, if `|G|=60` and
  `V_o(G)=V_o(A_5)`, then `G` is isomorphic to `A_5`.
- Exact noncoverage: no arbitrary simple target `S`, no infinite family, and no
  answer to the universal scope. The final classification is therefore
  `PARTIAL_RESULT`, not `CLAIM`.
- Controlling status: `status/conjectured`, `witness_equals_target: false`,
  `active_assignment_answered: no`, `validator_status: pending`.
- Review routing:
  `Agents/Kourovka/bus/inbox/Validator/2026-08-16T172439Z__Problem-19.30__REPORT__a5-order60-special-case.md`
  and
  `Agents/Kourovka/bus/inbox/Lead/2026-08-16T172439Z__Problem-19.30__REPORT__a5-order60-special-case.md`.

Final observed artifact hashes:

```text
cdfd8d52cac882d59265e4142ab4fffa4c966c8d0debde9569b84d12e80ce5b0  Agents/Kourovka/problems/19.30/runs/2026-08-16T132009Z-proof/scratch/a5-p5-hypothesis-closure.md
82679f4156df5e20a9553b5a59d985f7e093ec9f1310acb68480e6a7f65f0ca7  Agents/Kourovka/problems/19.30/runs/2026-08-16T132009Z-proof/findings.md
```

Final filesystem audit output: both bus messages were present and had 30 and 29
lines respectively; the required constraint IDs each appeared in the dossier;
the placeholder/dependency search returned no matches. A requested `git status`
inspection failed with `fatal: not a git repository (or any parent up to mount
point /mnt)` and had no mathematical or file-state effect.

- 2026-08-16T17:26:30Z — post-stop administration: Lead's controlling
  `2026-08-16T165948Z__Lead__DECISION__a5-p5-hypothesis-closure.md` was marked
  `status: done` and moved from the Problem-19.30 inbox to `bus/archive/`.
  A read-only check found no remaining source copy and found the archived copy.
  This administrative interval was not charged as active research time.

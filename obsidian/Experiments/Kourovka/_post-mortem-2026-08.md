---
title: "Kourovka crew — campaign post-mortem, 2026-08-11 to 2026-08-18"
domain: group-theory
project: kourovka
status: baseline
author: maumayma
tags: [agent/lead, user/maumayma, domain/group-theory, topic/kourovka, topic/agent-design, project/kourovka, status/baseline]
---

# Kourovka crew — campaign post-mortem, 2026-08-11 → 2026-08-18

Sixteen problems opened. **Zero solved.** Zero counterexamples found. Zero reductions
certified.

The prompts used in this campaign came back **byte-identical** to the ones committed in
`d47e283`. Nothing was locally modified. So this is a clean test of the prompt design,
and the design failed. This note records why, in enough detail that the revisions are
traceable to evidence rather than to taste.

Source material: `Agents/Kourovka/` — 1304 bus messages, 263 board decisions, ~100 run
directories.

---

## The headline number

**Zero false positives. Zero true positives.**

The crew never once claimed something that turned out to be wrong at the top level.
That sounds like a win. It is the single most damning fact in the record.

[[_common-kourovka]] §0 said, in the version under test:

> The single most likely failure mode for this program is an agent convincing itself it
> has solved an open problem when it has not. … **A 47-problem "no result, honestly
> reported" run is a success.**

The crew read that and delivered exactly it — a 16-problem "no result, honestly
reported" run — and by the letter of its own charter that was a success. The whole
verification apparatus was calibrated against overclaiming, a failure mode that **never
occurred once in eight days**, while the actual failure mode — never producing a
candidate at all — was completely unmonitored.

A research process that never overclaims is a process that never reaches far enough to
be wrong.

---

## 1. Giving up was a first-class, pre-authorised move

Outcome vocabulary counts across the corpus:

| token | count |
|---|---|
| `PARTIAL_RESULT` | 750 |
| `REPORT: DEAD` | 273 |
| `STRATEGY_EXHAUSTED` | 252 |
| `hard kill` / `hard-kill` | 180 / 85 |
| `PARK_RECOMMENDED` | 82 |
| `OUT_OF_SCOPE_EXAMPLE` | 49 |

Five ways to stop, one way to continue. `PARK_RECOMMENDED` and `STRATEGY_EXHAUSTED`
are **not in any prompt** — the crew invented them at runtime, because the prompt gave
`REPORT: DEAD` first-class status and described it as *"The most common outcome and a
completely acceptable one."*

Worse, Lead's own dispatch template offered surrender as a menu item in the same
breath as the assignment
(`bus/archive/2026-08-17T075348Z__Lead__CORRECTION__21.137-route-balance.md`):

> "If neither direction meets the evidence gate, return `PARK_RECOMMENDED`."

### Time-to-abandonment was minutes

- **21.89** — `REPORT: DEAD` at **11 active minutes**, accepted by the board.
- **17.76**, **19.25** — `DEAD (already solved)` at **2 minutes** each.
- **21.137** — first `REPORT: DEAD` at **1 minute**.
- Median strategy lifetime inside 21.137's 65-entry `strategy_history`: **~12 minutes**.

### Budget was handed back unspent

The most diagnostic pattern in the whole record:

- `board/_decisions.md:865` — park 21.137 with **35 minutes unspent**
- `board/_decisions.md:940` — park 20.21 with **52 minutes unspent**
- 19.30 parked with **54 minutes unspent**
- 21.137 cycle 32 — **20 minutes returned**

A mathematician with a hard open problem and 33 free minutes does not return them. An
agent optimising for a clean ledger does.

---

## 2. The crew was a star topology with a saturated hub

| metric | value |
|---|---|
| messages involving Lead | **1014 / 1304 (77.8%)** |
| Lead-authored archive messages | 343 / 838 (41%) |
| messages addressed **to** Lead | 645 |
| …matching compute-lease keywords | **186 (29%)** |
| filenames containing "lease" or "slot" | **252 (~19% of all traffic)** |
| unread files in `bus/inbox/Lead/` | **336** |
| files in every problem-agent inbox | **0** |
| `Problem-X → Problem-Y` messages | **0** |

**One message in five was about permission to run code.** The cause is
[[_common-kourovka]] §4 as written: a compute slot was required for anything over
**60 s CPU**. That threshold is absurdly low for group theory.

The clearest instance — `bus/inbox/.../2026-08-17T211733Z__…__REQUEST__compute-slot-r0-exact-group.md`
requests a **180-second** run, with three SHA-256 hashes. **19 active minutes were
charged to write that request.** The bureaucracy cost 6× the compute it authorised.

Escalations that reached Lead as `BLOCKER` — the highest-severity type:

- a **YAML `author:` field** saying `operator`, which *halted validation of a
  mathematical claim* (`2026-08-11T163734Z__Validator__BLOCKER__author-placeholder-blocks-21-31-validation.md`)
- a **path-string mismatch**
- **ledger arithmetic** — whether an interval was 15 or 18 minutes
- a **typo**, which required a DECISION, a re-lease, and a SHA re-match

---

## 3. Attention was smeared, and this was enforced by rule

`board/_decisions.md:1601`:

> "The managed runtime permits exactly three subagents alongside Lead, so assign all
> three available lanes to **distinct** scopes: 21.137, 21.90, and 12.15."

This is the structural killer. The system had three units of parallel capacity and a
standing rule **forbidding** their concentration. Three simultaneous attacks on one
problem — one enumerating, one proving, one adversarially testing — was *illegal*.

Consequences:

- 21.137 reached **cycle 32** with **18 extensions**, meaning it was stopped and
  restarted 32 times, each restart paying context-reload cost against a 45-minute
  budget. Result: 65 shallow strategies, almost none surviving two cycles.
- Six problems (16.4, 17.76, 19.25, 20.55, 21.31, 21.89) have **zero run directories**.
  Selected, allocated, never actually worked.
- Peak dilution: **8 distinct problems touched in one day** (2026-08-17).

Meanwhile [[lead-kourovka]] instructed Lead to keep **8** problem agents alive and
listed *"letting the live-agent count drift below 8"* as forbidden.

---

## 4. Proof-first, against the prompt's own instruction

[[problem-agent-kourovka]] already said to try refutation second and proof *last*. It
was ignored, because Lead's scope files set `active_direction: proof` and the runtime
never checked.

Across ~100 run directories, **exactly two** are named for counterexample search:

```
problems/19.30/runs/2026-08-16-r1-counterexample/
problems/21.137/runs/2026-08-16-r2-odd-counterexample/
```

The human noticed. `scopes/21.137-odd-prime-exponent-p2.json`, `strategy_history` #28:

> "Human flags the direction imbalance: **72 of 267 official active minutes were
> counterexample-directed** despite the current 0.52 truth estimate."

At `truth_likelihood = 0.52` — a coin flip — the crew spent **73% of effort on proof**.

Lead's correction failed because of what it demanded of the counterexample lane:

> "It still needs a structurally new, non-wreath, non-UT7, non-NS3-repair finite
> object, an exact actual-power-set observable, a bounded row/object count, and a hard
> kill."

**That requires the agent to know the answer before it is allowed to look for it.** A
counterexample search is: enumerate, test, stop on failure. Requiring a
characterisation theorem as the entry gate to searching is proof work wearing a
counterexample label.

### 20.115 — the same disease, plus a known reduction ignored

Six consecutive runs, six simple-group families, hand-verified one at a time
(`r17-psl2q`, `r18-suzuki`, `r19-ree2g2`, `r20-pgl2q`, `r21-sl2q`, `r22-gl2q`) — a
strategy with **no termination condition**, since the family list is infinite. And at
cumulative minute 5 the staleness gate had already reported:

> "a May 2026 paper states the exact conjecture, reduces it to nearly simple groups,
> and proves many cases"

They knew the reduction existed and redid it by hand anyway.

### The one time they brute-forced, it took 31.8 seconds

`bus/archive/2026-08-17T100133Z__Problem-21.137__BLOCKER__order2187-layer-exhausted.md`:

> "completed every catalogue ID `1..9310` … `COMPLETE_SCAN=yes groups=9310 exp9=8302
> noncomm_cube_seed=0` … exited 0 after about **31.8 seconds**."

The full exhaustive scan of order 3⁷ — the obvious first move — happened on **day 7**,
after **three** BLOCKER rounds spanning ~3 hours of wall clock, and cost half a minute
of CPU.

---

## 5. Problem selection had no tractability model

`board/_longlist.md` carries reasoning for the problems it **rejected** and none for
the ones it **picked**. All 50 selected entries read:

| Position | Problem | Disposition | Screen note |
|---:|---|---|---|
| 1 | 21.3 | selected | `selected rank 1` |
| 2 | 21.4 | selected | `selected rank 2` |

There is no notion anywhere in the corpus of "this problem is easy" or "this is one
computation away". The only tractability review performed
(`2026-08-11T164500Z__Validator__REPORT__tractability-review-selected-fifty.md`)
assessed **tooling availability**, not difficulty.

What got selected instead: **named famous conjectures** — 16.4 (Arad–Herzog), 21.89
(MacHale, *already verified computationally to 2,000,000*), 21.31 (Byott), 20.55
(Mattarei). Prominence is inversely correlated with tractability.

**Three selected problems were already solved**, and nobody checked until runtime —
17.76 (starred as solved **in the source PDF itself**), 19.25, and 21.31, the last
after ~49 active minutes of order-2016 enumeration.

And the two problems that got real attention were both **human overrides of the crew's
own exclusion list** (`board/_decisions.md:51`). The selection process rejected the
only problems it later found worth working on.

---

## 6. The 21.137 failure, step by step

This is the one that matters, because a plain Codex session reportedly solved a
comparable problem in an hour by being told "find a counterexample".

**The problem has three clauses.** The third — *for a 2-group of exponent 8, if the
squares form a subgroup, must it be abelian?* — is the tractable one, and it has a
counterexample of order 128.

**Step 1 — they found it in one minute, then deleted it from scope.**
`board/_decisions.md:41`:

> "Problem-21.137 found … `21_137.lean` (2026-04-14), claiming that `D8 wr C2` has
> order 128 and exponent 8, with a square set that is closed but nonabelian.
> **Decision: stop the problem agent after one active minute.**"

`D₈ ≀ C₂`, order 128. That is the answer. It was classified `DEAD (already solved)`.

**Step 2 — the restart amputated the tractable clause.** A "discovery-blind" rerun was
ordered (`board/_decisions.md:185`), with the guardrail:

> "**21.137 guardrail: … Every p=2 example and the separate exponent-8 clause are
> excluded.**"

The clause with the cheap known answer was removed from the problem.

**Step 3 — they banned the *shape* of the answer, because of a filename.**
`board/_decisions.md:678`:

> "the fresh counterexample agent saw the historical name
> `independent_wreath_counterexample.g` **but did not open it**. That is still
> solution-direction information… **any wreath-shaped construction from this run cannot
> be counted as discovery-blind evidence.**"

Frozen into the scope JSON. Wreath products are *the* standard construction for
p-groups with prescribed power structure. Banning them is like banning induction.

**Step 4 — the agent derived the answer and refused to test it.** At cumulative minute
**937**:

> "The unique cheap repair … generates `Hom(F_3^2,F_3^3) ⋊ C_3` … **I derived it from
> the missing-label formula, but it is recognizably wreath-shaped.** … I will not
> describe any hit as clean discovery"

and immediately after:

> "The canonical full-translation action cover has all nine labels but is wreath-shaped
> and excluded from clean-discovery credit… **No target candidate exists**"

**The agent found a candidate, recognised it, declined to construct it, and reported
that no candidate existed.** The run died there, for a bookkeeping reason.

Final state: `cycle: 32`, `active_minutes_used: 937`, `extensions_granted: 18`,
`state: stopped`.

**Step 5 — they deliberately did not evaluate the property they were searching for.**
`2026-08-17T215217Z__…__REPORT__release-slot1-all27-zero-hits.md`:

> "**Noncommutativity gate: deliberately not evaluated for any class** because the
> leased guardrail requires it only after literal closure passes; printed value is
> `None` in every class."

A scan over 6561 candidate rows that did not check the target predicate.

### Why plain Codex wins this

Open GAP, iterate `SmallGroup(n,i)`, compute the power set, test closure and
commutativity, print the hit. One hour. No ledger, no lease, no purity rule, no scope
JSON, and **no rule against the answer being a wreath product**.

---

## 7. Tooling was never verified before commitment

- **SmallGroups order 2187 (3⁷) absent** — three BLOCKER rounds over ~3 hours.
- **ANUPQ absent** — the p-quotient machinery, i.e. *the* tool for generating p-groups
  of given exponent. Route hard-killed at minute 5.
- **GRAPE required sudo** — blocked 21.90 on day 1.
- Sage, Magma, KBMAG, HAP, cohomolo, nq, Lean: all absent.

Problems requiring these tools were selected anyway.

---

## 8. Ritual overhead

The **only** audit in the corpus
(`board/audits/2026-08-18T012944Z-21.137-four-hour-window-final-audit.md`) is 114 lines
verifying that fifteen time intervals sum to 240:

> `13+18+8+30+54+27+10+14+4+14+8+12+5+15+8=240`
> "**This is a scheduling and provenance finding, not a mathematical solution.**"

Zero lines verifying mathematics. The audit function was pointed at the ledger.

Similarly, `kourovka-state-check.py` reporting `0 error(s)` was treated as a progress
signal. The instrumentation measured **file hygiene**, and file hygiene was excellent.

Protocol v2 (adopted 2026-08-16, adding scope JSONs, admissibility gates, claim-check
files) **increased** message volume and Lead centralisation. The day after adoption is
the day of peak dilution.

Note also the trajectory of 21.137's runs: from `r7-alg3-ut7-cube-image` (an actual
group) to `r36-defect-root-fibre-conjugacy`, whose own audit line says it *"is not a
group, power map, or witness"*. **As budget was consumed the objects got less
concrete.** Under time pressure a working mathematician retreats to computation; this
crew retreated to formalism.

---

## 9. What changed as a result

Applied to the prompts in the same commit as this note:

| # | Change | Evidence |
|---|---|---|
| 1 | Delete "no result is a success" framing; mission is closing problems | §0 above |
| 2 | Terminal states cut to `SOLVED` / `REFUTED` / `STILL-TRYING`; `DEAD` demoted, `PARK` banned; unspent budget may not be returned | §1 |
| 3 | Compute lease abolished for local jobs under 10 min; `BLOCKER` restricted to "I cannot run the mathematics" | §2 |
| 4 | **Max 3 problems**, all lanes concentrated on one problem by default; no intra-cycle switching | §3 |
| 5 | Mandatory exhaustive enumeration **before** any theory; counterexample lane needs no preconditions; target predicate evaluated in the same pass | §4 |
| 6 | Selection requires written tractability score + **named first computation** + expected runtime; easiest-first ordering; tool check at selection | §5, §7 |
| 7 | **Novelty/purity rules banned outright.** No construction may be forbidden. Never amputate a tractable clause. Derived candidate must be built and tested immediately | §6 |
| 8 | Validator retargeted to mathematics only — no ledger audits, no metadata blocking, no editing claimants' files | §2, §8 |
| 9 | Per-problem write-up into `Experiments/Kourovka/<id>-<slug>/` made mandatory at close | this note's sibling structure |
| 10 | `rtk` adopted to cut tool-call token cost | operator request |

## Related

- [[_type]] — Kourovka experiment area hub
- [[_common-kourovka]] — the revised protocol
- [[problem-agent-kourovka]], [[lead-kourovka]], [[validator-kourovka]]
- [[kourovka-crew-setup]] — the runbook

---
title: "Problem 21.53 counterexample lane — M11 two-colour separator"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/coloured-graphs
  - project/kourovka
  - status/draft
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
direction: counterexample
strategy: M11-TWO-COLOUR-SEPARATOR
cycle: 10
---

# Run log

## 2026-08-18T04:37:03Z — active work start

- Official starting cumulative active minute: `123`.
- Increment cap: `45` new active minutes; the cycle must stop by cumulative minute `168`.
- Exact fixed target: the Mathieu group customarily denoted `M11`, but no identification, simplicity, order, involution-class, or prime-divisor fact is assumed until independently checked in this run.
- Strictness requires an explicit permutation preserving the exact order-2 and order-`p` relations while changing at least one other occurring exact product-order colour. Equality can only be a bounded fixed-pair partial result.
- I read the common and problem-agent protocols in full, canonical scope revision 2, the current problem roster and cumulative ledger, and the current inbox in the required order. I do not use unreviewed A7 or odd-PSL2 findings as mathematical premises.
- A STARTED/CHECKPOINT message was sent to Lead through the file bus.

## Source and staleness gate

The configured source PDF resolves. I rendered PDF page 172 and visually inspected
the displayed statement, including all subscripts and the intersection symbol. The
source-faithful transcription is:

> In the notation of 21.52, `Aut_t(Gamma)` is the set of permutations
> `tau in S_D` such that `(a,b)~(a^tau,b^tau)` whenever `|ab|=t` for
> `a,b in D`. Clearly `Aut(Gamma)=intersection_t Aut_t(Gamma)`. Is it true
> that for every finite simple group `G`,
> `Aut(Gamma)=Aut_2(Gamma) intersection Aut_p(Gamma)`, where `{2,p}` are
> the two minimal prime divisors of `|G|`?

Problem 21.52 supplies the inherited notation: `L` is finite nonabelian simple,
`D` is one conjugacy class of involutions, and the complete graph on `D` is
coloured exactly by product order. `source_transcription_checked: yes`.

The source entry is unstarred and has no printed editor or later comment. No
issue-21 JSONL corpus record is present from which separate `answered`,
`has_editor_comment`, and `has_later_comment` booleans can be read. Canonical
scope revision 2 records a passed independent source-fidelity audit. Because the
canonical record marks this run blind (`open_web: false`),
`external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`.

### Clause matrix

| source clause | active formulation | in scope? | stale-result coverage |
|---|---|---:|---|
| notation inherited from 21.52 | finite nonabelian simple `L`; one involution class `D`; complete exact product-order colouring | yes | no external result consulted in this blind lane |
| definition of `Aut_t` | one-way preservation of every `t`-edge; absent `t` is vacuous | yes | none |
| full group | intersection over all occurring exact product-order colours | yes | none |
| question | use `2` and the second-smallest distinct prime divisor `p` of `|L|` | yes | none |

`active_scope_checked: yes`. One strict fixed-M11 computation would refute the
universal assertion; fixed-pair equality would not prove it.

### Constraint checklist

| constraint_id | fixed-pair gate |
|---|---|
| `21.53-forall-L-D` | one admissible fixed pair refutes the universal assertion only if strict inequality is certified |
| `21.53-L-finite-nonabelian-simple` | reconstruct the selected group and check finiteness, nonabelianity, and simplicity |
| `21.53-D-single-involution-class` | inventory all involution classes and choose exactly one full conjugacy class |
| `21.53-Gamma-product-order-colouring` | compute `|ab|` for every unordered pair of distinct class elements |
| `21.53-Aut-t-definition` | use the one-way relation stabilizer, with absent labels vacuous |
| `21.53-two-minimal-primes` | factor the exact group order and select the smallest prime greater than `2` |
| `21.53-full-colour-group-definition` | preserve every occurring exact product-order relation separately |
| `21.53-two-colours-determine-all` | test equality; strictness additionally needs an explicit exhaustively checked separator |

The visually checked source and canonical record agree on all eight required rows.

## Strategy portfolio

1. **Catalogue/small-case — exact natural permutation model (rank 1).** Build the
   library's natural degree-11 Mathieu permutation group, verify its order and
   simple-group identification, inventory every involution class, and enumerate
   the complete product-order matrix on the selected class. A negative separator
   search proves only fixed-pair equality, never the universal assertion.
2. **Structured construction — relation twins/trades (rank 2).** If the order-2
   and order-3 relations have local twins or small interchangeable configurations,
   test the resulting explicit permutation against every relevant edge and seek a
   changed edge of another colour.
3. **Theoretical — recover the degree-11 action or Witt incidence (rank 3).** If
   the two relations reconstruct the natural 11-point action, sandwich their
   automorphism group between the natural group normalizer and a recoverable
   incidence structure. This can explain a bounded equality but not the universal
   source statement.
4. **Certificate plan.** Freeze one deterministic GAP/GRAPE script and manifest
   before execution. It must verify the group/class/prime gates, enumerate every
   pair, stop at the tautology gate when appropriate, compute the two-colour and
   full-colour automorphism groups through separately coloured incidence vertices,
   and either print one explicit separating permutation with exhaustive checks or
   print a containment-and-order equality certificate. The manifest must hash the
   script, require absent outputs, use an explicit timeout, reject nonempty stderr,
   and accept only a unique final sentinel. Lead must issue the compute-slot lease.

The cheapest certifiable route is this one gated exact computation: its inventory
stage precedes any automorphism call, and the script exits at the tautology gate if
there is no third occurring colour.

## 2026-08-18T04:37:55Z — source gate and portfolio complete; cumulative minute 124

No M11 mathematical output has yet been produced. The next charged step is to
freeze and statically audit the bounded checker and manifest, then request a Lead
lease before any GAP invocation.

## 2026-08-18T04:45:36Z — exact checker frozen; cumulative minute 131

The deterministic GAP/GRAPE checker and one-shot manifest are frozen before any
invocation. Checker SHA-256:
`9c45bf4eab82fd27afa41258bdc55a429baa8b73d6bb2e9fee5e86d3bdedb4e8`.
Manifest SHA-256:
`7ca40193fac3c54533539645343b26d8e0cc4c7220bd65a073e93a0ff0675241`.
All three version-1 output paths are absent.

Static inspection confirms that the checker defines the two explicit natural
degree-11 generators, checks group order/nonabelian simplicity/sharp
4-transitivity/finite-simple type, enumerates all involution classes, factors the
group order, and fills all `165 choose 2` matrix entries before the tautology
gate. The two incidence-graph calls use distinct vertex-colour cells for every
relation, restrict faithfully to class vertices, and audit every returned
generator against the stored matrix. A strict branch cannot terminate without an
explicit permutation image list, zero selected-relation failures, and a displayed
changed edge.

Requested one Lead compute slot for exactly one manifest invocation: one CPU,
estimated peak below 1 GiB, hard timeout 240 seconds, ten-minute portable lease,
and immediate release. Charged research pauses at cumulative minute 131 while the
lease is pending; no GAP invocation has occurred.

## 2026-08-18T04:46Z — static identification audit; cumulative minute 132

While the lease is pending, I inspected the installed GAP constructor source,
not any earlier 21.53 run. In GAP's installed `grp/basicprm.gi`, the
`MathieuGroupCons(IsPermGroup,11)` branch defines exactly the two generator
permutations frozen in the checker and records degree 11, size 7920, and
nonabelian simplicity. The checker does not call that constructor or inherit its
cached properties: it constructs `Group(generator1,generator2)` directly, then
computes the order, `IsSimpleGroup`, the full ordered-four-tuple orbit, and
`IsomorphismTypeInfoFiniteSimpleGroup`. The installed simple-group classifier
maps a simple group of computed order `2^4*3^2*5*11` to short name `M11`.

This source inspection verifies that the frozen explicit model is the installed
standard M11 model, while the eventual one-shot run still has independent
fail-fast checks for the properties used mathematically. No output path was
created and charged research pauses again at minute 132.

## 2026-08-18T04:49Z — independent installed-table cross-check; cumulative minute 133

As a second cheap static check, GAP's installed CtblLib `data/ctomathi.tbl.gz`
contains the `MOT("M11",...)` table record sourced there to the ATLAS. It records
group order 7920, ten conjugacy classes, centralizer-order sequence beginning
`[7920,48,18,8,5,6,8,8,11,11]`, and `isSimple=true`. In particular, its single
class with representative order 2 has centralizer order 48 and hence class size
`7920/48=165`, matching the checker gates. This is a static database cross-check,
not a substitute for the explicit permutation-group and all-elements checks in
the frozen run. No output path was created; charged work pauses at minute 133.

## 2026-08-18T04:50:09Z--04:52:36Z — sole v1 run fails; cumulative minute 136

Lead granted slot 1 after matching both frozen hashes and all absence gates. I
ran the exact manifest command once, without edits. The shell exited `1`; the
unique terminal sentinel and all later acceptance gates are absent. There will
be no v1 rerun.

GAP reached and printed only the preliminary explicit-group gates: version
4.12.1, GRAPE 4.9.0, the two frozen generators, computed order 7920,
`IsFinite=true`, `IsAbelian=false`, `IsSimpleGroup=true`, simple type `M11`,
degree 11, ordered-four-tuple orbit size 7920, prime divisors `[2,3,5,11]`, and
`p=3`. It then stopped before the involution inventory at the undefined symbol
`OnConjugation`. Therefore no class, product-colour, tautology, or automorphism
result exists from v1. Stderr also contains two parse-time unbound-global
warnings for GRAPE functions because `LoadPackage("grape")` occurs after their
helper-function definitions. Both defects must be repaired before any new run.

Observed artifacts:

- stdout: 398 bytes, SHA-256
  `083e77f9dab5bc673b73a3858b4ca696d22af3549bf62c28174f04d2f0f3cc47`;
- stderr: 550 bytes, SHA-256
  `c8badf15a76e631f56c19d1d9230e8e713aa6fbad523aa289e1745dc310178c5`;
- resource: 904 bytes, SHA-256
  `f18070d4b0b42d4f3e68de1e20bb267a12fe8e7a5fdd6a1d9107335dbc3517ee`.

Resource record: 1.47 user seconds, 0.38 system seconds, 0.97 wall seconds,
141,824 KiB maximum RSS, command exit status 1. Exact status:
`FAILED_RUN_NO_RESULT`. Slot 1 is released immediately at cumulative minute 136.
Any repair requires new output paths, checker and manifest hashes, and a fresh
Lead lease.

## 2026-08-18T04:53:17Z--04:56:41Z — authorized v2 refreeze; cumulative minute 140

Lead released slot 1, kept v1 as `FAILED_RUN_NO_RESULT`, and authorized only the
two compatibility repairs. Static inspection of GAP's conjugacy-class machinery
shows that `OnPoints` is the registered action implementing `d^g`; no probe
invocation was run without a slot.

Version 2 moves `LoadPackage("grape")` before helper bodies that reference GRAPE
globals and replaces exactly the two undefined `OnConjugation` tokens by
`OnPoints`. The only additional operational change is the required v2 terminal
sentinel and wholly new v2 output paths. A literal diff confirms every
mathematical gate is otherwise unchanged.

Frozen checker SHA-256:
`77dfad03e67756968d2cb2438dcfdf0ec5a46605b81c2f374ec49031b5c500c2`.
Frozen manifest SHA-256:
`ff8258588f8f65b8a1b9a3b8e74011bb704238cfe825de812b92f68a394997ed`.
All three v2 output paths are absent. Request one new slot for the same one-CPU,
below-1-GiB, 240-second-capped command and immediate release. Charged work pauses
at cumulative minute 140; no v2 invocation has occurred.

## 2026-08-18T04:58:33Z--05:00:27Z — sole v2 run rejected by stderr gate; cumulative minute 142

Lead matched the v2 hashes and absence gates and granted slot 1. I ran the exact
frozen command once, without edits. GAP itself exited zero and reached the unique
terminal sentinel, but the manifest shell exited `1` because stderr is nonempty:
one parse-time warning says global `expectedValency` is unbound where a closure
captures it. Consequently v2 is `FAILED_RUN_NO_RESULT`; there will be no v2
rerun, and the following stdout is diagnostic only, not an accepted mathematical
result.

The diagnostic prefix is nevertheless precise about where the next run should
resume. It reports the explicit group has order 7920, is finite, nonabelian and
simple, has simple type `M11`, natural degree 11, and ordered-four-tuple orbit
size 7920. Its distinct prime divisors are `[2,3,5,11]`, so `p=3`. It reports ten
conjugacy classes, exactly one involution class, size 165 with centralizer order
48. All 13,530 unordered pairs were inventoried, with occurring exact colours
`[2,3,4,5,6]`, edge counts `[990,2640,1980,3960,3960]`, and valencies
`[12,32,24,48,48]`; hence the tautology gate passed. The diagnostic comparison
reports both restricted groups have order 7920, mutual containment, zero returned-
generator audit failures, containment of the natural conjugation action, and
`COMPARISON=EQUALITY`. None of these v2 mathematical lines is promoted to a
cycle result because the frozen empty-stderr acceptance gate failed.

Observed artifacts:

- stdout: 66,445 bytes, SHA-256
  `972e3351a68266d11bd861904417fbf4ad379554e61e6c5bef468e32faa075a4`;
- stderr: 263 bytes, SHA-256
  `66599c713a648cddf8d087df040e352acad457a29f2506b2fdb85d03752994c5`;
- resource: 870 bytes, SHA-256
  `03d3dd0be14284c31585d36e9f0cb6aacbe1f31f472d247104b668ab6c3f220a`.

Resource record: 8.22 user seconds, 0.53 system seconds, 9.71 wall seconds,
142,080 KiB maximum RSS, GAP/timeout exit status zero. The outer manifest status
is one. Slot 1 is released immediately. A v3 would need a single compatibility
repair that binds `expectedValency` before GAP parses the closure, plus new
output paths, hashes, sentinel, manifest, and lease; no rerun is attempted here.

## 2026-08-18T05:04:00Z--05:05:54Z — authorized v3 refreeze; cumulative minute 144

Lead released slot 1, retained v2 as `FAILED_RUN_NO_RESULT`, and authorized the
single pre-parse binding repair. Version 3 adds exactly the separate statement
`expectedValency := fail;` before the unchanged regularity loop, then uses new
v3 output paths and terminal sentinel. A literal v2-to-v3 diff shows no other
mathematical or algorithmic change.

Frozen checker SHA-256:
`f5da7d297c349c7a1709fd5e5cebf7fca7a1ba2407997ead1697298c7b576f28`.
Frozen manifest SHA-256:
`876f34f3439566ddae815887e7c9df7d7b586ff92c5e1eced475d1f1ca583aa3`.
All three v3 output paths are absent. Request one fresh slot for the same
one-CPU, below-1-GiB, 240-second-capped command, with immediate release. Charged
work pauses at cumulative minute 144; no v3 invocation has occurred.

## 2026-08-18T05:08:17Z--05:10:18Z — leased v3 run passes; cumulative minute 146

Lead matched both v3 hashes and all absence gates, then granted slot 1. I ran the
exact frozen manifest command once, without edits. Every acceptance gate passes:
shell exit zero; GAP/timeout exit zero; stderr empty; nonempty resource record;
all group/class/prime/colour/comparison tags present; the final stdout line is
exactly the unique sentinel
`FINAL_SUCCESS_SENTINEL=M11_TWO_COLOUR_CHECK_V3_PASS` and occurs once.

Accepted exact output:

- GAP 4.12.1, GRAPE 4.9.0;
- the explicit degree-11 group generated by
  `(1,2,3,4,5,6,7,8,9,10,11)` and `(3,7,11,8)(4,10,5,6)` has order 7920,
  is finite, nonabelian and simple, is identified as finite-simple type `M11`,
  and has an orbit of all `11*10*9*8=7920` ordered distinct four-tuples;
- the distinct prime divisors are `[2,3,5,11]`, hence the second-smallest is
  exactly `p=3`;
- among ten conjugacy classes there is exactly one involution class `D`; it has
  size 165, its displayed representative is
  `(4,10)(5,8)(6,7)(9,11)`, and its centralizer has order 48; an all-elements
  check also identifies `D` with the complete set of nonidentity involutions;
- all 13,530 unordered distinct pairs were evaluated. The exact occurring
  product-order colours are `[2,3,4,5,6]`, with edge counts
  `[990,2640,1980,3960,3960]` and valencies `[12,32,24,48,48]` in that order;
  all 165 matrix rows are preserved in stdout;
- the tautology gate passes because colours `4,5,6` occur;
- the order-2/order-3 incidence graph has 3,795 vertices and 7,260 edges; its
  automorphism group restricts faithfully to a group of order 7,920 on `D`, and
  all four returned generators have zero selected-relation audit failures;
- the all-five-colour incidence graph has 13,695 vertices and 27,060 edges; its
  automorphism group restricts faithfully to a group of order 7,920 on `D`, and
  all four returned generators have zero exact-colour audit failures;
- the natural M11 conjugation action has order 7,920 and lies in the full-colour
  group; the full-colour group lies in the two-colour group, and the two-colour
  group lies in the full-colour group. Thus the exact fixed-pair comparison is
  `EQUALITY`.

Artifact hashes:

- stdout: 66,445 bytes, SHA-256
  `7d6f5778c49232bd608dde20b52e2e33627d2e2bb95cfaed05996fe61c9e4e41`;
- empty stderr: SHA-256
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`;
- resource: 866 bytes, SHA-256
  `bf1d1f6487461a0cdf3a9eb4390c4eb9c03bfb96c3a87adf65ea94150a438669`.

Resource use: 7.83 user seconds, 0.48 system seconds, 7.64 wall seconds,
142,208 KiB maximum RSS, exit status zero. Slot 1 is released immediately.

This is exact bounded equality for the single admissible pair `(M11,D)`. It is
not a separator and not a universal inference. The fixed strategy has reached
its equality stop criterion; package `PARTIAL_RESULT` and enter
`awaiting_lead` after routing the finite determination for independent review.

## 2026-08-18T05:10:34Z--05:12:58Z — PARTIAL_RESULT packaged; cumulative minute 149

Lead independently matched the accepted output hashes and released slot 1.
`findings.md` now records the exact fixed-pair result, all eight canonical scope
rows, group/class/prime gates, complete colour inventory, incidence-lift argument,
mutual containment and natural-action sandwich, frozen hashes, failed-run
provenance, and limitations. Findings SHA-256:
`889005e3678d765d45067008b7e763f78b93da4ea180be485818de430aa352f4`.

Cycle outcome: `PARTIAL_RESULT`. The fixed `M11-TWO-COLOUR-SEPARATOR` strategy
has no separator because the exact groups are equal. The universal scope remains
open with `active_assignment_answered:no`; no claim-check file is warranted.
Route the fixed-pair determination for fresh independent reconstruction and ask
Lead/MathExpert to select any materially different continuation. This context
does not choose another group or strategy.

Exact charged increment: 26 active minutes, cumulative `123--149`. Return 19
unused minutes from the 45-minute cap. The 30-minute self-check threshold was not
reached. State: `awaiting_lead`.

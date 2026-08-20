---
title: "Problem 21.53 counterexample lane — A7 two-colour separator"
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
strategy: A7-TWO-COLOUR-SEPARATOR
---

# Run log

## 2026-08-18T04:07:15Z — active work start

- Official starting cumulative active minute: `106`.
- Increment cap: `45` active minutes; safety stop: `2026-08-18T05:04:12Z`.
- Exact fixed target: `L=A_7`, with `D` its class of double transpositions.  The
  lane asks whether the exact product-order colouring has
  `Aut(Gamma)=Aut_2(Gamma) intersect Aut_3(Gamma)`; strict inequality requires an
  explicit separating permutation with exhaustive relation checks.
- I read the common and problem-agent protocols in full, then scope revision 2,
  the permitted synthesis, and the current counterexample decision.  I did not
  inspect the unreviewed odd-`PSL_2` coherent-closure partial.

## Source and staleness gate

The configured source PDF resolves.  I rendered and visually inspected PDF page
172, not merely its extracted text.  The source-faithful transcription is:

> In the notation of 21.52, let `Aut_t(Gamma)` be the set of permutations
> `tau in S_D` such that `(a,b)~(a^tau,b^tau)` whenever `|ab|=t` for `a,b in D`.
> Clearly, `Aut(Gamma)=intersection_t Aut_t(Gamma)`.  Is it true that for every
> finite simple group `G` we have
> `Aut(Gamma)=Aut_2(Gamma) intersection Aut_p(Gamma)`, where `{2,p}` are the two
> minimal prime divisors of `|G|`?

Problem 21.52 supplies the inherited notation: `L` is finite nonabelian simple,
`D` is one conjugacy class of involutions, and the complete graph on `D` is
coloured exactly by `|ab|`.  Visual inspection confirms the subscripts, the
intersection over all `t`, the universal group quantifier, and the two minimal
prime divisors.  `source_transcription_checked: yes`.

The source entry is unstarred and has no printed editor or later comment.  This
vault has no issue-21 JSONL corpus record from which to read separate boolean
flags; the current source PDF and synthesis record no answer.  Scope revision 2
has already passed an independent source-fidelity audit.  Because the canonical
record marks this run blind (`open_web: false`), the external search is recorded
as `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`.

### Clause matrix

| source clause | active formulation | in scope? | stale-result coverage |
|---|---|---:|---|
| notation inherited from 21.52 | finite nonabelian simple `L`; one involution class `D`; complete exact product-order colouring | yes | no external result consulted in this blind lane |
| definition of `Aut_t` | one-way preservation of every `t`-edge; absent `t` is vacuous | yes | none |
| full group | intersection over every occurring exact product-order colour | yes | none |
| question | use primes `2` and the second-smallest distinct divisor `p` of `|L|` | yes | none |

`active_scope_checked: yes`; the fixed `A_7` calculation can only supply a
counterexample if strict, or a bounded equality if not strict.  It cannot prove
the universal assertion.

### Constraint checklist

| constraint_id | fixed-pair use |
|---|---|
| `21.53-forall-L-D` | one admissible fixed pair refutes the universal statement only if strict inequality is certified |
| `21.53-L-finite-nonabelian-simple` | check `A_7` is finite, nonabelian, simple |
| `21.53-D-single-involution-class` | check the double transpositions are exactly one `A_7` conjugacy class of order-2 elements |
| `21.53-Gamma-product-order-colouring` | compute `|ab|` for every unordered distinct pair in that class |
| `21.53-Aut-t-definition` | use the one-way relation stabilizer, including vacuous absent colours |
| `21.53-two-minimal-primes` | factor `|A_7|` and verify `p=3` |
| `21.53-full-colour-group-definition` | intersect the stabilizers of every occurring colour |
| `21.53-two-colours-determine-all` | test equality; for a counterexample, exhibit and exhaustively check a violating permutation |

The scope record and visually checked source agree on all required rows.

## Strategy portfolio

1. **Catalogue/small-case — fixed exact `A_7` incidence model (rank 1).** Encode
   all 105 double transpositions as two-edge matchings on seven points, enumerate
   all 5,460 unordered pairs, and inventory exact product orders.  A positive
   equality proves only this fixed-pair statement; strict inequality plus a
   separator refutes the universal assertion.
2. **Structured construction — relation twins/trades (rank 2).** Search within
   the matching geometry for vertices or small configurations interchangeable
   under the order-2 and order-3 relations but separated by an order-4, -5, or -6
   relation.  Any candidate permutation is checked on every relevant edge.
3. **Theoretical — reconstruct seven underlying points (rank 3).** Determine
   whether maximal or common-neighbour structures in `R_2,R_3` recover the
   natural `S_7` action; if so, derive fixed-pair equality without inferring the
   universal statement.
4. **Certificate plan.** Freeze a deterministic checker that independently
   reconstructs `A_7` as even permutations, its class, the full product-order
   matrix, and any proposed permutation.  For strictness it prints exhaustive
   preservation counts for every 2- and 3-edge and one changed other-colour edge.
   If exact automorphism-group computation is needed, freeze/hash a bounded GAP
   or nauty input plus resource estimates and request a Lead lease before running.

The cheapest certifiable first gate is the complete colour inventory.  If only
colours 2 and 3 occur, equality is tautological and the lane stops; otherwise the
fixed automorphism comparison remains live.

## 2026-08-18T04:12:35Z — exact fixed-pair inventory; cumulative minute 111

Hand reconstruction gives `|A_7|=7!/2=2520=2^3*3^2*5*7`, hence the
second-smallest distinct prime is `p=3`.  The theorem that `A_n` is nonabelian
simple for `n>=5` supplies simplicity.  An order-two element of `A_7` must have
an even positive number of disjoint transpositions; on seven points this forces
cycle type `2^2 1^3`.  That `S_7` class does not split in `A_7` (its cycle type is
not a list of distinct odd lengths), so the double transpositions form the one
involution class.  Its size is
`7!/(2^2 2! 3!)=105`, equivalently `2520/24=105`.

A bespoke independent tuple-permutation checker, frozen at SHA-256
`3974349af9ac2edbb1c73f4ac3ab034d39d92762931f2010fa2df03109c392bb`,
enumerated all 5,040 permutations on seven points, all 2,520 even ones, and all
5,460 unordered pairs in the 105-element class.  Command:

```bash
/usr/bin/time -f 'ELAPSED=%e MAX_RSS_KB=%M EXIT=%x' python3 Agents/Kourovka/problems/21.53/runs/2026-08-18-r9-a7-two-colour-separator/a7_inventory.py
```

Observed output: the nonidentity involutions and the explicit
double-transposition model are the same 105-element set; the full conjugacy orbit
has size 105; exact colour edge counts are
`2:420, 3:1890, 4:1260, 5:1260, 6:630`, with common valencies
`8,36,24,24,12`.  The upper-triangle product-order digest is
`4d3fe83103fe078db14711e68a7932fa2e30428ae5f69c08ef69bf812fdcfcfa`.
Runtime was 0.14 seconds, maximum RSS 14,848 KiB, exit zero.

Thus the tautology stop does **not** fire: three colours other than 2 and 3
occur.  I froze the bounded exact GRAPE/nauty comparison and manifest before any
permutation-group computation.  Checker SHA-256:
`88518186a09612fe9730f6628b07b4f2733326e74eb64443f72077dc70e8b444`;
manifest SHA-256:
`3133a91122e8d0cd06e1ae8fa8093e5b5d6c14c0ecfe8163193274a3e8390fff`.
The requested command has a 90-second hard timeout, one-CPU/under-512-MiB
estimate, and a five-minute lease request.  Charged research stops while awaiting
that lease.

## 2026-08-18T04:15:55Z — cheap local work resumes at cumulative minute 111

While the heavy-job lease is pending, test the smallest structured-construction
possibility: a transposition of two class vertices having identical order-2 and
order-3 incidence to every other vertex.  This is bounded and does not invoke a
general automorphism solver.

## 2026-08-18T04:16:25Z — twin probe stops; cumulative minute 112

The exact probe checked all 5,460 transpositions of class vertices and found no
pair with identical order-2 and order-3 incidences to all remaining vertices.
Script SHA-256
`1fee9026cfceb08ab37acd1d6c21bb4fb2466314a2ebf7b2fa5464d87dd59d87`;
runtime 0.22 seconds, maximum RSS 14,592 KiB, exit zero.  Thus the cheapest
support-two separator does not exist.  This rules out only vertex transpositions,
not larger-support relation automorphisms.  Charged work pauses again pending the
leased exact comparison.

## 2026-08-18T04:17:09Z — Lead correction; work resumes at cumulative minute 112

Lead rejected the first lease without allocating a slot: require the explicit
documented GRAPE call `AutGroupGraph(graph, colourclasses)` and freeze the entire
`/usr/bin/time -v` wrapper plus every redirection as one command.  No rejected
checker invocation occurred.  Patch only those interface/manifest defects, use
new output names, refreeze, and resubmit.

## 2026-08-18T04:17:43Z — corrected freeze; cumulative minute 113

Static inspection confirms both calls now use the documented two-argument GRAPE
signature.  The manifest contains one complete command, including `/usr/bin/time
-v`, 90-second timeout, GAP batch flags, and distinct stdout/stderr/resource
paths.  All three version-2 output paths are absent.  Fresh checker SHA-256:
`c530735cb42facec94cdebfcc9fe5d5652363d8d81296b5a9266eb4d7a2d8b07`;
fresh manifest SHA-256:
`161a85f6c1d586bc660648e5aee3442af237fc4619e46fc2ac9ab4bf556aceca`.
Charged work pauses at cumulative minute 113 pending a new lease.

## 2026-08-18T04:18Z — pre-lease static audit catches GAP range defect

Before any response or invocation, static inspection caught that GAP interprets
`[n+1..n]` as a descending range rather than an empty range.  The unordered-pair
loops therefore need the explicit outer bound `[1..n-1]`.  Patch all four such
loops, switch all outputs to never-used version-3 names, refreeze, and supersede
the version-2 request.  No version-2 output was created and no computation ran.

## 2026-08-18T04:19:44Z — version-3 freeze; cumulative minute 116

All unordered-pair loops now use the safe bounds; the remaining `[1..n]` loops
only set the diagonal or print the vertex table.  Fresh checker SHA-256:
`9b45ae67fe0aa91d45b75422c4c5852ee3618d573f6a5d0be044e697d08a6289`;
fresh manifest SHA-256:
`cf476ed9a011dc475ce56eacdd168af33ceeae03b3939df71a225678fb5f500a`.
All three version-3 output paths are absent.  Charged work pauses at cumulative
minute 116 pending the superseding request.

## 2026-08-18T04:20:50Z--04:21:23Z — hand colour inventory; cumulative minute 117

View a double transposition as a two-edge matching on seven points.  For two
distinct matchings, their union decomposes into alternating paths/cycles; on an
alternating path of `k` edges the product has a `(k+1)`-cycle, while an
alternating 4-cycle gives two transpositions.  With one common edge, the two
remaining edges are either disjoint (order 2) or meet (order 3).  With no common
edge the possible component types and orders are exactly
`C4 -> 2`, `P2+P2 -> 3`, `P3+P1 -> 4`, `P4 -> 5`, and
`P2+P1+P1 -> 6`.

For a fixed matching, the one-common-edge cases contribute `6` neighbours of
order 2 and `12` of order 3.  The no-common-edge cases contribute respectively
`2,24,24,24,12` neighbours for orders `2,3,4,5,6`.  Thus the hand valencies are
`8,36,24,24,12`, independently reproducing the checker and yielding edge counts
after multiplication by `105/2`.  Charged work pauses again at minute 117.

## 2026-08-18T04:21:24Z--04:22:16Z — leased v3 run fails before graph construction; cumulative minute 118

Slot 1 was granted for exactly one invocation, and I ran the frozen manifest
command once without edits.  The wrapper returned exit code zero because GAP
entered its recoverable error loop, but stderr is decisive: line 11 attempted
`Sort(D)` on the immutable list returned by `AsList(ConjugacyClass(...))`.
Therefore no graph was constructed and no automorphism result exists.

Observed files and SHA-256 digests:

- stdout: 90 bytes,
  `f9b82c671854ab2d01da22ec2962cc8cd8f7480e6e9b65fb480f1001a0b35c1a`;
- stderr: 404 bytes,
  `857f298f78df3327da18866554bd7a76d90d9a1c77b2d1f8b3217c1e0348c356`;
- resource: 834 bytes,
  `c664f2029991d35be9d01359ad2afa0af8a4160fc7701e935554aa8825291148`.

Resource record: 1.06 user seconds, 0.30 system seconds, 0.15 wall seconds,
141,824 KiB maximum RSS, wrapper exit status zero.  The exact mathematical
status is `FAILED_RUN_NO_RESULT`, not a positive computation.  Slot 1 is released
immediately.  A repair would require at least a mutable copy before sorting and
a fail-fast GAP wrapper; neither is patched or rerun without a new Lead decision.
Charged work stops at cumulative minute 118.

## 2026-08-18T04:24:16Z — authorized v4 refreeze begins at cumulative minute 118

Lead released slot 1 and authorized only a mutable-copy, fail-fast refreeze.
Make the conjugacy-class list mutable before sorting; add a unique terminal
success sentinel; add GAP `--quitonbreak`, empty-stderr, and exact final-line
gates to the single manifest command; and move to never-used version-4 paths.

## 2026-08-18T04:25:05Z — version-4 freeze; cumulative minute 119

Static inspection confirms `ShallowCopy` precedes `Sort`, the unique terminal
sentinel is the final checker output, and the exact command enforces
`--quitonbreak`, empty stderr, and an exact final-line match.  Fresh checker
SHA-256:
`ccd5087fe6d4bf47d624800e61bd8c2e0dd28ae94eae6a6521eddbc8fc08ff39`;
manifest SHA-256:
`1cf891e9debdaa90f99ce8396afeaaac3b33823ff7fc3bb4a31e1215a1f35c1d`.
All three version-4 output paths are absent.  Charged work pauses at cumulative
minute 119 pending a fresh lease.

## 2026-08-18T04:29:29Z--04:30:37Z — leased v4 comparison passes; cumulative minute 121

Lead granted slot 1 and I ran the exact frozen version-4 command once without
edits.  Every acceptance gate passes: shell exit zero; resource exit zero;
stderr empty; final stdout line exactly
`FINAL_SUCCESS_SENTINEL=A7_TWO_COLOUR_CHECK_V4_PASS`; required inventory,
group, generator-audit, and comparison tags all present.

Exact output:

- GAP 4.12.1, GRAPE 4.9.0;
- `A_7` order 2520, `IsSimpleGroup=true`, unique 105-element nonidentity
  involution class represented by `(1,2)(3,4)`, `p=3`;
- colours and edge counts `2:420, 3:1890, 4:1260, 5:1260, 6:630`;
- two-colour incidence gadget order 2,415, automorphism group order 5,040,
  faithful restriction to the 105 class vertices;
- full-colour incidence gadget order 5,565, automorphism group order 5,040,
  faithful restriction, and full group contained in the two-colour group;
- natural `S_7` conjugation action has order 5,040 and lies in the full group;
- all six returned two-colour generators exhaustively preserve all 420 order-2
  edges and all 1,890 order-3 edges with zero failures; all seven full-group
  generators preserve every one of the 5,460 exact colours;
- `COMPARISON=EQUALITY`.

Output SHA-256 digests: stdout
`9c9acecd3f65a450af9868867ca19086b77bafc26c215b55dbdd77b58b2a444d`
(2,605 bytes), empty stderr
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`,
resource
`4c724a56b63a03ca7a9d39d21c9a82d2e61d8e690a4d153da5dba0655cc0a300`
(852 bytes).  Resource use: 11.54 user seconds, 0.52 system seconds, 12.62
wall seconds, 142,336 KiB maximum RSS.

Slot 1 is released immediately.  This is an exact bounded equality for the one
pair `(A_7,D)`, not a counterexample and not evidence that answers the universal
scope.  The named `A7-TWO-COLOUR-SEPARATOR` strategy therefore meets its stop
criterion; package the bounded partial and enter `awaiting_lead`.

## 2026-08-18T04:30:38Z--04:32:42Z — outcome packaged; cumulative minute 123

Cycle outcome: `PARTIAL_RESULT`.  The linked `findings.md` records the complete
fixed-pair determination, every scope row, hand matching-geometry inventory,
exact group comparison, natural-`S_7` sandwich, file hashes, acceptance gates,
and limitations.  Findings SHA-256:
`74bb9c6be376ef5f0617eb6115791de9628f2502b212bff8d1e54c7390eaf4ce`.

This lane used 17 active minutes (`106--123`) of its 45-minute increment.  The
30-minute self-check threshold was not reached.  Research stops early because
the exact equality fires the fixed-target stop criterion.  State:
`awaiting_lead`; no new target or method begins without an explicit Lead
decision.

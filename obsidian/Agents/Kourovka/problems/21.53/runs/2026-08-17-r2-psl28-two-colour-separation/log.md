---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/graph-automorphisms
  - project/kourovka
  - status/draft
---

# Problem 21.53 — fresh PSL(2,8) two-colour lane

Scope: `21.53/two-minimal-prime-colours`  
Assignment revision: 2  
Direction: counterexample  
Run directory: `Agents/Kourovka/problems/21.53/runs/2026-08-17-r2-psl28-two-colour-separation`

## Active-time ledger

- `2026-08-17T19:24:51Z` — research start at cumulative active minute 14. Fresh PSL(2,8)-only decision received; hard allowance is 45 further active minutes.

## 2026-08-17T19:28:20Z — source, scope, and staleness gate

I inspected rendered PDF page 172, not only the text extraction. The displayed source says:

> In the notation of 21.52, let \(\operatorname{Aut}_t(\Gamma)\) be the set of permutations \(\tau\in S_D\) such that \((a,b)\sim(a^\tau,b^\tau)\) whenever \(|ab|=t\) for \(a,b\in D\). Clearly, \(\operatorname{Aut}(\Gamma)=\bigcap_t\operatorname{Aut}_t(\Gamma)\). Is it true that for every finite simple group \(G\) we have \(\operatorname{Aut}(\Gamma)=\operatorname{Aut}_2(\Gamma)\cap\operatorname{Aut}_p(\Gamma)\), where \(\{2,p\}\) are the two minimal prime divisors of \(|G|\)?

The inherited notation on the same rendered page specifies that the group is finite non-abelian simple, that `D` is one conjugacy class of involutions, that `Gamma` is complete on `D`, and that two edges have the same colour exactly when their endpoint products have equal order. This matches every row of canonical revision 2. In particular:

- `Aut_t` is defined for every positive integer `t`, not merely for occurring colours. If there is no `t`-edge, its implication has empty premise and `Aut_t=S_D` vacuously.
- The full coloured automorphism group is the intersection over all product-order colours.
- The primes are the two smallest *distinct* prime divisors. For an even simple group they are `2` and the least prime divisor greater than `2`.
- Only one involution conjugacy class is used; no union of classes is admissible.

`source_transcription_checked: yes`  
`active_scope_checked: yes`  
`external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`

The vault contains only the issue-20 corpus JSONL, not an issue-21 corpus record, so the requested corpus booleans `answered`, `has_editor_comment`, and `has_later_comment` are unavailable here. The rendered issue-21 page itself contains no editor or later comment attached to 21.53. The canonical source record says the statement was Lead-checked and independently scope-audited. I did not inspect any solution-bearing 21.52 material and did not use open-web search.

### Clause matrix

| source clause | equivalent formulation | active? | external-result status |
|---|---|---:|---|
| inherited 21.52 notation | finite non-abelian simple `L`; one involution class `D`; complete graph; colour `{a,b}` is exactly `order(ab)` | yes | blind run; deferred |
| definition of `Aut_t` | permutations carrying every `t`-edge to a `t`-edge; nonoccurring `t` is vacuous | yes | blind run; deferred |
| `Aut(Gamma)=intersection_t Aut_t(Gamma)` | preserve every occurring product-order relation | yes | definitional |
| two-minimal-prime question | test equality with `Aut_2 intersect Aut_p`, where `p` is the next distinct prime after `2` in `|L|` | yes | blind run; deferred |

### Admissibility checklist for the fixed probe

| constraint id | required check for `L=PSL(2,8)` |
|---|---|
| `21.53-forall-L-D` | A fixed pair can refute the universal assertion if it separates; equality is bounded evidence only. |
| `21.53-L-finite-nonabelian-simple` | Reconstruct the 504-element group and invoke the classical simplicity theorem for `PSL(2,q)`, `q>3`. |
| `21.53-D-single-involution-class` | Enumerate all nonidentity involutions and compare them with one full conjugacy orbit. |
| `21.53-Gamma-product-order-colouring` | Enumerate every unordered distinct pair and compute the exact order of its product. |
| `21.53-Aut-t-definition` | Preserve the implication definition, including vacuity for absent labels, in every later incidence test. |
| `21.53-two-minimal-primes` | Factor `504=2^3*3^2*7`, so `p=3`. |
| `21.53-full-colour-group-definition` | Later full group must preserve every occurring product-order incidence relation. |
| `21.53-two-colours-determine-all` | Strict inequality needs one explicit permutation checked on every 2/3 edge and one changed other-colour edge. Equality is not universal evidence. |

## Strategy portfolio

Ranked by information per active minute:

1. **Exact fixed-pair catalogue probe.** Build `GF(8)=F_2[x]/(x^3+x+1)`, enumerate `SL(2,8)=PSL(2,8)`, the full involution class, and all 1,953 unordered pair products. First output is the colour set and uniform valency profile. A negative separation result says only that this one pair is not a counterexample.
2. **Coloured-incidence comparison.** If four or more colours occur, encode the 2- and 3-relations together and compare their colour-preserving permutation group with the group preserving every relation. This is frozen and leased before it runs.
3. **Structured geometry.** Interpret involutions through their unique fixed points on `P^1(F_8)` and the root groups of order eight. Try to recover the other relations structurally from the 2/3 incidence; this is particularly useful if the exact groups are equal.
4. **Theoretical/tautology gate.** With at most three occurring colours, preservation of two relations forces the complement relation, giving equality immediately (including careful treatment of absent 2 or 3 colours).

Certificate plan: store the complete 63-by-63 product-order matrix (equivalently all 1,953 labelled unordered edges), the field/group/class reconstruction data, and all hashes. For strict inequality, store an explicit vertex permutation and independently loop through every 2-edge and every 3-edge, then exhibit one precise edge whose other colour changes. Validator can rebuild the field independently from the multiplication polynomial and check the permutation without trusting any automorphism-group package.

## 2026-08-17T19:35:14Z — exact field, group, class, and complete colour profile

Frozen cheap-model manifest: `scratch/model-run-manifest.md`.  
Program SHA-256: `f75ad5500924cef6164fc651273ac69d23be87b0ff8c678c28366055177c81ea`.  
Exact command (from this run directory):

`timeout 30s python3 scratch/build_psl28_scheme.py scratch/psl28-product-scheme.json`

Observed exit code: `0`. Observed wall time: `1.125061651` seconds. Verbatim stdout:

```json
{
  "centralizer_size": 8,
  "colours": [
    2,
    3,
    7,
    9
  ],
  "edge_count": 1953,
  "edge_counts": {
    "2": 189,
    "3": 252,
    "7": 756,
    "9": 756
  },
  "factorization": {
    "2": 3,
    "3": 2,
    "7": 1
  },
  "group_order": 504,
  "involution_count": 63,
  "orbit_equals_all_involutions": true,
  "output": "scratch/psl28-product-scheme.json",
  "second_smallest_distinct_prime": 3,
  "valencies": {
    "2": 6,
    "3": 8,
    "7": 24,
    "9": 24
  }
}
```

Output SHA-256: `54bb450db146199b72e51b2e18b4b2b507075d50725cc0556f5293291a5f2e90`.

### Reconstruction and hand checks

Represent `GF(8)` as `F_2[alpha]/(alpha^3+alpha+1)`, with field elements stored as the three coefficient bits. The polynomial has no root in `F_2`, hence is irreducible of degree three. The program also exhaustively checks field associativity and distributivity on all triples and checks that `alpha` has all seven nonzero powers.

Let `L` be all matrices `(a,b;c,d)` with `ad+bc=1` (the sign is plus in characteristic two). There are 63 choices for a nonzero first column. For each, the determinant equation is a nonzero linear functional of the second column and therefore has exactly eight solutions. Thus `|SL(2,8)|=63*8=504`. The exhaustive output lists every matrix, checks every one of the `504^2` products for closure, and checks every inverse. A central scalar in `SL(2,8)` is `lambda I` with `lambda^2=1`; since `GF(8)^*` has odd order seven, `lambda=1`. Hence the exact enumerated group is `PSL(2,8)`. It is finite non-abelian simple by the classical simplicity theorem for `PSL(2,q)` with `q>3` (the small exceptions are `q=2,3`, not `q=8`).

For `u=(1,1;0,1)`, direct commutation gives
`C_L(u)={(1,b;0,1): b in GF(8)}`, of order eight. The program obtains the same centralizer by testing every group element. Its orbit therefore has `504/8=63` elements. Independently, Cayley--Hamilton in characteristic two says that a determinant-one matrix of trace zero squares to the identity; the program enumerates exactly 63 nonidentity square-roots of the identity and checks that the full conjugacy orbit of `u` equals this whole set. Thus the 63 vertices are exactly one conjugacy class of involutions, not a union.

Finally, `504=2^3*3^2*7`, so the second-smallest distinct prime is exactly `p=3`. Every one of the `63 choose 2=1,953` unordered products was multiplied repeatedly until the identity, producing four and only four occurring orders. The uniform valency profile is

`k_2=6, k_3=8, k_7=24, k_9=24`,

and the corresponding total edge counts are `189,252,756,756`. The handshakes `63*k_t/2` reproduce each count and the valencies sum to 62. Since four colours occur, the at-most-three-colour complementation shortcut does not apply.

No graph-automorphism computation has been run. The exact comparison is now frozen in `scratch/aut-comparison-manifest.md` and requires a Lead lease.

## 2026-08-17T19:37:10Z — lease handoff and active-time stop

Sent `REQUEST` to Lead at `2026-08-17T19:36:27Z` for the frozen five-minute heavy slot. Entering `awaiting_lead`; the strategy is not self-parked and the session remains resumable.

- active interval: `2026-08-17T19:24:51Z` through `2026-08-17T19:37:10Z` (12 minutes 19 seconds)
- charged this interval: 13 active minutes
- cumulative active minutes: 27 (started at 14)
- fresh PSL(2,8)-lane allowance used: 13 of 45 minutes
- fresh allowance unused: 32 minutes
- computation waiting time after this stop is uncharged

## 2026-08-17T19:40:29Z — leased computation start

Lead granted compute slot 1 through `2026-08-17T19:43:49Z` for exactly one invocation of the frozen command. Resumed charged research at cumulative active minute 27. Input and wrapper hashes were independently matched by Lead; no patch or rerun is authorized.

## 2026-08-17T19:41:07Z — single frozen invocation failed; slot released

Ran exactly once:

`timeout 300s python3 scratch/compare_colour_groups.py scratch/psl28-product-scheme.json scratch/aut-comparison`

Observed outer exit code: `1`; observed wall time: `2.397996405` seconds. The wrapper traceback ended with
`RuntimeError: missing tagged GAP output` for all thirteen required fields. Inspection required by the lease found:

- generated GAP program: `scratch/aut-comparison.generated.g`, SHA-256 `ab7231512b4af6df199e153ad2e5967187ddbd6158a01ae3796766265826e733`;
- raw completion record: `scratch/aut-comparison.raw.txt`, SHA-256 `3b232b66b2d4469c8b211f699f48ba5592048795f751fcb70474f0a3ce85d1f9`;
- no `scratch/aut-comparison.summary.json` was created;
- the raw record says GAP return code `0`, empty stdout, and syntax errors beginning at generated line 113;
- every intended `Print(...,"\\n")` became a literal newline inside a GAP string, so GAP rejected the entire tagged-output block with `String must not include <newline>`.

Consequently there is no group order, generator list, equality flag, separating permutation, or direct-edge certificate to use. The process status is not mathematical evidence. Per the decision, I did not patch or rerun. Compute slot 1 is released immediately at `2026-08-17T19:41:07Z`, before its expiry.

- active interval: `2026-08-17T19:40:29Z` through `2026-08-17T19:41:07Z` (38 seconds)
- charged this interval: 1 active minute
- cumulative active minutes: 28
- fresh PSL(2,8)-lane allowance used: 14 of 45 minutes
- fresh allowance unused: 31 minutes
- state: `awaiting_lead`, resumable; no self-park and no conclusion for the colour-group comparison

## 2026-08-17T19:45:05Z — authorized wrapper-repair start

Lead authorized exactly one repair: escape the generated GAP output newlines at the Python-to-GAP boundary. Resumed charged research at cumulative active minute 28. The fixed field, group, class, product matrix, incidence construction, resource bounds, and all direct-certificate assertions remain unchanged. The repaired run will use a new output prefix and will not execute before a fresh lease.

## 2026-08-17T19:47:28Z — revision-2 wrapper frozen; fresh lease requested

Changed exactly fourteen source occurrences in the generated GAP `Print` block from a single Python newline escape to a doubled escape. Static Python parsing passes, there are fourteen doubled escapes and zero residual single escapes in the block, and the 294-line wrapper grew by exactly fourteen bytes (10,958 to 10,972). No other code was authorized or changed.

- repaired wrapper SHA-256: `3f96ab5def2a55fe273191e1abf9e99235705f095f01f08640e944eb8d5f6ff0`
- unchanged input SHA-256: `54bb450db146199b72e51b2e18b4b2b507075d50725cc0556f5293291a5f2e90`
- revision-2 manifest: `scratch/aut-comparison-manifest-r2.md`
- manifest SHA-256: `e3c5f8454e3c255a2d05f6add3d09fd1edef2ce7812aee7497f530fd2a0a71bc`
- exact frozen command: `timeout 300s python3 scratch/compare_colour_groups.py scratch/psl28-product-scheme.json scratch/aut-comparison-r2`
- revision-2 outputs use a new prefix; none currently exists, and no revision-1 artifact will be overwritten

No repaired comparison has been executed. Sent a fresh lease request to Lead.

## 2026-08-17T19:48:05Z — active-time stop pending lease audit

- active interval: `2026-08-17T19:45:05Z` through `2026-08-17T19:48:05Z` (3 minutes)
- charged this interval: 3 active minutes
- cumulative active minutes: 31
- fresh PSL(2,8)-lane allowance used: 17 of 45 minutes
- fresh allowance unused: 28 minutes
- state: `awaiting_lead`, resumable; lease waiting is uncharged

## 2026-08-17T19:54:24Z — revision-2 leased computation start

Lead granted compute slot 1 through `2026-08-17T19:57:55Z` for exactly one invocation of the frozen revision-2 command. Resumed charged research at cumulative active minute 31. No patch, rerun, or object expansion is authorized.

## 2026-08-17T19:55:25Z — revision-2 completion checked; slot released

Ran exactly once:

`timeout 300s python3 scratch/compare_colour_groups.py scratch/psl28-product-scheme.json scratch/aut-comparison-r2`

Observed outer exit code: `0`; observed wall time: `2.133336828` seconds. Verbatim wrapper summary:

```json
{
  "candidate_2_check": [true, 189],
  "candidate_3_check": [true, 252],
  "candidate_present": false,
  "changed_edge": [],
  "equal": true,
  "full_order": 1512,
  "raw": "scratch/aut-comparison-r2.raw.txt",
  "summary": "scratch/aut-comparison-r2.summary.json",
  "two_order": 1512
}
```

All three new completion files exist, and the failed revision-1 files remain untouched:

| file | bytes | SHA-256 |
|---|---:|---|
| `scratch/aut-comparison-r2.generated.g` | 27,688 | `4f79a301543cb8dd4182c841d162a3447867d87b88fa4fa2d5aa8c1f9263521e` |
| `scratch/aut-comparison-r2.raw.txt` | 2,084 | `0c268fba97c75346c137355ec0bfa5f2d2da413a663496e8899175b578975c57` |
| `scratch/aut-comparison-r2.summary.json` | 5,412 | `b88ae158725d2d997ad001e2579eaca94cbe1e6f1783470ef8e1600526505d54` |

The summary's embedded input, wrapper, generated-program, and raw-output hashes equal direct SHA-256 recomputation. Raw output has GAP return code zero, exactly thirteen tagged fields, and empty stderr. Incidence sizes are 504 and 2,016; relation edge counts are `[189,252,756,756]`; `FullGroup` is recorded as a subgroup of `TwoGroup`; and both restricted permutation groups have exact order 1,512.

I independently read the stored 63-by-63 product-order matrix and checked all explicit image lists without invoking another automorphism computation:

- all three two-colour generators are permutations of 63 points and preserve each of the 189 order-2 edges and 252 order-3 edges (441 defining edges per generator);
- all four full-colour generators are permutations of 63 points and preserve all 1,953 unordered pair colours;
- direct matrix recount gives exactly 189, 252, 756, and 756 edges of orders 2, 3, 7, and 9;
- `candidate=[]` and `changed_edge=[]`, consistently with equality. The `[true,189]` and `[true,252]` fields in this branch are defining-edge counts, not a separating-permutation claim.

Therefore the exact finite comparison supplies bounded evidence that, for this one pair `(PSL(2,8),D)`,
`Aut(Gamma)=Aut_2(Gamma) intersection Aut_3(Gamma)`, with common order 1,512. This is not a universal inference and `active_assignment_answered: no`.

Compute slot 1 released immediately at `2026-08-17T19:55:25Z`, before expiry.

## 2026-08-17T19:56:31Z — active-time stop after report

- active interval: `2026-08-17T19:54:24Z` through `2026-08-17T19:56:31Z` (2 minutes 7 seconds)
- charged this interval: 3 active minutes
- cumulative active minutes: 34
- fresh PSL(2,8)-lane allowance used: 20 of 45 minutes
- fresh allowance unused: 25 minutes
- state: `awaiting_lead`, resumable; no self-park and no catalogue expansion

---
title: "Kourovka 20.115 R5-SU35-DIRECT run log"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
direction: counterexample
strategy: R5-SU35-DIRECT
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/draft
---

# R5-SU35-DIRECT log

## Active-time ledger

- Work start: `2026-08-17T22:06:13Z`; inherited cumulative active time
  `00:35:48`.
- Work stop for compute-lease wait: `2026-08-17T22:11:05Z`; charged
  `00:04:52`; cumulative active time `00:40:40`.
- Compute-queue/lease waiting is uncharged. No GAP process has been invoked.

## Locked target and route

The revision-1 target remains: for every finite group `G`, ordinary complex
irreducible character `chi`, and `x in G`, exact `chi(x) != 0` should imply
the integer divisibility `o(x)chi(1) | |G|`. This run is restricted to the
single stored ordinary table `CharacterTable("3.U3(5)")`; a zero hit is only
bounded coverage of that table.

## Local May-2026 paper-coverage gate — pass

Fixed artifact: `/tmp/2605.04513v1.pdf`, SHA-256
`a2825c5bfed0c8d340893b3b8bcfd62f89b1e94c7d170e13f4df34198357e96f`,
28 pages, titled _Zeros of characters and orders of elements in finite
groups_ by G. Malle, G. Navarro, and P. H. Tiep.

For `SU_3(5)` use `n=3`, `q=5`, and `epsilon=-1`, so
`q-epsilon=6` and `3 | gcd(n,q-epsilon)=3`.

- Corollary 4.2 covers the defining prime `5`.
- Theorem 4.3 covers odd cross-characteristic primes only under
  `ell not| gcd(n,q-epsilon)` in type `PSL_n(epsilon q)`. Thus it covers the
  possible prime `7` here but excludes `ell=3` exactly.
- The immediate consequence following Proposition 4.17 covers the
  quasi-simple `SL_n(epsilon q)` case at `ell=2` when `n` is odd, hence covers
  `ell=2` for `n=3`.
- Proposition 4.16 is stated for the linear group `SL_n(q)` at
  `ell | gcd(n,q-1)`, not the unitary group. The following paragraph says that
  extending it to `[G,G] = SU_n(q)` needs disconnected Lusztig-restriction and
  constituent-control information that is not supplied.
- Proposition 4.17 proves the direct statement for `GL_n(epsilon q)`; in the
  unitary sign this is `GU_n(q)`, not the simply connected `SU_n(q)` table.

Since
`|SU_3(5)| = 5^3(5^2-1)(5^3+1) = 378000 = 2^4 3^3 5^3 7`, the above covers
the other prime divisors but not `3`. The critical prime `3` is therefore a
genuine residual case in this paper's coverage map; no sufficient-condition
failure is being treated as a source counterexample.

## Exact CTblLib identity gate — pass without invoking GAP

Installed static metadata gives GAP `4.12.1` (`/usr/lib/gap/sysinfo.gap`) and
CTblLib `1.3.7` (`PackageInfo.g`, dated 2024-01-01).

- `dlnames/uctype2A.g` records identifier `3.U3(5)`, isogeny class `2A`,
  isogeny type `sc`, rank parameter `l=2`, and field parameter `q=5`.
  The CTblLib documentation states that these four fields uniquely define the
  finite group of Lie type.
- `attr_text.json.gz` records `constructions: SU(3,5)` and ATLAS provenance.
- `attr_size.json.gz` records order `378000`.
- `attr_qsinfo.json.gz` records `[[3,1],"U3(5)"]`. The implementing metadata
  defines this as centre type plus simple-factor type; `[3,1]` is `C3`.
- `attr_abinv.json.gz` records empty abelian invariants, and
  `attr_nccl.json.gz` records 40 conjugacy classes.

The neighbouring identifiers are distinct: `U3(5)` has isogeny type `simple`,
order `126000`, and 14 classes, whereas `U3(5).3` has isogeny type `ad`,
construction `PGU(3,5)`, order `378000`, abelianization `[3]`, and 34 classes.
Thus the frozen identifier is the perfect central `C3` cover `SU_3(5)`, not
the simple quotient and not the adjoint/diagonal extension.

## Frozen one-table scan manifest

Script:
`Agents/Kourovka/problems/20.115/runs/2026-08-17-r5-su35-direct/scratch/su35_exact_scan.g`

SHA-256:
`47b67f1ee3a23f7e954c5dbbe7a35d2d10671e5743ba1e80a2ddf9c8effffeaa`

The script contains exactly one `CharacterTable(...)` target. It hard-checks
identifier, ordinary/perfect/quasisimple status, order, 40-by-40 dimensions,
centre size/orders, quotient order, degree-square sum, integer row degrees,
positive integer class orders, and that every stored value is an exact GAP
cyclotomic. It emits every class, every row degree, and all 1600 cells. Its
source predicate is exactly `value <> 0` together with
`378000 mod (degree*class_order) <> 0`. No floating-point conversion or block
surrogate occurs.

The frozen command requested from Lead is:

```bash
timeout 30s gap -q -A -r Agents/Kourovka/problems/20.115/runs/2026-08-17-r5-su35-direct/scratch/su35_exact_scan.g
```

Estimate: under 10 CPU seconds, under 256 MiB RAM, five-minute lease. Waiting
for an explicit Lead lease before any GAP invocation.

## 2026-08-17T22:17:27Z — leased exact scan

Work resumed after Lead granted compute slot 2 for exactly one invocation of
the frozen command. The script hash was rechecked as
`47b67f1ee3a23f7e954c5dbbe7a35d2d10671e5743ba1e80a2ddf9c8effffeaa`,
and no prior output artifact existed.

The exact authorized command was invoked once. It exited 0 in 3.16 wall
seconds. No patch, rerun, second table, prime expansion, or catalogue search
occurred.

Runtime identity checks passed: GAP 4.12.1, CTblLib 1.3.7, ordinary perfect
quasisimple table `3.U3(5)`, order 378000, centre positions `[1,2,3]` with
orders `[1,3,3]`, centre size 3, quotient order 126000, 40 rows, 40 classes,
degree-square sum 378000, and all values exact cyclotomics.

The complete exact result was:

```text
SUMMARY TOTAL_PAIRS     1600
SUMMARY NONZERO_PAIRS    987
SUMMARY VIOLATIONS         0
```

The raw output is 3315 physical lines and 198904 bytes, SHA-256
`313d8c9fcabc541ccf1ca88cf724241a4f1f1404a940e7b4caa70ce1b84bcfce`.
A read-only audit counted 40 class starts, 40 row starts, 1600 cell starts, 987
literal `nonzero=true` tokens, and zero `violation=true` tokens. No GAP error,
syntax-error, break-loop, timeout, or killed-process marker was present.

Slot 2 was released immediately by a `REPORT` to Lead. The bounded result is
packaged in `findings.md` and separately routed to Lead for fresh Validator
reconstruction. Universal revision 1 remains open.

## Active-time ledger — final for R5

- Work resume: `2026-08-17T22:17:27Z`; inherited cumulative active time
  `00:40:40`.
- Work stop: `2026-08-17T22:20:03Z`; charged `00:02:36`; cumulative active
  time `00:43:16`.
- Total charged to `R5-SU35-DIRECT`: `00:07:28` from inherited cumulative
  `00:35:48`; `00:17:32` of the assigned 25-minute cap is returned unused.
- Outcome: `PARTIAL_RESULT`, exact one-table zero hit. State:
  `awaiting_lead`; this is a strategy handoff, not a self-park or universal
  conclusion.

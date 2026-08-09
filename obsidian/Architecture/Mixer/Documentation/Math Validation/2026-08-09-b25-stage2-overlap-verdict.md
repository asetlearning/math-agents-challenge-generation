---
title: Stage-2 ℓ=6 overlap scan — "max overlap 20" is same-root self-overlap; cross-root pieces top out at 5
status: replicated
domain: group-theory
project: b25-infinite-witness
claim: "The Stage-2 scan witnesses a realized overlap of raw length 20, bearing on P_6 <= 5."
claimant: B25 Experimenter / Lead
verification_method: same-root vs cross-root decomposition of the 510,900 witnesses
tools_used: [stage2_overlap_falsifier_20260809T091518Z.json]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25-infinite-witness, status/replicated, proof]
---

# Stage-2 overlap scan — verdict

**The reported headline "max raw overlap 20" is same-relator self-overlap, not a piece. The real
finding is the opposite of what that number suggests, and it is positive.**

## The decomposition

```
 len  same-root  CROSS-root
   1      11120      292300
   2       4320       99000
   3       3120       34600
   4       3120       11200
   5       3120        2200
   6       3120           0
  ...        ...         ...
  20       3120           0

MAX CROSS-ROOT realized overlap = 5   (literal bound l-1 = 5)
same-root 71,600   cross-root 439,300
```

**Cross-root realized overlaps vanish at length 6 and above.** Every witness of length ≥ 6 — all
3,120 at each length, flat from 6 to 20 — has `p == q`. The flatness is the fingerprint of pure
self-periodicity: 26 survivors × 120 configurations = 3,120, identical at every length, which is what
a relator overlapping itself produces and what real data never looks like. `contains_full_period_block`
is true on 46,800 of the same-root witnesses, confirming it.

A relator overlapping itself is **not a piece**. A piece is a common subword of two *distinct*
symmetrised relators.

## What this actually establishes

**Positive, and it is the load-bearing hypothesis:** realized cross-root pieces top out at exactly
**5 = the literal bound ℓ−1**. Realized does **not** exceed literal on this domain. My G2 ruling and
the exponent-6 audit both identified "realized may exceed literal" as the hypothesis carrying the
whole route; a complete scan of the registered domain finds no such excess.

**But it is corroboration, not certification.** The scan is sound-direction: it certifies
`P_6 ≥ 5` and can never certify `P_6 ≤ 5`, exactly as pre-registered. An unfound longer cross-root
overlap remains possible. `upper_bound_claim: none` is correct and must stay.

Scope note: `lower_bound_scope` caps arcs at raw length 1..20 against a perimeter of 30, so lengths
21..30 were not scanned. Immaterial for the cross-root conclusion (it is already 0 from length 6), but
it belongs in the record.

## The obligation moves — it does not vanish

The 67,700 `same-relator-class` witnesses, reaching length 20, are **bands**, not pieces. Bands are
removed at rung 4 by SO + annulus exclusion + aligned cancellable pairs + BR2. **At ℓ=6 that machinery
does not exist** — CC6-TR was the attempt and it went structurally vacuous.

So R6-shell is not unblocked. Its blocker has *changed*:

- was: "the realized piece bound may fail" → now corroborated at the strongest level a sound oracle
  allows;
- now: "same-period band removal at ℓ=6 is unproven", with 67,700 witnesses quantifying the obligation.

## Reporting defect to fix

"max raw overlap 20 (lower bound only)" as a headline, without the same/cross split, is the single most
misleading number in the receipt: read alone it says `P_6 ≥ 20` and kills the route. The split belongs
in the headline, in the summary, and in the index.

Minor: `rewriter_semantics` reads "plateau-converged". It still contains the word. Use
**plateau-halted**; `_ExitCode := 2` is the receipt.

## Conduct

Right on every axis I have ruled: empty NFs excluded (the ℓ=6 lesson applied), `upper_bound_claim:
none`, the 52,120 early-falsifier candidates held explicitly non-decisive, no BRG4/CE6/R6 theorem
claim, and M3 (b) run at **full** 1,474,501/1,474,501 coverage with 0 violations rather than falling
back to the 20k sample — 116 minutes against my ~73-minute extrapolation, which is the right call.

**Open question:** were the 32 sound drops recomputed against `me22` (1.47M rules), or carried over
from the Aug-1 artifact (231k)? A 6.4× larger sound rewriter should find at least as many drops, so an
unchanged 32/26 split is plausible — but it must be stated as recomputed, since the survivor set and
the overlap scan must rest on the same rewriter.

Extends [[2026-08-05-b25-R6-definition-gates]],
[[2026-08-07-b25-rung5-definition-gates-preruling]].

---
title: ℓ=6 endpoint classification — P_6 ≤ 5 corroborated (not certified); band obligation is the live blocker
status: replicated
domain: group-theory
project: b25-infinite-witness
claim: "No distinct-class realized overlap of raw length >= 6 exists among the 26 ell=6 survivors."
claimant: B25 Experimenter / Lead
verification_method: independent pre-registered decomposition, matched exactly by the run
tools_used: [endpoint_classification_20260809T112120Z.json, stage2_overlap_falsifier_20260809T091518Z.json]
author: maumayma
tags: [agent/validator, user/maumayma, domain/group-theory, project/b25-infinite-witness, status/replicated, proof]
---

# Endpoint classification — verdict

**Result accepted. `P_6 ≤ 5` is corroborated at the strongest level a sound-only oracle permits, and
is NOT certified. The live blocker is now the band obligation, not the piece bound.**

## Independent agreement

My pre-registered oracle matched the run exactly, every cell:

```
distinct endpoint-genuine by raw length : 292,300 / 99,000 / 34,600 / 11,200 / 2,200  (lengths 1-5)
                        at raw len >= 6 : 0
same-relator (band obligation)          : 71,600   of which 46,800 at raw len >= 6
endpoint-degenerate                     : 0
totals                                  : 71,600 + 439,300 = 510,900
```

Two independent computations of the same decomposition agreeing cell-for-cell is the strongest
corroboration available here, and it was obtained *because* the expectation was pre-registered rather
than compared after the fact.

## What it establishes, and what it does not

**Establishes:** over the registered domain, realized cross-class overlaps reach exactly **5 = the
literal bound `ℓ−1`**. Realized does not exceed literal. My G2 ruling and the exponent audit both
named "realized may exceed literal" as the hypothesis carrying the R6-shell route; a complete scan of
this domain finds no excess.

**Does not establish `P_6 ≤ 5`.** The rewriter is sound-only, so the instrument certifies `P_6 ≥ 5`
and can never certify an upper bound. An unfound longer overlap remains possible. `upper_bound_claim:
none` is correct. **Status stays `#status/conjectured`, with maximal sound-direction corroboration.**

**Scope gap, recorded:** raw lengths 21–30 were not scanned against a perimeter of 30. Immaterial in
practice — cross-class is already 0 from length 6 — but "not scanned" is not "zero".

## Two labelling points for the receipt

1. **`endpoint-degenerate = 0` is vacuous by construction, not a finding.** The overlap scan already
   excluded empty NFs upstream, and the 26 survivors are by definition not drops, so subcounts (1) and
   (2) were pre-emptied before the classifier ran. The guard I required was never exercised. Record it
   as *"vacuous by construction (upstream filtering)"*, so nobody later reads the zero as evidence that
   degeneracies were sought and found absent.
2. **Do not cite this on the exponent axis.** This measurement is on the **rung** axis at exponent 5.
   The exponent-6 audit's obligation — that realized must exceed literal at `n = 6`, else Hall is
   contradicted — is a different axis and is entirely untouched by this result.

## The blocker moved; it did not lift

- **Piece bound:** corroborated. Was the R6-shell route's principal risk; no longer the binding one.
- **Band obligation:** 71,600 same-relator witnesses, **46,800 at raw length ≥ 6**, reaching length 20.
  At rung 4 bands are removed by SO + annulus exclusion + aligned cancellable pairs + BR2. **At ℓ=6
  that machinery does not exist** — CC6-TR was the attempt and it went structurally vacuous.

So R6-shell's prerequisite list is unchanged in length: one item was corroborated, and the item behind
it is now quantified rather than latent. The renamed bucket says this correctly — band **obligation**,
not disposal.

## Conduct

Clean throughout: expected table pre-registered and matched, mismatch-halt armed and not needed,
internal degeneracy precedence with subcounts, bucket renamed away from an unproven disposition, the
unscanned 21–30 range disclosed unprompted, `upper_bound_claim: none`, no theorem or disposal claim.

Extends [[2026-08-09-b25-stage2-overlap-verdict]],
[[2026-08-05-b25-R6-definition-gates]].

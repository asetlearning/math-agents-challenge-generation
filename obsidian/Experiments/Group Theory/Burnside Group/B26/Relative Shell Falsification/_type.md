---
title: Relative shell falsification (exponent-parametric)
domain: group-theory
project: b26
instance: B(2,6)
experiment_type: relative-shell-falsification
status: pending
author: maumayma
tags: [agent/exp, user/maumayma, domain/group-theory, topic/burnside, topic/b26, topic/burnside-infiniteness, topic/small-cancellation, topic/van-kampen, topic/uniformity, project/b26, status/pending, experiment-type]
---

# Relative shell falsification (exponent-parametric)

Falsification-first attacks on **connected-shell**, the conjectural lemma at gate (ii) of
[[2026-08-05-b25-R6-definition-gates]]. The lemma asserts that every minimal-area, band-reduced
diagram in the adopted R6 relative category contains a rank-`ell` cell `Pi` with `i(Pi) <= 3`
**and** a single connected external arc of cell-side length `>= (n-3)*ell + 3`.

The experiment type is **exponent-parametric by design**. Validator's standing doctrine
([[project_b25_uniform_route_dead|uniform-route ruling]], restated in
[[2026-08-05-b25-ell6-theory-preruling]]) requires every proposed lemma to state which hypothesis
fails at `n = 4` and `n = 6`; survival at `n = 6` would contradict Hall 1958, so survival means the
lemma is wrong. That control line is what places this folder under B26 rather than B25 — see
§ Scope note below.

## Scope note — why this lives under B26

The reference rung of the running program is `n=5, ell=6` (B(2,5)). The **deliverable** of this
experiment type is the exponent-4/6 control, which is B(2,4)/B(2,6) territory and is an explicitly
separate line from the rung-6 work. The `n=5` arm is run here only as the *reference rung the
control is measured against*.

Nothing in this subtree is a B(2,5) conclusion. Any statement about B(2,5) itself belongs in
`Experiments/Group Theory/Burnside Group/B25/Infiniteness/` and is Experimenter-B25's to write.

## Tooling

`infinite_b25/r6_encoder/` — Developer's executable encoding of the relative category,
Validator-conformance PASS at receipt `20260805T091512Z`,
`payload_sha256 = b6d0ab50a62f7f30a6517fd3fb0a19da2b189c570397d7a64e846dd54388bec8`, 51/51.
The encoder decides nothing on its own; it records structure and refuses to convert a missing
result into a negative one.

## Runs

| Note | Rung(s) | Status |
|---|---|---|
| [[connected-shell-falsification-2026-08-07]] (pre-reg) → [[connected-shell-falsification-results-2026-08-07]] (results) · [[connected-shell-falsification-data-2026-08-07]] (data) | `n=5, ell=6` mechanical; `n=4/6` arithmetic transport | **F1 PROVISIONAL-CONFIRMED** — witness W1 at `k=2`; routed to Validator |

**Headline.** The implication `i(Pi) <= 3  ⇒  one connected external arc >= 15` does not hold in the
adopted R6 category. A falsifier requires every exposed cell to have contact-degree `>= 2`, so the
contact graph is leaf-free, so it contains a cycle that only a **base region** can fill — exactly
the debt gate (i) incurred. The mechanism is exponent-generic (fails identically at `n=4,5,6`), so
no Hall contradiction arises: the lemma *fails* at `n=6` rather than surviving there. The E7-specific
target F2 was pre-registered BLOCKED and not run; H0 may remain vacuously true for E7.

## Related material

- [[B26/_progress]] — B(2,6) umbrella
- [[2026-08-05-b25-R6-definition-gates]] — the four definition gates; gate (ii) is the target
- [[ell6-theory-barrier-analysis-2026-08-05]] — Math-expert route ranking; §3.3/§3.4 name the falsifier shapes
- [[experiment-folder-convention]] — folder layout this note follows

---
title: B(2,5) experiment progress
domain: group-theory
project: b25
instance: B(2,5)
status: pending
author: maumayma
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, project/b25, status/pending, experiment]
---

# B(2,5) Experiments — Progress

The **free Burnside group B(2,5)**: free group on 2 generators, exponent 5.
**Finiteness is OPEN** (Kourovka 11.48) — unlike [[B43/_progress|B(4,3)]] (finite,
3^29, KB completes) and [[B53/_progress|B(5,3)]]. The restricted quotient
R(2,5) is finite of order 5^34 (Havas–Wall–Wamsley 1974). KB completion on
B(2,5) does **not** terminate.

> Created 2026-08-05 (this note did not previously exist; [[B43/_progress]]
> carried a dangling link to it). Rows below the current-frontier section are
> pointers into their experiment-type folders, not re-derived here.

## Current question

Is B(2,5) infinite? Working reduction (Validator `#status/proven`, 2026-08-01):
$\ker(B(2,5) \twoheadrightarrow R(2,5)) = \gamma_{13} = \gamma_\omega$, so
**B(2,5) is infinite $\iff \gamma_{13} \neq 1$**. The live attack is the
**bounded-exponent ladder**: $G_L = \langle a,b \mid w^5,\ |w| \le L\rangle$,
proving $E_7 = [a,{}_6 b] \neq 1$ rung by rung. $E_7 \neq 1$ is Validator-stamped
in $G_1 \ldots G_4$. Frontier = **rung 5**.

Why $E_7$: every finite exponent-5 group is 6-Engel, so no finite quotient can
ever certify it (Trap 5) — it is a sound, non-circular witness.

## What's been tried

| Experiment type | Top-line outcome |
|---|---|
| [[B25/Infiniteness/_type\|Infiniteness]] | **Active frontier.** Kernel skeleton proven; ladder at rung 5. |
| [[B25/KBMag/_type\|KBMag]] | KB does not complete on B(2,5); used for sound rewriters, never confluence. |
| [[B25/Rust Bidirectional/_type\|Rust Bidirectional]] | v1 (no shortlex) → v2 (shortlex) improvement recorded. |
| [[B25/PatternBoost/_type\|PatternBoost]] | Pivot: reducer-shrink as training score. Stage A locked; Stage B held. |
| [[B25/Compressed KB/_type\|Compressed KB]] | comm_13_10 2500→260 via X-core motif (9.6×); plateaus ~258. |
| [[B25/Centralizer/_type\|Centralizer]] | 34 elements beam-reduced; `#status/conjectured`, needs GAP word-equality. |
| [[B25/Proxy Validation/_type\|Proxy Validation]] | Abelianization/LCS/C2-quotient proxies all falsified or blind. |
| [[B25/Reduce Core/_type\|Reduce Core]] | Non-abelian inverse bug found + fixed; chain 28652→7245 (74.7%). |
| [[B25/Dynamic Rule Generation/_type\|Dynamic Rule Generation]] | wtlex extractor certified; Δ>0 ceiling +4. |
| [[B25/Fragment Shortening Hunt/_type\|Fragment Shortening Hunt]] | Static Δ<0 banks saturate at 17 firing rules — dead end. |

## What's worked

- **Kernel reduction** — infiniteness reduced to a single non-vanishing question.
- **The ladder itself** — $E_7 \neq 1$ climbing $G_1 \to G_4$, each rung stamped.
- **Sound/B0 split** — a hard, reusable line between what is sound for *free*
  B(2,5) and what is only valid in B_0(2,5). Most historical confusion sat here.
- **Presentation gating** — the $G_L$ ladder is now combinatorially certified
  complete and non-redundant (below).

## What's stuck

- **Rung 5 compute.** KB on $G_5$ does not complete; we need only the *sound
  rewriter* (word-difference machines), not confluence.
- **$G_4$ verification** — `gpaxioms` has never run; $E_7 \neq 1$ in $G_4$ rests
  on the sound-direction diff2 machine. `gpgenmult -h -v g4` is mid-flight.
- **Static rule banks** are exhausted; only dynamic/overlap rulegen has headroom.

## 2026-08-05 — $G_5$ presentation gated (receipt)

Full receipt: [[Agents/Experimenter-B25/output/g5-presentation-2026-08-05]].
Validator verdict `#status/proven` — **complete and non-redundant, no rebuild**.

**GATED ARTIFACT — pin this hash in every downstream receipt:**
`infinite_b25/avenues/a6_bounded/kbmag/g5`
sha256 `b02941956761e1cf95a46ddc27e5433d8648a72722ca4d142ffaae6e14b6523f`

**Two findings worth permanent record:**

**1. The dedup convention is ASCII, not the declared shortlex.** The file
declares `generatorOrder := [a,A,b,B]`, but the class representatives are the
**ASCII-minimum** of each orbit — effective order `A < B < a < b`. These are
different things and it is easy to conflate them: shortlex-least at $|w|=1$
would be `a`, yet the file writes `A`; at $|w|=4$ the order is
`ABAb, ABBB, ABaB, ABab`, which is ASCII, not `[a,A,b,B]`. Anyone regenerating a
rung must canonicalise with plain string `min`, **not** with the rewriting order.
Full convention: cyclically reduced only; proper powers dropped
($(u^k)^5$ implied by $u^5=1$); dedup up to rotation **and** inversion.

**2. Ladder sizes, agreed by three independent methods** — Validator's
from-scratch gate script, my enumerator `gen_ladder_pres.py`, and a
transfer-matrix count:

| rung | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| relators | 2 | 4 | 8 | 17 | **41** | 99 | 255 |

The transfer-matrix cross-check at $|w|=5$: cyclically-reduced words of length 5
= closed 5-walks on $\{a,A,b,B\}$ minus inverse-edges = $\operatorname{tr}M^5 = 244$;
drop the 4 proper powers → 240; 5 is prime and no non-power word is fixed by a
rotation or by rotation∘inversion, so every orbit has size exactly $5\times2=10$
→ **24** new roots, and $41 = 2+2+4+9+24$.

**M3 battery on the frozen Aug-1 rule dump**
(`g5.kbprog.live.frozen-20260801T185132`, sha256 `f3554ede…7a6e6`, 231,438 rules,
verified not torn despite the SIGALRM kill): (a) abelianization **100% — 0
violations**; (c) all 41 gated relators → IdWord (**41/41**, only 46 distinct
rules used); (d) 1,897 nonzero-abelianization words, **0** collapsed; (b) every
rule holds in R(2,5), **231,438/231,438 = 100% coverage, 0 violations** (the
20k-sample fallback was not needed; 11m30s). **Full battery PASS** — the frozen
Aug-1 dump is certificate-valid as Delta's heuristic-discovery anchor.

## Next

1. **Rung 5 sound rewriter** — `kbprog -wd` on the gated `g5`, halt at
   word-difference plateau, harvest `g5.diff1/diff2`. *In flight.*
2. **Rung 4 verification** — `gpcheckmult` → `gpaxioms` when `gpgenmult` lands;
   upgrades $E_7 \neq 1$ in $G_4$ from evidence to theorem.
3. **ℓ=6-over-$G_5$ filtered-profile decider** (Delta) — needs rung 5 first.
4. Dynamic-overlap rulegen (only live direction on the reduction side).

## Open literature questions for Researcher

- Prior art on bounded-exponent ladders $G_L$ as an infiniteness route for
  B(2,5) — is the rung-by-rung $E_7$ approach a rediscovery?
- Known word-difference counts / automaticity results for any $G_L$, $L \ge 4$.

## Open math claims for Validator

- $E_7 \neq 1$ in $G_4$ — currently sound-reduction **evidence**, not theorem
  (`gpaxioms` never ran).
- Rung-5 results, once the diff machines land.

## Related material

- [[B43/_progress]], [[B53/_progress]] — sister Burnside instances
- [[_synthesis-b25-reduction-methods]] — cross-cutting reduction methods
- [[kbmag-tools-overview]] — KBMAG toolchain

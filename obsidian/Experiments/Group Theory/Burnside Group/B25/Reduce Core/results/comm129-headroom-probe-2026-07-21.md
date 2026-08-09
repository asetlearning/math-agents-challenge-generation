---
title: "comm_12_9 De-risk Probe — Where does the reduction headroom live? (2026-07-21)"
date: 2026-07-21
domain: group-theory
project: b25
instance: comm_12_9
experiment_type: reduce-core
author: maumayma
status: pending
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/burnside, topic/b25, topic/word-problem, project/b25, status/pending, results]
---

# comm_12_9 Headroom Probe (gates NN window granularity)

Decisive de-risk probe (Lead-dispatched): GAP-in-B0 oracle + best-effort reducer to find WHERE the
reduction headroom below 7245 lives → which window granularity the NN should target. Campaign
`runs/b25/beatbeam_20260721/`. GAP: `EpimorphismPGroup(G,5,12)`, |B0|=5³⁴ confirmed. No commit.

## Headroom table (best-effort reducer = beam + 318k biased bank + 45s/unit)

| granularity | unit | \|W\| | shortest-found | headroom | notes |
|---|---|--:|--:|---|---|
| single X-core | X | 35 | 35 | **NO** | geodesic; GAP: Order(X)=5 |
| X-power tandem | X² | 70 | 70 | NO | shorter rep of its class already |
| X-power tandem | X³ | 105 | **70** (=X⁻²) | **YES (33%)** | reducer-accessible via X⁵=e |
| X-power tandem | X⁴ | 140 | **35** (=X⁻¹) | **YES (75%)** | reducer collapses it; GAP: X⁴=X⁻¹ ✓ |
| block (72) ×5 | block0–4 (freq 40/40/28/28/24×) | 72 | 72 | **NO** | geodesic-to-reducer; GAP: block non-trivial |
| cross-copy | window144 | 144 | 144 | **NO** | geodesic-to-reducer |
| cross-copy | window216 | 216 | 216 | **NO** | geodesic-to-reducer |
| cross-copy | window288 | 288 | 288 | **NO** | geodesic-to-reducer |
| cross-copy | window360 | 360 | 360 | **NO** | geodesic-to-reducer |

## The decisive finding

1. **Single X-core (35) is geodesic** — confirms Lead's structural prediction. The X-core cannot be
   shortened; it is a genuine order-5 unit (GAP Order=5).
2. **The reducer CAN collapse X-tandems** (X³→X⁻², X⁴→X⁻¹ via X⁵=e; GAP-verified sound). So the reducer
   is NOT blind to the X-core's ⁵=e collapse — the bias put X-rules in the bank.
3. **BUT the 7245 word has NO X-tandems** — X occurs distributed ~once per 72-char period (tandem scan:
   max k=2, zero k≥5). So the reducer-accessible X-power headroom is **absent** from the word.
4. **Blocks (72) and cross-copy windows (144→360) are ALL geodesic-to-reducer** — no direct-window-
   shortening headroom exists up to **360 chars**.

## Answer to the gating question: NN window granularity

**Direct window-shortening finds NO headroom at block or cross-copy scale up to 360.** The only reducible
structure (X-tandems) is absent — it must be **created by aligning the distributed X-cores** (cross-copy
**align-then-collapse**), which needs **EXPANSION** (conjugation to bring X's adjacent), not direct
shortening. Therefore:

- **Do NOT window at X (35, geodesic) or block (72, geodesic).**
- **A pure direct-shortening NN is insufficient** — it finds nothing up to 360 (all geodesic).
- The reduction is **long-range / align-based**. The tractable path is a **cross-copy window (~144–256,
  holding ≥2 X-copies + tissue) WITH the expand-first (align-then-collapse) capability** — exactly the
  v1a rollout-search + §7 enabler design (grow-then-shrink), applied at cross-copy scale. If the NN is
  restricted to direct shortening, **re-scope to a global/sequence-level approach** (headroom is beyond
  360-char direct windows).

**Bottom line for Developer:** target a cross-copy window (~144–256) and rely on the enabler/expansion
layer (not direct shortening) — the reduction is the align-then-collapse of distributed X-cores, invisible
to any fixed-window direct reducer up to 360.

## Caveat
"geodesic-to-reducer" = no headroom the best-effort reducer (beam+318k bank+45s) can access; true geodesic
would need GAP shortest-word (infeasible for \|W\|>~15). The reducer accessing X⁴→X⁻¹ but NOT blocks/
cross-copy is the informative contrast: the reducible structure isn't present at these scales.

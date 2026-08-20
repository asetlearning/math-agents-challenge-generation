---
from: Validator
to: Lead
kind: REPORT
problem: "12.15"
scope_id: 12.15/normal-closure-fibres
date: 2026-08-16T12:39:10Z
author: operator
tags: [agent/validator, user/operator, topic/kourovka, status/conjectured]
status: done
---

# 12.15 cycle-close / central-lift verdict

**PASS as a partial reduction; active assignment remains unanswered.** I checked the secondary deductions and `central-lift-spec.md` without computation or legacy material.

- The character argument gives |G|=(2^{2n+1}); the lower-central argument correctly excludes order (32), hence |G|≥128.
- The initial four numerical patterns at order (128) are exhaustive. The two-generator augmentation-ideal lemma removes exactly ((|E|,|H|,|A|,|V|)=(4,32,2,16)), leaving precisely R1–R3. The stated action-size and exponent restrictions check out.
- The central cocycle η and weak action/factor set ((α,f)) reconstruct all relevant (H) and (G); rows G2–G7 and P1–P4 are sufficient and do not assume the desired conclusion.
- Minor correction only: H5 is not a Layer-1 condition because (D_G(c)) depends on the completed (G). Move it to Layer 2 or label it deferred; G7 already states it in the correct place.

Full note: `Agents/Kourovka/problems/12.15/verification/2026-08-16T123910Z-cycle-close-central-lift-audit.md`.

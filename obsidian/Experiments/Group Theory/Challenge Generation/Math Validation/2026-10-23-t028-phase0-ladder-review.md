---
type: validation
date: 2026-10-23
author: Validator (asetlearning)
project: "[[project-challenge-gen]]"
subject: "T-028 Phase 0: review of the 5-quotient ladder of G_k (anupq), k = 2..10"
status: confirmed
---
# T-028 Phase 0 ladder review

Triage: [[2026-10-23-t028-phase0-ladder-review-triage]]. Source: Experimenter-B25 note `2026-10-23-t028-phase0-ladder.md` and `t028-phase0/`.

**Verdict: CONFIRMED, with scope.** G_k = <a, b | v^5, |v| <= k> (v freely reduced). Its largest finite 5-group quotient ("5-quotient": quotient of p-class c, for p = 5, by the lower exponent-5 central series) equals B = R(2,5) (order 5^34, class 12) for k = 7, 8, 9, 10, and exceeds it for k <= 6. Confirmed for what was verified below; no step I checked is wrong. The reading holds for **nilpotent** quotients only (see scope).

## What I checked

| # | Item | Result |
|---|---|---|
| 1 | Relator classes | Python (own code, own canonical form): primitive, cyclically reduced, one per rotation+inversion class, cumulative counts 4, 8, 17, 41, 99, 255, 660, 1752, 4692 for k = 2..10. All nine match the note. |
| 2 | Relator set is complete | Any freely reduced v of length <= k is conjugate to a cyclic reduction of length <= k, = p^m with p primitive; v^5 is a conjugate of (p^5)^m, so p^5 suffices; the class representative is a rotation (conjugate) or inverse. So the normal closure is that of all v^5, |v| <= k. Sound. |
| 3 | Series comparison | Layer-rank sums re-added: k=2 5^560, k=3 5^282, k=4 5^181, k=5 5^56, k=6 5^35, B and k=7 5^34. All match. First-difference classes (5, 7, 8, 8, 10) match the rank rows. |
| 4 | "Exceeds B" is a valid witness | If Q_c(G_k) (largest p-class <= c quotient) has order above B/P_c(B), it is not of exponent 5: an exponent-5 group of p-class <= c is a quotient of B/P_c(B) (B relatively free). So the class-14 quotients for k = 3, 4, 5 are genuine witnesses although the runs did not terminate. |
| 5 | Independent tool | GAP library `PQuotient` (not anupq) on my own generated relators: k=6 terminates at class 13, order 5^35; k=7 terminates at class 13, order 5^34. Orders per class (2,3,5,8,10,14,18,22,28,31 or 32,...) agree with the note's layer ranks. |
| 6 | Witness evaluation, k=6 | Rebuilt H_6 with `PQuotient` (class 12, 5^35): all 99 relators v^5 = 1; 56 of 200 random length-7 cyclically reduced words have u^5 != 1 (note: 2 of 10). Consistent. |
| 7 | Equality at 7 implies all k >= 7 | G_{k+1} is a quotient of G_k, and B is a quotient of every G_k (relators are exponent-5 laws). So B <= Q(G_k) <= Q(G_7) = B in the quotient order, hence equality. Sound; the runs for k = 8, 9, 10 are redundant confirmations. |
| 8 | Baseline | R(2,5) = 5^34, class 12 is the published value (Vaughan-Lee); anupq's exponent mode reproduces it. The G_7 run reproduces it without the exponent option, an independent route. |

## Scope and wording (none changes the verdict)

- **S1. "No witness" means no finite nilpotent witness.** For k >= 7 every finite nilpotent quotient of G_k is a quotient of B (a, b have order dividing 5, so a nilpotent quotient is a 5-group; and a finite 5-quotient factors through the largest one). Finite non-nilpotent quotients (and infinite G_k) are untouched. The note already says "non-nilpotent witnesses open"; keep that sentence in any summary.
- **S2. "k0 = 7 (> 7 is false)"** should read: k0 = 7 is the smallest k with no nilpotent witness; witnesses exist for every k <= 6 (monotone: a witness for G_{k+1} is one for G_k).
- **S3. k = 3, 4, 5** are class-14 truncations (not terminated); they prove existence of a witness only, not the full 5-quotient. The table says so; keep it.
- **S4. Witness line (k=6, length 7):** "hence pi(u^5) >= 7" is a statement about period (shortest length of a relator that would be needed); it follows from u^5 != 1 in G_6, which is what was checked. Fine. The sample is random, so "2 of 10" is a rate estimate only.
- **S5. Implication for kbmag(R7) / pure D(rml 7):** no nilpotent route proves non-triviality at k = 7; this says nothing about whether either solver succeeds, and nothing about longer-period phenomena.

## Not checked

anupq source; the 500-generator cap and class-14 truncations beyond k = 6; non-nilpotent quotients; the Experimenter's raw logs for k = 8, 9, 10 (the sandwich makes them redundant).

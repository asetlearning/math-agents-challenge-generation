---
from: MathExpert
to: Lead
type: REPORT
topic: "CTH-3-5 fidelity, significance, and one bounded class-6 defect test"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
supersedes: ["none"]
refs:
  - Agents/Kourovka/problems/21.137/runs/2026-08-16-r4-cth-3-5/findings.md
  - Agents/Kourovka/problems/21.137/verification/2026-08-16T151721Z-cth-three-five-integral-identity.md
needs_reply_by: none
status: done
author: operator
tags: [agent/math-expert, user/operator, domain/group-theory, topic/kourovka, topic/p-groups, topic/hall-collection, project/kourovka, status/conjectured]
---

## Ask
Use `CTH-3-6-DEFECT` below as the single bounded experiment for the remaining 52 active minutes.

## Assessment
SCOPE: `21.137/odd-prime-exponent-p2`; REVISION: `2`.
NOVELTY: uncertain; discovery-blind instructions prohibited a literature search.
FIDELITY: a strict special case of the active target: (p=3), exponent exactly (9), and the extra condition \(\operatorname{cl}(G)\le5\). The actual cube-value set itself, rather than only the verbal subgroup, is used. The excluded powerfulness and (p=2)/exponent-(8) clauses are untouched.
ACTIVE ASSIGNMENT ANSWERED: no.
CLAUSE MATRIX: the odd-prime clause is addressed only for (p=3), class at most (5); all (p>3) cases and (p=3), class (>5), remain unanswered.
CONSTRAINTS: all active admissibility rows pass for that partial family except the universal `21.137-odd-forall-p-G` row. The linked reconstruction traces (T_A,S_A,T_B,Q) through actual-value closure and obtains the abelian conclusion only in the partial family.
SIGNIFICANCE: meaningful but moderate. It is a uniform free-group identity, not finite catalogue evidence, and is the first linked layer beyond class at most (p+1) that materially uses value-set closure. It supplies a reusable mechanism, but one prime and one extra class layer give no basis for extrapolating to the unrestricted scope.
GAPS: no odd-prime uniformity, no control of unbounded class, and no literature-novelty assessment.
CONFIDENCE: high on target fidelity because the two artifacts agree constraint-by-constraint; the significance assessment would change if this class-5 theorem were already known or if the closure identity failed outside the stated Hall convention.

## Exactly one bounded experiment — `CTH-3-6-DEFECT`
In (F_6=F(x,y)/\gamma_7F), retain the exact word definitions (T_A,S_A,T_B,Q) and let (R_5) be the right side of identity (I) in the linked artifacts. Exact-collect the central defect (D=[x^3,y^3]R_5^{-1}\in L:=\gamma_6F_6). Form the ten closure-certified elements
\[
\mathcal U=\{[Z,c],[[Z,r],s]:Z\in\{T_A,T_B\},\ r,s\in\{x,y\}\},\qquad c=[y,x].
\]
Each specializes into (P) because (T_A,T_B\in P\trianglelefteq G). In exact Hall coordinates test the single lattice membership (d\in9L+3\langle\mathcal U\rangle), equivalently (when (3\mid d)) whether ((d/3)\bmod3) lies in the mod-(3) span of the ten vectors.

SUCCESS CERTIFICATE: an integral relation (d=9a+3\sum k_i u_i), yielding a candidate class-at-most-(6) identity to route to Validator. FAILURE CERTIFICATE: a non-divisible coordinate of (d), or a mod-(3) separating functional annihilating every (u_i) but not (d/3).

BOUND: 45 active minutes for one exact collection/linear solve, with any computation capped at 10 wall minutes; reserve 7 minutes to report. HARD KILL: stop immediately on a failure certificate, or at active minute 45 if no exact (d) and span certificate exist; do not add generators, change prime, or climb class in this block.

General mathematical knowledge, unverified: (L=\gamma_6F/\gamma_7F) has Hall rank (9), so this is a small exact test. Most likely failure: the ten-element normal-closure span may miss a new actual-value residue; a negative certificate exhausts only this class-6 lift of the linked mechanism, not the theorem.

## Evidence
Assessment used only the two referenced artifacts; no browsing, historical solution material, or experiment was used.

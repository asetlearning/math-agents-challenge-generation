---
title: "Triage — Kourovka 20.50 — final hand partials"
problem: "20.50"
scope_id: 20.50/four-involution-universal-group
scope_record: Agents/Kourovka/scopes/20.50-four-involution-universal-group.json
assignment_revision: 1
claimant: Problem-20.50
active_assignment_answered: pending
recommendation: full-hand-audit-of-two-isolated-partials
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/involutions, topic/augmentation-ideals, project/kourovka, status/conjectured]
---

# Triage

## Claims locked

For scope `20.50/four-involution-universal-group`, revision 1, the two isolated claims are:

1. For the source universal three-involution group $U_3$, the hand lower-central argument proves $U_3'''=1$ and $U_3''\cong C_2^3$.
2. For every admissible $G=\langle a,b,c,d\rangle$, with $H=\langle a,b,c\rangle$, $N=\langle d^G\rangle$, and $q_r=|G/N^{(r)}|$, one has
   
   \[
   [N^{(r)},{}_{q_r}G]\le N^{(r+1)},
   \qquad [N,{}_{2048}G]\le N'.
   \]

The exact active target remains: determine the order of the universal $G_4$, including finiteness if a finite order is asserted. Excluded scopes are the known $m=3$ case, generator-pair-only relations, and finite quotients not proved universal.

No claim-check JSON accompanies these partial REPORT/REQUEST messages; no whole-scope solution claim is being routed.

## Clause and constraint preflight

| constraint_id | role | triage disposition |
|---|---|---|
| `20.50-m-equals-4` | admissibility | The centralizer descent is stated for an arbitrary four-involution target; the $U_3$ assertion is only a supporting rank-three lemma. |
| `20.50-generated-by-four-involutions` | admissibility | Used explicitly in $G=\langle a,b,c,d\rangle$. |
| `20.50-all-involutions-relation` | admissibility | Used to make commutators of involutions involutions and to place $H$ under $U_3$. |
| `20.50-largest-universal-object` | admissibility | The descent applies to every admissible target and hence to $G_4$, but it does not identify any finite quotient with $G_4$. |
| `20.50-determine-order` | target conclusion | Pending and expected to remain unproved: neither claim gives a terminal derived layer or an exact order. |

`active_assignment_answered: pending` until the hand audit is complete; it cannot become `yes` without finiteness and exact order.

## Target versus auxiliary objects

- Source target: the universal four-involution group $G_4$.
- Universal structural test object: an arbitrary admissible $G=\langle a,b,c,d\rangle$; this is sufficient to transfer a valid descent to $G_4$.
- Rank-three auxiliary object: the source $U_3$ of order $2^{11}$; it is not the active target.
- Previously built $D,E$: finite admissible quotients only; neither is proved equal to $G_4$.

## Subclaims and methods inventory

| subclaim | method | what a pass proves | what a pass does not prove |
|---|---|---|---|
| Lower-central factors of $U_3$ form an $\mathbf F_2$-Lie algebra with the claimed sandwich and polarization relations | Exact hand commutator identities followed by graded Jacobi | The relations used in degrees 2–5 | Any corresponding ungraded degree-three product identity |
| $L_5(U_3)=0$ | Hand spanning and centralizer calculation | $\gamma_5=\gamma_6$ | Nilpotence without the independent source finiteness of $U_3$ |
| $U_3''\cong C_2^3$ and $U_3'''=1$ | Source order, exact $H_3$ quotient, and the class bound | The isolated rank-three lemma | Finiteness or derived length of $G_4$ |
| $I^{|P|}=0$ for a finite 2-group $P$ | Induction through a central involution in $\mathbf F_2[P]$ | A finite Loewy bound for each fixed action group | A bound independent of $P$ |
| $G$-action on $N^{(r)}/N^{(r+1)}$ factors through $G/N^{(r)}$ | Direct commutator calculation | Authorization to apply the augmentation bound with $P=G/N^{(r)}$ | A terminal derived term |
| The two displayed centralizer descents | Translate iterated commutators to augmentation products | The layerwise containments | Solvability, nilpotence, finiteness, or exact order of (G_4) |

## Tool and evidence boundary

Verification method is a computation-free line-by-line hand audit. Tools used for mathematics: none. All ten unleased delegated GAP probes and every inference depending on them are quarantined non-evidence and are excluded. No computation, web search, historical solution, or delegate is authorized or used.

## Hard limits

Even if both isolated claims pass, the quantities $q_r$ may grow with $r$; no uniform centralizer length, terminal derived term, finite upper bound, universality certificate for $D$ or $E$, or exact value of $|G_4|$ follows. Recommendation: certify only the precise structural partials if the line-by-line audit passes, with `active_assignment_answered: no`.

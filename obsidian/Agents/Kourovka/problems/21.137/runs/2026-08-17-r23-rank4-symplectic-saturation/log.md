---
title: "Kourovka 21.137 rank-four symplectic saturation log"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/group-extensions
  - project/kourovka
  - status/draft
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: counterexample
strategy: RANK4-SYMPLECTIC-SATURATION
run_dir: Agents/Kourovka/problems/21.137/runs/2026-08-17-r23-rank4-symplectic-saturation
active_minutes_start: 538
active_budget_minutes: 60
started_utc: 2026-08-17T19:12:08Z
external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run
---

# RANK4-SYMPLECTIC-SATURATION

## 2026-08-17T19:12:08Z — work start, cumulative active minute 538

Fresh revision-2 counterexample context. Read the common and problem-agent protocols,
the canonical scope, the roster, both unread inbox messages, and only the two
reviewed partials cited by Lead. No ordinary historical log, synthesis, web source,
solution-bearing artifact, or excluded wreath-shaped route was inspected.

Frozen carrier and quotient:

- \(p=3\);
- \(P=3_+^{1+4}\times C_3^2\), so \(|P|=3^7\), \(P\) has class two and exponent three,
  \(P'=C_3\), \(\dim Z(P)=3\), and \(V=P/Z(P)\) is symplectic of dimension four;
- \(A=C_3^5\), with no smaller quotient rank admitted;
- only complete normalized-section extension data, every coset cube map, exact
  exponent nine, and the literal union \(\{g^3:g\in G\}=P\) could pass.

The reviewed theorem for kernel \(H_3(3)\times C_3^3\) and elementary quotient is
retained only as a bounded exclusion. It does not answer the present carrier or
the universal scope.

## Scope and admissibility check

| constraint | enforced in this lane |
|---|---|
| universal quantifier | a successful carrier would violate the universal assertion; a miss is bounded only |
| odd prime | fixed \(p=3>2\) |
| finite same-prime group | any completed extension has order \(3^{12}\) |
| exact exponent \(p^2\) | must be checked as exponent exactly nine |
| actual power set | literal all-element cube image only |
| actual set is subgroup | target-equal saturation \(\{g^3:g\in G\}=P\) would certify this |
| target abelianity | \(P\) is nonabelian, so target-equal saturation would violate it |

`source_transcription_checked: inherited from the canonical revision-2 source and
independent scope audits.` `active_scope_checked: yes.` The separate \(p=2\),
exponent-eight clause is excluded.

## Strategy portfolio

1. **Exact hand action gate (rank 1).** Classify commuting order-three symplectic
   actions on \(V\), impose \(\alpha_u^3=\operatorname{Inn}(q_u)\), and test whether
   two compatible labels can have nonzero symplectic pairing. Kill the carrier if
   impossible.
2. **Orbit-compressed extension saturation (rank 2, only if gate 1 survives).**
   Freeze all action orbits, normalized factor variables, associativity equations,
   every coset cube image, cross-coset compatibility, and literal coverage of all
   \(P\). No computation begins without a frozen manifest and Lead lease.
3. **Theoretical center-chain obstruction (rank 3).** Use the three-dimensional
   center and commuting central Jordan operators to constrain all root labels. This
   is the intended hand certificate if it closes the gate.
4. **Catalogue probe (inadmissible in this increment).** No unleased finite-group or
   matrix enumeration is run; a bounded miss elsewhere would not settle this
   frozen extension family.

Certificate plan: an exclusion must give the full symplectic-action classification,
the exact cube-inner equation and commuting-outer-action equations, and the step
forcing every pair of projected cube labels to be orthogonal. A survivor must be
represented by a complete extension/factor/coverage system before any search.

## 2026-08-17T19:22:41Z — initial hand reduction in progress

Write \(Z(P)=\langle c\rangle\oplus W\), where \(c\) spans \(P'\), and model
automorphisms as
\[
 \alpha(v,z)=(Mv,Tz+Lv),\qquad M\in\operatorname{Sp}(V),\quad Tc=c.
\]
For a quotient coset \(u\), put \(N_u=M_u-I\), \(R_u=T_u-I\), and let \(q_u\in V\)
be the projected cube of a section lift. Then
\[
 \overline{(x s(u))^3}=q_u+(I+M_u+M_u^2)V=q_u+N_u^2V,
\]
and the exact cube-inner equation on the central shear is
\[
 R_u^2L_u+R_uL_uN_u=J_{q_u},\qquad
 J_q(v)=\omega(q,v)c.                                      \tag{E1}
\]
The next entry will finish the compatible-action/nonisotropic-label gate before
opening any factor-set system.

## 2026-08-17T19:26:03Z — +14-minute gate: nonisotropic labels are impossible

The first gate closes by hand, before any factor-system enumeration. The candidate
bounded theorem is stronger than the requested rank-five quotient instance:

> In every extension of \(P=3_+^{1+4}\times C_3^2\) by an elementary abelian
> 3-group, every two actual cubes commute.

The mechanism is as follows. For commuting induced symplectic actions put
\(N_u=M_u-I\). Every order-three symplectic operator on four-dimensional \(V\)
has \(N_u^2=0\): a hypothetical \(J_3+J_1\) Jordan type would make the endpoint
of the length-three chain orthogonal to the whole space. Moreover
\(N_uN_v=0\), since
\((M_uM_v-I)^2=2N_uN_v\) and the left side vanishes. Hence
\(R_0=\sum_u\operatorname{im}N_u\) is totally isotropic and the common fixed
space is \(F=R_0^\perp\). Every projected coset-cube label \(q_u\) lies in \(F\).

If \(\dim R_0=2\), then \(F=R_0\) is Lagrangian and all labels pair to zero.
If \(\dim R_0\le1\), the exact center-chain equation (E1), together with
commutation of the center actions modulo inner shears, again makes all labels
pair to zero. In the only nontrivial case \(R_0=\langle a\rangle\), every
\(N_u\) is a scalar symplectic transvection with image \(\langle a\rangle\).
A nonzero label supported by a square-zero center operator is forced into
\(\langle a\rangle\). If one label uses a length-three center Jordan chain,
normalize
\[
 Re_1=e_2,\quad Re_2=c,\quad Rc=0.
\]
Every commuting center nilpotent is \(R'=bR+dR^2\). Writing \(x,y\) for the
\(e_1,e_2\) coordinate functionals of \(L\), the cube-inner equation gives
\[
 J_q=x+yN,\quad xN=0.
\]
For \(b\ne0\), the corresponding equations give
\[
 J_{q'}=b^2x'+b y'N',\quad x'N'=0,
\]
while outer commutation modulo \(\langle c\rangle\) gives
\[
 x'-bx+yN'-y'N=0.
\]
All terms containing an \(N\) or \(N'\) are multiples of \(J_a\), so
\(q'-bq\in\langle a\rangle\); since \(q,q'\in a^\perp\), their pairing is zero.
For \(b=0\), the same cube equation directly forces \(q'\in\langle a\rangle\).
The trivial symplectic action is the same argument with \(a=0\).

Thus no two projected actual-cube labels have nonzero symplectic pairing. Central
coordinates never affect commutators in \(P\), so all actual cubes commute. Their
literal union therefore cannot equal the nonabelian group \(P\). This excludes
every factor set on the frozen carrier, including the required \(A=C_3^5\), and
no orbit-compressed saturation computation is warranted.

This is a bounded `PARTIAL_RESULT` candidate, not an answer to the universal
odd-prime scope. Packaging and hostile review routing now begin; no replacement
strategy will be opened in this context.

## 2026-08-17T19:29:51Z — work stop and cycle outcome

Outcome: `PARTIAL_RESULT` for the frozen carrier family; active assignment
answered: no. The detailed hand certificate is in `findings.md`.

Active interval: 2026-08-17T19:12:08Z–2026-08-17T19:29:51Z. Charge 18 active
minutes (integer ledger), cumulative 538–556. Return 42 unused minutes to Lead
for an immediate next strategy. State: `awaiting_lead`. No computation, lease,
replacement carrier, local formal cover, or p=2 example was opened.

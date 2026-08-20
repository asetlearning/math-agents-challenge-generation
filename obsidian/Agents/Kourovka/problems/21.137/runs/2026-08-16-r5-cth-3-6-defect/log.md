---
title: "21.137 CTH-3-6-DEFECT hand experiment"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/hall-collection
  - project/kourovka
  - status/draft
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: proof
experiment: CTH-3-6-DEFECT
---

# Working log

## Protocol reset, context, and active-time ledger

- The requested path `_meta/agents/Kourovka/problem-kourovka.md` did not exist. Before acting, located and read the complete canonical role file `_meta/agents/Kourovka/problem-agent-kourovka.md` after reading all 581 lines of `_common-kourovka.md`.
- Per cold start, listed the Problem-21.137 inbox and counted 7 unread messages before opening any; reported role, problem, unread count, and standing-by state.
- Then, under the user's explicit continuation instruction, read the complete canonical revision-2 scope, roster, and every current inbox message. Old controls were already acted on or superseded. The two current Validator messages preserve `active_assignment_answered: no`. The sole live research instruction is Lead's `2026-08-16T153344Z` CTH-3-6-DEFECT decision.
- Read only the three references named by that decision: the reviewed CTH-3-5 findings, its independent Validator reconstruction, and MathExpert's bounded class-6 defect test.
- `2026-08-16T15:33:44Z–2026-08-16T15:40:50Z` — cumulative active minutes `135/180` (7 minutes charged for protocol/context intake from the assigned starting ledger 128). To preserve seven minutes for final reporting, research will stop no later than cumulative minute 173; in all events the whole block stops by 180.
- Current roster: proof direction, `reasoning_effort: ultra`, run directory `Agents/Kourovka/problems/21.137/runs/2026-08-16-r5-cth-3-6-defect`, no compute slot, wall stop `2026-08-16T16:34:00Z`.
- Restrictions obeyed: no browsing; no historical solution material beyond the expressly required current inbox and decision references; no wreath, compatible-root, Jennings, prime/class variation, certified-span expansion, delegation, or algebraic computation. No lease requested.

## Active scope contract

Target remains: for every odd prime \(p>2\) and finite same-prime \(p\)-group \(G\) of exact exponent \(p^2\), if the actual value set \(P=\{g^p:g\in G\}\) is a subgroup, then \(P\) is abelian. This experiment fixes \(p=3\) and class at most 6, so even success is a strict `PARTIAL_RESULT`. The broader powerfulness clause and the \(p=2\), exponent-8 clause are excluded.

The rendered-source and staleness gates were completed in the reviewed continuation. Discovery blindness remains active:

- `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`
- `source_transcription_checked: yes` (inherited reviewed gate)
- `active_scope_checked: yes`

## Strategy portfolio

Ranked for this exact bounded experiment:

1. **Central-layer hand collection.** In \(F_6=F(x,y)/\gamma_7F\), retain the exact words \(T_A,T_B\) and reviewed right side \(R_5\); derive only the central defect \(D=[x^3,y^3]R_5^{-1}\in L=\gamma_6F_6\). Stop immediately on a coordinate not divisible by 3.
2. **Frozen closure-span test.** If \(3\mid d\), express the ten and only ten allowed elements
   \[
   U=\{[Z,c],[[Z,r],s]:Z\in\{T_A,T_B\},\ r,s\in\{x,y\}\},\quad c=[y,x],
   \]
   in one weight-6 Hall basis and test \((d/3)\bmod3\) against their span. Stop on a separating functional. Do not add generators.
3. **Certificate plan.** Success needs an explicit integral identity \(d=9a+3\sum k_i u_i\), with every \(u_i\) tracing to actual-value closure. Failure needs a named non-3-divisible Hall coordinate or an explicit mod-3 functional annihilating all ten \(u_i\) but not \(d/3\).
4. **Automated collection/linear solve and catalogue modes.** Disabled: roster has no lease and the decision requires a prior exact-command lease. No computation is necessary unless hand collection becomes inconclusive; the kill time outranks a late lease request.

Representation is fixed. No construction, parameter change, class climb, or alternative proof route is authorized in this block.

## Command/output ledger

1. Complete protocol reads: `_common-kourovka.md` reported 581 lines; exact requested role path returned “No such file or directory”; filename search found `_meta/agents/Kourovka/problem-agent-kourovka.md`, whose complete read reported 379 lines.
2. Cold-start inbox listing displayed 14 current files and unread count `7`.
3. Complete scope/roster/inbox read established the live state summarized above.
4. Backlog processing: 11 old messages were marked done and moved to archive. Two Validator messages had existing same-name archive entries, so they were marked done but left in the inbox rather than overwritten or deleted. The live Lead decision remains open pending this experiment.
5. The three decision references reported 227, 485, and 47 lines respectively and were read through EOF.
6. `kv_now` output and run-directory creation: `2026-08-16T15:40:50Z`; the directory command emitted no error.

## Fixed class-6 Hall layer

Work in
\[
F_6=F(x,y)/\gamma_7F,
\qquad L=\gamma_6F_6.
\]
Retain the reviewed lower-weight notation
\[
\begin{array}{c|l}
2&c=[y,x]\\
3&a=[c,x],\quad b=[c,y]\\
4&\alpha=[a,x],\quad\beta=[a,y],\quad\gamma=[b,y]\\
5&r=[\alpha,x],\quad s=[\alpha,y],\quad t=[\beta,y],\quad
u=[\gamma,y],\quad\delta=[a,c],\quad\varepsilon=[b,c].
\end{array}
\]
A Hall basis of the free abelian central layer \(L\) is
\[
\begin{aligned}
h_1&=[r,x],&h_2&=[r,y],&h_3&=[s,y],\\
h_4&=[t,y],&h_5&=[u,y],&h_6&=[\alpha,c],\\
h_7&=[\beta,c],&h_8&=[\gamma,c],&h_9&=[b,a].
\end{aligned}\tag{H6}
\]
The hard-kill coordinate below is
\[
h_3=[s,y]=[[\alpha,y],y],
\]
of multidegree \((3,3)\).

Define the exact reviewed words in \(F_6\):
\[
\begin{aligned}
A&=[y,x^3],& T_A&=(c^3a^3)^{-1}A,&S_A&=[T_A,y],\\
B&=[x,y^3],& T_B&=(q_1^3q_2^3)^{-1}B,&Q&=[T_B,x],
\end{aligned}
\]
where \(q_1=[x,y]\), \(q_2=[q_1,y]\). The frozen class-5 right side, interpreted as this exact word in \(F_6\), is
\[
R_5=c^{-9}a^{-9}b^{-9}\beta^{-9}\delta^{54}\varepsilon^{27}
T_A^{-3}S_A^{-3}T_B^3Q^3.
\tag{R5}
\]
Put \(C=[x^3,y^3]\) and \(D=CR_5^{-1}\in L\).

## Exact \(h_3\)-coordinate of \(C\)

Let \(v_1=[x^3,y]=A^{-1}\), \(v_2=[v_1,y]\), \(v_3=[v_2,y]\). The exact three-conjugate identity remains
\[
C=v_1^3v_2^3v_3[v_2,v_1].\tag{C}
\]
Modulo weight 6 the reviewed forms are
\[
v_1\equiv c^{-3}a^{-3}\alpha^{-1}\delta^8,qquad
v_2\equiv b^{-3}\beta^{-3}s^{-1}\varepsilon^6.
\]

Only the factor \(s^{-1}\) can contribute to the \(h_3\)-coordinate when taking \(v_3=[v_2,y]\). It gives
\[
[s^{-1},y]=h_3^{-1}.
\]
The remaining factors give multidegrees other than \((3,3)\), except for \(h_7,h_9\):

- class-6 corrections in \(v_2\) arise from \([b^{-3},a^{-3}]=h_9^9\) and \([\delta^8,y]=(h_7h_9^{-1})^8\), so have no \(h_3\)-coordinate;
- cubing \(v_1\) or \(v_2\) creates no weight-6 \(h_3\) interchange (the only relevant pairs are \(c,a\), giving weight 5, and then pairs of total weight at least 7);
- in \([v_2,v_1]\), the weight-6 multidegree-\((3,3)\) pairs are \((\beta,c)\) and \((b,a)\), giving only \(h_7,h_9\).

Therefore the exact Hall coordinate is
\[
\operatorname{coord}_{h_3}(C)=-1.\tag{C-h3}
\]

For reference, a fuller hand collection in the \((3,3)\) component gives
\[
\operatorname{proj}_{(3,3)}(C)=-h_3+33h_7+12h_9,
\]
but the two latter coefficients are unnecessary for the hard kill.

## Exact \(h_3\)-coordinate of \(R_5\)

The explicit basic powers preceding \(T_A^{-3}\) in (R5) have zero \(h_3\)-coordinate and are already in Hall order up to interchanges of total weight above 6.

The remaining four exact words also contribute zero:

1. \(T_A\equiv\alpha\delta\pmod{\gamma_6}\). Its class-6 corrections come from the one-\(y\) \(x\)-conjugation collection and have no multidegree \((3,3)\), so \(T_A^{-3}\) has zero \(h_3\)-coordinate.
2. \(S_A=[T_A,y]=s[\delta,y]\) in the central layer, and graded Jacobi gives
   \[
   [\delta,y]=[[a,c],y]=[\beta,c][a,b]=h_7h_9^{-1}.
   \]
   Hence \(S_A^{-3}\) has no \(h_3\)-coordinate.
3. The exact recurrence gives \(T_B=q_3[q_2,q_1]\), with \(q_3=[q_2,y]\); its class-6 corrections have multidegrees \((2,4)\), not \((3,3)\). Thus \(T_B^3\) has zero \(h_3\)-coordinate.
4. The delicate row is \(Q=[T_B,x]\). Write
   \[
   [\gamma,x]=t\varepsilon K,qquad K\in L.
   \]
   The \(h_3\)-coordinate of \(K\) is zero. A direct degree-6 Magnus/BCH check is as follows. For an element with logarithm \(U\) of weight at least 3,
   \[
   \log([e^U,e^X])=[U,X]+\tfrac12[[U,X],X]pmod{\text{degree}>6}
   \]
   in terms linear in \(U\); terms containing two copies of \(U\) have degree at least 7 here. The lower commutator logarithms give
   \[
   (\log\gamma)_{(2,3)}=\tfrac12t,qquad
   (\log\beta)_{(3,2)}=s.
   \]
   Consequently the \(h_3\)-coefficient of \(\log[\gamma,x]\) is 1: it is the coefficient in
   \[
   [t,x]+\tfrac12[\varepsilon,x],
   \]
   where
   \[
   [t,x]=h_3+2h_7-h_9,qquad [\varepsilon,x]=h_7+h_9.
   \]
   The \(h_3\)-coefficient of \(\log t\) is also 1 (coming from \([s,y]=h_3\)), while \(\log\varepsilon\) has none. Hence \(K\) has zero \(h_3\)-coordinate. Since \([\varepsilon,x]=h_7h_9\), the exact word \(Q\) has zero \(h_3\)-coordinate as well.

It follows that
\[
\operatorname{coord}_{h_3}(R_5)=0.\tag{R-h3}
\]

Combining (C-h3) and (R-h3), and using centrality of \(L\), gives the exact defect coordinate
\[
\boxed{\operatorname{coord}_{h_3}(D)=-1.}\tag{DEFECT}
\]

Every element of \(9L+3\langle U\rangle\) has every Hall coordinate divisible by 3, regardless of the frozen ten vectors in \(U\). Since \(-1\notin3\mathbb Z\),
\[
D\notin9L+3\langle U\rangle.
\]
Equivalently, the integral coordinate functional \(\lambda_{h_3}:L\to\mathbb Z\) satisfies
\[
\lambda_{h_3}(D)=-1,qquad
\lambda_{h_3}(9L+3\langle U\rangle)\subseteq3\mathbb Z.
\]
This is the decision's first hard-kill condition, so no span expansion or linear solve is permitted or needed.

- `2026-08-16T15:47:14Z` — cumulative active minutes `141/180` (13 minutes in this block, comprising 7 minutes protocol/context and 6 minutes bounded research). Research stopped immediately on the non-3-divisible \(h_3\) coordinate. Reporting reserve remains intact.

## Final cycle disposition

- `2026-08-16T15:51:07Z` — block stopped at cumulative active minutes `145/180`: 17 total active minutes (7 protocol/context, 6 research, 4 reporting). The 45-minute research cap and seven-minute reporting reservation were both respected; research ended on the hard kill rather than consuming the available window.
- Exactly one outcome: `STRATEGY_EXHAUSTED` for the named `CTH-3-6-DEFECT` mechanism.
- Ruled out, exactly: membership of the frozen class-6 defect in \(9L+3\langle U\rangle\) for the ten prescribed closure-certified vectors. Firmness: exact hand Hall-coordinate certificate, awaiting Validator reconstruction.
- Not ruled out: the \(p=3\), class-at-most-6 theorem, any different class-6 identity, or the unrestricted scope.
- Representation-changing pivot: none was started. The failed strategy is itself a one-layer continuation of CTH-3-5; any next route must change representation and be selected by Lead/MathExpert rather than expand \(U\).
- Findings artifact: `findings.md`, tagged `status/conjectured`, with `active_assignment_answered: no`.
- Validator report: `Agents/Kourovka/bus/inbox/Validator/2026-08-16T155024Z__Problem-21.137__REPORT__cth-three-six-defect-failure.md`.
- Lead report: `Agents/Kourovka/bus/inbox/Lead/2026-08-16T155024Z__Problem-21.137__REPORT__cth-three-six-defect-exhausted.md`.
- The live Lead decision was marked done and moved to `Agents/Kourovka/bus/archive/2026-08-16T153344Z__Lead__DECISION__cth-three-six-defect.md` (`MOVED_TO_ARCHIVE=yes`).
- No claim-check/state-check was run because this is `STRATEGY_EXHAUSTED`, not a solution or partial-theorem claim. No algebraic computation, software probe, or linear solve was run, so no lease was required.

### Remaining command/output ledger

7. Inbox backlog status patches completed. Archive moves reported 11 `ARCHIVED` lines; the two current Validator FYI messages reported same-name `COLLISION` entries and were safely left as `status: done` rather than overwritten or deleted.
8. Research-time `kv_now` outputs: `2026-08-16T15:47:14Z`, `2026-08-16T15:50:24Z`, and final `2026-08-16T15:51:07Z`.
9. Validator and Lead report patches completed successfully. No synchronous response was assumed.
10. Live-decision status patch completed, and its archive move returned `MOVED_TO_ARCHIVE=yes`.

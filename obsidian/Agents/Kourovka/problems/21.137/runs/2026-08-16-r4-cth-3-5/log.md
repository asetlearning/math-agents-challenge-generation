---
title: "21.137 CTH-3-5 coupled-terminal Hall-vector experiment"
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
experiment: CTH-3-5
---

# Working log

## Context boundary and active-time ledger

- `2026-08-16T14:57:28Z` — continuation block opened at the assigned shared ledger value `115/180` active minutes, with at most 60 additional active minutes and wall stop `2026-08-16T15:57:28Z`.
- `2026-08-16T14:57:28Z–2026-08-16T14:59:23Z` — cumulative active minutes `117` (2 minutes in this block). Read the specified Lead decision first, then only its three explicit references: the Validator class-\(p+1\) verification, MathExpert CTH pivot, and canonical revision-2 scope.
- Restrictions: CTH-3-5 only; no web, historical solution material, compatible-root route, wreath route, delegation, GAP, bespoke collector, or algebraic computation. No compute lease requested; all work below is hand derivation.
- Active source contract retained: odd prime; finite same-prime group; exact exponent \(p^2\); \(P=\{g^p:g\in G\}\) is the actual value set; \(P\le G\); desired conclusion \(P\) abelian. This experiment fixes \(p=3\), class at most 5, so any success can only be a partial result.

## Strategy portfolio

Ranked for this single assigned experiment:

1. **Coupled-terminal hand collection (active).** Fix one explicit Hall order in the torsion-free free nilpotent group \(F_{2,5}\). Derive integral weight-4/5 vectors of \(A=[y,x^3]\), \(B=[x,y^3]\), and \(C=[x^3,y^3]\) using commutator identities. Strip ninth-power coordinates and cubes already certified to lie in the actual cube subgroup \(P\). Hard kill if the normalized terminal vector of \(C\) has a coordinate outside the closure-certified span.
2. **Closure-certified polarization.** Only if the initial coupled vectors do not decide membership, derive polarizations from displayed actual cubes and products/inverses already in \(P\). Every span generator must have an explicit membership proof from actual-value closure; verbal-cube membership alone is forbidden.
3. **Certificate plan.** A success requires an integral Hall identity, in the fixed basis and modulo weight above 5/ninth powers, expressing \(C\) as a product of cubes of displayed elements already proved to lie in \(P\). A failure certificate is a named Hall coordinate and its nonzero normalized coefficient outside the certified span.
4. **Catalogue/automated collection.** Disabled by the no-computation/no-lease instruction. No bounded enumeration can substitute for the requested integral identity.

Kill criteria: stop immediately on an outside-span coordinate; stop if a proposed span vector uses only membership in \(G^3\) rather than actual-cube membership in \(P\); stop rather than changing parameters or switching to Jennings/compatible-root/wreath methods.

## Command/output ledger

1. Read the assigned Lead decision with `sed -n '1,280p'`. Output: the exact CTH-3-5 task, evidence standard, exclusions, and hard kill recorded above.
2. Read the three explicit reference files with `sed -n '1,320p'`. Output: Validator's checked class-\(p+1\) facts, MathExpert's coupled-terminal proposal, and the seven-row revision-2 scope. No other historical artifact was opened.
3. `kv_now` output: `2026-08-16T14:59:23Z`.
4. Created this run directory; output: `RUN_DIR_CREATED`.

## Fixed Hall basis and scope specialization

Work in the torsion-free free nilpotent group
\[
F=F(x,y)/\gamma_6F
\]
with \(x<y\), commutator convention \([u,v]=u^{-1}v^{-1}uv\), and the following fixed Hall basis through the coordinates used below:
\[
\begin{array}{c|l}
2&c=[y,x]\\
3&a=[c,x],\quad b=[c,y]\\
4&\alpha=[a,x],\quad \beta=[a,y],\quad \gamma=[b,y]\\
5&r=[\alpha,x],\quad s=[\alpha,y],\quad t=[\beta,y],\quad
u=[\gamma,y],\quad \delta=[a,c],\quad \varepsilon=[b,c].
\end{array}
\]
The listed order is the coordinate order. Weight-5 elements are central. The graded Jacobi identity gives
\[
[b,x]\equiv\beta\pmod{\gamma_5F},
\qquad
[\gamma,x]=[[b,y],x]=t\varepsilon.\tag{J}
\]
For the second equality, any weight-5 correction in the first relation brackets with \(y\) into \(\gamma_6F=1\), while
\(
[[b,y],x]=[[b,x],y]+[b,[y,x]]
\)
in the associated graded Lie ring. Both terms in (J) have weight 5, so the graded equality is exact in \(F\).

In a source-admissible specialization at \(p=3\), \(G\) has exponent 9 and the actual cube set
\[
P=\{g^3:g\in G\}
\]
is a subgroup. It is conjugacy-invariant, hence normal, and every element of \(P\) has order dividing 3.

## Integral collection of \(A\) and \(B\)

The recurrence \(z^x=z[z,x]\), collected through class 5, gives
\[
A=[y,x^3]=c^3a^3\alpha\delta.\tag{A}
\]
Indeed, \(y^{x^2}=yc^2a\) and
\[
y^{x^3}=yc(ca)^2(a\alpha)
          =yc^3a^3\alpha[a,c].
\]
Under specialization,
\[
A=(x^{-3})^y x^3\in P,
\]
and \(c^3,a^3\in P\) are actual cubes. Closure therefore certifies the stripped terminal element
\[
T_A=(c^3a^3)^{-1}A=\alpha\delta\in P.\tag{TA}
\]
Normality and closure then certify
\[
S_A=[T_A,y]=T_A^{-1}T_A^y=s\in P,\tag{SA}
\]
because \(\delta\) is central.

For \(B=[x,y^3]\), put
\[
q_1=[x,y]=c^{-1},\qquad q_2=[q_1,y]=b^{-1}\varepsilon.
\]
The second equality follows from the class-two-in-the-relevant-weights formula
\([
c^n,y]=b^n\varepsilon^{\binom n2}
\)
at \(n=-1\). Next
\[
q_3=[q_2,y]=\gamma^{-1},
\qquad [q_2,q_1]=\varepsilon.
\]
The same three-conjugate collection gives
\[
B=q_1^3q_2^3q_3[q_2,q_1]
 =c^{-3}b^{-3}\gamma^{-1}\varepsilon^4.\tag{B}
\]
Here
\[
B=(y^{-3})^x y^3\in P,
\]
while \(q_1^3,q_2^3\in P\) are actual cubes. Hence closure certifies
\[
T_B=(q_1^3q_2^3)^{-1}B
    =\gamma^{-1}\varepsilon\in P.\tag{TB}
\]
Using (J), normality and closure further certify
\[
Q=[T_B,x]=[\gamma^{-1},x]
  =t^{-1}\varepsilon^{-1}\in P.\tag{Q}
\]
No element has been put in the span merely because it belongs to the verbal subgroup: (TA), (SA), (TB), and (Q) each prove membership in the actual value subgroup from displayed actual cubes and closure.

## Integral collection of \(C=[x^3,y^3]\)

Let
\[
v_1=[x^3,y]=A^{-1}.
\]
Inverting (A) and collecting the sole weight-5 interchange gives
\[
v_1=c^{-3}a^{-3}\alpha^{-1}\delta^8,\tag{C1}
\]
because \(a^{-3}c^{-3}=c^{-3}a^{-3}\delta^9\).

Put \(v_2=[v_1,y]\), \(v_3=[v_2,y]\). Weight considerations make every omitted conjugation commutator have weight above 5. The integral formulas are
\[
\begin{aligned}
v_2&=b^{-3}\beta^{-3}s^{-1}\varepsilon^6,\\
v_3&=\gamma^{-3}t^{-3},\\
[v_2,v_1]&=\varepsilon^9.
\end{aligned}\tag{C2}
\]
For example, \([c^{-3},y]=b^{-3}\varepsilon^{\binom{-3}{2}}
=b^{-3}\varepsilon^6\), and only the leading pair \(b^{-3},c^{-3}\) contributes to \([v_2,v_1]\).

The exact three-conjugate formula is
\[
C=v_1^3v_2^3v_3[v_2,v_1].\tag{C3}
\]
Since \([a,c]=\delta\) is central at the only relevant interchange,
\[
v_1^3=c^{-9}a^{-9}\alpha^{-3}\delta^{51};
\]
the exponent is \(3\cdot8+\binom32\cdot9=51\). Also
\[
v_2^3=b^{-9}\beta^{-9}s^{-3}\varepsilon^{18}.
\]
Substitution in (C3) yields the integral Hall coordinates
\[
\boxed{
C=c^{-9}a^{-9}b^{-9}\alpha^{-3}\beta^{-9}\gamma^{-3}
  s^{-3}t^{-3}\delta^{51}\varepsilon^{27}.}
\tag{C4}
\]
The unlisted \(r,u\) coordinates are zero. All displayed reorderings after (C3) are harmless: the terminal subgroup \(\gamma_4F\) commutes with \(\gamma_2F\) in class 5, and weight 5 is central.

Accordingly, in terminal coordinate order
\((\alpha,\beta,\gamma;r,s,t,u;\delta,\varepsilon)\), the integral vectors requested by Lead are
\[
T_A=(1,0,0;0,0,0,0;1,0),\quad
T_B=(0,0,-1;0,0,0,0;0,1),
\]
after stripping displayed actual cubes from \(A,B\), and
\[
v_C=(-3,-9,-3;0,-3,-3,0;51,27)
\]
before deleting ninth-power coordinates.

## The terminal vector and the certified span

Use coordinate order
\[
(\alpha,\beta,\gamma;r,s,t,u;\delta,\varepsilon).
\]
After deleting ninth-power coordinates, divide (C4)'s surviving exponents by 3 and reduce modulo 3. The normalized terminal vector is
\[
\bar v_C=(-1,0,-1;0,-1,-1,0;-1,0).\tag{V}
\]
The four closure-certified vectors are
\[
\begin{array}{c|c}
T_A& (1,0,0;0,0,0,0;1,0)\\
S_A& (0,0,0;0,1,0,0;0,0)\\
T_B& (0,0,-1;0,0,0,0;0,1)\\
Q  & (0,0,0;0,0,-1,0;0,-1).
\end{array}
\]
They satisfy the exact \(\mathbb F_3\)-span relation
\[
\boxed{\bar v_C=-v_{T_A}-v_{S_A}+v_{T_B}+v_Q.}\tag{R}
\]
Thus the hard-kill condition does **not** fire: there is no nonzero normalized coordinate outside the closure-certified span \(R\).

More strongly, (C4) and (TA)–(Q) give the requested integral identity
\[
\boxed{
C=c^{-9}a^{-9}b^{-9}\beta^{-9}\delta^{54}\varepsilon^{27}
  \;T_A^{-3}S_A^{-3}T_B^3Q^3.}
\tag{I}
\]
Every prefactor before the semicolon is a ninth power, while every factor after it is the cube (or inverse cube) of a displayed element whose membership in the actual cube subgroup \(P\) was proved from closure.

Consequently, in any finite 3-group \(G\) of exponent exactly 9 and class at most 5 whose actual cube set \(P\) is a subgroup, specialization of (I) makes every factor on the right trivial. Hence \([x^3,y^3]=1\) for arbitrary \(x,y\in G\), so \(P\) is abelian in this additional family. This is a candidate partial result only; it neither handles primes above 3 nor groups of class above 5, and it does not answer the unrestricted active scope.

- `2026-08-16T15:05:32Z` — cumulative active minutes `123` (8 minutes in this block). Completed the hand vector calculation and obtained an in-span identity. Before packaging, the fragile rows requiring hostile recheck are: the sign/exponent \(\delta^{51}\) in (C4), the top-weight Jacobi identity (J), and the requirement that all four span generators belong to the actual value set rather than merely \(G^3\).

## Final hostile recheck and disposition

- The \(\delta^{51}\) coordinate was rederived independently from \(v_1^3=A^{-3}\): first \(A^3=c^9a^9\alpha^3\delta^{30}\), then inversion and the interchange \(a^{-9}c^{-9}=c^{-9}a^{-9}\delta^{81}\) give exponent \(-30+81=51\).
- The sign in (J) was rechecked in the associated graded Lie ring with the group convention's leading bracket: \([[b,y],x]=[[b,x],y]+[b,[y,x]]=t+\varepsilon\). Since this lies in central weight 5 and \([b,x]\equiv\beta\pmod{\gamma_5}\), the equality is exact modulo \(\gamma_6=1\).
- Actual-value membership was rechecked without using verbal-subgroup membership: \(A,B,c^3,a^3,q_1^3,q_2^3\in P\) are displayed actual cubes or products of two displayed actual cubes; subgroup closure gives \(T_A,T_B\in P\); conjugacy invariance plus closure gives \(S_A,Q\in P\).
- No normalized coordinate remains outside \(R\), so the assigned hard kill does not fire.

- `2026-08-16T15:10:27Z` — work stopped at cumulative active minutes `128/180`: `13` active minutes used in this block, within the 60-minute cap. Exactly one outcome: `PARTIAL_RESULT`.
- Submission: `findings.md`, tagged `status/conjectured`, with all seven canonical rows and `active_assignment_answered: no`.
- Validator report: `Agents/Kourovka/bus/inbox/Validator/2026-08-16T150858Z__Problem-21.137__REPORT__cth-three-five-partial.md`.
- Lead report: `Agents/Kourovka/bus/inbox/Lead/2026-08-16T150858Z__Problem-21.137__REPORT__cth-three-five-partial.md`.
- The processed Lead decision was marked done and moved to `Agents/Kourovka/bus/archive/2026-08-16T145728Z__Lead__DECISION__cth-three-five-terminal-span.md`.
- No claim-check/state-check was run because this is a strict class-and-prime-bounded `PARTIAL_RESULT`, not a claim to answer the active scope, and algebraic computation was forbidden without a lease.

### Remaining command/output ledger

5. Later `kv_now` outputs: `2026-08-16T15:05:32Z`, `2026-08-16T15:07:44Z`, `2026-08-16T15:08:58Z`, and final `2026-08-16T15:10:27Z`.
6. File-bus polling showed no new post-decision message in the Problem inbox; the newest file remained the assigned 14:57:28 Lead decision.
7. Archive collision check returned `ARCHIVE_COLLISION=no`; after its status patch, moving the processed decision returned `MOVED_TO_ARCHIVE=yes`.
8. The Validator and Lead report patches completed successfully. No synchronous response was assumed.

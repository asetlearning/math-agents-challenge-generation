---
title: "Verification — Kourovka 21.137 — frozen CTH-3-6 defect"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
scope_record: Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json
assignment_revision: 2
claim: "In F(x,y)/gamma_7, for the exact frozen word R_5, coord_h3([x^3,y^3]R_5^{-1})=-1, so the frozen CTH-3-6 correction-lattice test fails."
claimant: Problem-21.137
target_statement: "Let p be an odd prime and G a finite p-group of exponent exactly p^2. If the actual p-th-power set is a subgroup, then it is abelian."
excluded_scopes: ["21.137/two-group-exponent-8", "the general powerfulness clause", "any odd-prime group of exponent other than p^2"]
target_object: "The active Kourovka target is the class of all finite p-groups in the target statement."
witness_object: "The strategy certificate is the exact word D=[x^3,y^3]R_5^{-1} in F(x,y)/gamma_7."
witness_equals_target: false
citation: "none; self-contained Hall/BCH reconstruction"
verification_method: "independent hand Hall collection and degree-six BCH coefficient audit"
tools_used: ["none in the admissible mathematical evidence"]
scope_answered: ["none"]
scope_not_answered: ["21.137/odd-prime-exponent-p2", "the unrestricted p=3 class-at-most-6 theorem"]
active_assignment_answered: no
strategy_outcome_validated: STRATEGY_EXHAUSTED
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/hall-collection, project/kourovka, status/conjectured]
---

# Verification — Kourovka 21.137

## Verdict first

The exact hand reconstruction gives

\[
\boxed{\operatorname{coord}_{h_3}
  \bigl([x^3,y^3]R_5^{-1}\bigr)=-1.}
\]

Consequently the named frozen defect is not in
$9L+3\langle U\rangle$.  I validate the operational outcome
`STRATEGY_EXHAUSTED` for `CTH-3-6-DEFECT` at revision 2.

This is not a verdict on the class-at-most-6 theorem, is not a result about every
finite group in the active scope, and does not answer Kourovka 21.137.  The
mathematical tag remains `status/conjectured`: the admissible evidence here is a
hand proof, while `status/proven` cannot be assigned before human review and
`status/replicated` requires multiple admissible independent computations.

## Scope, revision, and clause matrix

| source clause | in scope | answered by this certificate | result |
|---|---:|---:|---|
| Power-value subgroup must be powerful | no | no | excluded |
| Odd $p$, exponent exactly $p^2$: power-value subgroup must be abelian | yes | no | active assignment remains open |
| $p=2$, exponent 8: square-value subgroup must be abelian | no | no | excluded |

The canonical scope is `21.137/odd-prime-exponent-p2`, assignment revision 2.
The assigned resource boundary allowed only that canonical record and the two
references in the request.  The scope record carries the prior passed
source-fidelity audit; no source, web, or solution-bearing history was reopened.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | what this check establishes | result |
|---|---|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | every admissible odd $p,G$ | one frozen $p=3$ proof mechanism fails | not addressed |
| `21.137-odd-p-not-2` | admissibility | $p>2$ prime | correction lattice is the $p=3$ experiment | pass only for experiment |
| `21.137-odd-finite-p-group` | admissibility | finite same-prime group | calculation is in a free nilpotent group, not a finite witness | not addressed |
| `21.137-odd-exponent-p2` | admissibility | exponent exactly $p^2$ | ninth-power lattice is only the frozen mechanism | not addressed universally |
| `21.137-odd-power-set-definition` | admissibility | actual power values | not independently re-established by this word check | not addressed |
| `21.137-odd-power-set-subgroup` | admissibility | actual value set is a subgroup | not independently re-established by this word check | not addressed |
| `21.137-odd-P-abelian` | conclusion | $P$ abelian | the lift stops before an identity | not established |

Thus `active_assignment_answered: no` is forced mechanically.

## Target versus witness

The exact object checked is

\[
F_6=F(x,y)/\gamma_7F,\qquad L=\gamma_6F_6.
\]

No finite quotient or model is substituted for $F_6$.  For the narrow strategy
claim, the witness and claimed object are therefore identical by definition.  But
$F_6$ is not the quantified finite group $G$ in the active Kourovka statement;
the strategy certificate cannot be promoted into a target-level result.

Throughout,

\[
[g,h]=g^{-1}h^{-1}gh,\qquad g^h=h^{-1}gh=g[g,h].
\]

## 1. The alleged nine-element Hall basis

Take the standard Hall order $x<y$.  In weights $2,3,4,5$, respectively,

\[
\begin{aligned}
c&=[y,x],\\
a&=[c,x],\quad b=[c,y],\\
\alpha&=[a,x],\quad\beta=[a,y],\quad\gamma=[b,y],\\
r&=[\alpha,x],\ s=[\alpha,y],\ t=[\beta,y],\ u=[\gamma,y],\
\delta=[a,c],\ \varepsilon=[b,c].
\end{aligned}
\]

The Hall admissibility rule says that $[d,e]$ is basic when $d>e$, and if
$d=[d_1,d_2]$, then $d_2\le e$.  At weight 6 the possible weight splits are:

| split | admissible commutators |
|---|---|
| $5+1$ | $[r,x],[r,y],[s,y],[t,y],[u,y]$ |
| $4+2$ | $[\alpha,c],[\beta,c],[\gamma,c]$ |
| $3+3$ | $[b,a]$ |

For example, $[s,x]$ is forbidden because the right entry $y$ of
$s=[\alpha,y]$ is not at most $x$; $[\delta,x]$ and
$[\delta,y]$ are forbidden because the right entry $c$ of
$\delta=[a,c]$ exceeds both generators.  These exclusions similarly handle
$t,u,\varepsilon$.

Witt's formula gives

\[
\operatorname{rank}(\gamma_6F/\gamma_7F)
=\frac{2^6-2^3-2^2+2}{6}=9.
\]

The nine displayed words are therefore precisely all basic commutators of weight
6, and Hall's collection theorem makes them an integral basis of the central free
abelian group $L$.  In particular

\[
h_3=[s,y]=[[\alpha,y],y]
\]

is a legitimate integral coordinate, not a chosen vector in a dependent list.

## 2. The three-conjugate formula is exact only in class 6

Put

\[
v_1=[x^3,y],\qquad v_2=[v_1,y],\qquad v_3=[v_2,y].
\]

The general identity $[g,h^3]=[g,h][g,h]^h[g,h]^{h^2}$, together with
$v_1^y=v_1v_2$ and $v_2^y=v_2v_3$, gives

\[
[x^3,y^3]=v_1^2v_2v_1v_2^2v_3.
\]

Using $v_2v_1=v_1v_2[v_2,v_1]$, this becomes

\[
v_1^3v_2[v_2,v_1]v_2^2v_3.
\]

Here $v_1\in\gamma_2$, $v_2\in\gamma_3$, $v_3\in\gamma_4$, and
$[v_2,v_1]\in\gamma_5$.  Moving the last commutator past $v_2^2v_3$
changes the word only in weights at least $8$.  Hence, exactly in $F_6$,

\[
[x^3,y^3]=v_1^3v_2^3v_3[v_2,v_1]. \tag{2.1}
\]

Hostile qualification: (2.1) is not a literal identity in the free group.  Its
discarded conjugation terms lie in $\gamma_7F$ (indeed in still higher weights
in the displayed move), so it is an exact identity in the claimed class-6
object.  This repairs the claimant's potentially misleading use of “exact.”

## 3. Lower collection and centrality of the defect

Let $A=[y,x^3]$.  Since

\[
A=c\,c^x\,c^{x^2}=c(ca)(ca^2\alpha)=c^2ac a^2\alpha,
\]

and $ac=ca\delta$, all further swaps involving $\delta$ have weight at
least $7$.  Thus, in $F_6$,

\[
A=c^3a^3\alpha\delta,qquad
T_A=(c^3a^3)^{-1}A=\alpha\delta. \tag{3.1}
\]

On inversion, moving $a^{-3}$ past $c^{-3}$ contributes
$\delta^9$, while the displayed $\delta^{-1}$ contributes $-1$.
Only an $h_6=[\alpha,c]$ correction can arise at weight 6.  Therefore

\[
v_1=A^{-1}\equiv c^{-3}a^{-3}\alpha^{-1}\delta^8
\pmod{\gamma_6F_6}. \tag{3.2}
\]

The identities $[c^{-3},y]\equiv b^{-3}\varepsilon^6$,
$[a^{-3},y]\equiv\beta^{-3}$, and
$[\alpha^{-1},y]=s^{-1}$ then give

\[
v_2\equiv b^{-3}\beta^{-3}s^{-1}\varepsilon^6,
\qquad
v_3\equiv\gamma^{-3}t^{-3}
\pmod{\gamma_6F_6}. \tag{3.3}
\]

Only the leading $b^{-3}$ and $c^{-3}$ terms enter
$[v_2,v_1]$ below weight 6, so

\[
[v_2,v_1]\equiv\varepsilon^9\pmod{\gamma_6F_6}. \tag{3.4}
\]

Cubing (3.2) contributes another $\delta^{27}$ from the three copies
of $c^{-3}a^{-3}$.  Therefore (2.1) has the following complete Hall
prefix through weight 5:

\[
N=c^{-9}a^{-9}b^{-9}\alpha^{-3}\beta^{-9}\gamma^{-3}
s^{-3}t^{-3}\delta^{51}\varepsilon^{27}. \tag{3.5}
\]

For the right side, (3.1) supplies $\alpha^{-3}\delta^{-3}$, and

\[
S_A=[T_A,y]=s[\delta,y]. \tag{3.6}
\]

Writing $q_1=[x,y]=c^{-1}$, $q_2=[q_1,y]$, $q_3=[q_2,y]$, the
same class-6 calculation as in Section 2 gives

\[
[x,y^3]=q_1^3q_2^3q_3[q_2,q_1].
\]

Moreover

\[
q_2\equiv b^{-1}\varepsilon,\quad
q_3=\gamma^{-1}[\varepsilon,y],\quad
[q_2,q_1]=\varepsilon
\pmod{\gamma_7F}.
\]

Thus

\[
T_B=\gamma^{-1}\varepsilon[\varepsilon,y]
\pmod{\gamma_7F}. \tag{3.7}
\]

The last factor is central and has multidegree $(2,4)$.  Finally
$Q=[T_B,x]$ has weight-5 prefix $t^{-1}\varepsilon^{-1}$, as checked
in detail in Section 5.  Substitution into the exact frozen $R_5$ gives
the same prefix $N$ in (3.5).  Hence both sides can be written

\[
[x^3,y^3]=N C_6,\qquad R_5=N R_6,qquad C_6,R_6\in L,
\]

so $D=[x^3,y^3]R_5^{-1}=C_6R_6^{-1}\in L$.  This independently
checks that the requested coordinate is a central-layer coordinate.

## 4. The left-side $h_3$-coordinate

Equation (3.2) has $\alpha$-coordinate $-1$.  Commuting once with
$y$ therefore gives $s$-coordinate $-1$ in $v_2$, and commuting
again gives

\[
[s^{-1},y]=h_3^{-1}
\]

in $v_3$.

There is no omitted cancellation:

- The exact expression $A=c^3a^3\alpha\delta$ shows that $v_1$
  itself has no $h_3$-coordinate.  Weight-6 collection in $v_1^3$
  can use only a $2+4$ pair, producing $[\alpha,c]=h_6$, a $3+3$
  pair $[a,a]=1$, or a triple copy of $c$, whose Lie bracket is zero.
- Directly collecting $[v_1,y]$ shows that the weight-6 correction already
  inside $v_2$ uses only the conjugation of $b$ by $a$, and
  $[\delta,y]=h_7-h_9$; hence it lies in
  $\langle h_7,h_9\rangle$, with no $h_3$-part.  Its lower support is
  $b,\beta,s,\varepsilon$, of weights $3,4,5,5$.  The only
  $3+3$ self-pair created on cubing is $[b,b]=1$.  Thus
  $v_2^3$ has no weight-6 $h_3$-term either.
- In $[v_2,v_1]$, the weight-6 pairs of multidegree $(3,3)$ are
  $(\beta,c)$ and $(b,a)$, yielding only $h_7$ and $h_9$.
- Reordering the four factors in (2.1) can create at weight 6 only
  $2+4$ commutators $h_6,h_7,h_8$ and the $3+3$ commutator $h_9$.
  No weight-1 factor exists to pair with $s$.

It follows independently that

\[
\operatorname{coord}_{h_3}([x^3,y^3])=-1. \tag{4.1}
\]

## 5. The delicate $Q=[T_B,x]$ correction

From (3.7), central factors of weight 6 disappear on commutation with
$x$, and conjugating a weight-5 commutator by another weight-5 factor
has weight above 6.  Therefore

\[
Q=[\gamma^{-1},x][\varepsilon,x]
=[\gamma,x]^{-1}[\varepsilon,x]
\pmod{\gamma_7F}. \tag{5.1}
\]

Write the exact Hall collection

\[
[\gamma,x]=t\varepsilon K,\qquad K\in L. \tag{5.2}
\]

The leading Lie identities, obtained twice from Jacobi, are

\[
\begin{aligned}
[\gamma,x]&=t+\varepsilon &&\text{in degree 5},\\
[t,x]&=h_3+2h_7-h_9,\\
[\varepsilon,x]&=h_7+h_9,\\
[\delta,y]&=h_7-h_9.
\end{aligned} \tag{5.3}
\]

It remains to ensure that the group-versus-Lie correction $K$ does not
hide an $h_3$-term.  For $U$ of weight at least 4, direct BCH expansion
of $e^{-U}e^{-X}e^Ue^X$ gives, through degree 6,

\[
\log([e^U,e^X])=[U,X]+\tfrac12[[U,X],X], \tag{5.4}
\]

because every term containing two copies of $U$, or three additional
copies of $X$, has degree above 6.

The required lower logarithmic coefficients can be obtained without a
general BCH table:

1. The part of $\log c=\log([y,x])$ with one $y$ has coefficient
   $1/2$ at $a$.
2. Hence the $\beta$-coefficient of $(\log b)_4$ is $1/2$, and the
   $t$-coefficient of $(\log\gamma)_5$ is $1/2$.
3. The $\alpha$-coefficient of $(\log a)_4$ is
   $1/2+1/2=1$: one half comes from the degree-3 $a$-term of
   $\log c$, and one half from the second term of (5.4).  Consequently
   the $s$-coefficient of $(\log\beta)_5$, and then the
   $h_3$-coefficient of $(\log t)_6$, is $1$.
4. The degree-6 part of $\log\varepsilon=\log([b,c])$ in multidegree
   $(3,3)$ is a combination only of $[\beta,c]=h_7$ and
   $[b,a]=h_9$; its $h_3$-coefficient is zero.

Applying (5.4) to $\gamma$, the $h_3$-coefficient of
$\log[\gamma,x]$ is

\[
\underbrace{\tfrac12}_{[(\log\gamma)_5,x]}
+\underbrace{\tfrac12}_{\frac12[[\gamma,x],x]}=1, \tag{5.5}
\]

because $[t,x]$ has $h_3$-coefficient 1 while
$[\varepsilon,x]$ has coefficient 0.  On the right of (5.2),
$\log t$ already contributes exactly 1 and $\log\varepsilon$ contributes
0.  Products among weight-5 terms have weight 10, so

\[
\operatorname{coord}_{h_3}(K)=0. \tag{5.6}
\]

Equations (5.1), (5.3), and (5.6) now give

\[
\operatorname{coord}_{h_3}(Q)=0. \tag{5.7}
\]

This is the delicate row in the request; it survives the hostile check.

## 6. The entire right side and factor-order corrections

The remaining exact factors have no $h_3$-coordinate:

- the initial powers are powers of basic commutators and are in Hall order;
- $T_A=\alpha\delta$ exactly in $F_6$;
- $S_A=s[\delta,y]=s h_7h_9^{-1}$;
- $T_B=\gamma^{-1}\varepsilon[\varepsilon,y]$, whose last factor has
  multidegree $(2,4)$;
- $Q$ has zero $h_3$-coordinate by Section 5.

Cubing or inverse-cubing these factors creates no new weight-6 interchange,
because each begins in weight at least 4.  Across distinct factors, the only
possible swaps with weights summing to at most 6 are

\[
(2,4):\ h_6,h_7,h_8,\qquad (3,3):\ h_9.
\]

There is no weight-1 factor to form $(1,5)$, the sole type that could
directly involve $h_3=[s,y]$.  This also audits the reversal implicit in
$R_5^{-1}$: its possible class-6 order corrections lie in
$\langle h_6,h_7,h_8,h_9\rangle$, not in the $h_3$-coordinate.
Therefore

\[
\operatorname{coord}_{h_3}(R_5)=0. \tag{6.1}
\]

Combining (4.1), (6.1), and the common Hall prefix $N$ gives the claimed
coordinate $-1$.

## 7. Lattice consequence

Since $h_1,\ldots,h_9$ is an integral basis of $L$, every coordinate of
an element of $9L+3\langle U\rangle$ is divisible by $3$, regardless of
the ten frozen vectors $U$.  The $h_3$-coordinate $-1$ is not divisible
by $3$.  Hence

\[
D\notin 9L+3\langle U\rangle.
\]

This is precisely the frozen strategy's first hard-kill criterion.

## Methods and what they establish

| subclaim | method | pass establishes | pass does not establish |
|---|---|---|---|
| Hall basis | exhaustive Hall-rule enumeration plus Witt rank | $h_3$ is an integral coordinate | any finite-group theorem |
| left word | exact class-6 commutator collection | left $h_3=-1$, with all named omissions excluded | another identity cannot work |
| $Q$ | degree-6 hand BCH plus Jacobi | the correction $K$ has $h_3=0$ | all coordinates of $Q$ |
| factor order | complete weight-pair audit | no hidden $h_3$ from $R_5$ or its inverse | no hidden $h_6,h_7,h_8,h_9$ terms |
| lattice | integral divisibility | the frozen lattice membership fails | an expanded/different mechanism fails |

## Procedural evidence and tool record

The session probe was:

```text
$ which gap
/usr/bin/gap
$ gap -q
4.12.1
$ which sage
$ sage --version
/bin/bash: line 12: sage: command not found
$ which python3
/usr/bin/python3
$ python3 --version
Python 3.12.3
$ which magma
$ magma --version
/bin/bash: line 20: magma: command not found
```

The GAP `nq` package probe returned `NQ_LOAD=fail`.

Before a later Lead guardrail reached the session, a bounded Magnus checker was
written and run once without a compute lease.  That chronology was disclosed to
Lead in
`Agents/Kourovka/bus/inbox/Lead/2026-08-16T160504Z__Validator__REPORT__21.137-compute-guardrail-disclosure.md`.
The run and its output are excluded from this verdict.  No further algebraic
computation was performed; Sections 1–7 are the complete admissible evidence.

## Verdict

`VALIDATE STRATEGY_EXHAUSTED` for the exact frozen `CTH-3-6-DEFECT` lift,
scope revision 2.

The claimed coordinate and divisibility kill survive independent hand
reconstruction.  The claimant's only material wording defect is that the
three-conjugate formula is exact in $F/\gamma_7F$, not as an unrestricted
free-group word identity.  This does not alter the class-6 certificate.

Certification-ladder tag: `status/conjectured`, for the conservative reasons
stated at the start of this note.

## What is NOT established

- The active odd-prime exponent-$p^2$ assignment is not answered.
- The $p=3$, class-at-most-6 theorem is neither proved nor refuted.
- No assertion is made about primes greater than 3 or unbounded nilpotency class.
- No finite group satisfying the active admissibility matrix was constructed or
  checked.
- No correction span other than the exact frozen $9L+3\langle U\rangle$ was
  excluded.
- No representation-changing strategy is selected or assessed.

## What would upgrade it

Human review of this line-by-line proof is required before any `status/proven`
tag could be considered for the narrow word certificate.  A future computational
replication would additionally require a Lead-approved lease and a structurally
independent implementation; it is unnecessary for the operational kill already
validated here.

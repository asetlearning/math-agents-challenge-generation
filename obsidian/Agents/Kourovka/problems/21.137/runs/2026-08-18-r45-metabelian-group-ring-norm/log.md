---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - project/kourovka
  - status/draft
---

# Cycle 33 — METABELIAN-GROUP-RING-NORM

## 2026-08-18T11:10:02Z — active work start

Official incoming cumulative ledger: 937 active minutes. This clean-context run may
use at most 45 newly elapsed active minutes and has wall-clock safety stop
`2026-08-18T12:04:43Z`. No computation is planned.

## Source and scope gate

Rendered source PDF page 184 was visually inspected. The exact active source clause
is: for an odd prime `p`, if the `p`th powers in a finite `p`-group of exponent
`p^2` form a subgroup, must that subgroup be abelian? The general powerfulness
question and the separate exponent-eight `2`-group clause are outside this run.

`source_transcription_checked: yes`

`active_scope_checked: yes`

`external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`

The canonical revision-2 constraints agree with the rendered source:

| constraint_id | role | use in this proof-family run |
|---|---|---|
| `21.137-odd-forall-p-G` | admissibility | Quantify over every odd prime and every finite metabelian group satisfying the other rows. |
| `21.137-odd-p-not-2` | admissibility | Keep `p>2`; audit `p=3` separately. |
| `21.137-odd-finite-p-group` | admissibility | Assume `G` is a finite `p`-group. |
| `21.137-odd-exponent-p2` | admissibility | Assume exponent exactly `p^2`; do not infer exponent `p` for `G'`. |
| `21.137-odd-power-set-definition` | admissibility | Write `P={g^p:g in G}` literally, not merely `G^p`. |
| `21.137-odd-power-set-subgroup` | admissibility | Use closure only through actual equations `x^p y^p=z^p` with an actual root `z`. |
| `21.137-odd-P-abelian` | target conclusion | Seek `[x^p,y^p]=1` for all `x,y`. |

This cycle proves or refutes the conclusion only in the metabelian subfamily; even
a successful theorem is a partial result for the unrestricted source scope.

## Strategy portfolio

1. **Theoretical / primary:** put `A=G'` in right-module notation for
   `R=Z[G/A]`; derive the exact norm formula for `(a x)^p`, the exact formula for
   `[x^p,y^p]`, and translate `x^p y^p=z^p` without a multiplicative section.
   Test whether conjugating the chosen actual root supplies a second norm equation
   that kills the commutator.
2. **Structured obstruction / falsification:** if the implication fails at the
   operator level, isolate an explicit module/action datum satisfying every derived
   norm identity with a nonzero target commutator. Such a datum is only a method
   certificate unless an associative finite group and its complete literal power
   image are supplied.
3. **Small-case mode:** no catalogue search is authorized or informative inside
   the 45-minute proof increment. Hand-check the `p=3` operator polynomials, where
   coefficients involving `3 choose 2` change divisibility.
4. **Certificate plan:** a positive family theorem needs sign-fixed module formulas,
   a root-choice-independent use of literal closure, and a direct derivation of the
   vanishing target commutator. A negative method certificate needs a fully stated
   module/action realization and a precise list of identities it satisfies and
   does not satisfy.

## 2026-08-18T11:26:00Z — exact norm reduction

Put `A=G'` and `Q=G/A`. Since `G` is metabelian, `A` is abelian and conjugation
turns it into a right `Z[Q]`-module; the action is well-defined because inner
conjugation by an element of `A` is trivial on `A`. For `q in Q`, put

`N(q)=1+q+...+q^(p-1)`.

If `gA=q` and `a in A`, direct collection gives

`(g a)^p = g^p a^{N(q)}`.                                      (R1)

Consequently the actual-power contribution of the single quotient coset `q` is
the canonical affine norm coset

`C(q)=g^p A^{N(q)}`; changing `g` only changes the displayed basepoint inside the
same coset. For `t in Q^p`, the complete literal fibre is

`F_t = union_{q^p=t} C(q)`.                                    (R2)

Let `H=P intersect A`. Because the *literal* power set `P` is a subgroup,
`F_t` is exactly one `H`-coset for every `t in Q^p`. In particular

`A^{N(q)} <= H` for every `q`.                                 (R3)

Also, if `w=g^p` and `h in H`, then `wh in P`, and every element of `P` has order
dividing `p`. Applying (R1) inside `P` yields

`H^{N(q^p)}=1` for every `q in Q`.                              (R4)

For `xA=q`, `yA=r`, and `c=[x,y] in A`, metabelian collection gives the exact
target formula

`d=[x^p,y^p]=c^{N(q)N(r)}`.                                   (R5)

If closure supplies an actual root `z^p=x^p y^p`, put `s=zA`. Then
`s^p=q^p r^p`, so `s=qrk` for a root-dependent `k in Q[p]`. Conjugating this
*same root* by `x^p` and by `y^p`, and applying (R1), gives

`[z,x]^{N(s)N(q)}=d^{-1}` and
`[z,y]^{N(s)N(r)}=d^{r^p}`.                                   (R6)

Thus `d` lies in all three norm images
`A^{N(q)} intersect A^{N(r)} intersect A^{N(s)}`. More generally, for any
actual value `w=z^p`, conjugating `z` by every `h in P` gives the useful exact
inclusion

`[w,P] <= A^{N(s)} <= H`.                                     (R7)

The root-dependent factor `k` cannot be deleted: it is exactly the freedom among
the quotient classes contributing to the union in (R2).

## 2026-08-18T11:28:00Z — operator nonimplication certificate

The relations (R3)--(R7), including the full exponent-`p^2` norm annihilators, do
not imply `d=1` as group-ring operator identities. For every odd prime let

`M_p=F_p[S,T]/(S^p,T^p)`, `X=1+S`, `Y=1+T`, and `Z=XY`.

These are commuting automorphisms of order `p`. In characteristic `p`,
`N(X)=S^(p-1)`, `N(Y)=T^(p-1)`, and
`N(Z)=(S+T+ST)^(p-1)`. With `c=1` and
`d=S^(p-1)T^(p-1)`, one has `d != 0` and

`N(X)N(Y)c=d`,
`N(Z)N(X)(-c)=-d`,
`N(Z)N(Y)(Yc)=d`.

Indeed, after multiplication by `S^(p-1)`, every term of `N(Z)` containing `S`
vanishes and only `T^(p-1)` remains; the other equality is symmetric. Moreover
`d` is fixed by `X,Y,Z`. Every length-`p^2` norm also vanishes: if `W^p=1`, then
`N_{p^2}(W)=N(W)N(W^p)=pN(W)=0` on `M_p`.

The light deterministic checker in
`scratch/check_norm_obstruction.py` reproduced all displayed identities for
`p=3,5,7`. Its observed output has every Boolean field true. For `p=3`
specifically, `N(X)=S^2`, `N(Y)=T^2`,
`N(Z)=(S+T+ST)^2`, and the surviving value is the nonzero monomial `S^2T^2`;
there is no hidden division by `3` or binomial-valuation exception.

This datum can also be completed at the **formal fibre-support** level. Take
`H=M_p` and let the prospective value group be a central exponent-`p` extension
of `C_p^2` by `H` whose two standard lifts have commutator `d`. For the root-label
quotient take
`Q=C_(p^2)^2 x C_p^2 x C_p^m`: let its first two generators act as `X,Y`, the
next two as `X^(-1),Y^(-1)`, and the remaining dummy generators trivially. Thus
every fibre over `pQ` has arbitrarily many labels with identity action (cancel the
distinguished action using the next two generators), whose norm cosets are
singletons because `pM_p=0`. With `m` large enough, arbitrary formal basepoints
fill every `H`-fibre, while the distinguished `X,Y,Z` norm cosets lie inside the
same fibres. Hence the literal support/coset rows themselves remain compatible
with `d != 0`.

This is deliberately **not a group** and not a counterexample: no single
associative extension cocycle has been supplied whose complete power map realizes
the formal basepoints. It isolates the exact missing input. Once root actions and
basepoints vary across (R2), norm algebra plus support closure leaves a nonzero
socle commutator; any continuation must impose global factor-system/power-map
coherence, which is a representation change from the named norm-only lane.

## 2026-08-18T11:30:02Z — active work stop and outcome

`PARTIAL_RESULT`. The exact interval `11:10:02Z--11:30:02Z` is 20 newly elapsed
active minutes, so the proposed cumulative ledger is `937 + 20 = 957`. The named
`METABELIAN-GROUP-RING-NORM` lane has met its operator-nonimplication gate. The
remaining 25 authorized minutes are returned to Lead; no replacement strategy is
started without a Lead decision.

The attempted current-edition corpus lookup failed because the protocol's
`kourovka-21-corpus.jsonl` path is absent in this vault; only the issue-20 corpus is
present. This does not affect the source gate: the rendered issue-21 PDF and the
independently audited revision-2 scope were read, and external staleness remained
deferred under the discovery-blind instruction.

## 2026-08-18T11:31:05Z — accounting correction

The preceding 20-minute figure omitted the mandatory protocol, scope, roster,
decision, inbox, and rendered-source inspection performed from the rostered spawn
time. Charge that work. The corrected active interval is
`11:04:43Z--11:30:02Z`, exactly 25 minutes 19 seconds. On the integer ledger this
is 25 completed newly elapsed minutes, so the corrected proposed cumulative value
is `937 + 25 = 962`; 20 authorized minutes remain unused. This supersedes only the
elapsed-time row, not the mathematical outcome.

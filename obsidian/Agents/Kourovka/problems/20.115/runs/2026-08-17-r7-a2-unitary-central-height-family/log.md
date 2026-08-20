---
title: "Kourovka 20.115 cycle 7 — A2 unitary central-height family log"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
direction: proof
strategy: A2-UNITARY-CENTRAL-HEIGHT-FAMILY
active_assignment_answered: no
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/draft]
---

# Cycle 7 log

## Active-time ledger

- `2026-08-17T23:55:28Z` — work started at inherited cumulative active time `00:56:50`; cap for this lane `00:45:00`, so absolute cumulative cap `01:41:50`.
- `2026-08-18T00:02:43Z` — strategy stopped after `00:07:15` charged;
  cumulative active time `01:04:05`.  State: `awaiting_lead`.

## Source, scope, and admissibility gate

The two mandatory protocol files, revision-1 canonical scope, source synthesis,
and the independently replicated `SU_3(5)` bridge were read in full before
mathematics.  The configured PDF was rendered at printed page 161 and visually
checked.  Correct source transcription:

> Let `chi` be a complex irreducible character of a finite group `G`.  If
> `chi(x) != 0` for some `x in G`, must the exact order `o(x)` divide
> `|G|/chi(1)`?  This is known for solvable `G`; for arbitrary `G` the printed
> contextual bound is `(o(x)chi(1))^4 | |G|^5`.

`source_transcription_checked: yes`.  Corpus flags are `answered: false`,
`has_editor_comment: false`, and `has_later_comment: false` (the corpus's page
field says 162 while the rendered printed page is 161).  Open-web staleness work
is forbidden in this lane; the only solution-bearing input admitted by the
assignment is the reviewed bounded bridge
`Agents/Kourovka/problems/20.115/verification/2026-08-17T234711Z-su35-central-height.md`.
`external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`.

Clause matrix:

| clause | active here | status |
|---|---:|---|
| universal ordinary irreducible nonzero-value implication | yes | not answered |
| solvable-group context | no | context only |
| fourth-power/fifth-power bound | no | excluded |
| `SU_3(q)` central-height bridge | auxiliary only | a family result, if obtained, is partial |

All six canonical constraint rows were reconciled.  The proposed auxiliary
bridge narrows the universal quantifier and Proposition 3.2 narrows the
conclusion to a prime part of an order modulo the center; hence
`active_scope_checked: yes` and `active_assignment_answered: no` throughout.

## Strategy portfolio

1. **Theoretical, selected:** derive the Sylow-three group and the exact
   height/exponent inequality for `L=SU_3(q)`, `3|(q+1)`, then determine exactly
   which block data are still needed.
2. **Structured family:** express a Sylow subgroup as the unitary diagonal
   torus's 3-part semidirect a Weyl 3-cycle; this should make the quotient
   exponent transparent.
3. **Catalogue/small case:** expressly disallowed; `q=5` is already replicated
   and another table cannot prove a parameter family.
4. **Certificate plan:** a valid family result needs a hand derivation of the
   Sylow quotient and a citable uniform ordinary 3-block theorem specifying all
   nonabelian-defect blocks and their height maxima, including restriction from
   `GU_3(q)` to `SU_3(q)` and disconnected semisimple-centralizer cases.

Kill criterion: if that uniform generic block theorem cannot be established from
the admitted sources, stop after recording its exact required statement; do not
infer block membership or heights from the `q=5` table.

## Parameter gate

Let `a=v_3(q+1)>=1`.  Since `q=-1 (mod 3)`, LTE gives

```text
v_3(q^3+1)=a+1,       v_3(q^2-1)=a,
|SU_3(q)|_3=3^(2a+1).
```

In the standard unitary diagonal torus, let

```text
T_3 = {diag(u1,u2,u3): ui^(q+1)=1, u1*u2*u3=1}_3
    ~= C_(3^a) x C_(3^a).
```

A permutation matrix for a Weyl three-cycle normalizes `T_3`.  Hence
`P=T_3 semidirect C3` has order `3^(2a+1)` and is Sylow.  The center is the
scalar subgroup `Z=Z(L)=C3 <= T_3`.  Every element outside `T_3` has cube one:
for the cycle `w`,

```text
(t w)^3 = t * w(t) * w^2(t) = diag(u1*u2*u3, u1*u2*u3, u1*u2*u3) = 1.
```

The coset of `diag(alpha,alpha^(-1),1)`, with `alpha` of order `3^a`,
still has order `3^a` modulo `Z`.  Therefore

```text
|P/Z|=3^(2a),          exp(P/Z)=3^a,
|P/Z|/exp(P/Z)=3^a.                         (1)
```

This includes `a=1`; the last noncentrality check is
`diag(omega,omega^(-1),1)` not scalar.

For any ordinary 3-block `B`, the central-Brauer-pair argument in the reviewed
bridge gives `Z<=D` for a defect group `D`.  Put

```text
|D|=3^d,  exp(D/Z)=3^e,  theta(1)_3=3^((2a+1)-d+h).
```

The exact identity is

```text
(|L:Z|/theta(1))_3 = 3^(d-1-h),
exp(D/Z) <= (|L:Z|/theta(1))_3
  iff h <= d-1-e
  iff 3^h <= |D/Z|/exp(D/Z).                (2)
```

Thus the principal block (`D=P`) requires exactly `h<=a`, not merely height
zero.  For an arbitrary defect group the exponent is a divisor of `3^a`, but
its exact value depends on `D cap T_3`; it cannot be read from the defect
number alone.  Two useful structural checks are:

| candidate defect shape | `d` | `exp(D/Z)` | threshold `|D/Z|/exp(D/Z)` |
|---|---:|---:|---:|
| `P=T_3 semidirect C3` | `2a+1` | `3^a` | `3^a` |
| full torus `T_3` | `2a` | `3^a` | `3^(a-1)` |
| cyclic `C_(3^b)` containing `Z` | `b` | `3^(b-1)` | `1` |
| `Z` | `1` | `1` | `1` |

The last three rows are group-theoretic shapes, not an asserted exhaustive list
of block defects.

## Which blocks can fail

If `D` is abelian, the Brauer height-zero theorem gives `h=0` for every
ordinary character in `B`; equation (2) then passes automatically because
`exp(D/Z)` divides `|D/Z|`.  Consequently only blocks with **nonabelian** defect
can fail the central-height condition.  In particular:

- the principal block fails exactly if it has a character of height `h>a`;
- any nonprincipal nonabelian-defect block would require its own exact pair
  `(d,e)` and could fail exactly at a character with `h>d-1-e`.

The `q=5` replication establishes neither the absence of the second family for
other `q` nor the first height bound uniformly.

## Early-stop gate: exact missing theorem

The admitted sources do not contain a generic ordinary 3-block classification
for `SU_3(q)` when `3|(q+1)` and `3` divides the center.  A sufficient uniform
statement, and the precise missing input, is:

> For every prime power `q>2` with `a=v_3(q+1)>=1`, every nonprincipal
> ordinary 3-block of `SU_3(q)` has abelian defect, and every character in the
> principal 3-block has height at most `a`.

Together with (1)--(2) and Brauer height zero, this statement would establish
Condition `(double-dagger-star)` for every 3-block.  It must include the passage
from generic `GU_3(q)` data to `SU_3(q)` (block/character restriction and
possible splitting) and the projective semisimple classes with disconnected
centralizer at the central prime 3.  A generic degree list without block
membership does not supply it.

No self-contained derivation of that classification is available from the
locked scope and reviewed `q=5` bridge, so the strategy's stated kill criterion
fires here.  In particular, the tempting extrapolation "all nonprincipal blocks
are toral/abelian and the principal heights are at most `a`" is recorded only as
the missing theorem, not as a result.

Cycle outcome: `PARTIAL_RESULT` (exact conditional reduction plus a precise
generic-block-theorem gap), with `active_assignment_answered: no`.

## Conditional Proposition 3.2 consequence and exception

If the missing block theorem is supplied, then for every `q>2` in the parameter
range and every finite `H` satisfying **all** Proposition 3.2 hypotheses

```text
L=[H,H]=SU_3(q) quasi-simple,
Z(L)=Z(H),
chi in Irr(H) faithful,
h in H, chi(h)!=0,
H=<L,h>,
```

the proposition gives only

```text
o(h Z(H))_3 divides (|H:Z(H)|/chi(1))_3.
```

It does not give the full order divisibility in the source question.  The
parameter `q=2` is an unavoidable exception to this Proposition 3.2 family:
`SU_3(2)` is not quasi-simple, so the cited proposition cannot be invoked even
if its block inequality happened to hold.

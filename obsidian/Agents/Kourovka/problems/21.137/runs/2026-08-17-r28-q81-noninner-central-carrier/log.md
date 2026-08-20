---
title: "Run log — Q81 noninner central carrier"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
direction: counterexample
strategy: Q81-NONINNER-CENTRAL-CARRIER
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - project/kourovka
  - status/draft
active_assignment_answered: no
---

# Scope guard

Every entry concerns only odd `p>2`, a finite same-`p` group of exponent
exactly `p^2`, the literal actual set `{g^p:g in G}` rather than the subgroup
it generates, the hypothesis that this literal set is itself a subgroup, and
the question whether that subgroup is abelian.  The `p=2`, exponent-eight
sibling is excluded.

## 2026-08-17T22:55:22Z — work start

- Official cumulative ledger at start: `675` active minutes.
- Authorized cap: `55` additional active minutes, through at most `730`.
- Read in the required order: common protocol; problem-agent protocol;
  canonical revision-2 scope; clean brief; selected MathExpert portfolio; Lead
  decision.
- Frozen strategy: one `p=3` datum with
  `K=3_+^(1+4) x C3^2`, `Q81=H_3(3) x C3`, and exactly the displayed
  `alpha_X`, `alpha_Y`, `alpha_W`, with `alpha_Z` derived.

## Action gate

- Reconstructed `K` as a class-two symplectic central product and represented
  every `(M,T,L)` as the block matrix `[[M,0],[L,T]]`.
- Fixed function-composition and commutator conventions explicitly before
  evaluating words.
- Derived `alpha_X^3=(I,I,a c)` and
  `alpha_Y^3=(I,I,b c)`, where `a(v)=omega(e1,v)` and
  `b(v)=omega(f1,v)`.  These are nonzero inner labels with symplectic pairing
  one, so the cube-label gate itself passes.
- Derived
  `alpha_Z=(I,I,(b-a)c+(a+b)s-a t)`.
- Found the required centrality word
  `[alpha_X,alpha_Z]=(I,I,a s+(b-a)c)`.  On `f1` this shifts the central
  coordinate by `s-c`; the `s` component proves it is non-inner.
- Therefore the frozen outer classes do not satisfy `[x,z]=1` in `Out(K)`.
  A factor system cannot repair an outer-action relation.
- Hard kill fired before projected-support, factor-system, or exact-group
  phases.  No solver/enumeration/heavy command was run and no lease was needed.

## Packaging

- Exact hand certificate:
  `Agents/Kourovka/problems/21.137/runs/2026-08-17-r28-q81-noninner-central-carrier/action-word-certificate.md`.
- Outcome:
  `Agents/Kourovka/problems/21.137/runs/2026-08-17-r28-q81-noninner-central-carrier/outcome.md`.
- Outcome vocabulary: `STRATEGY_EXHAUSTED` for the named frozen datum only.
- `active_assignment_answered: no`; the universal scope remains open.

## 2026-08-17T23:04:53Z — work stop

- Charged active time: `10` minutes (reading, hand derivation, inspection, and
  packaging).
- Official cumulative ledger on return to Lead: `685` minutes.
- Unused part of this 55-minute allocation returned: `45` minutes.
- State: `awaiting_lead`; no replacement strategy started.

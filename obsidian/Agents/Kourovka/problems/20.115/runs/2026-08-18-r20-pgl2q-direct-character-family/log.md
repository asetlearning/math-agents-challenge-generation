---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/draft
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
direction: proof
cycle: 20
strategy: PGL2Q-DIRECT-CHARACTER-FAMILY
---

# Cycle 20 — direct PGL(2,q) character family

## Active-time ledger

- Start: `2026-08-18T10:55:59Z`; inherited detailed cumulative active time `07:36:44`; newly elapsed `00:00:00`.
- Stop: `2026-08-18T11:03:16Z`; newly elapsed `00:07:17`; detailed cumulative active time `07:44:01`.  The lane stops to submit a candidate family partial for independent review, not because the strategy was abandoned.

## Assignment fidelity

Target: for every odd prime power `q>=5`, every ordinary irreducible complex character `chi` of `PGL(2,q)`, and every `x` with `chi(x) != 0`, prove or refute `o(x) chi(1) | |PGL(2,q)|`. Both `PSL(2,q)` and its diagonal outer coset are included. Earlier unreviewed family findings are not premises.

## Result

`findings.md` derives the complete four-type element inventory and the complete
linear/Steinberg/principal/cuspidal ordinary-character table.  Character support
then gives the divisibility immediately by degree: degrees `q`, `q+1`, and `q-1`
are supported respectively on semisimple types, split-plus-unipotent types, and
nonsplit-plus-unipotent types.  The note explicitly handles exact cyclotomic
cancellation, the unique self-twist row whose restriction to `PSL(2,q)` splits,
all outer-coset orders, and the `q=5,9` cases.

Outcome: `PARTIAL_RESULT`; `active_assignment_answered: no` because the universal
all-finite-groups quantifier remains open.

---
title: "Run log — CHAR-GALOIS-WEYL"
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: CHAR-GALOIS-WEYL
direction: proof
active_assignment_answered: no
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/character-theory
  - project/kourovka
  - status/draft
---

# Run log

## Active-time ledger

- `2026-08-18T00:12:04Z` — research start at official cumulative minute 717.
- `2026-08-18T00:19:56Z` — research stop after packaging: `8` active minutes,
  official cumulative minute `725`.  The minute-18 scalarization gate hard-killed
  on alternative (B), returning `40` unused minutes to Lead.

## Evidence boundary

Read in full before mathematics:

1. `_meta/agents/Kourovka/_common-kourovka.md`;
2. `_meta/agents/Kourovka/problem-agent-kourovka.md`;
3. `Agents/Kourovka/scopes/21.137-odd-prime-exponent-p2.json`;
4. `Agents/Kourovka/problems/21.137/ideas/2026-08-18-post-r4-faithful-character-portfolio.md`;
5. the two reviewed inputs cited by that portfolio:
   `verification/2026-08-16T181302Z-minimal-central-obstruction.md` and
   `verification/2026-08-17T164459Z-grad-pimage-jordan-reduction.md`.

The cited R4 outcome is explicitly labelled a claimant report in the selected
portfolio and was not opened.  No other solution-bearing history, web source,
computation, or `p=2`/exponent-eight material was used.

## Scope lock

The target is exactly: for every odd prime `p>2` and finite same-`p` group `G`
of exponent exactly `p^2`, if the literal set `P={g^p:g in G}` is itself a
subgroup, prove that `P` is abelian.  A generated-power subgroup is not a
substitute.  The separate `p=2`, exponent-eight clause is excluded.

## Strategy work

The minimum-counterexample facts used in the character setup were reconstructed
from the hypotheses before reliance.  A faithful irreducible complex
representation does follow self-containedly from cyclicity of `Z(G)`.

The Clifford gate does not scalarize in the required universal form.  If
`rho|P` has Clifford multiplicity `e` and `r` conjugate isotypic blocks, the
comparison between `rho|P` and `rho^sigma|P` takes values in

`End_P(V)^x = (product of r copies of GL_e(C))`,

with the quotient permuting factors and acting inwardly on multiplicity
spaces.  Changing the allowed `P`-intertwiner changes this comparison by a
nonabelian coboundary.  A block-scalar gauge along a permitted `p`-cycle
changes an apparently scalar root discrepancy into a nonconstant block tuple
while preserving every representation, root norm, trace, and Weyl identity.

This is alternative **(B)** of the minute-18 dichotomy.  The strategy therefore
hard-kills at the first gate.  The three-root gate and universal bridge are not
opened.

## Read-only command record

- `wc -l` and bounded `sed -n` calls read the two protocol files, canonical
  scope, selected portfolio, and the two reviewed inputs.  The line counts
  observed were `623`, `398`, `243`, `178`, `316`, and `503`, respectively.
- `source _meta/agents/Kourovka/paths.env; kv_now` returned the start/check
  timestamps recorded in this log.  `KOUROVKA_AUTHOR` resolved to `operator`.
- `test -e Agents/Kourovka/problems/21.137/runs/2026-08-18-r32-char-galois-weyl`
  returned status `1` before this run directory was created.

No mathematical executable or network command was run.

---
from: MathExpert
to: Problem-19.30
type: IDEA
topic: Same-order Bn/Cn pairs as counterexample targets
problem: "19.30"
refs: ["Agents/Kourovka/problems/19.30/log.md"]
needs_reply_by: none
status: done
---

## Ask

Test `O7(3)` versus `S6(3)` first as already identified in your log; if unequal, use `O9(3)` versus `S8(3)` only when both ordinary tables are installed.

## Context

General mathematical knowledge, unverified: odd-characteristic simple groups of types `B_n(q)` and `C_n(q)` have the same order while generally being nonisomorphic, so they are structurally better targets than searching unrelated same-order groups. Equality of vanishing-order sets is plausible only as a testable conjecture because the dual root data can align many element orders while different character zeros may still separate them. Falsify each target cheaply by printing one order in the symmetric difference. Most likely failure: vanishing behavior is substantially finer than order or prime-graph data and separates the pair immediately.

## Evidence

Your current log independently found `O7(3)` and `S6(3)` in CTblLib and designed the exact 60-second comparison. No sourced theorem asserting equality of their vanishing-order sets was found; do not infer it from weaker same-order recognition ambiguity.

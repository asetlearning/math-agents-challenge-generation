---
from: Validator
to: Problem-16.4
type: REPORT
topic: Multiplicity-one Szep reduction is valid
problem: "16.4"
refs: ["Agents/Kourovka/problems/16.4/log.md"]
needs_reply_by: none
status: unread
---

## Ask

You may use the multiplicity-one argument as a candidate filter, citing Fisman–Arad; do not present it as a solution of 16.4.

## Context

The argument checks line by line. For fixed `c=ab`, uniqueness makes the fiber invariant under `C_G(c)` and forces `C_G(c) <= C_G(a) intersect C_G(b)`; the reverse inclusion follows because an element centralizing both `a` and `b` centralizes `ab`. The `m=1` count and the subgroup product formula then give `|C_G(a)C_G(b)|=|G|`, hence `G=C_G(a)C_G(b)`. Since nontrivial conjugacy classes in a centerless simple group contain nonidentity elements, Szep's theorem applies and contradicts simplicity.

## Evidence

Fisman–Arad, *A proof of Szep's conjecture on nonsimplicity of certain finite groups*, J. Algebra 108 (1987), 340–354, DOI `10.1016/0021-8693(87)90107-4`; a modern statement explicitly says no finite nonabelian simple group is a product of two centralizers. This validates only `m >= 2` under the hypothetical singleton-product assumptions.

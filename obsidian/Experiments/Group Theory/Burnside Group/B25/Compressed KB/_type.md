---
name: compressed-kb
description: KB runs on the compressed {a,b,A,B,m,M} alphabet where m=CoreA and M=CoreB, targeting length reduction in the compressed domain before expanding back to raw.
domain: group-theory
project: b25
tags: [agent/exp-b25, user/maumayma, domain/group-theory, topic/b25, topic/knuth-bendix, experiment-type]
---

# Experiment Type: Compressed Alphabet KB

## What this technique is

Run kbprog on B(2,5) with an augmented 6-generator alphabet {a, A, b, B, m, M} where:
- m = CoreA = `ABabAbabABaBAbabABABabAbaBABaBAbabb` (35 chars)
- M = CoreB = `BBABabAbabABaBAbabaBABabAbaBABaBAba` (35 chars, = CoreA⁻¹ as a free-group string)

The presentation `b25_compressed_core.kbmag` encodes B(2,5) with FULL definitional equations (CoreA=m, CoreB=M as relators) plus the standard B(2,5) exponent-5 relators. This makes every kbprog-generated rule a structural consequence of B(2,5) (the step-4 gate is automatic).

## The two-level strategy

1. **Compressed phase**: compress target word (m/M introduced by greedy left-to-right scan), apply m/M-in-LHS rules for reductions in the compressed domain.
2. **Expand phase**: expand surviving compressed word back to raw alphabet, apply raw rule banks.

## Load-bearing gate (from [[b25-compressed-kb-soundness-verdict]])

Every m/M-containing rule USED in a reduction must have its expansion φ(u)=φ(v) verified in B(2,5) before use. The current `b25_compressed_core.kbmag` includes full CoreA/CoreB definitions as relators, making this gate structural for kbprog-generated rules. Verification must nonetheless be documented explicitly and routed to Validator for any math claim.

## Distinction from Biased KB Agents type

Biased KB Agents runs use the raw {a,b,A,B} alphabet. Compressed KB uses the extended alphabet. The biasing mechanism (-sw/-sp/-sk flags) is shared, but the target word for biasing is the COMPRESSED form of the target.

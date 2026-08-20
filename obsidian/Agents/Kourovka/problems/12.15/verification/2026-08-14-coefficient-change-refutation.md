---
title: "Verification — Kourovka 12.15 — coefficient-change refutation"
problem: 12.15
claim: "If a C2-valued extension class restricts trivially over complex coefficients on an abelian subgroup A, then it restricts trivially in H2(A,C2), so scalar twists lie in Hom(A,C2)."
claimant: Problem-12.15
target_object: "the coefficient-change lemma used in Steps 2 and 3 of the proposed isotropic dichotomy"
witness_object: "the nonsplit central extension C16 -> C8 with kernel C2"
witness_equals_target: proven-with-citation
citation: "none; explicit cocycle calculation below"
verification_method: "explicit cohomological counterexample and dependency audit"
tools_used: ["hand proof"]
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/cohomology, project/kourovka, status/refuted]
---

# Verification — Kourovka 12.15

## The claim

The 15:44 isotropic-dichotomy request used the following coefficient-change implication in Steps 2 and 3:

> A restriction of a \(C_2\)-valued extension class that is trivial in \(H^2(A,\mathbf C^*)\) is already trivial in \(H^2(A,C_2)\); hence the available scalar twists lie in \(\operatorname{Hom}(A,C_2)\).

The claimant's 15:47 correction retracts this implication. The retraction is mathematically necessary.

## Target vs witness

Take the central extension
\[
1\longrightarrow C_2\longrightarrow C_{16}\longrightarrow C_8\longrightarrow1.
\]
It is abelian but nonsplit, so its class is nonzero in \(H^2(C_8,C_2)\). Let \(a\) generate \(C_8\), choose the ordinary section with representatives \(0,1,\ldots,7\), and let \(c\) be its wrap cocycle. Under \(C_2=\{\pm1\}\hookrightarrow\mathbf C^*\), define a 1-cochain
\[
b(a^k)=\zeta_{16}^{,k}.
\]
The wrap factor is exactly the coboundary of \(b\) (up to the harmless reciprocal convention). Thus the pushed-forward class is zero in \(H^2(C_8,\mathbf C^*)\) even though the original \(C_2\)-class is nonzero.

This witness has the same non-elementary order-8 shape as the disputed `A=C8` branch. Analogously, \(C_8\times C_2\to C_4\times C_2\) defeats the same inference for `A=C4 x C2`.

## Sub-claims and what each method proves

1. Complex-alpha-isotropic means the restricted class vanishes **after coefficient extension to** \(\mathbf C^*\), or equivalently that the corresponding inverse image is abelian. It does not mean the marked central \(C_2\)-extension splits.
2. A complex cochain trivializing the restriction may use fourth, eighth, or higher 2-power roots. Its scalar characters need not be \(\{\pm1\}\)-valued.
3. Therefore non-elementary \(A\) is not excluded by the element of \(2A\), and a normal Lagrangian \(L\) is not forced to be \(C_2^4\).
4. The sentence “the unique nonidentity element of \(2A\)” is also literally false for \(A=C_8\), since \(2A\cong C_4\). Replacing it with “the unique involution” does not repair the coefficient-change error.

## Evidence

The explicit extension/coboundary calculation above is an actual counterexample to the coefficient lemma. No computation or assumption from the hypothetical minimum counterexample is used.

Dependency audit:

- `screen_exceptional_elementary_extensions_small.g` remains a legitimate computation only for its explicitly elementary `A=C2^3` subfamilies.
- `regular_smp16_in_agl4.g` remains a legitimate `L=C2^4` subcase computation but is not exhaustive for the Lagrangian branch.
- Claims that those scripts cover every non-Lagrangian or Lagrangian case must stop.
- Full-complex-dual calculations are not refuted by this coefficient example, but they require their own verification.

## Verdict

`status/refuted` for the coefficient-change lemma. Consequently Steps 2 and 3 of the 15:44 dichotomy are not certifiable as stated. The claimant's 15:47 correction is accepted.

## Why this verdict

The nonsplit abelian extension \(C_{16}\to C_8\) is a direct counterexample: complex isotropy and nontriviality over \(C_2\) occur simultaneously.

## What is NOT established

This refutes the stated inference, not every possible route to an elementary subgroup conclusion. It does not certify Proposition 3.2, the later full-dual five-class screen, the asserted closure of all elementary `[32,27]` branches, the later Q49 run, or the surviving Lagrangian reductions. Problem 12.15 remains `status/conjectured`.

## What would upgrade the corrected reduction

Restate every affine action using the full complex character group \(\widehat A\), keep non-elementary `A` and `L` branches, and independently verify each full-dual orbit and extension certificate. No conclusion may rely on the retracted `Hom(A,C2)` restriction.

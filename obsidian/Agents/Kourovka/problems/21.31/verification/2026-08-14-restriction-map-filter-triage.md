---
title: "Verification triage — Kourovka 21.31 — automorphism-component restriction filter"
problem: "21.31"
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/holomorphs, project/kourovka, status/conjectured]
---

# Verification triage — Kourovka 21.31 — automorphism-component restriction filter

## Claim

For any compatible order-2016 target realization, the automorphism component of the induced regular embedding of the actual subgroup (H=M_*<G) into `Hol(M)` must extend along that actual inclusion to a homomorphism (G\to Aut(M)); failure of extension is therefore a necessary obstruction.

## Target vs witness

The Kourovka target is every regular subgroup of `Hol(N)` for arbitrary finite soluble `N`. The proposed witnesses are five abstract `H` types, 46 order-252 `M` types, regular embeddings, nine conditional overgroups, and marked inclusions. They are only a finite conditional universe for hypothetical order 2016. Witness equals target: false; overall status is capped at `conjectured`.

## Sub-claims

1. A target realization makes `M` invariant under the automorphism component of every element of `G`.
2. Restricting those automorphisms to `M` gives a homomorphism `lambda_G:G->Aut(M)` whose restriction along the actual inclusion `i:H->G` is exactly `lambda_H`.
3. The finite universe must include all soluble order-252 `M`, all regular embeddings `H->Hol(M)`, all nine overgroups, and every relevant inclusion orbit `H<G`.
4. The equivalence relation must act simultaneously on the marked inclusion and regular embedding; independent quotienting by `Aut(H)` is potentially unsound.
5. Complete enumeration of regular embeddings requires both action homomorphisms and bijective crossed maps/complements, with a proved orbit correspondence.
6. Automorphism-component extension is necessary but not sufficient; translation/cocycle and additive-extension compatibility remain.
7. An exhaustive negative certificate must give complete input counts, canonical representatives or orbit proofs, every restriction-image result, and reproducible transcripts.

## Tools and methods inventory

- Hand proof from the holomorph multiplication law and `G`-invariance of `M`: proves necessity only.
- GAP 4.12.1 / SmallGrp 1.5.3: confirms the finite order-252 library/solubility scope and can implement later homomorphism/complement enumerations. A pass does not prove completeness unless orbit stabilizers and inclusion classes are recorded.
- Prior verified nine-overgroup classification: supplies abstract `(G,K)` classes, but not automatically all marked inclusion classes.
- Sage and Magma are unavailable; no missing tool is required for this design audit.

## Hard limits

No full regular-embedding enumeration is authorized within this 35-minute light audit. This note can validate the condition and specify a complete certificate, but cannot claim any elimination. Counts from sampled embeddings or one chosen inclusion cannot support a negative result.

## Recommendation

Accept automorphism-component nonextension as a sound necessary filter only on simultaneously marked tuples. Require the full certificate design below before treating a complete failure as an exclusion.

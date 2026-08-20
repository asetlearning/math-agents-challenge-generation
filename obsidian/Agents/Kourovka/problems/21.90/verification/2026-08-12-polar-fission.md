---
title: "Verification — Kourovka 21.90 — polar fission"
problem: 21.90
claim: "No vertex-transitive distance-regular graph with intersection array {39,25,10;1,5,30} has the explicit 300-vertex nonsquare-type perpendicularity graph over GF(5) as its distance-3 graph."
claimant: Problem-21.90
target_object: "The bounded class of vertex-transitive realizations with the stated intersection array and explicit distance-3 constituent"
witness_object: "The explicit 300-point perpendicularity graph and subgroup classes computed by GAP/GRAPE/TomLib"
witness_equals_target: unknown
citation: "none"
verification_method: "code audit plus attempted independent GAP 4.12.1 computation"
tools_used: ["GAP 4.12.1", "GRAPE 4.9.0", "TomLib"]
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/distance-regular-graphs, project/kourovka, status/conjectured]
---

# Verification — Kourovka 21.90

## The claim

The precise bounded claim in the frontmatter is coherent. It does not claim to solve Problem 21.90.

## Target vs witness

Source PDF page 177 asks for existence of any Q-polynomial distance-regular graph of diameter 3 whose distance-2 and distance-3 graphs are strongly regular. The witness computation concerns one intersection array, one explicit `srg(300,65,10,15)` constituent, and vertex-transitive fissions. Thus witness equality with the full Kourovka target is false; equality with the bounded computational target depends on completeness of the subgroup/orbital enumeration and has not been independently completed here.

## Sub-claims and what each method proves

The explicit construction and automorphism orders were independently reproduced. The index-two argument is valid: for transitive `H <= G` and `D` normal of index two, `H cap D` has at most two equal-sized orbits, hence is transitive or has two 150-point orbits. Inspection supports the outer-extension setup and the necessity of `A1*A3=10*A2+9*A3`. These checks do not independently exhaust all orbital unions.

## Evidence

Tool probe:

```text
GAP 4.12.1
grape: true
tomlib: true
atlasrep: true
Python 3.12.3
pdftotext version 24.02.0
sage: unavailable
magma: unavailable
```

Independent command:

```bash
timeout 60s gap -q Agents/Kourovka/problems/21.90/verification/scratch/independent_polar_fission_check.g > Agents/Kourovka/problems/21.90/verification/scratch/independent_polar_fission_check.out 2>&1
```

Output before timeout:

```text
vertices=300 degree=65 aut=9360000 derived=4680000
```

The independent enumeration did not finish within the cap. Two earlier attempts aborted before mathematics because my script used the read-only GAP name `X` and then called `VertexDegree` with the wrong arity; neither counts as evidence.

The claimant's completed output reports five transitive subgroup classes in `D`, three `150+150` classes, three outer transitive extensions, and zero target hits. Re-running or merely accepting that same implementation cannot satisfy the independent-computation requirement for `replicated`.

## Verdict

`status/conjectured`

## Why this verdict

The scoped argument appears mathematically plausible and no gap was found in the index-two or necessary-identity reasoning, but the decisive exhaustive search has only one completed implementation. Protocol requires multiple independent agreeing computations for `replicated`.

## What is NOT established

- Independent exhaustion of the subgroup/orbital search.
- Equality of this constituent with every `srg(300,65,10,15)`.
- Nonexistence of asymmetric realizations.
- Any answer to the literal Kourovka problem, including resolution of the convention ambiguity about degenerate/imprimitive witnesses.

## What would upgrade it

A second independently written finite enumeration that terminates and agrees, with a transcript, would support `status/replicated` for the bounded claim only.

---
title: "Hard Instance Generation — Directory Map"
author: asetlearning
language: en
tags:
  - agent/research
  - user/asetlearning
  - domain/cs
  - topic/hard-instance-generation
  - convention
  - status/draft
status: draft
domain: cs
---

# Hard Instance Generation — Directory Map

How to produce problem instances that are **hard for solvers but have a known answer**. This directory holds the non-group-theory side of that literature: planted solutions in random CSP/SAT, learned hard-instance samplers, and adversarial curricula. The group-theoretic side (hard trivial words, Andrews–Curtis presentations) lives in `Research/Group theory/`. The [[_moc-hard-instance-generation]] spans both.

## Contents

| File | Scope |
|---|---|
| `_synthesis-hard-instance-generation.md` | Cross-domain synthesis for `#project/challenge-gen` |
| `krzakala-zdeborova-2009-quiet-planting.md` | Quiet planting in random CSPs |
| `achlioptas-jia-moore-2004-hiding-assignments.md` | Hiding satisfying assignments in random k-SAT |
| `2606.15979.md` | Quiet planting for k-SAT with multiple solutions (2026) |
| `sato-2019-hisampler.md` | Learning to sample hard instances for graph algorithms |
| `dennis-2020-paired.md` | PAIRED: adversarial environment design |

## Related material

- [[_moc-hard-instance-generation]]: reading path across domains
- [[project-challenge-gen]]: the project this scan serves
- [[_moc-algorithm-cooperation]]: the SAT solvers (GRASP, ManySAT) these instances are meant to stress

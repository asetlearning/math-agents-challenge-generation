---
title: "Word Problem — Directory Map"
author: maumayma
language: en
tags:
  - agent/research
  - user/maumayma
  - domain/group-theory
  - topic/word-problem
  - convention
  - status/draft
status: draft
domain: group-theory
---

# Word Problem — Directory Map

This directory covers the word problem in finitely presented groups as a topic: decidability, specific algorithmic techniques, and target word methodology.

## Contents

| File | Scope |
|---|---|
| `decidability-landscape.md` | The word problem statement; Novikov-Boone undecidability for FPGs; decidability results for specific families (free, abelian, hyperbolic, automatic). Verbatim theorem citations. |
| `target-words.md` | What a "target word" is in our methodology (stated generally); how to construct one; how to verify equality. |
| `techniques/` | One note per technique: Knuth-Bendix completion, Dehn function, automatic groups via finite-state automata. Cross-linked to `Tools/GAP/examples/` and `Tools/KBMAG/examples/` where applicable. |
| `kapovich-2003-generic-case-complexity.md` | Paper: generic-case complexity (Kapovich–Myasnikov–Schupp–Shpilrain 2003). Word/conjugacy/membership problems are generically fast; trivial words have density zero. |
| `elder-2015-random-trivial-words.md` | Paper: Metropolis sampling of trivial words in finitely presented groups (Elder–Rechnitzer–Janse van Rensburg 2015). |

## What does NOT live here

- Tool-specific code → `Tools/GAP/` or `Tools/KBMAG/`
- Foundational group definitions → `General/basics/`
- Paper summaries about specific word-problem results → `Open problems/` or `Burnside groups/`

## Status

Content populated in F6.2.

## Related material
- [[myasnikov-ushakov-2011-random-van-kampen]]: random van Kampen diagrams and the depth filling function

- [[group-theory-overview]] — parent: Research/Group theory/ directory map
- [[_moc-word-problem]] — the word-problem MOC (this overview is the entry point; MOC is the reading path)
- [[decidability-landscape]] — core content: what's decidable and what's not
- [[target-words]] — core content: what target words are and how to verify them
- [[knuth-bendix]] — main technique: KB completion as word-problem algorithm
- [[dehn-function]] — technique: Dehn function and hyperbolic groups
- [[automatic-groups]] — technique: automatic group structure
- [[kapovich-2003-generic-case-complexity]] — paper: generic-case complexity of decision problems; why random words are almost never trivial
- [[elder-2015-random-trivial-words]] — paper: random sampling of trivial words by a Metropolis chain

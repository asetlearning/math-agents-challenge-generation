---
title: "16.4 idea — residual PSp8(3) character-column screen"
author: operator
tags:
  - agent/math-expert
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/conjugacy-classes
  - project/kourovka
  - status/conjectured
problem: "16.4"
---

# Obstruction

From general mathematical knowledge (unverified): the main obstruction is now a classification boundary, not lack of a finite test. Published family results remove broad families, but the surviving mixed Jordan-type class pairs in higher-rank non-type-A groups still form a large search space.

# Ranked idea 1 — `S8(3)` / `PSp8(3)`

**The idea.** Screen all ordered nonidentity class pairs in the CTblLib table `S8(3)`, applying strict class-size/centralizer filters first and then the character-column identity before full structure constants. Produce one violating irreducible character for every pair as a compact exclusion certificate.

**Why it might work — cited.** Guralnick–Malle–Tiep, *Transactions of the AMS* 365 (2013), arXiv:1202.2627, report the Arad–Herzog conclusion for alternating groups, `PSL_n(q)`, and specified low-rank classical families, and report exclusions for same-type semisimple/semisimple and unipotent/unipotent pairs in all finite simple groups of Lie type. The problem log's reading of their Propositions 3.1–3.3 places `PSp8(q)` just beyond the listed symplectic coverage and identifies `S8(3)` as an installed finite edge case.

**Falsification criterion.** Kill this one-hour target if table loading fails, the optimized scan cannot certify at least 10,000 residual pairs in a five-minute pilot, or any pair survives all exact column identities without a planned bounded full-support check.

**Cost.** About one hour of active analysis; GAP/CTblLib; one leased CPU slot, under 1 GB RAM, with a 20-minute wall cap for the full scan.

**Most likely failure.** The computation may exclude one table but yield no family-level mechanism; a surviving column-compatible pair may also require expensive structure-constant evaluation.

# Why ranked first

From general mathematical knowledge (unverified): this is narrower and more informative than another covered unitary or orthogonal table, and it directly tests the first uncovered classical edge already available in CTblLib. It remains bounded evidence only and needs Validator review.

---
title: GAP (Groups, Algorithms, Programming)
kind: system-tool
upstream: https://www.gap-system.org
license: GPL-2.0-or-later
ownership: upstream-pristine
obtain: system install (e.g. `brew install gap`) or source build from gap-system.org; GAP packages via the GAP package manager
build: none
test: "`gap -q <<< 'Print(GAPInfo.Version, \"\\n\"); QUIT;'`"
versions_in_use:
  - "4.15.1 (maumayma, /opt/homebrew/bin/gap) — record `GAPInfo.Version` per run"
  - "4.15.1 (asetlearning, source build on Ubuntu 24.04 arm64; kbmag + nq compiled) — since 2026-09-30"
local_patches: []
capabilities:
  - "group theory: presentations, Tietze transformations, coset enumeration, group orders"
  - "group theory: p-quotients (EpimorphismPGroup) and nilpotent quotients (nq package) — computes in the finite/nilpotent quotient, not the free group"
  - "group theory: word problem in finite / polycyclic groups"
  - "group theory: Knuth-Bendix via the kbmag package"
heavy_processes: [gap, nq]
mcp: none
local_checkouts:
  maumayma: /opt/homebrew/bin/gap
  asetlearning: /home/parallels/Research/mixer/gap-4.15.1/gap
docs: ""
used_by: ["[[project-b25]]", "[[project-mixer-core]]"]
tags: [meta, type/reference]
---

# GAP

## What it is
The canonical computational group theory system. It is Validator's primary oracle, and the experiments use it for presentations, p-quotients (`EpimorphismPGroup`), `nq`, and word-problem checks. The packages in use are `kbmag` and `nq`; record package versions per run.

## Protected surfaces
None of our own. Treat GAP strictly as a black-box oracle. Never reimplement it (see [[_common]] § Verification ≠ experiment).

## Known pitfalls
- `EpimorphismPGroup(G,p,c)` builds a **finite p-quotient** (for exponent 5, the restricted B₀), never the free Burnside group. State which group a computation ran in.
- Abelianization checks are blind on `[G,G]`; they are never a word-equality check.

## Related material
- [[projects-and-dependencies-convention]]
- [[dep-kbmag]]
- [[validator]]

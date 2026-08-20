---
title: "Frozen validator manifest — L4(3) prime-2 block bridge"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
frozen: true
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/draft]
---

# Frozen validator manifest — `L4(3)` prime-2 block bridge

- Exact finite inputs: installed CTblLib `1.3.7` tables `L4(3)` and
  `L4(3)mod2`; GAP's documented projective-line permutation construction
  `PSL(4,3)`; the claimant's printed three-generator principal-defect certificate
  and printed order-4 block-2 certificate.
- Frozen prime and scope: only (p=2) and only the bounded bridge with derived
  subgroup centerless (L_4(3)). No catalogue query, new table, new prime, or
  search for a source counterexample is permitted.
- Block reconstruction: connected components of the bipartite support graph of
  `DecompositionMatrix(BrauerTable(...))`, followed by Cartan matrices and their
  elementary divisors. The script does not use `PrimeBlocks` or the `ordchars`
  fields of `BlocksInfo`.
- Defect-group checks: reconstruct the displayed principal subgroup and enumerate
  all 128 elements; verify the order-4 element in the same fixed permutation
  model, its centralizer size, and the unique table-class invariants. The theorem
  step identifying its cyclic subgroup as a block-2 defect group remains a hand
  implication from the separately inspected Theorem 3.5.
- Character-defect check: independently divide each integral codegree by 2 to
  compute all 29 exact valuations; compare against the certified exponents
  (8,4,1,1,1,1).
- Script:
  `Agents/Kourovka/problems/20.115/verification/scratch/l43_2block_validator.g`.
- Frozen script SHA-256:
  `3067ca1baa200701f3868dda1ee3974de49bc6b6b7d70c4eb7665d14a84c888c`.
- Exact command:
  `timeout 45s gap -q -b Agents/Kourovka/problems/20.115/verification/scratch/l43_2block_validator.g`.
- Wall cap: 45 seconds. Estimated use: under 10 CPU seconds and under 300 MB RAM.
  This is a genuinely lightweight bounded exact rerun, below the protocol's heavy
  threshold, so no compute-slot lease is required.
- Required result: exit zero; six support components with rows
  `[1..15,20..22,27..29]`, `[16..19]`, `[23]`, `[24]`, `[25]`, `[26]`;
  defects `7,2,0,0,0,0`; displayed principal group size/exponent `128/8`;
  order-4 certificate with centralizer `1440`, unique class `4a`, and row-16 value
  `16`; exactly 29 passing character-defect inequalities; all assertions pass.
- Hard stop: any timeout, assertion failure, table/version/object mismatch,
  extra/missing component or row, failure of the explicit subgroup certificates,
  or failed inequality ends the run without tuning or widening.

The theorem artifact is fixed separately at SHA-256
`a2825c5bfed0c8d340893b3b8bcfd62f89b1e94c7d170e13f4df34198357e96f`.

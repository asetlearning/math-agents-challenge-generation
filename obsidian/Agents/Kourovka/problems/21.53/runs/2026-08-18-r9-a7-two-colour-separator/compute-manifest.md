---
author: operator
tags: [agent/problem, user/operator, domain/group-theory, topic/kourovka, topic/coloured-graphs, project/kourovka, status/draft]
problem: "21.53"
scope_id: 21.53/two-minimal-prime-colours
assignment_revision: 2
---

# Frozen compute manifest — A7 two-colour/full-colour comparison

## Exact command requested

```bash
/usr/bin/time -v -o Agents/Kourovka/problems/21.53/runs/2026-08-18-r9-a7-two-colour-separator/a7_two_colour_gap_v4.resource.txt timeout 90s gap --quitonbreak -q -b Agents/Kourovka/problems/21.53/runs/2026-08-18-r9-a7-two-colour-separator/a7_two_colour_gap.g > Agents/Kourovka/problems/21.53/runs/2026-08-18-r9-a7-two-colour-separator/a7_two_colour_gap_v4.stdout.txt 2> Agents/Kourovka/problems/21.53/runs/2026-08-18-r9-a7-two-colour-separator/a7_two_colour_gap_v4.stderr.txt && test ! -s Agents/Kourovka/problems/21.53/runs/2026-08-18-r9-a7-two-colour-separator/a7_two_colour_gap_v4.stderr.txt && tail -n 1 Agents/Kourovka/problems/21.53/runs/2026-08-18-r9-a7-two-colour-separator/a7_two_colour_gap_v4.stdout.txt | grep -Fxq 'FINAL_SUCCESS_SENTINEL=A7_TWO_COLOUR_CHECK_V4_PASS'
```

This single line is the complete requested invocation, including the exact
wrapper, all three redirections, a zero-length-stderr gate, and an exact final-line
success-sentinel gate.  It is run at most once and without edits.  GAP's
`--quitonbreak` option makes any uncaught GAP error terminate nonzero rather than
entering a recoverable break loop.

## Frozen scope and bounds

- Exactly `A_7` in its natural degree-seven action and the conjugacy class of
  `(1,2)(3,4)`; no catalogue expansion.
- Exhaustively enumerates all 105 vertices and all 5,460 unordered distinct
  pairs.
- Builds two finite incidence gadgets: 2,415 vertices for the exact order-2 and
  order-3 relation stabilizer; 5,565 vertices for the full five-colour group.
- Calls the documented GRAPE signature
  `AutGroupGraph(graph, colourclasses)` explicitly for each gadget.  The ordered
  partition separates original vertices and every edge-node colour class.
- Every unordered-pair loop has the explicit outer bound `1..n-1`; this avoids
  GAP's descending-range semantics at `i=n`.
- GRAPE calls nauty/dreadnaut once per gadget and restricts each result to the
  original 105 vertices.
- Hard wall timeout: 90 seconds.  Estimate: one CPU, under 30 CPU seconds and
  under 512 MiB RAM; lease requested for five portable minutes.
- Kill criterion: timeout, RSS approaching 1 GiB, malformed group restriction,
  or any failed exhaustive relation audit.  No repair or rerun without a new
  frozen hash and Lead decision.

## Acceptance gates

All are mandatory: the exact shell line returns zero; the resource record says
exit status zero; stderr has byte length zero; stdout's last line is exactly
`FINAL_SUCCESS_SENTINEL=A7_TWO_COLOUR_CHECK_V4_PASS`; and all expected group,
inventory, generator-audit, and comparison tags occur before that line.  Failure
of any gate means `FAILED_RUN_NO_RESULT` even if some earlier text was printed.

## Certificate semantics

The edge-node colour classes force automorphisms to preserve `E_2` and `E_3`
separately (or every occurring colour for the full gadget).  Unique edge-node
neighbourhoods make restriction to the 105 original vertices faithful.  The
checker independently audits every returned generator on every relevant edge.
If the comparison is strict, it prints one generator outside the full group,
all 105 images, exhaustive order-2/order-3 edge counts and failure counts, and
the first exact product-order change.

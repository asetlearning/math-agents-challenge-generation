---
author: operator
tags:
  - agent/math-expert
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - topic/word-maps
  - project/kourovka
  - status/conjectured
problem: "21.137"
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
strategy_id: NOTT3-N2-N14-CUBESET
status: conjectured
---

# Final-40 strategy: one truncated-substitution group

## Scope and blind boundary

Target only `21.137/odd-prime-exponent-p2`, revision 2: for odd prime `p`, a
finite same-`p` group `G` has exponent exactly `p^2`; the complete actual value
set `P={g^p:g in G}` is assumed to be a subgroup; decide whether `P` must be
abelian. Excluded: `p=2`, the exponent-8 sibling, the general powerfulness
clause, generated power subgroups, and groups of the wrong exponent.

I used only the request and the revision-2 canonical scope record. I did not
open the linked run/verification notes, use web or literature search, or inspect
hidden/wreath material. The canonical record says `scope_answered:false`; it
does not record a reviewed full-scope proof or counterexample.

## Obstruction

The actual-value-set condition is global: local root identities and large
generated power subgroups do not certify that every product of two values is
again one value. The last 40 minutes therefore need one group whose entire
power map is small enough to enumerate, while its power values can still have a
nonzero commutator.

## Selected route — `NOTT3-N2-N14-CUBESET`

Freeze `p=3` and exactly one carrier. Let

`A=F_3[t]/(t^14)` and

`T={f_a(t)=t+a_3t^3+a_4t^4+...+a_13t^13 : a_i in F_3}`,

with `f*g=f(g(t)) mod t^14`. Represent an element by its eleven-coordinate
tuple `(a_3,...,a_13)`. Thus the complete carrier has `3^11=177147` tuples; no
subgroup selection, relator choice, cocycle row, or parameter search is allowed.
Compute the complete actual cube map `a -> f_a^3` on this carrier.

General mathematical knowledge, unverified: this is a finite truncated
substitution (Nottingham-filtration) group. Ramification-depth heuristics make
this truncation a sharply chosen boundary: ninth powers should disappear before
degree 14, while commutators of lowest-depth cube values can first remain visible
near the top degree. These are only motivation. The exhaustive exponent and
commutator gates below must decide the relevant facts; the heuristic is not
evidence.

## Why this is materially new

The representation is nonlinear substitution under composition. It does not
vary the exhausted UT7/algebra rows, extension/cocycle rows, holomorph generators,
central-product repair, root-fibre gauge/marks, or pair/triple-root observables.
It is one complete finite group, not a catalogue or a formal value map, and it
does not use a wreath construction. A hit at `p=3` would face every target row
directly.

## Exact 40-minute gates

All times are cumulative active minutes from activation.

1. **G0, by +6:** freeze the tuple codec and composition orientation; enumerate
   exactly 177147 distinct tuples; check identity and computed inverse for every
   tuple. Failure or an unfrozen convention kills the route.
2. **G1, by +12:** exhaust all tuples and require `f^9=t`; also exhibit one tuple
   with `f^3 != t`. Any surviving ninth power, or absence of an order-nine
   element, is an exact wrong-exponent kill.
3. **G2, by +22:** write the complete input-to-cube table and deduplicate it to
   the literal set `P`. If `|P|` is not a power of 3, stop with the table and
   cardinality certificate. A power-of-3 size is only a necessary gate, never a
   subgroup conclusion.
4. **G3, by +31:** test every ordered pair in `P x P` by tuple composition and
   membership in the complete cube-image hash. The first missing product is the
   closure-defect artifact and kills this carrier. Identity and inverse membership
   must also be recorded explicitly.
5. **G4, by +35:** only if G3 passes, exhaust ordered pairs for commutativity.
   If all commute, this is an out-of-scope commuting example and the route stops.
   A hit must give two explicit roots `r,s`, their cube tuples `r^3,s^3`, and the
   two unequal products.
6. **G5, by +40:** package the manifest, hashes, counts, witnesses, exact command,
   and the revision-2 constraint-and-conclusion matrix. On a G4 hit, stop research
   as a prospective candidate claim and route it to Lead for the review circle.
   On any earlier hard gate, hand unused minutes back immediately; that is a stop
   for `NOTT3-N2-N14-CUBESET`, never authority to park the scope.

## Command and resource envelope

After writing the small bespoke tuple enumerator, request one heavy lease and run:

```bash
timeout 1500s python3 Agents/Kourovka/problems/21.137/scratch/nott_n2_n14_cube.py --p 3 --lowest-degree 3 --truncate 14 --exhaustive --artifact-dir Agents/Kourovka/problems/21.137/scratch/nott-n2-n14
```

Envelope: one CPU core, at most 2 GB RAM, 25-minute timeout, 30-minute lease.
No general-purpose system or unbounded enumeration is needed.

## Success artifact

A candidate counterexample artifact consists of the fixed substitution-group
definition; the complete 177147-row cube manifest; exhaustive ninth-power count
and one order-nine witness; the literal deduplicated cube set; zero closure misses;
and explicit noncommuting cube values with roots. It must additionally carry one
evidence row for every revision-2 constraint, including equality with the actual
cube set rather than its generated subgroup.

## Falsification and self-critique

The most likely failure is that the cube image is either nonclosed or becomes
abelian at the critical top layer. A second risk is that the depth heuristic is
off by one and the carrier contains an element of order 27; G1 deliberately kills
that before closure work. The 177147-row carrier is larger than prior single-row
experiments, so an inefficient symbolic-polynomial implementation could time out;
fixed-length base-3 tuples and truncated coefficient convolution are required.
No experiment or mathematical computation was performed for this proposal.

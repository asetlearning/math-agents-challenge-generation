---
title: "Verification — Kourovka 20.115 — SU3(5) central-height bridge"
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
scope_record: Agents/Kourovka/scopes/20.115-nonzero-character-order-divisibility.json
assignment_revision: 1
claim: "For L=SU_3(5), p=3, and Z=Z(L), all seven ordinary 3-blocks satisfy p^h <= |D/Z|/exp(D/Z), so Proposition 3.2 gives exactly its prime-three conclusion for H with [H,H]=L under every stated hypothesis."
claimant: Problem-20.115
target_statement: "For every finite G, chi in Irr(G), and x in G, chi(x) nonzero implies o(x)chi(1) divides |G|."
excluded_scopes: ["other finite groups", "other primes", "full element order rather than the 3-part of order modulo the center", "universal conclusion"]
target_object: "bounded auxiliary target L=SU_3(5)=3.U3(5) at p=3"
witness_object: "CTblLib ordinary table 3.U3(5) and GAP's exact SU(3,5) matrix group"
witness_equals_target: proven-with-citation
citation: "Standard SU_3(5)=3.U3(5) realization; Malle--Navarro--Tiep, arXiv:2605.04513v1, Conjecture 2.3, Proposition 3.2, and Theorem 3.5"
verification_method: "hand proof plus separately written bounded GAP 4.12.1 checker"
tools_used: ["GAP 4.12.1", "CTblLib", "Python 3.12.3 environment probe only"]
scope_answered: ["bounded auxiliary family [H,H]=SU_3(5), prime 3, with all Proposition 3.2 hypotheses"]
scope_not_answered: ["20.115/nonzero-character-order-divisibility"]
active_assignment_answered: no
author: operator
tags: [agent/validator, user/operator, domain/group-theory, topic/kourovka, topic/character-theory, project/kourovka, status/replicated]
---

# Verification — Kourovka 20.115 — SU3(5) central-height bridge

## Verdict

`status/replicated` for the submitted bounded prime-three family result.  A
separately written checker reconstructs the literal matrices and independently
reproduces all seven block rows, all 40 character rows, and the quotient
exponents `3,3,1,1,1,1,1`.  The Brauer-pair step, height identity, block-2
support inference, and Proposition 3.2 application also survive hostile
reconstruction.

This does **not** answer the active universal assignment:
`active_assignment_answered: no`.

## Scope, revision, and clause matrix

The locked scope is revision 1 of
`20.115/nonzero-character-order-divisibility`.

| source clause | active | result of this verification |
|---|---:|---|
| universal ordinary-character divisibility question | yes | not answered; only one derived-group family and one prime |
| known solvable-group context | no | not addressed |
| weaker fourth-power/fifth-power bound | no | not addressed |

The bounded result is not a direct character-table screen of every extension
`H`.  It verifies a sufficient block hypothesis for `L`; the passage to `H`
is exactly the cited Proposition 3.2 and retains all of its hypotheses.

## Constraint-and-conclusion matrix

| constraint id | role | required source condition | checked bounded use | result for active scope |
|---|---|---|---|---|
| `20.115-forall-G-chi-x` | admissibility | every admissible triple | only finite `H` with derived group `SU_3(5)`, at `p=3` | fail as universal coverage |
| `20.115-G-finite` | admissibility | `G` finite | Proposition 3.2 assumes finite `H` | pass only in bounded family |
| `20.115-chi-complex-irreducible` | admissibility | ordinary irreducible complex character | faithful `chi in Irr(H)` is retained | pass only in bounded family |
| `20.115-x-in-G` | admissibility | element of the group, exact order | `h in H`, but conclusion concerns `o(hZ(H))_3` | narrower than source row |
| `20.115-character-value-nonzero` | admissibility | exact nonzero value | exact `chi(h) != 0` is retained | pass only in bounded family |
| `20.115-order-degree-divisibility` | target conclusion | full `o(x)chi(1) | |G|` | only `o(hZ(H))_3 | (|H:Z(H)|/chi(1))_3` | not established |

The failed universal and full-conclusion rows mechanically force
`active_assignment_answered: no`.

## Target versus witness

The source target quantifies over every finite group.  The submitted target is
the explicitly narrower auxiliary statement for `L=SU_3(5)` at `p=3`.

GAP's `SU(3,5)` is the standard special unitary matrix realization.  The order
formula

```text
|SU_3(5)| = 5^3(5^3+1)(5^2-1) = 378000
```

and `|Z(SU_3(5))|=gcd(3,6)=3` agree with the fresh matrix checks.  The quotient
has order `126000`; the perfect triple cover is the group conventionally named
`3.U3(5)`, the exact CTblLib identifier used here.  Thus the matrix witness and
ordinary table address the bounded target, not an approximation or a finite
quotient of it.  The computation remains conditional on GAP/CTblLib's installed
exact data, as any such database replication does.

## Central subgroup and exact height identity

Let `B` be a `p`-block of a finite group `L`, with block idempotent `e_B` over
an algebraically closed field of characteristic `p`, and let
`Z <= Z(L)` be a central `p`-subgroup.  Since `C_L(Z)=L`, the Brauer map

```text
Br_Z : (kL)^Z -> kC_L(Z)
```

keeps every group-basis coefficient.  Hence `Br_Z(e_B)=e_B != 0`, and
`(Z,e_B)` is a `B`-Brauer pair.  It is contained in a maximal `B`-Brauer pair
`(D,e_D)`, whose first component is a defect group.  Therefore `Z<=D` for one
defect group.  All maximal `B`-Brauer pairs are conjugate and `Z` is central,
so every conjugate defect group also contains `Z`.

Write `|L|_p=p^a`, `|D|=p^d`, `|Z|=p^z`, and let
`theta in Irr(B)` have height `h`.  By the definition of height,

```text
theta(1)_p = p^(a-d+h).
```

Consequently

```text
(|L:Z|/theta(1))_p
  = p^(a-z-(a-d+h))
  = p^(d-z-h)
  = |D/Z|/p^h.
```

If `exp(D/Z)=p^e`, then

```text
exp(D/Z) <= (|L:Z|/theta(1))_p
iff p^e <= p^(d-z-h)
iff p^h <= p^(d-z-e)
iff p^h <= |D/Z|/exp(D/Z).
```

This is an equivalence, not merely a necessary estimate.  In the present case
`p=3`, `|L|_3=3^3`, and `Z=Z(L)_3=Z(L)=C3`.

## Seven blocks, explicit defects, and all thresholds

The independent run returns exactly the following block data.

| block | ordinary rows | defect | heights | representative | `|D/Z|` | `exp(D/Z)` | threshold |
|---:|---|---:|---|---|---:|---:|---:|
| 1 | 1,2,4,5,6,9,15,16,19,20,21,22,23,24,27,28 | 3 | 0 on 1,2,4,5,6,9; 1 otherwise | submitted three-generator Sylow subgroup `D1` | 9 | 3 | 3 |
| 2 | 3,7,8,17,18,25,26,29,30 | 2 | all 0 | submitted `<Z,x>` | 3 | 3 | 1 |
| 3 | 10,31,32 | 1 | all 0 | `Z` | 1 | 1 | 1 |
| 4 | 11,33,34 | 1 | all 0 | `Z` | 1 | 1 | 1 |
| 5 | 12,35,36 | 1 | all 0 | `Z` | 1 | 1 | 1 |
| 6 | 13,37,38 | 1 | all 0 | `Z` | 1 | 1 | 1 |
| 7 | 14,39,40 | 1 | all 0 | `Z` | 1 | 1 | 1 |

The checker does not inherit the stored height labels for the inequality.  It
derives the defect from the degree valuations within each block and then uses

```text
h = v_3(theta(1)) - (3-d).
```

Here are all 40 audited rows; each row appeared exactly once in the verbatim
output.

| row | block | degree | `v_3` | height | `3^h` | threshold | result |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 1 | 1 | 0 | 0 | 1 | 3 | pass |
| 2 | 1 | 20 | 0 | 0 | 1 | 3 | pass |
| 4 | 1 | 28 | 0 | 0 | 1 | 3 | pass |
| 5 | 1 | 28 | 0 | 0 | 1 | 3 | pass |
| 6 | 1 | 28 | 0 | 0 | 1 | 3 | pass |
| 9 | 1 | 125 | 0 | 0 | 1 | 3 | pass |
| 15 | 1 | 21 | 1 | 1 | 3 | 3 | pass |
| 16 | 1 | 21 | 1 | 1 | 3 | 3 | pass |
| 19 | 1 | 48 | 1 | 1 | 3 | 3 | pass |
| 20 | 1 | 48 | 1 | 1 | 3 | 3 | pass |
| 21 | 1 | 48 | 1 | 1 | 3 | 3 | pass |
| 22 | 1 | 48 | 1 | 1 | 3 | 3 | pass |
| 23 | 1 | 48 | 1 | 1 | 3 | 3 | pass |
| 24 | 1 | 48 | 1 | 1 | 3 | 3 | pass |
| 27 | 1 | 105 | 1 | 1 | 3 | 3 | pass |
| 28 | 1 | 105 | 1 | 1 | 3 | 3 | pass |
| 3 | 2 | 21 | 1 | 0 | 1 | 1 | pass |
| 7 | 2 | 84 | 1 | 0 | 1 | 1 | pass |
| 8 | 2 | 105 | 1 | 0 | 1 | 1 | pass |
| 17 | 2 | 21 | 1 | 0 | 1 | 1 | pass |
| 18 | 2 | 21 | 1 | 0 | 1 | 1 | pass |
| 25 | 2 | 84 | 1 | 0 | 1 | 1 | pass |
| 26 | 2 | 84 | 1 | 0 | 1 | 1 | pass |
| 29 | 2 | 105 | 1 | 0 | 1 | 1 | pass |
| 30 | 2 | 105 | 1 | 0 | 1 | 1 | pass |
| 10 | 3 | 126 | 2 | 0 | 1 | 1 | pass |
| 31 | 3 | 126 | 2 | 0 | 1 | 1 | pass |
| 32 | 3 | 126 | 2 | 0 | 1 | 1 | pass |
| 11 | 4 | 126 | 2 | 0 | 1 | 1 | pass |
| 33 | 4 | 126 | 2 | 0 | 1 | 1 | pass |
| 34 | 4 | 126 | 2 | 0 | 1 | 1 | pass |
| 12 | 5 | 126 | 2 | 0 | 1 | 1 | pass |
| 35 | 5 | 126 | 2 | 0 | 1 | 1 | pass |
| 36 | 5 | 126 | 2 | 0 | 1 | 1 | pass |
| 13 | 6 | 144 | 2 | 0 | 1 | 1 | pass |
| 37 | 6 | 144 | 2 | 0 | 1 | 1 | pass |
| 38 | 6 | 144 | 2 | 0 | 1 | 1 | pass |
| 14 | 7 | 144 | 2 | 0 | 1 | 1 | pass |
| 39 | 7 | 144 | 2 | 0 | 1 | 1 | pass |
| 40 | 7 | 144 | 2 | 0 | 1 | 1 | pass |

The literal five submitted matrices all lie in `SU(3,5)` and all have order
three.  The displayed scalar generates the full center.  The three submitted
`D1` generators generate a subgroup of order 27 containing `Z`; since
`|L|_3=27`, this is a Sylow subgroup and hence the principal-block defect
group.  Its quotient has order nine and exponent three.

For blocks 3--7, central containment and defect one force `D=Z`, so their
quotients are trivial and have exponent one.

## Block 2 and class support

The fresh checker uses conjugacy-class sizes, not the claimant's assumption
that columns after position 3 are noncentral.  It finds exactly the central
class positions `[1,2,3]` and exactly one noncentral order-three class,
position 7.  On that class, the block-2 support and exact values are

```text
rows [3,7,8], values [3,3,-3].
```

Thus the submitted noncentral order-three matrix `x` represents this unique
class.  Malle--Navarro--Tiep Theorem 3.5 states that a `p`-element is contained
in a conjugate of a block defect group if and only if some ordinary character
in that block is nonzero on it.  The forward direction needed here is also the
first step of their proof, citing the standard block theorem.  Hence `x` lies
in a conjugate `E` of a block-2 defect group.

The central-p-subgroup argument gives `Z<=E`.  Since `z` is central of order
three and `x` is noncentral of order three, `<Z,x>` has order nine; the literal
matrix calculation independently returns order nine.  Block 2 has defect two,
so `|E|=9`.  Therefore `<Z,x>=E`.  Its quotient by `Z` has order and exponent
three.  This validates the block-2 representative rather than merely finding
a subgroup of the correct order.

## Exact Proposition 3.2 implication

The permitted primary artifact has SHA-256
`a2825c5bfed0c8d340893b3b8bcfd62f89b1e94c7d170e13f4df34198357e96f`.
Its Condition `(‡*)` is exactly

```text
exp(D/Z(G)_p) <= (|G:Z(G)|/theta(1))_p
```

for every ordinary character `theta` in the block.  The seven-block audit
therefore verifies `(‡*)` for every 3-block of `L`.

Proposition 3.2 is applied with every hypothesis retained:

| hypothesis | present use |
|---|---|
| `H` finite | assumed |
| `L=[H,H]` quasi-simple | `L=SU_3(5)` |
| `Z(L)=Z(H)` | assumed, both equal the stated center `C3` |
| `chi in Irr(H)` faithful | assumed exactly |
| `h in H` | assumed exactly |
| `chi(h) != 0` | assumed exactly |
| `H=<L,h>` | assumed exactly |
| every 3-block of `L` satisfies `(‡*)` | established by the seven-block audit |

The last two hypotheses together with nonvanishing imply that `chi|L` is
irreducible, exactly as recalled in the proof of Proposition 3.2.  If `D` is a
defect group of `chi` and `D0<=D` is a defect group of `chi|L`, the proposition
uses `|D:D0|<=|H:L|_3` and gives

```text
o(hZ(H))_3
 <= exp(D/Z(H)_3)
 <= |H:L|_3 exp(D0/Z(L)_3)
 <= |H:Z(H)|_3/chi(1)_3.
```

Both endpoints are powers of three, so this is precisely

```text
o(hZ(H))_3 divides (|H:Z(H)|/chi(1))_3.
```

It is not the full-order statement, it is not a statement without faithfulness
or generation, and it is not a statement for arbitrary derived groups.

## Evidence

Environment probe:

```text
/usr/bin/gap
/usr/bin/python3
Python 3.12.3
gap 4.12.1-2build2
gap-core 4.12.1-2build2
gap-libs 4.12.1-2build2
```

The separately frozen checker has SHA-256
`34ccaaa928f370873991101352d429506905e57f7350a27c0299cd4cfa819153`.
Under Lead's slot-2 lease, it was invoked exactly once as

```bash
/usr/bin/time -f 'ELAPSED=%e MAX_RSS_KB=%M' timeout 45s gap -q -A -r Agents/Kourovka/problems/20.115/verification/scratch/validator_central_height_20260817T233926Z.g
```

It exited zero with `ELAPSED=1.98 MAX_RSS_KB=142208`.  Complete verbatim GAP
output is preserved in
`Agents/Kourovka/problems/20.115/verification/scratch/validator_central_height_20260817T233926Z.out`,
SHA-256 `0962076fc50913b87a737e4940a4a0b1ecc7dcd95e9257ed8df7b2b9c3832454`,
105 lines and 4957 bytes.  Its terminal records are exactly

```text
ROW_COUNT=40 ALL_THRESHOLDS_PASS=true
END VALIDATOR_SU35_CENTRAL_HEIGHT
```

The claimant's frozen output independently has SHA-256
`2b040684b4eeaae215276bfd9d6e83ef59b4bc74da904322b3784472c161c1cf`,
85 lines, 5115 bytes, 40 row records, seven block records, and the same block,
height, representative, exponent, and threshold data.

## Why this verdict

Two separately written bounded computations agree, one written and run by this
Validator.  The validator checker reconstructs the submitted matrices
literally, strengthens the central-class gate, derives heights independently
from degrees and block defects, and checks every row.  The noncomputational
steps were reconstructed from Brauer-pair definitions and from the complete
primary-source statements and immediately necessary proof steps.  This meets
the `replicated` threshold for the bounded result and no higher.

## What is NOT established

- The universal revision-1 Kourovka target is not answered.
- No group outside the stated `SU_3(5)` derived-group family is covered.
- No prime other than three is covered.
- The conclusion concerns the 3-part of the order of `hZ(H)`, not the full
  order of `h`.
- Proposition 3.2's faithfulness, nonvanishing, equal-center, derived-group,
  and generation hypotheses cannot be removed.
- CTblLib's ordinary table has been independently replayed against a separate
  checker, not rebuilt from a presentation; hence the appropriate status is
  `replicated`, not `proven`.

## What would upgrade it

A proof from presentation-level character and block data could upgrade this
bounded computational result.  Upgrading the active scope would instead require
a line-by-line proof for every finite group or a valid source counterexample;
this finite prime-three bridge alone cannot do so.

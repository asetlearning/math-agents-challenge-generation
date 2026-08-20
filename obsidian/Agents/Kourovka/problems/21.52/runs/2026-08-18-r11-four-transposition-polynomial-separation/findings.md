---
problem: "21.52"
scope_id: 21.52/involution-class-product-order-colouring
assignment_revision: 1
cycle: 11
outcome: PARTIAL_RESULT
active_assignment_answered: false
witness_equals_target: false
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/alternating-groups
  - project/kourovka
  - status/conjectured
---

# Candidate family theorem: four-transpositions in `A_n`, `n>=14`

## Active target

Scope: `21.52/involution-class-product-order-colouring`, revision 1.

Universal target: for every finite nonabelian simple `L` and every single
involution class `D`, every permutation of `D` preserving every exact product
order is induced by an automorphism of `L` stabilizing `D`.

## Precise partial result

For every integer `n>=14`, let `L=A_n` and let `D_n` be the conjugacy class of
involutions of cycle type `2^4 1^(n-8)`. I obtain the following candidate family
theorem:

> Every permutation of `D_n` preserving `|xy|` for every distinct `x,y` is induced
> by conjugation by a point permutation in `S_n`, hence by an automorphism of
> `A_n` stabilizing `D_n`.

This is an infinite-family partial only. It does not answer the universal active
scope.

## Constraint-and-conclusion matrix

| constraint_id | role | required condition | candidate value / proof use | evidence | result |
|---|---|---|---|---|---|
| `21.52-forall-L-D` | admissibility | all admissible `(L,D)` | Only `(A_n,D_n)`, `n>=14`, is treated. | Sections below | **not universal; active row open** |
| `21.52-L-finite-nonabelian-simple` | admissibility | `L` finite nonabelian simple | `A_n`, `n>=14`, is finite nonabelian simple. | Standard alternating-group theorem | family pass |
| `21.52-D-single-involution-class` | admissibility | one class of elements of order 2 | Products of four disjoint transpositions are even involutions. The `S_n` class does not split in `A_n` because its cycle type is not a set of distinct odd lengths. | Cycle-type criterion | family pass |
| `21.52-Gamma-complete-on-D` | admissibility | all unordered distinct pairs are edges | Counts below are attached to every distinct pair of four-matchings. | Definition of `N_{r,s}` | family pass |
| `21.52-edge-colour-exact-product-order` | admissibility | colour is exactly `|xy|` | Orders are computed as exact orders of permutation products; no conjugacy-class refinement is used. | Component rule and enumerator | family pass |
| `21.52-tau-preserves-all-edge-colours` | admissibility | `|xy|=|x^tau y^tau|` for every pair | This implies preservation of every two-point count `N_{r,s}` and hence the recovered relation `R`. | Counting argument below | family pass |
| `21.52-tau-induced-by-AutL` | target conclusion | every such `tau` extends | Reconstruct a point permutation `pi in S_n`; then `tau(x)=pi x pi^-1` for all `x in D_n`. | Clique reconstruction below | established only for this family; universal row open |

## 1. Union components and the exact product-order rule

Identify an element of `D_n` with its set of four disjoint 2-subsets, a
four-matching on `[n]`. For two such matchings `X,Y`, their two-coloured union has
maximum degree two. Its nontrivial components are exactly:

- `E`: one edge belonging to both matchings;
- `P_l`: an alternating path with `l>=1` edges; or
- `C_(2r)`: an alternating cycle with `2r` edges, `r>=2`.

On `P_l`, tracing `XY` gives one cycle of length `l+1`. On `C_(2r)`, it gives two
cycles of length `r`. On `E`, it is the identity. Therefore

`|XY| = lcm({l+1 : P_l occurs}, {r : C_(2r) occurs})`.

For an odd path `P_(2r+1)`, one endpoint matching supplies `r+1` edges and the
other `r`; the signature records this as `X` or `Y`. The full signature is the
multiset of component labels, modulo the single global swap `X<->Y`. This is a
complete unordered-pair invariant because each alternating connected component
of a given labelled type is unique up to point relabelling.

The component edge weights are

- `E:(1,1)`;
- `C_(2r):(r,r)`;
- `P_(2r):(r,r)`; and
- `P_(2r+1)X:(r+1,r)` and `P_(2r+1)Y:(r,r+1)`.

Thus the complete inventory is the finite list of component multisets whose two
weights both total four, excluding `E+E+E+E` (the diagonal `X=Y`). Independent
component-multiset and point-matching enumerations agree on exactly 54 signatures:
22 with at least one `E`, 32 with none. The complete inventory—including ID,
common-edge status, support size, component label, pair product order, and a
representative `X,Y`—is the 54 `SIG` rows of
`scratch/separation-certificate.tsv`.

## 2. Exact common-neighbour polynomials

For an unordered endpoint pair of signature `S`, define, for `2<=r<=s`,

`M^S_(r,s)(n) = #{Z : {|XZ|,|YZ|}={r,s}}`,

combining the two possible orientations when `r<s`. Equivalently,
`M_(r,s)=N_(r,s)+N_(s,r)` for `r<s` and `M_(r,r)=N_(r,r)`. Restricting to
`r,s>=2` automatically excludes `Z=X,Y`, because equality of involutions is the
only way a product order is one. Every exact-colour automorphism preserves every
coordinate `M_(r,s)`.

Let `U=supp(X) union supp(Y)` and `m=|U|`. A third four-matching `Z` uses a unique
set of `j` points outside `U`, where `0<=j<=8`. After this external set is chosen,
the remaining local datum is a matching on those `j` labelled points and
`8-j` selected points of `U`. Hence, exactly,

`M^S_(r,s)(n) = sum_(j=0)^8 a^S_(r,s,j) binom(n-m,j)`,

where `a^S_(r,s,j)` is obtained by the finite local enumeration on `U` plus `j`
labelled external points. For every `(S,j)`, the enumerator checks that the sum
over all oriented order coordinates is
`105 binom(m,8-j)`, the number of ways to select the internal points and perfectly
match the eight selected points.

The complete raw data are in `scratch/local-coefficients.tsv`:

- `SIG`: signature metadata and representative;
- `TOTAL`: all 486 local coverage checks;
- `C`: all 29,081 nonzero oriented arrays `a_(p,q,j)`; and
- `ORDERS`: every exact product order encountered.

The exact symmetrized coefficient arrays are the `A` rows of
`scratch/separation-certificate.tsv`. Each `A` row contains first the nine local
coefficients in the basis `binom(n-m,j)`, then the nine coefficients in the common
basis `binom(n-14,k)`. An omitted signature-coordinate array is identically zero.

To obtain the common basis, let `P(n)=M^S_(r,s)(n)` and set
`b_k=Delta^k P(14)`. Newton interpolation gives the polynomial identity

`P(n)=sum_(k=0)^8 b_k binom(n-14,k)`.

This is an identity of degree at most eight, not finite-degree sampling as a
surrogate for a proof.

## 3. Uniform separation certificate

There are `22*32=704` pairs `(S,T)` with `S` containing a common transposition and
`T` containing none. For every one, a `CERT` row in
`scratch/separation-certificate.tsv` gives:

`CERT  S-id  T-id  r,s  sign  d_0,...,d_8`,

where

`M^S_(r,s)(n)-M^T_(r,s)(n) = sum_(k=0)^8 d_k binom(n-14,k)`.

Every one of the 704 rows has `d_0` strictly of the displayed sign and every
other `d_k` either zero or of that same sign. In fact 674 selected differences
are constant and 30 are affine in `n-14`. Since every `binom(n-14,k)` is a
nonnegative integer for integer `n>=14`, each difference is strictly nonzero for
every such `n`. Thus the complete exact common-neighbour vector distinguishes
all common-edge signatures from all no-common-edge signatures uniformly for
`n>=14`.

Coverage metadata in the certificate are:

```text
signatures                              54
common_signatures                       22
no_common_signatures                    32
opposite_pairs                         704
coefficientwise_sign_certificates      704
unresolved_pairs                         0
available unordered coordinates        120
```

The standalone verifier checks uniqueness and completeness of the 704-pair
Cartesian product, recomputes every displayed difference from the `A` arrays, and
checks strict constant term plus coefficientwise sign.

## 4. Recovering the natural point action

Let `R` be the now intrinsic relation on `D_n`:

`X R Y` if and only if X and Y share a transposition.`

For each transposition/edge `e` of `K_n`, let

`S_e={X in D_n : e in X}`.

It is an `R`-clique of size `15 binom(n-2,6)`. These are exactly the largest
`R`-cliques when `n>=14`. Indeed, let `F` be any pairwise `R`-intersecting family
with no edge common to every member. Fix `A in F`. For each of the four edges
`e in A`, choose `B_e in F` omitting `e`. Every member of `F cap S_e` must share
with `B_e` one of its four edges `f`, so

`|F cap S_e| <= 4 |S_e cap S_f| <= 12 binom(n-4,4)`,

because two disjoint prescribed edges extend to a four-matching in
`3 binom(n-4,4)` ways. Since every member of `F` meets `A`,

`|F| <= 48 binom(n-4,4)`.

But

`15 binom(n-2,6) / (48 binom(n-4,4)) = (n-2)(n-3)/96 > 1`

for `n>=14`. A clique having a globally common edge lies inside the corresponding
`S_e`; therefore the largest cliques are precisely the full `S_e`.

Any colour automorphism `tau` preserves `R`, hence permutes these largest cliques
and induces a permutation `sigma` of the 2-subsets of `[n]`. For distinct edges
`e,f`,

- `S_e cap S_f` is empty if `e,f` meet; and
- it is nonempty if `e,f` are disjoint (they extend to a four-matching).

Thus `sigma` preserves intersection/disjointness of 2-subsets. The largest
pairwise-intersecting families of 2-subsets are exactly the `n` point-stars
`{e:p in e}` of size `n-1`: a pairwise-intersecting family without a common point
is contained in the three edges of a triangle. Since `n>=14`, size distinguishes
point-stars from triangles. Therefore `sigma` is induced by a point permutation
`pi in S_n`.

Finally, membership in the recovered stars determines each four-matching:

`e in X iff X in S_e iff tau(X) in S_(sigma(e))`.

Consequently `tau(X)={pi(e):e in X}=pi X pi^-1` for every `X in D_n`. Conjugation
by `pi` is an automorphism of `A_n` and stabilizes the cycle-type class `D_n`.

## Reproduction

From the run directory:

```text
g++ -O3 -std=c++17 -Wall -Wextra -pedantic scratch/enumerate.cpp -o /tmp/p2152-enumerate
timeout 60s /tmp/p2152-enumerate > scratch/local-coefficients.tsv
python3 scratch/certify.py scratch/local-coefficients.tsv > scratch/separation-certificate.tsv
python3 scratch/audit_signatures.py scratch/separation-certificate.tsv
python3 scratch/verify_certificate.py scratch/separation-certificate.tsv
```

Frozen SHA-256 values:

| file | SHA-256 |
|---|---|
| `scratch/enumerate.cpp` | `08088dbf076e89d4502d1c0775bc8f738ede81c478cc1b2b87845ef9d3222814` |
| `scratch/local-coefficients.tsv` | `3b11b3ecb6fbe71521be41e5fc64980238cc303360e84c5854c37911bd70b367` |
| `scratch/certify.py` | `1c37c7097dfec51c78806f884265d90a5f7538b326ad3141a36006a93fad6ac6` |
| `scratch/separation-certificate.tsv` | `9d4ea05e3c08affb6d686aefcf74a128eafaf1580ec92bbb4de8086bdcb108a4` |
| `scratch/audit_signatures.py` | `506ac72685ade629649f4150cf0129a0e43472002633b09787c72894bc656af9` |
| `scratch/verify_certificate.py` | `b90ecfdeb29dd154a1334abed450ba1db2161616acbdf63552f0df4dbcb1b85d` |

The definitive enumeration took 9.39 seconds and 3,584 KiB RSS under a 60-second
timeout. No heavy-compute lease was required.

## What this does not establish

- It does not prove the assertion for every finite nonabelian simple group or for
  any other involution class.
- It does not treat the same four-transposition class in degrees `8<=n<=13`.
- It does not address Problem 21.53, unions of classes, an uncoloured graph, or
  colouring by product conjugacy class.
- The family theorem and computational certificate are newly submitted and remain
  `status/conjectured` until independent Validator reconstruction.

## How this could be wrong

1. The component label could fail to classify an unordered two-coloured union;
   the independent multiset audit reduces but does not replace a hand check of
   this assertion.
2. The local enumerator or permutation-order routine could contain a shared bug;
   Validator should independently enumerate the component patterns and at least
   one full fixed-degree count array.
3. The interpretation of an off-diagonal symmetrized `M_(r,s)` as an intrinsic
   two-point statistic could be mishandled; it should be checked directly from the
   definition of a colour automorphism.
4. The largest-clique bound or the passage from transposition stars to point stars
   could hide an exceptional configuration; both inequalities and equality cases
   should be reconstructed independently.

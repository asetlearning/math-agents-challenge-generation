---
title: "Partial result: structural counterexample-family exclusions for Kourovka 19.30"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/characters
  - topic/suzuki-groups
  - project/kourovka
  - status/conjectured
---

# Scope and status

- Active scope: `19.30/vanishing-order-simple-recognition`
- Assignment revision: 1
- Direction: counterexample
- Cycle outcome: `PARTIAL_RESULT`
- Active target answered: **no**

This note does not give a counterexample and does not prove the universal recognition statement. It gives exact catalogue coverage, several uniform structural-family exclusions, explicit reconstructible near misses, and a broader Suzuki recognition criterion whose external theorem inputs still require Validator review.

The source transcription, clause matrix, admissibility audit, complete command history, and limitations are in `log.md` in this run directory. `source_transcription_checked: yes`; `active_scope_checked: yes`.

# Result 1: exact installed-table coverage

With GAP 4.12.1 and CTblLib 1.3.7, the installed ordinary-character-table catalogue has 2,613 names. Its complete precomputed size buckets at the two installed Suzuki simple-group orders are

\[
\{T:|T|=29120\}=\{\texttt{Sz(8)}\},\qquad
\{T:|T|=32537600\}=\{\texttt{Sz(32)}\}.
\]

Scanning every irreducible row against every class gives

\[
V(\operatorname{Sz}(8))=\{2,4,5,7,13\},\qquad
V(\operatorname{Sz}(32))=\{2,4,5,25,31,41\}.
\]

Every nonidentity class in both tables is vanishing. The exact leased command, scripts, exit status, and full stdout are:

- `scratch/leased_evidence_rerun.sh`
- `scratch/leased_evidence_rerun.out`

Coverage is exactly the installed CTblLib catalogue at those two orders. It is not a census of all finite groups of either order.

# Result 2: every normal-Hall-455 construction fails

## The family covered

Let \(G\) have order
\[
29120=2^6\cdot5\cdot7\cdot13
\]
and suppose its Hall \(\{5,7,13\}\)-subgroup \(A\) is normal. Then \(|A|=455\), and \(A\cong C_{455}\). One way to see this is that 455 is square-free and no one of 5, 7, 13 divides another minus one; equivalently \(\gcd(455,\varphi(455))=\gcd(455,288)=1\). Schur–Zassenhaus gives
\[
G=A\rtimes P,\qquad |P|=64.
\]
The proof below is uniform over every group \(P\) of order 64 and every homomorphism \(P\to\operatorname{Aut}(A)\).

## Exhaustive action partition

Write \(A=C_5\times C_7\times C_{13}\), and let
\(Q\) be the image of \(P\) in
\[
\operatorname{Aut}(A)_2\cong C_4\times C_2\times C_4.
\]
This image is abelian.

### Case 1: an action element is nontrivial on one prime factor and trivial on another

Suppose \(h\in P\) acts nontrivially on \(C_s\) and trivially on \(C_r\), for distinct \(r,s\in\{5,7,13\}\). Choose \(\lambda\in\operatorname{Irr}(A)\) supported on \(C_s\) and moved by \(h\), and choose \(1\ne a\in C_r\).

Let \(I=I_G(\lambda)\). Clifford correspondence supplies an irreducible character \(\chi\) induced from an irreducible character of \(I\) lying above \(\lambda\). No conjugate of \(ah\) lies in \(I\): conjugation does not change its image in the abelian action group \(Q\), and that image moves \(\lambda\). Hence \(\chi(ah)=0\).

Because \(h\) fixes \(a\), the factors commute and
\(|ah|=r|h|\), a mixed odd-even order. Such an order is absent from
\(V(\operatorname{Sz}(8))=\{2,4,5,7,13\}\). Thus no action in Case 1 can collide.

### Case 2: every nonidentity action-image element is nontrivial on all three factors

Projection \(Q\to\operatorname{Aut}(C_7)_2\cong C_2\) is then injective. Hence \(|Q|\le2\).

- If \(Q=1\), every Clifford orbit on \(\operatorname{Irr}(A)\) has size one.
- If \(|Q|=2\), its nonidentity element must be inversion on each of \(C_5,C_7,C_{13}\); every nontrivial orbit is \(\{\lambda,\lambda^{-1}\}\).

For any \(\chi\in\operatorname{Irr}(G)\), Clifford theory therefore gives on \(A\) either
\[
\chi_A=e\lambda
\quad\text{or}\quad
\chi_A=e(\lambda+\lambda^{-1}).
\]
The first value never vanishes. At any \(a\in A\), the second would vanish only if \(\lambda(a)^2=-1\), impossible because \(\lambda(a)\) has odd order. Thus every element of \(A\) is nonvanishing. Every element of \(G\) of order 5, 7, or 13 lies in \(A\), so
\[
\{5,7,13\}\cap V(G)=\varnothing.
\]
Again \(V(G)\ne V(\operatorname{Sz}(8))\).

Cases 1 and 2 exhaust every action. Therefore no group of order 29,120 with normal Hall subgroup of order 455 is a counterexample.

# Exact symbolic near miss

Take
\[
A=C_{455},\quad H=C_4\times C_2^4,
\]
and a homomorphism \(\varepsilon:H\to C_2\) nonzero on a \(C_2\)-coordinate. Let \(h\) act on \(A\) by inversion exactly when \(\varepsilon(h)=1\), and set \(G=A\rtimes H\).

With \(K=\ker\varepsilon\), the 64 inflated characters from \(H\) are linear. The other irreducibles are the degree-two characters induced from
\((\lambda\otimes\mu)\in\operatorname{Irr}(A\times K)\), one for each inversion pair \(\{\lambda,\lambda^{-1}\}\) and each \(\mu\in\operatorname{Irr}(K)\). The degree-square check is
\[
64+\frac{454}{2}\cdot32\cdot2^2=29120.
\]
They vanish exactly on \(A(H\setminus K)\), while on \(ak\in A K\) they equal
\[
\mu(k)(\lambda(a)+\lambda(a)^{-1})\ne0.
\]
For \(h\notin K\), \((ah)^2=h^2\), and the chosen \(\varepsilon\) makes both orders two and four occur. Hence
\[
V(G)=\{2,4\}.
\]

Constraint matrix for this near miss:

| constraint_id | role | required condition | candidate value / evidence | result |
|---|---|---|---|---|
| `19.30-forall-GS` | admissibility | one qualifying pair would refute the universal statement | pair tested against every remaining row | pass as test setup |
| `19.30-G-finite` | admissibility | finite \(G\) | explicit semidirect product of order 29,120 | pass |
| `19.30-S-finite-simple` | admissibility | finite simple \(S\) | \(S=\operatorname{Sz}(8)\), installed table reports `IS_SIMPLE=true` | pass |
| `19.30-vanishing-definition` | admissibility | zero of some irreducible complex character | complete symbolic irreducible list and zero-locus derivation above | pass |
| `19.30-equal-orders` | admissibility | \(|G|=|S|\) | \(455\cdot64=29120\) | pass |
| `19.30-equal-vanishing-order-sets` | admissibility | \(V(G)=V(S)\) | \(\{2,4\}\ne\{2,4,5,7,13\}\) | **fail** |
| `19.30-isomorphic` | target conclusion | candidate must violate isomorphism | \(G\) has normal abelian subgroup \(A\); \(S\) is simple | violated, but irrelevant after failed admissibility |

It is therefore an `OUT_OF_SCOPE_EXAMPLE`, not a counterexample.

# Result 3: any Suzuki-order collision is centreless and directly indecomposable

This applies to both `Sz(8)` and `Sz(32)` using their lease-reproduced vanishing-order sets.

Suppose \(V(G)=V(S)\). If \(1\ne z\in Z(G)\), take a power of \(z\) of prime order \(r\), and choose a different prime \(p\in V(S)\). There is \(x\in G\) of order \(p\) and \(\chi\in\operatorname{Irr}(G)\) with \(\chi(x)=0\). Schur's lemma gives \(\rho(z)=\lambda I\) in a representation affording \(\chi\), so \(\chi(zx)=\lambda\chi(x)=0\). But \(|zx|=rp\), and neither Suzuki vanishing-order set contains a mixed-prime order. Hence \(Z(G)=1\).

For finite groups \(A,B\), tensor-product characters give the exact formula
\[
V(A\times B)=
\{\operatorname{lcm}(v,n):v\in V(A),\ n\in\omega(B)\}
\cup
\{\operatorname{lcm}(m,w):m\in\omega(A),\ w\in V(B)\}.
\]
If a required prime \(p\) lies in \(V(A)\), then every prime divisor \(r\) of \(|B|\) must equal \(p\); otherwise the formula produces forbidden vanishing order \(pr\). Consequently \(V(A)\) cannot contain two different required primes when \(B\ne1\), and symmetrically \(V(B)\) cannot contain two. Yet each target set contains four distinct prime orders:
\[
\{2,5,7,13\}\subseteq V(\operatorname{Sz}(8)),\qquad
\{2,5,31,41\}\subseteq V(\operatorname{Sz}(32)).
\]
The two factors could supply at most two of them. Thus no matching \(G\) is a nontrivial direct product.

# Result 4: no solvable group collides with `Sz(8)` or `Sz(32)`

This result is independent of the classification of finite simple groups.

## Normal-prime lemma

Fix
\[
M=p\prod_i r_i^{a_i},\qquad v_p(M)=1,
\]
and suppose \(p\nmid|\operatorname{GL}_d(r_i)|\) for all \(i\) and all
\(1\le d\le a_i\). Then every solvable group \(H\) with \(|H|\mid M\) and \(p\mid|H|\) has a normal Sylow subgroup \(P\cong C_p\).

Use strong induction over all such divisor orders. Let \(N\cong C_r^d\) be a minimal normal subgroup of \(H\). If \(r=p\), the exponent-one hypothesis makes \(N\) the Sylow \(p\)-subgroup. If \(r\ne p\), induction gives a normal Sylow \(p\)-subgroup in \(H/N\); let \(K\) be its preimage and \(P\in\operatorname{Syl}_p(K)\). The linear-group hypothesis forces the conjugation action of \(P\) on \(N\) to be trivial. Hence \(P\) is the unique Sylow \(p\)-subgroup of \(K=NP\), so \(P\operatorname{char}K\triangleleft H\) and \(P\triangleleft H\).

If \(P=C_p\triangleleft H\), then every \(x\in P\setminus\{1\}\) is nonvanishing. For \(\chi\in\operatorname{Irr}(H)\), Clifford theory gives
\[
\chi_P=e\sum_{\lambda\in\mathcal O}\lambda
\]
for a conjugation orbit \(\mathcal O\subseteq\operatorname{Irr}(P)\). A trivial orbit gives a nonzero value. A nontrivial orbit evaluated at \(x\) gives \(e\) times a nonempty subset of the distinct nontrivial \(p\)-th roots. If that sum were zero, its \(0/1\)-coefficient polynomial would be divisible by
\(\Phi_p(X)=1+X+\cdots+X^{p-1}\), impossible because its constant coefficient is zero. Thus \(p\notin V(H)\).

## Application at the two exact orders

- For \(M=29120=2^6\cdot5\cdot7\cdot13\), choose \(p=13\). Here
  \(\operatorname{ord}_{13}(2)=12>6\), while
  \(|\operatorname{GL}_1(5)|=4\) and \(|\operatorname{GL}_1(7)|=6\).
  Every solvable \(G\) of this order has normal \(C_{13}\), so
  \(13\notin V(G)\); lease-reproduced table data give
  \(13\in V(\operatorname{Sz}(8))\).
- For \(M=32537600=2^{10}\cdot5^2\cdot31\cdot41\), choose \(p=41\). Here
  \(\operatorname{ord}_{41}(2)=20>10\),
  \(|\operatorname{GL}_2(5)|=(25-1)(25-5)=480\), and
  \(|\operatorname{GL}_1(31)|=30\).
  Every solvable \(G\) of this order has normal \(C_{41}\), so
  \(41\notin V(G)\); lease-reproduced table data give
  \(41\in V(\operatorname{Sz}(32))\).

Therefore every same-order collision with either simple group would have to be nonsolvable. This is universal coverage over all solvable groups at the two exact orders, not catalogue coverage.

# Conjectured broader partial theorem

Let \(n\ge3\) be odd, \(q=2^n\), and \(S=\operatorname{Sz}(q)\). Suppose a prime \(p\) divides \(q^2+1\) exactly once, satisfies \(\operatorname{ord}_p(2)=4n\), and does not divide \(|\operatorname{GL}_d(r)|\) for any other \(r^a\parallel |S|\) and \(1\le d\le a\). Subject to the standard classification and automorphism theorems for Suzuki groups and the standard Suzuki character formula, \(S\) is recognized by order and vanishing-order set.

The proof has three steps:

1. A nonabelian simple composition factor of a group whose order divides \(|S|\) must, by the classification of nonabelian simple groups of order prime to 3, be \(T=\operatorname{Sz}(2^m)\). Zsigmondy's theorem applied to \(2^m-1\) shows that \(|T|\mid|S|\) forces \(m\mid n\). For a proper factor, \(m<n\).
2. If a minimal normal subgroup is \(N=T^k\), then \(k\le n/m<p\) from the 2-parts of the orders and \(p\equiv1\pmod{4n}\). The primitive-order condition shows \(p\nmid|T|\); the standard formula \(|\operatorname{Out}(T)|=m\) and \(k<p\) then give \(p\nmid|\operatorname{Aut}(T^k)|\). For an abelian minimal normal subgroup, the stated general-linear condition gives the same conclusion.
3. First use strong induction for every group \(H\) with \(|H|\) a proper divisor of \(|S|\) and \(p\mid|H|\). The simple abelian base \(H=C_p\) already has normal Sylow \(C_p\); a proper **nonabelian** simple quotient containing \(p\) cannot occur because \(\operatorname{ord}_p(2)=4n\). For a minimal normal \(N\), if \(p\mid|N|\), the exponent-one hypothesis gives \(N=C_p\); a nonabelian \(N=T^k\) containing \(p\) is impossible for proper \(T\). If \(p\nmid|N|\), lift the normal Sylow subgroup from \(H/N\) and use \(p\nmid|\operatorname{Aut}(N)|\) to centralize \(N\). Apply the same minimal-normal argument to an exact-order nonsimple \(G\); the alternative \(N=S\) would force \(G=N\) simple. Thus every nonsimple same-order group has normal Sylow \(C_p\).
4. If \(C_p\triangleleft G\), Clifford restriction shows every nonidentity element of it is nonvanishing: a zero would be a vanishing proper subset of the \(p\)-th roots of unity, contradicting \(\Phi_p(X)=1+\cdots+X^{p-1}\). Thus \(p\notin V(G)\).
5. A standard Suzuki irreducible of degree \(q^2+1\) has \(p\)-defect zero, so \(p\in V(S)\). A simple group of the same order is the same Suzuki group by the classification theorem and equality of 2-parts.

The exact arithmetic instances currently recorded are
\[
q\in\{8,32,128,512,2048,8192\}
\]
with respective obstruction primes
\[
p\in\{13,41,113,109,397,53\}.
\]
All factorizations and modular checks are displayed in `log.md`.

This broader theorem is not yet submitted as certified. Dependencies still needing exact citations/checks are:

- every nonabelian finite simple group of order prime to 3 is a Suzuki group;
- \(\operatorname{Out}(\operatorname{Sz}(2^m))\) is cyclic of order \(m\);
- \(\operatorname{Sz}(q)\) has an irreducible complex character of degree \(q^2+1\);
- the defect-zero vanishing theorem;
- independent arithmetic verification for the three non-catalogued cases.

# Result 5: the full `Sz(8)`-radical branch at `Sz(512)` order is excluded

Let \(G\) be nonsimple of order \(|\operatorname{Sz}(512)|\), and suppose its unique nonabelian composition factor is the only possible proper Suzuki factor, `Sz(8)`. With \(R=\operatorname{Rad}(G)\), the standard classification of nonabelian simple groups whose orders are prime to 3, the divisor argument, and \(|\operatorname{Out}(\operatorname{Sz}(8))|=3\) give
\[
1\to R\to G\to\operatorname{Sz}(8)\to1,
\qquad
|R|=2^{12}\cdot37\cdot73\cdot109.
\]
No splitting is assumed, so this includes every action and extension class.

The radical \(R\) is solvable. Since
\[
\operatorname{ord}_{109}(2)=36>12,
\qquad 109\nmid36=|\operatorname{GL}_1(37)|,
\qquad 109\nmid72=|\operatorname{GL}_1(73)|,
\]
the normal-prime lemma makes its Sylow \(C_{109}\) unique and normal. It is therefore characteristic in \(R\) and normal in \(G\). Clifford theory makes all its nonidentity elements nonvanishing, so \(109\notin V(G)\).

The standard `Sz(512)` character of degree
\[
512^2+1=262145=5\cdot13\cdot37\cdot109
\]
has 109-defect zero, hence \(109\in V(\operatorname{Sz}(512))\). Thus no group in this entire nonsolvable radical-extension family is a collision.

This is a counterexample-family exclusion, not a proof of recognition for every group at the `Sz(512)` order; it remains dependent on the explicitly listed standard Suzuki inputs.

# Result 6: two order-504 construction branches fail

Take the finite simple target
\[
S=\operatorname{PSL}_2(8),\qquad |S|=504.
\]
Its element orders are \(1,2,3,7,9\). Its Steinberg character vanishes on its involutions, so \(2\in V(S)\), while no order 6, 12, 18, or 21 can lie in \(V(S)\) because no such element exists.

## Affine semilinear near miss

Let \(V=\mathbb F_8^+\cong C_2^3\), and set
\[
H=\langle a,b\mid a^7=b^9=1,\ bab^{-1}=a^2\rangle.
\]
Choose a primitive \(\alpha\in\mathbb F_8\). The action
\[
a:x\mapsto\alpha x,\qquad b:x\mapsto x^2
\]
is compatible with the displayed relation, and factors through the semilinear group \(C_7\rtimes C_3\). Put \(G=V\rtimes H\). Then
\(|G|=8\cdot63=504\), and \(V\triangleleft G\), so \(G\not\cong S\).

The irreducible characters of \(H\) have degrees
\[
1^9,\ 3^6.
\]
Indeed, \(H_{\mathrm{ab}}\cong C_9\), while the six nontrivial characters of \(C_7\) form two orbits of size three, each with three extensions to its inertia group. The complement is transitive on the seven nontrivial characters of \(V\); the stabilizer quotient is \(C_9\), giving nine induced irreducibles of degree seven. Hence the full degree list for \(G\) is
\[
1^9,\ 3^6,\ 7^9,
\qquad 9+6\cdot9+9\cdot49=504.
\]

Every involution lies in \(V\). Inflated characters are nonzero on \(V\), and each degree-seven character restricts to the sum of all seven nontrivial characters of \(V\), with value \(-1\) at every \(1\ne v\in V\). Thus
\[
2\notin V(G).
\]
On the other hand, \(b\) fixes \(u=1\in\mathbb F_8^+\). Therefore \(u\) and \(b\) commute and \(|ub|=18\). A degree-three character induced from a nontrivial character of \(C_7\) vanishes at \(b\), and its inflation to \(G\) vanishes at \(ub\). Thus
\[
18\in V(G).
\]
The pair fails `19.30-equal-vanishing-order-sets` in both directions: the target has vanishing order 2 and no element of order 18, whereas the affine group has no vanishing involution and does have a vanishing element of order 18. It is an `OUT_OF_SCOPE_EXAMPLE`, not a counterexample.

## Central-extension branch

Consider exactly the groups fitting
\[
1\longrightarrow C_3\longrightarrow G\longrightarrow
\operatorname{PSL}_2(7)\longrightarrow1.
\]
Conjugation is trivial because the perfect quotient has no nontrivial homomorphism to \(\operatorname{Aut}(C_3)=C_2\). Thus the extension is central. For \(Q=\operatorname{PSL}_2(7)\), one has \(Q_{\mathrm{ab}}=0\) and Schur multiplier \(M(Q)=C_2\), so the universal-coefficient sequence gives
\[
H^2(Q,C_3)\cong\operatorname{Hom}(C_2,C_3)=0.
\]
Consequently every group in this exact branch is
\[
G\cong\operatorname{PSL}_2(7)\times C_3.
\]
The ordinary character table gives
\(V(\operatorname{PSL}_2(7))=\{2,3,4,7\}\). Since \(C_3\) is abelian and has element-order set \(\{1,3\}\), the direct-product formula yields
\[
V(G)=\{2,3,4,6,7,12,21\}.
\]
Orders 6, 12, and 21 do not occur in \(S\), so this whole extension branch fails `19.30-equal-vanishing-order-sets`.

Exact coverage here is only the displayed extension orientation with normal kernel \(C_3\) and quotient \(\operatorname{PSL}_2(7)\). It is not a classification of every nonsimple group of order 504.

# Cycle recommendation

The counterexample direction has exhausted several genuinely different representations—installed character-table buckets, direct products, normal-Hall semidirect products, affine modules, primitive-prime radical extensions, and central extensions—without leaving a named residual candidate. The next cycle should switch to the proof direction and develop the normal-prime/composition-factor mechanism only after the four standard external dependencies listed above receive exact citations and independent verification.

# What this does not establish

- No counterexample was found.
- The active universal scope is not answered.
- CTblLib coverage is not coverage of all groups at the two target orders.
- The structural theorem covers exactly groups with a normal Hall-455 subgroup; it does not assume all order-29,120 groups have one.
- The broader recognition criterion covers odd prime and composite exponents only when an exponent-one primitive prime satisfies every stated linear-group condition; it says nothing when that arithmetic hypothesis fails.
- The two order-504 arguments exclude only the explicitly parametrized affine constructions and the displayed central-extension family; they do not enumerate all groups of order 504.
- None of these results may be labelled `status/proven` without Validator and human review.

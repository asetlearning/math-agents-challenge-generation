---
title: "A5, p=5 hypothesis-closure hand dossier"
author: operator
problem: "19.30"
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
strategy_id: P-A5-5-HYPOTHESIS-CLOSURE
direction: proof
cycle_outcome: PARTIAL_RESULT
validator_status: pending
witness_equals_target: false
active_assignment_answered: no
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/conjectured
---

# \((A_5,5)\) hypothesis-closure dossier

Only elementary hand arguments are used below. No character table,
classification theorem, computation, web/history, or delegated result is an
input.

## Row 1 — base: `PASS`

### Order

The sign homomorphism \(\operatorname{sgn}:S_5\to\{1,-1\}\) is onto because a
transposition has sign \(-1\). Its kernel is \(A_5\), so

\[
 |A_5|=|S_5|/2=5!/2=60.
\]

Thus \(A_5\) is finite of order \(60\).

### Conjugacy classes and simplicity

The even cycle types on five letters are exactly: the identity, a 3-cycle, a
product of two disjoint transpositions, and a 5-cycle.

- There are \(\binom53(3-1)!=20\) 3-cycles. For a 3-cycle \(x\), its
  centralizer in \(S_5\) consists of its three powers and the optional swap of
  its two fixed points, so has order \(6\). The swap is odd while the powers are
  even; hence \(|C_{A_5}(x)|=3\), and its \(A_5\)-class has size
  \(60/3=20\). Thus all 3-cycles form one \(A_5\)-class.
- There are \(5\cdot3=15\) double transpositions: choose the fixed point and
  partition the other four points into two unordered pairs. The \(S_5\)-centralizer
  of \((12)(34)\) has order \(8\). It contains the odd element \((12)\), so
  sign is onto on that centralizer and its even half has order \(4\). Therefore
  the \(A_5\)-class size is \(60/4=15\), and all double transpositions form one
  class.
- There are \((5-1)!=24\) 5-cycles. The centralizer in \(S_5\) of a 5-cycle
  is its cyclic group of order \(5\): a commuting permutation is determined by
  the image of one point and hence is a power of the cycle. Every power is even,
  so the \(A_5\)-centralizer also has order \(5\). Each \(A_5\)-class therefore
  has size \(60/5=12\), and the 24 elements split into exactly two such classes.

The conjugacy-class sizes are consequently

\[
  1,\ 20,\ 15,\ 12,\ 12.
\]

A normal subgroup is a union of conjugacy classes containing the identity. The
possible proper union sizes are

\[
  1,13,16,21,25,28,33,36,40,45,48.
\]

Apart from \(1\), none divides \(60\); the union of all five classes has size
\(60\). Lagrange's divisibility therefore leaves only the identity subgroup and
\(A_5\) itself as normal subgroups. Hence \(A_5\) is simple.

**Row 1 terminal entry:** `PASS` — \(|A_5|=60\), and the displayed complete
class-size argument establishes that \(A_5\) is finite simple.

## Row 2 — Target-vanishing: `PASS`

The 5-part of \(|A_5|=60\) is

\[
  m_5=5.
\]

Take the explicit element \(s=(12345)\in A_5\) and put
\(P=\langle s\rangle\). Let \(\Omega=\operatorname{Syl}_5(A_5)\). The 24
nonidentity 5-cycles found in Row 1 divide into disjoint sets of four generators
of their order-five subgroups, so \(|\Omega|=24/4=6\).

### The six-point action is 2-transitive

The conjugation action is transitive here without leaving a Sylow-conjugacy step
unexpanded. The centralizer of \(P=\langle s\rangle\) is \(P\): it equals the
centralizer of the 5-cycle \(s\), calculated in Row 1. The conjugation map from
\(N_{A_5}(P)\) to \(\operatorname{Aut}(P)\cong C_4\) has kernel
\(C_{A_5}(P)=P\), and therefore induces an injection
\(N_{A_5}(P)/P\hookrightarrow C_4\). The element \((25)(34)\in A_5\)
normalizes \(P\): conjugating the displayed cycle sends
\((1,2,3,4,5)\) to \((1,5,4,3,2)=s^{-1}\). Thus the image has even order. It
cannot have order four, because that would give an
element of \(A_5\) whose image, and hence whose own order, is divisible by four;
the complete cycle-type list in Row 1 has no such element. Therefore
\(|N_{A_5}(P)|=10\), and the conjugacy orbit of \(P\) has size \(60/10=6\).
It is all of \(\Omega\).

The subgroup
\(P\) fixes the point \(P\). It fixes no other point: if
\(Q\in\Omega\) were distinct from \(P\) and normalized by \(P\), conjugation
would give a homomorphism

\[
  P\longrightarrow\operatorname{Aut}(Q).
\]

Here \(|P|=5\), whereas \(Q\cong C_5\) has
\(|\operatorname{Aut}(Q)|=4\), because an automorphism is determined by any of
the four possible images of a generator. The homomorphism is therefore trivial,
so \(P\) centralizes \(Q\). Distinct order-five subgroups intersect trivially;
commutation would make \(PQ\) a subgroup of order \(25\), contradicting
\(25\nmid60\). Thus \(P\) fixes only itself.

Every orbit of the order-five group \(P\) has size \(1\) or \(5\). It follows
that \(P\) is transitive on the other five points of \(\Omega\). Since
\(A_5\) is transitive on \(\Omega\) and a point stabilizer contains a subgroup
transitive on the remaining points, the action is 2-transitive.

### Construction and irreducibility of the degree-five character

Let \(V=\mathbb C[\Omega]\) be the six-dimensional permutation module, with
permutation character \(\pi\). It splits as

\[
 V=\mathbb C\mathbf 1\oplus W,
 \qquad
 W=\left\{\sum_{\omega\in\Omega}a_\omega e_\omega:
                 \sum_{\omega\in\Omega}a_\omega=0\right\}.
\]

The first summand is the trivial module, \(W\) is invariant of dimension five,
and the character of \(W\) is \(\theta=\pi-1\).

To show directly that \(W\) is irreducible, consider an equivariant endomorphism
of \(V\) in the basis \(\{e_\omega\}\). Its matrix entries must be constant on
the \(A_5\)-orbits on \(\Omega\times\Omega\), and conversely every matrix with
that property is equivariant. Two-transitivity gives exactly two such orbits,
the diagonal and the off-diagonal, so

\[
  \dim_{\mathbb C}\operatorname{End}_{A_5}(V)=2.
\]

The fixed vectors of \(V\) are exactly the constant vectors, hence
\(W^{A_5}=0\). The standard Hermitian inner product for which the permutation
basis is orthonormal is invariant; therefore both equivariant cross-homomorphism
spaces between \(\mathbb C\mathbf1\) and \(W\) vanish. Consequently

\[
  2=\dim\operatorname{End}_{A_5}(V)
   =1+\dim\operatorname{End}_{A_5}(W),
\]

so \(\operatorname{End}_{A_5}(W)\) consists only of scalars. If \(W\) had a
nonzero proper invariant subspace, its invariant orthogonal complement would
give a nonscalar equivariant projection. Hence \(W\) is irreducible and
\(\theta\in\operatorname{Irr}(A_5)\) has degree five.

### The explicit zero

A Sylow-5 subgroup \(Q\) is fixed by \(s\) exactly when \(s\) normalizes
\(Q\). Since \(\langle s\rangle=P\), the preceding normalizer argument shows
that the only fixed point is \(P\). The trace of a permutation matrix is its
number of fixed basis vectors, so the permutation character counts fixed points.
Therefore

\[
  \pi(s)=1,
  \qquad
  \theta(s)=\pi(s)-1=0.
\]

Thus the explicit order-five element \(s=(12345)\) is vanishing for the
explicitly constructed irreducible character \(\theta\).

**Row 2 terminal entry:** `PASS` — \(m_5=5\), \(|s|=5\),
\(\theta\in\operatorname{Irr}(A_5)\), and \(\theta(s)=0\), all by the displayed
six-point action argument rather than a character table.

## Row 3 — CS-5: `PASS`

### Direct-power form, derived

We first derive the finite characteristically simple form needed here. Let
\(A\ne1\) be finite and characteristically simple. Induct on \(|A|\). Choose a
minimal nonidentity normal subgroup \(M\triangleleft A\). Every automorphic image
of \(M\) is again minimal normal in \(A\).

Choose a maximal collection \(M_1,\ldots,M_k\) of such images whose product
\(D=M_1\times\cdots\times M_k\) is direct; the collection is nonempty. The
product \(D\) is normal in \(A\). If \(L\) is any other automorphic image of
\(M\), then \(L\cap D\triangleleft A\). Minimality of \(L\) says either
\(L\le D\) or \(L\cap D=1\). In the second case
\([L,D]\le L\cap D=1\): the commutator lies in \(L\) because \(L\) is normal
and in \(D\) because \(D\) is normal. Thus \(L\) centralizes \(D\), so
\(D\times L\) would be a larger direct product,
contrary to maximality. Hence every automorphic image of \(M\) lies in \(D\).

The product of all automorphic images is therefore exactly \(D\): it contains
the chosen factors and every image lies in \(D\). Every automorphism permutes
the set of automorphic images, so this product is nontrivial and characteristic
in \(A\). Characteristic simplicity therefore forces

\[
 A=M_1\times\cdots\times M_k.
\]

If \(k=1\), then \(M_1=A\), and minimal normality says that \(A\) is simple.
If \(k>1\), every \(M_i\) is a proper characteristically simple group: a
characteristic subgroup of \(M_i\) is normalized by \(M_i\), centralized by all
other direct factors, and hence normal in \(A\); minimality of \(M_i\) leaves
only \(1\) and \(M_i\). By induction write \(M_1\cong T^r\) for a simple
group \(T\). Every \(M_i\) is the automorphic image of \(M_1\), hence is also
isomorphic to \(T^r\). Therefore

\[
  A\cong T^{rk}.
\]

Renaming \(rk\) as \(e\), every nontrivial finite characteristically simple
group has the form \(T^e\) for one finite simple \(T\) and \(e\ge1\).

### Exhaustion of the 5-divisible proper divisors

Now let \(A\) be nonabelian characteristically simple with
\(|A|\mid60\) and \(|A|<60\). Write \(A\cong T^e\) as above. The simple group
\(T\) must be nonabelian, because a direct power of an abelian group is abelian.

Suppose for contradiction that \(5\mid|A|\). Then \(5\mid|T|\), while
\(|T|\mid|A|\mid60\) and \(|T|<60\). The possible orders are

\[
  |T|\in\{5,10,15,20,30\}.
\]

- Order \(5\) is cyclic and hence abelian: any nonidentity element has order
  dividing the prime \(5\), so generates the group.
- At orders \(10,15,20\), the number of Sylow-5 subgroups is congruent to one
  modulo five and divides respectively \(2,3,4\); it is therefore one, giving a
  proper nonidentity normal subgroup.
- At order \(30\), simplicity would force six Sylow-5 subgroups and ten
  Sylow-3 subgroups. Distinct prime-order subgroups meet only in the identity, so
  these would already contribute \(6(5-1)=24\) elements of order five and
  \(10(3-1)=20\) elements of order three, more than the 29 nonidentity elements
  available.

No listed order supports a nonabelian simple \(T\). Therefore
\(5\nmid|A|\).

**Row 3 terminal entry:** `PASS` — every proper nonabelian characteristically
simple divisor of \(60\) has order prime to \(5\), by the displayed direct-power
derivation and complete 5-divisible divisor exhaustion.

## Row 4 — Aut-5: `PASS`

Let \(A\ne1\) be characteristically simple, let \(|A|\mid60\), and assume
\(5\nmid|A|\). Then \(|A|\mid12\). Row 3 gives
\(A\cong T^e\) for a finite simple group \(T\), and \(|T|\mid12\).

We now exclude every composite divisor of \(12\) as the order of a simple group,
without invoking a classification.

- At order \(4\), Cauchy's theorem gives a subgroup of order two. It has index
  two and is therefore normal: for an index-two subgroup, the unique nontrivial
  left coset and the unique nontrivial right coset are both its complement.
- At order \(6\), the number of Sylow-3 subgroups is congruent to one modulo
  three and divides two, hence is one.
- At order \(12\), the number of Sylow-3 subgroups is one or four. In the first
  case one is normal. In the second case, the four subgroups contribute eight
  distinct elements of order three. Any Sylow-2 subgroup has order four, and its
  three nonidentity elements must be precisely the three remaining nonidentity
  elements. Thus every Sylow-2 subgroup is the same subgroup, which is normal.

The only simple orders dividing \(12\) are consequently the prime orders two and
three; a group of prime order is cyclic. Hence the complete nontrivial list is

\[
  A\cong C_2,\qquad C_2^2,\qquad C_3,
\]

because \(2^e\mid60\) gives \(e\le2\), while \(3^e\mid60\) gives \(e\le1\).

Their automorphism orders follow directly:

\[
\begin{array}{c|c|c}
A & \text{derivation} & |\operatorname{Aut}(A)|\\ \hline
C_2 & \text{the unique nonidentity element must be fixed} & 1\\
C_2^2 & \text{choose a nonzero first basis image in 3 ways and an independent second in 2 ways} & 6\\
C_3 & \text{send a generator to either of the two generators} & 2
\end{array}
\]

All three automorphism orders are prime to five. If the trivial group is admitted
as characteristically simple, it adds only \(|\operatorname{Aut}(1)|=1\).

**Row 4 terminal entry:** `PASS` — the candidate list is complete and its
automorphism orders are \(1,6,2\), all prime to \(5\).

## Row 5 — simple-order uniqueness: `PASS`

Let \(T\) be an arbitrary finite simple group of order \(60\). It is
nonabelian, since a finite abelian simple group is cyclic of prime order. We show
directly that \(T\cong A_5\).

### Sylow counts

For Sylow-5 subgroups,

\[
 n_5\equiv1\pmod5,
 \qquad n_5\mid12,
\]

so \(n_5=1\) or \(6\). Simplicity excludes one, hence \(n_5=6\).

For Sylow-3 subgroups, \(n_3\equiv1\pmod3\) and \(n_3\mid20\), so
\(n_3\in\{1,4,10\}\). Again \(n_3\ne1\). If \(n_3=4\), conjugation on the
four Sylow-3 subgroups is nontrivial, since none is normal. Its kernel is normal
in \(T\), so simplicity would make the action faithful. This would embed the
order-60 group \(T\) into \(S_4\) of order \(24\), contrary to Lagrange's
divisibility. Therefore \(n_3=10\).

For Sylow-2 subgroups, \(n_2\equiv1\pmod2\) and \(n_2\mid15\). Simplicity
excludes \(n_2=1\). It also excludes \(n_2=3\): the same kernel argument for
the nontrivial conjugation action on three Sylow subgroups would embed \(T\) in
\(S_3\). Thus

\[
  n_2\in\{5,15\}.
\]

### The case \(n_2=5\)

Conjugation on the five Sylow-2 subgroups is nontrivial. Its kernel is normal,
so simplicity makes the action faithful and identifies \(T\) with a subgroup
\(H\le S_5\) of order \(60\). The sign map restricted to \(H\) must be
trivial: otherwise its kernel would be a proper normal subgroup of \(H\) of
order \(30\), contradicting simplicity. Hence \(H\le A_5\); equality of their
orders gives \(H=A_5\). Thus \(T\cong A_5\).

### The case \(n_2=15\)

A group of order four is either cyclic or Klein four: if it has an element of
order four it is cyclic; otherwise choose distinct involutions \(a,b\), note that
\(\langle a\rangle\) has index two and is normal, and obtain
\(ab=ba\) and \(\{1,a,b,ab\}\cong C_2^2\). All Sylow-2 subgroups of \(T\)
are conjugate, so they have the same type.

If they are cyclic, each of the 15 Sylow subgroups has two generators of order
four, and an order-four element generates a unique such subgroup. This gives 30
distinct elements of order four. The six Sylow-5 subgroups give
\(6(5-1)=24\) elements of order five, and the ten Sylow-3 subgroups give
\(10(3-1)=20\) elements of order three. These disjoint sets already contain
74 nonidentity elements, impossible in \(T\).

It remains to suppose all 15 Sylow-2 subgroups are Klein four groups. Let \(t\)
be any involution and choose a Sylow-2 subgroup \(P\) containing it. Since
\(P\cong C_2^2\) is abelian, \(P\le C_T(t)\). Therefore
\(4\mid|C_T(t)|\), and divisibility by \(60\) leaves

\[
  |C_T(t)|\in\{4,12,20,60\}.
\]

The value \(60\) would make \(t\) central, impossible in a nonabelian simple
group. The value \(20\) would give a conjugacy class of size three; conjugation
on that nontrivial class would have normal kernel and hence, by simplicity, embed
\(T\) into \(S_3\), again impossible. Thus every involution class has size
\(15\) or \(5\).

If some involution has a class of size five, conjugation on that class is a
nontrivial action of \(T\) on five points. It is faithful by simplicity, so the
same sign argument as in the \(n_2=5\) case identifies \(T\) with \(A_5\).

Suppose instead that every involution class has size \(15\). Then every
involution \(t\) has \(|C_T(t)|=4\). For \(t\in P\), the inclusion
\(P\le C_T(t)\) is therefore equality. Any Sylow-2 subgroup containing \(t\)
is Klein four and hence lies in \(C_T(t)=P\); it must equal \(P\). Thus each
involution lies in exactly one Sylow-2 subgroup. The 15 Klein-four subgroups
would then contain \(15\cdot3=45\) distinct involutions. Together with the 24
elements of order five and the 20 elements of order three already counted, this
would give 89 nonidentity elements, again impossible.

The last alternative is contradictory, so every simple group \(T\) of order
\(60\) admits a faithful degree-five action and is isomorphic to \(A_5\).

**Row 5 terminal entry:** `PASS` — every finite simple group of order \(60\) is
identified with \(A_5\) by the displayed Sylow, action-kernel, sign, and
involution-incidence argument; no classification theorem is invoked.

## Five-row terminal ledger

| row | line-referenced evidence | terminal entry |
|---|---|---|
| base | lines 29–82: order, complete class sizes, normal-subgroup union test | `PASS` |
| Target-vanishing | lines 84–193: \(m_5=5\), explicit \(s\), six-point module, irreducibility, zero | `PASS` |
| CS-5 | lines 195–267: direct-power derivation and every 5-divisible proper divisor | `PASS` |
| Aut-5 | lines 269–313: complete list \(C_2,C_2^2,C_3\) and automorphism orders \(1,6,2\) | `PASS` |
| uniqueness | lines 315–405: arbitrary simple order-60 group forced into \(A_5\) | `PASS` |

There is no conditional, cited-but-unexpanded, or blank terminal row.

## Fixed order-60 recognition consequence

We now specialize the reviewed prime-power separator without importing any
additional hypothesis. Define

\[
  V_o(X)=\{|x|:x\in X,\ \chi(x)=0
                 \text{ for some }\chi\in\operatorname{Irr}(X)\}.
\]

### Nonsimple groups of order 60 have a normal Sylow-5 subgroup

We prove simultaneously the following two statements: for every divisor
\(d<60\) with \(5\mid d\), every group of order \(d\) has a normal Sylow-5
subgroup; and, at \(d=60\), the same holds for every nonsimple group. If either
statement were false, choose a failed group \(X\) of least order. Let
\(N\ne1\) be minimal normal in \(X\). Every characteristic subgroup of \(N\)
is normal in \(X\), so minimality makes \(N\) characteristically simple; Row 3
then supplies its direct-power form.

If \(5\mid|N|\) and \(N\) is abelian, the simple factor in its direct-power
form is cyclic of prime order: every subgroup of an abelian simple group is
normal, so a nonidentity element generates the whole group, and that cyclic
order must be prime. Divisibility by five therefore makes the factor \(C_5\).
Thus \(N\cong C_5^e\); since \(v_5(60)=1\), one has \(e=1\), so \(N\) itself
is a normal Sylow-5 subgroup. If \(N\) is nonabelian, then \(|N|<60\): at
order 60 this uses that \(X\) is nonsimple, and at a proper divisor it is
automatic. Row 3 then contradicts \(5\mid|N|\).

It remains that \(5\nmid|N|\). The smaller quotient \(X/N\) has order a proper
divisor of \(60\) still divisible by five, so least-order induction gives it a
normal Sylow subgroup \(\overline P\) of order five. Let
\(M\triangleleft X\) be the inverse image of \(\overline P\), and choose
\(P\in\operatorname{Syl}_5(M)\). Since \(N\) is a normal \(5'\)-subgroup
and \(|M:N|=5\), orders give \(|P|=5\), \(P\cap N=1\), and \(M=NP\).
Conjugation gives

\[
  P\longrightarrow\operatorname{Aut}(N).
\]

Row 4 says the target order is prime to five, so the map is trivial. Hence
\([P,N]=1\), and \(P\triangleleft M\). It is the unique Sylow-5 subgroup of
\(M\), hence characteristic in \(M\); since \(M\triangleleft X\), this gives
\(P\triangleleft X\). Finally \(|X|_5=5=|P|\), so \(P\) is a normal
Sylow-5 subgroup of \(X\), contradicting the choice of \(X\). The induction
is complete.

### A normal Sylow-5 subgroup excludes order five from \(V_o\)

Let \(G\) be nonsimple of order \(60\), and let \(P\triangleleft G\) be the
normal subgroup of order five just obtained. Every element of order five lies in
this unique Sylow subgroup. Fix \(1\ne x\in P\). For any
\(\chi\in\operatorname{Irr}(G)\), Clifford restriction has the homogeneous
orbit form

\[
  \chi_P=e\sum_{\lambda\in\mathcal O}\lambda,
\]

where \(e>0\) and \(\mathcal O\) is one nonempty \(G\)-orbit in
\(\operatorname{Irr}(P)\). If the orbit is the trivial character, then
\(\chi(x)=e\ne0\). Otherwise choose a primitive fifth root \(\zeta\) and write

\[
  \chi(x)=e f(\zeta),
  \qquad
  f(T)=\sum_{j\in J}T^j,
  \qquad
  \varnothing\ne J\subseteq\{1,2,3,4\}.
\]

If \(f(\zeta)=0\), the minimal polynomial
\(\Phi_5(T)=1+T+T^2+T^3+T^4\) divides \(f\). This is impossible when
\(\deg f<4\); at degree four, equal leading coefficients would force
\(f=\Phi_5\), contradicting the zero constant coefficient of \(f\). Thus every
nonidentity element of \(P\) is nonvanishing and

\[
  5\notin V_o(G).
\]

### Recognition

Row 2 gives \(5\in V_o(A_5)\). Therefore a finite group \(G\) satisfying

\[
 |G|=60,
 \qquad
 V_o(G)=V_o(A_5)
\]

cannot be nonsimple. It is simple, and Row 5 then gives \(G\cong A_5\).
Consequently the dossier supports exactly the fixed-target statement

\[
 \boxed{\text{For every finite }G,\ |G|=60\text{ and }V_o(G)=V_o(A_5)
        \Longrightarrow G\cong A_5.}
\]

## Active-scope constraint matrix

| constraint_id | role | fixed-target use | evidence | result |
|---|---|---|---|---|
| `19.30-forall-GS` | admissibility | restricted to the single simple target \(S=A_5\) | five-row ledger and integration above | not established universally |
| `19.30-G-finite` | admissibility | arbitrary finite \(G\) of order 60 | induction and recognition above | pass for fixed target |
| `19.30-S-finite-simple` | admissibility | \(S=A_5\) | Row 1 | pass for fixed target |
| `19.30-vanishing-definition` | admissibility | zero of an explicitly constructed irreducible character; exact Clifford use in \(G\) | Row 2 and integration | exact for fixed target |
| `19.30-equal-orders` | admissibility | \(|G|=|A_5|=60\) | Row 1 and recognition hypothesis | pass for fixed target |
| `19.30-equal-vanishing-order-sets` | admissibility | equality of sets, contradicted at the single integer 5 if \(G\) is nonsimple | Row 2 and integration | pass for fixed target |
| `19.30-isomorphic` | target_conclusion | \(G\cong A_5\) | Row 5 and recognition | established only for fixed target |

`witness_equals_target: false`

`active_assignment_answered: no`

## What this does NOT establish

The universal quantifier over every finite simple \(S\) is untouched. This is
one order-60 recognition special case, not an infinite family and not a solution
of the active Kourovka scope.

## How this could be wrong

1. The normalizer calculation or the rank-two endomorphism argument in Row 2
   could fail to establish irreducibility of the constructed five-space.
2. The maximal-direct-subcollection argument in Row 3 could fail to justify the
   single-simple-factor direct-power form, invalidating the divisor exhaustion.
3. The Sylow-2 incidence split in Row 5 could omit a centralizer size or count an
   involution more than once.
4. The reviewed Clifford restriction formula could fail to give one equal-
   multiplicity orbit on \(P\), or the resulting \(0/1\) polynomial could fail
   the stated \(\Phi_5\)-divisibility argument.

These are audit targets, not additional assumptions; every corresponding step is
spelled out above and awaits independent Validator review.

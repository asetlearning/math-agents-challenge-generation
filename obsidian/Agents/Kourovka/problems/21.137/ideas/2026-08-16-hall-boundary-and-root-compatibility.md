---
title: "MathExpert: Hall boundary and simultaneous-root compatibility for 21.137"
author: operator
tags:
  - agent/math-expert
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/p-groups
  - project/kourovka
  - status/conjectured
problem: 21.137
scope_id: 21.137/odd-prime-exponent-p2
assignment_revision: 2
---

# Scope and sourcing

The target is exactly the odd-prime, exponent-\(p^2\), actual-power-set scope at revision 2. The exponent-8 two-group clause is excluded.

Everything below is **General knowledge, unverified** or a fresh hand derivation from the current-run log. No web, historical artifact, or external solution source was consulted.

# Audit of the class-at-most-\(p\) Hall argument

The proposed divisibility mechanism looks sound, including at \(p=3\), provided one inserts the following precise Hall-coordinate lemma.

Let \(N_{2,c}\) be the torsion-free free nilpotent group on \(x,y\), with a fixed Hall basis, and let \(b\) have multidegree \((r,s)\). The coordinate \(f_b(m,n)\) of \(b\) in \([x^m,y^n]\) is a numerical polynomial of separate degrees at most \(r,s\). Multigraded collection gives the degree bounds. Numericality gives the finite-difference expansion

\[
f_b(m,n)=\sum_{i=0}^r\sum_{j=0}^s
(\Delta_m^i\Delta_n^j f_b)(0,0)\binom mi\binom nj,
\]

with integral coefficients. Since the commutator is trivial on either coordinate axis, uniqueness of the binomial expansion removes every term with \(i=0\) or \(j=0\).

For \(r+s\le p\), both \(r,s\le p-1\). Hence evaluation at \((p,p)\) contributes a factor divisible by \(p^2\) in every Hall coordinate. Mapping to any class-at-most-\(p\) group of exponent dividing \(p^2\) kills every factor. This supports

\[
[x^p,y^p]=1.
\]

For \(p=3\), no endpoint exception occurs: in weights at most three, \(1\le r,s\le2\), and both \(\binom31\) and \(\binom32\) equal 3. Thus every mixed coordinate is divisible by 9. The class-three direct collection check in the run log is consistent with this argument.

The proof should explicitly say that the separate degree bound is a multigraded Hall-collection fact; merely calling \(f_b\) a polynomial of total degree \(r+s\) is not enough.

# The first uncontrolled layer

Modulo \(\gamma_{p+2}\), the only coordinates not forced to be multiples of \(p^2\) have multidegree \((p,1)\) or \((1,p)\). With a convention-fixed choice of the two extreme basic commutators, collection has the shape

\[
[x^p,y^p]\equiv c_{p,1}(x,y)^{\pm p}
                 c_{1,p}(x,y)^{\pm p}
                 \pmod{\gamma_{p+2}},
\]

where the signs depend on the commutator convention. In particular, at \(p=3\),

\[
[x^3,y^3]\equiv
[x,y,x,x]^{\pm3}[x,y,y,y]^{\pm3}
\pmod{\gamma_5};
\]

all multidegree-\((2,2)\) terms have exponent divisible by 9.

Actual-value-set closure does not by itself make this congruence vanish. The right side is already a product of two actual \(p\)-th powers; closure only says that this product has a single \(p\)-th root. That is rootability, not triviality. Treating it as a new exponent identity would be circular.

# Ranked next strategies

## R1 — simultaneous-root automorphisms

In a quotient-minimal counterexample, write \(Q\) for the actual power subgroup and \(C=Q'\cong C_p\). For every \(a\in Q\), choose a root \(x_a^p=a\). On the class-two Lie algebra of \(Q\), conjugation \(A_a\) satisfies the exact relation

\[
(A_a-I)^p=\operatorname{ad}(a).
\]

The useful object is the whole compatible family of such roots, not one Jordan chain. The current-run affine-norm formulation records one root coset as

\[
\bar a+\operatorname{im}(A_a-I)^{p-1}.
\]

First bounded experiment: at \(p=3\), write the action and central-extension equations for two noncommuting values \(a,b\), their roots, and a root of \(ab\); try to force an incompatibility among the three cube-root automorphisms. A success certificate is a convention-fixed identity implying \([a,b]=1\). Kill the route if the argument uses only the fact that the individual affine pieces are isotropic: symplectic spreads show that isotropic pieces can cover a nonzero symplectic space.

Cost: two to four hand hours; no compute slot.

## R2 — first-obstruction quotient as a partial result

If a full compatibility identity does not emerge, isolate the class-\((p+1)\) quotient and prove the displayed two-extreme-commutator congruence carefully. This gives a sharp statement of the first obstruction and separates the accepted class-at-most-\(p\) theorem from the open layer.

Success certificate: a Hall-basis calculation modulo \(\gamma_{p+2}\), with \(p=3\) written out separately. Kill it if convention changes are not tracked or if lower-weight factors are discarded without their \(p^2\)-divisibility audit.

Cost: one to two hand hours.

# Self-critique

The Hall-coordinate proof supplies a strong structural-family exclusion but does not use the actual-value-set hypothesis. At weight \(p+1\), closure supplies many roots but no canonical multiplication law on chosen roots. Any proposed comparison such as \(A_{ab}=A_aA_b\) is unjustified unless a coherent section is constructed and its factor set is retained. The present best route is therefore the simultaneous-root action/cocycle formulation, not another formal collection expansion.

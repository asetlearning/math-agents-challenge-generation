---
title: "MathExpert: normal-prime exclusion and Suzuki-criterion audit for 19.30"
author: operator
tags:
  - agent/math-expert
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/characters
  - topic/suzuki-groups
  - project/kourovka
  - status/conjectured
problem: 19.30
scope_id: 19.30/vanishing-order-simple-recognition
assignment_revision: 1
---

# Scope and sourcing

This assesses the clean-run structural exclusions and the corrected all-odd-exponent Suzuki criterion. Everything below is **General knowledge, unverified** or a fresh hand audit. No web or historical solution source was consulted, so none of the named external theorem inputs is cited here.

# Normal Hall subgroup argument

The exclusion for groups of order \(29120\) with normal Hall subgroup \(A\) of order 455 looks sound after one Clifford-theoretic detail is made explicit.

The square-free arithmetic makes \(A\cong C_{455}\), and Schur--Zassenhaus gives \(G=A\rtimes P\), \(|P|=64\). Let \(Q\) be the abelian image of \(P\) in \(\operatorname{Aut}(A)\).

If a lift \(h\in P\) acts nontrivially on one prime factor and trivially on another factor \(C_r\), choose \(\lambda\in\operatorname{Irr}(A)\) moved by \(h\), and \(1\ne a\in C_r\). Let \(I=I_G(\lambda)\), choose an irreducible Clifford correspondent over \(\lambda\), and induce it to \(G\). Every conjugate of \(ah\) has the same image in the abelian action group \(Q\); that image still moves \(\lambda\). Hence the conjugacy class misses \(I\), so the induced irreducible vanishes at \(ah\). Since \(a\) and \(h\) commute, \(|ah|=r|h|\), a forbidden mixed order.

If no such partially trivial action element exists, each nonidentity element of \(Q\) is nontrivial on all three prime factors. Projection to \(\operatorname{Aut}(C_7)_2\cong C_2\) is injective, so \(|Q|\le2\); its nonidentity element, if present, is simultaneous inversion. Clifford restrictions to \(A\) are then multiples of either \(\lambda\) or \(\lambda+\lambda^{-1}\). The latter cannot vanish on odd-order elements, because \(z+z^{-1}=0\) would give \(z^2=-1\), forcing order divisible by four. Thus the odd kernel elements are nonvanishing.

These two cases exhaust the action family. The proof does not need an extension of every \(\lambda\); Clifford correspondence above the inertia group is enough.

# Broader certifiable families

## N13 — arbitrary normal Sylow 13 subgroup

The cleanest enlargement is: **any** group \(G\) of order \(29120\) with normal Sylow subgroup \(C_{13}\) cannot match \(\operatorname{Sz}(8)\).

For \(P=C_p\triangleleft G\) and \(x\ne1\) in \(P\), Clifford restriction has the form

\[
\chi_P=e\sum_{\lambda\in\mathcal O}\lambda.
\]

At a generator \(x\), distinct \(\lambda\)'s give distinct \(p\)-th roots. A nonempty proper subset of those roots cannot sum to zero: its \(0/1\)-coefficient polynomial would have to be a multiple of \(\Phi_p\), but it omits the trivial root. Hence every nonidentity element of \(P\) is nonvanishing. In particular, \(13\notin V(G)\), whereas the current exact table data give \(13\in V(\operatorname{Sz}(8))\).

This family strictly contains the normal-Hall-455 family and does not assume solvability.

## SOLV — all solvable groups of the target order

The logged minimal-normal induction also looks sound. If \(p\) occurs once in the order and does not divide any relevant \(\operatorname{GL}_d(r)\), induction through an elementary-abelian minimal normal subgroup makes the Sylow \(C_p\) normal. For \(29120\), \(p=13\) and \(\operatorname{ord}_{13}(2)=12>6\); for \(32537600\), \(p=41\) and the displayed linear checks cover the other chief-factor dimensions. The preceding normal-prime lemma then excludes all solvable collisions at both orders.

Success certificate: state the induction over all divisor orders, include the Schur--Zassenhaus split of the preimage, and say why the resulting Sylow subgroup is unique and hence characteristic in that preimage.

# Audit of the corrected all-odd-exponent Suzuki criterion

Conditionally on its four named standard inputs, the corrected argument is coherent for composite as well as prime odd exponents.

From general mathematical knowledge, unverified here, the intended inputs are:

1. every nonabelian finite simple group of order prime to 3 is \(\operatorname{Sz}(2^m)\) for odd \(m\ge3\);
2. \(\operatorname{Out}(\operatorname{Sz}(2^m))\) is cyclic of order \(m\);
3. \(\operatorname{Sz}(q)\) has an irreducible complex character of degree \(q^2+1\);
4. a defect-zero irreducible character vanishes on the nontrivial \(p\)-singular classes.

The arithmetic/composition-factor step should be presented as follows. If \(\operatorname{Sz}(2^m)\) divides \(|\operatorname{Sz}(2^n)|\), a primitive prime divisor of \(2^m-1\) has order \(m\) modulo 2. Divisibility into \(2^n-1\) forces \(m\mid n\); divisibility into \(2^{2n}+1\) would give \(m\mid4n\), and oddness again gives \(m\mid n\) (indeed the \(-1\) congruence is then impossible unless the first factor already applies). Thus every proper Suzuki composition-factor exponent divides \(n\).

For a minimal normal subgroup \(T^k\), the 2-parts give \(k\le n/m\). Since \(\operatorname{ord}_p(2)=4n\), one has \(p\equiv1\pmod{4n}\), hence \(k<p\); also \(p\nmid|T|\) and \(p\nmid|\operatorname{Out}(T)|=m\). Therefore \(p\nmid|\operatorname{Aut}(T^k)|\). Together with the stated linear condition for abelian minimal normals, the same strong-induction argument forces a normal Sylow \(C_p\) in every nonsimple same-order group.

On the simple side, the degree-\(q^2+1\) character has full \(p\)-part when \(v_p(|S|)=1\), so the defect-zero input gives \(p\in V(S)\). This separates \(S\) from every nonsimple same-order group.

Two repairs are needed in the note:

- the final limitation saying that the criterion does not cover composite exponents is stale and contradicts the corrected statement and the \(q=512\), \(n=9\), \(p=109\) instance;
- the strong induction should explicitly handle the case in which the minimal normal subgroup is \(C_p\), and should state the wreath-product formula \(\operatorname{Aut}(T^k)=\operatorname{Aut}(T)\wr S_k\) used to exclude \(p\).

# Self-critique

The Hall and normal-prime arguments are classification-free and close broad, sharply defined families. The all-odd Suzuki criterion is much stronger, but it remains citation-dependent in exactly the four places listed above; discovery blindness prevents grounding them in this turn. It is a conditional partial theorem, not an answer to the universal 19.30 scope.

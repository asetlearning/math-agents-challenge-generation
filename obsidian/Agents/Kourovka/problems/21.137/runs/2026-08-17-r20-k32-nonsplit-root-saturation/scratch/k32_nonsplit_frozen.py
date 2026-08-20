#!/usr/bin/env python3
"""Frozen K32-NONSPLIT-ROOT-SATURATION certificate computation.

Scope: Kourovka 21.137, revision 2, p=3 only.

This is one fixed coordinate extension, not a family search.  It uses the two
length-three U-chains in Hom(V,Z), the fixed PF representatives, and the
lexicographically first c-valued Schreier correction satisfying the exact
top-pair normalization.  If any gate fails, the program stops; it never tries
another correction or representative.
"""

from itertools import product

F = range(3)


def fadd(*xs):
    return sum(xs) % 3


def fscale(a, x):
    return tuple((a * t) % 3 for t in x)


def vadd(a, b):
    return tuple((x + y) % 3 for x, y in zip(a, b))


def vneg(a):
    return tuple((-x) % 3 for x in a)


ZERO_K = (0,) * 6
ZERO_W = (0, 0, 0)  # (z exponent mod 9, z1 exponent mod 3, z2 exponent mod 3)


def uk(k):
    """U on K, basis order X0,X1,X2,Y0,Y1,Y2 and N Xi=Xi-1."""
    x0, x1, x2, y0, y1, y2 = k
    return ((x0 + x1) % 3, (x1 + x2) % 3, x2,
            (y0 + y1) % 3, (y1 + y2) % 3, y2)


def uw(w):
    """U on <z> x <z1,z2>, where z^3=c and U fixes z."""
    r, z1, z2 = w
    return ((r + 3 * z1) % 9, (z1 + z2) % 3, z2)


def upow_k(k, n):
    for _ in range(n % 3):
        k = uk(k)
    return k


def upow_w(w, n):
    for _ in range(n % 3):
        w = uw(w)
    return w


# Cross-pairing table b[i][j]=B(Y_i,X_j), in (c,z1,z2) coordinates.
# Same-chain pairings are zero and the reverse cross-pairing is determined by
# alternation.  This is the unique lexicographically first correction after:
# B(Y0,X2)=z2, B(X0,Y2)=2z2, B(Y2,X2)=0, U-equivariance,
# and zero same-chain pairings.  The only solved entries are c-valued Schreier
# corrections; no alternate row is attempted.
B_YX = (
    ((1, 0, 0), (0, 1, 0), (0, 0, 1)),
    ((0, 1, 0), (1, 1, 2), (0, 1, 2)),
    ((0, 0, 1), (2, 1, 2), (0, 0, 0)),
)


def bform(k, l):
    """Alternating F3-bilinear B: K x K -> <c,z1,z2>."""
    x = k[:3]
    y = k[3:]
    xp = l[:3]
    yp = l[3:]
    out = (0, 0, 0)
    for i in F:
        for j in F:
            # y_i*x'_j*B(Y_i,X_j) - x_j*y'_i*B(Y_i,X_j)
            coeff = (y[i] * xp[j] - x[j] * yp[i]) % 3
            out = vadd(out, fscale(coeff, B_YX[i][j]))
    return out


def embed_b(b):
    """Embed (c,z1,z2) into (<z> mod 9,z1,z2) via c=z^3."""
    return ((3 * b[0]) % 9, b[1], b[2])


def wadd(a, b):
    return ((a[0] + b[0]) % 9, (a[1] + b[1]) % 3,
            (a[2] + b[2]) % 3)


def wneg(a):
    return ((-a[0]) % 9, (-a[1]) % 3, (-a[2]) % 3)


def emul(a, b):
    """Multiplication in E=K x W with factor set (1/2)B=2B."""
    k, w = a
    l, v = b
    correction = embed_b(fscale(2, bform(k, l)))
    return (vadd(k, l), wadd(wadd(w, v), correction))


def einv(a):
    k, w = a
    # B(k,k)=0, so the inverse has no correction.
    return (vneg(k), wneg(w))


def uact_e(a, n):
    k, w = a
    return (upow_k(k, n), upow_w(w, n))


IDENTITY = (ZERO_K, ZERO_W, 0)


def gmul(g, h):
    """Normal form e*u^i, chosen so right conjugation by u is U."""
    e, i = (g[:2]), g[2]
    f, j = (h[:2]), h[2]
    moved = uact_e(f, -i)
    out = emul(e, moved)
    return (out[0], out[1], (i + j) % 3)


def ginv(g):
    e, i = (g[:2]), g[2]
    out = uact_e(einv(e), i)
    return (out[0], out[1], (-i) % 3)


def gpow(g, n):
    out = IDENTITY
    base = g
    while n:
        if n & 1:
            out = gmul(out, base)
        base = gmul(base, base)
        n >>= 1
    return out


def comm(a, b):
    """[a,b]=a^-1 b^-1 a b, so a^b=a[a,b]."""
    return gmul(gmul(gmul(ginv(a), ginv(b)), a), b)


def elt(k=ZERO_K, w=ZERO_W, i=0):
    return (tuple(k), tuple(w), i % 3)


K_BASIS = tuple(tuple(1 if i == j else 0 for i in range(6)) for j in range(6))
X0, X1, X2, Y0, Y1, Y2 = K_BASIS
C = (3, 0, 0)
Z1 = (0, 1, 0)
Z2 = (0, 0, 1)


def fail(gate, reason):
    print(f"GATE_{gate}=FAIL")
    print(f"FAIL_REASON={reason}")
    raise SystemExit(gate)


def check_gate0():
    # R0=(K/I) semidirect <u>; the four visible K coordinates are
    # X2,X1,Y2,Y1.  Right conjugation by u sends X2->X2+X1 and
    # Y2->Y2+Y1.
    labels = set(product(F, repeat=5))
    if len(labels) != 3 ** 5:
        fail(0, "five-coordinate normal form count")

    # Cube in the quotient.  Use representatives with X0=Y0=0 and W=0;
    # any bottom terms produced by multiplication are discarded modulo I.
    for x2, x1, y2, y1, i in labels:
        k = (0, x1, x2, 0, y1, y2)
        cube = gpow(elt(k=k, i=i), 3)
        qk = cube[0]
        if (qk[1], qk[2], qk[4], qk[5], cube[2]) != (0, 0, 0, 0, 0):
            fail(0, "R0 has an element of order greater than 3")

    # The two basic commutators are independent, central modulo I.
    cx = comm(elt(k=X2), elt(i=1))
    cy = comm(elt(k=Y2), elt(i=1))
    visible_cx = (cx[0][1], cx[0][2], cx[0][4], cx[0][5])
    visible_cy = (cy[0][1], cy[0][2], cy[0][4], cy[0][5])
    if len({(0, 0, 0, 0), visible_cx, visible_cy}) != 3:
        fail(0, "commutator image does not have the two prescribed generators")
    for celt in (cx, cy):
        for gen in (elt(k=X2), elt(k=Y2), elt(i=1)):
            cc = comm(celt, gen)
            if any((cc[0][j] for j in (1, 2, 4, 5))) or cc[2]:
                fail(0, "commutator image is not central modulo I")

    print("GATE_0=PASS")
    print("R0_NORMAL_FORM=x2^a*x1^b*y2^d*y1^e*u^i, all coordinates in F3")
    print("R0_ORDER=3^5=243")
    print("R0_EXPONENT=3")
    print("R0_RELATIONS=x2,x1,y2,y1 commute; all five generators cube to 1; "
          "u^-1*x2*u=x2*x1; u^-1*y2*u=y2*y1; u fixes x1,y1")
    print(f"R0_COMMUTATOR_GENERATORS={visible_cx},{visible_cy}")
    print("R0_COMMUTATOR_RANK=2")


def check_gate1_extension():
    # Alternation and U-equivariance are the Schreier consistency equations.
    for a in K_BASIS:
        if bform(a, a) != (0, 0, 0):
            fail(1, "B is not alternating")
        for b in K_BASIS:
            if bform(a, b) != fscale(2, bform(b, a)):
                fail(1, "B is not skew-symmetric")
            if bform(uk(a), uk(b)) != (
                    (lambda q: ((q[0] + q[1]) % 3,
                                (q[1] + q[2]) % 3, q[2]))(bform(a, b))):
                fail(1, "B is not U-equivariant")

    # Bilinear factor-set equation; basis triples suffice and are printed as
    # the exact finite Schreier audit.
    zero = (0, 0, 0)
    for a in K_BASIS:
        for b in K_BASIS:
            for d in K_BASIS:
                lhs = vadd(bform(a, b), bform(vadd(a, b), d))
                rhs = vadd(bform(b, d), bform(a, vadd(b, d)))
                if lhs != rhs:
                    fail(1, "factor-set cocycle equation failed")
    if bform(Y0, X2) != (0, 0, 1):
        fail(1, "fixed X2 action on e is wrong")
    if bform(X0, Y2) != (0, 0, 2):
        fail(1, "fixed Y2 action on f is wrong")
    if bform(Y0, X0) != (1, 0, 0):
        fail(1, "preimage P lost [e,f]=c")
    if bform(Y2, X2) != zero:
        fail(1, "top-pair normalization is not the frozen one")

    # Check the five prescribed actions on P by actual conjugation.
    e = elt(k=Y0)
    f = elt(k=X0)
    c = elt(w=C)
    z1 = elt(w=Z1)
    z2 = elt(w=Z2)
    u = elt(i=1)
    x = elt(k=X2)  # X=S_(R_f): e -> e*z2
    y = elt(k=Y2)  # Y=S_(R_e): f -> f*z2^2

    expected_u = (e, f, c, gmul(z1, c), gmul(z2, z1))
    actual_u = tuple(gmul(p, comm(p, u)) for p in (e, f, c, z1, z2))
    if actual_u != expected_u:
        fail(1, "right conjugation by u is not the fixed U")
    if gmul(e, comm(e, x)) != gmul(e, z2) or comm(f, x) != IDENTITY:
        fail(1, "X=S_(R_f) action mismatch")
    if gmul(f, comm(f, y)) != gmul(f, gpow(z2, 2)) or comm(e, y) != IDENTITY:
        fail(1, "Y=S_(R_e) action mismatch")

    # The fixed PF representatives are A_f=X o U and A_e=Y o U under the
    # right-conjugation convention, hence lifts u*x and u*y.
    af = gmul(u, x)
    ae = gmul(u, y)
    af3 = gpow(af, 3)
    ae3 = gpow(ae, 3)
    if af3[0] != X0 or af3[2] != 0 or af3[1][1:] != (0, 0):
        fail(1, "A_f^3 is not f times a permitted <c>-correction")
    if ae3[0] != Y0 or ae3[2] != 0 or ae3[1][1:] != (0, 0):
        fail(1, "A_e^3 is not e times a permitted <c>-correction")

    # Normal forms themselves prove finiteness and order; the checks above
    # prove the multiplication and action equations defining that normal form.
    print("GATE_1=PASS")
    print("SCHREIER_EQUATIONS=alternation, bilinear cocycle, U-equivariance: PASS")
    print("FIXED_ACTIONS=U,S_(R_f),S_(R_e): PASS")
    print(f"A_f_CUBE={af3}")
    print(f"A_e_CUBE={ae3}")
    print("G0_NORMAL_FORM=(K=F3^6, W0=<c,z1,z2>=F3^3, i in F3)")
    print("G0_ORDER=3^10=59049")
    print("G_NORMAL_FORM=(K=F3^6, W=<z>_9 x <z1,z2>_3, i in F3), z^3=c")
    print("G_ORDER=3^11=177147")


def quotient_label_of(g):
    """Label in A=P/<c>, ordered (X0,Y0,z1,z2)."""
    k, w, i = g
    if i != 0 or any(k[j] for j in (1, 2, 4, 5)) or w[0] % 3:
        raise ValueError("cube is outside P")
    return (k[0], k[3], w[1], w[2])


def quadratic_formula(component, i):
    """Expand the z1/z2 quotient component as a quadratic polynomial."""
    names = ("x0", "x1", "x2", "y0", "y1", "y2")

    def q(k):
        g = elt(k=k, i=i)
        return quotient_label_of(gpow(g, 3))[component]

    terms = []
    for a, ea in enumerate(K_BASIS):
        coeff = q(ea)
        if coeff:
            terms.append((coeff, f"{names[a]}^2"))
    for a in range(6):
        for b in range(a + 1, 6):
            coeff = (q(vadd(K_BASIS[a], K_BASIS[b]))
                     - q(K_BASIS[a]) - q(K_BASIS[b])) % 3
            if coeff:
                terms.append((coeff, f"{names[a]}*{names[b]}"))
    return " + ".join((term if coeff == 1 else f"{coeff}*{term}")
                      for coeff, term in terms) or "0"


def check_gate2_labels():
    labels = set()
    all_k = product(F, repeat=6)
    for coords in all_k:
        k = tuple(coords)
        for i in (0, 1, 2):
            cube = gpow(elt(k=k, i=i), 3)
            try:
                labels.add(quotient_label_of(cube))
            except ValueError as exc:
                fail(2, str(exc))

    print("CUBE_FORMULA=for g=(k,w,i), g^3 has E-part "
          "q*U^(-i)(q)*U^(-2i)(q); K-label is (I+U^(-i)+U^(-2i))k; "
          "central correction is 2*(B(k,Ak)+B(k,A^2k)+B(Ak,A^2k)); "
          "the W norm contributes only <c> modulo <c>")
    for i in (1, 2):
        print(f"LABEL_i={i}: X0=x2; Y0=y2; "
              f"z1={quadratic_formula(2, i)}; z2={quadratic_formula(3, i)}")
    print(f"ACTUAL_QUOTIENT_LABEL_COUNT={len(labels)}")
    all_labels = set(product(F, repeat=4))
    if labels != all_labels:
        missing = sorted(all_labels - labels)
        print(f"FIRST_MISSING_QUOTIENT_LABEL={missing[0]}")
        print(f"MISSING_QUOTIENT_LABEL_COUNT={len(missing)}")
        fail(2, "the complete actual cube-label set is a proper subset of P/<c>")

    print("GATE_2=PASS")
    print("ACTUAL_QUOTIENT_LABEL_SET=P/<c>, size 81")


def check_gate3_fibres_and_exponent():
    cubes = set()
    for k in product(F, repeat=6):
        for r in range(9):
            for z1 in F:
                for z2 in F:
                    for i in F:
                        cubes.add(gpow(elt(k=k, w=(r, z1, z2), i=i), 3))

    pset = set()
    for x0, y0, cexp, z1, z2 in product(F, repeat=5):
        pset.add(elt(k=(x0, 0, 0, y0, 0, 0),
                     w=(3 * cexp, z1, z2), i=0))
    if cubes != pset:
        fail(3, f"full actual cube set differs from P: cubes={len(cubes)}, P={len(pset)}")

    for p in pset:
        if gpow(p, 3) != IDENTITY:
            fail(3, "P does not have exponent 3")
    z = elt(w=(1, 0, 0))
    if gpow(z, 9) != IDENTITY or gpow(z, 3) == IDENTITY:
        fail(3, "the central root z does not have order 9")
    e = elt(k=Y0)
    f = elt(k=X0)
    if comm(e, f) != elt(w=C):
        fail(3, "[e,f] is not c")

    print("GATE_3=PASS")
    print("COMPLETE_ACTUAL_CUBE_SET=P")
    print("ACTUAL_CUBE_SET_SIZE=243")
    print("P_IS_SUBGROUP=yes (the displayed P normal form)")
    print("P_EXPONENT=3")
    print("P_NONABELIAN=yes; [e,f]=c=z^3!=1")
    print("G_EXPONENT=9 (all cubes lie in exponent-3 P; z has order 9)")


def main():
    print("STRATEGY=K32-NONSPLIT-ROOT-SATURATION")
    print("PRIME=3")
    print("FROZEN_CORRECTION=B_YX lexicographic row 0")
    check_gate0()
    check_gate1_extension()
    check_gate2_labels()
    check_gate3_fibres_and_exponent()
    print("ALL_GATES=PASS")


if __name__ == "__main__":
    main()

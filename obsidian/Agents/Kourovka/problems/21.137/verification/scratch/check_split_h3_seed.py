#!/usr/bin/env python3
"""Independent exact checker for the bounded 21.137 split H_3(3) seed.

All arithmetic is in F_3.  This checker implements the displayed coordinate laws
directly; it does not import or execute a claimant script.
"""

from itertools import product

P = 3
F = range(P)
I4 = (
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
)
A = (
    (1, 1, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 2, 1),
)
B = (
    (1, 0, 0, 1),
    (0, 1, 1, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
)
C_DISPLAYED = (
    (1, 0, 2, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
)
J = (
    (0, 0, 1, 0),
    (0, 0, 0, 1),
    (2, 0, 0, 0),
    (0, 2, 0, 0),
)


def mm(X, Y):
    return tuple(
        tuple(sum(X[i][k] * Y[k][j] for k in range(4)) % P for j in range(4))
        for i in range(4)
    )


def mv(X, v):
    return tuple(sum(X[i][j] * v[j] for j in range(4)) % P for i in range(4))


def mt(X):
    return tuple(tuple(X[j][i] for j in range(4)) for i in range(4))


def mpow(X, n):
    out = I4
    for _ in range(n):
        out = mm(out, X)
    return out


def omega(v, w):
    x1, x2, y1, y2 = v
    X1, X2, Y1, Y2 = w
    return (x1 * Y1 + x2 * Y2 - y1 * X1 - y2 * X2) % P


def qmul(q, qp):
    a, b, h = q
    ap, bp, hp = qp
    return ((a + ap) % P, (b + bp) % P, (h + hp - b * ap) % P)


def qinv(q):
    a, b, h = q
    return ((-a) % P, (-b) % P, (-h - a * b) % P)


def mq(q):
    a, b, h = q
    return (
        (1, a, (a * b - h) % P, b),
        (0, 1, b, 0),
        (0, 0, 1, 0),
        (0, 0, (-a) % P, 1),
    )


# Element order: (v0,v1,v2,v3,r,s,t,a,b,h).
IDENTITY = (0,) * 10


def gmul(g, gp):
    v, r, s, t, q = g[:4], g[4], g[5], g[6], g[7:]
    vp, rp, sp, tp, qp = gp[:4], gp[4], gp[5], gp[6], gp[7:]
    acted = mv(mq(q), vp)
    vv = tuple((v[i] + acted[i]) % P for i in range(4))
    rr = (r + rp + 2 * omega(v, acted)) % P
    qq = qmul(q, qp)
    return vv + (rr, (s + sp) % P, (t + tp) % P) + qq


def ginv_displayed(g):
    v, r, s, t, q = g[:4], g[4], g[5], g[6], g[7:]
    qi = qinv(q)
    vi = tuple((-x) % P for x in mv(mq(qi), v))
    return vi + ((-r) % P, (-s) % P, (-t) % P) + qi


def gpow(g, n):
    out = IDENTITY
    for _ in range(n):
        out = gmul(out, g)
    return out


def scalar_formula(g):
    _, x2, y1, y2, _, _, _, a, b, h = g
    return (2 * y1 * (a * x2 + b * y2 + (h - a * b) * y1)) % P


def main():
    qs = list(product(F, repeat=3))

    C = mm(mm(mm(mpow(A, 2), mpow(B, 2)), A), B)
    assert C == C_DISPLAYED
    assert mpow(A, 3) == I4 and mpow(B, 3) == I4 and mpow(C, 3) == I4
    assert mm(A, B) == mm(mm(B, A), C)
    assert mm(A, C) == mm(C, A) and mm(B, C) == mm(C, B)
    assert mm(mm(mt(A), J), A) == J and mm(mm(mt(B), J), B) == J

    assert all(qmul(qmul(q, qp), qpp) == qmul(q, qmul(qp, qpp))
               for q in qs for qp in qs for qpp in qs)
    assert all(qmul(q, qinv(q)) == (0, 0, 0) == qmul(qinv(q), q) for q in qs)
    assert all(qmul(qmul(q, q), q) == (0, 0, 0) for q in qs)
    assert qmul((1, 0, 0), (0, 1, 0)) != qmul((0, 1, 0), (1, 0, 0))

    assert all(mq(qmul(q, qp)) == mm(mq(q), mq(qp)) for q in qs for qp in qs)
    assert len({mq(q) for q in qs}) == 27
    assert all(mm(mm(mt(mq(q)), J), mq(q)) == J for q in qs)

    images = set()
    formula_mismatches = 0
    inverse_failures = 0
    ninth_power_failures = 0
    element_count = 0
    for data in product(F, repeat=10):
        g = tuple(data)
        element_count += 1
        gi = ginv_displayed(g)
        if gmul(g, gi) != IDENTITY or gmul(gi, g) != IDENTITY:
            inverse_failures += 1
        cube = gpow(g, 3)
        expected = (0, 0, 0, 0, scalar_formula(g), 0, 0, 0, 0, 0)
        if cube != expected:
            formula_mismatches += 1
        images.add(cube)
        if gpow(cube, 3) != IDENTITY:
            ninth_power_failures += 1

    expected_image = {
        (0, 0, 0, 0, r, 0, 0, 0, 0, 0) for r in F
    }
    assert images == expected_image
    assert all(gmul(x, y) in images for x in images for y in images)
    assert all(ginv_displayed(x) in images for x in images)

    # v=e2+f1 and q=A=(1,0,0) is the claimed order-nine witness.
    witness = (0, 1, 1, 0, 0, 0, 0, 1, 0, 0)
    witness_cube = gpow(witness, 3)
    witness_ninth = gpow(witness, 9)
    assert witness_cube == (0, 0, 0, 0, 2, 0, 0, 0, 0, 0)
    assert witness_ninth == IDENTITY

    print("matrix commutator C matches displayed:", C == C_DISPLAYED)
    print("A,B,C relation AB=BA*C and symplecticity: pass")
    print("Q associative, exponent 3, nonabelian, order:", len(qs))
    print("q -> M_q homomorphism image size:", len({mq(q) for q in qs}))
    print("seed coordinate tuple count:", element_count)
    print("displayed inverse failures:", inverse_failures)
    print("all-element cube-formula mismatches:", formula_mismatches)
    print("literal cube image:", sorted(x[4] for x in images))
    print("literal image subgroup and equals its generated subgroup: True")
    print("ninth-power failures:", ninth_power_failures)
    print("order-nine witness cube central coefficient:", witness_cube[4])


if __name__ == "__main__":
    main()

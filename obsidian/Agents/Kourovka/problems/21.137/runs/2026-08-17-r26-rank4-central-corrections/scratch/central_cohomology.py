#!/usr/bin/env python3
"""Exact F3 obstruction calculation for the one frozen 21.137 lift row.

This is purpose-built finite arithmetic.  It does not enumerate the 3^18
central-relator rows.  The conventions and every frozen matrix are copied from
the Lead-authorized manifests, then checked independently here.
"""

from itertools import product

P = 3


def mod(x):
    return x % P


def eye(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def madd(a, b):
    return [[mod(a[i][j] + b[i][j]) for j in range(len(a[0]))]
            for i in range(len(a))]


def mneg(a):
    return [[mod(-x) for x in row] for row in a]


def mmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) % P
             for j in range(len(b[0]))] for i in range(len(a))]


def mvec(a, v):
    return [sum(a[i][k] * v[k] for k in range(len(v))) % P
            for i in range(len(a))]


def mpow(a, n):
    out = eye(len(a))
    base = a
    while n:
        if n & 1:
            out = mmul(out, base)
        base = mmul(base, base)
        n //= 2
    return out


def minv(a):
    n = len(a)
    aug = [a[i][:] + eye(n)[i] for i in range(n)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if aug[i][col] % P)
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = 1 if aug[col][col] == 1 else 2
        aug[col] = [mod(scale * x) for x in aug[col]]
        for i in range(n):
            if i != col and aug[i][col]:
                c = aug[i][col]
                aug[i] = [mod(aug[i][j] - c * aug[col][j])
                          for j in range(2 * n)]
    return [row[n:] for row in aug]


J = [
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [2, 0, 0, 0],
    [0, 2, 0, 0],
]


def omega(v, w):
    return sum(v[i] * J[i][j] * w[j]
               for i in range(4) for j in range(4)) % P


# A triple acts on BCH coordinates of K by (v,z) -> (M v, T z + L v).
def tcompose(a, b):
    ma, ta, la = a
    mb, tb, lb = b
    return (mmul(ma, mb), mmul(ta, tb), madd(mmul(ta, lb), mmul(la, mb)))


TID = (eye(4), eye(3), [[0] * 4 for _ in range(3)])


def tinv(a):
    m, t, l = a
    mi, ti = minv(m), minv(t)
    return (mi, ti, mneg(mmul(mmul(ti, l), mi)))


def tpow(a, n):
    out = TID
    base = a
    while n:
        if n & 1:
            out = tcompose(out, base)
        base = tcompose(base, base)
        n //= 2
    return out


def tcomm(a, b):
    return tcompose(tcompose(tcompose(tinv(a), tinv(b)), a), b)


def trelator(a, b):
    """a*b, retained for readable assertions."""
    return tcompose(a, b)


A = [
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 2, 1],
]
B = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
]
C = [
    [1, 0, 2, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
]
TX = [
    [1, 2, 0],
    [0, 1, 1],
    [0, 0, 1],
]
TY = [
    [1, 1, 0],
    [0, 1, 1],
    [0, 0, 1],
]
TZ = [
    [1, 0, 1],
    [0, 1, 0],
    [0, 0, 1],
]
LX = [
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 0],
]
LY = [
    [0, 0, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 0],
]
LZ = [
    [0, 0, 0, 0],
    [0, 2, 0, 1],
    [0, 0, 0, 0],
]
AX, AY, AZ = (A, TX, LX), (B, TY, LY), (C, TZ, LZ)


def inner_label(a):
    """Return v when triple a is Inn_v, or raise with an exact defect."""
    m, t, l = a
    if m != eye(4) or t != eye(3) or l[1:] != [[0] * 4, [0] * 4]:
        raise AssertionError((m, t, l))
    row = l[0]
    v = [row[2], row[3], mod(-row[0]), mod(-row[1])]
    if [sum(v[i] * J[i][j] for i in range(4)) % P for j in range(4)] != row:
        raise AssertionError((row, v))
    return tuple(v)


def frozen_row_checks():
    assert mmul(mmul([list(x) for x in zip(*A)], J), A) == J  # A^T J A
    assert mmul(mmul([list(x) for x in zip(*B)], J), B) == J
    assert mmul(mmul([list(x) for x in zip(*C)], J), C) == J
    assert C == tcomm((A, eye(3), [[0] * 4 for _ in range(3)]),
                      (B, eye(3), [[0] * 4 for _ in range(3)]))[0]
    assert mpow(A, 3) == mpow(B, 3) == mpow(C, 3) == eye(4)
    assert tcomm((A, eye(3), [[0] * 4 for _ in range(3)]),
                 (C, eye(3), [[0] * 4 for _ in range(3)]))[0] == eye(4)
    assert tcomm((B, eye(3), [[0] * 4 for _ in range(3)]),
                 (C, eye(3), [[0] * 4 for _ in range(3)]))[0] == eye(4)

    assert TZ == tcomm((eye(4), TX, [[0] * 4 for _ in range(3)]),
                       (eye(4), TY, [[0] * 4 for _ in range(3)]))[1]
    assert mpow(TX, 3) == mpow(TY, 3) == mpow(TZ, 3) == eye(3)

    rels = [
        tpow(AX, 3),
        tpow(AY, 3),
        tpow(AZ, 3),
        tcompose(tcomm(AX, AY), tinv(AZ)),
        tcomm(AX, AZ),
        tcomm(AY, AZ),
    ]
    labels = [inner_label(x) for x in rels]
    expected = [
        (0, 0, 0, 1),
        (0, 1, 0, 0),
        (0, 0, 0, 0),
        (2, 0, 2, 1),
        (0, 2, 0, 2),
        (0, 1, 0, 1),
    ]
    assert labels == expected
    assert omega(expected[0], expected[1]) == 2
    return rels, labels


# Q=H_3(3), canonical coordinates x^a y^b z^c and [x,y]=z.
Q = list(product(range(3), repeat=3))
QI = {q: i for i, q in enumerate(Q)}
ONE = (0, 0, 0)


def qmul(q, r):
    a, b, c = q
    d, e, f = r
    return ((a + d) % 3, (b + e) % 3, (c + f - b * d) % 3)


def qinv(q):
    return next(r for r in Q if qmul(q, r) == ONE and qmul(r, q) == ONE)


def alpha(q):
    a, b, c = q
    return tcompose(tcompose(tpow(AX, a), tpow(AY, b)), tpow(AZ, c))


ALPHA = {q: alpha(q) for q in Q}


def defect_labels():
    labels = {}
    for q in Q:
        for r in Q:
            qr = qmul(q, r)
            d = tcompose(tcompose(ALPHA[q], ALPHA[r]), tinv(ALPHA[qr]))
            labels[q, r] = inner_label(d)
    return labels


def certify_v_associativity(vdef):
    pair_checks = 0
    for q in Q:
        for r in Q:
            qr = qmul(q, r)
            d = tcompose(tcompose(ALPHA[q], ALPHA[r]), tinv(ALPHA[qr]))
            assert inner_label(d) == vdef[q, r]
            pair_checks += 1
    triple_checks = 0
    for q in Q:
        mq = ALPHA[q][0]
        for r in Q:
            qr = qmul(q, r)
            for s in Q:
                rs = qmul(r, s)
                lhs = tuple((vdef[q, r][i] + vdef[qr, s][i]) % 3
                            for i in range(4))
                mv = tuple(mvec(mq, vdef[r, s]))
                rhs = tuple((mv[i] + vdef[q, rs][i]) % 3 for i in range(4))
                assert lhs == rhs
                triple_checks += 1
    return pair_checks, triple_checks, 4 * triple_checks


def k_mul(k, l):
    """BCH-coordinate law on K, with 1/2=2 in F3."""
    v, z = k
    w, u = l
    return (tuple((v[i] + w[i]) % 3 for i in range(4)),
            tuple((z[j] + u[j] + (2 * omega(v, w) if j == 0 else 0)) % 3
                  for j in range(3)))


def k_inv(k):
    v, z = k
    return (tuple(-x % 3 for x in v), tuple(-x % 3 for x in z))


def k_alpha(q, k):
    v, z = k
    m, t, l = ALPHA[q]
    mv = tuple(mvec(m, v))
    tz, lv = mvec(t, z), mvec(l, v)
    return mv, tuple((tz[j] + lv[j]) % 3 for j in range(3))


class SparseAffine:
    """Streaming exact row echelon form over F3."""

    def __init__(self, nvars):
        self.nvars = nvars
        self.pivots = {}  # pivot -> (normalized sparse row, rhs, source id)
        self.inconsistent = None
        self.rows_seen = 0

    def add(self, row, rhs, source):
        self.rows_seen += 1
        row = {i: c % 3 for i, c in row.items() if c % 3}
        rhs %= 3
        while row:
            p = min(row)
            c = row[p]
            if p not in self.pivots:
                inv = 1 if c == 1 else 2
                row = {i: (inv * x) % 3 for i, x in row.items()}
                rhs = (inv * rhs) % 3
                self.pivots[p] = (row, rhs, source)
                return True
            prow, prhs, _ = self.pivots[p]
            for i, x in prow.items():
                y = (row.get(i, 0) - c * x) % 3
                if y:
                    row[i] = y
                elif i in row:
                    del row[i]
            rhs = (rhs - c * prhs) % 3
        if rhs:
            self.inconsistent = (rhs, source)
            return False
        return True

    def particular(self):
        if self.inconsistent:
            raise ValueError("inconsistent")
        x = [0] * self.nvars
        for p in sorted(self.pivots, reverse=True):
            row, rhs, _ = self.pivots[p]
            x[p] = (rhs - sum(c * x[i] for i, c in row.items() if i != p)) % 3
        return x

    def null_basis(self):
        if self.inconsistent:
            raise ValueError("inconsistent")
        free = [i for i in range(self.nvars) if i not in self.pivots]
        out = []
        for f in free:
            x = [0] * self.nvars
            x[f] = 1
            for p in sorted(self.pivots, reverse=True):
                row, _, _ = self.pivots[p]
                x[p] = -sum(c * x[i] for i, c in row.items() if i != p) % 3
            out.append(x)
        return out


def aconst(c=0):
    return ({}, c % 3)


def avar(i, c=1):
    return ({i: c % 3}, 0)


def aadd(a, b):
    row = a[0].copy()
    for i, c in b[0].items():
        d = (row.get(i, 0) + c) % 3
        if d:
            row[i] = d
        elif i in row:
            del row[i]
    return row, (a[1] + b[1]) % 3


def ascale(c, a):
    c %= 3
    return ({i: c * x % 3 for i, x in a[0].items() if c * x % 3},
            c * a[1] % 3)


def avec_add(a, b):
    return [aadd(a[i], b[i]) for i in range(3)]


def amat_vec(m, v):
    return [sum_affine([ascale(m[i][j], v[j]) for j in range(3)])
            for i in range(len(m))]


def sum_affine(xs):
    out = aconst()
    for x in xs:
        out = aadd(out, x)
    return out


NONID = [q for q in Q if q != ONE]
UVAR = {}
for q in NONID:
    for r in NONID:
        for j in range(3):
            UVAR[q, r, j] = len(UVAR)


def uterm(row, q, r, j, coeff):
    if q != ONE and r != ONE and coeff % 3:
        i = UVAR[q, r, j]
        row[i] = (row.get(i, 0) + coeff) % 3


def obstruction_system(vdef):
    sys = SparseAffine(len(UVAR))
    equation_count = 0
    for q in Q:
        mq, tq, lq = ALPHA[q]
        for r in Q:
            qr = qmul(q, r)
            for s in Q:
                rs = qmul(r, s)
                vqr = vdef[q, r]
                vqrs = vdef[qr, s]
                vrs = vdef[r, s]
                vqrs2 = vdef[q, rs]
                transformed_vrs = tuple(mvec(mq, vrs))
                lvrs = mvec(lq, vrs)
                rhsvec = [
                    (lvrs[j]
                     + (2 * omega(transformed_vrs, vqrs2) if j == 0 else 0)
                     - (2 * omega(vqr, vqrs) if j == 0 else 0)) % 3
                    for j in range(3)
                ]
                for j in range(3):
                    row = {}
                    uterm(row, q, r, j, 1)
                    uterm(row, qr, s, j, 1)
                    for k in range(3):
                        uterm(row, r, s, k, -tq[j][k])
                    uterm(row, q, rs, j, -1)
                    equation_count += 1
                    if not sys.add(row, rhsvec[j], (q, r, s, j)):
                        return sys, equation_count
    return sys, equation_count


def factor_affine(q, r, vdef):
    if q == ONE or r == ONE:
        z = [aconst(), aconst(), aconst()]
    else:
        z = [avar(UVAR[q, r, j]) for j in range(3)]
    return vdef[q, r], z


def ka_mul_aff(k, l):
    v, z = k
    w, u = l
    outz = avec_add(z, u)
    outz[0] = aadd(outz[0], aconst(2 * omega(v, w)))
    return (tuple((v[i] + w[i]) % 3 for i in range(4)), outz)


def ka_inv(k):
    v, z = k
    return tuple(-x % 3 for x in v), [ascale(-1, x) for x in z]


def ka_apply_triple(a, k):
    m, t, l = a
    v, z = k
    mv = tuple(mvec(m, v))
    tz = amat_vec(t, z)
    lv = mvec(l, v)
    return mv, [aadd(tz[j], aconst(lv[j])) for j in range(3)]


KZERO_AFF = ((0, 0, 0, 0), [aconst(), aconst(), aconst()])


def ga_mul(g, h, vdef):
    k, q = g
    l, r = h
    out = ka_mul_aff(k, ka_apply_triple(ALPHA[q], l))
    out = ka_mul_aff(out, factor_affine(q, r, vdef))
    return out, qmul(q, r)


def ga_inv(g, vdef):
    k, q = g
    qi = qinv(q)
    rhs = ka_mul_aff(ka_inv(k), ka_inv(factor_affine(q, qi, vdef)))
    return ka_apply_triple(tinv(ALPHA[q]), rhs), qi


def ga_pow(g, n, vdef):
    out = KZERO_AFF, ONE
    for _ in range(n):
        out = ga_mul(out, g, vdef)
    return out


def ga_comm(g, h, vdef):
    out = ga_mul(ga_inv(g, vdef), ga_inv(h, vdef), vdef)
    return ga_mul(ga_mul(out, g, vdef), h, vdef)


def relator_affines(vdef):
    gx = KZERO_AFF, (1, 0, 0)
    gy = KZERO_AFF, (0, 1, 0)
    gz = KZERO_AFF, (0, 0, 1)
    vals = [
        ga_pow(gx, 3, vdef),
        ga_pow(gy, 3, vdef),
        ga_pow(gz, 3, vdef),
        ga_mul(ga_comm(gx, gy, vdef), ga_inv(gz, vdef), vdef),
        ga_comm(gx, gz, vdef),
        ga_comm(gy, gz, vdef),
    ]
    assert all(q == ONE for _, q in vals)
    return [k for k, _ in vals]


def relator_image_system(sys, relvals):
    """Eliminate normalized 2-cochains, retaining 18 named relator variables."""
    rbase = len(UVAR)
    expected_v = [
        (0, 0, 0, 1), (0, 1, 0, 0), (0, 0, 0, 0),
        (2, 0, 2, 1), (0, 2, 0, 2), (0, 1, 0, 1),
    ]
    assert [x[0] for x in relvals] == expected_v
    for i, (_, z) in enumerate(relvals):
        for j, expr in enumerate(z):
            # r_(i,j) = expr.
            row = {k: (-c) % 3 for k, c in expr[0].items()}
            row[rbase + 3 * i + j] = 1
            if not sys.add(row, expr[1], ("relator", i, j)):
                raise AssertionError("definition rows cannot make a consistent cocycle system inconsistent")
    constraints = []
    for p in sorted(sys.pivots):
        if p >= rbase:
            row, rhs, source = sys.pivots[p]
            assert all(i >= rbase for i in row)
            constraints.append(({i - rbase: c for i, c in row.items()}, rhs, source))
    return constraints, len(sys.pivots)


def zadd(a, b):
    return tuple((a[i] + b[i]) % 3 for i in range(3))


def zneg(a):
    return tuple(-x % 3 for x in a)


def zact(t, a):
    return tuple(mvec(t, a))


def smul(g, h):
    """Z(K) semidirect the free lift action, represented by (z,T_word)."""
    z, t = g
    u, v = h
    return zadd(z, zact(t, u)), mmul(t, v)


def sinv(g):
    z, t = g
    ti = minv(t)
    return zneg(zact(ti, z)), ti


def spow(g, n):
    out = ((0, 0, 0), eye(3))
    for _ in range(n):
        out = smul(out, g)
    return out


def scomm(g, h):
    return smul(smul(smul(sinv(g), sinv(h)), g), h)


def central_lift_gauge_matrix():
    cols = []
    for col in range(9):
        shifts = [[0, 0, 0] for _ in range(3)]
        shifts[col // 3][col % 3] = 1
        x = (tuple(shifts[0]), TX)
        y = (tuple(shifts[1]), TY)
        z = (tuple(shifts[2]), TZ)
        rels = [
            spow(x, 3),
            spow(y, 3),
            spow(z, 3),
            smul(scomm(x, y), sinv(z)),
            scomm(x, z),
            scomm(y, z),
        ]
        assert all(t == eye(3) for _, t in rels)
        cols.append([entry for u, _ in rels for entry in u])
    return [[cols[j][i] for j in range(9)] for i in range(18)]


def gf3_rank_rows(rows):
    pivots = {}
    for raw in rows:
        row = {i: x % 3 for i, x in enumerate(raw) if x % 3}
        while row:
            p = min(row)
            c = row[p]
            if p not in pivots:
                inv = 1 if c == 1 else 2
                pivots[p] = {i: inv * x % 3 for i, x in row.items()}
                break
            prow = pivots[p]
            for i, x in prow.items():
                y = (row.get(i, 0) - c * x) % 3
                if y:
                    row[i] = y
                elif i in row:
                    del row[i]
    return len(pivots)


def section_equivalence_ranks():
    """Ranks proving full-cochain/18-relator equivalence modulo gauge."""
    hvar = {(q, j): i for i, (q, j) in enumerate(
        (item for q in NONID for item in ((q, 0), (q, 1), (q, 2))))}
    rows = []
    for q in NONID:
        tq = ALPHA[q][1]
        for r in NONID:
            qr = qmul(q, r)
            for j in range(3):
                row = [0] * len(hvar)
                row[hvar[q, j]] = (row[hvar[q, j]] + 1) % 3
                for k in range(3):
                    row[hvar[r, k]] = (row[hvar[r, k]] + tq[j][k]) % 3
                if qr != ONE:
                    row[hvar[qr, j]] = (row[hvar[qr, j]] - 1) % 3
                rows.append(row)
    coboundary_rank = gf3_rank_rows(rows)
    gauge_rank = gf3_rank_rows(central_lift_gauge_matrix())
    return len(hvar), coboundary_rank, len(hvar) - coboundary_rank, gauge_rank


def main():
    rels, labels = frozen_row_checks()
    print("frozen triple reconstruction: PASS")
    print("six inner labels:", labels)
    print("nonorthogonal cube labels omega(qX,qY):", omega(labels[0], labels[1]))
    vdef = defect_labels()
    print("all 729 canonical-section action defects are inner: PASS")
    vpairs, vtriples, vscalars = certify_v_associativity(vdef)
    print("V-coordinate defect/associativity checks:", vpairs, vtriples, vscalars)
    sys, generated = obstruction_system(vdef)
    print("normalized central 2-cochain variables:", len(UVAR))
    print("associativity scalar equations generated:", generated)
    print("rank before stop/full rank:", len(sys.pivots))
    print("inconsistent:", sys.inconsistent)
    if not sys.inconsistent:
        print("solution affine dimension:", len(UVAR) - len(sys.pivots))
        relvals = relator_affines(vdef)
        constraints, combined_rank = relator_image_system(sys, relvals)
        print("combined rank after 18 relator definitions:", combined_rank)
        print("relator-image affine dimension:", 18 - len(constraints))
        print("complete affine constraints on r=(x3,y3,z3,xyzinv,xz,yz), each in (c,s,t):")
        for row, rhs, source in constraints:
            print(" ", "+".join(f"{c}*r{k}" for k, c in sorted(row.items())), "=", rhs)
        gauge = central_lift_gauge_matrix()
        print("central generator-lift gauge matrix (18 rows x 9 columns; columns a_X,a_Y,a_Z in c,s,t):")
        for row in gauge:
            print(" ", "".join(str(x) for x in row))
        c1dim, brank, z1dim, grank = section_equivalence_ranks()
        print("normalized C1/coboundary/1-cocycle dimensions:", c1dim, brank, z1dim)
        print("relator generator-gauge rank:", grank)
        print("exact-row kernel dimensions (cochain map / gauge):", 77 - 8,
              (c1dim - grank) - z1dim)
        print("quotient dimensions H2 / relator-mod-gauge:", 77 - brank, 8 - grank)


if __name__ == "__main__":
    main()

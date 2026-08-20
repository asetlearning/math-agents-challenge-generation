#!/usr/bin/env python3
"""Independent finite certificate checker for one frozen 21.137 family.

This checker was written without reading or importing the claimant's algorithms.
The nine frozen input arrays were extracted as literal data from the hash-pinned
submission; all algebra, elimination, orbit construction, factor extraction, and
literal-cube enumeration below are independent.
"""

from __future__ import annotations

import hashlib
import itertools
import sys
from dataclasses import dataclass


P = 3


def mod(x: int) -> int:
    return x % P


def vadd(a, b):
    return tuple((x + y) % P for x, y in zip(a, b))


def vsub(a, b):
    return tuple((x - y) % P for x, y in zip(a, b))


def vscale(c, a):
    return tuple((c * x) % P for x in a)


def mmul(a, b):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(len(b))) % P
              for j in range(len(b[0])))
        for i in range(len(a))
    )


def mvec(a, v):
    return tuple(sum(row[j] * v[j] for j in range(len(v))) % P for row in a)


def madd(a, b):
    return tuple(tuple((x + y) % P for x, y in zip(ra, rb))
                 for ra, rb in zip(a, b))


def mscale(c, a):
    return tuple(tuple((c * x) % P for x in row) for row in a)


def eye(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def minv(a):
    n = len(a)
    z = [list(row) + list(eye(n)[i]) for i, row in enumerate(a)]
    for c in range(n):
        pivot = next(i for i in range(c, n) if z[i][c] % P)
        z[c], z[pivot] = z[pivot], z[c]
        if z[c][c] == 2:
            z[c] = [(2 * x) % P for x in z[c]]
        for i in range(n):
            if i != c and z[i][c]:
                factor = z[i][c]
                z[i] = [(x - factor * y) % P for x, y in zip(z[i], z[c])]
    return tuple(tuple(row[n:]) for row in z)


J = (
    (0, 0, 1, 0),
    (0, 0, 0, 1),
    (2, 0, 0, 0),
    (0, 2, 0, 0),
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
C = (
    (1, 0, 2, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
)

TX = (
    (1, 2, 0),
    (0, 1, 1),
    (0, 0, 1),
)
TY = (
    (1, 1, 0),
    (0, 1, 1),
    (0, 0, 1),
)
TZ = (
    (1, 0, 1),
    (0, 1, 0),
    (0, 0, 1),
)

LX = (
    (0, 0, 0, 0),
    (1, 1, 0, 0),
    (0, 0, 0, 0),
)
LY = (
    (0, 0, 0, 0),
    (1, 0, 0, 0),
    (0, 0, 0, 0),
)
LZ = (
    (0, 0, 0, 0),
    (0, 2, 0, 1),
    (0, 0, 0, 0),
)


def omega(v, w):
    return sum(v[i] * J[i][j] * w[j] for i in range(4) for j in range(4)) % P


# Automorphisms are triples (M,T,L), acting by (v,z) -> (Mv,Tz+Lv).
def acomp(g, h):
    m, t, l = g
    n, u, r = h
    return mmul(m, n), mmul(t, u), madd(mmul(t, r), mmul(l, n))


def ainv(g):
    m, t, l = g
    mi, ti = minv(m), minv(t)
    return mi, ti, mscale(2, mmul(mmul(ti, l), mi))


def apow(g, n):
    out = (eye(4), eye(3), tuple(tuple(0 for _ in range(4)) for _ in range(3)))
    for _ in range(n):
        out = acomp(out, g)
    return out


AX = (A, TX, LX)
AY = (B, TY, LY)
AZ = (C, TZ, LZ)
AID = (eye(4), eye(3), tuple(tuple(0 for _ in range(4)) for _ in range(3)))


Q = tuple(itertools.product(range(P), repeat=3))
QINDEX = {q: i for i, q in enumerate(Q)}
QID = QINDEX[(0, 0, 0)]


def qmul_tuple(q, r):
    a, b, c = q
    d, e, f = r
    return ((a + d) % P, (b + e) % P, (c + f - b * d) % P)


def qinv_tuple(q):
    a, b, c = q
    return ((-a) % P, (-b) % P, (-c - a * b) % P)


QMUL = tuple(tuple(QINDEX[qmul_tuple(q, r)] for r in Q) for q in Q)
QINV = tuple(QINDEX[qinv_tuple(q)] for q in Q)


def action_for_q(q):
    a, b, c = q
    return acomp(acomp(apow(AX, a), apow(AY, b)), apow(AZ, c))


ACTIONS = tuple(action_for_q(q) for q in Q)
ACTION_INVS = tuple(ainv(g) for g in ACTIONS)


KID = ((0, 0, 0, 0), (0, 0, 0))


def kmul(k, h):
    v, z = k
    w, u = h
    cross = (2 * omega(v, w)) % P
    return vadd(v, w), ((z[0] + u[0] + cross) % P,
                        (z[1] + u[1]) % P,
                        (z[2] + u[2]) % P)


def kinv(k):
    v, z = k
    return vscale(2, v), vscale(2, z)


def kpow(k, n):
    out = KID
    for _ in range(n):
        out = kmul(out, k)
    return out


def kact(g, k):
    m, t, l = g
    v, z = k
    return mvec(m, v), vadd(mvec(t, z), mvec(l, v))


def inner_label(g):
    m, t, l = g
    assert m == eye(4) and t == eye(3)
    assert l[1] == (0, 0, 0, 0) and l[2] == (0, 0, 0, 0)
    matches = [v for v in itertools.product(range(P), repeat=4)
               if tuple(omega(v, e) for e in eye(4)) == l[0]]
    assert len(matches) == 1
    return matches[0]


def derive_action_defects():
    defects = [[None] * 27 for _ in range(27)]
    count = 0
    for qi in range(27):
        for ri in range(27):
            qri = QMUL[qi][ri]
            d = acomp(acomp(ACTIONS[qi], ACTIONS[ri]), ACTION_INVS[qri])
            defects[qi][ri] = inner_label(d)
            count += 1
    vtriples = 0
    vscalars = 0
    for qi in range(27):
        mq = ACTIONS[qi][0]
        for ri in range(27):
            qri = QMUL[qi][ri]
            for si in range(27):
                rsi = QMUL[ri][si]
                lhs = vadd(defects[qi][ri], defects[qri][si])
                rhs = vadd(mvec(mq, defects[ri][si]), defects[qi][rsi])
                assert lhs == rhs
                vtriples += 1
                vscalars += 4
    return defects, count, vtriples, vscalars


def uindex(qi, ri, c):
    if qi == QID or ri == QID:
        return None
    return (((qi - 1) * 26 + (ri - 1)) * 3 + c)


NVAR = 26 * 26 * 3


def uget(u, qi, ri):
    if qi == QID or ri == QID:
        return (0, 0, 0)
    j = uindex(qi, ri, 0)
    return tuple(u[j + c] for c in range(3))


def add_coeff(row, j, c):
    if j is None:
        return
    row[j] = (row.get(j, 0) + c) % P
    if row[j] == 0:
        del row[j]


def trit_add(a1, a2, b1, b2):
    an = a1 | a2
    bn = b1 | b2
    c1 = (a1 & ~bn) | (b1 & ~an) | (a2 & b2)
    c2 = (a2 & ~bn) | (b2 & ~an) | (a1 & b1)
    return c1, c2


def bits_from_sparse(row):
    a1 = a2 = 0
    for j, c in row.items():
        if c == 1:
            a1 |= 1 << j
        elif c == 2:
            a2 |= 1 << j
    return a1, a2


def bit_coeffs(a1, a2):
    while a1:
        b = a1 & -a1
        yield b.bit_length() - 1, 1
        a1 ^= b
    while a2:
        b = a2 & -a2
        yield b.bit_length() - 1, 2
        a2 ^= b


@dataclass
class Mod3Reducer:
    n: int

    def __post_init__(self):
        self.rows = {}
        self.inconsistent = None

    def add(self, sparse, rhs):
        a1, a2 = bits_from_sparse(sparse)
        rhs %= P
        while a1 | a2:
            bit = (a1 | a2) & -(a1 | a2)
            p = bit.bit_length() - 1
            old = self.rows.get(p)
            if old is None:
                if a2 & bit:
                    a1, a2 = a2, a1
                    rhs = (2 * rhs) % P
                self.rows[p] = (a1, a2, rhs)
                return True
            b1, b2, br = old
            if a1 & bit:
                a1, a2 = trit_add(a1, a2, b2, b1)
                rhs = (rhs + 2 * br) % P
            else:
                a1, a2 = trit_add(a1, a2, b1, b2)
                rhs = (rhs + br) % P
        if rhs:
            self.inconsistent = rhs
        return False

    @property
    def rank(self):
        return len(self.rows)

    def solve(self):
        assert self.inconsistent is None
        pivots = set(self.rows)
        free = [j for j in range(self.n) if j not in pivots]

        def backsolve(free_seed=None):
            x = [0] * self.n
            if free_seed is not None:
                x[free_seed] = 1
            for p in sorted(pivots, reverse=True):
                a1, a2, rhs = self.rows[p]
                total = 0
                for j, c in bit_coeffs(a1 & ~(1 << p), a2):
                    total += c * x[j]
                x[p] = (rhs - total) % P
            return x

        particular = backsolve()
        basis = []
        for f in free:
            x = [0] * self.n
            x[f] = 1
            for p in sorted(pivots, reverse=True):
                a1, a2, _ = self.rows[p]
                total = 0
                for j, c in bit_coeffs(a1 & ~(1 << p), a2):
                    total += c * x[j]
                x[p] = (-total) % P
            basis.append(x)
        return particular, basis


def central_rhs(defects, qi, ri, si):
    qri = QMUL[qi][ri]
    rsi = QMUL[ri][si]
    mq, _, lq = ACTIONS[qi]
    vrs = defects[ri][si]
    vqrs = defects[qi][rsi]
    vqr = defects[qi][ri]
    vqrs2 = defects[qri][si]
    out = list(mvec(lq, vrs))
    out[0] = (out[0]
              + 2 * omega(mvec(mq, vrs), vqrs)
              - 2 * omega(vqr, vqrs2)) % P
    return tuple(out)


def central_equation_row(defects, qi, ri, si, c):
    qri = QMUL[qi][ri]
    rsi = QMUL[ri][si]
    tq = ACTIONS[qi][1]
    row = {}
    add_coeff(row, uindex(qi, ri, c), 1)
    add_coeff(row, uindex(qri, si, c), 1)
    for d in range(3):
        add_coeff(row, uindex(ri, si, d), -tq[c][d])
    add_coeff(row, uindex(qi, rsi, c), -1)
    return row, central_rhs(defects, qi, ri, si)[c]


def build_central_system(defects):
    red = Mod3Reducer(NVAR)
    count = 0
    for qi in range(27):
        for ri in range(27):
            for si in range(27):
                for c in range(3):
                    row, rhs = central_equation_row(defects, qi, ri, si, c)
                    red.add(row, rhs)
                    assert red.inconsistent is None
                    count += 1
    particular, basis = red.solve()
    return red, particular, basis, count


def uadd(a, b, c=1):
    return [(x + c * y) % P for x, y in zip(a, b)]


def check_factor_equations(defects, u):
    checked = 0
    for qi in range(27):
        for ri in range(27):
            qri = QMUL[qi][ri]
            tq = ACTIONS[qi][1]
            for si in range(27):
                rsi = QMUL[ri][si]
                lhs = vsub(vadd(uget(u, qi, ri), uget(u, qri, si)),
                           vadd(mvec(tq, uget(u, ri, si)), uget(u, qi, rsi)))
                assert lhs == central_rhs(defects, qi, ri, si)
                checked += 1
    return checked


class CrossedProduct:
    def __init__(self, defects, u):
        self.factor = tuple(tuple((defects[q][r], uget(u, q, r))
                                  for r in range(27)) for q in range(27))

    def mul(self, g, h):
        k, qi = g
        l, ri = h
        left = kmul(k, kact(ACTIONS[qi], l))
        return kmul(left, self.factor[qi][ri]), QMUL[qi][ri]

    def inv(self, g):
        k, qi = g
        ri = QINV[qi]
        target = kmul(kinv(k), kinv(self.factor[qi][ri]))
        return kact(ACTION_INVS[qi], target), ri

    def pow(self, g, n):
        out = (KID, QID)
        for _ in range(n):
            out = self.mul(out, g)
        return out

    def comm(self, g, h):
        return self.mul(self.mul(self.mul(self.inv(g), self.inv(h)), g), h)


QX = QINDEX[(1, 0, 0)]
QY = QINDEX[(0, 1, 0)]
QZ = QINDEX[(0, 0, 1)]
RELATOR_V = (
    (0, 0, 0, 1),
    (0, 1, 0, 0),
    (0, 0, 0, 0),
    (2, 0, 2, 1),
    (0, 2, 0, 2),
    (0, 1, 0, 1),
)


def relator_row(defects, u, lift_centers=None):
    cp = CrossedProduct(defects, u)
    if lift_centers is None:
        lift_centers = ((0, 0, 0),) * 3
    x = (((0, 0, 0, 0), lift_centers[0]), QX)
    y = (((0, 0, 0, 0), lift_centers[1]), QY)
    z = (((0, 0, 0, 0), lift_centers[2]), QZ)
    vals = (
        cp.pow(x, 3),
        cp.pow(y, 3),
        cp.pow(z, 3),
        cp.mul(cp.comm(x, y), cp.inv(z)),
        cp.comm(x, z),
        cp.comm(y, z),
    )
    out = []
    for i, (k, qi) in enumerate(vals):
        assert qi == QID
        v, central = k
        assert v == RELATOR_V[i]
        out.extend(central)
    return tuple(out)


def dense_rank(vectors):
    basis = {}
    for original in vectors:
        v = list(original)
        while True:
            p = next((i for i, x in enumerate(v) if x), None)
            if p is None:
                break
            if p not in basis:
                if v[p] == 2:
                    v = [(2 * x) % P for x in v]
                basis[p] = v
                break
            c = v[p]
            v = [(x - c * y) % P for x, y in zip(v, basis[p])]
    return len(basis)


def independent_indices(vectors):
    basis = {}
    chosen = []
    for idx, original in enumerate(vectors):
        v = list(original)
        while True:
            p = next((i for i, x in enumerate(v) if x), None)
            if p is None:
                break
            if p not in basis:
                if v[p] == 2:
                    v = [(2 * x) % P for x in v]
                basis[p] = v
                chosen.append(idx)
                break
            c = v[p]
            v = [(x - c * y) % P for x, y in zip(v, basis[p])]
    return chosen


def row_add(a, b, c=1):
    return tuple((x + c * y) % P for x, y in zip(a, b))


def delta_column(hqi, hc):
    # Normalized central one-cochain supported at one nonidentity quotient value.
    out = [0] * NVAR
    unit = tuple(int(i == hc) for i in range(3))
    for qi in range(1, 27):
        tq = ACTIONS[qi][1]
        for ri in range(1, 27):
            qri = QMUL[qi][ri]
            val = (0, 0, 0)
            if qi == hqi:
                val = vadd(val, unit)
            if ri == hqi:
                val = vadd(val, mvec(tq, unit))
            if qri == hqi:
                val = vsub(val, unit)
            j = uindex(qi, ri, 0)
            out[j:j + 3] = val
    return out


EXPECTED_G_ROWS = (
    "002000000", "000000000", "000000000",
    "000001000", "000000000", "000000000",
    "000000000", "000000000", "000000000",
    "020020200", "002001020", "000000002",
    "002000021", "000000001", "000000000",
    "000002012", "000000001", "000000000",
)


EXPECTED_REPS = (
    "000000000000002002", "000000000000002102", "000000000000002202",
    "000000000000102002", "000000000000102102", "000000000000102202",
    "000000000000202002", "000000000000202102", "000000000000202202",
    "000000100000012022", "000000100000012122", "000000100000012222",
    "000000100000112022", "000000100000112122", "000000100000112222",
    "000000100000212022", "000000100000212122", "000000100000212222",
    "000000200000022012", "000000200000022112", "000000200000022212",
    "000000200000122012", "000000200000122112", "000000200000122212",
    "000000200000222012", "000000200000222112", "000000200000222212",
)


EXPECTED_AFFINE_EQUATIONS = (
    ((1, 1), 0), ((2, 1), 0), ((4, 1), 0), ((5, 1), 0),
    ((6, 1), (11, 2), (13, 2), 0),
    ((7, 1), 0), ((8, 1), 0),
    ((11, 1), (13, 2), (16, 2), 0),
    ((14, 1), 2), ((17, 1), 2),
)


def equation_vector(spec):
    rhs = spec[-1]
    row = [0] * 18
    for item in spec[:-1]:
        i, c = item
        row[i] = c
    return tuple(row), rhs


def enumerate_affine_rows(part, columns):
    out = {}
    for coeffs in itertools.product(range(P), repeat=len(columns)):
        row = part
        for c, col in zip(coeffs, columns):
            if c:
                row = row_add(row, col, c)
        assert row not in out
        out[row] = coeffs
    return out


KELS = tuple((v, z) for v in itertools.product(range(P), repeat=4)
             for z in itertools.product(range(P), repeat=3))


def pack_kernel(k):
    return tuple(k[0] + k[1])


def subgroup_generated(generators):
    gens = list(dict.fromkeys(generators))
    moves = gens + [kinv(g) for g in gens]
    seen = {KID}
    queue = [KID]
    head = 0
    while head < len(queue):
        h = queue[head]
        head += 1
        for g in moves:
            x = kmul(h, g)
            if x not in seen:
                seen.add(x)
                queue.append(x)
    return seen


def cube_image_and_closure(cp):
    cubes = set()
    witness = None
    inspected = 0
    ninth_checks = 0
    for qi in range(27):
        q2 = QMUL[qi][qi]
        assert QMUL[q2][qi] == QID
        fqq = cp.factor[qi][qi]
        fq2q = cp.factor[q2][qi]
        for k in KELS:
            cube = kmul(k, kact(ACTIONS[qi], k))
            cube = kmul(cube, fqq)
            cube = kmul(cube, kact(ACTIONS[q2], k))
            cube = kmul(cube, fq2q)
            assert kpow(cube, 3) == KID
            inspected += 1
            ninth_checks += 1
            cubes.add(cube)
            if witness is None and cube != KID:
                witness = pack_kernel(k) + Q[qi]
    generators = []
    closure = {KID}
    progression = [1]
    for cube in sorted(cubes, key=pack_kernel):
        if cube not in closure:
            generators.append(cube)
            closure = subgroup_generated(generators)
            progression.append(len(closure))
    return cubes, closure, progression, witness, inspected, ninth_checks


def main():
    assert sys.version_info >= (3, 10)
    for x in range(3):
        for y in range(3):
            a1, a2 = ((1, 0) if x == 1 else (0, 1) if x == 2 else (0, 0))
            b1, b2 = ((1, 0) if y == 1 else (0, 1) if y == 2 else (0, 0))
            c1, c2 = trit_add(a1, a2, b1, b2)
            got = 1 if c1 else 2 if c2 else 0
            assert got == (x + y) % 3

    # Kernel and quotient are independently checked before any extension claim.
    assert len(KELS) == 2187 and len(set(KELS)) == 2187
    assert all(kpow(k, 3) == KID for k in KELS)
    qx, qy, qz = Q[QX], Q[QY], Q[QZ]
    assert all(QMUL[QMUL[i][i]][i] == QID for i in range(27))
    qcomm = qmul_tuple(qmul_tuple(qinv_tuple(qx), qinv_tuple(qy)), qmul_tuple(qx, qy))
    assert qcomm == qz

    defects, pair_count, vtriple_count, vscalar_count = derive_action_defects()
    expected_labels = RELATOR_V

    # Direct action-word labels, independent of the crossed product factors.
    def acomm(g, h):
        return acomp(acomp(acomp(ainv(g), ainv(h)), g), h)

    action_words = (
        apow(AX, 3), apow(AY, 3), apow(AZ, 3),
        acomp(acomm(AX, AY), ainv(AZ)), acomm(AX, AZ), acomm(AY, AZ),
    )
    labels = tuple(inner_label(g) for g in action_words)
    assert labels == expected_labels
    assert omega(labels[0], labels[1]) == 2
    print("frozen lift reconstruction: PASS")
    print("six action-relator inner labels:", labels)
    print("V defect/associativity checks:", pair_count, vtriple_count, vscalar_count)

    reducer, upart, ubasis, equation_count = build_central_system(defects)
    assert equation_count == 59049
    assert reducer.rank == 1951 and len(ubasis) == 77
    print("central variables/equations/rank/dimension:",
          NVAR, equation_count, reducer.rank, len(ubasis))

    rpart = relator_row(defects, upart)
    relcols = []
    for b in ubasis:
        relcols.append(row_add(relator_row(defects, uadd(upart, b)), rpart, 2))
    relrank = dense_rank(relcols)
    assert relrank == 8
    selected = independent_indices(relcols)
    assert len(selected) == 8
    imagecols = [relcols[i] for i in selected]

    # Independently compare the derived affine image with all ten submitted rows.
    expected_eqs = [equation_vector(s) for s in EXPECTED_AFFINE_EQUATIONS]
    assert dense_rank([e[0] for e in expected_eqs]) == 10
    for coeff, rhs in expected_eqs:
        assert sum(coeff[i] * rpart[i] for i in range(18)) % 3 == rhs
        assert all(sum(coeff[i] * col[i] for i in range(18)) % 3 == 0
                   for col in imagecols)
    print("relator affine rank/dimension/feasible rows:", relrank, 8, 3 ** 8)
    print("complete affine relator equations:")
    for spec in EXPECTED_AFFINE_EQUATIONS:
        print(" ", spec)

    affine = enumerate_affine_rows(rpart, imagecols)
    assert len(affine) == 6561

    # Full normalized central one-cochains and their coboundaries.
    deltas = [delta_column(qi, c) for qi in range(1, 27) for c in range(3)]
    delta_rank = dense_rank(deltas)
    assert delta_rank == 74
    delta_relcols = [row_add(relator_row(defects, uadd(upart, d)), rpart, 2)
                     for d in deltas]
    gauge_rank = dense_rank(delta_relcols)
    assert gauge_rank == 5
    gen_indices = []
    for qi in (QX, QY, QZ):
        for c in range(3):
            gen_indices.append((qi - 1) * 3 + c)
    gencols = [delta_relcols[i] for i in gen_indices]
    grows = tuple("".join(str(gencols[j][i]) for j in range(9)) for i in range(18))
    assert grows == EXPECTED_G_ROWS
    assert dense_rank(gencols) == 5
    assert dense_rank(delta_relcols + gencols) == 5

    cochain_kernel_dim = len(ubasis) - relrank
    zero_relator_gauge_dim = delta_rank - gauge_rank
    assert cochain_kernel_dim == zero_relator_gauge_dim == 69
    assert len(ubasis) - delta_rank == relrank - gauge_rank == 3
    print("C1/coboundary/Z1 dimensions:", 78, delta_rank, 78 - delta_rank)
    print("gauge rank/image size:", gauge_rank, 3 ** gauge_rank)
    print("exact-row kernel equality:", cochain_kernel_dim, zero_relator_gauge_dim)
    print("quotient dimensions:", len(ubasis) - delta_rank, relrank - gauge_rank)
    print("gauge matrix rows:")
    for row in grows:
        print(" ", row)

    gauge_ind = independent_indices(gencols)
    assert len(gauge_ind) == 5
    gauge_basis = [gencols[i] for i in gauge_ind]
    gauge_set = set(enumerate_affine_rows((0,) * 18, gauge_basis))
    assert len(gauge_set) == 243
    seen = set()
    reps = []
    for row in sorted(affine):
        if row in seen:
            continue
        orbit = {row_add(row, g) for g in gauge_set}
        assert len(orbit) == 243 and orbit <= affine.keys()
        seen |= orbit
        reps.append(min(orbit))
    assert len(seen) == 6561 and len(reps) == 27
    rep_strings = tuple("".join(map(str, r)) for r in reps)
    assert rep_strings == EXPECTED_REPS
    print("derived orbit count/coverage:", len(reps), len(seen))

    class_results = []
    specific_outside = ((2, 1, 0, 2), (2, 0, 1))
    for ci, rep in enumerate(reps):
        coeffs = affine[rep]
        u = list(upart)
        for c, bi in zip(coeffs, selected):
            if c:
                u = uadd(u, ubasis[bi], c)
        assert relator_row(defects, u) == rep
        triple_checks = check_factor_equations(defects, u)
        assert triple_checks == 19683
        digest = hashlib.sha256(bytes(u)).hexdigest()
        cp = CrossedProduct(defects, u)
        # Direct normalization, inverse, and the six frozen relators.
        assert all(cp.factor[QID][i] == KID and cp.factor[i][QID] == KID
                   for i in range(27))
        for qi in range(27):
            probe = (KELS[(37 * qi) % len(KELS)], qi)
            assert cp.mul(probe, cp.inv(probe)) == (KID, QID)
            assert cp.mul(cp.inv(probe), probe) == (KID, QID)

        cubes, closure, progression, witness, inspected, ninth_checks = cube_image_and_closure(cp)
        assert inspected == ninth_checks == 59049
        assert witness is not None
        assert len(cubes) == 135
        assert len(closure) == 729
        assert cubes != closure
        assert specific_outside in closure and specific_outside not in cubes
        assert progression == [1, 3, 9, 27, 81, 243, 729]
        outside10 = pack_kernel(specific_outside) + (0, 0, 0)
        result = (ci, rep_strings[ci], digest, len(cubes), len(closure),
                  outside10, progression, witness)
        class_results.append(result)
        print("CLASS", ci, rep_strings[ci],
              "factor", digest,
              "factor_triples", triple_checks,
              "order/kernel/quotient", 59049, 2187, 27,
              "exp9", True,
              "literal_cube_size", len(cubes),
              "literal_closed", False,
              "generated_closure_size", len(closure))
        print(" CLOSURE_OUTSIDE", outside10, "progression", progression)
        print(" ORDER9_WITNESS", witness)

    assert len(class_results) == 27
    print("ALL 27 CLASSES: PASS")
    print("literal image sizes:", sorted({r[3] for r in class_results}))
    print("generated comparator sizes:", sorted({r[4] for r in class_results}))
    print("TARGET-EQUAL CLASS INDICES: []")
    print("BOUNDARY: exactly one frozen p=3 action/lift family; active_assignment_answered:no")


if __name__ == "__main__":
    main()

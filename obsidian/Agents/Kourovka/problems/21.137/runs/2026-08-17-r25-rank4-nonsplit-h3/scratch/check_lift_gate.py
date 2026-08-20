#!/usr/bin/env python3
"""Exact F3 checker for the frozen 21.137 nonsplit-H3 lift gate.

This implements only the manifest in lift_manifest.md.  It does not enumerate
factor systems or groups.
"""

from collections import Counter, defaultdict
from itertools import product
import sys

P = 3


def mat_zero(r, c):
    return tuple(tuple(0 for _ in range(c)) for _ in range(r))


def mat_id(n):
    return tuple(tuple(1 if i == j else 0 for j in range(n)) for i in range(n))


def mat_add(a, b):
    return tuple(
        tuple((a[i][j] + b[i][j]) % P for j in range(len(a[0])))
        for i in range(len(a))
    )


def mat_neg(a):
    return tuple(tuple((-x) % P for x in row) for row in a)


def mat_mul(a, b):
    assert len(a[0]) == len(b)
    return tuple(
        tuple(
            sum(a[i][k] * b[k][j] for k in range(len(b))) % P
            for j in range(len(b[0]))
        )
        for i in range(len(a))
    )


def mat_pow(a, n):
    out = mat_id(len(a))
    base = a
    while n:
        if n & 1:
            out = mat_mul(out, base)
        base = mat_mul(base, base)
        n >>= 1
    return out


def mat_inv(a):
    n = len(a)
    aug = [list(a[i]) + list(mat_id(n)[i]) for i in range(n)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if aug[i][col] % P)
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = pow(aug[col][col] % P, -1, P)
        aug[col] = [(scale * x) % P for x in aug[col]]
        for i in range(n):
            if i != col and aug[i][col] % P:
                scale = aug[i][col] % P
                aug[i] = [
                    (aug[i][j] - scale * aug[col][j]) % P
                    for j in range(2 * n)
                ]
    return tuple(tuple(row[n:]) for row in aug)


def comm(a, b):
    return mat_mul(mat_mul(mat_mul(mat_inv(a), mat_inv(b)), a), b)


I3 = mat_id(3)
I4 = mat_id(4)
Z34 = mat_zero(3, 4)

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

# Rows q^T J for qX=f2 and qY=e2 in basis (e1,e2,f1,f2).
JQX = (0, 2, 0, 0)
JQY = (0, 0, 0, 1)


def triple_mul(g, h):
    """Product g*h means composition g after h."""
    mg, tg, lg = g
    mh, th, lh = h
    return (
        mat_mul(mg, mh),
        mat_mul(tg, th),
        mat_add(mat_mul(tg, lh), mat_mul(lg, mh)),
    )


def triple_inv(g):
    m, t, l = g
    mi = mat_inv(m)
    ti = mat_inv(t)
    return mi, ti, mat_neg(mat_mul(mat_mul(ti, l), mi))


def triple_word(gens, letters):
    out = (I4, I3, Z34)
    for name, exponent in letters:
        g = gens[name]
        if exponent == -1:
            g = triple_inv(g)
        elif exponent != 1:
            raise ValueError(exponent)
        out = triple_mul(out, g)
    return out


RELATIONS = (
    ("x3", (("x", 1), ("x", 1), ("x", 1)), "exact_x"),
    ("y3", (("y", 1), ("y", 1), ("y", 1)), "exact_y"),
    ("z3", (("z", 1), ("z", 1), ("z", 1)), "inner"),
    (
        "comm_xy_zinv",
        (("x", -1), ("y", -1), ("x", 1), ("y", 1), ("z", -1)),
        "inner",
    ),
    ("comm_xz", (("x", -1), ("z", -1), ("x", 1), ("z", 1)), "inner"),
    ("comm_yz", (("y", -1), ("z", -1), ("y", 1), ("z", 1)), "inner"),
)


def unpack_l(values):
    mats = []
    for off in (0, 12, 24):
        mats.append(
            tuple(tuple(values[off + 4 * i + j] for j in range(4)) for i in range(3))
        )
    return mats


def equation_outputs(tx, ty, tz, values):
    lx, ly, lz = unpack_l(values)
    gens = {"x": (A, tx, lx), "y": (B, ty, ly), "z": (C, tz, lz)}
    outputs = []
    labels = []
    for rel_name, letters, kind in RELATIONS:
        m, t, l = triple_word(gens, letters)
        assert m == I4, (rel_name, "outer-M", m)
        assert t == I3, (rel_name, "center-T", t)
        if kind == "exact_x":
            for i in range(3):
                for j in range(4):
                    outputs.append(l[i][j])
                    labels.append((rel_name, i, j, JQX[j] if i == 0 else 0))
        elif kind == "exact_y":
            for i in range(3):
                for j in range(4):
                    outputs.append(l[i][j])
                    labels.append((rel_name, i, j, JQY[j] if i == 0 else 0))
        else:
            for i in (1, 2):
                for j in range(4):
                    outputs.append(l[i][j])
                    labels.append((rel_name, i, j, 0))
    return outputs, labels


def build_system(tx, ty, tz):
    zero = [0] * 36
    zero_out, labels = equation_outputs(tx, ty, tz, zero)
    assert not any(zero_out)
    columns = []
    for k in range(36):
        values = [0] * 36
        values[k] = 1
        out, labels2 = equation_outputs(tx, ty, tz, values)
        assert labels2 == labels
        columns.append(out)
    coeff = [list(row) for row in zip(*columns)]
    rhs = [label[3] for label in labels]
    return coeff, rhs, labels


def rref_certificate(coeff, rhs):
    """Return ranks, a solution if consistent, and a left-null certificate if not."""
    m = len(coeff)
    n = len(coeff[0])
    aug = [coeff[i][:] + [rhs[i] % P] for i in range(m)]
    track = [list(mat_id(m)[i]) for i in range(m)]
    pivot_cols = []
    row = 0
    for col in range(n):
        pivot = next((i for i in range(row, m) if aug[i][col] % P), None)
        if pivot is None:
            continue
        aug[row], aug[pivot] = aug[pivot], aug[row]
        track[row], track[pivot] = track[pivot], track[row]
        scale = pow(aug[row][col] % P, -1, P)
        aug[row] = [(scale * x) % P for x in aug[row]]
        track[row] = [(scale * x) % P for x in track[row]]
        for i in range(m):
            if i != row and aug[i][col] % P:
                scale = aug[i][col] % P
                aug[i] = [
                    (aug[i][j] - scale * aug[row][j]) % P for j in range(n + 1)
                ]
                track[i] = [
                    (track[i][j] - scale * track[row][j]) % P for j in range(m)
                ]
        pivot_cols.append(col)
        row += 1
        if row == m:
            break
    rank = len(pivot_cols)
    bad = next((i for i in range(m) if not any(aug[i][:n]) and aug[i][n]), None)
    if bad is not None:
        scale = pow(aug[bad][n] % P, -1, P)
        cert = [(scale * x) % P for x in track[bad]]
        # Independently check lambda*A=0 and lambda*b=1.
        assert all(sum(cert[i] * coeff[i][j] for i in range(m)) % P == 0 for j in range(n))
        assert sum(cert[i] * rhs[i] for i in range(m)) % P == 1
        return rank, rank + 1, None, cert
    sol = [0] * n
    for i, col in enumerate(pivot_cols):
        sol[col] = aug[i][n]
    assert all(sum(coeff[i][j] * sol[j] for j in range(n)) % P == rhs[i] for i in range(m))
    return rank, rank, sol, None


def matrix_code(a):
    return "".join(str(x) for row in a for x in row)


def center_actions():
    out = []
    positions = ((0, 1), (0, 2), (1, 1), (1, 2), (2, 1), (2, 2))
    for vals in product(range(P), repeat=len(positions)):
        r = [[0] * 3 for _ in range(3)]
        for (i, j), x in zip(positions, vals):
            r[i][j] = x
        r = tuple(tuple(row) for row in r)
        if mat_pow(r, 3) == mat_zero(3, 3):
            t = mat_add(I3, r)
            assert mat_pow(t, 3) == I3
            out.append(t)
    return out


def sparse_certificate(cert, labels):
    return [(*labels[i][:3], value) for i, value in enumerate(cert) if value]


def q_from_j_row(ell):
    """Invert q |-> q^T J in the fixed symplectic basis."""
    return (ell[2], ell[3], 2 * ell[0] % P, 2 * ell[1] % P)


def frozen_feasible_row():
    """Check the single explicit feasible center-action row in under one second."""
    tx = ((1, 2, 0), (0, 1, 1), (0, 0, 1))
    ty = ((1, 1, 0), (0, 1, 1), (0, 0, 1))
    tz = comm(tx, ty)
    assert mat_pow(tx, 3) == mat_pow(ty, 3) == mat_pow(tz, 3) == I3
    assert comm(tx, tz) == comm(ty, tz) == I3
    coeff, rhs, labels = build_system(tx, ty, tz)
    rank, augrank, sol, cert = rref_certificate(coeff, rhs)
    assert cert is None and sol is not None
    lx, ly, lz = unpack_l(sol)
    print("frozen feasible center row")
    print("TX", matrix_code(tx))
    print("TY", matrix_code(ty))
    print("TZ", matrix_code(tz))
    print("system equations/variables/rank/augmented-rank:", len(coeff), 36, rank, augrank)
    print("solution-space dimension:", 36 - rank)
    print("LX", matrix_code(lx))
    print("LY", matrix_code(ly))
    print("LZ", matrix_code(lz))
    gens = {"x": (A, tx, lx), "y": (B, ty, ly), "z": (C, tz, lz)}
    for rel_name, letters, _kind in RELATIONS:
        m, t, l = triple_word(gens, letters)
        assert m == I4 and t == I3
        assert l[1] == l[2] == (0, 0, 0, 0)
        print(rel_name, "J-row", "".join(str(x) for x in l[0]), "q", q_from_j_row(l[0]))
    residuals = {
        (sum(coeff[i][j] * sol[j] for j in range(36)) - rhs[i]) % P
        for i in range(len(coeff))
    }
    print("all 56 residuals:", sorted(residuals))


def main():
    assert comm(A, B) == C
    assert mat_pow(A, 3) == mat_pow(B, 3) == mat_pow(C, 3) == I4
    assert comm(A, C) == comm(B, C) == I4
    # Fixed-label and nonorthogonality checks from direct coordinates.
    qx = ((0,), (0,), (0,), (1,))
    qy = ((0,), (1,), (0,), (0,))
    assert mat_mul(A, qx) == qx and mat_mul(B, qy) == qy
    omega = (
        (0, 0, 1, 0),
        (0, 0, 0, 1),
        (2, 0, 0, 0),
        (0, 2, 0, 0),
    )
    omega_qx_qy = mat_mul(mat_mul(tuple(zip(*qx)), omega), qy)[0][0]
    assert omega_qx_qy == 2

    actions = center_actions()
    retained = []
    for tx in actions:
        for ty in actions:
            tz = comm(tx, ty)
            if mat_pow(tz, 3) != I3:
                continue
            if comm(tx, tz) != I3 or comm(ty, tz) != I3:
                continue
            retained.append((tx, ty, tz))

    distributions = Counter()
    feasible = []
    examples = {}
    certificate_supports = Counter()
    for index, (tx, ty, tz) in enumerate(retained):
        coeff, rhs, labels = build_system(tx, ty, tz)
        rank, augrank, sol, cert = rref_certificate(coeff, rhs)
        distributions[(rank, augrank)] += 1
        key = (rank, augrank)
        if key not in examples:
            examples[key] = (index, tx, ty, tz, cert, labels)
        if sol is not None:
            feasible.append((index, tx, ty, tz, sol, rank))
        else:
            certificate_supports[len(sparse_certificate(cert, labels))] += 1

    print("field: F3")
    print("outer checks: [A,B]=C; A^3=B^3=C^3=I; [A,C]=[B,C]=I")
    print("qX=f2 fixed by A: True")
    print("qY=e2 fixed by B: True")
    print("omega(qX,qY):", omega_qx_qy)
    print("center actions T fixing c with T^3=I:", len(actions))
    print("ordered (TX,TY) pairs tested:", len(actions) ** 2)
    print("retained H3 center-action triples:", len(retained))
    print("linear variables per retained triple: 36")
    print("linear equations per retained triple: 56")
    print("rank/augmented-rank distribution:", dict(sorted(distributions.items())))
    print("left-certificate support-size distribution:", dict(sorted(certificate_supports.items())))
    print("feasible retained triples:", len(feasible))
    for key in sorted(examples):
        index, tx, ty, tz, cert, labels = examples[key]
        print("representative class", key, "retained_index", index)
        print("  TX", matrix_code(tx))
        print("  TY", matrix_code(ty))
        print("  TZ", matrix_code(tz))
        if cert is not None:
            print("  lambda sparse (relation,row,col,coefficient):", sparse_certificate(cert, labels))
    if feasible:
        index, tx, ty, tz, sol, rank = feasible[0]
        print("first feasible retained_index:", index, "rank", rank)
        print("  TX", matrix_code(tx))
        print("  TY", matrix_code(ty))
        print("  TZ", matrix_code(tz))
        lx, ly, lz = unpack_l(sol)
        print("  LX", matrix_code(lx))
        print("  LY", matrix_code(ly))
        print("  LZ", matrix_code(lz))


if __name__ == "__main__":
    if "--frozen-only" in sys.argv:
        frozen_feasible_row()
    else:
        main()

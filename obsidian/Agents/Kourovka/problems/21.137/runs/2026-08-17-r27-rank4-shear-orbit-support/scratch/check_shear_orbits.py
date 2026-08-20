#!/usr/bin/env python3
"""Exact F3 checker for RANK4-H3-SHEAR-ORBIT-SUPPORT.

The program uses only elementary finite-field linear algebra.  It constructs
the 56-by-36 system from the frozen matrices and the displayed triple law; it
does not import any result or code from run r26 and does not construct a
factor system or a group extension.
"""

from __future__ import annotations

import argparse
import itertools
import json
from typing import Iterable, Sequence


P = 3


def vadd(x, y):
    return [(a + b) % P for a, b in zip(x, y)]


def vsub(x, y):
    return [(a - b) % P for a, b in zip(x, y)]


def vscale(a, x):
    return [(a * b) % P for b in x]


def dot(x, y):
    return sum(a * b for a, b in zip(x, y)) % P


def zero(rows, cols):
    return [[0] * cols for _ in range(rows)]


def eye(n):
    out = zero(n, n)
    for i in range(n):
        out[i][i] = 1
    return out


def transpose(a):
    if not a:
        return []
    return [list(row) for row in zip(*a)]


def madd(a, b):
    return [[(x + y) % P for x, y in zip(rx, ry)] for rx, ry in zip(a, b)]


def msub(a, b):
    return [[(x - y) % P for x, y in zip(rx, ry)] for rx, ry in zip(a, b)]


def mscale(c, a):
    return [[(c * x) % P for x in row] for row in a]


def mmul(a, b):
    bt = transpose(b)
    return [[dot(row, col) for col in bt] for row in a]


def mvec(a, x):
    return [dot(row, x) for row in a]


def mpow(a, n):
    out = eye(len(a))
    base = a
    while n:
        if n & 1:
            out = mmul(out, base)
        base = mmul(base, base)
        n >>= 1
    return out


def inv(a):
    n = len(a)
    aug = [row[:] + eye(n)[i] for i, row in enumerate(a)]
    rr, piv = rref(aug, pivot_limit=n)
    if piv != list(range(n)):
        raise ValueError("singular matrix")
    return [row[n:] for row in rr]


def rref(a, pivot_limit=None):
    if not a:
        return [], []
    out = [[x % P for x in row] for row in a]
    rows, cols = len(out), len(out[0])
    limit = cols if pivot_limit is None else pivot_limit
    pivots = []
    r = 0
    for c in range(limit):
        k = next((i for i in range(r, rows) if out[i][c]), None)
        if k is None:
            continue
        out[r], out[k] = out[k], out[r]
        z = pow(out[r][c], -1, P)
        out[r] = [(z * x) % P for x in out[r]]
        for i in range(rows):
            if i != r and out[i][c]:
                z = out[i][c]
                out[i] = [(x - z * y) % P for x, y in zip(out[i], out[r])]
        pivots.append(c)
        r += 1
        if r == rows:
            break
    return out, pivots


def rank(a):
    if not a:
        return 0
    return len(rref(a)[1])


def solve(a, b):
    """Return (particular, nullspace basis), or (None, []) if inconsistent."""
    if not a:
        return [], []
    rows, cols = len(a), len(a[0])
    aug = [a[i][:] + [b[i] % P] for i in range(rows)]
    rr, piv = rref(aug, pivot_limit=cols)
    for row in rr:
        if all(x == 0 for x in row[:cols]) and row[cols] != 0:
            return None, []
    free = [j for j in range(cols) if j not in piv]
    particular = [0] * cols
    for i, c in enumerate(piv):
        particular[c] = rr[i][cols]
    basis = []
    for f in free:
        x = [0] * cols
        x[f] = 1
        for i, c in enumerate(piv):
            x[c] = (-rr[i][f]) % P
        basis.append(x)
    return particular, basis


def nullspace(a):
    if not a:
        raise ValueError("nullspace requires a matrix with known column count")
    z, basis = solve(a, [0] * len(a))
    if z is None:
        raise AssertionError("homogeneous system inconsistent")
    return basis


def independent_basis(vectors):
    out = []
    old_rank = 0
    for v in vectors:
        new_rank = rank(out + [v])
        if new_rank > old_rank:
            out.append(v)
            old_rank = new_rank
    return out


def columns(vectors):
    if not vectors:
        return []
    return transpose(vectors)


def coordinates(basis, v):
    if not basis:
        if any(v):
            raise ValueError("nonzero vector outside zero space")
        return []
    ans, _ = solve(columns(basis), v)
    if ans is None:
        raise ValueError("vector outside supplied basis")
    return ans


def lincomb(coeffs, basis):
    if not basis:
        return []
    out = [0] * len(basis[0])
    for a, v in zip(coeffs, basis):
        out = vadd(out, vscale(a, v))
    return out


def all_span(basis):
    if not basis:
        return [(0, 0, 0, 0)]
    return [tuple(lincomb(c, basis)) for c in itertools.product(range(P), repeat=len(basis))]


def flatten(a):
    return [x for row in a for x in row]


def unflatten(v, rows, cols):
    return [list(v[i * cols:(i + 1) * cols]) for i in range(rows)]


def matrix_string(a):
    return "/".join("".join(str(x) for x in row) for row in a)


# Frozen coordinates: V=(e1,e2,f1,f2), Z=(c,s,t).
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
QX = [0, 0, 0, 1]
QY = [0, 1, 0, 0]
OMEGA = [
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [2, 0, 0, 0],
    [0, 2, 0, 0],
]


def omega(v, w):
    return dot(v, mvec(OMEGA, w))


def jrow(q):
    return [(-q[2]) % P, (-q[3]) % P, q[0] % P, q[1] % P]


def jmat(q):
    return [jrow(q), [0] * 4, [0] * 4]


def q_from_jrow(row):
    return [row[2] % P, row[3] % P, (-row[0]) % P, (-row[1]) % P]


# A triple is (M,T,L), with the composition law in the frozen manifest.
def triple_comp(u, v):
    m, t, l = u
    n, s, r = v
    return mmul(m, n), mmul(t, s), madd(mmul(t, r), mmul(l, n))


def triple_identity():
    return eye(4), eye(3), zero(3, 4)


def triple_inv(u):
    m, t, l = u
    mi, ti = inv(m), inv(t)
    return mi, ti, mscale(2, mmul(mmul(ti, l), mi))


def triple_pow(u, n):
    out = triple_identity()
    for _ in range(n):
        out = triple_comp(out, u)
    return out


def triple_word(*letters):
    out = triple_identity()
    for g in letters:
        out = triple_comp(out, g)
    return out


def triple_comm(u, v):
    return triple_word(triple_inv(u), triple_inv(v), u, v)


def split_lifts(x):
    return [unflatten(x[12 * i:12 * (i + 1)], 3, 4) for i in range(3)]


def make_generators(x):
    lx, ly, lz = split_lifts(x)
    return (A, TX, lx), (B, TY, ly), (C, TZ, lz)


def shear_constraints(x):
    """The exact 56 residual coordinates in the order of the manifest."""
    xg, yg, zg = make_generators(x)
    x3 = triple_pow(xg, 3)[2]
    y3 = triple_pow(yg, 3)[2]
    z3 = triple_pow(zg, 3)[2]
    cxyz = triple_comp(triple_comm(xg, yg), triple_inv(zg))[2]
    cxz = triple_comm(xg, zg)[2]
    cyz = triple_comm(yg, zg)[2]
    out = flatten(msub(x3, jmat(QX)))
    out += flatten(msub(y3, jmat(QY)))
    for rel in (z3, cxyz, cxz, cyz):
        out += flatten(rel[1:])
    assert len(out) == 56
    return out


def reconstruct_system():
    z = [0] * 36
    f0 = shear_constraints(z)
    cols = []
    for j in range(36):
        e = [0] * 36
        e[j] = 1
        cols.append(vsub(shear_constraints(e), f0))
    coeff = transpose(cols)
    rhs = vscale(2, f0)
    return coeff, rhs


def check_frozen_matrices():
    i4, i3 = eye(4), eye(3)
    assert mpow(A, 3) == i4 and mpow(B, 3) == i4 and mpow(C, 3) == i4
    assert triple_comm((A, i3, zero(3, 4)), (B, i3, zero(3, 4)))[0] == C
    assert triple_comm((A, i3, zero(3, 4)), (C, i3, zero(3, 4)))[0] == i4
    assert triple_comm((B, i3, zero(3, 4)), (C, i3, zero(3, 4)))[0] == i4
    assert mpow(TX, 3) == i3 and mpow(TY, 3) == i3 and mpow(TZ, 3) == i3
    assert triple_comm((i4, TX, zero(3, 4)), (i4, TY, zero(3, 4)))[1] == TZ
    assert triple_comm((i4, TX, zero(3, 4)), (i4, TZ, zero(3, 4)))[1] == i3
    assert triple_comm((i4, TY, zero(3, 4)), (i4, TZ, zero(3, 4)))[1] == i3
    assert mmul(transpose(A), mmul(OMEGA, A)) == OMEGA
    assert mmul(transpose(B), mmul(OMEGA, B)) == OMEGA
    assert mmul(transpose(C), mmul(OMEGA, C)) == OMEGA
    assert mvec(msub(A, i4), QX) == [0] * 4
    assert mvec(msub(B, i4), QY) == [0] * 4
    assert omega(QX, QY) == 2


def section_triple(x, h):
    xg, yg, zg = make_generators(x)
    return triple_word(triple_pow(xg, h[0]), triple_pow(yg, h[1]), triple_pow(zg, h[2]))


def norm_matrix(m):
    return madd(madd(eye(4), m), mpow(m, 2))


def section_label_and_norm(x, h):
    g = section_triple(x, h)
    cube = triple_pow(g, 3)
    if cube[0] != eye(4) or cube[1] != eye(3):
        raise AssertionError("section cube is not identity on V and Z")
    if cube[2][1:] != zero(2, 4):
        raise AssertionError("section cube is not inner")
    q = q_from_jrow(cube[2][0])
    return q, norm_matrix(g[0])


H_ELEMENTS = list(itertools.product(range(P), repeat=3))


def annihilator_rows(w):
    # Functionals r with r*w=0 are ker(w^T).
    return nullspace(transpose(w))


def signature(x):
    out = []
    for h in H_ELEMENTS:
        q, w = section_label_and_norm(x, h)
        out.extend(dot(r, q) for r in annihilator_rows(w))
    return out


def support_table(x):
    sigma = set()
    rows = []
    for h in H_ELEMENTS:
        q, w = section_label_and_norm(x, h)
        wb = independent_basis(transpose(w))
        fibre = sorted({tuple(vadd(q, u)) for u in all_span(wb)})
        sigma.update(fibre)
        rows.append({
            "h": list(h),
            "lambda": q,
            "W_basis": wb,
            "F": [list(v) for v in fibre],
        })
    sb = independent_basis([list(v) for v in sorted(sigma)])
    span_size = P ** len(sb)
    is_subspace = (tuple([0] * 4) in sigma and len(sigma) == span_size)
    gram = [[omega(u, v) for v in sb] for u in sb]
    return {
        "rows": rows,
        "sigma": [list(v) for v in sorted(sigma)],
        "sigma_size": len(sigma),
        "span_dimension": len(sb),
        "is_subspace": is_subspace,
        "symplectic_rank_on_span": rank(gram),
        "support_gate_pass": bool(is_subspace and rank(gram) > 0),
    }


def apply_linear(a, x):
    return mvec(a, x)


def build_gauge_vectors(coeff):
    gauge = []
    # Independent generator-lift changes by inner automorphisms: arbitrary c row.
    # The A and B norms vanish, so all four changes preserve qX and qY.
    assert norm_matrix(A) == zero(4, 4)
    assert norm_matrix(B) == zero(4, 4)
    for gen in range(3):
        for j in range(4):
            v = [0] * 36
            v[12 * gen + j] = 1
            gauge.append(v)
    # Simultaneous kernel conjugation by beta=(I,I,R):
    # L_i -> L_i + T_i R - R M_i.
    for rr in range(3):
        for cc in range(4):
            r = zero(3, 4)
            r[rr][cc] = 1
            blocks = [msub(mmul(t, r), mmul(r, m)) for m, t in ((A, TX), (B, TY), (C, TZ))]
            gauge.append(sum((flatten(block) for block in blocks), []))
    for v in gauge:
        if any(apply_linear(coeff, v)):
            raise AssertionError("claimed gauge vector leaves the homogeneous shear system")
    return gauge


def d_matrix(a):
    # Complete V-stabilizer derived in the manifest: f1 -> f1+a*e1.
    d = eye(4)
    d[0][2] = a % P
    return d


def u_matrix(d):
    # Complete Z-stabilizer derived in the manifest: t -> t+d*c.
    u = eye(3)
    u[0][2] = d % P
    return u


def check_stabilizer_matrices():
    for a in range(P):
        d = d_matrix(a)
        assert mmul(transpose(d), mmul(OMEGA, d)) == OMEGA
        assert mmul(d, A) == mmul(A, d)
        assert mmul(d, B) == mmul(B, d)
        assert mmul(d, C) == mmul(C, d)
        assert mvec(d, QX) == QX and mvec(d, QY) == QY
    for d in range(P):
        u = u_matrix(d)
        assert mmul(u, TX) == mmul(TX, u)
        assert mmul(u, TY) == mmul(TY, u)
        assert mmul(u, TZ) == mmul(TZ, u)
        assert mvec(u, [1, 0, 0]) == [1, 0, 0]


def stabilizer_transform(x, a, d):
    # beta=(D_a,U_d,0), beta^-1 alpha_i beta:
    # L_i -> U_d^-1 L_i D_a.
    din = d_matrix(a)
    uin = inv(u_matrix(d))
    return sum((flatten(mmul(mmul(uin, l), din)) for l in split_lifts(x)), [])


def affine_solution_coordinates(particular, basis, x):
    return coordinates(basis, vsub(x, particular))


def quotient_data(particular, basis, gauge):
    gauge_coords = [coordinates(basis, g) for g in gauge]
    gb = independent_basis(gauge_coords)
    # Q has kernel exactly the translation-gauge space.
    qrows = nullspace(gb) if gb else eye(len(basis))
    assert rank(qrows) == len(basis) - len(gb)
    return gauge_coords, gb, qrows


def quotient_affine_maps(particular, basis, qrows, gauge_coords):
    qdim = len(qrows)
    if qdim:
        qmat = qrows
        lifts = []
        for j in range(qdim):
            e = [0] * qdim
            e[j] = 1
            x, _ = solve(qmat, e)
            if x is None:
                raise AssertionError("quotient coordinate map not onto")
            lifts.append(x)
    else:
        lifts = []

    maps = {}
    for a, d in itertools.product(range(P), repeat=2):
        image0 = stabilizer_transform(particular, a, d)
        c = affine_solution_coordinates(particular, basis, image0)
        cols_s = []
        for v in basis:
            image = stabilizer_transform(vadd(particular, v), a, d)
            cols_s.append(vsub(affine_solution_coordinates(particular, basis, image), c))
        s = columns(cols_s)
        for g in gauge_coords:
            if any(mvec(qrows, mvec(s, g))):
                raise AssertionError("stabilizer does not preserve translation gauge")
        b = mvec(qrows, c)
        acols = [mvec(qrows, mvec(s, lift)) for lift in lifts]
        aq = columns(acols) if qdim else []
        maps[(a, d)] = (aq, b)

    def compose_affine(f, g):
        af, bf = f
        ag, bg = g
        if not af:
            return [], []
        return mmul(af, ag), vadd(mvec(af, bg), bf)

    for a, d, aa, dd in itertools.product(range(P), repeat=4):
        lhs = compose_affine(maps[(a, d)], maps[(aa, dd)])
        rhs = maps[((a + aa) % P, (d + dd) % P)]
        if lhs != rhs:
            raise AssertionError("the nine stabilizer maps do not form C3 x C3")
    return maps, lifts


def affine_apply(f, x):
    a, b = f
    return vadd(mvec(a, x), b) if a else []


def fixed_point_count(f, qdim):
    if qdim == 0:
        return 1
    a, b = f
    mat = msub(a, eye(qdim))
    sol, ns = solve(mat, vscale(2, b))
    return 0 if sol is None else P ** len(ns)


def orbit_representatives(maps, qdim, orbit_count):
    if orbit_count > 729:
        return None
    points = list(itertools.product(range(P), repeat=qdim))
    unseen = set(points)
    reps = []
    while unseen:
        seed = min(unseen)
        orb = {tuple(affine_apply(f, list(seed))) for f in maps.values()}
        unseen.difference_update(orb)
        reps.append(min(orb))
    if len(reps) != orbit_count:
        raise AssertionError("Burnside and explicit orbit counts disagree")
    return reps


def lift_quotient_point(qrows, z):
    if not qrows:
        return []
    x, _ = solve(qrows, list(z))
    if x is None:
        raise AssertionError("quotient point has no lift")
    return x


def transformed_sigma_expected(sigma, a):
    di = inv(d_matrix(a))
    return sorted({tuple(mvec(di, v)) for v in sigma})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--full", action="store_true", help="include every permitted representative support table")
    args = parser.parse_args()

    check_frozen_matrices()
    check_stabilizer_matrices()
    coeff, rhs = reconstruct_system()
    particular, basis = solve(coeff, rhs)
    if particular is None:
        raise AssertionError("56-row shear system is inconsistent")
    r = rank(coeff)
    r_aug = rank([row + [rhs[i]] for i, row in enumerate(coeff)])
    if (len(coeff), len(coeff[0]), r, r_aug, len(basis)) != (56, 36, 17, 17, 19):
        raise AssertionError("matrix reconstruction hard gate differs from 56/36/17/17/19")
    if any(shear_constraints(particular)):
        raise AssertionError("particular solution has a nonzero residual")

    # The inner-cube gate must hold affinely, not only for one row.
    for x in [particular] + [vadd(particular, v) for v in basis]:
        for h in H_ELEMENTS:
            section_label_and_norm(x, h)

    sig0 = signature(particular)
    sig_cols = [vsub(signature(vadd(particular, v)), sig0) for v in basis]
    signature_rank = rank(sig_cols)
    signature_kernel_dimension = len(basis) - signature_rank

    gauge = build_gauge_vectors(coeff)
    gauge_rank = rank(gauge)
    for g in gauge:
        if signature(vadd(particular, g)) != sig0:
            raise AssertionError("Phi is not invariant under a claimed translation gauge")
    gauge_coords, gauge_basis, qrows = quotient_data(particular, basis, gauge)
    qdim = len(qrows)
    maps, _ = quotient_affine_maps(particular, basis, qrows, gauge_coords)

    burnside_terms = {f"{a},{d}": fixed_point_count(maps[(a, d)], qdim)
                      for a, d in itertools.product(range(P), repeat=2)}
    burnside_sum = sum(burnside_terms.values())
    if burnside_sum % 9:
        raise AssertionError("nonintegral Burnside orbit count")
    orbit_count = burnside_sum // 9

    # Stabilizer support equivariance on the affine base row.
    base_support = support_table(particular)
    base_sigma = base_support["sigma"]
    for a, d in itertools.product(range(P), repeat=2):
        got = support_table(stabilizer_transform(particular, a, d))["sigma"]
        want = [list(v) for v in transformed_sigma_expected(base_sigma, a)]
        if got != want:
            raise AssertionError("Phi/support is not equivariant under the stabilizer")

    hard_kill = None
    if signature_rank > 8:
        hard_kill = f"signature image dimension {signature_rank} exceeds 8"
    elif orbit_count > 729:
        hard_kill = f"exact genuine-orbit count {orbit_count} exceeds 729"

    reps = orbit_representatives(maps, qdim, orbit_count) if hard_kill is None else None
    rep_records = []
    if args.full and reps is not None:
        for z in reps:
            xcoords = lift_quotient_point(qrows, z)
            x = vadd(particular, lincomb(xcoords, basis)) if basis else particular
            rep_records.append({"quotient_coordinate": list(z), "support": support_table(x)})

    result = {
        "strategy": "RANK4-H3-SHEAR-ORBIT-SUPPORT",
        "field": 3,
        "system": {
            "equations": len(coeff),
            "variables": len(coeff[0]),
            "coefficient_rank": r,
            "augmented_rank": r_aug,
            "affine_dimension": len(basis),
        },
        "particular_solution": {
            "LX": matrix_string(split_lifts(particular)[0]),
            "LY": matrix_string(split_lifts(particular)[1]),
            "LZ": matrix_string(split_lifts(particular)[2]),
        },
        "gauge": {
            "listed_generators": len(gauge),
            "translation_rank": gauge_rank,
            "affine_quotient_dimension": qdim,
            "complete_discrete_stabilizer_size": 9,
        },
        "signature": {
            "coordinate_count": len(sig0),
            "image_dimension": signature_rank,
            "kernel_dimension": signature_kernel_dimension,
        },
        "orbits": {
            "burnside_fixed_points": burnside_terms,
            "genuine_orbit_count": orbit_count,
            "orbit_size_sum": P ** len(basis),
            "representatives_recorded": len(rep_records),
        },
        "hard_kill": hard_kill,
        "base_support_summary": {k: v for k, v in base_support.items() if k != "rows" and k != "sigma"},
        "representatives": rep_records,
        "limits": {
            "factor_system_opened": False,
            "group_enumeration_run": False,
            "central_relators_varied": False,
            "universal_scope_answered": False,
        },
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()

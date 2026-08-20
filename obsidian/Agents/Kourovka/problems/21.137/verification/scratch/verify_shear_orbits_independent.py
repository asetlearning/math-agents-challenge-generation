#!/usr/bin/env python3
"""Independent exact-F3 certificate checker for the frozen 21.137 shear family.

Written from the displayed triple law and matrices, without importing the claimant
checker or its output.  No external package or group enumerator is used.
"""

import argparse
import itertools
import json

P = 3


def mod(x):
    return x % P


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def zero(r, c):
    return [[0] * c for _ in range(r)]


def add(A, B):
    return [[mod(A[i][j] + B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]


def sub(A, B):
    return [[mod(A[i][j] - B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) % P
             for j in range(len(B[0]))] for i in range(len(A))]


def transpose(A):
    return [list(row) for row in zip(*A)]


def mv(A, v):
    return [sum(A[i][j] * v[j] for j in range(len(v))) % P for i in range(len(A))]


def flat(A):
    return [x for row in A for x in row]


def unflat(v, r, c):
    return [list(v[i*c:(i+1)*c]) for i in range(r)]


def mpow(A, n):
    out = eye(len(A))
    for _ in range(n):
        out = mul(out, A)
    return out


def rref(rows):
    R = [[x % P for x in row] for row in rows]
    if not R:
        return R, []
    nr, nc = len(R), len(R[0])
    pivots = []
    rr = 0
    for cc in range(nc):
        pivot = next((i for i in range(rr, nr) if R[i][cc]), None)
        if pivot is None:
            continue
        R[rr], R[pivot] = R[pivot], R[rr]
        z = pow(R[rr][cc], -1, P)
        R[rr] = [(z * x) % P for x in R[rr]]
        for i in range(nr):
            if i != rr and R[i][cc]:
                z = R[i][cc]
                R[i] = [(R[i][j] - z * R[rr][j]) % P for j in range(nc)]
        pivots.append(cc)
        rr += 1
        if rr == nr:
            break
    return R, pivots


def rank(rows):
    return len(rref(rows)[1]) if rows else 0


def inverse(A):
    n = len(A)
    R, piv = rref([A[i] + eye(n)[i] for i in range(n)])
    assert piv[:n] == list(range(n)), "singular matrix"
    return [row[n:] for row in R]


def solve_affine(A, b, nvars):
    R, piv = rref([list(A[i]) + [b[i] % P] for i in range(len(A))])
    for row in R:
        if all(x == 0 for x in row[:nvars]) and row[nvars] != 0:
            raise AssertionError("inconsistent affine system")
    piv = [p for p in piv if p < nvars]
    free = [j for j in range(nvars) if j not in piv]
    part = [0] * nvars
    for i, p in enumerate(piv):
        part[p] = R[i][nvars]
    basis = []
    for f in free:
        v = [0] * nvars
        v[f] = 1
        for i, p in enumerate(piv):
            v[p] = (-R[i][f]) % P
        basis.append(v)
    return part, basis, piv


def affine_system(fn, nvars):
    z = [0] * nvars
    c = fn(z)
    columns = []
    for j in range(nvars):
        e = [0] * nvars
        e[j] = 1
        y = fn(e)
        columns.append([(y[i] - c[i]) % P for i in range(len(c))])
    A = [[columns[j][i] for j in range(nvars)] for i in range(len(c))]
    b = [(-x) % P for x in c]
    return A, b


def vadd(x, y):
    return [(a + b) % P for a, b in zip(x, y)]


def vsub(x, y):
    return [(a - b) % P for a, b in zip(x, y)]


def vscale(a, x):
    return [(a * z) % P for z in x]


def in_span(x, rows):
    return rank(rows + [x]) == rank(rows)


# A triple acts by (v,z) -> (M v, T z + L v).
def tcompose(g, h):
    M, T, L = g
    N, U, K = h
    return mul(M, N), mul(T, U), add(mul(T, K), mul(L, N))


def tinverse(g):
    M, T, L = g
    Mi, Ti = inverse(M), inverse(T)
    return Mi, Ti, mul(mul(Ti, [[(-x) % P for x in row] for row in L]), Mi)


def tpower(g, n):
    out = (eye(len(g[0])), eye(len(g[1])), zero(len(g[1]), len(g[0])))
    for _ in range(n):
        out = tcompose(out, g)
    return out


def tcomm(g, h):
    return tcompose(tcompose(tcompose(tinverse(g), tinverse(h)), g), h)


def jrow(q):
    # q=(e1,e2,f1,f2); omega convention from the manifest.
    return [[(-q[2]) % P, (-q[3]) % P, q[0] % P, q[1] % P], [0]*4, [0]*4]


def q_from_jrow(L):
    assert L[1] == [0]*4 and L[2] == [0]*4
    r = L[0]
    return (r[2], r[3], (-r[0]) % P, (-r[1]) % P)


A = [[1,1,0,0], [0,1,0,0], [0,0,1,0], [0,0,2,1]]
B = [[1,0,0,1], [0,1,1,0], [0,0,1,0], [0,0,0,1]]
C = [[1,0,2,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]
TX = [[1,2,0], [0,1,1], [0,0,1]]
TY = [[1,1,0], [0,1,1], [0,0,1]]
TZ = [[1,0,1], [0,1,0], [0,0,1]]
QX = (0,0,0,1)
QY = (0,1,0,0)
OMEGA = [[0,0,1,0], [0,0,0,1], [2,0,0,0], [0,2,0,0]]
MS = [A, B, C]
TS = [TX, TY, TZ]


def chunks(x):
    return [unflat(x[12*i:12*(i+1)], 3, 4) for i in range(3)]


def pack(Ls):
    return sum((flat(L) for L in Ls), [])


def triples(x):
    return [(MS[i], TS[i], chunks(x)[i]) for i in range(3)]


def residual(x):
    X, Y, Z = triples(x)
    out = flat(sub(tpower(X, 3)[2], jrow(QX)))
    out += flat(sub(tpower(Y, 3)[2], jrow(QY)))
    out += flat(tpower(Z, 3)[2][1:])
    out += flat(tcompose(tcomm(X, Y), tinverse(Z))[2][1:])
    out += flat(tcomm(X, Z)[2][1:])
    out += flat(tcomm(Y, Z)[2][1:])
    assert len(out) == 56
    return out


def word_triple(x, a, b, d):
    X, Y, Z = triples(x)
    return tcompose(tcompose(tpower(X, a), tpower(Y, b)), tpower(Z, d))


def image_set(N):
    return {tuple(mv(N, v)) for v in itertools.product(range(P), repeat=4)}


def cube_rows(x):
    rows = []
    for a, b, d in itertools.product(range(P), repeat=3):
        h = word_triple(x, a, b, d)
        h3 = tpower(h, 3)
        assert h3[0] == eye(4) and h3[1] == eye(3)
        lam = q_from_jrow(h3[2])
        N = add(add(eye(4), h[0]), mpow(h[0], 2))
        W = image_set(N)
        F = {tuple((lam[i] + w[i]) % P for i in range(4)) for w in W}
        rows.append({"word": (a,b,d), "lambda": lam, "W": W, "F": F})
    assert len(rows) == 27 and len({r["word"] for r in rows}) == 27
    return rows


def signature(x):
    rows = cube_rows(x)
    assert all(r["W"] == {(0,0,0,0)} for r in rows)
    return tuple(z for r in rows for z in r["lambda"])


def symp(u, v):
    return sum(u[i] * OMEGA[i][j] * v[j] for i in range(4) for j in range(4)) % P


def support_summary(x):
    rows = cube_rows(x)
    sigma = set().union(*(r["F"] for r in rows))
    span_rows = [list(v) for v in sorted(sigma)]
    sd = rank(span_rows)
    subspace = (len(sigma) == P ** sd and (0,0,0,0) in sigma)
    basis = []
    for v in sorted(sigma):
        if not in_span(list(v), basis):
            basis.append(list(v))
    gram = [[symp(u, v) for v in basis] for u in basis]
    return rows, sigma, sd, subspace, rank(gram)


def matrix_affine_solutions(resfn, nvars, shape, limit_dim=8):
    AA, bb = affine_system(resfn, nvars)
    p, bs, _ = solve_affine(AA, bb, nvars)
    assert len(bs) <= limit_dim, "enumeration hard kill"
    for coeff in itertools.product(range(P), repeat=len(bs)):
        x = p[:]
        for a, v in zip(coeff, bs):
            x = vadd(x, vscale(a, v))
        yield unflat(x, *shape)


def d_res(v):
    D = unflat(v, 4, 4)
    out = []
    for M in MS:
        out += flat(sub(mul(D, M), mul(M, D)))
    out += vsub(mv(D, QX), list(QX))
    out += vsub(mv(D, QY), list(QY))
    return out


def u_res(v):
    U = unflat(v, 3, 3)
    out = []
    for T in TS:
        out += flat(sub(mul(U, T), mul(T, U)))
    out += vsub(mv(U, [1,0,0]), [1,0,0])
    return out


def digits(v):
    return "".join(str(x) for x in v)


def mtext(M):
    return "/".join(digits(row) for row in M)


def transform_solution(x, D, U):
    Ui = inverse(U)
    return pack([mul(mul(Ui, L), D) for L in chunks(x)])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--full", action="store_true")
    args = ap.parse_args()

    # Frozen structural identities, derived independently from the triple law.
    for M in MS:
        assert mpow(M, 3) == eye(4)
        assert mul(mul(transpose(M), OMEGA), M) == OMEGA
    for T in TS:
        assert mpow(T, 3) == eye(3)
    zL = zero(3, 4)
    X0, Y0, Z0 = (A,TX,zL), (B,TY,zL), (C,TZ,zL)
    assert tcompose(tcomm(X0,Y0), tinverse(Z0))[:2] == (eye(4),eye(3))
    assert tcomm(X0,Z0)[:2] == (eye(4),eye(3))
    assert tcomm(Y0,Z0)[:2] == (eye(4),eye(3))
    assert mv(A, QX) == list(QX) and mv(B, QY) == list(QY)
    assert symp(QX, QY) == 2

    AA, bb = affine_system(residual, 36)
    part, hom, piv = solve_affine(AA, bb, 36)
    assert len(AA) == 56 and len(AA[0]) == 36
    assert rank(AA) == 17 and rank([AA[i] + [bb[i]] for i in range(56)]) == 17
    assert len(hom) == 19 and residual(part) == [0]*56

    # Twelve independent inner-lift coordinates, then all twelve R matrix units.
    gauges = []
    gauge_names = []
    for i, name in enumerate(("X","Y","Z")):
        for j in range(4):
            Ls = [zero(3,4) for _ in range(3)]
            Ls[i][0][j] = 1
            gauges.append(pack(Ls)); gauge_names.append("inner_%s_%d" % (name,j))
    for rr in range(3):
        for cc in range(4):
            R = zero(3,4); R[rr][cc] = 1
            Ls = [sub(mul(TS[i],R), mul(R,MS[i])) for i in range(3)]
            gauges.append(pack(Ls)); gauge_names.append("kernel_R_%d_%d" % (rr,cc))
    assert len(gauges) == 24
    assert all(residual(vadd(part,g)) == [0]*56 for g in gauges)
    assert rank(gauges[:12]) == 12 and rank(gauges) == 18

    # Complete linear centralizers, then the kernel-automorphism conditions.
    Ds = []
    for D in matrix_affine_solutions(d_res, 16, (4,4)):
        if rank(D) == 4 and mul(mul(transpose(D),OMEGA),D) == OMEGA:
            Ds.append(D)
    Us = []
    for U in matrix_affine_solutions(u_res, 9, (3,3)):
        if rank(U) == 3:
            Us.append(U)
    expected_D = [add(eye(4), [[0,0,a,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]) for a in range(3)]
    expected_U = [add(eye(3), [[0,0,d],[0,0,0],[0,0,0]]) for d in range(3)]
    assert {tuple(flat(D)) for D in Ds} == {tuple(flat(D)) for D in expected_D}
    assert {tuple(flat(U)) for U in Us} == {tuple(flat(U)) for U in expected_U}
    assert len(Ds) * len(Us) == 9

    sig0 = signature(part)
    sig_deltas = [vsub(signature(vadd(part,h)), sig0) for h in hom]
    sig_rank = rank(sig_deltas)
    assert sig_rank == 1
    sig_kernel_dim = len(hom) - sig_rank
    assert sig_kernel_dim == 18
    assert all(signature(vadd(part,g)) == sig0 for g in gauges)
    assert rank(gauges) == sig_kernel_dim
    direction = next(h for h in hom if signature(vadd(part,h)) != sig0)
    reps = [vadd(part, vscale(r,direction)) for r in range(3)]
    rep_sigs = [signature(x) for x in reps]
    assert len(set(rep_sigs)) == 3

    # Each of the nine stabilizers preserves the affine system and fixes all
    # three quotient points.  Burnside on the 3-point quotient is therefore 3.
    fixed_counts = []
    stabilizer_maps = []
    for D in sorted(Ds, key=lambda M: tuple(flat(M))):
        for U in sorted(Us, key=lambda M: tuple(flat(M))):
            induced = []
            for x in reps:
                y = transform_solution(x,D,U)
                assert residual(y) == [0]*56
                sy = signature(y)
                assert sy in rep_sigs
                induced.append(rep_sigs.index(sy))
            stabilizer_maps.append(induced)
            fixed_counts.append(sum(induced[r] == r for r in range(3)))
    assert fixed_counts == [3]*9
    burnside_orbits = sum(fixed_counts) // 9
    assert burnside_orbits == 3
    orbit_sizes = [P**18] * 3
    assert sum(orbit_sizes) == P**19

    # Complete projected cube supports for all 27 quotient cosets per orbit.
    support_records = []
    for r, x in enumerate(reps):
        rows, sigma, sd, is_subspace, sr = support_summary(x)
        assert len(rows) == 27 and all(row["W"] == {(0,0,0,0)} for row in rows)
        assert QY in sigma and QX in sigma and (0,1,0,1) not in sigma
        assert not is_subspace
        support_records.append({
            "r": r, "size": len(sigma), "span_dimension": sd,
            "symplectic_rank": sr, "sigma": sorted(sigma), "rows": rows,
        })
    assert sorted(rec["size"] for rec in support_records) == [13,15,15]
    assert all(rec["span_dimension"] == 3 and rec["symplectic_rank"] == 2
               for rec in support_records)

    # Explicit clean-room mixed-word check for the particular solution.
    mixed = next(row for row in cube_rows(part) if row["word"] == (1,1,0))
    assert mixed["lambda"] == (0,0,0,0)

    summary = {
        "field": 3,
        "system": {"equations": 56, "variables": 36, "rank": rank(AA),
                   "augmented_rank": rank([AA[i]+[bb[i]] for i in range(56)]),
                   "dimension": len(hom)},
        "particular": [mtext(L) for L in chunks(part)],
        "gauge": {"listed": len(gauges), "inner_rank": rank(gauges[:12]),
                  "total_rank": rank(gauges), "names": gauge_names},
        "stabilizer": {"D": [mtext(D) for D in sorted(Ds,key=lambda M:tuple(flat(M)))],
                       "U": [mtext(U) for U in sorted(Us,key=lambda M:tuple(flat(M)))],
                       "pairs": 9, "induced_maps": stabilizer_maps,
                       "fixed_counts": fixed_counts},
        "signature": {"image_dimension": sig_rank, "kernel_dimension": sig_kernel_dim},
        "orbits": {"burnside_count": burnside_orbits, "sizes": orbit_sizes,
                   "sum": sum(orbit_sizes)},
        "mixed_word_110_label": digits(mixed["lambda"]),
        "supports": [],
    }
    for rec in support_records:
        row_out = []
        for row in rec["rows"]:
            row_out.append({"word": digits(row["word"]), "lambda": digits(row["lambda"]),
                            "W": sorted(digits(w) for w in row["W"])})
        summary["supports"].append({
            "r": rec["r"], "size": rec["size"],
            "span_dimension": rec["span_dimension"],
            "symplectic_rank": rec["symplectic_rank"],
            "sigma": [digits(v) for v in rec["sigma"]],
            "rows": row_out if args.full else "use --full",
            "closure_defect": ["0100", "0001", "0101"],
        })
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

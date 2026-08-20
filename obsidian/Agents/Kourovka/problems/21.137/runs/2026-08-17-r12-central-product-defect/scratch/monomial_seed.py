#!/usr/bin/env python3
"""Exact F_3 arithmetic for one frozen 15-dimensional monomial-algebra seed.

J has basis x^i y^j, 0<=i,j<=3, (i,j)!=(0,0), with
x^4=y^4=yx=0.  The group tested is 1+J and C=1+F_3 x^3y^3.
No general-purpose group package is used.
"""

from itertools import product
import random

P = 3
BASIS = [(i, j) for i in range(4) for j in range(4) if (i, j) != (0, 0)]
INDEX = {m: r for r, m in enumerate(BASIS)}
DIM = len(BASIS)
C_MON = (3, 3)
C_IDX = INDEX[C_MON]
MIXED = [(i, j) for i in range(1, 4) for j in range(1, 4)]
XMON = [(i, 0) for i in range(1, 4)]
YMON = [(0, j) for j in range(1, 4)]


def add(u, v):
    return tuple((a + b) % P for a, b in zip(u, v))


def scale(a, u):
    return tuple((a * b) % P for b in u)


def mul(u, v):
    out = [0] * DIM
    for r, a in enumerate(u):
        if not a:
            continue
        i, j = BASIS[r]
        for s, b in enumerate(v):
            if not b:
                continue
            k, ell = BASIS[s]
            if j > 0 and k > 0:  # the monomial contains yx
                continue
            if i + k > 3 or j + ell > 3:
                continue
            out[INDEX[(i + k, j + ell)]] = (
                out[INDEX[(i + k, j + ell)]] + a * b
            ) % P
    return tuple(out)


ZERO = (0,) * DIM


def vec(positions, coeffs):
    out = [0] * DIM
    for m, a in zip(positions, coeffs):
        out[INDEX[m]] = a
    return tuple(out)


def cube(u):
    return mul(mul(u, u), u)


def row_basis(columns):
    """Return a row-echelon basis for the span of the supplied column vectors."""
    rows = [list(v) for v in columns if any(v)]
    basis = []
    pivot = 0
    while pivot < DIM and rows:
        hit = next((r for r, v in enumerate(rows) if v[pivot]), None)
        if hit is None:
            pivot += 1
            continue
        v = rows.pop(hit)
        inv = 1 if v[pivot] == 1 else 2
        v = [(inv * a) % P for a in v]
        new_rows = []
        for w in rows:
            if w[pivot]:
                factor = w[pivot]
                w = [(a - factor * b) % P for a, b in zip(w, v)]
            if any(w):
                new_rows.append(w)
        for r, w in enumerate(basis):
            if w[pivot]:
                factor = w[pivot]
                basis[r] = [(a - factor * b) % P for a, b in zip(w, v)]
        basis.append(v)
        rows = new_rows
        pivot += 1
    return [tuple(v) for v in basis]


def span(basis):
    vals = {ZERO}
    for b in basis:
        vals |= {add(v, b) for v in tuple(vals)}
        vals |= {add(v, scale(2, b)) for v in tuple(vals)}
    return vals


def span_with_witness(columns):
    """Map each value in the column span to one coefficient vector."""
    vals = {ZERO: (0,) * len(columns)}
    for j, b in enumerate(columns):
        old = tuple(vals.items())
        for value, coeffs in old:
            for a in (1, 2):
                new_value = add(value, scale(a, b))
                if new_value not in vals:
                    new_coeffs = list(coeffs)
                    new_coeffs[j] = a
                    vals[new_value] = tuple(new_coeffs)
    return vals


def without_c(v):
    return v[:C_IDX] + v[C_IDX + 1 :]


def sparse(v, omit_c=False):
    mons = [m for r, m in enumerate(BASIS) if not (omit_c and r == C_IDX)]
    pieces = []
    for a, (i, j) in zip(v, mons):
        if a:
            pieces.append(f"{a}*x^{i}y^{j}")
    return "+".join(pieces) if pieces else "0"


def main():
    # The exact identity used to avoid a 3^15 input loop is
    # (a+b+m)^3=a^3+b^3+a^2b+ab^2+a^2m+amb+mb^2,
    # where a is x-pure, b is y-pure, and m is mixed.
    W = set()
    representatives = {}
    ranks = {}
    for ac in product(range(P), repeat=3):
        a = vec(XMON, ac)
        a2 = mul(a, a)
        for bc in product(range(P), repeat=3):
            b = vec(YMON, bc)
            b2 = mul(b, b)
            base = add(add(cube(a), cube(b)), add(mul(a2, b), mul(a, b2)))
            columns = []
            for mon in MIXED:
                m = vec([mon], [1])
                columns.append(add(add(mul(a2, m), mul(mul(a, m), b)), mul(m, b2)))
            rb = row_basis(columns)
            ranks[len(rb)] = ranks.get(len(rb), 0) + 1
            for z, mc in span_with_witness(columns).items():
                value = add(base, z)
                W.add(value)
                representatives.setdefault(value, add(add(a, b), vec(MIXED, mc)))

    # Independent spot-check of the affine image identity against direct cubes.
    random.seed(21137)
    spot_ok = True
    for _ in range(500):
        coeffs = [random.randrange(P) for _ in range(DIM)]
        u = tuple(coeffs)
        if cube(u) not in W:
            spot_ok = False
            break

    fibres = {}
    for w in W:
        fibres.setdefault(without_c(w), set()).add(w[C_IDX])
    fibre_hist = {}
    for values in fibres.values():
        fibre_hist[len(values)] = fibre_hist.get(len(values), 0) + 1

    lifted_keys = []
    for key in fibres:
        full = list(key)
        full.insert(C_IDX, 0)
        lifted_keys.append(tuple(full))
    key_basis = row_basis(lifted_keys)
    quotient_image_is_subspace = len(fibres) == P ** len(key_basis)
    missing_sum = None
    key_set = set(fibres)
    if not quotient_image_is_subspace:
        for u in key_set:
            for v in key_set:
                w = tuple((a + b) % P for a, b in zip(u, v))
                if w not in key_set:
                    missing_sum = (u, v, w)
                    break
            if missing_sum is not None:
                break

    x = vec([(1, 0)], [1])
    y = vec([(0, 1)], [1])
    x3, y3 = cube(x), cube(y)
    commutator_defect = add(mul(x3, y3), scale(2, mul(y3, x3)))
    expected_c = vec([C_MON], [1])
    central_root = representatives.get(expected_c)

    zero_key = (0,) * (DIM - 1)
    print(f"field=F_3 algebra_dimension={DIM} group_order=3^{DIM}")
    print("relations=x^4=y^4=yx=0; C=F_3*x^3*y^3")
    print(f"cube_image_size={len(W)}")
    print(f"affine_map_rank_histogram={dict(sorted(ranks.items()))}")
    print(f"direct_cube_spot_checks=500 result={'pass' if spot_ok else 'FAIL'}")
    print(f"quotient_cube_image_size={len(fibres)} span_rank={len(key_basis)}")
    print(f"quotient_cube_image_additive_subspace={quotient_image_is_subspace}")
    if missing_sum is not None:
        print(f"missing_sum_u={sparse(missing_sum[0], omit_c=True)}")
        print(f"missing_sum_v={sparse(missing_sum[1], omit_c=True)}")
        print(f"missing_sum_u_plus_v={sparse(missing_sum[2], omit_c=True)}")
        for label, key in (("u", missing_sum[0]), ("v", missing_sum[1])):
            value = next(w for w in W if without_c(w) == key)
            root = representatives[value]
            print(f"missing_sum_{label}_root={sparse(root)}")
            print(f"missing_sum_{label}_root_cube={sparse(cube(root))}")
    print(f"central_fibre_size_histogram={dict(sorted(fibre_hist.items()))}")
    print(f"identity_central_fibre={sorted(fibres.get(zero_key, set()))}")
    if central_root is not None:
        print(f"central_c_root={sparse(central_root)}")
    print(f"x3_in_image={x3 in W} y3_in_image={y3 in W}")
    print(f"x3y3_minus_y3x3_equals_c={commutator_defect == expected_c}")
    print(f"all_central_fibres_at_least_two={all(len(v) >= 2 for v in fibres.values())}")

    if not quotient_image_is_subspace:
        print("seed_gate=FAIL: quotient actual-cube image is not a subgroup")
    elif not all(len(v) >= 2 for v in fibres.values()):
        first = next(k for k, v in fibres.items() if len(v) < 2)
        print(f"seed_gate=FAIL: singleton fibre key={first} values={sorted(fibres[first])}")
    elif commutator_defect != expected_c:
        print("seed_gate=FAIL: designated cube values do not retain a nonzero central commutator")
    else:
        print("seed_gate=PASS: self anti-diagonal central quotient meets the frozen set-theoretic gates")


if __name__ == "__main__":
    main()

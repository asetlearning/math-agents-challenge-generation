#!/usr/bin/env python3
"""Certify the full central-relator image and normalized section quotient.

This checker does not construct or enumerate alternate groups.  It derives the
full feasible image in the assigned 18 relator coordinates from the normalized
cochain equations, derives the exact central generator-lift gauge, partitions
the feasible image into gauge orbits, and realizes one full factor cochain for
every extracted representative.  No 3^18 enumeration occurs.
"""

import hashlib
from itertools import product

import central_cohomology as cc


def clone_system(src, nvars=None):
    out = cc.SparseAffine(src.nvars if nvars is None else nvars)
    # Existing pivot rows are read-only in SparseAffine.add; shallow copying
    # the pivot dictionary is therefore an exact independent continuation.
    out.pivots = src.pivots.copy()
    out.inconsistent = src.inconsistent
    out.rows_seen = src.rows_seen
    return out


def eval_affine(expr, x):
    return (expr[1] + sum(c * x[i] for i, c in expr[0].items())) % 3


def add_fixed_relator_row(base, relvals, row18):
    sys = clone_system(base)
    for i, (_, z) in enumerate(relvals):
        for j, expr in enumerate(z):
            assert sys.add(expr[0].copy(),
                           (row18[3 * i + j] - expr[1]) % 3,
                           ("fixed-relator", i, j))
    assert not sys.inconsistent
    x = sys.particular()
    got = tuple(eval_affine(expr, x) for _, z in relvals for expr in z)
    assert got == tuple(row18)
    digest = hashlib.sha256("".join(map(str, x)).encode("ascii")).hexdigest()
    return len(sys.pivots), len(cc.UVAR) - len(sys.pivots), digest


def affine_rows(constraints):
    rsys = cc.SparseAffine(18)
    for row, rhs, source in constraints:
        assert rsys.add(row.copy(), rhs, source)
    assert not rsys.inconsistent
    particular = rsys.particular()
    basis = rsys.null_basis()
    if len(basis) > 10:
        raise RuntimeError("derived relator dimension exceeds frozen 3^10 enumeration cap")
    rows = set()
    for coeffs in product(range(3), repeat=len(basis)):
        r = tuple((particular[i] + sum(coeffs[j] * basis[j][i]
                                       for j in range(len(basis)))) % 3
                  for i in range(18))
        rows.add(r)
    assert len(rows) == 3 ** len(basis)
    return tuple(particular), basis, rows


def gauge_image(gauge):
    image = set()
    for a in product(range(3), repeat=9):
        image.add(tuple(sum(gauge[i][j] * a[j] for j in range(9)) % 3
                        for i in range(18)))
    return image


def main():
    cc.frozen_row_checks()
    vdef = cc.defect_labels()
    vpairs, vtriples, vscalars = cc.certify_v_associativity(vdef)
    base, generated = cc.obstruction_system(vdef)
    assert not base.inconsistent
    relvals = cc.relator_affines(vdef)

    image_sys = clone_system(base)
    constraints, combined_rank = cc.relator_image_system(image_sys, relvals)
    rpart, rbasis, feasible = affine_rows(constraints)
    gauge = cc.central_lift_gauge_matrix()
    grank = cc.gf3_rank_rows(gauge)
    gimage = gauge_image(gauge)
    assert len(gimage) == 3 ** grank

    # Gauge increments must preserve every affine constraint homogeneously.
    for g in gimage:
        for row, _, _ in constraints:
            assert sum(row.get(i, 0) * g[i] for i in range(18)) % 3 == 0

    unseen = set(feasible)
    reps = []
    while unseen:
        seed = min(unseen)
        orbit = {tuple((seed[i] + g[i]) % 3 for i in range(18))
                 for g in gimage}
        assert orbit <= feasible
        assert len(orbit) == len(gimage)
        reps.append(min(orbit))
        unseen.difference_update(orbit)
    reps.sort()
    assert len(feasible) == len(reps) * len(gimage)
    if len(reps) > 100:
        raise RuntimeError("derived quotient has over 100 representatives; stop before factor extraction")

    c1dim, brank, z1dim, grank2 = cc.section_equivalence_ranks()
    assert grank2 == grank
    homogeneous_dim = len(cc.UVAR) - len(base.pivots)
    relator_dim = len(rbasis)
    exact_row_kernel = homogeneous_dim - relator_dim
    zero_relator_gauge = (c1dim - grank) - z1dim
    assert exact_row_kernel == zero_relator_gauge
    assert homogeneous_dim - brank == relator_dim - grank

    realized = []
    for r in reps:
        realized.append((r, *add_fixed_relator_row(base, relvals, r)))

    print("frozen lift reconstruction: PASS")
    print("V defect/associativity checks:", vpairs, vtriples, vscalars)
    print("normalized central variables/equations/rank/dimension:",
          len(cc.UVAR), generated, len(base.pivots), homogeneous_dim)
    print("relator-definition combined rank:", combined_rank)
    print("complete affine relator constraints:")
    for row, rhs, _ in constraints:
        print(" ", "+".join(f"{c}*r{i}" for i, c in sorted(row.items())), "=", rhs)
    print("relator particular:", "".join(map(str, rpart)))
    print("relator homogeneous dimension/feasible rows:", relator_dim, len(feasible))
    print("generator-lift gauge rank/image size:", grank, len(gimage))
    print("normalized C1/coboundary/Z1 dimensions:", c1dim, brank, z1dim)
    print("exact-row kernel dimensions (cochain/gauge):",
          exact_row_kernel, zero_relator_gauge)
    print("quotient dimensions (full cochain/relator):",
          homogeneous_dim - brank, relator_dim - grank)
    print("derived orbit count:", len(reps))
    print("representatives and full-factor certificates:")
    for i, (r, rank, dim, digest) in enumerate(realized):
        print(f" {i:02d}", "".join(map(str, r)), rank, dim, digest)
    print("NO alternate group or cube enumeration performed")


if __name__ == "__main__":
    main()

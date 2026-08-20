#!/usr/bin/env python3
"""Exact all-element target gates for the 27 certified central gauge classes."""

import hashlib
from collections import deque
from itertools import product

import central_cohomology as cc
import check_exact_group as eg
import check_full_family as ff


CERTIFIED = [
    ("000000000000002002", "a74a5d9b959366b0b8913fabd7cc7e7af1a4e3605df09c3d95d2f3a00492f824"),
    ("000000000000002102", "1007faf0d4b276771e1f91550aafaedfdec9381fea8198e1edd8d13735244eec"),
    ("000000000000002202", "2fc9bee1f3cf19206c66648414dc77dbb769efff85b57d989d7852a90f212e35"),
    ("000000000000102002", "d90bfd2e7a4425328adf452b5cf397d787f3d170601ee06840781acba6cbbd2d"),
    ("000000000000102102", "4b8bdf2c7832b5948883e5816aae84ded2abf9b09dd6b6fccb93e81bc9c13194"),
    ("000000000000102202", "27e7ab454407467922b213a86aa06e067b3bd7cd25a5ced8d9551733cc51e06b"),
    ("000000000000202002", "d75edbd9b366c37374c4a7606f59705daad344792328fba651cda53c8b0e7328"),
    ("000000000000202102", "e573d6d178d20f18647a6765c204150556c90c0693a6c8c07956a2811728a5fa"),
    ("000000000000202202", "68c1a9fabca880299da9d2d43d868f59d942119d2f0c6af95eef709711f48bb2"),
    ("000000100000012022", "6275f76c00ab7c7fcb35913158d6e56939625b76e15022ebccea231a2ea7074d"),
    ("000000100000012122", "f7ef7a4c58ebbf2b4f2722d8dd8679632b61948e2d8c0e4454244a63bf478c07"),
    ("000000100000012222", "b77a65f26ab70f2b573e6e789a8a67e97c9609c753f3311772f79d1dbc74d30b"),
    ("000000100000112022", "3830cd325b90d9a640dc6d4c87e6778407450a61cfbe1da12992fd8e2c3caef7"),
    ("000000100000112122", "d85e91f9fc153714f923f0d23ea6dc443bf13a85e915a95676350a3e9b353dd4"),
    ("000000100000112222", "701c7bf86d34ea8bf2ccda942a1c6828835af9c09453d33d7ca6aebbb389b339"),
    ("000000100000212022", "3cf9d2aad6f7c4506eed21e9bd3a43649d26e1bdd5ee21ece500d1735a023776"),
    ("000000100000212122", "a19ad8c7cd82dcbdff6b6e83e0363e3fd150e198a89db40a5c662dd021031880"),
    ("000000100000212222", "4ab6aceb5fae02a03208f33afe805917f32b98aa1467795524d0f39a1db143a6"),
    ("000000200000022012", "22c61b81e042c6c2dc22fddf02347fa203d528ffe51ac5abb7894503e4ece660"),
    ("000000200000022112", "0c910028f41a103c6fdc708f610a2dbacd202992e9c3d7c94c501f751a73ebae"),
    ("000000200000022212", "f8de2485f4b746d0d360fbda2d19677e905b6bec2b120690c4907a04264fe8f0"),
    ("000000200000122012", "7b789f1fd39f4a217d92fd7fcebc91e9c8aa348a7a46b73e06004be7dca1989f"),
    ("000000200000122112", "6f6d3451c2359876252fe7caf3a9040a9cdb3271026b8682eaa5fcf65f1b8aac"),
    ("000000200000122212", "09caaae575bec7b71da6b9394b572f11dea2f1765300e823be65bc9a74238d37"),
    ("000000200000222012", "64658c9fe8221df32b25b633829b06e4f304d02e35afa764495c28a0c0135999"),
    ("000000200000222112", "0d4a90c486bda9ae817c667b1818e931ac86f70620c865453c49fd0b36e74692"),
    ("000000200000222212", "d929c333010c56683ff9823dca1fb2c35470c5491a8fca875c7043799384a1e5"),
]


def solve_row(base, relvals, row, expected_digest):
    sys = ff.clone_system(base)
    for i, (_, z) in enumerate(relvals):
        for j, expr in enumerate(z):
            assert sys.add(expr[0].copy(),
                           (row[3 * i + j] - expr[1]) % 3,
                           ("certified-row", i, j))
    assert not sys.inconsistent
    x = sys.particular()
    got = tuple(ff.eval_affine(expr, x) for _, z in relvals for expr in z)
    assert got == row
    digest = hashlib.sha256("".join(map(str, x)).encode("ascii")).hexdigest()
    assert digest == expected_digest
    return x


def expected_relators(row, labels):
    qzero = (0, 0, 0)
    return [tuple(labels[i]) + tuple(row[3 * i:3 * i + 3]) + qzero
            for i in range(6)]


def generated_closure(cubes, mul, inv, one):
    gens = []
    generated = {one}
    orders = [1]
    for s in sorted(cubes):
        if s in generated:
            continue
        gens.append(s)
        steps = gens + [inv(x) for x in gens]
        generated = {one}
        queue = deque([one])
        while queue:
            h = queue.popleft()
            for a in steps:
                ha = mul(h, a)
                if ha not in generated:
                    generated.add(ha)
                    queue.append(ha)
        orders.append(len(generated))
    return generated, orders


def main():
    assert len(CERTIFIED) == 27
    assert len({r for r, _ in CERTIFIED}) == 27
    cc.frozen_row_checks()
    labels = cc.frozen_row_checks()[1]
    vdef = cc.defect_labels()
    vpairs, vtriples, vscalars = cc.certify_v_associativity(vdef)
    base, generated_equations = cc.obstruction_system(vdef)
    assert not base.inconsistent
    relvals = cc.relator_affines(vdef)
    print("certified input classes:", len(CERTIFIED))
    print("V checks/base equations/rank:", vpairs, vtriples, vscalars,
          generated_equations, len(base.pivots))

    one = (0,) * 10
    X = (0,) * 7 + (1, 0, 0)
    Y = (0,) * 7 + (0, 1, 0)
    Z = (0,) * 7 + (0, 0, 1)
    hits = []
    rows_out = []
    for idx, (rowstr, digest) in enumerate(CERTIFIED):
        row = tuple(map(int, rowstr))
        uvec = solve_row(base, relvals, row, digest)
        zvec, zscalars = eg.verify_central_associativity(vdef, uvec)
        assert (zvec, zscalars) == (19683, 59049)
        mul, inv, pow3, comm, _ = eg.make_group(vdef, uvec)
        relators = [pow3(X), pow3(Y), pow3(Z),
                    mul(comm(X, Y), inv(Z)), comm(X, Z), comm(Y, Z)]
        assert relators == expected_relators(row, labels)

        cubes = set()
        exp9 = True
        exp_defect = None
        order9_witness = None
        count = 0
        for g in product(range(3), repeat=10):
            count += 1
            cube = pow3(g)
            ninth = pow3(cube)
            if ninth != one and exp_defect is None:
                exp9, exp_defect = False, (g, ninth)
            if cube != one and order9_witness is None:
                order9_witness = g
            cubes.add(cube)
        assert count == 59049
        exact_exp9 = exp9 and order9_witness is not None

        closure, progression = generated_closure(cubes, mul, inv, one)
        closed = closure == cubes
        closure_size = len(closure)
        outside = None if closed else next(iter(closure - cubes))

        # Lead requires this gate only after literal closure passes.
        noncomm = None
        if closed:
            cx, cy = pow3(X), pow3(Y)
            noncomm = mul(cx, cy) != mul(cy, cx)
        hit = exact_exp9 and closed and noncomm is True
        if hit:
            hits.append(idx)
        rows_out.append((idx, rowstr, exact_exp9, exp_defect,
                         len(cubes), closed, closure_size, progression,
                         outside, noncomm, order9_witness))
        print("CLASS", idx, rowstr,
              "exp9", exact_exp9,
              "cube_size", len(cubes),
              "closed", closed,
              "closure_size", closure_size,
              "order/kernel/quotient", 59049, 2187, 27,
              "noncomm", noncomm,
              "hit", hit)
        if exp_defect is not None:
            print(" EXPONENT_DEFECT", exp_defect)
        if outside is not None:
            print(" CLOSURE_OUTSIDE", outside, "progression", progression)
        print(" ORDER9_WITNESS", order9_witness)
    print("ALL CLASS RESULTS:", rows_out)
    print("TARGET-EQUAL CLASS INDICES:", hits)


if __name__ == "__main__":
    main()

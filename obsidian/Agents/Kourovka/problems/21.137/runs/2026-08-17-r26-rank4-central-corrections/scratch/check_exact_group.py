#!/usr/bin/env python3
"""Heavy exact checker for the simplest feasible central-correction row R0.

The checker first reconstructs the full normalized cochain system, imposes R0,
and obtains one exact factor set.  It then uses the resulting ten-coordinate
polycyclic normal form to inspect every one of the 3^10 elements and its
literal cube.  No generated-power subgroup is substituted for the image set.
"""

import hashlib
from collections import deque
from itertools import product

import central_cohomology as cc


R0 = [0] * 18
R0[14] = 2
R0[17] = 2


def solve_r0():
    cc.frozen_row_checks()
    vdef = cc.defect_labels()
    vpairs, vtriples, vscalars = cc.certify_v_associativity(vdef)
    sys, generated = cc.obstruction_system(vdef)
    assert not sys.inconsistent
    assert len(sys.pivots) == 1951
    relvals = cc.relator_affines(vdef)
    for i, (_, z) in enumerate(relvals):
        for j, expr in enumerate(z):
            # expr == the fixed coordinate R0_(i,j).
            row = expr[0].copy()
            rhs = (R0[3 * i + j] - expr[1]) % 3
            assert sys.add(row, rhs, ("R0", i, j))
    assert not sys.inconsistent
    assert len(sys.pivots) == 1959
    uvec = sys.particular()
    assert len(uvec) == 2028
    for i, (_, z) in enumerate(relvals):
        got = [(expr[1] + sum(c * uvec[k] for k, c in expr[0].items())) % 3
               for expr in z]
        assert got == R0[3 * i:3 * i + 3], (i, got)
    digest = hashlib.sha256("".join(map(str, uvec)).encode("ascii")).hexdigest()
    return vdef, uvec, digest, generated, (vpairs, vtriples, vscalars)


def make_group(vdef, uvec):
    def u(q, r):
        if q == cc.ONE or r == cc.ONE:
            return (0, 0, 0)
        return tuple(uvec[cc.UVAR[q, r, j]] for j in range(3))

    ftable = {(q, r): (vdef[q, r], u(q, r)) for q in cc.Q for r in cc.Q}

    def kmul(k, l):
        v, z = k
        w, a = l
        return (tuple((v[i] + w[i]) % 3 for i in range(4)),
                ((z[0] + a[0] + 2 * cc.omega(v, w)) % 3,
                 (z[1] + a[1]) % 3,
                 (z[2] + a[2]) % 3))

    def kinv(k):
        v, z = k
        return tuple(-x % 3 for x in v), tuple(-x % 3 for x in z)

    def kalpha(q, k):
        v, z = k
        m, t, l = cc.ALPHA[q]
        mv = tuple(cc.mvec(m, v))
        tz, lv = cc.mvec(t, z), cc.mvec(l, v)
        return mv, tuple((tz[j] + lv[j]) % 3 for j in range(3))

    def unpack(g):
        return (g[:4], g[4:7]), g[7:]

    def pack(k, q):
        return tuple(k[0]) + tuple(k[1]) + tuple(q)

    def mul(g, h):
        k, q = unpack(g)
        l, r = unpack(h)
        out = kmul(kmul(k, kalpha(q, l)), ftable[q, r])
        return pack(out, cc.qmul(q, r))

    def inv(g):
        k, q = unpack(g)
        qi = cc.qinv(q)
        rhs = kmul(kinv(k), kinv(ftable[q, qi]))
        v, z = rhs
        mi, ti, li = cc.tinv(cc.ALPHA[q])
        mv = tuple(cc.mvec(mi, v))
        tz, lv = cc.mvec(ti, z), cc.mvec(li, v)
        return pack((mv, tuple((tz[j] + lv[j]) % 3 for j in range(3))), qi)

    def pow3(g):
        return mul(mul(g, g), g)

    def comm(g, h):
        return mul(mul(mul(inv(g), inv(h)), g), h)

    return mul, inv, pow3, comm, ftable


def verify_central_associativity(vdef, uvec):
    def u(q, r):
        if q == cc.ONE or r == cc.ONE:
            return (0, 0, 0)
        return tuple(uvec[cc.UVAR[q, r, j]] for j in range(3))

    vectors = scalars = 0
    for q in cc.Q:
        mq, tq, lq = cc.ALPHA[q]
        for r in cc.Q:
            qr = cc.qmul(q, r)
            for s in cc.Q:
                rs = cc.qmul(r, s)
                vqr, vqrs = vdef[q, r], vdef[qr, s]
                vrs, vqrs2 = vdef[r, s], vdef[q, rs]
                tvu = cc.mvec(tq, u(r, s))
                lv = cc.mvec(lq, vrs)
                mv = tuple(cc.mvec(mq, vrs))
                lhs = [
                    (u(q, r)[j] + u(qr, s)[j]
                     + (2 * cc.omega(vqr, vqrs) if j == 0 else 0)) % 3
                    for j in range(3)
                ]
                rhs = [
                    (tvu[j] + lv[j] + u(q, rs)[j]
                     + (2 * cc.omega(mv, vqrs2) if j == 0 else 0)) % 3
                    for j in range(3)
                ]
                assert lhs == rhs, (q, r, s, lhs, rhs)
                vectors += 1
                scalars += 3
    return vectors, scalars


def main():
    vdef, uvec, digest, eqs, vcounts = solve_r0()
    print("fixed R0 central row:", "".join(map(str, R0)))
    print("normalized factor solution SHA-256:", digest)
    print("cochain rank/dimension after R0:", 1959, 2028 - 1959)
    print("V defect/associativity checks:", *vcounts)
    zvec, zscalar = verify_central_associativity(vdef, uvec)
    print("central associativity checks:", zvec, zscalar)

    mul, inv, pow3, comm, _ = make_group(vdef, uvec)
    one = (0,) * 10
    X = (0,) * 7 + (1, 0, 0)
    Y = (0,) * 7 + (0, 1, 0)
    Z = (0,) * 7 + (0, 0, 1)
    assert mul(X, inv(X)) == mul(inv(X), X) == one
    assert mul(Y, inv(Y)) == mul(inv(Y), Y) == one
    assert mul(Z, inv(Z)) == mul(inv(Z), Z) == one
    relators = [
        pow3(X), pow3(Y), pow3(Z),
        mul(comm(X, Y), inv(Z)), comm(X, Z), comm(Y, Z),
    ]
    expected = [
        (0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0, 0, 0, 0, 0),
        one,
        (2, 0, 2, 1, 0, 0, 0, 0, 0, 0),
        (0, 2, 0, 2, 0, 0, 2, 0, 0, 0),
        (0, 1, 0, 1, 0, 0, 2, 0, 0, 0),
    ]
    assert relators == expected, (relators, expected)
    print("six corrected pc relators: PASS")
    print("unique coordinate normal forms/order:", "3^10", 3 ** 10)
    print("embedded kernel coordinate slice/order:", "3^7", 3 ** 7)
    print("quotient H3(3) coordinate projection/order:", "3^3", 3 ** 3)

    cubes = set()
    order9_witness = None
    element_count = 0
    for g in product(range(3), repeat=10):
        element_count += 1
        c = pow3(g)
        n = pow3(c)
        assert n == one, ("exponent defect", g, n)
        if c != one and order9_witness is None:
            order9_witness = g
        cubes.add(c)
    assert element_count == 59049
    assert order9_witness is not None
    print("all elements/cubes inspected:", element_count)
    print("exact exponent:", 9, "witness", order9_witness)
    print("literal cube-set size:", len(cubes))

    cube_list = sorted(cubes)
    subgroup_generators = []
    generated = {one}
    order_progression = [1]
    # Each newly admitted generator strictly enlarges the finite 3-subgroup,
    # so at most ten full BFS passes are possible.  Equality generated==cubes
    # is an exact subgroup test on the already-computed literal image set.
    for s in cube_list:
        if s in generated:
            continue
        subgroup_generators.append(s)
        steps = subgroup_generators + [inv(x) for x in subgroup_generators]
        generated = {one}
        queue = deque([one])
        while queue:
            h = queue.popleft()
            for a in steps:
                ha = mul(h, a)
                if ha not in generated:
                    generated.add(ha)
                    queue.append(ha)
        order_progression.append(len(generated))
    literal_closed = generated == cubes
    closure_extra = None if literal_closed else next(iter(generated - cubes))
    noncommuting_pair = None
    if literal_closed:
        for a in subgroup_generators:
            for b in subgroup_generators:
                ab, ba = mul(a, b), mul(b, a)
                if ab != ba:
                    noncommuting_pair = (a, b, ab, ba)
                    break
            if noncommuting_pair is not None:
                break
    print("literal cube generated-closure size:", len(generated))
    print("incremental subgroup orders:", order_progression)
    print("literal cube set equals its subgroup closure:", literal_closed)
    print("generated element outside literal set:", closure_extra)
    print("noncommuting literal cube pair:", noncommuting_pair)
    if literal_closed and noncommuting_pair is not None:
        print("TARGET ROWS: exponent nine PASS; literal cube set subgroup PASS; abelian conclusion VIOLATED")
    elif literal_closed:
        print("TARGET ROWS: exponent nine PASS; literal cube set subgroup PASS; cube set ABELIAN")
    else:
        print("TARGET ROWS: exponent nine PASS; literal cube set subgroup FAIL")


if __name__ == "__main__":
    main()

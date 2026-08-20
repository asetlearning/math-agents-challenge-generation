#!/usr/bin/env python3
"""Exact F_3 checker for the bounded formal-kernel obstruction.

This deliberately checks an integer array, not a group power map.  It verifies
only the rows claimed in the accompanying log/findings.
"""

from itertools import product

P3 = range(3)
V = tuple(product(P3, repeat=2))
P = tuple((v, t) for v in V for t in P3)


def beta(v, w):
    return (v[0] * w[1] - v[1] * w[0]) % 3


def negv(v):
    return ((-v[0]) % 3, (-v[1]) % 3)


def inv(a):
    # BCH coordinates for H_3(3): (v,t)^-1=(-v,-t).
    return (negv(a[0]), (-a[1]) % 3)


def conj(a, b):
    # a^b=a[a,b], and [a,b]=z^beta(abar,bbar).
    return (a[0], (a[1] + beta(a[0], b[0])) % 3)


def h(s):
    return 2 if s % 3 == 0 else -1


def kval(a, b, c):
    av, i = a
    bv, j = b
    cv, k = c
    delta = beta(av, bv)
    eps = beta(bv, cv)
    zeta = beta(cv, av)
    if delta * eps * zeta % 3 == 0:
        return 27
    skew = (eps * i + zeta * j + delta * k) % 3
    return 27 + h(skew)


def main():
    assert len(P) == 27
    values = {kval(a, b, c) for a in P for b in P for c in P}
    assert values == {26, 27, 29}

    # Every two-coordinate marginal is R(.)R(.)=27^2.
    for a in P:
        for b in P:
            assert sum(kval(a, b, c) for c in P) == 729
    for a in P:
        for c in P:
            assert sum(kval(a, b, c) for b in P) == 729
    for b in P:
        for c in P:
            assert sum(kval(a, b, c) for a in P) == 729

    # The three value-conjugation identities and two Hurwitz identities.
    for a, b, c in product(P, repeat=3):
        q = kval(a, b, c)
        assert q == kval(a, conj(b, a), conj(c, a))
        assert q == kval(conj(a, b), b, conj(c, b))
        assert q == kval(conj(a, c), conj(b, c), c)
        assert q == kval(b, inv(c), inv(a))
        assert q == kval(c, inv(b), a)

    # A selected quotient triple A=(1,0), B=(0,1), C=A+B has
    # (delta,eps,zeta)=(1,2,2), hence w=(eps,zeta,delta)=(2,2,1).
    av, bv, cv = (1, 0), (0, 1), (1, 1)
    delta = beta(av, bv)
    eps = beta(bv, cv)
    zeta = beta(cv, av)
    assert (delta, eps, zeta) == (1, 2, 2)
    level_counts = {s: [] for s in P3}
    for i, j, k in product(P3, repeat=3):
        skew = (eps * i + zeta * j + delta * k) % 3
        level_counts[skew].append(kval((av, i), (bv, j), (cv, k)))
    assert {s: (len(xs), set(xs)) for s, xs in level_counts.items()} == {
        0: (9, {29}),
        1: (9, {26}),
        2: (9, {26}),
    }

    # In Z[omega]/(omega^2+omega+1), the transforms at +w and -w are
    # both 9*(29+26*omega+26*omega^2)=27; the zero transform is 729.
    transform_zero = 9 * (29 + 26 + 26)
    transform_plus_w = 9 * (29 - 26)
    transform_minus_w = transform_plus_w
    assert (transform_zero, transform_plus_w, transform_minus_w) == (729, 27, 27)

    print("formal_object=integer_kernel_on_H3(3)^3_not_a_group_power_map")
    print("kernel_values=26,27,29")
    print("all_three_pair_marginals=729")
    print("value_conjugation_identities=pass")
    print("hurwitz_rotation_and_reflection=pass")
    print("selected_pairings_delta_eps_zeta=1,2,2")
    print("selected_skew_level_sizes=9,9,9")
    print("selected_fourier_blocks_zero_plus_minus=729,27,27")


if __name__ == "__main__":
    main()

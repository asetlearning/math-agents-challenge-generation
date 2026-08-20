#!/usr/bin/env python3
"""Exact bounded inventory for the double-transposition class in A_7.

No external algebra package is used.  Permutations are image tuples on 0,...,6,
and multiplication p*q means composition p after q.  The script enumerates all
7! permutations, filters A_7 by parity, independently identifies every
nonidentity involution, checks one full A_7 conjugacy orbit, and computes all
unordered-pair product orders in the class.
"""

from collections import Counter
from hashlib import sha256
from itertools import combinations, permutations


N = 7
IDENTITY = tuple(range(N))


def compose(p, q):
    return tuple(p[q[i]] for i in range(N))


def inverse(p):
    ans = [None] * N
    for i, j in enumerate(p):
        ans[j] = i
    return tuple(ans)


def is_even(p):
    inversions = sum(p[i] > p[j] for i in range(N) for j in range(i + 1, N))
    return inversions % 2 == 0


def perm_order(p):
    seen = [False] * N
    answer = 1
    for i in range(N):
        if seen[i]:
            continue
        length = 0
        j = i
        while not seen[j]:
            seen[j] = True
            length += 1
            j = p[j]
        # All orders encountered below divide 12, but use exact integer lcm.
        from math import gcd
        answer = answer * length // gcd(answer, length)
    return answer


def double_transposition(a, b, c, d):
    p = list(range(N))
    p[a], p[b] = b, a
    p[c], p[d] = d, c
    return tuple(p)


def main():
    s7 = [tuple(p) for p in permutations(range(N))]
    a7 = [p for p in s7 if is_even(p)]
    involutions = sorted(
        p for p in a7 if p != IDENTITY and compose(p, p) == IDENTITY
    )

    matchings = set()
    for support in combinations(range(N), 4):
        a, b, c, d = support
        matchings.add(double_transposition(a, b, c, d))
        matchings.add(double_transposition(a, c, b, d))
        matchings.add(double_transposition(a, d, b, c))
    vertices = sorted(matchings)

    assert len(s7) == 5040
    assert len(a7) == 2520
    assert len(vertices) == 105
    assert vertices == involutions
    assert all(is_even(x) and perm_order(x) == 2 for x in vertices)

    representative = vertices[0]
    orbit = {
        compose(compose(g, representative), inverse(g))
        for g in a7
    }
    assert orbit == set(vertices)

    edge_counts = Counter()
    valencies = [[0] * 7 for _ in vertices]
    matrix_bytes = bytearray()
    for i, a in enumerate(vertices):
        for j in range(i + 1, len(vertices)):
            t = perm_order(compose(a, vertices[j]))
            assert 0 <= t < 256
            matrix_bytes.append(t)
            edge_counts[t] += 1
            valencies[i][t] += 1
            valencies[j][t] += 1

    assert sum(edge_counts.values()) == len(vertices) * (len(vertices) - 1) // 2
    valency_profiles = Counter(tuple(row) for row in valencies)

    print("MODEL=S7 image tuples on 0..6; A7=even permutations")
    print(f"S7_ORDER={len(s7)}")
    print(f"A7_ORDER={len(a7)}")
    print("A7_ORDER_FACTORIZATION=2^3*3^2*5*7")
    print("SECOND_SMALLEST_DISTINCT_PRIME=3")
    print(f"NONIDENTITY_INVOLUTIONS_IN_A7={len(involutions)}")
    print(f"DOUBLE_TRANSPOSITION_MODEL_SIZE={len(vertices)}")
    print(f"A7_CONJUGACY_ORBIT_SIZE={len(orbit)}")
    print("SINGLE_CLASS_CHECK=PASS")
    print("UNORDERED_DISTINCT_PAIRS=" + str(sum(edge_counts.values())))
    print("COLOUR_EDGE_COUNTS=" + ",".join(f"{t}:{edge_counts[t]}" for t in sorted(edge_counts)))
    print("VALENCY_PROFILES=" + repr(dict(sorted(valency_profiles.items()))))
    print("PRODUCT_ORDER_UPPER_TRIANGLE_SHA256=" + sha256(matrix_bytes).hexdigest())
    print("INVENTORY_CHECK=PASS")


if __name__ == "__main__":
    main()

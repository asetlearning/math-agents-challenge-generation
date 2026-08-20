#!/usr/bin/env python3
"""Exact, deterministic PSL(2,8) involution product-order scheme builder.

Field elements are 3-bit coefficient vectors in F_2[x]/(x^3+x+1).
Matrices are row-major tuples (a,b,c,d).  In characteristic two the determinant
is ad+bc.  No graph-automorphism computation is performed by this program.
"""

from __future__ import annotations

import hashlib
import json
import platform
import sys
from collections import Counter, defaultdict
from pathlib import Path


MODULUS_BITS = 0b1011  # x^3+x+1
ONE = (1, 0, 0, 1)


def fadd(a: int, b: int) -> int:
    return a ^ b


def fmul(a: int, b: int) -> int:
    out = 0
    x = a
    y = b
    while y:
        if y & 1:
            out ^= x
        y >>= 1
        carry = x & 0b100
        x = (x << 1) & 0b111
        if carry:
            x ^= MODULUS_BITS & 0b111
    return out


def fpow(a: int, n: int) -> int:
    out = 1
    while n:
        if n & 1:
            out = fmul(out, a)
        a = fmul(a, a)
        n >>= 1
    return out


def finv(a: int) -> int:
    assert a != 0
    return fpow(a, 6)


def madd(x: tuple[int, ...], y: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(fadd(a, b) for a, b in zip(x, y))


def mmul(x: tuple[int, int, int, int], y: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    a, b, c, d = x
    e, f, g, h = y
    return (
        fadd(fmul(a, e), fmul(b, g)),
        fadd(fmul(a, f), fmul(b, h)),
        fadd(fmul(c, e), fmul(d, g)),
        fadd(fmul(c, f), fmul(d, h)),
    )


def mdet(x: tuple[int, int, int, int]) -> int:
    a, b, c, d = x
    return fadd(fmul(a, d), fmul(b, c))


def minv(x: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    # Every matrix used below has determinant one; minus equals plus in char 2.
    a, b, c, d = x
    return (d, b, c, a)


def order(x: tuple[int, int, int, int]) -> int:
    y = ONE
    for n in range(1, 505):
        y = mmul(y, x)
        if y == ONE:
            return n
    raise AssertionError("element order did not divide the 504-element group order")


def prime_factorization(n: int) -> dict[str, int]:
    ans: dict[str, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            ans[str(d)] = ans.get(str(d), 0) + 1
            n //= d
        d += 1
    if n > 1:
        ans[str(n)] = ans.get(str(n), 0) + 1
    return ans


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: build_psl28_scheme.py OUTPUT.json")
    out_path = Path(sys.argv[1])

    elems = list(range(8))
    add_table = [[fadd(a, b) for b in elems] for a in elems]
    mul_table = [[fmul(a, b) for b in elems] for a in elems]

    # Exhaustive finite-field checks, including all triples.
    assert all(fadd(a, 0) == a and fmul(a, 1) == a for a in elems)
    assert all(fadd(a, a) == 0 for a in elems)
    assert all(fmul(a, finv(a)) == 1 for a in elems[1:])
    assert all(fadd(fadd(a, b), c) == fadd(a, fadd(b, c)) for a in elems for b in elems for c in elems)
    assert all(fmul(fmul(a, b), c) == fmul(a, fmul(b, c)) for a in elems for b in elems for c in elems)
    assert all(fmul(a, fadd(b, c)) == fadd(fmul(a, b), fmul(a, c)) for a in elems for b in elems for c in elems)
    alpha_powers = [fpow(2, n) for n in range(7)]
    assert sorted(alpha_powers) == elems[1:]

    group = sorted(
        (a, b, c, d)
        for a in elems for b in elems for c in elems for d in elems
        if mdet((a, b, c, d)) == 1
    )
    group_set = set(group)
    assert len(group) == 504
    assert ONE in group_set
    assert all(minv(g) in group_set and mmul(g, minv(g)) == ONE for g in group)
    # Exact closure check over every ordered pair. Associativity is inherited from
    # the exhaustively checked field and the matrix multiplication formula.
    assert all(mmul(g, h) in group_set for g in group for h in group)

    involutions = sorted(g for g in group if g != ONE and mmul(g, g) == ONE)
    involution_set = set(involutions)
    assert len(involutions) == 63
    base = (1, 1, 0, 1)
    assert base in involution_set
    centralizer = sorted(g for g in group if mmul(g, base) == mmul(base, g))
    orbit = sorted({mmul(mmul(g, base), minv(g)) for g in group})
    assert len(centralizer) == 8
    assert orbit == involutions

    n = len(involutions)
    matrix = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    edges: list[list[int]] = []
    vertex_counts: list[Counter[int]] = [Counter() for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            t = order(mmul(involutions[i], involutions[j]))
            matrix[i][j] = matrix[j][i] = t
            edges.append([i, j, t])
            vertex_counts[i][t] += 1
            vertex_counts[j][t] += 1
    assert len(edges) == n * (n - 1) // 2 == 1953
    colours = sorted({t for _, _, t in edges})
    profile0 = {str(t): vertex_counts[0][t] for t in colours}
    assert all({str(t): counts[t] for t in colours} == profile0 for counts in vertex_counts)
    global_counts = Counter(t for _, _, t in edges)
    assert all(global_counts[t] * 2 == n * profile0[str(t)] for t in colours)

    # Product orders and complete matrix mutually check each other.
    assert all(matrix[i][j] == t and matrix[j][i] == t for i, j, t in edges)
    assert sum(profile0.values()) == n - 1

    result = {
        "schema": "psl28-involution-product-scheme-v1",
        "implementation": {
            "python": platform.python_version(),
            "python_implementation": platform.python_implementation(),
            "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        },
        "field": {
            "description": "F_2[x]/(x^3+x+1); integers are coefficient bit vectors",
            "modulus_bits": MODULUS_BITS,
            "elements": elems,
            "addition_table": add_table,
            "multiplication_table": mul_table,
            "alpha_integer": 2,
            "alpha_powers_n_0_through_6": alpha_powers,
            "exhaustive_field_axiom_checks": True,
        },
        "group": {
            "description": "SL(2,8), equal to PSL(2,8) because its center is trivial",
            "order": len(group),
            "order_factorization": prime_factorization(len(group)),
            "second_smallest_distinct_prime": 3,
            "members": [list(g) for g in group],
            "all_504_squared_products_closed": True,
            "all_inverses_checked": True,
        },
        "class": {
            "description": "all nonidentity elements squaring to identity",
            "size": len(involutions),
            "base_matrix": list(base),
            "base_centralizer_size": len(centralizer),
            "base_centralizer": [list(g) for g in centralizer],
            "full_conjugacy_orbit_equals_all_involutions": True,
            "vertices": [list(g) for g in involutions],
        },
        "scheme": {
            "edge_count": len(edges),
            "occurring_product_orders": colours,
            "valency_by_product_order": profile0,
            "edge_count_by_product_order": {str(t): global_counts[t] for t in colours},
            "all_vertices_have_same_profile": True,
            "edges_i_j_order": edges,
            "product_order_matrix": matrix,
        },
    }
    out_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "group_order": len(group),
        "factorization": result["group"]["order_factorization"],
        "second_smallest_distinct_prime": 3,
        "involution_count": len(involutions),
        "centralizer_size": len(centralizer),
        "orbit_equals_all_involutions": orbit == involutions,
        "edge_count": len(edges),
        "colours": colours,
        "valencies": profile0,
        "edge_counts": result["scheme"]["edge_count_by_product_order"],
        "output": str(out_path),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

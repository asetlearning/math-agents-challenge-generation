#!/usr/bin/env python3
"""Independent exact pair-orbit/order/intersection audit for 4-matchings.

Vertices are four-edge matchings on {0,...,n-1}, equivalently permutations of
cycle type 2^4 1^(n-8).  No constants from preceding runs are imported.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from collections import Counter


def perfect_matchings(points):
    points = tuple(points)
    if not points:
        yield ()
        return
    a = points[0]
    for j in range(1, len(points)):
        b = points[j]
        rest = points[1:j] + points[j + 1 :]
        for tail in perfect_matchings(rest):
            yield ((a, b),) + tail


PM8 = tuple(perfect_matchings(range(8)))
assert len(PM8) == 105


def all_matchings(n):
    for support in itertools.combinations(range(n), 8):
        for positional in PM8:
            yield tuple(sorted((support[i], support[j]) for i, j in positional))


def as_perm(matching, n):
    p = list(range(n))
    for a, b in matching:
        p[a], p[b] = b, a
    return tuple(p)


def product_order(p, q):
    # Composition p*q; its order equals the order of q*p as well.
    n = len(p)
    seen = [False] * n
    ans = 1
    for i in range(n):
        if not seen[i]:
            j = i
            length = 0
            while not seen[j]:
                seen[j] = True
                length += 1
                j = p[q[j]]
            ans = math.lcm(ans, length)
    return ans


def component_key(x, y, n):
    """Canonical coloured-union component type for ordered pair (x,y)."""
    ex = {tuple(sorted(e)) for e in x}
    ey = {tuple(sorted(e)) for e in y}
    common = ex & ey
    xs = ex - common
    ys = ey - common
    adj = [[] for _ in range(n)]
    for e in xs:
        a, b = e
        adj[a].append((b, "x"))
        adj[b].append((a, "x"))
    for e in ys:
        a, b = e
        adj[a].append((b, "y"))
        adj[b].append((a, "y"))
    seen = set()
    parts = []
    for start in range(n):
        if start in seen or not adj[start]:
            continue
        stack = [start]
        seen.add(start)
        vx = vy = 0
        vertices = []
        while stack:
            u = stack.pop()
            vertices.append(u)
            for v, colour in adj[u]:
                if u < v:
                    if colour == "x":
                        vx += 1
                    else:
                        vy += 1
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        edge_count = vx + vy
        degree2 = all(len(adj[u]) == 2 for u in vertices)
        if degree2:
            assert vx == vy
            parts.append(("C", vx))  # alternating 2*vx-cycle
        else:
            assert len(vertices) == edge_count + 1
            parts.append(("P", vx, vy))
    return (len(common), tuple(sorted(parts)))


def order_from_component_key(key):
    ans = 1
    for part in key[1]:
        if part[0] == "C":
            contribution = part[1]
        else:
            contribution = part[1] + part[2] + 1
        ans = math.lcm(ans, contribution)
    return ans


def audit(n):
    vertices = list(all_matchings(n))
    expected = math.comb(n, 8) * 105
    assert len(vertices) == expected
    perms = [as_perm(m, n) for m in vertices]
    x = ((0, 1), (2, 3), (4, 5), (6, 7))
    xi = vertices.index(x)
    px = perms[xi]

    reps = {}
    multiplicities = Counter()
    x_orders = []
    for i, y in enumerate(vertices):
        if i == xi:
            x_orders.append(1)
            continue
        key = component_key(x, y, n)
        order = product_order(px, perms[i])
        assert order == order_from_component_key(key), (n, x, y, key, order)
        x_orders.append(order)
        multiplicities[(key, order)] += 1
        reps.setdefault((key, order), i)

    assert sum(multiplicities.values()) == len(vertices) - 1

    records = []
    for (key, order), yi in sorted(reps.items(), key=lambda kv: repr(kv[0])):
        py = perms[yi]
        two_point = Counter()
        for zi, pz in enumerate(perms):
            if zi == xi or zi == yi:
                continue
            two_point[(x_orders[zi], product_order(py, pz))] += 1
        records.append(
            {
                "component_key": key,
                "common_edges": key[0],
                "order": order,
                "orbit_size": multiplicities[(key, order)],
                "representative": vertices[yi],
                "two_point_counts": [
                    [a, b, c] for (a, b), c in sorted(two_point.items())
                ],
            }
        )

    # Check whether the complete two-point colour-count vector separates each
    # stabilizer orbit among pairs having the same original colour.
    signatures = {}
    for r in records:
        sig = (r["order"], tuple(tuple(t) for t in r["two_point_counts"]))
        signatures.setdefault(sig, []).append(r["component_key"])
    collisions = [v for v in signatures.values() if len(v) > 1]
    target = [r for r in records if r["common_edges"] == 3]
    target_unique = []
    for r in target:
        sig = (r["order"], tuple(tuple(t) for t in r["two_point_counts"]))
        target_unique.append(
            {
                "component_key": r["component_key"],
                "order": r["order"],
                "signature_unique": len(signatures[sig]) == 1,
                "colliding_component_keys": signatures[sig],
            }
        )

    return {
        "n": n,
        "vertex_count": len(vertices),
        "class_formula": f"C({n},8)*105",
        "order_palette": sorted({r["order"] for r in records}),
        "pair_orbit_count": len(records),
        "pair_orbits": records,
        "signature_collision_count": len(collisions),
        "signature_collisions": collisions,
        "share_three_tests": target_unique,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("n", type=int)
    ap.add_argument("output")
    args = ap.parse_args()
    assert 8 <= args.n <= 13
    result = audit(args.n)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
        f.write("\n")
    print(
        json.dumps(
            {
                "n": result["n"],
                "vertex_count": result["vertex_count"],
                "order_palette": result["order_palette"],
                "pair_orbit_count": result["pair_orbit_count"],
                "signature_collision_count": result["signature_collision_count"],
                "share_three_tests": result["share_three_tests"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()

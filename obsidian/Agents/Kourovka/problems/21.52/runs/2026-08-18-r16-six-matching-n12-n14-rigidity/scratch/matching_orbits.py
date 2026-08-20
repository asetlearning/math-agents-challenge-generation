#!/usr/bin/env python3
"""Exact S_n-orbit inventory for pairs of six-matchings, n=12,13,14.

No prior tables/constants are used.  A pair orbit is encoded by the alternating
multigraph components of the two matchings relative to the fixed base matching.
"""

from collections import Counter
from math import gcd


def matchings(n, k=6):
    """Yield k-matchings as mate tuples (-1 means unmatched), lexicographically."""
    mate = [-1] * n

    def rec(start, left):
        if left == 0:
            yield tuple(-1 if x < 0 else x for x in mate)
            return
        free = sum(v < 0 for v in mate[start:])
        if free < 2 * left:
            return
        i = start
        while i < n and mate[i] >= 0:
            i += 1
        if i == n:
            return

        # Leave i unmatched when surplus permits.
        if free > 2 * left:
            mate[i] = -2
            yield from rec(i + 1, left)
            mate[i] = -1

        for j in range(i + 1, n):
            if mate[j] < 0:
                mate[i] = j
                mate[j] = i
                yield from rec(i + 1, left - 1)
                mate[i] = mate[j] = -1

    yield from rec(0, k)


def lcm(a, b):
    return a // gcd(a, b) * b


def pair_key_and_order(a, b):
    """Return canonical union-component key and exact order of permutation ab."""
    n = len(a)
    seen = [False] * n
    components = []
    order = 1
    common = 0
    for v in range(n):
        if seen[v] or (a[v] < 0 and b[v] < 0):
            continue
        stack = [v]
        verts = []
        edge_twice = False
        edge_count = 0
        while stack:
            u = stack.pop()
            if seen[u]:
                continue
            seen[u] = True
            verts.append(u)
            av, bv = a[u], b[u]
            if av >= 0 and av == bv and u < av:
                edge_twice = True
            for w in (av, bv):
                if w >= 0 and not seen[w]:
                    stack.append(w)
        # Count distinct coloured edges inside the component.
        edges = set()
        for u in verts:
            if a[u] >= 0:
                edges.add((min(u, a[u]), max(u, a[u]), 0))
            if b[u] >= 0:
                edges.add((min(u, b[u]), max(u, b[u]), 1))
        if edge_twice and len(verts) == 2:
            common += 1
            components.append(('d', 1))
            continue
        # No nontrivial component has repeated edges, so colour can be forgotten.
        simple_edges = {(x, y) for x, y, _ in edges}
        edge_count = len(simple_edges)
        degrees = []
        for u in verts:
            degrees.append(sum(u in e for e in simple_edges))
        is_cycle = all(d == 2 for d in degrees)
        if is_cycle:
            r = edge_count // 2
            components.append(('c', r))
            order = lcm(order, r)
        else:
            components.append(('p', edge_count))
            order = lcm(order, edge_count + 1)
    return (common, tuple(sorted(components))), order


def main():
    for n in (12, 13, 14):
        base = [-1] * n
        for i in range(0, 12, 2):
            base[i] = i + 1
            base[i + 1] = i
        base = tuple(base)
        inventory = Counter()
        reps = {}
        total = 0
        for m in matchings(n):
            total += 1
            if m == base:
                continue
            key, order = pair_key_and_order(base, m)
            full_key = (key, order)
            inventory[full_key] += 1
            reps.setdefault(full_key, m)
        print(f"n={n} vertices={total} nontrivial_pair_orbits={len(inventory)}")
        for idx, (full_key, count) in enumerate(sorted(inventory.items(), key=lambda x: repr(x[0]))):
            (common, components), order = full_key
            print(f"  orbit={idx:02d} count={count:8d} common={common} order={order:2d} components={components}")


if __name__ == '__main__':
    main()

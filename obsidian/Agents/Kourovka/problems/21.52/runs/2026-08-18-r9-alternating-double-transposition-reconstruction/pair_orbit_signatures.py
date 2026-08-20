#!/usr/bin/env python3
"""Exact pair-orbit and joint product-order counts for double transpositions."""

from collections import Counter, defaultdict, deque
from itertools import combinations


def matchings(points):
    a, b, c, d = points
    return (
        frozenset((frozenset((a, b)), frozenset((c, d)))),
        frozenset((frozenset((a, c)), frozenset((b, d)))),
        frozenset((frozenset((a, d)), frozenset((b, c)))),
    )


def vertices(m):
    return frozenset().union(*m)


def permutation(m, n):
    p = list(range(n))
    for e in m:
        a, b = tuple(e)
        p[a], p[b] = b, a
    return p


def compose(p, q):
    return [p[q[i]] for i in range(len(p))]


def order(p):
    seen = set()
    ans = 1
    for i in range(len(p)):
        if i not in seen:
            j, k = i, 0
            while j not in seen:
                seen.add(j)
                j = p[j]
                k += 1
            if k:
                from math import gcd
                ans = ans * k // gcd(ans, k)
    return ans


def pair_type(x, y):
    vx, vy = vertices(x), vertices(y)
    common_edges = len(x & y)
    graph = defaultdict(set)
    for e in x | y:
        a, b = tuple(e)
        graph[a].add(b)
        graph[b].add(a)
    components = []
    unseen = set(graph)
    while unseen:
        root = next(iter(unseen))
        todo = [root]
        comp = set()
        while todo:
            u = todo.pop()
            if u in comp:
                continue
            comp.add(u)
            todo.extend(graph[u] - comp)
        unseen -= comp
        edge_count = sum(len(graph[u]) for u in comp) // 2
        components.append((len(comp), edge_count))
    return (len(vx & vy), common_edges, tuple(sorted(components)))


def calculate(n):
    ds = [m for s in combinations(range(n), 4) for m in matchings(s)]
    perms = {m: permutation(m, n) for m in ds}
    x = matchings((0, 1, 2, 3))[0]
    representatives = {}
    for y in ds:
        if y != x:
            representatives.setdefault(pair_type(x, y), y)
    rows = []
    for typ, y in sorted(representatives.items()):
        xy = order(compose(perms[x], perms[y]))
        signature = Counter()
        for z in ds:
            if z != x and z != y:
                signature[(order(compose(perms[x], perms[z])),
                           order(compose(perms[y], perms[z])))] += 1
        rows.append((typ, xy, tuple(sorted(signature.items()))))
    return len(ds), rows


if __name__ == "__main__":
    for n in range(7, 13):
        size, rows = calculate(n)
        print(f"n={n} |D|={size}")
        for typ, colour, signature in rows:
            flat = " ".join(f"{i}{j}:{v}" for (i, j), v in signature)
            print(f"  type={typ} colour={colour} :: {flat}")

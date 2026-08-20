"""Conjecture filter only: sample colour-11 triangles around one 6-matching."""

from itertools import permutations, product
from random import Random
from collections import Counter
from math import gcd


def canon(edges):
    return tuple(sorted(tuple(sorted(e)) for e in edges))


def c11(a, b):
    common = set(a) & set(b)
    if len(common) != 1:
        return False
    rem = (set(a) | set(b)) - common
    # The ten remaining edges must form one alternating path on 11 vertices.
    adj = {}
    for u, v in rem:
        adj.setdefault(u, []).append(v)
        adj.setdefault(v, []).append(u)
    if len(adj) != 11 or sorted(map(len, adj.values())).count(1) != 2:
        return False
    if any(len(x) > 2 for x in adj.values()):
        return False
    seen = set()
    stack = [next(iter(adj))]
    while stack:
        u = stack.pop()
        if u in seen:
            continue
        seen.add(u)
        stack.extend(adj[u])
    return len(seen) == 11


def product_order(a, b, n):
    pa = list(range(n))
    pb = list(range(n))
    for u, v in a:
        pa[u], pa[v] = v, u
    for u, v in b:
        pb[u], pb[v] = v, u
    p = [pa[pb[i]] for i in range(n)]
    seen = set()
    ans = 1
    for i in range(n):
        if i in seen:
            continue
        j = i
        length = 0
        while j not in seen:
            seen.add(j)
            length += 1
            j = p[j]
        ans = ans * length // gcd(ans, length)
    return ans


def neighbours(base, n):
    out = []
    labels = []
    support = {x for e in base for x in e}
    for common in base:
        rest = [e for e in base if e != common]
        for x in range(n):
            if x in support:
                continue
            for order in permutations(rest):
                for bits in product((0, 1), repeat=5):
                    oriented = [e if bit == 0 else e[::-1]
                                for e, bit in zip(order, bits)]
                    p = [(x, oriented[0][0])]
                    p += [(oriented[i][1], oriented[i + 1][0])
                          for i in range(4)]
                    out.append(canon([common] + p))
                    labels.append(common)
    return out, labels


def main():
    n = 13
    base = canon([(0, 1), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11)])
    nbrs, labels = neighbours(base, n)
    assert len(nbrs) == 23040 and len(set(nbrs)) == len(nbrs)
    rng = Random(2152)
    trials = 2_000_000
    triangles = same = different = 0
    first_different = None
    same_orders = Counter()
    different_orders = Counter()
    for _ in range(trials):
        i = rng.randrange(len(nbrs))
        j = rng.randrange(len(nbrs))
        if i == j:
            continue
        order = product_order(nbrs[i], nbrs[j], n)
        (same_orders if labels[i] == labels[j] else different_orders)[order] += 1
        if order != 11:
            continue
        triangles += 1
        if labels[i] == labels[j]:
            same += 1
        else:
            different += 1
            if first_different is None:
                first_different = (labels[i], labels[j], nbrs[i], nbrs[j])
    print({"n": n, "degree": len(nbrs), "trials": trials,
           "triangles": triangles, "same_label": same,
           "different_label": different,
           "first_different": first_different})
    print("same-order histogram", sorted(same_orders.items()))
    print("different-order histogram", sorted(different_orders.items()))


if __name__ == "__main__":
    main()

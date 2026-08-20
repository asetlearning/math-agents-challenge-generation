#!/usr/bin/env python3
"""Write a dreadnaut input for the reconstructing relation R_n.

For n=8, R_n means exactly one common edge.  For 9<=n<=13, R_n
means exactly three common edges.  Vertices use the same canonical generation as
orbit_audit.py.  Only neighbours larger than the current index are emitted;
dreadnaut's undirected graph reader inserts the symmetric entries.
"""

from __future__ import annotations

import argparse
import itertools
import math


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


def all_matchings(n):
    for support in itertools.combinations(range(n), 8):
        for positional in PM8:
            yield tuple(sorted((support[i], support[j]) for i, j in positional))


def neighbours_share_three(m, n, index):
    out = set()
    for removed in m:
        core = tuple(e for e in m if e != removed)
        used = {u for e in core for u in e}
        available = [u for u in range(n) if u not in used]
        for a, b in itertools.combinations(available, 2):
            e = (a, b)
            if e == removed:
                continue
            candidate = tuple(sorted(core + (e,)))
            out.add(index[candidate])
    return out


def write_dre(n, path):
    vertices = list(all_matchings(n))
    assert len(vertices) == math.comb(n, 8) * 105
    index = {m: i for i, m in enumerate(vertices)}
    edge_count = 0
    expected_degree = 32 if n == 8 else 4 * (math.comb(n - 6, 2) - 1)
    with open(path, "w", encoding="ascii") as f:
        f.write("As\n")
        f.write(f"n={len(vertices)} g\n")
        if n == 8:
            sets = [set(m) for m in vertices]
            for i, a in enumerate(sets):
                all_ns = [j for j in range(len(sets)) if j != i and len(a & sets[j]) == 1]
                assert len(all_ns) == expected_degree
                ns = [j for j in all_ns if j > i]
                edge_count += len(ns)
                f.write(f"{i}: {' '.join(map(str, ns))};\n")
        else:
            for i, m in enumerate(vertices):
                all_ns = neighbours_share_three(m, n, index)
                assert len(all_ns) == expected_degree
                ns = sorted(j for j in all_ns if j > i)
                edge_count += len(ns)
                f.write(f"{i}: {' '.join(map(str, ns))};\n")
        # Explicitly print generators, orbit partition, and canonical group data.
        f.write("+a\n")
        f.write("x\n")
        f.write("o\n")
        f.write("q\n")
    assert edge_count * 2 == len(vertices) * expected_degree
    return len(vertices), expected_degree, edge_count


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("n", type=int)
    ap.add_argument("output")
    args = ap.parse_args()
    assert 8 <= args.n <= 13
    size, degree, edges = write_dre(args.n, args.output)
    print(f"n={args.n} vertices={size} degree={degree} edges={edges} output={args.output}")


if __name__ == "__main__":
    main()

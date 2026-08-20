#!/usr/bin/env python3
"""Two-point exact-colour intersection arrays for only the ambiguous colours.

For each n, compare every S_n-orbit of pairs having the same product order as
the desired sparse relation.  The output matrix for (x,y) is
  N_{r,s}(x,y) = #{z != x,y : |xz|=r and |yz|=s}.
This is intrinsic to the exact-order coloured complete graph.
"""

import argparse
from collections import Counter
import hashlib
import json
from math import gcd

from matching_orbits import matchings, pair_key_and_order


def lcm(a, b):
    return a // gcd(a, b) * b


def product_order(a, b):
    n = len(a)
    perm = [0] * n
    for v in range(n):
        w = b[v] if b[v] >= 0 else v
        perm[v] = a[w] if a[w] >= 0 else w
    seen = [False] * n
    ans = 1
    for v in range(n):
        if seen[v]:
            continue
        u = v
        length = 0
        while not seen[u]:
            seen[u] = True
            length += 1
            u = perm[u]
        ans = lcm(ans, length)
    return ans


def base_matching(n):
    ans = [-1] * n
    for i in range(0, 12, 2):
        ans[i], ans[i + 1] = i + 1, i
    return tuple(ans)


def orbit_label(key, order):
    common, comps = key
    return f"common={common};order={order};components={comps}"


def run(n, compact=False):
    base = base_matching(n)
    desired_orders = {2} if n == 12 else ({3} if n == 13 else {2, 3})
    reps = {}
    vertex_count = 0
    for m in matchings(n):
        vertex_count += 1
        if m == base:
            continue
        key, order = pair_key_and_order(base, m)
        if order in desired_orders:
            reps.setdefault((key, order), m)

    ordered = sorted(reps.items(), key=lambda item: repr(item[0]))
    arrays = [Counter() for _ in ordered]
    seen_vertices = 0
    for z in matchings(n):
        seen_vertices += 1
        ox = product_order(base, z)
        for i, ((key, order), y) in enumerate(ordered):
            if z == base or z == y:
                continue
            arrays[i][(ox, product_order(y, z))] += 1

    assert seen_vertices == vertex_count
    print(f"n={n} vertices={vertex_count} candidate_pair_orbits={len(ordered)}")
    fingerprints = {}
    records = []
    for i, (((key, order), y), arr) in enumerate(zip(ordered, arrays)):
        label = orbit_label(key, order)
        fp = tuple(sorted(arr.items()))
        fingerprints.setdefault(fp, []).append(label)
        digest_input = json.dumps([[r, s, count] for (r, s), count in fp], separators=(',', ':')).encode()
        records.append((i, label, arr, hashlib.sha256(digest_input).hexdigest(), sum(arr.values())))
        if not compact:
            print(f"PAIR {i:02d} {label}")
            print("  " + " ".join(f"{r},{s}:{count}" for (r, s), count in fp))
            print(f"  ROWSUM={sum(arr.values())}")
    print(f"distinct_fingerprints={len(fingerprints)}")
    for labels in fingerprints.values():
        if len(labels) > 1:
            print("COLLISION " + " || ".join(labels))
    if compact:
        # Greedily choose exact coordinates separating all candidate orbit arrays.
        coords = sorted(set().union(*(set(arr) for _, _, arr, _, _ in records)))
        classes = [list(range(len(records)))]
        selected = []
        while any(len(c) > 1 for c in classes):
            best = None
            best_classes = None
            best_score = len(classes)
            for coord in coords:
                if coord in selected:
                    continue
                refined = []
                for c in classes:
                    buckets = {}
                    for idx in c:
                        buckets.setdefault(records[idx][2].get(coord, 0), []).append(idx)
                    refined.extend(buckets.values())
                score = len(refined)
                if score > best_score:
                    best, best_classes, best_score = coord, refined, score
            assert best is not None
            selected.append(best)
            classes = best_classes
        print("separating_coordinates=" + repr(selected))
        for i, label, arr, digest, rowsum in records:
            values = [arr.get(coord, 0) for coord in selected]
            print(f"PAIR {i:02d} values={values} sha256={digest} rowsum={rowsum} {label}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int, choices=(12, 13, 14))
    parser.add_argument('--compact', action='store_true')
    args = parser.parse_args()
    run(args.n, args.compact)

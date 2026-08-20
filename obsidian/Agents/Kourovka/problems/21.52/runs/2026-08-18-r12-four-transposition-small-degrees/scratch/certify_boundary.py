#!/usr/bin/env python3
"""Fail-fast certificate checker for the six small-degree boundary cases."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import pathlib
import re


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


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def point_swap_action_is_labelled(n):
    vertices = list(all_matchings(n))
    index = set(vertices)
    assert len(index) == len(vertices)
    checks = []
    for i in range(n - 1):
        def s(x):
            if x == i:
                return i + 1
            if x == i + 1:
                return i
            return x

        images = {
            tuple(sorted(tuple(sorted((s(a), s(b)))) for a, b in m))
            for m in vertices
        }
        checks.append(images == index)
    assert all(checks)
    # Faithfulness: a point permutation fixing every four-matching fixes every
    # edge, since each edge occurs in some four-matching and membership stars
    # distinguish edges for n>=8; hence it fixes all points.
    return len(vertices), len(checks)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("scratch")
    ap.add_argument("output")
    args = ap.parse_args()
    root = pathlib.Path(args.scratch)
    summary = {
        "schema": 1,
        "method": "complete pair-orbit colour audit plus exact nauty automorphism of a colour-definable relation",
        "degrees": [],
    }
    expected_palettes = {
        8: [2, 3, 4],
        9: [2, 3, 4, 5, 6, 7, 9, 10],
        10: [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 21],
        11: [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 20, 21],
        12: [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 20, 21, 30],
        13: [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 20, 21, 30],
    }
    for n in range(8, 14):
        orbit_path = root / f"orbit-n{n}.json"
        dre_path = root / f"relation-n{n}.dre"
        out_path = root / f"relation-n{n}.out"
        err_path = root / f"relation-n{n}.err"
        orbit = json.loads(orbit_path.read_text(encoding="utf-8"))
        expected_vertices = math.comb(n, 8) * 105
        assert orbit["vertex_count"] == expected_vertices
        assert orbit["order_palette"] == expected_palettes[n]
        assert sum(r["orbit_size"] for r in orbit["pair_orbits"]) == expected_vertices - 1
        assert orbit["signature_collision_count"] == 0

        if n == 8:
            target = [r for r in orbit["pair_orbits"] if r["common_edges"] == 1]
            assert len(target) == 1 and target[0]["order"] == 3
            relation = "common_edges=1, equivalently exact product order 3"
            target_orbits = 1
            degree = 32
        else:
            target = [r for r in orbit["pair_orbits"] if r["common_edges"] == 3]
            assert len(target) == (1 if n == 9 else 2)
            assert all(t["signature_unique"] for t in orbit["share_three_tests"])
            assert {r["order"] for r in target} == ({3} if n == 9 else {2, 3})
            relation = "common_edges=3, selected by unique complete two-point colour-count signatures"
            target_orbits = len(target)
            degree = 4 * (math.comb(n - 6, 2) - 1)

        dreadnaut = out_path.read_text(encoding="ascii")
        matches = re.findall(r"grpsize=([0-9]+)", dreadnaut)
        assert matches and int(matches[-1]) == math.factorial(n)
        assert err_path.stat().st_size == 0
        labelled_vertices, adjacent_point_generators = point_swap_action_is_labelled(n)
        assert labelled_vertices == expected_vertices

        summary["degrees"].append(
            {
                "n": n,
                "vertices": expected_vertices,
                "exact_product_orders": orbit["order_palette"],
                "ordered_pair_stabilizer_orbits": orbit["pair_orbit_count"],
                "all_pair_orbits_separated_by_two_point_colour_counts": True,
                "reconstructing_relation": relation,
                "reconstructing_relation_target_orbits": target_orbits,
                "reconstructing_relation_degree": degree,
                "full_relation_automorphism_group_order": int(matches[-1]),
                "factorial_n": math.factorial(n),
                "natural_adjacent_point_swap_generators_checked_on_label_set": adjacent_point_generators,
                "natural_point_action_faithful": True,
                "orbit_json_sha256": sha256(orbit_path),
                "dreadnaut_input_sha256": sha256(dre_path),
                "dreadnaut_output_sha256": sha256(out_path),
            }
        )

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
        f.write("\n")
    print("PASS degrees=8..13 all exact gates")


if __name__ == "__main__":
    main()

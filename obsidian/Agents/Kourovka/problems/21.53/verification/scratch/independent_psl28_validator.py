#!/usr/bin/env python3
"""Independent bounded certificate checker for the fixed PSL(2,8) claim.

The field multiplication is implemented by coefficient convolution and polynomial
reduction, independently of the claimant's bit-shift implementation.  The complete
two-colour automorphism group is enumerated by the nine-block/perfect-matching
structure, without GAP, GRAPE, nauty, or the claimant's automorphism wrapper.
"""

from __future__ import annotations

import ast
import hashlib
import itertools
import json
import re
import sys
from collections import Counter, deque
from pathlib import Path


def fadd_tuple(x: tuple[int, int, int], y: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(a ^ b for a, b in zip(x, y))  # type: ignore[return-value]


def fmul_tuple(x: tuple[int, int, int], y: tuple[int, int, int]) -> tuple[int, int, int]:
    # Convolution, followed by x^d = x^(d-2) + x^(d-3), from x^3=x+1.
    c = [0] * 5
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            c[i + j] ^= a & b
    for d in (4, 3):
        if c[d]:
            c[d] = 0
            c[d - 2] ^= 1
            c[d - 3] ^= 1
    return c[0], c[1], c[2]


def as_tuple(n: int) -> tuple[int, int, int]:
    return n & 1, (n >> 1) & 1, (n >> 2) & 1


ELEMENTS = tuple(range(8))
ADD = tuple(tuple(int("".join(str(b) for b in reversed(fadd_tuple(as_tuple(x), as_tuple(y)))), 2)
                  for y in ELEMENTS) for x in ELEMENTS)
MUL = tuple(tuple(int("".join(str(b) for b in reversed(fmul_tuple(as_tuple(x), as_tuple(y)))), 2)
                  for y in ELEMENTS) for x in ELEMENTS)


Matrix = tuple[int, int, int, int]


def madd(x: int, y: int) -> int:
    return ADD[x][y]


def mmul(x: Matrix, y: Matrix) -> Matrix:
    a, b, c, d = x
    e, f, g, h = y
    return (
        madd(MUL[a][e], MUL[b][g]),
        madd(MUL[a][f], MUL[b][h]),
        madd(MUL[c][e], MUL[d][g]),
        madd(MUL[c][f], MUL[d][h]),
    )


IDENTITY: Matrix = (1, 0, 0, 1)


def minv(x: Matrix) -> Matrix:
    a, b, c, d = x
    return d, b, c, a


def det(x: Matrix) -> int:
    a, b, c, d = x
    return madd(MUL[a][d], MUL[b][c])


def element_order(x: Matrix) -> int:
    y = IDENTITY
    for n in range(1, 505):
        y = mmul(y, x)
        if y == IDENTITY:
            return n
    raise AssertionError("element order did not divide the finite group bound")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def components_for_relation(matrix: list[list[int]], colour: int) -> list[list[int]]:
    unseen = set(range(len(matrix)))
    components: list[list[int]] = []
    while unseen:
        root = min(unseen)
        comp = []
        queue = [root]
        unseen.remove(root)
        while queue:
            u = queue.pop()
            comp.append(u)
            neighbours = [v for v in list(unseen) if matrix[u][v] == colour]
            for v in neighbours:
                unseen.remove(v)
                queue.append(v)
        components.append(sorted(comp))
    return sorted(components)


def enumerate_two_colour_automorphisms(matrix: list[list[int]]) -> tuple[list[tuple[int, ...]], list[int]]:
    """Enumerate Aut(R2,R3) from its K7-block and matching decomposition.

    Every R2-automorphism permutes its connected components.  Once the image of
    component 0 and the bijection on that component are fixed, R3 preservation
    uniquely forces the bijection on every other component.  The recursion checks
    all remaining inter-component R3 matchings, so the enumeration is exhaustive.
    """
    components = components_for_relation(matrix, 2)
    assert len(components) == 9 and all(len(c) == 7 for c in components)
    assert all(matrix[u][v] == 2 for comp in components for u, v in itertools.combinations(comp, 2))

    local = [{vertex: i for i, vertex in enumerate(comp)} for comp in components]
    match: list[list[tuple[int, ...] | None]] = [[None] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if i == j:
                continue
            row = []
            for u in components[i]:
                hits = [local[j][v] for v in components[j] if matrix[u][v] == 3]
                assert len(hits) == 1
                row.append(hits[0])
            assert sorted(row) == list(range(7))
            match[i][j] = tuple(row)

    automorphisms: list[tuple[int, ...]] = []
    depth_nodes = [0] * 10
    source_order = list(range(1, 9))

    def compatible(i: int, j: int, sigma: list[int | None], fibre_maps: list[tuple[int, ...] | None]) -> bool:
        si, sj = sigma[i], sigma[j]
        fi, fj = fibre_maps[i], fibre_maps[j]
        assert si is not None and sj is not None and fi is not None and fj is not None
        mij = match[i][j]
        mt = match[si][sj]
        assert mij is not None and mt is not None
        return all(fj[mij[u]] == mt[fi[u]] for u in range(7))

    def finish(sigma: list[int | None], fibre_maps: list[tuple[int, ...] | None]) -> None:
        image = [0] * 63
        for i in range(9):
            si, fi = sigma[i], fibre_maps[i]
            assert si is not None and fi is not None
            for u, vertex in enumerate(components[i]):
                image[vertex] = components[si][fi[u]]
        automorphisms.append(tuple(image))

    def recurse(depth: int, sigma: list[int | None], fibre_maps: list[tuple[int, ...] | None], used: set[int]) -> None:
        depth_nodes[depth] += 1
        if depth == 8:
            finish(sigma, fibre_maps)
            return
        i = source_order[depth]
        a0 = sigma[0]
        f0 = fibre_maps[0]
        assert a0 is not None and f0 is not None
        mi0 = match[i][0]
        assert mi0 is not None
        for target in range(9):
            if target in used:
                continue
            mt = match[a0][target]
            assert mt is not None
            fi = tuple(mt[f0[mi0[u]]] for u in range(7))
            sigma[i] = target
            fibre_maps[i] = fi
            if all(compatible(i, j, sigma, fibre_maps) for j in range(1, i)):
                used.add(target)
                recurse(depth + 1, sigma, fibre_maps, used)
                used.remove(target)
            sigma[i] = None
            fibre_maps[i] = None

    for target0 in range(9):
        for f0 in itertools.permutations(range(7)):
            sigma: list[int | None] = [None] * 9
            fibre_maps: list[tuple[int, ...] | None] = [None] * 9
            sigma[0] = target0
            fibre_maps[0] = f0
            recurse(0, sigma, fibre_maps, {target0})

    assert len(automorphisms) == len(set(automorphisms))
    return automorphisms, depth_nodes


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(q[p[i]] for i in range(len(p)))


def generated_group(generators: list[tuple[int, ...]]) -> set[tuple[int, ...]]:
    identity = tuple(range(len(generators[0])))
    seen = {identity}
    queue = deque([identity])
    while queue:
        p = queue.popleft()
        for g in generators:
            h = compose(p, g)
            if h not in seen:
                seen.add(h)
                queue.append(h)
    return seen


def preserves(matrix: list[list[int]], p: tuple[int, ...], colours: set[int] | None) -> bool:
    for i in range(62):
        for j in range(i + 1, 63):
            old = matrix[i][j]
            new = matrix[p[i]][p[j]]
            if colours is None:
                if old != new:
                    return False
            elif old in colours and new != old:
                return False
    return True


def parse_gap_assignment(text: str, name: str, next_name: str) -> object:
    pattern = rf"{re.escape(name)} := (.*?);;\s*{re.escape(next_name)} :="
    match = re.search(pattern, text, flags=re.S)
    assert match is not None
    return ast.literal_eval(match.group(1))


def main(argv: list[str]) -> None:
    if len(argv) != 8:
        raise SystemExit(
            "usage: independent_psl28_validator.py SCHEME SUMMARY RAW GENERATED WRAPPER BUILDER MANIFEST"
        )
    scheme_path, summary_path, raw_path, generated_path, wrapper_path, builder_path, manifest_path = map(Path, argv[1:])

    # Field audit, from coefficient arithmetic rather than the supplied tables.
    field_associative = all(MUL[MUL[x][y]][z] == MUL[x][MUL[y][z]] for x in ELEMENTS for y in ELEMENTS for z in ELEMENTS)
    field_distributive = all(
        MUL[x][ADD[y][z]] == ADD[MUL[x][y]][MUL[x][z]]
        and MUL[ADD[y][z]][x] == ADD[MUL[y][x]][MUL[z][x]]
        for x in ELEMENTS for y in ELEMENTS for z in ELEMENTS
    )
    inverse_counts = [sum(MUL[x][y] == 1 for y in range(1, 8)) for x in range(1, 8)]
    assert field_associative and field_distributive and inverse_counts == [1] * 7
    alpha_powers = [1]
    for _ in range(6):
        alpha_powers.append(MUL[alpha_powers[-1]][2])
    assert alpha_powers == [1, 2, 4, 3, 6, 7, 5]

    # Entire determinant-one matrix group.
    group = sorted(
        (a, b, c, d)
        for a in ELEMENTS for b in ELEMENTS for c in ELEMENTS for d in ELEMENTS
        if det((a, b, c, d)) == 1
    )
    group_set = set(group)
    assert len(group) == 504
    assert all(mmul(x, y) in group_set for x in group for y in group)
    assert all(mmul(x, minv(x)) == IDENTITY == mmul(minv(x), x) for x in group)
    center = [x for x in group if all(mmul(x, y) == mmul(y, x) for y in group)]
    noncommuting_pair = next((x, y) for x in group for y in group if mmul(x, y) != mmul(y, x))
    assert center == [IDENTITY]

    involutions = sorted(x for x in group if x != IDENTITY and mmul(x, x) == IDENTITY)
    base = (1, 1, 0, 1)
    centralizer = [x for x in group if mmul(x, base) == mmul(base, x)]
    orbit = {mmul(mmul(minv(x), base), x) for x in group}
    assert len(involutions) == 63 and len(centralizer) == 8 and orbit == set(involutions)

    matrix = [[1] * 63 for _ in range(63)]
    edge_counts: Counter[int] = Counter()
    profiles: list[Counter[int]] = [Counter() for _ in range(63)]
    edges = []
    for i in range(62):
        for j in range(i + 1, 63):
            order = element_order(mmul(involutions[i], involutions[j]))
            matrix[i][j] = matrix[j][i] = order
            edge_counts[order] += 1
            profiles[i][order] += 1
            profiles[j][order] += 1
            edges.append([i, j, order])
    assert edge_counts == Counter({7: 756, 9: 756, 3: 252, 2: 189})
    assert all(profile == Counter({7: 24, 9: 24, 3: 8, 2: 6}) for profile in profiles)

    # Compare every mathematical payload in the claimant's scheme certificate.
    scheme = json.loads(scheme_path.read_text(encoding="utf-8"))
    scheme_payload_matches = (
        scheme["field"]["addition_table"] == [list(row) for row in ADD]
        and scheme["field"]["multiplication_table"] == [list(row) for row in MUL]
        and scheme["group"]["members"] == [list(x) for x in group]
        and scheme["class"]["vertices"] == [list(x) for x in involutions]
        and scheme["scheme"]["product_order_matrix"] == matrix
        and scheme["scheme"]["edges_i_j_order"] == edges
    )
    assert scheme_payload_matches

    # Independent complete enumeration of Aut(R2,R3), with no graph package.
    two_auts, depth_nodes = enumerate_two_colour_automorphisms(matrix)
    two_aut_set = set(two_auts)
    all_two_preserve_full = all(preserves(matrix, p, None) for p in two_auts)
    assert len(two_auts) == 1512 and all_two_preserve_full

    # Claimant artifact hashes, raw tags, generated payload, and generators.
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    raw = raw_path.read_text(encoding="utf-8")
    generated = generated_path.read_text(encoding="utf-8")
    actual_hashes = {
        "scheme": sha256(scheme_path),
        "summary": sha256(summary_path),
        "raw": sha256(raw_path),
        "generated": sha256(generated_path),
        "wrapper": sha256(wrapper_path),
        "builder": sha256(builder_path),
        "manifest": sha256(manifest_path),
    }
    expected_hashes = {
        "scheme": "54bb450db146199b72e51b2e18b4b2b507075d50725cc0556f5293291a5f2e90",
        "summary": "b88ae158725d2d997ad001e2579eaca94cbe1e6f1783470ef8e1600526505d54",
        "raw": "0c268fba97c75346c137355ec0bfa5f2d2da413a663496e8899175b578975c57",
        "generated": "4f79a301543cb8dd4182c841d162a3447867d87b88fa4fa2d5aa8c1f9263521e",
        "wrapper": "3f96ab5def2a55fe273191e1abf9e99235705f095f01f08640e944eb8d5f6ff0",
        "builder": "f75ad5500924cef6164fc651273ac69d23be87b0ff8c678c28366055177c81ea",
        "manifest": "e3c5f8454e3c255a2d05f6add3d09fd1edef2ce7812aee7497f530fd2a0a71bc",
    }
    assert actual_hashes == expected_hashes
    assert summary["input_scheme_sha256"] == actual_hashes["scheme"]
    assert summary["raw_output_sha256"] == actual_hashes["raw"]
    assert summary["generated_gap_sha256"] == actual_hashes["generated"]
    assert summary["wrapper_sha256"] == actual_hashes["wrapper"]
    assert "returncode=0" in raw and raw.count("@@") == 13 and raw.endswith("--- stderr ---\n")

    generated_matrix = parse_gap_assignment(generated, "M", "Edges2")
    generated_edges2 = parse_gap_assignment(generated, "Edges2", "Edges3")
    generated_edges3 = parse_gap_assignment(generated, "Edges3", "Edges7")
    generated_edges7 = parse_gap_assignment(generated, "Edges7", "Edges9")
    generated_edges9 = parse_gap_assignment(generated, "Edges9", "BuildIncidence")
    expected_by_colour = {
        t: [[i + 1, j + 1] for i, j, u in edges if u == t] for t in (2, 3, 7, 9)
    }
    generated_payload_matches = (
        generated_matrix == matrix
        and generated_edges2 == expected_by_colour[2]
        and generated_edges3 == expected_by_colour[3]
        and generated_edges7 == expected_by_colour[7]
        and generated_edges9 == expected_by_colour[9]
    )
    encoding_fragments = all(
        fragment in generated
        for fragment in (
            "cells := [[1..NOriginal]];",
            "return rec(graph := gamma, colourClasses := cells);",
            "TwoGraph := BuildIncidence([Edges2, Edges3]);;",
            "FullGraph := BuildIncidence([Edges2, Edges3, Edges7, Edges9]);;",
            "TwoIncidenceGroup := AutGroupGraph(TwoGraph);;",
            "FullIncidenceGroup := AutGroupGraph(FullGraph);;",
        )
    )
    assert generated_payload_matches and encoding_fragments

    def normalize_generators(rows: list[list[int]]) -> list[tuple[int, ...]]:
        result = [tuple(x - 1 for x in row) for row in rows]
        assert all(sorted(p) == list(range(63)) for p in result)
        return result

    two_generators = normalize_generators(summary["two_generators"])
    full_generators = normalize_generators(summary["full_generators"])
    assert all(preserves(matrix, p, {2, 3}) for p in two_generators)
    assert all(preserves(matrix, p, None) for p in full_generators)
    # Equality predicts the displayed two-colour generators preserve all colours too.
    assert all(preserves(matrix, p, None) for p in two_generators)
    claimed_two_group = generated_group(two_generators)
    claimed_full_group = generated_group(full_generators)
    assert claimed_two_group == claimed_full_group == two_aut_set

    components = components_for_relation(matrix, 2)
    canonical_aut_hash = hashlib.sha256(
        json.dumps([list(p) for p in sorted(two_aut_set)], separators=(",", ":")).encode()
    ).hexdigest()
    matrix_hash = hashlib.sha256(json.dumps(matrix, separators=(",", ":")).encode()).hexdigest()

    output = {
        "software": {"python": sys.version.split()[0], "method": "coefficient-field plus block-matching backtracker"},
        "field": {
            "associative": field_associative,
            "distributive": field_distributive,
            "one_inverse_each_nonzero": inverse_counts == [1] * 7,
            "alpha_powers": alpha_powers,
        },
        "group": {
            "order": len(group),
            "closed_all_ordered_products": True,
            "all_inverses": True,
            "center_size": len(center),
            "nonabelian_witness": [list(noncommuting_pair[0]), list(noncommuting_pair[1])],
        },
        "class": {
            "involutions": len(involutions),
            "centralizer_size": len(centralizer),
            "orbit_size": len(orbit),
            "orbit_equals_all_involutions": orbit == set(involutions),
        },
        "prime": {"factorization": "504=2^3*3^2*7", "second_smallest_distinct": 3},
        "scheme": {
            "colours": sorted(edge_counts),
            "edge_counts": {str(k): edge_counts[k] for k in sorted(edge_counts)},
            "valencies": {"2": 6, "3": 8, "7": 24, "9": 24},
            "matrix_compact_sha256": matrix_hash,
            "claimant_payload_exact_match": scheme_payload_matches,
        },
        "two_colour_structure": {
            "order2_components": len(components),
            "component_sizes": [len(c) for c in components],
            "order3_between_each_block_pair": "perfect matching",
            "backtrack_nodes_by_depth": depth_nodes,
            "automorphism_count": len(two_auts),
            "all_preserve_full_product_matrix": all_two_preserve_full,
            "canonical_automorphism_set_sha256": canonical_aut_hash,
        },
        "claimant_artifacts": {
            "hashes_match_log": actual_hashes == expected_hashes,
            "hashes": actual_hashes,
            "raw_returncode_zero_and_13_tags": "returncode=0" in raw and raw.count("@@") == 13,
            "generated_matrix_and_edges_exact": generated_payload_matches,
            "incidence_encoding_fragments_present": encoding_fragments,
            "two_generator_count": len(two_generators),
            "full_generator_count": len(full_generators),
            "two_generated_order": len(claimed_two_group),
            "full_generated_order": len(claimed_full_group),
            "generator_groups_equal_independent_aut_set": claimed_two_group == claimed_full_group == two_aut_set,
        },
        "verdict_for_fixed_pair": "Aut(Gamma)=Aut_2(Gamma) intersect Aut_3(Gamma), common order 1512",
        "active_assignment_answered": False,
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main(sys.argv)

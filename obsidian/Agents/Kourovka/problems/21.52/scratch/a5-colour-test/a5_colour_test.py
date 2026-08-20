#!/usr/bin/env python3
"""Exact A5 involution-class product-order colour-automorphism test.

This is a bounded, dependency-free certificate generator.  It constructs A5 as
the even permutations of five points, constructs its full involution class,
enumerates every colour-preserving permutation of that class by exhaustive
backtracking, and independently enumerates every automorphism of A5 from the
possible images of a fixed generating pair.

Permutation convention: p*q means p after q, so (p*q)[i] = p[q[i]].
All permutations stored in the JSON certificate use one-based image lists.
"""

from __future__ import annotations

import argparse
from collections import Counter, deque
import hashlib
import itertools
import json
from pathlib import Path
from typing import Iterable, Sequence


Perm = tuple[int, ...]
DEGREE = 5
IDENTITY: Perm = tuple(range(DEGREE))


def compose(left: Perm, right: Perm) -> Perm:
    """Return left after right."""
    return tuple(left[right[i]] for i in range(len(left)))


def inverse(perm: Perm) -> Perm:
    result = [0] * len(perm)
    for i, image in enumerate(perm):
        result[image] = i
    return tuple(result)


def parity(perm: Perm) -> int:
    return sum(perm[i] > perm[j] for i in range(len(perm))
               for j in range(i + 1, len(perm))) % 2


def element_order(perm: Perm) -> int:
    power = IDENTITY
    for exponent in range(1, 61):
        power = compose(power, perm)
        if power == IDENTITY:
            return exponent
    raise AssertionError("permutation order exceeded 60")


def cycle_notation(perm: Perm) -> str:
    seen: set[int] = set()
    cycles: list[str] = []
    for start in range(len(perm)):
        if start in seen or perm[start] == start:
            seen.add(start)
            continue
        cycle: list[int] = []
        point = start
        while point not in seen:
            seen.add(point)
            cycle.append(point + 1)
            point = perm[point]
        cycles.append("(" + " ".join(map(str, cycle)) + ")")
    return "".join(cycles) if cycles else "()"


def generated_subgroup(generators: Sequence[Perm]) -> set[Perm]:
    steps = tuple(generators) + tuple(inverse(g) for g in generators)
    seen = {IDENTITY}
    queue = deque([IDENTITY])
    while queue:
        current = queue.popleft()
        for step in steps:
            nxt = compose(current, step)
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return seen


def edge_colour_matrix(vertices: Sequence[Perm]) -> list[list[int]]:
    size = len(vertices)
    matrix = [[1 if i == j else 0 for j in range(size)]
              for i in range(size)]
    for i in range(size):
        for j in range(i + 1, size):
            colour = element_order(compose(vertices[i], vertices[j]))
            matrix[i][j] = colour
            matrix[j][i] = colour
    return matrix


def enumerate_colour_automorphisms(
    matrix: Sequence[Sequence[int]],
) -> tuple[list[Perm], int]:
    """Enumerate all matrix-preserving permutations, with no group assumptions."""
    size = len(matrix)
    signatures = []
    for i in range(size):
        counts = Counter(matrix[i][j] for j in range(size) if i != j)
        signatures.append(tuple(sorted(counts.items())))

    image: dict[int, int] = {}
    used: set[int] = set()
    answers: list[Perm] = []
    search_nodes = 0

    def candidates(source: int) -> list[int]:
        possible = []
        for target in range(size):
            if target in used or signatures[source] != signatures[target]:
                continue
            if all(matrix[source][old_source] == matrix[target][old_target]
                   for old_source, old_target in image.items()):
                possible.append(target)
        return possible

    def visit() -> None:
        nonlocal search_nodes
        search_nodes += 1
        if len(image) == size:
            answer = tuple(image[i] for i in range(size))
            assert len(set(answer)) == size
            assert all(matrix[i][j] == matrix[answer[i]][answer[j]]
                       for i in range(size) for j in range(size))
            answers.append(answer)
            return

        choices = []
        for source in range(size):
            if source not in image:
                possible = candidates(source)
                choices.append((len(possible), source, possible))
        _, source, possible = min(choices)
        for target in possible:
            image[source] = target
            used.add(target)
            visit()
            used.remove(target)
            del image[source]

    visit()
    answers.sort()
    assert len(answers) == len(set(answers))
    return answers, search_nodes


def extend_generator_images(
    domain_steps: Sequence[Perm],
    image_steps: Sequence[Perm],
    group: Sequence[Perm],
) -> dict[Perm, Perm] | None:
    """Extend images along the full labelled Cayley graph, rejecting conflicts."""
    mapping: dict[Perm, Perm] = {IDENTITY: IDENTITY}
    queue = deque([IDENTITY])
    while queue:
        current = queue.popleft()
        current_image = mapping[current]
        for domain_step, image_step in zip(domain_steps, image_steps):
            nxt = compose(current, domain_step)
            nxt_image = compose(current_image, image_step)
            if nxt in mapping:
                if mapping[nxt] != nxt_image:
                    return None
            else:
                mapping[nxt] = nxt_image
                queue.append(nxt)
    if len(mapping) != len(group):
        raise AssertionError("fixed domain steps do not generate the whole group")
    return mapping


def enumerate_a5_automorphisms(
    group: Sequence[Perm], generator_a: Perm, generator_b: Perm
) -> tuple[list[tuple[int, ...]], int]:
    """Test all |A5|^2 possible image pairs for a fixed generating pair."""
    group_index = {element: i for i, element in enumerate(group)}
    domain_steps = (
        generator_a,
        generator_b,
        inverse(generator_a),
        inverse(generator_b),
    )
    automorphisms: set[tuple[int, ...]] = set()
    tested = 0
    for image_a in group:
        for image_b in group:
            tested += 1
            image_steps = (
                image_a,
                image_b,
                inverse(image_a),
                inverse(image_b),
            )
            mapping = extend_generator_images(
                domain_steps, image_steps, group
            )
            if mapping is None:
                continue
            if len(set(mapping.values())) != len(group):
                continue
            if not all(
                mapping[compose(x, y)] == compose(mapping[x], mapping[y])
                for x in group for y in group
            ):
                continue
            automorphisms.add(tuple(group_index[mapping[x]] for x in group))
    return sorted(automorphisms), tested


def one_based(perm: Sequence[int]) -> list[int]:
    return [value + 1 for value in perm]


def canonical_digest(payload: object) -> str:
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")
    return hashlib.sha256(encoded).hexdigest()


def build_certificate(script_path: Path) -> dict[str, object]:
    all_s5 = sorted(tuple(p) for p in itertools.permutations(range(DEGREE)))
    a5 = [p for p in all_s5 if parity(p) == 0]
    a5_index = {element: i for i, element in enumerate(a5)}
    assert len(all_s5) == 120
    assert len(a5) == 60
    assert all(compose(x, y) in a5_index for x in a5 for y in a5)

    involutions = [element for element in a5 if element_order(element) == 2]
    involution_index = {element: i for i, element in enumerate(involutions)}
    assert len(involutions) == 15

    # A fixed generating pair: (1 2 3) and (1 2 3 4 5).
    generator_a: Perm = (1, 2, 0, 3, 4)
    generator_b: Perm = (1, 2, 3, 4, 0)
    generated = generated_subgroup((generator_a, generator_b))
    assert generated == set(a5)

    matrix = edge_colour_matrix(involutions)
    edge_classes: dict[str, list[list[int]]] = {}
    for i in range(len(involutions)):
        for j in range(i + 1, len(involutions)):
            edge_classes.setdefault(str(matrix[i][j]), []).append([i + 1, j + 1])

    colour_automorphisms, colour_search_nodes = (
        enumerate_colour_automorphisms(matrix)
    )

    a5_automorphisms, image_pairs_tested = enumerate_a5_automorphisms(
        a5, generator_a, generator_b
    )
    restriction_image: set[Perm] = set()
    for automorphism in a5_automorphisms:
        restriction = []
        for involution in involutions:
            image_element = a5[automorphism[a5_index[involution]]]
            if image_element not in involution_index:
                raise AssertionError("group automorphism did not preserve involutions")
            restriction.append(involution_index[image_element])
        restriction_image.add(tuple(restriction))

    # Separate construction: conjugation by every element of S5.
    s5_conjugation_image: set[Perm] = set()
    for conjugator in all_s5:
        conjugator_inverse = inverse(conjugator)
        restriction = []
        for involution in involutions:
            image_element = compose(
                compose(conjugator, involution), conjugator_inverse
            )
            if image_element not in involution_index:
                raise AssertionError("S5 conjugation did not preserve the class")
            restriction.append(involution_index[image_element])
        s5_conjugation_image.add(tuple(restriction))

    colour_set = set(colour_automorphisms)
    restriction_only = sorted(restriction_image - colour_set)
    colour_only = sorted(colour_set - restriction_image)
    if colour_only:
        relation = "strict_containment_counterexample"
        separating = one_based(colour_only[0])
    elif restriction_only:
        relation = "internal_consistency_failure"
        separating = None
    else:
        relation = "equality_for_A5"
        separating = None

    script_hash = hashlib.sha256(script_path.read_bytes()).hexdigest()
    certificate: dict[str, object] = {
        "schema": "kourovka-21.52-a5-colour-certificate-v1",
        "script_sha256": script_hash,
        "conventions": {
            "base_points": [1, 2, 3, 4, 5],
            "permutation_storage": "one-based image lists",
            "multiplication": "left after right",
            "vertex_indices": "one through fifteen in lexicographic one-line order",
            "matrix_diagonal": "1 is a placeholder; only distinct pairs are edges",
        },
        "group": {
            "name": "A5 as all even permutations of five points",
            "order": len(a5),
            "elements": [
                {
                    "index": i + 1,
                    "images": one_based(element),
                    "cycles": cycle_notation(element),
                    "order": element_order(element),
                }
                for i, element in enumerate(a5)
            ],
            "fixed_generators": {
                "a": {
                    "images": one_based(generator_a),
                    "cycles": cycle_notation(generator_a),
                },
                "b": {
                    "images": one_based(generator_b),
                    "cycles": cycle_notation(generator_b),
                },
                "generated_subgroup_order": len(generated),
            },
        },
        "involution_class": {
            "size": len(involutions),
            "vertices": [
                {
                    "vertex": i + 1,
                    "a5_element_index": a5_index[element] + 1,
                    "images": one_based(element),
                    "cycles": cycle_notation(element),
                    "order": element_order(element),
                }
                for i, element in enumerate(involutions)
            ],
        },
        "complete_product_order_colouring": {
            "matrix": matrix,
            "edge_colour_classes": edge_classes,
            "edge_colour_set": sorted(int(colour) for colour in edge_classes),
            "edge_count": sum(len(edges) for edges in edge_classes.values()),
            "per_vertex_colour_degrees": [
                dict(sorted(Counter(
                    matrix[i][j] for j in range(len(involutions)) if i != j
                ).items()))
                for i in range(len(involutions))
            ],
        },
        "full_colour_automorphism_group": {
            "order": len(colour_automorphisms),
            "exhaustive_backtracking_nodes": colour_search_nodes,
            "elements_on_vertices": [one_based(p) for p in colour_automorphisms],
            "completeness_method": (
                "exhaustive injective vertex-image backtracking; at every node all "
                "unused targets compatible with every already mapped edge colour "
                "are tried"
            ),
        },
        "full_A5_automorphism_enumeration": {
            "candidate_generator_image_pairs_tested": image_pairs_tested,
            "automorphism_order": len(a5_automorphisms),
            "automorphisms_on_A5_elements": [
                one_based(p) for p in a5_automorphisms
            ],
            "restriction_image_order": len(restriction_image),
            "restriction_image_on_vertices": [
                one_based(p) for p in sorted(restriction_image)
            ],
            "completeness_method": (
                "the fixed pair generates A5; all 60^2 image pairs are extended "
                "through the labelled Cayley graph and every accepted bijection "
                "is checked on all 60^2 products"
            ),
        },
        "independent_S5_conjugation_image": {
            "conjugators_tested": len(all_s5),
            "restriction_image_order": len(s5_conjugation_image),
            "restriction_image_on_vertices": [
                one_based(p) for p in sorted(s5_conjugation_image)
            ],
            "equals_direct_A5_automorphism_restriction": (
                s5_conjugation_image == restriction_image
            ),
        },
        "comparison": {
            "relation": relation,
            "colour_automorphisms_outside_restriction_count": len(colour_only),
            "restriction_elements_outside_colour_group_count": len(restriction_only),
            "lexicographically_first_separating_permutation": separating,
        },
    }
    certificate["certificate_sha256"] = canonical_digest(certificate)
    return certificate


def summary_lines(certificate: dict[str, object]) -> list[str]:
    group = certificate["group"]
    involutions = certificate["involution_class"]
    colouring = certificate["complete_product_order_colouring"]
    colour_group = certificate["full_colour_automorphism_group"]
    aut_group = certificate["full_A5_automorphism_enumeration"]
    s5_image = certificate["independent_S5_conjugation_image"]
    comparison = certificate["comparison"]
    assert isinstance(group, dict)
    assert isinstance(involutions, dict)
    assert isinstance(colouring, dict)
    assert isinstance(colour_group, dict)
    assert isinstance(aut_group, dict)
    assert isinstance(s5_image, dict)
    assert isinstance(comparison, dict)
    return [
        f"SCRIPT_SHA256 {certificate['script_sha256']}",
        f"A5_ORDER {group['order']}",
        f"D_SIZE {involutions['size']}",
        f"EDGE_COUNT {colouring['edge_count']}",
        f"EDGE_COLOUR_SET {colouring['edge_colour_set']}",
        f"COLOUR_AUT_ORDER {colour_group['order']}",
        f"COLOUR_BACKTRACKING_NODES {colour_group['exhaustive_backtracking_nodes']}",
        f"AUT_A5_CANDIDATE_IMAGE_PAIRS {aut_group['candidate_generator_image_pairs_tested']}",
        f"AUT_A5_ORDER {aut_group['automorphism_order']}",
        f"AUT_A5_RESTRICTION_IMAGE_ORDER {aut_group['restriction_image_order']}",
        f"S5_CONJUGATION_IMAGE_ORDER {s5_image['restriction_image_order']}",
        "DIRECT_RESTRICTION_EQUALS_S5_CONJUGATION "
        f"{s5_image['equals_direct_A5_automorphism_restriction']}",
        f"COMPARISON_RELATION {comparison['relation']}",
        "COLOUR_ONLY_COUNT "
        f"{comparison['colour_automorphisms_outside_restriction_count']}",
        "RESTRICTION_ONLY_COUNT "
        f"{comparison['restriction_elements_outside_colour_group_count']}",
        "SEPARATING_PERMUTATION "
        f"{comparison['lexicographically_first_separating_permutation']}",
        f"CERTIFICATE_SHA256 {certificate['certificate_sha256']}",
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", required=True, type=Path)
    parser.add_argument("--summary", required=True, type=Path)
    args = parser.parse_args()

    script_path = Path(__file__).resolve()
    certificate = build_certificate(script_path)
    summary = "\n".join(summary_lines(certificate)) + "\n"

    args.certificate.parent.mkdir(parents=True, exist_ok=True)
    args.summary.parent.mkdir(parents=True, exist_ok=True)
    args.certificate.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    args.summary.write_text(summary, encoding="utf-8")
    print(summary, end="")


if __name__ == "__main__":
    main()

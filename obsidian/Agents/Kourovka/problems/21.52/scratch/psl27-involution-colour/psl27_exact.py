#!/usr/bin/env python3
"""Exact bounded PSL(2,7) involution product-order colour computation.

The group model is SL(2,7)/{+I,-I}; elements are canonical representatives of
sign-pairs of determinant-one 2 by 2 matrices.  No external packages are used.
The script exhaustively enumerates (1) the selected complete involution class,
(2) every colour-preserving permutation of that class, and (3) every abstract
automorphism of the group via all possible images of a deterministic generating
pair.  It writes a self-contained JSON certificate.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
from collections import Counter, deque
from pathlib import Path


Q = 7
EXPECTED_GROUP_ORDER = 168
EXPECTED_CLASS_SIZE = 21
Matrix = tuple[int, int, int, int]


def canonical(matrix: Matrix) -> Matrix:
    matrix = tuple(x % Q for x in matrix)  # type: ignore[assignment]
    negative = tuple((-x) % Q for x in matrix)
    return min(matrix, negative)  # type: ignore[return-value]


def multiply(left: Matrix, right: Matrix) -> Matrix:
    a, b, c, d = left
    e, f, g, h = right
    return canonical(
        (
            a * e + b * g,
            a * f + b * h,
            c * e + d * g,
            c * f + d * h,
        )
    )


def inverse(matrix: Matrix) -> Matrix:
    a, b, c, d = matrix
    return canonical((d, -b, -c, a))


IDENTITY = canonical((1, 0, 0, 1))


def determinant(matrix: Matrix) -> int:
    a, b, c, d = matrix
    return (a * d - b * c) % Q


def build_group() -> list[Matrix]:
    elements = {
        canonical(matrix)
        for matrix in itertools.product(range(Q), repeat=4)
        if determinant(matrix) == 1
    }
    result = sorted(elements)
    if len(result) != EXPECTED_GROUP_ORDER:
        raise AssertionError(f"expected 168 quotient elements, got {len(result)}")
    if IDENTITY not in elements:
        raise AssertionError("identity missing")
    return result


def element_order(element: Matrix) -> int:
    value = IDENTITY
    for exponent in range(1, EXPECTED_GROUP_ORDER + 1):
        value = multiply(value, element)
        if value == IDENTITY:
            return exponent
    raise AssertionError("Lagrange bound failed")


def conjugacy_class(element: Matrix, group: list[Matrix]) -> tuple[Matrix, ...]:
    return tuple(
        sorted(
            {
                multiply(multiply(inverse(g), element), g)
                for g in group
            }
        )
    )


def involution_classes(group: list[Matrix]) -> list[tuple[Matrix, ...]]:
    involutions = {g for g in group if element_order(g) == 2}
    remaining = set(involutions)
    classes: list[tuple[Matrix, ...]] = []
    while remaining:
        representative = min(remaining)
        current = conjugacy_class(representative, group)
        if not set(current) <= involutions:
            raise AssertionError("conjugacy class left the involutions")
        classes.append(current)
        remaining.difference_update(current)
    classes.sort()
    if set().union(*(set(cls) for cls in classes)) != involutions:
        raise AssertionError("involution class partition incomplete")
    return classes


def generated_subgroup(
    generators: tuple[Matrix, Matrix], group_set: set[Matrix]
) -> set[Matrix]:
    steps = (
        generators[0],
        inverse(generators[0]),
        generators[1],
        inverse(generators[1]),
    )
    found = {IDENTITY}
    queue = deque([IDENTITY])
    while queue:
        x = queue.popleft()
        for step in steps:
            y = multiply(x, step)
            if y not in group_set:
                raise AssertionError("multiplication left the group")
            if y not in found:
                found.add(y)
                queue.append(y)
    return found


def deterministic_generating_pair(group: list[Matrix]) -> tuple[Matrix, Matrix]:
    group_set = set(group)
    nonidentity = [g for g in group if g != IDENTITY]
    for first in nonidentity:
        for second in nonidentity:
            if len(generated_subgroup((first, second), group_set)) == len(group):
                return first, second
    raise AssertionError("no generating pair found")


def enumerate_automorphisms(
    group: list[Matrix], source_pair: tuple[Matrix, Matrix]
) -> tuple[list[tuple[int, ...]], int]:
    """Enumerate every automorphism through all images of a generating pair.

    For a candidate image pair, propagate the putative map around the complete
    right Cayley graph for the source generators and their inverses.  Conflicting
    paths reject the candidate.  A conflict-free bijection is an automorphism.
    Since the source pair generates, every automorphism occurs exactly once.
    """

    index = {g: i for i, g in enumerate(group)}
    identity_index = index[IDENTITY]
    source_steps = (
        source_pair[0],
        inverse(source_pair[0]),
        source_pair[1],
        inverse(source_pair[1]),
    )
    automorphisms: list[tuple[int, ...]] = []
    candidates_tested = 0

    for image_first in group:
        for image_second in group:
            candidates_tested += 1
            image_steps = (
                image_first,
                inverse(image_first),
                image_second,
                inverse(image_second),
            )
            mapping = [-1] * len(group)
            mapping[identity_index] = identity_index
            queue = deque([identity_index])
            consistent = True

            while queue and consistent:
                source_index = queue.popleft()
                image_index = mapping[source_index]
                for source_step, image_step in zip(source_steps, image_steps):
                    next_source = index[multiply(group[source_index], source_step)]
                    next_image = index[multiply(group[image_index], image_step)]
                    if mapping[next_source] == -1:
                        mapping[next_source] = next_image
                        queue.append(next_source)
                    elif mapping[next_source] != next_image:
                        consistent = False
                        break

            if consistent and -1 not in mapping and len(set(mapping)) == len(group):
                automorphisms.append(tuple(mapping))

    if len(set(automorphisms)) != len(automorphisms):
        raise AssertionError("duplicate automorphisms")
    return sorted(automorphisms), candidates_tested


def colour_matrix(involution_class: tuple[Matrix, ...]) -> list[list[int]]:
    size = len(involution_class)
    matrix = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(i + 1, size):
            colour = element_order(multiply(involution_class[i], involution_class[j]))
            matrix[i][j] = matrix[j][i] = colour
    return matrix


def enumerate_colour_automorphisms(
    colours: list[list[int]], max_nodes: int
) -> tuple[list[tuple[int, ...]], int]:
    """Exhaustively enumerate all permutations preserving the full colour matrix."""

    size = len(colours)
    image = [-1] * size
    used = [False] * size
    assigned: list[int] = []
    automorphisms: list[tuple[int, ...]] = []
    nodes = 0

    def candidates(source: int) -> list[int]:
        result = []
        for target in range(size):
            if used[target]:
                continue
            if all(
                colours[source][old_source]
                == colours[target][image[old_source]]
                for old_source in assigned
            ):
                result.append(target)
        return result

    def search() -> None:
        nonlocal nodes
        nodes += 1
        if nodes > max_nodes:
            raise RuntimeError(f"node limit {max_nodes} exceeded; result incomplete")
        if len(assigned) == size:
            automorphisms.append(tuple(image))
            return

        best_source = -1
        best_candidates: list[int] | None = None
        for source in range(size):
            if image[source] != -1:
                continue
            possible = candidates(source)
            if not possible:
                return
            if (
                best_candidates is None
                or len(possible) < len(best_candidates)
                or (
                    len(possible) == len(best_candidates)
                    and source < best_source
                )
            ):
                best_source = source
                best_candidates = possible

        if best_candidates is None:
            raise AssertionError("unassigned source selection failed")
        for target in best_candidates:
            image[best_source] = target
            used[target] = True
            assigned.append(best_source)

            # Forward checking makes every rejected branch explicit while leaving
            # the search exhaustive.
            viable = True
            for source in range(size):
                if image[source] == -1 and not candidates(source):
                    viable = False
                    break
            if viable:
                search()

            assigned.pop()
            used[target] = False
            image[best_source] = -1

    search()
    if len(set(automorphisms)) != len(automorphisms):
        raise AssertionError("duplicate colour automorphisms")
    return sorted(automorphisms), nodes


def permutation_preserves_colours(
    permutation: tuple[int, ...], colours: list[list[int]]
) -> bool:
    size = len(colours)
    return sorted(permutation) == list(range(size)) and all(
        colours[i][j] == colours[permutation[i]][permutation[j]]
        for i in range(size)
        for j in range(i + 1, size)
    )


def sha256_json(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def run(max_nodes: int) -> dict[str, object]:
    group = build_group()
    group_index = {g: i for i, g in enumerate(group)}
    classes = involution_classes(group)
    if len(classes) != 1:
        raise AssertionError(f"expected one involution class, got {len(classes)}")
    involution_class = classes[0]
    if len(involution_class) != EXPECTED_CLASS_SIZE:
        raise AssertionError(
            f"expected involution class size 21, got {len(involution_class)}"
        )

    colours = colour_matrix(involution_class)
    edge_counts = Counter(
        colours[i][j]
        for i in range(len(involution_class))
        for j in range(i + 1, len(involution_class))
    )
    colour_automorphisms, search_nodes = enumerate_colour_automorphisms(
        colours, max_nodes
    )
    if not all(
        permutation_preserves_colours(permutation, colours)
        for permutation in colour_automorphisms
    ):
        raise AssertionError("enumerator returned a non-colour-automorphism")

    source_pair = deterministic_generating_pair(group)
    automorphisms, image_pairs_tested = enumerate_automorphisms(group, source_pair)
    class_index = {g: i for i, g in enumerate(involution_class)}
    restriction_image: set[tuple[int, ...]] = set()
    setwise_stabilizer_count = 0
    class_set = set(involution_class)

    for automorphism in automorphisms:
        images = {
            group[automorphism[group_index[x]]]
            for x in involution_class
        }
        if images == class_set:
            setwise_stabilizer_count += 1
            restriction = tuple(
                class_index[group[automorphism[group_index[x]]]]
                for x in involution_class
            )
            restriction_image.add(restriction)

    colour_set = set(colour_automorphisms)
    if not restriction_image <= colour_set:
        raise AssertionError("an Aut(L) restriction failed colour preservation")
    extra_colour_automorphisms = sorted(colour_set - restriction_image)
    separator = extra_colour_automorphisms[0] if extra_colour_automorphisms else None

    certificate: dict[str, object] = {
        "schema_version": 1,
        "algorithm": "PSL27-INVOLUTION-COLOUR exact exhaustive v1",
        "model": "PSL(2,7)=SL(2,7)/{+I,-I}",
        "field_order": Q,
        "group_order": len(group),
        "group_elements": [list(x) for x in group],
        "involution_count": sum(len(cls) for cls in classes),
        "involution_class_count": len(classes),
        "involution_class": [list(x) for x in involution_class],
        "involution_class_size": len(involution_class),
        "colour_matrix": colours,
        "colour_matrix_sha256": sha256_json(colours),
        "edge_colour_counts": {
            str(colour): count for colour, count in sorted(edge_counts.items())
        },
        "colour_automorphism_count": len(colour_automorphisms),
        "colour_automorphisms": [list(x) for x in colour_automorphisms],
        "colour_search_nodes": search_nodes,
        "colour_search_max_nodes": max_nodes,
        "source_generating_pair": [list(x) for x in source_pair],
        "autL_image_pairs_tested": image_pairs_tested,
        "autL_count": len(automorphisms),
        "setwise_stabilizer_count": setwise_stabilizer_count,
        "restriction_image_count": len(restriction_image),
        "restriction_image": [list(x) for x in sorted(restriction_image)],
        "restriction_image_is_colour_subgroup": True,
        "groups_equal": colour_set == restriction_image,
        "separator": list(separator) if separator is not None else None,
    }
    certificate["certificate_content_sha256"] = sha256_json(certificate)
    return certificate


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--max-nodes", type=int, default=50_000_000)
    args = parser.parse_args()
    if args.max_nodes <= 0:
        parser.error("--max-nodes must be positive")

    certificate = run(args.max_nodes)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    summary_keys = (
        "group_order",
        "involution_class_size",
        "edge_colour_counts",
        "colour_automorphism_count",
        "colour_search_nodes",
        "autL_count",
        "setwise_stabilizer_count",
        "restriction_image_count",
        "groups_equal",
        "separator",
        "certificate_content_sha256",
    )
    print(json.dumps({key: certificate[key] for key in summary_keys}, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:  # Make an incomplete run unmistakable.
        print(f"FATAL: {type(error).__name__}: {error}", file=sys.stderr)
        raise

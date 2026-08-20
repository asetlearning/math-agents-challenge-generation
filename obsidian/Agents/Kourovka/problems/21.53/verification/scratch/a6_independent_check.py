#!/usr/bin/env python3
"""Independent standard-library certificate checker for the bounded (A6,2A) case.

This does not call GAP, nauty/dreadnaut, bliss, Sage, or claimant code.  Permutations
are literal tuples on range(6).  The group-order conclusion is obtained from the
duad--syntheme reconstruction and an explicit incidence duality, not from a graph
automorphism oracle.
"""

from collections import Counter, deque
from itertools import combinations, permutations
from math import factorial


N = 6
IDENTITY = tuple(range(N))


def compose(a, b):
    """Return a after b."""
    return tuple(a[b[i]] for i in range(N))


def inverse(a):
    out = [None] * N
    for i, image in enumerate(a):
        out[image] = i
    return tuple(out)


def parity(a):
    return sum(a[i] > a[j] for i in range(N) for j in range(i + 1, N)) % 2


def perm_order(a):
    power = IDENTITY
    for k in range(1, 61):
        power = compose(a, power)
        if power == IDENTITY:
            return k
    raise AssertionError("order bound failed")


def cycle_type(a):
    seen = set()
    lengths = []
    for i in range(N):
        if i in seen:
            continue
        j = i
        length = 0
        while j not in seen:
            seen.add(j)
            length += 1
            j = a[j]
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def conjugate(h, x):
    return compose(compose(h, x), inverse(h))


def subgroup_generated(generators):
    generators = tuple(generators)
    found = {IDENTITY}
    queue = deque([IDENTITY])
    while queue:
        x = queue.popleft()
        for g in generators:
            y = compose(x, g)
            if y not in found:
                found.add(y)
                queue.append(y)
    return found


def duad_label(d):
    return "".join(str(i + 1) for i in sorted(d))


def syntheme_label(s):
    return "/".join(duad_label(d) for d in s)


def canonical_syntheme(parts):
    return tuple(sorted((frozenset(p) for p in parts), key=lambda d: tuple(sorted(d))))


def all_synthemes(points):
    points = tuple(sorted(points))
    if not points:
        return [tuple()]
    a = points[0]
    result = []
    for b in points[1:]:
        rest = tuple(x for x in points if x not in (a, b))
        for tail in all_synthemes(rest):
            result.append(canonical_syntheme((frozenset((a, b)),) + tail))
    return sorted(set(result), key=lambda s: tuple(duad_label(d) for d in s))


def flag_of_involution(x):
    fixed = frozenset(i for i in range(N) if x[i] == i)
    transposed = []
    for i in range(N):
        if x[i] != i and i < x[i]:
            transposed.append(frozenset((i, x[i])))
    assert len(fixed) == 2 and len(transposed) == 2
    return fixed, canonical_syntheme((fixed,) + tuple(transposed))


def bfs_distances(adjacency, source):
    dist = {source: 0}
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for v in adjacency[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                queue.append(v)
    return dist


def find_polarity(duads, synthemes):
    """Find P: duads -> synthemes with d in P(e) iff e in P(d)."""
    mapping = {}
    used = set()

    def candidates(d):
        return [s for s in synthemes if s not in used and
                all((d in image_e) == (e in s) for e, image_e in mapping.items())]

    def recurse():
        if len(mapping) == len(duads):
            return dict(mapping)
        d = min((d for d in duads if d not in mapping), key=lambda x: len(candidates(x)))
        for s in candidates(d):
            mapping[d] = s
            used.add(s)
            result = recurse()
            if result is not None:
                return result
            used.remove(s)
            del mapping[d]
        return None

    result = recurse()
    if result is None:
        raise AssertionError("no duad--syntheme polarity found")
    return result


def main():
    symmetric = tuple(permutations(range(N)))
    alternating = tuple(g for g in symmetric if parity(g) == 0)
    assert len(symmetric) == factorial(6) == 720
    assert len(alternating) == 360

    noncommuting_pair = next((a, b) for a in alternating for b in alternating
                             if compose(a, b) != compose(b, a))

    unseen = set(alternating)
    conjugacy_classes = []
    while unseen:
        x = min(unseen)
        cls = {conjugate(h, x) for h in alternating}
        conjugacy_classes.append(cls)
        unseen -= cls
    class_summary = sorted((cycle_type(next(iter(cls))), len(cls)) for cls in conjugacy_classes)
    normal_closure_sizes = sorted(
        len(subgroup_generated(cls)) for cls in conjugacy_classes if cls != {IDENTITY}
    )
    assert normal_closure_sizes == [360] * (len(conjugacy_classes) - 1)

    involutions = sorted(g for g in alternating if g != IDENTITY and perm_order(g) == 2)
    assert len(involutions) == 45
    assert {cycle_type(g) for g in involutions} == {(2, 2, 1, 1)}
    involution_class = {conjugate(h, involutions[0]) for h in alternating}
    assert involution_class == set(involutions)

    prime_divisors = [p for p in (2, 3, 5) if len(alternating) % p == 0]
    assert prime_divisors == [2, 3, 5]

    duads = sorted((frozenset(c) for c in combinations(range(N), 2)), key=duad_label)
    synthemes = all_synthemes(range(N))
    assert len(duads) == len(synthemes) == 15
    flags = [flag_of_involution(x) for x in involutions]
    assert len(set(flags)) == 45
    assert set(flags) == {(d, s) for d in duads for s in synthemes if d in s}
    flag_index = {flag: i for i, flag in enumerate(flags)}

    product_matrix = [
        [perm_order(compose(x, y)) for y in involutions]
        for x in involutions
    ]
    assert all(product_matrix[i][i] == 1 for i in range(45))
    assert all(product_matrix[i][j] == product_matrix[j][i]
               for i in range(45) for j in range(45))

    relation = {t: [set() for _ in involutions] for t in (2, 3, 4, 5)}
    edge_counts = Counter()
    pair_order = {}
    for i, j in combinations(range(len(involutions)), 2):
        t = product_matrix[i][j]
        pair_order[i, j] = t
        edge_counts[t] += 1
        relation.setdefault(t, [set() for _ in involutions])
        relation[t][i].add(j)
        relation[t][j].add(i)
    assert set(edge_counts) == {2, 3, 4, 5}
    valencies = {t: sorted({len(neighbours) for neighbours in relation[t]})
                 for t in sorted(edge_counts)}
    assert valencies == {2: [4], 3: [16], 4: [8], 5: [16]}
    assert edge_counts == Counter({3: 360, 5: 360, 4: 180, 2: 90})

    distance_orders = {}
    distance_distributions = set()
    for i in range(45):
        dist = bfs_distances(relation[2], i)
        assert len(dist) == 45
        distance_distributions.add(tuple(Counter(dist.values())[d] for d in range(5)))
        for j in range(i + 1, 45):
            distance_orders.setdefault(dist[j], set()).add(pair_order[i, j])
    assert distance_distributions == {(1, 4, 8, 16, 16)}
    assert distance_orders == {1: {2}, 2: {4}, 3: {3}, 4: {5}}

    adjacency2 = relation[2]
    triangles = []
    for triple in combinations(range(45), 3):
        if all(v in adjacency2[u] for u, v in combinations(triple, 2)):
            triangles.append(frozenset(triple))
    four_cliques = []
    for quad in combinations(range(45), 4):
        if all(v in adjacency2[u] for u, v in combinations(quad, 2)):
            four_cliques.append(frozenset(quad))
    assert len(triangles) == 30 and not four_cliques
    assert {sum(i in tri for tri in triangles) for i in range(45)} == {2}
    assert {sum({i, j} <= tri for tri in triangles)
            for i, j in combinations(range(45), 2) if j in adjacency2[i]} == {1}

    expected_duad_triangles = {frozenset(flag_index[(d, s)] for s in synthemes if d in s): d
                               for d in duads}
    expected_syntheme_triangles = {frozenset(flag_index[(d, s)] for d in s): s
                                   for s in synthemes}
    assert set(triangles) == set(expected_duad_triangles) | set(expected_syntheme_triangles)

    triangle_index = {tri: i for i, tri in enumerate(triangles)}
    incidence = {i: set() for i in range(30)}
    for i, j in combinations(range(30), 2):
        intersection = triangles[i] & triangles[j]
        if intersection:
            assert len(intersection) == 1
            incidence[i].add(j)
            incidence[j].add(i)
    assert {len(incidence[i]) for i in incidence} == {3}
    recovered_parts = [set(), set()]
    recovered_parts[0].add(0)
    queue = deque([0])
    while queue:
        u = queue.popleft()
        side = 0 if u in recovered_parts[0] else 1
        for v in incidence[u]:
            if v in recovered_parts[side]:
                raise AssertionError("triangle-intersection graph not bipartite")
            if v not in recovered_parts[1 - side]:
                recovered_parts[1 - side].add(v)
                queue.append(v)
    assert set.union(*recovered_parts) == set(range(30))
    assert sorted(map(len, recovered_parts)) == [15, 15]

    duad_nodes = {triangle_index[tri] for tri in expected_duad_triangles}
    syntheme_nodes = {triangle_index[tri] for tri in expected_syntheme_triangles}
    assert {frozenset(recovered_parts[0]), frozenset(recovered_parts[1])} == {
        frozenset(duad_nodes), frozenset(syntheme_nodes)
    }

    duad_node_by_duad = {d: triangle_index[tri] for tri, d in expected_duad_triangles.items()}
    syntheme_node_by_syntheme = {s: triangle_index[tri] for tri, s in expected_syntheme_triangles.items()}
    duad_by_node = {node: d for d, node in duad_node_by_duad.items()}
    syntheme_by_node = {node: s for s, node in syntheme_node_by_syntheme.items()}
    for d, e in combinations(duads, 2):
        common_incidence_neighbour = bool(
            incidence[duad_node_by_duad[d]] & incidence[duad_node_by_duad[e]]
        )
        assert common_incidence_neighbour == d.isdisjoint(e)

    disjointness = {d: {e for e in duads if e != d and d.isdisjoint(e)} for d in duads}
    independent_fives = []
    for family in combinations(duads, 5):
        if all(e not in disjointness[d] for d, e in combinations(family, 2)):
            independent_fives.append(frozenset(family))
    assert not any(all(e not in disjointness[d] for d, e in combinations(family, 2))
                   for family in combinations(duads, 6))
    point_stars = {frozenset(d for d in duads if point in d) for point in range(N)}
    assert set(independent_fives) == point_stars and len(point_stars) == 6

    polarity = find_polarity(duads, synthemes)
    inverse_polarity = {s: d for d, s in polarity.items()}
    assert len(inverse_polarity) == 15
    assert all((d in polarity[e]) == (e in polarity[d]) for d in duads for e in duads)
    duality = {}
    for d in duads:
        duality[duad_node_by_duad[d]] = syntheme_node_by_syntheme[polarity[d]]
    for s in synthemes:
        duality[syntheme_node_by_syntheme[s]] = duad_node_by_duad[inverse_polarity[s]]
    assert set(duality) == set(range(30)) and len(set(duality.values())) == 30
    assert all(duality[duality[u]] == u for u in range(30))
    assert all((v in incidence[u]) == (duality[v] in incidence[duality[u]])
               for u, v in combinations(range(30), 2))
    assert all(duality[u] in syntheme_nodes for u in duad_nodes)
    assert all(duality[u] in duad_nodes for u in syntheme_nodes)

    duality_on_flags = {}
    for i, (d, s) in enumerate(flags):
        image_s = syntheme_by_node[duality[duad_node_by_duad[d]]]
        image_d = duad_by_node[duality[syntheme_node_by_syntheme[s]]]
        assert image_d in image_s
        duality_on_flags[i] = flag_index[(image_d, image_s)]
    assert len(set(duality_on_flags.values())) == 45
    assert all(pair_order[min(i, j), max(i, j)] ==
               pair_order[min(duality_on_flags[i], duality_on_flags[j]),
                          max(duality_on_flags[i], duality_on_flags[j])]
               for i, j in combinations(range(45), 2))

    # Independent audit of the incidence-subdivision encodings used for graph oracles.
    augmented_sizes = {}
    for name, colours in (("two", (2, 3)), ("full", (2, 3, 4, 5))):
        cells = [45] + [edge_counts[t] for t in colours]
        augmented_sizes[name] = {"colours": colours, "cell_sizes": cells,
                                 "vertices": sum(cells),
                                 "incidence_edges": 2 * sum(cells[1:])}
    assert augmented_sizes["two"] == {
        "colours": (2, 3), "cell_sizes": [45, 90, 360],
        "vertices": 495, "incidence_edges": 900
    }
    assert augmented_sizes["full"] == {
        "colours": (2, 3, 4, 5), "cell_sizes": [45, 90, 360, 180, 360],
        "vertices": 1035, "incidence_edges": 1980
    }

    base = flags.index((frozenset((4, 5)), canonical_syntheme(
        (frozenset((0, 1)), frozenset((2, 3)), frozenset((4, 5)))
    )))
    base_dist = bfs_distances(adjacency2, base)
    representatives = {}
    for distance in range(1, 5):
        j = min(i for i in range(45) if base_dist[i] == distance)
        representatives[distance] = {
            "flag": f"{duad_label(flags[j][0])}|{syntheme_label(flags[j][1])}",
            "product_order": pair_order[min(base, j), max(base, j)]
        }

    print("MODEL")
    print(f"|S6|={len(symmetric)} |A6|={len(alternating)} nonabelian={bool(noncommuting_pair)}")
    print(f"A6 conjugacy classes (cycle type,size)={class_summary}")
    print(f"nonidentity normal-closure sizes={normal_closure_sizes}; hence simple")
    print(f"involutions={len(involutions)} cycle_types={sorted({cycle_type(g) for g in involutions})}")
    print(f"A6-conjugacy orbit on first involution={len(involution_class)}")
    print(f"prime divisors={prime_divisors}; second-smallest p={prime_divisors[1]}")
    print("PRODUCT MATRIX")
    print(f"matrix entries={sum(map(len, product_matrix))}; diagonal order={{1}}; unordered off-diagonal pairs={len(pair_order)}")
    print(f"off-diagonal colours={sorted(edge_counts)}")
    print(f"edge counts={dict(sorted(edge_counts.items()))}")
    print(f"valencies={valencies}")
    print(f"colour-2 distance spheres={next(iter(distance_distributions))}")
    print(f"distance -> product-order sets={dict(sorted(distance_orders.items()))}")
    print(f"base flag=56|12/34/56; representatives={representatives}")
    print("DUAD--SYNTHEME RECONSTRUCTION")
    print(f"maximal triangles={len(triangles)} K4s={len(four_cliques)} memberships/flag=2")
    print(f"triangle-intersection graph: vertices=30 degree=3 parts={sorted(map(len,recovered_parts))}")
    print("common syntheme neighbour of two duads iff disjoint: PASS")
    print(f"duad-disjointness independence number=5; maximum families={len(independent_fives)}; all six point-stars: PASS")
    print("Thus part-preserving incidence automorphisms inject into S6 (<=720),")
    print("and all incidence automorphisms have order <=2*720=1440.")
    print("EXPLICIT PART-SWAPPING INCIDENCE AUTOMORPHISM")
    for d in duads:
        print(f"P({duad_label(d)})={syntheme_label(polarity[d])}")
    print("P is bijective and d in P(e) iff e in P(d); the induced incidence duality is involutory.")
    print("induced flag permutation preserves all 990 product orders: PASS")
    print("Natural S6 gives 720 part-preserving full-colour automorphisms; the displayed")
    print("duality gives a disjoint coset, so |Aut(full colour)|>=1440.")
    print("Together with Aut(full)<=Aut_2<=Aut(line incidence)<=1440:")
    print("|Aut(full colour)|=|Aut_2|=|Aut_2 intersection Aut_3|=1440.")
    print("AUGMENTED INCIDENCE ENCODINGS")
    print(augmented_sizes)
    print("Each edge-node has exactly its two original endpoints and its own colour cell;")
    print("therefore restriction/unique extension is a bijection with the named relation automorphism group.")
    print("AUT_t VACUITY")
    print("Occurring labels are 2,3,4,5. For every other positive t, E_t is empty,")
    print("so the implication defining Aut_t is vacuous and Aut_t=S_45.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Bound the pointwise closed-neighborhood stabilizer in the K_14 flip graph.

Equitable colour refinement is an automorphism invariant.  We individualize a
base perfect matching and each of its 42 neighbors.  If every stable colour
class has size at most two, the pointwise stabilizer has an orbit of size at
most two.  Individualizing one vertex of a two-cell and obtaining the discrete
partition makes its stabilizer trivial, hence bounds the original kernel by 2.
"""

from array import array
from collections import Counter
from itertools import combinations, product

from matching_orbits import matchings


N = 14
K = 7


def neighbors(m):
    edges = [(i, m[i]) for i in range(N) if m[i] > i]
    for p in range(K):
        a, b = edges[p]
        for q in range(p + 1, K):
            c, d = edges[q]
            z = list(m)
            z[a], z[c], z[b], z[d] = c, a, d, b
            yield tuple(z)
            z = list(m)
            z[a], z[d], z[b], z[c] = d, a, c, b
            yield tuple(z)


def refine(colours, adjacency, degree, max_rounds=20):
    counts = [len(set(colours))]
    for _ in range(max_rounds):
        table = {}
        new = [0] * len(colours)
        for i in range(len(colours)):
            off = i * degree
            neigh = sorted(colours[adjacency[off + j]] for j in range(degree))
            key = (colours[i], tuple(neigh))
            if key not in table:
                table[key] = len(table)
            new[i] = table[key]
        colours = new
        counts.append(len(table))
        if counts[-1] == counts[-2]:
            break
    return colours, counts


def main():
    vertices = list(matchings(N, K))
    index = {m: i for i, m in enumerate(vertices)}
    assert len(vertices) == 135135 == len(index)
    degree = 42
    adjacency = array('I')
    for m in vertices:
        row = sorted(index[z] for z in neighbors(m))
        assert len(row) == degree and len(set(row)) == degree
        adjacency.extend(row)

    base = tuple([1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12])
    b = index[base]
    local = list(adjacency[b * degree:(b + 1) * degree])
    raw_local = [index[z] for z in neighbors(base)]
    assert set(raw_local) == set(local)
    directions = list(combinations(range(K), 2))
    blocks = {direction: raw_local[2*t:2*t+2]
              for t, direction in enumerate(directions)}
    adjsets = {v: set(adjacency[v*degree:(v+1)*degree]) for v in raw_local}

    pair_common_counts = Counter()
    for d1, d2 in combinations(directions, 2):
        relation = 'intersect' if set(d1) & set(d2) else 'disjoint'
        for x in blocks[d1]:
            for y in blocks[d2]:
                pair_common_counts[(relation, len(adjsets[x] & adjsets[y]))] += 1
    same_direction_common = {
        len(adjsets[block[0]] & adjsets[block[1]]) for block in blocks.values()
    }
    assert same_direction_common == {1}
    assert {q for (rel, q) in pair_common_counts if rel == 'intersect'} == {3}
    assert {q for (rel, q) in pair_common_counts if rel == 'disjoint'} == {2}

    triangle_common_counts = Counter()
    for i, j, k in combinations(range(K), 3):
        tri = ((i, j), (i, k), (j, k))
        for bits in product((0, 1), repeat=3):
            chosen_local = [blocks[d][bit] for d, bit in zip(tri, bits)]
            q = len(set.intersection(*(adjsets[v] for v in chosen_local)))
            triangle_common_counts[(sum(bits) % 2, q)] += 1
    colours = [0] * len(vertices)
    colours[b] = 1
    for c, v in enumerate(local, start=2):
        colours[v] = c
    colours, counts1 = refine(colours, adjacency, degree)
    multiplicities = Counter(colours)
    sizes = Counter(multiplicities.values())
    max_cell = max(multiplicities.values())
    assert max_cell <= 2

    two_cell_colour = next(c for c, size in multiplicities.items() if size == 2)
    chosen = next(i for i, c in enumerate(colours) if c == two_cell_colour)
    colours[chosen] = max(colours) + 1
    colours2, counts2 = refine(colours, adjacency, degree)
    assert len(set(colours2)) == len(vertices)

    print(f"vertices={len(vertices)} degree={degree} adjacency_entries={len(adjacency)}")
    print(f"closed_neighborhood_sources={1+len(local)}")
    print(f"same_direction_pair_common_neighbor_counts={sorted(same_direction_common)}")
    print(f"distinct_direction_pair_common_neighbor_table={sorted(pair_common_counts.items())}")
    print(f"direction_triangle_parity_common_neighbor_table={sorted(triangle_common_counts.items())}")
    print(f"first_refinement_counts={counts1}")
    print(f"stable_cell_size_distribution={sorted(sizes.items())} max_cell={max_cell}")
    print(f"second_refinement_counts={counts2}")
    print("individualized_second_partition_is_discrete=true")
    print("pointwise_closed_neighborhood_stabilizer_order_bound=2")


if __name__ == '__main__':
    main()

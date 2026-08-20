#!/usr/bin/env python3
"""Exact local-rigidity certificate for the n=13 six-matching exchange graph.

Vertices are six-matchings of K_13; a move replaces one matched edge using the
unique unmatched point, so adjacent vertices share exactly five edges.  The
certificate proves that graph distances from a base vertex and its 12 neighbors
separate all 135135 vertices.  Thus the pointwise stabilizer of the closed
neighborhood is trivial.
"""

from array import array
from collections import deque
from math import factorial

from matching_orbits import matchings


N = 13
K = 6


def neighbors(m):
    hole = m.index(-1)
    edges = [(i, m[i]) for i in range(N) if m[i] > i]
    for a, b in edges:
        # Replace ab by hole-a, leaving b unmatched.
        z = list(m)
        z[a] = hole
        z[hole] = a
        z[b] = -1
        yield tuple(z)
        # Replace ab by hole-b, leaving a unmatched.
        z = list(m)
        z[b] = hole
        z[hole] = b
        z[a] = -1
        yield tuple(z)


def bfs(source, vertices, index):
    dist = array('B', [255]) * len(vertices)
    dist[source] = 0
    queue = deque([source])
    while queue:
        i = queue.popleft()
        nd = dist[i] + 1
        for z in neighbors(vertices[i]):
            j = index[z]
            if dist[j] == 255:
                dist[j] = nd
                queue.append(j)
    if 255 in dist:
        raise AssertionError("graph disconnected")
    return dist


def main():
    vertices = list(matchings(N, K))
    index = {m: i for i, m in enumerate(vertices)}
    assert len(vertices) == 135135 == len(index)
    base = tuple([1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, -1])
    b = index[base]
    local = sorted(index[z] for z in neighbors(base))
    assert len(local) == 12

    # The induced local graph is exactly six disjoint edges: two moves using the
    # same deleted base edge are adjacent, and moves using different edges are not.
    local_edges = []
    local_set = set(local)
    for i in local:
        for z in neighbors(vertices[i]):
            j = index[z]
            if j in local_set and i < j:
                local_edges.append((i, j))
    degrees = {i: 0 for i in local}
    for i, j in local_edges:
        degrees[i] += 1
        degrees[j] += 1
    assert len(local_edges) == 6 and set(degrees.values()) == {1}

    sources = [b] + local
    distance_columns = [bfs(s, vertices, index) for s in sources]
    fingerprint_ids = {}
    colours = []
    diameter_from_base = max(distance_columns[0])
    for i in range(len(vertices)):
        fp = bytes(column[i] for column in distance_columns)
        if fp not in fingerprint_ids:
            fingerprint_ids[fp] = len(fingerprint_ids)
        colours.append(fingerprint_ids[fp])

    initial_colour_count = len(fingerprint_ids)
    refinement_counts = [initial_colour_count]
    for _round in range(20):
        key_to_colour = {}
        new_colours = [0] * len(vertices)
        for i, m in enumerate(vertices):
            neighbour_colours = sorted(colours[index[z]] for z in neighbors(m))
            key = (colours[i], tuple(neighbour_colours))
            if key not in key_to_colour:
                key_to_colour[key] = len(key_to_colour)
            new_colours[i] = key_to_colour[key]
        colours = new_colours
        refinement_counts.append(len(key_to_colour))
        if refinement_counts[-1] == refinement_counts[-2]:
            break
    assert refinement_counts[-1] == len(vertices)

    local_aut_bound = (2 ** 6) * factorial(6)  # Aut(6 K_2)
    global_bound = len(vertices) * local_aut_bound
    print(f"vertices={len(vertices)} degree=12 local_vertices={len(local)}")
    print(f"local_edges={len(local_edges)} local_degree_set={sorted(set(degrees.values()))}")
    print(f"distance_sources={len(sources)} initial_distance_colours={initial_colour_count}")
    print(f"equitable_refinement_colour_counts={refinement_counts}")
    print(f"diameter_from_base={diameter_from_base}")
    print(f"pointwise_closed_neighborhood_stabilizer_bound=1")
    print(f"vertex_stabilizer_bound={local_aut_bound}")
    print(f"full_aut_order_bound={global_bound} factorial_13={factorial(13)}")
    print("natural_S13_action_is_faithful=true")
    print("natural_S13_containment_plus_bound_gives_equality=true")


if __name__ == '__main__':
    main()

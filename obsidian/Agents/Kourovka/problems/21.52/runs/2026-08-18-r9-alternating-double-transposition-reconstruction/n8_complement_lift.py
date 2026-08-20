#!/usr/bin/env python3
"""Check whether 4-set complementation in n=8 lifts to the exact colour graph."""

from itertools import combinations, permutations
from importlib.machinery import SourceFileLoader

HELPER = (
    "Agents/Kourovka/problems/21.52/runs/"
    "2026-08-18-r9-alternating-double-transposition-reconstruction/"
    "pair_orbit_signatures.py"
)
m = SourceFileLoader("pair_sigs", HELPER).load_module()

N = 8
UNIVERSE = frozenset(range(N))
SUPPORTS = tuple(map(frozenset, combinations(range(N), 4)))
INDEX = {s: i for i, s in enumerate(SUPPORTS)}
FIBRES = tuple(m.matchings(tuple(sorted(s))) for s in SUPPORTS)
PERMS = tuple(permutations(range(3)))
P = [[m.permutation(x, N) for x in fibre] for fibre in FIBRES]


def matrix(i, j):
    return tuple(
        tuple(m.order(m.compose(P[i][a], P[j][b])) for b in range(3))
        for a in range(3)
    )


MATRICES = {}
ALLOWED = {}
NEIGHBOURS = [set() for _ in SUPPORTS]
for i, s in enumerate(SUPPORTS):
    ic = INDEX[UNIVERSE - s]
    for j in range(i + 1, len(SUPPORTS)):
        t = SUPPORTS[j]
        jc = INDEX[UNIVERSE - t]
        a = matrix(i, j)
        b = matrix(ic, jc)
        allowed = set()
        for u, pu in enumerate(PERMS):
            for v, pv in enumerate(PERMS):
                if all(a[r][q] == b[pu[r]][pv[q]]
                       for r in range(3) for q in range(3)):
                    allowed.add((u, v))
        if len(allowed) < 36:
            ALLOWED[i, j] = allowed
            NEIGHBOURS[i].add(j)
            NEIGHBOURS[j].add(i)


def compatible(i, di, j, dj):
    if i < j:
        return (di, dj) in ALLOWED.get((i, j), ALL)
    return (dj, di) in ALLOWED.get((j, i), ALL)


ALL = {(i, j) for i in range(6) for j in range(6)}


def propagate(domains, queue):
    queue = list(queue)
    while queue:
        i, j = queue.pop()
        new_i = {di for di in domains[i]
                 if any(compatible(i, di, j, dj) for dj in domains[j])}
        if new_i != domains[i]:
            if not new_i:
                return False
            domains[i] = new_i
            queue.extend((k, i) for k in NEIGHBOURS[i] if k != j)
    return True


nodes = 0


def solve(domains):
    global nodes
    nodes += 1
    if not propagate(domains, ((i, j) for i in range(len(SUPPORTS))
                               for j in NEIGHBOURS[i])):
        return None
    undecided = [i for i, d in enumerate(domains) if len(d) > 1]
    if not undecided:
        return domains
    i = min(undecided, key=lambda q: len(domains[q]))
    for value in sorted(domains[i]):
        branch = [set(d) for d in domains]
        branch[i] = {value}
        answer = solve(branch)
        if answer is not None:
            return answer
    return None


domains = [set(range(6)) for _ in SUPPORTS]
# Normalize one fibre using a point permutation preserving its complement pair.
domains[0] = {0}
answer = solve(domains)
print("supports", len(SUPPORTS))
print("nontrivial_pair_constraints", len(ALLOWED))
print("search_nodes", nodes)
print("complement_lift_exists", answer is not None)
if answer is not None:
    chosen = [next(iter(d)) for d in answer]
    print("chosen_domain_indices", chosen)

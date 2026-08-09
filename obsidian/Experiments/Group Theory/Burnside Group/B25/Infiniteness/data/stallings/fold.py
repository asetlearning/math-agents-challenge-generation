#!/usr/bin/env python3
"""Exact membership of a word in H_M = <d^5 : d reduced word over {a,b}, 1 <= |d| <= M>
via Stallings folding. H_M is an ordinary (non-normal) subgroup of F2; H_M increases to
the verbal subgroup F^5 as M -> infinity. So:  target in H_M  =>  target = 1 in B(2,5);
target not in H_M  =>  "not a product of fifth powers with root length <= M" (exact theorem).

Labels: 0=a,1=b,2=A,3=B ; inverse label = l^2 (xor 2).
Folding: worklist algorithm with union-find, adjacency = list of dicts.
"""
import sys
from collections import deque

INV = {0: 2, 1: 3, 2: 0, 3: 1}
C2L = {'a': 0, 'b': 1, 'A': 2, 'B': 3}

class Graph:
    def __init__(self):
        self.parent = []
        self.adj = []          # vertex -> {label: neighbor}
        self.base = self.new_vertex()

    def new_vertex(self):
        self.parent.append(len(self.parent))
        self.adj.append({})
        return len(self.parent) - 1

    def find(self, v):
        p = self.parent
        while p[v] != v:
            p[v] = p[p[v]]
            v = p[v]
        return v

    def add_word_loop(self, labels):
        """Attach a loop at base spelling `labels` (list of 0..3)."""
        cur = self.find(self.base)
        n = len(labels)
        for i, l in enumerate(labels):
            nxt = self.find(self.base) if i == n - 1 else self.new_vertex()
            self._add_edge(cur, l, nxt)
            cur = nxt

    def _add_edge(self, u, l, v):
        u, v = self.find(u), self.find(v)
        # record both directions; conflicts resolved in fold()
        self._set(u, l, v)
        self._set(v, INV[l], u)

    def _set(self, u, l, v):
        a = self.adj[u]
        if l in a:
            w = self.find(a[l])
            if w != v:
                self.pending.append((w, v))
            # keep existing; merge will unify
        else:
            a[l] = v

    def fold(self):
        # iterate: find any vertex with two same-label edges -> merge targets
        self.pending = deque()
        # initial scan: adj dicts can't hold duplicates, but merges create them via merge step
        changed = True
        while changed:
            changed = False
            for u in range(len(self.adj)):
                if self.parent[u] != u:
                    continue
                a = self.adj[u]
                for l in list(a.keys()):
                    a[l] = self.find(a[l])
            # duplicates within a dict are impossible; the real work happens in merge()
            while self.pending:
                x, y = self.pending.popleft()
                self.merge(x, y)
                changed = True

    def merge(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        # merge smaller adjacency into larger
        if len(self.adj[x]) < len(self.adj[y]):
            x, y = y, x
        self.parent[y] = x
        ax, ay = self.adj[x], self.adj[y]
        for l, w in ay.items():
            w = self.find(w)
            if l in ax:
                w2 = self.find(ax[l])
                if w != w2:
                    self.pending.append((w, w2))
            else:
                ax[l] = w
        self.adj[y] = {}

    def build(self, words):
        self.pending = deque()
        for labels in words:
            self.add_word_loop(labels)
        # full fold to fixpoint
        while True:
            # normalize adjacency
            for u in range(len(self.adj)):
                if self.parent[u] == u:
                    a = self.adj[u]
                    for l in list(a.keys()):
                        a[l] = self.find(a[l])
            if not self.pending:
                break
            while self.pending:
                x, y = self.pending.popleft()
                self.merge(x, y)

    def accepts(self, labels):
        v = self.find(self.base)
        for l in labels:
            a = self.adj[v]
            if l not in a:
                return False
            v = self.find(a[l])
        return v == self.find(self.base)


def word_to_labels(w):
    return [C2L[c] for c in w]

def labels_to_5th_power(root):
    return root * 5

def gen_reduced_words(maxlen):
    """All reduced words over labels 0..3, length 1..maxlen, one per {w, w^-1} pair,
    skipping proper powers (d = f^k => d^5 in <f^5>)."""
    out = []
    def inv_labels(ls):
        return [INV[l] for l in reversed(ls)]
    def is_proper_power(ls):
        n = len(ls)
        for p in range(1, n):
            if n % p == 0 and ls == ls[:p] * (n // p):
                return True
        return False
    stack = [[l] for l in range(4)]
    while stack:
        w = stack.pop()
        iw = inv_labels(w)
        if w <= iw and not is_proper_power(w):
            out.append(w)
        if len(w) < maxlen:
            for l in range(4):
                if l != INV[w[-1]]:
                    stack.append(w + [l])
    return out

def main():
    M = int(sys.argv[1])
    targets_file = sys.argv[2]
    roots = gen_reduced_words(M)
    words = [labels_to_5th_power(r) for r in roots]
    total_edges = sum(len(w) for w in words)
    print(f"M={M} roots={len(roots)} total_path_edges={total_edges}", flush=True)
    g = Graph()
    g.build(words)
    live = sum(1 for u in range(len(g.parent)) if g.parent[u] == u)
    print(f"folded: vertices={live}", flush=True)
    for line in open(targets_file):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        name, w = (line.split(None, 1) if ' ' in line else (line[:12] + '...', line))
        r = g.accepts(word_to_labels(w.strip()))
        print(f"MEMBER={r} M={M} {name}", flush=True)

if __name__ == '__main__':
    main()

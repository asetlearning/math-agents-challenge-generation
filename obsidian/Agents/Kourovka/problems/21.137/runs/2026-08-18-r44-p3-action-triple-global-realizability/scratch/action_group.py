#!/usr/bin/env python3
"""Exact F_3 matrix audit for the independently chosen root-action pair.

Basis is (x,y,u,v,z), with [x,y]=z and u,v,z central.  Matrices act
on column vectors.  This script only checks the finite local automorphism group;
it does not construct an ambient group and cannot certify a counterexample.
"""

from collections import deque, Counter

P = 3
N = 5


def ident():
    return tuple(1 if i == j else 0 for i in range(N) for j in range(N))


def mm(a, b):
    return tuple(
        sum(a[i * N + k] * b[k * N + j] for k in range(N)) % P
        for i in range(N)
        for j in range(N)
    )


def mpow(a, n):
    out = ident()
    while n:
        if n & 1:
            out = mm(out, a)
        a = mm(a, a)
        n //= 2
    return out


def inv(a):
    # All matrices used here have exponent dividing 9.
    return mpow(a, 8)


def comm(a, b):
    # [a,b]=a^-1 b^-1 a b.
    return mm(mm(inv(a), inv(b)), mm(a, b))


def matrix_from_columns(cols):
    return tuple(cols[j][i] % P for i in range(N) for j in range(N))


e = [tuple(1 if i == j else 0 for i in range(N)) for j in range(N)]
x, y, u, v, z = e


def add(*vs):
    return tuple(sum(q) % P for q in zip(*vs))


alpha = matrix_from_columns((x, add(y, u), add(u, v), add(v, z), z))
beta = matrix_from_columns((add(x, u), y, add(u, v), add(v, z), z))
# Canonical missing-diagonal completion: gamma^3=Inn(x+y).
gamma = matrix_from_columns((add(x, u), add(y, u, u), add(u, v), add(v, z), z))

# Inner actions by -x and y in the convention p -> a^-1 p a.
inn_minus_x = matrix_from_columns((x, add(y, z), u, v, z))
inn_y = matrix_from_columns((add(x, z), y, u, v, z))


def generated(gens):
    one = ident()
    seen = {one}
    todo = deque([one])
    while todo:
        g = todo.popleft()
        for h in gens:
            gh = mm(g, h)
            if gh not in seen:
                seen.add(gh)
                todo.append(gh)
    return seen


A = generated((alpha, beta))
I = generated((inn_minus_x, inn_y))
ab = mm(alpha, beta)
d = comm(alpha, beta)

print("alpha^3_is_inn_minus_x", mpow(alpha, 3) == inn_minus_x)
print("beta^3_is_inn_y", mpow(beta, 3) == inn_y)
print("(alpha_beta)^3_columns", [tuple(mpow(ab, 3)[i*N+j] for i in range(N)) for j in range(N)])
print("alpha_beta_order", next(k for k in range(1, 28) if mpow(ab, k) == ident()))
print("commutator_order", next(k for k in range(1, 28) if mpow(d, k) == ident()))
print("A_order", len(A))
print("I_order", len(I), "I_subset_A", I <= A)
print("Q_order_A_mod_I", len(A) // len(I))
print("A_element_orders", dict(sorted(Counter(next(k for k in (1, 3, 9, 27) if mpow(g, k) == ident()) for g in A).items())))

# Test normality of I in A and enumerate quotient cosets.
print("I_normal_in_A", all(mm(mm(inv(g), h), g) in I for g in A for h in I))
Acubes = {mpow(g, 3) for g in A}
print("A_literal_cube_count", len(Acubes), "A_cubes_equal_I", Acubes == I)
def inner_label(g):
    # g(x)=x+Bz and g(y)=y-Az is conjugation by A*x+B*y.
    B = g[4*N+0]
    Acoord = (-g[4*N+1]) % 3
    return (Acoord, B)
print("A_cube_inner_labels", sorted(inner_label(g) for g in Acubes))
print("missing_inner_labels", sorted({(a,b) for a in range(3) for b in range(3)}
                                     - {inner_label(g) for g in Acubes}))
unseen = set(A)
cosets = []
while unseen:
    g = next(iter(unseen))
    c = frozenset(mm(g, h) for h in I)
    cosets.append(c)
    unseen -= c
print("quotient_cosets", len(cosets))

# Central fixed-vector test for the prospective product label
# c = -x+y-u-v, expected fixed by alpha*beta.
c = tuple(q % P for q in (-1, 1, -1, -1, 0))
def mv(a, w):
    return tuple(sum(a[i*N+j]*w[j] for j in range(N)) % P for i in range(N))
print("product_label_fixed", mv(ab, c) == c, "label", c)

# Cheap action-only completion diagnostic.  This is not an extension or group
# witness; it only tests the necessary complete-action cube-cover gate.
B = generated((alpha, beta, gamma))
Bcubes = {mpow(g, 3) for g in B}
print("completed_action_B_order", len(B))
print("gamma^3_label", inner_label(mpow(gamma, 3)), "gamma_fixes_x_plus_y", mv(gamma, add(x,y)) == add(x,y))
print("B_literal_cube_count", len(Bcubes), "B_cubes_equal_I", Bcubes == I)

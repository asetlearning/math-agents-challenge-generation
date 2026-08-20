#!/usr/bin/env python3
"""Complete exact cube audit of H=P semidirect <alpha,beta>.

This is a sharply fixed 3^10 group attached to the local action triple.  It is a
method test: a hit would still need an independent presentation certificate.
"""

from collections import deque, Counter

F = 3
N = 5


def madd(*vs):
    return tuple(sum(t) % F for t in zip(*vs))


def mid():
    return tuple(1 if i == j else 0 for i in range(N) for j in range(N))


def mm(a, b):
    return tuple(
        sum(a[i*N+k] * b[k*N+j] for k in range(N)) % F
        for i in range(N) for j in range(N)
    )


def mv(a, w):
    return tuple(sum(a[i*N+j] * w[j] for j in range(N)) % F for i in range(N))


def matrix_from_columns(cols):
    return tuple(cols[j][i] % F for i in range(N) for j in range(N))


e = [tuple(1 if i == j else 0 for i in range(N)) for j in range(N)]
x, y, u, v, z = e
alpha = matrix_from_columns((x, madd(y, u), madd(u, v), madd(v, z), z))
beta = matrix_from_columns((madd(x, u), y, madd(u, v), madd(v, z), z))


def generated_matrices(gens):
    one = mid()
    seen = {one}
    todo = deque([one])
    while todo:
        g = todo.popleft()
        for h in gens:
            gh = mm(g, h)
            if gh not in seen:
                seen.add(gh)
                todo.append(gh)
    return tuple(sorted(seen))


A = generated_matrices((alpha, beta))
A_index = {a: i for i, a in enumerate(A)}
A_mul = [[A_index[mm(a,b)] for b in A] for a in A]
Aid = A_index[mid()]

# P coordinate product: (a,b,u,v,c)(a',b',u',v',c') has central
# Heisenberg carry a*b' in z.  Thus [x,y]=z.
Pels = tuple((a,b,c,d,e0) for a in range(3) for b in range(3)
             for c in range(3) for d in range(3) for e0 in range(3))
P_index = {p:i for i,p in enumerate(Pels)}


def pmul(p, q):
    return ((p[0]+q[0])%3, (p[1]+q[1])%3,
            (p[2]+q[2])%3, (p[3]+q[3])%3,
            (p[4]+q[4]+p[0]*q[1])%3)


def pact(ai, p):
    return mv(A[ai], p)


# Verify the fixed matrices really act on this exact coordinate group.
for g in (A_index[alpha], A_index[beta]):
    for p in Pels:
        for q in Pels:
            assert pact(g, pmul(p,q)) == pmul(pact(g,p), pact(g,q))


# H element is (P-index, A-index); (p,a)(q,b)=(p*a(q),ab).
def hmul(g, h):
    p, a = g
    q, b = h
    return (P_index[pmul(Pels[p], pact(a, Pels[q]))], A_mul[a][b])


one = (P_index[(0,0,0,0,0)], Aid)


def hpow(g, n):
    out = one
    while n:
        if n & 1:
            out = hmul(out, g)
        g = hmul(g, g)
        n //= 2
    return out


H = tuple((p,a) for a in range(len(A)) for p in range(len(Pels)))
cubes = {hpow(g,3) for g in H}
orders = Counter()
bad_exp = None
for g in H:
    if hpow(g,9) != one:
        bad_exp = g
        break
    orders[next(k for k in (1,3,9) if hpow(g,k)==one)] += 1

closure_defect = None
cube_list = sorted(cubes)
for g in cube_list:
    for h in cube_list:
        gh = hmul(g,h)
        if gh not in cubes:
            closure_defect = (g,h,gh)
            break
    if closure_defect:
        break

noncommuting = None
for g in cube_list:
    for h in cube_list:
        if hmul(g,h) != hmul(h,g):
            noncommuting = (g,h)
            break
    if noncommuting:
        break

print("P_order", len(Pels), "A_order", len(A), "H_order", len(H))
print("all_action_checks", True)
print("exponent_divides_9", bad_exp is None, "order_distribution", dict(orders))
print("literal_cube_count", len(cubes))
print("cube_set_closed", closure_defect is None)
print("closure_defect", closure_defect)
print("noncommuting_cube_pair", noncommuting)
print("cube_projection_to_A_count", len({a for _,a in cubes}))


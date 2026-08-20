#!/usr/bin/env python3
"""Build exact unordered common-neighbour polynomial separation certificates."""

from collections import defaultdict
from math import factorial
import sys


def gbinom(a, j):
    """Polynomial binomial a(a-1).../j!, valid also for negative integer a."""
    z = 1
    for t in range(j):
        z *= a - t
    return z // factorial(j)


def shifted_coeff(local, m, base=14):
    """Convert sum local[j] C(n-m,j) to sum out[k] C(n-base,k)."""
    values = []
    for t in range(9):
        n = base + t
        values.append(sum(local[j] * gbinom(n-m, j) for j in range(9)))
    out = []
    row = values
    for _ in range(9):
        out.append(row[0])
        row = [row[i+1]-row[i] for i in range(len(row)-1)]
    return tuple(out)


def vec_sub(a, b):
    return tuple(x-y for x,y in zip(a,b))


def sign_kind(a):
    # Since C(n-14,k)=0 for k>0 at n=14, a nonzero constant coefficient
    # is required for the advertised all-integer n>=14 certificate.
    if a[0] > 0 and all(x >= 0 for x in a):
        return "+"
    if a[0] < 0 and all(x <= 0 for x in a):
        return "-"
    return None


def main(path):
    sig = {}
    raw = defaultdict(lambda: [0]*9)
    totals = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            row = line.rstrip("\n").split("\t")
            if row[0] == "SIG":
                i = int(row[1])
                sig[i] = dict(common=int(row[2]), m=int(row[3]), label=row[4],
                              x=row[5], y=row[6], pair_order=int(row[7]))
            elif row[0] == "TOTAL":
                i,j,got,want = map(int,row[1:])
                if got != want:
                    raise AssertionError((i,j,got,want))
                totals[i,j] = got
            elif row[0] == "C":
                i,j,p,q,c = map(int,row[1:])
                if p == 1 or q == 1:
                    continue             # endpoints are not graph common neighbours
                u=(min(p,q),max(p,q))
                raw[i,u][j] += c

    ids=sorted(sig)
    assert ids == list(range(len(ids)))
    assert all((i,j) in totals for i in ids for j in range(9))
    # For p=q the raw entry was added once; for p<q both orientations enter u.
    shifted={}
    allcoords=set()
    for i in ids:
        coords={u for ii,u in raw if ii==i}
        allcoords |= coords
        for u in coords:
            shifted[i,u]=shifted_coeff(raw[i,u],sig[i]["m"])

    common=[i for i in ids if sig[i]["common"]]
    none=[i for i in ids if not sig[i]["common"]]
    coords=sorted(allcoords, key=lambda u:(u[0]!=u[1], max(u), min(u)))
    cert=[]
    unresolved=[]
    for a in common:
        for b in none:
            candidates=[]
            for u in coords:
                va=shifted.get((a,u),(0,)*9)
                vb=shifted.get((b,u),(0,)*9)
                d=vec_sub(va,vb)
                sk=sign_kind(d)
                if sk:
                    # Prefer sparse, low-order, and a large absolute value at n=14.
                    score=(sum(x!=0 for x in d), max(u), u, -abs(d[0]))
                    candidates.append((score,u,sk,d))
            if not candidates:
                unresolved.append((a,b))
            else:
                _,u,sk,d=min(candidates)
                cert.append((a,b,u,sk,d))

    print("META\tformat\tFOUR_MATCHING_SEPARATION_V1")
    print(f"META\tsignatures\t{len(ids)}")
    print(f"META\tcommon_signatures\t{len(common)}")
    print(f"META\tno_common_signatures\t{len(none)}")
    print(f"META\topposite_pairs\t{len(common)*len(none)}")
    print(f"META\tcoefficientwise_sign_certificates\t{len(cert)}")
    print(f"META\tunresolved_pairs\t{len(unresolved)}")
    print(f"META\tcoordinate_count\t{len(coords)}")
    for i in ids:
        s=sig[i]
        print("SIG",i,s["common"],s["m"],s["label"],s["pair_order"],s["x"],s["y"],sep="\t")
    for i in ids:
        for u in coords:
            local=raw.get((i,u),(0,)*9)
            sh=shifted.get((i,u),(0,)*9)
            if any(local) or any(sh):
                print("A",i,f"{u[0]},{u[1]}",",".join(map(str,local)),
                      ",".join(map(str,sh)),sep="\t")
    for a,b,u,sk,d in cert:
        print("CERT",a,b,f"{u[0]},{u[1]}",sk,",".join(map(str,d)),sep="\t")
    for a,b in unresolved:
        print("UNRESOLVED",a,b,sep="\t")
    return 0 if not unresolved else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1]))

#!/usr/bin/env python3
"""Farey gap-order false-control audit.

Computes Franel L2 discrepancy for the natural Farey order and for two
non-arithmetic reorderings of the exact same gap multiset.
"""

import argparse
import csv
import math


def farey_denominators(n):
    a, b, c, d = 0, 1, 1, n
    den = [1]
    while c <= n:
        den.append(d)
        k = (n + b) // d
        a, b, c, d = c, d, k * c - a, k * d - b
        if a == 1 and b == 1:
            break
    return den


def farey_gaps(n):
    den = farey_denominators(n)
    return [1.0 / (den[i] * den[i + 1]) for i in range(len(den) - 1)]


def energy(gaps):
    m = len(gaps)
    u = 1.0 / m
    s = 0.0
    e2 = 0.0
    max_abs = 0.0
    for j, g in enumerate(gaps):
        s += g - u
        if j + 1 < m:
            e2 += s * s
            max_abs = max(max_abs, abs(s))
    return e2, max_abs


def balanced_extreme(gaps):
    m = len(gaps)
    u = 1.0 / m
    dev = [g - u for g in gaps]
    pos = sorted((x for x in dev if x > 0.0), reverse=True)
    neg = sorted((x for x in dev if x < 0.0))
    ip = 0
    ineg = 0
    s = 0.0
    out = []
    while ip < len(pos) or ineg < len(neg):
        candidates = []
        if ip < len(pos):
            candidates.append(("p", pos[ip]))
        if ineg < len(neg):
            candidates.append(("n", neg[ineg]))
        typ, x = min(candidates, key=lambda tx: abs(s + tx[1]))
        out.append(x + u)
        s += x
        if typ == "p":
            ip += 1
        else:
            ineg += 1
    return out


def opposite_sign_extreme(gaps):
    m = len(gaps)
    u = 1.0 / m
    dev = [g - u for g in gaps]
    pos = sorted((x for x in dev if x > 0.0), reverse=True)
    neg = sorted((x for x in dev if x < 0.0))
    ip = 0
    ineg = 0
    s = 0.0
    out = []
    while ip < len(pos) or ineg < len(neg):
        if ip >= len(pos):
            x = neg[ineg]; ineg += 1
        elif ineg >= len(neg):
            x = pos[ip]; ip += 1
        elif s >= 0.0:
            x = neg[ineg]; ineg += 1
        else:
            x = pos[ip]; ip += 1
        out.append(x + u)
        s += x
    return out


def row(n):
    g = farey_gaps(n)
    ea, ma = energy(g)
    eb, mb = energy(balanced_extreme(g))
    eo, mo = energy(opposite_sign_extreme(g))
    return {
        "n": n,
        "gap_count": len(g),
        "actual_energy": ea,
        "n_actual_energy": n * ea,
        "balanced_energy": eb,
        "n_balanced_energy": n * eb,
        "balanced_to_actual": eb / ea,
        "opposite_energy": eo,
        "n_opposite_energy": n * eo,
        "opposite_to_actual": eo / ea,
        "actual_max_discrepancy": ma,
        "balanced_max_discrepancy": mb,
        "opposite_max_discrepancy": mo,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", nargs="+", type=int,
                    default=[50, 100, 200, 400, 800, 1200])
    ap.add_argument("--csv", default=None)
    args = ap.parse_args()
    rows = [row(n) for n in args.n]
    fields = list(rows[0])
    if args.csv:
        with open(args.csv, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader(); w.writerows(rows)
    print(",".join(fields))
    for r in rows:
        print(",".join(str(r[k]) for k in fields))


if __name__ == "__main__":
    main()

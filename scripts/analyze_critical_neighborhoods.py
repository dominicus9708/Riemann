#!/usr/bin/env python3
"""Analyze local multiplicative-channel structure around prime critical positions.

Purpose
-------
Compare prime centers with composite control centers after removing the strongest
small-prime residue bias by restricting centers to gcd(n, 30) == 1.

For a center c and radius r, excluding c itself, define

    L_omega(c,r) = (1/(2r)) * sum_{0<|h|<=r} omega(c+h)
    L_Omega(c,r) = (1/(2r)) * sum_{0<|h|<=r} Omega(c+h)

where omega counts distinct prime factors and Omega counts prime factors with
multiplicity. The script also counts neighboring prime positions.

Audit boundary
--------------
These are descriptive local statistics. They do not constitute a primality test,
a new theorem about prime distribution, or evidence for RH by themselves.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path


def sieve(N: int):
    spf = list(range(N + 1))
    if N >= 0:
        spf[0] = 0
    if N >= 1:
        spf[1] = 0
    for p in range(2, int(N ** 0.5) + 1):
        if spf[p] == p:
            for m in range(p * p, N + 1, p):
                if spf[m] == m:
                    spf[m] = p

    is_prime = [False] * (N + 1)
    omega = [0] * (N + 1)
    Omega = [0] * (N + 1)
    smallest = [0] * (N + 1)

    for n in range(2, N + 1):
        is_prime[n] = spf[n] == n
        x = n
        distinct = 0
        total = 0
        first = 0
        while x > 1:
            p = spf[x]
            if first == 0:
                first = p
            distinct += 1
            while x % p == 0:
                x //= p
                total += 1
        omega[n] = distinct
        Omega[n] = total
        smallest[n] = first

    return spf, is_prime, omega, Omega, smallest


def prefix(values):
    out = [0] * len(values)
    s = 0
    for i, v in enumerate(values):
        s += int(v)
        out[i] = s
    return out


def interval_sum(pref, lo: int, hi: int) -> int:
    return pref[hi] - (pref[lo - 1] if lo > 0 else 0)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=100000)
    ap.add_argument("--lo", type=int, default=1000)
    ap.add_argument("--hi", type=int, default=99000)
    ap.add_argument("--radii", default="3,5,10,20,50")
    ap.add_argument(
        "--summary",
        type=Path,
        default=Path("data/formation/critical_neighborhood_summary_100k.csv"),
    )
    ap.add_argument(
        "--spf-summary",
        type=Path,
        default=Path("data/formation/composite_spf_neighborhood_r5_100k.csv"),
    )
    args = ap.parse_args()

    radii = [int(x) for x in args.radii.split(",") if x.strip()]
    if args.lo <= max(radii) or args.hi + max(radii) > args.N:
        raise SystemExit("analysis range must leave room for the largest radius")

    _, is_prime, omega, Omega, smallest = sieve(args.N)
    p_omega = prefix(omega)
    p_Omega = prefix(Omega)
    p_prime = prefix([1 if x else 0 for x in is_prime])

    centers = [n for n in range(args.lo, args.hi + 1) if math.gcd(n, 30) == 1]

    args.summary.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "radius",
        "prime_centers",
        "wheel_composite_centers",
        "prime_mean_neighbor_omega",
        "composite_mean_neighbor_omega",
        "delta_omega_prime_minus_composite",
        "prime_mean_neighbor_Omega",
        "composite_mean_neighbor_Omega",
        "delta_Omega_prime_minus_composite",
        "prime_mean_neighbor_prime_count",
        "composite_mean_neighbor_prime_count",
        "delta_neighbor_primes",
    ]

    r5_rows = []
    with args.summary.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()

        for r in radii:
            by_class = {
                True: {"n": 0, "omega": 0.0, "Omega": 0.0, "primes": 0.0},
                False: {"n": 0, "omega": 0.0, "Omega": 0.0, "primes": 0.0},
            }

            for c in centers:
                denom = 2 * r
                om = (interval_sum(p_omega, c - r, c + r) - omega[c]) / denom
                Om = (interval_sum(p_Omega, c - r, c + r) - Omega[c]) / denom
                pc = interval_sum(p_prime, c - r, c + r) - int(is_prime[c])
                cls = is_prime[c]
                d = by_class[cls]
                d["n"] += 1
                d["omega"] += om
                d["Omega"] += Om
                d["primes"] += pc
                if r == 5 and not cls:
                    r5_rows.append((smallest[c], om, Om, pc))

            P = by_class[True]
            C = by_class[False]
            pm_o = P["omega"] / P["n"]
            cm_o = C["omega"] / C["n"]
            pm_O = P["Omega"] / P["n"]
            cm_O = C["Omega"] / C["n"]
            pm_p = P["primes"] / P["n"]
            cm_p = C["primes"] / C["n"]

            w.writerow({
                "radius": r,
                "prime_centers": P["n"],
                "wheel_composite_centers": C["n"],
                "prime_mean_neighbor_omega": f"{pm_o:.12f}",
                "composite_mean_neighbor_omega": f"{cm_o:.12f}",
                "delta_omega_prime_minus_composite": f"{pm_o-cm_o:.12f}",
                "prime_mean_neighbor_Omega": f"{pm_O:.12f}",
                "composite_mean_neighbor_Omega": f"{cm_O:.12f}",
                "delta_Omega_prime_minus_composite": f"{pm_O-cm_O:.12f}",
                "prime_mean_neighbor_prime_count": f"{pm_p:.12f}",
                "composite_mean_neighbor_prime_count": f"{cm_p:.12f}",
                "delta_neighbor_primes": f"{pm_p-cm_p:.12f}",
            })

    # Radius-5 composite-center stratification by smallest prime factor.
    buckets = {}
    for spf, om, Om, pc in r5_rows:
        b = buckets.setdefault(spf, [0, 0.0, 0.0, 0.0])
        b[0] += 1
        b[1] += om
        b[2] += Om
        b[3] += pc

    with args.spf_summary.open("w", newline="", encoding="utf-8") as f:
        fields2 = ["spf", "n", "mean_omega", "mean_Omega", "neighbor_primes"]
        w = csv.DictWriter(f, fieldnames=fields2)
        w.writeheader()
        for spf in sorted(buckets):
            n, so, sO, sp = buckets[spf]
            w.writerow({
                "spf": spf,
                "n": n,
                "mean_omega": f"{so/n:.12f}",
                "mean_Omega": f"{sO/n:.12f}",
                "neighbor_primes": f"{sp/n:.12f}",
            })


if __name__ == "__main__":
    main()

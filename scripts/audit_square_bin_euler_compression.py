#!/usr/bin/env python3
"""Numerical consistency audit for square-bin Euler compression.

For each ordinary prime p>=5, set q(p)=floor(sqrt(p))^2. The canonical
Beurling system has c_m copies of m^2, where c_m counts primes in
[m^2,(m+1)^2).

This script evaluates truncated real-axis logarithmic factor differences
H_X(sigma)=sum_{p<=X,p>=5}[-log(1-q(p)^(-sigma))+log(1-p^(-sigma))].

The exact theorem is analytic and does not depend on this computation.
The output is only a finite numerical consistency check.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import numpy as np


def primes_upto(n: int) -> np.ndarray:
    a = np.ones(n + 1, dtype=np.bool_)
    a[:2] = False
    for p in range(2, int(n**0.5) + 1):
        if a[p]:
            a[p * p : n + 1 : p] = False
    return np.flatnonzero(a).astype(np.int64)


def h_square_partial(primes: np.ndarray, X: int, sigma: float) -> float:
    total = 0.0
    for p0 in primes:
        p = int(p0)
        if p > X:
            break
        if p < 5:
            continue
        m = math.isqrt(p)
        q = m * m
        total += -math.log1p(-(q ** (-sigma))) + math.log1p(-(p ** (-sigma)))
    return total


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--kmin", type=int, default=12)
    ap.add_argument("--kmax", type=int, default=22)
    ap.add_argument("--kstep", type=int, default=2)
    ap.add_argument("--sigmas", default="0.50,0.52,0.55,0.60,0.75")
    ap.add_argument("--out", default="square_bin_euler_ratio_real_axis.csv")
    args = ap.parse_args()

    sigmas = [float(x.strip()) for x in args.sigmas.split(",") if x.strip()]
    Xmax = 2**args.kmax
    primes = primes_upto(Xmax)

    rows = []
    for k in range(args.kmin, args.kmax + 1, args.kstep):
        X = 2**k
        row: dict[str, float | int] = {"k": k, "X": X}
        for sigma in sigmas:
            row[f"H_sigma_{sigma:.2f}"] = h_square_partial(primes, X, sigma)
        rows.append(row)

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0].keys())
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    print(f"wrote {out}")


if __name__ == "__main__":
    main()

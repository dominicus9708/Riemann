#!/usr/bin/env python3
"""Audit the square-bin residual d_m=2 c_m log m-(2m+1).

The exact theorem proved in the companion note is
    sum_{m<=M} d_m = theta((M+1)^2)-(M+1)^2 + O(M),
so RH is equivalent to square-root-scale cancellation of these partial sums.

This script only reproduces finite numerical checks.
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


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--jmin", type=int, default=4)
    ap.add_argument("--jmax", type=int, default=11)
    ap.add_argument("--out", default="square_bin_residual_dyadic_M.csv")
    args = ap.parse_args()

    Mmax = 2**args.jmax
    Xmax = (Mmax + 1) ** 2
    primes = primes_upto(Xmax)

    c = np.zeros(Mmax + 1, dtype=np.int64)
    for m in range(2, Mmax + 1):
        lo = int(np.searchsorted(primes, m * m, side="left"))
        hi = int(np.searchsorted(primes, (m + 1) * (m + 1), side="left"))
        c[m] = hi - lo

    A = 0.0
    S = math.log(6.0)
    rows = []
    checkpoints = {2**j for j in range(args.jmin, args.jmax + 1)}

    for m in range(2, Mmax + 1):
        dm = 2.0 * c[m] * math.log(m) - (2 * m + 1)
        A += dm
        S += 2.0 * c[m] * math.log(m)

        if m not in checkpoints:
            continue

        x = (m + 1) ** 2
        pcut = primes[primes < x]
        theta = float(np.log(pcut.astype(float)).sum())
        norm = A / (m * math.log(m) ** 2)

        rows.append(
            {
                "M": m,
                "x_next_square": x,
                "c_M": int(c[m]),
                "residual_partial_sum": A,
                "S_minus_x": S - x,
                "theta_minus_x": theta - x,
                "compression_error_S_minus_theta": S - theta,
                "residual_over_M_log2M": norm,
            }
        )

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    print(f"wrote {out}")


if __name__ == "__main__":
    main()

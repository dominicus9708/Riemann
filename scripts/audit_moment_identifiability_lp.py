#!/usr/bin/env python3
"""Audit how much parity is determined by the first K omega-layer moments.

Input:
    data/formation/mobius_layer_counts_dyadic_24.csv

For each cutoff X and K, keep the exact factorial/binomial moments

    B_j = sum_r A_r * C(r,j),   j=0,...,K

fixed, require A_r >= 0 on the observed support, and solve two linear programs
for the minimum and maximum feasible parity sum

    sum_r (-1)^r A_r.

This is an information-relaxation audit.  Alternative feasible layer vectors
need not be realizable by actual sets of integers.

Dependencies: numpy, scipy.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import numpy as np
from scipy.optimize import linprog


def read_rows(path: Path):
    with path.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            yield row


def layer_vector(row):
    keys = sorted(
        (k for k in row if k.startswith("A") and k[1:].isdigit()),
        key=lambda s: int(s[1:]),
    )
    A = [int(row[k]) for k in keys]
    m = max(i for i, v in enumerate(A) if v != 0)
    return np.asarray(A[: m + 1], dtype=float)


def moment_matrix(m: int, K: int):
    C = np.zeros((K + 1, m + 1), dtype=float)
    for j in range(K + 1):
        for r in range(j, m + 1):
            C[j, r] = math.comb(r, j)
    return C


def audit_one(A: np.ndarray, K: int):
    m = len(A) - 1
    C = moment_matrix(m, K)
    b = C @ A
    parity = np.asarray([(-1.0) ** r for r in range(m + 1)])
    bounds = [(0.0, None)] * (m + 1)

    lo = linprog(parity, A_eq=C, b_eq=b, bounds=bounds, method="highs")
    hi = linprog(-parity, A_eq=C, b_eq=b, bounds=bounds, method="highs")
    if not (lo.success and hi.success):
        raise RuntimeError(f"LP failed at K={K}: {lo.message}; {hi.message}")
    return float(lo.fun), float(-hi.fun)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--input",
        type=Path,
        default=Path("data/formation/mobius_layer_counts_dyadic_24.csv"),
    )
    ap.add_argument(
        "--details",
        type=Path,
        default=Path("data/formation/parity_moment_identifiability_lp.csv"),
    )
    ap.add_argument(
        "--summary",
        type=Path,
        default=Path("data/formation/parity_moment_identifiability_summary.csv"),
    )
    args = ap.parse_args()

    detail_rows = []
    summary_rows = []

    for row in read_rows(args.input):
        X = int(row["X"])
        A = layer_vector(row)
        m = len(A) - 1
        actual = int(round(sum(((-1) ** r) * A[r] for r in range(m + 1))))
        sqrt_x = math.sqrt(X)

        first_all_within = None
        first_width = None
        for K in range(m + 1):
            lo, hi = audit_one(A, K)
            width = hi - lo
            maxdev = max(abs(lo - actual), abs(hi - actual))
            detail_rows.append(
                {
                    "X": X,
                    "max_omega": m,
                    "K": K,
                    "M": actual,
                    "min_feasible_M": lo,
                    "max_feasible_M": hi,
                    "interval_width": width,
                    "max_deviation_from_actual": maxdev,
                }
            )
            if first_all_within is None and maxdev <= sqrt_x:
                first_all_within = K
            if first_width is None and width <= 2.0 * sqrt_x:
                first_width = K

        summary_rows.append(
            {
                "X": X,
                "max_omega": m,
                "M": actual,
                "sqrt_X": sqrt_x,
                "first_K_all_feasible_within_sqrt": first_all_within,
                "first_K_interval_width_le_2sqrt": first_width,
            }
        )

    args.details.parent.mkdir(parents=True, exist_ok=True)
    with args.details.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=detail_rows[0].keys())
        w.writeheader()
        w.writerows(detail_rows)

    with args.summary.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=summary_rows[0].keys())
        w.writeheader()
        w.writerows(summary_rows)


if __name__ == "__main__":
    main()

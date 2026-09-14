#!/usr/bin/env python3
"""Audit the local phase boundary around t=pi for squarefree omega layers.

Uses exact layer counts A_r(X) to form

    H_X(t) = sum_r A_r(X) exp(i t r).

At t=pi,

    H_X(pi) = M(X)

and

    H_X'(pi)/i = sum_r r A_r(X) (-1)^r
                  = sum_{n<=X} mu(n) omega(n).

For each dyadic X the script finds the first positive delta satisfying

    |H_X(pi+delta)| = sqrt(X)

and compares it with the finite linear prediction

    sqrt(X-M(X)^2) / |sum mu omega|

and with the asymptotic first-order scale log(X)^2/sqrt(X).

Dependencies: numpy.
"""

from __future__ import annotations

import argparse
import cmath
import csv
import math
from pathlib import Path

import numpy as np


def read_rows(path: Path):
    with path.open(encoding="utf-8") as f:
        yield from csv.DictReader(f)


def layer_vector(row):
    keys = sorted(
        (k for k in row if k.startswith("A") and k[1:].isdigit()),
        key=lambda s: int(s[1:]),
    )
    A = [int(row[k]) for k in keys]
    m = max(i for i, v in enumerate(A) if v != 0)
    return A[: m + 1]


def abs_H(A, delta):
    t = math.pi + delta
    return abs(sum(a * cmath.exp(1j * t * r) for r, a in enumerate(A)))


def first_crossing(A, X, max_delta=0.8, grid=16000):
    target = math.sqrt(X)
    ds = np.linspace(0.0, max_delta, grid + 1)
    prev = 0.0
    for d in ds:
        if abs_H(A, float(d)) >= target:
            lo, hi = prev, float(d)
            for _ in range(60):
                mid = (lo + hi) / 2.0
                if abs_H(A, mid) >= target:
                    hi = mid
                else:
                    lo = mid
            return hi
        prev = float(d)
    return float("nan")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--input",
        type=Path,
        default=Path("data/formation/mobius_layer_counts_dyadic_24.csv"),
    )
    ap.add_argument(
        "--output",
        type=Path,
        default=Path("data/formation/parity_phase_boundary_dyadic_24.csv"),
    )
    args = ap.parse_args()

    out = []
    for row in read_rows(args.input):
        X = int(row["X"])
        M = int(row["M"])
        A = layer_vector(row)
        d1 = sum(r * a * ((-1) ** r) for r, a in enumerate(A))
        obs = first_crossing(A, X)
        lin = (
            math.sqrt(max(X - M * M, 0.0)) / abs(d1)
            if d1 != 0
            else float("nan")
        )
        asym = math.log(X) ** 2 / math.sqrt(X)
        out.append(
            {
                "X": X,
                "M": M,
                "sum_mu_omega": d1,
                "scaled_derivative": d1 * math.log(X) ** 2 / X,
                "observed_delta_to_absH_eq_sqrtX": obs,
                "linear_delta_using_actual_derivative": lin,
                "observed_over_linear": obs / lin if lin else float("nan"),
                "asymptotic_log2_over_sqrt": asym,
                "observed_over_asymptotic": obs / asym,
            }
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=out[0].keys())
        w.writeheader()
        w.writerows(out)


if __name__ == "__main__":
    main()

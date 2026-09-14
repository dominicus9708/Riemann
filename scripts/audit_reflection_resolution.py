#!/usr/bin/env python3
"""Finite-cutoff reflection-symmetry false control.

For an off-center symmetric pair beta=1/2+-delta, use the envelope

    S_delta(x) = x^(1/2+delta) + x^(1/2-delta)
               = 2 x^(1/2) cosh(delta log x).

Its local effective exponent is

    1/2 + delta tanh(delta log x).

The script also fits dyadic finite-window OLS exponents without privileging
1/2 in the regression.  This is a resolution/false-positive audit, not a
model asserting the existence of off-critical zeta zeros.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import numpy as np


def dyadic_ols(delta: float, k_min: int, k_max: int) -> float:
    k = np.arange(k_min, k_max + 1, dtype=float)
    a = (0.5 + delta) * k
    b = (0.5 - delta) * k
    m = np.maximum(a, b)
    log2_signal = m + np.log2(np.exp2(a - m) + np.exp2(b - m))
    return float(np.polyfit(k, log2_signal, 1)[0])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--deltas", default="0.001,0.002,0.005,0.01,0.02,0.03,0.05,0.1")
    ap.add_argument("--k-min", type=int, default=10)
    ap.add_argument("--k-max", type=int, default=75)
    ap.add_argument(
        "--out",
        type=Path,
        default=Path("data/mertens/reflection_resolution_false_control.csv"),
    )
    args = ap.parse_args()

    deltas = [float(x) for x in args.deltas.split(",") if x]
    rows = []
    for delta in deltas:
        rows.append(
            {
                "delta": delta,
                "k_min": args.k_min,
                "k_max": args.k_max,
                "delta_log_X": delta * args.k_max * math.log(2),
                "ols_effective_exponent": dyadic_ols(delta, args.k_min, args.k_max),
            }
        )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    print(f"conservative 1/log(X) scale at X=2^{args.k_max}: {1/(args.k_max*math.log(2)):.12g}")
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()

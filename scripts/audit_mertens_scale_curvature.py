#!/usr/bin/env python3
"""Audit multiplicative scale curvature of the Mertens function.

For dyadic published Mertens values this computes

    K_2(2^k) = M(2^(k-1))^2 - M(2^k) M(2^(k-2)).

Optionally, with mpmath installed, it also evaluates the finite known-zero
energy prediction

    2 * sum_{0<gamma, first m zeros}
        sin(gamma log 2)^2 / |rho zeta'(rho)|^2.

The zero-informed calculation is a reconstruction/audit, not an independent
RH argument.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import numpy as np


def read_dyadic(path: Path) -> dict[int, int]:
    out: dict[int, int] = {}
    with path.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            out[int(row["n"])] = int(row["M_2pow_n"])
    return out


def curvature_rows(M: dict[int, int], k_min: int, k_max: int):
    rows = []
    for k in range(k_min, k_max + 1):
        K = M[k - 1] ** 2 - M[k] * M[k - 2]
        X = 2**k
        rows.append(
            {
                "k": k,
                "K2": K,
                "K2_over_X": K / X,
                "abs_over_X": abs(K) / X,
            }
        )
    return rows


def slope_summary(rows):
    k = np.asarray([r["k"] for r in rows], dtype=float)
    y = np.log2(np.asarray([abs(r["K2"]) for r in rows], dtype=float))
    slope, intercept = np.polyfit(k, y, 1)
    return float(slope), float(intercept)


def zero_energy(counts: list[int]):
    try:
        import mpmath as mp
    except ImportError as exc:
        raise SystemExit("mpmath is required for --zero-counts") from exc

    mp.mp.dps = 30
    max_count = max(counts)
    h = mp.log(2)
    terms = []
    for j in range(1, max_count + 1):
        rho = mp.zetazero(j)
        zp = mp.diff(mp.zeta, rho)
        c = 1 / (rho * zp)
        terms.append(2 * abs(c) ** 2 * mp.sin(mp.im(rho) * h) ** 2)

    partial = []
    s = mp.mpf("0")
    wanted = set(counts)
    for j, term in enumerate(terms, start=1):
        s += term
        if j in wanted:
            partial.append((j, float(s)))
    return partial


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--input",
        type=Path,
        default=Path("data/mertens/mertens_powers_of_two_0_75.csv"),
    )
    ap.add_argument("--k-min", type=int, default=10)
    ap.add_argument("--k-max", type=int, default=75)
    ap.add_argument(
        "--out-curvature",
        type=Path,
        default=Path("data/mertens/mertens_scale_curvature_dyadic_10_75.csv"),
    )
    ap.add_argument(
        "--out-zero-energy",
        type=Path,
        default=Path("data/mertens/mertens_scale_curvature_zero_energy.csv"),
    )
    ap.add_argument(
        "--zero-counts",
        default="1,2,5,10,20,30,50,75,100",
        help="comma-separated positive integers; empty string skips zero calculation",
    )
    args = ap.parse_args()

    M = read_dyadic(args.input)
    rows = curvature_rows(M, args.k_min, args.k_max)
    args.out_curvature.parent.mkdir(parents=True, exist_ok=True)
    with args.out_curvature.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["k", "K2", "K2_over_X", "abs_over_X"])
        w.writeheader()
        w.writerows(rows)

    values = np.asarray([r["K2_over_X"] for r in rows], dtype=float)
    positive_rate = float(np.mean(np.asarray([r["K2"] for r in rows]) > 0))
    slope, _ = slope_summary(rows)
    empirical_mean = float(values.mean())

    print(f"samples={len(rows)}")
    print(f"positive_rate={positive_rate:.12g}")
    print(f"mean_K2_over_X={empirical_mean:.12g}")
    print(f"OLS_log2_absK_slope={slope:.12g}")
    print(f"naive_beta_eff={slope/2:.12g}")

    if args.zero_counts.strip():
        counts = sorted({int(x) for x in args.zero_counts.split(",") if x.strip()})
        preds = zero_energy(counts)
        args.out_zero_energy.parent.mkdir(parents=True, exist_ok=True)
        with args.out_zero_energy.open("w", newline="", encoding="utf-8") as f:
            fields = [
                "zero_count",
                "predicted_mean_K2_over_X",
                "empirical_mean_k10_75",
                "relative_difference_empirical_minus_prediction_over_prediction",
            ]
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            for m, pred in preds:
                w.writerow(
                    {
                        "zero_count": m,
                        "predicted_mean_K2_over_X": pred,
                        "empirical_mean_k10_75": empirical_mean,
                        "relative_difference_empirical_minus_prediction_over_prediction":
                            (empirical_mean - pred) / pred,
                    }
                )
        for m, pred in preds:
            print(f"zeros={m:3d} predicted_mean={pred:.12g}")


if __name__ == "__main__":
    main()

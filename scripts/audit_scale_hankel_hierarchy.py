#!/usr/bin/env python3
"""Audit higher scale-Hankel determinants of dyadic Mertens data.

For y_k=M(2^k), define

    H_r(k) = det[y_{k+i+j}]_{i,j=0}^{r-1}.

A finite exponential signal y_k=sum_l c_l q_l^k satisfies a Cauchy-Binet
mode-selection identity for these determinants.  The optional zero-informed
branch reconstructs y_k/sqrt(2^k) from the first m zeta zeros and compares the
resulting Hankel determinants with the published Mertens sequence.

The zero-informed calculation is an audit of spectral re-encoding, not an
independent argument for RH.
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


def bareiss_det(mat: list[list[int]]) -> int:
    a = [row[:] for row in mat]
    n = len(a)
    if n == 1:
        return a[0][0]
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = next((i for i in range(k + 1, n) if a[i][k] != 0), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * pivot - a[i][k] * a[k][j]) // prev
        prev = pivot
    return sign * a[-1][-1]


def actual_rows(M: dict[int, int], rank: int, k_min: int, k_max: int):
    rows = []
    for k in range(k_min, k_max - 2 * (rank - 1) + 1):
        mat = [[M[k + i + j] for j in range(rank)] for i in range(rank)]
        det = bareiss_det(mat)
        if det == 0:
            continue
        norm_exp = rank * k / 2 + rank * (rank - 1) / 2
        rows.append((k, det, det / (2.0**norm_exp)))
    return rows


def zero_wave(k_values: range, zero_count: int):
    import mpmath as mp

    mp.mp.dps = 40
    coeffs = []
    for j in range(1, zero_count + 1):
        rho = mp.zetazero(j)
        zp = mp.diff(mp.zeta, rho)
        coeffs.append((mp.im(rho), 1 / (rho * zp)))

    h = mp.log(2)
    out = {}
    for k in k_values:
        z = mp.mpc(0)
        for gamma, c in coeffs:
            z += c * mp.e ** (1j * gamma * k * h)
        normalized = 2 * mp.re(z)
        out[k] = mp.power(2, mp.mpf(k) / 2) * normalized
    return out


def predicted_normalized_det(pred: dict[int, object], rank: int, k: int) -> float:
    import mpmath as mp

    mat = mp.matrix([[pred[k + i + j] for j in range(rank)] for i in range(rank)])
    det = mp.det(mat)
    norm_exp = mp.mpf(rank * k) / 2 + mp.mpf(rank * (rank - 1)) / 2
    return float(det / mp.power(2, norm_exp))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", type=Path, default=Path("data/mertens/mertens_powers_of_two_0_75.csv"))
    ap.add_argument("--out", type=Path, default=Path("data/mertens/scale_hankel_hierarchy_summary.csv"))
    ap.add_argument("--rank-min", type=int, default=2)
    ap.add_argument("--rank-max", type=int, default=8)
    ap.add_argument("--k-min", type=int, default=10)
    ap.add_argument("--k-max", type=int, default=75)
    ap.add_argument("--zero-count", type=int, default=100)
    args = ap.parse_args()

    M = read_dyadic(args.input)
    pred = zero_wave(range(0, args.k_max + 1), args.zero_count) if args.zero_count else None

    summary = []
    for rank in range(args.rank_min, args.rank_max + 1):
        rows = actual_rows(M, rank, args.k_min, args.k_max)
        ks = np.asarray([r[0] for r in rows], dtype=float)
        logs = np.asarray([math.log2(abs(r[1])) for r in rows], dtype=float)
        slope = float(np.polyfit(ks, logs, 1)[0])
        half = len(rows) // 2
        late_slope = float(np.polyfit(ks[half:], logs[half:], 1)[0])

        corr = float("nan")
        r2 = float("nan")
        if pred is not None:
            actual_norm = np.asarray([r[2] for r in rows], dtype=float)
            pred_norm = np.asarray(
                [predicted_normalized_det(pred, rank, int(r[0])) for r in rows],
                dtype=float,
            )
            corr = float(np.corrcoef(actual_norm, pred_norm)[0, 1])
            r2 = float(
                1
                - np.sum((actual_norm - pred_norm) ** 2)
                / np.sum((actual_norm - actual_norm.mean()) ** 2)
            )

        summary.append(
            {
                "rank": rank,
                "sample_count": len(rows),
                "ols_log2_absdet_slope": slope,
                "beta_eff_full": slope / rank,
                "late_half_beta_eff": late_slope / rank,
                f"first{args.zero_count}_zero_wave_corr": corr,
                f"first{args.zero_count}_zero_wave_R2": r2,
            }
        )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    fields = list(summary[0].keys())
    with args.out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(summary)

    for row in summary:
        print(row)


if __name__ == "__main__":
    main()

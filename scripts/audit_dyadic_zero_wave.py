#!/usr/bin/env python3
"""Audit dyadic Mertens oscillation against the first zeta-zero residue waves.

Input:
    data/mertens/mertens_powers_of_two_0_75.csv

For x=2^k and simple nontrivial zeros rho_j=1/2+i gamma_j, compare

    M(x)/sqrt(x)

with the truncated residue wave

    Z_m(x)=2 Re sum_{j<=m} exp(i gamma_j log x)/(rho_j zeta'(rho_j)).

This script is an audit/diagnostic only. It must not be used as an independent
RH argument, because the explanatory variables are zeta-zero data themselves.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import mpmath as mp
import numpy as np


def read_data(path: Path, lo: int, hi: int):
    rows = {}
    with path.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows[int(row["n"])] = int(row["M_2pow_n"])
    ks = np.arange(lo, hi + 1, dtype=np.int64)
    y = np.array([rows[int(k)] / (2.0 ** (int(k) / 2.0)) for k in ks])
    return ks, y


def sign_changes(a: np.ndarray) -> int:
    s = np.sign(a)
    return int(np.count_nonzero(s[1:] * s[:-1] < 0))


def lag1(a: np.ndarray) -> float:
    return float(np.corrcoef(a[:-1], a[1:])[0, 1])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", type=Path, default=Path("data/mertens/mertens_powers_of_two_0_75.csv"))
    ap.add_argument("--output", type=Path, default=Path("data/mertens/dyadic_zero_wave_residual_recomputed.csv"))
    ap.add_argument("--lo", type=int, default=10)
    ap.add_argument("--hi", type=int, default=75)
    ap.add_argument("--terms", default="0,1,2,5,10,20,30,40,50,75,100")
    ap.add_argument("--dps", type=int, default=40)
    args = ap.parse_args()

    terms = sorted({int(x) for x in args.terms.split(",")})
    max_terms = max(terms)
    ks, y = read_data(args.input, args.lo, args.hi)

    mp.mp.dps = args.dps
    zeros = [mp.zetazero(j) for j in range(1, max_terms + 1)]
    coeff = [1 / (rho * mp.diff(mp.zeta, rho)) for rho in zeros]

    waves = np.zeros((max_terms + 1, len(ks)), dtype=np.float64)
    running = np.zeros(len(ks), dtype=np.complex128)
    log2 = mp.log(2)
    for j, (rho, c) in enumerate(zip(zeros, coeff), start=1):
        gamma = mp.im(rho)
        for u, k in enumerate(ks):
            phase = mp.e ** (1j * gamma * int(k) * log2)
            running[u] += complex(c * phase)
        waves[j] = 2.0 * running.real

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow([
            "zero_terms_removed", "residual_RMS", "residual_lag1_corr",
            "residual_sign_changes", "corr_original_vs_zero_wave", "R2_zero_wave"
        ])
        denom = float(np.sum((y - y.mean()) ** 2))
        for m in terms:
            z = np.zeros_like(y) if m == 0 else waves[m]
            r = y - z
            corr = 0.0 if m == 0 else float(np.corrcoef(y, z)[0, 1])
            r2 = 0.0 if m == 0 else 1.0 - float(np.sum(r * r)) / denom
            w.writerow([
                m,
                f"{math.sqrt(float(np.mean(r*r))):.12f}",
                f"{lag1(r):.12f}",
                sign_changes(r),
                f"{corr:.12f}",
                f"{r2:.12f}",
            ])


if __name__ == "__main__":
    main()

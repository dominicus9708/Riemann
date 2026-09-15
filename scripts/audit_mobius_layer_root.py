#!/usr/bin/env python3
"""Audit the real zero of G_X(z)=sum_r A_r(X) z^r nearest z=-1.

Input: data/formation/mobius_layer_counts_dyadic_24.csv
Output fields reproduce data/formation/mobius_layer_root_near_minus1.csv.
Requires numpy only in addition to the standard library.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "formation" / "mobius_layer_counts_dyadic_24.csv"
OUTPUT = ROOT / "data" / "formation" / "mobius_layer_root_near_minus1.csv"


def load_rows(path: Path):
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            X = int(row["X"])
            M = int(row["M"])
            coeffs = []
            j = 0
            while f"A{j}" in row and row[f"A{j}"] != "":
                coeffs.append(int(row[f"A{j}"]))
                j += 1
            while coeffs and coeffs[-1] == 0:
                coeffs.pop()
            yield X, M, coeffs


def audit(X: int, M: int, A: list[int]):
    roots = np.roots(np.asarray(A[::-1], dtype=float))
    real_roots = sorted(
        (float(z.real) for z in roots if abs(float(z.imag)) <= 1e-8),
        key=lambda r: abs(r + 1.0),
    )
    nearest = real_roots[0] if real_roots else float("nan")
    nonreal = sum(abs(float(z.imag)) > 1e-8 for z in roots)

    gp = sum(r * A[r] * ((-1) ** (r - 1)) for r in range(1, len(A)))
    gpp = sum(
        r * (r - 1) * A[r] * ((-1) ** (r - 2))
        for r in range(2, len(A))
    )

    delta = nearest + 1.0 if math.isfinite(nearest) else float("nan")
    newton = -M / gp if gp else float("nan")
    simple_asymptotic = M * math.log(X) ** 2 / X

    return {
        "X": X,
        "M": M,
        "degree": len(A) - 1,
        "nonreal_root_count": nonreal,
        "nearest_real_root": nearest,
        "root_displacement": delta,
        "Gprime_minus1": gp,
        "Gsecond_minus1": gpp,
        "newton_displacement": newton,
        "root_over_newton": delta / newton if newton and math.isfinite(delta) else float("nan"),
        "M_log2_over_X": simple_asymptotic,
        "root_over_Mlog2X": delta / simple_asymptotic if simple_asymptotic and math.isfinite(delta) else float("nan"),
    }


def main():
    records = [audit(*row) for row in load_rows(INPUT)]
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)
    for rec in records:
        print(rec)


if __name__ == "__main__":
    main()

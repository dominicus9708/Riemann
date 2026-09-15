#!/usr/bin/env python3
"""Audit a square-root-local Beurling prime perturbation null.

Within each dyadic block [2^k,2^(k+1)), split into subblocks of length
ceil(2^(k/2)); inside each subblock, preserve the actual prime-gap multiset
and shuffle only its order.

The construction guarantees |q_j-p_j| = O(sqrt(p_j)), so the associated
Beurling Euler-product ratio with the classical zeta has an analytic,
nonvanishing continuation to Re(s)>1/2.

Finite computations below are diagnostics only and do not prove RH.
"""

from __future__ import annotations

import argparse
import bisect
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


def mobius_upto(n: int) -> np.ndarray:
    mu = np.ones(n + 1, dtype=np.int8)
    mu[0] = 0
    lp = np.zeros(n + 1, dtype=np.int32)
    ps: list[int] = []
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            ps.append(i)
            mu[i] = -1
        for p in ps:
            if p > lp[i] or i * p > n:
                break
            lp[i * p] = p
            if p == lp[i]:
                mu[i * p] = 0
            else:
                mu[i * p] = -mu[i]
    return mu


def sqrt_local_generators(
    primes: np.ndarray, X: int, seed: int, freeze: int = 100
) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    actual = primes[primes <= X].copy()
    pseudo = actual.copy()

    k0 = int(math.floor(math.log2(max(freeze + 1, 2))))
    k1 = int(math.floor(math.log2(X)))

    for k in range(k0, k1 + 1):
        dlo = 2**k
        dhi = min(2 ** (k + 1), X + 1)
        L = max(1, int(math.ceil(math.sqrt(dlo))))
        a = max(dlo, freeze + 1)

        while a < dhi:
            b = min(a + L, dhi)
            mask = (actual >= a) & (actual < b)
            inds = np.flatnonzero(mask)
            block = actual[mask]

            if block.size >= 2:
                anchor = a - 1
                gaps = np.diff(np.concatenate(([anchor], block))).astype(np.int64)
                rng.shuffle(gaps)
                pseudo[inds] = anchor + np.cumsum(gaps)

            a = b

    return actual, pseudo


def generalized_mobius_sum(gens: np.ndarray, X: int) -> int:
    g = [int(v) for v in gens if v <= X]
    total = 1

    def dfs(start: int, product: int, sign: int) -> None:
        nonlocal total
        end = bisect.bisect_right(g, X // product)
        for j in range(start, end):
            nxt = product * g[j]
            nsign = -sign
            total += nsign
            dfs(j + 1, nxt, nsign)

    dfs(0, 1, 1)
    return total


def generalized_integer_count(gens: np.ndarray, X: int) -> int:
    g = [int(v) for v in gens if v <= X]
    count = 1

    def dfs(start: int, product: int) -> None:
        nonlocal count
        for j in range(start, len(g)):
            q = g[j]
            if product * q > X:
                break
            value = product * q
            while value <= X:
                count += 1
                dfs(j + 1, value)
                if value > X // q:
                    break
                value *= q

    dfs(0, 1)
    return count


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--kmin", type=int, default=14)
    ap.add_argument("--kmax", type=int, default=20)
    ap.add_argument("--samples", type=int, default=20)
    ap.add_argument("--freeze", type=int, default=100)
    ap.add_argument("--out", default="beurling_sqrt_local_null_summary.csv")
    ap.add_argument("--ndef-out", default="beurling_sqrt_local_null_integer_defect.csv")
    args = ap.parse_args()

    rows = []
    nrows = []

    for k in range(args.kmin, args.kmax + 1):
        X = 2**k
        primes = primes_upto(X)
        actual_M = int(mobius_upto(X).sum())

        mvals = []
        s05 = []
        s055 = []
        s06 = []
        disp = []
        ndef = []

        for seed in range(args.samples):
            p, q = sqrt_local_generators(primes, X, seed, args.freeze)
            mask = p > args.freeze
            ratio = np.abs(q[mask] - p[mask]) / np.sqrt(p[mask])
            disp.append(float(np.max(ratio)) if ratio.size else 0.0)

            for sigma, bucket in [(0.5, s05), (0.55, s055), (0.6, s06)]:
                bucket.append(
                    float(
                        np.sum(
                            np.abs(np.log(q[mask] / p[mask]))
                            * p[mask].astype(float) ** (-sigma)
                        )
                    )
                )

            mvals.append(generalized_mobius_sum(q, X))
            if k <= 18:
                ndef.append(generalized_integer_count(q, X) - X)

        mean = float(np.mean(mvals))
        sd = float(np.std(mvals, ddof=1))
        rows.append(
            {
                "k": k,
                "X": X,
                "M_actual": actual_M,
                "M_null_mean": mean,
                "M_null_sd": sd,
                "M_z": (actual_M - mean) / sd if sd > 0 else float("nan"),
                "max_disp_over_sqrtp_max": max(disp),
                "S05_mean": float(np.mean(s05)),
                "S055_mean": float(np.mean(s055)),
                "S06_mean": float(np.mean(s06)),
            }
        )

        if ndef:
            nrows.append(
                {
                    "k": k,
                    "X": X,
                    "N_defect_mean": float(np.mean(ndef)),
                    "N_defect_sd": float(np.std(ndef, ddof=1)),
                    "N_defect_min": min(ndef),
                    "N_defect_max": max(ndef),
                }
            )

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    nout = Path(args.ndef_out)
    nout.parent.mkdir(parents=True, exist_ok=True)
    with nout.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(nrows[0].keys()))
        w.writeheader()
        w.writerows(nrows)

    print(f"wrote {out}")
    print(f"wrote {nout}")


if __name__ == "__main__":
    main()

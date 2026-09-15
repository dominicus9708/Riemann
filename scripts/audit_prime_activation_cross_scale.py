#!/usr/bin/env python3
"""Prime-activation cross-scale parity-coherence audit.

Reproduces the numerical diagnostics in
04_prime_connection/prime_activation_cross_scale_audit.md.

The null freezes primes <=100, preserves the prime-gap multiset in each dyadic
block, shuffles gap order, and treats pseudo-generators as independent Boolean
channels under the same product cutoff.

This is a numerical diagnostic, not a proof of RH.
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
    return np.flatnonzero(a)


def gap_permuted_generators(primes: np.ndarray, X: int, seed: int, freeze: int) -> list[int]:
    rng = np.random.default_rng(seed)
    actual = primes[primes <= X].astype(np.int64)
    out = actual[actual <= freeze].astype(int).tolist()
    lo = 2 ** int(math.floor(math.log2(max(freeze + 1, 2))))
    while lo <= X:
        hi = min(2 * lo, X + 1)
        block = actual[(actual >= max(lo, freeze + 1)) & (actual < hi)]
        if block.size:
            anchor = max(lo, freeze + 1) - 1
            gaps = np.diff(np.concatenate(([anchor], block))).astype(int)
            rng.shuffle(gaps)
            pseudo = anchor + np.cumsum(gaps)
            out.extend(int(v) for v in pseudo if v <= X)
        lo *= 2
    return sorted(set(out))


def enumerate_states(generators: list[int], X: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    products: list[int] = [1]
    signs: list[int] = [1]
    max_index: list[int] = [-1]

    def dfs(start: int, product: int, parity: int) -> None:
        end = bisect.bisect_right(generators, X // product)
        for j in range(start, end):
            nxt = product * generators[j]
            products.append(nxt)
            signs.append(-1 if parity == 0 else 1)
            max_index.append(j)
            dfs(j + 1, nxt, 1 - parity)

    dfs(0, 1, 0)
    return (
        np.asarray(products, dtype=np.int64),
        np.asarray(signs, dtype=np.int8),
        np.asarray(max_index, dtype=np.int32),
    )


def activation_profile(generators: list[int], X: int, freeze: int) -> dict[str, np.ndarray]:
    g = np.asarray(generators, dtype=np.int64)
    products, signs, mx = enumerate_states(generators, X)
    m = len(g)
    valid = mx >= 0
    counts = np.bincount(mx[valid], minlength=m).astype(np.int64)
    signed = np.bincount(mx[valid], weights=signs[valid], minlength=m).astype(np.int64)

    Q_before = 1 + np.concatenate(([0], np.cumsum(counts)[:-1]))
    F_before = 1 + np.concatenate(([0], np.cumsum(signed)[:-1]))

    # Label-visible cross-scale sector: X/p >= p.
    ids = np.flatnonzero((g > freeze) & (g * g <= X))
    values = g[ids]
    y = X // values

    low = products <= int(y.max())
    p_low = products[low]
    s_low = signs[low]
    m_low = mx[low]

    F1 = np.empty(len(ids), dtype=float)
    Q1 = np.empty(len(ids), dtype=float)
    for k, (j, yy) in enumerate(zip(ids, y)):
        mask = (p_low <= yy) & (m_low < j)
        F1[k] = float(s_low[mask].sum())
        Q1[k] = float(mask.sum())

    F0 = F_before[ids].astype(float)
    Q0 = Q_before[ids].astype(float)
    r0 = F0 / Q0
    r1 = F1 / Q1
    a = Q0 / (Q0 + Q1)
    b = Q1 / (Q0 + Q1)
    coherence = r0 + r1
    residual = r1 - r0
    dissipation = a * b * coherence**2

    return {
        "values": values,
        "r0": r0,
        "r1": r1,
        "coherence": coherence,
        "residual": residual,
        "dissipation": dissipation,
    }


def loo_profile(actual: np.ndarray, null: np.ndarray) -> tuple[float, float, float, float]:
    mean = null.mean(axis=0)
    sd = null.std(axis=0, ddof=1)
    z = np.divide(actual - mean, sd, out=np.full_like(actual, np.nan), where=sd > 0)
    amax = float(np.nanmax(np.abs(z)))
    amz2 = float(np.nanmean(z * z))

    loo_max = []
    loo_mz2 = []
    for i in range(null.shape[0]):
        others = np.delete(null, i, axis=0)
        m = others.mean(axis=0)
        s = others.std(axis=0, ddof=1)
        zz = np.divide(null[i] - m, s, out=np.full_like(actual, np.nan), where=s > 0)
        loo_max.append(np.nanmax(np.abs(zz)))
        loo_mz2.append(np.nanmean(zz * zz))

    return amax, float(np.mean(np.asarray(loo_max) >= amax)), amz2, float(np.mean(np.asarray(loo_mz2) >= amz2))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--X", type=int, default=2**18)
    ap.add_argument("--samples", type=int, default=20)
    ap.add_argument("--freeze", type=int, default=100)
    ap.add_argument("--seed0", type=int, default=3000)
    ap.add_argument("--out", default="prime_activation_cross_scale_summary.csv")
    args = ap.parse_args()

    primes = primes_upto(args.X)
    actual = activation_profile(primes.astype(int).tolist(), args.X, args.freeze)

    null_profiles = []
    for s in range(args.samples):
        generators = gap_permuted_generators(primes, args.X, args.seed0 + s, args.freeze)
        null_profiles.append(activation_profile(generators, args.X, args.freeze))

    fields = ["X", "channels", "observable", "metric", "actual", "null_mean", "null_sd", "null_exceed_fraction"]
    rows: list[dict[str, float | int | str]] = []

    for key in ["r0", "r1", "coherence", "residual", "dissipation"]:
        null = np.vstack([p[key] for p in null_profiles])
        amax, pmax, amz2, pmz2 = loo_profile(actual[key], null)
        rows.append({"X": args.X, "channels": len(actual["values"]), "observable": key, "metric": "profile_max_abs_z", "actual": amax, "null_mean": "", "null_sd": "", "null_exceed_fraction": pmax})
        rows.append({"X": args.X, "channels": len(actual["values"]), "observable": key, "metric": "profile_mean_z2", "actual": amz2, "null_mean": "", "null_sd": "", "null_exceed_fraction": pmz2})

    for key, metric in [("dissipation", "mean"), ("coherence", "rms"), ("residual", "rms")]:
        fn = (lambda x: float(np.mean(x))) if metric == "mean" else (lambda x: float(np.sqrt(np.mean(x * x))))
        av = fn(actual[key])
        nv = np.asarray([fn(p[key]) for p in null_profiles])
        rows.append({"X": args.X, "channels": len(actual["values"]), "observable": key, "metric": metric, "actual": av, "null_mean": float(nv.mean()), "null_sd": float(nv.std(ddof=1)), "null_exceed_fraction": float(np.mean(nv >= av))})

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    print(f"X={args.X} channels={len(actual['values'])}")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()

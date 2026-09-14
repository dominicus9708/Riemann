#!/usr/bin/env python3
"""Connected visibility-boundary flux null audit.

This script reproduces the singleton onset audit in
04_prime_connection/connected_boundary_flux_audit.md.

The pseudo-generator null freezes small primes, preserves the prime-gap multiset
inside each dyadic block, shuffles only the order of those gaps, and treats each
generator as an independent Boolean channel with all-minus character.

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

    j = int(math.floor(math.log2(max(freeze + 1, 2))))
    lo = 2**j
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


def enumerate_signed_products(generators: list[int], X: int) -> tuple[np.ndarray, np.ndarray]:
    """Enumerate independent-channel subset states by product cutoff.

    Duplicate numeric products from different channel subsets are intentionally
    retained: the state space is Boolean-channel space, not integer factorization
    of pseudo-generators.
    """

    g = list(map(int, generators))
    products: list[int] = [1]
    signs: list[int] = [1]

    def dfs(start: int, product: int, parity: int) -> None:
        end = bisect.bisect_right(g, X // product)
        for j in range(start, end):
            nxt = product * g[j]
            products.append(nxt)
            signs.append(-1 if parity == 0 else 1)
            dfs(j + 1, nxt, 1 - parity)

    dfs(0, 1, 0)
    arr = np.asarray(products, dtype=np.int64)
    sgn = np.asarray(signs, dtype=np.int8)
    order = np.argsort(arr, kind="stable")
    arr = arr[order]
    cumulative = np.cumsum(sgn[order], dtype=np.int64)
    return arr, cumulative


def cumulative_at(arr: np.ndarray, cumulative: np.ndarray, values: np.ndarray) -> np.ndarray:
    idx = np.searchsorted(arr, values.astype(np.int64), side="right") - 1
    return cumulative[idx]


def boundary_flux(generators: list[int], X: int, freeze: int) -> tuple[np.ndarray, np.ndarray]:
    arr, cumulative = enumerate_signed_products(generators, X)
    values = np.asarray([g for g in generators if freeze < g <= X], dtype=np.int64)
    # At Y=g, no state containing g and another channel can fit. The singleton
    # {g} contributes -1 to the total prefix, so excluding channel g adds +1.
    prefix_without_g = cumulative_at(arr, cumulative, values) + 1
    return values, 2 * prefix_without_g


def leave_one_out_metrics(null_matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    max_abs = []
    mean_z2 = []
    for i in range(null_matrix.shape[0]):
        others = np.delete(null_matrix, i, axis=0)
        mean = others.mean(axis=0)
        sd = others.std(axis=0, ddof=1)
        z = np.divide(
            null_matrix[i] - mean,
            sd,
            out=np.full(null_matrix.shape[1], np.nan, dtype=float),
            where=sd > 0,
        )
        max_abs.append(np.nanmax(np.abs(z)))
        mean_z2.append(np.nanmean(z * z))
    return np.asarray(max_abs), np.asarray(mean_z2)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--X", type=int, default=2**18)
    ap.add_argument("--samples", type=int, default=20)
    ap.add_argument("--freeze", type=int, default=100)
    ap.add_argument("--seed0", type=int, default=0)
    ap.add_argument("--out", default="connected_boundary_flux_summary.csv")
    args = ap.parse_args()

    primes = primes_upto(args.X)
    actual_generators = primes.astype(int).tolist()
    actual_values, actual_flux = boundary_flux(actual_generators, args.X, args.freeze)

    null_fluxes = []
    null_values = []
    for j in range(args.samples):
        g = gap_permuted_generators(primes, args.X, args.seed0 + j, args.freeze)
        values, flux = boundary_flux(g, args.X, args.freeze)
        if len(values) != len(actual_values):
            raise RuntimeError("null channel count changed; rank alignment invalid")
        null_values.append(values)
        null_fluxes.append(flux)

    null_flux = np.vstack(null_fluxes)
    mean = null_flux.mean(axis=0)
    sd = null_flux.std(axis=0, ddof=1)
    z = np.divide(
        actual_flux - mean,
        sd,
        out=np.full_like(mean, np.nan, dtype=float),
        where=sd > 0,
    )

    loo_max, loo_mean_z2 = leave_one_out_metrics(null_flux)
    actual_max = float(np.nanmax(np.abs(z)))
    actual_mean_z2 = float(np.nanmean(z * z))

    rows: list[dict[str, float | int | str]] = []
    rows.append(
        {
            "kind": "global",
            "band_k": -1,
            "count": len(actual_values),
            "actual_stat": actual_max,
            "null_mean": float(np.mean(loo_max)),
            "null_sd": float(np.std(loo_max, ddof=1)),
            "null_exceed_fraction": float(np.mean(loo_max >= actual_max)),
        }
    )
    rows.append(
        {
            "kind": "global_mean_z2",
            "band_k": -1,
            "count": len(actual_values),
            "actual_stat": actual_mean_z2,
            "null_mean": float(np.mean(loo_mean_z2)),
            "null_sd": float(np.std(loo_mean_z2, ddof=1)),
            "null_exceed_fraction": float(np.mean(loo_mean_z2 >= actual_mean_z2)),
        }
    )

    null_values_arr = [np.asarray(v) for v in null_values]
    band_actual = []
    band_null = []
    band_meta = []
    for k in range(int(math.log2(args.freeze + 1)), int(math.log2(args.X)) + 1):
        lo, hi = 2**k, min(2 ** (k + 1), args.X + 1)
        mask = (actual_values >= lo) & (actual_values < hi)
        if int(mask.sum()) < 5:
            continue
        a = float(np.sqrt(np.mean((actual_flux[mask] / np.sqrt(actual_values[mask])) ** 2)))
        nvals = np.asarray(
            [
                np.sqrt(
                    np.mean(
                        (null_flux[s, mask] / np.sqrt(null_values_arr[s][mask])) ** 2
                    )
                )
                for s in range(args.samples)
            ],
            dtype=float,
        )
        band_actual.append(a)
        band_null.append(nvals)
        band_meta.append((k, int(mask.sum())))

    band_actual_arr = np.asarray(band_actual)
    band_null_arr = np.vstack(band_null).T
    band_mean = band_null_arr.mean(axis=0)
    band_sd = band_null_arr.std(axis=0, ddof=1)
    band_z = (band_actual_arr - band_mean) / band_sd

    loo_band_max = []
    for i in range(args.samples):
        others = np.delete(band_null_arr, i, axis=0)
        m = others.mean(axis=0)
        s = others.std(axis=0, ddof=1)
        zz = (band_null_arr[i] - m) / s
        loo_band_max.append(np.nanmax(np.abs(zz)))
    loo_band_max = np.asarray(loo_band_max)
    actual_band_max = float(np.nanmax(np.abs(band_z)))

    for j, (k, count) in enumerate(band_meta):
        rows.append(
            {
                "kind": "band_rms_flux_over_sqrt_g",
                "band_k": k,
                "count": count,
                "actual_stat": float(band_actual_arr[j]),
                "null_mean": float(band_mean[j]),
                "null_sd": float(band_sd[j]),
                "null_exceed_fraction": float(np.mean(band_null_arr[:, j] >= band_actual_arr[j])),
            }
        )

    rows.append(
        {
            "kind": "band_global_max_abs_z",
            "band_k": -1,
            "count": len(band_meta),
            "actual_stat": actual_band_max,
            "null_mean": float(np.mean(loo_band_max)),
            "null_sd": float(np.std(loo_band_max, ddof=1)),
            "null_exceed_fraction": float(np.mean(loo_band_max >= actual_band_max)),
        }
    )

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    fields = ["kind", "band_k", "count", "actual_stat", "null_mean", "null_sd", "null_exceed_fraction"]
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    print(f"X={args.X} movable_channels={len(actual_values)}")
    print(f"actual max |z|={actual_max:.12g}; null exceed={np.mean(loo_max >= actual_max):.6g}")
    print(f"actual mean z^2={actual_mean_z2:.12g}; null exceed={np.mean(loo_mean_z2 >= actual_mean_z2):.6g}")
    print(f"actual band max |z|={actual_band_max:.12g}; null exceed={np.mean(loo_band_max >= actual_band_max):.6g}")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()

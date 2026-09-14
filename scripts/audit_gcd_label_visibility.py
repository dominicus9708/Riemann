#!/usr/bin/env python3
"""Exact gcd-label visibility and gap-permutation null audit.

This script refines omega(gcd)-sector diagnostics to exact common generator labels.
It is a numerical audit, not a proof of RH.
"""
from __future__ import annotations

import argparse
import bisect
import csv
import itertools
import math
from collections import defaultdict

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


def enumerate_states(gens: list[int], X: int) -> list[tuple[int, ...]]:
    g = np.asarray(gens, dtype=np.int64)
    states: list[tuple[int, ...]] = [()]

    def dfs(start: int, product: int, state: tuple[int, ...]) -> None:
        end = bisect.bisect_right(g, X // product)
        for j in range(start, end):
            nxt = state + (j,)
            states.append(nxt)
            dfs(j + 1, product * int(g[j]), nxt)

    dfs(0, 1, ())
    return states


def derivative_maps(states: list[tuple[int, ...]]) -> tuple[dict, dict]:
    signed: dict[tuple[int, ...], int] = defaultdict(int)
    positive: dict[tuple[int, ...], int] = defaultdict(int)
    for S in states:
        r = len(S)
        for k in range(r + 1):
            sign = -1 if ((r - k) & 1) else 1
            for A in itertools.combinations(S, k):
                positive[A] += 1
                signed[A] += sign
    return signed, positive


def singleton_exact(states, signed, positive, ngen: int):
    C = np.zeros(ngen, dtype=np.int64)
    N = np.zeros(ngen, dtype=np.int64)
    for B in states:
        if not B:
            continue
        coeff = -1 if ((len(B) - 1) & 1) else 1
        cterm = coeff * signed[B] * signed[B]
        nterm = coeff * positive[B] * positive[B]
        for j in B:
            C[j] += cterm
            N[j] += nterm
    C -= 1
    N -= 1
    rho = np.full(ngen, np.nan)
    mask = N > 0
    rho[mask] = C[mask] / N[mask]
    return C, N, rho


def selected_pair_exact(states, signed, positive, selected):
    selected = list(selected)
    selected_set = set(selected)
    C = {a: 0 for a in selected}
    N = {a: 0 for a in selected}
    for B in states:
        r = len(B)
        if r < 2:
            continue
        coeff = -1 if ((r - 2) & 1) else 1
        cterm = coeff * signed[B] * signed[B]
        nterm = coeff * positive[B] * positive[B]
        for A in itertools.combinations(B, 2):
            if A in selected_set:
                C[A] += cterm
                N[A] += nterm
    rho, counts = [], []
    for A in selected:
        c, n = C[A] - 1, N[A] - 1
        rho.append(c / n if n > 0 else np.nan)
        counts.append(n)
    return np.asarray(rho), np.asarray(counts)


def leave_one_out_global(null: np.ndarray, actual_z: np.ndarray):
    actual_max = float(np.nanmax(np.abs(actual_z)))
    actual_ms = float(np.nanmean(actual_z**2))
    null_max, null_ms = [], []
    for i in range(null.shape[0]):
        others = np.delete(null, i, axis=0)
        mean = np.nanmean(others, axis=0)
        sd = np.nanstd(others, axis=0, ddof=1)
        z = (null[i] - mean) / sd
        good = np.isfinite(z) & (sd > 1e-12)
        null_max.append(float(np.max(np.abs(z[good]))))
        null_ms.append(float(np.mean(z[good] ** 2)))
    return {
        "actual_max_abs_z": actual_max,
        "actual_mean_z2": actual_ms,
        "null_exceed_max_fraction": float(np.mean(np.asarray(null_max) >= actual_max)),
        "null_exceed_mean_z2_fraction": float(np.mean(np.asarray(null_ms) >= actual_ms)),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--X", type=int, default=2**18)
    ap.add_argument("--samples", type=int, default=20)
    ap.add_argument("--freeze", type=int, default=100)
    ap.add_argument("--min-pairs", type=int, default=1000)
    ap.add_argument("--seed0", type=int, default=0)
    ap.add_argument("--band-out", default="gcd_label_visibility_band.csv")
    ap.add_argument("--pair-out", default="gcd_label_visibility_pairs.csv")
    args = ap.parse_args()

    X = args.X
    primes = primes_upto(X)
    gens0 = primes.astype(int).tolist()
    states0 = enumerate_states(gens0, X)
    signed0, positive0 = derivative_maps(states0)
    C0, N0, rho0 = singleton_exact(states0, signed0, positive0, len(gens0))

    # Fully-visible two-prime candidates: q <= floor(X/(pq)).
    pair_candidates = []
    for i, p in enumerate(gens0):
        if p * p > X:
            break
        for j in range(i + 1, len(gens0)):
            q = gens0[j]
            if p * q > X:
                break
            Y = X // (p * q)
            if q > Y:
                break
            if q > args.freeze:
                pair_candidates.append((i, j))

    pair_rho0, pair_N0 = selected_pair_exact(states0, signed0, positive0, pair_candidates)
    keep = pair_N0 >= args.min_pairs
    pair_candidates = [a for a, k in zip(pair_candidates, keep) if k]
    pair_rho0 = pair_rho0[keep]
    pair_N0 = pair_N0[keep]

    singleton_null = []
    pair_null = []
    singleton_N_null = []
    for seed in range(args.seed0, args.seed0 + args.samples):
        gens = gap_permuted_generators(primes, X, seed, args.freeze)
        states = enumerate_states(gens, X)
        signed, positive = derivative_maps(states)
        _, Ns, rs = singleton_exact(states, signed, positive, len(gens))
        singleton_null.append(rs)
        singleton_N_null.append(Ns)
        rp, _ = selected_pair_exact(states, signed, positive, pair_candidates)
        pair_null.append(rp)

    singleton_null = np.asarray(singleton_null)
    singleton_N_null = np.asarray(singleton_N_null)
    pair_null = np.asarray(pair_null)

    # Singleton active-label region.
    mean_s = np.nanmean(singleton_null, axis=0)
    sd_s = np.nanstd(singleton_null, axis=0, ddof=1)
    z_s = (rho0 - mean_s) / sd_s
    active = (
        (np.asarray(gens0) > args.freeze)
        & (np.asarray(gens0) <= math.isqrt(X))
        & (N0 >= args.min_pairs)
        & np.isfinite(z_s)
        & (sd_s > 0)
    )
    singleton_global = leave_one_out_global(singleton_null[:, active], z_s[active])

    # Dyadic band aggregate.
    null_C = np.where(np.isfinite(singleton_null), singleton_null * singleton_N_null, 0.0)
    with open(args.band_out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["X", "band_lo", "band_hi", "channels", "ordered_offdiag_pairs", "actual_rho", "null_mean", "null_sd", "z"])
        k0 = int(math.floor(math.log2(max(args.freeze + 1, 2))))
        for k in range(k0, int(math.ceil(math.log2(X)))):
            lo, hi = 2**k, min(2 ** (k + 1), X + 1)
            mask = (np.asarray(gens0) >= lo) & (np.asarray(gens0) < hi) & (N0 > 0)
            if not np.any(mask):
                continue
            actual = C0[mask].sum() / N0[mask].sum()
            vals = []
            for r in range(args.samples):
                den = singleton_N_null[r, mask].sum()
                vals.append(null_C[r, mask].sum() / den if den > 0 else np.nan)
            vals = np.asarray(vals)
            mean, sd = np.nanmean(vals), np.nanstd(vals, ddof=1)
            z = (actual - mean) / sd if sd > 0 else np.nan
            w.writerow([X, lo, hi, int(mask.sum()), int(N0[mask].sum()), actual, mean, sd, z])

    # Fully-visible pair diagnostics.
    mean_p = np.nanmean(pair_null, axis=0)
    sd_p = np.nanstd(pair_null, axis=0, ddof=1)
    z_p = (pair_rho0 - mean_p) / sd_p
    good_p = np.isfinite(z_p) & (sd_p > 0)
    pair_global = leave_one_out_global(pair_null[:, good_p], z_p[good_p])

    with open(args.pair_out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["X", "p", "q", "ordered_offdiag_pairs", "actual_rho", "null_mean", "null_sd", "z", "fully_visible"])
        for idx, A in enumerate(pair_candidates):
            p, q = gens0[A[0]], gens0[A[1]]
            w.writerow([X, p, q, int(pair_N0[idx]), pair_rho0[idx], mean_p[idx], sd_p[idx], z_p[idx], 1])

    print(f"X={X} singleton_active={int(active.sum())} singleton_global={singleton_global}")
    print(f"X={X} fully_visible_pairs={len(pair_candidates)} pair_global={pair_global}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Gap-permutation null audit for weighted-threshold derivative energy.

The null model freezes small generators, preserves the prime-gap multiset inside
successive dyadic blocks, shuffles only the order of those gaps, and retains the
all-minus parity character on allowed subsets.

This is a diagnostic/null-model script, not part of a proof of RH.
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


def enumerate_allowed_subsets(generators: list[int], X: int) -> list[tuple[int, ...]]:
    g = np.asarray(generators, dtype=np.int64)
    states: list[tuple[int, ...]] = [()]

    def dfs(start: int, product: int, state: tuple[int, ...]) -> None:
        end = bisect.bisect_right(g, X // product)
        for j in range(start, end):
            nxt = state + (j,)
            states.append(nxt)
            dfs(j + 1, product * int(g[j]), nxt)

    dfs(0, 1, ())
    return states


def derivative_energies(states: list[tuple[int, ...]]) -> tuple[list[int], list[int]]:
    max_r = max(map(len, states))
    deriv = [defaultdict(int) for _ in range(max_r + 1)]
    baseline = [0] * (max_r + 1)

    for S in states:
        r = len(S)
        for k in range(r + 1):
            baseline[k] += math.comb(r, k)
            sign = -1 if ((r - k) & 1) else 1
            for A in itertools.combinations(S, k):
                deriv[k][A] += sign

    energy = [sum(v * v for v in d.values()) for d in deriv]
    return energy, baseline


def first_positive_crossover(energy: list[int], baseline: list[int]) -> float:
    coeff = np.asarray(energy, dtype=float) - np.asarray(baseline, dtype=float)
    roots = np.polynomial.polynomial.polyroots(coeff)
    positive = sorted(r.real for r in roots if abs(r.imag) < 1e-7 and r.real > 0)
    return positive[0] if positive else float("nan")


def run_one(X: int, samples: int, freeze: int, seed0: int) -> list[dict[str, float | int]]:
    primes = primes_upto(X)
    actual_states = enumerate_allowed_subsets(primes.astype(int).tolist(), X)
    e0, b0 = derivative_energies(actual_states)
    actual_root = first_positive_crossover(e0, b0)

    rows: list[dict[str, float | int]] = []
    for j in range(samples):
        seed = seed0 + j
        gens = gap_permuted_generators(primes, X, seed, freeze)
        states = enumerate_allowed_subsets(gens, X)
        energy, baseline = derivative_energies(states)
        root = first_positive_crossover(energy, baseline)
        row: dict[str, float | int] = {
            "X": X,
            "seed": seed,
            "actual_t_star": actual_root,
            "null_t_star": root,
            "generator_count": len(gens),
            "state_count": len(states),
        }
        for k in range(min(5, len(energy))):
            row[f"R{k}"] = energy[k] / baseline[k]
        rows.append(row)
    return rows


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--X", type=int, default=2**16)
    ap.add_argument("--samples", type=int, default=50)
    ap.add_argument("--freeze", type=int, default=100)
    ap.add_argument("--seed0", type=int, default=0)
    ap.add_argument("--out", default="derivative_energy_gap_null.csv")
    args = ap.parse_args()

    rows = run_one(args.X, args.samples, args.freeze, args.seed0)
    fields = ["X", "seed", "actual_t_star", "null_t_star", "generator_count", "state_count", "R0", "R1", "R2", "R3", "R4"]
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    roots = np.asarray([float(r["null_t_star"]) for r in rows], dtype=float)
    roots = roots[np.isfinite(roots)]
    print(f"X={args.X} actual_t_star={rows[0]['actual_t_star']:.12g}")
    if roots.size:
        print(
            f"null n={roots.size} mean={roots.mean():.12g} sd={roots.std(ddof=1):.12g} "
            f"min={roots.min():.12g} max={roots.max():.12g}"
        )


if __name__ == "__main__":
    main()

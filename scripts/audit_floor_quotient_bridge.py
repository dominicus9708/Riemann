#!/usr/bin/env python3
"""Audit floor-quotient representations of Mertens cancellation.

Two exact finite structures are checked.

1. Quotient-count matrix
       W[n,q] = floor(n/q)-floor(n/(q+1))
   and its inverse
       U[n,q] = M(floor(n/q))-M(floor(n/(q+1))).
   The identity U W = I is the finite matrix form of T_mu T_1 = I.

2. Lagarias--Richman floor-quotient poset bridge.
   For n=s(s+1), the lower and upper halves of Q[1,n] are disjoint and
       M(s) = - sum_{d=1}^s mu_1(d,n),
   where mu_1 is the two-variable Mobius function of the floor-quotient poset.

The script is an audit of representation/conditioning, not a proof of RH.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import numpy as np


def mobius_sieve(N: int) -> np.ndarray:
    mu = np.zeros(N + 1, dtype=np.int64)
    mu[1] = 1
    primes: list[int] = []
    composite = np.zeros(N + 1, dtype=np.bool_)
    for i in range(2, N + 1):
        if not composite[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > N:
                break
            composite[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def is_floor_quotient(d: int, n: int) -> bool:
    return 1 <= d <= n and n // (n // d) == d


def floor_quotients(n: int) -> list[int]:
    vals = set()
    k = 1
    while k <= n:
        q = n // k
        vals.add(q)
        k = n // q + 1
    return sorted(vals)


def fixed_top_mu1(n: int) -> dict[int, int]:
    Q = floor_quotients(n)
    out: dict[int, int] = {}
    for d in reversed(Q):
        if d == n:
            out[d] = 1
            continue
        total = 0
        for e, value in out.items():
            if is_floor_quotient(d, e):
                total += value
        out[d] = -total
    return out


def lower_half_rows(s_values: list[int]):
    max_s = max(s_values)
    mu = mobius_sieve(max_s)
    M = np.cumsum(mu, dtype=np.int64)
    rows = []
    for s in s_values:
        n = s * (s + 1)
        m1 = fixed_top_mu1(n)
        lower = [m1[d] for d in range(1, s + 1)]
        upper = [m1[n // k] for k in range(1, s + 1)]
        rows.append(
            {
                "s": s,
                "n_s_splus1": n,
                "M_s": int(M[s]),
                "upper_half_sum": sum(upper),
                "lower_half_sum": sum(lower),
                "l1_lower": sum(abs(v) for v in lower),
                "l2_lower": math.sqrt(sum(v * v for v in lower)),
                "max_abs_lower": max(abs(v) for v in lower),
                "nonzero_lower": sum(v != 0 for v in lower),
            }
        )
    return rows


def quotient_matrices(N: int):
    mu = mobius_sieve(N)
    M = np.cumsum(mu, dtype=np.int64)
    W = np.zeros((N, N), dtype=float)
    U = np.zeros((N, N), dtype=float)
    for n in range(1, N + 1):
        q = np.arange(1, n + 1, dtype=np.int64)
        W[n - 1, :n] = n // q - n // (q + 1)
        U[n - 1, :n] = M[n // q] - M[n // (q + 1)]
    return W, U


def condition_rows(N_values: list[int]):
    rows = []
    for N in N_values:
        W, U = quotient_matrices(N)
        sv = np.linalg.svd(W, compute_uv=False)
        rows.append(
            {
                "N": N,
                "sigma_max_W": float(sv[0]),
                "sigma_min_W": float(sv[-1]),
                "cond2_W": float(sv[0] / sv[-1]),
                "norm2_inverse": float(1 / sv[-1]),
                "max_inverse_row_l1": int(np.max(np.sum(np.abs(U), axis=1))),
                "inverse_product_error": float(np.max(np.abs(U @ W - np.eye(N)))),
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--s-values",
        default="4,8,16,32,64,128,256,512,1024,2048",
    )
    ap.add_argument("--matrix-N", default="16,32,64,128,256,512")
    ap.add_argument(
        "--out-poset",
        type=Path,
        default=Path("data/mertens/floor_quotient_lower_half_bridge.csv"),
    )
    ap.add_argument(
        "--out-matrix",
        type=Path,
        default=Path("data/mertens/quotient_matrix_conditioning.csv"),
    )
    args = ap.parse_args()

    s_values = [int(x) for x in args.s_values.split(",") if x]
    N_values = [int(x) for x in args.matrix_N.split(",") if x]
    poset = lower_half_rows(s_values)
    cond = condition_rows(N_values)
    write_csv(args.out_poset, poset)
    write_csv(args.out_matrix, cond)

    for row in poset:
        assert row["upper_half_sum"] == row["M_s"]
        assert row["lower_half_sum"] == -row["M_s"]
    for row in cond:
        assert row["inverse_product_error"] == 0.0

    print("floor-quotient lower-half bridge: exact for all requested s")
    print("quotient inverse product: exact for all requested N")


if __name__ == "__main__":
    main()

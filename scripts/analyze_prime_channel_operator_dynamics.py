#!/usr/bin/env python3
"""Audit canonical prime-channel dynamics for Möbius formation states.

For primes p <= y define

    F_y(x) = sum_{n<=x, squarefree, P+(n)<=y} mu(n).

Activating one prime channel p acts by

    (U_p f)(x) = f(x) - f(floor(x/p)).

Hence F_y is obtained by applying U_p over the primes p<=y to the
initial constant state. The script records the activation trajectory at
dyadic X and also the canonical largest-prime formation-tree residual

    R_X(m) = sum_{d<=X/m, P-(d)>P+(m)} mu(d).

This is an audit/diagnostic script. It does not claim a new RH result.
"""

from __future__ import annotations

import argparse
import csv
import math
from collections import defaultdict
from pathlib import Path

import numpy as np


def build_tables(N: int):
    is_prime = np.ones(N + 1, dtype=np.bool_)
    is_prime[:2] = False
    for p in range(2, int(N**0.5) + 1):
        if is_prime[p]:
            is_prime[p * p : N + 1 : p] = False
    primes = np.flatnonzero(is_prime).astype(np.int64)

    omega = np.zeros(N + 1, dtype=np.uint8)
    squarefree = np.ones(N + 1, dtype=np.bool_)
    squarefree[0] = False
    pmax = np.zeros(N + 1, dtype=np.int64)

    for p0 in primes:
        p = int(p0)
        omega[p : N + 1 : p] += 1
        pmax[p : N + 1 : p] = p
        pp = p * p
        if pp <= N:
            squarefree[pp : N + 1 : pp] = False

    mu = np.zeros(N + 1, dtype=np.int8)
    mu[1] = 1
    idx = squarefree & (np.arange(N + 1) >= 1)
    mu[idx] = np.where((omega[idx] % 2) == 0, 1, -1)
    pmax[1] = 1

    pi = np.cumsum(is_prime.astype(np.int64))
    return primes, is_prime, pi, omega, squarefree, pmax, mu


def primorial_threshold(primes, X: int):
    prod = 1
    last = 1
    next_prime = None
    for p0 in primes:
        p = int(p0)
        if prod <= X // p:
            prod *= p
            last = p
        else:
            next_prime = p
            break
    return last, prod, next_prime


def activation_metrics(X, primes, pi, squarefree, pmax, mu):
    signed_by_pmax = defaultdict(int)
    count_by_pmax = defaultdict(int)
    for n in range(1, X + 1):
        if squarefree[n]:
            p = int(pmax[n])
            signed_by_pmax[p] += int(mu[n])
            count_by_pmax[p] += 1

    F = signed_by_pmax[1]
    max_abs = abs(F)
    p_at_max = 1
    first_nonzero = None
    sign_changes = 0
    previous_sign = 0

    ordered = [int(p) for p in primes if p <= X]
    for p in ordered:
        F += signed_by_pmax[p]
        if F != 0:
            sign = 1 if F > 0 else -1
            if previous_sign and sign != previous_sign:
                sign_changes += 1
            previous_sign = sign
            if first_nonzero is None:
                first_nonzero = p
        if abs(F) > max_abs:
            max_abs = abs(F)
            p_at_max = p

    final_M = F

    half = X // 2
    F_half = signed_by_pmax[1]
    for p in ordered:
        if p > half:
            break
        F_half += signed_by_pmax[p]

    prime_tail = int(pi[X] - pi[half])
    return {
        "M": final_M,
        "first_nonzero_activation_prime": first_nonzero or 0,
        "max_abs_activation_state": max_abs,
        "prime_at_max_abs": p_at_max,
        "max_abs_over_X": max_abs / X,
        "abs_final_over_max_abs": (abs(final_M) / max_abs) if max_abs else 0.0,
        "F_at_X_over_2": F_half,
        "prime_count_X_over_2_to_X": prime_tail,
        "M_plus_prime_tail": final_M + prime_tail,
        "activation_sign_changes": sign_changes,
    }


def write_dyadic(args, primes, pi, squarefree, pmax, mu):
    args.dyadic.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "X",
        "M",
        "primorial_last_prime",
        "primorial_value",
        "next_prime",
        "first_nonzero_activation_prime",
        "max_abs_activation_state",
        "prime_at_max_abs",
        "max_abs_over_X",
        "abs_final_over_max_abs",
        "F_at_X_over_2",
        "prime_count_X_over_2_to_X",
        "M_plus_prime_tail",
        "activation_sign_changes",
    ]
    with args.dyadic.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for k in range(args.min_power, args.max_power + 1):
            X = 2**k
            last, primorial, next_prime = primorial_threshold(primes, X)
            row = activation_metrics(X, primes, pi, squarefree, pmax, mu)
            row.update(
                {
                    "X": X,
                    "primorial_last_prime": last,
                    "primorial_value": primorial,
                    "next_prime": next_prime or 0,
                }
            )
            w.writerow({name: row[name] for name in fields})


def write_tree_residual(args, squarefree, pmax):
    X = 2**args.max_power
    sf = squarefree[: X + 1]
    R = np.zeros(X + 1, dtype=np.int64)
    R[sf] = 1
    child_count = np.zeros(X + 1, dtype=np.int32)

    for n in range(2, X + 1):
        if sf[n]:
            parent = n // int(pmax[n])
            child_count[parent] += 1

    for n in range(X, 1, -1):
        if sf[n]:
            parent = n // int(pmax[n])
            R[parent] -= R[n]

    buckets = defaultdict(lambda: [0, 0.0, 0.0, 0, 0.0])
    raw = defaultdict(list)
    for m in range(2, X + 1):
        if not sf[m] or child_count[m] == 0:
            continue
        y = int(pmax[m])
        remaining = X / m
        u = math.log(remaining) / math.log(y)
        b = int(math.floor(u))
        raw[b].append(int(R[m]))
        a = buckets[b]
        a[0] += 1
        a[1] += float(R[m])
        a[2] += abs(float(R[m]))
        a[3] = max(a[3], abs(int(R[m])))
        a[4] += int(child_count[m])

    args.tree.parent.mkdir(parents=True, exist_ok=True)
    with args.tree.open("w", newline="", encoding="utf-8") as f:
        fields = [
            "floor_u",
            "nodes",
            "mean_R",
            "median_R",
            "mean_abs_R",
            "max_abs_R",
            "mean_children",
        ]
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for b in sorted(raw):
            vals = np.asarray(raw[b], dtype=np.float64)
            n, sum_R, sum_abs, max_abs, sum_children = buckets[b]
            w.writerow(
                {
                    "floor_u": b,
                    "nodes": n,
                    "mean_R": sum_R / n,
                    "median_R": float(np.median(vals)),
                    "mean_abs_R": sum_abs / n,
                    "max_abs_R": max_abs,
                    "mean_children": sum_children / n,
                }
            )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-power", type=int, default=10)
    ap.add_argument("--max-power", type=int, default=20)
    ap.add_argument(
        "--dyadic",
        type=Path,
        default=Path("data/formation/prime_channel_operator_dynamics_dyadic_20.csv"),
    )
    ap.add_argument(
        "--tree",
        type=Path,
        default=Path("data/formation/canonical_tree_residual_summary_2pow20.csv"),
    )
    args = ap.parse_args()

    N = 2**args.max_power
    primes, _, pi, _, squarefree, pmax, mu = build_tables(N)
    write_dyadic(args, primes, pi, squarefree, pmax, mu)
    write_tree_residual(args, squarefree, pmax)


if __name__ == "__main__":
    main()

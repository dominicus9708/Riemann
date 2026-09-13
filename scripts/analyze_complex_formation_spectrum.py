#!/usr/bin/env python3
"""Complex re-exploration of prime-channel / formation descriptors.

This script treats finite sums

    F_{f,N}(s) = sum_{n=2}^N f(n) n^{-s}

as finite Dirichlet polynomials only. They are NOT identified with analytic
continuations of infinite Dirichlet series inside 0 < Re(s) < 1.

Outputs compact audit summaries used by
04_prime_connection/complex_reexploration_audit.md.
"""

from __future__ import annotations

import argparse
import csv
import math
from collections import Counter
from functools import lru_cache
from pathlib import Path

import numpy as np


def sieve(N: int):
    spf = np.zeros(N + 1, dtype=np.int32)
    for i in range(2, N + 1):
        if spf[i] == 0:
            spf[i] = i
            if i * i <= N:
                for m in range(i * i, N + 1, i):
                    if spf[m] == 0:
                        spf[m] = i

    is_prime = np.zeros(N + 1, dtype=bool)
    omega = np.zeros(N + 1, dtype=np.int16)
    Omega = np.zeros(N + 1, dtype=np.int16)
    Lambda = np.zeros(N + 1, dtype=np.float64)

    for n in range(2, N + 1):
        is_prime[n] = spf[n] == n
        p = int(spf[n])
        m = n // p
        Omega[n] = Omega[m] + 1
        omega[n] = omega[m] + (1 if m == 1 or spf[m] != p else 0)

        x = n
        while x % p == 0:
            x //= p
        if x == 1:
            Lambda[n] = math.log(p)

    return spf, is_prime, omega, Omega, Lambda


def peeled_omega(spf, N: int, Q: int):
    out = np.zeros(N + 1, dtype=np.int16)
    for n in range(2, N + 1):
        p = int(spf[n])
        m = n // p
        out[n] = out[m] + (1 if p > Q and (m == 1 or spf[m] != p) else 0)
    return out


def complex_spectra(n, seqs, sigmas, ts, block=20):
    logs = np.log(n)
    columns = []
    labels = []
    denoms = []
    for sigma in sigmas:
        weight = n ** (-sigma)
        for name, values in seqs.items():
            c = weight * values
            columns.append(c)
            labels.append((float(sigma), name))
            denoms.append(float(c.sum()))

    C = np.column_stack(columns)
    R = np.empty((len(ts), C.shape[1]), dtype=np.complex128)
    for j in range(0, len(ts), block):
        tb = ts[j:j + block]
        phase = np.exp(-1j * np.outer(tb, logs))
        R[j:j + len(tb)] = phase @ C
    return labels, np.asarray(denoms), R


def write_spectrum_summary(path, labels, denoms, R, ts, tmin=5.0):
    coherence = np.abs(R) / denoms
    mask = ts >= tmin
    fields = ["sigma", "observable", "t_min", "min_coherence", "median_coherence", "q10_coherence"]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for col, (sigma, name) in enumerate(labels):
            sub = coherence[mask, col]
            inds = np.where(mask)[0]
            idx = inds[int(np.argmin(sub))]
            w.writerow({
                "sigma": f"{sigma:.2f}",
                "observable": name,
                "t_min": f"{ts[idx]:.8f}",
                "min_coherence": f"{coherence[idx, col]:.12g}",
                "median_coherence": f"{np.median(sub):.12g}",
                "q10_coherence": f"{np.quantile(sub, 0.1):.12g}",
            })
    return coherence


def critical_line_contrast(labels, coherence, ts, observable):
    ids = [labels.index((s, observable)) for s in (0.35, 0.5, 0.65)]
    eps = 1e-300
    return (
        np.log(coherence[:, ids[1]] + eps)
        - 0.5 * (
            np.log(coherence[:, ids[0]] + eps)
            + np.log(coherence[:, ids[2]] + eps)
        )
    )


def local_minima(ts, values, tmin=5.0, top=8):
    rows = []
    for i in range(1, len(ts) - 1):
        if ts[i] >= tmin and values[i] < values[i - 1] and values[i] < values[i + 1]:
            rows.append((float(values[i]), float(ts[i])))
    return sorted(rows)[:top]


def factor_multiset(n: int, spf):
    vals = []
    while n > 1:
        p = int(spf[n])
        vals.append(p)
        n //= p
    return vals


def formation_word_count(n: int, spf, is_prime) -> int:
    if is_prime[n]:
        return 0
    vals = factor_multiset(n, spf)
    c = Counter(vals)
    ans = math.factorial(len(vals))
    for e in c.values():
        ans //= math.factorial(e)
    return ans


def factor_pairs(n: int):
    return [(a, n // a) for a in range(2, math.isqrt(n) + 1) if n % a == 0]


def build_tree_counter(is_prime):
    @lru_cache(maxsize=None)
    def trees(n: int):
        if is_prime[n]:
            return (str(n),)
        out = set()
        for a, b in factor_pairs(n):
            for left in trees(a):
                for right in trees(b):
                    x, y = sorted((left, right))
                    out.add(f"({x}*{y})")
        return tuple(sorted(out))
    return trees


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=100000)
    ap.add_argument("--formation-N", type=int, default=1000)
    ap.add_argument("--t-max", type=float, default=50.0)
    ap.add_argument("--dt", type=float, default=0.2)
    ap.add_argument("--outdir", type=Path, default=Path("data/formation"))
    args = ap.parse_args()

    if args.formation_N > args.N:
        raise SystemExit("formation-N must be <= N")

    spf, is_prime, omega, Omega, Lambda = sieve(args.N)
    n = np.arange(2, args.N + 1, dtype=np.float64)
    ts = np.arange(0.0, args.t_max + 0.5 * args.dt, args.dt)
    sigmas = [0.20, 0.35, 0.50, 0.65, 0.80]

    seqs = {
        "one": np.ones(args.N - 1, dtype=np.float64),
        "prime": is_prime[2:].astype(np.float64),
        "Lambda": Lambda[2:],
        "omega": omega[2:].astype(np.float64),
        "Omega": Omega[2:].astype(np.float64),
        "omega_gt5": peeled_omega(spf, args.N, 5)[2:].astype(np.float64),
        "omega_gt17": peeled_omega(spf, args.N, 17)[2:].astype(np.float64),
        "omega_gt47": peeled_omega(spf, args.N, 47)[2:].astype(np.float64),
    }

    labels, denoms, R = complex_spectra(n, seqs, sigmas, ts)
    coherence = write_spectrum_summary(
        args.outdir / "complex_spectrum_summary_100k.csv",
        labels, denoms, R, ts,
    )

    # sigma=1/2 peeling audit.
    full = labels.index((0.5, "omega"))
    mask = ts >= 5.0
    rows = []
    for Q, name in ((5, "omega_gt5"), (17, "omega_gt17"), (47, "omega_gt47")):
        col = labels.index((0.5, name))
        x = R[mask, full] / denoms[full]
        y = R[mask, col] / denoms[col]
        corr = np.vdot(x, y) / np.sqrt(np.vdot(x, x) * np.vdot(y, y))
        residual = R[mask, full] - R[mask, col]
        energy = float(np.sum(np.abs(residual) ** 2) / np.sum(np.abs(R[mask, full]) ** 2))
        rows.append((Q, abs(corr), np.angle(corr), energy))

    with (args.outdir / "complex_peeling_sigma05.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Q", "normalized_spectral_correlation", "phase_offset_rad", "removed_raw_energy_fraction"])
        for row in rows:
            w.writerow(row)

    # Critical-line contrast minima at N.
    with (args.outdir / "complex_critical_line_contrast_100k.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["observable", "rank", "t", "contrast"])
        for name in ("one", "prime", "Lambda", "omega", "Omega", "omega_gt17", "omega_gt47"):
            A = critical_line_contrast(labels, coherence, ts, name)
            for rank, (value, t) in enumerate(local_minima(ts, A), 1):
                w.writerow([name, rank, t, value])

    # Formation descriptors to formation-N.
    M = args.formation_N
    trees = build_tree_counter(is_prime)
    W = np.zeros(M + 1, dtype=np.float64)
    T = np.zeros(M + 1, dtype=np.float64)
    for m in range(2, M + 1):
        if not is_prime[m]:
            W[m] = formation_word_count(m, spf, is_prime)
            T[m] = len(trees(m))

    nf = np.arange(2, M + 1, dtype=np.float64)
    tsf = np.arange(0.0, args.t_max + 0.025, 0.05)
    seqf = {
        "W_count": W[2:],
        "T_count": T[2:],
        "log1p_W": np.log1p(W[2:]),
        "log1p_T": np.log1p(T[2:]),
    }
    lf, df, RF = complex_spectra(nf, seqf, sigmas, tsf, block=50)
    write_spectrum_summary(
        args.outdir / "complex_formation_summary_1000.csv",
        lf, df, RF, tsf,
    )


if __name__ == "__main__":
    main()

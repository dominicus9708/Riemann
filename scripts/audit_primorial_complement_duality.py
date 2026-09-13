#!/usr/bin/env python3
"""Audit complement duality in finite primorial divisor groups.

For P_m = product of first m primes and
    F_m^<=(X) = sum_{d|P_m, d<=X} mu(d),
the divisor complement d <-> P_m/d gives
    F_m^<=(X) = (-1)^(m+1) sum_{e|P_m, e<P_m/X} mu(e).

At the first primorial crossing P_{m-1}<=X<P_m the strict small cutoff is
<=p_m, so the right-hand side is an ordinary small Mertens value.
The script verifies this identity at dyadic X and audits the even-m central
symmetry P_m ~= X^2.  It is a finite combinatorial audit, not an RH proof.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path


def sieve_primes(limit: int) -> list[int]:
    a = bytearray(b"\x01") * (limit + 1)
    a[:2] = b"\x00\x00"
    for p in range(2, int(limit**0.5) + 1):
        if a[p]:
            a[p*p:limit+1:p] = b"\x00" * (((limit-p*p)//p)+1)
    return [i for i in range(2, limit+1) if a[i]]


def mobius_table(N: int) -> list[int]:
    mu = [1] * (N + 1)
    prime = [True] * (N + 1)
    prime[0:2] = [False, False]
    for p in range(2, N + 1):
        if prime[p]:
            for j in range(p, N + 1, p):
                prime[j] = False if j != p else prime[j]
                mu[j] *= -1
            pp = p * p
            if pp <= N:
                for j in range(pp, N + 1, pp):
                    mu[j] = 0
    mu[0] = 0
    return mu


def state_sum(primes: list[int], m: int, X: int) -> tuple[int, int]:
    states = [(1, 1)]
    for p in primes[:m]:
        base = list(states)
        states.extend((d*p, -sgn) for d, sgn in base if d*p <= X)
    return sum(s for _, s in states), len(states)


def write(path: Path, rows: list[dict]):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-power", type=int, default=10)
    ap.add_argument("--max-power", type=int, default=24)
    ap.add_argument("--first-out", type=Path,
                    default=Path("data/formation/primorial_first_crossing_duality_2pow10_24.csv"))
    ap.add_argument("--center-out", type=Path,
                    default=Path("data/formation/primorial_even_center_audit_2pow10_24.csv"))
    args = ap.parse_args()

    primes = sieve_primes(200)
    mu = mobius_table(200)
    M = [0] * len(mu)
    for n in range(1, len(mu)):
        M[n] = M[n-1] + mu[n]

    first_rows = []
    center_rows = []
    for k in range(args.min_power, args.max_power + 1):
        X = 2**k
        P = 1
        first = None
        candidates = []
        for m, p in enumerate(primes, start=1):
            P *= p
            candidates.append((m, p, P))
            if first is None and P > X:
                Y = P / X
                cutoff = math.ceil(Y) - 1  # integers n<Y
                F, N = state_sum(primes, m, X)
                pred = ((-1) ** (m + 1)) * M[cutoff]
                if F != pred:
                    raise AssertionError((X, m, F, pred))
                first = dict(
                    k=k, X=X, m0=m, p_m0=p, P_m0=P,
                    Y_over_1=P/X, strict_cutoff=cutoff,
                    F_m0=F, prediction=pred, N_allowed=N,
                )
            if math.log(P) > 2 * math.log(X) + 8:
                break
        first_rows.append(first)

        even = [r for r in candidates if r[0] % 2 == 0]
        m, p, Pc = min(even, key=lambda r: abs(math.log(r[2]) - 2*math.log(X)))
        F, N = state_sum(primes, m, X)
        ratio = Pc / (X*X)
        center_rows.append(dict(
            k=k, X=X, m=m, p_m=p, P_over_X2=ratio,
            Y_over_X=ratio, F=F, N_allowed=N,
            F_over_sqrtN=F/math.sqrt(N),
        ))

    write(args.first_out, first_rows)
    write(args.center_out, center_rows)
    print(f"verified {len(first_rows)} first-crossing identities")
    print(f"wrote {args.first_out}")
    print(f"wrote {args.center_out}")


if __name__ == "__main__":
    main()

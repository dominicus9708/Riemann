#!/usr/bin/env python3
"""Audit how many omega-layer moments are needed to reconstruct Möbius parity.

For squarefree layer counts

    A_r(x) = #{n<=x : mu(n)^2=1, omega(n)=r},

set

    B_j(x) = sum_r A_r(x) * binom(r,j).

The universal Newton expansion of parity is

    (-1)^r = sum_{j=0}^r (-2)^j binom(r,j),

hence

    M(x) = sum_j (-2)^j B_j(x).

The script reads the repository's dyadic layer-count table, records every
partial sum, and reports the first order K that enters several target error
scales. This is a finite diagnostic of the universal expansion, not a lower
bound for every possible x-dependent approximation scheme.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path


def read_rows(path: Path):
    with path.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            layers=[]
            j=0
            while f"A{j}" in row:
                layers.append(int(row[f"A{j}"]))
                j += 1
            yield int(row["X"]), int(row["M"]), layers


def first_nonzero_max(layers: list[int]) -> int:
    return max(i for i,v in enumerate(layers) if v)


def binomial_moments(layers: list[int], m: int) -> list[int]:
    out=[]
    for j in range(m+1):
        out.append(sum(layers[r]*math.comb(r,j) for r in range(j,m+1)))
    return out


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument(
        "--input", type=Path,
        default=Path("data/formation/mobius_layer_counts_dyadic_24.csv")
    )
    ap.add_argument(
        "--out-all", type=Path,
        default=Path("data/formation/parity_moment_truncation_all.csv")
    )
    ap.add_argument(
        "--out-summary", type=Path,
        default=Path("data/formation/parity_moment_truncation_summary.csv")
    )
    ap.add_argument("--target-exponents", default="0.5,0.55,0.6")
    args=ap.parse_args()

    exponents=[float(v) for v in args.target_exponents.split(",") if v]
    detail=[]
    summary=[]

    for X,M,layers in read_rows(args.input):
        m=first_nonzero_max(layers)
        B=binomial_moments(layers,m)
        partial=0
        partials=[]
        for K,b in enumerate(B):
            partial += (-2)**K*b
            partials.append(partial)
            detail.append({
                "X":X,
                "M":M,
                "max_omega":m,
                "K":K,
                "B_K":b,
                "partial_sum":partial,
                "error_to_M":partial-M,
                "error_over_sqrtX":(partial-M)/math.sqrt(X),
            })
        assert partials[-1] == M

        record={"X":X,"M":M,"max_omega":m}
        for exponent in exponents:
            threshold=X**exponent
            K=next(k for k,value in enumerate(partials) if abs(value-M)<=threshold)
            label=str(exponent).replace(".","")
            record[f"min_K_X{label}"]=K
        summary.append(record)

    args.out_all.parent.mkdir(parents=True, exist_ok=True)
    with args.out_all.open("w",newline="",encoding="utf-8") as f:
        writer=csv.DictWriter(f,fieldnames=list(detail[0].keys()))
        writer.writeheader(); writer.writerows(detail)
    with args.out_summary.open("w",newline="",encoding="utf-8") as f:
        writer=csv.DictWriter(f,fieldnames=list(summary[0].keys()))
        writer.writeheader(); writer.writerows(summary)

    print("verified exact parity reconstruction for every input cutoff")
    for row in summary:
        print(row)


if __name__ == "__main__":
    main()

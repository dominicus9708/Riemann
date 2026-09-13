"""Generate a non-certifying baseline table of critical-line zeta zeros.

Purpose
-------
This script is a reproducibility/regression tool, not a proof of RH and not a
complete zero certification procedure. It uses mpmath.zetazero, then evaluates
zeta again at each returned zero and derives gap statistics.

For rigorous completeness claims, later stages must use an independent
zero-counting/certification method (e.g. Turing-type counting with interval
arithmetic) rather than this script alone.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path

import mpmath as mp


def normalized_gap(gamma: mp.mpf, gap: mp.mpf) -> mp.mpf:
    """Normalize by local mean spacing 2*pi/log(gamma/(2*pi))."""
    return gap * mp.log(gamma / (2 * mp.pi)) / (2 * mp.pi)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=50)
    parser.add_argument("--dps", type=int, default=80)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/baseline/first_50_zeros.csv"),
    )
    args = parser.parse_args()

    if args.count < 2:
        raise SystemExit("--count must be at least 2")
    if args.dps < 30:
        raise SystemExit("--dps should be at least 30 for the baseline run")

    mp.mp.dps = args.dps
    zeros = [mp.zetazero(n) for n in range(1, args.count + 1)]

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(
            [
                "n",
                "re",
                "gamma",
                "gap_to_next",
                "normalized_gap_local",
                "abs_zeta_at_zero",
            ]
        )

        for i, zero in enumerate(zeros):
            gamma = mp.im(zero)
            re = mp.re(zero)
            residual = abs(mp.zeta(zero))

            if i + 1 < len(zeros):
                gap = mp.im(zeros[i + 1]) - gamma
                ngap = normalized_gap(gamma, gap)
                gap_s = mp.nstr(gap, 25)
                ngap_s = mp.nstr(ngap, 25)
            else:
                gap_s = ""
                ngap_s = ""

            writer.writerow(
                [
                    i + 1,
                    mp.nstr(re, 20),
                    mp.nstr(gamma, 35),
                    gap_s,
                    ngap_s,
                    mp.nstr(residual, 12),
                ]
            )

    print(f"wrote {args.count} rows to {args.output}")
    print("AUDIT: output is regression data, not a certified complete zero list")


if __name__ == "__main__":
    main()

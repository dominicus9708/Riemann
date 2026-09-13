"""Analyze a one-ordinate-per-line zeta-zero table.

Designed for Odlyzko-style tables and locally generated critical-line zero
lists. Outputs summary statistics only; it does not infer global theorems from
finite samples.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


def quantile(sorted_values: list[float], q: float) -> float:
    if not sorted_values:
        raise ValueError("empty sample")
    pos = (len(sorted_values) - 1) * q
    lo = math.floor(pos)
    hi = math.ceil(pos)
    if lo == hi:
        return sorted_values[lo]
    w = pos - lo
    return sorted_values[lo] * (1 - w) + sorted_values[hi] * w


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument("--start-index", type=int, default=1)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    raw = args.path.read_bytes()
    text = raw.decode("ascii")
    gammas = [float(line.strip()) for line in text.splitlines() if line.strip()]
    if len(gammas) < 2:
        raise SystemExit("need at least two ordinates")

    if any(b <= a for a, b in zip(gammas, gammas[1:])):
        raise SystemExit("table is not strictly increasing")

    gaps = [b - a for a, b in zip(gammas, gammas[1:])]
    normalized = [
        gap * math.log(gamma / (2 * math.pi)) / (2 * math.pi)
        for gamma, gap in zip(gammas, gaps)
    ]

    def mean(xs: list[float]) -> float:
        return sum(xs) / len(xs)

    def std_population(xs: list[float]) -> float:
        m = mean(xs)
        return math.sqrt(sum((x - m) ** 2 for x in xs) / len(xs))

    sorted_norm = sorted(normalized)
    min_gap_i = min(range(len(gaps)), key=gaps.__getitem__)
    max_gap_i = max(range(len(gaps)), key=gaps.__getitem__)

    result = {
        "source_path": str(args.path),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "start_index": args.start_index,
        "count": len(gammas),
        "first_gamma": gammas[0],
        "last_gamma": gammas[-1],
        "raw_gap": {
            "mean": mean(gaps),
            "min": gaps[min_gap_i],
            "min_between_indices": [
                args.start_index + min_gap_i,
                args.start_index + min_gap_i + 1,
            ],
            "max": gaps[max_gap_i],
            "max_between_indices": [
                args.start_index + max_gap_i,
                args.start_index + max_gap_i + 1,
            ],
        },
        "normalized_gap": {
            "mean": mean(normalized),
            "std_population": std_population(normalized),
            "q01": quantile(sorted_norm, 0.01),
            "q05": quantile(sorted_norm, 0.05),
            "q25": quantile(sorted_norm, 0.25),
            "q50": quantile(sorted_norm, 0.50),
            "q75": quantile(sorted_norm, 0.75),
            "q95": quantile(sorted_norm, 0.95),
            "q99": quantile(sorted_norm, 0.99),
        },
        "audit": {
            "status": "NUMERICAL_EXPERIMENTAL",
            "warning": (
                "Finite-sample extrema, quantiles, and apparent patterns are not "
                "global bounds or proofs. Normalization uses a smooth asymptotic "
                "local mean spacing, not an exact individual-gap law."
            ),
        },
    }

    encoded = json.dumps(result, indent=2, sort_keys=True)
    print(encoded)
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

"""Fetch Odlyzko zeta-zero tables and record provenance.

This script is intended to be run in an environment with network access.
Raw external datasets need not be committed to Git; the generated manifest
records URL, byte size, SHA-256, line count, and first/last values.

Important: downloading a table does not certify RH or even completeness beyond
what is established by the source's associated methodology.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import urllib.request
from pathlib import Path

BASE = "https://www-users.cse.umn.edu/~odlyzko/zeta_tables/"

TABLES = {
    "first_100000": "zeros1",
    "first_100_high_precision": "zeros2",
    "near_1e12": "zeros3",
    "near_1e21": "zeros4",
    "near_1e22": "zeros5",
    "first_2001052": "zeros6",
}


def parse_numeric_lines(raw: bytes) -> list[str]:
    text = raw.decode("ascii")
    return [line.strip() for line in text.splitlines() if line.strip()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("table", choices=sorted(TABLES))
    parser.add_argument("--outdir", type=Path, default=Path("data/external/raw"))
    parser.add_argument("--manifest-dir", type=Path, default=Path("data/external/manifests"))
    args = parser.parse_args()

    filename = TABLES[args.table]
    url = BASE + filename

    with urllib.request.urlopen(url, timeout=120) as response:
        raw = response.read()

    lines = parse_numeric_lines(raw)
    if not lines:
        raise RuntimeError("downloaded table contains no numeric lines")

    args.outdir.mkdir(parents=True, exist_ok=True)
    args.manifest_dir.mkdir(parents=True, exist_ok=True)

    raw_path = args.outdir / f"{args.table}.txt"
    raw_path.write_bytes(raw)

    manifest = {
        "dataset": args.table,
        "source_url": url,
        "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "line_count": len(lines),
        "first_value": lines[0],
        "last_value": lines[-1],
        "audit_status": "EXTERNAL_NUMERICAL_DATASET",
        "warning": (
            "Dataset precision/index metadata must be interpreted using the "
            "source page and associated literature; this manifest is provenance, "
            "not a completeness proof."
        ),
    }

    manifest_path = args.manifest_dir / f"{args.table}.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()

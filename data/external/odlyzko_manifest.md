# External Dataset Manifest — Odlyzko Zeta-Zero Tables

## Source

Andrew Odlyzko, *Tables of zeros of the Riemann zeta function*, University of Minnesota.

Public index:
https://www-users.cse.umn.edu/~odlyzko/zeta_tables/

## Published table groups

The source page currently exposes:

1. first 100,000 zeros — stated accuracy within `3×10^-9`;
2. first 100 zeros — over 1,000 decimal places;
3. zeros `10^12+1` through `10^12+10^4`;
4. zeros `10^21+1` through `10^21+10^4`;
5. zeros `10^22+1` through `10^22+10^4`;
6. first 2,001,052 zeros — stated accuracy within `4×10^-9`.

## Intended repository use

### Low-height corpus
The first 100,000 values will be used for:
- gap distributions;
- normalized spacing;
- Gram-interval structure;
- local density drift;
- candidate-pattern generation.

### High-height stress windows
The three 10,000-zero windows near indices `10^12`, `10^21`, and `10^22` will be used to test whether patterns inferred at low height survive enormous scale changes.

These windows are not substitutes for an exhaustive table from zero 1 to zero `10^22`.

## Audit classification

`EXTERNAL_NUMERICAL_DATASET`.

### Strengths
- produced and hosted by a principal researcher in large-scale zeta-zero computation/statistics;
- multiple height regimes are explicitly available;
- stated decimal accuracy is adequate for spacing/statistical work at the planned level.

### Limitations
- the table index is a data source, not itself a proof of RH or a full modern interval-certification paper;
- stated decimal accuracy must not be promoted to a completeness guarantee unless the associated computational method establishes it;
- high-index windows are selected windows, so they cannot establish properties of all intervening zeros;
- pattern persistence in these windows remains empirical evidence, not proof of an asymptotic law.

## Cross-check already completed

The repository's directly generated values at indices

`1, 10, 100, 250, 500, 750, 1000`

agree exactly after rounding to the published first-100,000 table precision.

## Later ingestion rule

When a raw table is imported locally, record:
- exact source file URL;
- retrieval date;
- byte size;
- SHA-256;
- line count;
- parser version;
- first/last parsed index and ordinate;
- stated source accuracy.

Raw multi-megabyte files need not be committed to Git if the manifest, checksum, and parser make the analysis reproducible.

# First 1,000 Zeros — Direct Computation and External Cross-Check

## 1. Direct computation

The first 1,000 positive critical-line zeros were generated with `mpmath.zetazero(n)` using 35-decimal-digit working precision in a parallel 8-process run.

The canonical record format used for the run was

```text
n,gamma_n
```

with each `gamma_n` serialized to 30 significant decimal digits.

SHA-256 of the 1,000-line canonical record:

```text
8e02f6568df449b08130302ce820f6002ae1e9120cc4840b623c93b81c12e02b
```

Status: `NUMERICAL_EXPERIMENTAL / REPRODUCIBLE_REGRESSION`.

This hash proves reproducibility of this exact generated table only. It does **not** certify that the table contains every nontrivial zero in the strip.

## 2. Selected directly computed ordinates

| n | gamma_n |
|---:|---:|
| 1 | 14.1347251417346937904572519836 |
| 10 | 49.7738324776723021819167846786 |
| 100 | 236.524229665816205802475507956 |
| 250 | 470.773655478101647690118879454 |
| 500 | 811.184358846506260337884327465 |
| 750 | 1123.10111738780920016666445553 |
| 1000 | 1419.42248094599568646598903808 |

## 3. External cross-check A — Odlyzko table

Andrew Odlyzko's public zeta-zero tables state that the first 100,000 zeros are tabulated to within `3×10^-9`.

The selected indices above round exactly to the corresponding Odlyzko entries:

| n | our value rounded to table precision | Odlyzko |
|---:|---:|---:|
| 1 | 14.134725142 | 14.134725142 |
| 10 | 49.773832478 | 49.773832478 |
| 100 | 236.524229666 | 236.524229666 |
| 250 | 470.773655478 | 470.773655478 |
| 500 | 811.184358847 | 811.184358847 |
| 750 | 1123.101117388 | 1123.101117388 |
| 1000 | 1419.422480946 | 1419.422480946 |

Audit classification: `EXTERNAL_NUMERICAL_CROSSCHECK`.

### Source audit

Strengths:
- independent public dataset from a leading researcher in computational zeta-zero statistics;
- explicitly states the first-100,000 dataset accuracy;
- also supplies widely separated very-high-index windows, useful later for low-height-pattern stress tests.

Limitations:
- the web table itself is a data publication, not by itself a full rigorous completeness proof;
- its quoted decimal error is far lower precision than our 30-digit local serialization;
- agreement at selected indices tests implementation/indexing, not RH.

Therefore it is accepted as an independent numerical reference, not as a global theorem source.

Source: Andrew Odlyzko, *Tables of zeros of the Riemann zeta function*, University of Minnesota.

## 4. External cross-check B — Wolfram `ZetaZero`

A second implementation was queried at indices

`1, 10, 100, 250, 500, 750, 1000`.

The values agreed with the local computation for at least the first 50 decimal digits in the returned high-precision outputs.

### Important audit limitation

Wolfram Language documents `ZetaZero[k]` as the `k`th zero **on the critical line**. Thus this function is suitable for numerical implementation cross-checking in a range already independently known to lie on the line, but it cannot establish that no off-line zeros exist.

Audit label: `CRITICAL_LINE_ENUMERATOR_NOT_GLOBAL_COMPLETENESS_TEST`.

## 5. Distribution summary for n=1,...,1000

For the 999 consecutive gaps

\[
\Delta_n=\gamma_{n+1}-\gamma_n,
\]

we obtained:

- mean raw gap: `1.4066944502545156`
- minimum raw gap: `0.161500788964986`, between zeros 922 and 923
- maximum raw gap: `6.887314497036861`, between zeros 1 and 2

Using

\[
\delta_n=\Delta_n\frac{\log(\gamma_n/(2\pi))}{2\pi},
\]

we obtained:

- mean normalized gap: `0.9989016218845007`
- standard deviation: `0.37951321289367906`
- quantiles:
  - 1%: `0.28061063399844594`
  - 5%: `0.4334606080798077`
  - 25%: `0.7236583708356292`
  - 50%: `0.9582092839902462`
  - 75%: `1.2492773687627277`
  - 95%: `1.6766651745700683`
  - 99%: `1.9907441385670408`

Status: `NUMERICAL_EXPERIMENTAL`.

## 6. Audit interpretation

The normalized mean being close to 1 is expected from the smooth Riemann–von Mangoldt density and is not a new theorem.

The smallest and largest gaps in the first 1,000 zeros are sample extrema only; they must not be generalized to global bounds.

The first-1,000 table is now adequate as a low-height implementation regression corpus, but not yet as a large pattern corpus. The next pattern stage should use the first 10,000/100,000 external values and separated high-height windows.

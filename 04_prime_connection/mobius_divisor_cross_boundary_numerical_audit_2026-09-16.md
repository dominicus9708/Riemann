# Möbius–divisor cross-boundary numerical audit — 2026-09-16

## Status
- Riemann hypothesis: OPEN.
- Purpose: false-control / route triage only.
- Range: integer cutoffs `N=10,000, 11,000, ..., 1,000,000`.
- Exact hyperbola decomposition verified numerically to floating roundoff.
- Strong small-d / large-d anticorrelation: NOT OBSERVED in this finite range.
- This does not rule out a deeper asymptotic signed mechanism.

## 1. Decomposition under test

Let

\[
T(N)=\psi(N)-N+2\gamma
=\sum_{d\le N}\mu(d)B\!\left(\left\lfloor\frac Nd\right\rfloor\right).
\]

Set

\[
K=\lfloor\sqrt N\rfloor,
\qquad
Q=\left\lfloor\frac{N}{K+1}\right\rfloor.
\]

Define

\[
A(N)=\sum_{d\le K}\mu(d)B\!\left(\left\lfloor\frac Nd\right\rfloor\right),
\]

and

\[
C(N)=\sum_{q\le Q}b(q)M\!\left(\left\lfloor\frac Nq\right\rfloor\right)-M(K)B(Q).
\]

Then exactly

\[
T(N)=A(N)+C(N).
\]

The intended interpretation is:
- `A`: small-d / high-quotient divisor-kernel side;
- `C`: large-d / low-quotient Mertens side.

## 2. Direct finite diagnostic

At the sampled cutoffs the identity was verified to maximum floating discrepancy below `8e-9`.

Raw-sample statistics:

- Pearson `corr(A,C) ~= -0.346`;
- Pearson `corr(A,T) ~= 0.053`;
- Pearson `corr(C,T) ~= 0.918`;
- RMS `A ~= 62.90`;
- RMS `C ~= 158.96`;
- RMS `T ~= 149.33`;
- mean absolute `A ~= 48.06`;
- mean absolute `C ~= 122.05`;
- mean absolute `T ~= 116.46`.

After normalization by `sqrt(N)`:

- `corr(A/sqrt(N), C/sqrt(N)) ~= -0.315`;
- `corr(C/sqrt(N), T/sqrt(N)) ~= 0.914`.

Thus the observed anticorrelation is modest rather than near-deterministic, while the large-d/Mertens side tracks the full prime error much more strongly.

## 3. Finite growth regression

Simple log-log regressions of absolute values over the same sample range give apparent slopes

- `|A(N)|`: about `0.449`;
- `|C(N)|`: about `0.529`;
- `|T(N)|`: about `0.528`.

These are diagnostics only. They are not asymptotic exponents and must not be used as RH evidence.

## 4. Low-q band decomposition of the Mertens side

Ignoring the final boundary term, split the `q`-sum into

- `1..10`,
- `11..50`,
- `51..100`,
- `101..300`,
- `301..Q`.

The individual bands have RMS sizes comparable to or larger than the final `C(N)`, showing substantial cancellation **inside the Mertens side itself**. No single band accounts for the whole final signal.

Representative Pearson correlations with `T(N)` were approximately

- `q=1..10`: `0.43`;
- `q=11..50`: `0.46`;
- `q=51..100`: `-0.01`;
- `q=101..300`: `0.33`;
- `q=301..Q`: `-0.11`;
- boundary term: approximately `0`.

Thus the hard cancellation is distributed across quotient scales rather than being a simple boundary effect.

## 5. Audit verdict

The simplest hoped-for mechanism

\[
A(N)\approx-C(N)
\]

with strong deterministic anticorrelation is not visible in this finite range.

Classification:

`CROSS_BOUNDARY_STRONG_ANTICORRELATION_FALSE_CONTROL`.

The surviving question must therefore be more structured than a two-block covariance claim. It would need a signed identity/inequality that resolves internal quotient-scale cancellation inside `C(N)` itself.

## 6. Next target

The next useful decomposition is not another geometric split in `d` or `q`. Instead, decompose the Mertens side by **kernel increments / quotient-scale interaction order** and test whether `b(q)` has a discrete cancellation law against

\[
M(\lfloor N/q\rfloor)
\]

that survives after subtracting the generic floor-quotient prediction.

Any candidate must be compared with the already-closed floor-quotient matrix inverse and Mertens block-increment route.

# Quotient dyadic-band null audit — 2026-09-16

## Status
- Riemann hypothesis: OPEN.
- Relative dyadic-band anticorrelation in the large-d quotient side: NUMERICALLY OBSERVED.
- Special-kernel explanation: REJECTED by component/null controls.
- Classification: generic Mertens quotient-scale geometry / finite control, not an RH candidate.

## 1. Setup

For the square-root split, let

\[
Q=\left\lfloor\frac{N}{\lfloor\sqrt N\rfloor+1}\right\rfloor
\]

and decompose

\[
\sum_{q\le Q} b(q)M(\lfloor N/q\rfloor)
\]

into relative dyadic bands

\[
(Q/2,Q],\ (Q/4,Q/2],\ldots.
\]

The finite audit used

\[
N=20000,22000,\ldots,10^6
\]

and normalized band contributions by `sqrt(N)` before computing correlations.

## 2. Initial observation

For the full kernel

\[
b(q)=\log q-\tau(q)+2\gamma,
\]

the seven adjacent-band Pearson correlations were approximately

\[
-0.331,-0.356,-0.251,-0.231,-0.476,-0.206,-0.253.
\]

Their mean is about

\[
-0.301.
\]

A 30-run control obtained by randomly permuting the values of `b(q)` over the sampled q-range produced mean adjacent correlation about `-0.021`, with run-to-run standard deviation about `0.123`. The observed mean is therefore roughly `2.3` control standard deviations below the null mean.

By itself this looked like a possible arithmetic alignment signal.

## 3. Component controls

The crucial controls replace `b(q)` by simpler kernels while leaving the same Mertens quotient geometry intact.

Observed mean adjacent-band correlations:

- full `b(q)=log q-tau(q)+2gamma`: about `-0.301`;
- `log q` only: about `-0.725`;
- `-tau(q)` only: about `-0.731`;
- constant kernel `2gamma`: about `-0.719`.

Thus the anticorrelation is **not special to the divisor kernel**. It is substantially stronger for generic/simple component kernels.

The special linear combination defining `b` actually weakens the generic dyadic anticorrelation rather than generating it.

## 4. Verdict

Classification:

`DYADIC_MERTENS_ANTICORRELATION_GENERIC_CONTROL`.

Permanent rule:

`QUOTIENT_DYADIC_CORRELATION_FALSE_CONTROL` — adjacent negative correlations between quotient bands must be compared against constant, smooth, and component-kernel controls before being interpreted as arithmetic structure of the special kernel.

The observed finite anticorrelation is therefore removed from the live RH route.

## 5. Consequence

Together with `QUOTIENT_INTERNAL_ABEL_CIRCULARITY`, this closes the simplest quotient-side ideas:

- linear Abel/telescoping transforms;
- two-block cross-boundary covariance;
- adjacent dyadic-band anticorrelation;
- componentwise `log`, `tau`, constant decompositions.

Any surviving quotient-side candidate must use a genuinely nonlinear/high-order relation that is absent from these generic controls, or introduce independent arithmetic information beyond the Mertens quotient geometry.

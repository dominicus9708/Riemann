# Divisor-kernel zero-sensitivity audit — 2026-09-16

## Status
- Riemann hypothesis: OPEN.
- Dirichlet-series identity: EXACT.
- Zero multiplicity response: EXACT.
- Spectral desensitization by the special divisor kernel: FALSE.
- Arithmetic weighted-quotient inequality: still OPEN, but any RH-scale success would be a genuine full zero-sensitive estimate rather than a weak smoothing artifact.

## 1. Kernel Dirichlet series

Recall

\[
b(n)=\log n-\tau(n)+2\gamma.
\]

For `Re(s)>1`, standard Dirichlet-series identities give

\[
\sum_{n\ge1}\frac{\log n}{n^s}=-\zeta'(s),
\qquad
\sum_{n\ge1}\frac{\tau(n)}{n^s}=\zeta(s)^2,
\qquad
\sum_{n\ge1}\frac1{n^s}=\zeta(s).
\]

Therefore

\[
\boxed{
\mathcal B(s):=\sum_{n\ge1}\frac{b(n)}{n^s}
=-\zeta'(s)-\zeta(s)^2+2\gamma\zeta(s).
}
\]

Since Möbius convolution multiplies by `1/zeta(s)`, the transformed kernel is

\[
\boxed{
\frac{\mathcal B(s)}{\zeta(s)}
=-\frac{\zeta'(s)}{\zeta(s)}-\zeta(s)+2\gamma.
}
\]

Adding the Dirichlet series of `1-2gamma delta` recovers exactly

\[
-\frac{\zeta'(s)}{\zeta(s)},
\]

as required by the arithmetic identity

\[
\Lambda=\mathbf1-2\gamma\delta+\mu*b.
\]

## 2. Response at a nontrivial zero

Let `rho` be a zero of `zeta` of multiplicity `m>=1`. Write locally

\[
\zeta(s)=(s-\rho)^m g(s),\qquad g(\rho)\ne0.
\]

Then

\[
\frac{\zeta'(s)}{\zeta(s)}
=\frac{m}{s-\rho}+\frac{g'(s)}{g(s)}.
\]

Hence

\[
\boxed{
\operatorname*{Res}_{s=\rho}
\frac{\mathcal B(s)}{\zeta(s)}=-m.
}
\]

Equivalently, the numerator has exactly one fewer order of vanishing than `zeta`:

\[
\mathcal B(s)
=-m\,g(\rho)(s-\rho)^{m-1}+O((s-\rho)^m).
\]

For a simple zero,

\[
\boxed{\mathcal B(\rho)=-\zeta'(\rho)\ne0.}
\]

Thus the divisor kernel does not cancel or attenuate a hypothetical off-critical simple zero at the analytic level.

## 3. Contrast with Selberg spectral desensitization

In the previously audited Selberg channel,

\[
\frac{\zeta''(s)}{\zeta(s)}
=L(s)^2-L'(s),
\qquad
L=-\frac{\zeta'}{\zeta},
\]

the strongest double-pole response at a simple zero cancels, leaving only a simple pole. That was classified as `SPECTRAL_DESENSITIZATION`.

The present divisor kernel behaves differently: after Möbius inversion it retains the **full logarithmic-derivative residue** `-m` at every zero. It is therefore not a softened zero detector.

Classification:

`DIVISOR_KERNEL_FULL_ZERO_SENSITIVITY`.

## 4. Consequence for the weighted quotient route

The exact arithmetic representation

\[
\psi(N)-N
=-2\gamma+
\sum_q B(q)
\left[
M\!\left(\left\lfloor\frac Nq\right\rfloor\right)
-M\!\left(\left\lfloor\frac N{q+1}\right\rfloor\right)
\right]
\]

therefore has two simultaneous properties:

1. it is an exact additive-divisor / multiplicative-Möbius bridge;
2. it retains the full zeta-zero obstruction analytically.

This sharpens the status of

`DIVISOR_KERNEL_WEIGHTED_QUOTIENT_CORRELATION_OPEN`.

A nontrivial arithmetic inequality for this weighted quotient sum could still be valuable, but if it reaches the square-root scale it cannot be interpreted as a mere benefit of divisor smoothing. It must supply genuinely RH-strength signed cancellation.

## 5. Permanent guard

`DIVISOR_KERNEL_ZERO_SENSITIVITY_GUARD`:

Do not treat the small pointwise size or integrated smoothness of the divisor-error component as evidence that the transformed prime channel has lost sensitivity to off-critical zeros. The exact Dirichlet series shows that the Möbius-transformed kernel has residue `-m` at a zero of multiplicity `m`.

## 6. Next viable test

The remaining arithmetic question is more precise than before:

\[
\boxed{
\text{Can the special weights }B(q)
\text{ enforce signed cancellation among Mertens quotient blocks}
\text{ by an inequality that is not merely an encoded bound on }1/\zeta?
}
\]

The next audit should split the quotient range at `q~sqrt(N)` and test whether the small-q divisor/Voronoi structure and the large-q exact Mertens blocks possess an exact cross-boundary compensation identity. If the split only reconstructs the original logarithmic derivative or a hyperbola decomposition, close the route as re-encoding.

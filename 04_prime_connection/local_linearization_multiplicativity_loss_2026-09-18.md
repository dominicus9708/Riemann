# Local linearization / multiplicativity-loss audit — 2026-09-18

## Status
- Riemann hypothesis: OPEN.
- Candidate audited: partition the long reciprocal Möbius sum into short intervals, linearize the phase on each interval, and apply a strong theorem for linear exponential sums with multiplicative coefficients.
- Conclusion: not a valid direct transfer. Translation destroys multiplicativity; the global Fourier alternative re-enters the same band-energy problem.

## 1. Long reciprocal phase
On a dyadic long factor `w~L`, normalize

\[
f(w)=X\left(\frac wL\right)^{-1/2}.
\]

Then

\[
f'(w)\asymp \frac XL,
\qquad
f''(w)\asymp \frac X{L^2}.
\]

A Taylor-linear block may have length at most

\[
B\asymp \frac{L}{\sqrt X}
\]

before the quadratic remainder becomes order one.

At the critical edge `X=L^(2/3)`, this is

\[
B\asymp L^{2/3}.
\]

## 2. Translation obstruction
On a block `w=w_0+m`, linearization gives schematically

\[
e(f(w))\approx e(f(w_0))e(\alpha_{w_0}m).
\]

But the coefficient becomes

\[
\mu(w_0+m),
\]

which is not a multiplicative function of `m`.

Therefore a theorem of Montgomery--Vaughan / Bachman / Robles for

\[
\sum_{m\le B}g(m)e(\alpha m)
\]

with multiplicative `g(m)` cannot simply be applied to a translated interval after local linearization.

Classification:

`LOCAL_LINEARIZATION_DESTROYS_MULTIPLICATIVE_INPUT`.

## 3. Difference-of-prefixes does not fix the nonlinear phase
A translated **linear** Möbius sum can of course be written as a difference of two prefix sums and bounded by a uniform linear theorem. But the reciprocal phase has a different tangent frequency on each block. Replacing each nonlinear block by a different linear phase and summing the approximation errors does not produce a single prefix sum to which one multiplicative theorem applies.

The quadratic phase errors also accumulate unless the blocks remain at the Taylor scale above.

## 4. Global additive-Fourier alternative
Instead keep the dyadic variable intact and write the smooth nonlinear weight

\[
g(w)=W(w/L)e\!\left(X(w/L)^{-1/2}\right)
\]

as an additive Fourier superposition

\[
g(w)=\int \widehat g(\alpha)e(\alpha w)\,d\alpha.
\]

Then

\[
\sum_{w\asymp L}\mu(w)g(w)
=\int \widehat g(\alpha)
\left(\sum_{w\asymp L}\mu(w)e(\alpha w)\right)d\alpha.
\]

This preserves the multiplicative coefficient inside the global linear sum.

However stationary phase places `hat g` in a frequency arc of width about

\[
\Delta\alpha\asymp \frac XL.
\]

Using a pointwise linear Möbius estimate and the L1 norm of `hat g` loses the stationary-phase factor and is weaker than the required reciprocal bound. Using Cauchy/Parseval instead asks for the local L2 energy

\[
\int_{\alpha\text{-arc}}
\left|
\sum_{w\asymp L}\mu(w)e(\alpha w)
\right|^2d\alpha,
\]

which is precisely the previously identified mesoscopic Möbius band-energy problem.

Classification:

`GLOBAL_LINEAR_FOURIER_REENTERS_BAND_ENERGY`.

## 5. Consequence
Strong modern theorems for one linear Möbius frequency remain useful benchmarks, but they do not automatically transfer to the nonlinear reciprocal phase by local Taylor partitioning.

Any successful use of them must control a **family of frequencies simultaneously** while retaining the original multiplicative variable. At that point the necessary input is again an L2/large-values statement for the Möbius Fourier transform, not merely a pointwise linear bound.

Permanent guard:
`LINEAR_TWIST_LOCALIZATION_MULTIPLICATIVITY_GUARD`.

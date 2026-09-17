# Quotient quadratic interaction parity false-control — 2026-09-17

## Status
- Riemann hypothesis: OPEN.
- Local quadratic correlation of `b(q) M(floor(N/q))`: NUMERICALLY strong.
- Quotient/Mertens origin of the correlation: REJECTED.
- Dominant source: parity bias already present in the divisor kernel `b(q)`.
- Simple adjacent quadratic quotient interaction: CLOSED as an RH candidate.

## 1. Candidate

On the large-d side of the square-root hyperbola split, define

\[
z_q(N)=b(q)M\!\left(\left\lfloor\frac Nq\right\rfloor\right),
\qquad
b(q)=\log q-\tau(q)+2\gamma.
\]

A natural first nonlinear test is the adjacent normalized quadratic correlation

\[
\rho_1(N)
=
\frac{\sum_{q<Q}z_q(N)z_{q+1}(N)}
{\left(\sum_{q<Q}z_q(N)^2\sum_{q<Q}z_{q+1}(N)^2\right)^{1/2}},
\]

with `Q` at the square-root hyperbola cutoff.

For `N=20000,22000,...,10^6`, the mean observed value is approximately

\[
\boxed{\rho_1\approx-0.467.}
\]

At first sight this is a strong anticorrelation.

## 2. Kernel-only false control

Remove the Mertens factor and compute the same lag correlation for `b(q)` alone.

Through the corresponding q-range the lag-1 normalized correlation is about

\[
\boxed{-0.476.}
\]

Thus essentially the entire observed sign pattern is already present before any quotient/Mertens interaction is introduced.

Higher short lags show the same phenomenon: the signs and magnitudes of the `z_q` lag correlations closely follow the autocorrelation structure of `b(q)`.

Classification:

`QUOTIENT_QUADRATIC_KERNEL_AUTOCORRELATION_FALSE_CONTROL`.

## 3. Exact origin: parity bias of the divisor kernel

The kernel has a large parity mode.

Let

\[
B_{\rm odd}(x)=\sum_{\substack{n\le x\\n\text{ odd}}}b(n),
\qquad
B_{\rm even}(x)=\sum_{\substack{n\le x\\n\text{ even}}}b(n).
\]

For odd integers,

\[
\sum_{\substack{n\ge1\\n\text{ odd}}}\frac{\tau(n)}{n^s}
=(1-2^{-s})^2\zeta(s)^2.
\]

The coefficient of the double pole at `s=1` is `1/4`, hence

\[
\sum_{\substack{n\le x\\n\text{ odd}}}\tau(n)
=\frac14x\log x+O(x).
\]

Also

\[
\sum_{\substack{n\le x\\n\text{ odd}}}\log n
=\frac12x\log x+O(x),
\qquad
\#\{n\le x:n\text{ odd}\}=\frac x2+O(1).
\]

Therefore

\[
\boxed{
B_{\rm odd}(x)=\frac14x\log x+O(x).
}
\]

The full summatory kernel satisfies

\[
B(x)=\sum_{n\le x}b(n)=S(x)-\Delta(x)=o(x\log x),
\]

so

\[
\boxed{
B_{\rm even}(x)=-\frac14x\log x+O(x).
}
\]

Equivalently, the conditional mean of `b(n)` is

\[
\frac12\log x+O(1)
\]

on odd integers and

\[
-\frac12\log x+O(1)
\]

on even integers.

Thus adjacent indices automatically inherit a strong alternating component.

A direct finite check gives, for example, around `q<=10000`, mean `b(q)` approximately `+3.99` on odd q and `-3.99` on even q.

## 4. Dirichlet-series view

The parity-twisted divisor series is

\[
\sum_{n\ge1}\frac{(-1)^n\tau(n)}{n^s}
=
\zeta(s)^2\left[1-2(1-2^{-s})^2\right].
\]

At `s=1` the bracket equals `1/2`, so the parity twist retains a double pole. By contrast, the parity twists of the smooth `log n` and constant terms do not supply a compensating double pole.

Hence the alternating mode of `b` is macroscopic; it is not a small finite-sample artifact.

## 5. Consequence for quotient-side nonlinear searches

Any local quadratic statistic involving adjacent q-values can be dominated by this kernel parity mode.

Permanent guard:

`DIVISOR_KERNEL_PARITY_MODE_GUARD` — before interpreting a nonlinear quotient statistic as interaction between Mertens blocks, subtract or control the low-modulus residue-class structure already present in `b(q)`.

This closes the simplest adjacent quadratic candidate.

A surviving large-d candidate must therefore:

1. be invariant to, or explicitly remove, fixed small-modulus modes of `b(q)`;
2. still distinguish the real Mertens quotient sequence from kernel-only and shuffled/block controls;
3. involve nonlocal/high-order interaction rather than a local autocorrelation inherited from `b` itself.

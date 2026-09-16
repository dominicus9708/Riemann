# Multiplicative-block absolute exponent threshold — 2026-09-16

## Status
- Riemann hypothesis: OPEN.
- Multiplicative-block prime-square reserve asymptotic: UNCONDITIONAL from PNT.
- Absolute-value exponent threshold: EXACT scale comparison.
- Standard zero-free-region PNT error used absolutely: INSUFFICIENT.

## 1. Positive reserve on fixed multiplicative blocks

Let

\[
S_2(M):=\sum_{m<M}A_m^{(2)},
\]

where

\[
A_m^{(2)}
=\bigl(\vartheta((m+1)^2)-\vartheta(m^2)\bigr)
\frac{\vartheta(m)+\vartheta(m+1)}2.
\]

The previous audit proved unconditionally

\[
S_2(M)\sim\frac23M^3.
\]

Therefore for every fixed \(\lambda>1\),

\[
\boxed{
S_2(\lambda M)-S_2(M)
\sim
\frac23(\lambda^3-1)M^3>0.
}
\]

Likewise, for the prime-square oriented area

\[
W_2(M):=\sum_{m<M}W_m^{(2)}\sim\frac13M^3,
\]

so

\[
\boxed{
W_2(\lambda M)-W_2(M)
\sim
\frac13(\lambda^3-1)M^3>0.
}
\]

Thus sufficiently large fixed-ratio blocks possess an unconditional positive cross-scale reserve.

## 2. Absolute control of the hard Chebyshev transport

Write

\[
R(x)=\psi(x)-x.
\]

Suppose only that on a fixed-ratio interval

\[
M^2\le x\le\lambda^2M^2
\]

we have an absolute bound

\[
|R(x)|\ll x^\beta L(x),
\]

where \(L\) is subpower/slowly varying.

Then the integral contribution obeys

\[
\left|
\int_{M^2}^{\lambda^2M^2}R(t)dt
\right|
\ll
M^{2\beta+2}L(M^2).
\]

The deterministic prime-square reserve on the same block has scale \(M^3\).
Therefore an absolute comparison can reach the reserve scale only if

\[
2\beta+2\le3,
\]

that is,

\[
\boxed{\beta\le\frac12.}
\]

For \(\beta<1\), the integrated error exponent \(2\beta+2\) also dominates the endpoint quadratic exponent \(4\beta\), so the integral transport is the primary absolute-value obstruction.

Classification:

`MULTIPLICATIVE_BLOCK_ABSOLUTE_THRESHOLD`.

The square-root exponent is not removed by moving from one shell to a fixed-ratio block; it reappears from the ratio of transport volume to the M^3 prime-square reserve.

## 3. Why classical strong PNT errors still miss the reserve

The Vinogradov-Korobov zero-free region yields a standard error of the form

\[
R(x)
=O\left(
x\exp\left[-c\frac{(\log x)^{3/5}}{(\log\log x)^{1/5}}\right]
\right).
\]

Set

\[
\eta(x)=\exp\left[-c\frac{(\log x)^{3/5}}{(\log\log x)^{1/5}}\right].
\]

On x~M^2, absolute integration over a fixed-ratio block gives at best

\[
O(M^4\eta(M^2)).
\]

Relative to the M^3 reserve this is

\[
O(M\eta(M^2)).
\]

But

\[
\log\bigl(M\eta(M^2)\bigr)
=
\log M
-O\bigl((\log M)^{3/5}(\log\log M)^{-1/5}\bigr)
\to+\infty.
\]

Hence

\[
\boxed{M\eta(M^2)\to\infty.}
\]

So even this strong classical unconditional PNT remainder is asymptotically much too large when propagated by absolute values.

The same is true a fortiori for any fixed logarithmic saving

\[
R(x)=O_A(x/\log^A x).
\]

## 4. Why changing the block length does not cure an absolute-value proof

For a shell window of K=o(M) consecutive square shells near M, the t-length is naturally

\[
\Delta x\asymp MK.
\]

If the square reserve has its natural size \(\asymp M^2K\), while

\[
|R(x)|\ll M^{2\beta}L(M^2),
\]

then absolute integration gives

\[
O(M^{2\beta+1}K L(M^2)).
\]

Comparing with \(M^2K\), the K factor cancels and again requires

\[
\beta\le\frac12.
\]

This shorter-window statement is a scale calculation, not a uniform short-interval theorem for the reserve; the fixed-ratio block result above is the rigorous unconditional version.

## 5. Audit verdict

Block growth alone cannot convert a PNT-level absolute error estimate into an RH-scale event-energy inequality.

Permanent guard:

`PNT_ABSOLUTE_SCALE_MISMATCH` — if a proposed square-shell/block proof replaces the signed Chebyshev transport by an absolute pointwise PNT error, check the exponent comparison first. On the natural prime-square reserve scale it immediately demands the square-root exponent.

Therefore the surviving route must exploit signed cancellation or additional arithmetic structure in the hard transport. Zero-free-region magnitude bounds, regardless of strong subexponential logarithmic savings, do not supply that cancellation.

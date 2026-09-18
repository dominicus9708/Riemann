# Long Möbius polynomial finite mean-square audit — 2026-09-18

## Status
- Riemann hypothesis: OPEN.
- Purpose: finite false-control / scale diagnostic only.
- Target window: length `X=L^(2/3)` centered at `T=tau X`.
- Normalization: `X sum_{L<=n<2L} |a_n|^2`.
- Coefficients compared: actual `mu(n)`, squarefree support `mu(n)^2`, and independent random signs on the same squarefree support.
- Conclusion: actual Möbius mean square stays at diagonal/random scale in the tested range, but is not separated from the random-sign control. This is not RH evidence and does not supply a proof input.

## 1. Quantity

For coefficients `a_n` define

\[
R_a(L,\tau)
=
\frac{
\int_{\tau X-X/2}^{\tau X+X/2}
\left|\sum_{L\le n<2L}a_n n^{it}\right|^2dt
}{
X\sum_{L\le n<2L}|a_n|^2
},
\qquad X=L^{2/3}.
\]

If the off-diagonal behaves at random/diagonal scale, one expects `R_a=O(1)`.

## 2. Results

The audit used
`L=1024,2048,4096,8192,16384`
and
`tau=1.5,2.5,3.5`.

For actual Möbius coefficients all observed ratios lie between approximately

\[
0.69\quad\text{and}\quad1.29.
\]

Random signs on the same squarefree support also remain near `1`, with the observed run means roughly between `0.84` and `1.08`.

Thus the Möbius data are compatible with the desired diagonal scale but are not exceptional relative to the random-sign false control.

## 3. Positive support control

For `a_n=\mu(n)^2`, the normalized ratio is much smaller in this particular high-`t` window and decreases across much of the tested range; representative values at `tau=2.5` are approximately

\[
0.176,\ 0.135,\ 0.115,\ 0.089,\ 0.081.
\]

This shows that the multiplicative phase `n^{it}` itself can strongly cancel a smooth/nonnegative coefficient profile. Therefore a small finite mean square cannot by itself be attributed to Möbius parity.

Permanent guard:

`LONG_POLYNOMIAL_RANDOM_SCALE_FALSE_CONTROL`.

## 4. Interpretation

The finite data support only the scale statement

\[
\int_{I_X}
\left|\sum_{n\asymp L}\mu(n)n^{it}\right|^2dt
\asymp
X\sum_{n\asymp L}\mu(n)^2
\]

over the tested sizes.

They do **not** establish:
- a uniform asymptotic theorem;
- an `L^epsilon` bound at arbitrary `L`;
- a distinction from random signs;
- a new RH mechanism.

The positive-support result is especially important: high Mellin frequency already supplies deterministic oscillation for regular coefficients, while arbitrary rough signs can defeat such phase estimates. The hard proof problem is therefore to exploit enough arithmetic regularity of `mu` without assuming the random-variance conclusion.

## 5. Reproducibility

Numerical output is stored in

`data/mertens/long_mobius_polynomial_mean_square_2026-09-18.csv`.

The integral was evaluated on a uniform `t` grid; this is a diagnostic quadrature rather than a rigorous interval enclosure.

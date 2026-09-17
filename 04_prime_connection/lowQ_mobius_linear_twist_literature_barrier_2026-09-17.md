# Low-Q Möbius linear-twist literature barrier — 2026-09-17

## Status
- Riemann hypothesis: OPEN.
- Target sector: `K~D`, `Q<D^(1/3)`, hence `H=sqrt(D/Q)>D^(1/3)`.
- Local replacement of the reciprocal phase by an arbitrary linear Fourier twist: not sufficient with presently available integer Möbius estimates.
- The low-Q route must preserve additional reciprocal curvature / cross-scale structure or use genuinely new arithmetic input.

## 1. Tempting reduction
On a short `d`-block around `D0~D`,

\[
2K\sqrt n\,d^{-1/2}
\]

has local derivative of size

\[
\asymp H^{-1}.
\]

It is therefore tempting to replace the phase locally by

\[
e(\alpha m),\qquad \alpha\asymp H^{-1},
\]

and import a uniform estimate for

\[
\sum_{m\le X}\mu(m)e(\alpha m).
\]

The literature audit shows that this does not currently reach the required diagonal scale.

## 2. Classical unconditional scale
Davenport's classical theorem gives, uniformly in real `alpha`, for every fixed `A>0`,

\[
\sum_{n\le X}\mu(n)e(\alpha n)
\ll_A \frac{X}{(\log X)^A}.
\]

This is extremely strong logarithmic cancellation but still far from square-root cancellation on a polynomial scale.

Replacing the reciprocal phase by an arbitrary Fourier mode and using only this estimate therefore leaves a polynomial deficit relative to the present target.

## 3. Conditional uniform linear-twist scale
Baker–Harman (1991), under generalized-Riemann-hypothesis-type zero assumptions for Dirichlet `L`-functions, obtained a uniform estimate of the shape

\[
\max_{\theta\in[0,1)}
\left|\sum_{n\le X}\mu(n)e(n\theta)\right|
\ll_\varepsilon X^{3/4+\varepsilon}.
\]

Later work, including Wei Zhang's refinement, improves parts of this conditional theory under zero-free / zero-density hypotheses, but does not convert the unconditional integer problem into a square-root-scale uniform Fourier theorem.

Thus even the classical conditional linear-twist framework does not simply hand over the `X^(1/2+epsilon)` type control that would trivialize the present low-Q cell.

## 4. Why short-interval and k-free results do not close this branch
Modern results on Möbius cancellation in almost all short intervals and higher uniformity are important, but their stated average/logarithmic forms do not automatically imply a deterministic diagonal-size bound for every local reciprocal cell.

Likewise recent sharp results for squarefree or general `k`-free exponential sums concern the indicator `mu^2` or `k`-free weights, not the signed Möbius sequence itself. They are useful comparison classes, not direct substitutes for the needed signed estimate.

## 5. Classification

`LOW_Q_LINEAR_TWIST_LITERATURE_INSUFFICIENT`.

Do not replace the low-Q reciprocal problem by an arbitrary linear Möbius twist and then count Davenport/log-saving or known conditional `3/4`-type estimates as closure at RH scale.

## 6. Consequence
The low-Q sector must use at least one feature discarded by generic linearization:

1. reciprocal curvature across several local blocks;
2. signed compensation between distinct shift scales;
3. exact multiplicative structure of the Möbius coefficients coupled to that curvature;
4. a new estimate stronger than the currently imported linear-twist theory.

This narrows the live Sector-B question to the genuinely discrete reciprocal kernel rather than generic Fourier orthogonality.

## References retained for the literature ledger
- H. Davenport, *On some infinite series involving arithmetical functions (II)*, Quart. J. Math. 8 (1937), 313–320.
- R. C. Baker and G. Harman, *Exponential Sums Formed with the Möbius Function*, J. London Math. Soc. 43 (1991), 193–198, DOI 10.1112/jlms/s2-43.2.193.
- Wei Zhang, *On an exponential sum related to the Möbius function*, Proc. Amer. Math. Soc. (2024), arXiv:2204.04613, DOI 10.1090/PROC/16270.

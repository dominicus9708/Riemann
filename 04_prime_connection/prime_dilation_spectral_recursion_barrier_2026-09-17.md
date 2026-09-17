# Prime-dilation spectral recursion barrier — 2026-09-17

## Status
- Riemann hypothesis: OPEN.
- Exact prime-dilation identities for Liouville: DERIVED.
- Möbius squarefree-corrected recursion: DERIVED.
- Linear averaging of single-prime dilation identities: CLOSED as a polynomial-scale band-energy mechanism by a divisor-count signal/noise barrier.
- Nonlinear / joint-prime use of the dilation identities remains OPEN.

## 1. Liouville exact dilation
For a dyadic block define

\[
P_D^\lambda(\alpha)
:=\sum_{D<n\le2D}\lambda(n)e(\alpha n).
\]

For every prime `p`, complete multiplicativity gives `lambda(pm)=-lambda(m)`. Therefore

\[
\boxed{
\sum_{\substack{D<n\le2D\\p\mid n}}
\lambda(n)e(\alpha n)
=
-P_{D/p}^\lambda(p\alpha).
}
\]

The interval notation on the right means `D/p<m<=2D/p`, with the obvious integer endpoints.

Thus one prime divisor maps

\[
(D,\alpha)\mapsto(D/p,p\alpha).
\]

For a reciprocal band `alpha~1/H`, this is precisely

\[
(D,H)\mapsto(D/p,H/p).
\]

The scale ratio to the Sector-A boundary improves:

\[
\frac{H/p}{(D/p)^{1/3}}
=
\frac{H}{D^{1/3}}p^{-2/3}.
\]

So an exact prime dilation moves the configuration deeper into the high-frequency / smaller-`H` side.

Classification:

`LIOUVILLE_EXACT_PRIME_DILATION`.

## 2. Möbius corrected dilation
For

\[
P_D^\mu(\alpha)
:=\sum_{D<n\le2D}\mu(n)e(\alpha n),
\]

we have

\[
\boxed{
\sum_{\substack{D<n\le2D\\p\mid n}}
\mu(n)e(\alpha n)
=
-\sum_{\substack{D/p<m\le2D/p\\p\nmid m}}
\mu(m)e(p\alpha m).
}
\]

Writing the `p\nmid m` restriction as full sum minus the next divisible layer yields

\[
A_p(D,\alpha)
=-P_{D/p}^\mu(p\alpha)+A_p(D/p,p\alpha),
\]

where

\[
A_p(D,\alpha)
:=\sum_{\substack{D<n\le2D\\p\mid n}}\mu(n)e(\alpha n).
\]

Iterating to the first empty interval gives the exact finite recursion

\[
\boxed{
A_p(D,\alpha)
=-\sum_{k\ge1}P_{D/p^k}^\mu(p^k\alpha),
}
\]

with only finitely many nonempty terms.

Classification:

`MOBIUS_PRIME_DILATION_SQUAREFREE_RECURSION`.

## 3. Linear recovery from many primes
Let `mathcal P` be a finite prime set and choose real weights `w_p`. Define

\[
W(n)=\sum_{p\in\mathcal P}w_p1_{p\mid n},
\qquad
L=\sum_{p\in\mathcal P}\frac{w_p}{p}.
\]

For Liouville, the exact dilation identities imply

\[
\sum_{p\in\mathcal P}w_pP_{D/p}^\lambda(p\alpha)
=-\sum_{D<n\le2D}W(n)\lambda(n)e(\alpha n).
\]

Hence

\[
\boxed{
L P_D^\lambda(\alpha)
=-\sum_{p\in\mathcal P}w_pP_{D/p}^\lambda(p\alpha)
+E_{\mathcal P}(\alpha),
}
\]

where

\[
E_{\mathcal P}(\alpha)
=\sum_{D<n\le2D}(L-W(n))\lambda(n)e(\alpha n).
\]

This is an exact algebraic decomposition once `L` is chosen.

## 4. Parseval variance of the recovery error
Parseval gives

\[
\int_0^1|E_{\mathcal P}(\alpha)|^2d\alpha
=
\sum_{D<n\le2D}|L-W(n)|^2.
\]

Over a long dyadic interval the divisibility indicators have the usual Turán–Kubilius/CRT variance scale

\[
\sum_{D<n\le2D}|L-W(n)|^2
\asymp
D\sum_{p\in\mathcal P}\frac{w_p^2}{p}
\]

up to the standard lower-order endpoint/covariance terms.

For the unweighted choice `w_p=1`, the mean count is

\[
L\sim\sum_{p\in\mathcal P}\frac1p,
\]

so the relative `L^2` recovery error is only of order `L^{-1/2}`.

Even allowing arbitrary real weights cannot change the scale. Cauchy–Schwarz gives

\[
\boxed{
L^2
=\left(\sum_p\frac{w_p}{p}\right)^2
\le
\left(\sum_p\frac{w_p^2}{p}\right)
\left(\sum_p\frac1p\right).
}
\]

Thus the best possible linear signal-to-variance ratio from prime divisibility is bounded by

\[
\frac{L^2}{\sum_p w_p^2/p}
\le
\sum_{p\in\mathcal P}\frac1p.
\]

Using all primes up to a polynomial scale gives at most

\[
\sum_{p\le D^c}\frac1p
=\log\log D+O(1).
\]

Therefore every such linear recovery has an intrinsic relative RMS floor of order

\[
\boxed{(\log\log D)^{-1/2}}.
\]

Classification:

`PRIME_DILATION_LINEAR_SNR_BARRIER`.

## 5. Comparison with the reciprocal band target
The mesoscopic band target asks for an `L^2` norm reduction of order

\[
H^{-1/2}
\]

relative to placing all coefficient energy in a band of width `1/H`.

A linear prime-dilation reconstruction whose error is only

\[
(\log\log D)^{-1/2}
\]

cannot by itself provide this when `H` is a positive power of `D`.

Equivalently, using the error term alone on the target band gives a norm of size at best

\[
\sqrt{D/\log\log D},
\]

whereas the desired band norm is

\[
\sqrt{D/H}.
\]

The linear method would require an impossible effective divisor-count signal

\[
\sum_{p\in\mathcal P}\frac1p\gtrsim H
\]

instead of the available `O(log log D)`.

This explains why standard prime-factor averaging naturally yields logarithmic / doubly-logarithmic Fourier-uniformity gains rather than the polynomial spectral flattening required by the present band estimate.

## 6. Scope of the barrier
The result closes only the architecture

> single-prime dilation identities + real linear averaging + Parseval/Turán–Kubilius control of the divisor-count error.

It does **not** rule out:

1. nonlinear use of several prime labels simultaneously;
2. signed coupling between different dilation depths `p^k`;
3. retaining the exact reciprocal curvature while applying the dilation;
4. cancellation between the squarefree-support correction and parity layers for Möbius;
5. a genuinely high-order multiplicative identity whose signal/noise is not controlled by an additive prime-divisor count.

This distinction is important because the preceding parity audit indicates that the active broadband component is the multiplicative parity layer, while an additive count of visible prime divisors contains much less information.

## 7. Next direction
The next candidate must therefore use **joint multiplicative parity**, not merely the first moment of prime divisibility.

A natural audit is to form a two-depth or Boolean prime-dilation difference that cancels the additive divisor-count fluctuation before applying `L^2`, and then check whether it collapses back to:

- a low-order prime-label marginal (already barred),
- an ordinary Vaughan/Heath–Brown decomposition,
- or a new signed cross-scale operator that genuinely retains global parity.

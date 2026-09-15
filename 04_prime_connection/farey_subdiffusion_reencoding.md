# Farey subdiffusion and Mertens re-encoding audit

Status: exact scaling reformulation + classical Franel/Landau reduction + numerical null analysis.

## 1. Normalized gap walk
Let the Farey sequence of order n have m gaps
\[
g_j=r_{j+1}-r_j,\qquad j=0,\dots,m-1,
\]
with \(\sum g_j=1\). Define
\[
y_j=mg_j-1,
\qquad
S_k=\sum_{j<k}y_j.
\]
Then
\[
S_k=m\left(r_k-\frac{k}{m}\right)=m\delta_k,
\]
so Franel's quadratic discrepancy is exactly
\[
\boxed{
E_F(n)=\sum_{k=1}^{m-1}\delta_k^2
=\frac1{m^2}\sum_{k=1}^{m-1}S_k^2.
}
\]
Since \(m\sim 3n^2/\pi^2\), the RH-equivalent Franel condition
\[
E_F(n)=O_\varepsilon(n^{-1+\varepsilon})
\]
is equivalent, up to epsilon conversion, to
\[
\boxed{
\frac1m\sum_{k=1}^{m-1}S_k^2
=O_\varepsilon(m^{1/2+\varepsilon}).
}
\]
Thus the RMS normalized-gap partial sum must satisfy
\[
\boxed{S_{\rm rms}=O_\varepsilon(m^{1/4+\varepsilon}).}
\]
This is a strongly subdiffusive target. Generic finite-variance mixing/random-walk behavior would instead have RMS partial sums on the order \(m^{1/2}\).

## 2. Exact random-permutation expectation
For the centered gaps
\[
e_j=g_j-1/m,
\qquad \sum e_j=0,
\]
let \(\pi\) be a uniformly random permutation and
\[
T_k=\sum_{j<k}e_{\pi(j)}.
\]
Sampling without replacement gives exactly
\[
\mathbb E T_k^2
=\frac{k(m-k)}{m-1}\sigma_e^2,
\qquad
\sigma_e^2=\frac1m\sum_j e_j^2.
\]
Therefore
\[
\boxed{
\mathbb E\sum_{k=1}^{m-1}T_k^2
=\frac{m(m+1)}6\sigma_e^2
=\frac{m+1}{6m}\operatorname{Var}(y).
}
\]
No Monte-Carlo simulation is required for the random-order mean.

Representative values:

| n | m | actual E | exact random-order mean | random/actual |
|---:|---:|---:|---:|---:|
| 50 | 774 | 0.0097559 | 0.176689 | 18.1 |
| 100 | 3044 | 0.0051138 | 0.217649 | 42.6 |
| 200 | 12232 | 0.0031831 | 0.261715 | 82.2 |
| 400 | 48678 | 0.0015542 | 0.303765 | 195.4 |
| 800 | 194750 | 0.0007872 | 0.346559 | 440.3 |
| 1200 | 437786 | 0.0005281 | 0.371459 | 703.4 |
| 1600 | 778232 | 0.0004023 | 0.389179 | 967.5 |
| 2000 | 1216588 | 0.0003280 | 0.403023 | 1228.7 |

The natural Farey order therefore has genuine long-range cancellation relative to random ordering.

## 3. Balanced false control
The companion audit `farey_hminus1_order_audit.md` constructs a non-arithmetic balanced reordering of the same gap multiset. At n=2000,
\[
nE_{\rm actual}\approx0.6560,
\qquad
nE_{\rm balanced}\approx0.1010.
\]
Thus engineered balancing can beat the natural Farey order while using no determinant-one adjacency. Small Franel energy by itself is not an arithmetic uniqueness signature.

## 4. Long-range block-shuffle diagnostic
Preserve every adjacency inside contiguous blocks of B natural Farey gaps, but randomly permute the blocks. For n=1200 (m=437786), 20-null means gave approximately
\[
B=1024:\quad E_{\rm null}/E_{\rm actual}\approx87.4,
\]
\[
B=4096:\quad \approx4.40,
\]
\[
B=16384:\quad \approx1.44.
\]
Thus retaining thousands of exact local Farey transitions is insufficient to preserve the full low-frequency cancellation. The effect is genuinely long-range in Farey index.

This diagnostic is finite numerical evidence only; no asymptotic correlation length is claimed.

## 5. Classical Franel--Landau reduction
Landau's 1924 note starts from Littlewood's equivalence
\[
\mathrm{RH}\iff M(n)=O_\varepsilon(n^{1/2+\varepsilon})
\]
and recalls Franel's exact bridge. In Landau's notation one introduces a Mertens transform C(n) and a positive quadratic expression I(n) built from values of C at floor quotients; Franel's squared Farey discrepancy satisfies
\[
\boxed{
\sum_{\nu=1}^{A(n)}\eta_\nu(n)^2
=\frac1{A(n)}\left(I(n)-\frac1{12}\right).
}
\]
The RH-equivalent bound
\[
\sum_\nu \eta_\nu(n)^2=O_\varepsilon(n^{-1+\varepsilon})
\]
is then obtained from the same Mertens square-root control.

Thus the global Franel energy is historically and exactly a quadratic Mertens re-encoding, not an independent source of cancellation.

## 6. Dynamical interpretation and limitation
The BCZ map gives a canonical dynamical model for Farey ordering and is a Poincare section of horocycle flow. Cheung--Quas (2024) proved weak mixing, while mixing and rigidity remain open.

Qualitative weak mixing only rules out nontrivial eigenfunction atoms; it does not provide the quantitative depletion of spectral mass near frequency zero needed for the H^{-1} norm. The Franel target requires an m^{1/4+epsilon} RMS partial-sum law, far stronger than generic diffusive m^{1/2} behavior.

Classification:
- Farey local adjacency/statistics: mathematically structured;
- random-order separation: `NUMERICAL_ORDER_SIGNAL`;
- balanced low-energy reorder: `BALANCING_FALSE_CONTROL`;
- BCZ weak mixing alone: `INSUFFICIENT_FOR_RH_RATE`;
- Franel global L2 target: `MERTENS_QUADRATIC_REENCODING`.

## 7. Consequence for the project
The additive-lattice + multiplicative-coprimality idea is real, but the most direct Farey functional is already known to encode Mertens cancellation exactly. A new route must therefore use a different joint additive/multiplicative invariant whose quantitative bound does not algebraically reduce to Mertens, 1/zeta, or an equivalent Franel functional.

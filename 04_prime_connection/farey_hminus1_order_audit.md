# Farey H^{-1} order audit

Status: exact Fourier reformulation + numerical false-control audit.

## 1. Farey discrepancy as a cumulative gap walk
Let
\[
0=r_0<r_1<\cdots<r_m=1
\]
be the Farey sequence of order n, with m gaps. Put
\[
g_j=r_{j+1}-r_j,\qquad e_j=g_j-\frac1m.
\]
Then \(\sum_{j=0}^{m-1}e_j=0\), and the discrepancy from the uniform grid is
\[
\delta_k=r_k-\frac{k}{m}=\sum_{j<k}e_j,
\qquad \delta_0=\delta_m=0.
\]
Thus Franel's quadratic discrepancy is
\[
E_F(n)=\sum_{k=1}^{m-1}\delta_k^2.
\]

## 2. Exact discrete Fourier / H^{-1} identity
Use the DFT
\[
\widehat e_\ell=\sum_{j=0}^{m-1}e_j e^{-2\pi i\ell j/m}.
\]
Since \(e_j=\delta_{j+1}-\delta_j\), for \(1\le \ell\le m-1\),
\[
\widehat e_\ell=(e^{2\pi i\ell/m}-1)\widehat\delta_\ell.
\]
Parseval therefore gives
\[
\boxed{
E_F(n)=\frac1m\sum_{\ell=1}^{m-1}
\frac{|\widehat e_\ell|^2}
{|e^{2\pi i\ell/m}-1|^2}
}.
\]
Equivalently,
\[
E_F(n)=\frac1{4m}\sum_{\ell=1}^{m-1}
\frac{|\widehat e_\ell|^2}{\sin^2(\pi\ell/m)}.
\]
Hence the Franel energy is an exact discrete negative-Sobolev/H^{-1}-type energy of the centered Farey gap sequence. Low-frequency gap modes receive the strongest weight.

For consecutive Farey fractions \(a_j/b_j<a_{j+1}/b_{j+1}\),
\[
a_{j+1}b_j-a_jb_{j+1}=1,\qquad
 g_j=\frac1{b_jb_{j+1}}.
\]
Thus the natural Farey order imposes an arithmetic ordering on a positive gap multiset.

## 3. First permutation null
Keeping the exact gap multiset but randomly permuting the gaps destroys the small cumulative discrepancy energy by one to several orders of magnitude. Even left-right-symmetry-preserving permutations remain far above the actual Farey energy in tested ranges. This shows that the natural order carries genuine low-frequency cancellation beyond the unordered gap statistics.

However this alone is not an RH signal, because the target scale itself is RH-equivalent.

## 4. Balanced greedy false control
A stronger null was constructed using only the gap multiset and no Farey adjacency information. Let \(e_j=g_j-1/m\). Split the deviations into positive and negative lists, ordered from largest magnitude. Starting with partial sum S=0, at each step choose the next available positive or negative extreme which minimizes the next |S+e|. This creates a generic discrepancy-minimizing ordering.

Results:

| n | gaps m | actual E_F | n actual E_F | balanced E | n balanced E | balanced/actual |
|---:|---:|---:|---:|---:|---:|---:|
| 50 | 774 | 9.7559e-3 | 0.4878 | 3.6915e-3 | 0.1846 | 0.3784 |
| 100 | 3044 | 5.1138e-3 | 0.5114 | 1.0065e-3 | 0.1006 | 0.1968 |
| 200 | 12232 | 3.1831e-3 | 0.6366 | 6.1961e-4 | 0.1239 | 0.1947 |
| 400 | 48678 | 1.5542e-3 | 0.6217 | 5.0093e-4 | 0.2004 | 0.3223 |
| 800 | 194750 | 7.8717e-4 | 0.6297 | 1.3372e-4 | 0.1070 | 0.1699 |
| 1200 | 437786 | 5.2811e-4 | 0.6337 | 8.4359e-5 | 0.1012 | 0.1597 |

At n=1200 the balanced non-arithmetic ordering has about 6.26 times smaller energy than the natural Farey ordering.

Therefore:

\[
\boxed{
\text{small Franel energy is not unique to arithmetic Farey ordering.}
}
\]

Moreover, on this finite range the balanced null itself empirically has \(E=O(1/n)\), the same nominal scale that appears in the RH-equivalent Franel criterion. This is numerical only and is not an asymptotic theorem.

Classification:
- natural Farey ordering vs random permutation: `NUMERICAL_ORDER_SIGNAL`;
- small H^{-1} energy by itself: `BALANCING_FALSE_CONTROL`;
- actual Franel target \(E_F(n)=O_\varepsilon(n^{-1+\varepsilon})\): still RH-equivalent.

## 5. Dynamical literature audit
The BCZ map models Farey statistics and is a Poincare section of horocycle flow. Cheung--Quas (2024) proved weak mixing; mixing and rigidity remain open. Qualitative ergodicity/weak mixing cannot by itself supply the RH-equivalent quantitative discrepancy rate.

Therefore the route
\[
\text{BCZ ergodicity / weak mixing}\Rightarrow\text{Franel critical rate}
\]
is `INSUFFICIENT` without a new effective estimate at the required scale.

## 6. Remaining live question
The interesting problem is no longer whether one can arrange the Farey gap multiset with small cumulative energy; one can do so synthetically. The live arithmetic question is why the **canonical determinant-one Farey adjacency dynamics**, without global balancing optimization, attains an RH-equivalent low-frequency cancellation rate.

Any proposed mechanism must distinguish the natural BCZ/Farey orbit from discrepancy-minimizing artificial reorderings and must provide a quantitative effective rate, not only qualitative mixing.

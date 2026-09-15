# Weil explicit-formula support-resolution guard

Status: exact compact-support sensitivity bound + methodological false control.

## 1. Setup
Let g be an integrable test function supported in [-A,A], with Fourier transform
\[
\widehat g(z)=\int_{-A}^{A}g(u)e^{izu}\,du.
\]
In the Guinand-Weil explicit formula, support |u|<=A restricts the arithmetic prime-power contribution to log n<=A, i.e. n<=e^A (up to endpoint/convention details).

Suppose a hypothetical off-critical zero has
\[
\rho=\frac12+\delta+i\gamma.
\]
Functional equation and conjugation force the reflected zero at the same positive height,
\[
\rho^*=\frac12-\delta+i\gamma.
\]
On the spectral variable z=(rho-1/2)/i, the pair is \(\gamma\mp i\delta\).

## 2. Exact reflected-pair identity
Compare this reflected pair with two coincident critical-line zeros at height gamma. Then
\[
\begin{aligned}
&\widehat g(\gamma+i\delta)+\widehat g(\gamma-i\delta)-2\widehat g(\gamma)\\
&\qquad=2\int_{-A}^{A}g(u)e^{i\gamma u}\bigl(\cosh(\delta u)-1\bigr)\,du.
\end{aligned}
\]
Therefore
\[
\boxed{
|\Delta_{\delta,\gamma}(g)|
\le 2\|g\|_1\bigl(\cosh(|\delta|A)-1\bigr).
}
\]
This bound is independent of the height gamma; an adaptive test may modulate by the target frequency without changing support or L1 norm.

For |delta|A<=1,
\[
\boxed{
|\Delta_{\delta,\gamma}(g)|
\ll \|g\|_1\,\delta^2A^2.
}
\]
The first-order displacement cancels exactly because the zero set occurs in reflected pairs.

## 3. Prime-range form
Let
\[
X=e^A.
\]
Then any L1-normalized compact-support explicit-formula test using only prime powers up to X has robust reflected-pair sensitivity bounded by
\[
O\bigl((\delta\log X)^2\bigr)
\]
when |delta|log X is small.

Thus the natural stable horizontal resolution is
\[
\boxed{\delta_{\rm res}(X)\asymp1/\log X.}
\]
This upgrades the project's earlier synthetic `REFLECTION_RESOLUTION_GUARD` from a power-regression false control to the whole normalized compact-support linear explicit-formula class.

Classification: `WEIL_SUPPORT_RESOLUTION_GUARD`.

## 4. Quadratic Weil criterion
For Weil positivity one commonly takes
\[
g=f*\widetilde f,
\]
with supp f subset [-L,L], so supp g subset [-2L,2L]. Then A=2L and only prime powers with log n<2L enter the arithmetic side. The same reflected-pair bound applies to g.

Therefore positivity on any one fixed window is only a finite-resolution fragment of Weil's all-support criterion.

New false control:
`FINITE_WINDOW_POSITIVITY_FALSE_CONTROL` — numerical or certified positivity at fixed L does not by itself support RH unless the argument extends uniformly to unbounded support.

## 5. Condition-number caveat
The bound is normalized by \|g\|_1. One can amplify a tiny displacement response by allowing test-function norms or coefficient condition numbers to blow up. That does not beat the resolution barrier stably; it transfers the difficulty into arithmetic cancellation/precision and one-sided error control.

Therefore any proposed finite-X zero detector should report both displacement response and a norm/conditioning measure.

## 6. Relation to Li sensitivity
The standard Li basis is not height-adaptive. For a zero at height gamma and horizontal displacement delta its natural sensitivity scale is roughly n|delta|/(gamma^2+1/4), so high zeros require large Li index n. General compact-support Weil tests can adapt their oscillatory phase to gamma, removing this particular gamma^2 penalty, but they retain the universal reflected-pair support penalty |delta|A.

Thus the two guards measure different restrictions:
- Li: fixed universal basis, height-index penalty;
- Weil support: height-adaptive basis, arithmetic log-support penalty.

## 7. Recent compact-window literature
A September 2026 preprint by Marcus Chuk studies the compact-window profile
\[
\lambda^*(L)=\inf Q(f)/\|f\|_2^2
\]
for supp f subset [-L,L], gives certified positivity at fixed windows, and reports very rapid decay of the smallest margin as L grows. Because this is a recent preprint, it is used only as literature alignment, not as a foundational input here.

Its explicit formula also makes the support rule transparent: for supp f subset [-L,L], the autocorrelation has support [-2L,2L] and only prime powers with log n<2L contribute.

## 8. Project consequence
No finite-range prime computation in the compact-support explicit-formula class can robustly resolve arbitrary reflected departures much smaller than 1/log X without paying a diverging conditioning cost. A proof of RH must therefore either:
1. control an unbounded family of supports uniformly, or
2. use a nonlinear/noncompact mechanism outside this normalized test class.

This does not prove a universal information-theoretic impossibility for all algorithms using primes <=X; it is a precise barrier for normalized compact-support explicit-formula tests.

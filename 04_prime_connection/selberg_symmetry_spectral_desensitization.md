# Selberg symmetry: spectral desensitization audit

Status: exact Dirichlet-series structure + method barrier; no RH proof.

## 1. Selberg's second von Mangoldt function
Define
\[
\Lambda_2=\mu*\log^2.
\]
Equivalently,
\[
\boxed{\Lambda_2(n)=\Lambda(n)\log n+(\Lambda*\Lambda)(n).}
\]
Selberg's symmetry formula gives
\[
\sum_{n\le x}\Lambda_2(n)=2x\log x+O(x).
\]
This is the arithmetic engine in the elementary proof of the prime number theorem.

## 2. Dirichlet-series identity
Let
\[
L(s)=-\frac{\zeta'(s)}{\zeta(s)}=\sum_{n\ge1}\frac{\Lambda(n)}{n^s}.
\]
Then
\[
\sum_{n\ge1}\frac{\Lambda(n)\log n}{n^s}=-L'(s),
\qquad
\sum_{n\ge1}\frac{(\Lambda*\Lambda)(n)}{n^s}=L(s)^2.
\]
Hence
\[
\boxed{
\sum_{n\ge1}\frac{\Lambda_2(n)}{n^s}
=L(s)^2-L'(s)=\frac{\zeta''(s)}{\zeta(s)}.
}
\]

## 3. Cancellation of the strongest zero singularity
At a simple zero \(\rho\) of \(\zeta\), write locally
\[
L(s)=-\frac1{s-\rho}+c_0+O(s-\rho).
\]
Then
\[
L(s)^2=\frac1{(s-\rho)^2}-\frac{2c_0}{s-\rho}+O(1),
\]
while
\[
L'(s)=\frac1{(s-\rho)^2}+O(1).
\]
Therefore
\[
\boxed{
L(s)^2-L'(s)
=-\frac{2c_0}{s-\rho}+O(1).
}
\]
The double pole cancels exactly. Thus the prime and semiprime channels in Selberg's symmetry formula cancel the strongest simple-zero response and leave only a simple pole.

For a zero of multiplicity m, the remaining double-pole coefficient is \(m(m-1)\), so the cancellation is complete at double-pole order precisely for simple zeros.

Classification: `SPECTRAL_DESENSITIZATION`.

## 4. Why the O(x) symmetry remainder cannot locate the critical line
A simple zero with real part \(\beta<1\) contributes an \(x^\rho\)-scale secondary term to Perron-type summatory formulas for \(\zeta''/\zeta\). The unconditional Selberg remainder \(O(x)\) is compatible with every such \(\beta<1\).

Hence the classical symmetry formula is strong enough for PNT but too coarse to distinguish \(\beta=1/2\) from any other interior exponent.

To make this channel an RH detector one would need a genuinely RH-scale remainder after subtracting all main terms, not merely the classical O(x) estimate.

## 5. Standard recursive PNT inequality loses polynomial exponents
A standard consequence of the symmetry method has the schematic form
\[
\frac{|R(x)|}{x}
\lesssim
\frac1{\log x}\int_1^x\frac{|R(u)|}{u^2}\,du
+\text{lower-order terms},
\qquad R(x)=\psi(x)-x.
\]
Set \(x=e^y\) and \(f(y)=|R(e^y)|/e^y\). The leading operator is the Hardy/Cesaro average
\[
(Af)(y)=\frac1y\int_0^y f(v)\,dv.
\]
For a polynomial-error mode \(R(x)\asymp x^\beta\), \(\beta<1\), one has
\[
f(y)\asymp e^{-(1-\beta)y},
\]
but
\[
Af(y)\asymp \frac1{(1-\beta)y},
\]
so the power exponent is erased and replaced by logarithmic decay. This operator is well suited to proving \(R(x)=o(x)\), not to preserving or improving a specific polynomial exponent such as 1/2.

Classification: `SELBERG_HARDY_AVERAGING_BARRIER` for the standard recursive route.

## 6. Higher Selberg order does not automatically restore exponent sensitivity
For fixed k,
\[
\Lambda_k:=\mu*\log^k,
\qquad
\sum_{n\ge1}\frac{\Lambda_k(n)}{n^s}
=(-1)^k\frac{\zeta^{(k)}(s)}{\zeta(s)}.
\]
At a simple zero \(\rho\), this quotient has at most a simple pole (and may even lose that pole if \(\zeta^{(k)}(\rho)=0\)). Increasing fixed k changes amplitudes and arithmetic support but does not change the spectral exponent \(\Re\rho\).

Therefore `raise Selberg order k` is not by itself a mechanism selecting 1/2.

## 7. Project consequence
The Selberg symmetry route demonstrates a genuine arithmetic bilinear mechanism, but its classical power comes from smoothing/cancellation that also suppresses zero sensitivity. A surviving variant would need a scale-localized bilinear estimate that retains polynomial exponent information and does not collapse to known Type-II/Vaughan/zero-density machinery.

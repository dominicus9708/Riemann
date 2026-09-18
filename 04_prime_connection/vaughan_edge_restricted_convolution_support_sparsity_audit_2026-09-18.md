# Vaughan-edge restricted-convolution support sparsity audit — 2026-09-18

## Status
- Riemann hypothesis: OPEN.
- Candidate: after product collapse `r=dw`, hope that the restricted coefficient `Gamma_{V,L}(r)` is supported on a polynomially sparse set.
- Conclusion: FALSE. An elementary semiprime subfamily already gives support size `K/(log K)^2` up to constants when `VL~K`.
- Ford's divisor-in-an-interval theory independently confirms that the ambient divisor condition has only logarithmic, not polynomial, sparsity.
- Classification: `RESTRICTED_CONVOLUTION_SUPPORT_NOT_POWER_SPARSE`.

## 1. Product-collapsed edge coefficient

At the critical Vaughan edge,

\[
\Gamma_{V,L}(r)
=
\sum_{\substack{dw=r\\d\asymp V,\ w\asymp L}}
\mu(d)\mu(w),
\qquad
VL\asymp K,
\]

with the extreme scales

\[
V\asymp K^{1/4},
\qquad
L\asymp K^{3/4}.
\]

A necessary condition for `Gamma_{V,L}(r)\ne0` is that `r` possess a divisor in the short multiplicative interval `d\asymp V`.

## 2. Elementary semiprime lower bound

Restrict to

\[
d=p\in[V,2V],
\qquad
w=q\in[L,2L],
\]

with `p,q` prime.

Because `L\gg V`, the prime factors are separated in scale. The product

\[
r=pq
\]

determines `p` and `q` uniquely in these two ranges.

Moreover

\[
\mu(p)\mu(q)=(-1)(-1)=+1,
\]

and the divisors of `pq` are `1,p,q,pq`; only `p` lies in the short `V`-range. Therefore this subfamily contributes

\[
\Gamma_{V,L}(pq)=+1.
\]

By the prime number theorem, the number of such distinct products is

\[
\asymp
\frac{V}{\log V}
\frac{L}{\log L}
\asymp
\boxed{
\frac{K}{(\log K)^2}
}.
\]

Thus the exact support satisfies the unconditional lower-order statement

\[
|\operatorname{supp}\Gamma_{V,L}|
\ge K^{1-o(1)}.
\]

In particular it is not `O(K^{3/4+epsilon})` by cardinality alone.

## 3. Comparison with divisor-in-an-interval theory

Kevin Ford's work on

\[
H(x,y,2y)
=
\#\{n\le x:\exists d\mid n,\ y<d\le2y\}
\]

shows that the ambient set of integers possessing a divisor in a dyadic interval has density tending to zero only at logarithmic/subpower scale. In particular the classical density exponent is

\[
\delta
=
1-\frac{1+\log\log2}{\log2}
=
0.086071\ldots
\]

in the `(y,2y]` problem, with the full 2008 theorem determining the order of magnitude in all ranges.

For the present purpose the elementary semiprime lower bound is already enough, so no fine form of Ford's theorem is needed in the proof audit.

References:
- K. Ford, *The distribution of integers with a divisor in a given interval*, Ann. of Math. 168 (2008), 367--433.
- K. Ford, *Integers with a divisor in (y,2y]*, CRM Proc. Lecture Notes 46 (2008).

## 4. Consequence

The route

`restricted product support -> polynomial sparsity -> K^(1/4) saving`

is closed.

Any successful estimate for

\[
\sum_r\Gamma_{V,L}(r)e(Ar^{-1/2})
\]

must exploit cancellation of phases and/or arithmetic coefficients, not merely that `Gamma` is supported on products having a divisor near `V`.

Permanent guard:

`DIVISOR_INTERVAL_SUPPORT_SPARSITY_GUARD`.

## 5. Additional warning

The semiprime subfamily has coherent coefficient sign `+1`. Therefore even on a large explicit subset there is no Möbius sign cancellation to appeal to.

This does not prove that the semiprime contribution is large: the reciprocal phase can still oscillate. It only rules out support size or factor-sign randomness as the source of the missing polynomial saving.

# Large-prime tail / truncated-parity audit at the Vaughan edge — 2026-09-18

## Status
- Riemann hypothesis: OPEN.
- Candidate: exploit the fact that the critical long Möbius variable has only finitely many prime factors above the Vaughan threshold.
- Exact bounded-tail statement: TRUE.
- Polynomial sparsity of the remaining small-prime sector: FALSE.
- Transfer from known truncated-Möbius correlation theorems: NOT AVAILABLE in the present fixed-`u` regime.
- Structural classification: finite-depth Buchstab/Heath--Brown re-expression, not an automatic new cancellation mechanism.

## 1. Critical scales

At the hardest Vaughan edge write

\[
V=K^{1/4},
\qquad
L=K^{3/4}=V^3,
\qquad
w\asymp L.
\]

For squarefree `w`, split its prime factors into
- small primes `p<=V`;
- large primes `p>V`.

If `w<=2L=2V^3` and `V>2`, four prime factors larger than `V` would have product

\[
>V^4>2V^3.
\]

Hence

\[
\boxed{
\#\{p\mid w:p>V\}\le3.
}
\]

Thus the large-prime tail has bounded depth.

## 2. Exact parity decomposition

For squarefree `w`, write

\[
w=a p_1\cdots p_j,
\qquad
0\le j\le3,
\]

where every prime factor of `a` is at most `V` and every `p_i>V`.

Then

\[
\mu(w)=(-1)^j\mu(a).
\]

Accordingly the long Möbius sum can be decomposed exactly into four sectors `j=0,1,2,3`, with a residual `V`-smooth squarefree coefficient `mu(a)`.

This is useful bookkeeping, but the parity difficulty has not disappeared: it has moved into `mu(a)`.

## 3. The smooth sector is not polynomially sparse

Classically, for fixed `u`,

\[
\Psi(x,x^{1/u})\sim\rho(u)x.
\]

Here `x=L=V^3`, `y=V=L^{1/3}`, so `u=3` and

\[
\Psi(L,V)\sim \rho(3)L,
\qquad
\rho(3)\approx0.0486083883>0.
\]

Thus the set of `V`-smooth integers itself has positive asymptotic density at this fixed smoothness parameter.

For the Möbius-supported squarefree sector one does not even need a refined smooth-squarefree theorem to rule out polynomial sparsity.

Choose four distinct primes in a short interval

\[
p_i\asymp V^{3/4}
\]

whose multiplicative endpoints are selected so that

\[
L\le p_1p_2p_3p_4\le2L.
\]

Unique factorization then gives

\[
\gg \frac{V^3}{(\log V)^4}
\asymp
\frac{L}{(\log L)^4}
\]

distinct squarefree `V`-smooth integers in the dyadic `w` range. Each has

\[
\mu(w)=+1.
\]

Therefore even the `j=0` sector is

\[
L^{1-o(1)}
\]

in cardinality.

Classification:

`SMOOTH_MOBIUS_SECTOR_NOT_POWER_SPARSE`.

## 4. Why truncated-Möbius correlation theorems do not close the gap

A natural truncated parity is

\[
\mu_y(n)=\mu(n)^2(-1)^{\omega_y(n)},
\]

where `omega_y` counts prime factors at most `y`.

Quantitative bivariate Erdős--Kac / truncated-Möbius correlation results study regimes in which

\[
\beta=\frac{\log x}{\log y}\to\infty.
\]

At the present edge,

\[
x=L,
\qquad
y=V=L^{1/3},
\qquad
\boxed{\beta=3.}
\]

The parameter is fixed, not divergent.

Therefore those results cannot be inserted as a theorem controlling the present full-parity sector.

Moreover

\[
\mu(w)
=
\mu_V(w)(-1)^{\omega_{>V}(w)}
\]

on squarefree integers. Although `omega_{>V}(w)<=3`, the residual factor is not negligible and the small-prime parity `mu_V(w)` still ranges over a polynomial-size set.

Classification:

`TRUNCATED_MOBIUS_BETA_FIXED_TRANSFER_FAILURE`.

## 5. Relation to Buchstab / Heath--Brown decompositions

Sorting integers by the number and order of prime factors above a threshold is a finite Buchstab-type decomposition.

Because the large-prime depth is bounded by 3 here, it yields a finite family of multilinear sums. But merely exposing these variables does not change the previously audited facts:

1. regrouping into arbitrary coefficient blocks re-enters the dense-spacing DLS barrier;
2. recursively decomposing a long Möbius factor re-enters the reciprocal self-dual Vaughan scale;
3. collapsing to the product variable restores a restricted Möbius convolution;
4. the smooth residual sector remains of polynomial size.

Thus bounded tail depth is a structural simplification, not yet a power saving.

## 6. Surviving possibility

The only reason to retain this decomposition is if one of the finite sectors has **extra phase geometry tied to ordered large primes** that survives product collapse and is absent in generic Buchstab regrouping.

Any future use must therefore keep the ordered prime variables through the oscillatory estimate. If the calculation immediately regroups them into one product coefficient or applies modulus bounds to all prime sums, classify it as re-entry rather than progress.

Permanent guards:
- `BOUNDED_LARGE_PRIME_TAIL_NOT_SPARSE`.
- `TRUNCATED_PARITY_FIXED_U_GUARD`.
- `FINITE_BUCHSTAB_DEPTH_NOT_AUTOMATIC_SAVING`.

## References
- Dickman--de Bruijn smooth-number law: `Psi(x,x^(1/u)) ~ rho(u)x` for fixed `u`.
- A. P. Mangerel, *On the Bivariate Erdos-Kac Theorem and Correlations of the Möbius Function* (2016/2018): truncated Möbius correlations in a regime with `beta=log x/log y -> infinity`.

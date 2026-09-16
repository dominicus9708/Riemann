# Möbius–divisor-error bridge audit — 2026-09-16

## Status
- Riemann hypothesis: OPEN.
- Classical decomposition `log - d + 2 gamma`: STANDARD / already used in elementary PNT proofs.
- Exact refinement by the Dirichlet divisor error: EXACT.
- Quotient-block form: EXACT.
- Barnes-G integrated form: EXACT.
- Absolute transfer from divisor-error bounds to prime-error bounds: CLOSED / no polynomial saving.
- Independent floor-quotient route: NOT NEW; it falls into the already-audited quotient/Mertens block-increment structure.
- Surviving question: whether the *special oscillatory kernel* coming from the divisor error has extra cancellation against the Mertens block increments beyond generic floor-quotient inversion.

## 1. Classical arithmetic decomposition

Let `tau(n)` be the divisor function and let `gamma` be Euler's constant. Define

\[
b(n)=\log n-\tau(n)+2\gamma.
\]

Since

\[
\tau=\mathbf 1*\mathbf 1,
\qquad
\mu*\mathbf 1=\delta,
\qquad
\Lambda=\mu*\log,
\]

we have exactly

\[
\boxed{
\Lambda
=\mathbf 1-2\gamma\,\delta+\mu*b.
}
\]

This identity is standard; Granville–Soundararajan use this same `log n-d(n)+2gamma` decomposition in an elementary proof of the prime number theorem.

## 2. Exact refinement by the divisor problem

For integer `y>=1`, define

\[
D(y)=\sum_{n\le y}\tau(n),
\]

and the standard Dirichlet divisor error

\[
\Delta(y)=D(y)-y\log y-(2\gamma-1)y.
\]

Also define the Stirling lattice remainder

\[
S(y)=\log(y!)-y\log y+y.
\]

The summatory function of `b` is then exactly

\[
B(y):=\sum_{n\le y}b(n)
=\log(y!)-D(y)+2\gamma y,
\]

hence

\[
\boxed{B(y)=S(y)-\Delta(y).}
\]

This is not merely an asymptotic relation.

Since

\[
S(y)=\frac12\log(2\pi y)+O(1/y),
\]

the genuinely oscillatory part of `B` is the divisor-error term `-Delta(y)`.

## 3. Exact prime-error bridge

Summing the convolution identity to an integer cutoff `N` gives

\[
\psi(N)-N
=-2\gamma
+\sum_{d\le N}\mu(d)
B\!\left(\left\lfloor\frac Nd\right\rfloor\right).
\]

Thus

\[
\boxed{
\psi(N)-N
=-2\gamma+C_S(N)-C_\Delta(N),
}
\]

where

\[
C_S(N)=\sum_{d\le N}\mu(d)
S\!\left(\left\lfloor\frac Nd\right\rfloor\right),
\]

and

\[
C_\Delta(N)=\sum_{d\le N}\mu(d)
\Delta\!\left(\left\lfloor\frac Nd\right\rfloor\right).
\]

The RH-scale issue is therefore not the size of `Delta` alone; it is the correlated cancellation of two Möbius-transformed lattice/divisor pieces.

## 4. Quotient-block form and reappearance of Mertens increments

Let

\[
M(x)=\sum_{n\le x}\mu(n).
\]

Group the `d`-sum by the floor quotient

\[
q=\left\lfloor\frac Nd\right\rfloor.
\]

Then exactly

\[
\boxed{
\psi(N)-N
=-2\gamma
+\sum_{q=1}^{N}B(q)
\left[
M\!\left(\left\lfloor\frac Nq\right\rfloor\right)
-
M\!\left(\left\lfloor\frac N{q+1}\right\rfloor\right)
\right].
}
\]

The bracket is precisely the Mertens block increment over

\[
\frac{N}{q+1}<d\le\frac Nq.
\]

Therefore the additive/divisor kernel does not remove the multiplicative difficulty: it weights the same quotient-block Mertens increments already identified in `floor_quotient_poset_bridge_audit.md`.

Classification:

`DIVISOR_KERNEL_QUOTIENT_REENTRY`.

## 5. Absolute-transfer barrier

Suppose only that

\[
B(q)=O(q^\alpha L(q))
\]

for some `alpha<1` and a slowly varying factor `L`.

Taking absolute values in the original `d`-sum gives

\[
\sum_{d\le N}
\left|B\!\left(\left\lfloor\frac Nd\right\rfloor\right)\right|
\ll
N^\alpha L(N)\sum_{d\le N}d^{-\alpha}
\asymp N L(N).
\]

Equivalently, in quotient form the trivial interval-length bound

\[
\left|
M\!\left(\left\lfloor\frac Nq\right\rfloor\right)
-
M\!\left(\left\lfloor\frac N{q+1}\right\rfloor\right)
\right|
\le
\frac{N}{q(q+1)}+1
\]

again gives only linear scale.

Hence even a conjectural divisor-problem bound near `q^(1/4+epsilon)` does **not** transfer to a nontrivial prime-error bound without signed Möbius cancellation.

Permanent guard:

`DIVISOR_ERROR_ABSOLUTE_TRANSFER_BARRIER`.

## 6. Integrated / Barnes-G exact form

For an integer `N`, define the once-integrated Chebyshev sum

\[
\Psi_1(N)
:=\sum_{n\le N}\Lambda(n)(N-n).
\]

Using `Lambda=mu*log`, write

\[
q_d=\left\lfloor\frac Nd\right\rfloor,
\qquad
r_d=N-dq_d.
\]

Then exactly

\[
\Psi_1(N)
=
\sum_{d\le N}\mu(d)
\left[
N\log(q_d!)-d\sum_{m=1}^{q_d}m\log m
\right].
\]

Since

\[
q\log(q!)-\sum_{m=1}^{q}m\log m
=\sum_{j=1}^{q-1}\log(j!),
\]

we obtain

\[
\boxed{
\Psi_1(N)
=
\sum_{d\le N}\mu(d)
\left[
 d\log G(q_d+1)
+r_d\log\Gamma(q_d+1)
\right],
}
\]

where `G` is the Barnes G-function.

This is an exact additive-lattice/multiplicative-inversion representation.

## 7. Why the Barnes-G representation is not by itself a new RH route

The smooth asymptotic of the Barnes kernel produces weighted reciprocal-Möbius sums such as

\[
F(X)=\sum_{n\le X}\frac{\mu(n)}n\log\frac Xn.
\]

Its Mellin/Perron kernel is

\[
\frac{1}{s^2\zeta(1+s)}.
\]

The residue at `s=0` gives the main value `1`, while every nontrivial zeta zero `rho` produces a pole at

\[
s=\rho-1.
\]

Therefore an error estimate on the scale

\[
F(X)-1=O_\varepsilon(X^{-1/2+\varepsilon})
\]

is already RH-scale spectral information.

Classification:

`BARNES_RECIPROCAL_REENCODING_GUARD`.

The factorial/Barnes notation makes the integer lattice explicit but does not by itself remove the reciprocal-zeta obstruction.

## 8. Relation to the integrated divisor problem

The integrated divisor error is much smoother than the pointwise divisor error. Voronoi/Ivic-type formulas give an oscillatory expansion of natural size `x^(3/4)` for

\[
\int_1^x\Delta(u)\,du.
\]

This is potentially useful only in the small-`d` part of the Möbius transform. For large `d`, the quotient `N/d` is small and quotient grouping turns the same contribution back into Mertens interval increments. Thus smoothing the divisor side alone does not globally remove the multiplicative obstruction.

Classification:

`VORONOI_SMALL_D_MERTENS_LARGE_D_DUALITY`.

## 9. Numerical diagnostic

A direct exact computation through `N=120000` verifies the bridge to floating roundoff.

At sampled cutoffs `N=1000,2000,...,120000`, define `C_S,C_Delta` as above. The two transformed components are strongly correlated over this finite range (sample Pearson correlation about `0.964`), while their exact difference reconstructs `psi(N)-N+2gamma`.

Representative values:

- `N=10000`: `C_S~-25.147`, `C_Delta~-39.698`, `psi(N)-N~13.397`;
- `N=50000`: `C_S~5.792`, `C_Delta~18.680`, `psi(N)-N~-14.042`;
- `N=100000`: `C_S~-47.695`, `C_Delta~-100.414`, `psi(N)-N~51.564`.

This correlation is only a finite diagnostic; it is not evidence for RH. The exact identity already forces the *difference* to be the prime error.

## 10. Current consequence

This route does produce a genuine bridge between:

1. the multiplicative Möbius structure;
2. the additive integer-lattice/divisor error structure;
3. the prime error `psi(N)-N`.

However, generic floor-quotient inversion and absolute divisor-error estimates are already closed.

The only potentially independent continuation is therefore:

\[
\boxed{
\text{Does the special oscillatory kernel }B(q)=S(q)-\Delta(q)
\text{ force extra signed cancellation against the Mertens block increments?}
}
\]

Any such claim must exceed the information contained in the generic quotient inverse and must not merely restate an RH-scale bound for `M(x)` or `1/zeta(s)`.

Suggested audit tag:

`DIVISOR_KERNEL_WEIGHTED_QUOTIENT_CORRELATION_OPEN`.

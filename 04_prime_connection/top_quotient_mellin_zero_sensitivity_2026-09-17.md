# Top-quotient Mellin zero-sensitivity audit — 2026-09-17

## Status
- Riemann hypothesis: OPEN.
- Top-quotient decomposition: EXACT.
- Mellin multiplier for every fixed top-quotient window: EXACT.
- `q=1` top-half Mertens block: full sensitivity to every nontrivial zeta zero.
- Fixed finite quotient locality as a zero-erasing mechanism: CLOSED in the generic sense; a finite exponential multiplier cannot cancel the full zeta zero set.
- Growing-`Q` nonlinear interaction: still OPEN.

## 1. Top quotient blocks

Let

\[
U_q(N):=
M\!\left(\left\lfloor\frac Nq\right\rfloor\right)
-
M\!\left(\left\lfloor\frac N{q+1}\right\rfloor\right)
=
\sum_{N/(q+1)<d\le N/q}\mu(d).
\]

The large-`d` side of the Möbius–divisor bridge is built from these blocks with coefficients `B(q)`.

For a fixed integer `Q>=1`, define

\[
T_Q(N):=\sum_{q\le Q}B(q)U_q(N).
\]

Equivalently,

\[
T_Q(N)=\sum_{d\ge1}\mu(d)w_Q(d/N),
\]

where the compact step weight is

\[
w_Q(x)=B(q)
\quad\text{for}\quad
\frac1{q+1}<x\le\frac1q,
\qquad q\le Q,
\]

and zero outside the union of these intervals.

## 2. Exact Mellin multiplier

For `Re(s)>0`,

\[
\widehat w_Q(s)
:=\int_0^\infty w_Q(x)x^{s-1}\,dx
\]

is exactly

\[
\boxed{
\widehat w_Q(s)
=
\frac1s
\sum_{q\le Q}B(q)
\left(q^{-s}-(q+1)^{-s}\right).
}
\]

Mellin inversion gives the formal/standard Perron representation

\[
T_Q(N)
=
\frac1{2\pi i}
\int_{(c)}
\frac{\widehat w_Q(s)}{\zeta(s)}N^s\,ds,
\qquad c>1,
\]

with the usual endpoint convention for the step weight.

Thus a nontrivial zeta zero `rho` contributes a pole whenever

\[
\widehat w_Q(\rho)\ne0.
\]

## 3. The top-half block is a complete zero detector

For `Q=1`,

\[
T_1(N)=B(1)\,[M(N)-M(\lfloor N/2\rfloor)].
\]

Since

\[
B(1)=b(1)=2\gamma-1\ne0,
\]

we have

\[
\boxed{
\widehat w_1(s)
=
\frac{2\gamma-1}{s}(1-2^{-s}).
}
\]

If `rho` is any nontrivial zeta zero, then `0<Re(rho)<1`, so

\[
|2^{-\rho}|=2^{-\operatorname{Re}\rho}<1.
\]

Hence

\[
1-2^{-\rho}\ne0.
\]

Therefore

\[
\boxed{
\widehat w_1(\rho)\ne0
\quad\text{for every nontrivial zeta zero }\rho.
}
\]

The top-half Mertens increment by itself retains the complete nontrivial zero obstruction.

Classification:

`TOP_HALF_MERTENS_FULL_ZERO_SENSITIVITY`.

This explains why the large-`d` half cannot be treated as a harmless low-quotient remainder.

## 4. Fixed finite Q cannot erase the whole zeta spectrum

For fixed `Q`, the numerator

\[
s\widehat w_Q(s)
=\sum_{q\le Q}B(q)(q^{-s}-(q+1)^{-s})
\]

is a finite exponential polynomial in `s`, with finitely many real frequencies `log q` and `log(q+1)`.

Unless it is identically zero, it is an entire function of finite exponential type, whose zero count in a vertical disk/strip grows at most linearly with the height parameter.

By contrast, the Riemann-von Mangoldt zero count for zeta grows like

\[
N_\zeta(T)\sim\frac{T}{2\pi}\log\frac{T}{2\pi}.
\]

Therefore no fixed nonzero finite-`Q` multiplier can vanish at the full nontrivial zeta zero set.

This does not exclude accidental cancellation of particular zeros. It shows that fixed finite quotient locality is not a universal zero-erasing mechanism.

Classification:

`FIXED_TOP_QUOTIENT_SPECTRAL_LOCALITY_BARRIER`.

## 5. Consequence for the live route

The large-`d` obstruction is sharper than a generic Mertens re-entry statement:

1. the `q=1` block alone already sees every nontrivial zero;
2. any fixed finite collection of quotient blocks remains a finite Mellin multiplier and cannot cancel the complete zeta spectrum;
3. therefore a route based on bounded quotient depth cannot explain RH-scale cancellation by local compensation alone.

A genuinely new large-`d` mechanism must use quotient depth growing with `N`, or another arithmetic structure coupling an unbounded number of quotient blocks.

Permanent guard:

`BOUNDED_QUOTIENT_DEPTH_GUARD` — do not promote a fixed finite top-quotient compensation identity to an RH mechanism unless its Mellin multiplier analysis is performed. Bounded quotient depth cannot erase the full zeta spectrum.

## 6. Updated open target

The surviving large-`d` target is now:

\[
\boxed{
\text{Find a genuinely growing-depth nonlinear relation among }U_q(N)
\text{ that is not reducible to a finite Mellin multiplier, Abel transform,}\
\text{or generic Mertens quotient geometry.}
}

This target is complementary to the small-`d` Voronoi–Möbius reciprocal-phase module.

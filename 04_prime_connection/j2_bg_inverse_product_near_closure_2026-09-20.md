# j=2 two-factor boundary: Bourgain--Garaev inverse-product near-closure — 2026-09-20

## Status
- Riemann hypothesis: OPEN.
- Hard core:
  \[
  q=e\,r\,s,\qquad
  e\asymp H^{3/2},\quad
  r,s\asymp H^{3/4},
  \]
  so
  \[
  k:=rs\asymp H^{3/2}.
  \]
- Opposite prime modulus scale:
  \[
  p\asymp H^3.
  \]
- Thus
  \[
  e\asymp k\asymp \sqrt p.
  \]
- New literature match: Bourgain--Garaev Theorem 9 gives an explicit \(p^{-1/16}\) saving for arbitrary bounded weights in
  \[
  \sum_{e\sim\sqrt p}\sum_{k\sim\sqrt p}
  \alpha_e\beta_k e_p(c\bar e\bar k).
  \]
- Required amplitude-side saving is only
  \[
  H^{-1/8}=p^{-1/24}.
  \]
- Hence a legal reduction to this exact normal form has spare margin
  \[
  p^{-1/48}=H^{-1/16}.
  \]
- Classification: \`J2_BG_INVERSE_PRODUCT_SUFFICIENT_IF_LEGAL_NORMAL_FORM\`.

## 1. Two-factor Type-III scale

At the sharp boundary,
\[
e\asymp H^{3/2},
\qquad
r,s\asymp H^{3/4}.
\]

Relative to
\[
q\asymp H^3,
\]
this is
\[
\boxed{
q^{1/2}\times q^{1/4}\times q^{1/4}.
}
\]

Combining the two small factors,
\[
k=rs\asymp H^{3/2},
\]
gives
\[
\boxed{
e\asymp k\asymp H^{3/2}.
}
\]

If the opposite original prime
\[
p\asymp H^3
\]
is retained as a prime modulus, then
\[
\boxed{
e,k\asymp p^{1/2}.
}
\]

The semiprime coefficient on k is divisor-bounded and supported in an ordinary dyadic interval, so a theorem allowing arbitrary bounded interval weights can absorb it up to \(H^\varepsilon\).

## 2. Bourgain--Garaev Theorem 9

Bourgain--Garaev prove, for arbitrary intervals \(I_1,I_2\subset\mathbf F_p\) of lengths \(N_1,N_2\) and bounded weights,
\[
\left|
\sum_{x_1\in I_1}\sum_{x_2\in I_2}
\alpha_1(x_1)\alpha_2(x_2)
e_p(a x_1^{-1}x_2^{-1})
\right|
\]
\[
\ll
p^{1/8}
N_1^{3/4}N_2^{3/4}
\left(\frac{N_1^3}{p}+1\right)^{1/16}
\left(\frac{N_2^3}{p}+1\right)^{1/16}
p^{o(1)}.
\]

At
\[
N_1=N_2=p^{1/2},
\]
the first factor is
\[
p^{1/8}p^{3/8}p^{3/8}
=
p^{7/8},
\]
while each bracket contributes
\[
(p^{1/2}+1)^{1/16}
=
p^{1/32+o(1)}.
\]

Therefore
\[
\boxed{
S_{\rm BG}
\ll
p^{15/16+o(1)}.
}
\]

The trivial bilinear scale is
\[
N_1N_2=p.
\]

Thus the explicit saving is
\[
\boxed{p^{-1/16}.}
\]

Classification:
\`BG_SQRT_SQRT_INVERSE_PRODUCT_P1_16_SAVING\`.

## 3. Compare with the actual j=2 residual

The current branchwise amplitude target is
\[
H^{6+\varepsilon}
\]
from a standard-DLS bound
\[
H^{6+1/8+\varepsilon}.
\]

Hence the missing saving is
\[
H^{-1/8}.
\]

Since
\[
p=H^3,
\]
this equals
\[
\boxed{
H^{-1/8}
=
p^{-1/24}.
}
\]

But Bourgain--Garaev supplies
\[
p^{-1/16}.
\]

Therefore
\[
\frac{p^{-1/16}}{p^{-1/24}}
=
\boxed{
p^{-1/48}
=
H^{-1/16}.
}
\]

So the theorem is quantitatively stronger than the missing j=2 saving.

## 4. Overhead budget

Suppose an exact transformation of the hard branch to the Bourgain--Garaev kernel incurs an amplitude overhead
\[
H^\eta.
\]

Then the route still closes provided
\[
H^\eta H^{-3/16}
\le
H^{-1/8},
\]
i.e.
\[
\boxed{
\eta\le\frac1{16}.
}
\]

Thus the normal-form problem has a precise budget:

\[
\boxed{
\text{all transformation / coefficient-handling losses must total at most }H^{1/16+o(1)}.
}
\]

This is significantly more informative than the previous statement that an unspecified power saving is needed.

Classification:
\`BG_NORMAL_FORM_OVERHEAD_BUDGET_H1_16\`.

## 5. Where the inverse-product kernel arises

In the determinant congruence
\[
ap-bp'=h,
\]
let
\[
p'=e k.
\]

Reducing modulo the opposite prime p gives
\[
b e k\equiv-h\pmod p.
\]

Equivalently
\[
\boxed{
b\equiv-h\,\bar e\,\bar k\pmod p.
}
\]

Thus any additive Fourier resolution of the b-variable produces exactly
\[
e_p(c\,\bar e\,\bar k).
\]

This is the Bourgain--Garaev kernel, with
\[
e,k\asymp\sqrt p.
\]

Therefore the functional-class match is exact, not heuristic.

## 6. The remaining legality obstruction

The b-variable carries the inherited outer Möbius/divisor coefficient.

It is not a smooth amplitude.

A smooth b-weight would have Fourier support of length
\[
p/D=H,
\]
but an arbitrary Möbius-weighted interval has a full additive Fourier spectrum modulo p.

Using only Parseval,
\[
\sum_{c\bmod p}
|\widehat\alpha(c)|^2
=
p\sum_{b\asymp D}|\alpha_b|^2
\asymp pD.
\]

A generic Cauchy treatment of the full Fourier spectrum costs far more than the available
\[
H^{1/16}
\]
overhead budget.

Hence the existing illegal step
“treat the Möbius b-variable as smooth and Poisson-localized”
cannot be repaired by a generic Fourier inequality.

Permanent guard:
\`BG_GAIN_SUFFICIENT_BUT_OUTER_MOBIUS_FOURIER_OVERHEAD_TOO_LARGE\`.

## 7. What is now needed

No stronger inverse-product theorem is presently required.

The exact missing lemma is a coefficient-transfer statement of the following kind:

> Transform the outer Möbius/divisor-weighted determinant variable into the inverse-product kernel with total loss at most \(H^{1/16+o(1)}\).

Possible mechanisms:
1. exploit multiplicativity of the outer coefficient before additive Fourier expansion;
2. use a Möbius-weighted incomplete Kloosterman estimate;
3. split the outer factorability strata so only the atomic prime-like portion needs special treatment;
4. preserve both outer coefficients in a dispersion norm and apply Bourgain--Garaev only after Cauchy has produced an \(L^2\), not \(L^1\), Fourier cost.

## 8. Current verdict

The two-factor core is no longer blocked by the strength of known inverse-product exponential-sum estimates.

It is blocked by the transfer
\[
\boxed{
\text{outer Möbius determinant coefficient}
\longrightarrow
\text{theorem-ready inverse-product kernel}
}
\]
within an H^(1/16) overhead budget.

This is the smallest current j=2 analytic target.

Permanent priority:
\`J2_OUTER_MOBIUS_TO_BG_KERNEL_TRANSFER\`.

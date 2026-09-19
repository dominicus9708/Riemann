# j=2 two-factor boundary: inverse congruence and exact four-factor character frontier — 2026-09-20

## Status
- Riemann hypothesis: OPEN.
- Hard variance core:
  \[
  b\,e\,k\equiv-h\pmod p,
  \]
  with
  \[
  p\asymp H^3,\quad
  b\asymp H^2=p^{2/3},\quad
  e,k\asymp H^{3/2}=p^{1/2},\quad
  0<|h|\lesssim H=p^{1/3}.
  \]
- New exact transformation: because h,b,e,k are nonzero modulo p, invert the congruence before applying additive or multiplicative orthogonality.
- This preserves the outer Möbius coefficient and avoids the illegal step of Fourier-transforming it as if it were smooth.
- Final exact character form has lengths
  \[
  p^{2/3},p^{1/2},p^{1/2},p^{1/3}
  \]
  and still misses the centered target by exactly \(p^{1/3}=H\) under generic multiplicative-energy estimates.
- Classification: J2_INVERSE_CONGRUENCE_FOUR_FACTOR_CHARACTER_FRONTIER.

## 1. Invert the determinant congruence

For the nonzero determinant shell,
\[
0<|h|\lesssim H\ll p.
\]

The two-factor boundary gives
\[
p'=e k,
\]
and the determinant equation modulo p is
\[
b e k\equiv-h\pmod p.
\]

All four entries are invertible modulo p.

Therefore this is equivalent to
\[
\boxed{
\bar b\,\bar e\,\bar k
\equiv
-\bar h
\pmod p.
}
\]

This elementary inversion is crucial.

The outer coefficient \(\alpha_b\), including its Möbius sign, remains attached directly to b.

Permanent rule:
INVERT_CONGRUENCE_BEFORE_TRANSFORMING_OUTER_MOBIUS.

## 2. Additive-orthogonality form

Let
\[
R_p(h)
=
\sum_{b,e,k}
\alpha_b\beta_e\gamma_k
\mathbf1_{\bar b\bar e\bar k\equiv-\bar h\pmod p}.
\]

Then
\[
R_p(h)
=
\frac1p
\sum_{c\bmod p}
e_p(c\bar h)
T_p(c),
\]
where
\[
\boxed{
T_p(c)
=
\sum_{b,e,k}
\alpha_b\beta_e\gamma_k
e_p(c\bar b\bar e\bar k).
}
\]

The zero frequency is the local density term.

Hence the centered part is
\[
R_p(h)-\mathfrak M_p
=
\frac1p
\sum_{c\ne0}
e_p(c\bar h)T_p(c).
\]

This is a genuine weighted trilinear reciprocal-product sum; no coefficient has been smoothed artificially.

## 3. Existing weighted trilinear benchmark

Petridis--Shparlinski prove weighted trilinear finite-field bounds.

In the range \(XY\gg p\), their comparison form is
\[
\ll
p^{1/4}X^{3/4}Y^{3/4}Z^{7/8}.
\]

For
\[
X=p^{2/3},\qquad
Y=Z=p^{1/2},
\]
this gives
\[
\boxed{
|T_p(c)|
\ll
p^{25/16+o(1)}.
}
\]

This is nontrivial relative to the raw
\[
XYZ=p^{5/3}.
\]

But summing the full additive frequency range pointwise does not approach the centered target.

Thus:
\[
\boxed{
\text{outer-Mobius legality is fixed,
but pointwise trilinear control is not centered-frequency control.}
}
\]

Classification:
WEIGHTED_TRILINEAR_RECIPROCAL_POINTWISE_NOT_CENTERED_CLOSURE.

## 4. Shift aggregate

Let \(\eta_h\) be the normalized smooth shift weight on
\[
0<|h|\lesssim p^{1/3}.
\]

Define
\[
\mathcal A_p
=
\sum_h\eta_h
\left(R_p(h)-\mathfrak M_p\right).
\]

Then
\[
\mathcal A_p
=
\frac1p
\sum_{c\ne0}
T_p(c)
S_p(c),
\]
where
\[
S_p(c)
=
\sum_h\eta_h e_p(c\bar h).
\]

Parseval gives exactly
\[
\sum_{c\bmod p}|S_p(c)|^2
=
p\sum_h|\eta_h|^2
\asymp
\boxed{p^{4/3}}.
\]

This alone does not give the required saving.

## 5. Multiplicative-character form

The original congruence is multiplicative, so a cleaner expression is obtained by character orthogonality.

Define
\[
B(\chi)=\sum_{b\asymp p^{2/3}}\alpha_b\chi(b),
\]
\[
E(\chi)=\sum_{e\asymp p^{1/2}}\beta_e\chi(e),
\]
\[
K(\chi)=\sum_{k\asymp p^{1/2}}\gamma_k\chi(k),
\]
and
\[
H(\chi)=\sum_{0<|h|\lesssim p^{1/3}}\eta_h\chi(h).
\]

After removing the principal-character local density,
\[
\boxed{
\mathcal A_p
=
\frac1{p-1}
\sum_{\chi\ne\chi_0}
B(\chi)E(\chi)K(\chi)\overline{H(\chi)}
}
\]
up to harmless sign/conjugation conventions.

This formula preserves:
- the outer arithmetic coefficient;
- the distinguished large-factor coefficient;
- the two-small-factor product coefficient;
- the full short-shift average.

## 6. Natural pairing reproduces the exact H deficit

Pair
\[
B(\chi)H(\chi)
\qquad\text{and}\qquad
E(\chi)K(\chi).
\]

The product lengths are
\[
p^{2/3}p^{1/3}=p,
\]
and
\[
p^{1/2}p^{1/2}=p.
\]

Character orthogonality converts
\[
\sum_\chi|BH|^2
\]
into the multiplicative energy of products \(bh\), and similarly
\[
\sum_\chi|EK|^2
\]
into the energy of products \(ek\).

At these exact total lengths the generic energies are diagonal/random scale:
\[
\sum_\chi|BH|^2
\ll
p^{2+o(1)},
\]
\[
\sum_\chi|EK|^2
\ll
p^{2+o(1)}.
\]

Cauchy therefore gives
\[
|\mathcal A_p|
\ll
p^{-1}\cdot p\cdot p
=
\boxed{p^{1+o(1)}}.
\]

## 7. Required centered scale

For one fixed prime modulus, the raw number of triples per shift has density
\[
\frac{
p^{2/3}p^{1/2}p^{1/2}
}{p}
=
p^{2/3}.
\]

The project normalization requires the centered aggregate over the \(p^{1/3}\)-length shift family to remain at essentially this scale:
\[
\boxed{
\mathcal A_p
\ll
p^{2/3+o(1)}.
}
\]

Thus the generic character-energy architecture misses by
\[
\boxed{
p^{1/3}=H.
}
\]

This exactly reproduces the original determinant variance deficit.

Classification:
FOUR_FACTOR_CHARACTER_FORM_REPRODUCES_EXACT_H_DEFICIT.

## 8. Banks--Shparlinski incidence check

For one outer interval of length
\[
B=p^{2/3}
\]
and an arbitrary set of size
\[
M=p^{1/2},
\]
Banks--Shparlinski give
\[
J(B,\mathcal M)
\ll
B^2M^2/p+BM\,p^{o(1)}
\asymp
p^{4/3+o(1)}.
\]

If one uses this after Cauchy in the remaining \(p^{1/2}\) variable, the resulting scale is
\[
p^{1/4}J(B,\mathcal M)^{1/2}
=
\boxed{p^{11/12+o(1)}}.
\]

This is not enough to reach \(p^{2/3}\).

Thus the interval/arbitrary-set incidence theorem confirms that the problem cannot be solved by severing one of the two square-root factors before exploiting their joint structure.

Classification:
BANKS_SHPARLINSKI_ONE_FACTOR_CAUCHY_NOT_CLOSURE.

## 9. Consequence for Bourgain--Garaev

The bilinear inverse-product saving \(p^{-1/16}\) acts naturally on the \(e,k\) pair.

But the exact character formulation shows that the full centered problem also contains the \(BH\) pair and requires an overall extra \(p^{-1/3}\).

Therefore a standalone \(e,k\) theorem cannot be credited with closure unless it is embedded in an estimate coupling it to the \(b,h\) side.

This is the corrected role of Bourgain--Garaev.

Permanent guard:
BILINEAR_EK_SAVING_MUST_COUPLE_TO_BH_SIDE.

## 10. Exact current theorem target

A sufficient theorem is the coefficient-sensitive four-factor estimate
\[
\boxed{
\sum_{\chi\ne\chi_0}
B(\chi)E(\chi)K(\chi)\overline{H(\chi)}
\ll
p^{5/3+o(1)}.
}
\]

Indeed division by \(p-1\) gives
\[
\mathcal A_p\ll p^{2/3+o(1)}.
\]

Generic energy gives only
\[
p^{2+o(1)}.
\]

Thus the exact missing character-sum saving is
\[
\boxed{p^{-1/3}=H^{-1}.}
\]

The weights are highly non-generic:
- B inherits Mobius/divisor structure;
- E is von-Mangoldt/prime-like;
- K is the two-small-prime product boundary coefficient;
- H is a smooth short-shift interval.

The next analytic search should target this exact structured four-factor moment rather than another generic reciprocal exponential-sum theorem.

Permanent priority:
J2_STRUCTURED_FOUR_FACTOR_CHARACTER_MOMENT.

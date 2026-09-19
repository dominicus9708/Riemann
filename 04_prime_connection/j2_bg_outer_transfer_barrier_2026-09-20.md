# j=2 outer-coefficient transfer barrier for the Bourgain--Garaev kernel — 2026-09-20

## Status
- Riemann hypothesis: OPEN.
- Context: Bourgain--Garaev gives enough explicit saving on the critical inverse-product kernel \(e_p(c\bar e\bar k)\).
- New exact obstruction: generic transfer of the outer arithmetic coefficient into that kernel has a \(p^{1/6}\) fixed-modulus deficit, far larger than the available \(p^{1/48}\) spare margin.
- Therefore Bourgain--Garaev is quantitatively sufficient **only if** one exploits special outer Möbius/divisor structure before generic Fourier/character Cauchy.
- Classification: \`J2_BG_OUTER_TRANSFER_P1_6_BARRIER\`.

## 1. Fixed-modulus congruence model

At the two-factor boundary,
\[
p\asymp H^3,
\]
and
\[
e\asymp k=rs\asymp H^{3/2}=p^{1/2}.
\]

The outer determinant variable has length
\[
B:=H^2=p^{2/3}.
\]

Reducing
\[
ap-bek=h
\]
modulo p gives
\[
\boxed{
bek\equiv-h\pmod p.
}
\]

Ignore for the moment the second outer coefficient on a and ask only for a generic bound for
\[
\mathcal C_p(c)
=
\sum_{b\asymp B}
\alpha_b
\sum_{e\asymp p^{1/2}}
\beta_e
\sum_{k\asymp p^{1/2}}
\gamma_k
\mathbf1_{bek\equiv c\pmod p}.
\]

All coefficients are divisor-bounded.

The random-density size is
\[
\frac{BEK}{p}
=
\frac{p^{2/3}p^{1/2}p^{1/2}}p
=
\boxed{p^{2/3}}.
\]

## 2. Multiplicative-character diagonalization

Character orthogonality gives
\[
\mathcal C_p(c)
=
\frac1{p-1}
\sum_{\chi\bmod p}
\overline{\chi(c)}
B(\chi)E(\chi)K(\chi),
\]
where
\[
B(\chi)=\sum_{b\asymp B}\alpha_b\chi(b)
\]
and similarly for E,K.

The exact second moments are
\[
\sum_\chi |B(\chi)|^2
\ll
pB\,p^\varepsilon
=
p^{5/3+\varepsilon},
\]
\[
\sum_\chi |E(\chi)|^2
\ll
pE\,p^\varepsilon
=
p^{3/2+\varepsilon},
\]
and similarly for K.

## 3. Optimal elementary Hölder scale

Using L2 for B and fourth moments for E,K,
\[
|\mathcal C_p(c)|
\le
\frac1p
\|B\|_2
\|E\|_4
\|K\|_4.
\]

For \(E=K=p^{1/2}\), multiplicative product energy is diagonal-scale up to \(p^\varepsilon\), hence
\[
\sum_\chi |E(\chi)|^4
\ll
p^{2+\varepsilon},
\]
and the same for K.

Therefore
\[
|\mathcal C_p(c)|
\ll
p^{-1}
p^{5/6}
p^{1/2}
p^{1/2}
p^\varepsilon
=
\boxed{
p^{5/6+\varepsilon}.
}
\]

Other elementary Hölder allocations do not improve this random-character scale.

## 4. Exact deficit

The desired fixed-modulus density scale is
\[
p^{2/3}.
\]

Thus the generic character architecture loses
\[
\boxed{
p^{5/6-2/3}
=
p^{1/6}.
}
\]

Since
\[
p=H^3,
\]
this is
\[
\boxed{H^{1/2}.}
\]

Classification:
\`OUTER_GENERIC_CHARACTER_TRANSFER_H1_2_LOSS\`.

## 5. Compare with the Bourgain--Garaev margin

The inverse-product theorem gives
\[
p^{-1/16}
\]
while the amplitude branch needs
\[
p^{-1/24}.
\]

The spare margin is only
\[
p^{-1/48}.
\]

But the generic outer transfer costs
\[
p^{1/6}.
\]

Therefore
\[
\frac16\gg\frac1{48}.
\]

So:
\[
\boxed{
\text{BG saving}
+
\text{generic outer Fourier/character transfer}
}
\]
cannot close the hard core.

Permanent guard:
\`BG_MARGIN_CANNOT_PAY_GENERIC_OUTER_TRANSFER\`.

## 6. Additive-Fourier version gives the same message

Solving the congruence for b gives
\[
b\equiv c\,\bar e\,\bar k\pmod p.
\]

Expand the outer coefficient:
\[
\alpha_b\mathbf1_{b\asymp B}
=
\frac1p
\sum_{t\bmod p}
\widehat\alpha(t)e_p(tb).
\]

Then
\[
\mathcal C_p(c)
=
\frac1p
\sum_t
\widehat\alpha(t)
\sum_{e,k}
\beta_e\gamma_k
e_p(tc\bar e\bar k).
\]

Bourgain--Garaev controls each nonzero inner frequency.

However Parseval gives only
\[
\sum_t|\widehat\alpha(t)|^2
\asymp pB,
\]
while the inverse-product family itself has total L2 energy of the generic multiplicative-energy scale.

Cauchy therefore reproduces the same \(p^{5/6}\)-type barrier rather than the \(p^{2/3}\) target.

Thus the obstruction is not an artefact of choosing multiplicative rather than additive Fourier coordinates.

## 7. Möbius-specific reciprocal estimates

Korolev proves, for prime modulus p and
\[
x\ge p^{1/2+\varepsilon},
\]
a power-saving estimate
\[
\sum_{n\le x}\mu(n)e_p(a\bar n+bn)
\ll_\varepsilon
x p^{-c\varepsilon^4}
\]
for an absolute \(c>0\).

Our outer length
\[
B=p^{2/3}
\]
lies in this range with \(\varepsilon=1/6\).

This confirms that the Möbius coefficient is analytically stronger than a generic bounded sequence in reciprocal phases.

However the available theorem supplies an unspecified small exponent
\[
c/1296
\]
and does not by itself verify the much larger \(p^{-1/6}\) transfer gain required by the generic fixed-modulus congruence model.

Classification:
\`MOBIUS_RECIPROCAL_POWER_SAVING_EXISTS_BUT_NOT_NUMERIC_CLOSURE\`.

## 8. Consequence

The exact remaining analytic problem is now:

\[
\boxed{
\text{combine outer Möbius reciprocal cancellation
with the }p^{-1/16}\text{ critical inverse-product bilinear saving
without paying the }p^{1/6}\text{ generic transfer loss}.
}
\]

This requires a **coupled** estimate.

Applying the two theorems sequentially after separate Cauchy steps is not enough.

Candidate forms:
- a trilinear reciprocal estimate with one Möbius variable of length \(p^{2/3}\) and two arbitrary variables of length \(p^{1/2}\);
- a dispersion theorem retaining both outer variables;
- a Bourgain--Garaev argument modified to include a multiplicative Möbius weight on the inverse image.

Permanent priority:
\`J2_MOBIUS_TIMES_INVERSE_PRODUCT_COUPLED_ESTIMATE\`.


## 9. Correction after amplitude/variance normalization audit

The comparison in Sections 5 and 8 used an obsolete interpretation in which the Bourgain--Garaev \(p^{-1/16}\) saving was credited directly against the amplitude-side \(H^{-1/8}\) deficit.

The inverse-product congruence lives on the variance/dispersion side.

The correct refined variance deficit corresponding to the amplitude factor \(H^{1/8}\) is
\[
H^{1/4}=p^{1/12}.
\]

Thus even before paying any outer-coefficient transfer cost, the BG saving leaves
\[
p^{1/12}p^{-1/16}
=
\boxed{p^{1/48}=H^{1/16}}.
\]

Accordingly:
- there is no spare \(p^{-1/48}\) margin;
- instead there is an additional \(p^{-1/48}\) saving still required;
- the generic outer character/Fourier transfer cost \(p^{1/6}\) remains far too large and therefore the barrier conclusion of this file becomes even stronger.

Replace the old phrase “BG margin cannot pay generic outer transfer” by the sharper statement:

\[
\boxed{
\text{BG itself does not fully close the refined variance residual,
and generic outer transfer worsens the gap by }p^{1/6}.
}
\]

Updated classification:
BG_LEAVES_P1_48_BEFORE_OUTER_TRANSFER.

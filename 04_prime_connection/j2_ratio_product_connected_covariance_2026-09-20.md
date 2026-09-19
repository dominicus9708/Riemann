# j=2 exact ratio-product connected covariance reduction — 2026-09-20

## Status
- Riemann hypothesis: OPEN.
- This note starts from the corrected canonical frontier
  \[
  b e r s\equiv -h\pmod P,
  \]
  with
  \[
  b\asymp P^{2/3},\qquad
  e\asymp P^{1/2},\qquad
  r,s\asymp P^{1/4},\qquad
  h\asymp P^{1/3}.
  \]
- No Cauchy regrouping is reinterpreted as a new character identity.
- New result: the five-factor character target is exactly a centered covariance between
  1. the prime-times-two-prime product distribution \(ers\pmod P\), and
  2. the short-ratio distribution \(-h/b\pmod P\).
- Classification: J2_RATIO_PRODUCT_CONNECTED_COVARIANCE_REDUCTION.
- This is an exact reduction, not a closure of the j=2 hard core.

## 1. Multiplicative-group notation

Let
\[
G=\mathbb F_P^\times,
\qquad |G|=P-1.
\]

For functions on \(G\), use the unnormalised multiplicative convolution
\[
(f*g)(x)
=
\sum_{y\in G} f(y)g(xy^{-1}).
\]

Write
\[
f^\circ
=
f-\frac1{|G|}\sum_{x\in G}f(x)
\]
for the mean-zero projection.

A direct calculation gives
\[
\boxed{
(f*g)^\circ=f^\circ*g^\circ.
}
\]

Thus lower-order uniform components disappear exactly after centering.

## 2. Product and ratio residue distributions

Let \(E,R,S\) denote the residue weight functions carried by the
\[
e\asymp P^{1/2},\qquad
r,s\asymp P^{1/4}
\]
prime variables.

Define
\[
A=E*R*S.
\]

Then
\[
A(x)
=
\sum_{ers\equiv x\,(P)}
\beta_e\rho_r\sigma_s.
\]

For the outer coefficient, let \(B\) denote the residue function carried by
\[
b\asymp P^{2/3},
\]
and define the inverse-reflection
\[
\widetilde B(x)
=
\overline{B(x^{-1})}.
\]

Let \(H_-\) be the short-shift residue function with the fixed minus sign absorbed:
\[
H_-(x)=H(-x).
\]

Define
\[
C=H_-*\widetilde B.
\]

Then
\[
C(x)
=
\sum_{-h\bar b\equiv x\,(P)}
\eta_h\overline{\alpha_b}.
\]

Hence \(C\) is exactly the weighted ratio distribution
\[
x\equiv-\frac{h}{b}\pmod P.
\]

## 3. Exact Fourier identity

For a multiplicative character \(\chi\),
\[
\widehat A(\chi)
=
E(\chi)R(\chi)S(\chi),
\]
while
\[
\widehat C(\chi)
=
H_-(\chi)\overline{B(\chi)}.
\]

Therefore, after the harmless fixed sign convention in \(H_-\),
\[
\widehat A(\chi)\overline{\widehat C(\chi)}
=
B(\chi)E(\chi)R(\chi)S(\chi)\overline{H(\chi)}.
\]

Multiplicative Parseval gives the exact orientation-safe identity
\[
\boxed{
\sum_{\chi\ne\chi_0}
B(\chi)E(\chi)R(\chi)S(\chi)\overline{H(\chi)}
=
(P-1)
\sum_{x\in G}
A^\circ(x)\overline{C^\circ(x)}.
}
\]

Thus the current target
\[
\sum_{\chi\ne\chi_0}
BERS\overline H
\ll P^{5/3+o(1)}
\]
is equivalent to
\[
\boxed{
\left|
\sum_{x\in G}
A^\circ(x)\overline{C^\circ(x)}
\right|
\ll
P^{2/3+o(1)}.
}
\]

Permanent rule:
J2_CHARACTER_TARGET_EQUALS_RATIO_PRODUCT_CONNECTED_COVARIANCE.

## 4. All lower-order marginals vanish algebraically

Because centering commutes with multiplicative convolution,
\[
\boxed{
A^\circ
=
E^\circ*R^\circ*S^\circ,
}
\]
and
\[
\boxed{
C^\circ
=
H_-^\circ*\widetilde B^\circ.
}
\]

Therefore the corrected j=2 hard core is already fully connected on the multiplicative group.

There is no surviving one-body term that can be closed independently and then counted as the missing \(P^{-1/3}\) saving.

This explains algebraically why sharper one-factor marginals and separate self-moments do not close the current frontier.

Permanent rule:
J2_NONPRINCIPAL_FIVE_FACTOR_MOMENT_IS_3V2_CONNECTED_CONVOLUTION.

## 5. Natural self-energy scales

The \(ers\) tuple count is
\[
P^{1/2+1/4+1/4+o(1)}
=
P^{1+o(1)}.
\]

Moreover, if
\[
ers\equiv e'r's'\pmod P,
\]
both integer products lie in fixed dyadic multiples of \(P\), so
\[
ers-e'r's'=mP
\]
with \(|m|=O(1)\).

For each fixed triple and bounded \(m\), the shifted integer has only \(P^{o(1)}\) admissible factorizations. Hence the multiplicative energy is at the natural scale
\[
\boxed{
\|A^\circ\|_2^2
\ll
P^{1+o(1)}.
}
\]

On the ratio side,
\[
h\bar b\equiv h'\bar b'\pmod P
\]
is equivalent to
\[
hb'-h'b=mP,
\qquad |m|=O(1),
\]
because \(h,b'\) and \(h',b\) are both of scale \(P\).

The determinant count, together with divisor-bounded outer coefficients, gives the same natural scale
\[
\boxed{
\|C^\circ\|_2^2
\ll
P^{1+o(1)}.
}
\]

This is consistent with the previously closed centered ratio-multiplicity \(L^2\) calculation.

Cauchy therefore gives only
\[
|\langle A^\circ,C^\circ\rangle|
\ll
P^{1+o(1)},
\]
equivalently the old character numerator bound \(P^{2+o(1)}\).

## 6. Exact missing statement as a coherence bound

The target covariance is
\[
P^{2/3+o(1)}.
\]

Since both natural \(L^2\) norms are \(P^{1/2+o(1)}\), a sufficient normalized form is
\[
\boxed{
\frac{
|\langle A^\circ,C^\circ\rangle|
}{
\|A^\circ\|_2\|C^\circ\|_2
}
\ll
P^{-1/3+o(1)}.
}
\]

Thus the missing \(P^{-1/3}\) is precisely a **cross-distribution coherence saving**, not a self-energy saving.

New minimal target:
J2_RATIO_PRODUCT_COHERENCE_P13_OPEN.

## 7. Quotient/Farey form remains valid

The support intersection
\[
ers\equiv-h\bar b\pmod P
\]
is exactly
\[
bers+h=\ell P.
\]

With
\[
n=ers\asymp P
\]
this becomes
\[
\boxed{
bn-\ell P=-h,
}
\]
up to the fixed sign convention.

At the hard scales,
\[
b,\ell\asymp P^{2/3},
\qquad
|h|\lesssim P^{1/3},
\]
so
\[
\left|
\frac nP-\frac\ell b
\right|
\lesssim
P^{-4/3}
\asymp
b^{-2}.
\]

Thus the ratio-product covariance lives exactly at Farey-critical resolution, but ordinary Farey spacing supplies no free polynomial saving.

## 8. Additive-frequency form and short-shift corridor

Additive orthogonality applied directly to
\[
bers+h\equiv0\pmod P
\]
gives, after subtracting the local density,
\[
\mathcal C_P
=
\frac1P
\sum_{c\ne0}
\widehat\eta(c)
T(c)
+
O(P^{o(1)}),
\]
where
\[
T(c)
=
\sum_{b,e,r,s}
\alpha_b\beta_e\rho_r\sigma_s
e_P(cbers).
\]

The \(O(P^{o(1)})\) term only records the harmless difference between additive zero-frequency density \(1/P\) and multiplicative principal density \(1/(P-1)\).

For a smooth shift weight of length
\[
H=P^{1/3},
\]
one has rapid Fourier decay
\[
|\widehat\eta(c)|
\ll_A
H\left(1+\frac{|c|H}{P}\right)^{-A}.
\]

Hence only the corridor
\[
\boxed{
|c|\lesssim P/H=P^{2/3+o(1)}
}
\]
is relevant up to arbitrary power saving.

This frequency truncation alone is not closure: Parseval still carries the same short-shift energy and an additional mixed estimate is required.

Permanent rule:
SHORT_SHIFT_FOURIER_CORRIDOR_NOT_CLOSURE.

## 9. Literature comparison

Targeted comparison with existing finite-field results gives useful controls but no black-box closure of the present covariance:

- Shparlinski, *Multiple Exponential and Character Sums with Monomials* (2013): multilinear monomial exponential/character sums, including ranges below the individual Burgess barrier in several variables. The main all-prime bounds concern cubes or generic bounded weights and do not directly give the present anisotropic prime/semiprime/Möbius centered covariance.
- Cilleruelo--Garaev, *Congruences involving product of intervals and sets with small multiplicative doubling modulo a prime and applications* (2014): strong unsigned incidence bounds for interval/product-set congruences, but not the required signed connected covariance with prime convolution weights.
- Petridis--Shparlinski trilinear/quadrilinear finite-field bounds remain relevant pointwise controls, but previous parameter audits already show that pointwise trilinear saving is not the same as centered five-factor closure.
- Alsetri--Shao (2025) gives Burgess-type estimates for rank-2 generalized arithmetic progressions; the support geometry is different from the present prime-times-semiprime versus short-ratio covariance.

No novelty claim is made from this targeted search.

## 10. Next calculation

Do not return to the invalid \(bh-ers=mP\) wrap-shell.

The next calculation should work with the exact operator
\[
\boxed{
\langle
E^\circ*R^\circ*S^\circ,
H_-^\circ*\widetilde B^\circ
\rangle
}
\]
and test estimates that keep at least one factor from each side coupled before absolute values.

Priority:
1. split the connected covariance by the distinguished prime \(e\) without destroying the \(R*S\) interaction;
2. compute the exact second moment of the resulting ratio-semiprime correlation over \(e\);
3. compare that second moment with the \(P^{1/3}\) coherence deficit;
4. terminate any route that reduces to separate \(L^2\) norms or generic Hölder.

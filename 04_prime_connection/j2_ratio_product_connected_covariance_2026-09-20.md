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


## 11. Distinguished-prime Cauchy audit

Let
\[
Q=R^\circ*S^\circ,
\qquad
C=H_-^\circ*\widetilde B^\circ.
\]

Then
\[
A^\circ=E^\circ*Q
\]
and
\[
\langle A^\circ,C\rangle
=
\sum_{e\in G}E^\circ(e)D(e),
\]
where
\[
D(e)
=
\sum_{x\in G}
Q(xe^{-1})\overline{C(x)}.
\]

Because \(Q\) is mean-zero,
\[
\sum_{e\in G}D(e)=0.
\]
Hence the uniform part of \(E^\circ\) disappears exactly, and one may write the same first moment using the actual distinguished-prime weight.

For a prime/von-Mangoldt block of length
\[
P^{1/2},
\]
one has
\[
\sum_e|E(e)|^2
\ll
P^{1/2+o(1)}.
\]

Therefore Cauchy would close the covariance target only if
\[
\boxed{
\sum_{e\asymp P^{1/2}\atop e\ {m prime}}
|D(e)|^2
\ll
P^{5/6+o(1)}.
}
\]

This is substantially stronger than a generic localized-energy statement.

Indeed,
\[
\|Q\|_2^2\asymp P^{1/2+o(1)},
\qquad
\|C\|_2^2\asymp P^{1+o(1)}.
\]

A random-shift model therefore predicts
\[
|D(e)|^2
\asymp
\frac{\|Q\|_2^2\|C\|_2^2}{P}
\asymp
P^{1/2+o(1)}.
\]

Across \(P^{1/2+o(1)}\) prime locations this gives natural energy
\[
P^{1+o(1)},
\]
whereas Cauchy closure asks for
\[
P^{5/6+o(1)}.
\]

Thus a distinguished-prime second-moment route requires an additional non-generic depletion
\[
\boxed{P^{-1/6}}
\]
relative even to the random localized-energy scale.

Conclusion:
generic second-moment/Cauchy on the distinguished prime is too strong as the next target unless one proves a special anticorrelation between prime support and the ratio-semiprime correlation.

Classification:
J2_DISTINGUISHED_PRIME_GENERIC_SECOND_MOMENT_OVERSTRONG.

Permanent guard:
DO_NOT_SQUARE_DISTINGUISHED_PRIME_BEFORE_USING_ITS_ARITHMETIC_STRUCTURE.

## 12. Exact near-multiple restricted-convolution representation

The congruence
\[
bers\equiv-h\pmod P
\]
is equivalent, on the hard ranges, to the integer equation
\[
\boxed{
bers+h=\ell P
}
\]
with
\[
\ell\asymp P^{2/3}.
\]

Define the restricted four-factor Dirichlet-convolution coefficient
\[
a(N)
=
\sum_{\substack{
bers=N\\
b\asymp P^{2/3},\ e\asymp P^{1/2}\\
r,s\asymp P^{1/4}
}}
\alpha_b\beta_e\rho_r\sigma_s.
\]

Then the non-main arithmetic count is exactly a short-residue-window sample
\[
\boxed{
\sum_{\ell\asymp P^{2/3}}
\sum_{|h|\lesssim P^{1/3}}
\eta_h\,
a(\ell P-h),
}
\]
with the appropriate local-density subtraction.

This formulation changes no character orientation and does not use the withdrawn
\[
bh-ers=mP
\]
shell.

It converts the modular problem into the distribution of a restricted factorable convolution along integers immediately adjacent to multiples of \(P\).

## 13. Scale map to divisor-in-arithmetic-progression theory

Set
\[
X=P^{5/3}.
\]

Then
\[
P=X^{3/5},
\qquad
b\asymp X^{2/5},
\qquad
e\asymp X^{3/10},
\qquad
r,s\asymp X^{3/20},
\]
and
\[
\ell\asymp X^{2/5},
\qquad
h\asymp X^{1/5}.
\]

Thus the current exact hard core is a prime-modulus arithmetic-progression problem at exponent
\[
\boxed{3/5}
\]
for a highly factorable, restricted four-fold coefficient, averaged over a consecutive residue window of length
\[
X^{1/5}.
\]

A useful two-product grouping is
\[
u=br\asymp X^{11/20},
\qquad
v=es\asymp X^{9/20},
\qquad
uv\asymp X.
\]

This is only \(1/20\) away from exact square-root balance on each side.

### Literature comparison

- The classical binary divisor problem admits uniform prime-modulus distribution substantially into the range below \(X^{2/3}\), so the modulus exponent \(3/5\) is not intrinsically beyond binary-divisor geometry.
- For pointwise/uniform ternary-divisor distribution, Fouvry--Kowalski--Michel prove exponent \(1/2+1/46\), and Sharma improves this to \(1/2+1/30\), both below \(3/5\). A 2026 result of Aydemir--Boran reaches \(8/11\) **after averaging over reduced residue classes modulo a prime**. That averaging regime is different from the present consecutive window of length \(X^{1/5}\), so it is not used as a black-box closure.
- General \(d_k\), \(k\ge4\), results beyond square-root often use smooth/factorable moduli or averaging over moduli. They do not directly apply to the present single prime modulus \(P\).
- Therefore treating the coefficient merely as a generic ternary/quaternary divisor function loses too much structure.
- The potentially useful feature is instead the near-balanced binary grouping
  \[
  X^{11/20}\times X^{9/20}
  \]
  together with the original prime/Möbius factorization retained inside each side and the short residue-window average.

No closure is claimed.

New priority:
J2_NEAR_MULTIPLE_RESTRICTED_CONVOLUTION_AP_ROUTE.

The next theorem search should ask for a coefficient-sensitive binary/Type-II distribution estimate at modulus \(X^{3/5}\) that also gains from the \(X^{1/5}\)-long consecutive residue window, rather than applying generic \(d_3\) or \(d_4\) distribution black boxes.


## 14. Smooth binary comparison model: exact dual Kloosterman scale

This section is a **comparison model**, not yet a legal transformation of the actual arithmetic weights.

Group
\[
u=br,
\qquad
v=es.
\]

Then
\[
U\asymp P^{11/12},
\qquad
V\asymp P^{3/4},
\qquad
UV\asymp P^{5/3}=X.
\]

Temporarily replace the arithmetic convolution coefficients on \(u,v\) by smooth dyadic weights.

For
\[
uv\equiv-h\pmod P,
\]
two-dimensional Poisson summation separates the zero frequency from a nonzero dual Kloosterman core of the schematic form
\[
\frac{UV}{P^2}
\sum_{m,n}
\widehat W_1\!\left(\frac{mU}{P}\right)
\widehat W_2\!\left(\frac{nV}{P}\right)
S(\pm h,mn;P).
\]

Writing the classical Kloosterman sum in normalized form
\[
\mathrm{Kl}_2(a;P)=P^{-1/2}S(a,1;P)
\]
and absorbing harmless inversions/signs, the centered nondegenerate core has prefactor
\[
\boxed{
\frac{UV}{P^{3/2}}
=
P^{1/6}.
}
\]

The dual lengths are
\[
M=\frac PU=P^{1/12},
\qquad
N=\frac PV=P^{1/4}.
\]

The short residue window has length
\[
H=P^{1/3}.
\]

Hence the exact scale coincidence is
\[
\boxed{
MN=P^{1/3}=H.
}
\]

This is the strongest structural feature of the smooth binary comparison model.

Classification:
J2_SMOOTH_BINARY_DUAL_LENGTH_MATCH_MN_EQ_H.

## 15. Exact Kloosterman saving demanded by the comparison model

After summing the centered discrepancy over the short \(h\)-window, the nondegenerate comparison core is
\[
P^{1/6}
\sum_{h\asymp P^{1/3}}
\sum_{m\asymp P^{1/12}}
\sum_{n\asymp P^{1/4}}
\gamma_h\alpha_m\beta_n
\mathrm{Kl}_2(\pm hmn;P),
\]
up to smooth weights and dyadic decomposition.

The desired arithmetic target is
\[
P^{2/3+o(1)}.
\]

Therefore it would suffice to prove
\[
\boxed{
\sum_{h\asymp P^{1/3}}
\sum_{m\asymp P^{1/12}}
\sum_{n\asymp P^{1/4}}
\gamma_h\alpha_m\beta_n
\mathrm{Kl}_2(\pm hmn;P)
\ll
P^{1/2+o(1)}.
}
\]

There are
\[
P^{1/3+1/12+1/4}
=
P^{2/3}
\]
terms.

Thus the exact required saving over bounded normalized Kloosterman sums is
\[
\boxed{P^{-1/6}.}
\]

Equivalently, because
\[
H=P^{1/3},
\]
the comparison model asks for
\[
\boxed{H^{-1/2}}
\]
of cancellation.

Classification:
J2_DUAL_TRILINEAR_KL2_P16_SAVING_TARGET.

## 16. Why a generic bilinear collapse is not presently a black-box closure

If the dual variables \(m,n\) are collapsed to
\[
k=mn\asymp P^{1/3},
\]
the comparison sum becomes bilinear in
\[
h\asymp P^{1/3},
\qquad
k\asymp P^{1/3}.
\]

The Kowalski--Michel--Sawin 2018 generalized-Kloosterman benchmark is nontrivial for two equal lengths from
\[
P^{3/8+\delta}
\]
onward.

Thus the symmetric
\[
P^{1/3}\times P^{1/3}
\]
box lies below that general threshold.

Recent 2026 Blomer--Pascadi bounds improve the critical square-root-length saving, but their abstract-level critical regime is not the present \(P^{1/3}\times P^{1/3}\) box.

Therefore no black-box closure is recorded from these theorems.

This does **not** prove that the target is impossible with known methods. It shows that the internal factorization
\[
P^{1/12}\times P^{1/4}
\]
must be retained until an exact theorem parameter map is established.

Permanent rule:
DO_NOT_COLLAPSE_DUAL_P112_P14_BEFORE_KLOOSTERMAN_AUDIT.

## 17. Consecutive-residue divisor literature is structurally aligned

Kerr--Shparlinski study the binary divisor function averaged over sets of consecutive reduced residue classes and use Voronoi/Kloosterman bilinear methods. Their motivation is precisely to gain from residue-class averaging beyond the individual-residue regime.

This is structurally close to the present
\[
|h|\lesssim X^{1/5}
\]
consecutive residue window.

However the present coefficient is not \(d_2\). It is a restricted signed convolution whose two grouped sides still contain:
- the inherited outer Möbius/divisor coefficient;
- one distinguished prime;
- the two-prime boundary coefficient.

Hence the divisor result is used as a transformation template, not as a theorem already proving the j=2 estimate.

New direct priority:
J2_FACTORABLE_VORONOI_KL2_TRANSFER_OPEN.

The next step is to determine whether the original factorable coefficients can be transferred to the smooth dual Kloosterman model with total loss at most the required
\[
P^{1/6-o(1)}
\]
saving budget, while preserving the \(P^{1/12}\times P^{1/4}\) dual factorization.

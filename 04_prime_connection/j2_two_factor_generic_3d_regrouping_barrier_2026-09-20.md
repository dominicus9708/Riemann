# j=2 two-factor core: generic 3D regrouping barrier — 2026-09-20

## Status
- Riemann hypothesis: OPEN.
- Hard core factor exponents:
  \[
  \left\{
  2,\ 3,\ \frac32,\ \frac34,\ \frac34
  \right\}.
  \]
- Candidate tested: collapse the five arithmetic factors into three product variables in every possible nonempty set partition, then apply the Robert--Sargos generic three-dimensional monomial theorem with every possible choice of distinguished variable.
- Best resulting exponent:
  \[
  \boxed{H^{107/16+\varepsilon}=H^{6+11/16+\varepsilon}.}
  \]
- This is much worse than the current product-DLS bound
  \[
  H^{6+1/8+\varepsilon}.
  \]
- Classification: \`J2_TWO_FACTOR_GENERIC_3D_REGROUPING_BARRIER\`.

## 1. Generic theorem model

For three collapsed product lengths
\[
H^a,\qquad H^b,\qquad H^c,
\qquad
a+b+c=8,
\]
and normalized phase amplitude
\[
X=H^4,
\]
the Robert--Sargos benchmark has the form
\[
H^{8+\varepsilon}
\left[
H^{(4-a-b-2c)/4}
+
H^{-(a+b)/4}
+
H^{-c/2}
+
H^{-2}
\right]
\]
after choosing c as the distinguished variable.

All permutations of a,b,c must be checked.

## 2. Factor list

The two-small-factor boundary layer has atomic H-exponents
\[
\boxed{
2,\ 3,\ \frac32,\ \frac34,\ \frac34.
}
\]

These correspond schematically to:
- outer Möbius factor;
- opposite large prime;
- distinguished Lambda factor in the hard H^3 branch;
- the two small factors r,s with
  \[
  b_H(rs)=-1.
  \]

Every collapsed three-variable model is obtained by partitioning these five atoms into three nonempty groups.

## 3. Best finite regroupings

The optimal scale patterns include, up to permutation,
\[
\left(
\frac34,\frac{11}{4},\frac92
\right),
\]
\[
\left(
\frac32,\frac{11}{4},\frac{15}{4}
\right),
\]
and
\[
\left(
\frac94,\frac{11}{4},3
\right).
\]

For the best distinguished-variable placement, the dominant Robert--Sargos term gives saving exponent
\[
-\frac{21}{16}
\]
relative to the raw H^8 scale.

Hence
\[
8-\frac{21}{16}
=
\boxed{\frac{107}{16}}
=
6+\frac{11}{16}.
\]

## 4. Comparison with current DLS

The current double-refined/product-balance architecture gives
\[
\boxed{
H^{6+1/8+\varepsilon}
=
H^{98/16+\varepsilon}.
}
\]

Thus generic 3D regrouping is worse by
\[
\frac{107-98}{16}
=
\boxed{\frac9{16}}.
\]

Therefore one cannot combine the words
“three-dimensional monomial theorem”
and
“hard two-factor core”
and expect an automatic improvement.

## 5. Consequence

The remaining H^(1/8) problem is genuinely coefficient-sensitive.

Any successful input must use at least one feature absent from the generic Robert--Sargos setup:
- the exact coefficient \(b_H(rs)=-1\);
- signed head-tail recombination;
- prime support;
- a determinant/Kloosterman structure after a legal transform;
- a norm adapted specifically to the two-factor boundary.

Permanent rule:
\`GENERIC_3D_REGROUPING_WORSE_THAN_H1_8_DLS\`.

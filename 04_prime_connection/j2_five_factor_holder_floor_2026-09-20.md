# j=2 corrected five-factor moment and Hölder diagonal-floor barrier — 2026-09-20

## Status
- Riemann hypothesis: OPEN.
- This file supersedes the invalid bounded wrap-shell reduction.
- Exact hard two-small-factor variance core:
  \[
  b e r s\equiv -h\pmod P,
  \]
  with
  \[
  b\asymp P^{2/3},\quad
  e\asymp P^{1/2},\quad
  r,s\asymp P^{1/4},\quad
  h\asymp P^{1/3}.
  \]
- Exact character target:
  \[
  \boxed{
  \sum_{\chi\ne\chi_0}
  B(\chi)E(\chi)R(\chi)S(\chi)\overline{H(\chi)}
  \ll P^{5/3+o(1)}.
  }
  \]
- Generic Cauchy/Hölder remains at \(P^{2+o(1)}\).
- Classification: J2_FIVE_FACTOR_HOLDER_DIAGONAL_FLOOR.

## 1. Exact orientation

Character orthogonality applied to
\[
B E R S\overline H
\]
encodes
\[
b e r s\equiv h\pmod P
\]
up to the fixed sign convention for h.

No regrouping used only inside absolute values may alter this orientation.

Permanent guard:
CAUCHY_GROUPING_IS_NOT_CHARACTER_REORIENTATION.

## 2. Entropy sum

The five support exponents are
\[
\alpha_B=\frac23,\qquad
\alpha_E=\frac12,\qquad
\alpha_R=\alpha_S=\frac14,\qquad
\alpha_H=\frac13.
\]

Their sum is
\[
\boxed{
\sum_i\alpha_i=2.
}
\]

## 3. Diagonal-scale moment model

Suppose a factor or product group of total tuple exponent \(\alpha\) has an ideal diagonal-scale \(q\)-norm over the nonprincipal characters:
\[
\|F\|_q
\ll
P^{1/q+\alpha/2+o(1)}.
\]

This is the strongest scale one expects from a moment estimate whose only surviving contribution is the arithmetic diagonal.

Take any Hölder decomposition with exponents \(q_j\) satisfying
\[
\sum_j\frac1{q_j}=1.
\]

If the corresponding factor/product groups partition the five variables, their tuple exponents satisfy
\[
\sum_j\alpha_j=2.
\]

Multiplying the diagonal-scale moment bounds gives exponent
\[
\sum_j\left(\frac1{q_j}+\frac{\alpha_j}{2}\right)
=
1+\frac12\cdot2
=
\boxed2.
\]

Hence:
\[
\boxed{
\text{diagonal-optimal separate moments still give only }P^{2+o(1)}.
}
\]

## 4. Consequence

The target
\[
P^{5/3+o(1)}
\]
requires
\[
P^{-1/3}
\]
beyond the complete diagonal-moment/Hölder architecture.

Therefore the missing saving cannot come from:
- choosing a different Cauchy pairing;
- proving sharper individual \(L^{2k}\) moments down to their diagonal scale;
- splitting \(K\) into \(R S\) and applying ordinary Hölder;
- treating one factor pointwise and all others by diagonal moments, unless the pointwise theorem itself carries genuinely cross-structural information.

Permanent rule:
J2_P1_3_SAVING_MUST_BE_CROSS_CORRELATION_NOT_SELF_MOMENTS.

## 5. Bettin--Chandee determinant audit

A legal way to make the prime e-variable smooth is to take the all-unit Vaughan branch.

Then Bettin--Chandee Corollary 1 fits the determinant
\[
h b-e k=\Delta
\]
with
\[
M_1=P^{1/3},\quad
M_2=P^{1/2},\quad
N_1=P^{1/2},\quad
N_2=P^{2/3},
\]
where \(h,e\) are the smooth variables and \(k,b\) carry arbitrary coefficients.

The anisotropy parameter is
\[
R_{\rm BC}
=
\frac{M_1N_2}{M_2N_1}
+
\frac{M_2N_1}{M_1N_2}
\asymp1,
\]
because
\[
M_1N_2=M_2N_1=P.
\]

Thus the rectangular aspect ratio itself costs no power in this theorem.

But
\[
\|\alpha\|\|\beta\|
\asymp
P^{1/4}P^{1/3}
=
P^{7/12},
\]
\[
(N_1N_2)^{7/20}
=
P^{49/120},
\]
and
\[
(N_1+N_2)^{1/4}
=
P^{1/6}.
\]

Therefore the Corollary 1 error is
\[
\boxed{
P^{139/120+\varepsilon},
}
\]
even with smoothness parameter \(P^{o(1)}\).

This is larger than the raw \(P\)-scale and far above the required centered \(P^{2/3}\).

Classification:
BC_TWO_ARBITRARY_DETERMINANT_QUANTITATIVELY_CLOSED_AS_ROUTE.

## 6. Meaning of the aspect-ratio calculation

Although Bettin--Chandee is too weak, the identity
\[
M_1N_2=M_2N_1=P
\]
shows that the box
\[
P^{2/3},P^{1/3},P^{1/2},P^{1/2}
\]
is determinant-balanced despite being geometrically anisotropic.

This agrees with the smooth Ganguly--Guria determinant result, where spectral/Kuznetsov cancellation reaches the \(X^{1+\varepsilon}\) scale in the isotropic model.

The remaining difficulty is therefore arithmetic-weight transfer, not a basic failure of determinant geometry.

## 7. Correct next target

The exact frontier remains:
\[
\boxed{
\sum_{\chi\ne\chi_0}
B E R S\overline H
\ll
P^{5/3+o(1)}.
}
\]

Any next theorem must correlate at least two of the factor groups before absolute values or self-moments destroy the needed \(P^{-1/3}\).

Priority:
J2_FIVE_FACTOR_CROSS_CORRELATION_ESTIMATE.


## 8. Audit correction — Bettin--Chandee determinant map was tied to the invalid wrap-shell

Sections 5--6 above used the determinant model
\[
h b-e k=\Delta.
\]

That equation came from the now-withdrawn character reorientation
\[
BH\mid EK.
\]

It is therefore **not an exact reformulation of the j=2 hard core**.

The exact arithmetic condition remains
\[
\boxed{
b e k\equiv -h\pmod P,
}
\]
and with \(k=rs\),
\[
\boxed{
b e r s\equiv -h\pmod P.
}
\]

Hence the Bettin--Chandee calculation in Sections 5--6 is retained only as a comparison showing that the artificial balanced determinant box would not have closed quantitatively anyway.

It must not be used as a legal route from the current j=2 frontier.

Withdrawn as proof route:
BC_TWO_ARBITRARY_DETERMINANT_QUANTITATIVELY_CLOSED_AS_ROUTE.

Reclassified as:
BC_ARTIFICIAL_CAUCHY_DETERMINANT_COMPARISON_ONLY.

Permanent guard:
EXACT_DETERMINANT_MAP_MUST_BE_DERIVED_BEFORE_APPLYING_BC_DFI.

## 9. Correct quotient equation

Introduce the integer quotient \(\ell\) by
\[
b e r s+h=\ell P.
\]

Since
\[
b\asymp P^{2/3},
\qquad
ers\asymp P,
\]
we have
\[
\boxed{
\ell\asymp P^{2/3}.
}
\]

Let
\[
n:=ers\asymp P.
\]

Then the exact congruence is equivalent to
\[
\boxed{
b n-\ell P=-h.
}
\]

This is the correct two-by-two determinant-like relation:
\[
\det
\begin{pmatrix}
b & \ell\\
P & n
\end{pmatrix}
=
bn-\ell P
=
-h,
\]
with \(P\) fixed prime and \(n\) carrying the structured triple-prime coefficient.

No character orientation is changed in deriving this equation.

## 10. Exact Farey-critical geometry

Divide the quotient equation by \(bP\):
\[
\frac{n}{P}-\frac{\ell}{b}
=
-\frac{h}{bP}.
\]

At the hard scales
\[
b,\ell\asymp P^{2/3},
\qquad
|h|\lesssim P^{1/3},
\]
so
\[
\boxed{
\left|
\frac{n}{P}-\frac{\ell}{b}
\right|
\lesssim
P^{-4/3}.
}
\]

But
\[
b^{-2}\asymp P^{-4/3}.
\]

Therefore the quotient formulation is exactly Farey-critical:
\[
\boxed{
\left|
\frac{n}{P}-\frac{\ell}{b}
\right|
\lesssim b^{-2}.
}
\]

As in the earlier determinant audit, this supplies no free spacing gain by itself.

Permanent rule:
J2_VALID_QUOTIENT_FAREY_SCALE_IS_CRITICAL.

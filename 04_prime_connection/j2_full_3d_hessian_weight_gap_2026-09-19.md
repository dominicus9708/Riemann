# j=2 full three-variable Hessian benchmark and arithmetic-coefficient gap — 2026-09-19

## Status
- Riemann hypothesis: OPEN.
- Context: sharp j=2 block
  \[
  d\asymp H^2,\qquad p,q\asymp H^3,
  \]
  with reciprocal normalized amplitude \(F=H^4\).
- New geometric result: the full three-variable reciprocal phase has a nondegenerate Hessian, and a smooth unweighted 3D B-process lands exactly on the target H^6 scale.
- Literature benchmark: a generic Robert--Sargos three-dimensional monomial estimate with arbitrary bounded arithmetic coefficients misses the target by H^(3/4) in the best permutation.
- Interpretation: the current obstruction is precisely the transfer of full three-dimensional mixed-curvature cancellation through one Möbius and two von-Mangoldt weights.
- Classification: \`J2_3D_HESSIAN_WEIGHT_TRANSFER_FRONTIER\`.

## 1. Full sharp phase

Write
\[
D:=H^2,\qquad P:=H^3.
\]

The sharp j=2 sum has schematic phase
\[
f(d,p,q)
=
F\,\phi(d/D,p/P,q/P),
\qquad
F=H^4,
\]
with
\[
\phi(x,y,z)
=
c\,x^{-1/2}y^{-1/2}z^{-1/2},
\qquad
c\asymp1.
\]

The arithmetic weights are:
- Möbius/divisor-bounded on d;
- von Mangoldt / prime on p;
- von Mangoldt / prime on q.

The target is
\[
\boxed{
T_{j=2}\ll_\varepsilon H^{6+\varepsilon}.
}
\]

## 2. Normalized Hessian is nondegenerate

For
\[
\phi(x,y,z)=x^{-1/2}y^{-1/2}z^{-1/2},
\]
at normalized dyadic scale the Hessian has the form
\[
D^2\phi
=
\frac{\phi}{4}
\begin{pmatrix}
3x^{-2} & x^{-1}y^{-1} & x^{-1}z^{-1}\\
x^{-1}y^{-1} & 3y^{-2} & y^{-1}z^{-1}\\
x^{-1}z^{-1} & y^{-1}z^{-1} & 3z^{-2}
\end{pmatrix}.
\]

After extracting the nonzero diagonal scaling factors, the core matrix is
\[
\begin{pmatrix}
3&1&1\\
1&3&1\\
1&1&3
\end{pmatrix}.
\]

Its eigenvalues are
\[
2,\ 2,\ 5,
\]
so
\[
\det
\begin{pmatrix}
3&1&1\\
1&3&1\\
1&1&3
\end{pmatrix}
=
20.
\]

Hence
\[
\boxed{
\det D^2\phi\ne0
}
\]
uniformly on every fixed dyadic box.

## 3. Physical Hessian determinant

The physical variable lengths are
\[
L_d=H^2,
\qquad
L_p=L_q=H^3.
\]

Each Hessian entry has the scale
\[
\frac F{L_iL_j}.
\]

Therefore
\[
\det D^2_{d,p,q}f
\asymp
\frac{F^3}
{L_d^2L_p^2L_q^2}.
\]

Substituting the sharp scales gives
\[
\frac{H^{12}}
{H^4H^6H^6}
=
\boxed{H^{-4}}.
\]

Thus the three-dimensional stationary amplitude is
\[
\boxed{
|\det D^2 f|^{-1/2}
\asymp H^2.
}
\]

## 4. Dual gradient box

The gradient widths in the three variables are
\[
\frac F{L_d}
=
\frac{H^4}{H^2}
=
H^2,
\]
and
\[
\frac F{L_p}
=
\frac F{L_q}
=
\frac{H^4}{H^3}
=
H.
\]

Therefore the three-dimensional Poisson/B-process dual box contains
\[
\boxed{
H^2\cdot H\cdot H
=
H^4
}
\]
relevant lattice frequencies.

Bounding the stationary integrals absolutely yields
\[
H^4\times H^2
=
\boxed{H^6}.
\]

Thus for smooth unweighted integer coefficients the natural 3D stationary-phase bound is exactly the target:
\[
\boxed{
T_{\rm smooth,3D}
\ll_\varepsilon
H^{6+\varepsilon}.
}
\]

Classification:
\`SMOOTH_3D_BPROCESS_EXACTLY_MATCHES_J2_TARGET\`.

## 5. Why lower-dimensional reductions lose power

The 3D dual lengths are
\[
H^2,\ H,\ H.
\]

If one first destroys one mixed direction by Cauchy / one-sided large sieve / branchwise absolute values, the remaining analysis no longer sees the full determinant of the 3x3 Hessian.

This is consistent with the sequence of method losses already found:
\[
H^{1/2},
\quad
H^{1/4},
\quad
H^{1/6},
\quad
H^{1/8}.
\]

Those are not contradictory estimates for the true sum.

They are losses from progressively richer but still partial uses of the full mixed curvature.

Permanent interpretation:
\`J2_POLYNOMIAL_DEFICITS_ARE_PARTIAL_HESSIAN_METHOD_LOSSES\`.

## 6. Robert--Sargos generic arithmetic-coefficient benchmark

Robert--Sargos consider three-dimensional monomial sums with arbitrary coefficients of modulus at most one and prove bounds of the schematic form
\[
S_0(H_1,M,N)
\ll_\varepsilon
(H_1MN)^{1+\varepsilon}
\left[
\left(
\frac{X}{H_1MN^2}
\right)^{1/4}
+
(H_1M)^{-1/4}
+
N^{-1/2}
+
X^{-1/2}
\right]
\]
after choosing a distinguished N-variable.

Insert
\[
H_1=H^2,\qquad
M=N=H^3,\qquad
X=H^4.
\]

The four terms produce:
\[
H^8\cdot H^{-7/4}
=
H^{25/4},
\]
\[
H^8\cdot H^{-5/4}
=
H^{27/4},
\]
\[
H^8\cdot H^{-3/2}
=
H^{13/2},
\]
and
\[
H^8\cdot H^{-2}
=
H^6.
\]

The dominant term is
\[
\boxed{
H^{27/4+\varepsilon}
=
H^{6+3/4+\varepsilon}.
}
\]

If the H^2 variable is chosen as the distinguished N-variable, the result is worse.

Therefore the best direct generic Robert--Sargos insertion misses the target by
\[
\boxed{H^{3/4}}.
\]

Classification:
\`ROBERT_SARGOS_GENERIC_3D_H3_4_GAP\`.

## 7. Meaning of the H^(3/4) literature gap

The smooth stationary-phase benchmark proves that the phase geometry itself has enough cancellation.

The Robert--Sargos comparison shows that a theorem robust under essentially arbitrary bounded arithmetic coefficients does not retain all of that gain at the present asymmetric lengths.

Hence the new analytic question is not:
\[
\text{is the reciprocal phase oscillatory enough?}
\]

It is:
\[
\boxed{
\text{can the special }(\mu,\Lambda,\Lambda)\text{ coefficient structure
retain the missing mixed-curvature gain?}
}
\]

This is much narrower.

## 8. Double-Vaughan progress inside this gap

Applying Vaughan structure to both prime variables has already reduced the branchwise deficit to
\[
\boxed{H^{1/8}}
\]
on the double-refined central branch.

Thus there are now two numerical benchmarks:

- fully generic bounded-coefficient 3D theorem:
  \[
  H^{3/4}\text{ gap};
  \]

- coefficient-aware double-Vaughan + product-balance architecture:
  \[
  H^{1/8}\text{ gap}.
  \]

The latter is much closer to the smooth Hessian limit.

This confirms that the actual prime/Möbius coefficient structure is already recovering most of the generic arithmetic-weight loss.

## 9. Exact current target

The most economical current theorem would be either:

### Route A — direct weighted 3D Hessian theorem
\[
\boxed{
\sum_{d\asymp H^2}
\mu(d)
\sum_{p,q\asymp H^3}
\Lambda(p)\Lambda(q)
e(H^4\phi(d/H^2,p/H^3,q/H^3))
\ll_\varepsilon
H^{6+\varepsilon}.
}
\]

### Route B — close the reduced residual
Improve the double-refined central branch only by
\[
\boxed{H^{-1/8}}.
\]

Route B is currently the smaller technical target.

## 10. Literature status

Robert--Sargos gives a directly relevant real three-dimensional monomial framework with arbitrary coefficients, but not the target exponent in this parameter range.

A fresh search did not identify a published theorem that directly handles the exact weighted phase above at H^(6+epsilon).

No novelty claim is made.

Permanent priority:
\`J2_H1_8_RESIDUAL_AS_WEIGHTED_3D_HESSIAN_GAP\`.

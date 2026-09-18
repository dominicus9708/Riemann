# j=2 connected determinant prior-art audit and generic Kloosterman-fraction barrier — 2026-09-19

## Status
- Riemann hypothesis: OPEN.
- Sector: j=2 sharp connected covariance after diagonal, principal-density, one-prime marginals, outer-factorability, and gcd-shell reductions.
- First stress test: g=1,
  [
  a,basymp D=H^2,qquad p,p'asymp P=H^3,qquad |ap-bp'|lesssim H.
  ]
- Correct normalized target:
  [
  mathcal C_{m conn}ll_arepsilon H^{5+arepsilon}=S^{1+arepsilon}.
  ]
- Main audit results:
  1. close determinant-equation prior art exists, but does not directly cover the two-small-arithmetic-weight + two-prime anisotropic geometry;
  2. general E2 correlation theorems apply to the shift range but are not strong enough to imply the Poisson-scale centered aggregate;
  3. even a favorable hypothetical smoothing of the two small variables followed by classical/generic Kloosterman-fraction bounds misses the required target by a polynomial factor (H^{13/8}).
- Classification: `J2_CONNECTED_DETERMINANT_PRIOR_ART_GAP`.

## 1. Current connected shell

The remaining g=1 object has the determinant equation
[
oxed{ap-bp'=k}
]
with
[
a,basymp H^2,qquad p,p'asymp H^3,qquad |k|lesssim H.
]

The small variables retain inherited Möbius/divisor-bounded arithmetic coefficients, while p,p' carry prime/von-Mangoldt weights.

The raw unsigned shell has scale
[
H^6,
]
whereas the centered target is
[
oxed{H^5}.
]

Thus one full factor H of variance-level cancellation remains necessary.

## 2. Guria determinant theorem: closest positive control

Guria studies
[
ad-pb=r
]
in an equal box, with one arbitrary coefficient (alpha(a)=O(a^arepsilon)), one prime variable p, and the other two determinant variables unrestricted and smoothed.

Her theorem gives, for fixed nonzero r, an error of the shape
[
O_arepsilon!left(
X^{7/4+arepsilon}
+
|r|^{1/5}X^{31/20+arepsilon}
ight).
]

Taking the arbitrary coefficient as a prime indicator yields a determinant count with two prime entries and a power-saving error.

This is a strong positive control: prime restrictions and determinant geometry are compatible with genuine power saving.

However it does **not** directly imply the present estimate, because our shell simultaneously contains:
- two arithmetic small-variable coefficients (alpha_aalpha_b);
- two large prime variables p,p';
- anisotropic lengths (H^2,H^2,H^3,H^3);
- a centered aggregate over (|k|lesssim H).

Guria's Poisson step explicitly uses an unrestricted/smooth determinant variable. In the present shell neither small variable may be silently replaced by a smooth coefficient.

Classification:
`GURIA_TWO_PRIME_DETERMINANT_NEAR_MATCH_NOT_BLACK_BOX`.

## 3. Fixed four-prime determinant severity guard

On the coherent atomic subfamily, a and b may themselves be prime-scale factors with constant Möbius sign.

A route which demands a pointwise theorem for
[
ap-bp'=k
]
with all four entries prime and a fixed k would enter the fixed-determinant prime-matrix problem.

The literature treats even the infinitude question for (2	imes2) prime-entry matrices with fixed determinant 2 as open/twin-prime-type.

Therefore the current project must exploit the **averaging in k and/or in the frames (a,b)**. It must not replace the averaged centered theorem by a stronger pointwise four-prime determinant theorem.

Permanent guard:
`DO_NOT_UPGRADE_AVERAGED_CONNECTED_TARGET_TO_FIXED_FOUR_PRIME_DETERMINANT`.

## 4. Evans E2-correlation theorem is in range

Let
[
S=H^5.
]

Our product sequence is a fixed-range E2-type sequence:
[
n=ap,qquad aasymp S^{2/5},quad pasymp S^{3/5}.
]

Evans proves Hardy--Littlewood-type asymptotics for general E2-E2 correlations for almost all shifts (|h|le H_{m shift}) once
[
H_{m shift}ge
exp((log S)^{1-arepsilon}).
]

Our shift length
[
H_{m shift}=S^{1/5}
]
is much larger, so the theorem is comfortably in range.

This confirms that the fixed-range E2 pair geometry itself is not an exotic unsupported model.

## 5. Why almost-all shift asymptotics do not close the variance target

The current target is not merely:
[
mathcal R(h)=	ext{expected main term}+o(	ext{main term})
]
for most h.

It is the **signed normalized aggregate**
[
sum_{|h|lesssim H}W(h/H)mathcal R_{m centered}(h)
ll S^{1+arepsilon},
]
starting from a raw (HS)-scale correlation mass.

Thus the required gain is polynomial:
[
oxed{H^{-1}}.
]

An exceptional set of size (Hlog^{-B}S), or a typical correlation error with only logarithmic relative saving, does not by itself supply this full factor H after summing the shifts.

Therefore:
[
oxed{
	ext{almost-all E2 correlation asymptotic}

otRightarrow
	ext{Poisson-scale centered variance}.
}
]

Permanent guard:
`ALMOST_ALL_SHIFT_ASYMPTOTIC_NOT_POISSON_VARIANCE`.

## 6. Favorable smoothing false control

To measure how strong a generic Kloosterman-fraction black box would be, temporarily replace the two small arithmetic weights by smooth weights.

This is **not** a legal proof step; it is a deliberately favorable false control.

Write the determinant as
[
pa-p'b=k
]
with
[
p,p'asymp P=H^3,qquad a,basymp D=H^2.
]

Eliminate a and view the equation modulo p:
[
p'bequiv-kpmod p.
]

If b has a smooth D-scale weight, Poisson summation in b modulo p has:
- zero mode producing the density/main term;
- nonzero dual frequency
  [
  |n|lesssim P/D=H;
  ]
- prefactor
  [
  D/P=H^{-1};
  ]
- Kloosterman-fraction phase
  [
  e!left(rac{nk,overline{p'}}{p}ight).
  ]

Since
[
|n|lesssim H,qquad |k|lesssim H,
]
the numerator variable
[
c=nk
]
has support length
[
Aasymp H^2.
]

Thus the formal nonzero-frequency model is
[
rac{D}{P}
sum_{p,p'asymp P}
lambda_plambda_{p'}
sum_{clesssim H^2}
u_c,
e(coverline{p'}/p).
]

## 7. Irving benchmark

For fixed numerator c, Irving's prime Kloosterman-fraction average with
[
Qasymp Xasymp P
]
gives the scale
[
P^{15/8+arepsilon}
]
(the second term (P^{11/6}) is smaller).

Trivially summing the H^2 choices arising from (n,k), then multiplying the Poisson prefactor H^{-1}, gives
[
H^{-1}cdot H^2cdot P^{15/8}
=
H^{-1+2+45/8}
=
oxed{H^{53/8+arepsilon}}.
]

Compared with the target
[
H^5=H^{40/8},
]
the deficit is
[
oxed{H^{13/8}}.
]

Classification:
`IRVING_GENERIC_FRACTION_H13_8_DEFICIT`.

## 8. Bettin--Chandee trilinear benchmark

The same false-control geometry may combine c=nk into a divisor-bounded coefficient (
u_c).

Use:
[
M=N=P=H^3,qquad A=H^2.
]

Coefficient L2 norms have scales
[
|lambda_p|_2asymp H^{3/2+o(1)},
qquad
|lambda_{p'}|_2asymp H^{3/2+o(1)},
qquad
|
u|_2ll H^{1+o(1)}.
]

Hence the norm product is
[
H^{4+o(1)}.
]

In the Bettin--Chandee trilinear estimate the two principal geometric terms have scales
[
(AMN)^{7/20}(M+N)^{1/4}
=
H^{71/20+o(1)}
]
and
[
(AMN)^{3/8}(AM+AN)^{1/8}
=
H^{29/8+o(1)}.
]

The second dominates. Therefore the trilinear sum is bounded at the scale
[
H^{4+29/8+arepsilon}
=
H^{61/8+arepsilon}.
]

Restoring the Poisson factor H^{-1} gives
[
oxed{H^{53/8+arepsilon}},
]
again missing the target H^5 by
[
oxed{H^{13/8}}.
]

Thus two independent classical Kloosterman-fraction routes identify the same generic benchmark gap.

Permanent rule:
`GENERIC_KLOOSTERMAN_FRACTION_H13_8_GAP`.

## 9. Interpretation of the benchmark

This does **not** prove that the connected sector cannot be closed.

It proves something more limited and useful:

- merely making the small variables smooth would not be enough;
- ordinary Poisson + generic prime Kloosterman-fraction estimates still fall polynomially short;
- therefore a successful proof must use structure beyond this black-box architecture.

Potential additional resources still available in the original problem include:
1. connected centering before completion;
2. the full k-average rather than absolute summation over k;
3. the unimodular determinant-one relation between the two linear forms;
4. outer-factorability strata;
5. the g-shell hierarchy;
6. coefficient-sensitive cancellation before Poisson;
7. a modern Kloosterman estimate only after deriving an exact form that retains these resources.

## 10. Refined next target

Do not start with Poisson in a or b.

The next legal reduction should first transform the connected centered prime factors while leaving the small arithmetic coefficients intact.

Two candidate legal routes remain:

### A. character/dispersion route
Exploit the already-closed ratio-multiplicity and one-prime marginal modes, then derive a genuinely connected character kernel. Test whether a fourth-moment/hybrid large-sieve estimate gains the missing H without converting the problem to pointwise AP distribution.

### B. prime-identity route
Apply Vaughan/Heath--Brown to one or both large prime variables, preserve a,b,k until a genuinely smooth summation variable appears, and only then apply Poisson/Kloosterman completion.

Any route which first replaces the Möbius coefficients by smooth weights is classified only as a false-control benchmark.

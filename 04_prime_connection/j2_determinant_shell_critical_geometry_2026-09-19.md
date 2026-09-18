# j=2 H-normalization and determinant-shell geometry — 2026-09-19

## Status
- Riemann hypothesis: OPEN.
- Sector: j=2 sharp asymmetric endpoint alpha=0.
- Previous normalized-shift target corrected to D_shift << S^(1+eps).
- New structural reduction: the residual is a centered determinant-shell discrepancy at the exact Farey resolution.
- Classification: `J2_DETERMINANT_SHELL_CRITICAL_GEOMETRY`.

## 1. One-parameter sharp scaling

Set
[
H:=V^{1/2}.
]

Then the entire sharp endpoint becomes
[
oxed{
D=H^2,qquad
P=H^3,qquad
S=DP=H^5,qquad
X=S/H=H^4.
}
]

Thus the generic modulus ratio
[
D=P^{2/3}
]
and the shift length
[
H=P^{1/3}
]
are not independent exponents: they come from a single critical scale H.

## 2. Correct centered shift target

For a normalized triangular/smooth shift weight W(h/H)=O(1), the Selberg expansion has the form
[
J_a(S,H)
=
Hsum_{|h|lesssim H}W(h/H),mathcal R(h)
+
O(	ext{boundary/smoothing}),
]
where (mathcal R(h)) is the centered correlation.

Therefore
[
J_a(S,H)ll_arepsilon HS^{1+arepsilon}
]
requires
[
oxed{
sum_{|h|lesssim H}W(h/H),mathcal R(h)
ll_arepsilon S^{1+arepsilon}=H^{5+arepsilon}.
}
]

The uncentered correlation mass has natural scale
[
HS=H^6.
]

Hence the arithmetic residual must recover one full factor
[
oxed{H^{-1}}.
]

After the square root in the original double-large-sieve estimate this is exactly
[
H^{-1/2}=V^{-1/4},
]
the previously identified j=2 imbalance loss.

Permanent guard:
`NORMALIZED_SHIFT_TARGET_IS_S_NOT_HS`.

## 3. GCD removal and determinant form

Write
[
g=(d,d'),qquad d=ga,qquad d'=gb,qquad (a,b)=1,
]
and
[
h=gk.
]

The shifted-product equation becomes
[
oxed{
ap-bp'=k.
}
]

Equivalently,
[
det
egin{pmatrix}
a & b\
p'&p
end{pmatrix}
=k.
]

Thus the nonzero centered residual is an averaged family of determinant-k shells with
[
a,basymp H^2/g,qquad
p,p'asymp H^3,qquad
|k|lesssim H/g.
]

For k nonzero, p=p' is impossible because then p divides k while |k|<p.
Since p,p' are larger than a,b and (a,b)=1, there are no cross prime divisibilities; in the generic coprime sector the two products ap and bp' are coprime.

Classification:
`DETERMINANT_SHELL_FORM`.

## 4. Uniqueness for fixed prime pair

Fix p,p' and k.

All integer solutions of
[
ap-bp'=k
]
differ by
[
(a,b)mapsto(a+t p',,b+t p).
]

But
[
a,basymp H^2,qquad
p,p'asymp H^3.
]

The admissible a,b windows are shorter than one solution step.

Hence:
[
oxed{
	ext{for fixed }(p,p',k),	ext{ there is at most one admissible }(a,b)
}
]
inside a fixed dyadic box.

This removes multiplicity as a possible source of the DLS loss, but does not itself yield the required H-saving.

## 5. Exact Farey-resolution boundary

From
[
ap-bp'=k
]
we obtain
[
left|
rac{a}{b}-rac{p'}{p}
ight|
=
rac{|k|}{bp}.
]

At the sharp scales,
[
rac{|k|}{bp}
lesssim
rac{H}{H^2H^3}
=
H^{-4}
=
D^{-2}
=
X^{-1}.
]

Reduced fractions with denominator of order D naturally have spacing of order D^{-2}.

Therefore the j=2 sharp residual sits exactly at the Farey resolution:
[
oxed{
left|a/b-p'/pight|lesssim D^{-2}.
}
]

Consequences:
- ordinary fraction-spacing alone cannot give a polynomial saving;
- the critical configuration is not an artifact of a loose DLS proximity estimate;
- any successful estimate must exploit arithmetic signs, prime structure, determinant-shell averaging, or post-spacing phase information.

Permanent guard:
`FAREY_CRITICAL_RESOLUTION_NO_FREE_SPACING_GAIN`.

## 6. Exact linear-form parametrization

For fixed coprime a,b choose (ar a) with
[
aar aequiv1pmod b
]
and define
[
t_{a,b}:=rac{aar a-1}{b}.
]

The congruence
[
apequiv kpmod b
]
gives
[
p=kar a+bell.
]

Substitution into (ap-bp'=k) gives
[
oxed{
p=kar a+bell,qquad
p'=aell+k,t_{a,b}.
}
]

Since
[
p,p'asymp H^3,qquad a,basymp H^2,
]
the free parameter has length
[
ellasymp P/Dasymp H.
]

Thus both short variables satisfy
[
|k|lesssim H,qquad ellasymp H.
]

The j=2 determinant shell is therefore a two-short-variable family of simultaneous prime linear forms over a long ((a,b))-family.

Classification:
`J2_TWO_SHORT_VARIABLE_LINEAR_FORMS`.

## 7. Why the required saving is now transparent

Before centering, the parameter count is schematically
[
(a,b)	imes(k,ell)
sim
H^4	imes H^2
=
H^6.
]

The normalized centered target is
[
H^5.
]

Therefore one needs exactly one factor H of cancellation beyond the local-density main term:
[
oxed{
H^6longrightarrow H^5.
}
]

Equivalently, the H x H short box (k,ell) must contribute one square-root-sized saving in aggregate, or an equivalent saving must arise from a coupled dispersion/Kloosterman mechanism involving a,b,p,p'.

This is the variance-level form of the same missing V^{-1/4} DLS factor.

## 8. Correct transform order

A direct Poisson transform in a or b is not legitimate for the full residual when the inherited coefficients alpha_d are Möbius/divisor-bounded rather than smooth.

Therefore the next transform must preserve the different small factors and first use an identity/dispersion step on the prime variables (Vaughan, Heath--Brown, or an equivalent prime decomposition).

Only after that step may one legitimately expose reciprocal phases generated by
[
pequiv kar apmod b.
]

Permanent guard:
`DO_NOT_POISSON_ARBITRARY_MOBIUS_COEFFICIENT_AS_SMOOTH`.

## 9. Literature audit correction

The January 2026 Dong--Robles--Zeindler preprint on bilinear Kloosterman fractions carries an author correction: a missing L^2 factor changes L^5 to L^7, and the authors state that the argument no longer yields the improved bound originally claimed.

Therefore this project must not cite that preprint as supplying a new improved saving for the present residual.

Blomer--Pascadi (2026) proves genuine new bilinear Kloosterman-sum bounds for all moduli, including a c^{-1/32} saving in the square-root-length critical regime. However the current j=2 determinant residual has not yet been transformed into the exact fixed-modulus bilinear Kloosterman form required by that theorem.

Classification:
- `DRZ_2026_IMPROVED_BOUND_WITHDRAWN`.
- `BLOMER_PASCADI_EXACT_PARAMETER_MAP_REQUIRED`.

## 10. Next analytic target

Starting from
[
ap-bp'=k,
]
retain
[
a,basymp H^2,qquad
k,ellasymp H,qquad
p,p'asymp H^3.
]

Apply a prime decomposition while keeping a,b,k distinct, derive the first exact bilinear/trilinear reciprocal form, and measure its unconditional saving against the required
[
oxed{H^{-1}}
]
variance-level gain.

The next checkpoint is not whether a Kloosterman theorem gives any power saving, but whether its exact transformed parameter range supplies the full missing H.

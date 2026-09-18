# Common cell-mean / centered-variance residual reduction — 2026-09-19

## Status
- Riemann hypothesis: OPEN.
- Context: common sector balance functional leaves a residual factor (V^{Delta/2}) in every sharp asymmetric two-product block.
- New reduction: after splitting the long-side product support into its local mean density plus centered cell fluctuation, the mean-density contribution is already bounded at the target (V^{3+arepsilon}) by ordinary reciprocal curvature.
- Therefore the only genuinely new input required is a diagonal-scale centered cell variance estimate.
- Classification: `COMMON_CELL_VARIANCE_REDUCTION`.

## 1. General asymmetric block

Let the optimal two-product split have lengths
[
R=V^{2-delta},
qquad
S=V^{2+delta},
qquad
delta=Delta>0,
]
with normalized reciprocal parameter
[
X=V^2.
]

The DLS frequency resolution on the long side is
[
X^{-1}.
]

For
[
v(y)=left(rac ySight)^{-1/2},
qquad
v'(y)asymp S^{-1},
]
one natural frequency cell corresponds to an arithmetic (y)-interval of length
[
oxed{
H=rac SX=V^delta.
}
]

There are
[
Basymp rac SH=X=V^2
]
such cells across a dyadic long-side interval.

## 2. Cell decomposition

Let
[
c_b
]
be the weighted arithmetic coefficient mass in the (b)-th long-side cell.

Write
[
c_b=ar c_b+eta_b,
]
where
- (ar c_b) is a smooth local density/main term;
- (eta_b) is the centered fluctuation.

For a constant-density model one may take (ar c_bapprox ho H). In a rigorous implementation (ar c_b) may vary smoothly across the dyadic interval.

## 3. Mean-density part closes by reciprocal curvature

Fix a short-side frequency parameter (uasymp1).
The mean-density long-side contribution is modeled by
[
hosum_{yasymp S}W(y/S)e(Xu,v(y)).
]

For
[
f(y)=Xu,v(y),
]
we have
[
|f''(y)|asymp rac{X}{S^2}.
]

The ordinary second-derivative estimate gives
[
sum_{yasymp S}W(y/S)e(f(y))
ll
Ssqrt{X/S^2}
+
(X/S^2)^{-1/2}.
]

Since
[
S=V^{2+delta},qquad X=V^2,
]
both terms have size
[
oxed{V^{1+delta}}.
]

Multiplying by the short-side length
[
R=V^{2-delta}
]
gives
[
oxed{
R,V^{1+delta}=V^3.
}
]

Thus the smooth mean-density component is already at the required edge scale.

Permanent rule:
`CELL_MEAN_CURVATURE_CLOSED`.

## 4. Centered fluctuation target

After replacing each long-side cell by its centered coefficient (eta_b), the cell centers are separated at the natural (1/X) frequency resolution.

The short side has length (R<X), so its own DLS proximity energy is diagonal-scale:
[
mathcal B_Rll_arepsilon R V^arepsilon.
]

If the centered cell coefficients satisfy
[
oxed{
sum_{basymp B}|eta_b|^2
ll_arepsilon
S V^arepsilon,
}
]
then the cell-center DLS gives
[
|T_{m fluct}|^2
ll_arepsilon
Xcdot Rcdot Scdot V^arepsilon
=
V^{6+arepsilon}.
]

Hence
[
oxed{
T_{m fluct}ll_arepsilon V^{3+arepsilon}.
}
]

Therefore diagonal/Poisson-scale centered cell variance supplies **exactly** the missing factor
[
V^{-delta/2}
]
from the common balance functional.

## 5. Equivalent Selberg-integral form

Let (a_n) be the long-side product coefficient and (ho(x)) its smooth mean density.
Define
[
A(x;H)
=
sum_{x<nle x+H}a_n
-
int_x^{x+H}ho(t),dt.
]

The cell variance condition is implied by the short-interval Selberg-type estimate
[
oxed{
J_a(S,H)
:=
int_S^{2S}|A(x;H)|^2,dx
ll_arepsilon
H S^{1+arepsilon}.
}
]

Indeed, sampling disjoint (H)-cells converts this to
[
sum_b|eta_b|^2
ll_arepsilon
S^{1+arepsilon}.
]

Thus the remaining analytic input can be stated independently of the reciprocal phase.

## 6. Sharp-sector dictionary

### (j=2, alpha=0)

Long side:
[
S=V^{5/2}.
]

Cell:
[
H=V^{1/2}=S^{1/5}.
]

Coefficient shape:
[
a_n
=
sum_{substack{n=dp\dasymp V\pasymp V^{3/2} {m prime}}}
a_d,
]
with divisor-bounded/Möbius-type (a_d).

Required variance:
[
oxed{
J_{E_2}(S,S^{1/5})
ll_arepsilon
S^{6/5+arepsilon}.
}
]

### (j=1) long-smooth sharp point

Long side:
[
S=V^{7/3}.
]

Cell:
[
H=V^{1/3}=S^{1/7}.
]

Prime-product model:
[
n=dq_1q_2,
qquad
dasymp V,quad q_1,q_2asymp V^{2/3}.
]

Required:
[
oxed{
J_{E_3	ext{-type}}(S,S^{1/7})
ll_arepsilon
S^{8/7+arepsilon}.
}
]

### (j=0) sharp point

Long side:
[
S=V^{9/4}.
]

Cell:
[
H=V^{1/4}=S^{1/9}.
]

Prime-product model:
[
n=q_1q_2q_3,
qquad
q_iasymp V^{3/4}=S^{1/3}.
]

Required:
[
oxed{
J_{E_3,mathrm{balanced}}(S,S^{1/9})
ll_arepsilon
S^{10/9+arepsilon}.
}
]

## 7. Literature audit

### Matomäki 2022

Matomäki's *Almost primes in almost all very short intervals* proves mean-square bounds of the form
[
int |E^pm(x)|^2,dxll hX
]
for carefully constructed Richert-sieve coefficients.

This is structurally the same Poisson/diagonal scale required here.

However the theorem is not a black-box variance theorem for an arbitrary exact (E_2) or (E_3) dyadic product indicator. The proof uses specially factorable sieve weights and separate Type-I / Kloosterman estimates.

Classification:
`SIEVE_WEIGHTED_VARIANCE_PROMISING_NOT_DIRECT`.

### Matomäki--Teräväinen E2 work

Their exact-(E_2) results reach polylogarithmic interval lengths, but via specially engineered prime-factor ranges, minorants and sparse Dirichlet-polynomial estimates.

Their Type-II propositions cannot simply be quoted for the present centered dyadic product variance; the parameter geometry and the coefficient to be centered differ.

Classification:
`EXISTENCE_NOT_CENTERED_VARIANCE_GUARD`.

### Gorodetsky rough-number variance

For (j=0), the balanced triple-prime support lies at roughness threshold
[
y=S^{1/3}
]
and cell length
[
H=S^{1/9}.
]

Gorodetsky's unconditional rough-number variance theorem, when (H=S^c), allows (y) only up to a polylogarithmic size roughly
[
(log S)^{1/c-1-delta}.
]

Thus the required polynomial threshold (S^{1/3}) is far outside the theorem's unconditional range.

Classification:
`ROUGH_VARIANCE_POWER_RANGE_MISMATCH`.

## 8. Consequence

The common residual front has been reduced to a family of **centered short-interval variance problems for fixed-shape almost-prime product coefficients**.

The order of likely accessibility is:
1. (j=2) sharp (E_2)-type variance at (H=S^{1/5});
2. (j=1) long-smooth (E_3)-type variance at (H=S^{1/7});
3. (j=0) balanced (E_3) variance at (H=S^{1/9}).

The current literature demonstrates the required variance mechanism for related sieve-weighted sequences but does not yet supply these exact three estimates as black boxes.

Permanent rules:
- `CELL_MEAN_CURVATURE_CLOSED`.
- `CENTERED_VARIANCE_NOT_EXISTENCE`.
- `EXACT_PRODUCT_RANGE_MUST_MATCH`.

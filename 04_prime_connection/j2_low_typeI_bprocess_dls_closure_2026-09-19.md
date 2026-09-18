# j=2 low-Type-I B-process + DLS closure — 2026-09-19

## Status
- Riemann hypothesis: OPEN.
- Context: Vaughan-decompose the short prime q before any short-side Cauchy step.
- Sector: Type-I dyadic factorization
  [
  q=mn,qquad
  masymp H^	heta,quad
  nasymp H^{3-	heta},
  qquad 0le	hetale1.
  ]
- Main result: after a smooth B-process / Poisson stationary-phase transform in the unrestricted n-variable, the stationary main term is a bilinear product phase whose two spacing energies are diagonal-scale. Standard double large sieve then gives exactly the target H^{6+epsilon}.
- Remaining bookkeeping: insert the exact Vaughan coefficients and smooth partition/Mellin separations globally. No new arithmetic conjecture is required for this dyadic block.
- Classification: `J2_LOW_TYPEI_BPROCESS_DLS_CLOSED`.

## 1. Original Type-I block

At sharp scale:
[
dasymp H^2,
qquad
pasymp H^3,
qquad
masymp H^	heta,
qquad
nasymp H^{3-	heta}.
]

The reciprocal phase has normalized size
[
F=H^4
]
and schematic form
[
e!left(
F,
Phi!left(
rac d{H^2},
rac p{H^3},
rac m{H^	heta},
rac n{H^{3-	heta}}
ight)
ight),
]
with monomial core
[
(dpmn)^{-1/2}.
]

The n-variable in Type I is unrestricted apart from smooth/logarithmic weights.

## 2. n-derivative scales

Freeze d,p,m and write
[
f(n)=C_{d,p,m},n^{-1/2}.
]

On
[
nasymp N:=H^{3-	heta},
]
the phase magnitude is H^4.

Hence
[
|f'(n)|
asymp
rac{H^4}{N}
=
oxed{H^{1+	heta}},
]
and
[
|f''(n)|
asymp
rac{H^4}{N^2}
=
H^{-2+2	heta}.
]

The dual B-process frequency therefore has length
[
oxed{
R:=H^{1+	heta}.
}
]

The stationary amplitude is
[
|f''|^{-1/2}
asymp
oxed{H^{1-	heta}}.
]

## 3. Exact Legendre phase shape

For
[
f(n)=C n^{-1/2}
]
the stationary equation has
[
n_rasymp(C/r)^{2/3}.
]

The Legendre phase is, up to a nonzero absolute constant,
[
C^{2/3}r^{1/3}.
]

Since
[
C=A(dpm)^{-1/2},
]
the transformed oscillatory core is
[
oxed{
e!left(
c,A^{2/3}
r^{1/3}(dpm)^{-1/3}
ight).
}
]

After normalization this is
[
oxed{
e!left(
H^4,
U(d,r),
V(p,m)
ight),
}
]
where
[
U(d,r)
=
left(rac rRight)^{1/3}
left(rac d{H^2}ight)^{-1/3},
]
and
[
V(p,m)
=
left(rac p{H^3}ight)^{-1/3}
left(rac m{H^	heta}ight)^{-1/3}.
]

Thus the B-process converts the Type-I block into an exact two-group DLS phase.

## 4. Stationary amplitude also separates

A direct stationary-phase calculation gives
[
|f''(n_r)|^{-1/2}
asymp
C^{1/3}r^{-5/6}.
]

Therefore the nonconstant amplitude is a product of powers in
[
(d,r)
quad	ext{and}quad
(p,m),
]
up to the smooth stationary cutoff.

The cutoff condition
[
n_r/Ninoperatorname{supp}W
]
depends smoothly on a multiplicative normalized product and can be separated by Mellin inversion with rapidly decaying transform.

Thus, up to H^epsilon losses, the transformed main term is admissible for a standard double large sieve.

Permanent rule:
`TYPEI_STATIONARY_CUTOFF_MELLIN_SEPARABLE`.

## 5. U-side spacing

The DLS resolution is
[
H^{-4}.
]

Because the cube-root map has derivative bounded above and below on normalized dyadic support,
[
|U(d,r)-U(d',r')|lesssim H^{-4}
]
implies the same scale for the normalized ratio
[
rac{r/H^{1+	heta}}{d/H^2}.
]

Equivalently,
[
|rd'-r'd|
lesssim
H^{	heta-1}.
]

### If 0 <= theta < 1

The left side is an integer, while the right side is o(1).

Hence
[
oxed{rd'=r'd.}
]

The multiplicative energy of the rectangular ratio set
[
dasymp H^2,qquad rasymp H^{1+	heta}
]
is
[
ll_arepsilon
H^{3+	heta+arepsilon},
]
by the standard reduced-fraction/gcd parametrization.

### If theta=1

The determinant is bounded:
[
|rd'-r'd|ll1.
]

Fixed bounded determinant shells in an H^2 x H^2 box contain
[
ll_arepsilon H^{4+arepsilon}
]
quadruples.

Thus uniformly for
[
0le	hetale1,
]
the U-side spacing energy is
[
oxed{
mathcal B_U
ll_arepsilon
H^{3+	heta+arepsilon}.
}
]

## 6. V-side spacing

The V variable depends only on the product pm.

Again
[
|V(p,m)-V(p',m')|lesssim H^{-4}
]
implies
[
|pm-p'm'|
lesssim
H^{	heta-1}.
]

For theta<1 this forces
[
pm=p'm'.
]

Since
[
p,p'asymp H^3
]
are prime while
[
m,m'll H,
]
the equality forces, outside harmless coefficient degeneracies,
[
p=p',qquad m=m'.
]

At theta=1 only O(1) product shifts occur. Treating the product coefficient as divisor-bounded gives the same diagonal-scale energy.

Hence
[
oxed{
mathcal B_V
ll_arepsilon
H^{3+	heta+arepsilon}.
}
]

## 7. Double-large-sieve bound

The transformed normalized phase parameter is
[
X_*=H^4.
]

Bombieri--Iwaniec type DLS therefore gives
[
|widetilde T_	heta|^2
ll_arepsilon
H^4,
mathcal B_U,
mathcal B_V
ll_arepsilon
H^{10+2	heta+arepsilon}.
]

Thus
[
oxed{
widetilde T_	heta
ll_arepsilon
H^{5+	heta+arepsilon}.
}
]

Restoring the B-process stationary amplitude
[
H^{1-	heta}
]
gives
[
oxed{
T_	heta
ll_arepsilon
H^{6+arepsilon}.
}
]

This is exactly the sharp j=2 target.

Classification:
`LOW_TYPEI_STATIONARY_MAIN_CLOSED_AT_H6`.

## 8. Stationary-phase error budget

After scaling n=Nt, the oscillatory integral has large parameter H^4.

A smooth one-dimensional stationary-phase expansion has leading size
[
N H^{-2}=H^{1-	heta}
]
and next error of size at most
[
N H^{-6}
=
H^{-3-	heta}
]
per stationary frequency, with arbitrary further powers available under smooth weights.

There are
[
R=H^{1+	heta}
]
relevant frequencies, so the first omitted stationary error is
[
ll H^{-2}
]
per fixed outer tuple.

Even summing trivially over
[
d,p,m
]
of total cardinality
[
H^{5+	heta+o(1)}
]
gives
[
H^{3+	heta+o(1)}
ll H^6
]
for theta<=1.

Nonstationary frequencies are removable by repeated integration by parts.

Therefore the smooth B-process error is comfortably below target.

Classification:
`LOW_TYPEI_STATIONARY_ERROR_BUDGET_CLOSED`.

## 9. Scope and guards

This closure uses crucially:
- an unrestricted/smooth n-variable;
- theta<=1;
- B-process before any short-side Cauchy;
- retention of the transformed ratio geometry.

It must **not** be transferred to the central Type-II block where both factors carry arithmetic coefficients.

Permanent guards:
- `BPROCESS_BEFORE_SHORT_SIDE_CAUCHY`;
- `RATIO_PRODUCT_DLS_AFTER_BPROCESS`;
- `LOW_TYPEI_CLOSURE_NOT_TYPEII_TRANSFER`.

## 10. Consequence for the phase branch

The original atomic j=2 H^{1/2} obstruction no longer survives in the low-Type-I sector.

After a prime decomposition, the remaining genuinely difficult q-side pieces are pushed into the central arithmetic-factor ranges, where ordinary factor-scale DLS already leaves at most H^{1/4}.

Thus, modulo exact Vaughan bookkeeping, the live phase-adapted obstruction has been reduced from

[
oxed{H^{1/2}}
]
to at most
[
oxed{H^{1/4}}
]
on the genuinely bilinear central branch.

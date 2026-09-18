# j=2 Vaughan factor-scale balance map — 2026-09-19

## Status
- Riemann hypothesis: OPEN.
- Context: phase-adapted branch after the guard that short-side Cauchy forces full E2 variance re-entry.
- Operation: decompose the short prime variable q before Cauchy by a Vaughan/Heath--Brown type identity and audit only the resulting dyadic factor scales.
- Main result: a genuine two-factor decomposition q=mn improves the common product-balance deficit; in the central Type-II range the worst DLS amplitude loss drops from H^{1/2} to H^{1/4}.
- This is not yet a sector closure because Type-I endpoint blocks can retain the original H^{1/2} deficit.
- Classification: `J2_VAUGHAN_FACTOR_SCALE_BALANCE_MAP`.

## 1. Sharp H geometry

Use
[
dasymp H^2,
qquad
pasymp H^3,
qquad
qasymp H^3,
]
so the full product has H-exponent 8 and the self-dual product scale is
[
H^4	imes H^4.
]

Before decomposing q, the factor exponent multiset is
[
{2,3,3}.
]

The nearest subset exponent to 4 is 3 or 5, so the H-scale imbalance is
[
delta_H=1,
]
and standard two-product DLS loses
[
H^{1/2}=V^{1/4}.
]

## 2. Decompose q=mn

On a dyadic piece write
[
masymp H^	heta,
qquad
nasymp H^{3-	heta},
qquad
0le	hetale3.
]

The factor exponent multiset becomes
[
oxed{{2,3,	heta,3-	heta}}.
]

Two useful cross partitions are

[
(pm)mid(dn),
]
with exponents
[
3+	heta,qquad 5-	heta,
]
and

[
(dm)mid(pn),
]
with exponents
[
2+	heta,qquad 6-	heta.
]

The undecomposed partition
[
(mn)mid(dp)
]
has exponents 3 and 5.

Therefore the best distance from exponent 4 is

[
oxed{
delta_H(	heta)
=
minigl(
|	heta-1|,
|	heta-2|,
1
igr).
}
]

## 3. Standard DLS consequence

For a dyadic decomposition piece whose collapsed product coefficients have divisor-type second moments, the common DLS architecture gives

[
oxed{
T_	heta
ll_arepsilon
H^{6+delta_H(	heta)/2+arepsilon}.
}
]

This is only a scale/bookkeeping statement. Legality still requires:
- the exact Vaughan/Heath--Brown coefficient on the dyadic block;
- Mellin separation of coupled smooth cutoffs;
- divisor-moment control after product collapse.

## 4. Central Type-II range

For a standard symmetric prime decomposition with cutoff near H, the genuinely bilinear central range has both factors at least H and at most H^2, i.e.

[
1le	hetale2.
]

Then
[
delta_H(	heta)
=
min(	heta-1,2-	heta)
lerac12.
]

The worst point is
[
	heta=rac32,
]
where
[
m,nasymp H^{3/2}
]
and
[
oxed{
delta_H=1/2.
}
]

Hence the standard DLS loss is only
[
oxed{H^{1/4}}
]
instead of the original atomic-prime loss H^{1/2}.

At the transition points
[
	heta=1
quad	ext{or}quad
	heta=2,
]
one cross partition is exactly balanced:
[
H^4	imes H^4.
]

Classification:
`J2_VAUGHAN_TYPEII_DLS_GAP_H1_4`.

## 5. Why this does not yet close j=2

The prime identity also has Type-I / endpoint pieces.

At
[
	heta	o0
]
the decomposition has
[
masymp1,qquad nasymp H^3,
]
and
[
delta_H(	heta)	o1.
]

Likewise at
[
	heta	o3.
]

Thus purely factor-scale DLS reproduces the original
[
H^{1/2}
]
loss at the atomic endpoint.

This is consistent with the existing permanent guard:
[
	exttt{HB_DEPTH_NOT_AUTOMATIC_PRODUCT_BALANCE}.
]

A prime identity does not by itself erase the prime obstruction.

## 6. New advantage of the Type-I endpoint

Although the endpoint remains imbalanced under **generic** DLS, it is no longer identical to the original prime variable.

In a Vaughan Type-I piece, the long factor n carries an integer/logarithmic convolution weight rather than an indivisible prime indicator.

For
[
nasymp H^{3-	heta},
]
with d,p,m frozen, the reciprocal phase as a function of n has normalized amplitude X=H^4 and

[
|f''(n)|
asymp
rac{H^4}{H^{2(3-	heta)}}
=
H^{-2+2	heta}.
]

The ordinary unweighted second-derivative benchmark gives

[
sum_{nasymp H^{3-	heta}} e(f(n))
ll
H^2+H^{1-	heta}.
]

Thus the pointwise integer benchmark is essentially
[
oxed{H^2}
]
throughout the Type-I range (	hetale1).

Relative to the trivial n-length (H^{3-	heta}), this contains a potential saving
[
H^{1-	heta}.
]

That saving is polynomially larger than the remaining DLS amplitude deficit
[
H^{(1-	heta)/2}.
]

However these two estimates cannot simply be multiplied: the curvature estimate and DLS may spend the same oscillation.

Therefore this is a **promising resource**, not a closure theorem.

Classification:
`J2_VAUGHAN_TYPEI_INTEGER_CURVATURE_RESOURCE`.

## 7. Correct next subproblem

The phase-adapted branch has now split into:

### Type I
Prove a hybrid estimate which preserves the outer d,p,m averaging while using the genuinely unweighted/logarithmic long n-variable curvature.

Target:
[
oxed{
	ext{recover at least }H^{-(1-	heta)/2}
}
]
beyond generic product DLS for (0le	heta<1).

### Type II
The factor-scale reduction already leaves only
[
oxed{H^{1/4}}
]
at worst.

The next task is to test whether:
- four-variable signed spacing;
- a second prime decomposition;
- or a legal B-process retaining the secondary phase

recovers this remaining H^{1/4}.

## 8. Methodological consequence

The original H^{1/2} j=2 deficit is not rigid under a prime decomposition.

It splits into two qualitatively different problems:

[
oxed{
egin{array}{c}
	ext{Type-I endpoint: integer-curvature transfer problem},\
	ext{Type-II center: reduced }H^{1/4}	ext{ multilinear spacing problem}.
end{array}
}
]

This is strictly more localized than the previous connected E2 covariance statement.

Permanent rules:
- `PRIME_DECOMPOSITION_BEFORE_SHORT_SIDE_CAUCHY`;
- `TYPEII_FACTOR_BALANCE_HALVES_J2_DEFICIT`;
- `TYPEI_CURVATURE_AND_DLS_SAVINGS_MUST_NOT_BE_MULTIPLIED_WITHOUT_A_HYBRID_PROOF`.

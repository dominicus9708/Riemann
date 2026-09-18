# j=2 Vaughan Type-II support collapse and H^(1/6) residual — 2026-09-19

## Status
- Riemann hypothesis: OPEN.
- Context: exact Vaughan decomposition with U=V=H, after identifying the separate-branch Type-II H^(1/4) DLS deficit and the exact Type-I/Type-II cancellation on H-rough semiprimes.
- New exact support result: on H<k<H^2, the restricted Möbius coefficient
  [
  b_H(k):=sum_{substack{dmid k\dle H}}mu(d)
  ]
  vanishes on every composite k having a prime factor >H.
- Therefore the nonzero composite Type-II support is H-smooth.
- Combining this support rigidity with divisor subset balance reduces the composite Type-II DLS imbalance from H^(1/4) to H^(1/6).
- The remaining prime-k piece is not an independent Type-II obstruction: for prime e it is the H-rough semiprime branch that cancels against the d=1 first-Type-I term.
- Classification: `J2_TYPEII_SUPPORT_COLLAPSE_TO_H1_6`.

## 1. Exact Vaughan Type-II coefficient

For q in the dyadic H^3 range, standard Vaughan gives the Type-II piece in the form
[
-sum_{substack{e>H, k>H\ekasymp H^3}}
Lambda(e),b_H(k),F(ek),
]
where
[
oxed{
b_H(k)=
sum_{substack{dmid k\dle H}}mu(d).
}
]

The sign is immaterial for a separate upper bound but important for inter-branch cancellation.

## 2. Support lemma for H<k<H^2

Assume
[
H<k<H^2.
]

Suppose k is composite and has a prime factor
[
P>H.
]

Since
[
k<H^2,
]
there can be at most one such prime factor.

Write
[
k=P^a u,
]
where every prime factor of u is <P and
[
u<rac{k}{P}<H.
]

If a>=2, then
[
P^2>H^2>k,
]
impossible. Hence a=1 and
[
k=Pu,
qquad
1<u<H
]
because k is composite.

Every divisor d of k with
[
dle H
]
is then a divisor of u: any divisor containing P exceeds H.

Therefore
[
b_H(k)
=
sum_{dmid u}mu(d).
]

Since
[
u>1,
]
the Möbius divisor identity gives
[
oxed{
b_H(k)=0.
}
]

Thus:
[
oxed{
H<k<H^2,quad
k	ext{ composite},quad
b_H(k)
e0
Longrightarrow
P^+(k)le H.
}
]

Classification:
`VAUGHAN_TYPEII_COMPOSITE_SUPPORT_IS_H_SMOOTH`.

## 3. Exceptional prime support

If k is prime and k>H, then its only divisor <=H is 1, so
[
oxed{b_H(k)=1.}
]

Hence the only H-rough support surviving in b_H on (H,H^2) is the prime support.

When e is also prime, q=ek is an H-rough semiprime and this Type-II term cancels pointwise with the d=1 term of the first Type-I branch, as proved in
`j2_vaughan_rough_composite_interbranch_cancellation_2026-09-19.md`.

Prime powers in the e-variable are treated separately; their support is sparse enough for standard DLS after L2 coefficient counting.

Permanent rule:
`ROUGH_TYPEII_SUPPORT_EQUALS_PRIME_K_PLUS_ZERO`.

## 4. Prime-power e is lower order for the DLS deficit

On a dyadic block
[
easymp E=H^	heta,
qquad
1le	hetale2,
]
the number of proper prime powers is
[
ll E^{1/2+o(1)}
=
H^{	heta/2+o(1)}.
]

Replacing a full E-length coefficient by this sparse support reduces its L2 mass by
[
H^{	heta/2-o(1)}
]
and hence the DLS amplitude by
[
H^{	heta/4-o(1)}.
]

The generic separate-branch Type-II loss is
[
H^{delta(	heta)/2},
qquad
delta(	heta)=min(	heta-1,2-	heta)le1/2.
]

But
[
rac{	heta}{4}
ge
rac{delta(	heta)}2
qquad(1le	hetale2).
]

Therefore the proper-prime-power e-subsector is already within
[
H^{6+arepsilon}.
]

The sharp residual may hence be restricted to e prime, up to harmless H^epsilon bookkeeping.

Classification:
`TYPEII_E_PRIME_POWER_SUBSECTOR_CLOSED`.

## 5. Smooth composite k: divisor-balance lemma

Now restrict to
[
kasymp H^kappa,
qquad
1lekappale2,
]
with
[
P^+(k)le H.
]

In the Type-II relation
[
ekasymp H^3,
]
write
[
easymp H^	heta,
qquad
kappa=3-	heta.
]

Define
[
	au:=2-	heta=kappa-1,
qquad
0le	aule1.
]

Factor
[
k=prod_i r_i,
qquad
lambda_i:=log_H r_ile1,
qquad
sum_ilambda_i=1+	au+o(1).
]

### Lemma
There exists a divisor
[
umid k,
qquad
uasymp H^t,
]
such that
[
oxed{|t-	au|le1/3+o(1).}
]

### Proof

If
[
0le	aule1/3,
]
take u=1. Then
[
|t-	au|=	aule1/3.
]

Assume
[
1/3<	aule1.
]

Take a partial product of atomic prime factors, in any fixed order, and stop at the first subset sum crossing tau.

Let s<tau be the previous logarithmic sum and let lambda be the next atomic exponent.

If
[
sge	au-1/3,
]
the previous divisor already works.

If
[
s+lambdale	au+1/3,
]
the new divisor works.

Otherwise
[
s<	au-1/3,
qquad
s+lambda>	au+1/3,
]
so
[
lambda>2/3.
]

Consider the complementary divisor obtained by omitting this single prime factor. Its exponent is
[
(1+	au)-lambda.
]

Because
[
2/3<lambdale1,
]
we have
[
	au
le
1+	au-lambda
<
	au+1/3.
]

Thus the complementary divisor works.

This proves the lemma.

The constant 1/3 is sharp: at
[
	au=1/3,
qquad
lambda_1=lambda_2=2/3,
]
the subset sums are
[
0, 2/3, 4/3,
]
whose nearest distance to tau=1/3 is exactly 1/3.

Classification:
`H_SMOOTH_TYPEII_DIVISOR_TARGET_ONE_THIRD`.

## 6. Product partition after the divisor choice

Write
[
k=uv,
qquad
uasymp H^t,
qquad
vasymp H^{kappa-t}.
]

The complete sharp j=2 factor exponents are now
[
oxed{
{2,3,	heta,t,3-	heta-t}.
}
]

Two complementary candidate partitions are
[
(deu)mid(pv)
]
and
[
(d e v)mid(pu),
]
depending on the side of tau on which t lies.

Since
[
	au=2-	heta,
]
the exponent of deu is
[
2+	heta+t
=
4+(t-	au).
]

Therefore the product-balance discrepancy satisfies
[
oxed{
Delta_Hle|t-	au|le1/3.
}
]

Standard two-product DLS consequently gives
[
oxed{
T_{II,mathrm{smooth comp}}
ll_arepsilon
H^{6+1/6+arepsilon}.
}
]

Thus the nonzero composite Type-II support has improved from the previous separate-branch worst bound
[
H^{6+1/4+arepsilon}
]
to
[
oxed{
H^{6+1/6+arepsilon}.
}
]

## 7. Sharp residual configuration

The divisor lemma is sharp at
[
	au=1/3,
qquad
	heta=5/3,
qquad
k=r_1r_2,
qquad
r_1,r_2asymp H^{2/3}.
]

Then the exponent multiset is
[
oxed{
left{
2, 3, rac53, rac23, rac23
ight}.
}
]

The nearest subset exponent to 4 is at distance
[
1/3.
]

Hence the H^(1/6) DLS loss is sharp within:
- exact Type-II support restriction;
- internal factor preservation of k;
- ordinary two-product DLS.

Classification:
`J2_TYPEII_H1_6_SHARP_AFTER_SUPPORT_COLLAPSE`.

## 8. Consequence for the global Vaughan map

After using inter-branch cancellation/support before taking absolute values:

1. first Type-I low blocks:
   [
   H^{6+arepsilon}
   quad	ext{CLOSED};
   ]

2. second Type-I high residual:
   [
   H^{6+1/6+arepsilon};
   ]

3. Type-II proper-prime-power e:
   [
   H^{6+arepsilon}
   quad	ext{CLOSED};
   ]

4. Type-II e-prime, k-prime rough-semiprime subfamily:
   exact cancellation with the first-Type-I unit branch;

5. Type-II e-prime, composite nonzero support:
   k is H-smooth and
   [
   H^{6+1/6+arepsilon}.
   ]

Therefore the previous H^(1/4) dominant residual is removed from the support-aware branch analysis.

The new branchwise frontier is
[
oxed{H^{1/6}.}
]

This is still an upper-bound deficit, not a lower bound for the full Vaughan sum.

Permanent priority:
`J2_SUPPORT_AWARE_H1_6_FRONTIER`.

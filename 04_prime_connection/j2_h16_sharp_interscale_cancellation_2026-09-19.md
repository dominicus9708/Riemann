# j=2 H^(1/6) sharp witnesses cancel across Vaughan scales — 2026-09-19

## Status
- Riemann hypothesis: OPEN.
- Context: after support-aware reduction, both the high second-Type-I branch and the smooth-composite Type-II branch have a sharp separate-block DLS loss H^(1/6).
- New exact calculation: the canonical sharp squarefree configuration realizing this H^(1/6) loss cancels exactly in the full Vaughan identity.
- Consequence: H^(1/6) is currently a **dyadic/branch triangle-inequality barrier**, not a demonstrated obstruction of the full prime sum.
- Classification: `J2_H1_6_SHARP_WITNESS_INTERSCALE_CANCELLATION`.

## 1. Sharp configuration

Take distinct primes
[
Pasymp H^{5/3},
qquad
r,sasymp H^{2/3},
]
and put
[
q=Prsasymp H^3.
]

Then:
- P>H;
- r,s<H;
- rsasymp H^{4/3}>H;
- Pr,Psasymp H^{7/3}>H^2.

This is exactly the exponent pattern
[
oxed{
left{
rac53,rac23,rac23
ight}
}
]
inside q which generated the support-aware H^(1/6) product-partition barrier.

Since q has three distinct prime factors,
[
Lambda(q)=0.
]

We now verify how this zero is assembled from the exact Vaughan branches.

## 2. First Type-I coefficient

The first Type-I coefficient at q is
[
A_1(q)
=
sum_{substack{dmid q\dle H}}
mu(d)log(q/d).
]

The divisors of q not exceeding H are exactly
[
1, r, s.
]

The divisor rs is >H, and divisors involving P are >H.

Therefore
[
egin{aligned}
A_1(q)
&=
log(Prs)
-log(Ps)
-log(Pr)\
&=
oxed{-log P}.
end{aligned}
]

## 3. Second Type-I coefficient cancels across its own dyadic k-scales

Write
[
a_H(k)
=
sum_{substack{de=k\dle H, ele H}}
Lambda(d)mu(e).
]

The second Type-I contribution is
[
-sum_{substack{kmid q\kle H^2}}a_H(k).
]

Relevant k-values include
[
r,quad s,quad rs.
]

We have
[
a_H(r)=log r,
qquad
a_H(s)=log s,
]
while
[
a_H(rs)
=
-log r-log s.
]

Hence
[
-a_H(r)-a_H(s)-a_H(rs)
=
-log r-log s+log r+log s
=
oxed{0}.
]

Thus the **high second-Type-I sharp block**
[
k=rsasymp H^{4/3}
]
is not an independent obstruction: its coefficient is cancelled exactly by the lower k=r and k=s blocks.

Classification:
`SECOND_TYPEI_H1_6_SHARP_BLOCK_CROSS_SCALE_CANCELLED`.

## 4. Type-II coefficient

For
[
k=rs,
]
the restricted Möbius coefficient is
[
b_H(rs)
=
1-1-1
=
-1,
]
because
[
1,r,sle H,
qquad
rs>H.
]

The only large von-Mangoldt divisor in the sharp factorization is
[
e=P.
]

The standard Vaughan Type-II term carries the sign
[
-Lambda(e)b_H(k).
]

Therefore
[
-Lambda(P)b_H(rs)
=
-(log P)(-1)
=
oxed{+log P}.
]

This cancels the first Type-I value:
[
A_1(q)+T_{II}(q)
=
-log P+log P
=
0.
]

Classification:
`TYPEII_H1_6_SHARP_BLOCK_CANCELLED_BY_FIRST_TYPEI`.

## 5. Full identity check

Combining:
[
A_1(q)=-log P,
]
[
T_{I,2}(q)=0,
]
[
T_{II}(q)=+log P.
]

Hence
[
oxed{
A_1(q)+T_{I,2}(q)+T_{II}(q)=0=Lambda(q).
}
]

The exact composite cancellation is recovered.

## 6. Meaning for the H^(1/6) frontier

The exponent pattern
[
left{
2, 3, rac53, rac23, rac23
ight}
]
is a genuine sharp pattern for **separate-block product DLS**.

But the canonical arithmetic realization of that pattern is annihilated by signed cross-scale Vaughan recombination.

Therefore one cannot use this pattern as a lower-barrier witness for the full q-sum.

Permanent correction:
[
oxed{
	ext{factor-scale sharpness}

e
	ext{full Vaughan-sum sharpness}.
}
]

## 7. General methodological consequence

All composite q satisfy
[
Lambda(q)=0.
]

Therefore any proposed hard subfamily supported only on composites must pass the following audit before being promoted to a true obstruction:

1. include every Vaughan branch that contributes to the same q;
2. include neighboring divisor/dyadic scales inside each branch;
3. recombine their signed coefficients;
4. only then test the analytic size.

The current H^(1/6) witnesses fail this test.

Permanent rule:
`COMPOSITE_FACTOR_SCALE_WITNESS_REQUIRES_FULL_VAUGHAN_RECOMBINATION`.

## 8. Updated live problem

The unresolved issue is no longer:

> can one improve the H^(1/6) DLS estimate on the isolated sharp factor block?

It is:

[
oxed{
	ext{Can the exact signed cross-scale Vaughan recombination be retained
through the reciprocal-phase spacing/B-process estimate?}
}
]

Equivalently, one needs an operator estimate which sees the factor coordinates for analytic balance while still preserving the coefficient-level null directions which annihilate composites.

This is a **signed multiscale spacing problem**, not an unsigned subset-partition problem.

Classification:
`J2_SIGNED_MULTISCALE_VAUGHAN_SPACING_OPEN`.

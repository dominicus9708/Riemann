# j=2 exact Vaughan bookkeeping at U=V=H — 2026-09-19

## Status
- Riemann hypothesis: OPEN.
- Context: globalize the phase-adapted q-decomposition after proving the low-Type-I B-process + DLS closure.
- Parameter:
  [
  qasymp Q=H^3,qquad U=V=H.
  ]
- Result: the exact Vaughan identity splits the q-sum into:
  1. a first Type-I family already closed by the B-process lemma;
  2. a second Type-I family whose preserved internal factorization leaves at most H^{1/6};
  3. a genuine Type-II family whose sharp product-partition deficit is H^{1/4}.
- Thus the dominant unresolved Vaughan branch is the central Type-II H^{1/4} residual.
- Classification: `J2_EXACT_VAUGHAN_GLOBAL_BOOKKEEPING`.

## 1. Exact identity

Use
[
Lambda
=
Lambda_{le V}
+
mu_{le U}*L
-
mu_{le U}*Lambda_{le V}*1
+
mu_{>U}*Lambda_{>V}*1.
]

Choose
[
U=V=H.
]

On the dyadic range
[
qasymp H^3,
]
the term
[
Lambda_{le H}(q)
]
vanishes identically.

Hence only the two Type-I convolutions and the Type-II convolution remain.

## 2. First Type-I: mu_{<=H} * L

This has dyadic pieces
[
q=mn,
qquad
mle H,
]
with
[
masymp H^	heta,
qquad
0le	hetale1,
]
and
[
nasymp H^{3-	heta}.
]

The n-variable is unrestricted apart from a logarithmic/smooth weight.

By the previous B-process + ratio/product DLS lemma,
[
oxed{
T_{I,1}(	heta)
ll_arepsilon
H^{6+arepsilon}
}
]
uniformly for
[
0le	hetale1.
]

Therefore
[
oxed{
T_{I,1}
ll_arepsilon
H^{6+arepsilon}.
}
]

Classification:
`VAUGHAN_FIRST_TYPEI_CLOSED`.

## 3. Second Type-I: mu_{<=H} * Lambda_{<=H} * 1

Write
[
q=bcn,
]
with
[
ble H,
qquad
cle H,
]
and coefficient
[
mu(b)Lambda(c)
]
up to the exact convolution convention.

Put
[
basymp H^eta,
qquad
casymp H^gamma,
qquad
0leeta,gammale1,
]
and
[
	heta:=eta+gamma.
]

Then
[
bcasymp H^	heta,
qquad
nasymp H^{3-	heta}.
]

### 3.1 Low second-Type-I: theta <=1

Collapse
[
m=bc.
]

The coefficient in m is divisor-bounded and the n-variable remains unrestricted.

Therefore the low-Type-I B-process lemma applies without requiring m to be prime or atomic:

[
oxed{
T_{I,2}(	heta)
ll_arepsilon
H^{6+arepsilon},
qquad
0le	hetale1.
}
]

Classification:
`VAUGHAN_SECOND_TYPEI_LOW_CLOSED`.

## 4. High second-Type-I: preserve b,c

Now
[
1le	hetale2.
]

The H-exponent multiset is
[
oxed{
{2,3,eta,gamma,3-	heta},
qquad
eta+gamma=	heta,
quad
0leeta,gammale1.
}
]

The self-dual target is exponent 4.

Three immediate candidate subsets give discrepancies

[
delta_1=	heta-1
]
from
[
d,n:
quad
2+(3-	heta)=5-	heta,
]

[
delta_2=2-	heta
]
from
[
d,b,c:
quad
2+	heta,
]

and, choosing
[
e=max(eta,gamma)ge	heta/2,
]
[
delta_3le1-	heta/2
]
from
[
p	imes(	ext{larger of }b,c):
quad
3+e.
]

Therefore
[
Delta_H
le
minleft(
	heta-1,
2-	heta,
1-rac	heta2
ight).
]

For
[
1le	hetale2,
]
the maximum of this upper envelope occurs at
[
	heta=rac43
]
and equals
[
oxed{rac13}.
]

Hence standard product DLS gives
[
oxed{
T_{I,2}^{m high}
ll_arepsilon
H^{6+1/6+arepsilon}.
}
]

## 5. Sharp high-Type-I configuration

Take
[
	heta=rac43,
qquad
eta=gamma=rac23.
]

Then
[
3-	heta=rac53,
]
and the exponent multiset is
[
oxed{
left{
2,3,rac23,rac23,rac53
ight}.
}
]

The nearest subset exponents to 4 are
[
3+rac23=rac{11}{3}
]
and
[
2+rac53=rac{11}{3},
]
together with complementary sums at (13/3).

Thus the distance is exactly
[
oxed{rac13}.
]

So the high second-Type-I DLS loss
[
oxed{H^{1/6}}
]
is sharp within pure factor preservation + standard two-product DLS.

Classification:
`VAUGHAN_SECOND_TYPEI_H1_6_PARTITION_BARRIER`.

## 6. Type-II term

The exact Type-II piece may be written in the standard form
[
q=e k,
]
with
[
e>H,
qquad
k>H,
qquad
ekasymp H^3,
]
and coefficients of the form
[
Lambda(e),b(k),
qquad
b(k)=sum_{substack{dmid k\dle H}}mu(d).
]

Hence on dyadic blocks
[
easymp H^	heta,
qquad
kasymp H^{3-	heta},
]
with
[
oxed{
1le	hetale2.
}
]

Treating e,k as the two arithmetic factors gives exactly the previous central Type-II scale map:
[
Delta_H
=
min(	heta-1,2-	heta)
lerac12,
]
with equality at
[
	heta=rac32.
]

Therefore
[
oxed{
T_{II}
ll_arepsilon
H^{6+1/4+arepsilon}
}
]
by standard product DLS, and the H^{1/4} loss is sharp within that class.

Classification:
`VAUGHAN_TYPEII_H1_4_PARTITION_BARRIER`.

## 7. Why the restricted Möbius coefficient does not automatically improve Type II

The coefficient
[
b(k)=sum_{substack{dmid k\dle H}}mu(d)
]
contains the unit divisor d=1.

For prime k>H,
[
b(k)=1.
]

Thus a coherent atomic subfamily survives in which no internal small-divisor cancellation is present.

Expanding b(k) may improve factorable k-subsectors, but cannot uniformly remove the sharp central obstruction.

Permanent guard:
`TYPEII_RESTRICTED_MOBIUS_UNIT_SUBFAMILY_PERSISTS`.

## 8. Global Vaughan map

At U=V=H the q-side decomposition is therefore:

[
oxed{
egin{array}{c|c}
	ext{Vaughan branch}&	ext{current bound}\
hline
mu_{le H}*L & H^{6+arepsilon} 	ext{CLOSED}\
mu_{le H}*Lambda_{le H}*1, 	hetale1
& H^{6+arepsilon} 	ext{CLOSED}\
mu_{le H}*Lambda_{le H}*1, 1<	hetale2
& H^{6+1/6+arepsilon} 	ext{OPEN residual}\
mu_{>H}*Lambda_{>H}*1
& H^{6+1/4+arepsilon} 	ext{OPEN residual}
end{array}
}
]

Therefore the dominant unresolved branch is
[
oxed{
	ext{central Vaughan Type II with missing }H^{1/4}.
}
]

## 9. Consequence

The original j=2 atomic-prime deficit
[
H^{1/2}
]
has been reduced, by an exact standard prime identity plus a proved low-Type-I B-process mechanism, to two smaller central residuals:

[
oxed{
H^{1/6}quad	ext{and}quad H^{1/4}.
}
]

The H^{1/4} Type-II piece dominates.

The next theorem search / derivation should therefore target the exact Type-II coefficient geometry
[
Lambda(e),b(k)
]
together with the outer variables
[
dasymp H^2,qquad pasymp H^3,
]
rather than returning to the full original prime-q sum.

Permanent priority:
`J2_CENTRAL_VAUGHAN_TYPEII_H1_4_FIRST`.

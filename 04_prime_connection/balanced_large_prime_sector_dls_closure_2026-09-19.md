# Balanced large-prime sectors (j=2,3): product-pair DLS closure — 2026-09-19

## Status
- Riemann hypothesis: OPEN.
- Context: bounded large-prime-tail decomposition at the Vaughan edge (V=K^{1/4}), (wasymp V^3), (dasymp V).
- New closures:
  - (j=3) sector: CLOSED at (V^{3+arepsilon}).
  - (j=2), residual (aasymp V) balanced endpoint: CLOSED at (V^{3+arepsilon}).
- Method: regroup the multiplicative variables into two product variables of scale (V^2), then apply the Bombieri--Iwaniec double large sieve with divisor-bounded product coefficients.

## 1. Exact structure of the (j=3) sector

Write
[
w=a p_1p_2p_3,
]
where all (p_i>V), (P^+(a)le V), and
[
V^3le wle2V^3.
]

Since
[
p_1p_2p_3>V^3,
]
if (age2) then
[
w>2V^3,
]
contradicting the dyadic support.

Hence
[
oxed{a=1.}
]

Moreover, if any (p_i>2V), then
[
p_1p_2p_3>2V^3,
]
again impossible. Therefore
[
oxed{V<p_ile2Vquad(i=1,2,3).}
]

Thus the (j=3) sector is not merely power-scale balanced; its three large primes are all genuinely (V)-scale.

## 2. Ordered-prime symmetrization

Because the Möbius support is squarefree, the three primes are distinct.

The phase and dyadic weight depend symmetrically on the product
[
p_1p_2p_3.
]

Therefore the unordered triple sum may be replaced by (1/6) times the sum over ordered triples of distinct primes, with diagonal equal-prime configurations absent.

This allows one prime to be assigned to the first product block without introducing a new arithmetic condition.

## 3. Balanced product variables

Set
[
x=dp_1,
qquad
y=p_2p_3.
]

Then
[
xasymp V^2,
qquad
yasymp V^2.
]

The original reciprocal phase
[
e!left(A(dp_1p_2p_3)^{-1/2}ight),
qquad Aasymp V^4,
]
becomes
[
e!left(Xu(x)v(y)ight),
qquad
X:=A/V^2asymp V^2,
]
with
[
u(x)=left(rac{x}{V^2}ight)^{-1/2},
qquad
v(y)=left(rac{y}{V^2}ight)^{-1/2}.
]

## 4. Product coefficients

Define schematically
[
A_x
=
sum_{substack{dp=x\dasymp V, pasymp V\p {m prime}}}
mu(d),
]
and
[
B_y
=
sum_{substack{p_2p_3=y\p_iasymp V\p_i {m prime}}}
1,
]
with smooth dyadic factors suppressed.

Then
[
|A_x|, |B_y|le	au(x),	au(y)
]
up to harmless fixed multiplicities.

Therefore
[
sum_{xasymp V^2}|A_x|^2
+
sum_{yasymp V^2}|B_y|^2
ll
V^2(log V)^{O(1)}.
]

## 5. Spacing

For (x,yasymp V^2),
[
u'(x),v'(y)asymp V^{-2}.
]

Since
[
X^{-1}asymp V^{-2},
]
the DLS proximity conditions
[
|u(x)-u(x')|lesssim X^{-1},
qquad
|v(y)-v(y')|lesssim X^{-1}
]
force
[
|x-x'|, |y-y'|ll1.
]

Thus the weighted spacing energies are
[
mathcal B_x,mathcal B_y
ll
V^2(log V)^{O(1)}.
]

## 6. (j=3) closure

Bombieri--Iwaniec double large sieve gives
[
|T_{j=3}|^2
ll
Xmathcal B_xmathcal B_y
ll
V^6(log V)^{O(1)}.
]

Hence
[
oxed{
T_{j=3}ll_arepsilon V^{3+arepsilon}.
}
]

Classification:
`J3_BALANCED_MULTIPRIME_DLS_CLOSED`.

## 7. (j=2) balanced endpoint

For (j=2), write
[
w=a p q,
qquad
p,q>V,
qquad
P^+(a)le V.
]

At the balanced endpoint
[
aasymp V,
]
the support (wasymp V^3) forces
[
pqasymp V^2.
]

Set
[
x=daasymp V^2,
qquad
y=pqasymp V^2.
]

After product collapse and, when needed, Mellin separation of the (apq/V^3) cutoff, both product coefficients are divisor-bounded. The same spacing calculation therefore yields
[
oxed{
T_{j=2, aasymp V}
ll_arepsilon
V^{3+arepsilon}.
}
]

Classification:
`J2_BALANCED_ENDPOINT_DLS_CLOSED`.

## 8. Updated sector map

The bounded-large-prime-tail front is now:

- (j=3): CLOSED.
- (j=2), (aasymp V): CLOSED.
- (j=2), (a=V^alpha, 0lealpha<1): OPEN asymmetric flank.
- (j=1), (aasymp V): CLOSED.
- (j=1), (0lealpha<1): OPEN long-prime flank.
- (j=1), (1<alphale2): OPEN long-smooth-Möbius flank.
- (j=0): OPEN smooth-Möbius sector.

## 9. Methodological consequence

The critical lesson is that a fixed number of original prime/factor variables should not be declared difficult merely because no **single** variable sits at the self-dual scale.

Before invoking new cancellation, test whether the multiplicative variables can be partitioned into two product groups each of scale
[
V^2=sqrt{V^4}.
]

If so, product coefficients may be divisor-bounded while the phase becomes a two-variable monomial exactly at the DLS self-dual scale.

Permanent rule:
`PRODUCT_PARTITION_BEFORE_NEW_CANCELLATION`.

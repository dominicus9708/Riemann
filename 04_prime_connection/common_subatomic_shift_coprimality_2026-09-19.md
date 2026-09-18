# Common subatomic-shift coprimality rigidity — 2026-09-19

## Status
- Riemann hypothesis: OPEN.
- Context: common centered-cell residual for the sharp (j=0), (j=1) long-smooth and (j=2) asymmetric prime-product subfamilies.
- Exact arithmetic observation: the natural DLS cell/shift length is smaller than every atomic prime factor on the long side.
- Therefore every nonzero near-shift pair of long-side products is coprime.
- Classification: `SUBATOMIC_SHIFT_COPRIMALITY_RIGIDITY`.

## 1. General lemma

Let
[
y=prod_{i=1}^k r_i,
qquad
y'=prod_{i=1}^k r'_i
]
be squarefree products, and suppose every prime factor satisfies
[
r_i,r_i'>H.
]

If
[
y-y'=h,qquad 0<|h|le H,
]
then
[
oxed{(y,y')=1.}
]

Proof:
if a prime (qmid(y,y')), then
[
qmid(y-y')=h.
]
But
[
q>Hge|h|>0,
]
which is impossible.

For (h=0), unique factorization gives the diagonal product equality, up to ordering of the same prime factors.

## 2. (j=0) sharp sector

Long side:
[
y=q_1q_2q_3,
qquad
q_iasymp V^{3/4}.
]

Natural cell length:
[
H=V^{1/4}.
]

Thus
[
q_i>H
]
by a polynomial factor, and every nonzero shifted pair
[
q_1q_2q_3-q'_1q'_2q'_3=h
]
is coprime across the two products.

In particular no prime can occur on both sides of an off-diagonal shifted correlation.

## 3. (j=1) long-smooth sharp sector

One long-side realization is
[
y=dq_1q_2,
]
with
[
dasymp V,qquad
q_iasymp V^{2/3}.
]

The natural cell length is
[
H=V^{1/3}.
]

Again every atomic prime factor exceeds (H), so every nonzero near-shift pair is coprime.

## 4. (j=2) sharp sector

Long side:
[
y=dp,
qquad
dasymp V,qquad
pasymp V^{3/2},
]
and
[
H=V^{1/2}.
]

Both prime scales exceed (H), so
[
dp-d'p'=h
e0
]
forces
[
(dp,d'p')=1
]
on the coherent-prime sharp subfamily.

The same conclusion persists after separating gcd factors in more general divisor-bounded (d,d') coefficients: any common prime exceeding (H) cannot divide a nonzero shift.

## 5. Consequence for dispersion

The residual cannot be treated as an arbitrary dense near-pair problem.

For every nonzero shift, all cross-side atomic factors are invertible modulo the factors on the opposite side.

Thus equations such as
[
ap-bp'=k
]
or
[
abc-a'b'c'=h
]
may be converted without exceptional shared-prime cases into reciprocal residue conditions, e.g.
[
pequiv kar apmod b,
]
or
[
aequiv h,overline{bc}pmod{a'}.
]

This is exactly the setting where Kloosterman-fraction / dispersion methods become natural.

## 6. What this does not prove

Coprimality does not by itself reduce the number of shifted pairs to diagonal scale.

Indeed the common cell-saturation lower bound already shows that many such near pairs can exist.

Therefore the lemma is a **structural simplification**, not the missing power saving.

Its value is that a future common residual theorem can be formulated entirely in a coprime reciprocal-residue geometry, without carrying shared-factor correction terms in the sharp nonzero-shift blocks.

## 7. Updated common residual target

The sharp open sectors now share:

1. product scales (V^{2-delta}	imes V^{2+delta});
2. cell length (H=V^delta);
3. coherent prime-product subfamilies saturating unsigned DLS cells;
4. mean-density contribution closed by reciprocal curvature;
5. nonzero centered shifted pairs automatically coprime.

Thus the remaining common mechanism is more specifically
[
oxed{
	ext{centered coprime shifted-product dispersion with reciprocal phases}.
}
]

Permanent rule:
`SUBATOMIC_SHIFT_COPRIMALITY_BEFORE_DISPERSION`.

# Common coherent-prime cell-saturation barrier — 2026-09-19

## Status
- Riemann hypothesis: OPEN.
- Context: common (j)-sector balance functional
[
Delta(mathcal E)=min_Sleft|sum_{ein S}e-2ight|,
qquad
Tll V^{3+Delta/2+arepsilon}
]
from standard two-product DLS.
- New result: in the sharp open sectors, the polynomial spacing excess (V^Delta) can be saturated by explicit coherent-sign prime-product subfamilies.
- Consequence: the residual factor (V^{Delta/2}) is not merely an artifact of divisor-bounded coefficient estimates.
- Classification: `COMMON_COHERENT_PRIME_CELL_SATURATION`.

## 1. Abstract cell-saturation principle

Suppose an admissible sharp subfamily admits an optimal two-product split
[
xasymp V^{2-delta},
qquad
yasymp V^{2+delta},
qquad
delta>0,
]
with normalized reciprocal parameter
[
Xasymp V^2.
]

Assume the long-side support (mathcal Y) consists of products of a fixed number (k) of primes in fixed dyadic ranges and has
[
|mathcal Y|=V^{2+delta-o(1)}.
]

For
[
v(y)=left(rac{y}{V^{2+delta}}ight)^{-1/2},
]
we have
[
|v'(y)|asymp V^{-2-delta}.
]

The DLS proximity condition
[
|v(y)-v(y')|lesssim X^{-1}asymp V^{-2}
]
corresponds to
[
|y-y'|lesssim V^delta.
]

Partition the long-side interval into cells of length (V^delta).
There are
[
Basymp V^{2+delta}/V^delta=V^2
]
cells.

If (n_b) is the occupancy of cell (b), then
[
sum_b n_b^2ge rac{|mathcal Y|^2}{B}
=
V^{2+2delta-o(1)}.
]

Thus the DLS long-side proximity energy is at least
[
oxed{V^{2+2delta-o(1)}}.
]

The diagonal scale is only
[
|mathcal Y|=V^{2+delta-o(1)}.
]

Hence the genuine spacing excess is
[
oxed{V^{delta-o(1)}}.
]

After the square root in the double large sieve this becomes
[
oxed{V^{delta/2-o(1)}},
]
which is exactly the common balance-functional loss.

## 2. Coherent Möbius sign

If the selected subfamily has a fixed number of prime factors in every Möbius block, then its Möbius sign is constant.

Consequently the spacing excess cannot be attributed to random sign cancellation that was lost by absolute values.

This yields a general audit principle:

> whenever a sharp sector contains a fixed-parity prime-product subfamily saturating the natural DLS cells, neither Möbius parity nor support sparsity can uniformly recover the factor (V^{Delta/2}).

## 3. (j=0)

Sharp subfamily:
[
dasymp V 	ext{prime},
qquad
q_1,ldots,q_4asymp V^{3/4} 	ext{prime}.
]

Take
[
x=dq_1asymp V^{7/4},
qquad
y=q_2q_3q_4asymp V^{9/4}.
]

Hence
[
delta=rac14.
]

The long-side cell width is
[
V^{1/4},
]
and the near-pair count is
[
V^{5/2-o(1)}.
]

The square-root spacing excess is
[
oxed{V^{1/8-o(1)}}.
]

Also
[
mu(d)mu(q_1q_2q_3q_4)=-1
]
throughout the subfamily.

Thus the (j=0) (V^{1/8}) residual is genuinely analytic.

## 4. (j=1) long-smooth sharp family

Take
[
dasymp V 	ext{prime},
quad
pasymp V^{5/3} 	ext{prime},
quad
q_1,q_2asymp V^{2/3} 	ext{prime}.
]

This is the sharp
[
alpha=rac43
]
configuration.

Use
[
x=pasymp V^{5/3},
qquad
y=dq_1q_2asymp V^{7/3}.
]

Thus
[
delta=rac13.
]

The DLS cell width is
[
V^{1/3},
]
the long-side near-pair count has scale
[
V^{8/3-o(1)},
]
and the square-root excess is
[
oxed{V^{1/6-o(1)}}.
]

The Möbius sign is again constant on this fixed-prime-count subfamily.

Hence the sharp (V^{1/6}) barrier cannot be removed by parity or support sparsity.

## 5. (j=2) asymmetric balanced-prime family

Take the endpoint (alpha=0):
[
a=1,qquad
dasymp V 	ext{prime},
qquad
p,qasymp V^{3/2} 	ext{prime}.
]

The best two-product split is
[
x=qasymp V^{3/2},
qquad
y=dpasymp V^{5/2},
]
up to symmetry.

Hence
[
delta=rac12.
]

The long-side cell width is
[
V^{1/2}.
]

The prime-product support has cardinality
[
V^{5/2-o(1)},
]
and the cell argument forces proximity energy
[
V^{3-o(1)}.
]

Thus the square-root excess is
[
oxed{V^{1/4-o(1)}},
]
exactly the ((1-alpha)/4) loss at (alpha=0).

Again the Möbius sign is fixed.

For general (alpha<1), the same mechanism tracks the sharp
[
delta=rac{1-alpha}{2}
]
family.

## 6. Consequence for a future common residual theorem

The common residual theorem cannot be of either form

[
	ext{extra Möbius parity cancellation}
]
or
[
	ext{prime-product support sparsity}.
]

The missing factor must use phase information discarded by the ordinary DLS proximity count.

The natural common target is therefore:

[
oxed{
	ext{recover }V^{-Delta/2}
	ext{ from signed oscillation between/among occupied DLS cells.}
}
]

Possible mechanisms:
- higher (A^rD) processes retaining the secondary phase;
- a multilinear spacing theorem with signed rather than unsigned proximity energy;
- a transform of the long arithmetic coefficient that separates a smooth density main term from an oscillatory residual.

Permanent guards:
- `COHERENT_PRIME_SUBFAMILY_PARITY_GUARD`.
- `DLS_CELL_SATURATION_GUARD`.
- `COMMON_RESIDUAL_MUST_USE_POST_SPACING_PHASE`.

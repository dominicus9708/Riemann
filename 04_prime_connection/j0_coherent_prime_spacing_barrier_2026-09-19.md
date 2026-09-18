# j=0 sharp coherent-prime spacing barrier — 2026-09-19

## Status
- Riemann hypothesis: OPEN.
- Context: pure smooth-Möbius sector (j=0), whose common two-product balance functional leaves a sharp (V^{1/8}) loss.
- New audit: an explicit five-prime subfamily has coherent Möbius sign and polynomially dense long-side spacing.
- Consequence: neither Möbius parity nor support sparsity can supply the missing (V^{1/8}) uniformly.
- Classification: `J0_COHERENT_PRIME_SPACING_BARRIER`.

## 1. Sharp prime subfamily

Take a narrow dyadic subfamily with
[
dasymp V,qquad d 	ext{prime},
]
and
[
q_1,q_2,q_3,q_4asymp V^{3/4},
qquad q_i 	ext{distinct primes},
]
chosen so that
[
a=q_1q_2q_3q_4asymp V^3.
]

Then
[
mu(d)=-1,qquad
mu(a)=(-1)^4=+1,
]
hence
[
oxed{mu(d)mu(a)=-1}
]
throughout the whole subfamily.

Therefore any closure mechanism that requires sign cancellation from Möbius parity is unavailable on this admissible part of the (j=0) sector.

Permanent guard:
`J0_MOBIUS_PARITY_NOT_UNIFORM_RESIDUAL_SOURCE`.

## 2. Standard best two-product partition

One sharp partition is
[
x=dq_1asymp V^{7/4},
qquad
y=q_2q_3q_4asymp V^{9/4}.
]

The normalized reciprocal phase has frequency parameter
[
Xasymp V^2.
]

On the long side
[
v(y)=left(rac{y}{V^{9/4}}ight)^{-1/2},
]
so
[
|v'(y)|asymp V^{-9/4}.
]

The DLS proximity condition
[
|v(y)-v(y')|lesssim X^{-1}asymp V^{-2}
]
therefore corresponds to
[
oxed{|y-y'|lesssim V^{1/4}}.
]

This is precisely the spacing multiplicity responsible for the common-balance loss
[
V^{(1/4)/2}=V^{1/8}.
]

## 3. Triple-prime support is not polynomially sparse at that resolution

Let (mathcal Y) be the set of distinct products
[
y=q_2q_3q_4
]
in a fixed narrow product interval of length (asymp V^{9/4}).

Unique factorization implies only (O(1)) ordered representations per distinct product. By the prime number theorem,
[
|mathcal Y|
asymp
rac{V^{9/4}}{(log V)^3}
]
up to fixed dyadic constants.

Partition the (y)-interval into cells of length
[
Delta=V^{1/4}.
]

The number of cells is
[
Basymp
rac{V^{9/4}}{V^{1/4}}
=
V^2.
]

If (n_b) denotes the number of elements of (mathcal Y) in the (b)-th cell, then Cauchy gives
[
sum_b n_b^2
ge
rac{|mathcal Y|^2}{B}.
]

Hence the number of ordered pairs lying in a common spacing cell is at least
[
oxed{
gg
rac{V^{5/2}}{(log V)^6}.
}
]

Every such pair satisfies
[
|y-y'|ll V^{1/4},
]
and hence contributes to the DLS long-side proximity energy.

Thus the long-side energy cannot be reduced to diagonal size
[
V^{9/4+o(1)}
]
using support cardinality or unique factorization alone.

The polynomial excess
[
V^{5/2}/V^{9/4}=V^{1/4}
]
is exactly the spacing excess whose square root gives the (V^{1/8}) DLS loss.

Permanent guard:
`J0_TRIPLE_PRIME_SUPPORT_SPARSITY_CANNOT_RECOVER_V18`.

## 4. Consequence

The (j=0) sharp residual cannot be closed uniformly by either:

1. Möbius sign cancellation — the five-prime subfamily has coherent sign;
2. product-support sparsity — triple-prime products are polynomially dense at the natural DLS cell scale.

Therefore the missing saving must come from a mechanism that preserves more information than the unsigned DLS proximity count.

The live possibilities are:
- signed/oscillatory cancellation among near-spacing pairs after differencing;
- a genuine higher-dimensional (A^rD) / spacing estimate;
- a prime-sensitive multilinear estimate for the coherent five-prime monomial sum.

This sharpens `METHOD-OPEN-29 / J0_SMOOTH_V18_RESIDUAL_OPEN`.

## 5. Relation to existing multiple-monomial theory

Sargos--Wu and later Cao--Zhai develop higher (A^rD) spacing methods for multiple monomial exponential sums. Their existence makes this the correct literature family to audit.

However no theorem has yet been verified in the present project whose hypotheses and explicit terms, when inserted at
[
V, V^{3/4},V^{3/4},V^{3/4},V^{3/4},
qquad X=V^2,
]
give the required (V^{3+arepsilon}) uniformly.

Do not mark the sector closed merely because a four-variable/multiple-monomial theorem is nontrivial.
The exact target remains the recovery of the full missing factor
[
V^{1/8}.
]

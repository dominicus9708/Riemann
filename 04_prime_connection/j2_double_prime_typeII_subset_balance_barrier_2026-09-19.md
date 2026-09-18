# j=2 double-prime Type-II subset-balance barrier — 2026-09-19

## Status
- Riemann hypothesis: OPEN.
- Context: after decomposing the short prime q before Cauchy, the central Type-II factor-scale map leaves at worst an H^{1/4} DLS loss.
- Question: does decomposing the other prime p as well remove this remaining product-partition imbalance?
- Result: no. In the central Type-II scale class the subset-balance discrepancy remains uniformly <=1/2 in H-exponent and this bound is sharp.
- Classification: `J2_DOUBLE_PRIME_TYPEII_H1_4_PARTITION_BARRIER`.

## 1. Two central prime factorizations

Write
[
p=r s,
qquad
q=m n,
]
with dyadic H-exponents
[
rasymp H^phi,
qquad
sasymp H^{3-phi},
]
and
[
masymp H^	heta,
qquad
nasymp H^{3-	heta}.
]

In the genuinely bilinear central ranges assume
[
1lephi,	hetale2.
]

Then all four prime-decomposition factors have exponents in [1,2].

Together with
[
dasymp H^2,
]
the exponent multiset is
[
oxed{
mathcal E
=
{2,phi,3-phi,	heta,3-	heta},
}
]
with total exponent 8.

The self-dual target is subset exponent 4.

## 2. Uniform 1/2 subset bound

Consider the pair
[
phi, 3-phi.
]

Since both lie in [1,2] and sum to 3, at least one belongs to
[
[3/2,2].
]

Call that exponent e.

Then the subset consisting of d and that one factor has exponent
[
2+ein[7/2,4].
]

Therefore
[
oxed{
Delta_H(mathcal E)le1/2.
}
]

The same conclusion follows from the q-pair.

Hence ordinary two-product DLS after decomposing both primes has at worst
[
oxed{H^{1/4}}
]
amplitude loss.

## 3. Sharp configuration

Take
[
phi=	heta=rac32.
]

Then
[
mathcal E
=
left{
2,rac32,rac32,rac32,rac32
ight}.
]

Subset sums nearest 4 are
[
2+rac32=rac72
]
and
[
rac32+rac32+rac32=rac92.
]

There is no subset sum in
[
(7/2,9/2).
]

Thus
[
oxed{
Delta_H=1/2
}
]
and the DLS loss
[
oxed{H^{1/4}}
]
is sharp within pure subset partition + standard two-product DLS.

Permanent rule:
`DOUBLE_TYPEII_FACTORING_DOES_NOT_BEAT_H1_4_PARTITION_BARRIER`.

## 4. Interpretation

The first prime decomposition is still useful:
[
H^{1/2}longrightarrow H^{1/4}
]
on the central Type-II range.

But a second decomposition of the other prime does not iterate this halving.

The obstruction is no longer an atomic-prime obstruction. It is a genuine five-factor subset-balance configuration.

Thus the remaining Type-II H^{1/4} must come from something beyond:
- further two-product regrouping alone;
- a second symmetric Vaughan factorization alone;
- divisor-moment bookkeeping alone.

Possible remaining resources:
1. signed four/five-variable spacing;
2. a B-process which retains the secondary phase;
3. factorability of d;
4. genuinely multilinear large sieve / Kloosterman input.

## 5. Relation to outer-d factorability

If d has a divisor near H, the factor exponent 2 can itself split near 1+1.

Then the sharp
[
{2,3/2,3/2,3/2,3/2}
]
configuration is no longer atomic and exact exponent-4 subsets may appear.

Therefore this H^{1/4} barrier is genuinely sharp only for the outer-d strata that remain poorly factorable, including the prime-d coherent subfamily already identified.

Permanent order:
[
oxed{
	ext{outer-d factorability}
ightarrow
	ext{prime decompositions}
ightarrow
	ext{multilinear residual}.
}
]

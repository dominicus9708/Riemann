# j=2 Vaughan rough-composite exact inter-branch cancellation — 2026-09-19

## Status
- Riemann hypothesis: OPEN.
- Context: exact Vaughan decomposition of the short prime q with U=V=H.
- Correction: a coherent prime-prime subfamily inside the central Type-II term is not an independent positive obstruction; on H-rough squarefree composites it cancels the first Type-I term pointwise.
- Interpretation: the remaining central H^{1/4} branch is a parity/sieving correction required to turn an easy all-integer logarithmic sum into actual prime support.
- Classification: `J2_VAUGHAN_ROUGH_COMPOSITE_EXACT_CANCELLATION`.

## 1. Vaughan identity on the rough sector

Use
[
Lambda
=
Lambda_{le H}
+
mu_{le H}*L
-
mu_{le H}*Lambda_{le H}*1
+
mu_{>H}*Lambda_{>H}*1.
]

Let q be squarefree and assume
[
P^-(q)>H.
]

On the dyadic range
[
qasymp H^3,
]
the first and second low-prime pieces simplify strongly.

First,
[
Lambda_{le H}(q)=0.
]

Second, the only divisor of q not exceeding H is 1, so
[
(mu_{le H}*L)(q)
=
mu(1)log q
=
oxed{log q}.
]

Third,
[
(mu_{le H}*Lambda_{le H}*1)(q)=0,
]
because q has no prime divisor at most H.

Thus on the squarefree H-rough sector:
[
Lambda(q)
=
log q
+
(mu_{>H}*Lambda_{>H}*1)(q).
]

## 2. Type-II coefficient on a rough squarefree composite

Write
[
q=p_1cdots p_j,
qquad
p_i>H,
]
with distinct primes.

For the Type-II convolution,
[
T_{II}(q)
=
sum_{substack{abc=q\a>H, b>H}}
mu(a)Lambda(b).
]

Because q is squarefree, a nonzero (Lambda(b)) requires b to be one of the prime factors p_i.

Fix
[
b=p_i.
]

Then a may be any **nonempty** product of a subset of the remaining j-1 primes; every such a automatically exceeds H.

Hence the contribution associated to p_i is
[
log p_i
sum_{emptyset
e Asubseteq{1,ldots,j}setminus{i}}
(-1)^{|A|}.
]

If
[
jge2,
]
then
[
sum_{emptyset
e Asubseteq[j-1]}(-1)^{|A|}
=
-1.
]

Therefore
[
T_{II}(q)
=
-sum_{i=1}^jlog p_i
=
oxed{-log q}.
]

Consequently,
[
oxed{
(mu_{le H}*L)(q)+T_{II}(q)=0
}
]
for every squarefree H-rough composite q with at least two prime factors.

## 3. Rough prime

If q itself is prime and q>H, there is no factorization
[
q=abc
]
with both a>H and b>H.

Thus
[
T_{II}(q)=0,
]
while
[
(mu_{le H}*L)(q)=log q.
]

Hence
[
oxed{
	ext{rough prime survives; rough composite cancels.}
}
]

This is exactly what the Vaughan identity must accomplish.

## 4. Consequence for the sharp central Type-II subfamily

At the sharp central scale
[
e,kasymp H^{3/2},
]
the subfamily with e and k prime produces
[
q=ek
]
as an H-rough semiprime.

Its Type-II coefficient is
[
-(log e+log k)
=
-log q,
]
which exactly cancels the first-Type-I coefficient (+log q).

Therefore it is incorrect to use this coherent prime-prime Type-II subfamily by itself as a lower-barrier witness for the **full Vaughan-decomposed q-sum**.

Permanent correction:
`TYPEII_COHERENT_SEMIPRIME_NOT_INDEPENDENT_BARRIER`.

## 5. What remains true

This exact cancellation does not close the central Type-II estimate by itself.

If the Vaughan branches are bounded separately, the Type-II term still has the H^{1/4} standard-DLS deficit.

If the branches are recombined completely, one simply returns to the original (Lambda(q)) coefficient.

Thus the new information is about **where the difficulty lives**:

[
oxed{
	ext{central Type-II}
=
	ext{parity/sieve correction to the easy Type-I integer sum}.
}
]

The remaining H^{1/4} should therefore be interpreted as the cost of preserving this branch cancellation while exploiting the reciprocal phase, not as an unsigned semiprime-density obstacle.

## 6. New candidate architecture

A potentially stronger route is to avoid the triangle inequality across Vaughan branches.

Instead, combine:
- the B-process representation of the first Type-I sum;
- the central Type-II correction;

before absolute values / DLS spacing energies are taken.

The target is to expose the exact rough-composite cancellation **inside the transformed representation**, leaving only prime/prime-power support and lower-factorability corrections.

This is a different problem from improving the Type-II bound in isolation.

Classification:
`J2_BRANCH_COUPLED_VAUGHAN_PARITY_ROUTE_OPEN`.

## 7. Audit guards

Permanent rules:
- `CHECK_INTER_BRANCH_CANCELLATION_BEFORE_COHERENT_SUBFAMILY_BARRIER`;
- `VAUGHAN_TYPEII_IS_PARITY_CORRECTION_NOT_STANDALONE_SEQUENCE`;
- `SEPARATE_BRANCH_BOUNDS_MAY_CREATE_ARTIFICIAL_H1_4_BARRIER`.

The existing H^{1/4} Type-II DLS bound remains a valid **separate-branch upper-bound deficit**, but not yet a proof that the full phase-adapted Vaughan architecture requires H^{1/4} of genuinely new cancellation.

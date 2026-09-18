# j=2 exact Vaughan tail-difference identity and signed-tail frontier — 2026-09-19

## Status
- Riemann hypothesis: OPEN.
- Context: support-aware j=2 Vaughan analysis after H^(1/4) and H^(1/6) sharp composite witnesses were shown to cancel in the full identity.
- New exact structural identity: the first two Vaughan branches combine into a full factorable convolution, while the Type-II branch is exactly its k>H tail. Their difference is the k<=H head, which collapses to Lambda_{>H} by the Möbius divisor identity.
- Consequence: the remaining analytic problem is a signed head-minus-tail operator estimate. Treating the tail separately creates the observed product-balance deficits.
- Classification: `J2_VAUGHAN_SIGNED_TAIL_OPERATOR_FRONTIER`.

## 1. Standard coefficient notation

Let
[
mu_{le H}(n)=mu(n)mathbf 1_{nle H},
qquad
Lambda_{le H}(n)=Lambda(n)mathbf 1_{nle H},
]
and
[
Lambda_{>H}=Lambda-Lambda_{le H}.
]

Let
[
L(n)=log n.
]

Since
[
L=Lambda*1,
]
the first Vaughan Type-I convolution is
[
mu_{le H}*L.
]

The second Type-I convolution is
[
mu_{le H}*Lambda_{le H}*1.
]

## 2. First two branches combine exactly

Subtracting the second Type-I convolution from the first gives
[
egin{aligned}
mu_{le H}*L
-
mu_{le H}*Lambda_{le H}*1
&=
mu_{le H}*(Lambda*1)
-
mu_{le H}*Lambda_{le H}*1\
&=
oxed{
mu_{le H}*Lambda_{>H}*1.
}
end{aligned}
]

Thus the first two branches are not independent analytic objects.

## 3. Restricted Möbius coefficient

Define
[
b_H(k)
=
(mu_{le H}*1)(k)
=
sum_{substack{dmid k\dle H}}mu(d).
]

Then
[
mu_{le H}*Lambda_{>H}*1
=
Lambda_{>H}*b_H.
]

The standard Vaughan Type-II term is exactly the part of this convolution with
[
k>H,
]
and enters with the opposite sign:
[
T_{II}
=
-sum_{substack{ek=n\e>H, k>H}}
Lambda(e)b_H(k).
]

Hence, for n>H,
[
T_{I,1}-T_{I,2}+T_{II}
=
sum_{substack{ek=n\e>H, kle H}}
Lambda(e)b_H(k).
]

## 4. The head collapses

If
[
kle H,
]
then every divisor of k also lies below H, so
[
b_H(k)
=
sum_{dmid k}mu(d)
=
egin{cases}
1,&k=1,\
0,&k>1.
end{cases}
]

Therefore the entire k<=H head is just
[
oxed{
Lambda_{>H}(n).
}
]

For n in the q~H^3 range,
[
n>H,
]
so
[
Lambda_{>H}(n)=Lambda(n).
]

Thus the exact Vaughan identity reduces to
[
oxed{
T_{I,1}-T_{I,2}+T_{II}
=
Lambda
}
]
on the working dyadic range, as required.

## 5. Interpretation of the Type-II branch

The Type-II term is not a standalone sequence.

It is
[
oxed{
-	ext{(the k>H tail of }Lambda_{>H}*b_H	ext{)}.
}
]

The combined Type-I contribution is the **full** convolution
[
Lambda_{>H}*b_H.
]

Their exact difference retains only the trivial Möbius head k=1.

Therefore every hard composite Type-II configuration must be audited as part of a head-tail cancellation before being treated as a genuine obstruction.

Permanent rule:
`TYPEII_IS_FACTORABLE_CONVOLUTION_TAIL`.

## 6. Why complete recombination is analytically useless by itself

If one recombines head and tail completely before applying any analytic estimate, the coefficient becomes
[
Lambda(n)
]
and all factor coordinates disappear.

If one estimates the tail separately by absolute-value DLS, the factor coordinates are preserved but the exact composite null directions are lost.

Thus the proof problem is an interpolation between two extremes:

[
oxed{
egin{array}{c}
	ext{full recombination: exact arithmetic cancellation, no factor geometry},\
	ext{full separation: factor geometry, lost signed cancellation}.
end{array}
}
]

The required new estimate must preserve enough of both.

## 7. Signed-tail operator formulation

Let (mathcal T_H) denote the reciprocal-phase operator applied to the factorable convolution
[
Lambda_{>H}*b_H.
]

Decompose
[
mathcal T_H
=
mathcal T_H^{m head}
+
mathcal T_H^{m tail},
]
according to
[
kle H
quad	ext{and}quad
k>H.
]

The target prime operator is
[
oxed{
mathcal T_H^{m head}
=
mathcal T_H-mathcal T_H^{m tail}.
}
]

The current separate-branch analysis controls:
- large parts of (mathcal T_H) by B-process + DLS;
- (mathcal T_H^{m tail}) by support-aware factor DLS up to an H^(1/6) residual.

But the sharp H^(1/6) witnesses lie in directions where
[
mathcal T_H
quad	ext{and}quad
mathcal T_H^{m tail}
]
cancel exactly before absolute values.

Hence the missing theorem should be stated as a **signed difference norm bound**, not as a stronger unsigned tail bound.

Classification:
`SIGNED_HEAD_MINUS_TAIL_OPERATOR_OPEN`.

## 8. Relation to sieve parity

The algebraic collapse
[
b_H(k)=delta_{k,1}
qquad(kle H)
]
is an exact Möbius inclusion-exclusion statement.

Thus the current obstruction has the character of a phase-sensitive parity problem:

- exact inclusion-exclusion isolates primes;
- unsigned factor estimates lose the cancellation;
- a successful analytic argument must use oscillation while the inclusion-exclusion signs are still present.

This is not a claim that the classical sieve parity barrier formally proves impossibility.

It is a classification of the current mechanism:
[
oxed{
	ext{phase-sensitive signed sieve tail}.
}
]

## 9. Next analytic target

The next candidate theorem should control directly
[
mathcal T_H-mathcal T_H^{m tail}
]
or an equivalent smooth signed truncation, with the reciprocal phase retained.

Promising frameworks to compare:
1. well-factorable / triply-well-factorable dispersion;
2. a signed multiscale Gram operator;
3. Kloosterman completion after head-tail cancellation rather than before it;
4. a smooth sieve weight replacing the sharp k=H cut while preserving exact reconstruction up to a controllable error.

Permanent priority:
`J2_SIGNED_VAUGHAN_TAIL_BEFORE_ABSOLUTE_VALUES`.

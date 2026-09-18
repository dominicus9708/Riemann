# Heath--Brown all-unit sector: exact low-(Omega) persistence — 2026-09-19

## Status
- Riemann hypothesis: OPEN.
- Context: long-prime flank after testing whether cancellation between different Heath--Brown identity depths could remove the difficult prime component.
- Exact result: the sector in which every truncated Möbius variable equals (1) recombines explicitly.
- For every integer (n) with (Omega(n)<k), this all-unit sector equals (Lambda(n)) exactly.
- In particular it preserves the full prime weight (log p) on every prime.
- Consequence: fixed-depth Heath--Brown cross-(j) recombination does not automatically cancel the prime-support obstruction.
- Classification: `HB_ALL_UNIT_LOW_OMEGA_PERSISTENCE`.

## 1. Convolution form

Use the standard fixed-(k) Heath--Brown identity
[
Lambda
=
sum_{j=1}^{k}
(-1)^{j-1}inom{k}{j}
mu_{le z}^{*j}
*
mathbf 1^{*(j-1)}
*
L,
]
on the valid finite range, where
[
L(n)=log n
]
and (z^k) dominates the summation range.

Write
[
mu_{le z}=delta_1+
u,
]
where (delta_1) is supported at (1).

## 2. All-unit sector

Choose (delta_1) from every one of the (j) Möbius factors.

The sum over all identity depths is
[
Q_{k,0}
=
sum_{j=1}^{k}
(-1)^{j-1}inom{k}{j}
mathbf1^{*(j-1)}*L.
]

This is the exact cross-(j) recombination of the all-unit truncated-Möbius sectors.

## 3. Dirichlet-series calculation

For (Re s>1),
[
mathcal D[mathbf1](s)=zeta(s),
qquad
mathcal D[L](s)=-zeta'(s).
]

Therefore
[
mathcal D[Q_{k,0}](s)
=
-zeta'(s)
sum_{j=1}^{k}
(-1)^{j-1}inom{k}{j}zeta(s)^{j-1}.
]

Using
[
sum_{j=1}^{k}
(-1)^{j-1}inom{k}{j}z^{j-1}
=
rac{1-(1-z)^k}{z},
]
we obtain
[
oxed{
mathcal D[Q_{k,0}](s)
=
-rac{zeta'(s)}{zeta(s)}
left[1-(1-zeta(s))^kight].
}
]

Equivalently,
[
Q_{k,0}
=
Lambda
-
Lambda * c_k,
]
where (c_k) is the coefficient sequence of
[
(1-zeta(s))^k.
]

## 4. Support of the correction

We have
[
1-zeta(s)
=
-sum_{nge2}n^{-s}.
]

Hence the coefficient (c_k(n)) is supported only on integers that can be represented as
[
n=n_1cdots n_k,
qquad n_ige2.
]

This requires
[
Omega(n)ge k,
]
where (Omega) counts prime factors with multiplicity.

Conversely, any integer with (Omega(n)ge k) can have its prime factors grouped into (k) factors (>1), so this is the exact natural support threshold.

Thus if
[
Omega(n)<k,
]
then every divisor of (n) also has (Omega<k), and the convolution correction vanishes.

Therefore
[
oxed{
Omega(n)<k
quadLongrightarrowquad
Q_{k,0}(n)=Lambda(n).
}
]

## 5. Prime consequence

For every prime (p),
[
Omega(p)=1.
]

Hence for every fixed (kge2),
[
oxed{
Q_{k,0}(p)=Lambda(p)=log p.
}
]

So the all-unit sector retains the complete prime signal.

More generally, it retains (Lambda(n)) on all integers with fewer than (k) prime factors counted with multiplicity.

## 6. Audit consequence

The hope
[
	ext{alternating Heath--Brown depths}
Longrightarrow
	ext{automatic cancellation of the difficult all-unit prime block}
]
is false.

Increasing fixed (k) does not remove this sector. It enlarges the low-(Omega) region on which the all-unit recombination agrees exactly with (Lambda).

This does not make Heath--Brown's identity useless: the non-unit sectors can still expose multilinear factorization that is valuable for Type I/II/III estimates.

But one cannot credit the alternating binomial coefficients alone with cancellation of the original prime obstruction.

Permanent guard:
`HB_ALL_UNIT_PRIME_PERSISTENCE_GUARD`.

## 7. Consequence for long-prime flank

The representative three-variable block found in the previous audit cannot be dismissed by saying that summing over (j) will necessarily cancel the prime contribution.

Any successful fixed-depth Heath--Brown strategy must instead:
1. estimate the all-unit / low-(Omega) component by a genuinely prime-sensitive oscillatory argument; or
2. combine it with non-unit sectors through an identity that uses more than the formal alternating coefficients.

Thus the long-prime flank remains OPEN, but its remaining difficulty is now more sharply localized.

## References
- Heath--Brown generalized Vaughan identity, fixed-(k) convolution form.

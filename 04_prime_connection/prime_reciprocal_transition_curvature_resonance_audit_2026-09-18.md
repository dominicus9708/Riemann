# Prime reciprocal transition: curvature/resonance audit — 2026-09-18

## Status
- Riemann hypothesis: OPEN.
- Active subproblem: the (j=1) ordered-large-prime transition
[
S(P,C)=sum_{P<nle2P}Lambda(n)e(Cn^{-1/2}),
qquad Casymp P^{3/2}.
]
- Required scale in the current Vaughan-edge module:
[
|S(P,C)|ll_arepsilon P^{1/2+arepsilon}.
]
- Unweighted integer curvature benchmark reaches (P^{1/2}), but this does **not** transfer to prime weights.
- Direct theorem at the required square-root scale: NOT IDENTIFIED.
- Current 2026 pointwise linear-prime theorem is insufficient when used as a black box.
- Finite data are compatible with the target but also with random-prime scale and are not evidence.

## 1. Derivative geometry

Let
[
f(x)=Cx^{-1/2},qquad C=cP^{3/2},
]
where (c) lies in a fixed compact positive interval.

Then on (xasymp P),
[
f'(x)=-rac C2x^{-3/2}asymp1,
]
[
f''(x)=rac{3C}{4}x^{-5/2}asymp P^{-1},
]
and
[
f'''(x)asymp P^{-2}.
]

Hence the total variation of the derivative across a dyadic interval is
[
Delta f'asymp Pcdot P^{-1}=O(1).
]

Therefore the number of **integer** derivative resonances
[
f'(x)=m,qquad minmathbb Z,
]
is bounded by a constant depending only on the dyadic amplitude constants.

This explains the ordinary B-process scale: each stationary integer contributes at most order (P^{1/2}), and there are only (O(1)) such stationary integers.

## 2. Why this does not solve the prime-weighted sum

For the unweighted sum
[
sum_{P<nle2P}e(f(n)),
]
the second derivative test gives
[
ll Pcdot P^{-1/2}+P^{1/2}
ll P^{1/2}.
]

For
[
sumLambda(n)e(f(n)),
]
the coefficient (Lambda(n)) is not a smooth bounded amplitude. Partial summation against the unconditional PNT error does not retain the (P^{1/2}) scale: the classical PNT error is still much larger than (P^{1/2}).

Likewise, applying Vaughan's identity creates:
- Type-I pieces whose inner unweighted reciprocal sums may be (O(P^{1/2})), but whose outer divisor sums reintroduce polynomial loss if taken absolutely;
- Type-II pieces that re-enter a bilinear spacing problem.

Thus
[
oxed{	ext{unweighted curvature }P^{1/2}
otRightarrow
	ext{prime-weighted }P^{1/2}.}
]

Permanent guard:
`PRIME_WEIGHT_CURVATURE_TRANSFER_GUARD`.

## 3. Rational-frequency issue

Integer stationary points are not the only arithmetic obstruction for primes.

Prime exponential sums can have large linear Fourier coefficients near rationals (a/q) of small denominator. Since (f'(x)) sweeps through a fixed (O(1)) frequency interval, it also sweeps through many rational frequencies.

Thus a proof must control a **curved traversal of major and minor arcs**, not only the bounded set of integer B-process stationary points.

This gives a more accurate formulation of the transition:
[
oxed{	ext{prime reciprocal transition}
=
	ext{curved frequency sweep through prime major/minor arcs}.}
]

## 4. Benchmark against the 2026 linear-prime theorem

Maynard--Pandey--Radziwiłł (2026) prove for
[
alpha=a/q+epsilon,qquad qle N^{1/2},
]
with
[
B=max(q,qN|epsilon|),
]
the pointwise linear bound
[
left|sum_{n<N}Lambda(n)e(nalpha)ight|
le
N^{o(1)}
left(
rac N{sqrt B}+N^{19/24}
ight).
]

The generic floor (N^{19/24}) is much larger than (N^{1/2}).

Therefore local linearization of the reciprocal phase followed by this pointwise theorem cannot by itself prove the required transition estimate. A successful use would have to exploit **averaging across the continuously changing local frequencies**, not apply the pointwise bound independently on each block.

Classification:
`LINEAR_PRIME_POINTWISE_FLOOR_NOT_TRANSITION_CLOSURE`.

## 5. Natural local scale

Because
[
f''asymp P^{-1},
]
the phase changes its local frequency by approximately one Fourier-resolution unit over a spatial interval
[
Rasymp P^{1/2}.
]

Indeed:
[
Delta f'asymp f''Rasymp P^{-1/2},
]
while a length-(R) interval has additive Fourier resolution
[
R^{-1}=P^{-1/2}.
]

Thus the dyadic interval naturally contains
[
Jasymp P/R=P^{1/2}
]
critical packets whose frequency centers are separated by essentially their own Fourier width.

This exact matching is the prime analogue of the earlier reciprocal self-dual geometry.

It suggests that any successful estimate must exploit a **time-frequency almost-orthogonality with arithmetic prime coefficients**, not merely a single-frequency estimate.

Classification:
`PRIME_RECIPROCAL_PACKET_SELFDUALITY`.

## 6. Finite false-control audit

Computed
[
R_Lambda(P,c)
=
rac{|S(P,cP^{3/2})|}{sqrt P}
]
for
[
P=10^4,5cdot10^4,10^5,2cdot10^5,4cdot10^5
]
and
[
c=0.5,1,2,3,4,6.
]

Observed values range roughly from (0.32) to (7.68).

No monotone growth larger than a slowly varying factor is visible in this range. This is compatible with the desired (P^{1/2+arepsilon}) scale.

However it is equally compatible with a random-prime heuristic of size
[
sqrt{Plog P},
]
since (sqrt{log P}) is only a modest constant in the tested range.

The unweighted integer control behaves very differently:
- when the derivative interval contains no integer stationary point, the normalized integer sum is often (10^{-3})–(10^{-2});
- when one or two integer stationary points occur, it is (O(1)) after division by (sqrt P).

Thus the finite comparison itself confirms that prime weighting changes the problem qualitatively.

Data:
`data/mertens/prime_reciprocal_transition_audit_2026-09-18.csv`.

## 7. Next exact frontier

The next route should not try to sharpen the ordinary second-derivative test.

It should ask whether the (Jasympsqrt P) local packets, whose Fourier centers tile a fixed frequency interval at spacing (P^{-1/2}), admit an arithmetic mean-value inequality stronger than applying the 2026 pointwise prime bound packet-by-packet.

A useful target is a packetized inequality of schematic form
[
sum_{jle J}
left|
sum_{nin I_j}Lambda(n)
,e(alpha_j n),W_j(n)
ight|^2
ll_arepsilon
P^{1+arepsilon},
]
combined with the actual stationary-phase coefficients linking the packets.

But an (L^2) estimate alone followed by Cauchy would still lose (J^{1/2}=P^{1/4}). Therefore any claim of closure must preserve the phases connecting neighboring packets or exhibit an additional signed/arithmetic structure.

Permanent warning:
`PACKET_L2_CAUCHY_P14_LOSS`.

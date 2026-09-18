# j=2 outer-Möbius factorability stratification — 2026-09-19

## Status
- Riemann hypothesis: OPEN.
- Sector: j=2, alpha=0, with d~V, p,q~V^{3/2}.
- Purpose: refine the sharp V^{1/4} barrier by preserving internal factorization of the outer Möbius variable d before treating it as atomic.
- Classification: `J2_OUTER_FACTORABILITY_STRATIFICATION`.

## 1. H normalization

Set
[
H:=V^{1/2}.
]

Then
[
dasymp H^2,
qquad
p,qasymp H^3,
]
and the full reciprocal product scale is (H^8), with self-dual product length (H^4).

## 2. Divisor-balance discrepancy

For a squarefree (dasymp H^2), define
[
oxed{
sigma_H(d)
:=
min_{umid d}
left|log_H u-1ight|.
}
]

Write a selected divisor as
[
uasymp H^t,
qquad
d/uasymp H^{2-t}.
]

Instead of keeping d atomic, use the cross partition
[
(up) ig| ((d/u)q).
]

The two product lengths are
[
H^{3+t}
qquad	ext{and}qquad
H^{5-t}.
]

Their distance from the self-dual exponent 4 is
[
|t-1|.
]

In the V-exponent convention of the common balance functional,
[
Delta_d
=
rac12 |t-1|.
]

Minimizing over divisors gives
[
oxed{
Delta_d=rac12sigma_H(d).
}
]

Hence the standard two-product DLS loss for this d-stratum is
[
oxed{
H^{sigma_H(d)/2}
=
V^{sigma_H(d)/4}.
}
]

At the sector level, after dyadic/canonical divisor selection and divisor-bounded multiplicity bookkeeping, the corresponding target scale is
[
T_{j=2,d	ext{-stratum}}
ll_arepsilon
H^{6+sigma/2+arepsilon}.
]

Classification:
`J2_DIVISOR_BALANCE_REFINEMENT`.

## 3. Cell length also shrinks

For imbalance
[
Delta_d=sigma/2
]
in V-units, the common DLS cell length is
[
V^{Delta_d}
=
V^{sigma/2}
=
oxed{H^sigma}.
]

Thus the old H-long shift range is only the maximally atomic case (sigma=1).

More generally:
[
oxed{
H_{m cell}(d)=H^{sigma_H(d)}.
}
]

The amplitude-level DLS excess is
[
H_{m cell}^{1/2}=H^{sigma/2},
]
so the centered variance theorem must recover exactly
[
oxed{
H_{m cell}^{-1}=H^{-sigma}
}
]
relative to the raw local cell mass.

This interpolates continuously between:
- (sigma=0): balanced, no residual;
- (0<sigma<1): shorter residual shift;
- (sigma=1): atomic prime-type worst case, original H-shift and H^{-1} variance saving.

## 4. Prime d is the exact sharp endpoint

If d is prime and (dasymp H^2), its only divisors are 1 and d.

Therefore
[
sigma_H(d)=1+o(1),
]
and
[
Delta_d=rac12+o(1).
]

This recovers the sharp original loss
[
H^{1/2}=V^{1/4}.
]

Hence the common j=2 sharp barrier is genuinely realized by the atomic-prime outer-d subfamily; it is not only an artifact of refusing to factor a generic composite d.

Permanent guard:
`PRIME_D_REALIZES_J2_SHARP_BARRIER`.

## 5. Balanced composite d closes

If d has a divisor
[
u=H^{1+o(1)},
]
then
[
sigma_H(d)=o(1),
]
and the product split
[
(up)mid((d/u)q)
]
is self-dual up to (H^{o(1)}).

Therefore this factorable d-subsector is already closed at
[
H^{6+arepsilon}=V^{3+arepsilon}
]
by standard product DLS.

This removes a large class of composites from the determinant-shell residual before any new prime-correlation estimate is invoked.

Permanent rule:
`OUTER_DIVISOR_BALANCE_BEFORE_DETERMINANT_DISPERSION`.

## 6. Smooth-factor greedy lemma

Suppose every prime factor r of d satisfies
[
rle H^eta.
]

Write
[
d=prod_i r_i,
qquad
lambda_i:=log_H r_ileeta,
qquad
sum_ilambda_i=2+o(1).
]

Multiply factors greedily until the logarithmic partial sum first crosses 1.

If the previous partial sum is s<1 and the next increment is at most eta, then one of the two adjacent subset sums lies within eta of 1.

Hence
[
oxed{
P^+(d)le H^eta
quadLongrightarrowquad
sigma_H(d)leeta+o(1).
}
]

Consequently an (H^eta)-smooth outer d has at most
[
H^{eta/2+o(1)}
]
DLS loss.

For a final (H^arepsilon)-allowance, choose the smooth threshold with eta small in terms of epsilon; this sector is absorbed into the standard (H^{6+arepsilon}) bound.

Classification:
`SMOOTH_OUTER_D_BALANCE_CLOSED`.

## 7. Finite ordered-prime residual

The contrapositive of the greedy lemma is useful:

if
[
sigma_H(d)>eta,
]
then
[
P^+(d)>H^eta.
]

Peeling all prime factors larger than (H^eta) yields only (O_eta(1)) factors because their logarithmic exponents sum to 2.

Thus, after removing the smoothly factorable part, the remaining outer-d obstruction reduces to a finite ordered-large-prime exponent pattern plus an (H^eta)-smooth residual.

This means the true j=2 residual does not require treating an arbitrary Möbius coefficient as an indivisible block.

It can be refined into finitely many factor-scale sectors, each governed first by the same subset-balance functional.

Classification:
`J2_OUTER_ORDERED_PRIME_REDUCTION`.

## 8. Consequence for the determinant-shell route

The determinant-shell normalization
[
D=H^2,quad P=H^3,quad |k|lesssim H
]
should now be reserved for the (sigmaapprox1) atomic end of the outer-d spectrum.

For a general factorability stratum (sigma), the natural residual shift length is only
[
|k|lesssim H^sigma.
]

Therefore the next dispersion audit should proceed in this order:

1. factor d before declaring the j=2 block asymmetric;
2. compute (sigma_H(d));
3. close (sigma=o(1)) sectors by balanced DLS;
4. for fixed positive (sigma), use the reduced shift length (H^sigma);
5. treat the (sigmaapprox1) atomic/prime-like sector as the genuine worst determinant-shell problem.

Permanent rules:
- `COMMON_BALANCE_FUNCTIONAL_INCLUDES_OUTER_D_FACTORS`.
- `RESIDUAL_SHIFT_LENGTH_IS_H_TO_SIGMA`.
- `ATOMIC_D_FIRST_FOR_WORST_CASE_DISPERSION`.

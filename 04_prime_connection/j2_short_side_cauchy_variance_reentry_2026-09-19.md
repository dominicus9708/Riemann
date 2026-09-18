# j=2 short-side Cauchy forces variance re-entry — 2026-09-19

## Status
- Riemann hypothesis: OPEN.
- Context: phase-adapted alternative to the full centered-variance route for the sharp j=2 sector.
- Result: applying Cauchy / a one-sided large sieve to the short prime-product side first inevitably collapses the problem back to the long E2 centered-variance problem.
- Consequence: any genuinely weaker phase-adapted route must preserve the short-side off-diagonal structure until after a multilinear transformation.
- Classification: `J2_SHORT_SIDE_CAUCHY_VARIANCE_REENTRY`.

## 1. Sharp bilinear form

At the sharp endpoint use
[
H=V^{1/2},
qquad
D=H^2,
qquad
P=H^3,
qquad
X=H^4.
]

The optimized two-product split has schematic form
[
T
=
sum_{qasymp P}eta_q
sum_{yasymp DP} a_y,
e!left(X,u(q/P),v(y/(DP))ight),
]
where
[
qasymp H^3,qquad
y=dpasymp H^5.
]

The target is
[
Tll_arepsilon H^{6+arepsilon}=V^{3+arepsilon}.
]

Standard two-product DLS leaves
[
H^{1/2}=V^{1/4}
]
too much.

## 2. Short-side frequency spacing is sub-integer

For
[
u(q/P)asymp (q/P)^{-1/2},
]
we have
[
u'(q)asymp P^{-1}=H^{-3}.
]

The DLS frequency resolution is
[
X^{-1}=H^{-4}.
]

Thus
[
|u(q)-u(q')|lesssim X^{-1}
]
forces
[
|q-q'|
lesssim
P/X
=
H^{-1}.
]

Since q and q' are integers,
[
oxed{q=q'.}
]

Therefore the short side is already perfectly separated at the natural reciprocal resolution.

## 3. What Cauchy does

If one Cauchy-squares in q before exploiting the joint arithmetic phase, one obtains an expression controlled by
[
sum_{qasymp P}
left|
sum_{yasymp H^5}
a_y e(Xu_qv_y)
ight|^2.
]

Expanding the square gives
[
sum_{y,y'}
a_yoverline{a_{y'}}
sum_{qasymp P}
e!left(Xu_q(v_y-v_{y'})ight).
]

The q-sum is large only when
[
|v_y-v_{y'}|lesssim X^{-1}.
]

Since
[
v'(y)asymp (DP)^{-1}=H^{-5},
]
this becomes
[
|y-y'|
lesssim
rac{DP}{X}
=
H.
]

Thus the long-side pairs are exactly the natural E2 cell pairs:
[
oxed{|dp-d'p'|lesssim H.}
]

This is precisely the centered-variance / determinant-shell problem already isolated.

## 4. Variance re-entry theorem

Hence, schematically,
[
oxed{
	ext{Cauchy in }q
Longrightarrow
	ext{long-side E2 short-shift energy at length }H.
}
]

No later manipulation can claim to have avoided the variance route once the q-off-diagonal has been discarded.

Permanent rule:
`SHORT_SIDE_CAUCHY_FORCES_VARIANCE_REENTRY`.

## 5. One-cell phase variation is only order one

Inside a single long-side arithmetic cell
[
|y-y_0|lesssim H,
]
the phase increment is
[
X,|v'(y_0)|,H
asymp
H^4cdot H^{-5}cdot H
asymp1.
]

Therefore the original reciprocal phase does not oscillate through a polynomial number of cycles **inside one DLS cell**.

Consequently:
[
oxed{
	ext{internal cell phase alone cannot supply a full polynomial }H	ext{-saving}.
}
]

Any phase-adapted improvement must use interference **between many cells / multiple arithmetic variables**, not merely a sharper treatment of one occupied cell.

Permanent rule:
`ONE_CELL_PHASE_VARIATION_O1_NO_POLYNOMIAL_GAIN`.

## 6. Structural consequence for Branch P

A phase-adapted route that is genuinely weaker than full centered variance must avoid all of the following before the new cancellation has been extracted:

1. Cauchy in q;
2. one-sided large sieve in q;
3. absolute-value summation over q packets;
4. replacing q by an already-diagonal frequency energy.

Instead it must preserve q together with d and p in a multilinear form.

The next legal operations are therefore of the type:
- Vaughan / Heath--Brown decomposition of the prime q **before Cauchy**;
- a joint 3- or 4-variable spacing theorem;
- a B-process / Poisson transform that keeps the q-generated secondary phase;
- a bilinear Kloosterman form derived only after the new factorization variables have been retained.

Classification:
`PHASE_ROUTE_MUST_PRESERVE_SHORT_SIDE_OFFDIAGONAL_BEFORE_CAUCHY`.

## 7. Relation to previous barriers

This explains why the following otherwise natural routes all meet the same H deficit:
- ordinary two-product DLS;
- centered E2 variance;
- determinant-shell dispersion;
- Mellin fourth-moment Cauchy.

They all diagonalize one side before extracting genuinely joint multilinear cancellation.

Thus the next branch should test whether a prime decomposition creates additional multiplicative coordinates that can be product-partitioned closer to the self-dual H^4 scale **before** any one-sided Cauchy step.

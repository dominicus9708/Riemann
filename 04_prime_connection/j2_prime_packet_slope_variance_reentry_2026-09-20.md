# j=2 prime-packet slope averaging re-enters E2 variance — 2026-09-20

## Status
- Riemann hypothesis: OPEN.
- Context: attempt to transfer the exact smooth 3D Hessian gain to the two prime weights by decomposing p,q~H^3 into packets of natural quadratic length H.
- Result: the outer d-variable scans the local prime frequencies at exactly H^{-1} resolution, but for each fixed packet pair the two frequencies move on a one-dimensional radial line.
- Averaging the packet slopes recovers the correct local determinant geometry, but after reassembling all packets the off-diagonal condition is exactly the earlier E2 product-cell condition
  \[
  |pq-p'q'|\lesssim H^2.
  \]
- Consequence: packet slope averaging is not an independent closure route; without an additional coefficient-sensitive input it is equivalent to the centered E2 variance frontier.
- Classification: \`J2_PACKET_SLOPE_VARIANCE_REENTRY\`.

## 1. Natural quadratic packet lengths

At the sharp scale
\[
d\asymp H^2,\qquad p,q\asymp P:=H^3,\qquad F=H^4,
\]
the physical second derivatives satisfy
\[
f_{dd}\asymp1,
\qquad
f_{pp},f_{qq},f_{pq}\asymp H^{-2},
\qquad
f_{dp},f_{dq}\asymp H^{-1}.
\]

Therefore the natural quadratic cells are
\[
\boxed{
\Delta d\asymp1,\qquad
\Delta p\asymp H,\qquad
\Delta q\asymp H.
}
\]

The d-direction is already at lattice scale.

Each prime interval of length P contains
\[
P/H=H^2
\]
prime packets of length H.

## 2. Local prime frequencies

Fix packet centers
\[
p_0,q_0\asymp P.
\]

The local linear frequencies are
\[
\alpha_p(d):=\partial_p f(d,p_0,q_0),
\qquad
\alpha_q(d):=\partial_q f(d,p_0,q_0).
\]

Their d-derivatives have size
\[
\alpha_p'(d),\alpha_q'(d)
\asymp H^{-1}.
\]

Thus increasing d by one moves each local frequency by exactly the Fourier resolution
\[
H^{-1}
\]
of a length-H packet.

This initially suggests a prime-packet large-sieve mechanism.

## 3. Rank-one obstruction for fixed packet centers

However
\[
\partial_p f
=
-\frac{f}{2p},
\qquad
\partial_q f
=
-\frac{f}{2q}.
\]

Hence for fixed packet centers
\[
\boxed{
\frac{\alpha_p(d)}{\alpha_q(d)}
=
\frac{q_0}{p_0}.
}
\]

As d varies, the pair
\[
(\alpha_p(d),\alpha_q(d))
\]
moves on a one-dimensional radial line in the two-dimensional frequency torus.

Therefore the d-average alone cannot supply two independent Parseval savings.

Classification:
\`FIXED_PACKET_D_FREQUENCY_MAP_HAS_RANK_ONE\`.

## 4. Local line energy

Write local offsets
\[
p=p_0+u,\qquad q=q_0+v,
\qquad
|u|,|v|\lesssim H.
\]

After expanding a squared packet sum, local differences
\[
a=u-u',
\qquad
b=v-v'
\]
enter the d-frequency through a linear form.

The H^{-1} Fourier resolution gives the near-resonance condition
\[
\boxed{
|p_0 a+q_0 b|
\lesssim H^2.
}
\]

For one fixed slope q_0/p_0, the number of local difference pairs satisfying this strip condition is naturally one power H above the exact diagonal.

Thus a single packet slope recovers only one of the two desired H^{1/2} amplitude savings.

Classification:
\`SINGLE_PACKET_SLOPE_HAS_H_ENERGY_EXCESS\`.

## 5. Averaging over packet slopes

Now let p_0 and q_0 range over their H-spaced packet centers.

For fixed nonzero a,b of comparable size, the condition
\[
|p_0a+q_0b|\lesssim H^2
\]
restricts the packet-center pair to a strip.

Elementary lattice counting shows that, after summing over all packet slopes, the local strip multiplicity returns to the diagonal scale up to logarithmic/divisor losses.

Thus the missing second H^{1/2} saving is geometrically available only after slope averaging.

This is the local manifestation of the nonzero mixed Hessian determinant.

## 6. Global reassembly

The local strip condition is the first-order expansion of the exact product condition.

Indeed,
\[
pq-p'q'
=
p_0(v-v')+q_0(u-u')
+
O(H^2)
\]
inside H x H packets.

Therefore
\[
|p_0a+q_0b|\lesssim H^2
\]
is equivalent, up to the packet Taylor error already of size H^2, to
\[
\boxed{
|pq-p'q'|\lesssim H^2.
}
\]

After summing all packets, the packet-slope energy is therefore precisely the near-product energy
\[
\#\{p,q,p',q': |pq-p'q'|\lesssim H^2\},
\]
with the actual prime/Von-Mangoldt coefficients inserted.

## 7. Return to the E2 cell

The long product variable is
\[
y=pq\asymp H^6.
\]

The natural product cell has length
\[
H^2.
\]

Equivalently, after the earlier j=2 normalization where one prime was already combined with the outer factor, this is the same Poisson-resolution product cell as the centered E2 variance formulation.

The smooth local density contribution is already closed by reciprocal curvature.

The remaining object is the centered fluctuation of the prime-product coefficient in these cells.

Hence:
\[
\boxed{
\text{prime-packet slope averaging}
\Longleftrightarrow
\text{centered E2 product-cell variance}
}
\]
at the unresolved off-diagonal level.

Permanent rule:
\`PACKET_SLOPE_AVERAGE_NOT_INDEPENDENT_OF_E2_VARIANCE\`.

## 8. Prime short-interval variance does not black-box close it

A tempting approach is to use short-interval variance for each individual prime packet of length
\[
H=P^{1/3}.
\]

Classical unconditional almost-all prime results do apply in a nontrivial range around this scale, but the known unconditional Selberg-integral estimates do not provide the Poisson-size variance required to tensor two prime directions and close the exact product-cell target.

Thus replacing the product variance by two independent prime short-interval variance black boxes is not justified.

Classification:
\`INDIVIDUAL_PRIME_PACKET_VARIANCE_NOT_SUFFICIENT_BLACK_BOX\`.

## 9. Consequence for the H^(1/8) route

The packet analysis explains the full hierarchy:

- one fixed slope loses H^{1/2};
- slope averaging geometrically supplies the second H^{1/2};
- but with prime coefficients the global slope-averaged off-diagonal becomes the E2 centered variance problem.

Therefore a direct packet proof of the remaining H^{-1/8} gain must use more than elementary frequency geometry.

It must insert arithmetic cancellation **inside** the near-product strip, or use the double-Vaughan refinement before the packets are globally recombined.

## 10. Updated live target

The current smallest target remains the double-refined H^(1/8) residual.

The packet calculation supplies a new diagnostic:

\[
\boxed{
\text{any proposed H}^{-1/8}\text{ gain must beat the centered near-product strip,
not merely average packet slopes.}
}
\]

This prevents counting the mixed-Hessian geometry twice.

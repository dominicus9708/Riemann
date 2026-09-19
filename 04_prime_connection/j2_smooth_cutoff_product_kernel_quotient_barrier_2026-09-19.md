# j=2 smooth-cutoff admissibility and product-kernel quotient barrier — 2026-09-19

## Status
- Riemann hypothesis: OPEN.
- Context: signed Vaughan head-tail frontier after exact inter-branch cancellation was identified.
- Two new results:
  1. sharp Vaughan truncations at scale H may be replaced by smooth cutoffs with only balanced H^6-scale transition errors;
  2. any linear/Gram architecture whose kernel sees a factorization atom only through its total product q cannot extract a new gain from signed Vaughan recombination: after quotienting the exact nullspace it is precisely the original prime operator.
- Consequence: a successful signed multiscale route must create factor-sensitive secondary phase before the norm/spacing step, e.g. by a B-process in a genuinely smooth cofactor.
- Classification:
  - \`J2_SMOOTH_CUTOFF_TRANSITION_CLOSED\`;
  - \`J2_PRODUCT_KERNEL_QUOTIENT_BARRIER\`.

## 1. Smooth the Möbius truncation

Choose a fixed smooth function W with
\[
W(x)=1\quad(0\le x\le1),
\qquad
W(x)=0\quad(x\ge2).
\]

Define
\[
\mu_W(d):=\mu(d)W(d/H).
\]

Then
\[
\Delta\mu(d)
:=
\mu_W(d)-\mu(d)\mathbf1_{d\le H}
\]
is supported on
\[
\boxed{H<d<2H.}
\]

Consider the induced difference in the factorable convolution
\[
\Delta\mu*\Lambda_{>H}*1.
\]

On q~H^3 write
\[
q=d\,e\,r.
\]

Since d~H,
\[
er\asymp H^2.
\]

In the full sharp j=2 sector there are also the outer factors
\[
d_0\asymp H^2,
\qquad
p\asymp H^3.
\]

Thus the four effective H-exponents are
\[
\boxed{\{2,3,1,2\}.}
\]

They admit the exact self-dual partition
\[
(d_0\cdot er)\mid(p\cdot d)
\]
with
\[
H^4\times H^4.
\]

The collapsed coefficient on er is divisor/log-bounded, so standard product DLS gives
\[
\boxed{
T_{\Delta\mu}
\ll_\varepsilon H^{6+\varepsilon}.
}
\]

Hence smoothing the Möbius cutoff costs no polynomial power.

Permanent rule:
\`MOBIUS_CUTOFF_TRANSITION_IS_BALANCED\`.

## 2. Smooth the head-tail cutoff

Likewise choose a smooth head weight V with
\[
V(x)=1\quad(x\le1),
\qquad
V(x)=0\quad(x\ge2).
\]

Replacing
\[
\mathbf1_{k\le H}
\]
by
\[
V(k/H)
\]
creates an error supported on
\[
k\asymp H.
\]

Since
\[
q=ek\asymp H^3,
\]
we have
\[
e\asymp H^2.
\]

Together with
\[
d_0\asymp H^2,
\qquad
p\asymp H^3,
\]
the exponent list is again
\[
\{2,3,1,2\},
\]
and the same H^4 x H^4 partition closes the transition.

Therefore
\[
\boxed{
T_{\rm sharp\ head}
=
T_{\rm smooth\ head}
+
O_\varepsilon(H^{6+\varepsilon}).
}
\]

Equivalently, the sharp tail may be replaced by a smooth tail modulo an already-closed error.

Permanent rule:
\`HEAD_TAIL_CUTOFF_TRANSITION_IS_BALANCED\`.

## 3. Consequence: Mellin separation is legal

After smoothing, a tail weight such as
\[
1-V(dr/H)
\]
may be Mellin-separated on dyadic boxes:
\[
1-V(dr/H)
=
\int_{\mathbb R}
\widehat{\mathcal V}(t)
(d/H)^{it}r^{it}\,dt,
\]
with rapidly decaying transform after localization.

Thus the sharp truncation itself is not an obstruction to a factor-sensitive B-process or dispersion argument.

Classification:
\`SMOOTH_SIGNED_TAIL_MELLIN_ADMISSIBLE\`.

## 4. Product map for Vaughan atoms

Let an arithmetic factorization atom be
\[
\alpha=(e,d,r)
\]
with product
\[
\pi(\alpha):=edr=q.
\]

Before any factor-sensitive transformation, the reciprocal phase and all outer variables see alpha only through q:
\[
\Phi(\alpha;\xi)
=
\Phi(q;\xi),
\]
where \(\xi\) denotes the outer j=2 variables.

Let c_alpha be the signed Vaughan atom coefficient.

Define the product-collapsed coefficient
\[
C_q
=
\sum_{\pi(\alpha)=q}c_\alpha.
\]

Exact Vaughan recombination gives
\[
\boxed{C_q=\Lambda(q)}
\]
on the working q-range.

## 5. Exact nullspace

Let P be the product-collapsing map
\[
(Pc)_q
=
\sum_{\pi(\alpha)=q}c_\alpha.
\]

Then every coefficient vector z satisfying
\[
\sum_{\pi(\alpha)=q}z_\alpha=0
\quad\text{for every }q
\]
lies in
\[
\ker P.
\]

All exact composite inter-branch cancellation directions are elements of this kernel.

If the analytic operator has the form
\[
\mathcal A c
=
\sum_\alpha c_\alpha \Phi(\pi(\alpha);\xi),
\]
then
\[
\boxed{
\mathcal A=\widetilde{\mathcal A}\,P.
}
\]

Hence
\[
\ker P\subseteq\ker\mathcal A.
\]

The Vaughan null directions are already invisible to the original phase operator.

## 6. Gram quotient theorem

The Gram kernel before a factor-sensitive transform is
\[
K_{\alpha,\beta}
=
\langle
\Phi(\pi(\alpha)),
\Phi(\pi(\beta))
\rangle.
\]

Therefore
\[
K_{\alpha,\beta}
=
\widetilde K_{\pi(\alpha),\pi(\beta)}.
\]

In operator notation,
\[
\boxed{
K=P^*\widetilde K P.
}
\]

Consequently the quotient of the factorization-atom Hilbert space by
\[
\ker P
\]
is exactly the product/q-space.

After quotienting all exact signed Vaughan null directions, the surviving coefficient is
\[
C_q=\Lambda(q).
\]

Thus any Gram/DLS estimate whose kernel depends only on total products is analytically equivalent to an estimate for the original prime q-sum.

Classification:
\`PRODUCT_KERNEL_SIGNED_QUOTIENT_EQUALS_PRIME_OPERATOR\`.

## 7. Why branchwise absolute values lose power

If one takes absolute values or Cauchy in factorization coordinates before applying P, the cancellation in
\[
\ker P
\]
is destroyed.

This creates the artificial H^(1/4) and H^(1/6) factor-scale deficits already observed.

But simply “keeping the signs” without changing the kernel does not create a gain either: it merely performs the exact quotient and returns to Lambda(q).

Hence:
\[
\boxed{
\text{sign preservation alone is necessary but not sufficient.}
}
\]

## 8. Required escape mechanism

To obtain genuinely new analytic information from factorization coordinates, one must first create a kernel which distinguishes them.

A legal example is:
- choose a genuinely smooth cofactor r;
- apply a B-process / Poisson transform in r before Cauchy;
- obtain a secondary phase involving d and the dual frequency separately.

Then the transformed kernel no longer factors only through
\[
q=edr.
\]

Only at that point can a signed multiscale norm estimate potentially exploit both:
- factor geometry;
- Vaughan null directions.

Permanent rule:
\`FACTOR_SENSITIVE_SECONDARY_PHASE_BEFORE_SIGNED_GRAM_GAIN\`.

## 9. Updated frontier

The next route is therefore not a generic well-factorable weight insertion.

It is:

\[
\boxed{
\text{smooth the cutoffs}
\to
\text{expose a smooth cofactor}
\to
\text{B-process before product collapse}
\to
\text{build the signed Gram operator in the dual variables}.
}
\]

If no smooth cofactor exceeds or reaches the useful B-process scale, the branch returns to the previously audited self-dual barrier.

This sharply separates:
- harmless cutoff smoothing;
- algebraic signed cancellation;
- genuinely new factor-sensitive oscillatory information.

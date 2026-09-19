# j=2 double completion to rank-3 hyper-Kloosterman: exact functional-class audit — 2026-09-20

## Status
- Riemann hypothesis: OPEN.
- Context: after the ordinary Kloosterman near-match encountered an inverse-support obstruction.
- New algebraic observation: simultaneous completion of a reciprocal product phase in two factors produces a rank-3 hyper-Kloosterman complete sum.
- Literature: Kowalski--Michel--Sawin (KMS) bilinear hyper-Kloosterman theorems apply to the correct trace-function class for prime modulus.
- Critical limitation: after a full Vaughan decomposition on both prime variables the natural determinant modulus is no longer prime-supported; to preserve a prime modulus one must leave the modulus-side prime undecomposed.
- Thus the hyper-Kloosterman route is structurally promising but is not yet a legal closure of the H^(1/8) double-refined branch.
- Classification: \`J2_HYPERKLOOSTERMAN_DOUBLE_COMPLETION_FRONTIER\`.

## 1. Reciprocal product kernel

The determinant/Kloosterman reduction naturally produces reciprocal phases of the form
\[
e_p\!\left(A\,\overline{mn}\right),
\]
where p is the modulus and m,n are multiplicative factors on the opposite side.

Assume temporarily that m,n are supported with smooth dyadic weights.

## 2. Simultaneous completion

Complete both variables modulo p.

The complete kernel at dual frequencies h_1,h_2 is
\[
\mathcal K(h_1,h_2)
=
\sum_{x,y\bmod p}^{*}
e_p\!\left(
h_1x+h_2y+\frac{A}{xy}
\right).
\]

If h_1,h_2 are nonzero, set
\[
X=h_1x,\qquad Y=h_2y.
\]

Then
\[
\mathcal K(h_1,h_2)
=
\sum_{X,Y\bmod p}^{*}
e_p\!\left(
X+Y+\frac{Ah_1h_2}{XY}
\right).
\]

This is exactly the unnormalized rank-3 hyper-Kloosterman sum:
\[
\boxed{
\mathcal K(h_1,h_2)
=
p\,\mathrm{Kl}_3(Ah_1h_2;p)
}
\]
under the standard normalization
\[
\mathrm{Kl}_3(t;p)
=
p^{-1}
\sum_{XY Z=t}^{*}e_p(X+Y+Z).
\]

Classification:
\`RECIPROCAL_DOUBLE_COMPLETION_GIVES_KL3\`.

## 3. Critical dual lengths

If
\[
m,n\asymp M=N=\sqrt p,
\]
smooth completion localizes the dual variables to
\[
|h_1|,|h_2|
\lesssim
p/M
=
\sqrt p.
\]

Thus the completed bilinear form has exactly the critical shape
\[
\boxed{
\sum_{h_1,h_2\asymp\sqrt p}
\alpha_{h_1}\beta_{h_2}
\mathrm{Kl}_3(Ah_1h_2;p).
}
\]

This matches the functional form studied by KMS.

## 4. KMS literature match

Kowalski--Michel--Sawin prove nontrivial bilinear estimates for normalized hyper-Kloosterman kernels
\[
K(mn;p)=\mathrm{Kl}_k(a mn;p).
\]

Their later stratification theorem applies whenever
\[
M,N\ge p^\delta,
\qquad
MN\ge p^{3/4+\delta}
\]
for fixed \(\delta>0\), giving some power saving.

At
\[
M=N=\sqrt p
\]
the parameter range is comfortably satisfied.

Hence:
\[
\boxed{
\text{the simultaneous-completion kernel lies in a known nontrivial trace-function class.}
}
\]

Classification:
\`KL3_CRITICAL_BILINEAR_CLASS_LITERATURE_EXISTS\`.

## 5. Explicit benchmark from the older KMS bound

For critical square-root lengths, the explicit KMS prime-modulus benchmark cited in later literature saves
\[
p^{-1/64}
\]
over the trivial bilinear scale.

With
\[
p\asymp H^3,
\]
this is
\[
\boxed{
H^{-3/64}.
}
\]

Relative to the current double-refined requirement
\[
H^{-1/8}
=
H^{-8/64},
\]
one such explicit saving would leave
\[
\boxed{
H^{5/64}.
}
\]

The later stratification theorem guarantees a power saving in this range but does not, in the theorem statement used here, provide an explicit exponent large enough to verify the full H^(-1/8) target.

Permanent guard:
\`NONTRIVIAL_KL3_SAVING_NE_REQUIRED_NUMERICAL_SAVING\`.

## 6. Prime-modulus preservation obstruction

The determinant completion uses one original prime variable as modulus.

If Vaughan/Heath--Brown decompositions are applied to **both** original prime variables, then on an individual branch the modulus-side integer is no longer restricted to primes.

It is a product variable carrying a convolution coefficient.

The KMS theorems cited above require a prime modulus.

Therefore:
\[
\boxed{
\text{double-refined H}^{1/8}\text{ branch}
\not\Rightarrow
\text{prime-modulus KMS form}
}
\]
by direct substitution.

Permanent rule:
\`DO_NOT_KEEP_PRIME_MODULUS_AFTER_DECOMPOSING_THE_MODULUS_VARIABLE\`.

## 7. Legal one-sided architecture

To retain a prime modulus p, decompose only the opposite prime variable p'.

Then:
- p remains prime and can serve as KMS modulus;
- p' may expose factors near \(p^{1/2}\);
- smooth factors can be completed;
- arithmetic factors can remain as bilinear coefficients if the completed kernel reaches a normalized hyper-Kloosterman form.

This architecture is legal in principle.

However it no longer automatically inherits the full double-refined H^(1/8) product-balance improvement, because only one prime side has been refined.

Thus its net exponent must be recalculated from scratch.

Classification:
\`ONE_SIDED_PRIME_MODULUS_HYPERKL_ROUTE_OPEN\`.

## 8. Smoothness requirement for completion

Simultaneous Poisson/completion localizes dual lengths to p/M only when the completed variables carry smooth interval weights.

An arbitrary Möbius or von-Mangoldt coefficient cannot be silently completed as if it were a smooth amplitude.

Exact finite Fourier completion is always possible, but its transform may occupy the full modulus p and then loses the critical square-root support.

Therefore each proposed KL3 map must record:
1. which variables are genuinely smooth;
2. which variables remain arithmetic coefficients;
3. the Fourier support length after completion.

Permanent rule:
\`HYPERKL_COMPLETION_REQUIRES_GENUINELY_SMOOTH_VARIABLES\`.

## 9. Updated exact search problem

There are now two possible legal paths.

### Path A — one-sided prime modulus
Keep p prime, decompose p', and seek a smooth factorization whose completion gives
\[
\sum_{m,n\asymp\sqrt p}
\alpha_m\beta_n\mathrm{Kl}_3(A mn;p)
\]
with both supports critical.

Then compute the total exponent including:
- Poisson prefactors;
- untouched small arithmetic factors;
- KMS saving.

### Path B — composite-modulus replacement
If both prime sides are decomposed, derive a trace-function/bilinear theorem valid for the resulting composite modulus.

The 2026 Pascadi/Blomer--Pascadi ordinary-Kloosterman results handle arbitrary composite moduli, but not automatically the rank-3 hyper-Kloosterman kernel arising here.

No direct theorem has yet been identified.

## 10. Current verdict

Double completion resolves the earlier modular-inverse-support issue at the level of functional form:
\[
e_p(A\overline{mn})
\to
\mathrm{Kl}_3(Ah_1h_2;p).
\]

But the three requirements
\[
\boxed{
\text{prime modulus}
+
\text{smooth completion variables}
+
\text{sufficient explicit saving}
}
\]
have not yet been satisfied simultaneously.

Therefore the official j=2 frontier remains
\[
\boxed{H^{1/8}},
\]
with the hyper-Kloosterman route promoted to a serious candidate rather than a closure.

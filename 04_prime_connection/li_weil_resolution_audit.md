# Li-Weil resolution audit

Status: exact quartet algebra + finite-resolution guard + generalized-Li height tuning. No RH proof claim.

## 1. Standard Li quartet

Li's coefficients are

lambda_n = sum_rho [1-(1-1/rho)^n].

Let rho=beta+i gamma, and put

r=(rho-1)/rho = exp(kappa+i theta).

The functional-equation/conjugation quartet rho, 1-rho, conjugate(rho), 1-conjugate(rho) contributes exactly

Q_n(rho)=4-4 cosh(n kappa) cos(n theta).

On the critical line beta=1/2, kappa=0 and

Q_n=4(1-cos(n theta))>=0.

Off the line, |kappa|>0 and cosh(n kappa) grows exponentially; the Bombieri-Lagarias/Li theorem says eventual positivity for every n is impossible.

## 2. Height-amplified reflection resolution

Write beta=1/2+delta and A=gamma^2+1/4. Then

kappa
= (1/2) log[(A-delta+delta^2)/(A+delta+delta^2)]
= -delta/A + O(delta^3/A^2)  (for small delta relative to A).

Hence the natural finite-index sensitivity parameter is

Xi_Li = n |delta|/(gamma^2+1/4).

If Xi_Li <<1, the off-line displacement enters the reflection-symmetric quartet only through

cosh(n kappa)-1 = O(Xi_Li^2).

Thus positivity checks only up to n<=N have an intrinsic amplitude false-control scale

|delta| << (gamma^2+1/4)/N.

This is not an impossibility theorem for every conceivable use of the first N coefficients; it is a mandatory finite-resolution guard for direct Li-quartet amplitude diagnostics.

## 3. Generalized Li parameter

For real a<1/2, let c=1/2-a>0 and use the generalized Li Mobius ratio

R_a(rho)=(rho-a)/(rho+a-1).

On beta=1/2 this has unit modulus. For beta=1/2+delta,

kappa_a := log|R_a(rho)|
= (1/2) log[((c+delta)^2+gamma^2)/((c-delta)^2+gamma^2)]
= [2c delta/(c^2+gamma^2)] + O(delta^3).

For a target height gamma, the linear sensitivity 2c/(c^2+gamma^2) is maximized at

c=|gamma|,

where

|kappa_a| ~ |delta|/|gamma|.

Thus a height-tuned generalized Li transform improves the standard high-height penalty from gamma^2 to gamma:

standard:     n|delta|/gamma^2,
height-tuned: n|delta|/gamma.

This is still an RH-equivalent reparameterization, not extra information.

## 4. Exact target phase alignment

For a specific off-line zero, choosing

c=sqrt(gamma^2+delta^2)

makes R_a(rho) purely imaginary, because the real part of

(c+delta+i gamma)/(delta-c+i gamma)

vanishes exactly. Therefore its phase is +/-pi/2. For n divisible by 4, the target quartet contribution is

Q_n=4-4 cosh(n kappa_a)<0

whenever delta!=0.

This shows explicitly how the generalized parameter can be tuned to a height/displacement and remove the Diophantine phase-alignment delay for that target quartet. However the full Li coefficient contains every zero, so a negative target quartet need not make the total coefficient negative until its exponential growth dominates.

## 5. Relation to Weil criterion

Bombieri-Lagarias proved that Li's criterion is a restricted instance of Weil's positivity criterion and gave an arithmetic formula via the Guinand-Weil explicit formula. Lagarias identifies the corresponding test functions with associated Laguerre polynomials.

Therefore generalized-Li height tuning is best interpreted as increasing test-function localization freedom on the way toward the full Weil class.

The arithmetic side does not become manifestly positive: the Laguerre/Weil prime weights oscillate in sign. Proving positivity of the full family remains the RH content.

## 6. Audit verdict

- Li quartet positivity on the line: EXACT.
- off-line exponential amplifier: EXACT.
- `LI_HEIGHT_RESOLUTION_GUARD`: new permanent finite-n audit rule.
- generalized-Li tuning c~gamma: EXACT first-order optimization.
- target phase alignment c=sqrt(gamma^2+delta^2): EXACT.
- independent proof mechanism: NOT FOUND.
- classification: SPECTRAL DETECTOR / WEIL REENCODING.

Future finite Li numerical claims must report the dimensionless resolution n|delta|/(gamma^2+1/4), or the corresponding tuned generalized-Li resolution if a is varied.
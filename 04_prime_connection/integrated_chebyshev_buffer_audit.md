# Integrated Chebyshev buffer audit

Status: exact decomposition + RH-side asymptotic buffer bound + smoothing audit. No proof claim beyond known Johnston criterion.

## 1. Johnston criterion

Daniel R. Johnston proved that RH is equivalent to

I_0(x):=\int_2^x (\vartheta(t)-t)\,dt <0 \qquad (x>2).

The purpose here is not to reprove novelty, but to expose the mechanism in the formation language: a deterministic prime-square bias competes with the zero-sensitive part of \psi(t)-t.

## 2. Prime-power decomposition

Use

\psi(t)=\vartheta(t)+\vartheta(t^{1/2})+\vartheta(t^{1/3})+\cdots.

Then

I_0(x)
=\int_2^x(\psi(t)-t)\,dt
-\sum_{k\ge2}\int_2^x\vartheta(t^{1/k})\,dt.

The k=2 term is dominant. By PNT,

\int_2^x\vartheta(\sqrt t)\,dt
=\frac23 x^{3/2}+o(x^{3/2}).

All k>=3 prime-power layers contribute o(x^{3/2}); the first of them is on the x^{4/3} scale.

Thus the deterministic leading bias is

-\frac23 x^{3/2}.

## 3. Integrated zero wave

A once-integrated explicit formula for \psi(t)-t gives the nontrivial-zero contribution

-\sum_\rho \frac{x^{\rho+1}}{\rho(\rho+1)},

up to terms lower than x^{3/2} on RH. Hence under RH,

\frac{I_0(x)}{x^{3/2}}
=
-\frac23
-\sum_\rho \frac{x^{i\gamma}}{\rho(\rho+1)}
+o(1).

For \rho=1/2+i\gamma,

|\rho(\rho+1)|
=\sqrt{(\gamma^2+1/4)(\gamma^2+9/4)}
>\gamma^2+1/4
=\rho(1-\rho).

Using the classical first-Li-coefficient identity

\sum_\rho \frac1{\rho(1-\rho)}
=2+\gamma_E-\log(4\pi)
=0.046191417932242\ldots

under RH, we obtain

S_0:=\sum_\rho \frac1{|\rho(\rho+1)|}
<0.046191417932242\ldots.

Therefore the worst absolute zero-wave mass is less than 6.93% of the prime-square buffer:

S_0/(2/3)<0.0692872.

Equivalently, the leading-scale margin is at least

2/3-(2+\gamma_E-\log(4\pi))
=0.6204752487\ldots.

This gives a transparent asymptotic explanation for the RH=>negative direction of Johnston's criterion. Johnston's paper supplies explicit finite-x bounds (including |\int_2^x(\psi(t)-t)dt|<=0.08 x^{3/2} for x>=3000 under RH) and finite-range verification needed for the global x>2 statement.

## 4. Why RH false eventually beats the buffer

If a zero has real part \beta>1/2, then its integrated contribution has scale x^{\beta+1}, while the prime-square buffer is x^{3/2}. The relative amplitude therefore grows as x^{\beta-1/2}. Standard oscillation/Landau arguments imply arbitrarily large positive excursions; this is the converse mechanism in Johnston's theorem.

Thus the criterion has a simple formation interpretation:

prime-square deterministic bias   vs.   off-critical spectral growth.

## 5. Repeated positive smoothing

For fixed integer r>=0 define

I_r(x):=\frac1{r!}\int_2^x (x-t)^r(\vartheta(t)-t)\,dt.

For r>=1, integration by parts gives the exact inheritance identity

I_r(x)
=\frac1{(r-1)!}\int_2^x (x-u)^{r-1} I_0(u)\,du.

Hence RH=>I_r(x)<0 for every x>2 and every fixed r: higher-order negativity is inherited through a positive kernel and is not new information.

The prime-square leading coefficient is

B_r
=\frac{\Gamma(3/2)}{\Gamma(r+5/2)},

so

I_r(x)\supset -B_r x^{r+3/2}.

The zero \rho contributes

-\frac{x^{\rho+r+1}}
{\rho(\rho+1)\cdots(\rho+r+1)}.

Under RH define

S_r:=\sum_\rho
\frac1{|\rho(\rho+1)\cdots(\rho+r+1)|}.

Since

|\rho+r+2|\ge r+5/2

and

B_{r+1}=B_r/(r+5/2),

we have

S_{r+1}/B_{r+1}\le S_r/B_r.

Therefore

\boxed{S_r/B_r<0.0692872\quad\text{for every fixed }r\ge0.}

So repeated smoothing does not weaken the asymptotic RH-side buffer-to-zero-wave margin.

## 6. Smoothing-detection tradeoff

For an off-line zero \rho=1/2+\delta+i\gamma, \delta>0, the normalized zero contribution relative to the prime-square buffer is

R_r(\rho)x^\delta,

where

R_r(\rho)
=\frac{\Gamma(r+5/2)}{\Gamma(3/2)}
\frac{|\Gamma(\rho)|}{|\Gamma(\rho+r+2)|}.

For fixed \rho and large r,

R_r(\rho)\asymp C_\rho r^{-\delta}.

Thus every fixed r still detects a false RH eventually, because x^\delta dominates. But increasing r can postpone the first visible sign reversal. For r small compared with |\gamma|, each added integration contributes roughly another factor 1/|\gamma| to the target zero; for large r the delay becomes approximately an r^{-\delta} relative suppression.

Permanent audit rule:

`SMOOTHING_DELAY_GUARD` — stronger finite-x sign stability after repeated positive smoothing is not stronger evidence for RH unless the loss of sensitivity to a hypothetical off-line zero is quantified.

## 7. Literature relation

- Johnston (Canadian Mathematical Bulletin 66 (2023), 185-195) proves the exact r=0 sign criterion and explicit RH-side estimates.
- Suzuki (Ramanujan Journal 68 (2025), article 95; corrected 2026) studies related weighted von-Mangoldt sign criteria and Riesz-like smoothing, reinforcing that weighted sign constancy is a broad RH/GRH-equivalent framework rather than an automatic new proof method.

## 8. Audit verdict

- Johnston integral sign criterion: KNOWN EXACT RH EQUIVALENCE.
- prime-square leading buffer 2/3: STRUCTURAL / EXACT ASYMPTOTIC.
- critical-line zero-wave absolute mass <0.0461915: RH-CONDITIONAL EXACT BOUND.
- buffer/zero-wave ratio >14.43: RH-CONDITIONAL STRUCTURAL EXPLANATION.
- repeated smoothing negativity: POSITIVE-KERNEL REENCODING.
- higher smoothing as stronger numerical evidence: REJECT without `SMOOTHING_DELAY_GUARD`.

This branch is useful because it isolates the role of prime powers more cleanly than the Robin-Nicolas corridor, but it does not remove the core off-critical zero obstruction.
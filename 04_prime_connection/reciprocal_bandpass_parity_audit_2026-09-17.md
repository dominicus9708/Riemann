# Reciprocal band-pass / parity audit — 2026-09-17

## Status
- Riemann hypothesis: OPEN.
- The previous spectral-primitive boundary identity is correct, but it admits a simpler exact reformulation as a positive band-pass energy for a genuine autocorrelation block.
- This reformulation clarifies the positive-coefficient false control and isolates a mesoscopic Fourier-energy problem.
- Finite audits show Möbius and Liouville band energy at essentially random-sign scale, while squarefree support alone is substantially sub-random in the same bands.
- Existing Fourier-uniformity / Gowers-uniformity results do not directly reach the required diagonal `L^2` band scale in polynomially shrinking bands.

## 1. Exact band-pass collapse
Let `a_m` be a finite real sequence and

\[
P(\alpha)=\sum_m a_m e(\alpha m),
\qquad
A_h=\sum_m a_m a_{m+h},
\qquad
A_0=\sum_m a_m^2.
\]

For

\[
F(y)=\int_1^2 e(y\sqrt t)\,dt,
\]

we have

\[
A_0+2\operatorname{Re}\sum_{h\ge1}A_hF(h/H)
=
\int_1^2\left|P\!\left(\frac{\sqrt t}{H}\right)\right|^2dt.
\]

Changing variables `u=sqrt(t)/H` gives the exact identity

\[
\boxed{
A_0+2\operatorname{Re}\sum_{h\ge1}A_hF(h/H)
=
2H^2\int_{1/H}^{\sqrt2/H}u\,|P(u)|^2\,du.
}
\]

Classification:

`RECIPROCAL_BANDPASS_ENERGY_IDENTITY`.

This is exactly equivalent to the previous first/second spectral-primitive formula. The apparent cancellation between the two primitive boundary terms is the integration-by-parts form of a positive Fourier-energy integral over the annulus

\[
[1/H,\sqrt2/H].
\]

## 2. Interpretation
The continuous local reciprocal kernel does not require flatness all the way down to frequency zero. It probes only a shrinking nonzero band.

For a coefficient block with energy `A0`, random spectral density predicts

\[
\int_{1/H}^{\sqrt2/H}|P(u)|^2du
\asymp
\frac{A_0}{H}.
\]

Thus the local diagonal-scale target is a **mesoscopic band-energy law**, not a bound for the DC component `P(0)` and not, by itself, a square-root Mertens estimate.

A smooth positive sequence can have most of its Fourier energy concentrated near zero and therefore have very small energy in the reciprocal band. This explains the previous positive-coefficient false control without attributing the small reciprocal sum to Möbius cancellation.

## 3. Important partition correction
The positive band-pass identity applies directly only when `A_h` is the full autocorrelation of one coefficient sequence (or a genuine separately truncated block).

In the exact lag-side partition used in Sector A, define

\[
b_j(m)=\chi_j(m)a_m,
\qquad
P_j(u)=\sum_m b_j(m)e(um),
\qquad
P(u)=\sum_m a_m e(um).
\]

The one-sided/full-lag cross-correlation is

\[
C_{j,h}=\sum_m b_j(m)a_{m+h},\qquad h\in\mathbb Z.
\]

Then, for a frozen local frequency `alpha_j`, the exact cross identity is

\[
\boxed{
\sum_{h\in\mathbb Z}C_{j,h}F(\alpha_j h)
=
\frac{2}{\alpha_j^2}
\int_{\alpha_j}^{\sqrt2\alpha_j}
 u\,\overline{P_j(u)}P(u)\,du.
}
\]

This quantity is not positive block by block. Summing over `j` only becomes an ordinary positive band energy if the same frequency window is shared and `sum_j P_j=P` can be used before taking bounds.

Permanent guard:

`LOCAL_BANDPASS_BLOCK_ORTHOGONALITY_GUARD` — do not replace the exact lag-side partition by independently positive local band energies. Doing so discards cross-block compensation and may impose a stronger problem than the original reciprocal mean square.

## 4. Finite parity/support audit
For a length-`D` dyadic coefficient block define the normalized band ratio

\[
R_H(a)
:=
\frac{\displaystyle \int_{1/H}^{\sqrt2/H}|P_a(u)|^2\,du}
{\displaystyle ((\sqrt2-1)/H)\sum_m|a_m|^2}.
\]

`R_H=1` is the flat/random-energy baseline.

The audit used

- `D=2^12,...,2^17`;
- `H=4,8,16,32,...` restricted to `H<=D^(1/3)` plus the integer endpoint `floor(D^(1/3))`;
- exact autocorrelations computed by FFT and exact integration of each Fourier mode over the band.

Across 25 `(D,H)` cells per coefficient family:

| coefficients | mean `R_H` | std | min | max |
|---|---:|---:|---:|---:|
| Möbius `mu` | 0.9995 | 0.0376 | 0.8965 | 1.0538 |
| Liouville `lambda` | 1.0070 | 0.0233 | 0.9679 | 1.0725 |
| squarefree support `mu^2` | 0.2306 | 0.1688 | 0.1120 | 0.5319 |
| random signs on squarefree support | 0.9984 | 0.0595 | 0.8325 | 1.1680 |

Classification:

`FINITE_PARITY_BANDPASS_RANDOM_SCALE`.

This is numerical evidence only.

### Interpretation
The squarefree support itself is much smoother than a random sign sequence in these bands. Multiplicative parity changes the picture sharply:

- `mu` and `lambda` sit near the flat random-energy baseline;
- random signs on the same squarefree support do the same;
- therefore the missing band energy of `mu^2` is not caused merely by support density;
- the sign layer associated with prime-factor parity is the numerically active broadband component.

However, arbitrary deterministic signs are not enough. At `D=65536`, periodic controls such as `mu^2(n)(-1)^n` or a mod-3 character times `mu^2` show strong `H`-dependent spectral concentration/depletion. Thus the observation is specific to the actual multiplicative-parity structure, not to the presence of signs in general.

Permanent guard:

`PARITY_SIGN_NOT_GENERIC_RANDOMNESS_GUARD`.

## 5. Current theorem gap
For a length-`N` Möbius polynomial

\[
P(\theta)=\sum_{n\sim N}\mu(n)e(n\theta),
\]

the desired shrinking-band scale is

\[
\int_I|P(\theta)|^2d\theta
\ll
\frac{N^{1+\varepsilon}}{H},
\qquad |I|\asymp H^{-1}.
\]

Global Parseval only gives `O(N)`, losing a factor `H`.

The strongly logarithmic `U^2` uniformity of Möbius implies, after translating the normalized `U^2` statement,

\[
\int_0^1|P(\theta)|^4d\theta
\ll_A
N^3(\log N)^{-4A}
\]

for every fixed `A>0` (ineffective constants allowed). Hölder on a band of width `1/H` then gives only

\[
\int_I|P|^2
\ll_A
N^{3/2}H^{-1/2}(\log N)^{-2A}.
\]

Relative to the desired `N/H`, this still loses

\[
\sqrt{NH}(\log N)^{-2A},
\]

which is polynomial in the present ranges and cannot be removed by fixing a larger logarithmic exponent.

Likewise the Matomäki–Radziwiłł–Tao short-interval Fourier-uniformity theorem gives qualitative `o(H)` cancellation on average over interval locations, but not the random-sign/diagonal `L^2` scale required here.

The August 2026 work of Ben Doyle on short `k`-free exponential sums explicitly identifies improvements to a Möbius `ell^2` estimate as the obstruction to further moment improvements. This is consistent with the present reduction rather than closing it.

Recent quantitative logarithmic Chowla results for growing shifts remain logarithmically weighted and currently cover polylogarithmic shift ranges, so they do not directly supply the ordinary mesoscopic band estimate above.

Classification:

`MESOSCOPIC_MOBIUS_BAND_L2_OPEN`.

## 6. What has and has not been gained
The band-pass collapse is useful because it proves that the current Sector-A object is **not** simply square-root Mertens in disguise: the band starts at frequency `1/H`, and a sequence may have an arbitrarily large DC component while having tiny reciprocal-band energy (the positive sequence is the simplest finite false control).

But it also shows that a proof based solely on freezing the reciprocal geometry and then demanding local positive band-energy bounds would require a genuine mesoscopic spectral equidistribution theorem for Möbius that is not currently available.

Therefore the next main line should preserve more of the exact multiplicative/reciprocal structure instead of declaring `MESOSCOPIC_MOBIUS_BAND_L2_OPEN` to be the sole proof target.

## 7. Next direct audit
The finite support/parity split suggests testing the exact prime-dilation recursion of the parity sequence before any coefficient absolute values are taken.

For Liouville,

\[
\sum_{\substack{D<n\le2D\\p\mid n}}
\lambda(n)e(\alpha n)
=
- P_{D/p}(p\alpha)
\]

exactly.

For Möbius the corresponding identity contains the squarefree correction `p\nmid m`.

The next question is whether averaging these exact prime-dilation identities can transfer energy from the difficult band `(D,H)` to smaller `(D/p,H/p)` scales with a true contraction, rather than reproducing only the logarithmic Turán–Kubilius savings already implicit in standard Fourier-uniformity methods.

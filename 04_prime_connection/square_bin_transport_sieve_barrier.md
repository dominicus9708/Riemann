# Square-bin local-transport invariance and sieve-parity barrier

Date: 2026-09-16

## Status

- RH: `OPEN`.
- Square-bin compression: `EXACT RH-EQUIVALENT REENCODING`.
- Finite-lag autocorrelation: `NOT AN RH-INVARIANT`.
- Complete square-bin sieve: `EXACT`.
- Linear/lower-bound sieve route: `CLOSED_BY_PARITY_BARRIER`.

## 1. Exact square-bin residual and discrete derivative

Let

\[
c_m=\pi((m+1)^2)-\pi(m^2),
\]

and

\[
d_m=2c_m\log m-(2m+1).
\]

Define the exact Chebyshev-bin residual

\[
g_m=\vartheta((m+1)^2)-\vartheta(m^2)-(2m+1).
\]

If

\[
E_m=\vartheta(m^2)-m^2,
\]

then

\[
\boxed{g_m=E_{m+1}-E_m}.
\]

Moreover

\[
\boxed{
d_m-g_m
=\sum_{m^2\le p<(m+1)^2}(2\log m-\log p).
}
\]

Thus the previously observed negative lag-1/lag-2 correlation of `d_m` is largely inherited from taking a discrete derivative of the Chebyshev error, plus a smooth within-bin correction. It is not by itself an independent prime interaction.

## 2. Local transport destroys finite-lag statistics but preserves the RH half-plane

The Beurling stability result used in this repository is:

if rank-matched generalized primes `q_j` and ordinary primes `p_j` satisfy

\[
|q_j-p_j|\le p_j^{1/2+o(1)},
\]

then

\[
\zeta_{\mathcal Q}(s)=\zeta(s)e^{H(s)}
\]

with `H` analytic in every half-plane `Re(s)>1/2`; hence both Euler products have the same zero/pole divisor there.

Now group consecutive square bins into blocks of length

\[
L(m)=m^{o(1)}.
\]

Arbitrarily permuting the counts `c_m` inside one such block moves the collapsed generalized primes by at most

\[
O(mL(m))=p^{1/2+o(1)}.
\]

Therefore these local permutations remain in the same RH-equivalent Beurling class, while finite-lag autocorrelations can change substantially.

Numerical example (`m\le4096`, block length 16): the actual normalized residual had approximately lag-1 `-0.137` and lag-2 `-0.088`, while within-block permutations moved the null means to roughly `-0.024` and `-0.023` respectively.

Hence fixed-lag local correlations are not necessary invariants of the right critical half-plane.

## 3. Square-bin count is an exact complete sieve

For

\[
I_m=[m^2,(m+1)^2),
\]

every composite integer in `I_m` has a prime divisor at most `m`. Conversely an integer in `I_m` with no prime factor at most `m` must be prime. Therefore

\[
\boxed{
c_m
=\#\{n\in I_m:(n,\prod_{p\le m}p)=1\}.
}
\]

By inclusion-exclusion,

\[
\boxed{
c_m=
\sum_{\substack{d\ \mathrm{squarefree}\\P^+(d)\le m}}
\mu(d)
\left(
\Big\lfloor\frac{(m+1)^2-1}{d}\Big\rfloor-
\Big\lfloor\frac{m^2-1}{d}\Big\rfloor
\right).
}
\]

This is not an approximate sieve representation: it is exact.

## 4. Linear-sieve parameter lands inside the parity barrier

The interval length is

\[
H=(m+1)^2-m^2=2m+1\asymp m,
\]

and the complete sieving limit is `z=m`.

Even if one optimistically grants a distribution level `D\asymp H`, the linear-sieve parameter is

\[
s=\frac{\log D}{\log z}=1+o(1).
\]

For the linear sieve the lower-bound function satisfies `f(s)=0` for `s\le2`. Thus the square-bin representation sits deeply inside the classical sieve parity range. Pure lower-bound sieve / truncated inclusion-exclusion cannot by itself reach the needed prime count.

Breaking this barrier requires additional bilinear / Type-II information, as in the asymptotic-sieve tradition. When expanded globally, those bilinear structures reconnect to classical von Mangoldt decompositions rather than yielding an independent RH mechanism.

## 5. Audit conclusion

The square-bin route remains a useful information-compression theorem:

\[
\text{exact prime positions}
\longrightarrow
\text{square-root-resolution counts}
\longrightarrow
\text{same zero divisor for Re(s)>1/2}.
\]

But two tempting follow-ups are closed:

1. fixed-lag `d_m` correlations are not RH invariants because RH-preserving local transport can alter them;
2. direct complete-sieve lower bounds hit the standard parity barrier.

Any further square-bin proof route must use a low-frequency / block-sum invariant that survives `p^{1/2+o(1)}` transport **and** contains genuinely bilinear arithmetic information not reducible to standard sieve decompositions.

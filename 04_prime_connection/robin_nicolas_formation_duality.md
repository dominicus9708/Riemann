# Robin–Nicolas formation duality audit

Date: 2026-09-16

## Status

- RH: `OPEN`.
- Colossally-abundant atom decomposition: `EXACT`.
- Legendre-dual Robin formulation: `EXACT` (apart from the standard finite startup range).
- Robin–Nicolas complement identity: `EXACT`.
- Leading complement asymptotic `2 sqrt(2)/(sqrt(x) log x)`: `ASYMPTOTIC / PNT`.
- Use as an independent RH proof: `CLOSED_AS_COMPLEMENTARY_REENCODING` at the present stage.

## 1. Prime-power formation atoms

For a prime `p` and exponent `a>=0`, let

\[
f_p(a)=\frac{\sigma(p^a)}{p^a}=\frac{1-p^{-(a+1)}}{1-p^{-1}}.
\]

The increment `a -> a+1` has horizontal and vertical weights

\[
x_{p,a}=\log p,
\]

\[
y_{p,a}=\log\frac{1-p^{-(a+2)}}{1-p^{-(a+1)}}.
\]

Define its slope

\[
\eta_{p,a}=\frac{y_{p,a}}{\log p}.
\]

For fixed `epsilon>0`, maximizing

\[
\log\frac{\sigma(n)}n-\epsilon\log n
\]

factorizes over primes, and the maximizing colossally-abundant state contains exactly the exponent-increment atoms with `eta_{p,a}>epsilon` (up to tie conventions). Hence the CA path is a decreasing-slope formation path.

## 2. Exact Legendre dual

Define

\[
\Phi_{CA}(\epsilon)=\sup_n\left[\log\frac{\sigma(n)}n-\epsilon\log n\right].
\]

Then exactly

\[
\boxed{
\Phi_{CA}(\epsilon)=\sum_p\sum_{a\ge0}(y_{p,a}-\epsilon\log p)_+.
}
\]

For the Robin boundary, with `t=log n`,

\[
B(t)=\gamma+\log\log t,
\]

and

\[
\Phi_B(\epsilon)=\sup_{t>1}[B(t)-\epsilon t].
\]

The stationary point satisfies

\[
t\log t=1/\epsilon.
\]

Writing `W` for Lambert W,

\[
T_0(\epsilon)=\frac1{\epsilon W(1/\epsilon)},
\]

\[
\boxed{
\Phi_B(\epsilon)=\gamma+\log W(1/\epsilon)-\frac1{W(1/\epsilon)}.
}
\]

At differentiability points,

\[
\Phi'_{CA}(\epsilon)=-\log n_{CA}(\epsilon),
\qquad
\Phi'_B(\epsilon)=-T_0(\epsilon).
\]

This gives a precise formation-spectrum formulation, but not a monotone-contraction theorem: the derivative difference can oscillate.

## 3. Prime-power activation layers

For `k>=1`, define

\[
\eta_k(x)=
\frac{\log((1-x^{-(k+1)})/(1-x^{-k}))}{\log x}.
\]

Let `X_k(epsilon)` solve `eta_k(X_k)=epsilon`. Then, aside from tie choices,

\[
\boxed{
\log n_{CA}(\epsilon)=\sum_{k\ge1}\vartheta(X_k(\epsilon)).
}
\]

If

\[
\epsilon=\frac1{T\log T},
\]

then for each fixed `k`,

\[
X_k(\epsilon)\sim(kT)^{1/k}.
\]

In particular

\[
X_1\sim T,
\qquad
X_2\sim\sqrt{2T}.
\]

Combining the first two layers with

\[
\vartheta(T)=\psi(T)-\vartheta(\sqrt T)-\vartheta(T^{1/3})-\cdots
\]

gives the leading formation balance

\[
\boxed{
\log n_{CA}-T
=(\sqrt2-1)\sqrt T+(\psi(T)-T)+o(\sqrt T)
}
\]

at the formal leading square-root level. After integrating in the dual parameter, the deterministic buffer is

\[
\boxed{
\frac{2(\sqrt2-1)}{\sqrt T\log T}.
}
\]

This reproduces the classical Ramanujan coefficient `2(sqrt(2)-1)` in the Robin asymptotic. It is therefore classified as a formation interpretation of known structure, not as a new RH proof.

## 4. Saturated prime columns give the Nicolas product

For a fixed prime, the entire exponent column telescopes:

\[
\boxed{
\sum_{a\ge0}y_{p,a}
=-\log(1-p^{-1}).
}
\]

Thus saturating every exponent column for `p<=x` gives

\[
P(x):=\log\prod_{p\le x}(1-p^{-1})^{-1}.
\]

Nicolas's primorial criterion is therefore the **saturated-column envelope** of the same prime-power formation from which Robin's CA path is obtained by slope truncation.

## 5. Exact Robin–Nicolas complement identity

Let `n=n_CA(epsilon)` be a CA state, let

\[
t=\log n,
\]

and let `x` be its largest prime divisor. Write

\[
A(n)=\log\frac{\sigma(n)}n,
\]

\[
G_R(n)=\gamma+\log\log t-A(n),
\]

and define the matched Nicolas logarithmic surplus

\[
G_N(x)=P(x)-\gamma-\log\log\vartheta(x).
\]

Since all primes `p<=x` occur in the CA support,

\[
P(x)-A(n)
=\sum_{p\le x}-\log(1-p^{-(a_p+1)})>0.
\]

Also `t>=theta(x)`. Direct cancellation yields

\[
\boxed{
G_R(n)+G_N(x)
=
[P(x)-A(n)]
+
\log\frac{\log t}{\log\vartheta(x)}
=:C(n,x)>0.
}
\]

This identity is unconditional and contains no zeta zeros.

Consequences:

- if the matched Nicolas inequality fails, `G_N<=0`, then the corresponding Robin gap is automatically positive: `G_R>=C>0`;
- if Robin fails at the CA state, `G_R<=0`, then the matched Nicolas inequality holds with surplus `G_N>=C>0`.

Thus matched Robin and Nicolas counterexamples cannot occur at the same support state.

## 6. Leading size of the complement

Let `x=X_1(epsilon)` and `y=X_2(epsilon)`. From the threshold equations,

\[
y\sim\sqrt{2x}.
\]

The scale-surplus term satisfies

\[
\log\frac{\log t}{\log\vartheta(x)}
\sim
\frac{\sqrt2}{\sqrt x\log x}.
\]

The saturation deficit is dominated by primes having exponent one, namely `y<p<=x`:

\[
P(x)-A(n)
\sim
\sum_{y<p\le x}\frac1{p^2}
\sim
\frac{\sqrt2}{\sqrt x\log x}.
\]

Hence

\[
\boxed{
C(n,x)
\sim
\frac{2\sqrt2}{\sqrt x\log x}.
}
\]

Numerically, the normalized complement `C sqrt(x) log x` is already close to `2sqrt(2)=2.828427...` by support near `10^6`.

## 7. Zero-wave split and why the combination does not prove RH

Under RH, Ramanujan's Robin asymptotic has the leading form

\[
G_R
\sim
\frac{2(\sqrt2-1)-W(x)}{\sqrt x\log x},
\]

where `W` denotes the zero-wave term (equivalently the `S_1` term in the standard notation, after matching the scale).

Nicolas's quantitative primorial asymptotic has the complementary form

\[
G_N
\sim
\frac{2+W(x)}{\sqrt x\log x}.
\]

Their sum is exactly compatible with

\[
2(\sqrt2-1)+2=2\sqrt2.
\]

Thus the common zero-wave cancels when the criteria are added.

This cancellation is not a proof mechanism. It removes exactly the spectral information that decides **how the positive total complement is split** between `G_R` and `G_N`. Under an off-critical zero, the normalized zero-wave acquires growing oscillation; positive phases can violate Robin while negative phases can violate Nicolas, at different scales. This is compatible with the known oscillation theorems when RH is false.

Therefore a naive strategy of 'combining two RH-equivalent inequalities so the zero terms cancel' is classified as

`COMPLEMENTARY_REENCODING`.

The remaining hard problem is a sign-splitting bound such as

\[
0<G_N(x)<C(n,x),
\]

but either side of this corridor already carries RH-level information.

## 8. Precision barrier

The derivative-level formation spectrum contains `psi(T)-T`. Standard unconditional PNT zero-free-region errors are far larger than the `sqrt(T)` formation buffer. After dual integration they remain much larger than the `1/(sqrt(T) log T)` Robin gap. Therefore existing PNT error terms cannot settle the sign by a direct majorization argument.

Moreover, even under RH the derivative gap need not be positive pointwise; only the integrated dual gap is controlled. Hence an attempted proof based on monotonicity of `log n_CA(epsilon)-T_0(epsilon)` would be stronger than what RH itself naturally supplies and is not supported by the observed CA sawtooth path.

## 9. Prior-art boundary

Relevant established results include:

- Alaoglu–Erdos: structure of colossally abundant numbers.
- Robin: RH equivalence via `sigma(n)<e^gamma n log log n` for `n>5040`.
- Nicolas: RH equivalence via the primorial Euler-totient inequality and quantitative estimates for its normalized defect.
- Ramanujan / later Nicolas: the `2(sqrt(2)-1)` divisor-sum asymptotic and zero-wave `S_1`.

The atom/Legendre and matched-complement language is used here as an audit/formation reorganization. No novelty claim is made solely from the absence of an identical formulation in a targeted literature search.

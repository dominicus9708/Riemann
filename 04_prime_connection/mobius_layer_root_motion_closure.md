# Möbius Layer Root-Motion Closure

Date: 2026-09-15

## setup

Let

\[
G_N(z)=\sum_{n\le N}\mu(n)^2z^{\omega(n)}.
\]

For sufficiently large N, let `rho_N` denote the unique real zero in the Selberg--Delange neighborhood of `z=-1` established in `mobius_layer_root_criterion_audit.md`.

If N is not squarefree, then

\[
G_N=G_{N-1}
\]

and therefore

\[
\boxed{\rho_N=\rho_{N-1}}.
\]

If N is squarefree and `k=omega(N)`, then

\[
\boxed{G_N(z)=G_{N-1}(z)+z^k.}
\]

## exact root-motion identity

Since

\[
G_{N-1}(\rho_{N-1})=0,
\qquad
G_N(\rho_N)=0,
\]

we have

\[
G_{N-1}(\rho_N)-G_{N-1}(\rho_{N-1})=-\rho_N^k.
\]

By the real mean-value theorem, for some `xi_N` between the two roots,

\[
\boxed{
\rho_N-\rho_{N-1}
=-\frac{\rho_N^{\omega(N)}}{G'_{N-1}(\xi_N)}.
}
\]

This is exact whenever the distinguished real branch exists at N-1 and N.

## eventual sign law

The local Selberg--Delange estimate gives uniformly on the root neighborhood

\[
G'_{N-1}(z)
=-\frac{N}{\log^2N}(1+o(1))<0.
\]

Also `rho_N<0` eventually. For squarefree N,

\[
\operatorname{sgn}(\rho_N^{\omega(N)})
=(-1)^{\omega(N)}
=\mu(N).
\]

Therefore

\[
\boxed{
\operatorname{sgn}(\rho_N-\rho_{N-1})=\mu(N)
}
\]

for all sufficiently large squarefree N.

Thus the local root trajectory cannot be eventually monotone: its direction directly reproduces the Möbius sign.

## asymptotic step size

The unconditional Mertens bound implies

\[
\rho_N+1=o(1/\omega(N)),
\]

so

\[
\rho_N^{\omega(N)}
=(-1)^{\omega(N)}(1+o(1))
=\mu(N)(1+o(1)).
\]

Together with the derivative estimate,

\[
\boxed{
\rho_N-\rho_{N-1}
=\mu(N)\frac{\log^2N}{N}(1+o(1))
}
\]

on squarefree activations, and the step is exactly zero on nonsquarefree N.

Hence the root motion is a logarithmically weighted re-encoding of the original Möbius increments.

## normalized coordinate

The root criterion already gives

\[
\boxed{
\frac{N}{\log^2N}(\rho_N+1)=M(N)(1+o(1)).
}
\]

So both position and velocity of the distinguished root carry asymptotically the same information as the Mertens endpoint and its increments.

There is no independent contraction law exposed by the one-dimensional root branch.

## finite-X caution

The asymptotic distinguished root need not exist as a separated real branch at small X. In exact dyadic/intermediate computations, real roots near -1 can temporarily collide and become a complex pair before returning. Therefore no finite-X interlacing claim is made.

This does not affect the eventual theorem, whose neighborhood shrinks according to the unconditional Mertens bound.

## verdict

- exact root update: `EXACT`.
- eventual root-motion sign = Möbius sign: `DERIVED EXACT SIGN LAW` once the asymptotic local branch exists.
- step size `mu(N) log^2 N/N`: `ASYMPTOTIC`.
- monotonicity/contraction route: `CLOSED`.
- near-minus-one root criterion remains useful as an algebraic RH reformulation, but not as an independent proof mechanism.

The research front should return to genuinely multivariate, prime-weight-sensitive incomplete-boundary structure rather than the diagonal layer polynomial alone.

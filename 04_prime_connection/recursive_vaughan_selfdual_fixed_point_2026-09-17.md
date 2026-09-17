# Recursive Vaughan self-dual fixed-point barrier — 2026-09-17

## Status
- Riemann hypothesis: OPEN.
- Symmetric second decomposition of the long Möbius factor: AUDITED.
- Natural Vaughan threshold for a reciprocal phase: DERIVED.
- Balanced Type-II + coefficient expansion returns to the same B-process self-dual scale at every recursive generation.
- Repeated symmetric Vaughan decomposition alone: NOT an automatic source of polynomial saving.

## 1. Abstract reciprocal Möbius module

Consider a dyadic module

\[
\mathcal S(Y,X)
=
\sum_{m\asymp Y}\mu(m)c_m
 e\!\left(X\left(\frac mY\right)^{-1/2}\right),
\]

where `c_m` is slowly varying or is frozen at the current decomposition level.

The phase has derivative scale

\[
\left|\frac{d}{dm}
X(m/Y)^{-1/2}\right|
\asymp \frac XY.
\]

After a Type-I factorization `m=de`, the cofactor has length `Y/d`, and the derivative in `e` has scale

\[
\asymp \frac{Xd}{Y}.
\]

Therefore the natural Type-I first-derivative threshold is

\[
\boxed{
Q:=\frac YX.
}
\]

Indeed `d<=Q` is the regime in which the derivative remains at or below unit scale up to endpoint-resonance corrections.

## 2. Natural symmetric Vaughan choice

Choose

\[
U=V=Q^{1/2}.
\]

Then `UV=Q`, exactly as in the first-generation reciprocal Vaughan audit.

The Type-II term has a non-Möbius coefficient

\[
b_d=\sum_{\substack{c\mid d\\c>V}}\mu(c).
\]

In a balanced Type-II box one has

\[
d\asymp w\asymp Y^{1/2}.
\]

Expand

\[
d=cr,
\qquad c>V=Q^{1/2}.
\]

The longest possible smooth cofactor is therefore

\[
R_{\max}
\asymp
\frac{Y^{1/2}}{Q^{1/2}}.
\]

Since `Q=Y/X`,

\[
\boxed{
R_{\max}
\asymp
\sqrt X.
}
\]

## 3. Reciprocal B-process fixed point

For a reciprocal monomial phase of normalized amplitude `X` on a variable of length `R`, the B-process dual length is

\[
R^*\asymp\frac XR.
\]

Hence the self-dual length is

\[
R=R^*=\sqrt X.
\]

Combining with the previous section gives

\[
\boxed{
\text{natural Vaughan threshold}
\to
\text{balanced Type II}
\to
\text{expand }b_d
\to
R_{\max}=\sqrt X
}
\]

which is exactly the B-process self-dual point.

This is an algebraic scale identity, not a finite-range numerical observation.

## 4. Recursive application to a long Möbius factor

Suppose the first Type-II box is unbalanced and the longer factor is the actual Möbius variable. Freeze all other factors and regard that long factor as a new module of length `Y_1` with normalized reciprocal amplitude `X_1`.

The same calculation gives its natural threshold

\[
Q_1=\frac{Y_1}{X_1}.
\]

A symmetric second-generation Vaughan decomposition with

\[
U_1=V_1=Q_1^{1/2}
\]

followed by expansion of its non-Möbius coefficient again creates, in the balanced daughter Type-II box,

\[
R_{1,\max}
\asymp
\frac{Y_1^{1/2}}{Q_1^{1/2}}
=\sqrt{X_1}.
\]

Thus the construction reproduces the B-process self-dual scale at the next generation.

The same argument iterates.

Classification:

`RECURSIVE_VAUGHAN_SELFDUAL_FIXED_POINT`.

## 5. Connection with the first-generation `(N,D)` module

For the Voronoi–Möbius block,

\[
Y=D,
\qquad
X=X_0=\frac{K\sqrt N}{\sqrt D},
\]

and

\[
Q=\frac D{X_0}
=\frac{D^{3/2}}{K\sqrt N}
=H.
\]

So the previously introduced resolution width `H` is exactly the abstract natural Vaughan threshold `Y/X`.

The identities

\[
HX_0=D,
\qquad
U=V=\sqrt H,
\qquad
R_{\max}=\sqrt{X_0}
\]

are therefore one instance of the general fixed-point mechanism above.

## 6. Extreme corner check

At

\[
D=K,
\qquad N=1,
\]

one has

\[
X_0=K^{1/2},
\qquad H=K^{1/2},
\qquad \sqrt{X_0}=K^{1/4}.
\]

The first balanced daughter cofactor is of length `K^(1/4)`. If one instead follows an unbalanced long Möbius factor and decomposes it again with its own natural reciprocal threshold, its balanced daughter again terminates at the corresponding `sqrt(X_1)` self-dual scale rather than producing a parametrically longer smooth factor.

## 7. What this closes and what it does not

This audit closes the following naive expectation:

> repeated symmetric Vaughan decomposition will eventually expose an increasingly long smooth factor on which an ordinary B-process gives the missing power saving.

At the natural derivative thresholds, the balanced daughter box is a fixed point of the scale map and does not automatically become easier.

This does **not** prove that all iterated identities fail. Possible exits remain:

1. deliberately asymmetric Vaughan parameters rather than `U=V=sqrt(Q)`;
2. using arithmetic signs before the balanced daughter box is collapsed by Cauchy;
3. combining two generations into a genuinely multilinear mean-value estimate;
4. a transformation that changes the reciprocal exponent, not merely the factor lengths.

## 8. Next direct calculation

The next calculation should optimize **asymmetric** parameters

\[
U=Q^\theta,
\qquad
V=Q^{1-\theta}
\]

subject to `UV=Q`, and measure simultaneously:

- Type-I cost;
- daughter smooth-cofactor length;
- B-process dual length;
- surviving Möbius-factor lengths.

If every `theta` merely transfers the loss between Type I and one Type-II orientation, the entire pure-Vaughan/B-process family can be closed as a scale barrier. If a non-symmetric window lowers the worst exponent, that window becomes the next live branch.
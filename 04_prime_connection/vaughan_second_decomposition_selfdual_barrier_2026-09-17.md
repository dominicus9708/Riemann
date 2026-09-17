# Vaughan second-decomposition / self-dual barrier audit — 2026-09-17

## Status
- Riemann hypothesis: OPEN.
- Expansion of the non-Möbius Vaughan Type-II coefficient: EXACT.
- New unweighted cofactor variable: EXACT.
- Balanced Type-II box: the new cofactor lands exactly at the reciprocal B-process self-dual length.
- Pure second-decomposition + smooth-variable B-process: DOES NOT automatically close the balanced box.
- Unbalanced boxes with the non-Möbius factor larger than `sqrt(D)`: may gain and remain worth separating.

## 1. Exact Möbius Vaughan Type-II structure

Use the Möbius Vaughan decomposition in the Green–Tao form. On a dyadic Type-II box the relevant term has schematic shape

\[
\sum_{d\asymp M} b_d
\sum_{w\asymp L}\mu(w)
 f(dw),
\qquad ML\asymp D,
\]

where

\[
\boxed{
 b_d=\sum_{\substack{c\mid d\\c>V}}\mu(c).
}
\]

In the reciprocal-phase application

\[
f(r)=e\!\left(2K\sqrt n\,r^{-1/2}\right).
\]

The first-generation audit chose

\[
U=V=H^{1/2},
\qquad
H:=\frac{D^{3/2}}{K\sqrt N},
\]

so that `UV=H` is aligned with the Type-I derivative threshold.

## 2. Expand `b_d` before Cauchy

Write

\[
d=cr,
\qquad c>V.
\]

Then the Type-II box becomes a trilinear arithmetic sum

\[
\sum_{c}\mu(c)
\sum_r
\sum_w\mu(w)
 e\!\left(2K\sqrt n\,(crw)^{-1/2}\right),
\]

with the dyadic restrictions

\[
c\asymp C,
\qquad r\asymp R,
\qquad w\asymp L,
\qquad CR\asymp M,
\qquad CRL\asymp D.
\]

The important point is that `r` is an **unweighted smooth cofactor**.

## 3. Reciprocal phase amplitude and exact scale identity

On a `(N,D)` block define

\[
X_0:=\frac{K\sqrt N}{\sqrt D}.
\]

The previously derived resolution width is

\[
H=\frac{D^{3/2}}{K\sqrt N}.
\]

Therefore the two scales satisfy the exact scale relation

\[
\boxed{H X_0=D.}
\]

Equivalently,

\[
\boxed{X_0=\frac DH.}
\]

This relation is the key to the second-decomposition geometry.

## 4. B-process self-dual length for the smooth cofactor

For fixed `n,c,w`, the `r`-phase is

\[
\phi(r)=A r^{-1/2}
\]

with normalized amplitude `X_0` across a dyadic `r`-block of length `R`.

The derivative scale is

\[
|\phi'(r)|\asymp\frac{X_0}{R},
\]

so the van der Corput B-process has a dual length of scale

\[
R^*\asymp\frac{X_0}{R}.
\]

Hence the self-dual point is

\[
\boxed{R\asymp\sqrt{X_0}.}
\]

A B-process can only be expected to shorten the variable automatically when `R` is appreciably larger than `sqrt(X_0)`.

## 5. Balanced Type-II box lands exactly at self-duality

Take the balanced factor geometry

\[
M\asymp L\asymp\sqrt D.
\]

Since `c>V=sqrt(H)`, the longest possible cofactor from the exact expansion `d=cr` is

\[
R_{\max}
\asymp
\frac{\sqrt D}{\sqrt H}.
\]

Using `D/H=X_0`,

\[
\boxed{
R_{\max}
\asymp
\sqrt{\frac DH}
=\sqrt{X_0}.
}
\]

Thus the second Vaughan decomposition exposes a smooth variable, but **precisely at the reciprocal B-process self-dual length**.

This is not a numerical coincidence and does not depend on the extreme choice `D=K,N=1`.

Permanent classification:

`VAUGHAN_SECOND_DECOMPOSITION_SELFDUAL_BARRIER`.

## 6. Extreme unresolved corner as a check

For

\[
D=K,
\qquad N=1,
\]

we have

\[
H=K^{1/2},
\qquad
X_0=K^{1/2},
\qquad
U=V=K^{1/4}.
\]

In the balanced box `M~L~K^(1/2)`, the smallest admissible divisor scale is `C~K^(1/4)`, so

\[
R_{\max}\asymp K^{1/4}=\sqrt{X_0}.
\]

The B-process therefore transforms a length `K^(1/4)` sum to another length of the same power. No automatic polynomial saving is created.

## 7. Unbalanced boxes

Write

\[
M=\lambda\sqrt D,
\qquad
L=\lambda^{-1}\sqrt D.
\]

At the smallest divisor scale `C~sqrt(H)`,

\[
R_{\max}
\asymp
\frac{M}{\sqrt H}
=\lambda\sqrt{X_0}.
\]

Therefore:
- if `lambda>1`, the non-Möbius factor `d` is larger than `sqrt(D)` and the exposed smooth cofactor can lie beyond self-duality; a B-process may shorten it;
- if `lambda=1`, one is exactly self-dual;
- if `lambda<1`, the cofactor is shorter than self-dual and a plain B-process does not provide an automatic length gain.

Thus route 2 can potentially prune the **large-`d` unbalanced half**, but it does not remove the balanced core or the side where the large factor is the Möbius variable `w`.

## 8. Consequence for the next proof search

The remaining hard region is no longer described merely as a generic three-variable monomial sum.

After the exact second decomposition, the obstruction is concentrated where

1. the available smooth cofactor has length at most the self-dual reciprocal scale;
2. the longer factor, when present, is the actual Möbius variable rather than a smooth coefficient;
3. unsigned spacing/B-process transformations therefore cannot extract the required power saving without using arithmetic signs.

This narrows the next candidates to:

- a **Möbius-sensitive B/A-process** on the long factor;
- a symmetric/iterated Vaughan or Heath–Brown decomposition that exposes a smooth factor on the opposite orientation without enlarging the Type-I loss;
- a weighted double-large-sieve estimate that carries the `mu(c)mu(w)` signs through the spacing step.

## 9. Audit warning

Do not count the mere appearance of an unweighted cofactor after expanding `b_d` as progress toward the RH-scale bound. In the balanced Type-II box its maximum natural length is forced by `HX_0=D` to equal the B-process self-dual length.

The next direct calculation should test whether a **symmetric second decomposition of the long Möbius factor** creates a genuinely longer smooth variable or merely reproduces the same self-dual geometry.
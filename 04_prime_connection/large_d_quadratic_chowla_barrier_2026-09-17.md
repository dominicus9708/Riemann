# Large-d quotient quadratic / Chowla barrier audit — 2026-09-17

## Status
- Riemann hypothesis: OPEN.
- Linear/Abel/dyadic quotient routes: previously closed.
- Quadratic-energy lift of the large-d quotient side: EXACT reduction to weighted Möbius two-point correlations.
- Pointwise RH-scale closure from current averaged Chowla technology: NOT AVAILABLE.
- Growing-depth nonlinear quotient route: still OPEN, but must exceed averaged/log-averaged correlation input.

## 1. Large-d quotient sum

Let

\[
U_q(N)=
M\!\left(\left\lfloor\frac Nq\right\rfloor\right)
-
M\!\left(\left\lfloor\frac N{q+1}\right\rfloor\right)
\]

and

\[
T_Q(N)=\sum_{q\le Q}B(q)U_q(N).
\]

Equivalently,

\[
T_Q(N)=\sum_d \mu(d)W_{N,Q}(d),
\]

where `W_{N,Q}` is the deterministic step weight equal to `B(q)` on

\[
N/(q+1)<d\le N/q.
\]

## 2. Squaring does not create free positivity

A natural nonlinear attempt is to study

\[
|T_Q(N)|^2.
\]

Expanding gives exactly

\[
\boxed{
|T_Q(N)|^2
=
\sum_{d,e}
\mu(d)\mu(e)
W_{N,Q}(d)W_{N,Q}(e).
}
\]

The diagonal `d=e` is controlled by the squarefree support. The off-diagonal is a weighted two-point Möbius correlation.

Writing `e=d+h`, the off-diagonal may be reorganized schematically as

\[
\sum_{h\ne0}
\sum_d
\mu(d)\mu(d+h)
W_{N,Q}(d)W_{N,Q}(d+h).
\]

Thus quadratic positivity merely moves the problem from one-point Mertens cancellation to two-point Möbius cancellation.

Classification:

`QUOTIENT_QUADRATIC_CHOWLA_REENTRY`.

## 3. Why current Chowla technology does not close the pointwise problem

The Chowla conjecture predicts cancellation in fixed-shift sums such as

\[
\sum_{n\le X}\mu(n)\mu(n+h).
\]

Strong modern results prove averaged forms over shifts and logarithmically averaged two-point forms, and related averaged short-interval estimates.

Those theorems are highly relevant as controls, but the present RH route requires a bound for a **specific deterministic weight at a specific cutoff N**.

An average over `N`, an average over shifts `h`, or a logarithmic average in the summation variable does not directly imply the pointwise estimate required to force

\[
T_Q(N)=O_\varepsilon(N^{1/2+\varepsilon})
\]

for every large `N`.

Therefore current averaged Chowla technology cannot be inserted as a black box to finish the large-d quotient side.

## 4. Relation to bounded quotient depth

The previous Mellin audit showed:

- `q=1` alone is fully sensitive to every nontrivial zeta zero;
- fixed finite quotient depth is a finite Mellin multiplier and cannot erase the full zeta spectrum.

The present quadratic audit adds:

- replacing a growing family of quotient blocks by an energy estimate introduces pair correlations;
- simple Cauchy-Schwarz loses the signed cross-block information;
- recovering RH scale requires cancellation among the off-diagonal pair terms.

Hence the difficulty does not disappear when passing from linear to quadratic structure; it changes category from Mertens cancellation to Chowla-type correlation.

## 5. Mean-square versus pointwise distinction

Averaging `|T_Q(N)|^2` over `N` may be approachable using mean-value theorems for multiplicative functions and averaged correlation technology.

Such a result would still be a different statement from the RH-equivalent pointwise bound.

Permanent guard:

`AVERAGED_CHOWLA_POINTWISE_GAP` — mean-square, shift-averaged, or logarithmically averaged Möbius correlation control must not be promoted to pointwise RH-scale quotient cancellation without an explicit de-averaging theorem.

## 6. Surviving nonlinear target

A genuinely new large-d mechanism would need one of the following:

1. a deterministic growing-depth identity that pairs quotient blocks before taking absolute values and produces a one-sided reserve;
2. a pointwise weighted two-point (or higher-order) Möbius correlation theorem strong enough for the specific quotient geometry;
3. a nonlinear arithmetic invariant that uses multiplicativity across quotient scales without expanding into an uncontrolled Chowla hierarchy.

If a proposed nonlinear construction expands into generic pair correlations and then invokes Cauchy-Schwarz or averaged Chowla, classify it as re-entry rather than independent RH progress.

Suggested tags:

- `QUOTIENT_QUADRATIC_CHOWLA_REENTRY`;
- `AVERAGED_CHOWLA_POINTWISE_GAP`.

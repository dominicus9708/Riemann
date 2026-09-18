# Vaughan-edge ordered large-prime sector scale audit — 2026-09-18

## Status
- Riemann hypothesis: OPEN.
- Context: critical Vaughan edge (V=K^{1/4}), (L=V^3=K^{3/4}), reciprocal amplitude (X=V^2=K^{1/2}).
- Previous bounded-tail audit: for squarefree (w\asymp L), the number of prime factors (>V) is at most 3.
- New exact scale classification: writing (w=a p_1\cdots p_j), the hardest (j=1) sector has a genuine transition at (a\asymp V), (p\asymp V^2).
- Finite sector audit: (j=1) is the largest observed sector in the tested edge models, but it is not separated from random-sign controls.
- No proof closure is claimed.

## 1. Scale parametrization

Write
[
a=V^\alpha,qquad p_i=V^{\beta_i},
]
up to dyadic constants. Since (w\asymp V^3),
[
\boxed{\alpha+\sum_{i=1}^j\beta_i=3,qquad \beta_i\ge1.}
]

The full phase on a normalized product block has oscillatory amplitude
[
\boxed{X\asymp V^2.}
]

For any one variable of length
[
R=V^\rho
]
with all other normalized factors frozen, the reciprocal-square-root phase has
[
|f''|\asymp \frac{X}{R^2}=V^{2-2\rho}.
]

The ordinary second-derivative estimate gives
[
\sum_{r\asymp R}e(f(r))
\ll
R\sqrt{|f''|}+|f''|^{-1/2}
\asymp
\boxed{V+V^{\rho-1}.}
]

This is an **unweighted integer-sum benchmark only**. It cannot be transferred automatically to prime or Möbius weighted variables.

## 2. Consequence of the benchmark

Compared with the trivial length (V^\rho):
- (\rho=1): no power saving;
- (1<\rho<2): saving (V^{\rho-1});
- (\rho=2): saving exactly (V);
- (\rho>2): the bound (V^{\rho-1}) again gives a saving (V).

Thus a single unweighted factor of length at least (V^2) is, at the level of phase geometry, capable of supplying the entire missing (V)-saving of the edge Type-II problem.

## 3. Sector (j=1)

Write
[
w=ap,qquad P^+(a)\le V,qquad p>V.
]

Then
[
\alpha+\beta=3.
]

There are three scale zones.

### 3.1 Small residual: (a\ll V)

Then (eta>2), so (p\gg V^2). The prime variable is long enough that the unweighted reciprocal phase alone has a full (V)-saving.

Any obstruction here is therefore a **prime-weight transfer problem**, not a lack of analytic curvature.

### 3.2 Transition residual: (a\asymp V)

Then
[
\boxed{a\asymp V,qquad p\asymp V^2.}
]

This is the exact transition point:
[
|f''(p)|\asymp V^{-2}\asymp p^{-1}.
]

For ordinary integer coefficients,
[
\sum_{p\text{-variable as integers}}e(f)
\ll V,
]
which is exactly the size needed after summing the two (V)-scale outer variables.

For actual primes, however, one would need a theorem at essentially square-root scale for a reciprocal fractional-power phase. The general prime exponential-sum sources identified in the current literature audit provide nontrivial power savings but no direct theorem was identified that gives this exact uniform (V^{1+\varepsilon}) bound in the present transition range.

Classification:
[
\boxed{\texttt{J1_PRIME_RECIPROCAL_TRANSITION_OPEN}.}
]

### 3.3 Large residual: (V\ll a\lesssim V^2)

Then (V\lesssim p\ll V^2). The prime variable alone no longer supplies the full benchmark saving. The missing curvature has moved into the (V)-smooth Möbius cofactor (a).

Thus the sector interpolates continuously between
- a prime-weight oscillation problem, and
- a smooth-Möbius parity problem.

The transition (a\asymp V) is therefore the correct first target.

## 4. Sector (j=2)

Now
[
w=ap_1p_2,qquad \alpha+\beta_1+\beta_2=3,
qquad \alpha\le1.
]

If ordinary second-derivative savings from the two prime variables could be multiplied independently, their total phase saving would have scale
[
V^{(\beta_1-1)+(\beta_2-1)}
=
V^{1-\alpha}.
]

Hence for (\alpha>0) a residual factor (V^\alpha) is still missing. This is exactly the size carried by the small (V)-smooth Möbius cofactor.

Therefore generic one-variable curvature does not by itself close every (j=2) scale.

Classification:
[
\texttt{J2_RESIDUAL_SMOOTH_PARITY_REMAINS}.
]

## 5. Sector (j=3)

Here
[
\alpha+\beta_1+\beta_2+\beta_3=3,qquad \beta_i\ge1,
]
so asymptotically
[
\alpha=0,qquad \beta_1=\beta_2=\beta_3=1
]
at power scale.

Thus all three large-prime variables are (V^{1+o(1)})-scale and no single variable gives a polynomial saving under the second-derivative benchmark.

Any saving must be genuinely multilinear / joint-spacing in nature.

Classification:
[
\texttt{J3_BALANCED_MULTIPRIME_GEOMETRY}.
]

## 6. Finite false-control audit

The model
[
\sum_{d\asymp V}\mu(d)
\sum_{w\asymp V^3}\mu(w)
e\!\left(
V^2(d/V)^{-1/2}(w/V^3)^{-1/2}
\right)
]
was decomposed by the number
[
j=\#\{p\mid w:p>V\}.
]

Tested:
[
V=10,15,20,25,30.
]

The (j=1) sector was the largest or among the largest nonempty sectors throughout the useful range. At (V=20,25,30), its absolute size divided by the edge target (V^3) was approximately
[
0.0257,quad0.0258,quad0.0118.
]

However random signs on the same squarefree support produce values of the same order. Therefore:
- the finite audit only prioritizes (j=1);
- it is not evidence for Möbius-specific cancellation;
- it is not evidence for RH.

Data:
`data/mertens/vaughan_edge_large_prime_sector_audit_2026-09-18.csv`.

## 7. Literature position

Two current benchmarks matter.

1. Granville–Lamzouri (2026) prove strong bounds for **linear** additive twists of multiplicative functions restricted to smooth numbers. This is relevant to the (V)-smooth residual sectors, but a direct Fourier transfer of the nonlinear reciprocal phase incurs a stationary-band cost and does not immediately close the present block.

2. Maynard–Pandey–Radziwiłł (2026) improve linear exponential sums over primes to a (N^{19/24+o(1)})-type generic term. This is again a linear-phase result and does not directly supply the square-root-scale reciprocal monomial estimate required at (p\asymp V^2).

Do not treat either source as a closure theorem for the present nonlinear edge problem.

## 8. New active target

The first exact subproblem is now

[
\boxed{
\sum_{p\asymp P}\Lambda(p)
e\!\left(Cp^{-1/2}\right)
\quad
\text{with }
P\asymp V^2,;
C\asymp P^{3/2},
}
]
or its prime-unweighted partial-summation counterpart, uniformly in the dyadic constants inherited from (d\asymp a\asymp V).

The target scale is
[
\boxed{P^{1/2+\varepsilon}=V^{1+\varepsilon}.}
]

This target should next be audited against general smooth-phase prime exponential-sum theorems. If known theory only gives (P^{1-\delta}) with (\delta<1/2), record the exact exponent deficit rather than treating 'nontrivial' as sufficient.

Permanent guards:
- `UNWEIGHTED_CURVATURE_NOT_PRIME_WEIGHT_TRANSFER`.
- `SECTOR_NUMERICS_NOT_MOBIUS_EVIDENCE`.
- `J1_TRANSITION_FIRST`.

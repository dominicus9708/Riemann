# j=2 centered-variance Mellin reformulation and H-loss barrier — 2026-09-19

## Status
- Riemann hypothesis: OPEN.
- Context: j=2 sharp fixed-range E2-type centered variance branch.
- Purpose: test whether the required short-interval variance becomes routine after Mellin/Dirichlet-polynomial reformulation.
- Result: the same missing factor H reappears exactly as a fourth-moment barrier.
- Consequence: centered variance remains a useful sufficient condition, but it should not be treated as the unique or necessary closure route.
- Classification: `J2_CENTERED_VARIANCE_MELLIN_H_BARRIER`.

## 1. Scale conversion

At the sharp endpoint,
[
S=H^5.
]

The arithmetic short-interval/cell length is
[
H.
]

The corresponding multiplicative/Mellin resolution height is
[
oxed{
T:=rac{S}{H}=H^4.
}
]

Therefore
[
oxed{
D=H^2=T^{1/2},
qquad
P=H^3=T^{3/4}.
}
]

This is a critical mixed-length Dirichlet-polynomial geometry.

## 2. Normalized product polynomial

Suppressing harmless logarithmic factors, normalize the coefficient L2 masses and write
[
A(t)
=
sum_{aasymp D}
rac{alpha_a}{sqrt a},a^{-it},
]
and
[
mathcal P(t)
=
sum_{pasymp P}
rac{lambda_p}{sqrt p},p^{-it},
]
where (lambda_p) denotes a normalized prime/von-Mangoldt coefficient.

Then the restricted semiprime polynomial is
[
F(t)=A(t)mathcal P(t).
]

The coefficient support has total product length
[
DP=S=T^{5/4},
]
which is longer than the Mellin window T by precisely
[
S/T=H=T^{1/4}.
]

## 3. Diagonal-scale mean-square target

Gallagher/Selberg transfer identifies the Poisson-scale centered short-interval target with a diagonal-scale mean-square estimate of the schematic form
[
oxed{
int_{|t|lesssim T}
|A(t)mathcal P(t)|^2,dt
ll_arepsilon
T^{1+arepsilon}.
}
]

The diagonal contribution is naturally of this order after coefficient normalization.

A generic mean-value theorem for the full product polynomial of length S instead sees
[
T+Sasymp S=HT,
]
and is therefore larger by exactly H.

Thus the short-interval H-saving and the long-polynomial off-diagonal saving are the same problem.

## 4. Fourth-moment Cauchy barrier

Apply Cauchy:
[
int |A|^2|mathcal P|^2
le
left(int|A|^4ight)^{1/2}
left(int|mathcal P|^4ight)^{1/2}.
]

### A-side

The A polynomial has length
[
D=T^{1/2}.
]

Its square has length (D^2=T), so the standard fourth-moment scale is
[
int_{|t|lesssim T}|A(t)|^4dt
ll_arepsilon
T^{1+arepsilon}.
]

### Prime side

The prime polynomial has length
[
P=T^{3/4}.
]

Its square has length
[
P^2=T^{3/2},
]
well beyond the t-window.

Without exploiting additional connected arithmetic cancellation, the generic fourth-moment scale is
[
int_{|t|lesssim T}|mathcal P(t)|^4dt
ll_arepsilon
T^{3/2+arepsilon}.
]

Therefore Cauchy gives
[
int |A|^2|mathcal P|^2
ll_arepsilon
T^{5/4+arepsilon}.
]

Since
[
T^{1/4}=H,
]
this is
[
oxed{
TH
}
]
rather than the desired T.

Thus:
[
oxed{
	ext{generic fourth-moment Cauchy loses exactly one factor }H.
}
]

Permanent rule:
`MELLIN_FOURTH_MOMENT_REPRODUCES_FULL_H_DEFICIT`.

## 5. Consistency with the other formulations

The same H appears as:

1. common DLS cell-variance raw/target ratio:
   [
   HS/S=H;
   ]

2. determinant-shell raw/target ratio:
   [
   H^6/H^5=H;
   ]

3. Mellin total-length/window ratio:
   [
   S/T=H;
   ]

4. fourth-moment Cauchy loss:
   [
   T^{5/4}/T=H.
   ]

This four-way agreement shows that the H deficit is not a normalization accident.

Classification:
`J2_H_DEFICIT_REPRESENTATION_INVARIANT_WITHIN_VARIANCE_ROUTE`.

## 6. Relation to existing mean-value literature

Classical and modern work on zeta times Dirichlet polynomials can cross the square-root-length barrier in special coefficient geometries, including special products and Kloosterman-assisted configurations.

However the present target is not a direct zeta-twisted second moment:
- A carries Möbius/divisor-bounded arithmetic structure;
- (mathcal P) is a dyadic prime polynomial;
- the exact lengths are (T^{1/2}) and (T^{3/4});
- the desired estimate requires cancellation in their **joint** off-diagonal.

Therefore existing zeta-polynomial mean-square theorems are comparison tools, not current closure theorems.

## 7. Evans correlation comparison

Evans's general E2 correlation theorem applies to almost all shifts in the present polynomial shift range (H=S^{1/5}).

This is evidence that the shifted-E2 geometry is analytically accessible on average.

But an almost-all correlation asymptotic with logarithmic exceptional/error saving does not imply
[
int|Amathcal P|^2ll T^{1+arepsilon},
]
because the latter demands the full polynomial gain
[
H^{-1}=T^{-1/4}
]
relative to the raw off-diagonal scale.

Permanent guard:
`E2_ALMOST_ALL_CORRELATION_NOT_DIAGONAL_MELLIN_MEAN_SQUARE`.

## 8. Methodological consequence

The common centered-cell variance theorem remains a sufficient route:

[
	ext{diagonal E2 variance}
Longrightarrow
j=2	ext{ closure}.
]

But the project must preserve the earlier rule
[
oxed{
	exttt{CENTERED_VARIANCE_SUFFICIENT_NOT_NECESSARY}.
}
]

If the variance branch requires an unavailable four-prime/E2 Poisson-scale theorem, this does not imply failure of the original reciprocal-phase sector.

The alternative route is to retain the original post-spacing reciprocal phase and seek only the specific signed Fourier component needed by the j=2 sum, rather than controlling the entire centered fluctuation energy.

## 9. Next split

Maintain two branches:

### Branch V — variance
Search for a coefficient-sensitive mean-value theorem that directly treats
[
T^{1/2}	imes T^{3/4}
]
Möbius-prime product polynomials at diagonal mean-square scale.

### Branch P — phase-adapted residual
Return to the original reciprocal phase and derive a weaker signed residual condition that does not imply the full E2 short-interval variance theorem.

The project should prefer Branch P if Branch V only re-enters currently unavailable Poisson-scale E2 variance.

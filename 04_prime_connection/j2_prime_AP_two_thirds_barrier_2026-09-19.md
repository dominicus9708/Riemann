# j=2 prime-AP black-box exponent barrier — 2026-09-19

## Status
- Riemann hypothesis: OPEN.
- Context: (j=2) sharp centered dispersion, with prime length (P), small-factor/modulus scale (D=P^{2/3}), shift range (H=P^{1/3}).
- Conclusion: currently available black-box mean-value theorems for primes in arithmetic progressions do not directly reach the required generic modulus scale (P^{2/3}).
- Therefore any closure must use the extra shift/bilinear reciprocal structure, not only ordinary AP equidistribution.
- Classification: `J2_PRIME_AP_TWO_THIRDS_BARRIER`.

## 1. Sharp rescaling

From
[
S=V^{5/2},
qquad
D=V,
qquad
P=V^{3/2},
qquad
H=V^{1/2},
]
we obtain
[
oxed{
D=P^{2/3},
qquad
H=P^{1/3}.
}
]

After gcd separation, the shifted-product equation leads to residue conditions such as
[
pequiv kar apmod b
]
with generic modulus
[
basymp D=P^{2/3}.
]

## 2. Comparison with current prime-AP levels

Classical Bombieri--Vinogradov reaches average modulus scale
[
P^{1/2-o(1)}.
]

Maynard's well-factorable estimates reach
[
P^{3/5-arepsilon}
]
for suitably well-factorable modulus weights.

Recent triply-well-factorable prime distribution results reach approximately
[
P^{5/8-o(1)}.
]

But
[
oxed{
rac23>rac58>rac35>rac12.
}
]

Hence the generic (P^{2/3}) modulus in the sharp (j=2) dispersion lies polynomially beyond these black-box distribution levels.

## 3. Why factorable-modulus hypotheses cannot be assumed

The common coherent-prime sharp subfamily may take
[
d,d'asymp V
]
to be primes.

Then after gcd separation with (g=1), the moduli
[
a=d,qquad b=d'
]
are themselves prime-scale atomic moduli.

Thus one cannot uniformly invoke:
- smooth-modulus distribution;
- convenient-divisor hypotheses;
- well-factorable modulus weights

without separately proving that the sharp atomic-modulus contribution is negligible.

It is not negligible by support cardinality alone.

## 4. Remaining resource

The problem contains extra averaging absent from a black-box prime-AP theorem:
- both moduli/factors (d,d');
- the shift
[
|h|le H=P^{1/3};
]
- reciprocal residues
[
kar apmod b;
]
- the second prime variable (p').

Thus the correct next object is a bilinear/trilinear dispersion or Kloosterman-fraction form that uses these variables simultaneously.

The (P^{1/3}) shift range must be treated as an analytic resource rather than discarded by a supremum over residue classes.

## 5. Current 2026 Kloosterman context

Recent 2026 work improves bilinear Kloosterman and Kloosterman-fraction bounds, including:
- Dong--Robles--Zeindler on arbitrary-coefficient bilinear Kloosterman fractions;
- Blomer--Pascadi on bilinear Kloosterman sums for general moduli with explicit power savings near the square-root length.

These results make the dispersion route plausible, but the project has not yet derived an exact transformed form with matching parameters. Therefore they are **not** counted as closure theorems.

Permanent guard:
`LATEST_KLOOSTERMAN_RESULT_REQUIRES_EXACT_PARAMETER_MAP`.
